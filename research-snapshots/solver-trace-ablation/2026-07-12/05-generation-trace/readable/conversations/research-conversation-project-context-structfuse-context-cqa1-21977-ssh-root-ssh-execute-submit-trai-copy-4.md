# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: cqa1-21977 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/a4897adb-444f-47e1-81f6-81048ce3e3e1.jsonl`
- **Structured JSON:** [`4b53a1ea60de129e83c2.json`](../../sessions/4b/4b53a1ea60de129e83c2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T22:07:32.418Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T22:07:32.418Z",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: cqa1-21977\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse-context\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：Circuit Discovery 文献调研（2024-2026，聚焦 novelty 验证）\n\n### 背景\n项目 structfuse-context 的核心贡献是：用跨方法二值共识（CSS = Cross-method Stability Scoring）来鲁棒地发现电路。核心 claim 是不同方法找到的 circuit 有显著差异（off-diagonal），而共识子集（CSS-core）比单方法更鲁棒。\n\n**Novelty 关键问题**：有没有已发表的工作做过类似的\"比较不同 circuit discovery 方法的一致性\"或\"聚合多种方法的结果\"？\n\n### 调研问题（按优先级）\n\n**Q1（最重要）：方法一致性比较**\n搜索是否有论文系统比较了不同 circuit discovery 方法（EAP, ACDC, Edge Pruning, subnetwork probing 等）找到的 circuit 的一致性/差异性。\n- 关键词：`circuit discovery comparison`, `circuit agreement`, `circuit consistency`, `mechanistic interpretability comparison`\n- 如果有，记录：论文标题、方法、结论、与我们的区别\n\n**Q2（最重要）：Circuit aggregation / ensemble**\n搜索是否有论文提出聚合多种 circuit discovery 方法的结果（类似我们的 CSS/CIRCUS）。\n- 关键词：`circuit aggregation`, `circuit ensemble`, `multi-method circuit`, `robust circuit discovery`\n- 如果有，这直接威胁我们的 novelty\n\n**Q3：2024-2026 主要新方法**\n除了 EAP-IG, ACDC, Edge Pruning, IFR 之外，2024-2026 年还有什么重要的 circuit discovery 方法？\n- 关键词：`circuit discovery 2024`, `automated circuit discovery`, `mechanistic interpretability 2025`\n- 列出方法名、论文、算法族\n\n**Q4：顶会论文列表**\nICLR 2024/2025, NeurIPS 2024, ICML 2024/2025 上的 circuit discovery / mechanistic interpretability 相关论文。\n\n### 搜索策略\n1. 用 WebSearch 搜索 arXiv, Semantic Scholar, Google Scholar\n2. 对 Q1 和 Q2，搜索至少 3 种不同的关键词组合\n3. 对找到的高相关论文，用 WebFetch 读取 abstract 和 introduction 确认内容\n\n### 输出格式\n\n写到本地：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md`\n\n```markdown\n# Circuit Discovery Related Work Notes (2024-2026)\n\n## 1. 方法一致性比较（Novelty 关键）\n[找到的论文列表 + 摘要 + 与我们的区别]\n[如果没找到，明确说\"未找到直接比较不同方法一致性的工作\"]\n\n## 2. Circuit Aggregation / Ensemble（Novelty 威胁）\n[同上]\n\n## 3. 2024-2026 新方法\n| 方法 | 论文 | 年份 | 算法族 | 备注 |\n|------|------|------|--------|------|\n\n## 4. 顶会论文列表\n| 论文 | 会议 | 年份 | 主要贡献 |\n|------|------|------|----------|\n\n## 5. Novelty 评估\n[基于调研，评估 structfuse-context 的 novelty 是否站得住]\n[指出最大的 novelty 威胁和差异化点]\n```\n\n### 产出\n汇报重点：Q1 和 Q2 的结论（有没有直接竞争对手），以及 novelty 评估。\n\n### 注意事项\n- 只报告真实找到的论文，不要编造引用\n- 如果某个方向没找到相关工作，明确说\"未找到\"而非省略\n- 区分\"方法比较\"（如评估 benchmark）和\"方法聚合\"（如我们的 CSS），这是不同的贡献\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-12T22:07:32.422Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T22:07:32.422Z",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-12T22:07:32.462Z_

&lt;project_context>
# 项目: structfuse-context

## 运行环境
- 服务器名: cqa1-21977
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/structfuse-context


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：Circuit Discovery 文献调研（2024-2026，聚焦 novelty 验证）

### 背景
项目 structfuse-context 的核心贡献是：用跨方法二值共识（CSS = Cross-method Stability Scoring）来鲁棒地发现电路。核心 claim 是不同方法找到的 circuit 有显著差异（off-diagonal），而共识子集（CSS-core）比单方法更鲁棒。

**Novelty 关键问题**：有没有已发表的工作做过类似的"比较不同 circuit discovery 方法的一致性"或"聚合多种方法的结果"？

### 调研问题（按优先级）

**Q1（最重要）：方法一致性比较**
搜索是否有论文系统比较了不同 circuit discovery 方法（EAP, ACDC, Edge Pruning, subnetwork probing 等）找到的 circuit 的一致性/差异性。
- 关键词：`circuit discovery comparison`, `circuit agreement`, `circuit consistency`, `mechanistic interpretability comparison`
- 如果有，记录：论文标题、方法、结论、与我们的区别

**Q2（最重要）：Circuit aggregation / ensemble**
搜索是否有论文提出聚合多种 circuit discovery 方法的结果（类似我们的 CSS/CIRCUS）。
- 关键词：`circuit aggregation`, `circuit ensemble`, `multi-method circuit`, `robust circuit discovery`
- 如果有，这直接威胁我们的 novelty

**Q3：2024-2026 主要新方法**
除了 EAP-IG, ACDC, Edge Pruning, IFR 之外，2024-2026 年还有什么重要的 circuit discovery 方法？
- 关键词：`circuit discovery 2024`, `automated circuit discovery`, `mechanistic interpretability 2025`
- 列出方法名、论文、算法族

**Q4：顶会论文列表**
ICLR 2024/2025, NeurIPS 2024, ICML 2024/2025 上的 circuit discovery / mechanistic interpretability 相关论文。

### 搜索策略
1. 用 WebSearch 搜索 arXiv, Semantic Scholar, Google Scholar
2. 对 Q1 和 Q2，搜索至少 3 种不同的关键词组合
3. 对找到的高相关论文，用 WebFetch 读取 abstract 和 introduction 确认内容

### 输出格式

写到本地：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md`

```markdown
# Circuit Discovery Related Work Notes (2024-2026)

## 1. 方法一致性比较（Novelty 关键）
[找到的论文列表 + 摘要 + 与我们的区别]
[如果没找到，明确说"未找到直接比较不同方法一致性的工作"]

## 2. Circuit Aggregation / Ensemble（Novelty 威胁）
[同上]

## 3. 2024-2026 新方法
| 方法 | 论文 | 年份 | 算法族 | 备注 |
|------|------|------|--------|------|

## 4. 顶会论文列表
| 论文 | 会议 | 年份 | 主要贡献 |
|------|------|------|----------|

## 5. Novelty 评估
[基于调研，评估 structfuse-context 的 novelty 是否站得住]
[指出最大的 novelty 威胁和差异化点]
```

### 产出
汇报重点：Q1 和 Q2 的结论（有没有直接竞争对手），以及 novelty 评估。

### 注意事项
- 只报告真实找到的论文，不要编造引用
- 如果某个方向没找到相关工作，明确说"未找到"而非省略
- 区分"方法比较"（如评估 benchmark）和"方法聚合"（如我们的 CSS），这是不同的贡献


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ac1e15a4-789d-401b-936c-5f0b5ab58ba0",
  "type": "user",
  "uuid": "4045b35e-02cb-4cda-85c6-6eaba673a621",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T22:07:32.461Z_

```json
{
  "parentUuid": "4045b35e-02cb-4cda-85c6-6eaba673a621",
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
      "mcp__agent-ml-research__register_artifact",
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
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "bb78f85f-83a9-4d1f-a645-be972bdce71a",
  "timestamp": "2026-05-12T22:07:32.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T22:07:32.461Z_

```json
{
  "parentUuid": "bb78f85f-83a9-4d1f-a645-be972bdce71a",
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
  "uuid": "cb1e9e9d-427f-448f-948f-250d1fd485cc",
  "timestamp": "2026-05-12T22:07:32.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-12T22:07:32.461Z_

```json
{
  "parentUuid": "cb1e9e9d-427f-448f-948f-250d1fd485cc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f35a24df-7969-4ccb-8209-0a777a6b1e24",
  "timestamp": "2026-05-12T22:07:32.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
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
  "aiTitle": "Literature review on circuit discovery methods comparison",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---

### Assistant

_source line 8 · 2026-05-12T22:07:36.051Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a literature survey on Circuit Discovery (2024-2026) focusing on novelty verification for their project structfuse-context. The key questions are about whether anyone has compared consistency across circuit discovery methods or aggregated multiple methods' results.

Let me launch multiple search agents in parallel to cover the different questions efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f35a24df-7969-4ccb-8209-0a777a6b1e24",
  "isSidechain": false,
  "requestId": "req_011CaySFe5UCTpcSaoJWvJRL",
  "type": "assistant",
  "uuid": "6e11afc5-bfd3-4359-845e-9165e7d0a3ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNF9Kdgwyn4nhyrpTZEaAt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11925,
      "cache_read_input_tokens": 11841,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 185,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11925
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

_source line 9 · 2026-05-12T22:07:36.714Z_

开始文献调研，分四个方向并行搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e11afc5-bfd3-4359-845e-9165e7d0a3ab",
  "isSidechain": false,
  "requestId": "req_011CaySFe5UCTpcSaoJWvJRL",
  "type": "assistant",
  "uuid": "fc7c2246-e37c-4a59-b35b-9a81c52b630b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNF9Kdgwyn4nhyrpTZEaAt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11925,
      "cache_read_input_tokens": 11841,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 185,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11925
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

_source line 10 · 2026-05-12T22:07:37.064Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013AuTaAqpYhP5UsT6MCSAAx`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc7c2246-e37c-4a59-b35b-9a81c52b630b",
  "isSidechain": false,
  "requestId": "req_011CaySFe5UCTpcSaoJWvJRL",
  "type": "assistant",
  "uuid": "b88b6742-25ca-4094-b44d-d702995edbdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNF9Kdgwyn4nhyrpTZEaAt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11925,
      "cache_read_input_tokens": 11841,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 185,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11925
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

_source line 11 · 2026-05-12T22:07:37.070Z_

<details><summary>↩ Tool result · `toolu_013AuTaAqpYhP5UsT6MCSAAx`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b88b6742-25ca-4094-b44d-d702995edbdf",
  "isSidechain": false,
  "promptId": "ac1e15a4-789d-401b-936c-5f0b5ab58ba0",
  "type": "user",
  "uuid": "60b35c21-e7fa-4d49-8748-0f6bf81bd6be",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "b88b6742-25ca-4094-b44d-d702995edbdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-12T22:07:40.559Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me launch parallel search agents for the four questions. I'll use multiple agents to search in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60b35c21-e7fa-4d49-8748-0f6bf81bd6be",
  "isSidechain": false,
  "requestId": "req_011CaySFygBzYdJFHSrVzfcv",
  "type": "assistant",
  "uuid": "2a9e9fa9-3d8d-45bc-af1b-072a420209d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "output_tokens": 1421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1421,
          "cache_read_input_tokens": 23766,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
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

_source line 13 · 2026-05-12T22:07:47.265Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LDQfvBwWGQLX9DkoSBc9AR`</summary>

```json
{
  "description": "Q1: Circuit method consistency comparison",
  "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability. \n\n**Task**: Find papers that systematically compare different circuit discovery methods (e.g., EAP, ACDC, Edge Pruning, subnetwork probing, activation patching) and evaluate the consistency/agreement of the circuits they find.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit discovery comparison mechanistic interpretability\"\n2. \"circuit agreement consistency different methods transformers\"\n3. \"comparing automated circuit discovery ACDC EAP edge pruning\"\n4. \"circuit discovery benchmark evaluation\"\n5. \"mechanistic interpretability methods comparison 2024 2025\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors (first author + et al.)\n- Year / Venue\n- URL\n- What methods they compare\n- Key findings about consistency/disagreement\n- How it relates to \"cross-method binary consensus\" or aggregation\n\nIf no paper directly compares method consistency, say so explicitly. Be thorough - this is the most important question for novelty assessment.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a9e9fa9-3d8d-45bc-af1b-072a420209d6",
  "isSidechain": false,
  "requestId": "req_011CaySFygBzYdJFHSrVzfcv",
  "type": "assistant",
  "uuid": "588fb5df-a246-4538-8108-9e1ef3279fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "output_tokens": 1421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1421,
          "cache_read_input_tokens": 23766,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
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

_source line 14 · 2026-05-12T22:07:52.137Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JX4st1y5kYpBpUAVKFTMdz`</summary>

```json
{
  "description": "Q2: Circuit aggregation/ensemble methods",
  "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find papers that propose aggregating or ensembling results from multiple circuit discovery methods to get more robust circuits. This is the most critical novelty threat - if someone has done \"multi-method circuit aggregation\" or \"consensus circuit discovery\", we need to know.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit aggregation ensemble mechanistic interpretability\"\n2. \"robust circuit discovery multi-method consensus\"\n3. \"combining circuit discovery methods transformers\"\n4. \"cross-method circuit stability scoring\"\n5. \"circuit discovery robustness ensemble neural network\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors\n- Year / Venue\n- URL\n- What aggregation/ensemble approach they use\n- How similar it is to \"Cross-method Stability Scoring\" (CSS) - binary consensus across methods\n\nIf nothing found, explicitly state \"No papers found proposing multi-method circuit aggregation.\" Be very thorough.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "588fb5df-a246-4538-8108-9e1ef3279fd0",
  "isSidechain": false,
  "requestId": "req_011CaySFygBzYdJFHSrVzfcv",
  "type": "assistant",
  "uuid": "bd4dbeda-fc01-4b07-b7d3-f1066a412592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "output_tokens": 1421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1421,
          "cache_read_input_tokens": 23766,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
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

_source line 15 · 2026-05-12T22:07:56.886Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01L3fLhWV9gRjmmjD2tKgqGa`</summary>

```json
{
  "description": "Q3: New circuit discovery methods 2024-2026",
  "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find important new circuit discovery methods published in 2024-2026, beyond the well-known ones (EAP-IG, ACDC, Edge Pruning, IFR, activation patching).\n\nSearch using these keywords:\n1. \"circuit discovery 2024 2025 mechanistic interpretability\"\n2. \"automated circuit discovery new method transformer 2024\"\n3. \"mechanistic interpretability circuit finding 2025 2026\"\n4. \"subnetwork discovery interpretability 2024\"\n\nFor each search, use WebSearch. For promising papers, use WebFetch to read the abstract.\n\n**Output format**: A table with columns:\n- Method name\n- Paper title\n- Authors (first + et al.)\n- Year\n- Venue (if known)\n- Algorithm family (gradient-based, pruning-based, attribution-based, etc.)\n- Brief description\n- URL\n\nFocus on genuinely new methods, not just applications of existing methods to new models/tasks.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd4dbeda-fc01-4b07-b7d3-f1066a412592",
  "isSidechain": false,
  "requestId": "req_011CaySFygBzYdJFHSrVzfcv",
  "type": "assistant",
  "uuid": "6c810407-5965-4670-a536-a852a80f2a68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "output_tokens": 1421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1421,
          "cache_read_input_tokens": 23766,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
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

_source line 16 · 2026-05-12T22:08:01.168Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011k1dq6zk5AsEF3sipmxFHp`</summary>

```json
{
  "description": "Q4: Top venue circuit papers 2024-2025",
  "prompt": "You are conducting a literature survey on circuit discovery and mechanistic interpretability at top ML venues.\n\n**Task**: Find circuit discovery / mechanistic interpretability papers published at these venues:\n- ICLR 2024, ICLR 2025\n- NeurIPS 2024\n- ICML 2024, ICML 2025\n\nSearch using these queries:\n1. \"circuit discovery ICLR 2024 2025\"\n2. \"mechanistic interpretability NeurIPS 2024\"\n3. \"circuit discovery ICML 2024 2025\"\n4. \"automated interpretability circuits top conference 2024 2025\"\n5. \"mechanistic interpretability ICLR 2025 accepted papers\"\n\nFor each search, use WebSearch. Use WebFetch to confirm venue/year for important papers.\n\n**Output format**: A table with columns:\n- Paper title\n- Conference + Year\n- Main contribution (1-2 sentences)\n- URL\n\nOnly include papers genuinely about circuit discovery or closely related mechanistic interpretability (not general XAI or probing studies).",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c810407-5965-4670-a536-a852a80f2a68",
  "isSidechain": false,
  "requestId": "req_011CaySFygBzYdJFHSrVzfcv",
  "type": "assistant",
  "uuid": "b823c913-9973-42fd-9154-877e64bdb5b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o6KmdZm6WtJbmosiU4UfQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1204,
      "cache_read_input_tokens": 23766,
      "output_tokens": 1421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1421,
          "cache_read_input_tokens": 23766,
          "cache_creation_input_tokens": 1204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1204
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

_source line 17 · 2026-05-12T22:10:52.236Z_

<details><summary>↩ Tool result · `toolu_01L3fLhWV9gRjmmjD2tKgqGa`</summary>

```text


Here is the compiled literature survey table of new circuit discovery methods (2024--2026), excluding the well-known baselines (EAP-IG, ACDC, Edge Pruning, IFR, activation patching):

---

| **Method** | **Paper Title** | **Authors** | **Year** | **Venue** | **Algorithm Family** | **Brief Description** | **URL** |
|---|---|---|---|---|---|---|---|
| **CD-T** | Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition | Aliyah R. Hsu et al. | 2024 | ICLR 2025 | Decomposition-based | Recursively decomposes feature contributions through the computational graph using contextual decomposition equations. No activation patching needed. Reduces circuit discovery from hours to seconds; 97% ROC AUC on standard benchmarks. | [arxiv.org/abs/2407.00886](https://arxiv.org/abs/2407.00886) |
| **DiscoGP** | Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning | Lei Yu et al. | 2024 | ICML 2024 | Pruning-based (differentiable) | Joint weight and edge pruning via learnable binary masks trained end-to-end. Unifies weight-level and connection-level circuit discovery, which prior methods treated separately. | [arxiv.org/html/2407.03779v1](https://arxiv.org/html/2407.03779v1/) |
| **Transcoders** | Transcoders Find Interpretable LLM Feature Circuits | Jacob Dunefsky et al. | 2024 | NeurIPS 2024 | Sparse replacement model | Replaces dense MLP layers with wider, sparsely-activating MLP layers (transcoders) that approximate the original. Enables weights-based circuit analysis through MLPs, decomposing circuits into input-dependent and input-invariant terms. | [arxiv.org/abs/2406.11944](https://arxiv.org/abs/2406.11944) |
| **Sparse Feature Circuits** | Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | Samuel Marks et al. | 2024 | ICLR 2025 | Attribution-based (SAE features) | Discovers circuits over SAE-learned sparse features rather than neurons/heads. Introduces SHIFT for editing model behavior by removing task-irrelevant features. Fully unsupervised pipeline discovering thousands of circuits at scale. | [arxiv.org/abs/2403.19647](https://arxiv.org/abs/2403.19647) |
| **Circuit Tracing (Attribution Graphs)** | Circuit Tracing: Revealing Computational Graphs in Language Models | Emmanuel Ameisen, Chris Olah et al. (Anthropic, 26 authors) | 2025 | Anthropic Technical Report | Sparse replacement model + attribution | Replaces MLPs with cross-layer transcoders (CLTs) to build a "replacement model" of interpretable sparse features. Constructs per-prompt attribution graphs (DAGs) with linear edges between features. Applied to Claude 3.5 Haiku. | [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) |
| **GIM** | GIM: Improved Interpretability for Large Language Models | Joakim Edin et al. (Corti) | 2025 | arXiv (under review) | Gradient-based (modified backprop) | Addresses self-repair in attention (softmax redistribution) and LayerNorm by modifying gradient computation during backpropagation. Temperature-adjusted softmax gradients + LayerNorm freeze + gradient normalization. Tops HuggingFace MIB benchmark. | [arxiv.org/abs/2505.17630](https://arxiv.org/abs/2505.17630) |
| **HAP** | Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework | Hao Gu et al. (Algoverse) | 2025 | arXiv preprint | Hybrid (attribution + pruning) | Sequences EAP (fast, approximate) then Edge Pruning (faithful) on the EAP-filtered subgraph. 46% faster than EP alone with comparable faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that pure attribution misses. | [arxiv.org/html/2510.03282v1](https://arxiv.org/html/2510.03282v1) |
| **ModCirc** | Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of LLMs | Yinhan He et al. | 2025 | ICML 2025 | Modular decomposition | Discovers task-agnostic modular circuit vocabularies shared across language tasks, rather than task-specific circuits. Defines five criteria characterizing modular circuits. Enables global-level interpretability with reusable interpretations. | [openreview.net/forum?id=do5vVfKEXZ](https://openreview.net/forum?id=do5vVfKEXZ) |
| **Stream** | Stream: Scaling up Mechanistic Interpretability to Long Context in LLMs via Sparse Attention | J. Rosser et al. | 2025 | arXiv preprint | Hierarchical pruning | Compilable hierarchical pruning algorithm for per-head sparse attention masks in O(T log T) time. Binary-search-style refinement retains top-k key blocks per query. Prunes 97--99% of token interactions, enabling interpretability at 100K+ tokens on consumer GPUs. | [arxiv.org/abs/2510.19875](https://arxiv.org/abs/2510.19875) |
| **Weight-Sparse Circuits** | Weight-sparse transformers have interpretable circuits | Leo Gao et al. (OpenAI) | 2025 | arXiv preprint | Sparsity-constrained training | Trains transformers with extreme weight sparsity (~1 in 1000 nonzero). Resulting circuits are ~16x smaller than those from dense baselines. Neurons correspond to natural concepts with interpretable connections. Defines a capability--interpretability frontier. | [arxiv.org/abs/2511.13653](https://arxiv.org/abs/2511.13653) |
| **Formal MI (Verification-based)** | Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | Itamar Hadad et al. | 2026 | ICLR 2026 | Verification-based | First to use neural network verification for circuit discovery. Provides three provable guarantees: (1) input domain robustness, (2) robust patching over continuous perturbations, (3) minimality. Eliminates reliance on heuristics. | [arxiv.org/abs/2602.16823](https://arxiv.org/abs/2602.16823) |
| **SVD Directional Masking** | Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits | Areeb Ahmad et al. | 2025 | arXiv preprint | SVD + differentiable masking | Decomposes attention heads and MLPs into orthogonal singular directions via SVD, revealing superposed subfunctions within single heads. Learnable diagonal masks on singular values identify functionally important directions. | [arxiv.org/html/2511.20273](https://arxiv.org/html/2511.20273) |

---

**Notable non-method papers relevant to the field:**

| **Paper** | **Authors** | **Year** | **Venue** | **Relevance** |
|---|---|---|---|---|
| The Computational Complexity of Circuit Discovery for Inner Interpretability | Federico Adolfi et al. | 2025 | ICLR 2025 (Spotlight) | Proves many circuit-finding queries are NP-hard and inapproximable; establishes fundamental complexity barriers. |
| MIB: A Mechanistic Interpretability Benchmark | Aaron Mueller et al. (20+ authors) | 2025 | ICML 2025 | Standard benchmark with two tracks (circuit localization, causal variable localization) across 5 models. Attribution and mask optimization methods lead on circuit localization. |
| InterpBench: Semi-Synthetic Transformers for Evaluating MI Techniques | Rohan Gupta et al. | 2024 | NeurIPS 2024 | Semi-synthetic transformers with known ground-truth circuits for evaluating discovery methods. Uses Strict IIT training. |

**Key trends observed:**

1. **Decomposition over patching**: CD-T and SVD directional masking avoid activation patching entirely, using mathematical decomposition for speedups of orders of magnitude.
2. **Feature-level circuits**: Sparse Feature Circuits, Transcoders, and Anthropic's Circuit Tracing all operate over learned sparse features (via SAEs or transcoders) rather than raw neurons/heads, yielding more interpretable units.
3. **Formal guarantees**: The verification-based approach (ICLR 2026) is the first to provide provable correctness, addressing a long-standing gap.
4. **Sparsity by design**: OpenAI's weight-sparse training creates models that are inherently more interpretable, sidestepping post-hoc discovery entirely.
5. **Scaling**: Stream and GIM specifically target practical scalability -- long contexts and production-scale models respectively.

agentId: ab64af982756e2f1f (use SendMessage with to: 'ab64af982756e2f1f' to continue this agent)
&lt;usage>total_tokens: 39682
tool_uses: 31
duration_ms: 175345&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c810407-5965-4670-a536-a852a80f2a68",
  "isSidechain": false,
  "promptId": "ac1e15a4-789d-401b-936c-5f0b5ab58ba0",
  "type": "user",
  "uuid": "1c65dfb4-e921-4dc1-b061-a8984d146f2a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find important new circuit discovery methods published in 2024-2026, beyond the well-known ones (EAP-IG, ACDC, Edge Pruning, IFR, activation patching).\n\nSearch using these keywords:\n1. \"circuit discovery 2024 2025 mechanistic interpretability\"\n2. \"automated circuit discovery new method transformer 2024\"\n3. \"mechanistic interpretability circuit finding 2025 2026\"\n4. \"subnetwork discovery interpretability 2024\"\n\nFor each search, use WebSearch. For promising papers, use WebFetch to read the abstract.\n\n**Output format**: A table with columns:\n- Method name\n- Paper title\n- Authors (first + et al.)\n- Year\n- Venue (if known)\n- Algorithm family (gradient-based, pruning-based, attribution-based, etc.)\n- Brief description\n- URL\n\nFocus on genuinely new methods, not just applications of existing methods to new models/tasks.",
    "agentId": "ab64af982756e2f1f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the compiled literature survey table of new circuit discovery methods (2024--2026), excluding the well-known baselines (EAP-IG, ACDC, Edge Pruning, IFR, activation patching):\n\n---\n\n| **Method** | **Paper Title** | **Authors** | **Year** | **Venue** | **Algorithm Family** | **Brief Description** | **URL** |\n|---|---|---|---|---|---|---|---|\n| **CD-T** | Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition | Aliyah R. Hsu et al. | 2024 | ICLR 2025 | Decomposition-based | Recursively decomposes feature contributions through the computational graph using contextual decomposition equations. No activation patching needed. Reduces circuit discovery from hours to seconds; 97% ROC AUC on standard benchmarks. | [arxiv.org/abs/2407.00886](https://arxiv.org/abs/2407.00886) |\n| **DiscoGP** | Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning | Lei Yu et al. | 2024 | ICML 2024 | Pruning-based (differentiable) | Joint weight and edge pruning via learnable binary masks trained end-to-end. Unifies weight-level and connection-level circuit discovery, which prior methods treated separately. | [arxiv.org/html/2407.03779v1](https://arxiv.org/html/2407.03779v1/) |\n| **Transcoders** | Transcoders Find Interpretable LLM Feature Circuits | Jacob Dunefsky et al. | 2024 | NeurIPS 2024 | Sparse replacement model | Replaces dense MLP layers with wider, sparsely-activating MLP layers (transcoders) that approximate the original. Enables weights-based circuit analysis through MLPs, decomposing circuits into input-dependent and input-invariant terms. | [arxiv.org/abs/2406.11944](https://arxiv.org/abs/2406.11944) |\n| **Sparse Feature Circuits** | Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | Samuel Marks et al. | 2024 | ICLR 2025 | Attribution-based (SAE features) | Discovers circuits over SAE-learned sparse features rather than neurons/heads. Introduces SHIFT for editing model behavior by removing task-irrelevant features. Fully unsupervised pipeline discovering thousands of circuits at scale. | [arxiv.org/abs/2403.19647](https://arxiv.org/abs/2403.19647) |\n| **Circuit Tracing (Attribution Graphs)** | Circuit Tracing: Revealing Computational Graphs in Language Models | Emmanuel Ameisen, Chris Olah et al. (Anthropic, 26 authors) | 2025 | Anthropic Technical Report | Sparse replacement model + attribution | Replaces MLPs with cross-layer transcoders (CLTs) to build a \"replacement model\" of interpretable sparse features. Constructs per-prompt attribution graphs (DAGs) with linear edges between features. Applied to Claude 3.5 Haiku. | [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) |\n| **GIM** | GIM: Improved Interpretability for Large Language Models | Joakim Edin et al. (Corti) | 2025 | arXiv (under review) | Gradient-based (modified backprop) | Addresses self-repair in attention (softmax redistribution) and LayerNorm by modifying gradient computation during backpropagation. Temperature-adjusted softmax gradients + LayerNorm freeze + gradient normalization. Tops HuggingFace MIB benchmark. | [arxiv.org/abs/2505.17630](https://arxiv.org/abs/2505.17630) |\n| **HAP** | Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework | Hao Gu et al. (Algoverse) | 2025 | arXiv preprint | Hybrid (attribution + pruning) | Sequences EAP (fast, approximate) then Edge Pruning (faithful) on the EAP-filtered subgraph. 46% faster than EP alone with comparable faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that pure attribution misses. | [arxiv.org/html/2510.03282v1](https://arxiv.org/html/2510.03282v1) |\n| **ModCirc** | Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of LLMs | Yinhan He et al. | 2025 | ICML 2025 | Modular decomposition | Discovers task-agnostic modular circuit vocabularies shared across language tasks, rather than task-specific circuits. Defines five criteria characterizing modular circuits. Enables global-level interpretability with reusable interpretations. | [openreview.net/forum?id=do5vVfKEXZ](https://openreview.net/forum?id=do5vVfKEXZ) |\n| **Stream** | Stream: Scaling up Mechanistic Interpretability to Long Context in LLMs via Sparse Attention | J. Rosser et al. | 2025 | arXiv preprint | Hierarchical pruning | Compilable hierarchical pruning algorithm for per-head sparse attention masks in O(T log T) time. Binary-search-style refinement retains top-k key blocks per query. Prunes 97--99% of token interactions, enabling interpretability at 100K+ tokens on consumer GPUs. | [arxiv.org/abs/2510.19875](https://arxiv.org/abs/2510.19875) |\n| **Weight-Sparse Circuits** | Weight-sparse transformers have interpretable circuits | Leo Gao et al. (OpenAI) | 2025 | arXiv preprint | Sparsity-constrained training | Trains transformers with extreme weight sparsity (~1 in 1000 nonzero). Resulting circuits are ~16x smaller than those from dense baselines. Neurons correspond to natural concepts with interpretable connections. Defines a capability--interpretability frontier. | [arxiv.org/abs/2511.13653](https://arxiv.org/abs/2511.13653) |\n| **Formal MI (Verification-based)** | Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | Itamar Hadad et al. | 2026 | ICLR 2026 | Verification-based | First to use neural network verification for circuit discovery. Provides three provable guarantees: (1) input domain robustness, (2) robust patching over continuous perturbations, (3) minimality. Eliminates reliance on heuristics. | [arxiv.org/abs/2602.16823](https://arxiv.org/abs/2602.16823) |\n| **SVD Directional Masking** | Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits | Areeb Ahmad et al. | 2025 | arXiv preprint | SVD + differentiable masking | Decomposes attention heads and MLPs into orthogonal singular directions via SVD, revealing superposed subfunctions within single heads. Learnable diagonal masks on singular values identify functionally important directions. | [arxiv.org/html/2511.20273](https://arxiv.org/html/2511.20273) |\n\n---\n\n**Notable non-method papers relevant to the field:**\n\n| **Paper** | **Authors** | **Year** | **Venue** | **Relevance** |\n|---|---|---|---|---|\n| The Computational Complexity of Circuit Discovery for Inner Interpretability | Federico Adolfi et al. | 2025 | ICLR 2025 (Spotlight) | Proves many circuit-finding queries are NP-hard and inapproximable; establishes fundamental complexity barriers. |\n| MIB: A Mechanistic Interpretability Benchmark | Aaron Mueller et al. (20+ authors) | 2025 | ICML 2025 | Standard benchmark with two tracks (circuit localization, causal variable localization) across 5 models. Attribution and mask optimization methods lead on circuit localization. |\n| InterpBench: Semi-Synthetic Transformers for Evaluating MI Techniques | Rohan Gupta et al. | 2024 | NeurIPS 2024 | Semi-synthetic transformers with known ground-truth circuits for evaluating discovery methods. Uses Strict IIT training. |\n\n**Key trends observed:**\n\n1. **Decomposition over patching**: CD-T and SVD directional masking avoid activation patching entirely, using mathematical decomposition for speedups of orders of magnitude.\n2. **Feature-level circuits**: Sparse Feature Circuits, Transcoders, and Anthropic's Circuit Tracing all operate over learned sparse features (via SAEs or transcoders) rather than raw neurons/heads, yielding more interpretable units.\n3. **Formal guarantees**: The verification-based approach (ICLR 2026) is the first to provide provable correctness, addressing a long-standing gap.\n4. **Sparsity by design**: OpenAI's weight-sparse training creates models that are inherently more interpretable, sidestepping post-hoc discovery entirely.\n5. **Scaling**: Stream and GIM specifically target practical scalability -- long contexts and production-scale models respectively."
      }
    ],
    "totalDurationMs": 175345,
    "totalTokens": 39682,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 36975,
      "output_tokens": 2325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2325,
          "cache_read_input_tokens": 36975,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 379,
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
      "otherToolCount": 31
    }
  },
  "sourceToolAssistantUUID": "6c810407-5965-4670-a536-a852a80f2a68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "leafUuid": "1c65dfb4-e921-4dc1-b061-a8984d146f2a",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature review on circuit discovery methods comparison",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---

### Tool result

_source line 20 · 2026-05-12T22:11:13.502Z_

<details><summary>↩ Tool result · `toolu_01LDQfvBwWGQLX9DkoSBc9AR`</summary>

```text


Here is the comprehensive literature survey on cross-method comparison and consistency in circuit discovery.

---

## Summary of Findings

**No paper directly studies "cross-method binary consensus" as a first-class research question.** No existing work systematically takes multiple circuit discovery methods, runs them on the same tasks, binarizes each method's output into edge-level masks, and then measures agreement rates (e.g., Jaccard, intersection-over-union, Cohen's kappa) across methods. This is a clear gap in the literature.

However, several papers are closely adjacent and provide partial evidence or related frameworks. Below are the relevant papers organized by relevance.

---

## Tier 1: Papers That Directly Compare Multiple Circuit Discovery Methods

### 1. "Towards Automated Circuit Discovery for Mechanistic Interpretability"
- **Authors:** Conmy, Mavor-Parker, Lynch, Heimersheim, Garriga-Alonso
- **Year/Venue:** NeurIPS 2023
- **URL:** https://arxiv.org/abs/2304.14997
- **Methods compared:** ACDC vs. Subnetwork Probing (SP) vs. Head Importance Score Pruning (HISP)
- **Key findings:** ACDC achieved ROC AUC of 0.982 on Docstring (vs. SP 0.937, HISP 0.805) and 0.853 on Greater-Than (vs. SP 0.806, HISP 0.693). All manually-identified heads were recovered by ACDC, but ACDC also found additional components not in manual circuits.
- **Re: cross-method consensus:** Compares methods via ROC AUC against ground-truth manual circuits, but does NOT measure pairwise agreement between automated methods themselves.

### 2. "Attribution Patching Outperforms Automated Circuit Discovery"
- **Authors:** Syed, Rager, Conmy
- **Year/Venue:** NeurIPS 2023 ATTRIB Workshop; BlackboxNLP 2024 (ACL Anthology)
- **URL:** https://arxiv.org/abs/2310.10348
- **Methods compared:** EAP vs. ACDC vs. SP vs. HISP
- **Key findings:** EAP achieves greater AUC from circuit recovery than ACDC while requiring only two forward passes and one backward pass (vs. ACDC's exponential scaling). EAP is competitive with ACDC on recovering ground-truth circuits.
- **Re: cross-method consensus:** Evaluates each method against ground-truth via AUC. Does not measure inter-method overlap or agreement directly.

### 3. "Finding Transformer Circuits with Edge Pruning"
- **Authors:** Bhaskar, Wettig, Friedman, Chen
- **Year/Venue:** NeurIPS 2024 (Spotlight)
- **URL:** https://arxiv.org/abs/2406.16778
- **Methods compared:** Edge Pruning vs. ACDC vs. EAP
- **Key findings:** Edge Pruning is "considerably more faithful on IOI and GT than both ACDC and EAP, especially at higher sparsities." Scales to CodeLlama-13B (100x larger). Finds circuits with less than half the edges of prior methods.
- **Re: cross-method consensus:** Shows methods disagree substantially on which edges matter, especially at high sparsity. Edge Pruning finds sparser, more faithful circuits than EAP/ACDC, implying the circuits do NOT fully overlap.

### 4. "Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition" (CD-T)
- **Authors:** Hsu, Zhou, Cherapanamjeri, Huang, Odisho, Carroll, Yu
- **Year/Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2407.00886
- **Methods compared:** CD-T vs. ACDC vs. EAP
- **Key findings:** CD-T achieves 97% ROC AUC on average for recovering manual circuits, outperforming ACDC and EAP. Optimal granularity varies by task (fine-grained for IOI, coarse for Greater-Than).
- **Re: cross-method consensus:** Evaluates against ground-truth circuits. Notes that manual circuits of the same size still exhibit higher faithfulness than any automated method, suggesting all automated methods miss some edges.

### 5. "GIM: Improved Interpretability for Large Language Models"
- **Authors:** Edin, Csordás, Ruotsalo, Wu, Maistro, Christensen, Huang, Maaløe
- **Year/Venue:** 2025 (arXiv, tops HuggingFace MIB leaderboard)
- **URL:** https://arxiv.org/abs/2505.17630
- **Methods compared:** GIM vs. EActP, EAP, EAP-IG, NAP, IFR, UGS
- **Key findings:** GIM significantly outperforms other gradient-based methods in early layers; Integrated Gradients has slight advantages in middle/late layers. Tested across Gemma, LLAMA, Qwen families.
- **Re: cross-method consensus:** Compares faithfulness metrics across methods but does not measure structural overlap between discovered circuits.

---

## Tier 2: Papers That Address Method Agreement / Disagreement Directly

### 6. "Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms"
- **Authors:** Hanna, Pezzelle, Belinkov
- **Year/Venue:** 2024 (arXiv)
- **URL:** https://arxiv.org/abs/2403.17806
- **Methods compared:** EAP vs. EAP-IG (with causal intervention baseline)
- **Key findings:** **This is the closest paper to the "consensus" question.** It shows that EAP and EAP-IG circuits have HIGH NODE OVERLAP with causal intervention circuits, yet EAP circuits are LESS FAITHFUL than EAP-IG circuits. The critical insight: **overlap ≠ faithfulness**. Two methods can agree on ~same edges yet produce circuits with very different functional properties.
- **Re: cross-method consensus:** Directly measures node overlap between methods and shows it is misleading. Argues faithfulness, not overlap, should be the evaluation criterion. This is a strong cautionary result for any "binary consensus" approach.

### 7. "Mechanistic Interpretability as Statistical Estimation: A Variance Analysis"
- **Authors:** Méloux, Portet, Peyrard
- **Year/Venue:** 2025 (arXiv, v3 Feb 2026)
- **URL:** https://arxiv.org/abs/2510.00845
- **Methods compared:** Focuses on EAP-IG variants (does NOT compare across fundamentally different methods)
- **Key findings:** **Circuits are highly unstable.** Bootstrap resampling produces circuits with Jaccard index of only 0.561. Hyperparameter variations yield Jaccard similarities ranging from 0.086 to 1.0. Small perturbations in input data or hyperparameters yield "vastly different circuits." The method can converge to "multiple, distinct, yet stable circuit solutions."
- **Re: cross-method consensus:** Uses Jaccard index to measure overlap but only WITHIN one method under different conditions. Does NOT compare across methods. The finding of extreme instability within a single method raises serious questions about whether cross-method consensus is meaningful if intra-method consistency is already low.

---

## Tier 3: Ensemble / Aggregation Approaches (Most Relevant to "Binary Consensus")

### 8. "BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods"
- **Authors:** Mondorf, Wang, Gerstner, Hakimi, Liu, Veloso, Zhou, Schütze, Plank
- **Year/Venue:** BlackboxNLP 2025 (ACL Workshop)
- **URL:** https://arxiv.org/abs/2510.06811
- **Methods ensembled:** EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning
- **Key findings:** **This is the most directly relevant paper to "binary consensus."** They explicitly frame score aggregation in binary terms:
  - **Maximum** = union of circuits (edge selected by ANY method)
  - **Minimum** = intersection of circuits (edge selected by ALL methods)
  - **Mean** = soft consensus
  - Result: **Mean outperforms both union and intersection.** The hybrid ensemble (parallel + sequential) achieved best results (CMD 0.03, CPR 1.83).
- **Re: cross-method consensus:** Directly implements union/intersection as binary consensus operations. However, they do NOT report the agreement rate itself (what fraction of edges are selected by all methods vs. only one). They treat it as a score combination problem, not an analysis of disagreement.

### 9. "Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models"
- **Authors:** Arad, Belinkov, Chen, Kim, Mohebbi, Mueller, Sarti, Tutek
- **Year/Venue:** BlackboxNLP 2025
- **URL:** https://arxiv.org/abs/2511.18409
- **Key findings:** 3 teams, 8 methods. Ensemble and regularization strategies were most effective. Methods that "filter components with unstable contributions" performed best.
- **Re: cross-method consensus:** Does not report inter-method agreement statistics.

### 10. "MIB: A Mechanistic Interpretability Benchmark"
- **Authors:** Mueller, Geiger, Wiegreffe, et al. (25+ authors)
- **Year/Venue:** ICML 2025
- **URL:** https://arxiv.org/abs/2504.13151
- **Methods benchmarked:** Attribution patching, mask optimization, information flow methods
- **Key findings:** Establishes standardized evaluation (faithfulness integral/CPR, minimality, AUROC). Attribution and mask optimization methods perform best. SAEs show no advantage over raw neurons for featurization.
- **Re: cross-method consensus:** Provides a common evaluation framework but does not measure inter-method agreement on discovered circuits.

---

## Tier 4: Additional Related Papers

### 11. "Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework" (HAP)
- **Authors:** Gu, Nair, Kumar, Sharma, Lagasse
- **Year/Venue:** NeurIPS 2025 MechInterp Workshop
- **URL:** https://arxiv.org/abs/2510.03282
- **Methods combined:** Attribution patching → Edge Pruning (sequential)
- **Key findings:** 46% faster than baselines. Case study shows attribution patching prunes S-inhibition heads at high sparsity that HAP preserves — demonstrating that attribution patching and edge pruning disagree on cooperative circuit components.

### 12. "Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees"
- **Authors:** (multiple)
- **Year/Venue:** 2025
- **URL:** https://arxiv.org/abs/2602.16823
- **Key contribution:** Proposes circuits with provable guarantees (robustness, minimality) using neural network verification. Shows standard circuit discovery methods lack robustness guarantees.

---

## Key Takeaways for Novelty Assessment

1. **No paper measures cross-method binary consensus as its primary contribution.** The Mondorf et al. (2025) ensemble paper comes closest by implementing union/intersection operations, but treats it as a practical combination strategy, not an analytical study of agreement.

2. **The evidence strongly suggests methods disagree substantially:**
   - Edge Pruning finds circuits with <50% of the edges that ACDC/EAP find (Bhaskar et al.)
   - High node overlap does NOT imply high faithfulness (Hanna et al.)
   - Even a SINGLE method (EAP-IG) produces circuits with Jaccard ~0.56 under bootstrap resampling (Méloux et al.)
   - Different methods preserve/prune different cooperative components (HAP paper)

3. **The gap is clear:** Nobody has systematically run N methods on the same tasks, binarized the outputs, computed pairwise Jaccard / agreement matrices, and analyzed WHERE methods agree vs. disagree (e.g., by layer, by component type, by edge importance rank). A "cross-method binary consensus" study would be novel.

4. **The Méloux et al. variance paper is the strongest cautionary result:** If intra-method variance is already high (Jaccard 0.56), cross-method consensus may be even lower, or the consensus signal may be more robust than any individual method (which is the hypothesis behind ensembling in Mondorf et al.).

agentId: a12b9308a37a2d7a7 (use SendMessage with to: 'a12b9308a37a2d7a7' to continue this agent)
&lt;usage>total_tokens: 43939
tool_uses: 35
duration_ms: 206231&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "588fb5df-a246-4538-8108-9e1ef3279fd0",
  "isSidechain": false,
  "promptId": "ac1e15a4-789d-401b-936c-5f0b5ab58ba0",
  "type": "user",
  "uuid": "2580b9fb-40fa-4a2b-9fe2-cadacd68c941",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability. \n\n**Task**: Find papers that systematically compare different circuit discovery methods (e.g., EAP, ACDC, Edge Pruning, subnetwork probing, activation patching) and evaluate the consistency/agreement of the circuits they find.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit discovery comparison mechanistic interpretability\"\n2. \"circuit agreement consistency different methods transformers\"\n3. \"comparing automated circuit discovery ACDC EAP edge pruning\"\n4. \"circuit discovery benchmark evaluation\"\n5. \"mechanistic interpretability methods comparison 2024 2025\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors (first author + et al.)\n- Year / Venue\n- URL\n- What methods they compare\n- Key findings about consistency/disagreement\n- How it relates to \"cross-method binary consensus\" or aggregation\n\nIf no paper directly compares method consistency, say so explicitly. Be thorough - this is the most important question for novelty assessment.",
    "agentId": "a12b9308a37a2d7a7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the comprehensive literature survey on cross-method comparison and consistency in circuit discovery.\n\n---\n\n## Summary of Findings\n\n**No paper directly studies \"cross-method binary consensus\" as a first-class research question.** No existing work systematically takes multiple circuit discovery methods, runs them on the same tasks, binarizes each method's output into edge-level masks, and then measures agreement rates (e.g., Jaccard, intersection-over-union, Cohen's kappa) across methods. This is a clear gap in the literature.\n\nHowever, several papers are closely adjacent and provide partial evidence or related frameworks. Below are the relevant papers organized by relevance.\n\n---\n\n## Tier 1: Papers That Directly Compare Multiple Circuit Discovery Methods\n\n### 1. \"Towards Automated Circuit Discovery for Mechanistic Interpretability\"\n- **Authors:** Conmy, Mavor-Parker, Lynch, Heimersheim, Garriga-Alonso\n- **Year/Venue:** NeurIPS 2023\n- **URL:** https://arxiv.org/abs/2304.14997\n- **Methods compared:** ACDC vs. Subnetwork Probing (SP) vs. Head Importance Score Pruning (HISP)\n- **Key findings:** ACDC achieved ROC AUC of 0.982 on Docstring (vs. SP 0.937, HISP 0.805) and 0.853 on Greater-Than (vs. SP 0.806, HISP 0.693). All manually-identified heads were recovered by ACDC, but ACDC also found additional components not in manual circuits.\n- **Re: cross-method consensus:** Compares methods via ROC AUC against ground-truth manual circuits, but does NOT measure pairwise agreement between automated methods themselves.\n\n### 2. \"Attribution Patching Outperforms Automated Circuit Discovery\"\n- **Authors:** Syed, Rager, Conmy\n- **Year/Venue:** NeurIPS 2023 ATTRIB Workshop; BlackboxNLP 2024 (ACL Anthology)\n- **URL:** https://arxiv.org/abs/2310.10348\n- **Methods compared:** EAP vs. ACDC vs. SP vs. HISP\n- **Key findings:** EAP achieves greater AUC from circuit recovery than ACDC while requiring only two forward passes and one backward pass (vs. ACDC's exponential scaling). EAP is competitive with ACDC on recovering ground-truth circuits.\n- **Re: cross-method consensus:** Evaluates each method against ground-truth via AUC. Does not measure inter-method overlap or agreement directly.\n\n### 3. \"Finding Transformer Circuits with Edge Pruning\"\n- **Authors:** Bhaskar, Wettig, Friedman, Chen\n- **Year/Venue:** NeurIPS 2024 (Spotlight)\n- **URL:** https://arxiv.org/abs/2406.16778\n- **Methods compared:** Edge Pruning vs. ACDC vs. EAP\n- **Key findings:** Edge Pruning is \"considerably more faithful on IOI and GT than both ACDC and EAP, especially at higher sparsities.\" Scales to CodeLlama-13B (100x larger). Finds circuits with less than half the edges of prior methods.\n- **Re: cross-method consensus:** Shows methods disagree substantially on which edges matter, especially at high sparsity. Edge Pruning finds sparser, more faithful circuits than EAP/ACDC, implying the circuits do NOT fully overlap.\n\n### 4. \"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition\" (CD-T)\n- **Authors:** Hsu, Zhou, Cherapanamjeri, Huang, Odisho, Carroll, Yu\n- **Year/Venue:** ICLR 2025\n- **URL:** https://arxiv.org/abs/2407.00886\n- **Methods compared:** CD-T vs. ACDC vs. EAP\n- **Key findings:** CD-T achieves 97% ROC AUC on average for recovering manual circuits, outperforming ACDC and EAP. Optimal granularity varies by task (fine-grained for IOI, coarse for Greater-Than).\n- **Re: cross-method consensus:** Evaluates against ground-truth circuits. Notes that manual circuits of the same size still exhibit higher faithfulness than any automated method, suggesting all automated methods miss some edges.\n\n### 5. \"GIM: Improved Interpretability for Large Language Models\"\n- **Authors:** Edin, Csordás, Ruotsalo, Wu, Maistro, Christensen, Huang, Maaløe\n- **Year/Venue:** 2025 (arXiv, tops HuggingFace MIB leaderboard)\n- **URL:** https://arxiv.org/abs/2505.17630\n- **Methods compared:** GIM vs. EActP, EAP, EAP-IG, NAP, IFR, UGS\n- **Key findings:** GIM significantly outperforms other gradient-based methods in early layers; Integrated Gradients has slight advantages in middle/late layers. Tested across Gemma, LLAMA, Qwen families.\n- **Re: cross-method consensus:** Compares faithfulness metrics across methods but does not measure structural overlap between discovered circuits.\n\n---\n\n## Tier 2: Papers That Address Method Agreement / Disagreement Directly\n\n### 6. \"Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms\"\n- **Authors:** Hanna, Pezzelle, Belinkov\n- **Year/Venue:** 2024 (arXiv)\n- **URL:** https://arxiv.org/abs/2403.17806\n- **Methods compared:** EAP vs. EAP-IG (with causal intervention baseline)\n- **Key findings:** **This is the closest paper to the \"consensus\" question.** It shows that EAP and EAP-IG circuits have HIGH NODE OVERLAP with causal intervention circuits, yet EAP circuits are LESS FAITHFUL than EAP-IG circuits. The critical insight: **overlap ≠ faithfulness**. Two methods can agree on ~same edges yet produce circuits with very different functional properties.\n- **Re: cross-method consensus:** Directly measures node overlap between methods and shows it is misleading. Argues faithfulness, not overlap, should be the evaluation criterion. This is a strong cautionary result for any \"binary consensus\" approach.\n\n### 7. \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\"\n- **Authors:** Méloux, Portet, Peyrard\n- **Year/Venue:** 2025 (arXiv, v3 Feb 2026)\n- **URL:** https://arxiv.org/abs/2510.00845\n- **Methods compared:** Focuses on EAP-IG variants (does NOT compare across fundamentally different methods)\n- **Key findings:** **Circuits are highly unstable.** Bootstrap resampling produces circuits with Jaccard index of only 0.561. Hyperparameter variations yield Jaccard similarities ranging from 0.086 to 1.0. Small perturbations in input data or hyperparameters yield \"vastly different circuits.\" The method can converge to \"multiple, distinct, yet stable circuit solutions.\"\n- **Re: cross-method consensus:** Uses Jaccard index to measure overlap but only WITHIN one method under different conditions. Does NOT compare across methods. The finding of extreme instability within a single method raises serious questions about whether cross-method consensus is meaningful if intra-method consistency is already low.\n\n---\n\n## Tier 3: Ensemble / Aggregation Approaches (Most Relevant to \"Binary Consensus\")\n\n### 8. \"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods\"\n- **Authors:** Mondorf, Wang, Gerstner, Hakimi, Liu, Veloso, Zhou, Schütze, Plank\n- **Year/Venue:** BlackboxNLP 2025 (ACL Workshop)\n- **URL:** https://arxiv.org/abs/2510.06811\n- **Methods ensembled:** EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning\n- **Key findings:** **This is the most directly relevant paper to \"binary consensus.\"** They explicitly frame score aggregation in binary terms:\n  - **Maximum** = union of circuits (edge selected by ANY method)\n  - **Minimum** = intersection of circuits (edge selected by ALL methods)\n  - **Mean** = soft consensus\n  - Result: **Mean outperforms both union and intersection.** The hybrid ensemble (parallel + sequential) achieved best results (CMD 0.03, CPR 1.83).\n- **Re: cross-method consensus:** Directly implements union/intersection as binary consensus operations. However, they do NOT report the agreement rate itself (what fraction of edges are selected by all methods vs. only one). They treat it as a score combination problem, not an analysis of disagreement.\n\n### 9. \"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models\"\n- **Authors:** Arad, Belinkov, Chen, Kim, Mohebbi, Mueller, Sarti, Tutek\n- **Year/Venue:** BlackboxNLP 2025\n- **URL:** https://arxiv.org/abs/2511.18409\n- **Key findings:** 3 teams, 8 methods. Ensemble and regularization strategies were most effective. Methods that \"filter components with unstable contributions\" performed best.\n- **Re: cross-method consensus:** Does not report inter-method agreement statistics.\n\n### 10. \"MIB: A Mechanistic Interpretability Benchmark\"\n- **Authors:** Mueller, Geiger, Wiegreffe, et al. (25+ authors)\n- **Year/Venue:** ICML 2025\n- **URL:** https://arxiv.org/abs/2504.13151\n- **Methods benchmarked:** Attribution patching, mask optimization, information flow methods\n- **Key findings:** Establishes standardized evaluation (faithfulness integral/CPR, minimality, AUROC). Attribution and mask optimization methods perform best. SAEs show no advantage over raw neurons for featurization.\n- **Re: cross-method consensus:** Provides a common evaluation framework but does not measure inter-method agreement on discovered circuits.\n\n---\n\n## Tier 4: Additional Related Papers\n\n### 11. \"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework\" (HAP)\n- **Authors:** Gu, Nair, Kumar, Sharma, Lagasse\n- **Year/Venue:** NeurIPS 2025 MechInterp Workshop\n- **URL:** https://arxiv.org/abs/2510.03282\n- **Methods combined:** Attribution patching → Edge Pruning (sequential)\n- **Key findings:** 46% faster than baselines. Case study shows attribution patching prunes S-inhibition heads at high sparsity that HAP preserves — demonstrating that attribution patching and edge pruning disagree on cooperative circuit components.\n\n### 12. \"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\"\n- **Authors:** (multiple)\n- **Year/Venue:** 2025\n- **URL:** https://arxiv.org/abs/2602.16823\n- **Key contribution:** Proposes circuits with provable guarantees (robustness, minimality) using neural network verification. Shows standard circuit discovery methods lack robustness guarantees.\n\n---\n\n## Key Takeaways for Novelty Assessment\n\n1. **No paper measures cross-method binary consensus as its primary contribution.** The Mondorf et al. (2025) ensemble paper comes closest by implementing union/intersection operations, but treats it as a practical combination strategy, not an analytical study of agreement.\n\n2. **The evidence strongly suggests methods disagree substantially:**\n   - Edge Pruning finds circuits with <50% of the edges that ACDC/EAP find (Bhaskar et al.)\n   - High node overlap does NOT imply high faithfulness (Hanna et al.)\n   - Even a SINGLE method (EAP-IG) produces circuits with Jaccard ~0.56 under bootstrap resampling (Méloux et al.)\n   - Different methods preserve/prune different cooperative components (HAP paper)\n\n3. **The gap is clear:** Nobody has systematically run N methods on the same tasks, binarized the outputs, computed pairwise Jaccard / agreement matrices, and analyzed WHERE methods agree vs. disagree (e.g., by layer, by component type, by edge importance rank). A \"cross-method binary consensus\" study would be novel.\n\n4. **The Méloux et al. variance paper is the strongest cautionary result:** If intra-method variance is already high (Jaccard 0.56), cross-method consensus may be even lower, or the consensus signal may be more robust than any individual method (which is the hypothesis behind ensembling in Mondorf et al.)."
      }
    ],
    "totalDurationMs": 206231,
    "totalTokens": 43939,
    "totalToolUseCount": 35,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 40127,
      "output_tokens": 3117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 692
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3117,
          "cache_read_input_tokens": 40127,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 692,
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
      "otherToolCount": 35
    }
  },
  "sourceToolAssistantUUID": "588fb5df-a246-4538-8108-9e1ef3279fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T22:11:54.800Z_

<details><summary>↩ Tool result · `toolu_011k1dq6zk5AsEF3sipmxFHp`</summary>

```text


Here is the compiled literature survey table. I excluded papers that are only workshop papers, papers not yet accepted at the target venues, and papers outside the scope (ICLR 2026, general XAI, etc.).

---

| Paper Title | Conference + Year | Main Contribution | URL |
|---|---|---|---|
| **Sparse Autoencoders Find Highly Interpretable Features in Language Models** | ICLR 2024 | Uses sparse autoencoders to discover monosemantic, interpretable features in LM residual streams, resolving superposition and enabling finer-grained causal analysis of circuits (e.g., IOI task) than neuron-level methods. | [OpenReview](https://openreview.net/forum?id=F76bwRSLeK) |
| **Towards Best Practices of Activation Patching in Language Models: Metrics and Methods** | ICLR 2024 | Systematically examines how methodological choices (corruption method, evaluation metric) in activation patching affect circuit discovery results, and provides best-practice recommendations for reliable circuit analysis. | [OpenReview](https://openreview.net/forum?id=Hf17y6u9BC) |
| **Circuit Component Reuse Across Tasks in Transformer Language Models** | ICLR 2024 | Demonstrates that circuits are not purely task-specific: the IOI circuit in GPT-2 is ~78% reused for the Colored Objects task, providing evidence that circuit-level insights generalize across tasks. | [arXiv](https://arxiv.org/abs/2310.08744) |
| **Successor Heads: Recurring, Interpretable Attention Heads In The Wild** | ICLR 2024 | Discovers and mechanistically explains "successor heads" — attention heads that perform incrementation (e.g., Monday→Tuesday) — recurring across architectures from 31M to 12B parameters. | [OpenReview](https://openreview.net/forum?id=kvcbV8KQsi) |
| **Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models** | ICLR 2025 (Oral) | Combines SAE-based dictionary learning with causal analysis to discover sparse feature circuits — human-interpretable causal subgraphs at the SAE-feature level — and demonstrates downstream editing (SHIFT) and unsupervised pipeline for thousands of circuits. | [OpenReview](https://openreview.net/forum?id=I4e82CIDxv) |
| **Scaling and Evaluating Sparse Autoencoders** | ICLR 2025 (Oral) | Proposes k-sparse autoencoders with systematic scaling laws; trains a 16M-latent SAE on GPT-4 activations; introduces new evaluation metrics for feature quality (recovery, explainability, downstream sparsity). Foundational infrastructure for SAE-based circuit work. | [OpenReview](https://openreview.net/forum?id=tcsZt9ZNKD) |
| **Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition** | ICLR 2025 | Introduces CD-T, which reduces automated circuit discovery runtime from hours to seconds while achieving 97% avg ROC AUC on standard benchmarks (IOI, greater-than, docstring), and supports circuits at any granularity level. | [arXiv](https://arxiv.org/abs/2407.00886) |
| **The Computational Complexity of Circuit Discovery for Inner Interpretability** | ICLR 2025 (Spotlight) | Proves that many circuit-finding queries are NP-hard / Σ²_p-hard and inapproximable; identifies tractable sub-queries that retain useful affordances, establishing theoretical limits of automated circuit discovery. | [OpenReview](https://openreview.net/forum?id=QogcGNXJVw) |
| **Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?** | ICLR 2025 | Shows overwhelming non-identifiability in circuit-based interpretability: multiple circuits can replicate behavior, multiple interpretations exist per circuit, and algorithms align with different subspaces — challenging uniqueness assumptions. | [OpenReview](https://openreview.net/forum?id=5IWJBStfU7) |
| **Sparse Autoencoders Do Not Find Canonical Units of Analysis** | ICLR 2025 | Introduces SAE stitching and meta-SAEs to show SAE features are neither complete nor atomic — smaller SAEs miss information, larger SAE latents decompose into combinations — challenging the idea of a canonical feature set. | [OpenReview](https://openreview.net/forum?id=9ca9eHNrdH) |
| **Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations** | ICLR 2025 | Unifies prior mechanistic explanations of group-operation networks and translates them into compact formal proofs of model accuracy, connecting interpretability completeness to proof tightness. | [arXiv](https://arxiv.org/abs/2410.07476) |
| **Transcoders Find Interpretable LLM Feature Circuits** | NeurIPS 2024 | Introduces transcoders (sparse MLP approximations) to enable weights-based circuit analysis through MLP sublayers, overcoming a key limitation of attention-head-only circuit methods; validated on models up to 1.4B params. | [NeurIPS](https://neurips.cc/virtual/2024/poster/95736) |
| **LLM Circuit Analyses Are Consistent Across Training and Scale** | NeurIPS 2024 | Tracks circuit emergence over 300B tokens across 70M–2.8B parameter models; finds that task circuits and their algorithms emerge at consistent token counts and replicate across scale, validating small-model circuit studies. | [arXiv](https://arxiv.org/abs/2407.10827) |
| **Compact Proofs of Model Performance via Mechanistic Interpretability** | NeurIPS 2024 | Formalizes using mechanistic interpretability to derive provable accuracy bounds; demonstrates on Max-of-K transformers with 102 proof strategies, finding shorter proofs require deeper mechanistic understanding. | [NeurIPS](https://neurips.cc/virtual/2024/poster/96781) |
| **Hypothesis Testing the Circuit Hypothesis in LLMs** | NeurIPS 2024 | Formalizes circuit criteria (behavior preservation, localization, minimality) and develops hypothesis tests; finds synthetic circuits satisfy idealized properties while discovered Transformer circuits satisfy them to varying degrees. | [NeurIPS](https://neurips.cc/virtual/2024/poster/96582) |
| **InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques** | NeurIPS 2024 (D&B Track) | Creates 86 semi-synthetic transformers with known ground-truth circuits via Strict IIT training; benchmarks ACDC, Edge Attribution Patching, and Subnetwork Probing, finding ACDC and EAP-IG statistically indistinguishable. | [OpenReview](https://openreview.net/forum?id=R9gR9MPuD5) |
| **MIB: A Mechanistic Interpretability Benchmark** | ICML 2025 | Large-scale benchmark for comparing circuit localization methods; evaluates attribution and mask optimization approaches, finding them best-performing for identifying circuits in transformers. | [ICML](https://icml.cc/virtual/2025/poster/43836) |
| **Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models** | ICML 2025 | Proposes ModCirc framework for discovering task-agnostic modular circuit (MC) vocabularies — reusable functional units — addressing the poor cross-task generalizability and high per-task cost of existing circuit discovery. | [OpenReview](https://openreview.net/forum?id=do5vVfKEXZ) |
| **Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis** | ICML 2025 | Tracks circuits across fine-tuning checkpoints; shows component identity is preserved but connection strengths change; introduces circuit-aware LoRA that allocates capacity to most-altered connections for better parameter efficiency. | [OpenReview](https://openreview.net/forum?id=45EIiFd6Oa) |

---

**Notes on scope exclusions:**
- ACDC ("Towards Automated Circuit Discovery for Mechanistic Interpretability") is NeurIPS 2023, outside the requested range.
- "Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees" is ICLR 2026.
- "Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability" — submitted to ICLR 2025 but no confirmed acceptance found.
- "Scaling Sparse Feature Circuits for Studying In-Context Learning" — only found as an ICLR 2025 workshop paper, not main track.
- No ICML 2024 main-track circuit discovery papers were identified; ICML 2024 hosted a large Mechanistic Interpretability Workshop (140+ submissions) but the circuit-relevant papers there were workshop-only.

agentId: acd29577a78bc2c01 (use SendMessage with to: 'acd29577a78bc2c01' to continue this agent)
&lt;usage>total_tokens: 52265
tool_uses: 45
duration_ms: 233630&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b823c913-9973-42fd-9154-877e64bdb5b6",
  "isSidechain": false,
  "promptId": "ac1e15a4-789d-401b-936c-5f0b5ab58ba0",
  "type": "user",
  "uuid": "85f8729e-a7a0-4e11-9d5f-4c9e7f1b7341",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are conducting a literature survey on circuit discovery and mechanistic interpretability at top ML venues.\n\n**Task**: Find circuit discovery / mechanistic interpretability papers published at these venues:\n- ICLR 2024, ICLR 2025\n- NeurIPS 2024\n- ICML 2024, ICML 2025\n\nSearch using these queries:\n1. \"circuit discovery ICLR 2024 2025\"\n2. \"mechanistic interpretability NeurIPS 2024\"\n3. \"circuit discovery ICML 2024 2025\"\n4. \"automated interpretability circuits top conference 2024 2025\"\n5. \"mechanistic interpretability ICLR 2025 accepted papers\"\n\nFor each search, use WebSearch. Use WebFetch to confirm venue/year for important papers.\n\n**Output format**: A table with columns:\n- Paper title\n- Conference + Year\n- Main contribution (1-2 sentences)\n- URL\n\nOnly include papers genuinely about circuit discovery or closely related mechanistic interpretability (not general XAI or probing studies).",
    "agentId": "acd29577a78bc2c01",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is the compiled literature survey table. I excluded papers that are only workshop papers, papers not yet accepted at the target venues, and papers outside the scope (ICLR 2026, general XAI, etc.).\n\n---\n\n| Paper Title | Conference + Year | Main Contribution | URL |\n|---|---|---|---|\n| **Sparse Autoencoders Find Highly Interpretable Features in Language Models** | ICLR 2024 | Uses sparse autoencoders to discover monosemantic, interpretable features in LM residual streams, resolving superposition and enabling finer-grained causal analysis of circuits (e.g., IOI task) than neuron-level methods. | [OpenReview](https://openreview.net/forum?id=F76bwRSLeK) |\n| **Towards Best Practices of Activation Patching in Language Models: Metrics and Methods** | ICLR 2024 | Systematically examines how methodological choices (corruption method, evaluation metric) in activation patching affect circuit discovery results, and provides best-practice recommendations for reliable circuit analysis. | [OpenReview](https://openreview.net/forum?id=Hf17y6u9BC) |\n| **Circuit Component Reuse Across Tasks in Transformer Language Models** | ICLR 2024 | Demonstrates that circuits are not purely task-specific: the IOI circuit in GPT-2 is ~78% reused for the Colored Objects task, providing evidence that circuit-level insights generalize across tasks. | [arXiv](https://arxiv.org/abs/2310.08744) |\n| **Successor Heads: Recurring, Interpretable Attention Heads In The Wild** | ICLR 2024 | Discovers and mechanistically explains \"successor heads\" — attention heads that perform incrementation (e.g., Monday→Tuesday) — recurring across architectures from 31M to 12B parameters. | [OpenReview](https://openreview.net/forum?id=kvcbV8KQsi) |\n| **Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models** | ICLR 2025 (Oral) | Combines SAE-based dictionary learning with causal analysis to discover sparse feature circuits — human-interpretable causal subgraphs at the SAE-feature level — and demonstrates downstream editing (SHIFT) and unsupervised pipeline for thousands of circuits. | [OpenReview](https://openreview.net/forum?id=I4e82CIDxv) |\n| **Scaling and Evaluating Sparse Autoencoders** | ICLR 2025 (Oral) | Proposes k-sparse autoencoders with systematic scaling laws; trains a 16M-latent SAE on GPT-4 activations; introduces new evaluation metrics for feature quality (recovery, explainability, downstream sparsity). Foundational infrastructure for SAE-based circuit work. | [OpenReview](https://openreview.net/forum?id=tcsZt9ZNKD) |\n| **Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition** | ICLR 2025 | Introduces CD-T, which reduces automated circuit discovery runtime from hours to seconds while achieving 97% avg ROC AUC on standard benchmarks (IOI, greater-than, docstring), and supports circuits at any granularity level. | [arXiv](https://arxiv.org/abs/2407.00886) |\n| **The Computational Complexity of Circuit Discovery for Inner Interpretability** | ICLR 2025 (Spotlight) | Proves that many circuit-finding queries are NP-hard / Σ²_p-hard and inapproximable; identifies tractable sub-queries that retain useful affordances, establishing theoretical limits of automated circuit discovery. | [OpenReview](https://openreview.net/forum?id=QogcGNXJVw) |\n| **Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?** | ICLR 2025 | Shows overwhelming non-identifiability in circuit-based interpretability: multiple circuits can replicate behavior, multiple interpretations exist per circuit, and algorithms align with different subspaces — challenging uniqueness assumptions. | [OpenReview](https://openreview.net/forum?id=5IWJBStfU7) |\n| **Sparse Autoencoders Do Not Find Canonical Units of Analysis** | ICLR 2025 | Introduces SAE stitching and meta-SAEs to show SAE features are neither complete nor atomic — smaller SAEs miss information, larger SAE latents decompose into combinations — challenging the idea of a canonical feature set. | [OpenReview](https://openreview.net/forum?id=9ca9eHNrdH) |\n| **Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations** | ICLR 2025 | Unifies prior mechanistic explanations of group-operation networks and translates them into compact formal proofs of model accuracy, connecting interpretability completeness to proof tightness. | [arXiv](https://arxiv.org/abs/2410.07476) |\n| **Transcoders Find Interpretable LLM Feature Circuits** | NeurIPS 2024 | Introduces transcoders (sparse MLP approximations) to enable weights-based circuit analysis through MLP sublayers, overcoming a key limitation of attention-head-only circuit methods; validated on models up to 1.4B params. | [NeurIPS](https://neurips.cc/virtual/2024/poster/95736) |\n| **LLM Circuit Analyses Are Consistent Across Training and Scale** | NeurIPS 2024 | Tracks circuit emergence over 300B tokens across 70M–2.8B parameter models; finds that task circuits and their algorithms emerge at consistent token counts and replicate across scale, validating small-model circuit studies. | [arXiv](https://arxiv.org/abs/2407.10827) |\n| **Compact Proofs of Model Performance via Mechanistic Interpretability** | NeurIPS 2024 | Formalizes using mechanistic interpretability to derive provable accuracy bounds; demonstrates on Max-of-K transformers with 102 proof strategies, finding shorter proofs require deeper mechanistic understanding. | [NeurIPS](https://neurips.cc/virtual/2024/poster/96781) |\n| **Hypothesis Testing the Circuit Hypothesis in LLMs** | NeurIPS 2024 | Formalizes circuit criteria (behavior preservation, localization, minimality) and develops hypothesis tests; finds synthetic circuits satisfy idealized properties while discovered Transformer circuits satisfy them to varying degrees. | [NeurIPS](https://neurips.cc/virtual/2024/poster/96582) |\n| **InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques** | NeurIPS 2024 (D&B Track) | Creates 86 semi-synthetic transformers with known ground-truth circuits via Strict IIT training; benchmarks ACDC, Edge Attribution Patching, and Subnetwork Probing, finding ACDC and EAP-IG statistically indistinguishable. | [OpenReview](https://openreview.net/forum?id=R9gR9MPuD5) |\n| **MIB: A Mechanistic Interpretability Benchmark** | ICML 2025 | Large-scale benchmark for comparing circuit localization methods; evaluates attribution and mask optimization approaches, finding them best-performing for identifying circuits in transformers. | [ICML](https://icml.cc/virtual/2025/poster/43836) |\n| **Towards Global-level Mechanistic Interpretability: A Perspective of Modular Circuits of Large Language Models** | ICML 2025 | Proposes ModCirc framework for discovering task-agnostic modular circuit (MC) vocabularies — reusable functional units — addressing the poor cross-task generalizability and high per-task cost of existing circuit discovery. | [OpenReview](https://openreview.net/forum?id=do5vVfKEXZ) |\n| **Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis** | ICML 2025 | Tracks circuits across fine-tuning checkpoints; shows component identity is preserved but connection strengths change; introduces circuit-aware LoRA that allocates capacity to most-altered connections for better parameter efficiency. | [OpenReview](https://openreview.net/forum?id=45EIiFd6Oa) |\n\n---\n\n**Notes on scope exclusions:**\n- ACDC (\"Towards Automated Circuit Discovery for Mechanistic Interpretability\") is NeurIPS 2023, outside the requested range.\n- \"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\" is ICLR 2026.\n- \"Adaptive Circuit Behavior and Generalization in Mechanistic Interpretability\" — submitted to ICLR 2025 but no confirmed acceptance found.\n- \"Scaling Sparse Feature Circuits for Studying In-Context Learning\" — only found as an ICLR 2025 workshop paper, not main track.\n- No ICML 2024 main-track circuit discovery papers were identified; ICML 2024 hosted a large Mechanistic Interpretability Workshop (140+ submissions) but the circuit-relevant papers there were workshop-only."
      }
    ],
    "totalDurationMs": 233630,
    "totalTokens": 52265,
    "totalToolUseCount": 45,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 49607,
      "output_tokens": 2272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 383
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2272,
          "cache_read_input_tokens": 49607,
          "cache_creation_input_tokens": 383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 383,
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
      "otherToolCount": 45
    }
  },
  "sourceToolAssistantUUID": "b823c913-9973-42fd-9154-877e64bdb5b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "85f8729e-a7a0-4e11-9d5f-4c9e7f1b7341",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature review on circuit discovery methods comparison",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---

### Tool result

_source line 24 · 2026-05-12T22:14:23.486Z_

<details><summary>↩ Tool result · `toolu_01JX4st1y5kYpBpUAVKFTMdz`</summary>

```text
Now I have a comprehensive picture. Let me compile the findings.

---

## Literature Survey Results: Multi-Method Circuit Aggregation / Consensus Circuit Discovery

### Critical Finding: No paper proposes exactly "Cross-method Stability Scoring" (CSS) as described — binary consensus across fundamentally different circuit discovery algorithms (ACDC, EAP, SP, etc.). However, two papers are close enough to constitute partial novelty threats.

---

### Paper 1 (HIGHEST THREAT): CIRCUS

- **Title**: CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles
- **Authors**: Swapnil Parekh
- **Year/Venue**: March 2026, arXiv preprint (2603.00523)
- **URL**: https://arxiv.org/abs/2603.00523
- **Approach**: Computes per-edge inclusion frequencies by running ONE attribution method under multiple pruning threshold configurations (non-nested pairs of node/edge thresholds). Assigns each edge a stability score s(e) in [0,1]. Extracts a "consensus circuit" = edges present in ALL configurations. Produces a core/contingent/noise taxonomy.
- **Key distinction from CSS**: CIRCUS varies **hyperparameters within a single method** (pruning thresholds on one attribution graph), NOT across fundamentally different algorithms. It does not run ACDC + EAP + SP and intersect. The "configuration family" is threshold pairs, not different algorithmic approaches.
- **Similarity to CSS**: HIGH conceptually (stability scoring, consensus extraction, per-edge inclusion frequency). The mathematical framing is very similar — both assign edges a robustness score based on how consistently they appear. But the source of variation is different: CIRCUS varies thresholds within one method; CSS would vary across fundamentally different methods.

### Paper 2 (MODERATE THREAT): Mondorf et al. — Ensemble Strategies for Circuit Localization

- **Title**: BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods
- **Authors**: Philipp Mondorf, Mingyang Wang, Sebastian Gerstner, Ahmad Dawar Hakimi, Yihong Liu, Leonor Veloso, Shijia Zhou, Hinrich Schütze, Barbara Plank
- **Year/Venue**: October 2025, BlackboxNLP-2025 Workshop (ACL Anthology)
- **URL**: https://arxiv.org/abs/2510.06811
- **Approach**: Combines outputs from multiple circuit discovery methods via parallel ensembling (averaging continuous attribution scores from EAP, EAP-IG-inputs, EAP-IG-activations) and sequential ensembling (using EAP-IG scores to warm-start edge pruning). Also tested min (intersection) and max (union) aggregation. Hybrid ensemble combines all four methods.
- **Key distinction from CSS**: They aggregate **continuous scores** (mean/min/max of attribution values), not binary edge-in/edge-out decisions. The methods combined are mostly EAP variants + edge pruning — not the full diversity of ACDC + EAP + SP. No explicit "stability score" or "binary consensus" framing.
- **Similarity to CSS**: MODERATE. This is the closest to multi-method aggregation in the literature. They do combine fundamentally different method families (attribution-based + pruning-based). However, the aggregation is score averaging rather than binary consensus, and the paper is a short shared task submission (not a full method paper).

### Paper 3 (LOW-MODERATE THREAT): Méloux et al. — Variance Analysis

- **Title**: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis
- **Authors**: Maxime Méloux, François Portet, Maxime Peyrard
- **Year/Venue**: October 2025, arXiv preprint (2510.00845)
- **URL**: https://arxiv.org/abs/2510.00845
- **Approach**: Analyzes variance of EAP-IG across data resampling, hyperparameter changes, and approximation choices. Shows that varying multiple parameters (resampling strategy, aggregation method, intervention type, EAP method, pruning strategy) yields very different circuits. Visualizes union and median circuits.
- **Key distinction from CSS**: This is purely a **diagnostic/analysis** paper. It does not propose aggregation as a solution — it identifies the problem that circuits are unstable. Stays within the EAP family; does not compare across ACDC/SP.
- **Similarity to CSS**: LOW. Motivates the need for CSS-like approaches but doesn't propose one.

### Paper 4 (LOW THREAT): Nikankin et al. — Bootstrapping for Edge Stability

- **Title**: BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection
- **Authors**: Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov
- **Year/Venue**: October 2025, BlackboxNLP-2025 Workshop
- **URL**: https://arxiv.org/abs/2510.25786
- **Approach**: Bootstraps EAP-IG scores across data resamples to identify edges with consistent score signs; filters out unstable edges. Combines with ILP-based selection and ratio-based prioritization.
- **Key distinction from CSS**: Single method (EAP-IG) only. Bootstrapping is across **data samples**, not across different algorithms. No cross-method component.
- **Similarity to CSS**: LOW. The bootstrapping stability idea is related, but it's within-method data resampling, not cross-method.

### Paper 5 (LOW THREAT): Certified Circuits

- **Title**: Certified Circuits: Stability Guarantees for Mechanistic Circuits
- **Authors**: Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer
- **Year/Venue**: February 2026, arXiv preprint (2602.22968)
- **URL**: https://arxiv.org/abs/2602.22968
- **Approach**: Wraps any single circuit discovery algorithm with a certification layer using randomized data subsampling. Certifies stability under bounded dataset edits via deletion-based randomized smoothing. Abstains on unstable neurons.
- **Key distinction from CSS**: Method-agnostic wrapper but applied to ONE method at a time. Does not aggregate across methods.
- **Similarity to CSS**: LOW. Certifies single-method output, does not combine multiple methods.

### Paper 6 (CONTEXT): InterpBench

- **Title**: InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques
- **Year/Venue**: NeurIPS 2024 (Datasets & Benchmarks)
- **URL**: https://arxiv.org/abs/2407.14494
- **Relevance**: Compares ACDC, SP, EAP, EAP-IG on the same tasks with ground-truth circuits, showing they produce different results. Does NOT propose aggregation — purely evaluation.

### Paper 7 (CONTEXT): Miller et al.

- **Title**: Transformer Circuit Faithfulness Metrics are not Robust
- **Year/Venue**: CoLM 2024
- **URL**: https://arxiv.org/abs/2407.08734
- **Relevance**: Shows faithfulness metrics are highly sensitive to ablation methodology choices. Motivates the need for robust approaches but proposes no aggregation.

---

## Summary Assessment

**No paper found proposing the specific CSS approach of: running multiple fundamentally different circuit discovery algorithms (ACDC, EAP, SP, edge pruning), converting each output to binary edge inclusion, and computing a binary consensus/stability score across methods.**

The closest threats are:
1. **CIRCUS** — same mathematical spirit (per-edge stability scores, consensus extraction) but varies thresholds within ONE method, not across algorithms.
2. **Mondorf et al.** — actually combines different method families via score averaging, but uses continuous score aggregation (not binary consensus) and is a short workshop paper, not a full method contribution.

The CSS idea of running N fundamentally different circuit discovery algorithms and marking edges as "stable" if found by K-of-N methods remains novel. The key differentiator is the **cross-algorithm** dimension — all existing work either (a) varies hyperparameters within one method, or (b) averages continuous scores from method variants rather than applying binary consensus across truly different algorithmic families.

agentId: ab23d576408a4772b (use SendMessage with to: 'ab23d576408a4772b' to continue this agent)
&lt;usage>total_tokens: 42430
tool_uses: 32
duration_ms: 391341&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd4dbeda-fc01-4b07-b7d3-f1066a412592",
  "isSidechain": false,
  "promptId": "ac1e15a4-789d-401b-936c-5f0b5ab58ba0",
  "type": "user",
  "uuid": "87c17282-3df3-443c-97ca-f7fbc1fba390",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are conducting a literature survey on circuit discovery in mechanistic interpretability.\n\n**Task**: Find papers that propose aggregating or ensembling results from multiple circuit discovery methods to get more robust circuits. This is the most critical novelty threat - if someone has done \"multi-method circuit aggregation\" or \"consensus circuit discovery\", we need to know.\n\nSearch using these keyword combinations (at least 3 different searches):\n1. \"circuit aggregation ensemble mechanistic interpretability\"\n2. \"robust circuit discovery multi-method consensus\"\n3. \"combining circuit discovery methods transformers\"\n4. \"cross-method circuit stability scoring\"\n5. \"circuit discovery robustness ensemble neural network\"\n\nFor each search, use WebSearch. For any highly relevant paper found, use WebFetch on its arXiv abstract page to confirm the content.\n\n**Output format**: For each relevant paper found, report:\n- Title\n- Authors\n- Year / Venue\n- URL\n- What aggregation/ensemble approach they use\n- How similar it is to \"Cross-method Stability Scoring\" (CSS) - binary consensus across methods\n\nIf nothing found, explicitly state \"No papers found proposing multi-method circuit aggregation.\" Be very thorough.",
    "agentId": "ab23d576408a4772b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Let me compile the findings.\n\n---\n\n## Literature Survey Results: Multi-Method Circuit Aggregation / Consensus Circuit Discovery\n\n### Critical Finding: No paper proposes exactly \"Cross-method Stability Scoring\" (CSS) as described — binary consensus across fundamentally different circuit discovery algorithms (ACDC, EAP, SP, etc.). However, two papers are close enough to constitute partial novelty threats.\n\n---\n\n### Paper 1 (HIGHEST THREAT): CIRCUS\n\n- **Title**: CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\n- **Authors**: Swapnil Parekh\n- **Year/Venue**: March 2026, arXiv preprint (2603.00523)\n- **URL**: https://arxiv.org/abs/2603.00523\n- **Approach**: Computes per-edge inclusion frequencies by running ONE attribution method under multiple pruning threshold configurations (non-nested pairs of node/edge thresholds). Assigns each edge a stability score s(e) in [0,1]. Extracts a \"consensus circuit\" = edges present in ALL configurations. Produces a core/contingent/noise taxonomy.\n- **Key distinction from CSS**: CIRCUS varies **hyperparameters within a single method** (pruning thresholds on one attribution graph), NOT across fundamentally different algorithms. It does not run ACDC + EAP + SP and intersect. The \"configuration family\" is threshold pairs, not different algorithmic approaches.\n- **Similarity to CSS**: HIGH conceptually (stability scoring, consensus extraction, per-edge inclusion frequency). The mathematical framing is very similar — both assign edges a robustness score based on how consistently they appear. But the source of variation is different: CIRCUS varies thresholds within one method; CSS would vary across fundamentally different methods.\n\n### Paper 2 (MODERATE THREAT): Mondorf et al. — Ensemble Strategies for Circuit Localization\n\n- **Title**: BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods\n- **Authors**: Philipp Mondorf, Mingyang Wang, Sebastian Gerstner, Ahmad Dawar Hakimi, Yihong Liu, Leonor Veloso, Shijia Zhou, Hinrich Schütze, Barbara Plank\n- **Year/Venue**: October 2025, BlackboxNLP-2025 Workshop (ACL Anthology)\n- **URL**: https://arxiv.org/abs/2510.06811\n- **Approach**: Combines outputs from multiple circuit discovery methods via parallel ensembling (averaging continuous attribution scores from EAP, EAP-IG-inputs, EAP-IG-activations) and sequential ensembling (using EAP-IG scores to warm-start edge pruning). Also tested min (intersection) and max (union) aggregation. Hybrid ensemble combines all four methods.\n- **Key distinction from CSS**: They aggregate **continuous scores** (mean/min/max of attribution values), not binary edge-in/edge-out decisions. The methods combined are mostly EAP variants + edge pruning — not the full diversity of ACDC + EAP + SP. No explicit \"stability score\" or \"binary consensus\" framing.\n- **Similarity to CSS**: MODERATE. This is the closest to multi-method aggregation in the literature. They do combine fundamentally different method families (attribution-based + pruning-based). However, the aggregation is score averaging rather than binary consensus, and the paper is a short shared task submission (not a full method paper).\n\n### Paper 3 (LOW-MODERATE THREAT): Méloux et al. — Variance Analysis\n\n- **Title**: Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\n- **Authors**: Maxime Méloux, François Portet, Maxime Peyrard\n- **Year/Venue**: October 2025, arXiv preprint (2510.00845)\n- **URL**: https://arxiv.org/abs/2510.00845\n- **Approach**: Analyzes variance of EAP-IG across data resampling, hyperparameter changes, and approximation choices. Shows that varying multiple parameters (resampling strategy, aggregation method, intervention type, EAP method, pruning strategy) yields very different circuits. Visualizes union and median circuits.\n- **Key distinction from CSS**: This is purely a **diagnostic/analysis** paper. It does not propose aggregation as a solution — it identifies the problem that circuits are unstable. Stays within the EAP family; does not compare across ACDC/SP.\n- **Similarity to CSS**: LOW. Motivates the need for CSS-like approaches but doesn't propose one.\n\n### Paper 4 (LOW THREAT): Nikankin et al. — Bootstrapping for Edge Stability\n\n- **Title**: BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection\n- **Authors**: Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov\n- **Year/Venue**: October 2025, BlackboxNLP-2025 Workshop\n- **URL**: https://arxiv.org/abs/2510.25786\n- **Approach**: Bootstraps EAP-IG scores across data resamples to identify edges with consistent score signs; filters out unstable edges. Combines with ILP-based selection and ratio-based prioritization.\n- **Key distinction from CSS**: Single method (EAP-IG) only. Bootstrapping is across **data samples**, not across different algorithms. No cross-method component.\n- **Similarity to CSS**: LOW. The bootstrapping stability idea is related, but it's within-method data resampling, not cross-method.\n\n### Paper 5 (LOW THREAT): Certified Circuits\n\n- **Title**: Certified Circuits: Stability Guarantees for Mechanistic Circuits\n- **Authors**: Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer\n- **Year/Venue**: February 2026, arXiv preprint (2602.22968)\n- **URL**: https://arxiv.org/abs/2602.22968\n- **Approach**: Wraps any single circuit discovery algorithm with a certification layer using randomized data subsampling. Certifies stability under bounded dataset edits via deletion-based randomized smoothing. Abstains on unstable neurons.\n- **Key distinction from CSS**: Method-agnostic wrapper but applied to ONE method at a time. Does not aggregate across methods.\n- **Similarity to CSS**: LOW. Certifies single-method output, does not combine multiple methods.\n\n### Paper 6 (CONTEXT): InterpBench\n\n- **Title**: InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques\n- **Year/Venue**: NeurIPS 2024 (Datasets & Benchmarks)\n- **URL**: https://arxiv.org/abs/2407.14494\n- **Relevance**: Compares ACDC, SP, EAP, EAP-IG on the same tasks with ground-truth circuits, showing they produce different results. Does NOT propose aggregation — purely evaluation.\n\n### Paper 7 (CONTEXT): Miller et al.\n\n- **Title**: Transformer Circuit Faithfulness Metrics are not Robust\n- **Year/Venue**: CoLM 2024\n- **URL**: https://arxiv.org/abs/2407.08734\n- **Relevance**: Shows faithfulness metrics are highly sensitive to ablation methodology choices. Motivates the need for robust approaches but proposes no aggregation.\n\n---\n\n## Summary Assessment\n\n**No paper found proposing the specific CSS approach of: running multiple fundamentally different circuit discovery algorithms (ACDC, EAP, SP, edge pruning), converting each output to binary edge inclusion, and computing a binary consensus/stability score across methods.**\n\nThe closest threats are:\n1. **CIRCUS** — same mathematical spirit (per-edge stability scores, consensus extraction) but varies thresholds within ONE method, not across algorithms.\n2. **Mondorf et al.** — actually combines different method families via score averaging, but uses continuous score aggregation (not binary consensus) and is a short workshop paper, not a full method contribution.\n\nThe CSS idea of running N fundamentally different circuit discovery algorithms and marking edges as \"stable\" if found by K-of-N methods remains novel. The key differentiator is the **cross-algorithm** dimension — all existing work either (a) varies hyperparameters within one method, or (b) averages continuous scores from method variants rather than applying binary consensus across truly different algorithmic families."
      }
    ],
    "totalDurationMs": 391341,
    "totalTokens": 42430,
    "totalToolUseCount": 32,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 39557,
      "output_tokens": 2064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 808
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2064,
          "cache_read_input_tokens": 39557,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 808,
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
  "sourceToolAssistantUUID": "bd4dbeda-fc01-4b07-b7d3-f1066a412592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-12T22:14:26.873Z_

<details><summary>Logged reasoning block</summary>

```text
All four agents have returned comprehensive results. Let me now compile the findings into the required output file and register it as an artifact. Let me also load the MCP tools I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87c17282-3df3-443c-97ca-f7fbc1fba390",
  "isSidechain": false,
  "requestId": "req_011CaySmw6k37tvaiKLQd5xA",
  "type": "assistant",
  "uuid": "af2aa9b1-1608-4323-b04d-16fd2af2f660",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWwqA5T5WqpTauMZGxSKo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4791,
      "cache_creation_input_tokens": 6802,
      "cache_read_input_tokens": 24970,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4791,
          "output_tokens": 178,
          "cache_read_input_tokens": 24970,
          "cache_creation_input_tokens": 6802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6802
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

_source line 26 · 2026-05-12T22:14:27.849Z_

四个方向的调研结果已返回。现在汇总写入产出文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af2aa9b1-1608-4323-b04d-16fd2af2f660",
  "isSidechain": false,
  "requestId": "req_011CaySmw6k37tvaiKLQd5xA",
  "type": "assistant",
  "uuid": "dd1318bf-1860-454b-845b-e035e0af00bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWwqA5T5WqpTauMZGxSKo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4791,
      "cache_creation_input_tokens": 6802,
      "cache_read_input_tokens": 24970,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4791,
          "output_tokens": 178,
          "cache_read_input_tokens": 24970,
          "cache_creation_input_tokens": 6802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6802
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

_source line 27 · 2026-05-12T22:14:28.810Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AKWWt5fNb1qVYrEHTzn8am`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd1318bf-1860-454b-845b-e035e0af00bd",
  "isSidechain": false,
  "requestId": "req_011CaySmw6k37tvaiKLQd5xA",
  "type": "assistant",
  "uuid": "92ff2e55-82dc-4a9d-9338-c722cab21e5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWwqA5T5WqpTauMZGxSKo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4791,
      "cache_creation_input_tokens": 6802,
      "cache_read_input_tokens": 24970,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4791,
          "output_tokens": 178,
          "cache_read_input_tokens": 24970,
          "cache_creation_input_tokens": 6802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6802
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

_source line 28 · 2026-05-12T22:14:28.814Z_

<details><summary>↩ Tool result · `toolu_01AKWWt5fNb1qVYrEHTzn8am`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92ff2e55-82dc-4a9d-9338-c722cab21e5c",
  "isSidechain": false,
  "promptId": "ac1e15a4-789d-401b-936c-5f0b5ab58ba0",
  "type": "user",
  "uuid": "be092e04-11fe-478b-87ce-7eb6af3694a2",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "92ff2e55-82dc-4a9d-9338-c722cab21e5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T22:16:12.435Z_

<details open><summary>🔧 Tool call — Write · `toolu_01JYAVxaD8PChTg5KgKGo2bJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "content": "# Circuit Discovery Related Work Notes (2024-2026)\n\n> 调研日期：2026-05-12 | 项目：structfuse-context\n> 核心问题：CSS（Cross-method Stability Scoring）的 novelty 是否站得住？\n\n---\n\n## 1. 方法一致性比较（Novelty 关键）\n\n**结论：没有论文以\"跨方法一致性分析\"为核心贡献。** 多篇论文在评估新方法时附带比较了不同方法的表现，但比较维度是各方法 vs ground-truth 的 faithfulness/AUC，而非方法之间的 pairwise agreement。\n\n### 直接比较多方法的论文\n\n| 论文 | 方法比较 | 比较维度 | 是否测量方法间一致性 |\n|------|----------|----------|---------------------|\n| Conmy et al. \"Towards Automated Circuit Discovery\" (NeurIPS 2023) | ACDC vs SP vs HISP | ROC AUC vs ground-truth | ❌ 不测方法间 overlap |\n| Syed et al. \"Attribution Patching Outperforms Automated Circuit Discovery\" (BlackboxNLP 2024) | EAP vs ACDC vs SP vs HISP | AUC vs ground-truth | ❌ |\n| Bhaskar et al. \"Finding Transformer Circuits with Edge Pruning\" (NeurIPS 2024 Spotlight) | Edge Pruning vs ACDC vs EAP | Faithfulness at various sparsities | ❌ 但隐含表明方法差异大：EP 找到的边不到 ACDC/EAP 的一半 |\n| Hsu et al. \"CD-T\" (ICLR 2025) | CD-T vs ACDC vs EAP | ROC AUC vs ground-truth | ❌ |\n| Edin et al. \"GIM\" (2025, arXiv) | GIM vs EActP vs EAP vs EAP-IG vs NAP vs IFR vs UGS | Faithfulness metrics | ❌ |\n| InterpBench (NeurIPS 2024 D&B) | ACDC vs EAP vs SP on 86 semi-synthetic models | Ground-truth recovery | ❌ 但发现 ACDC 与 EAP-IG 统计上不可区分 |\n\n### 最接近\"一致性分析\"的论文\n\n**Hanna et al. \"Have Faith in Faithfulness: Going Beyond Circuit Overlap\" (2024, arXiv 2403.17806)**\n- 比较 EAP vs EAP-IG 的 **node overlap**，发现两者 overlap 很高但 faithfulness 差异大\n- 核心结论：overlap ≠ faithfulness，高 overlap 不代表电路功能等价\n- **与 CSS 的关系**：这是对 overlap-based 评估的警告，但不是跨方法一致性的系统研究\n\n**Méloux et al. \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\" (2025, arXiv 2510.00845)**\n- 对 EAP-IG 做 bootstrap resampling，发现 **单方法内** Jaccard 仅 0.561\n- 超参数变化导致 Jaccard 从 0.086 到 1.0 不等\n- **与 CSS 的关系**：揭示了电路不稳定性问题（motivates CSS），但仅限单方法内变异，未跨方法\n\n**总结：无人系统测量不同方法间的 pairwise Jaccard / agreement matrix。这正是 CSS 要填补的空白。**\n\n---\n\n## 2. Circuit Aggregation / Ensemble（Novelty 威胁）\n\n### 🔴 最高威胁：CIRCUS\n\n**CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles**\n- 作者：Swapnil Parekh\n- 时间：2026年3月, arXiv 2603.00523\n- 方法：对单一归因方法，在多组剪枝阈值配置下运行，计算每条边的 inclusion frequency → stability score s(e) ∈ [0,1]，提取 consensus circuit（所有配置下都存在的边），分为 core/contingent/noise\n- **与 CSS 的区别**：CIRCUS 变化的是**单方法内的超参数**（剪枝阈值），不是跨不同算法族。它不运行 ACDC + EAP + SP 然后求交集\n- **与 CSS 的相似度**：数学框架高度相似（per-edge stability scoring, consensus extraction, core/contingent taxonomy）\n- **威胁评级**：🔴 HIGH — 概念上最接近，但维度不同（intra-method vs cross-method）\n\n### 🟡 中等威胁：Mondorf et al. Ensemble\n\n**Mondorf et al. \"Exploring Ensemble Strategies for Circuit Localization Methods\" (BlackboxNLP 2025, arXiv 2510.06811)**\n- 方法：组合 EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning 的输出\n  - Max = union（任一方法选中）\n  - Min = intersection（所有方法选中）\n  - Mean = 连续分数平均\n  - Hybrid = 并行+串行组合\n- 结果：Mean > union/intersection，Hybrid 最佳 (CMD 0.03, CPR 1.83)\n- **与 CSS 的区别**：聚合的是**连续归因分数**（mean/min/max），不是二值 edge-in/edge-out；方法主要是 EAP 变体，不是真正不同的算法族；workshop 短文非完整方法贡献\n- **与 CSS 的相似度**：确实跨方法组合（attribution + pruning），实现了 union/intersection 操作\n- **威胁评级**：🟡 MODERATE — 最接近跨方法聚合，但 framing 为 shared task 工程方案非方法论贡献\n\n### 🟢 低威胁\n\n| 论文 | 方法 | 与 CSS 区别 | 威胁 |\n|------|------|------------|------|\n| Nikankin et al. \"Improving Circuit Faithfulness via Better Edge Selection\" (BlackboxNLP 2025) | Bootstrap EAP-IG scores across data resamples | 单方法 + 数据重采样，非跨方法 | 🟢 LOW |\n| Anani et al. \"Certified Circuits: Stability Guarantees\" (2026, arXiv 2602.22968) | 随机化数据子采样 + 删除平滑认证 | 单方法 wrapper，不聚合多方法 | 🟢 LOW |\n| Miller et al. \"Transformer Circuit Faithfulness Metrics are not Robust\" (CoLM 2024) | 分析 faithfulness 指标敏感性 | 纯诊断，不提出聚合 | 🟢 LOW |\n\n**总结：没有论文提出 CSS 的精确方案——运行 N 种根本不同的算法族（ACDC, EAP, SP, EP），对每种输出做二值化，然后计算跨方法 binary consensus。CIRCUS 最接近但维度不同（intra-method threshold variation vs cross-method）。Mondorf et al. 确实跨方法但用连续分数聚合且为 workshop 工程方案。**\n\n---\n\n## 3. 2024-2026 新方法\n\n| 方法 | 论文 | 年份 | 会议 | 算法族 | 备注 |\n|------|------|------|------|--------|------|\n| CD-T | Hsu et al. \"Efficient Automated Circuit Discovery using Contextual Decomposition\" | 2024 | ICLR 2025 | 分解 (decomposition) | 无需 activation patching，秒级发现，97% AUC |\n| DiscoGP | Yu et al. \"Functional Faithfulness in the Wild\" | 2024 | ICML 2024 | 可微剪枝 | 联合权重+边剪枝，端到端学习二值 mask |\n| Transcoders | Dunefsky et al. \"Transcoders Find Interpretable LLM Feature Circuits\" | 2024 | NeurIPS 2024 | 稀疏替换模型 | 用稀疏 MLP 替换原 MLP，实现 weights-based 电路分析 |\n| Sparse Feature Circuits | Marks et al. \"Discovering and Editing Interpretable Causal Graphs\" | 2024 | ICLR 2025 (Oral) | 归因 + SAE 特征 | 在 SAE 特征级别发现电路，支持 SHIFT 编辑 |\n| Circuit Tracing | Ameisen, Olah et al. (Anthropic) \"Attribution Graphs\" | 2025 | Tech Report | 稀疏替换 + 归因 | Cross-layer transcoders → per-prompt DAG，应用于 Claude 3.5 |\n| GIM | Edin et al. \"Improved Interpretability for LLMs\" | 2025 | arXiv | 梯度修正 | 修正 softmax/LayerNorm 反传，MIB 排行榜第一 |\n| HAP | Gu et al. \"Hybrid Attribution and Pruning Framework\" | 2025 | arXiv | 混合 (EAP → EP) | 先 EAP 粗筛再 EP 精修，比 EP 快 46% |\n| ModCirc | He et al. \"Modular Circuits of LLMs\" | 2025 | ICML 2025 | 模块化分解 | 发现跨任务共享的模块化电路词表 |\n| Stream | Rosser et al. \"Scaling up MI to Long Context\" | 2025 | arXiv | 层次化剪枝 | O(T log T) 稀疏注意力 mask，支持 100K+ token |\n| Weight-Sparse Circuits | Gao et al. (OpenAI) | 2025 | arXiv | 稀疏训练 | 极端权重稀疏 (~1/1000) → 天然可解释电路 |\n| Formal MI | Hadad et al. \"Automated Circuit Discovery with Provable Guarantees\" | 2026 | ICLR 2026 | 验证 (verification) | 首个可证明保证的电路发现（鲁棒性 + 最小性） |\n| SVD Directional Masking | Ahmad et al. \"Beyond Components\" | 2025 | arXiv | SVD + 可微 mask | 揭示单头内叠加子功能 |\n\n---\n\n## 4. 顶会论文列表\n\n### ICLR 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Autoencoders Find Highly Interpretable Features in LMs | SAE 发现单语义特征，解决 superposition |\n| Towards Best Practices of Activation Patching in LMs | 系统分析 patching 方法选择对电路发现的影响 |\n| Circuit Component Reuse Across Tasks | IOI 电路 ~78% 被 Colored Objects 复用 |\n| Successor Heads: Recurring Interpretable Attention Heads | 发现跨架构的 successor heads（递增操作） |\n\n### ICLR 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Feature Circuits (Oral) | SAE 特征级电路发现 + SHIFT 编辑 |\n| Scaling and Evaluating Sparse Autoencoders (Oral) | k-sparse SAE 扩展到 GPT-4，16M latents |\n| CD-T: Contextual Decomposition for Circuit Discovery | 秒级电路发现，97% AUC |\n| Computational Complexity of Circuit Discovery (Spotlight) | 证明多数电路发现查询 NP-hard |\n| Everything Everywhere All at Once: Is MI Identifiable? | 电路非唯一性：多电路可复现同一行为 |\n| SAEs Do Not Find Canonical Units of Analysis | SAE stitching 证明特征非原子/非完备 |\n| Unifying and Verifying Mechanistic Interpretations | 统一群运算网络的机制解释并形式化证明 |\n\n### NeurIPS 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Finding Transformer Circuits with Edge Pruning (Spotlight) | EP 方法，更忠实且更稀疏，扩展到 13B |\n| Transcoders Find Interpretable LLM Feature Circuits | 稀疏 MLP 替换实现 weights-based 电路分析 |\n| LLM Circuit Analyses Are Consistent Across Training and Scale | 电路在训练过程和模型规模间一致出现 |\n| Compact Proofs of Model Performance via MI | MI → 可证明的准确率下界 |\n| Hypothesis Testing the Circuit Hypothesis | 形式化电路假设的假设检验 |\n| InterpBench: Semi-Synthetic Transformers for Evaluating MI | 86 个有 ground-truth 的半合成模型评估基准 |\n\n### ICML 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| MIB: A Mechanistic Interpretability Benchmark | 标准化电路定位基准，归因+mask 优化方法领先 |\n| ModCirc: Modular Circuits of LLMs | 跨任务模块化电路词表 |\n| Towards Understanding Fine-Tuning via Circuit Analysis | 追踪微调中电路变化，提出 circuit-aware LoRA |\n\n---\n\n## 5. Novelty 评估\n\n### CSS 的 novelty 站得住吗？**站得住，但需要精确定位差异化。**\n\n#### ✅ Novelty 成立的理由\n\n1. **无人做跨算法族的 binary consensus**：所有现有工作要么是单方法内变异分析（CIRCUS, Méloux），要么是连续分数聚合（Mondorf），要么只是各方法 vs ground-truth 的性能比较。CSS 提出跨 N 种根本不同的算法族做二值共识，这个精确配方是新的。\n\n2. **方法间差异的系统分析是空白**：没有论文报告过不同方法的 pairwise Jaccard matrix / agreement heatmap。大量论文隐含表明方法差异很大（EP 边数不到 ACDC 一半），但无人将此作为研究问题。\n\n3. **core/contingent 分类的跨方法版本未被探索**：CIRCUS 做了类似的 core/contingent/noise taxonomy，但基于 intra-method threshold variation。CSS 基于 cross-method agreement 做分类，维度不同且信息更丰富。\n\n#### ⚠️ 需要小心的 Novelty 威胁\n\n1. **CIRCUS (2603.00523)** 是最大威胁。虽然维度不同，但 reviewer 可能认为 conceptual overlap 太大。**建议**：论文中必须明确讨论 CIRCUS，强调区别（intra-method hyperparameter variation vs cross-method algorithmic diversity），并论证为何跨方法维度更有意义（不同方法有不同 inductive bias，而阈值变化只探索同一方法的 Rashomon set）。\n\n2. **Mondorf et al.** 已经实现了 union/intersection 操作并发现 mean 优于两者。CSS 需要论证 binary consensus 相比连续分数平均的优势（如可解释性、对阈值选择的鲁棒性）。\n\n3. **Méloux et al. 的 intra-method instability 问题**：如果单方法内 Jaccard 仅 0.56，跨方法 consensus 可能更低。需要实验证明 CSS-core 的 faithfulness 确实优于单方法，否则 consensus 可能只是噪声的交集。\n\n4. **非唯一性问题 (ICLR 2025 \"Everything Everywhere All at Once\")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。\n\n#### 🎯 差异化建议\n\n- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。\n- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。\n- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be092e04-11fe-478b-87ce-7eb6af3694a2",
  "isSidechain": false,
  "requestId": "req_011CaySnL1Q4uVu1Gk7jhoJ3",
  "type": "assistant",
  "uuid": "b6883c92-982c-414d-b9be-8eed3a44832d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DAZ866gJesKTxRaV24H2p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5844,
      "cache_read_input_tokens": 31772,
      "output_tokens": 4842,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4842,
          "cache_read_input_tokens": 31772,
          "cache_creation_input_tokens": 5844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5844
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

_source line 30 · 2026-05-12T22:16:12.479Z_

<details><summary>↩ Tool result · `toolu_01JYAVxaD8PChTg5KgKGo2bJ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6883c92-982c-414d-b9be-8eed3a44832d",
  "isSidechain": false,
  "promptId": "ac1e15a4-789d-401b-936c-5f0b5ab58ba0",
  "type": "user",
  "uuid": "68a7c083-4416-45d6-84f9-815f45fc4451",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
    "content": "# Circuit Discovery Related Work Notes (2024-2026)\n\n> 调研日期：2026-05-12 | 项目：structfuse-context\n> 核心问题：CSS（Cross-method Stability Scoring）的 novelty 是否站得住？\n\n---\n\n## 1. 方法一致性比较（Novelty 关键）\n\n**结论：没有论文以\"跨方法一致性分析\"为核心贡献。** 多篇论文在评估新方法时附带比较了不同方法的表现，但比较维度是各方法 vs ground-truth 的 faithfulness/AUC，而非方法之间的 pairwise agreement。\n\n### 直接比较多方法的论文\n\n| 论文 | 方法比较 | 比较维度 | 是否测量方法间一致性 |\n|------|----------|----------|---------------------|\n| Conmy et al. \"Towards Automated Circuit Discovery\" (NeurIPS 2023) | ACDC vs SP vs HISP | ROC AUC vs ground-truth | ❌ 不测方法间 overlap |\n| Syed et al. \"Attribution Patching Outperforms Automated Circuit Discovery\" (BlackboxNLP 2024) | EAP vs ACDC vs SP vs HISP | AUC vs ground-truth | ❌ |\n| Bhaskar et al. \"Finding Transformer Circuits with Edge Pruning\" (NeurIPS 2024 Spotlight) | Edge Pruning vs ACDC vs EAP | Faithfulness at various sparsities | ❌ 但隐含表明方法差异大：EP 找到的边不到 ACDC/EAP 的一半 |\n| Hsu et al. \"CD-T\" (ICLR 2025) | CD-T vs ACDC vs EAP | ROC AUC vs ground-truth | ❌ |\n| Edin et al. \"GIM\" (2025, arXiv) | GIM vs EActP vs EAP vs EAP-IG vs NAP vs IFR vs UGS | Faithfulness metrics | ❌ |\n| InterpBench (NeurIPS 2024 D&B) | ACDC vs EAP vs SP on 86 semi-synthetic models | Ground-truth recovery | ❌ 但发现 ACDC 与 EAP-IG 统计上不可区分 |\n\n### 最接近\"一致性分析\"的论文\n\n**Hanna et al. \"Have Faith in Faithfulness: Going Beyond Circuit Overlap\" (2024, arXiv 2403.17806)**\n- 比较 EAP vs EAP-IG 的 **node overlap**，发现两者 overlap 很高但 faithfulness 差异大\n- 核心结论：overlap ≠ faithfulness，高 overlap 不代表电路功能等价\n- **与 CSS 的关系**：这是对 overlap-based 评估的警告，但不是跨方法一致性的系统研究\n\n**Méloux et al. \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\" (2025, arXiv 2510.00845)**\n- 对 EAP-IG 做 bootstrap resampling，发现 **单方法内** Jaccard 仅 0.561\n- 超参数变化导致 Jaccard 从 0.086 到 1.0 不等\n- **与 CSS 的关系**：揭示了电路不稳定性问题（motivates CSS），但仅限单方法内变异，未跨方法\n\n**总结：无人系统测量不同方法间的 pairwise Jaccard / agreement matrix。这正是 CSS 要填补的空白。**\n\n---\n\n## 2. Circuit Aggregation / Ensemble（Novelty 威胁）\n\n### 🔴 最高威胁：CIRCUS\n\n**CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles**\n- 作者：Swapnil Parekh\n- 时间：2026年3月, arXiv 2603.00523\n- 方法：对单一归因方法，在多组剪枝阈值配置下运行，计算每条边的 inclusion frequency → stability score s(e) ∈ [0,1]，提取 consensus circuit（所有配置下都存在的边），分为 core/contingent/noise\n- **与 CSS 的区别**：CIRCUS 变化的是**单方法内的超参数**（剪枝阈值），不是跨不同算法族。它不运行 ACDC + EAP + SP 然后求交集\n- **与 CSS 的相似度**：数学框架高度相似（per-edge stability scoring, consensus extraction, core/contingent taxonomy）\n- **威胁评级**：🔴 HIGH — 概念上最接近，但维度不同（intra-method vs cross-method）\n\n### 🟡 中等威胁：Mondorf et al. Ensemble\n\n**Mondorf et al. \"Exploring Ensemble Strategies for Circuit Localization Methods\" (BlackboxNLP 2025, arXiv 2510.06811)**\n- 方法：组合 EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning 的输出\n  - Max = union（任一方法选中）\n  - Min = intersection（所有方法选中）\n  - Mean = 连续分数平均\n  - Hybrid = 并行+串行组合\n- 结果：Mean > union/intersection，Hybrid 最佳 (CMD 0.03, CPR 1.83)\n- **与 CSS 的区别**：聚合的是**连续归因分数**（mean/min/max），不是二值 edge-in/edge-out；方法主要是 EAP 变体，不是真正不同的算法族；workshop 短文非完整方法贡献\n- **与 CSS 的相似度**：确实跨方法组合（attribution + pruning），实现了 union/intersection 操作\n- **威胁评级**：🟡 MODERATE — 最接近跨方法聚合，但 framing 为 shared task 工程方案非方法论贡献\n\n### 🟢 低威胁\n\n| 论文 | 方法 | 与 CSS 区别 | 威胁 |\n|------|------|------------|------|\n| Nikankin et al. \"Improving Circuit Faithfulness via Better Edge Selection\" (BlackboxNLP 2025) | Bootstrap EAP-IG scores across data resamples | 单方法 + 数据重采样，非跨方法 | 🟢 LOW |\n| Anani et al. \"Certified Circuits: Stability Guarantees\" (2026, arXiv 2602.22968) | 随机化数据子采样 + 删除平滑认证 | 单方法 wrapper，不聚合多方法 | 🟢 LOW |\n| Miller et al. \"Transformer Circuit Faithfulness Metrics are not Robust\" (CoLM 2024) | 分析 faithfulness 指标敏感性 | 纯诊断，不提出聚合 | 🟢 LOW |\n\n**总结：没有论文提出 CSS 的精确方案——运行 N 种根本不同的算法族（ACDC, EAP, SP, EP），对每种输出做二值化，然后计算跨方法 binary consensus。CIRCUS 最接近但维度不同（intra-method threshold variation vs cross-method）。Mondorf et al. 确实跨方法但用连续分数聚合且为 workshop 工程方案。**\n\n---\n\n## 3. 2024-2026 新方法\n\n| 方法 | 论文 | 年份 | 会议 | 算法族 | 备注 |\n|------|------|------|------|--------|------|\n| CD-T | Hsu et al. \"Efficient Automated Circuit Discovery using Contextual Decomposition\" | 2024 | ICLR 2025 | 分解 (decomposition) | 无需 activation patching，秒级发现，97% AUC |\n| DiscoGP | Yu et al. \"Functional Faithfulness in the Wild\" | 2024 | ICML 2024 | 可微剪枝 | 联合权重+边剪枝，端到端学习二值 mask |\n| Transcoders | Dunefsky et al. \"Transcoders Find Interpretable LLM Feature Circuits\" | 2024 | NeurIPS 2024 | 稀疏替换模型 | 用稀疏 MLP 替换原 MLP，实现 weights-based 电路分析 |\n| Sparse Feature Circuits | Marks et al. \"Discovering and Editing Interpretable Causal Graphs\" | 2024 | ICLR 2025 (Oral) | 归因 + SAE 特征 | 在 SAE 特征级别发现电路，支持 SHIFT 编辑 |\n| Circuit Tracing | Ameisen, Olah et al. (Anthropic) \"Attribution Graphs\" | 2025 | Tech Report | 稀疏替换 + 归因 | Cross-layer transcoders → per-prompt DAG，应用于 Claude 3.5 |\n| GIM | Edin et al. \"Improved Interpretability for LLMs\" | 2025 | arXiv | 梯度修正 | 修正 softmax/LayerNorm 反传，MIB 排行榜第一 |\n| HAP | Gu et al. \"Hybrid Attribution and Pruning Framework\" | 2025 | arXiv | 混合 (EAP → EP) | 先 EAP 粗筛再 EP 精修，比 EP 快 46% |\n| ModCirc | He et al. \"Modular Circuits of LLMs\" | 2025 | ICML 2025 | 模块化分解 | 发现跨任务共享的模块化电路词表 |\n| Stream | Rosser et al. \"Scaling up MI to Long Context\" | 2025 | arXiv | 层次化剪枝 | O(T log T) 稀疏注意力 mask，支持 100K+ token |\n| Weight-Sparse Circuits | Gao et al. (OpenAI) | 2025 | arXiv | 稀疏训练 | 极端权重稀疏 (~1/1000) → 天然可解释电路 |\n| Formal MI | Hadad et al. \"Automated Circuit Discovery with Provable Guarantees\" | 2026 | ICLR 2026 | 验证 (verification) | 首个可证明保证的电路发现（鲁棒性 + 最小性） |\n| SVD Directional Masking | Ahmad et al. \"Beyond Components\" | 2025 | arXiv | SVD + 可微 mask | 揭示单头内叠加子功能 |\n\n---\n\n## 4. 顶会论文列表\n\n### ICLR 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Autoencoders Find Highly Interpretable Features in LMs | SAE 发现单语义特征，解决 superposition |\n| Towards Best Practices of Activation Patching in LMs | 系统分析 patching 方法选择对电路发现的影响 |\n| Circuit Component Reuse Across Tasks | IOI 电路 ~78% 被 Colored Objects 复用 |\n| Successor Heads: Recurring Interpretable Attention Heads | 发现跨架构的 successor heads（递增操作） |\n\n### ICLR 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Feature Circuits (Oral) | SAE 特征级电路发现 + SHIFT 编辑 |\n| Scaling and Evaluating Sparse Autoencoders (Oral) | k-sparse SAE 扩展到 GPT-4，16M latents |\n| CD-T: Contextual Decomposition for Circuit Discovery | 秒级电路发现，97% AUC |\n| Computational Complexity of Circuit Discovery (Spotlight) | 证明多数电路发现查询 NP-hard |\n| Everything Everywhere All at Once: Is MI Identifiable? | 电路非唯一性：多电路可复现同一行为 |\n| SAEs Do Not Find Canonical Units of Analysis | SAE stitching 证明特征非原子/非完备 |\n| Unifying and Verifying Mechanistic Interpretations | 统一群运算网络的机制解释并形式化证明 |\n\n### NeurIPS 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Finding Transformer Circuits with Edge Pruning (Spotlight) | EP 方法，更忠实且更稀疏，扩展到 13B |\n| Transcoders Find Interpretable LLM Feature Circuits | 稀疏 MLP 替换实现 weights-based 电路分析 |\n| LLM Circuit Analyses Are Consistent Across Training and Scale | 电路在训练过程和模型规模间一致出现 |\n| Compact Proofs of Model Performance via MI | MI → 可证明的准确率下界 |\n| Hypothesis Testing the Circuit Hypothesis | 形式化电路假设的假设检验 |\n| InterpBench: Semi-Synthetic Transformers for Evaluating MI | 86 个有 ground-truth 的半合成模型评估基准 |\n\n### ICML 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| MIB: A Mechanistic Interpretability Benchmark | 标准化电路定位基准，归因+mask 优化方法领先 |\n| ModCirc: Modular Circuits of LLMs | 跨任务模块化电路词表 |\n| Towards Understanding Fine-Tuning via Circuit Analysis | 追踪微调中电路变化，提出 circuit-aware LoRA |\n\n---\n\n## 5. Novelty 评估\n\n### CSS 的 novelty 站得住吗？**站得住，但需要精确定位差异化。**\n\n#### ✅ Novelty 成立的理由\n\n1. **无人做跨算法族的 binary consensus**：所有现有工作要么是单方法内变异分析（CIRCUS, Méloux），要么是连续分数聚合（Mondorf），要么只是各方法 vs ground-truth 的性能比较。CSS 提出跨 N 种根本不同的算法族做二值共识，这个精确配方是新的。\n\n2. **方法间差异的系统分析是空白**：没有论文报告过不同方法的 pairwise Jaccard matrix / agreement heatmap。大量论文隐含表明方法差异很大（EP 边数不到 ACDC 一半），但无人将此作为研究问题。\n\n3. **core/contingent 分类的跨方法版本未被探索**：CIRCUS 做了类似的 core/contingent/noise taxonomy，但基于 intra-method threshold variation。CSS 基于 cross-method agreement 做分类，维度不同且信息更丰富。\n\n#### ⚠️ 需要小心的 Novelty 威胁\n\n1. **CIRCUS (2603.00523)** 是最大威胁。虽然维度不同，但 reviewer 可能认为 conceptual overlap 太大。**建议**：论文中必须明确讨论 CIRCUS，强调区别（intra-method hyperparameter variation vs cross-method algorithmic diversity），并论证为何跨方法维度更有意义（不同方法有不同 inductive bias，而阈值变化只探索同一方法的 Rashomon set）。\n\n2. **Mondorf et al.** 已经实现了 union/intersection 操作并发现 mean 优于两者。CSS 需要论证 binary consensus 相比连续分数平均的优势（如可解释性、对阈值选择的鲁棒性）。\n\n3. **Méloux et al. 的 intra-method instability 问题**：如果单方法内 Jaccard 仅 0.56，跨方法 consensus 可能更低。需要实验证明 CSS-core 的 faithfulness 确实优于单方法，否则 consensus 可能只是噪声的交集。\n\n4. **非唯一性问题 (ICLR 2025 \"Everything Everywhere All at Once\")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。\n\n#### 🎯 差异化建议\n\n- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。\n- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。\n- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "b6883c92-982c-414d-b9be-8eed3a44832d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "leafUuid": "68a7c083-4416-45d6-84f9-815f45fc4451",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature review on circuit discovery methods comparison",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---

### Tool call

_source line 33 · 2026-05-12T22:16:18.626Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01FtFvCveFXyQbhuip2Jecyz`</summary>

```json
{
  "name": "related_work_notes",
  "type": "report",
  "description": "Circuit Discovery 文献调研报告（2024-2026），聚焦 CSS novelty 验证，覆盖方法一致性比较、聚合/ensemble、新方法、顶会论文",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "tags": [
    "literature-survey",
    "novelty",
    "circuit-discovery",
    "CSS"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68a7c083-4416-45d6-84f9-815f45fc4451",
  "isSidechain": false,
  "requestId": "req_011CaySuyFhYvDGmooTawnoq",
  "type": "assistant",
  "uuid": "0c77fd36-0f56-493f-945f-0788d90c7796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HY4wRnZEfgz4E2qjwx8Df",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4898,
      "cache_read_input_tokens": 37616,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 37616,
          "cache_creation_input_tokens": 4898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4898
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

_source line 34 · 2026-05-12T22:16:18.677Z_

<details><summary>↩ Tool result · `toolu_01FtFvCveFXyQbhuip2Jecyz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_1c4c99\", \"name\": \"related_work_notes\", \"type\": \"report\", \"description\": \"Circuit Discovery 文献调研报告（2024-2026），聚焦 CSS novelty 验证，覆盖方法一致性比较、聚合/ensemble、新方法、顶会论文\", \"path\": \"projects/structfuse-context/artifacts/_project/report/related_work_notes.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:16:18.634607+00:00\", \"tags\": [\"literature-survey\", \"novelty\", \"circuit-discovery\", \"CSS\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c77fd36-0f56-493f-945f-0788d90c7796",
  "isSidechain": false,
  "promptId": "ac1e15a4-789d-401b-936c-5f0b5ab58ba0",
  "type": "user",
  "uuid": "11ca896b-67a9-48a9-9766-63c1b33ca50c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260512_1c4c99\\\", \\\"name\\\": \\\"related_work_notes\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Circuit Discovery 文献调研报告（2024-2026），聚焦 CSS novelty 验证，覆盖方法一致性比较、聚合/ensemble、新方法、顶会论文\\\", \\\"path\\\": \\\"projects/structfuse-context/artifacts/_project/report/related_work_notes.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"structfuse-context\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-12T22:16:18.634607+00:00\\\", \\\"tags\\\": [\\\"literature-survey\\\", \\\"novelty\\\", \\\"circuit-discovery\\\", \\\"CSS\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_1c4c99\", \"name\": \"related_work_notes\", \"type\": \"report\", \"description\": \"Circuit Discovery 文献调研报告（2024-2026），聚焦 CSS novelty 验证，覆盖方法一致性比较、聚合/ensemble、新方法、顶会论文\", \"path\": \"projects/structfuse-context/artifacts/_project/report/related_work_notes.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:16:18.634607+00:00\", \"tags\": [\"literature-survey\", \"novelty\", \"circuit-discovery\", \"CSS\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "0c77fd36-0f56-493f-945f-0788d90c7796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-12T22:16:18.689Z_

```json
{
  "parentUuid": "11ca896b-67a9-48a9-9766-63c1b33ca50c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b1e585a2-af64-465a-bc0b-0ac921837653",
  "timestamp": "2026-05-12T22:16:18.689Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-12T22:16:31.790Z_

报告已写入 `artifacts/related_work_notes.md` 并注册。

---

## 核心结论

**Q1 方法一致性比较**：**无人将此作为核心贡献。** 多篇论文附带比较了不同方法的 faithfulness（vs ground-truth），但没有论文系统测量方法之间的 pairwise agreement / Jaccard matrix。Méloux et al. 做了单方法内的 variance analysis（Jaccard 仅 0.56），Hanna et al. 发现 overlap 高但 faithfulness 差异大——都是局部证据，不是系统的跨方法一致性研究。

**Q2 Circuit Aggregation**：**无直接竞品，但有两个需要讨论的工作：**
- **CIRCUS (2026.03, arXiv 2603.00523)** 🔴 最大威胁——per-edge stability scoring + consensus extraction，数学框架与 CSS 高度相似。但它变化的是**单方法内的剪枝阈值**，不是跨算法族。必须在论文中明确区分。
- **Mondorf et al. (BlackboxNLP 2025)** 🟡 中等威胁——确实组合了 EAP + EP 的输出（含 union/intersection），但用连续分数平均，且为 workshop 短文。

**Novelty 评估：CSS 的 novelty 站得住。** 跨 N 种根本不同算法族的二值共识、方法间 agreement matrix 分析、基于跨方法共识的 core/contingent 分类——这个精确配方没有被做过。关键是论文中必须：
1. 正面讨论 CIRCUS，论证 cross-method vs intra-method variation 的本质区别
2. 论证二值共识相比连续分数平均（Mondorf）的优势
3. 实验证明 CSS-core 的 faithfulness 确实优于单方法结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1e585a2-af64-465a-bc0b-0ac921837653",
  "isSidechain": false,
  "requestId": "req_011CaySvRcTqEr7NrySWJfLE",
  "type": "assistant",
  "uuid": "5190dbc8-d3cf-4131-89af-39199b89c1c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5Ke9J1RbDag7R8VLXjptr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 42514,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 42514,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 667
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

_source line 37_

```json
{
  "type": "last-prompt",
  "leafUuid": "5190dbc8-d3cf-4131-89af-39199b89c1c4",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature review on circuit discovery methods comparison",
  "sessionId": "a4897adb-444f-47e1-81f6-81048ce3e3e1"
}
```

---
