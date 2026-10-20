# Research conversation: <project_context> # 项目: causal_annot_error_attrib ## 运行环境 - 服务器名: home-1x5090 - SSH 账户: sonny（调用 ssh_execute / submit_tr

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/f4e2217a-b32c-4a8a-a616-c19348792700.jsonl`
- **Structured JSON:** [`87ebb0b40d716ba43d8b.json`](../../sessions/87/87ebb0b40d716ba43d8b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T09:29:13.331Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T09:29:13.331Z",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "content": "&lt;project_context>\n# 项目: causal_annot_error_attrib\n\n## 运行环境\n- 服务器名: home-1x5090\n- SSH 账户: sonny（调用 ssh_execute / submit_training_job 时传入 account=\"sonny\"）\n- SSH 连接命令: ssh implicit5638.xyfu.me  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /home/sonny/causal_annot_error_attrib\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：搜索公开可用的 protest/political event 多分类标注数据集\n\n本项目需要一个 K≥3 的多分类文本分类数据集用于实证验证。之前候选 ACLED 因 ToS 禁止 ML 用途被排除，GLOCON Gold 需邮件申请。Director 要求搜索完全公开可用的替代。\n\n### 按优先级搜索以下数据集\n\n1. **POLDEM Protest Event Dataset** — 搜索其公开可用性、类别数、样本量、是否有 gold labels\n2. **Mass Mobilization Project (MMD)** — 搜索公开可用性、事件类型分类（K≥3?）、标注质量\n3. **其他公开 protest/political event 多分类数据集**，关键词搜索：\n   - \"protest event dataset NLP\" OR \"political event classification dataset\"\n   - \"contentious politics dataset annotation\"\n   - \"event type classification benchmark\"\n   - 也搜一下 Papers with Code 上的相关 benchmark\n\n### 要求\n- K ≥ 3（多分类，核心需求）\n- 有 gold-standard human labels（不是弱监督/远程监督）\n- 完全公开可下载（不需要审批/申请）\n- 英文或多语言\n- 样本量 ≥ 1000\n\n### 对每个找到的数据集报告\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```\n\n### 注意\n- 必须用 WebSearch 实际搜索确认，不要凭记忆\n- 如果都不满足要求，也如实报告，并建议是否应该回到 GLOCON 申请或换任务类型（如 emotion detection K=6, intent classification K≥4 等）"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T09:29:13.335Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T09:29:13.335Z",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

## Round 1

20 recorded events

### User

_source line 3 · 2026-05-20T09:29:13.383Z_

&lt;project_context>
# 项目: causal_annot_error_attrib

## 运行环境
- 服务器名: home-1x5090
- SSH 账户: sonny（调用 ssh_execute / submit_training_job 时传入 account="sonny"）
- SSH 连接命令: ssh implicit5638.xyfu.me  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /home/sonny/causal_annot_error_attrib


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：搜索公开可用的 protest/political event 多分类标注数据集

本项目需要一个 K≥3 的多分类文本分类数据集用于实证验证。之前候选 ACLED 因 ToS 禁止 ML 用途被排除，GLOCON Gold 需邮件申请。Director 要求搜索完全公开可用的替代。

### 按优先级搜索以下数据集

1. **POLDEM Protest Event Dataset** — 搜索其公开可用性、类别数、样本量、是否有 gold labels
2. **Mass Mobilization Project (MMD)** — 搜索公开可用性、事件类型分类（K≥3?）、标注质量
3. **其他公开 protest/political event 多分类数据集**，关键词搜索：
   - "protest event dataset NLP" OR "political event classification dataset"
   - "contentious politics dataset annotation"
   - "event type classification benchmark"
   - 也搜一下 Papers with Code 上的相关 benchmark

### 要求
- K ≥ 3（多分类，核心需求）
- 有 gold-standard human labels（不是弱监督/远程监督）
- 完全公开可下载（不需要审批/申请）
- 英文或多语言
- 样本量 ≥ 1000

### 对每个找到的数据集报告
```
数据集名称: xxx
类别数 K: x
类别列表: [...]
样本量: xxx
License: xxx
下载方式: xxx (具体 URL 或命令)
Gold-standard human labels: 是/否 (标注方式说明)
引用论文: xxx
备注: xxx
```

### 注意
- 必须用 WebSearch 实际搜索确认，不要凭记忆
- 如果都不满足要求，也如实报告，并建议是否应该回到 GLOCON 申请或换任务类型（如 emotion detection K=6, intent classification K≥4 等）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4c5374c5-7414-4221-88b9-803a1684c317",
  "type": "user",
  "uuid": "0c1067b6-1b20-4a5a-9dcb-8a7918305d41",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T09:29:13.382Z_

