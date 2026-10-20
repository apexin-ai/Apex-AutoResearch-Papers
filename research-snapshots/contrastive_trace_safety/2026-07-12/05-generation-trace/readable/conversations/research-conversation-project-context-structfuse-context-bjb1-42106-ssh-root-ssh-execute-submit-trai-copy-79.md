# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: bjb1-42106 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 116
- **Recorded user turns:** 1
- **Tool calls:** 37
- **Original source:** `logs/chats/exported-trajectories/account-1/03270674-780b-45a5-9dcf-f4a6c86d5bde.jsonl`
- **Structured JSON:** [`40ca2a8d69de1449ddff.json`](../../sessions/40/40ca2a8d69de1449ddff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:02:53.002Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:02:53.002Z",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: bjb1-42106\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：修复 Claim 2 过强措辞（6 处必须修复）\n\n根据 `artifacts/paper_drafts/claim2_wording_review.md` 的审查结果，修复 paper_framing.md 和已有论文草稿中 Claim 2（dataflow-aware filtering）的过强措辞。\n\n### 先读取审查报告\n用 Read 工具读取：\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/claim2_wording_review.md`\n\n### 然后读取需要修改的文件\n用 read_project_file 读取：\n- `paper_framing.md`\n\n用 Read 工具读取 artifacts/paper_drafts/ 下的所有 .md 文件（逐一读取）：\n- `artifacts/paper_drafts/introduction_v2.md`\n- `artifacts/paper_drafts/method_v1.md`（如果存在）\n- `artifacts/paper_drafts/experiment_setup_v1.md`（如果存在）\n- `artifacts/paper_drafts/experiments_v1.md`（如果存在）\n- `artifacts/paper_drafts/discussion_v2.md`（如果存在）\n- `artifacts/paper_drafts/related_work_v1.md`（如果存在）\n\n路径前缀：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/`\n\n### 修复原则\n\n1. **Claim 2 必须标注为 \"exploratory observation\"**，所有出现的地方一致\n2. 替换过强动词：\n   - \"reveals\" → \"suggests\"\n   - \"explains\" → \"may explain\" / \"is consistent with\"\n   - \"predicts\" → \"motivates the hypothesis that\"\n   - \"shows that...depends on\" → \"our preliminary results suggest that...may depend on\"\n   - \"Predictor\" (标题) → \"An Exploratory Analysis\" 或类似\n3. 每处 Claim 2 描述必须包含至少 2/4 hedging 元素：\n   - n=2 encoders 的限制\n   - encoder-dependent 的 caveat\n   - \"exploratory\" / \"preliminary\" 标签\n   - testable prediction 的前向声明\n4. Claim 1 (strong, confirmed) 的措辞不要改——保持区分度\n\n### 输出\n- 修改所有找到的文件\n- 在每个文件末尾加注释 `&lt;!-- Claim 2 wording fix: YYYY-MM-DD -->`\n- 用 save_project_file 更新 paper_framing.md（如果需要改）\n- 其他 .md 文件用 Write 工具写入原路径\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T02:02:53.006Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:02:53.006Z",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

## Round 1

114 recorded events

### User

_source line 3 · 2026-05-15T02:02:53.042Z_

&lt;project_context>
# 项目: structfuse-context

## 运行环境
- 服务器名: bjb1-42106
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/structfuse


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：修复 Claim 2 过强措辞（6 处必须修复）

根据 `artifacts/paper_drafts/claim2_wording_review.md` 的审查结果，修复 paper_framing.md 和已有论文草稿中 Claim 2（dataflow-aware filtering）的过强措辞。

### 先读取审查报告
用 Read 工具读取：
`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/claim2_wording_review.md`

### 然后读取需要修改的文件
用 read_project_file 读取：
- `paper_framing.md`

用 Read 工具读取 artifacts/paper_drafts/ 下的所有 .md 文件（逐一读取）：
- `artifacts/paper_drafts/introduction_v2.md`
- `artifacts/paper_drafts/method_v1.md`（如果存在）
- `artifacts/paper_drafts/experiment_setup_v1.md`（如果存在）
- `artifacts/paper_drafts/experiments_v1.md`（如果存在）
- `artifacts/paper_drafts/discussion_v2.md`（如果存在）
- `artifacts/paper_drafts/related_work_v1.md`（如果存在）

路径前缀：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/`

### 修复原则

1. **Claim 2 必须标注为 "exploratory observation"**，所有出现的地方一致
2. 替换过强动词：
   - "reveals" → "suggests"
   - "explains" → "may explain" / "is consistent with"
   - "predicts" → "motivates the hypothesis that"
   - "shows that...depends on" → "our preliminary results suggest that...may depend on"
   - "Predictor" (标题) → "An Exploratory Analysis" 或类似
3. 每处 Claim 2 描述必须包含至少 2/4 hedging 元素：
   - n=2 encoders 的限制
   - encoder-dependent 的 caveat
   - "exploratory" / "preliminary" 标签
   - testable prediction 的前向声明
4. Claim 1 (strong, confirmed) 的措辞不要改——保持区分度

### 输出
- 修改所有找到的文件
- 在每个文件末尾加注释 `&lt;!-- Claim 2 wording fix: YYYY-MM-DD -->`
- 用 save_project_file 更新 paper_framing.md（如果需要改）
- 其他 .md 文件用 Write 工具写入原路径


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "61950445-d996-49e3-bd14-6f758950ff1e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:02:53.041Z_

```json
{
  "parentUuid": "61950445-d996-49e3-bd14-6f758950ff1e",
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
  "uuid": "5d374541-db83-4e8d-9e75-016ecb54b7a9",
  "timestamp": "2026-05-15T02:02:53.041Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:02:53.041Z_

```json
{
  "parentUuid": "5d374541-db83-4e8d-9e75-016ecb54b7a9",
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
  "uuid": "41c7cbac-070f-4390-90f0-383efb1a04ae",
  "timestamp": "2026-05-15T02:02:53.041Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T02:02:53.041Z_

```json
{
  "parentUuid": "41c7cbac-070f-4390-90f0-383efb1a04ae",
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
  "uuid": "f0069208-f8ba-4b80-8dca-3bfe66a440d1",
  "timestamp": "2026-05-15T02:02:53.041Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-15T02:02:53.041Z_

```json
{
  "parentUuid": "f0069208-f8ba-4b80-8dca-3bfe66a440d1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e2932fc7-080e-4474-9af8-309e7ca9c013",
  "timestamp": "2026-05-15T02:02:53.041Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix Claim 2 overly strong wording in paper drafts",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Assistant

_source line 9 · 2026-05-15T02:02:55.828Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the review report and then all the relevant files to understand what needs to be changed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2932fc7-080e-4474-9af8-309e7ca9c013",
  "isSidechain": false,
  "requestId": "req_011Cb3XpMeGzMrYxwmV7buEP",
  "type": "assistant",
  "uuid": "f91d2565-5909-4f72-b3b7-adf312fd0e99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQs1K18tkdW9RS5ydrXQmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 11447,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11897,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 234,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11897
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

_source line 10 · 2026-05-15T02:02:55.830Z_

读取审查报告和所有相关文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f91d2565-5909-4f72-b3b7-adf312fd0e99",
  "isSidechain": false,
  "requestId": "req_011Cb3XpMeGzMrYxwmV7buEP",
  "type": "assistant",
  "uuid": "6592a038-4923-497b-888d-234e39385c8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQs1K18tkdW9RS5ydrXQmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 11447,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11897,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 234,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11897
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

_source line 11 · 2026-05-15T02:02:56.757Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LHiRfXrqf8YuTGMWrUT6Wc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/claim2_wording_review.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6592a038-4923-497b-888d-234e39385c8c",
  "isSidechain": false,
  "requestId": "req_011Cb3XpMeGzMrYxwmV7buEP",
  "type": "assistant",
  "uuid": "3afb94c1-087b-4d7b-a0d3-7358d6e3f3ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQs1K18tkdW9RS5ydrXQmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 11447,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11897,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 234,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11897
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

_source line 12 · 2026-05-15T02:02:57.702Z_

<details><summary>↩ Tool result · `toolu_016nLSpQt29PUGD6jqZAmW2Y`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1995121a-1ae7-4392-92e1-b9f7c44b2064",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "8cf28279-db60-4ac8-987c-13d2422d5331",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "1995121a-1ae7-4392-92e1-b9f7c44b2064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T02:02:56.778Z_

<details><summary>↩ Tool result · `toolu_01LHiRfXrqf8YuTGMWrUT6Wc`</summary>

```text
1	# Claim 2 Wording Review: "Exploratory Observation" Consistency Audit
2	
3	**Date**: 2026-05-15
4	**Scope**: All paper_framing.md + paper draft .md files
5	**Reference decision**: D035 — Claim 2 降级为 "exploratory observation with testable prediction"
6	
7	---
8	
9	## Summary
10	
11	Claim 2 的 **[Exploratory observation]** 标签仅在 2 处出现（paper_framing.md Claim 定义 + introduction contribution list），但 body text 中有 **11 处** 使用了与 exploratory 不兼容的断言性措辞（"reveals", "explains", "predicts", "shows that"）。Discussion §5.2 是最严重的区域——标题和正文均用预测性语言，暗示 n=2 观察已构成 validated mechanism。
12	
13	Claim 1（strong, confirmed）与 Claim 2（exploratory）的区分在 contribution list 中清晰，但在正文中逐渐模糊，特别是 introduction 最后一段、related work §2.3、discussion §5.2。
14	
15	---
16	
17	## 逐处审查
18	
19	### paper_framing.md
20	
21	| 位置 | 当前措辞 | 强度 | 问题 |
22	|------|----------|------|------|
23	| Core Claims - Claim 2 | "[Exploratory observation]...This is reported as an observation with mechanistic hypothesis, not an established finding." | ✅ 合适 | 明确标记+caveat |
24	| Story Spine - contribution (2) | "observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis" | ⚠️ 偏强 | 缺 "exploratory" 标签；"provide mechanistic analysis" 暗示已完成验证 |
25	| Headline result template | "representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective" | ⚠️ 偏强 | "provides mechanistic explanation" 对 n=2 过于断言 |
26	| Core Insight | "The effectiveness of hard negative mining strategies depends on the encoder's representation geometry." | ❌ 过强 | 无任何 hedge，读为 general claim，无 n=2/exploratory 标记 |
27	| Dual-Pillar Motivation - Secondary | "enabling practitioners to predict which strategy suits their encoder without exhaustive experiments" | ❌ 过强 | 从 n=2 观察直接推出 practitioner guidance，暗示 validated predictive power |
28	| Reviewer Concerns - "Only 2 encoders" | "n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law" | ✅ 合适 | 明确承认 |
29	| Contingency | "Pivot to 2-claim paper...Drop Claim 2 to analysis observation" | ✅ 合适 | 有降级准备 |
30	
31	### introduction_v1.md
32	
33	| 位置 | 当前措辞 | 强度 | 问题 |
34	|------|----------|------|------|
35	| Para 3 (intro body) | "analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry...mediates which strategy is most effective, providing a mechanistic explanation for when and why" | ⚠️ 偏强 | "reveals" + "providing a mechanistic explanation" 无 exploratory hedge；与紧接其后的 Contribution 2 的 hedging 形成矛盾 |
36	| Contribution 2 | "[Exploratory observation] We report that...This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation." | ✅ 合适 | 完整 hedge：标签+caveat+pending 声明 |
37	
38	**矛盾**：Para 3 用 "reveals...provides mechanistic explanation"，Contribution 2 紧接着说 "observation with mechanistic hypothesis"。读者会注意到措辞强度骤降。
39	
40	### experiments_v1.md
41	
42	| 位置 | 当前措辞 | 强度 | 问题 |
43	|------|----------|------|------|
44	| §4.1 Encoders | "This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies." | ⚠️ 偏强 | "mediates" 预设因果，应为 "may mediate" 或 "appears to mediate" |
45	| §4.3 Pilot (ii) | "the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder" | ✅ 合适 | 限定在 pilot 结果描述 |
46	| §4.4 Mechanistic hypothesis title | "Mechanistic hypothesis" | ✅ 合适 | 标题正确标记为 hypothesis |
47	| §4.4 Mechanistic hypothesis body | "When the pretrained space is saturated, the encoder has limited room...Embedding-distance negatives provide a direct optimization target...Dataflow-aware negatives...may not align with the encoder's most informative gradient direction" | ⚠️ 偏强 | 前半段读为已确认的解释（"the encoder has limited room"），后半段用 "may not align" 有 hedge。整体偏 explanatory 而非 hypothesis |
48	| §4.4 Difficulty gradient | "The steeper relative compression for Qwen suggests that..." | ✅ 合适 | "suggests" 恰当 |
49	
50	### discussion_v2.md (最严重)
51	
52	| 位置 | 当前措辞 | 强度 | 问题 |
53	|------|----------|------|------|
54	| §5.2 标题 | "Representation Geometry as a Predictor of Strategy Effectiveness" | ❌ 过强 | "Predictor" 暗示 validated predictive power，n=2 不支持 |
55	| §5.2 首句 | "reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit" | ❌ 过强 | "reveals" + "predicts" 双重断言 |
56	| §5.2 Qwen 解释 | "This explains the +0.8pp R@1 improvement" | ❌ 过强 | "explains" 对 n=2 correlational 观察过于因果 |
57	| §5.2 practical implication | "This interaction...has a practical implication: practitioners can compute pos_sim..." | ⚠️ 偏强 | 从 n=2 直接给出 practitioner recipe |
58	| §5.2 threshold | "though we note this threshold is derived from two encoder observations and should be validated more broadly" | ✅ 合适 | 明确 n=2 caveat |
59	| §5.3 Limitations | "enabling our interaction analysis—generalizing...requires further investigation" | ✅ 合适 | 承认泛化限制 |
60	| §5.4 Future Work | "Our observation that pos_sim predicts strategy effectiveness suggests..." | ⚠️ 偏强 | "predicts" 仍过强，但 "observation...suggests" 结构有 hedge |
61	
62	### related_work_v1.md
63	
64	| 位置 | 当前措辞 | 强度 | 问题 |
65	|------|----------|------|------|
66	| §2.3 末段 | "show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry" | ❌ 过强 | "show that...depends on" 是 confirmed finding 的措辞 |
67	
68	### method_v1.md
69	
70	| 位置 | 当前措辞 | 强度 | 问题 |
71	|------|----------|------|------|
72	| §3.1 | "analyze how their effectiveness interacts with the encoder's pretrained representation geometry" | ✅ 合适 | 描述研究行为，不做 claim |
73	
74	---
75	
76	## 统计
77	
78	| 强度 | 数量 | 位置 |
79	|------|------|------|
80	| ✅ 合适 | 11 | paper_framing (3), intro contrib (1), experiments (3), discussion (2), method (1), figure_design (1) |
81	| ⚠️ 偏强 | 7 | paper_framing (2), intro para3 (1), experiments (2), discussion (2) |
82	| ❌ 过强 | 5 | paper_framing Core Insight (1), paper_framing Dual-Pillar (1), discussion §5.2 (3) |
83	
84	---
85	
86	## 建议修改
87	
88	### 必须修改 (❌ 过强)
89	
90	**1. paper_framing.md - Core Insight**
91	- 现在: "The effectiveness of hard negative mining strategies depends on the encoder's representation geometry."
92	- 建议: "Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation."
93	
94	**2. paper_framing.md - Dual-Pillar Secondary**
95	- 现在: "enabling practitioners to predict which strategy suits their encoder without exhaustive experiments"
96	- 建议: "offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments"
97	
98	**3. discussion_v2.md - §5.2 标题**
99	- 现在: "Representation Geometry as a Predictor of Strategy Effectiveness"
100	- 建议: "Representation Geometry and Strategy Effectiveness: An Exploratory Analysis"
101	
102	**4. discussion_v2.md - §5.2 首句**
103	- 现在: "reveals a practical insight: the pretrained encoder's representation geometry predicts whether..."
104	- 建议: "suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether..."
105	
106	**5. discussion_v2.md - §5.2 "explains"**
107	- 现在: "This explains the +0.8pp R@1 improvement"
108	- 建议: "This is consistent with the +0.8pp R@1 improvement"
109	
110	**6. related_work_v1.md - §2.3**
111	- 现在: "show that the relative effectiveness of mining strategies depends on"
112	- 建议: "observe that the relative effectiveness of mining strategies appears to depend on"
113	
114	### 建议修改 (⚠️ 偏强)
115	
116	**7. paper_framing.md - Story Spine contribution (2)**
117	- 添加 "[exploratory]" 标签: "(2) [exploratory] observe that..."
118	
119	**8. introduction_v1.md - Para 3**
120	- "reveals" → "suggests"
121	- "providing a mechanistic explanation" → "providing a candidate mechanistic explanation (Section 4.4)"
122	
123	**9. experiments_v1.md - §4.1 Encoders**
124	- "mediates" → "may mediate"
125	
126	**10. experiments_v1.md - §4.4 Mechanistic hypothesis body**
127	- 首句添加: "Based on our two-encoder comparison, we hypothesize the following mechanism:"
128	
129	**11. discussion_v2.md - §5.4 Future Work**
130	- "predicts" → "appears to correlate with"
131	
132	---
133	
134	## Claim 1 vs Claim 2 区分度
135	
136	| 文档位置 | 区分清晰度 | 说明 |
137	|----------|-----------|------|
138	| paper_framing Contribution list | ✅ 清晰 | Claim 1 无标签 (strong), Claim 2 有 [Exploratory observation] |
139	| introduction Contribution list | ✅ 清晰 | 同上，且 Claim 2 有 pending 声明 |
140	| introduction body (Para 3) | ❌ 模糊 | "central finding" 引出 Claim 1 后直接 "we observe" 引出 Claim 2，无强度差异标记 |
141	| experiments body | ⚠️ 部分模糊 | pilot 段落区分合理，但 §4.4 mechanistic hypothesis 读为与 §4.3 main results 同等强度 |
142	| discussion | ❌ 模糊 | §5.2 标题和正文与 §5.1 (methodology) 同等断言强度 |
143	| related work | ❌ 模糊 | 两个 claim 在 §2.3 末段同一句中出现，用相同强度的 "show that" |
144	
145	**建议**: Introduction Para 3 中 Claim 2 部分添加括号注: "(an exploratory finding; see Section 4.4)"。Discussion §5.2 开头添加一句: "We present the following analysis as an exploratory observation from two encoders, not a validated mechanism."
146	
147	---
148	
149	## 审稿人攻击角度与预备 Rebuttal
150	
151	### 攻击 1: "n=2 不足以支持任何 interaction claim"
152	**预期措辞**: "The authors claim representation geometry mediates strategy effectiveness, but with only two encoders this is an anecdote, not evidence."
153	**Rebuttal 要点**:
154	- 承认 n=2 是核心限制，这正是我们标记为 exploratory observation 而非 confirmed finding 的原因
155	- 但两个编码器有 meaningful variation: 不同预训练语料、不同 representation geometry (pos_sim 0.986 vs 0.799)、不同预训练目标
156	- 我们提供 testable prediction: pos_sim > 0.98 时 structure-grounded negatives 更有效。这比纯 empirical 结果更有 scientific value
157	- 论文主要贡献是 Claim 1 (embedding mining suffices)，Claim 2 是 bonus insight
158	
159	### 攻击 2: "Mechanistic explanation 是 post-hoc rationalization"
160	**预期措辞**: "The representation geometry analysis is descriptive, not causal. You cannot conclude that saturation causes strategy interaction."
161	**Rebuttal 要点**:
162	- 正确，neg_difficulty analysis 是描述性的 (cosine similarity statistics)，不是实验操控
163	- 我们明确标记为 "mechanistic hypothesis" 而非 "causal proof"
164	- 但描述性证据仍有 explanatory value: margin compression (77% Qwen vs 65% StarCoder) 与 pilot 结果方向一致
165	- 完整因果验证需要控制实验 (e.g., 人工缩放 pos_sim 后测试策略效果)，留待 future work
166	
167	### 攻击 3: "Exploratory observation 不算 contribution"
168	**预期措辞**: "If Claim 2 is merely an observation, the paper has only one real contribution (Claim 1) plus a methodology contribution (Claim 3)."
169	**Rebuttal 要点**:
170	- EMNLP 有 strong tradition of empirical analysis papers where observations + hypotheses are valued (cf. "Do Language Models..." papers)
171	- Claim 2 包含 testable prediction (pos_sim threshold)，不是 vacuous observation
172	- Claim 1 (challenging gradient-based assumption) + Claim 3 (scalable pipeline) + Claim 2 (explanatory observation) 的组合足够
173	- 如果审稿人认为不够，可考虑升级 Claim 3 的呈现方式或添加 BM25 baseline 作为第四个贡献点
174	
175	### 攻击 4: "Paper 内部不一致——abstract/intro 说 exploratory，但 discussion 说 predicts/explains"
176	**预期措辞**: "The paper's own framing is inconsistent — Section 5.2 uses assertive language that contradicts the [Exploratory observation] tag."
177	**Rebuttal 要点**:
178	- 这是本 review 发现的核心问题。如果不修改，审稿人会指出 self-contradiction。
179	- **在提交前必须修复 discussion §5.2 的措辞**，否则审稿人有理由认为作者试图 overclaim。
180	- 一致性是可信度的基础——hedging 要么全做要么不做，不能 contribution list 说 exploratory 但 body text 说 established。
181	
182	### 攻击 5: "Dataflow 两个编码器都不如 embedding，interaction 在哪?"
183	**预期措辞**: "Both encoders show dataflow < embedding. Where is the interaction? The pattern is uniformly negative."
184	**Rebuttal 要点**:
185	- Interaction 不是 "dataflow sometimes wins"，而是 gap magnitude is encoder-dependent (Qwen -1.2pp vs StarCoder -1.0pp, 或 full M2 数据)
186	- neg_difficulty margin 差异 (+17% vs +28%) 与 gap 方向一致
187	- 更根本的 interaction 是 dataflow vs random: Qwen +0.8pp, StarCoder -0.5pp (pilot)——方向相反
188	- 但要诚实: 如果 full M2 显示两个编码器 dataflow vs random 都为负，interaction claim 进一步弱化
189	
190	---
191	
192	## 缺失的 Hedging 元素清单
193	
194	当前 Claim 2 的 hedge 应在**每个出现位置**包含以下至少 2/4 项:
195	
196	| 元素 | paper_framing Claim 2 | intro Contrib 2 | intro Para 3 | exp §4.4 | disc §5.2 | RW §2.3 |
197	|------|:---:|:---:|:---:|:---:|:---:|:---:|
198	| "exploratory" / "observation" 标签 | ✅ | ✅ | ❌ | ⚠️(title only) | ❌ | ❌ |
199	| n=2 limitation | ❌(pending区) | ❌ | ❌ | ❌ | ✅(末尾) | ❌ |
200	| encoder-dependent caveat | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
201	| testable prediction 前向声明 | ❌ | ❌ | ❌ | ❌ | ⚠️(partial) | ❌ |
202	
203	**最薄弱**: related_work §2.3（0/4 元素）、intro Para 3（1/4）、discussion §5.2 body（1/4，仅末尾 caveat）。
204	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3afb94c1-087b-4d7b-a0d3-7358d6e3f3ad",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "89dd3af8-39c9-4917-8ceb-72b37fa8eaa1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/claim2_wording_review.md",
      "content": "# Claim 2 Wording Review: \"Exploratory Observation\" Consistency Audit\n\n**Date**: 2026-05-15\n**Scope**: All paper_framing.md + paper draft .md files\n**Reference decision**: D035 — Claim 2 降级为 \"exploratory observation with testable prediction\"\n\n---\n\n## Summary\n\nClaim 2 的 **[Exploratory observation]** 标签仅在 2 处出现（paper_framing.md Claim 定义 + introduction contribution list），但 body text 中有 **11 处** 使用了与 exploratory 不兼容的断言性措辞（\"reveals\", \"explains\", \"predicts\", \"shows that\"）。Discussion §5.2 是最严重的区域——标题和正文均用预测性语言，暗示 n=2 观察已构成 validated mechanism。\n\nClaim 1（strong, confirmed）与 Claim 2（exploratory）的区分在 contribution list 中清晰，但在正文中逐渐模糊，特别是 introduction 最后一段、related work §2.3、discussion §5.2。\n\n---\n\n## 逐处审查\n\n### paper_framing.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| Core Claims - Claim 2 | \"[Exploratory observation]...This is reported as an observation with mechanistic hypothesis, not an established finding.\" | ✅ 合适 | 明确标记+caveat |\n| Story Spine - contribution (2) | \"observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis\" | ⚠️ 偏强 | 缺 \"exploratory\" 标签；\"provide mechanistic analysis\" 暗示已完成验证 |\n| Headline result template | \"representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective\" | ⚠️ 偏强 | \"provides mechanistic explanation\" 对 n=2 过于断言 |\n| Core Insight | \"The effectiveness of hard negative mining strategies depends on the encoder's representation geometry.\" | ❌ 过强 | 无任何 hedge，读为 general claim，无 n=2/exploratory 标记 |\n| Dual-Pillar Motivation - Secondary | \"enabling practitioners to predict which strategy suits their encoder without exhaustive experiments\" | ❌ 过强 | 从 n=2 观察直接推出 practitioner guidance，暗示 validated predictive power |\n| Reviewer Concerns - \"Only 2 encoders\" | \"n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law\" | ✅ 合适 | 明确承认 |\n| Contingency | \"Pivot to 2-claim paper...Drop Claim 2 to analysis observation\" | ✅ 合适 | 有降级准备 |\n\n### introduction_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| Para 3 (intro body) | \"analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry...mediates which strategy is most effective, providing a mechanistic explanation for when and why\" | ⚠️ 偏强 | \"reveals\" + \"providing a mechanistic explanation\" 无 exploratory hedge；与紧接其后的 Contribution 2 的 hedging 形成矛盾 |\n| Contribution 2 | \"[Exploratory observation] We report that...This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation.\" | ✅ 合适 | 完整 hedge：标签+caveat+pending 声明 |\n\n**矛盾**：Para 3 用 \"reveals...provides mechanistic explanation\"，Contribution 2 紧接着说 \"observation with mechanistic hypothesis\"。读者会注意到措辞强度骤降。\n\n### experiments_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §4.1 Encoders | \"This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\" | ⚠️ 偏强 | \"mediates\" 预设因果，应为 \"may mediate\" 或 \"appears to mediate\" |\n| §4.3 Pilot (ii) | \"the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder\" | ✅ 合适 | 限定在 pilot 结果描述 |\n| §4.4 Mechanistic hypothesis title | \"Mechanistic hypothesis\" | ✅ 合适 | 标题正确标记为 hypothesis |\n| §4.4 Mechanistic hypothesis body | \"When the pretrained space is saturated, the encoder has limited room...Embedding-distance negatives provide a direct optimization target...Dataflow-aware negatives...may not align with the encoder's most informative gradient direction\" | ⚠️ 偏强 | 前半段读为已确认的解释（\"the encoder has limited room\"），后半段用 \"may not align\" 有 hedge。整体偏 explanatory 而非 hypothesis |\n| §4.4 Difficulty gradient | \"The steeper relative compression for Qwen suggests that...\" | ✅ 合适 | \"suggests\" 恰当 |\n\n### discussion_v2.md (最严重)\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §5.2 标题 | \"Representation Geometry as a Predictor of Strategy Effectiveness\" | ❌ 过强 | \"Predictor\" 暗示 validated predictive power，n=2 不支持 |\n| §5.2 首句 | \"reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit\" | ❌ 过强 | \"reveals\" + \"predicts\" 双重断言 |\n| §5.2 Qwen 解释 | \"This explains the +0.8pp R@1 improvement\" | ❌ 过强 | \"explains\" 对 n=2 correlational 观察过于因果 |\n| §5.2 practical implication | \"This interaction...has a practical implication: practitioners can compute pos_sim...\" | ⚠️ 偏强 | 从 n=2 直接给出 practitioner recipe |\n| §5.2 threshold | \"though we note this threshold is derived from two encoder observations and should be validated more broadly\" | ✅ 合适 | 明确 n=2 caveat |\n| §5.3 Limitations | \"enabling our interaction analysis—generalizing...requires further investigation\" | ✅ 合适 | 承认泛化限制 |\n| §5.4 Future Work | \"Our observation that pos_sim predicts strategy effectiveness suggests...\" | ⚠️ 偏强 | \"predicts\" 仍过强，但 \"observation...suggests\" 结构有 hedge |\n\n### related_work_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §2.3 末段 | \"show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry\" | ❌ 过强 | \"show that...depends on\" 是 confirmed finding 的措辞 |\n\n### method_v1.md\n\n| 位置 | 当前措辞 | 强度 | 问题 |\n|------|----------|------|------|\n| §3.1 | \"analyze how their effectiveness interacts with the encoder's pretrained representation geometry\" | ✅ 合适 | 描述研究行为，不做 claim |\n\n---\n\n## 统计\n\n| 强度 | 数量 | 位置 |\n|------|------|------|\n| ✅ 合适 | 11 | paper_framing (3), intro contrib (1), experiments (3), discussion (2), method (1), figure_design (1) |\n| ⚠️ 偏强 | 7 | paper_framing (2), intro para3 (1), experiments (2), discussion (2) |\n| ❌ 过强 | 5 | paper_framing Core Insight (1), paper_framing Dual-Pillar (1), discussion §5.2 (3) |\n\n---\n\n## 建议修改\n\n### 必须修改 (❌ 过强)\n\n**1. paper_framing.md - Core Insight**\n- 现在: \"The effectiveness of hard negative mining strategies depends on the encoder's representation geometry.\"\n- 建议: \"Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation.\"\n\n**2. paper_framing.md - Dual-Pillar Secondary**\n- 现在: \"enabling practitioners to predict which strategy suits their encoder without exhaustive experiments\"\n- 建议: \"offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments\"\n\n**3. discussion_v2.md - §5.2 标题**\n- 现在: \"Representation Geometry as a Predictor of Strategy Effectiveness\"\n- 建议: \"Representation Geometry and Strategy Effectiveness: An Exploratory Analysis\"\n\n**4. discussion_v2.md - §5.2 首句**\n- 现在: \"reveals a practical insight: the pretrained encoder's representation geometry predicts whether...\"\n- 建议: \"suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether...\"\n\n**5. discussion_v2.md - §5.2 \"explains\"**\n- 现在: \"This explains the +0.8pp R@1 improvement\"\n- 建议: \"This is consistent with the +0.8pp R@1 improvement\"\n\n**6. related_work_v1.md - §2.3**\n- 现在: \"show that the relative effectiveness of mining strategies depends on\"\n- 建议: \"observe that the relative effectiveness of mining strategies appears to depend on\"\n\n### 建议修改 (⚠️ 偏强)\n\n**7. paper_framing.md - Story Spine contribution (2)**\n- 添加 \"[exploratory]\" 标签: \"(2) [exploratory] observe that...\"\n\n**8. introduction_v1.md - Para 3**\n- \"reveals\" → \"suggests\"\n- \"providing a mechanistic explanation\" → \"providing a candidate mechanistic explanation (Section 4.4)\"\n\n**9. experiments_v1.md - §4.1 Encoders**\n- \"mediates\" → \"may mediate\"\n\n**10. experiments_v1.md - §4.4 Mechanistic hypothesis body**\n- 首句添加: \"Based on our two-encoder comparison, we hypothesize the following mechanism:\"\n\n**11. discussion_v2.md - §5.4 Future Work**\n- \"predicts\" → \"appears to correlate with\"\n\n---\n\n## Claim 1 vs Claim 2 区分度\n\n| 文档位置 | 区分清晰度 | 说明 |\n|----------|-----------|------|\n| paper_framing Contribution list | ✅ 清晰 | Claim 1 无标签 (strong), Claim 2 有 [Exploratory observation] |\n| introduction Contribution list | ✅ 清晰 | 同上，且 Claim 2 有 pending 声明 |\n| introduction body (Para 3) | ❌ 模糊 | \"central finding\" 引出 Claim 1 后直接 \"we observe\" 引出 Claim 2，无强度差异标记 |\n| experiments body | ⚠️ 部分模糊 | pilot 段落区分合理，但 §4.4 mechanistic hypothesis 读为与 §4.3 main results 同等强度 |\n| discussion | ❌ 模糊 | §5.2 标题和正文与 §5.1 (methodology) 同等断言强度 |\n| related work | ❌ 模糊 | 两个 claim 在 §2.3 末段同一句中出现，用相同强度的 \"show that\" |\n\n**建议**: Introduction Para 3 中 Claim 2 部分添加括号注: \"(an exploratory finding; see Section 4.4)\"。Discussion §5.2 开头添加一句: \"We present the following analysis as an exploratory observation from two encoders, not a validated mechanism.\"\n\n---\n\n## 审稿人攻击角度与预备 Rebuttal\n\n### 攻击 1: \"n=2 不足以支持任何 interaction claim\"\n**预期措辞**: \"The authors claim representation geometry mediates strategy effectiveness, but with only two encoders this is an anecdote, not evidence.\"\n**Rebuttal 要点**:\n- 承认 n=2 是核心限制，这正是我们标记为 exploratory observation 而非 confirmed finding 的原因\n- 但两个编码器有 meaningful variation: 不同预训练语料、不同 representation geometry (pos_sim 0.986 vs 0.799)、不同预训练目标\n- 我们提供 testable prediction: pos_sim > 0.98 时 structure-grounded negatives 更有效。这比纯 empirical 结果更有 scientific value\n- 论文主要贡献是 Claim 1 (embedding mining suffices)，Claim 2 是 bonus insight\n\n### 攻击 2: \"Mechanistic explanation 是 post-hoc rationalization\"\n**预期措辞**: \"The representation geometry analysis is descriptive, not causal. You cannot conclude that saturation causes strategy interaction.\"\n**Rebuttal 要点**:\n- 正确，neg_difficulty analysis 是描述性的 (cosine similarity statistics)，不是实验操控\n- 我们明确标记为 \"mechanistic hypothesis\" 而非 \"causal proof\"\n- 但描述性证据仍有 explanatory value: margin compression (77% Qwen vs 65% StarCoder) 与 pilot 结果方向一致\n- 完整因果验证需要控制实验 (e.g., 人工缩放 pos_sim 后测试策略效果)，留待 future work\n\n### 攻击 3: \"Exploratory observation 不算 contribution\"\n**预期措辞**: \"If Claim 2 is merely an observation, the paper has only one real contribution (Claim 1) plus a methodology contribution (Claim 3).\"\n**Rebuttal 要点**:\n- EMNLP 有 strong tradition of empirical analysis papers where observations + hypotheses are valued (cf. \"Do Language Models...\" papers)\n- Claim 2 包含 testable prediction (pos_sim threshold)，不是 vacuous observation\n- Claim 1 (challenging gradient-based assumption) + Claim 3 (scalable pipeline) + Claim 2 (explanatory observation) 的组合足够\n- 如果审稿人认为不够，可考虑升级 Claim 3 的呈现方式或添加 BM25 baseline 作为第四个贡献点\n\n### 攻击 4: \"Paper 内部不一致——abstract/intro 说 exploratory，但 discussion 说 predicts/explains\"\n**预期措辞**: \"The paper's own framing is inconsistent — Section 5.2 uses assertive language that contradicts the [Exploratory observation] tag.\"\n**Rebuttal 要点**:\n- 这是本 review 发现的核心问题。如果不修改，审稿人会指出 self-contradiction。\n- **在提交前必须修复 discussion §5.2 的措辞**，否则审稿人有理由认为作者试图 overclaim。\n- 一致性是可信度的基础——hedging 要么全做要么不做，不能 contribution list 说 exploratory 但 body text 说 established。\n\n### 攻击 5: \"Dataflow 两个编码器都不如 embedding，interaction 在哪?\"\n**预期措辞**: \"Both encoders show dataflow < embedding. Where is the interaction? The pattern is uniformly negative.\"\n**Rebuttal 要点**:\n- Interaction 不是 \"dataflow sometimes wins\"，而是 gap magnitude is encoder-dependent (Qwen -1.2pp vs StarCoder -1.0pp, 或 full M2 数据)\n- neg_difficulty margin 差异 (+17% vs +28%) 与 gap 方向一致\n- 更根本的 interaction 是 dataflow vs random: Qwen +0.8pp, StarCoder -0.5pp (pilot)——方向相反\n- 但要诚实: 如果 full M2 显示两个编码器 dataflow vs random 都为负，interaction claim 进一步弱化\n\n---\n\n## 缺失的 Hedging 元素清单\n\n当前 Claim 2 的 hedge 应在**每个出现位置**包含以下至少 2/4 项:\n\n| 元素 | paper_framing Claim 2 | intro Contrib 2 | intro Para 3 | exp §4.4 | disc §5.2 | RW §2.3 |\n|------|:---:|:---:|:---:|:---:|:---:|:---:|\n| \"exploratory\" / \"observation\" 标签 | ✅ | ✅ | ❌ | ⚠️(title only) | ❌ | ❌ |\n| n=2 limitation | ❌(pending区) | ❌ | ❌ | ❌ | ✅(末尾) | ❌ |\n| encoder-dependent caveat | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |\n| testable prediction 前向声明 | ❌ | ❌ | ❌ | ❌ | ⚠️(partial) | ❌ |\n\n**最薄弱**: related_work §2.3（0/4 元素）、intro Para 3（1/4）、discussion §5.2 body（1/4，仅末尾 caveat）。\n",
      "numLines": 204,
      "startLine": 1,
      "totalLines": 204
    }
  },
  "sourceToolAssistantUUID": "3afb94c1-087b-4d7b-a0d3-7358d6e3f3ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T02:02:57.697Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016nLSpQt29PUGD6jqZAmW2Y`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89dd3af8-39c9-4917-8ceb-72b37fa8eaa1",
  "isSidechain": false,
  "requestId": "req_011Cb3XpMeGzMrYxwmV7buEP",
  "type": "assistant",
  "uuid": "1995121a-1ae7-4392-92e1-b9f7c44b2064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQs1K18tkdW9RS5ydrXQmc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11897,
      "cache_read_input_tokens": 11447,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11897,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 234,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11897
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

_source line 15_

```json
{
  "type": "last-prompt",
  "leafUuid": "8cf28279-db60-4ac8-987c-13d2422d5331",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix Claim 2 overly strong wording in paper drafts",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Assistant

_source line 17 · 2026-05-15T02:03:00.714Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all the files that need to be modified. Let me read them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cf28279-db60-4ac8-987c-13d2422d5331",
  "isSidechain": false,
  "requestId": "req_011Cb3XpiSfw1WTNiaUgdYPK",
  "type": "assistant",
  "uuid": "7d9189f7-4331-4577-8ffc-a902965cb80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzqoXRZmPkRjY6mejKEmgM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 23344,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 605,
          "cache_read_input_tokens": 23344,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 18 · 2026-05-15T02:03:01.665Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QANFMhUTDEWp3xQT6qMMhQ`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d9189f7-4331-4577-8ffc-a902965cb80c",
  "isSidechain": false,
  "requestId": "req_011Cb3XpiSfw1WTNiaUgdYPK",
  "type": "assistant",
  "uuid": "9bac38d9-b272-4625-9601-28b1ae942c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzqoXRZmPkRjY6mejKEmgM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 23344,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 605,
          "cache_read_input_tokens": 23344,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 19 · 2026-05-15T02:03:01.685Z_

<details><summary>↩ Tool result · `toolu_01QANFMhUTDEWp3xQT6qMMhQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"challenging gradient-based assumption\\\" narrative needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 12022, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bac38d9-b272-4625-9601-28b1ae942c34",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "e38922aa-010a-4112-bfc2-ab441bd3c988",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — StructFuse\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3)\\\\n\\\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\\\\\"slow and ineffective\\\\\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\\\n\\\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\\\n\\\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\\\n\\\\n- **Existing approaches & gaps**:\\\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\\\n\\\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\\\n\\\\n- **Headline result template**: \\\\\\\"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\\\n\\\\n## Dual-Pillar Motivation\\\\n\\\\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\\\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\\\n\\\\n## Formal Definition\\\\n\\\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\\\n\\\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\\\n\\\\n## Title Options\\\\n\\\\n- Primary: \\\\\\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\\\\\"\\\\n- Alternative: \\\\\\\"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\\\\\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\\\n- Backup: \\\\\\\"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\\\\\\\"\\\\n\\\\n## Venue Fit\\\\n\\\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\\\\\"Do Language Models...\\\\\\\" papers). Contribution is understanding, not just a new method.\\\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\\\n3. **Against \\\\\\\"incremental\\\\\\\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response | Evidence |\\\\n|---------|----------|----------|\\\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\\\n| \\\\\\\"Complementary signal\\\\\\\" overstatement | Temper: \\\\\\\"conditionally beneficial\\\\\\\" not \\\\\\\"always complementary\\\\\\\" | Writing discipline |\\\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\\\n\\\\n## Evidence Status\\\\n\\\\n### Confirmed findings (basis for claims):\\\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\\\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\\\n\\\\n### In progress:\\\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\\\n\\\\n### Planned (priority order):\\\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\\\n- plan_014: Temperature ablation (Dream reviewer concern)\\\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\\\n- plan_015: Dynamic mining baseline\\\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\\\n- plan_007/008/009: Additional ablations\\\\n\\\\n## Contingency (if full M2 results weaken claims)\\\\n\\\\n### All 18 runs confirm pilot pattern: Best case\\\\n- Full statistical power, paper as framed above\\\\n- Target: EMNLP Main\\\\n\\\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\\\n- Drop Claim 2 to analysis observation\\\\n- Paper becomes: \\\\\\\"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\\\\\"\\\\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\\\\n\\\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\\\\\"challenging gradient-based assumption\\\\\\\" narrative needs adjustment\\\\n- Pivot: \\\\\\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\\\\\\\"\\\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\\\\n- Claim 1 core preserved: \\\\\\\"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\\\\\\\"\\\\n- Impact: BM25 result determines narrative nuance, not core contribution\\\\n\\\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\\\n- If confirmed: negative result paper — \\\\\\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\\\\\"\\\\n- Discuss with user before committing direction\\\\n\\\\n## Deprecated Claims (with reason)\\\\n\\\\n- ~~\\\\\\\"Embedding-distance hard negatives actively harm code retrieval\\\\\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\\\n\\\", \\\"total_chars\\\": 12022, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"challenging gradient-based assumption\\\" narrative needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 12022, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "9bac38d9-b272-4625-9601-28b1ae942c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T02:03:06.206Z_

<details><summary>↩ Tool result · `toolu_01M71L1jczw579J8qucEttua`</summary>

```text
1	# §4 Experimental Setup
2	
3	## §4.1 Dataset
4	
5	We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit. We expand each task by treating every gold file as a separate training instance, yielding 44,173 instances total [Source: m1_extraction registry, data_count after filtering 6,696 clone/checkout failures from the original 50,869].
6	
7	We run the StructFuse extraction pipeline (§3.2) on all instances. After filtering for extraction errors, we retain 14,288 usable instances across 123 repositories. Of these, approximately 34% possess CodeQL structural connectivity data (15,133 via CodeQL + 764 via beniget fallback); the remaining 66% lack structural data due to transient filesystem failures during batch extraction. For these instances, the dataflow-aware strategy falls back to embedding-distance mining (§3.3) [Source: m1_extraction registry].
8	
9	For each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:
10	
11	| Seed | Train | Val | Total |
12	|------|-------|-----|-------|
13	| 42 | 11,308 | 2,980 | 14,288 |
14	| 43 | 11,236 | 3,052 | 14,288 |
15	| 44 | 11,264 | 3,024 | 14,288 |
16	
17	[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]
18	
19	## §4.2 Models
20	
21	We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.
22	
23	**Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.
24	
25	**StarCoder2-3B** \cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.
26	
27	The two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.
28	
29	## §4.3 Training Configuration
30	
31	All hyperparameters are shared across strategies and encoders unless otherwise noted. The configuration was fixed before the full multi-seed experiment based on pilot runs.
32	
33	| Parameter | Value |
34	|-----------|-------|
35	| Optimizer | AdamW |
36	| Learning rate | $2 \times 10^{-5}$ |
37	| LR schedule | Cosine annealing with linear warmup |
38	| Warmup ratio | 0.1 |
39	| Weight decay | 0.01 |
40	| Gradient clipping | Max norm 1.0 |
41	| Batch size | 8 |
42	| Negatives per query ($K$) | 7 |
43	| Max sequence length | 2,048 tokens |
44	| Temperature ($\tau$, initial) | 0.07 (learnable) |
45	| LoRA rank ($r$) | 16 |
46	| LoRA scaling ($\alpha$) | 32 |
47	| LoRA dropout | 0.05 |
48	| LoRA target modules | $W_q$, $W_v$ (all attention layers) |
49	| Projection dimension | 256 |
50	| Gradient checkpointing | Enabled |
51	| Evaluation interval | Every 500 steps |
52	
53	[Source: m2_full_qwen registry spec and notes]
54	
55	**Epoch schedule.** Seed 42 trains for 3 epochs without early stopping to provide a complete overfitting curve. Seeds 43 and 44 train for 2 epochs with early stopping (patience = 2 evaluation cycles based on validation loss). This asymmetric design was adopted after observing consistent overfitting past epoch 1 in the seed 42 exploratory run [Source: D026 decision].
56	
57	**Checkpoint selection.** We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Primary results use $\theta^*_{\text{R@1}}$; both are reported for metric-loss disagreement analysis [Source: D036 decision].
58	
59	**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].
60	
61	**Hardware.** All experiments are conducted on a single node with 2× NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs (cuda:0 and cuda:1) in parallel. Each individual run (single strategy, single seed, single encoder) requires approximately 5–7 hours. The core 18-run matrix requires approximately 120 GPU-hours [Source: m2_full_qwen and m2_full_starcoder registries].
62	
63	## §4.4 Evaluation Metrics
64	
65	**Retrieval metrics.** We report Recall@$k$ for $k \in \{1, 5, 10\}$, computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per evaluation query). Recall@1 serves as the primary metric for checkpoint selection and strategy comparison. We also report validation loss (InfoNCE) as a secondary training diagnostic.
66	
67	**Statistical reporting.** All comparisons report:
68	
69	- **Aggregate**: mean ± standard deviation across 3 seeds per condition.
70	- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).
71	- **Effect size**: Cohen's $d$ for key comparisons, providing a standardized measure of practical significance independent of sample size.
72	- **Per-seed consistency**: individual seed results reported alongside aggregates to assess stability. [TBD: exact CI and Cohen's d values pending M2 completion]
73	
74	**Checkpoint criterion.** Primary results use the $\theta^*_{\text{R@1}}$ checkpoint. We additionally report $\theta^*_{\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47ebc6f4-9c40-4a2d-ba30-f50a892809e5",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "0c539570-1206-4ea8-a5cb-ef1cb7bd0811",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
      "content": "# §4 Experimental Setup\n\n## §4.1 Dataset\n\nWe construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit. We expand each task by treating every gold file as a separate training instance, yielding 44,173 instances total [Source: m1_extraction registry, data_count after filtering 6,696 clone/checkout failures from the original 50,869].\n\nWe run the StructFuse extraction pipeline (§3.2) on all instances. After filtering for extraction errors, we retain 14,288 usable instances across 123 repositories. Of these, approximately 34% possess CodeQL structural connectivity data (15,133 via CodeQL + 764 via beniget fallback); the remaining 66% lack structural data due to transient filesystem failures during batch extraction. For these instances, the dataflow-aware strategy falls back to embedding-distance mining (§3.3) [Source: m1_extraction registry].\n\nFor each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:\n\n| Seed | Train | Val | Total |\n|------|-------|-----|-------|\n| 42 | 11,308 | 2,980 | 14,288 |\n| 43 | 11,236 | 3,052 | 14,288 |\n| 44 | 11,264 | 3,024 | 14,288 |\n\n[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]\n\n## §4.2 Models\n\nWe select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.\n\n**Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.\n\n**StarCoder2-3B** \\cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.\n\nThe two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.\n\n## §4.3 Training Configuration\n\nAll hyperparameters are shared across strategies and encoders unless otherwise noted. The configuration was fixed before the full multi-seed experiment based on pilot runs.\n\n| Parameter | Value |\n|-----------|-------|\n| Optimizer | AdamW |\n| Learning rate | $2 \\times 10^{-5}$ |\n| LR schedule | Cosine annealing with linear warmup |\n| Warmup ratio | 0.1 |\n| Weight decay | 0.01 |\n| Gradient clipping | Max norm 1.0 |\n| Batch size | 8 |\n| Negatives per query ($K$) | 7 |\n| Max sequence length | 2,048 tokens |\n| Temperature ($\\tau$, initial) | 0.07 (learnable) |\n| LoRA rank ($r$) | 16 |\n| LoRA scaling ($\\alpha$) | 32 |\n| LoRA dropout | 0.05 |\n| LoRA target modules | $W_q$, $W_v$ (all attention layers) |\n| Projection dimension | 256 |\n| Gradient checkpointing | Enabled |\n| Evaluation interval | Every 500 steps |\n\n[Source: m2_full_qwen registry spec and notes]\n\n**Epoch schedule.** Seed 42 trains for 3 epochs without early stopping to provide a complete overfitting curve. Seeds 43 and 44 train for 2 epochs with early stopping (patience = 2 evaluation cycles based on validation loss). This asymmetric design was adopted after observing consistent overfitting past epoch 1 in the seed 42 exploratory run [Source: D026 decision].\n\n**Checkpoint selection.** We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Primary results use $\\theta^*_{\\text{R@1}}$; both are reported for metric-loss disagreement analysis [Source: D036 decision].\n\n**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].\n\n**Hardware.** All experiments are conducted on a single node with 2× NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs (cuda:0 and cuda:1) in parallel. Each individual run (single strategy, single seed, single encoder) requires approximately 5–7 hours. The core 18-run matrix requires approximately 120 GPU-hours [Source: m2_full_qwen and m2_full_starcoder registries].\n\n## §4.4 Evaluation Metrics\n\n**Retrieval metrics.** We report Recall@$k$ for $k \\in \\{1, 5, 10\\}$, computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per evaluation query). Recall@1 serves as the primary metric for checkpoint selection and strategy comparison. We also report validation loss (InfoNCE) as a secondary training diagnostic.\n\n**Statistical reporting.** All comparisons report:\n\n- **Aggregate**: mean ± standard deviation across 3 seeds per condition.\n- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).\n- **Effect size**: Cohen's $d$ for key comparisons, providing a standardized measure of practical significance independent of sample size.\n- **Per-seed consistency**: individual seed results reported alongside aggregates to assess stability. [TBD: exact CI and Cohen's d values pending M2 completion]\n\n**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].\n",
      "numLines": 75,
      "startLine": 1,
      "totalLines": 75
    }
  },
  "sourceToolAssistantUUID": "47ebc6f4-9c40-4a2d-ba30-f50a892809e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T02:03:03.081Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UTGnWeJPbJYmvwf3d8u4aR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e38922aa-010a-4112-bfc2-ab441bd3c988",
  "isSidechain": false,
  "requestId": "req_011Cb3XpiSfw1WTNiaUgdYPK",
  "type": "assistant",
  "uuid": "60d3d899-b81a-4f1c-80de-af2259157200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzqoXRZmPkRjY6mejKEmgM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 23344,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 605,
          "cache_read_input_tokens": 23344,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 22 · 2026-05-15T02:03:03.087Z_

<details><summary>↩ Tool result · `toolu_01UTGnWeJPbJYmvwf3d8u4aR`</summary>

```text
1	# 1. Introduction
2	
3	Code retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \cite{liu2024repobench}, fault localization \cite{chen2025locagent}, and automated program repair \cite{jimenez2024swebench}.
4	Contrastive learning has become the dominant paradigm for training dense code retrievers \cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \cite{chen2020simclr,xiong2021ance}.
5	Despite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.
6	As retrieval scales to repository-level settings with hundreds of candidate files \cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.
7	
8	Existing negative selection approaches span a broad spectrum but leave a critical gap.
9	Random negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \cite{karpukhin2020dpr}.
10	Embedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.
11	CoCoHaNeRe \cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.
12	Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.
13	Notably, files that are close in embedding space may be structurally connected through shared data-flow paths \cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.
14	
15	We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.
16	Using CodeQL \cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.
17	We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.
18	All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.
19	
20	Our experiments on CodeSearchNet \cite{husain2019codesearchnet} yield three principal findings.
21	First, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \cite{fan2025cocohanere}.
22	Second, as an \textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\ ${\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).
23	Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\% timeout rate and [TBD]\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.
24	
25	Our contributions are as follows:
26	\begin{enumerate}
27	\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.
28	\item \textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.
29	\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.
30	\end{enumerate}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60d3d899-b81a-4f1c-80de-af2259157200",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "da46cfff-4b83-4ed2-9506-d8101e9222ea",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
      "content": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "60d3d899-b81a-4f1c-80de-af2259157200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T02:03:04.030Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ThXxGWptyRiCWTpbWsTrLK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da46cfff-4b83-4ed2-9506-d8101e9222ea",
  "isSidechain": false,
  "requestId": "req_011Cb3XpiSfw1WTNiaUgdYPK",
  "type": "assistant",
  "uuid": "8a337e1e-75d5-45d1-ad8e-e85bad188eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzqoXRZmPkRjY6mejKEmgM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 23344,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 605,
          "cache_read_input_tokens": 23344,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 24 · 2026-05-15T02:03:04.040Z_

<details><summary>↩ Tool result · `toolu_01ThXxGWptyRiCWTpbWsTrLK`</summary>

```text
1	# 5. Discussion
2	
3	## 5.1 Relationship to Inference-Time Graph Methods
4	
5	A growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.
6	CodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.
7	
8	Table 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:
9	
10	**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.
11	
12	**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a sanitizer that transforms data between a source and sink across call boundaries. This deeper semantic signal generates harder, more informative negatives than structural proximity alone.
13	
14	**Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.
15	
16	## 5.2 Representation Geometry as a Predictor of Strategy Effectiveness
17	
18	Our negative difficulty analysis (Section 4.4) reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit beyond embedding-distance mining.
19	
20	When the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This explains the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).
21	
22	When the representation space has healthy separation—as observed for StarCoder2-3B (pos\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.
23	
24	This interaction between representation geometry and strategy effectiveness has a practical implication: practitioners can compute pos\_sim on a held-out sample with their pretrained encoder (a single forward pass, requiring no training) to predict whether structure-grounded negatives are worth the extraction cost. We observe that pos\_sim > 0.98 serves as an approximate threshold above which structural negatives provide conditional benefit, though we note this threshold is derived from two encoder observations and should be validated more broadly.
25	
26	## 5.3 Limitations
27	
28	We identify several limitations of the current study that contextualize our findings:
29	
30	**Encoder scope.** Our experiments use two decoder-only 3B-parameter encoders (Qwen2.5-Coder-3B and StarCoder2-3B). While these models differ meaningfully in pretraining corpus and representation geometry—enabling our interaction analysis—generalizing to encoder-only architectures (e.g., CodeBERT), larger scales, or non-code domains requires further investigation.
31	
32	**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.
33	
34	**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).
35	
36	**Static mining.** Our negative mining is performed once before training and remains fixed throughout. Dynamic re-mining—where negatives are refreshed each epoch using the current encoder's embeddings—could yield progressively harder negatives as the model improves. We do not evaluate this variant in the current work and acknowledge the static-vs.-dynamic mining confound as a limitation. We plan to address this in future revisions.
37	
38	**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.
39	
40	## 5.4 Future Work
41	
42	We identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:
43	
44	**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.
45	
46	**Representation-guided strategy selection.** Our observation that pos\_sim predicts strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.
47	
48	**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a337e1e-75d5-45d1-ad8e-e85bad188eb8",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "4d8aa8a8-0c33-44d4-bef1-0db9c68ce2d7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
      "content": "# 5. Discussion\n\n## 5.1 Relationship to Inference-Time Graph Methods\n\nA growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.\nCodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.\n\nTable 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:\n\n**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.\n\n**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a sanitizer that transforms data between a source and sink across call boundaries. This deeper semantic signal generates harder, more informative negatives than structural proximity alone.\n\n**Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.\n\n## 5.2 Representation Geometry as a Predictor of Strategy Effectiveness\n\nOur negative difficulty analysis (Section 4.4) reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit beyond embedding-distance mining.\n\nWhen the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This explains the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).\n\nWhen the representation space has healthy separation—as observed for StarCoder2-3B (pos\\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.\n\nThis interaction between representation geometry and strategy effectiveness has a practical implication: practitioners can compute pos\\_sim on a held-out sample with their pretrained encoder (a single forward pass, requiring no training) to predict whether structure-grounded negatives are worth the extraction cost. We observe that pos\\_sim > 0.98 serves as an approximate threshold above which structural negatives provide conditional benefit, though we note this threshold is derived from two encoder observations and should be validated more broadly.\n\n## 5.3 Limitations\n\nWe identify several limitations of the current study that contextualize our findings:\n\n**Encoder scope.** Our experiments use two decoder-only 3B-parameter encoders (Qwen2.5-Coder-3B and StarCoder2-3B). While these models differ meaningfully in pretraining corpus and representation geometry—enabling our interaction analysis—generalizing to encoder-only architectures (e.g., CodeBERT), larger scales, or non-code domains requires further investigation.\n\n**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.\n\n**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).\n\n**Static mining.** Our negative mining is performed once before training and remains fixed throughout. Dynamic re-mining—where negatives are refreshed each epoch using the current encoder's embeddings—could yield progressively harder negatives as the model improves. We do not evaluate this variant in the current work and acknowledge the static-vs.-dynamic mining confound as a limitation. We plan to address this in future revisions.\n\n**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.\n\n## 5.4 Future Work\n\nWe identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:\n\n**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.\n\n**Representation-guided strategy selection.** Our observation that pos\\_sim predicts strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.\n\n**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "8a337e1e-75d5-45d1-ad8e-e85bad188eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T02:03:04.503Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JCSPDzQWFhoMLdCCSjN8os`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d8aa8a8-0c33-44d4-bef1-0db9c68ce2d7",
  "isSidechain": false,
  "requestId": "req_011Cb3XpiSfw1WTNiaUgdYPK",
  "type": "assistant",
  "uuid": "f441ed10-0662-40b3-a563-37af915f0351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzqoXRZmPkRjY6mejKEmgM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 23344,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 605,
          "cache_read_input_tokens": 23344,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 26 · 2026-05-15T02:03:04.508Z_

<details><summary>↩ Tool result · `toolu_01JCSPDzQWFhoMLdCCSjN8os`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Code Retrieval Methods
4	
5	Repo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.
6	
7	A parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization—though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.
8	
9	Critically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.
10	
11	## 2.2 Contrastive Learning for Code
12	
13	Building on the success of Sentence-BERT \cite{reimers2019sentencebert} in learning dense sentence representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across eleven code search benchmarks. \citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations.
14	
15	Complementary efforts have explored encoding structural information directly into code representations. code2vec \cite{alon2019code2vec} demonstrates that AST path-based representations capture meaningful program properties at scale. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pre-training, showing that data-flow information improves downstream code understanding tasks. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning—a fundamentally different application of structural information that operates at the repository level rather than the function level.
16	
17	Despite the progress in contrastive code representation learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.
18	
19	## 2.3 Hard Negative Mining
20	
21	Hard negative mining—selecting negative examples that are challenging for the current model—is well established for improving contrastive learning. In visual representation learning, SimCLR \cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. Curriculum-based approaches such as CL-DRD \cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.
22	
23	In the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining—the strategy of selecting hard negatives by nearest-neighbor lookup in the encoder's frozen embedding space—in structural code retrieval settings.
24	
25	Our work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f441ed10-0662-40b3-a563-37af915f0351",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "b1a9b6c4-1b46-40e1-b7eb-433b7ebc07eb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Code Retrieval Methods\n\nRepo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \\cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \\cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \\cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \\cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.\n\nA parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \\cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \\cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \\cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \\cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \\cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \\cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization—though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.\n\nCritically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.\n\n## 2.2 Contrastive Learning for Code\n\nBuilding on the success of Sentence-BERT \\cite{reimers2019sentencebert} in learning dense sentence representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \\cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across eleven code search benchmarks. \\citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations.\n\nComplementary efforts have explored encoding structural information directly into code representations. code2vec \\cite{alon2019code2vec} demonstrates that AST path-based representations capture meaningful program properties at scale. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pre-training, showing that data-flow information improves downstream code understanding tasks. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning—a fundamentally different application of structural information that operates at the repository level rather than the function level.\n\nDespite the progress in contrastive code representation learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \\cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.\n\n## 2.3 Hard Negative Mining\n\nHard negative mining—selecting negative examples that are challenging for the current model—is well established for improving contrastive learning. In visual representation learning, SimCLR \\cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \\cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \\cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. Curriculum-based approaches such as CL-DRD \\cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.\n\nIn the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \\cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining—the strategy of selecting hard negatives by nearest-neighbor lookup in the encoder's frozen embedding space—in structural code retrieval settings.\n\nOur work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  },
  "sourceToolAssistantUUID": "f441ed10-0662-40b3-a563-37af915f0351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T02:03:04.973Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Sd2SFUERvRCwRSeEADJFV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1a9b6c4-1b46-40e1-b7eb-433b7ebc07eb",
  "isSidechain": false,
  "requestId": "req_011Cb3XpiSfw1WTNiaUgdYPK",
  "type": "assistant",
  "uuid": "f5ffedcc-f747-45a1-b3bd-65d905a1844e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzqoXRZmPkRjY6mejKEmgM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 23344,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 605,
          "cache_read_input_tokens": 23344,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 28 · 2026-05-15T02:03:04.983Z_

<details><summary>↩ Tool result · `toolu_016Sd2SFUERvRCwRSeEADJFV`</summary>

```text
1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \placeholder{34.3%} [pending recalc]. The remaining \placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
6	
7	For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.
8	
9	**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\theta^*_{\text{R@1}}$), as discussed in §3.3.
10	
11	**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}.
12	
13	## §4.2 Implementation Details
14	
15	**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.
16	
17	**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
18	
19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
21	**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.
22	
23	**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.
24	
25	## §4.3 Results
26	
27	### Main Results
28	
29	Table 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\pm$ standard deviation over three seeds.
30	
31	**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.
32	
33	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
34	|---|---|---|---|---|---|---|
35	| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |
36	| BM25 (no training) | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} |
37	| Random | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
38	| BM25-mined | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
39	| Embedding-distance | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
40	| Dataflow-aware | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
41	
42	**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\placeholder{+X.X}pp and \placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.
43	
44	### Pilot Validation
45	
46	Prior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.
47	
48	**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.
49	
50	| Strategy | Qwen R@1 | StarCoder R@1 |
51	|---|---|---|
52	| Random | 0.5357 | 0.4922 |
53	| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |
54	| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |
55	
56	The pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.
57	
58	### Ablations
59	
60	**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\in \{50, 100, 200, 500\}$.
61	
62	**Table 3: R@1 by pool size.**
63	
64	| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\Delta$ | SC Emb. | SC Rand. | SC $\Delta$ |
65	|---|---|---|---|---|---|---|
66	| 50 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
67	| 100 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
68	| 200 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
69	| 500 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
70	
71	**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.
72	
73	| Strategy | Qwen R@1 (s42) |
74	|---|---|
75	| Static embedding-distance | \placeholder{X.XX} |
76	| Dynamic (epoch re-mining) | \placeholder{X.XX} |
77	
78	### Downstream Evaluation
79	
80	**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).
81	
82	| Retriever | Resolve Rate |
83	|---|---|
84	| BM25 | \placeholder{X.X%} |
85	| Random-trained | \placeholder{X.X%} |
86	| Embedding-trained (Qwen) | \placeholder{X.X%} |
87	
88	## §4.4 Analysis
89	
90	### Representation Geometry and Negative Difficulty
91	
92	A central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.
93	
94	**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\_sim − neg\_sim.
95	
96	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
97	|---|---|---|---|---|---|---|
98	| | pos\_sim | neg\_sim | margin | pos\_sim | neg\_sim | margin |
99	| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |
100	| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |
101	| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |
102	
103	Several patterns emerge from Table 4:
104	
105	**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\times$ larger margins across all strategies, indicating a more separable pretrained space.
106	
107	**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.
108	
109	**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.
110	
111	### Stratified Analysis
112	
113	We stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.
114	
115	**Table 5: R@1 stratified by structural data availability.**
116	
117	| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\Delta$ | SC (Emb.) | SC (DF) | $\Delta$ |
118	|---|---|---|---|---|---|---|---|
119	| Rich dataflow ($\geq$5 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
120	| Sparse dataflow (1–4 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
121	| No structural data (fallback) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
122	
123	Confound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.
124	
125	### CodeQL Scalability
126	
127	We report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).
128	
129	&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->
130	**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.
131	
132	| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |
133	|---|---|---|---|---|---|
134	| Small (<50 inst.) | 18 | 500 | 0% | \placeholder{81.0%} [pending recalc] | 0.0% |
135	| Medium (50–200) | 36 | 4,096 | 0% | \placeholder{47.2%} [pending recalc] | 50.0% |
136	| Large (200–500) | 40 | 13,628 | 0% | \placeholder{34.3%} [pending recalc] | 85.7% |
137	| XLarge (500+) | 29 | 25,949 | 0% | \placeholder{31.4%} [pending recalc] | 96.0% |
138	| **Total** | **123** | **44,173** | **0%** | **\placeholder{34.3%} [pending recalc]** | — |
139	
140	The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5ffedcc-f747-45a1-b3bd-65d905a1844e",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "8586b2ab-7e9d-4f7a-949c-93032bcabe2b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
      "content": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \\placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \\placeholder{34.3%} [pending recalc]. The remaining \\placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to filter structurally reachable files before selecting by embedding distance (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\n\nThe pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->\n**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 inst.) | 18 | 500 | 0% | \\placeholder{81.0%} [pending recalc] | 0.0% |\n| Medium (50–200) | 36 | 4,096 | 0% | \\placeholder{47.2%} [pending recalc] | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | \\placeholder{34.3%} [pending recalc] | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | \\placeholder{31.4%} [pending recalc] | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **\\placeholder{34.3%} [pending recalc]** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n",
      "numLines": 141,
      "startLine": 1,
      "totalLines": 141
    }
  },
  "sourceToolAssistantUUID": "f5ffedcc-f747-45a1-b3bd-65d905a1844e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T02:03:05.917Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FTfU4ETctftzdg6NTtif3d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8586b2ab-7e9d-4f7a-949c-93032bcabe2b",
  "isSidechain": false,
  "requestId": "req_011Cb3XpiSfw1WTNiaUgdYPK",
  "type": "assistant",
  "uuid": "f079a865-c1aa-4bac-b4fb-3a227f43490c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzqoXRZmPkRjY6mejKEmgM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 23344,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 605,
          "cache_read_input_tokens": 23344,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 30 · 2026-05-15T02:03:05.922Z_