```json
{
  "parentUuid": "0c1067b6-1b20-4a5a-9dcb-8a7918305d41",
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
  "uuid": "73037283-bfa3-498c-8a79-1697e38680b9",
  "timestamp": "2026-05-20T09:29:13.382Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T09:29:13.382Z_

```json
{
  "parentUuid": "73037283-bfa3-498c-8a79-1697e38680b9",
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
  "uuid": "e39f4d30-32d8-460e-8587-ae4512074a92",
  "timestamp": "2026-05-20T09:29:13.382Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T09:29:13.382Z_

```json
{
  "parentUuid": "e39f4d30-32d8-460e-8587-ae4512074a92",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cb5203a3-0812-44a3-855f-55f9c8857cb4",
  "timestamp": "2026-05-20T09:29:13.382Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
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
  "aiTitle": "Search for public protest event classification datasets",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Assistant

_source line 8 · 2026-05-20T09:29:15.975Z_

I'll search for publicly available protest/political event multi-class annotation datasets in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb5203a3-0812-44a3-855f-55f9c8857cb4",
  "isSidechain": false,
  "requestId": "req_011CbDau2j1Z3cW3MCPuyaix",
  "type": "assistant",
  "uuid": "c7b8cfbb-7f8c-4d0d-84d1-99dd68ec2f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsUWX2atVeW8YWaRLaW2WJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11812,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1071,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1071,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11812
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

_source line 9 · 2026-05-20T09:29:20.131Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Cgb3VqR4Wn9RangSRTpyE5`</summary>

````json
{
  "description": "Search POLDEM dataset",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for the \"POLDEM Protest Event Dataset\" and report on its public availability, number of categories, sample size, and whether it has gold-standard human labels.\n\nSpecifically search for:\n1. \"POLDEM protest event dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories (K≥3?)\n4. Sample size\n5. License\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7b8cfbb-7f8c-4d0d-84d1-99dd68ec2f7d",
  "isSidechain": false,
  "requestId": "req_011CbDau2j1Z3cW3MCPuyaix",
  "type": "assistant",
  "uuid": "9ab89efb-c2f6-4f2d-9842-4b914e3b58bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsUWX2atVeW8YWaRLaW2WJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11812,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1071,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1071,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11812
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

_source line 10 · 2026-05-20T09:29:23.430Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RKjDE1P2EHBH2piAJtV2ws`</summary>

````json
{
  "description": "Search MMD dataset",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for the \"Mass Mobilization Project\" (also known as MMD or Mass Mobilization Data) and report on its public availability for NLP/ML use.\n\nSpecifically search for:\n1. \"Mass Mobilization Project dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories — does it have K≥3 classification categories?\n4. Sample size\n5. License and terms of use — is it allowed for ML/NLP research?\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ab89efb-c2f6-4f2d-9842-4b914e3b58bc",
  "isSidechain": false,
  "requestId": "req_011CbDau2j1Z3cW3MCPuyaix",
  "type": "assistant",
  "uuid": "b5f66ded-cf40-4533-a59f-cbea94c2fbc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsUWX2atVeW8YWaRLaW2WJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11812,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1071,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1071,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11812
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

_source line 11 · 2026-05-20T09:29:30.645Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0192Rf5hZwdGc442eWRxtvrU`</summary>

````json
{
  "description": "Search protest NLP datasets",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for publicly available protest/political event multi-class text classification datasets suitable for NLP research. I need datasets with K≥3 categories, gold-standard human labels, fully public download (no approval needed), English or multilingual, and sample size ≥1000.\n\nUse WebSearch with these queries (try at least 3-4 of them):\n1. \"protest event dataset NLP\" OR \"political event classification dataset\"\n2. \"contentious politics dataset annotation NLP\"\n3. \"event type classification benchmark\" protest\n4. Search Papers with Code for protest event or political event benchmarks\n5. \"protest news classification dataset\" github\n6. \"political event coding dataset\" public download\n\nFor each dataset found, report:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```\n\nIf you find datasets from shared tasks (e.g., CLEF, SemEval) related to protest event detection, include those too. Also look for:\n- Indian Protest Event datasets\n- SPEED (Social, Political and Economic Event Database)\n- Any HuggingFace datasets related to protest classification\n- ProtestNews shared task datasets (CLEF)\n\nBe thorough — search multiple queries and report ALL candidates found."
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f66ded-cf40-4533-a59f-cbea94c2fbc7",
  "isSidechain": false,
  "requestId": "req_011CbDau2j1Z3cW3MCPuyaix",
  "type": "assistant",
  "uuid": "a1fdcd79-ca93-47d1-9a78-1693517c2624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsUWX2atVeW8YWaRLaW2WJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11812,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1071,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1071,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11812
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

_source line 12 · 2026-05-20T09:31:51.935Z_

<details><summary>↩ Tool result · `toolu_01RKjDE1P2EHBH2piAJtV2ws`</summary>

````text
Based on comprehensive web searches, here is the report:

```
数据集名称: Mass Mobilization Data Project (MMD / MMP)
         作者: David H. Clark (Binghamton University) & Patrick M. Regan (University of Notre Dame)

类别数 K: 
  - 抗议者诉求 (protester demand): 7 类
  - 政府响应 (government response): 7 类

类别列表:
  Protester demands: [labor/wages, land, police brutality, political process, prices/taxes, removal of politician, social restrictions]
  Government responses: [accommodation, arrests, beatings, crowd dispersal, ignore, killings, shootings]
  注意：每个事件可以同时有多个 demand 和多个 response（multi-label）

样本量: ~17,000+ 事件（162 个国家，1990–2020），每条记录对应一次 50 人以上的抗议事件

License: Harvard Dataverse 默认 CC0 Public Domain Dedication（该数据集未见特殊限制说明），可用于学术/ML 研究

下载方式: 
  - Harvard Dataverse: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL
  - 官网: https://massmobilization.github.io/
  - data.world 镜像: https://data.world/government/mass-mobilization-protest-data
  - 无需申请/审批，直接下载

Gold-standard human labels: 是
  标注方式：人工编码员从 Lexis-Nexis 检索新闻报道（主要来源为 NYT、Washington Post、Christian Science Monitor、Times of London），
  按 codebook 标准对每起抗议事件的诉求类型、政府响应、规模、地点等进行手工编码。

引用论文: 
  - 数据集引用: Clark, David H.; Regan, Patrick M., 2016, "Mass Mobilization Protest Data", 
    https://doi.org/10.7910/DVN/HTTWYL, Harvard Dataverse
  - 相关分析论文: Klein, Graig R. and Patrick M. Regan. 2018. "Dynamics of Political Protests." 
    International Organization 72(2): 485-521.

备注:
  1. 该数据集是结构化事件数据（tabular），不含原始新闻文本。变量为编码后的分类标签（demand/response 为 0/1 二值列）、
     数值（protest size）和元数据（country, date, location）。如果用于 NLP 文本分类任务，
     需要自行匹配/获取原始新闻文本——数据集本身不提供 article text。
  2. Demand 和 response 都是 multi-label 设定（K=7 但非互斥），不是单标签 K 分类。
     作为 K>=3 的分类任务可行，但需注意 multi-label 性质。
  3. 另有 Mass Mobilization in Autocracies Database (MMAD, mmadatabase.org) 是独立扩展版，
     覆盖独裁国家，使用 AP/AFP/BBC Monitoring + ML 预筛选 + 人工编码，与 Clark/Regan 的 MMD 是不同数据集。
```

agentId: a8e25cafc895a96c2 (use SendMessage with to: 'a8e25cafc895a96c2' to continue this agent)
&lt;usage>total_tokens: 33265
tool_uses: 19
duration_ms: 148502&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "b5f66ded-cf40-4533-a59f-cbea94c2fbc7",
  "isSidechain": false,
  "promptId": "4c5374c5-7414-4221-88b9-803a1684c317",
  "type": "user",
  "uuid": "2f77a9a4-7eac-4732-98cf-df58d69cc67f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the \"Mass Mobilization Project\" (also known as MMD or Mass Mobilization Data) and report on its public availability for NLP/ML use.\n\nSpecifically search for:\n1. \"Mass Mobilization Project dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories — does it have K≥3 classification categories?\n4. Sample size\n5. License and terms of use — is it allowed for ML/NLP research?\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```",
    "agentId": "a8e25cafc895a96c2",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on comprehensive web searches, here is the report:\n\n```\n数据集名称: Mass Mobilization Data Project (MMD / MMP)\n         作者: David H. Clark (Binghamton University) & Patrick M. Regan (University of Notre Dame)\n\n类别数 K: \n  - 抗议者诉求 (protester demand): 7 类\n  - 政府响应 (government response): 7 类\n\n类别列表:\n  Protester demands: [labor/wages, land, police brutality, political process, prices/taxes, removal of politician, social restrictions]\n  Government responses: [accommodation, arrests, beatings, crowd dispersal, ignore, killings, shootings]\n  注意：每个事件可以同时有多个 demand 和多个 response（multi-label）\n\n样本量: ~17,000+ 事件（162 个国家，1990–2020），每条记录对应一次 50 人以上的抗议事件\n\nLicense: Harvard Dataverse 默认 CC0 Public Domain Dedication（该数据集未见特殊限制说明），可用于学术/ML 研究\n\n下载方式: \n  - Harvard Dataverse: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL\n  - 官网: https://massmobilization.github.io/\n  - data.world 镜像: https://data.world/government/mass-mobilization-protest-data\n  - 无需申请/审批，直接下载\n\nGold-standard human labels: 是\n  标注方式：人工编码员从 Lexis-Nexis 检索新闻报道（主要来源为 NYT、Washington Post、Christian Science Monitor、Times of London），\n  按 codebook 标准对每起抗议事件的诉求类型、政府响应、规模、地点等进行手工编码。\n\n引用论文: \n  - 数据集引用: Clark, David H.; Regan, Patrick M., 2016, \"Mass Mobilization Protest Data\", \n    https://doi.org/10.7910/DVN/HTTWYL, Harvard Dataverse\n  - 相关分析论文: Klein, Graig R. and Patrick M. Regan. 2018. \"Dynamics of Political Protests.\" \n    International Organization 72(2): 485-521.\n\n备注:\n  1. 该数据集是结构化事件数据（tabular），不含原始新闻文本。变量为编码后的分类标签（demand/response 为 0/1 二值列）、\n     数值（protest size）和元数据（country, date, location）。如果用于 NLP 文本分类任务，\n     需要自行匹配/获取原始新闻文本——数据集本身不提供 article text。\n  2. Demand 和 response 都是 multi-label 设定（K=7 但非互斥），不是单标签 K 分类。\n     作为 K>=3 的分类任务可行，但需注意 multi-label 性质。\n  3. 另有 Mass Mobilization in Autocracies Database (MMAD, mmadatabase.org) 是独立扩展版，\n     覆盖独裁国家，使用 AP/AFP/BBC Monitoring + ML 预筛选 + 人工编码，与 Clark/Regan 的 MMD 是不同数据集。\n```"
      }
    ],
    "totalDurationMs": 148502,
    "totalTokens": 33265,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 31271,
      "output_tokens": 919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 919,
          "cache_read_input_tokens": 31271,
          "cache_creation_input_tokens": 1074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1074,
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
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "b5f66ded-cf40-4533-a59f-cbea94c2fbc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 13 · 2026-05-20T09:33:39.168Z_

<details><summary>↩ Tool result · `toolu_01Cgb3VqR4Wn9RangSRTpyE5`</summary>

````text
Now I have all the information needed. Here is the report:

---

```
数据集名称: PolDem – Protest Dataset 30 European Countries (poldem-protest_30), Version 1
类别数 K: 
  - action_form (抗议形式): 6 类
  - issue (议题): 9 实质类 + 2 缺失/不知道类 = 11 列 (binary multi-label)
类别列表:
  action_form:
    1. demonstrations (13,327 events, 43.2%)
    2. violent protest (6,224, 20.2%)
    3. strikes (5,176, 16.8%)
    4. confrontations (2,594, 8.4%)
    5. petitions, symbolic actions (2,447, 7.9%)
    6. other protest (1,080, 3.5%)
  issue (multi-label binary columns):
    1. issue_econ_private — 企业/雇主相关经济议题 (12.2%)
    2. issue_econ_public — 公共机构相关经济议题 (30.0%)
    3. issue_cult_lib — 文化自由主义 (和平/女权/LGBTQ/反种族主义/移民权利) (17.0%)
    4. issue_environment — 环境/能源/基础设施 (6.6%)
    5. issue_political — 政治议题 (腐败/选举改革/代表权) (15.2%)
    6. issue_regional — 地区主义/分离主义 (7.2%)
    7. issue_cult_cons — 文化保守主义 (2.9%)
    8. issue_xeno — 仇外/右翼极端主义/反移民 (5.9%)
    9. issue_other — 其他 (10.8%)
    10. issue_dontknow (0.1%)
    11. issue_missing (4.2%)
样本量: 30,852 行 (对应约 33,655 coded events，论文原文数字；CSV 去重后 30,852 条记录)
License: 未在网站明确标注。但方法论论文 (Lorenzini et al., 2022) 以 CC BY 4.0 发表。数据集本身在 poldem.eui.eu 上无登录即可直接下载，无明确 license 声明，页脚标注 "© EUI & WZB. All rights reserved."
下载方式: 免费直接下载，无需注册/登录/申请
  - CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv (约 8.5 MB)
  - Stata: https://poldem.eui.eu/downloads/pea/poldem-protest_30.dta
  - Codebook: https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf
  - Documentation: https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf
  - 下载页面: https://poldem.eui.eu/download/protest-events/
Gold-standard human labels: 部分是，质量中等
  - 标注方式: 半自动流程 (semi-automated NLP pipeline)。先用关键词检索 520 万新闻文档，经去重/过滤/分类器筛选后，由 35 名研究生人工编码 45,680 篇文档（耗时 642 个工作日）
  - Intercoder reliability: 事件识别 F1 = 0.60 (SD 0.06)；议题 Cohen's κ = 0.53 (SD 0.13)；行动者 κ = 0.57；参与人数 κ = 0.45
  - 作者明确指出任务对人类编码者来说也"困难"，标注一致性属于 "fair to good"，并非高一致性 gold standard
引用论文:
  - 数据集: Kriesi, H., Wüest, B., Lorenzini, J., Makarov, P., Enggist, M., Rothenhäusler, K., Kurer, T., Häusermann, S., Wangen, P., Altiparmakis, A., Borbáth, E., Bremer, B., Gessler, T., Hunger, S., Hutter, S., Schulte-Cloos, J., & Wang, C. (2020). PolDem – Protest Dataset 30 European Countries, Version 1.
  - 方法论文: Lorenzini, J., Kriesi, H., Makarov, P., & Wüest, B. (2022). Protest Event Analysis: Developing a Semiautomated NLP Approach. American Behavioral Scientist, 66(5), 555–577. https://doi.org/10.1177/00027642211021650
备注:
  - 覆盖 30 个欧洲国家，2000-2015 年
  - issue 列是 multi-label (一个事件可同时标记多个议题)，不是单标签分类
  - action_form 是单标签分类，K=6
  - 数据源为 10 家英文通讯社的新闻稿 (Reuters, AFP, DPA 等)
  - 另有两个子集: poldem-protest_6 (6国, 1975-2011) 和 poldem-protest_eu (6国EU议题, 1995-2010)
  - 如果要做 annotation error attribution 实验，action_form 是 K=6 的单标签分类任务，比较适合；issue 是 multi-label 二值标注，intercoder κ 仅 0.53，噪声较大
```

Sources:
- [PolDem Observatory Homepage](https://poldem.eui.eu/)
- [Protest Events Download Page](https://poldem.eui.eu/download/protest-events/)
- [PolDem-Protest 30 Codebook (PDF)](https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf)
- [PEA Documentation v1 (PDF)](https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf)
- [Lorenzini et al. (2022) - SAGE Journals](https://journals.sagepub.com/doi/10.1177/00027642211021650)
- [PolDem Data Overview - EUI](https://poldem.eui.eu/data-overview/)
- [VU Amsterdam Dataset Page](https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries)
- [Discuss-Data Repository](https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/)
- [WZB Berlin - PolDem Project](https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa)

agentId: aaa88ae80b764645d (use SendMessage with to: 'aaa88ae80b764645d' to continue this agent)
&lt;usage>total_tokens: 39758
tool_uses: 31
duration_ms: 259031&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "9ab89efb-c2f6-4f2d-9842-4b914e3b58bc",
  "isSidechain": false,
  "promptId": "4c5374c5-7414-4221-88b9-803a1684c317",
  "type": "user",
  "uuid": "886d432b-417b-46e8-8932-ecdce36099ff",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the \"POLDEM Protest Event Dataset\" and report on its public availability, number of categories, sample size, and whether it has gold-standard human labels.\n\nSpecifically search for:\n1. \"POLDEM protest event dataset\" — what it is, where to download\n2. Whether it's freely downloadable without application/approval\n3. Number of event type categories (K≥3?)\n4. Sample size\n5. License\n6. Citation paper\n\nUse WebSearch to actually verify — don't rely on memory. Try multiple search queries if needed.\n\nReport in this format:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```",
    "agentId": "aaa88ae80b764645d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here is the report:\n\n---\n\n```\n数据集名称: PolDem – Protest Dataset 30 European Countries (poldem-protest_30), Version 1\n类别数 K: \n  - action_form (抗议形式): 6 类\n  - issue (议题): 9 实质类 + 2 缺失/不知道类 = 11 列 (binary multi-label)\n类别列表:\n  action_form:\n    1. demonstrations (13,327 events, 43.2%)\n    2. violent protest (6,224, 20.2%)\n    3. strikes (5,176, 16.8%)\n    4. confrontations (2,594, 8.4%)\n    5. petitions, symbolic actions (2,447, 7.9%)\n    6. other protest (1,080, 3.5%)\n  issue (multi-label binary columns):\n    1. issue_econ_private — 企业/雇主相关经济议题 (12.2%)\n    2. issue_econ_public — 公共机构相关经济议题 (30.0%)\n    3. issue_cult_lib — 文化自由主义 (和平/女权/LGBTQ/反种族主义/移民权利) (17.0%)\n    4. issue_environment — 环境/能源/基础设施 (6.6%)\n    5. issue_political — 政治议题 (腐败/选举改革/代表权) (15.2%)\n    6. issue_regional — 地区主义/分离主义 (7.2%)\n    7. issue_cult_cons — 文化保守主义 (2.9%)\n    8. issue_xeno — 仇外/右翼极端主义/反移民 (5.9%)\n    9. issue_other — 其他 (10.8%)\n    10. issue_dontknow (0.1%)\n    11. issue_missing (4.2%)\n样本量: 30,852 行 (对应约 33,655 coded events，论文原文数字；CSV 去重后 30,852 条记录)\nLicense: 未在网站明确标注。但方法论论文 (Lorenzini et al., 2022) 以 CC BY 4.0 发表。数据集本身在 poldem.eui.eu 上无登录即可直接下载，无明确 license 声明，页脚标注 \"© EUI & WZB. All rights reserved.\"\n下载方式: 免费直接下载，无需注册/登录/申请\n  - CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv (约 8.5 MB)\n  - Stata: https://poldem.eui.eu/downloads/pea/poldem-protest_30.dta\n  - Codebook: https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf\n  - Documentation: https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf\n  - 下载页面: https://poldem.eui.eu/download/protest-events/\nGold-standard human labels: 部分是，质量中等\n  - 标注方式: 半自动流程 (semi-automated NLP pipeline)。先用关键词检索 520 万新闻文档，经去重/过滤/分类器筛选后，由 35 名研究生人工编码 45,680 篇文档（耗时 642 个工作日）\n  - Intercoder reliability: 事件识别 F1 = 0.60 (SD 0.06)；议题 Cohen's κ = 0.53 (SD 0.13)；行动者 κ = 0.57；参与人数 κ = 0.45\n  - 作者明确指出任务对人类编码者来说也\"困难\"，标注一致性属于 \"fair to good\"，并非高一致性 gold standard\n引用论文:\n  - 数据集: Kriesi, H., Wüest, B., Lorenzini, J., Makarov, P., Enggist, M., Rothenhäusler, K., Kurer, T., Häusermann, S., Wangen, P., Altiparmakis, A., Borbáth, E., Bremer, B., Gessler, T., Hunger, S., Hutter, S., Schulte-Cloos, J., & Wang, C. (2020). PolDem – Protest Dataset 30 European Countries, Version 1.\n  - 方法论文: Lorenzini, J., Kriesi, H., Makarov, P., & Wüest, B. (2022). Protest Event Analysis: Developing a Semiautomated NLP Approach. American Behavioral Scientist, 66(5), 555–577. https://doi.org/10.1177/00027642211021650\n备注:\n  - 覆盖 30 个欧洲国家，2000-2015 年\n  - issue 列是 multi-label (一个事件可同时标记多个议题)，不是单标签分类\n  - action_form 是单标签分类，K=6\n  - 数据源为 10 家英文通讯社的新闻稿 (Reuters, AFP, DPA 等)\n  - 另有两个子集: poldem-protest_6 (6国, 1975-2011) 和 poldem-protest_eu (6国EU议题, 1995-2010)\n  - 如果要做 annotation error attribution 实验，action_form 是 K=6 的单标签分类任务，比较适合；issue 是 multi-label 二值标注，intercoder κ 仅 0.53，噪声较大\n```\n\nSources:\n- [PolDem Observatory Homepage](https://poldem.eui.eu/)\n- [Protest Events Download Page](https://poldem.eui.eu/download/protest-events/)\n- [PolDem-Protest 30 Codebook (PDF)](https://poldem.eui.eu/downloads/pea/poldem-protest_30_codebook.pdf)\n- [PEA Documentation v1 (PDF)](https://poldem.eui.eu/downloads/pea/PEA_documentation_v1.pdf)\n- [Lorenzini et al. (2022) - SAGE Journals](https://journals.sagepub.com/doi/10.1177/00027642211021650)\n- [PolDem Data Overview - EUI](https://poldem.eui.eu/data-overview/)\n- [VU Amsterdam Dataset Page](https://research.vu.nl/en/datasets/poldem-protest-dataset-30-european-countries)\n- [Discuss-Data Repository](https://discuss-data.net/dataset/c7e7af8f-fa6f-46d3-8ae5-41a4aad6e4b9/)\n- [WZB Berlin - PolDem Project](https://www.wzb.eu/en/research/dynamics-of-political-systems/center-for-civil-society-research/projects/daten-portal-zu-politischen-konflikten-und-protest-in-europa)"
      }
    ],
    "totalDurationMs": 259031,
    "totalTokens": 39758,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 37318,
      "output_tokens": 1921,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1921,
          "cache_read_input_tokens": 37318,
          "cache_creation_input_tokens": 518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 518,
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
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 24
    }
  },
  "sourceToolAssistantUUID": "9ab89efb-c2f6-4f2d-9842-4b914e3b58bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "leafUuid": "886d432b-417b-46e8-8932-ecdce36099ff",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Search for public protest event classification datasets",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Tool result

_source line 16 · 2026-05-20T09:34:09.188Z_

<details><summary>↩ Tool result · `toolu_0192Rf5hZwdGc442eWRxtvrU`</summary>

````text
Now I have enough information to compile a thorough report. Here are my findings:

---

## Protest/Political Event Multi-Class Text Classification Datasets

### 1. CASE 2021 Task 2 -- Fine-Grained Socio-Political Event Classification

```
数据集名称: CASE 2021 Shared Task 2 (Fine-Grained Event Classification)
类别数 K: 25 (main task) + 3 zero-shot + 2 surprise = 30 total
类别列表: ACLED 25 sub-event types, including Armed Clash, Government Regains Territory, 
  Non-state Actor Overtakes Territory, Violent Demonstration, Peaceful Protest, 
  Protest with Intervention, Excessive Force Against Protesters, Mob Violence, 
  Chemical Weapon, Air/Drone Strike, Suicide Bomb, Shelling/Artillery/Missile Attack, 
  Remote Explosive/Landmine/IED, Grenade, Sexual Violence, Attack, Abduction/Forced 
  Disappearance, Agreement, Arrests, Change to Group Activity, Disrupted Weapons Use, 
  Headquarters or Base Established, Looting/Property Destruction, 
  Non-violent Transfer of Territory, Other
样本量: ~600K short event descriptions (from ACLED text snippets)
License: 学术用途（需通过 ACLED 获取原始数据）
下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task2 文件夹含测试集 TSV)；
  训练数据需从 ACLED https://acleddata.com/ 获取
Gold-standard human labels: 是 (ACLED 专业编码员标注)
引用论文: Haneczok et al. "Fine-grained Event Classification in News-like Text Snippets - 
  Shared Task 2, CASE 2021" (ACL Anthology 2021.case-1.23)
备注: 测试集含标签可直接下载；训练数据建议从 ACLED 导出工具获取。K=25 是核心类别，
  非常适合多分类研究。涵盖政治暴力、示威、战略发展三大类。
```

### 2. CASE 2021/2022 Task 1 -- Multilingual Protest News Detection

```
数据集名称: CASE Shared Task 1 (Multilingual Protest News Detection)
类别数 K: Subtask 1 为二分类 (protest-related / not)；Subtask 2 为句子级二分类
类别列表: [protest-related, not protest-related] (文档级)；[event sentence, non-event sentence] (句子级)
样本量: Subtask 2 句子分类约 26,208 sentences；文档级数据涵盖多语言
License: 公开（GitHub 直接下载）
下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task1 文件夹)
  CASE 2022: https://github.com/emerging-welfare/case-2022-multilingual-event
Gold-standard human labels: 是 (政治学家标注，inter-annotator adjudication)
引用论文: Hürriyetoğlu et al. "Multilingual Protest News Detection - Shared Task 1, CASE 2021"
  (ACL Anthology 2021.case-1.11)
备注: ⚠️ K=2（二分类），不满足 K≥3 的要求。但与 Task 2 同源数据，可作为辅助。
  语言覆盖：English, Spanish, Portuguese, Hindi, Mandarin, Turkish, Urdu。
```

### 3. GLOCON Gold Standard Corpus (Cross-Context News Corpus)

```
数据集名称: GLOCON Gold Standard Corpus / Cross-Context News Corpus for Protest Events
类别数 K: 多层标注——文档级 (protest/non-protest)、句子级、token 级 (event trigger + arguments)
类别列表: 文档级二分类 + token级事件类型（protest event triggers with typed arguments）
样本量: 621,290 events from 9,509,193 news documents (自动预测);
  Gold standard 部分规模较小（需确认具体数量）
License: 需申请访问
下载方式: https://github.com/emerging-welfare/glocongold (申请流程说明)
  Dashboard: https://glocon.ku.edu.tr/
Gold-standard human labels: 是 (两位政治学家标注 + supervisor adjudication + 
  semi-automatic error detection)
引用论文: Hürriyetoğlu et al. "Cross-Context News Corpus for Protest Event-Related 
  Knowledge Base Construction" Data Intelligence 2021
备注: 覆盖 India, China, South Africa 新闻源。Gold standard 部分需要通过 GitHub 申请，
  不是完全免费下载。大规模自动标注数据可通过 dashboard 获取。
```

### 4. GLOCON Database (Full)

```
数据集名称: GLOCON (Global Contentious Politics Database)
类别数 K: 多类（事件类型包括 demonstrations, rallies, strikes, clashes, political violence 等）
类别列表: [Demonstration, Rally, Strike, Clash, Political Violence, ...] (具体完整列表需查文档)
样本量: 621,290 events（来自 India, South Africa, Argentina, Brazil, Turkey）
License: 公开下载（需在网站注册）
下载方式: https://glocon.ku.edu.tr/ (Download section) 
  数据格式: JSONL (每个新闻源一个文件)
Gold-standard human labels: 部分是（gold corpus 人工标注），大部分为自动预测标签
引用论文: Duruşan & Hürriyetoğlu "GLOCON Database: Design Decisions and User Manual (v1.0)" 
  arXiv:2405.18613
备注: 数据量大但标签为自动预测，非全部 gold-standard。适合大规模实验，
  但需注意标签噪声。覆盖全球南方五国。
```

### 5. ACLED (Armed Conflict Location & Event Data)

```
数据集名称: ACLED (Armed Conflict Location & Event Data Project)
类别数 K: 6 event types / 25 sub-event types / 3 disorder types
类别列表: 
  Disorder types: [Political Violence, Demonstrations, Strategic Developments]
  Event types: [Battles, Explosions/Remote Violence, Violence Against Civilians, 
    Riots, Protests, Strategic Developments]
  Sub-event types (25): [Armed Clash, Government Regains Territory, Non-state Actor
    Overtakes Territory, Chemical Weapon, Air/Drone Strike, Suicide Bomb, 
    Shelling/Artillery/Missile Attack, Remote Explosive/Landmine/IED, Grenade, 
    Sexual Violence, Attack, Abduction/Forced Disappearance, Violent Demonstration, 
    Mob Violence, Peaceful Protest, Protest with Intervention, Excessive Force 
    Against Protesters, Agreement, Arrests, Change to Group Activity, 
    Disrupted Weapons Use, HQ/Base Established, Looting/Property Destruction, 
    Non-violent Transfer of Territory, Other]
样本量: >1.3 million events (截至 2022)，实时更新
License: 开放访问（注册免费账户即可下载），学术/非营利用途免费
下载方式: https://acleddata.com/conflict-data/download-data/ (Data Export Tool / API)
  也可通过 HDX: https://data.humdata.org/organization/acled
Gold-standard human labels: 是 (专业编码员按 codebook 标注)
引用论文: Raleigh et al. "Introducing ACLED: An Armed Conflict Location and Event 
  Dataset" Journal of Peace Research 2010
备注: ⭐ 最佳候选之一。K=6 (event types) 或 K=25 (sub-event types)，样本量巨大，
  专业人工标注，免费注册下载。每条记录包含事件文本描述 (notes 字段) 可用于 NLP。
  注意：这不是"原始新闻文本"数据集，而是编码后的结构化事件数据（含短文本摘要）。
```

### 6. CEHA (Conflict Events in the Horn of Africa)

```
数据集名称: CEHA (Conflict Events in the Horn of Africa)
类别数 K: 4 (event types) + 2 (relevance classification)
类别列表: [Tribal/Communal/Ethnic Conflict, Religious Conflict, 
  Socio-political Violence Against Women, Climate-Related Security Risks]
样本量: 500 event descriptions
License: 公开 (GitHub)
下载方式: https://github.com/dataminr-ai/CEHA
Gold-standard human labels: 是 (subject matter experts 标注)
引用论文: CEHA: A Dataset of Conflict Events in the Horn of Africa (COLING 2025)
备注: ⚠️ 样本量仅 500，不满足 ≥1000 的要求。K=4 满足要求。
  数据来源于 ACLED 和 GDELT。适合低资源场景研究。
```

### 7. SPEED (Social, Political and Economic Event Database)

```
数据集名称: SPEED (Social Political Economic Event Dataset)
类别数 K: 4 Tier-1 categories + 多个子类
类别列表: Tier-1: [Political Expression Events, Politically Motivated Attacks, 
  Disruptive State Acts, Political Power Reconfigurations]
样本量: 覆盖 Liberia, Philippines, Sierra Leone (1979-2008)，具体事件数未在搜索中确认
License: 公开下载
下载方式: https://databank.illinois.edu/datasets/IDB-7407320 
  官方: https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED
Gold-standard human labels: 是 (Cline Center 编码员标注)
引用论文: Cline Center for Advanced Social Research, UIUC
备注: 结构化事件数据（非原始新闻文本）。覆盖时间较早(1979-2008)。
  K=4 满足要求。需确认是否包含可用于 NLP 的文本字段。
```

### 8. PolDem Protest Event Dataset 30

```
数据集名称: PolDem-Protest Dataset 30
类别数 K: 多类（action forms / organizational types 等多维标注）
类别列表: Action forms (多类), 组织类型 (SMOs, initiatives, loose networks 等),
  事件关联类型等
样本量: 45,680 documents (30 European countries, 2000-2015)
License: 需确认（网站下载）
下载方式: https://poldem.eui.eu/ (Downloads section)
Gold-standard human labels: 是 (semi-automated coding of newswire reports + 人工验证)
引用论文: PolDem documentation (EUI)
备注: 覆盖 30 个欧洲国家。数据基于新闻通讯社报道。标注维度丰富，
  不仅仅是事件类型，还有参与组织、暴力程度等。需要去网站确认具体类别数和下载条件。
```

### 9. HumAID (Human-Annotated Disaster Incidents Data)

```
数据集名称: HumAID
类别数 K: 11
类别列表: [Caution and Advice, Displaced People and Evacuations, 
  Don't Know or Can't Judge, Infrastructure and Utility Damage, 
  Injured or Dead People, Missing or Found People, Not Humanitarian, 
  Other Relevant Information, Requests or Urgent Needs, Rescue/Volunteering/Donation, 
  Sympathy and Support]
样本量: ~77,000 manually annotated tweets from 19 disaster events (2016-2019)
License: CC-BY-NC (学术用途)
下载方式: https://crisisnlp.qcri.org/humaid_dataset.html
  HuggingFace: https://huggingface.co/datasets/QCRI/HumAID-event-type
Gold-standard human labels: 是 (人工标注)
引用论文: Alam et al. "HumAID: Human-Annotated Disaster Incidents Data from Twitter" 
  ICWSM 2021
备注: ⚠️ 这是灾难事件数据集，不是抗议事件数据集。但方法论和任务类型相似，
  可作为参考。K=11, 样本量充足，完全公开下载。
```

### 10. CrisisNLP / CrisisLexT26

```
数据集名称: CrisisLexT26 / CrisisLexT6
类别数 K: 7 (information types including NOT RELATED)
类别列表: [Affected Individuals, Infrastructure/Utilities, Donations/Volunteering, 
  Caution/Advice, Sympathy, Information Source, Not Related]
样本量: CrisisLexT26 ~28,000 tweets from 26 events; CrisisLexT6 ~60,000 tweets from 6 events
License: 公开
下载方式: https://crisisnlp.qcri.org/
Gold-standard human labels: 是 (crowdsourced annotation)
引用论文: Olteanu et al. "CrisisLex: A Lexicon for Collecting and Filtering 
  Microblogged Communications in Crises" ICWSM 2014
备注: ⚠️ 同样是灾难/危机事件，非专门抗议事件。但标注框架可参考。
```

### 11. MPEDS (Machine-learning Protest Event Data System)

```
数据集名称: MPEDS
类别数 K: 多类（protest form categories）
类别列表: 包含多种抗议形式分类（具体列表需查看 codebook）
样本量: 需确认（系统用于生成抗议事件数据）
License: 公开 (GitHub + Zenodo)
下载方式: https://github.com/MPEDS/mpeds (需 Git LFS)
  Zenodo: https://zenodo.org/records/886459
  Annotation Interface: https://github.com/MPEDS/mpeds-coder
Gold-standard human labels: 是 (系统辅助 + 人工验证)
引用论文: Hanna "MPEDS: Automating the Generation of Protest Event Data" (2017)
备注: 更多是一个工具/系统而非固定数据集。需要深入查看 repo 确认是否有现成标注数据。
```

### 12. Crowd Counting Consortium (CCC)

```
数据集名称: Crowd Counting Consortium U.S. Protest Event Data
类别数 K: 494 discrete descriptive tags (多标签)
类别列表: 494 个标签涵盖抗议类型、议题、参与者等
样本量: 42,347 protest events (US, Jan 2017 - Jan 2021); 138,826 English articles
License: 公开
下载方式: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6OPP7H
  GitHub: https://github.com/rexdouglass/crowd-counting-consortium
Gold-standard human labels: 是 (人工标注)
引用论文: Pressman & Chenoweth, Harvard Kennedy School
备注: ⭐ 多标签（494 tags），非多分类。数据量大，完全公开（Harvard Dataverse）。
  包含新闻文章 URL，但原始文本需自行爬取。结构化标签数据直接可用。
```

### 13. INDI-PROP (Indian Propaganda Dataset)

```
数据集名称: INDI-PROP
类别数 K: 3 (article-level bias) + 多类 (narrative frames)
类别列表: Article-level: [Pro-Government, Pro-Opposition, Neutral]
  + event-specific fine-grained narrative frames
样本量: 1,266 articles (CAA protest + Farmers' protest)
License: 需确认（arXiv 论文附数据）
下载方式: 需查看论文附录/GitHub（arXiv:2512.03582）
Gold-standard human labels: 是 (人工标注 + GPT-4o-mini 辅助)
引用论文: "Fine-grained Narrative Classification in Biased News Articles" (arXiv:2512.03582)
备注: 专注于印度抗议事件新闻的偏见与叙事分类。K=3 满足，样本量 1,266 满足 ≥1000。
  但不是"事件类型"分类，而是"叙事立场"分类。
```

---

## 总结推荐（满足全部筛选条件：K≥3, gold labels, public download, ≥1000 samples）

| 排名 | 数据集 | K | 样本量 | 最适合用途 |
|------|--------|---|--------|-----------|
| 1 | **ACLED** | 6/25 | >1.3M | 政治暴力+抗议事件多分类，文本字段可用于 NLP |
| 2 | **CASE 2021 Task 2** | 25 | ~600K snippets | 细粒度社会政治事件分类，NLP 共享任务标准 |
| 3 | **CCC (Harvard)** | 494 tags (多标签) | 42K events | 美国抗议事件多标签分类 |
| 4 | **PolDem-30** | 多类 | 45K docs | 欧洲 30 国抗议事件，多维标注 |
| 5 | **GLOCON** | 多类 | 621K events | 全球南方五国，大规模自动标签 |
| 6 | **INDI-PROP** | 3+ | 1,266 | 印度抗议事件叙事分类 |

**首选推荐**：ACLED (K=25 sub-event types) 和 CASE 2021 Task 2 是最贴合需求的数据集 -- 专门面向抗议/政治事件、多分类、gold-standard 人工标注、公开下载、样本量远超 1000。

Sources:
- [CASE 2021 Shared Task GitHub](https://github.com/emerging-welfare/case-2021-shared-task)
- [CASE 2022 Multilingual Event GitHub](https://github.com/emerging-welfare/case-2022-multilingual-event)
- [ACLED Data Download](https://acleddata.com/conflict-data/download-data/)
- [ACLED Codebook](https://acleddata.com/methodology/acled-codebook/)
- [GLOCON Database](https://glocon.ku.edu.tr/)
- [GLOCON Gold Standard GitHub](https://github.com/emerging-welfare/glocongold)
- [GLOCON Annotation Manuals (Zenodo)](https://zenodo.org/records/6540579)
- [CEHA GitHub (Dataminr)](https://github.com/dataminr-ai/CEHA)
- [SPEED Dataset (UIUC)](https://databank.illinois.edu/datasets/IDB-7407320)
- [Cline Center SPEED Project](https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED)
- [PolDem Protest Event Dataset](https://poldem.eui.eu/)
- [CCC Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6OPP7H)
- [CCC GitHub](https://github.com/rexdouglass/crowd-counting-consortium)
- [HumAID on HuggingFace](https://huggingface.co/datasets/QCRI/HumAID-event-type)
- [CrisisNLP](https://crisisnlp.qcri.org/)
- [MPEDS GitHub](https://github.com/MPEDS/mpeds)
- [MPEDS Zenodo](https://zenodo.org/records/886459)
- [Cross-Context News Corpus (MIT Press)](https://direct.mit.edu/dint/article/3/2/308/100736/Cross-Context-News-Corpus-for-Protest-Event)
- [CASE 2021 Task 2 Overview Paper](https://aclanthology.org/2021.case-1.23/)
- [INDI-PROP Paper](https://www.arxiv.org/pdf/2512.03582)
- [ACLED on HDX](https://data.humdata.org/organization/acled)

agentId: aa45e88c0b435afd8 (use SendMessage with to: 'aa45e88c0b435afd8' to continue this agent)
&lt;usage>total_tokens: 53511
tool_uses: 32
duration_ms: 278539&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "a1fdcd79-ca93-47d1-9a78-1693517c2624",
  "isSidechain": false,
  "promptId": "4c5374c5-7414-4221-88b9-803a1684c317",
  "type": "user",
  "uuid": "b21f7c90-b17c-41ee-8636-1e7c9c13910c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for publicly available protest/political event multi-class text classification datasets suitable for NLP research. I need datasets with K≥3 categories, gold-standard human labels, fully public download (no approval needed), English or multilingual, and sample size ≥1000.\n\nUse WebSearch with these queries (try at least 3-4 of them):\n1. \"protest event dataset NLP\" OR \"political event classification dataset\"\n2. \"contentious politics dataset annotation NLP\"\n3. \"event type classification benchmark\" protest\n4. Search Papers with Code for protest event or political event benchmarks\n5. \"protest news classification dataset\" github\n6. \"political event coding dataset\" public download\n\nFor each dataset found, report:\n```\n数据集名称: xxx\n类别数 K: x\n类别列表: [...]\n样本量: xxx\nLicense: xxx\n下载方式: xxx (具体 URL 或命令)\nGold-standard human labels: 是/否 (标注方式说明)\n引用论文: xxx\n备注: xxx\n```\n\nIf you find datasets from shared tasks (e.g., CLEF, SemEval) related to protest event detection, include those too. Also look for:\n- Indian Protest Event datasets\n- SPEED (Social, Political and Economic Event Database)\n- Any HuggingFace datasets related to protest classification\n- ProtestNews shared task datasets (CLEF)\n\nBe thorough — search multiple queries and report ALL candidates found.",
    "agentId": "aa45e88c0b435afd8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to compile a thorough report. Here are my findings:\n\n---\n\n## Protest/Political Event Multi-Class Text Classification Datasets\n\n### 1. CASE 2021 Task 2 -- Fine-Grained Socio-Political Event Classification\n\n```\n数据集名称: CASE 2021 Shared Task 2 (Fine-Grained Event Classification)\n类别数 K: 25 (main task) + 3 zero-shot + 2 surprise = 30 total\n类别列表: ACLED 25 sub-event types, including Armed Clash, Government Regains Territory, \n  Non-state Actor Overtakes Territory, Violent Demonstration, Peaceful Protest, \n  Protest with Intervention, Excessive Force Against Protesters, Mob Violence, \n  Chemical Weapon, Air/Drone Strike, Suicide Bomb, Shelling/Artillery/Missile Attack, \n  Remote Explosive/Landmine/IED, Grenade, Sexual Violence, Attack, Abduction/Forced \n  Disappearance, Agreement, Arrests, Change to Group Activity, Disrupted Weapons Use, \n  Headquarters or Base Established, Looting/Property Destruction, \n  Non-violent Transfer of Territory, Other\n样本量: ~600K short event descriptions (from ACLED text snippets)\nLicense: 学术用途（需通过 ACLED 获取原始数据）\n下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task2 文件夹含测试集 TSV)；\n  训练数据需从 ACLED https://acleddata.com/ 获取\nGold-standard human labels: 是 (ACLED 专业编码员标注)\n引用论文: Haneczok et al. \"Fine-grained Event Classification in News-like Text Snippets - \n  Shared Task 2, CASE 2021\" (ACL Anthology 2021.case-1.23)\n备注: 测试集含标签可直接下载；训练数据建议从 ACLED 导出工具获取。K=25 是核心类别，\n  非常适合多分类研究。涵盖政治暴力、示威、战略发展三大类。\n```\n\n### 2. CASE 2021/2022 Task 1 -- Multilingual Protest News Detection\n\n```\n数据集名称: CASE Shared Task 1 (Multilingual Protest News Detection)\n类别数 K: Subtask 1 为二分类 (protest-related / not)；Subtask 2 为句子级二分类\n类别列表: [protest-related, not protest-related] (文档级)；[event sentence, non-event sentence] (句子级)\n样本量: Subtask 2 句子分类约 26,208 sentences；文档级数据涵盖多语言\nLicense: 公开（GitHub 直接下载）\n下载方式: https://github.com/emerging-welfare/case-2021-shared-task (task1 文件夹)\n  CASE 2022: https://github.com/emerging-welfare/case-2022-multilingual-event\nGold-standard human labels: 是 (政治学家标注，inter-annotator adjudication)\n引用论文: Hürriyetoğlu et al. \"Multilingual Protest News Detection - Shared Task 1, CASE 2021\"\n  (ACL Anthology 2021.case-1.11)\n备注: ⚠️ K=2（二分类），不满足 K≥3 的要求。但与 Task 2 同源数据，可作为辅助。\n  语言覆盖：English, Spanish, Portuguese, Hindi, Mandarin, Turkish, Urdu。\n```\n\n### 3. GLOCON Gold Standard Corpus (Cross-Context News Corpus)\n\n```\n数据集名称: GLOCON Gold Standard Corpus / Cross-Context News Corpus for Protest Events\n类别数 K: 多层标注——文档级 (protest/non-protest)、句子级、token 级 (event trigger + arguments)\n类别列表: 文档级二分类 + token级事件类型（protest event triggers with typed arguments）\n样本量: 621,290 events from 9,509,193 news documents (自动预测);\n  Gold standard 部分规模较小（需确认具体数量）\nLicense: 需申请访问\n下载方式: https://github.com/emerging-welfare/glocongold (申请流程说明)\n  Dashboard: https://glocon.ku.edu.tr/\nGold-standard human labels: 是 (两位政治学家标注 + supervisor adjudication + \n  semi-automatic error detection)\n引用论文: Hürriyetoğlu et al. \"Cross-Context News Corpus for Protest Event-Related \n  Knowledge Base Construction\" Data Intelligence 2021\n备注: 覆盖 India, China, South Africa 新闻源。Gold standard 部分需要通过 GitHub 申请，\n  不是完全免费下载。大规模自动标注数据可通过 dashboard 获取。\n```\n\n### 4. GLOCON Database (Full)\n\n```\n数据集名称: GLOCON (Global Contentious Politics Database)\n类别数 K: 多类（事件类型包括 demonstrations, rallies, strikes, clashes, political violence 等）\n类别列表: [Demonstration, Rally, Strike, Clash, Political Violence, ...] (具体完整列表需查文档)\n样本量: 621,290 events（来自 India, South Africa, Argentina, Brazil, Turkey）\nLicense: 公开下载（需在网站注册）\n下载方式: https://glocon.ku.edu.tr/ (Download section) \n  数据格式: JSONL (每个新闻源一个文件)\nGold-standard human labels: 部分是（gold corpus 人工标注），大部分为自动预测标签\n引用论文: Duruşan & Hürriyetoğlu \"GLOCON Database: Design Decisions and User Manual (v1.0)\" \n  arXiv:2405.18613\n备注: 数据量大但标签为自动预测，非全部 gold-standard。适合大规模实验，\n  但需注意标签噪声。覆盖全球南方五国。\n```\n\n### 5. ACLED (Armed Conflict Location & Event Data)\n\n```\n数据集名称: ACLED (Armed Conflict Location & Event Data Project)\n类别数 K: 6 event types / 25 sub-event types / 3 disorder types\n类别列表: \n  Disorder types: [Political Violence, Demonstrations, Strategic Developments]\n  Event types: [Battles, Explosions/Remote Violence, Violence Against Civilians, \n    Riots, Protests, Strategic Developments]\n  Sub-event types (25): [Armed Clash, Government Regains Territory, Non-state Actor\n    Overtakes Territory, Chemical Weapon, Air/Drone Strike, Suicide Bomb, \n    Shelling/Artillery/Missile Attack, Remote Explosive/Landmine/IED, Grenade, \n    Sexual Violence, Attack, Abduction/Forced Disappearance, Violent Demonstration, \n    Mob Violence, Peaceful Protest, Protest with Intervention, Excessive Force \n    Against Protesters, Agreement, Arrests, Change to Group Activity, \n    Disrupted Weapons Use, HQ/Base Established, Looting/Property Destruction, \n    Non-violent Transfer of Territory, Other]\n样本量: >1.3 million events (截至 2022)，实时更新\nLicense: 开放访问（注册免费账户即可下载），学术/非营利用途免费\n下载方式: https://acleddata.com/conflict-data/download-data/ (Data Export Tool / API)\n  也可通过 HDX: https://data.humdata.org/organization/acled\nGold-standard human labels: 是 (专业编码员按 codebook 标注)\n引用论文: Raleigh et al. \"Introducing ACLED: An Armed Conflict Location and Event \n  Dataset\" Journal of Peace Research 2010\n备注: ⭐ 最佳候选之一。K=6 (event types) 或 K=25 (sub-event types)，样本量巨大，\n  专业人工标注，免费注册下载。每条记录包含事件文本描述 (notes 字段) 可用于 NLP。\n  注意：这不是\"原始新闻文本\"数据集，而是编码后的结构化事件数据（含短文本摘要）。\n```\n\n### 6. CEHA (Conflict Events in the Horn of Africa)\n\n```\n数据集名称: CEHA (Conflict Events in the Horn of Africa)\n类别数 K: 4 (event types) + 2 (relevance classification)\n类别列表: [Tribal/Communal/Ethnic Conflict, Religious Conflict, \n  Socio-political Violence Against Women, Climate-Related Security Risks]\n样本量: 500 event descriptions\nLicense: 公开 (GitHub)\n下载方式: https://github.com/dataminr-ai/CEHA\nGold-standard human labels: 是 (subject matter experts 标注)\n引用论文: CEHA: A Dataset of Conflict Events in the Horn of Africa (COLING 2025)\n备注: ⚠️ 样本量仅 500，不满足 ≥1000 的要求。K=4 满足要求。\n  数据来源于 ACLED 和 GDELT。适合低资源场景研究。\n```\n\n### 7. SPEED (Social, Political and Economic Event Database)\n\n```\n数据集名称: SPEED (Social Political Economic Event Dataset)\n类别数 K: 4 Tier-1 categories + 多个子类\n类别列表: Tier-1: [Political Expression Events, Politically Motivated Attacks, \n  Disruptive State Acts, Political Power Reconfigurations]\n样本量: 覆盖 Liberia, Philippines, Sierra Leone (1979-2008)，具体事件数未在搜索中确认\nLicense: 公开下载\n下载方式: https://databank.illinois.edu/datasets/IDB-7407320 \n  官方: https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED\nGold-standard human labels: 是 (Cline Center 编码员标注)\n引用论文: Cline Center for Advanced Social Research, UIUC\n备注: 结构化事件数据（非原始新闻文本）。覆盖时间较早(1979-2008)。\n  K=4 满足要求。需确认是否包含可用于 NLP 的文本字段。\n```\n\n### 8. PolDem Protest Event Dataset 30\n\n```\n数据集名称: PolDem-Protest Dataset 30\n类别数 K: 多类（action forms / organizational types 等多维标注）\n类别列表: Action forms (多类), 组织类型 (SMOs, initiatives, loose networks 等),\n  事件关联类型等\n样本量: 45,680 documents (30 European countries, 2000-2015)\nLicense: 需确认（网站下载）\n下载方式: https://poldem.eui.eu/ (Downloads section)\nGold-standard human labels: 是 (semi-automated coding of newswire reports + 人工验证)\n引用论文: PolDem documentation (EUI)\n备注: 覆盖 30 个欧洲国家。数据基于新闻通讯社报道。标注维度丰富，\n  不仅仅是事件类型，还有参与组织、暴力程度等。需要去网站确认具体类别数和下载条件。\n```\n\n### 9. HumAID (Human-Annotated Disaster Incidents Data)\n\n```\n数据集名称: HumAID\n类别数 K: 11\n类别列表: [Caution and Advice, Displaced People and Evacuations, \n  Don't Know or Can't Judge, Infrastructure and Utility Damage, \n  Injured or Dead People, Missing or Found People, Not Humanitarian, \n  Other Relevant Information, Requests or Urgent Needs, Rescue/Volunteering/Donation, \n  Sympathy and Support]\n样本量: ~77,000 manually annotated tweets from 19 disaster events (2016-2019)\nLicense: CC-BY-NC (学术用途)\n下载方式: https://crisisnlp.qcri.org/humaid_dataset.html\n  HuggingFace: https://huggingface.co/datasets/QCRI/HumAID-event-type\nGold-standard human labels: 是 (人工标注)\n引用论文: Alam et al. \"HumAID: Human-Annotated Disaster Incidents Data from Twitter\" \n  ICWSM 2021\n备注: ⚠️ 这是灾难事件数据集，不是抗议事件数据集。但方法论和任务类型相似，\n  可作为参考。K=11, 样本量充足，完全公开下载。\n```\n\n### 10. CrisisNLP / CrisisLexT26\n\n```\n数据集名称: CrisisLexT26 / CrisisLexT6\n类别数 K: 7 (information types including NOT RELATED)\n类别列表: [Affected Individuals, Infrastructure/Utilities, Donations/Volunteering, \n  Caution/Advice, Sympathy, Information Source, Not Related]\n样本量: CrisisLexT26 ~28,000 tweets from 26 events; CrisisLexT6 ~60,000 tweets from 6 events\nLicense: 公开\n下载方式: https://crisisnlp.qcri.org/\nGold-standard human labels: 是 (crowdsourced annotation)\n引用论文: Olteanu et al. \"CrisisLex: A Lexicon for Collecting and Filtering \n  Microblogged Communications in Crises\" ICWSM 2014\n备注: ⚠️ 同样是灾难/危机事件，非专门抗议事件。但标注框架可参考。\n```\n\n### 11. MPEDS (Machine-learning Protest Event Data System)\n\n```\n数据集名称: MPEDS\n类别数 K: 多类（protest form categories）\n类别列表: 包含多种抗议形式分类（具体列表需查看 codebook）\n样本量: 需确认（系统用于生成抗议事件数据）\nLicense: 公开 (GitHub + Zenodo)\n下载方式: https://github.com/MPEDS/mpeds (需 Git LFS)\n  Zenodo: https://zenodo.org/records/886459\n  Annotation Interface: https://github.com/MPEDS/mpeds-coder\nGold-standard human labels: 是 (系统辅助 + 人工验证)\n引用论文: Hanna \"MPEDS: Automating the Generation of Protest Event Data\" (2017)\n备注: 更多是一个工具/系统而非固定数据集。需要深入查看 repo 确认是否有现成标注数据。\n```\n\n### 12. Crowd Counting Consortium (CCC)\n\n```\n数据集名称: Crowd Counting Consortium U.S. Protest Event Data\n类别数 K: 494 discrete descriptive tags (多标签)\n类别列表: 494 个标签涵盖抗议类型、议题、参与者等\n样本量: 42,347 protest events (US, Jan 2017 - Jan 2021); 138,826 English articles\nLicense: 公开\n下载方式: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6OPP7H\n  GitHub: https://github.com/rexdouglass/crowd-counting-consortium\nGold-standard human labels: 是 (人工标注)\n引用论文: Pressman & Chenoweth, Harvard Kennedy School\n备注: ⭐ 多标签（494 tags），非多分类。数据量大，完全公开（Harvard Dataverse）。\n  包含新闻文章 URL，但原始文本需自行爬取。结构化标签数据直接可用。\n```\n\n### 13. INDI-PROP (Indian Propaganda Dataset)\n\n```\n数据集名称: INDI-PROP\n类别数 K: 3 (article-level bias) + 多类 (narrative frames)\n类别列表: Article-level: [Pro-Government, Pro-Opposition, Neutral]\n  + event-specific fine-grained narrative frames\n样本量: 1,266 articles (CAA protest + Farmers' protest)\nLicense: 需确认（arXiv 论文附数据）\n下载方式: 需查看论文附录/GitHub（arXiv:2512.03582）\nGold-standard human labels: 是 (人工标注 + GPT-4o-mini 辅助)\n引用论文: \"Fine-grained Narrative Classification in Biased News Articles\" (arXiv:2512.03582)\n备注: 专注于印度抗议事件新闻的偏见与叙事分类。K=3 满足，样本量 1,266 满足 ≥1000。\n  但不是\"事件类型\"分类，而是\"叙事立场\"分类。\n```\n\n---\n\n## 总结推荐（满足全部筛选条件：K≥3, gold labels, public download, ≥1000 samples）\n\n| 排名 | 数据集 | K | 样本量 | 最适合用途 |\n|------|--------|---|--------|-----------|\n| 1 | **ACLED** | 6/25 | >1.3M | 政治暴力+抗议事件多分类，文本字段可用于 NLP |\n| 2 | **CASE 2021 Task 2** | 25 | ~600K snippets | 细粒度社会政治事件分类，NLP 共享任务标准 |\n| 3 | **CCC (Harvard)** | 494 tags (多标签) | 42K events | 美国抗议事件多标签分类 |\n| 4 | **PolDem-30** | 多类 | 45K docs | 欧洲 30 国抗议事件，多维标注 |\n| 5 | **GLOCON** | 多类 | 621K events | 全球南方五国，大规模自动标签 |\n| 6 | **INDI-PROP** | 3+ | 1,266 | 印度抗议事件叙事分类 |\n\n**首选推荐**：ACLED (K=25 sub-event types) 和 CASE 2021 Task 2 是最贴合需求的数据集 -- 专门面向抗议/政治事件、多分类、gold-standard 人工标注、公开下载、样本量远超 1000。\n\nSources:\n- [CASE 2021 Shared Task GitHub](https://github.com/emerging-welfare/case-2021-shared-task)\n- [CASE 2022 Multilingual Event GitHub](https://github.com/emerging-welfare/case-2022-multilingual-event)\n- [ACLED Data Download](https://acleddata.com/conflict-data/download-data/)\n- [ACLED Codebook](https://acleddata.com/methodology/acled-codebook/)\n- [GLOCON Database](https://glocon.ku.edu.tr/)\n- [GLOCON Gold Standard GitHub](https://github.com/emerging-welfare/glocongold)\n- [GLOCON Annotation Manuals (Zenodo)](https://zenodo.org/records/6540579)\n- [CEHA GitHub (Dataminr)](https://github.com/dataminr-ai/CEHA)\n- [SPEED Dataset (UIUC)](https://databank.illinois.edu/datasets/IDB-7407320)\n- [Cline Center SPEED Project](https://clinecenter.illinois.edu/project/human-loop-event-data-projects/SPEED)\n- [PolDem Protest Event Dataset](https://poldem.eui.eu/)\n- [CCC Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6OPP7H)\n- [CCC GitHub](https://github.com/rexdouglass/crowd-counting-consortium)\n- [HumAID on HuggingFace](https://huggingface.co/datasets/QCRI/HumAID-event-type)\n- [CrisisNLP](https://crisisnlp.qcri.org/)\n- [MPEDS GitHub](https://github.com/MPEDS/mpeds)\n- [MPEDS Zenodo](https://zenodo.org/records/886459)\n- [Cross-Context News Corpus (MIT Press)](https://direct.mit.edu/dint/article/3/2/308/100736/Cross-Context-News-Corpus-for-Protest-Event)\n- [CASE 2021 Task 2 Overview Paper](https://aclanthology.org/2021.case-1.23/)\n- [INDI-PROP Paper](https://www.arxiv.org/pdf/2512.03582)\n- [ACLED on HDX](https://data.humdata.org/organization/acled)"
      }
    ],
    "totalDurationMs": 278539,
    "totalTokens": 53511,
    "totalToolUseCount": 32,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1894,
      "cache_read_input_tokens": 45893,
      "output_tokens": 5723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1894
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5723,
          "cache_read_input_tokens": 45893,
          "cache_creation_input_tokens": 1894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1894,
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
      "otherToolCount": 32
    }
  },
  "sourceToolAssistantUUID": "a1fdcd79-ca93-47d1-9a78-1693517c2624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "leafUuid": "b21f7c90-b17c-41ee-8636-1e7c9c13910c",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Search for public protest event classification datasets",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Assistant

_source line 19 · 2026-05-20T09:34:38.671Z_

<details><summary>Logged reasoning block</summary>

```text
Let me synthesize the results from all three agents. I need to carefully evaluate which datasets actually meet ALL the criteria:

1. K ≥ 3 (multi-class)
2. Gold-standard human labels
3. Fully public download (no approval needed)
4. English or multilingual
5. Sample size ≥ 1000

Key concern: The user explicitly mentioned ACLED was excluded due to ToS prohibiting ML use. So ACLED and CASE 2021 Task 2 (which uses ACLED data for training) are both problematic.


Now I'm examining the specific candidates more closely. POLDEM Protest Dataset 30 has six action categories with nearly 31,000 events and free access, but the gold labels come from semi-automated methods with moderate intercoder agreement, and the copyright notice raises licensing concerns. The Mass Mobilization Project offers seven categories for both protester demands and government responses across 17,000+ events on Harvard Dataverse, though I need to verify the full accessibility and labeling quality.

CASE 2021 Task 2 provides 25 sub-event types across 600K snippets but requires access to ACLED data for training, creating the same licensing barrier. The Crowd Counting Consortium has 42K events but uses 494 multi-label tags rather than discrete classes, and the text data isn't directly available. SPEED covers four categories with public access but appears to be structured data from an older period (1979-2008) without clear text fields. GLOCON requires an application to access.

Looking at other candidates, CEHA only has 500 samples which is too small, while MPEDS functions more as a tool than a dataset. INDI-PROP focuses on narrative bias rather than event classification, and though HumAID has 11 categories across 77K tweets with public access and gold labels, it covers disaster events rather than protest-specific ones. CrisisLexT26 similarly addresses crisis events with 7 categories and 28K tweets but again isn't protest-focused.

The strongest option remains PolDem-30, which offers six action form categories across roughly 30K events with free download and human-coded labels, though the annotation quality is moderate.

But I'm realizing a critical issue: for this annotation error attribution project, I actually need raw text paired with labels for NLP classification tasks. Most of these political event datasets are structured coded data extracted from newswires without the original text included. PolDem and MMD both fall into this trap—they're event metadata rather than text corpora. So I need to refocus on datasets that actually contain the source text alongside their labels, which narrows things down significantly.

Looking at what's viable, CASE 2021 Task 2 has text snippets with event type labels, though it depends on ACLED for training data which has licensing concerns—though the test set is publicly available on GitHub. PolDem-30 might have some text fields embedded in its CSV. If neither of these work out, I could pivot to crisis-related tweet datasets like HumAID or CrisisLexT26, or shift to entirely different classification domains like emotion or intent detection. Let me organize what I've found into a clear recommendation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b21f7c90-b17c-41ee-8636-1e7c9c13910c",
  "isSidechain": false,
  "requestId": "req_011CbDbGqCLFfMJRJksn4YFU",
  "type": "assistant",
  "uuid": "dd1fa13d-c03d-441e-9b13-40a4d0f9fe7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DwAeG5uacN2zHE6mvucBP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9932,
      "cache_read_input_tokens": 23653,
      "output_tokens": 2777,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2777,
          "cache_read_input_tokens": 23653,
          "cache_creation_input_tokens": 9932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9932
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

_source line 20 · 2026-05-20T09:35:07.471Z_

## 搜索结果汇总

**关键前提**：ACLED ToS 禁止 ML 用途，因此 ACLED 本身和依赖 ACLED 训练数据的 CASE 2021 Task 2 均排除。

---

### 符合条件的候选

#### 1. PolDem Protest Dataset 30
```
数据集名称: PolDem-Protest Dataset 30 (poldem-protest_30)
类别数 K: action_form = 6 (单标签); issue = 9 (多标签)
类别列表 (action_form): [demonstrations, violent protest, strikes, confrontations, 
  petitions/symbolic actions, other protest]
样本量: 30,852 events (30 European countries, 2000-2015)
License: 未明确标注，页脚 "© EUI & WZB. All rights reserved."
下载方式: 直接下载，无需注册
  CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv
Gold-standard human labels: 半自动流程 + 35名编码员人工标注
  intercoder: 事件识别 F1=0.60, 议题 κ=0.53
引用论文: Lorenzini et al. (2022) American Behavioral Scientist
备注: 
  ⚠️ 结构化事件数据，不含原始新闻全文（来源为通讯社 newswire，但 CSV 中可能只有编码字段）
  ⚠️ License 模糊，"All rights reserved" 有风险
  ✅ action_form K=6 单标签分类，标注质量中等，适合研究标注噪声
```

#### 2. Mass Mobilization Project (MMD)
```
数据集名称: Mass Mobilization Data Project
类别数 K: protester demand = 7 (多标签); government response = 7 (多标签)
类别列表 (demand): [labor/wages, land, police brutality, political process, 
  prices/taxes, removal of politician, social restrictions]
样本量: ~17,000 events (162 countries, 1990-2020)
License: Harvard Dataverse (CC0 Public Domain)
下载方式: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL
Gold-standard human labels: 是，人工编码员从 Lexis-Nexis 新闻编码
引用论文: Clark & Regan (2016), Harvard Dataverse
备注:
  ⚠️ 结构化事件数据，不含原始新闻文本
  ⚠️ Demand/response 为多标签 (0/1 binary columns)，非单标签多分类
  ✅ License 好 (CC0)，完全公开
```

#### 3. SPEED (Social Political Economic Event Database)
```
数据集名称: SPEED
类别数 K: 4 Tier-1 categories
类别列表: [Political Expression Events, Politically Motivated Attacks, 
  Disruptive State Acts, Political Power Reconfigurations]
样本量: 覆盖 3 国 (1979-2008)，具体数量待确认
License: 公开
下载方式: https://databank.illinois.edu/datasets/IDB-7407320
Gold-standard human labels: 是 (Cline Center 编码员)
引用论文: Cline Center for Advanced Social Research, UIUC
备注: ⚠️ 同样是结构化事件数据，非 NLP 文本分类格式
```

---

### 不满足条件的排除项

| 数据集 | 排除原因 |
|--------|---------|
| ACLED / CASE 2021 Task 2 | ToS 禁止 ML 用途（训练数据来自 ACLED） |
| GLOCON Gold | 需邮件申请 |
| CEHA | 样本量仅 500 |
| CCC | 494 多标签 tags，无原始文本 |
| CASE Task 1 | K=2 二分类 |
| MPEDS | 工具/系统，非固定数据集 |

---

### 核心问题

**protest/political event 领域没有理想的公开 NLP 文本分类数据集。** 上述候选全部是结构化编码数据（tabular），不含可直接用于文本分类的原始新闻文本。要做 NLP 实验需要自行匹配/爬取新闻，这引入额外复杂度和版权问题。

---

### 建议

如果坚持 protest 领域确实困难，建议考虑换到有成熟公开 NLP 数据集的任务类型：

| 替代方向 | 数据集 | K | 样本量 | 特点 |
|---------|--------|---|--------|------|
| **危机事件分类** | HumAID | 11 | ~77K tweets | CC-BY-NC, HuggingFace 直接下载，gold labels |
| **情感分类** | GoEmotions | 27/28 | 58K | Reddit 文本，多标签，Google 标注 |
| **意图分类** | CLINC150 / BANKING77 | 150/77 | 23K/13K | 对话意图，完全公开 |
| **新闻主题** | AG News | 4 | 120K | 经典 benchmark |

其中 **HumAID** 最接近 protest 领域（crisis/disaster events），K=11，标注质量好，且项目本身研究标注错误归因，crisis event 分类的标注难度和噪声模式与 protest 类似。

是否要：(1) 用 PolDem action_form 做实验（接受 license 风险 + 无原始文本限制），(2) 转向 HumAID 等 crisis 数据集，还是 (3) 申请 GLOCON？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd1fa13d-c03d-441e-9b13-40a4d0f9fe7c",
  "isSidechain": false,
  "requestId": "req_011CbDbGqCLFfMJRJksn4YFU",
  "type": "assistant",
  "uuid": "43ac48c7-8d1c-4192-9187-cf0e13bce4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DwAeG5uacN2zHE6mvucBP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9932,
      "cache_read_input_tokens": 23653,
      "output_tokens": 2777,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2777,
          "cache_read_input_tokens": 23653,
          "cache_creation_input_tokens": 9932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9932
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

_source line 21_

```json
{
  "type": "last-prompt",
  "leafUuid": "43ac48c7-8d1c-4192-9187-cf0e13bce4a5",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Search for public protest event classification datasets",
  "sessionId": "f4e2217a-b32c-4a8a-a616-c19348792700"
}
```

---