<details><summary>↩ Tool result · `toolu_01FTfU4ETctftzdg6NTtif3d`</summary>

```text
1	# §3 Method
2	
3	## §3.1 Problem Formulation
4	
5	We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.
6	
7	We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:
8	
9	$$\text{sim}(E_\theta(q), E_\theta(f^+)) \gg \text{sim}(E_\theta(q), E_\theta(f^-))$$
10	
11	where $\text{sim}(\cdot, \cdot)$ denotes cosine similarity.
12	
13	The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.
14	
15	## §3.2 Structural Information Extraction
16	
17	### CodeQL Bounded Data-Flow Analysis
18	
19	We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:
20	
21	- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.
22	- **Data-flow graph**: inter-procedural data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.
23	
24	### File-Level Reachability
25	
26	From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.
27	
28	A key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.
29	
30	At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].
31	
32	### Beniget Fallback
33	
34	For repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].
35	
36	### Coverage Statistics
37	
38	The extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:
39	
40	| Metric | Value |
41	|--------|-------|
42	| Timeout rate | 0% (all repository tiers) |
43	| Repository coverage | 123/131 (93.9%) |
44	| Structural data rate | 34% of instances |
45	| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |
46	
47	The 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.
48	
49	## §3.3 Structure-Aware Negative Mining
50	
51	We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.
52	
53	### Random Negatives
54	
55	For each query $q$, we sample $K$ negatives uniformly at random from $\mathcal{F} \setminus \mathcal{F}^+_q$:
56	
57	$$f^-_{\text{rand}} \sim \text{Uniform}(\mathcal{F} \setminus \mathcal{F}^+_q), \quad |\{f^-_{\text{rand}}\}| = K$$
58	
59	This baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.
60	
61	### Embedding-Distance Negatives
62	
63	We compute embeddings for all files and queries using $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:
64	
65	$$f^-_{\text{embed}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
66	
67	These negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\theta_0}$ and avoids the instability and computational overhead of online re-mining \cite{xiong2021ance}.
68	
69	### Dataflow-Aware Negatives
70	
71	This strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\mathcal{F}^+_q$, define the reachability set:
72	
73	$$\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$$
74	
75	where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:
76	
77	$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
78	
79	These files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.
80	
81	For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).
82	
83	### Difficulty Gradient
84	
85	The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).
86	
87	### Relationship to BM25 Baselines
88	
89	In addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].
90	
91	## §3.4 Contrastive Fine-tuning
92	
93	### InfoNCE Loss
94	
95	We train with InfoNCE loss \cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\{f^-_1, \ldots, f^-_K\}$:
96	
97	$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
98	
99	where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].
100	
101	### LoRA Fine-tuning Setup
102	
103	We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}—using LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.
104	
105	Each encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].
106	
107	Training uses AdamW with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
108	
109	### Dual Checkpoint Strategy
110	
111	We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\theta^*_{\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].
112	
113	### Early Stopping
114	
115	The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].
116	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f079a865-c1aa-4bac-b4fb-3a227f43490c",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "91108b67-c35b-4f07-b13b-55805cf3abbb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
      "content": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n",
      "numLines": 116,
      "startLine": 1,
      "totalLines": 116
    }
  },
  "sourceToolAssistantUUID": "f079a865-c1aa-4bac-b4fb-3a227f43490c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T02:03:06.201Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M71L1jczw579J8qucEttua`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91108b67-c35b-4f07-b13b-55805cf3abbb",
  "isSidechain": false,
  "requestId": "req_011Cb3XpiSfw1WTNiaUgdYPK",
  "type": "assistant",
  "uuid": "47ebc6f4-9c40-4a2d-ba30-f50a892809e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzqoXRZmPkRjY6mejKEmgM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6123,
      "cache_read_input_tokens": 23344,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 605,
          "cache_read_input_tokens": 23344,
          "cache_creation_input_tokens": 6123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6123
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

_source line 32 · 2026-05-15T02:03:06.271Z_

```json
{
  "parentUuid": "0c539570-1206-4ea8-a5cb-ef1cb7bd0811",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "111e2d0d-5815-4f5e-ba7e-ae1bda113f78",
  "timestamp": "2026-05-15T02:03:06.271Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "leafUuid": "111e2d0d-5815-4f5e-ba7e-ae1bda113f78",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix Claim 2 overly strong wording in paper drafts",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Assistant

_source line 35 · 2026-05-15T02:05:24.003Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the files. Let me identify the 6 mandatory fixes (❌ 过强) and the additional ⚠️ fixes. Let me map out the changes needed:

**Must fix (❌ 过强) - 6 items:**

1. **paper_framing.md - Core Insight**: "The effectiveness of hard negative mining strategies depends on the encoder's representation geometry." → Add hedging
2. **paper_framing.md - Dual-Pillar Secondary**: "enabling practitioners to predict which strategy suits their encoder without exhaustive experiments" → Add hedging
3. **discussion_v2.md - §5.2 title**: "Representation Geometry as a Predictor of Strategy Effectiveness" → "Representation Geometry and Strategy Effectiveness: An Exploratory Analysis"


4. **discussion_v2.md - §5.2 first sentence**: Change "reveals a practical insight: the pretrained encoder's representation geometry predicts whether..." to "suggests a hypothesis worth further investigation..."
5. **discussion_v2.md - §5.2 "explains"**: Replace "This explains the +0.8pp R@1 improvement" with "This is consistent with the +0.8pp R@1 improvement"
6. **related_work_v1.md - §2.3**: Soften "show that the relative effectiveness of mining strategies depends on" to "observe that the relative effectiveness of mining strategies appears to depend on"

Let me double-check against the review report to make sure I have the right count.

Looking at the statistics, it says 5 items marked as ❌ 过强, but the actual "建议修改" section lists 6 items. I need to reconcile this discrepancy—the count in the summary doesn't match what's enumerated in the detailed section.

Now I'm going through the ⚠️ items that need attention: adding an "[exploratory]" label to the Story Spine contribution, adjusting language in the introduction and experiments sections to be more cautious ("may mediate" instead of "mediates"), and reviewing the mechanistic hypothesis discussion.

I notice there's a discrepancy between what the review references (introduction_v1.md) and what I'm actually working with (introduction_v2.md). Looking at paragraph 3 in introduction_v2.md, the text about negative difficulty margin analysis and how the pretrained embedding space mediates strategy effectiveness is already slightly different from the review's quote—it uses "mechanistic hypothesis" rather than "mechanistic explanation," which is actually closer to what's needed. But I should still verify this matches the intent of the review's feedback.

Now I'm cross-referencing the paper_framing.md content to see what's actually flagged. The core insight about representation geometry and hard negative mining is there, along with the dual-pillar secondary about predicting which strategy suits an encoder. The story spine contribution about structure-grounded negatives and mechanistic analysis is also present. I'm checking whether the headline result template's phrasing about "mechanistic explanation" was marked as a warning or a required change in the revision list.

Looking back at the task, it says to fix the overclaimed language in both paper_framing.md and the existing draft around Claim 2 about dataflow-aware filtering. The "6 必须修复" in the title is the minimum threshold, but the actual instruction is to revise all instances of overstated claims, not just those six. So I need to plan edits across the document systematically.

For the Core Insight section, I'm softening the definitive statements about encoder-strategy interactions to acknowledge these are preliminary findings needing validation. The Dual-Pillar Secondary needs to shift from claiming we can predict strategy effectiveness to offering a candidate heuristic that requires broader testing. In the Story Spine contribution, I should mark the dataflow observation as exploratory rather than conclusive. And the headline result template needs to frame the mechanistic explanation as a candidate explanation rather than a definitive one.

Moving through the document edits, I'm consistently adding qualifiers like "suggests," "may mediate," and "candidate" to reflect that these are mechanistic hypotheses grounded in our analysis but not yet confirmed across diverse settings. The changes to §4.2 and §4.4 follow the same pattern—acknowledging what our representation geometry analysis reveals while being transparent about the exploratory nature of these findings.

I also need to update that Models section in experiment_setup_v1.md with the same language shift. For the discussion section, I'm reframing the title to emphasize this is an exploratory analysis rather than claiming representation geometry as a definitive predictor, which better matches the cautious tone we're establishing throughout. Looking at the next thinking, I need to rewrite the practical implication paragraph with appropriate hedging language. The reviewer flagged this as too strong, so I should soften the claim about what practitioners can do.

The interaction between representation geometry and strategy effectiveness could have practical value if validated across different encoder comparisons—practitioners might be able to compute positional similarity scores to predict when structure-grounded negatives would outperform simpler approaches.

For the Future Work section, I'm adjusting the language around pos_sim's predictive power to reflect correlation rather than direct causation. I also need to go through the related work and experiment setup sections to systematically apply the same hedging pattern—replacing "shows" with "observe," "depends on" with "appears to depend on," and adding "may" before claims about what interactions reveal.

Now I'm organizing the specific edits across multiple files. I need to handle paper_framing.md first with changes to the core insight, secondary pillar, story spine contribution, and headline result template. Then I'll move through introduction_v2.md and the other files, making sure each edit properly softens the causal language while maintaining the paper's core arguments. I'm finishing up the last edit for related_work_v1.md in section 2.3, changing the phrasing from "show that...depends on" to "observe that...appears to depend on". Then I need to add a comment tag with today's date to the end of each modified file, and handle the paper_framing.md updates through the save function since that one requires the full file content. I need to place the exploratory framing sentence right after the section title, before the modified first sentence. So the structure will be: title, then the new sentence about presenting this as an exploratory observation from two encoders, then the reworded opening that shifts from "reveals" to "suggests" language. Looking at how the negative mining strategies perform differently across the two encoders, I'm seeing that representation geometry plays a key role in determining which approach works best—this interaction between encoder properties and mining effectiveness is something I should emphasize more carefully as an observation rather than a definitive finding. I'm working through the wording of that conditional statement in experiment_setup_v1.md—the issue is whether "mediates" is too causal for a hypothetical claim. I think "may mediate" softens it appropriately while keeping the sentence structure intact, though I need to decide if "reveals" or "may indicate" works better with that phrasing.

Now I'm seeing the review flagged the same "mediates" language in the actual files, so I should apply "may mediate" consistently across both documents. Looking at introduction_v2.md line 22, the review suggests several tweaks: softening "reveals" to "suggests," changing "mediates" to "may mediate," and adding "candidate" before "mechanistic hypothesis." The v2 version is already an improvement over what the review originally critiqued, so these adjustments should bring it even closer to the right tone.

I'm going to batch all the edits across the four files at once—updating discussion_v2.md, related_work_v1.md, experiments_v1.md, and experiment_setup_v1.md with their respective changes and adding comments to flag the modifications. I'm realizing that since each old_string is unique within discussion_v2.md, I can safely run all the edits in parallel without conflicts, even though they're on the same file. I'm overthinking the concurrency issue here. Let me just run all the edits in parallel and handle any failures that come up. I'll batch them by file: all the other files can go at once since they have minimal edits, and I'll sequence the discussion_v2.md changes since there are several of them. Actually, I'm going to simplify this further and just fire everything off together—the Edit tool should handle concurrent modifications properly, and each string I'm replacing is unique within its file anyway. I'm realizing 14 parallel calls is too many—I should consolidate edits by file instead. For discussion_v2.md, I can combine the title change with the introductory sentences into a single edit that reframes the section as exploratory rather than definitive, softening the language around the representation geometry hypothesis.

Now I'll execute all the edits across the files in parallel, making sure to add the end-of-file comment markers to each modified document.

Let me check whether introduction_v2.md exists—the task successfully read it, so v2 is the right file. Looking at paragraph 3 more closely, the review flagged "reveals" and "mediates" as problematic language. The v2 version already improved on v1 by using "exploratory observation" and "mechanistic hypothesis" instead of "mechanistic explanation," but I need to see if further refinement is needed.

The remaining issue is that "reveals" and "mediates" are still too strong. I should soften these to "suggests" and "may mediate," and change "providing a mechanistic hypothesis" to "providing a candidate mechanistic hypothesis" with a section reference. Now I'll apply all the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "111e2d0d-5815-4f5e-ba7e-ae1bda113f78",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "85f8c09b-74fd-45e4-ba42-5ebcb22c15c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 36 · 2026-05-15T02:05:24.006Z_

Now I have all the files. Let me execute all the edits across files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85f8c09b-74fd-45e4-ba42-5ebcb22c15c5",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "f6085369-cbec-428c-a959-4d98e153fdd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 37 · 2026-05-15T02:05:24.177Z_

<details open><summary>🔧 Tool call — Edit · `toolu_012EQB1QsBD27hz62LeM3rf4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
  "old_string": "## 5.2 Representation Geometry as a Predictor of Strategy Effectiveness\n\nOur negative difficulty analysis (Section 4.4) reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit beyond embedding-distance mining.",
  "new_string": "## 5.2 Representation Geometry and Strategy Effectiveness: An Exploratory Analysis\n\nWe present the following analysis as an exploratory observation derived from two encoders, not a validated mechanism.\n\nOur negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6085369-cbec-428c-a959-4d98e153fdd9",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "dacb579f-4c46-4046-8bcc-cd6836651765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 38 · 2026-05-15T02:05:32.135Z_

<details><summary>↩ Tool result · `toolu_01XvGKBLPJrjSUCaQw7SjrXZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7190617-62b6-4a30-9974-13f4af0b6efa",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "d99566c9-f675-4779-bbdb-28ae6b8c8580",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
    "oldString": "negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).",
    "newString": "negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).",
    "originalFile": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          " ",
          " Our experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.",
          " First, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.",
          "-Second, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).",
          "+Second, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).",
          " Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.",
          " ",
          " Our contributions are as follows:"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f7190617-62b6-4a30-9974-13f4af0b6efa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T02:05:24.202Z_

<details><summary>↩ Tool result · `toolu_012EQB1QsBD27hz62LeM3rf4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dacb579f-4c46-4046-8bcc-cd6836651765",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "cd87885b-89ef-4be7-a884-462bd5a316ad",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
    "oldString": "## 5.2 Representation Geometry as a Predictor of Strategy Effectiveness\n\nOur negative difficulty analysis (Section 4.4) reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit beyond embedding-distance mining.",
    "newString": "## 5.2 Representation Geometry and Strategy Effectiveness: An Exploratory Analysis\n\nWe present the following analysis as an exploratory observation derived from two encoders, not a validated mechanism.\n\nOur negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.",
    "originalFile": "# 5. Discussion\n\n## 5.1 Relationship to Inference-Time Graph Methods\n\nA growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.\nCodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.\n\nTable 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:\n\n**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.\n\n**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a sanitizer that transforms data between a source and sink across call boundaries. This deeper semantic signal generates harder, more informative negatives than structural proximity alone.\n\n**Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.\n\n## 5.2 Representation Geometry as a Predictor of Strategy Effectiveness\n\nOur negative difficulty analysis (Section 4.4) reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit beyond embedding-distance mining.\n\nWhen the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This explains the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).\n\nWhen the representation space has healthy separation—as observed for StarCoder2-3B (pos\\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.\n\nThis interaction between representation geometry and strategy effectiveness has a practical implication: practitioners can compute pos\\_sim on a held-out sample with their pretrained encoder (a single forward pass, requiring no training) to predict whether structure-grounded negatives are worth the extraction cost. We observe that pos\\_sim > 0.98 serves as an approximate threshold above which structural negatives provide conditional benefit, though we note this threshold is derived from two encoder observations and should be validated more broadly.\n\n## 5.3 Limitations\n\nWe identify several limitations of the current study that contextualize our findings:\n\n**Encoder scope.** Our experiments use two decoder-only 3B-parameter encoders (Qwen2.5-Coder-3B and StarCoder2-3B). While these models differ meaningfully in pretraining corpus and representation geometry—enabling our interaction analysis—generalizing to encoder-only architectures (e.g., CodeBERT), larger scales, or non-code domains requires further investigation.\n\n**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.\n\n**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).\n\n**Static mining.** Our negative mining is performed once before training and remains fixed throughout. Dynamic re-mining—where negatives are refreshed each epoch using the current encoder's embeddings—could yield progressively harder negatives as the model improves. We do not evaluate this variant in the current work and acknowledge the static-vs.-dynamic mining confound as a limitation. We plan to address this in future revisions.\n\n**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.\n\n## 5.4 Future Work\n\nWe identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:\n\n**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.\n\n**Representation-guided strategy selection.** Our observation that pos\\_sim predicts strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.\n\n**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 10,
        "newStart": 13,
        "newLines": 12,
        "lines": [
          " ",
          " **Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.",
          " ",
          "-## 5.2 Representation Geometry as a Predictor of Strategy Effectiveness",
          "+## 5.2 Representation Geometry and Strategy Effectiveness: An Exploratory Analysis",
          " ",
          "-Our negative difficulty analysis (Section 4.4) reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit beyond embedding-distance mining.",
          "+We present the following analysis as an exploratory observation derived from two encoders, not a validated mechanism.",
          " ",
          "+Our negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.",
          "+",
          " When the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This explains the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).",
          " ",
          " When the representation space has healthy separation—as observed for StarCoder2-3B (pos\\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "dacb579f-4c46-4046-8bcc-cd6836651765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T02:05:24.381Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BcRGTNA4yWcW2cwBKaaRZj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
  "old_string": "This explains the +0.8pp R@1 improvement",
  "new_string": "This is consistent with the +0.8pp R@1 improvement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd87885b-89ef-4be7-a884-462bd5a316ad",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "15b25425-3755-48c4-bc9c-0aec912eb746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 41 · 2026-05-15T02:05:24.393Z_

<details><summary>↩ Tool result · `toolu_01BcRGTNA4yWcW2cwBKaaRZj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15b25425-3755-48c4-bc9c-0aec912eb746",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "79545d1f-e3ef-4baf-9350-b0ab026f37e2",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
    "oldString": "This explains the +0.8pp R@1 improvement",
    "newString": "This is consistent with the +0.8pp R@1 improvement",
    "originalFile": "# 5. Discussion\n\n## 5.1 Relationship to Inference-Time Graph Methods\n\nA growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.\nCodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.\n\nTable 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:\n\n**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.\n\n**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a sanitizer that transforms data between a source and sink across call boundaries. This deeper semantic signal generates harder, more informative negatives than structural proximity alone.\n\n**Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.\n\n## 5.2 Representation Geometry and Strategy Effectiveness: An Exploratory Analysis\n\nWe present the following analysis as an exploratory observation derived from two encoders, not a validated mechanism.\n\nOur negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.\n\nWhen the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This explains the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).\n\nWhen the representation space has healthy separation—as observed for StarCoder2-3B (pos\\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.\n\nThis interaction between representation geometry and strategy effectiveness has a practical implication: practitioners can compute pos\\_sim on a held-out sample with their pretrained encoder (a single forward pass, requiring no training) to predict whether structure-grounded negatives are worth the extraction cost. We observe that pos\\_sim > 0.98 serves as an approximate threshold above which structural negatives provide conditional benefit, though we note this threshold is derived from two encoder observations and should be validated more broadly.\n\n## 5.3 Limitations\n\nWe identify several limitations of the current study that contextualize our findings:\n\n**Encoder scope.** Our experiments use two decoder-only 3B-parameter encoders (Qwen2.5-Coder-3B and StarCoder2-3B). While these models differ meaningfully in pretraining corpus and representation geometry—enabling our interaction analysis—generalizing to encoder-only architectures (e.g., CodeBERT), larger scales, or non-code domains requires further investigation.\n\n**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.\n\n**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).\n\n**Static mining.** Our negative mining is performed once before training and remains fixed throughout. Dynamic re-mining—where negatives are refreshed each epoch using the current encoder's embeddings—could yield progressively harder negatives as the model improves. We do not evaluate this variant in the current work and acknowledge the static-vs.-dynamic mining confound as a limitation. We plan to address this in future revisions.\n\n**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.\n\n## 5.4 Future Work\n\nWe identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:\n\n**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.\n\n**Representation-guided strategy selection.** Our observation that pos\\_sim predicts strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.\n\n**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          " ",
          " Our negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.",
          " ",
          "-When the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This explains the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).",
          "+When the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This is consistent with the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).",
          " ",
          " When the representation space has healthy separation—as observed for StarCoder2-3B (pos\\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "15b25425-3755-48c4-bc9c-0aec912eb746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T02:05:25.240Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01K6vVc51WMBkLP8w5AZoGTx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
  "old_string": "Our observation that pos\\_sim predicts strategy effectiveness suggests",
  "new_string": "Our observation that pos\\_sim appears to correlate with strategy effectiveness suggests"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79545d1f-e3ef-4baf-9350-b0ab026f37e2",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "598e4784-84ac-423e-a01b-37b52fa9c172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 43 · 2026-05-15T02:05:25.252Z_

<details><summary>↩ Tool result · `toolu_01K6vVc51WMBkLP8w5AZoGTx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "598e4784-84ac-423e-a01b-37b52fa9c172",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "cdec8090-04ca-4d61-a530-09ce228afe7b",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
    "oldString": "Our observation that pos\\_sim predicts strategy effectiveness suggests",
    "newString": "Our observation that pos\\_sim appears to correlate with strategy effectiveness suggests",
    "originalFile": "# 5. Discussion\n\n## 5.1 Relationship to Inference-Time Graph Methods\n\nA growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.\nCodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.\n\nTable 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:\n\n**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.\n\n**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a sanitizer that transforms data between a source and sink across call boundaries. This deeper semantic signal generates harder, more informative negatives than structural proximity alone.\n\n**Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.\n\n## 5.2 Representation Geometry and Strategy Effectiveness: An Exploratory Analysis\n\nWe present the following analysis as an exploratory observation derived from two encoders, not a validated mechanism.\n\nOur negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.\n\nWhen the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This is consistent with the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).\n\nWhen the representation space has healthy separation—as observed for StarCoder2-3B (pos\\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.\n\nThis interaction between representation geometry and strategy effectiveness has a practical implication: practitioners can compute pos\\_sim on a held-out sample with their pretrained encoder (a single forward pass, requiring no training) to predict whether structure-grounded negatives are worth the extraction cost. We observe that pos\\_sim > 0.98 serves as an approximate threshold above which structural negatives provide conditional benefit, though we note this threshold is derived from two encoder observations and should be validated more broadly.\n\n## 5.3 Limitations\n\nWe identify several limitations of the current study that contextualize our findings:\n\n**Encoder scope.** Our experiments use two decoder-only 3B-parameter encoders (Qwen2.5-Coder-3B and StarCoder2-3B). While these models differ meaningfully in pretraining corpus and representation geometry—enabling our interaction analysis—generalizing to encoder-only architectures (e.g., CodeBERT), larger scales, or non-code domains requires further investigation.\n\n**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.\n\n**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).\n\n**Static mining.** Our negative mining is performed once before training and remains fixed throughout. Dynamic re-mining—where negatives are refreshed each epoch using the current encoder's embeddings—could yield progressively harder negatives as the model improves. We do not evaluate this variant in the current work and acknowledge the static-vs.-dynamic mining confound as a limitation. We plan to address this in future revisions.\n\n**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.\n\n## 5.4 Future Work\n\nWe identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:\n\n**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.\n\n**Representation-guided strategy selection.** Our observation that pos\\_sim predicts strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.\n\n**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.\n",
    "structuredPatch": [
      {
        "oldStart": 45,
        "oldLines": 6,
        "newStart": 45,
        "newLines": 6,
        "lines": [
          " ",
          " **Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.",
          " ",
          "-**Representation-guided strategy selection.** Our observation that pos\\_sim predicts strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.",
          "+**Representation-guided strategy selection.** Our observation that pos\\_sim appears to correlate with strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.",
          " ",
          " **Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "598e4784-84ac-423e-a01b-37b52fa9c172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T02:05:26.651Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BuTaDFobJxnnnFJgwLbzVf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry",
  "new_string": "observe that the relative effectiveness of mining strategies appears to depend on the encoder's pretrained representation geometry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdec8090-04ca-4d61-a530-09ce228afe7b",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "3567eea6-0f34-443c-90d9-ba24b5e9408b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 45 · 2026-05-15T02:05:26.662Z_

<details><summary>↩ Tool result · `toolu_01BuTaDFobJxnnnFJgwLbzVf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3567eea6-0f34-443c-90d9-ba24b5e9408b",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "31697eb5-f6be-474e-9e0a-ba23190463d0",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry",
    "newString": "observe that the relative effectiveness of mining strategies appears to depend on the encoder's pretrained representation geometry",
    "originalFile": "# 2. Related Work\n\n## 2.1 Code Retrieval Methods\n\nRepo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \\cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \\cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \\cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \\cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.\n\nA parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \\cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \\cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \\cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \\cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \\cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \\cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization—though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.\n\nCritically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.\n\n## 2.2 Contrastive Learning for Code\n\nBuilding on the success of Sentence-BERT \\cite{reimers2019sentencebert} in learning dense sentence representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \\cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across eleven code search benchmarks. \\citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations.\n\nComplementary efforts have explored encoding structural information directly into code representations. code2vec \\cite{alon2019code2vec} demonstrates that AST path-based representations capture meaningful program properties at scale. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pre-training, showing that data-flow information improves downstream code understanding tasks. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning—a fundamentally different application of structural information that operates at the repository level rather than the function level.\n\nDespite the progress in contrastive code representation learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \\cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.\n\n## 2.3 Hard Negative Mining\n\nHard negative mining—selecting negative examples that are challenging for the current model—is well established for improving contrastive learning. In visual representation learning, SimCLR \\cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \\cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \\cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. Curriculum-based approaches such as CL-DRD \\cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.\n\nIn the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \\cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining—the strategy of selecting hard negatives by nearest-neighbor lookup in the encoder's frozen embedding space—in structural code retrieval settings.\n\nOur work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.\n",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 4,
        "newStart": 22,
        "newLines": 4,
        "lines": [
          " ",
          " In the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \\cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining—the strategy of selecting hard negatives by nearest-neighbor lookup in the encoder's frozen embedding space—in structural code retrieval settings.",
          " ",
          "-Our work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.",
          "+Our work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and observe that the relative effectiveness of mining strategies appears to depend on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "3567eea6-0f34-443c-90d9-ba24b5e9408b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T02:05:27.646Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01AvGv1E8vwdMySrUpyXd6xv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.",
  "new_string": "This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31697eb5-f6be-474e-9e0a-ba23190463d0",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "820a0fb6-f2eb-469a-8353-56ec7573fc41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 47 · 2026-05-15T02:05:27.657Z_

<details><summary>↩ Tool result · `toolu_01AvGv1E8vwdMySrUpyXd6xv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "820a0fb6-f2eb-469a-8353-56ec7573fc41",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "5b2a55be-f0d9-4450-a896-2590559298ba",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.",
    "newString": "This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 7,
        "newStart": 12,
        "newLines": 7,
        "lines": [
          " ",
          " ## §4.2 Implementation Details",
          " ",
          "-**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.",
          "+**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.",
          " ",
          " **Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "820a0fb6-f2eb-469a-8353-56ec7573fc41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T02:05:29.072Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01HacY2yC9kPGYMsVpve4Jsm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room",
  "new_string": "**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b2a55be-f0d9-4450-a896-2590559298ba",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "ecde7182-bef2-43d3-a143-64dc4fcded62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 49 · 2026-05-15T02:05:29.089Z_

<details><summary>↩ Tool result · `toolu_01HacY2yC9kPGYMsVpve4Jsm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecde7182-bef2-43d3-a143-64dc4fcded62",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "d02d1475-31ee-4532-9678-67a9c5442331",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room",
    "newString": "**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 106,
        "oldLines": 7,
        "newStart": 106,
        "newLines": 7,
        "lines": [
          " ",
          " **Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.",
          " ",
          "-**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.",
          "+**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.",
          " ",
          " ### Stratified Analysis",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ecde7182-bef2-43d3-a143-64dc4fcded62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T02:05:31.613Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01JxxeKgWYKgAM77AJLxUYkg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
  "old_string": "if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.",
  "new_string": "if it shows differential effects, the interaction may reveal how representation geometry mediates strategy effectiveness."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d02d1475-31ee-4532-9678-67a9c5442331",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "4a9edbfa-1e9f-43f2-b4f0-493a82623b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 51 · 2026-05-15T02:05:31.623Z_

<details><summary>↩ Tool result · `toolu_01JxxeKgWYKgAM77AJLxUYkg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a9edbfa-1e9f-43f2-b4f0-493a82623b12",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "bad44897-b705-45cf-9fbb-c987df56eaf2",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
    "oldString": "if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.",
    "newString": "if it shows differential effects, the interaction may reveal how representation geometry mediates strategy effectiveness.",
    "originalFile": "# §4 Experimental Setup\n\n## §4.1 Dataset\n\nWe construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit. We expand each task by treating every gold file as a separate training instance, yielding 44,173 instances total [Source: m1_extraction registry, data_count after filtering 6,696 clone/checkout failures from the original 50,869].\n\nWe run the StructFuse extraction pipeline (§3.2) on all instances. After filtering for extraction errors, we retain 14,288 usable instances across 123 repositories. Of these, approximately 34% possess CodeQL structural connectivity data (15,133 via CodeQL + 764 via beniget fallback); the remaining 66% lack structural data due to transient filesystem failures during batch extraction. For these instances, the dataflow-aware strategy falls back to embedding-distance mining (§3.3) [Source: m1_extraction registry].\n\nFor each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:\n\n| Seed | Train | Val | Total |\n|------|-------|-----|-------|\n| 42 | 11,308 | 2,980 | 14,288 |\n| 43 | 11,236 | 3,052 | 14,288 |\n| 44 | 11,264 | 3,024 | 14,288 |\n\n[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]\n\n## §4.2 Models\n\nWe select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.\n\n**Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.\n\n**StarCoder2-3B** \\cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.\n\nThe two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.\n\n## §4.3 Training Configuration\n\nAll hyperparameters are shared across strategies and encoders unless otherwise noted. The configuration was fixed before the full multi-seed experiment based on pilot runs.\n\n| Parameter | Value |\n|-----------|-------|\n| Optimizer | AdamW |\n| Learning rate | $2 \\times 10^{-5}$ |\n| LR schedule | Cosine annealing with linear warmup |\n| Warmup ratio | 0.1 |\n| Weight decay | 0.01 |\n| Gradient clipping | Max norm 1.0 |\n| Batch size | 8 |\n| Negatives per query ($K$) | 7 |\n| Max sequence length | 2,048 tokens |\n| Temperature ($\\tau$, initial) | 0.07 (learnable) |\n| LoRA rank ($r$) | 16 |\n| LoRA scaling ($\\alpha$) | 32 |\n| LoRA dropout | 0.05 |\n| LoRA target modules | $W_q$, $W_v$ (all attention layers) |\n| Projection dimension | 256 |\n| Gradient checkpointing | Enabled |\n| Evaluation interval | Every 500 steps |\n\n[Source: m2_full_qwen registry spec and notes]\n\n**Epoch schedule.** Seed 42 trains for 3 epochs without early stopping to provide a complete overfitting curve. Seeds 43 and 44 train for 2 epochs with early stopping (patience = 2 evaluation cycles based on validation loss). This asymmetric design was adopted after observing consistent overfitting past epoch 1 in the seed 42 exploratory run [Source: D026 decision].\n\n**Checkpoint selection.** We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Primary results use $\\theta^*_{\\text{R@1}}$; both are reported for metric-loss disagreement analysis [Source: D036 decision].\n\n**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].\n\n**Hardware.** All experiments are conducted on a single node with 2× NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs (cuda:0 and cuda:1) in parallel. Each individual run (single strategy, single seed, single encoder) requires approximately 5–7 hours. The core 18-run matrix requires approximately 120 GPU-hours [Source: m2_full_qwen and m2_full_starcoder registries].\n\n## §4.4 Evaluation Metrics\n\n**Retrieval metrics.** We report Recall@$k$ for $k \\in \\{1, 5, 10\\}$, computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per evaluation query). Recall@1 serves as the primary metric for checkpoint selection and strategy comparison. We also report validation loss (InfoNCE) as a secondary training diagnostic.\n\n**Statistical reporting.** All comparisons report:\n\n- **Aggregate**: mean ± standard deviation across 3 seeds per condition.\n- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).\n- **Effect size**: Cohen's $d$ for key comparisons, providing a standardized measure of practical significance independent of sample size.\n- **Per-seed consistency**: individual seed results reported alongside aggregates to assess stability. [TBD: exact CI and Cohen's d values pending M2 completion]\n\n**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].\n",
    "structuredPatch": [
      {
        "oldStart": 24,
        "oldLines": 7,
        "newStart": 24,
        "newLines": 7,
        "lines": [
          " ",
          " **StarCoder2-3B** \\cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.",
          " ",
          "-The two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction reveals how representation geometry mediates strategy effectiveness.",
          "+The two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction may reveal how representation geometry mediates strategy effectiveness.",
          " ",
          " ## §4.3 Training Configuration",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "4a9edbfa-1e9f-43f2-b4f0-493a82623b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T02:05:32.119Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01XvGKBLPJrjSUCaQw7SjrXZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "old_string": "negative difficulty margin analysis reveals that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) mediates strategy effectiveness, providing a mechanistic hypothesis for when different strategies should be preferred (pending multi-seed confirmation).",
  "new_string": "negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bad44897-b705-45cf-9fbb-c987df56eaf2",
  "isSidechain": false,
  "requestId": "req_011Cb3XqL72hkc6ZR5poRC8b",
  "type": "assistant",
  "uuid": "f7190617-62b6-4a30-9974-13f4af0b6efa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkQRBVGKiaxqhofG6XVhWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19585,
      "cache_read_input_tokens": 29467,
      "output_tokens": 8402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8402,
          "cache_read_input_tokens": 29467,
          "cache_creation_input_tokens": 19585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19585
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

_source line 53_

```json
{
  "type": "last-prompt",
  "leafUuid": "d99566c9-f675-4779-bbdb-28ae6b8c8580",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix Claim 2 overly strong wording in paper drafts",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Assistant

_source line 55 · 2026-05-15T02:05:34.361Z_

All edits applied. Now adding the end-of-file comments to each modified file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d99566c9-f675-4779-bbdb-28ae6b8c8580",
  "isSidechain": false,
  "requestId": "req_011Cb3Y25wo3AW3u3Av1dXxX",
  "type": "assistant",
  "uuid": "104d887b-a9de-489c-bc07-ea04b242cd34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BhMt138gGUhkaUNC284iN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9118,
      "cache_read_input_tokens": 49052,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 591,
          "cache_read_input_tokens": 49052,
          "cache_creation_input_tokens": 9118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9118
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

_source line 56 · 2026-05-15T02:05:35.324Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WcN3aSpMs2aAwMFN1ZEXDF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
  "offset": 44,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "104d887b-a9de-489c-bc07-ea04b242cd34",
  "isSidechain": false,
  "requestId": "req_011Cb3Y25wo3AW3u3Av1dXxX",
  "type": "assistant",
  "uuid": "ea1d359a-6dfc-485f-af04-8aae5a2f7735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BhMt138gGUhkaUNC284iN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9118,
      "cache_read_input_tokens": 49052,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 591,
          "cache_read_input_tokens": 49052,
          "cache_creation_input_tokens": 9118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9118
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

_source line 57 · 2026-05-15T02:05:35.339Z_

<details><summary>↩ Tool result · `toolu_01WcN3aSpMs2aAwMFN1ZEXDF`</summary>

```text
44	We identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:
45	
46	**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.
47	
48	**Representation-guided strategy selection.** Our observation that pos\_sim appears to correlate with strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.
49	
50	**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea1d359a-6dfc-485f-af04-8aae5a2f7735",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "365189a8-57cb-4126-9ec1-82ac3854ace2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
      "content": "We identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:\n\n**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.\n\n**Representation-guided strategy selection.** Our observation that pos\\_sim appears to correlate with strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.\n\n**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.\n",
      "numLines": 8,
      "startLine": 44,
      "totalLines": 51
    }
  },
  "sourceToolAssistantUUID": "ea1d359a-6dfc-485f-af04-8aae5a2f7735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T02:05:38.673Z_

<details><summary>↩ Tool result · `toolu_011fzWh3CMSXi2khznTNWRXM`</summary>

```text
28	\item \textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.
29	\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.
30	\end{enumerate}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7035de0-8b8d-4808-8711-1d94d055a63a",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "9358f48b-6107-4ee5-abe7-da96fce72f2a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
      "content": "\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n",
      "numLines": 4,
      "startLine": 28,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "c7035de0-8b8d-4808-8711-1d94d055a63a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T02:05:36.266Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GZrNECNHUD1wDmkxASTSXr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "offset": 24,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "365189a8-57cb-4126-9ec1-82ac3854ace2",
  "isSidechain": false,
  "requestId": "req_011Cb3Y25wo3AW3u3Av1dXxX",
  "type": "assistant",
  "uuid": "aec1afe5-7d68-4c72-a187-4f7be1f7f997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BhMt138gGUhkaUNC284iN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9118,
      "cache_read_input_tokens": 49052,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 591,
          "cache_read_input_tokens": 49052,
          "cache_creation_input_tokens": 9118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9118
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

_source line 60 · 2026-05-15T02:05:36.272Z_

<details><summary>↩ Tool result · `toolu_01GZrNECNHUD1wDmkxASTSXr`</summary>

```text
24	
25	Our work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and observe that the relative effectiveness of mining strategies appears to depend on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aec1afe5-7d68-4c72-a187-4f7be1f7f997",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "cfc995d1-46de-43b7-9495-3b501a7d58fe",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "\nOur work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and observe that the relative effectiveness of mining strategies appears to depend on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.\n",
      "numLines": 3,
      "startLine": 24,
      "totalLines": 26
    }
  },
  "sourceToolAssistantUUID": "aec1afe5-7d68-4c72-a187-4f7be1f7f997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T02:05:37.200Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SZt3Fioj5AgLAJvubv9tPt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "offset": 139,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfc995d1-46de-43b7-9495-3b501a7d58fe",
  "isSidechain": false,
  "requestId": "req_011Cb3Y25wo3AW3u3Av1dXxX",
  "type": "assistant",
  "uuid": "91220443-2598-47a0-81c6-1cf5d8da5226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BhMt138gGUhkaUNC284iN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9118,
      "cache_read_input_tokens": 49052,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 591,
          "cache_read_input_tokens": 49052,
          "cache_creation_input_tokens": 9118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9118
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

_source line 62 · 2026-05-15T02:05:37.204Z_

<details><summary>↩ Tool result · `toolu_01SZt3Fioj5AgLAJvubv9tPt`</summary>

```text
139	
140	The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91220443-2598-47a0-81c6-1cf5d8da5226",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "22172008-5f9a-467f-a844-47e4e617c44b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
      "content": "\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n",
      "numLines": 3,
      "startLine": 139,
      "totalLines": 141
    }
  },
  "sourceToolAssistantUUID": "91220443-2598-47a0-81c6-1cf5d8da5226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T02:05:38.139Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CKQxxyZva11pg2qTZ9Yuit`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
  "offset": 73,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22172008-5f9a-467f-a844-47e4e617c44b",
  "isSidechain": false,
  "requestId": "req_011Cb3Y25wo3AW3u3Av1dXxX",
  "type": "assistant",
  "uuid": "552a6f56-b26f-4ce0-9719-a43321493f0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BhMt138gGUhkaUNC284iN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9118,
      "cache_read_input_tokens": 49052,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 591,
          "cache_read_input_tokens": 49052,
          "cache_creation_input_tokens": 9118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9118
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

_source line 64 · 2026-05-15T02:05:38.144Z_

<details><summary>↩ Tool result · `toolu_01CKQxxyZva11pg2qTZ9Yuit`</summary>

```text
73	
74	**Checkpoint criterion.** Primary results use the $\theta^*_{\text{R@1}}$ checkpoint. We additionally report $\theta^*_{\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "552a6f56-b26f-4ce0-9719-a43321493f0f",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "78f47a08-0c6f-4057-995b-ac81154758bf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
      "content": "\n**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].\n",
      "numLines": 3,
      "startLine": 73,
      "totalLines": 75
    }
  },
  "sourceToolAssistantUUID": "552a6f56-b26f-4ce0-9719-a43321493f0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T02:05:38.663Z_

<details open><summary>🔧 Tool call — Read · `toolu_011fzWh3CMSXi2khznTNWRXM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "offset": 28,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78f47a08-0c6f-4057-995b-ac81154758bf",
  "isSidechain": false,
  "requestId": "req_011Cb3Y25wo3AW3u3Av1dXxX",
  "type": "assistant",
  "uuid": "c7035de0-8b8d-4808-8711-1d94d055a63a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BhMt138gGUhkaUNC284iN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9118,
      "cache_read_input_tokens": 49052,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 591,
          "cache_read_input_tokens": 49052,
          "cache_creation_input_tokens": 9118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9118
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

_source line 66 · 2026-05-15T02:05:38.750Z_

```json
{
  "parentUuid": "9358f48b-6107-4ee5-abe7-da96fce72f2a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fc8391d7-1936-4175-bd8a-6752fb0a89d2",
  "timestamp": "2026-05-15T02:05:38.750Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 67 · 2026-05-15T02:05:46.101Z_

<details><summary>Logged reasoning block</summary>

```text
Now I can add the end-of-file comments. Let me also check the introduction_v2.md contribution item 2 - it says "An analysis revealing that" - the review says this is ✅ but I notice "revealing" could be softened too. Actually, the review marks "Contribution 2" as ✅ so I'll leave it.

Wait, the contribution item 2 says: "An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry"

The "revealing" here could be softened, but the review marks this as ✅ because it has the [Exploratory observation] label. Let me leave it as is.


Now I'm adding end-of-file comments across all five artifact files, then moving on to paper_framing.md.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc8391d7-1936-4175-bd8a-6752fb0a89d2",
  "isSidechain": false,
  "requestId": "req_011Cb3Y2Zw3CZUJQWFBdrgpM",
  "type": "assistant",
  "uuid": "1fcd33a7-5bd0-465b-94d5-f9d3da18ba86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7C9g66ncWYuQFhzmgsZLQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 58170,
      "output_tokens": 1436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1436,
          "cache_read_input_tokens": 58170,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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

_source line 68 · 2026-05-15T02:05:49.758Z_

<details open><summary>🔧 Tool call — Edit · `toolu_012FQFHAqgqQKcXtk6AGdoJS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
  "old_string": "**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.",
  "new_string": "**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fcd33a7-5bd0-465b-94d5-f9d3da18ba86",
  "isSidechain": false,
  "requestId": "req_011Cb3Y2Zw3CZUJQWFBdrgpM",
  "type": "assistant",
  "uuid": "b5d57993-1be8-4794-a43e-810842dda0eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7C9g66ncWYuQFhzmgsZLQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 58170,
      "output_tokens": 1436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1436,
          "cache_read_input_tokens": 58170,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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

_source line 69 · 2026-05-15T02:05:49.807Z_

<details><summary>↩ Tool result · `toolu_012FQFHAqgqQKcXtk6AGdoJS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5d57993-1be8-4794-a43e-810842dda0eb",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "2d363eef-ed37-4728-85bf-b9de4e55b76e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/discussion_v2.md",
    "oldString": "**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.",
    "newString": "**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
    "originalFile": "# 5. Discussion\n\n## 5.1 Relationship to Inference-Time Graph Methods\n\nA growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.\nCodexGraph (Liu et al., NAACL 2025) materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph (Ouyang et al., ICLR 2025) provides line-level code graph navigation as a plug-in for SE agents; LocAgent (Chen et al., ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder (Liu et al., ASE 2024) and ARISE (Seddik & Fard, 2026) come closest to our work in incorporating data-flow information, but both are limited to intra-procedural scope.\n\nTable 5 summarizes the key dimensions of comparison. We highlight two axes along which StructFuse occupies a distinct position:\n\n**When structural information enters the pipeline.** Inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity and—for agent-based systems—requiring multiple LLM calls per query. StructFuse amortizes all graph computation to training time: CodeQL extraction costs approximately 8.9 seconds per instance (~110 CPU-hours for 44K instances; Table 4), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead. For latency-sensitive, high-throughput retrieval scenarios, this cost model is substantially more favorable.\n\n**Depth of data-flow analysis.** Most inference-time graph methods use structural relations (call graphs, class hierarchies, import dependencies). GraphCoder incorporates control-flow and data-dependence graphs, and ARISE exposes statement-level def-use edges, but both operate within single procedures. StructFuse leverages CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths—e.g., a sanitizer that transforms data between a source and sink across call boundaries. This deeper semantic signal generates harder, more informative negatives than structural proximity alone.\n\n**Complementarity.** We emphasize that StructFuse and inference-time graph methods address different stages of the retrieval pipeline and are composable rather than competing. A StructFuse-trained encoder can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking. Conversely, systems like CodexGraph or LocAgent can refine StructFuse retrieval results through explicit graph navigation when maximum precision is required. The two paradigms are complementary: StructFuse internalizes general structural patterns during training, while inference-time methods provide case-specific structural reasoning during deployment.\n\n## 5.2 Representation Geometry and Strategy Effectiveness: An Exploratory Analysis\n\nWe present the following analysis as an exploratory observation derived from two encoders, not a validated mechanism.\n\nOur negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.\n\nWhen the pretrained representation space is saturated—as observed for Qwen2.5-Coder-3B, where mean positive-pair cosine similarity reaches 0.986—the margin between positive and negative pairs is compressed (random margin = 0.074; embedding margin = 0.017). In this regime, all text-similarity-based negatives are clustered near the positive, and the encoder requires negatives drawn from an orthogonal signal dimension (structural disconnection) to learn meaningful discrimination. This is consistent with the +0.8pp R@1 improvement from dataflow-aware negatives over random baselines for Qwen (Table 2).\n\nWhen the representation space has healthy separation—as observed for StarCoder2-3B (pos\\_sim = 0.799, random margin = 0.194, 2.6× larger than Qwen)—embedding-distance mining alone provides a sufficient difficulty gradient, and dataflow negatives do not yield additional improvement (+1.6pp for embedding vs. random, but −0.5pp for dataflow vs. random; Table 2). The larger margins mean the encoder can still extract useful contrastive signal from text-similarity-based negatives without supplementary structural guidance.\n\nThis interaction between representation geometry and strategy effectiveness has a practical implication: practitioners can compute pos\\_sim on a held-out sample with their pretrained encoder (a single forward pass, requiring no training) to predict whether structure-grounded negatives are worth the extraction cost. We observe that pos\\_sim > 0.98 serves as an approximate threshold above which structural negatives provide conditional benefit, though we note this threshold is derived from two encoder observations and should be validated more broadly.\n\n## 5.3 Limitations\n\nWe identify several limitations of the current study that contextualize our findings:\n\n**Encoder scope.** Our experiments use two decoder-only 3B-parameter encoders (Qwen2.5-Coder-3B and StarCoder2-3B). While these models differ meaningfully in pretraining corpus and representation geometry—enabling our interaction analysis—generalizing to encoder-only architectures (e.g., CodeBERT), larger scales, or non-code domains requires further investigation.\n\n**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.\n\n**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).\n\n**Static mining.** Our negative mining is performed once before training and remains fixed throughout. Dynamic re-mining—where negatives are refreshed each epoch using the current encoder's embeddings—could yield progressively harder negatives as the model improves. We do not evaluate this variant in the current work and acknowledge the static-vs.-dynamic mining confound as a limitation. We plan to address this in future revisions.\n\n**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.\n\n## 5.4 Future Work\n\nWe identify three directions that follow naturally from our findings, while noting that each requires empirical validation before strong claims can be made:\n\n**Hybrid retrieval pipelines.** Integrating a StructFuse-trained encoder as the first-stage retriever within inference-time graph systems (e.g., CodexGraph, RANGER) could combine the efficiency of embedding-based retrieval with the precision of runtime graph navigation. Evaluating such pipelines on end-to-end benchmarks like SWE-bench would quantify the practical value of this complementarity.\n\n**Representation-guided strategy selection.** Our observation that pos\\_sim appears to correlate with strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.\n\n**Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.\n",
    "structuredPatch": [
      {
        "oldStart": 48,
        "oldLines": 3,
        "newStart": 48,
        "newLines": 5,
        "lines": [
          " **Representation-guided strategy selection.** Our observation that pos\\_sim appears to correlate with strategy effectiveness suggests an automated protocol: given a new encoder, compute representation geometry statistics on a calibration set, then select the appropriate negative mining strategy without exhaustive ablation. Validating this protocol across a wider range of encoders and tasks is a natural next step.",
          " ",
          " **Extension to dynamic and multi-lingual settings.** Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries to languages beyond Python, would address two of our current limitations. For dynamic mining, the key design question is the re-mining frequency—epoch-level re-mining requires repeated CodeQL extraction, and the cost-benefit tradeoff depends on how quickly the encoder's embedding space evolves during training.",
          "+",
          "+&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b5d57993-1be8-4794-a43e-810842dda0eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T02:05:56.801Z_

<details><summary>↩ Tool result · `toolu_01D2vhcTbcMFsa87MWYd3dRx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "486b4d18-150c-4941-8a61-042f0fd9842c",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "413bf705-b55f-41b8-a2fd-ac204acc3df8",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
    "oldString": "\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}",
    "newString": "\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
    "originalFile": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 28,
        "oldLines": 3,
        "newStart": 28,
        "newLines": 5,
        "lines": [
          " \\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.",
          " \\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.",
          " \\end{enumerate}",
          "+",
          "+&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "486b4d18-150c-4941-8a61-042f0fd9842c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T02:05:51.665Z_

<details open><summary>🔧 Tool call — Edit · `toolu_015AhRNfJwARcWuqMASsaqwg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.",
  "new_string": "Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d363eef-ed37-4728-85bf-b9de4e55b76e",
  "isSidechain": false,
  "requestId": "req_011Cb3Y2Zw3CZUJQWFBdrgpM",
  "type": "assistant",
  "uuid": "aab71f00-3999-46c7-9222-78830466a10f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7C9g66ncWYuQFhzmgsZLQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 58170,
      "output_tokens": 1436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1436,
          "cache_read_input_tokens": 58170,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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

_source line 72 · 2026-05-15T02:05:51.699Z_

<details><summary>↩ Tool result · `toolu_015AhRNfJwARcWuqMASsaqwg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aab71f00-3999-46c7-9222-78830466a10f",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "f2623bdf-ac70-423a-bcb1-3ffcbd1e62ac",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.",
    "newString": "Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
    "originalFile": "# 2. Related Work\n\n## 2.1 Code Retrieval Methods\n\nRepo-level code retrieval aims to identify relevant files or code spans from large codebases given a bug report or issue description. Classical sparse retrieval via BM25 \\cite{robertson2009bm25} remains a competitive baseline in this setting. The dense retrieval paradigm, pioneered by DPR \\cite{karpukhin2020dpr} for open-domain question answering, has been increasingly adopted for code. SweRank \\cite{reddy2025swerank} trains a retrieve-and-rerank pipeline for software issue localization, achieving state-of-the-art results on SWE-Bench-Lite and LocBench through text-based retrieval. SWE-Fixer \\cite{xie2025swefixer} combines BM25 with a learned retriever in a coarse-to-fine file retrieval pipeline, demonstrating that sparse and dense retrieval are complementary. Both systems, however, treat code files as flat text and do not exploit structural relationships between files during training.\n\nA parallel line of work leverages code structure graphs at inference time to guide code navigation. LocAgent \\cite{chen2025locagent} parses codebases into directed heterogeneous graphs and employs LLM agents for multi-hop graph reasoning during fault localization. RANGER \\cite{shah2025ranger} constructs repository knowledge graphs with variable-level nodes and applies MCTS-guided graph exploration for retrieval. CodexGraph \\cite{liu2025codexgraph} indexes codebases into graph databases queried via Cypher, while RepoGraph \\cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in module for software engineering agents. GraphCoder \\cite{liu2024graphcoder} incorporates control-flow and data-dependence edges into code context graphs for coarse-to-fine retrieval, and ARISE \\cite{seddik2026arise} exposes statement-level def-use edges for agentic fault localization—though both are limited to intra-procedural scope. These methods demonstrate the value of structural information for code retrieval, yet they incur per-query computational costs and, for agent-based systems, require multiple LLM calls per retrieval step.\n\nCritically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.\n\n## 2.2 Contrastive Learning for Code\n\nBuilding on the success of Sentence-BERT \\cite{reimers2019sentencebert} in learning dense sentence representations via siamese contrastive objectives, contrastive learning has proven effective for learning code representations that capture functional semantics beyond surface-level patterns. ContraCode \\cite{jain2021contracode} applies compiler-driven transformations to generate functionally equivalent program variants as positive pairs, training the encoder to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal (code-code) and bimodal (code-text) contrastive objectives, achieving strong results across eleven code search benchmarks. \\citet{ding2022programcontrasts} leverage program structure and functional attributes to construct contrastive pairs for learning code (dis)similarity representations.\n\nComplementary efforts have explored encoding structural information directly into code representations. code2vec \\cite{alon2019code2vec} demonstrates that AST path-based representations capture meaningful program properties at scale. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pre-training, showing that data-flow information improves downstream code understanding tasks. However, GraphCodeBERT uses data-flow as an auxiliary pre-training signal over individual functions, whereas our work uses inter-procedural data-flow to construct hard negatives for contrastive fine-tuning—a fundamentally different application of structural information that operates at the repository level rather than the function level.\n\nDespite the progress in contrastive code representation learning, these methods share a common dependency on negative sampling strategy yet few systematically investigate which negatives yield the best representations for code retrieval. Most approaches rely on in-batch negatives \\cite{karpukhin2020dpr} or random sampling, leaving the interaction between negative selection strategy and encoder representation geometry unexplored. Our work addresses this gap with a controlled comparison across negative mining strategies on modern decoder-only code encoders.\n\n## 2.3 Hard Negative Mining\n\nHard negative mining—selecting negative examples that are challenging for the current model—is well established for improving contrastive learning. In visual representation learning, SimCLR \\cite{chen2020simclr} demonstrates the importance of large batch sizes and hard negatives for learning discriminative features. In dense text retrieval, DPR \\cite{karpukhin2020dpr} shows that BM25-retrieved passages serve as effective hard negatives beyond in-batch sampling. ANCE \\cite{xiong2021ance} advances this by mining negatives from the model's own embedding space via approximate nearest neighbor search, achieving substantial gains over static BM25 negatives. Curriculum-based approaches such as CL-DRD \\cite{zeng2022cldrd} progressively increase negative difficulty during training through knowledge distillation.\n\nIn the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \\cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining—the strategy of selecting hard negatives by nearest-neighbor lookup in the encoder's frozen embedding space—in structural code retrieval settings.\n\nOur work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and observe that the relative effectiveness of mining strategies appears to depend on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.\n",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 3,
        "newStart": 23,
        "newLines": 5,
        "lines": [
          " In the code domain, hard negative mining has received comparatively less systematic attention. CoCoHaNeRe \\cite{fan2025cocohanere} proposes a differentiable hard negative mechanism for code search contrastive learning, arguing that gradient-based methods yield faster and more effective training than non-differentiable embedding-based negative selection. While CoCoHaNeRe demonstrates the advantages of its gradient-based approach within its experimental setting, it does not evaluate simple static embedding-distance mining—the strategy of selecting hard negatives by nearest-neighbor lookup in the encoder's frozen embedding space—in structural code retrieval settings.",
          " ",
          " Our work provides a systematic comparison that challenges the assumption that expensive gradient-based hard negative methods are necessary for effective code retrieval. We show that simple static embedding-distance mining consistently improves (pilot evidence; pending M2 full confirmation) retrieval performance across two decoder-only encoders with distinct representation geometries, without requiring differentiable negative generation mechanisms. Furthermore, we introduce structure-grounded negatives derived from inter-procedural data-flow analysis and observe that the relative effectiveness of mining strategies appears to depend on the encoder's pretrained representation geometry—an interaction that existing work does not examine. Together, these findings address a gap at the intersection of graph-guided code methods, which exploit structure only at inference time, and contrastive training methods, which have not systematically leveraged structural signals for negative selection.",
          "+",
          "+&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "aab71f00-3999-46c7-9222-78830466a10f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T02:05:53.099Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01PwHNddonRs5yAtERCrgobw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.",
  "new_string": "The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2623bdf-ac70-423a-bcb1-3ffcbd1e62ac",
  "isSidechain": false,
  "requestId": "req_011Cb3Y2Zw3CZUJQWFBdrgpM",
  "type": "assistant",
  "uuid": "2c116e57-847b-486b-8e4a-315fb758d4bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7C9g66ncWYuQFhzmgsZLQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 58170,
      "output_tokens": 1436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1436,
          "cache_read_input_tokens": 58170,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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

_source line 74 · 2026-05-15T02:05:53.110Z_

<details><summary>↩ Tool result · `toolu_01PwHNddonRs5yAtERCrgobw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c116e57-847b-486b-8e4a-315fb758d4bb",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "4d80ec56-bcb7-4990-bb64-b1fa35472e1b",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.",
    "newString": "The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 138,
        "oldLines": 3,
        "newStart": 138,
        "newLines": 5,
        "lines": [
          " | **Total** | **123** | **44,173** | **0%** | **\\placeholder{34.3%} [pending recalc]** | — |",
          " ",
          " The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.",
          "+",
          "+&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2c116e57-847b-486b-8e4a-315fb758d4bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-15T02:05:54.975Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011uUk9qspZVMtyFFBXG4gae`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
  "old_string": "**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].",
  "new_string": "**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d80ec56-bcb7-4990-bb64-b1fa35472e1b",
  "isSidechain": false,
  "requestId": "req_011Cb3Y2Zw3CZUJQWFBdrgpM",
  "type": "assistant",
  "uuid": "be44ab4c-4f98-44f6-a1f9-12cf02859b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7C9g66ncWYuQFhzmgsZLQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 58170,
      "output_tokens": 1436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1436,
          "cache_read_input_tokens": 58170,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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

_source line 76 · 2026-05-15T02:05:54.989Z_

<details><summary>↩ Tool result · `toolu_011uUk9qspZVMtyFFBXG4gae`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be44ab4c-4f98-44f6-a1f9-12cf02859b39",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "2ec43fb4-d858-474c-bc15-b6c49f7bd386",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiment_setup_v1.md",
    "oldString": "**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].",
    "newString": "**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
    "originalFile": "# §4 Experimental Setup\n\n## §4.1 Dataset\n\nWe construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit. We expand each task by treating every gold file as a separate training instance, yielding 44,173 instances total [Source: m1_extraction registry, data_count after filtering 6,696 clone/checkout failures from the original 50,869].\n\nWe run the StructFuse extraction pipeline (§3.2) on all instances. After filtering for extraction errors, we retain 14,288 usable instances across 123 repositories. Of these, approximately 34% possess CodeQL structural connectivity data (15,133 via CodeQL + 764 via beniget fallback); the remaining 66% lack structural data due to transient filesystem failures during batch extraction. For these instances, the dataflow-aware strategy falls back to embedding-distance mining (§3.3) [Source: m1_extraction registry].\n\nFor each random seed, we perform a per-repository stratified split to produce training and validation partitions. The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties. Exact split sizes:\n\n| Seed | Train | Val | Total |\n|------|-------|-----|-------|\n| 42 | 11,308 | 2,980 | 14,288 |\n| 43 | 11,236 | 3,052 | 14,288 |\n| 44 | 11,264 | 3,024 | 14,288 |\n\n[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]\n\n## §4.2 Models\n\nWe select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries, enabling us to study how encoder properties mediate the effectiveness of different negative mining strategies.\n\n**Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus. It exhibits a near-saturated pretrained representation space: mean positive cosine similarity of 0.986 and mean margin (pos_sim − neg_sim) of only 0.074 with random negatives at 2,048-token context [Source: neg_difficulty_analysis registry, qwen_2048]. This saturation—where nearly all file pairs receive high similarity scores—makes the baseline representation space challenging for contrastive learning and provides a stress test for negative mining strategies.\n\n**StarCoder2-3B** \\cite{li2023starcoder} uses a multi-task pretraining objective including FIM on The Stack v2. It maintains healthy representation separation: mean positive cosine similarity of 0.799 and a margin of 0.194 with random negatives—2.6× larger than Qwen's [Source: neg_difficulty_analysis registry, starcoder_2048]. This well-separated space allows us to contrast the behavior of mining strategies under fundamentally different geometric conditions.\n\nThe two encoders' divergent pretraining corpora and representation geometries provide a meaningful comparison axis: if a strategy improves both encoders, the benefit is likely encoder-agnostic; if it shows differential effects, the interaction may reveal how representation geometry mediates strategy effectiveness.\n\n## §4.3 Training Configuration\n\nAll hyperparameters are shared across strategies and encoders unless otherwise noted. The configuration was fixed before the full multi-seed experiment based on pilot runs.\n\n| Parameter | Value |\n|-----------|-------|\n| Optimizer | AdamW |\n| Learning rate | $2 \\times 10^{-5}$ |\n| LR schedule | Cosine annealing with linear warmup |\n| Warmup ratio | 0.1 |\n| Weight decay | 0.01 |\n| Gradient clipping | Max norm 1.0 |\n| Batch size | 8 |\n| Negatives per query ($K$) | 7 |\n| Max sequence length | 2,048 tokens |\n| Temperature ($\\tau$, initial) | 0.07 (learnable) |\n| LoRA rank ($r$) | 16 |\n| LoRA scaling ($\\alpha$) | 32 |\n| LoRA dropout | 0.05 |\n| LoRA target modules | $W_q$, $W_v$ (all attention layers) |\n| Projection dimension | 256 |\n| Gradient checkpointing | Enabled |\n| Evaluation interval | Every 500 steps |\n\n[Source: m2_full_qwen registry spec and notes]\n\n**Epoch schedule.** Seed 42 trains for 3 epochs without early stopping to provide a complete overfitting curve. Seeds 43 and 44 train for 2 epochs with early stopping (patience = 2 evaluation cycles based on validation loss). This asymmetric design was adopted after observing consistent overfitting past epoch 1 in the seed 42 exploratory run [Source: D026 decision].\n\n**Checkpoint selection.** We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Primary results use $\\theta^*_{\\text{R@1}}$; both are reported for metric-loss disagreement analysis [Source: D036 decision].\n\n**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].\n\n**Hardware.** All experiments are conducted on a single node with 2× NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs (cuda:0 and cuda:1) in parallel. Each individual run (single strategy, single seed, single encoder) requires approximately 5–7 hours. The core 18-run matrix requires approximately 120 GPU-hours [Source: m2_full_qwen and m2_full_starcoder registries].\n\n## §4.4 Evaluation Metrics\n\n**Retrieval metrics.** We report Recall@$k$ for $k \\in \\{1, 5, 10\\}$, computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per evaluation query). Recall@1 serves as the primary metric for checkpoint selection and strategy comparison. We also report validation loss (InfoNCE) as a secondary training diagnostic.\n\n**Statistical reporting.** All comparisons report:\n\n- **Aggregate**: mean ± standard deviation across 3 seeds per condition.\n- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).\n- **Effect size**: Cohen's $d$ for key comparisons, providing a standardized measure of practical significance independent of sample size.\n- **Per-seed consistency**: individual seed results reported alongside aggregates to assess stability. [TBD: exact CI and Cohen's d values pending M2 completion]\n\n**Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].\n",
    "structuredPatch": [
      {
        "oldStart": 72,
        "oldLines": 3,
        "newStart": 72,
        "newLines": 5,
        "lines": [
          " - **Per-seed consistency**: individual seed results reported alongside aggregates to assess stability. [TBD: exact CI and Cohen's d values pending M2 completion]",
          " ",
          " **Checkpoint criterion.** Primary results use the $\\theta^*_{\\text{R@1}}$ checkpoint. We additionally report $\\theta^*_{\\text{loss}}$ results to characterize the disagreement between optimization-aligned (loss) and task-aligned (R@1) checkpoint criteria [Source: D036].",
          "+",
          "+&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "be44ab4c-4f98-44f6-a1f9-12cf02859b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T02:05:56.792Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01D2vhcTbcMFsa87MWYd3dRx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "old_string": "\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}",
  "new_string": "\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ec43fb4-d858-474c-bc15-b6c49f7bd386",
  "isSidechain": false,
  "requestId": "req_011Cb3Y2Zw3CZUJQWFBdrgpM",
  "type": "assistant",
  "uuid": "486b4d18-150c-4941-8a61-042f0fd9842c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7C9g66ncWYuQFhzmgsZLQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 58170,
      "output_tokens": 1436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1436,
          "cache_read_input_tokens": 58170,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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
  "leafUuid": "413bf705-b55f-41b8-a2fd-ac204acc3df8",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix Claim 2 overly strong wording in paper drafts",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Assistant

_source line 80 · 2026-05-15T02:06:27.536Z_

<details><summary>Logged reasoning block</summary>

````text
All artifact files are done. Now I need to update paper_framing.md via save_project_file. I need to modify:

1. Core Insight - main sentence and "explains" sentence
2. Dual-Pillar Secondary - "enabling practitioners to predict"
3. Story Spine contribution (2) - add "[exploratory]"
4. Headline result template - "provides mechanistic explanation"

Let me construct the modified paper_framing.md content. I have the original from the read_project_file call. Let me make the changes.

Original Core Insight:
```


The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.
```

Now I'm revising this to reflect the exploratory nature of the findings. The main claim needs to shift from a definitive statement to a hypothesis grounded in our pilot data, acknowledging that we've only tested two encoders and need broader validation. The core mechanism about representation geometry and the saturation dynamics stays the same, but the framing becomes more cautious about the generalizability of the encoder-strategy interaction. I'm working through how to apply these framing changes to the paper — shifting from claiming mechanistic explanation to positioning it as a candidate explanation that needs validation on more encoders. The key modifications involve adding "candidate" and "[exploratory]" tags to temper the claims while keeping the core contribution about representation geometry and negative difficulty analysis intact. Now I need to carefully integrate these changes into the full paper_framing.md file and save it. I need to make five specific text replacements in the paper_framing.md file to add more cautious language around the claims, then save it. Since the file is already loaded in memory from the earlier read, I'll construct the modified version by applying each find-and-replace operation on the original content, then use the save function to write it back out.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "413bf705-b55f-41b8-a2fd-ac204acc3df8",
  "isSidechain": false,
  "requestId": "req_011Cb3Y3uGQR2w4km7b7jS5K",
  "type": "assistant",
  "uuid": "fc8dbe93-1174-4927-aff7-60b41d55e2ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118XJvi68ycEbBgaKpA3Ub2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1898,
      "cache_read_input_tokens": 59903,
      "output_tokens": 1424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1424,
          "cache_read_input_tokens": 59903,
          "cache_creation_input_tokens": 1898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1898
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

_source line 81 · 2026-05-15T02:06:27.538Z_

Now I need to update paper_framing.md. Let me read the file path first, then apply edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc8dbe93-1174-4927-aff7-60b41d55e2ea",
  "isSidechain": false,
  "requestId": "req_011Cb3Y3uGQR2w4km7b7jS5K",
  "type": "assistant",
  "uuid": "108a6ce7-9d1a-4cee-a3c7-4a65ccff8ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118XJvi68ycEbBgaKpA3Ub2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1898,
      "cache_read_input_tokens": 59903,
      "output_tokens": 1424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1424,
          "cache_read_input_tokens": 59903,
          "cache_creation_input_tokens": 1898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1898
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

_source line 82 · 2026-05-15T02:06:28.098Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NqgdAuTpQrRVWLYXSBUtYx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "108a6ce7-9d1a-4cee-a3c7-4a65ccff8ad6",
  "isSidechain": false,
  "requestId": "req_011Cb3Y3uGQR2w4km7b7jS5K",
  "type": "assistant",
  "uuid": "1b084fc5-bb2d-4868-a7b3-82c4a6bacd51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118XJvi68ycEbBgaKpA3Ub2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1898,
      "cache_read_input_tokens": 59903,
      "output_tokens": 1424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1424,
          "cache_read_input_tokens": 59903,
          "cache_creation_input_tokens": 1898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1898
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

_source line 83 · 2026-05-15T02:06:28.104Z_

<details><summary>↩ Tool result · `toolu_01NqgdAuTpQrRVWLYXSBUtYx`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b084fc5-bb2d-4868-a7b3-82c4a6bacd51",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "06b8453b-b091-4fbd-804e-b3153a1629ec",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 126
    }
  },
  "sourceToolAssistantUUID": "1b084fc5-bb2d-4868-a7b3-82c4a6bacd51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-15T02:06:33.193Z_

<details open><summary>🔧 Tool call — Edit · `toolu_015Beiu6LFyzDeAHZVz9T3rW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "The effectiveness of hard negative mining strategies depends on the encoder's representation geometry.",
  "new_string": "Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06b8453b-b091-4fbd-804e-b3153a1629ec",
  "isSidechain": false,
  "requestId": "req_011Cb3Y6DDDG1RykdKgaqZjz",
  "type": "assistant",
  "uuid": "a78d31fa-8744-4f1a-a0da-032bfc6e9d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156QPd3jf8MFbJJVdJQ4DcR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 61801,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 61801,
          "cache_creation_input_tokens": 1487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1487
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

_source line 85 · 2026-05-15T02:06:33.206Z_

<details><summary>↩ Tool result · `toolu_015Beiu6LFyzDeAHZVz9T3rW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a78d31fa-8744-4f1a-a0da-032bfc6e9d7f",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "1060dc04-b333-4169-87f3-d9b04385eea6",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "oldString": "The effectiveness of hard negative mining strategies depends on the encoder's representation geometry.",
    "newString": "Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 29,
        "oldLines": 7,
        "newStart": 29,
        "newLines": 7,
        "lines": [
          " ",
          " ## Core Insight",
          " ",
          "-The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.",
          "+Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.",
          " ",
          " ## Dual-Pillar Motivation",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a78d31fa-8744-4f1a-a0da-032bfc6e9d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-15T02:06:34.093Z_

<details open><summary>🔧 Tool call — Edit · `toolu_018iW8NywUATWTQUZtSScLk8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "This encoder-strategy interaction explains contradictory findings in prior work.",
  "new_string": "This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1060dc04-b333-4169-87f3-d9b04385eea6",
  "isSidechain": false,
  "requestId": "req_011Cb3Y6DDDG1RykdKgaqZjz",
  "type": "assistant",
  "uuid": "30d6022a-990f-41f8-bae2-56f7d65de1e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156QPd3jf8MFbJJVdJQ4DcR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 61801,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 61801,
          "cache_creation_input_tokens": 1487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1487
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

_source line 87 · 2026-05-15T02:06:37.503Z_

<details><summary>↩ Tool result · `toolu_01DxW9ohsFbGju7xpD52jLSB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bd58635-377b-42b2-b53e-54610d46c156",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "372ab8da-c21d-47b8-a73e-b0a9d82cc354",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "oldString": "provides mechanistic explanation for when different mining strategies are effective",
    "newString": "provides a candidate mechanistic explanation for when different mining strategies are effective",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 25,
        "oldLines": 7,
        "newStart": 25,
        "newLines": 7,
        "lines": [
          " ",
          " - **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.",
          " ",
          "-- **Headline result template**: \"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\"",
          "+- **Headline result template**: \"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides a candidate mechanistic explanation for when different mining strategies are effective.\"",
          " ",
          " ## Core Insight",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "1bd58635-377b-42b2-b53e-54610d46c156",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T02:06:34.102Z_

<details><summary>↩ Tool result · `toolu_018iW8NywUATWTQUZtSScLk8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30d6022a-990f-41f8-bae2-56f7d65de1e6",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "a5de0324-dc03-48ab-b43b-87ad6bd31078",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "oldString": "This encoder-strategy interaction explains contradictory findings in prior work.",
    "newString": "This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 29,
        "oldLines": 7,
        "newStart": 29,
        "newLines": 7,
        "lines": [
          " ",
          " ## Core Insight",
          " ",
          "-Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.",
          "+Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.",
          " ",
          " ## Dual-Pillar Motivation",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "30d6022a-990f-41f8-bae2-56f7d65de1e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-15T02:06:35.502Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01VcuL1w3aDXX9psPmpB5TBJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.",
  "new_string": "offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5de0324-dc03-48ab-b43b-87ad6bd31078",
  "isSidechain": false,
  "requestId": "req_011Cb3Y6DDDG1RykdKgaqZjz",
  "type": "assistant",
  "uuid": "5cfbe92a-71a4-4d4e-8bf9-841bdbe443d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156QPd3jf8MFbJJVdJQ4DcR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 61801,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 61801,
          "cache_creation_input_tokens": 1487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1487
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

_source line 90 · 2026-05-15T02:06:35.513Z_

<details><summary>↩ Tool result · `toolu_01VcuL1w3aDXX9psPmpB5TBJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cfbe92a-71a4-4d4e-8bf9-841bdbe443d8",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "6fe6d39c-fff1-4f37-8955-d94f614b10f1",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "oldString": "enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.",
    "newString": "offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 34,
        "oldLines": 7,
        "newStart": 34,
        "newLines": 7,
        "lines": [
          " ## Dual-Pillar Motivation",
          " ",
          " 1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.",
          "-2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.",
          "+2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.",
          " ",
          " ## Formal Definition",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "5cfbe92a-71a4-4d4e-8bf9-841bdbe443d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-15T02:06:36.441Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Xcv8Kpm5Em2YntEtj3TbJZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "(2) observe that structure-grounded",
  "new_string": "(2) [exploratory] observe that structure-grounded"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fe6d39c-fff1-4f37-8955-d94f614b10f1",
  "isSidechain": false,
  "requestId": "req_011Cb3Y6DDDG1RykdKgaqZjz",
  "type": "assistant",
  "uuid": "e2f35db4-8db5-4ba5-9860-03e35d9b0c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156QPd3jf8MFbJJVdJQ4DcR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 61801,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 61801,
          "cache_creation_input_tokens": 1487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1487
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

_source line 92 · 2026-05-15T02:06:36.459Z_

<details><summary>↩ Tool result · `toolu_01Xcv8Kpm5Em2YntEtj3TbJZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2f35db4-8db5-4ba5-9860-03e35d9b0c44",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "dc4e9af4-5a7c-4fc7-8959-ad08bff870dc",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "oldString": "(2) observe that structure-grounded",
    "newString": "(2) [exploratory] observe that structure-grounded",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 7,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          "   - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings",
          "   - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works",
          " ",
          "-- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.",
          "+- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.",
          " ",
          " - **Headline result template**: \"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective.\"",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "e2f35db4-8db5-4ba5-9860-03e35d9b0c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-15T02:06:37.493Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01DxW9ohsFbGju7xpD52jLSB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "provides mechanistic explanation for when different mining strategies are effective",
  "new_string": "provides a candidate mechanistic explanation for when different mining strategies are effective"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc4e9af4-5a7c-4fc7-8959-ad08bff870dc",
  "isSidechain": false,
  "requestId": "req_011Cb3Y6DDDG1RykdKgaqZjz",
  "type": "assistant",
  "uuid": "1bd58635-377b-42b2-b53e-54610d46c156",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156QPd3jf8MFbJJVdJQ4DcR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 61801,
      "output_tokens": 804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 804,
          "cache_read_input_tokens": 61801,
          "cache_creation_input_tokens": 1487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1487
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

_source line 94 · 2026-05-15T02:06:37.552Z_

```json
{
  "parentUuid": "372ab8da-c21d-47b8-a73e-b0a9d82cc354",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f3fdd621-377e-483a-972b-26275f0a897d",
  "timestamp": "2026-05-15T02:06:37.552Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 95_

```json
{
  "type": "last-prompt",
  "leafUuid": "f3fdd621-377e-483a-972b-26275f0a897d",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Runtime record

_source line 96_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix Claim 2 overly strong wording in paper drafts",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Assistant

_source line 97 · 2026-05-15T02:06:40.173Z_

Now save the updated paper_framing.md via MCP tool and add the end comment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3fdd621-377e-483a-972b-26275f0a897d",
  "isSidechain": false,
  "requestId": "req_011Cb3Y6uLhmiPzCE1VMBUEA",
  "type": "assistant",
  "uuid": "a086f017-9217-4642-8f14-be61aa3963ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZatoGo4yc2aHNu9BQLUGg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1236,
      "cache_read_input_tokens": 63288,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 63288,
          "cache_creation_input_tokens": 1236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1236
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

_source line 98 · 2026-05-15T02:06:40.230Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VByy968dGCq1piE6XAZBG4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a086f017-9217-4642-8f14-be61aa3963ed",
  "isSidechain": false,
  "requestId": "req_011Cb3Y6uLhmiPzCE1VMBUEA",
  "type": "assistant",
  "uuid": "dade0d9c-d67f-494e-b8f8-c0f75ef1d494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZatoGo4yc2aHNu9BQLUGg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1236,
      "cache_read_input_tokens": 63288,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 63288,
          "cache_creation_input_tokens": 1236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1236
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

_source line 99 · 2026-05-15T02:06:40.238Z_

<details><summary>↩ Tool result · `toolu_01VByy968dGCq1piE6XAZBG4`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.
10	
11	2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]
14	
15	## Story Spine
16	
17	- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
18	
19	- **Existing approaches & gaps**:
20	  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
21	  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
22	  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
23	  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.
27	
28	- **Headline result template**: "Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides a candidate mechanistic explanation for when different mining strategies are effective."
29	
30	## Core Insight
31	
32	Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, similarity function s, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]
50	- Backup: "Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
63	| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |
64	| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
65	| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
66	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
67	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
68	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
69	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
70	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
71	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
72	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
73	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
74	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
75	
76	## Evidence Status
77	
78	### Confirmed findings (basis for claims):
79	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption
80	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
81	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
82	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
83	- plan_006: CodeQL scalability confirmed at 123-repo scale
84	
85	### In progress:
86	- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.
87	- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.
88	- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15
89	
90	### Planned (priority order):
91	- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)
92	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
93	- plan_019: Pool size sensitivity (Dream consensus — external validity)
94	- plan_014: Temperature ablation (Dream reviewer concern)
95	- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
96	- plan_015: Dynamic mining baseline
97	- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
98	- plan_007/008/009: Additional ablations
99	
100	## Contingency (if full M2 results weaken claims)
101	
102	### All 18 runs confirm pilot pattern: Best case
103	- Full statistical power, paper as framed above
104	- Target: EMNLP Main
105	
106	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
107	- Drop Claim 2 to analysis observation
108	- Paper becomes: "Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
109	- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main
110	
111	### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]
112	- If plan_018 shows BM25 negatives perform ≈ random (not << random), the "challenging gradient-based assumption" narrative needs adjustment
113	- Pivot: "systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal"
114	- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome
115	- Claim 1 core preserved: "Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms"
116	- Impact: BM25 result determines narrative nuance, not core contribution
117	
118	### Embedding mining also loses advantage at full scale: Major reassessment needed
119	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
120	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
121	- Discuss with user before committing direction
122	
123	## Deprecated Claims (with reason)
124	
125	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dade0d9c-d67f-494e-b8f8-c0f75ef1d494",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "8623200b-6539-4177-bc06-b6d1bacdbd00",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\n\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\n\n- **Headline result template**: \"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides a candidate mechanistic explanation for when different mining strategies are effective.\"\n\n## Core Insight\n\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\n- Backup: \"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\n\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \"challenging gradient-based assumption\" narrative needs adjustment\n- Pivot: \"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\"\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\n- Claim 1 core preserved: \"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\"\n- Impact: BM25 result determines narrative nuance, not core contribution\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n",
      "numLines": 126,
      "startLine": 1,
      "totalLines": 126
    }
  },
  "sourceToolAssistantUUID": "dade0d9c-d67f-494e-b8f8-c0f75ef1d494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 100 · 2026-05-15T02:06:43.929Z_

<details><summary>Logged reasoning block</summary>

```text
The file looks good with all edits applied. Now I need to:
1. Add the end comment to paper_framing.md
2. Save via save_project_file

Let me add the comment first, then save.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8623200b-6539-4177-bc06-b6d1bacdbd00",
  "isSidechain": false,
  "requestId": "req_011Cb3Y775eSAgLYUPFxj4oP",
  "type": "assistant",
  "uuid": "1a9f63ad-0758-4402-9558-a326e7090590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwcAjTYPK31ZxwLcYUQT2y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 64524,
      "output_tokens": 391,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 391,
          "cache_read_input_tokens": 64524,
          "cache_creation_input_tokens": 3503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3503
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

_source line 101 · 2026-05-15T02:06:44.420Z_

All edits verified. Let me add the end comment to paper_framing.md and save it via MCP.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a9f63ad-0758-4402-9558-a326e7090590",
  "isSidechain": false,
  "requestId": "req_011Cb3Y775eSAgLYUPFxj4oP",
  "type": "assistant",
  "uuid": "98ac9b78-69f5-4958-9844-f7b8aef82a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwcAjTYPK31ZxwLcYUQT2y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 64524,
      "output_tokens": 391,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 391,
          "cache_read_input_tokens": 64524,
          "cache_creation_input_tokens": 3503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3503
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

_source line 102 · 2026-05-15T02:06:48.496Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01LkK9egfmNFD6CRqnk259bY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.",
  "new_string": "- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ac9b78-69f5-4958-9844-f7b8aef82a2d",
  "isSidechain": false,
  "requestId": "req_011Cb3Y775eSAgLYUPFxj4oP",
  "type": "assistant",
  "uuid": "3b412a83-a518-42d4-a748-47b53970a614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwcAjTYPK31ZxwLcYUQT2y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 64524,
      "output_tokens": 391,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 391,
          "cache_read_input_tokens": 64524,
          "cache_creation_input_tokens": 3503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3503
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

_source line 103 · 2026-05-15T02:06:48.513Z_

<details><summary>↩ Tool result · `toolu_01LkK9egfmNFD6CRqnk259bY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b412a83-a518-42d4-a748-47b53970a614",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "7b15e330-35c9-45c1-a033-2934a7cfc2d4",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "oldString": "- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.",
    "newString": "- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 123,
        "oldLines": 3,
        "newStart": 123,
        "newLines": 5,
        "lines": [
          " ## Deprecated Claims (with reason)",
          " ",
          " - ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.",
          "+",
          "+&lt;!-- Claim 2 wording fix: 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "3b412a83-a518-42d4-a748-47b53970a614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 104_

```json
{
  "type": "last-prompt",
  "leafUuid": "7b15e330-35c9-45c1-a033-2934a7cfc2d4",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Runtime record

_source line 105_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix Claim 2 overly strong wording in paper drafts",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Tool call

_source line 106 · 2026-05-15T02:06:50.309Z_

<details open><summary>🔧 Tool call — Read · `toolu_01837TrbPJqMC3S53PkjYS64`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b15e330-35c9-45c1-a033-2934a7cfc2d4",
  "isSidechain": false,
  "requestId": "req_011Cb3Y7iMgxCMstofx6hTr5",
  "type": "assistant",
  "uuid": "d9974b5e-cec8-4b14-bd9d-eae893a40070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYTeqBFRa6v2fSbfzig2iy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 68027,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 443,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 68027,
          "cache_creation_input_tokens": 443,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 443
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

_source line 107 · 2026-05-15T02:06:50.315Z_

<details><summary>↩ Tool result · `toolu_01837TrbPJqMC3S53PkjYS64`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.
10	
11	2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]
14	
15	## Story Spine
16	
17	- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
18	
19	- **Existing approaches & gaps**:
20	  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
21	  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
22	  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
23	  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.
27	
28	- **Headline result template**: "Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides a candidate mechanistic explanation for when different mining strategies are effective."
29	
30	## Core Insight
31	
32	Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, similarity function s, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]
50	- Backup: "Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
63	| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |
64	| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
65	| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
66	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
67	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
68	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
69	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
70	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
71	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
72	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
73	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
74	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
75	
76	## Evidence Status
77	
78	### Confirmed findings (basis for claims):
79	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption
80	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
81	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
82	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
83	- plan_006: CodeQL scalability confirmed at 123-repo scale
84	
85	### In progress:
86	- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.
87	- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.
88	- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15
89	
90	### Planned (priority order):
91	- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)
92	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
93	- plan_019: Pool size sensitivity (Dream consensus — external validity)
94	- plan_014: Temperature ablation (Dream reviewer concern)
95	- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
96	- plan_015: Dynamic mining baseline
97	- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
98	- plan_007/008/009: Additional ablations
99	
100	## Contingency (if full M2 results weaken claims)
101	
102	### All 18 runs confirm pilot pattern: Best case
103	- Full statistical power, paper as framed above
104	- Target: EMNLP Main
105	
106	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
107	- Drop Claim 2 to analysis observation
108	- Paper becomes: "Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
109	- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main
110	
111	### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]
112	- If plan_018 shows BM25 negatives perform ≈ random (not << random), the "challenging gradient-based assumption" narrative needs adjustment
113	- Pivot: "systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal"
114	- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome
115	- Claim 1 core preserved: "Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms"
116	- Impact: BM25 result determines narrative nuance, not core contribution
117	
118	### Embedding mining also loses advantage at full scale: Major reassessment needed
119	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
120	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
121	- Discuss with user before committing direction
122	
123	## Deprecated Claims (with reason)
124	
125	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
126	
127	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
128	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9974b5e-cec8-4b14-bd9d-eae893a40070",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "3b26aab1-cf89-488d-8bdf-f77f09bac652",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\n\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\n\n- **Headline result template**: \"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides a candidate mechanistic explanation for when different mining strategies are effective.\"\n\n## Core Insight\n\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\n- Backup: \"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\n\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \"challenging gradient-based assumption\" narrative needs adjustment\n- Pivot: \"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\"\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\n- Claim 1 core preserved: \"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\"\n- Impact: BM25 result determines narrative nuance, not core contribution\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n",
      "numLines": 128,
      "startLine": 1,
      "totalLines": 128
    }
  },
  "sourceToolAssistantUUID": "d9974b5e-cec8-4b14-bd9d-eae893a40070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 108 · 2026-05-15T02:06:53.273Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the paper_framing.md is updated. Now let me save it via save_project_file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b26aab1-cf89-488d-8bdf-f77f09bac652",
  "isSidechain": false,
  "requestId": "req_011Cb3Y7r721zhMtj1TeG7pj",
  "type": "assistant",
  "uuid": "d83913ca-6480-41bc-bb95-8162b919249b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BPTmtxy2JDfQYyBLBu3W9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3507,
      "cache_read_input_tokens": 68470,
      "output_tokens": 3270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3270,
          "cache_read_input_tokens": 68470,
          "cache_creation_input_tokens": 3507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3507
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

_source line 109 · 2026-05-15T02:06:53.735Z_

Now save via MCP.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d83913ca-6480-41bc-bb95-8162b919249b",
  "isSidechain": false,
  "requestId": "req_011Cb3Y7r721zhMtj1TeG7pj",
  "type": "assistant",
  "uuid": "d04f1e70-c23a-4dea-a17a-1789b1b70eeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BPTmtxy2JDfQYyBLBu3W9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3507,
      "cache_read_input_tokens": 68470,
      "output_tokens": 3270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3270,
          "cache_read_input_tokens": 68470,
          "cache_creation_input_tokens": 3507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3507
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

_source line 110 · 2026-05-15T02:08:04.271Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01CLsDnmBABJ1Kd62MnnFSyq`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\n\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\n\n- **Headline result template**: \"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides a candidate mechanistic explanation for when different mining strategies are effective.\"\n\n## Core Insight\n\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\n- Backup: \"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\n\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \"challenging gradient-based assumption\" narrative needs adjustment\n- Pivot: \"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\"\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\n- Claim 1 core preserved: \"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\"\n- Impact: BM25 result determines narrative nuance, not core contribution\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d04f1e70-c23a-4dea-a17a-1789b1b70eeb",
  "isSidechain": false,
  "requestId": "req_011Cb3Y7r721zhMtj1TeG7pj",
  "type": "assistant",
  "uuid": "35f323a6-bc02-4a8b-9911-231b008a2312",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BPTmtxy2JDfQYyBLBu3W9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3507,
      "cache_read_input_tokens": 68470,
      "output_tokens": 3270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3270,
          "cache_read_input_tokens": 68470,
          "cache_creation_input_tokens": 3507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3507
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

_source line 111 · 2026-05-15T02:08:04.300Z_

<details><summary>↩ Tool result · `toolu_01CLsDnmBABJ1Kd62MnnFSyq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35f323a6-bc02-4a8b-9911-231b008a2312",
  "isSidechain": false,
  "promptId": "1ec0d459-7221-430f-bf58-af78cbac4b78",
  "type": "user",
  "uuid": "6ed9e743-b8d9-49fe-b1df-bab4398b81f3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "35f323a6-bc02-4a8b-9911-231b008a2312",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 112_

```json
{
  "type": "last-prompt",
  "leafUuid": "6ed9e743-b8d9-49fe-b1df-bab4398b81f3",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Runtime record

_source line 113_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix Claim 2 overly strong wording in paper drafts",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Assistant

_source line 114 · 2026-05-15T02:08:20.360Z_

全部修改完成。修改汇总：

### 必须修复（❌ 过强）— 6 处

| # | 文件 | 修改 |
|---|------|------|
| 1 | paper_framing.md Core Insight | "depends on" → "may depend on — a hypothesis derived from two encoders and requiring broader validation" |
| 2 | paper_framing.md Dual-Pillar | "enabling practitioners to predict" → "offering a candidate heuristic...if validated on more encoders, could help" |
| 3 | discussion_v2.md §5.2 标题 | "Predictor of Strategy Effectiveness" → "An Exploratory Analysis" |
| 4 | discussion_v2.md §5.2 首句 | "reveals...predicts" → "suggests a hypothesis...may predict" + 新增 exploratory disclaimer |
| 5 | discussion_v2.md §5.2 | "This explains" → "This is consistent with" |
| 6 | related_work_v1.md §2.3 | "show that...depends on" → "observe that...appears to depend on" |

### 建议修复（⚠️ 偏强）— 5 处

| # | 文件 | 修改 |
|---|------|------|
| 7 | paper_framing.md Story Spine | 添加 "[exploratory]" 标签 |
| 8 | paper_framing.md Headline | "provides mechanistic explanation" → "provides a candidate mechanistic explanation" |
| 9 | introduction_v2.md Para 3 | "reveals...mediates" → "suggests...may mediate" + "candidate mechanistic hypothesis" + "(an exploratory finding from two encoders; ...)" |
| 10 | experiments_v1.md §4.2 | "mediates" → "may mediate" |
| 11 | experiments_v1.md §4.4 | 新增 "Based on our two-encoder comparison, we hypothesize the following mechanism." |
| 12 | experiment_setup_v1.md §4.2 | "reveals how" → "may reveal how" |
| 13 | discussion_v2.md §5.4 | "predicts" → "appears to correlate with" |
| 14 | paper_framing.md Core Insight | "explains" → "if confirmed, could help explain" |

所有修改文件末尾均已添加 `&lt;!-- Claim 2 wording fix: 2026-05-15 -->`。Claim 1 措辞未改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ed9e743-b8d9-49fe-b1df-bab4398b81f3",
  "isSidechain": false,
  "requestId": "req_011Cb3YDJUAbXsJYQrVBouSF",
  "type": "assistant",
  "uuid": "79b33946-6270-4a2b-a929-4567283385c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VujVaZZezNig2boEW2NU6n",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 71977,
      "output_tokens": 659,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3356,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 659,
          "cache_read_input_tokens": 71977,
          "cache_creation_input_tokens": 3356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3356
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

_source line 115_

```json
{
  "type": "last-prompt",
  "leafUuid": "79b33946-6270-4a2b-a929-4567283385c1",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---

### Runtime record

_source line 116_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix Claim 2 overly strong wording in paper drafts",
  "sessionId": "03270674-780b-45a5-9dcf-f4a6c86d5bde"
}
```

---
