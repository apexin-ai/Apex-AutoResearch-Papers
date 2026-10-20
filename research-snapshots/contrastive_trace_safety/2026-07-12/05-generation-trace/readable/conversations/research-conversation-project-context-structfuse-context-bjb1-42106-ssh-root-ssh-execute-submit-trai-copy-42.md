# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: bjb1-42106 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/cf51224d-fd16-44c7-b53d-2f35ec8def65.jsonl`
- **Structured JSON:** [`cfeb7545337d4f72a84d.json`](../../sessions/cf/cfeb7545337d4f72a84d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:10:43.095Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:10:43.095Z",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: bjb1-42106\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n**[D041] 修正 paper_framing.md 中 dataflow-aware 策略描述**\n\n## 背景\nReviewer 发现代码 `build_m1_training_data.py:197-199` 中 dataflow-aware 策略实际用 BM25 top-K 排序选负样本，但论文 framing 写的是 embedding similarity。决策：修改论文匹配代码，不重建数据。实验结果有效，代码是对的。\n\n## 任务\n修改 `paper_framing.md` 中 §3.4（或涉及 dataflow-aware 策略描述的部分）：\n\n1. **公式修正**：将 `sim(E_θ0(q), E_θ0(f))` 改为 `BM25(q, f)`（凡是描述 dataflow-aware 负样本排序方式的地方）\n2. **Difficulty gradient 论述调整**：三策略探索不同维度的难度——\n   - random：无信号baseline\n   - embedding-distance：语义相似性（pretrained encoder cosine similarity）\n   - dataflow-aware：结构过滤（只从 CodeQL call-graph connected 文件中选）+ 词法相似性（BM25 排序）\n3. **修正不准确描述**：如 \"files that the pretrained encoder considers similar yet structurally disconnected\" → 准确描述 dataflow-aware 的实际机制（结构连接的文件中按 BM25 相似性排序选最难的）\n4. 检查整个文件中所有提到 dataflow-aware 策略机制的地方，确保一致性\n\n## 文件路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md`\n\n## 约束\n- 只改论文/framing 文档，不改代码\n- Claim 1（embedding > random）的措辞不要动\n- 文件末尾加 `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->`\n\n{\"method\":\"tools/call\",\"params\":{\"name\":\"spawn_worker\",\"arguments\":{\"task_type\":\"fix:d041-method-drafts-dataflow\",\"project\":\"structfuse-context\",\"task_prompt\":\"**[D041] 修正论文初稿中 dataflow-aware 策略描述**\\n\\n## 背景\\nReviewer 发现代码中 dataflow-aware 策略实际用 BM25 top-K 排序选负样本（在 CodeQL call-graph connected 文件中），但论文初稿写的是 embedding similarity。决策：修改论文匹配代码，不重建数据。\\n\\n## 任务\\n检查并修正以下论文初稿文件中所有涉及 dataflow-aware 负样本选择机制的描述：\\n\\n1. `artifacts/paper_drafts/method_v1.md` — 方法描述，若提到 dataflow-aware 用 embedding similarity 排序，改为 BM25 排序\\n2. `artifacts/paper_drafts/introduction_v2.md` — 若提到 dataflow-aware 机制\\n3. `artifacts/paper_drafts/experiment_setup_v1.md` — 实验设置，若描述三策略差异\\n4. `artifacts/paper_drafts/experiments_v1.md` — 实验结果，若解释 dataflow-aware 表现时引用错误机制\\n5. `artifacts/paper_drafts/related_work_v1.md` — 若对比时提到\\n\\n正确描述：\\n- dataflow-aware 策略：从 CodeQL 2-hop bounded data-flow analysis 确定的 structurally connected 文件中，用 BM25 相似性排序选 top-K 作为 hard negatives\\n- embedding-distance 策略：用 pretrained encoder (E_θ0) cosine similarity 排序选 top-K\\n- random 策略：随机采样\\n\\n## 文件路径前缀\\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/`\\n\\n先用 read_project_file 检查每个文件是否存在及内容，再修改。\\n\\n## 约束\\n- 只改论文文档，不改代码\\n- 每个修改的文件末尾加 `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->`\\n\",\"tool_groups\":[\"knowledge\"]},\"_meta\":{\"claudecode/toolUseId\":\"toolu_01Qua4tJToEpcpMn5ZAGcqFW\",\"progressToken\":6}},\"jsonrpc\":\"2.0\",\"id\":6}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T02:10:43.099Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:10:43.099Z",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-15T02:10:43.143Z_

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
**[D041] 修正 paper_framing.md 中 dataflow-aware 策略描述**

## 背景
Reviewer 发现代码 `build_m1_training_data.py:197-199` 中 dataflow-aware 策略实际用 BM25 top-K 排序选负样本，但论文 framing 写的是 embedding similarity。决策：修改论文匹配代码，不重建数据。实验结果有效，代码是对的。

## 任务
修改 `paper_framing.md` 中 §3.4（或涉及 dataflow-aware 策略描述的部分）：

1. **公式修正**：将 `sim(E_θ0(q), E_θ0(f))` 改为 `BM25(q, f)`（凡是描述 dataflow-aware 负样本排序方式的地方）
2. **Difficulty gradient 论述调整**：三策略探索不同维度的难度——
   - random：无信号baseline
   - embedding-distance：语义相似性（pretrained encoder cosine similarity）
   - dataflow-aware：结构过滤（只从 CodeQL call-graph connected 文件中选）+ 词法相似性（BM25 排序）
3. **修正不准确描述**：如 "files that the pretrained encoder considers similar yet structurally disconnected" → 准确描述 dataflow-aware 的实际机制（结构连接的文件中按 BM25 相似性排序选最难的）
4. 检查整个文件中所有提到 dataflow-aware 策略机制的地方，确保一致性

## 文件路径
`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md`

## 约束
- 只改论文/framing 文档，不改代码
- Claim 1（embedding > random）的措辞不要动
- 文件末尾加 `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->`

{"method":"tools/call","params":{"name":"spawn_worker","arguments":{"task_type":"fix:d041-method-drafts-dataflow","project":"structfuse-context","task_prompt":"**[D041] 修正论文初稿中 dataflow-aware 策略描述**\n\n## 背景\nReviewer 发现代码中 dataflow-aware 策略实际用 BM25 top-K 排序选负样本（在 CodeQL call-graph connected 文件中），但论文初稿写的是 embedding similarity。决策：修改论文匹配代码，不重建数据。\n\n## 任务\n检查并修正以下论文初稿文件中所有涉及 dataflow-aware 负样本选择机制的描述：\n\n1. `artifacts/paper_drafts/method_v1.md` — 方法描述，若提到 dataflow-aware 用 embedding similarity 排序，改为 BM25 排序\n2. `artifacts/paper_drafts/introduction_v2.md` — 若提到 dataflow-aware 机制\n3. `artifacts/paper_drafts/experiment_setup_v1.md` — 实验设置，若描述三策略差异\n4. `artifacts/paper_drafts/experiments_v1.md` — 实验结果，若解释 dataflow-aware 表现时引用错误机制\n5. `artifacts/paper_drafts/related_work_v1.md` — 若对比时提到\n\n正确描述：\n- dataflow-aware 策略：从 CodeQL 2-hop bounded data-flow analysis 确定的 structurally connected 文件中，用 BM25 相似性排序选 top-K 作为 hard negatives\n- embedding-distance 策略：用 pretrained encoder (E_θ0) cosine similarity 排序选 top-K\n- random 策略：随机采样\n\n## 文件路径前缀\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/`\n\n先用 read_project_file 检查每个文件是否存在及内容，再修改。\n\n## 约束\n- 只改论文文档，不改代码\n- 每个修改的文件末尾加 `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->`\n","tool_groups":["knowledge"]},"_meta":{"claudecode/toolUseId":"toolu_01Qua4tJToEpcpMn5ZAGcqFW","progressToken":6}},"jsonrpc":"2.0","id":6}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e0e0e99b-f04a-440d-b03d-7ba309184820",
  "type": "user",
  "uuid": "d745a336-de25-4b37-b3a2-c627e591483c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:10:43.142Z_

```json
{
  "parentUuid": "d745a336-de25-4b37-b3a2-c627e591483c",
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
  "uuid": "5e8e55fc-efe8-4e09-9b5c-caebe6d00771",
  "timestamp": "2026-05-15T02:10:43.142Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:10:43.142Z_

```json
{
  "parentUuid": "5e8e55fc-efe8-4e09-9b5c-caebe6d00771",
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
  "uuid": "23b41bad-cfe7-45ec-b550-1e3f9e287d8e",
  "timestamp": "2026-05-15T02:10:43.142Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T02:10:43.142Z_

```json
{
  "parentUuid": "23b41bad-cfe7-45ec-b550-1e3f9e287d8e",
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
  "uuid": "4073fd74-d9b9-46ad-bfb9-3a37664d61b8",
  "timestamp": "2026-05-15T02:10:43.142Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-15T02:10:43.143Z_

```json
{
  "parentUuid": "4073fd74-d9b9-46ad-bfb9-3a37664d61b8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7493acee-4efe-4694-be94-ba8285302896",
  "timestamp": "2026-05-15T02:10:43.143Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
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
  "aiTitle": "Fix dataflow-aware strategy description in paper",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Assistant

_source line 9 · 2026-05-15T02:10:49.782Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to modify `paper_framing.md` to correct the description of the dataflow-aware strategy. Let me first read the file to understand its current content, then make the necessary edits.

Let me also note that there's a spawn_worker JSON at the end - this appears to be a task dispatched to me as a worker. I need to focus on the main task: modifying `paper_framing.md`.

Let me read the file first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7493acee-4efe-4694-be94-ba8285302896",
  "isSidechain": false,
  "requestId": "req_011Cb3YR1PLztbY5f9mbduYL",
  "type": "assistant",
  "uuid": "d366facc-4f45-498b-b38d-efaac679a43a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWr3Y2hdMsUVyKwcfcaPpw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12454,
      "cache_read_input_tokens": 11447,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12454,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 219,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12454
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

_source line 10 · 2026-05-15T02:10:50.386Z_

I'll read the paper_framing.md file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d366facc-4f45-498b-b38d-efaac679a43a",
  "isSidechain": false,
  "requestId": "req_011Cb3YR1PLztbY5f9mbduYL",
  "type": "assistant",
  "uuid": "9b6b8568-b544-4975-956c-ebbdf8a48b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWr3Y2hdMsUVyKwcfcaPpw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12454,
      "cache_read_input_tokens": 11447,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12454,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 219,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12454
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

_source line 11 · 2026-05-15T02:10:50.785Z_

<details open><summary>🔧 Tool call — Read · `toolu_0186XCZeaTtD13N77HUFC1J7`</summary>

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
  "parentUuid": "9b6b8568-b544-4975-956c-ebbdf8a48b17",
  "isSidechain": false,
  "requestId": "req_011Cb3YR1PLztbY5f9mbduYL",
  "type": "assistant",
  "uuid": "29523eb5-2577-434b-b737-fc8a1ba46209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWr3Y2hdMsUVyKwcfcaPpw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12454,
      "cache_read_input_tokens": 11447,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12454,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 219,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12454
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

_source line 12 · 2026-05-15T02:10:50.797Z_

<details><summary>↩ Tool result · `toolu_0186XCZeaTtD13N77HUFC1J7`</summary>

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
  "parentUuid": "29523eb5-2577-434b-b737-fc8a1ba46209",
  "isSidechain": false,
  "promptId": "e0e0e99b-f04a-440d-b03d-7ba309184820",
  "type": "user",
  "uuid": "1f918ac3-31c1-4b2f-81d1-90f272878602",
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
  "sourceToolAssistantUUID": "29523eb5-2577-434b-b737-fc8a1ba46209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "leafUuid": "1f918ac3-31c1-4b2f-81d1-90f272878602",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix dataflow-aware strategy description in paper",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Assistant

_source line 15 · 2026-05-15T02:11:49.356Z_

<details><summary>Logged reasoning block</summary>

````text
Now I need to carefully analyze the file for all mentions of dataflow-aware strategy mechanisms. Let me identify the places that need changes:

1. **Line 11 (Claim 2)**: "Pilot data shows dataflow < embedding on both encoders" - this doesn't describe the mechanism, seems fine.

2. **Line 41-43 (Formal Definition)**: 
```
Given retrieval domain D, structural graph G, similarity function s, query q:
**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)


```

Wait, I'm noticing something odd here. The formal definition selects items that are NOT reachable in the graph, which would mean structurally disconnected files. But that seems backwards from what dataflow-aware selection should do—it should be pulling from files that ARE connected through the call graph, not disconnected ones.

Let me reconsider what this formal definition is actually describing. It says "structure-grounded hard negative," so maybe it's defining a general concept for selecting negative examples rather than the positive selection strategy itself. The actual dataflow-aware approach filters to connected files and ranks them by BM25 similarity, which is the opposite of what the negation symbol suggests.

``` a hard negative - it's structurally related but not the answer.

So the formal definition needs updating: the negatives should come from files that ARE reachable in the call graph, not unreachable ones, and we're using BM25 scoring instead of generic similarity. Let me correct that formula to match what the code actually does.

The structure-grounded hard negative should be the highest-scoring reachable file that isn't the gold answer itself. Now I need to verify the other formula corrections the task is asking for - checking whether embedding similarity functions need to be swapped out for BM25 throughout the definitions. The structural graph being fixed and not updating with the encoder is correct as stated. Looking through the claims more carefully, the mechanism isn't explicitly detailed in most places—the mention of structure-grounded negatives interacting with encoder geometry doesn't spell out how the scoring actually works, which is fine. I'm noticing the task description mentions formula corrections and difficulty gradient adjustments, so I need to focus on those specific areas that need updating. I see the issue now - the formal definition actually describes files that are structurally connected and reachable in the call graph, ranked by similarity, not disconnected ones. That's the opposite of what the text currently says. I need to fix that description, and I should also verify the Anticipated Reviewer Concerns table to make sure the BM25 comparison is being characterized correctly as a separate strategy rather than part of the dataflow-aware mechanism.

The main fixes are updating the formal definition to reflect reachability and BM25 ranking, clarifying that both the structural graph and ranking function are encoder-independent, and making sure the three strategies have distinct difficulty gradients as required. I'm reviewing the Core Insight section and it seems fine—the mention of "orthogonal signal dimension (structure)" accurately captures the dataflow-aware approach. Now I'll plan my edits: clarify the formal definition to precisely describe how dataflow-awareness works, add an explicit breakdown of the three strategies' difficulty mechanisms, verify there are no other inaccuracies, and append the D041 comment.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f918ac3-31c1-4b2f-81d1-90f272878602",
  "isSidechain": false,
  "requestId": "req_011Cb3YRaE3HaEzDMNxqaax9",
  "type": "assistant",
  "uuid": "249fed8a-9bee-4efd-8f35-a20f77f95a0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLQnDrdQcQNTCabbvGoVMm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 23901,
      "output_tokens": 3181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3181,
          "cache_read_input_tokens": 23901,
          "cache_creation_input_tokens": 3640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3640
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

_source line 16 · 2026-05-15T02:11:50.429Z_

Now I'll identify all places that need correction. The key issues:

1. **Formal Definition (line 41-43)**: Formula uses `s(x,q) > τ ∧ ¬reachable_G(x,q)` — describes structurally *disconnected* files ranked by generic similarity. Actual mechanism: structurally *connected* files ranked by BM25.
2. Need to add clear three-strategy difficulty gradient description.
3. Add D041 comment at end.

Let me make the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "249fed8a-9bee-4efd-8f35-a20f77f95a0e",
  "isSidechain": false,
  "requestId": "req_011Cb3YRaE3HaEzDMNxqaax9",
  "type": "assistant",
  "uuid": "59d9ad20-8ce8-4166-a335-6d63bcf1c76d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLQnDrdQcQNTCabbvGoVMm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 23901,
      "output_tokens": 3181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3181,
          "cache_read_input_tokens": 23901,
          "cache_creation_input_tokens": 3640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3640
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

_source line 17 · 2026-05-15T02:11:57.630Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01VMayAThUiRCJQutX2xi7mx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).",
  "new_string": "## Formal Definition\n\nGiven retrieval domain D, structural graph G (CodeQL 2-hop bounded data-flow), gold file x*, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : reachable_G(x,q) ∧ x ≠ x*} BM25(q, x)\n\nBoth the structural graph and the BM25 ranking are encoder-independent (drift-immune).\n\n### Three-Strategy Difficulty Gradient\n\nThe three negative mining strategies explore different dimensions of difficulty:\n- **random**: No signal baseline — uniform sampling from the repository file pool.\n- **embedding-distance**: Semantic similarity — pretrained encoder (E_θ0) cosine similarity ranking selects top-K most similar files as hard negatives.\n- **dataflow-aware**: Structural filtering (only files reachable via CodeQL call-graph connectivity) + lexical similarity (BM25 ranking within the structurally connected set selects the hardest negatives)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59d9ad20-8ce8-4166-a335-6d63bcf1c76d",
  "isSidechain": false,
  "requestId": "req_011Cb3YRaE3HaEzDMNxqaax9",
  "type": "assistant",
  "uuid": "b98e3c88-9da6-410a-98a9-302f2ae9692a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLQnDrdQcQNTCabbvGoVMm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3640,
      "cache_read_input_tokens": 23901,
      "output_tokens": 3181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3181,
          "cache_read_input_tokens": 23901,
          "cache_creation_input_tokens": 3640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3640
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

_source line 18 · 2026-05-15T02:11:57.653Z_

<details><summary>↩ Tool result · `toolu_01VMayAThUiRCJQutX2xi7mx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b98e3c88-9da6-410a-98a9-302f2ae9692a",
  "isSidechain": false,
  "promptId": "e0e0e99b-f04a-440d-b03d-7ba309184820",
  "type": "user",
  "uuid": "0cc58a17-8657-44c9-afa0-24c7e587c3d5",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "oldString": "## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).",
    "newString": "## Formal Definition\n\nGiven retrieval domain D, structural graph G (CodeQL 2-hop bounded data-flow), gold file x*, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : reachable_G(x,q) ∧ x ≠ x*} BM25(q, x)\n\nBoth the structural graph and the BM25 ranking are encoder-independent (drift-immune).\n\n### Three-Strategy Difficulty Gradient\n\nThe three negative mining strategies explore different dimensions of difficulty:\n- **random**: No signal baseline — uniform sampling from the repository file pool.\n- **embedding-distance**: Semantic similarity — pretrained encoder (E_θ0) cosine similarity ranking selects top-K most similar files as hard negatives.\n- **dataflow-aware**: Structural filtering (only files reachable via CodeQL call-graph connectivity) + lexical similarity (BM25 ranking within the structurally connected set selects the hardest negatives).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 38,
        "oldLines": 11,
        "newStart": 38,
        "newLines": 18,
        "lines": [
          " ",
          " ## Formal Definition",
          " ",
          "-Given retrieval domain D, structural graph G, similarity function s, query q:",
          "-**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)",
          "+Given retrieval domain D, structural graph G (CodeQL 2-hop bounded data-flow), gold file x*, query q:",
          "+**structure-grounded hard negative** = argmax_{x ∈ D : reachable_G(x,q) ∧ x ≠ x*} BM25(q, x)",
          " ",
          "-The structural graph is externally fixed and does not update with the encoder (drift-immune).",
          "+Both the structural graph and the BM25 ranking are encoder-independent (drift-immune).",
          " ",
          "+### Three-Strategy Difficulty Gradient",
          "+",
          "+The three negative mining strategies explore different dimensions of difficulty:",
          "+- **random**: No signal baseline — uniform sampling from the repository file pool.",
          "+- **embedding-distance**: Semantic similarity — pretrained encoder (E_θ0) cosine similarity ranking selects top-K most similar files as hard negatives.",
          "+- **dataflow-aware**: Structural filtering (only files reachable via CodeQL call-graph connectivity) + lexical similarity (BM25 ranking within the structurally connected set selects the hardest negatives).",
          "+",
          " ## Title Options",
          " ",
          " - Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b98e3c88-9da6-410a-98a9-302f2ae9692a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T02:12:01.498Z_

<details open><summary>🔧 Tool call — Edit · `toolu_014fFCDXYhA1pkdYt8dU8NYQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
  "old_string": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
  "new_string": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc58a17-8657-44c9-afa0-24c7e587c3d5",
  "isSidechain": false,
  "requestId": "req_011Cb3YWVyC5ubnhfv3F5JWB",
  "type": "assistant",
  "uuid": "fcf3a7cd-1cb7-48e1-a7f2-8c8176fb38c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeBLkptvJCBQausDNYByXW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3246,
      "cache_read_input_tokens": 27541,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 27541,
          "cache_creation_input_tokens": 3246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3246
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

_source line 20 · 2026-05-15T02:12:01.538Z_

<details><summary>↩ Tool result · `toolu_014fFCDXYhA1pkdYt8dU8NYQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcf3a7cd-1cb7-48e1-a7f2-8c8176fb38c3",
  "isSidechain": false,
  "promptId": "e0e0e99b-f04a-440d-b03d-7ba309184820",
  "type": "user",
  "uuid": "3c2e0565-0442-4630-8dc7-51b184ffd6ce",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
    "oldString": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->",
    "newString": "&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 132,
        "oldLines": 3,
        "newStart": 132,
        "newLines": 4,
        "lines": [
          " - ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.",
          " ",
          " &lt;!-- Claim 2 wording fix: 2026-05-15 -->",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "fcf3a7cd-1cb7-48e1-a7f2-8c8176fb38c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-15T02:12:03.812Z_

Now let me verify the full file to check for any other references to the dataflow-aware mechanism that might be inconsistent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c2e0565-0442-4630-8dc7-51b184ffd6ce",
  "isSidechain": false,
  "requestId": "req_011Cb3YWnoyCGaUcHQCWuRtW",
  "type": "assistant",
  "uuid": "226a5cfb-b76e-4286-ba6d-940249f785bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KA19itggWey1tGqdw3FVpM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 30787,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 30787,
          "cache_creation_input_tokens": 255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 255
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

_source line 22 · 2026-05-15T02:12:04.274Z_

<details open><summary>🔧 Tool call — Read · `toolu_018DPMYb9WB6iNdBtQQuGssT`</summary>

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
  "parentUuid": "226a5cfb-b76e-4286-ba6d-940249f785bd",
  "isSidechain": false,
  "requestId": "req_011Cb3YWnoyCGaUcHQCWuRtW",
  "type": "assistant",
  "uuid": "a3b2e80b-a35e-4561-a80e-fb2f8f244668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KA19itggWey1tGqdw3FVpM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 30787,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 30787,
          "cache_creation_input_tokens": 255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 255
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

_source line 23 · 2026-05-15T02:12:04.291Z_

<details><summary>↩ Tool result · `toolu_018DPMYb9WB6iNdBtQQuGssT`</summary>

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
41	Given retrieval domain D, structural graph G (CodeQL 2-hop bounded data-flow), gold file x*, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : reachable_G(x,q) ∧ x ≠ x*} BM25(q, x)
43	
44	Both the structural graph and the BM25 ranking are encoder-independent (drift-immune).
45	
46	### Three-Strategy Difficulty Gradient
47	
48	The three negative mining strategies explore different dimensions of difficulty:
49	- **random**: No signal baseline — uniform sampling from the repository file pool.
50	- **embedding-distance**: Semantic similarity — pretrained encoder (E_θ0) cosine similarity ranking selects top-K most similar files as hard negatives.
51	- **dataflow-aware**: Structural filtering (only files reachable via CodeQL call-graph connectivity) + lexical similarity (BM25 ranking within the structurally connected set selects the hardest negatives).
52	
53	## Title Options
54	
55	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
56	- Alternative: "Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]
57	- Backup: "Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code"
58	
59	## Venue Fit
60	
61	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
62	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
63	3. **Against "incremental" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.
64	
65	## Anticipated Reviewer Concerns
66	
67	| Concern | Response | Evidence |
68	|---------|----------|----------|
69	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
70	| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |
71	| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
72	| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
73	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
74	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
75	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
76	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
77	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
78	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
79	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
80	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
81	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
82	
83	## Evidence Status
84	
85	### Confirmed findings (basis for claims):
86	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption
87	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
88	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
89	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
90	- plan_006: CodeQL scalability confirmed at 123-repo scale
91	
92	### In progress:
93	- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.
94	- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.
95	- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15
96	
97	### Planned (priority order):
98	- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)
99	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
100	- plan_019: Pool size sensitivity (Dream consensus — external validity)
101	- plan_014: Temperature ablation (Dream reviewer concern)
102	- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
103	- plan_015: Dynamic mining baseline
104	- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
105	- plan_007/008/009: Additional ablations
106	
107	## Contingency (if full M2 results weaken claims)
108	
109	### All 18 runs confirm pilot pattern: Best case
110	- Full statistical power, paper as framed above
111	- Target: EMNLP Main
112	
113	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
114	- Drop Claim 2 to analysis observation
115	- Paper becomes: "Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
116	- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main
117	
118	### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]
119	- If plan_018 shows BM25 negatives perform ≈ random (not << random), the "challenging gradient-based assumption" narrative needs adjustment
120	- Pivot: "systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal"
121	- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome
122	- Claim 1 core preserved: "Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms"
123	- Impact: BM25 result determines narrative nuance, not core contribution
124	
125	### Embedding mining also loses advantage at full scale: Major reassessment needed
126	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
127	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
128	- Discuss with user before committing direction
129	
130	## Deprecated Claims (with reason)
131	
132	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
133	
134	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
135	&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3b2e80b-a35e-4561-a80e-fb2f8f244668",
  "isSidechain": false,
  "promptId": "e0e0e99b-f04a-440d-b03d-7ba309184820",
  "type": "user",
  "uuid": "2651c39c-ba41-4509-a5bc-1ca13610a4ae",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Simple static embedding-distance mining suffices for contrastive code retrieval, challenging the assumption that expensive gradient-based hard negative methods are necessary.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields +1.6–2.0pp R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\n\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining suffices, challenging the assumption that expensive gradient-based methods are necessary (CoCoHaNeRe's premise), (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis of when/why different strategies yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\n\n- **Headline result template**: \"Simple static embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), challenging the need for expensive gradient-based hard negative methods. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty provides a candidate mechanistic explanation for when different mining strategies are effective.\"\n\n## Core Insight\n\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis challenging gradient-based assumptions**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) assumes expensive gradient-based hard negative methods are necessary for effective code search. Our controlled comparison shows simple static embedding-distance mining suffices in structural code retrieval, isolating the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G (CodeQL 2-hop bounded data-flow), gold file x*, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : reachable_G(x,q) ∧ x ≠ x*} BM25(q, x)\n\nBoth the structural graph and the BM25 ranking are encoder-independent (drift-immune).\n\n### Three-Strategy Difficulty Gradient\n\nThe three negative mining strategies explore different dimensions of difficulty:\n- **random**: No signal baseline — uniform sampling from the repository file pool.\n- **embedding-distance**: Semantic similarity — pretrained encoder (E_θ0) cosine similarity ranking selects top-K most similar files as hard negatives.\n- **dataflow-aware**: Structural filtering (only files reachable via CodeQL call-graph connectivity) + lexical similarity (BM25 ranking within the structurally connected set selects the hardest negatives).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"Beyond Gradient-Based Mining: Static Embedding Negatives Suffice for Contrastive Code Retrieval\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\n- Backup: \"Simple Embedding Mining Suffices: Challenging Gradient-Based Assumptions in Hard Negative Mining for Code\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper challenges a prevalent assumption + provides mechanistic explanation for strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — challenges gradient-based necessity assumption\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 RUNNING (eval@500 R@1=0.6009). 2/10 runs complete, ~50h remaining.\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\n- m1_reextract_v2: 80.8% complete (22,842/28,276), 0 ERROR, ETA ~15:00 CST May 15\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"Simple embedding mining suffices (challenging gradient-based assumption) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: challenging gradient-based assumption + mechanistic analysis is sufficient for EMNLP Main\n\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \"challenging gradient-based assumption\" narrative needs adjustment\n- Pivot: \"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; gradient-based methods may not be necessary even when BM25 provides no signal\"\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining suffices) stands regardless of BM25 outcome\n- Claim 1 core preserved: \"Simple static embedding-distance mining consistently improves code retrieval without gradient-based mechanisms\"\n- Impact: BM25 result determines narrative nuance, not core contribution\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
      "numLines": 136,
      "startLine": 1,
      "totalLines": 136
    }
  },
  "sourceToolAssistantUUID": "a3b2e80b-a35e-4561-a80e-fb2f8f244668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
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
  "leafUuid": "2651c39c-ba41-4509-a5bc-1ca13610a4ae",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix dataflow-aware strategy description in paper",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Assistant

_source line 26 · 2026-05-15T02:12:20.480Z_

<details><summary>Logged reasoning block</summary>

```text
Let me verify all references to dataflow-aware strategy mechanisms in the file are consistent:

1. **Line 11 (Claim 2)**: "Structure-grounded (dataflow) negatives interact with encoder representation geometry" — describes the observation, not the mechanism. OK.

2. **Line 26**: "structure-grounded (dataflow) negatives interact with encoder representation geometry" — same, observation-level. OK.

3. **Line 28**: "Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns" — observation-level. OK.


4. **Line 32**: "the encoder needs harder negatives from an orthogonal signal dimension (structure)" — correctly frames dataflow-aware as providing signal from a structural dimension. OK.

5. **Lines 41-51**: The formal definition and three-strategy gradient now properly describes BM25 ranking within structurally connected files. OK.

6. **Line 70**: "BM25 vs true embedding negatives?" — this addresses plan_018 (BM25 as a standalone strategy), separate from the dataflow-aware mechanism. OK.

7. **Line 88**: "3-strategy comparison confirms ranking" — no mechanism description needed here.

8. **Line 98**: "BM25 negative baseline" — again tied to plan_018, not dataflow-aware. OK.

9. **Lines 118-123**: BM25 contingency plan is about plan_018's BM25-as-strategy approach. OK.

10. **Line 132**: Historical note correctly identifies the deprecated claim about BM25-proxy negatives being mislabeled as embedding_distance in the MVP. OK.

The formal definitions and strategy descriptions are now consistent throughout. Claim 1 wording remains unchanged as required, and the D041 comment has been added. Now I need to check whether the paper_drafts files mentioned in the spawn_worker task actually exist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2651c39c-ba41-4509-a5bc-1ca13610a4ae",
  "isSidechain": false,
  "requestId": "req_011Cb3YWzWvVCZstQjLZ8w8k",
  "type": "assistant",
  "uuid": "41fc9d36-051d-43a9-8184-35adf801308d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BewdjvaGAkZEqGdf2sWUpn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3712,
      "cache_read_input_tokens": 31042,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 626,
          "cache_read_input_tokens": 31042,
          "cache_creation_input_tokens": 3712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3712
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

_source line 27 · 2026-05-15T02:12:20.489Z_

Full file verified — all dataflow-aware references are now consistent. Let me also check the paper_drafts directory for any files that might need the same fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41fc9d36-051d-43a9-8184-35adf801308d",
  "isSidechain": false,
  "requestId": "req_011Cb3YWzWvVCZstQjLZ8w8k",
  "type": "assistant",
  "uuid": "60292085-e19c-42ee-b12b-86811106379c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BewdjvaGAkZEqGdf2sWUpn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3712,
      "cache_read_input_tokens": 31042,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 626,
          "cache_read_input_tokens": 31042,
          "cache_creation_input_tokens": 3712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3712
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

_source line 28 · 2026-05-15T02:12:21.761Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UsqZzMqNRZFPfrNTqpDpRg`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60292085-e19c-42ee-b12b-86811106379c",
  "isSidechain": false,
  "requestId": "req_011Cb3YWzWvVCZstQjLZ8w8k",
  "type": "assistant",
  "uuid": "61bb6614-173e-41d2-af57-4cbf837e22be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BewdjvaGAkZEqGdf2sWUpn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3712,
      "cache_read_input_tokens": 31042,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 626,
          "cache_read_input_tokens": 31042,
          "cache_creation_input_tokens": 3712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3712
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

_source line 29 · 2026-05-15T02:12:21.782Z_

<details><summary>↩ Tool result · `toolu_01UsqZzMqNRZFPfrNTqpDpRg`</summary>

```text
artifacts/paper_drafts/experimental_setup_k_checkpoint.md
artifacts/paper_drafts/introduction_v1.md
artifacts/paper_drafts/figure_design_v1.md
artifacts/paper_drafts/method_v1.md
artifacts/paper_drafts/claim2_wording_review.md
artifacts/paper_drafts/discussion_v2.md
artifacts/paper_drafts/related_work_v1.md
artifacts/paper_drafts/experiments_v1.md
artifacts/paper_drafts/experiment_setup_v1.md
artifacts/paper_drafts/introduction_v2.md
artifacts/paper_drafts/bm25_code_review.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61bb6614-173e-41d2-af57-4cbf837e22be",
  "isSidechain": false,
  "promptId": "e0e0e99b-f04a-440d-b03d-7ba309184820",
  "type": "user",
  "uuid": "22e8adcd-2076-433e-ab27-4f934a931c87",
  "toolUseResult": {
    "filenames": [
      "artifacts/paper_drafts/experimental_setup_k_checkpoint.md",
      "artifacts/paper_drafts/introduction_v1.md",
      "artifacts/paper_drafts/figure_design_v1.md",
      "artifacts/paper_drafts/method_v1.md",
      "artifacts/paper_drafts/claim2_wording_review.md",
      "artifacts/paper_drafts/discussion_v2.md",
      "artifacts/paper_drafts/related_work_v1.md",
      "artifacts/paper_drafts/experiments_v1.md",
      "artifacts/paper_drafts/experiment_setup_v1.md",
      "artifacts/paper_drafts/introduction_v2.md",
      "artifacts/paper_drafts/bm25_code_review.md"
    ],
    "durationMs": 12,
    "numFiles": 11,
    "truncated": false
  },
  "sourceToolAssistantUUID": "61bb6614-173e-41d2-af57-4cbf837e22be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-15T02:12:24.677Z_

<details><summary>Logged reasoning block</summary>

```text
The spawn_worker task at the bottom of the user's message mentions checking these paper_drafts files too. Let me search for any references to the dataflow-aware mechanism using embedding similarity in these files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22e8adcd-2076-433e-ab27-4f934a931c87",
  "isSidechain": false,
  "requestId": "req_011Cb3YYH66kKUoHNF3ppvL9",
  "type": "assistant",
  "uuid": "5c9ca2f3-80a4-4a68-93a9-d9fc84a193c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKzxMGvQeDKWHFmwMNja1q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 34754,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 34754,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 31 · 2026-05-15T02:12:25.149Z_

Let me check these drafts for any incorrect dataflow-aware descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c9ca2f3-80a4-4a68-93a9-d9fc84a193c8",
  "isSidechain": false,
  "requestId": "req_011Cb3YYH66kKUoHNF3ppvL9",
  "type": "assistant",
  "uuid": "abc955fe-f490-4b39-bfb8-65009802784e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKzxMGvQeDKWHFmwMNja1q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 34754,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 34754,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 32 · 2026-05-15T02:12:27.294Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016CvRLjYwFdQbQsKiN3PEWG`</summary>

```json
{
  "pattern": "dataflow|data.flow|structure.grounded|BM25|E_θ|sim\\(|embedding.*similar|structurally.disconnected",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abc955fe-f490-4b39-bfb8-65009802784e",
  "isSidechain": false,
  "requestId": "req_011Cb3YYH66kKUoHNF3ppvL9",
  "type": "assistant",
  "uuid": "ce8be6a3-4275-4231-b839-240ec0683cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKzxMGvQeDKWHFmwMNja1q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 34754,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 34754,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 33 · 2026-05-15T02:12:27.326Z_

<details><summary>↩ Tool result · `toolu_016CvRLjYwFdQbQsKiN3PEWG`</summary>

```text
&lt;persisted-output>
Output too large (25.9KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/cf51224d-fd16-44c7-b53d-2f35ec8def65/tool-results/toolu_016CvRLjYwFdQbQsKiN3PEWG.txt

Preview (first 2KB):
artifacts/paper_drafts/discussion_v2.md:6:[Omitted long matching line]
artifacts/paper_drafts/discussion_v2.md:12:[Omitted long matching line]
artifacts/paper_drafts/discussion_v2.md:14:[Omitted long matching line]
artifacts/paper_drafts/discussion_v2.md:20:Our negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.
artifacts/paper_drafts/discussion_v2.md:22:[Omitted long matching line]
artifacts/paper_drafts/discussion_v2.md:24:[Omitted long matching line]
artifacts/paper_drafts/discussion_v2.md:26:[Omitted long matching line]
artifacts/paper_drafts/discussion_v2.md:34:**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.
artifacts/paper_drafts/discussion_v2.md:36:**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce8be6a3-4275-4231-b839-240ec0683cc0",
  "isSidechain": false,
  "promptId": "e0e0e99b-f04a-440d-b03d-7ba309184820",
  "type": "user",
  "uuid": "1462d8fb-e30d-4a5c-b213-da96d23dbd71",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/paper_drafts/discussion_v2.md:6:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:12:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:14:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:20:Our negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.\nartifacts/paper_drafts/discussion_v2.md:22:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:24:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:26:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:34:**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.\nartifacts/paper_drafts/discussion_v2.md:36:**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).\nartifacts/paper_drafts/discussion_v2.md:40:**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.\nartifacts/paper_drafts/experiment_setup_v1.md:7:[Omitted long matching line]\nartifacts/paper_drafts/experiment_setup_v1.md:17:[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]\nartifacts/paper_drafts/experiment_setup_v1.md:59:**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].\nartifacts/paper_drafts/experiment_setup_v1.md:70:- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).\nartifacts/paper_drafts/method_v1.md:7:We formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\nartifacts/paper_drafts/method_v1.md:13:The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\nartifacts/paper_drafts/method_v1.md:17:### CodeQL Bounded Data-Flow Analysis\nartifacts/paper_drafts/method_v1.md:19:We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\nartifacts/paper_drafts/method_v1.md:22:- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\nartifacts/paper_drafts/method_v1.md:26:From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\nartifacts/paper_drafts/method_v1.md:30:At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\nartifacts/paper_drafts/method_v1.md:51:We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\nartifacts/paper_drafts/method_v1.md:63:We compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\nartifacts/paper_drafts/method_v1.md:69:### Dataflow-Aware Negatives\nartifacts/paper_drafts/method_v1.md:75:where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\nartifacts/paper_drafts/method_v1.md:79:[Omitted long matching line]\nartifacts/paper_drafts/method_v1.md:81:For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\nartifacts/paper_drafts/method_v1.md:85:[Omitted long matching line]\nartifacts/paper_drafts/method_v1.md:87:### Relationship to BM25 Baselines\nartifacts/paper_drafts/method_v1.md:89:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:5:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:11:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:21:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:23:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:36:| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\nartifacts/paper_drafts/experiments_v1.md:38:| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\nartifacts/paper_drafts/experiments_v1.md:40:| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\nartifacts/paper_drafts/experiments_v1.md:42:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:54:| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\nartifacts/paper_drafts/experiments_v1.md:56:The pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\nartifacts/paper_drafts/experiments_v1.md:84:| BM25 | \\placeholder{X.X%} |\nartifacts/paper_drafts/experiments_v1.md:92:A central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\nartifacts/paper_drafts/experiments_v1.md:101:| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\nartifacts/paper_drafts/experiments_v1.md:107:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:109:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:113:We stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\nartifacts/paper_drafts/experiments_v1.md:119:| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\nartifacts/paper_drafts/experiments_v1.md:120:| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\nartifacts/paper_drafts/experiments_v1.md:123:Confound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\nartifacts/paper_drafts/experiments_v1.md:140:[Omitted long matching line]\nartifacts/paper_drafts/introduction_v1.md:6:In practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.\nartifacts/paper_drafts/introduction_v1.md:12:These methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.\nartifacts/paper_drafts/introduction_v1.md:18:We present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.\nartifacts/paper_drafts/introduction_v1.md:22:Beyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.\nartifacts/paper_drafts/introduction_v1.md:28:[Omitted long matching line]\nartifacts/paper_drafts/introduction_v1.md:30:3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \\cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.\nartifacts/paper_drafts/experimental_setup_k_checkpoint.md:16:| m2_embed_verify / dataflow | Qwen | dataflow | step 500 (0.5602) | step 500 (0.5436) | Yes |\nartifacts/paper_drafts/experimental_setup_k_checkpoint.md:19:| plan_013_starcoder / dataflow | StarCoder | dataflow | step 1000 (0.5255) | final (0.5078 > 0.4869@1000) | **No** |\nartifacts/paper_drafts/experimental_setup_k_checkpoint.md:33:[Omitted long matching line]\nartifacts/paper_drafts/bm25_code_review.md:1:# BM25 Negative Mining Code Review\nartifacts/paper_drafts/bm25_code_review.md:3:**File**: `/root/structfuse/scripts/mine_bm25_negatives.py` (251 lines)\nartifacts/paper_drafts/bm25_code_review.md:9:## 1. BM25 索引构建\nartifacts/paper_drafts/bm25_code_review.md:15:| BM25 参数 (k1, b) | ✅ | 使用 `BM25Okapi` 默认值 k1=1.5, b=0.75，标准 IR 参数 |\nartifacts/paper_drafts/bm25_code_review.md:16:| Per-repo 索引 | ✅ | 每个 repo 独立建 BM25 索引，避免跨 repo 污染 |\nartifacts/paper_drafts/bm25_code_review.md:19:**关于 `.split()` tokenization 的说明**: 空白分词对代码不是最优（如 `foo(self,` 作为单一 token），但作为 BM25 lexical baseline，这恰好是正确的设计选择——使用更精细的 code tokenizer 会引入代码特定知识，模糊 \"lexical vs structural\" 的对比边界。\nartifacts/paper_drafts/bm25_code_review.md:27:| 采样策略 | ✅ | Top-K by BM25 score（确定性，非随机采样） |\nartifacts/paper_drafts/bm25_code_review.md:29:| 训练 num_negatives=7 | ✅ | `run_m2_full_bm25_qwen.sh` L72: `--num-negatives 7`，与其他策略一致 |\nartifacts/paper_drafts/bm25_code_review.md:38:| Val record count | ✅ | val_bm25_s42=2980 = val_random_s42=2980 |\nartifacts/paper_drafts/bm25_code_review.md:42:| Schema 一致 | ✅ | 输出字段: query_id, query_tokens, pos_id, pos_tokens, pos_dataflow_distance, neg_candidates, candidate_tokens — 与其他策略完全一致 |\nartifacts/paper_drafts/bm25_code_review.md:43:| Seed 处理 | ✅ | Seed 仅用于选择 reference 文件，BM25 scoring 本身是确定性的，不需要随机种子 |\nartifacts/paper_drafts/bm25_code_review.md:49:| Repo < 2 files | ✅ | `if len(self.all_files) < 2: self.bm25 = None`，安全返回空 |\nartifacts/paper_drafts/bm25_code_review.md:50:| 候选池 < pool_size | ✅ | Fallback: BM25 结果 + 字母序补齐，不会 crash |\nartifacts/paper_drafts/bm25_code_review.md:51:| 空文件 | ✅ | `\"\".split()` → `[]`，BM25Okapi 正常处理，score=0 |\nartifacts/paper_drafts/bm25_code_review.md:61:| 不含 structural info | ✅ | BM25 仅用文件文本内容，无 dataflow/AST 信息 |\nartifacts/paper_drafts/bm25_code_review.md:64:**BM25 vs Embedding 本质区别**: BM25 在原始代码文本上计算词法相似度（TF-IDF weighted），embedding 在 pretrained encoder space 计算语义相似度。两者都不使用 structural information，是正确的 baseline 设计。\nartifacts/paper_drafts/bm25_code_review.md:76:        bm25_instances[idx] = inst  # 使用 reference 的 random negatives\nartifacts/paper_drafts/bm25_code_review.md:80:**影响**: 如果某 repo 目录缺失，该 repo 的所有 instance 会使用 reference（random）的 negatives，而非 BM25 negatives。输出文件不会报错，但这些 instance 实际是 random 策略。\nartifacts/paper_drafts/bm25_code_review.md:82:**当前风险**: **低**。Record counts 完全匹配（11308=11308），说明所有 instance 都被处理。且 overlap 分析显示 BM25 vs random 平均 overlap=15.5%，远低于 100%，说明绝大多数 instance 确实用了 BM25 negatives。\nartifacts/paper_drafts/bm25_code_review.md:90:remaining = [f for f in bm25_idx.all_files if f not in used]\nartifacts/paper_drafts/bm25_code_review.md:94:**影响**: 当 repo 的 .py 文件数 < pool_size+2 时，BM25 结果不够 50 个，补齐用字母序。这对 small repos (46/83 repos, avg 25.3 files) 有影响。\nartifacts/paper_drafts/bm25_code_review.md:96:**当前风险**: **极低**。补齐的文件仍不包含 query 和 positive。训练时从 50 中选 7 个，BM25 top-ranked 的文件会被优先选为 hard negatives（由 hard_negative_mining 模块控制）。字母序 padding 只影响 pool 尾部的 easy negatives。\nartifacts/paper_drafts/bm25_code_review.md:100:### ⚠️ P3: BM25 query 使用原始文件内容而非 mutated query_tokens（设计选择）\nartifacts/paper_drafts/bm25_code_review.md:107:**说明**: BM25 scoring 使用 repo 磁盘上的原始文件内容，而非 reference instance 中的 `query_tokens`（mutated version）。由于 mutations 保留了大部分代码结构，BM25 ranking 差异可忽略。且所有策略的训练数据都使用同一 `query_tokens`，模型看到的输入是一致的。\nartifacts/paper_drafts/bm25_code_review.md:115:来自 `bm25_overlap_stratified.json` (s42, K=7):\nartifacts/paper_drafts/bm25_code_review.md:119:| BM25 vs Random | 15.5% | BM25 与随机有低 overlap，符合预期 |\nartifacts/paper_drafts/bm25_code_review.md:120:| BM25 vs Embedding | 30.6% | BM25 与 embedding 有中等 overlap，合理（都偏好相似文件） |\nartifacts/paper_drafts/bm25_code_review.md:121:| BM25 vs Dataflow | 25.5% | BM25 与 dataflow 低于 embedding，说明 structural info 选择了不同的 negatives |\nartifacts/paper_drafts/bm25_code_review.md:124:- Small (<50 files): overlap 高（BM25 vs embedding: 43.7%）— 候选池小，策略区分度低\nartifacts/paper_drafts/bm25_code_review.md:125:- Medium (50-200): overlap 适中（BM25 vs embedding: 19.1%）\nartifacts/paper_drafts/bm25_code_review.md:126:- Large (200+): overlap 低（BM25 vs embedding: 6.9%）— 策略区分度最高\nartifacts/paper_drafts/bm25_code_review.md:128:结论：overlap 分布合理，BM25 确实提供了与其他策略不同的 negative mining 视角。\nartifacts/paper_drafts/bm25_code_review.md:134:**BM25 Phase 2 训练可以安全进行。** ✅\nartifacts/paper_drafts/bm25_code_review.md:136:代码逻辑正确，数据一致性已验证，无 blocking issues。三个 ⚠️ 均为低风险的设计细节，不影响实验结论的有效性。BM25 作为 lexical baseline 的定位准确——使用标准 BM25Okapi 参数、空白分词、same candidate pool、same training config，与 embedding/dataflow 策略形成了合理的对照。\nartifacts/paper_drafts/related_work_v1.md:5:[Omitted long matching line]\nartifacts/paper_drafts/related_work_v1.md:9:Critically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.\nartifacts/paper_drafts/related_work_v1.md:15:[Omitted long matching line]\nartifacts/paper_drafts/related_work_v1.md:21:[Omitted long matching line]\nartifacts/paper_drafts/related_work_v1.md:25:[Omitted long matching line]\nartifacts/paper_drafts/introduction_v2.md:12:Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nartifacts/paper_drafts/introduction_v2.md:13:Notably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\nartifacts/paper_drafts/introduction_v2.md:15:We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nartifacts/paper_drafts/introduction_v2.md:16:Using CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nartifacts/paper_drafts/introduction_v2.md:17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.\nartifacts/paper_drafts/introduction_v2.md:22:[Omitted long matching line]\nartifacts/paper_drafts/introduction_v2.md:23:Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\nartifacts/paper_drafts/introduction_v2.md:28:\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\nartifacts/paper_drafts/introduction_v2.md:29:\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\nartifacts/paper_drafts/claim2_wording_review.md:24:| Story Spine - contribution (2) | \"observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis\" | ⚠️ 偏强 | 缺 \"exploratory\" 标签；\"provide mechanistic analysis\" 暗示已完成验证 |\nartifacts/paper_drafts/claim2_wording_review.md:45:| §4.3 Pilot (ii) | \"the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder\" | ✅ 合适 | 限定在 pilot 结果描述 |\nartifacts/paper_drafts/claim2_wording_review.md:47:| §4.4 Mechanistic hypothesis body | \"When the pretrained space is saturated, the encoder has limited room...Embedding-distance negatives provide a direct optimization target...Dataflow-aware negatives...may not align with the encoder's most informative gradient direction\" | ⚠️ 偏强 | 前半段读为已确认的解释（\"the encoder has limited room\"），后半段用 \"may not align\" 有 hedge。整体偏 explanatory 而非 hypothesis |\nartifacts/paper_drafts/claim2_wording_review.md:55:| §5.2 首句 | \"reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit\" | ❌ 过强 | \"reveals\" + \"predicts\" 双重断言 |\nartifacts/paper_drafts/claim2_wording_review.md:156:- 我们提供 testable prediction: pos_sim > 0.98 时 structure-grounded negatives 更有效。这比纯 empirical 结果更有 scientific value\nartifacts/paper_drafts/claim2_wording_review.md:173:- 如果审稿人认为不够，可考虑升级 Claim 3 的呈现方式或添加 BM25 baseline 作为第四个贡献点\nartifacts/paper_drafts/claim2_wording_review.md:182:### 攻击 5: \"Dataflow 两个编码器都不如 embedding，interaction 在哪?\"\nartifacts/paper_drafts/claim2_wording_review.md:183:**预期措辞**: \"Both encoders show dataflow < embedding. Where is the interaction? The pattern is uniformly negative.\"\nartifacts/paper_drafts/claim2_wording_review.md:185:- Interaction 不是 \"dataflow sometimes wins\"，而是 gap magnitude is encoder-dependent (Qwen -1.2pp vs StarCoder -1.0pp, 或 full M2 数据)\nartifacts/paper_drafts/claim2_wording_review.md:187:- 更根本的 interaction 是 dataflow vs random: Qwen +0.8pp, StarCoder -0.5pp (pilot)——方向相反\nartifacts/paper_drafts/claim2_wording_review.md:188:- 但要诚实: 如果 full M2 显示两个编码器 dataflow vs random 都为负，interaction claim 进一步弱化\nartifacts/paper_drafts/figure_design_v1.md:18:│ Bug      │      │ Data-flow    │      │ Mining       │      │ Fine-tuning  │\nartifacts/paper_drafts/figure_design_v1.md:25:                                         │ Dataflow  │\nartifacts/paper_drafts/figure_design_v1.md:30:- Extraction block: CodeQL logo/icon, arrows showing inter-procedural data-flow paths crossing file boundaries, output = Graph G (nodes=files, edges=data-flow)\nartifacts/paper_drafts/figure_design_v1.md:31:- Mining block: 3 parallel branches for the 3 strategies, each with a mini-icon (dice for random, cosine curve for embedding, graph for dataflow). Show query → candidate selection for each\nartifacts/paper_drafts/figure_design_v1.md:38:- Color: 3 distinct colors for the 3 strategies — use Okabe-Ito palette consistently across all figures (orange=#E69F00 for random, blue=#0072B2 for embedding, green=#009E73 for dataflow)\nartifacts/paper_drafts/figure_design_v1.md:49:**Purpose**: Make the 3 strategies intuitive. Directly supports §3.4 and helps readers understand what \"structurally disconnected but textually similar\" means concretely.\nartifacts/paper_drafts/figure_design_v1.md:55:(a) Random               (b) Embedding-distance      (c) Dataflow-aware\nartifacts/paper_drafts/figure_design_v1.md:69:- File nodes arranged as a graph with data-flow edges (solid lines)\nartifacts/paper_drafts/figure_design_v1.md:71:- Gold/positive file (green fill, connected to query via data-flow)\nartifacts/paper_drafts/figure_design_v1.md:74:- (b) Embedding: negatives clustered near query in embedding space (shown as spatial proximity), some connected via data-flow\nartifacts/paper_drafts/figure_design_v1.md:75:- (c) Dataflow: negatives near query in embedding space BUT with no data-flow edges to gold files — dashed lines showing \"no connection\"\nartifacts/paper_drafts/figure_design_v1.md:77:Key visual element: data-flow edges drawn as solid gray lines between connected nodes; absence of edges for dataflow-aware negatives emphasized with ✕ or dotted-line-with-cross.\nartifacts/paper_drafts/figure_design_v1.md:84:- Add a small \"sim(q, f⁻)\" annotation showing relative similarity values\nartifacts/paper_drafts/figure_design_v1.md:85:- Reference style: similar to GraphCodeBERT (Guo et al. 2021) data-flow illustrations\nartifacts/paper_drafts/figure_design_v1.md:94:**Purpose**: Visual summary of Table 1 main results. Supports Claim 1 (embedding mining suffices) and Claim 2 (dataflow encoder-dependent).\nartifacts/paper_drafts/figure_design_v1.md:106:- X-axis: 4 strategies (Random, BM25-mined, Embedding-distance, Dataflow-aware)\nartifacts/paper_drafts/figure_design_v1.md:110:- Horizontal dashed line: BM25 retrieval baseline (no training)\nartifacts/paper_drafts/figure_design_v1.md:116:- Embedding/dataflow seeds: not yet started\nartifacts/paper_drafts/figure_design_v1.md:131:**Purpose**: Visual evidence for the mechanistic hypothesis (Claim 2). Shows WHY embedding mining works and why dataflow interacts with encoder geometry.\nartifacts/paper_drafts/figure_design_v1.md:164:- Qwen 2048t: random margin=0.074, embedding margin=0.017, dataflow margin=0.029\nartifacts/paper_drafts/figure_design_v1.md:165:- StarCoder 2048t: random margin=0.194, embedding margin=0.067, dataflow margin=0.119\nartifacts/paper_drafts/figure_design_v1.md:166:- SC/Qwen ratio: random=2.61, embedding=3.94, dataflow=4.07\nartifacts/paper_drafts/figure_design_v1.md:194: │     ─△─ Dataflow\nartifacts/paper_drafts/figure_design_v1.md:228: │   / ──── Dataflow\nartifacts/paper_drafts/figure_design_v1.md:264: │  ██ BM25\nartifacts/paper_drafts/figure_design_v1.md:273:- 3 bars (BM25 baseline, random-trained, embedding-trained)\nartifacts/paper_drafts/figure_design_v1.md:290:**Purpose**: Disentangle the dataflow strategy's effectiveness from confound variables (repo size, pool size). Addresses the 99.3% rich-dataflow-in-large-repos confound identified in plan_005.\nartifacts/paper_drafts/figure_design_v1.md:296: │  ██ Rich dataflow (≥5 edges)\nartifacts/paper_drafts/figure_design_v1.md:304:- Show per-stratum R@1 delta between embedding and dataflow strategies\nartifacts/paper_drafts/figure_design_v1.md:309:- Confound analysis available: rich-dataflow 99.3% in large/xlarge repos\nartifacts/paper_drafts/figure_design_v1.md:314:- If dataflow benefit is stratum-dependent, figure is more effective than table\nartifacts/paper_drafts/figure_design_v1.md:345:- Dataflow-aware: #009E73 (green)\nartifacts/paper_drafts/figure_design_v1.md:346:- BM25: #CC79A7 (pink/mauve)",
    "numLines": 151
  },
  "sourceToolAssistantUUID": "ce8be6a3-4275-4231-b839-240ec0683cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-15T02:12:27.356Z_

```json
{
  "parentUuid": "1462d8fb-e30d-4a5c-b213-da96d23dbd71",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fb763362-3350-4e52-82c4-b2d75f6d14dd",
  "timestamp": "2026-05-15T02:12:27.356Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "leafUuid": "fb763362-3350-4e52-82c4-b2d75f6d14dd",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix dataflow-aware strategy description in paper",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Tool call

_source line 37 · 2026-05-15T02:12:29.660Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EGSA28WYY9TH3pZDDXV9Q7`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/cf51224d-fd16-44c7-b53d-2f35ec8def65/tool-results/toolu_016CvRLjYwFdQbQsKiN3PEWG.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb763362-3350-4e52-82c4-b2d75f6d14dd",
  "isSidechain": false,
  "requestId": "req_011Cb3YYgsaqA1BNVDPkmuzc",
  "type": "assistant",
  "uuid": "1be35b77-dbda-4fe9-9d4d-f8a9b734783f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELJToTBpLYFuq1o3n6pRdL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 35559,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 35559,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 896
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

_source line 38 · 2026-05-15T02:12:29.926Z_

<details><summary>↩ Tool result · `toolu_01EGSA28WYY9TH3pZDDXV9Q7`</summary>

```text
1	artifacts/paper_drafts/discussion_v2.md:6:[Omitted long matching line]
2	artifacts/paper_drafts/discussion_v2.md:12:[Omitted long matching line]
3	artifacts/paper_drafts/discussion_v2.md:14:[Omitted long matching line]
4	artifacts/paper_drafts/discussion_v2.md:20:Our negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.
5	artifacts/paper_drafts/discussion_v2.md:22:[Omitted long matching line]
6	artifacts/paper_drafts/discussion_v2.md:24:[Omitted long matching line]
7	artifacts/paper_drafts/discussion_v2.md:26:[Omitted long matching line]
8	artifacts/paper_drafts/discussion_v2.md:34:**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.
9	artifacts/paper_drafts/discussion_v2.md:36:**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).
10	artifacts/paper_drafts/discussion_v2.md:40:**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.
11	artifacts/paper_drafts/experiment_setup_v1.md:7:[Omitted long matching line]
12	artifacts/paper_drafts/experiment_setup_v1.md:17:[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]
13	artifacts/paper_drafts/experiment_setup_v1.md:59:**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].
14	artifacts/paper_drafts/experiment_setup_v1.md:70:- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).
15	artifacts/paper_drafts/method_v1.md:7:We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:
16	artifacts/paper_drafts/method_v1.md:13:The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.
17	artifacts/paper_drafts/method_v1.md:17:### CodeQL Bounded Data-Flow Analysis
18	artifacts/paper_drafts/method_v1.md:19:We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:
19	artifacts/paper_drafts/method_v1.md:22:- **Data-flow graph**: inter-procedural data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.
20	artifacts/paper_drafts/method_v1.md:26:From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.
21	artifacts/paper_drafts/method_v1.md:30:At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].
22	artifacts/paper_drafts/method_v1.md:51:We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.
23	artifacts/paper_drafts/method_v1.md:63:We compute embeddings for all files and queries using $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:
24	artifacts/paper_drafts/method_v1.md:69:### Dataflow-Aware Negatives
25	artifacts/paper_drafts/method_v1.md:75:where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:
26	artifacts/paper_drafts/method_v1.md:79:[Omitted long matching line]
27	artifacts/paper_drafts/method_v1.md:81:For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).
28	artifacts/paper_drafts/method_v1.md:85:[Omitted long matching line]
29	artifacts/paper_drafts/method_v1.md:87:### Relationship to BM25 Baselines
30	artifacts/paper_drafts/method_v1.md:89:[Omitted long matching line]
31	artifacts/paper_drafts/experiments_v1.md:5:[Omitted long matching line]
32	artifacts/paper_drafts/experiments_v1.md:11:[Omitted long matching line]
33	artifacts/paper_drafts/experiments_v1.md:21:[Omitted long matching line]
34	artifacts/paper_drafts/experiments_v1.md:23:[Omitted long matching line]
35	artifacts/paper_drafts/experiments_v1.md:36:| BM25 (no training) | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} |
36	artifacts/paper_drafts/experiments_v1.md:38:| BM25-mined | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
37	artifacts/paper_drafts/experiments_v1.md:40:| Dataflow-aware | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
38	artifacts/paper_drafts/experiments_v1.md:42:[Omitted long matching line]
39	artifacts/paper_drafts/experiments_v1.md:54:| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |
40	artifacts/paper_drafts/experiments_v1.md:56:The pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.
41	artifacts/paper_drafts/experiments_v1.md:84:| BM25 | \placeholder{X.X%} |
42	artifacts/paper_drafts/experiments_v1.md:92:A central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.
43	artifacts/paper_drafts/experiments_v1.md:101:| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |
44	artifacts/paper_drafts/experiments_v1.md:107:[Omitted long matching line]
45	artifacts/paper_drafts/experiments_v1.md:109:[Omitted long matching line]
46	artifacts/paper_drafts/experiments_v1.md:113:We stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.
47	artifacts/paper_drafts/experiments_v1.md:119:| Rich dataflow ($\geq$5 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
48	artifacts/paper_drafts/experiments_v1.md:120:| Sparse dataflow (1–4 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
49	artifacts/paper_drafts/experiments_v1.md:123:Confound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.
50	artifacts/paper_drafts/experiments_v1.md:140:[Omitted long matching line]
51	artifacts/paper_drafts/introduction_v1.md:6:In practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.
52	artifacts/paper_drafts/introduction_v1.md:12:These methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.
53	artifacts/paper_drafts/introduction_v1.md:18:We present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.
54	artifacts/paper_drafts/introduction_v1.md:22:Beyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.
55	artifacts/paper_drafts/introduction_v1.md:28:[Omitted long matching line]
56	artifacts/paper_drafts/introduction_v1.md:30:3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.
57	artifacts/paper_drafts/experimental_setup_k_checkpoint.md:16:| m2_embed_verify / dataflow | Qwen | dataflow | step 500 (0.5602) | step 500 (0.5436) | Yes |
58	artifacts/paper_drafts/experimental_setup_k_checkpoint.md:19:| plan_013_starcoder / dataflow | StarCoder | dataflow | step 1000 (0.5255) | final (0.5078 > 0.4869@1000) | **No** |
59	artifacts/paper_drafts/experimental_setup_k_checkpoint.md:33:[Omitted long matching line]
60	artifacts/paper_drafts/bm25_code_review.md:1:# BM25 Negative Mining Code Review
61	artifacts/paper_drafts/bm25_code_review.md:3:**File**: `/root/structfuse/scripts/mine_bm25_negatives.py` (251 lines)
62	artifacts/paper_drafts/bm25_code_review.md:9:## 1. BM25 索引构建
63	artifacts/paper_drafts/bm25_code_review.md:15:| BM25 参数 (k1, b) | ✅ | 使用 `BM25Okapi` 默认值 k1=1.5, b=0.75，标准 IR 参数 |
64	artifacts/paper_drafts/bm25_code_review.md:16:| Per-repo 索引 | ✅ | 每个 repo 独立建 BM25 索引，避免跨 repo 污染 |
65	artifacts/paper_drafts/bm25_code_review.md:19:**关于 `.split()` tokenization 的说明**: 空白分词对代码不是最优（如 `foo(self,` 作为单一 token），但作为 BM25 lexical baseline，这恰好是正确的设计选择——使用更精细的 code tokenizer 会引入代码特定知识，模糊 "lexical vs structural" 的对比边界。
66	artifacts/paper_drafts/bm25_code_review.md:27:| 采样策略 | ✅ | Top-K by BM25 score（确定性，非随机采样） |
67	artifacts/paper_drafts/bm25_code_review.md:29:| 训练 num_negatives=7 | ✅ | `run_m2_full_bm25_qwen.sh` L72: `--num-negatives 7`，与其他策略一致 |
68	artifacts/paper_drafts/bm25_code_review.md:38:| Val record count | ✅ | val_bm25_s42=2980 = val_random_s42=2980 |
69	artifacts/paper_drafts/bm25_code_review.md:42:| Schema 一致 | ✅ | 输出字段: query_id, query_tokens, pos_id, pos_tokens, pos_dataflow_distance, neg_candidates, candidate_tokens — 与其他策略完全一致 |
70	artifacts/paper_drafts/bm25_code_review.md:43:| Seed 处理 | ✅ | Seed 仅用于选择 reference 文件，BM25 scoring 本身是确定性的，不需要随机种子 |
71	artifacts/paper_drafts/bm25_code_review.md:49:| Repo < 2 files | ✅ | `if len(self.all_files) < 2: self.bm25 = None`，安全返回空 |
72	artifacts/paper_drafts/bm25_code_review.md:50:| 候选池 < pool_size | ✅ | Fallback: BM25 结果 + 字母序补齐，不会 crash |
73	artifacts/paper_drafts/bm25_code_review.md:51:| 空文件 | ✅ | `"".split()` → `[]`，BM25Okapi 正常处理，score=0 |
74	artifacts/paper_drafts/bm25_code_review.md:61:| 不含 structural info | ✅ | BM25 仅用文件文本内容，无 dataflow/AST 信息 |
75	artifacts/paper_drafts/bm25_code_review.md:64:**BM25 vs Embedding 本质区别**: BM25 在原始代码文本上计算词法相似度（TF-IDF weighted），embedding 在 pretrained encoder space 计算语义相似度。两者都不使用 structural information，是正确的 baseline 设计。
76	artifacts/paper_drafts/bm25_code_review.md:76:        bm25_instances[idx] = inst  # 使用 reference 的 random negatives
77	artifacts/paper_drafts/bm25_code_review.md:80:**影响**: 如果某 repo 目录缺失，该 repo 的所有 instance 会使用 reference（random）的 negatives，而非 BM25 negatives。输出文件不会报错，但这些 instance 实际是 random 策略。
78	artifacts/paper_drafts/bm25_code_review.md:82:**当前风险**: **低**。Record counts 完全匹配（11308=11308），说明所有 instance 都被处理。且 overlap 分析显示 BM25 vs random 平均 overlap=15.5%，远低于 100%，说明绝大多数 instance 确实用了 BM25 negatives。
79	artifacts/paper_drafts/bm25_code_review.md:90:remaining = [f for f in bm25_idx.all_files if f not in used]
80	artifacts/paper_drafts/bm25_code_review.md:94:**影响**: 当 repo 的 .py 文件数 < pool_size+2 时，BM25 结果不够 50 个，补齐用字母序。这对 small repos (46/83 repos, avg 25.3 files) 有影响。
81	artifacts/paper_drafts/bm25_code_review.md:96:**当前风险**: **极低**。补齐的文件仍不包含 query 和 positive。训练时从 50 中选 7 个，BM25 top-ranked 的文件会被优先选为 hard negatives（由 hard_negative_mining 模块控制）。字母序 padding 只影响 pool 尾部的 easy negatives。
82	artifacts/paper_drafts/bm25_code_review.md:100:### ⚠️ P3: BM25 query 使用原始文件内容而非 mutated query_tokens（设计选择）
83	artifacts/paper_drafts/bm25_code_review.md:107:**说明**: BM25 scoring 使用 repo 磁盘上的原始文件内容，而非 reference instance 中的 `query_tokens`（mutated version）。由于 mutations 保留了大部分代码结构，BM25 ranking 差异可忽略。且所有策略的训练数据都使用同一 `query_tokens`，模型看到的输入是一致的。
84	artifacts/paper_drafts/bm25_code_review.md:115:来自 `bm25_overlap_stratified.json` (s42, K=7):
85	artifacts/paper_drafts/bm25_code_review.md:119:| BM25 vs Random | 15.5% | BM25 与随机有低 overlap，符合预期 |
86	artifacts/paper_drafts/bm25_code_review.md:120:| BM25 vs Embedding | 30.6% | BM25 与 embedding 有中等 overlap，合理（都偏好相似文件） |
87	artifacts/paper_drafts/bm25_code_review.md:121:| BM25 vs Dataflow | 25.5% | BM25 与 dataflow 低于 embedding，说明 structural info 选择了不同的 negatives |
88	artifacts/paper_drafts/bm25_code_review.md:124:- Small (<50 files): overlap 高（BM25 vs embedding: 43.7%）— 候选池小，策略区分度低
89	artifacts/paper_drafts/bm25_code_review.md:125:- Medium (50-200): overlap 适中（BM25 vs embedding: 19.1%）
90	artifacts/paper_drafts/bm25_code_review.md:126:- Large (200+): overlap 低（BM25 vs embedding: 6.9%）— 策略区分度最高
91	artifacts/paper_drafts/bm25_code_review.md:128:结论：overlap 分布合理，BM25 确实提供了与其他策略不同的 negative mining 视角。
92	artifacts/paper_drafts/bm25_code_review.md:134:**BM25 Phase 2 训练可以安全进行。** ✅
93	artifacts/paper_drafts/bm25_code_review.md:136:代码逻辑正确，数据一致性已验证，无 blocking issues。三个 ⚠️ 均为低风险的设计细节，不影响实验结论的有效性。BM25 作为 lexical baseline 的定位准确——使用标准 BM25Okapi 参数、空白分词、same candidate pool、same training config，与 embedding/dataflow 策略形成了合理的对照。
94	artifacts/paper_drafts/related_work_v1.md:5:[Omitted long matching line]
95	artifacts/paper_drafts/related_work_v1.md:9:Critically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.
96	artifacts/paper_drafts/related_work_v1.md:15:[Omitted long matching line]
97	artifacts/paper_drafts/related_work_v1.md:21:[Omitted long matching line]
98	artifacts/paper_drafts/related_work_v1.md:25:[Omitted long matching line]
99	artifacts/paper_drafts/introduction_v2.md:12:Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.
100	artifacts/paper_drafts/introduction_v2.md:13:Notably, files that are close in embedding space may be structurally connected through shared data-flow paths \cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.
101	artifacts/paper_drafts/introduction_v2.md:15:We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.
102	artifacts/paper_drafts/introduction_v2.md:16:Using CodeQL \cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.
103	artifacts/paper_drafts/introduction_v2.md:17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.
104	artifacts/paper_drafts/introduction_v2.md:22:[Omitted long matching line]
105	artifacts/paper_drafts/introduction_v2.md:23:Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\% timeout rate and [TBD]\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.
106	artifacts/paper_drafts/introduction_v2.md:28:\item \textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.
107	artifacts/paper_drafts/introduction_v2.md:29:\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.
108	artifacts/paper_drafts/claim2_wording_review.md:24:| Story Spine - contribution (2) | "observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis" | ⚠️ 偏强 | 缺 "exploratory" 标签；"provide mechanistic analysis" 暗示已完成验证 |
109	artifacts/paper_drafts/claim2_wording_review.md:45:| §4.3 Pilot (ii) | "the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder" | ✅ 合适 | 限定在 pilot 结果描述 |
110	artifacts/paper_drafts/claim2_wording_review.md:47:| §4.4 Mechanistic hypothesis body | "When the pretrained space is saturated, the encoder has limited room...Embedding-distance negatives provide a direct optimization target...Dataflow-aware negatives...may not align with the encoder's most informative gradient direction" | ⚠️ 偏强 | 前半段读为已确认的解释（"the encoder has limited room"），后半段用 "may not align" 有 hedge。整体偏 explanatory 而非 hypothesis |
111	artifacts/paper_drafts/claim2_wording_review.md:55:| §5.2 首句 | "reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit" | ❌ 过强 | "reveals" + "predicts" 双重断言 |
112	artifacts/paper_drafts/claim2_wording_review.md:156:- 我们提供 testable prediction: pos_sim > 0.98 时 structure-grounded negatives 更有效。这比纯 empirical 结果更有 scientific value
113	artifacts/paper_drafts/claim2_wording_review.md:173:- 如果审稿人认为不够，可考虑升级 Claim 3 的呈现方式或添加 BM25 baseline 作为第四个贡献点
114	artifacts/paper_drafts/claim2_wording_review.md:182:### 攻击 5: "Dataflow 两个编码器都不如 embedding，interaction 在哪?"
115	artifacts/paper_drafts/claim2_wording_review.md:183:**预期措辞**: "Both encoders show dataflow < embedding. Where is the interaction? The pattern is uniformly negative."
116	artifacts/paper_drafts/claim2_wording_review.md:185:- Interaction 不是 "dataflow sometimes wins"，而是 gap magnitude is encoder-dependent (Qwen -1.2pp vs StarCoder -1.0pp, 或 full M2 数据)
117	artifacts/paper_drafts/claim2_wording_review.md:187:- 更根本的 interaction 是 dataflow vs random: Qwen +0.8pp, StarCoder -0.5pp (pilot)——方向相反
118	artifacts/paper_drafts/claim2_wording_review.md:188:- 但要诚实: 如果 full M2 显示两个编码器 dataflow vs random 都为负，interaction claim 进一步弱化
119	artifacts/paper_drafts/figure_design_v1.md:18:│ Bug      │      │ Data-flow    │      │ Mining       │      │ Fine-tuning  │
120	artifacts/paper_drafts/figure_design_v1.md:25:                                         │ Dataflow  │
121	artifacts/paper_drafts/figure_design_v1.md:30:- Extraction block: CodeQL logo/icon, arrows showing inter-procedural data-flow paths crossing file boundaries, output = Graph G (nodes=files, edges=data-flow)
122	artifacts/paper_drafts/figure_design_v1.md:31:- Mining block: 3 parallel branches for the 3 strategies, each with a mini-icon (dice for random, cosine curve for embedding, graph for dataflow). Show query → candidate selection for each
123	artifacts/paper_drafts/figure_design_v1.md:38:- Color: 3 distinct colors for the 3 strategies — use Okabe-Ito palette consistently across all figures (orange=#E69F00 for random, blue=#0072B2 for embedding, green=#009E73 for dataflow)
124	artifacts/paper_drafts/figure_design_v1.md:49:**Purpose**: Make the 3 strategies intuitive. Directly supports §3.4 and helps readers understand what "structurally disconnected but textually similar" means concretely.
125	artifacts/paper_drafts/figure_design_v1.md:55:(a) Random               (b) Embedding-distance      (c) Dataflow-aware
126	artifacts/paper_drafts/figure_design_v1.md:69:- File nodes arranged as a graph with data-flow edges (solid lines)
127	artifacts/paper_drafts/figure_design_v1.md:71:- Gold/positive file (green fill, connected to query via data-flow)
128	artifacts/paper_drafts/figure_design_v1.md:74:- (b) Embedding: negatives clustered near query in embedding space (shown as spatial proximity), some connected via data-flow
129	artifacts/paper_drafts/figure_design_v1.md:75:- (c) Dataflow: negatives near query in embedding space BUT with no data-flow edges to gold files — dashed lines showing "no connection"
130	artifacts/paper_drafts/figure_design_v1.md:77:Key visual element: data-flow edges drawn as solid gray lines between connected nodes; absence of edges for dataflow-aware negatives emphasized with ✕ or dotted-line-with-cross.
131	artifacts/paper_drafts/figure_design_v1.md:84:- Add a small "sim(q, f⁻)" annotation showing relative similarity values
132	artifacts/paper_drafts/figure_design_v1.md:85:- Reference style: similar to GraphCodeBERT (Guo et al. 2021) data-flow illustrations
133	artifacts/paper_drafts/figure_design_v1.md:94:**Purpose**: Visual summary of Table 1 main results. Supports Claim 1 (embedding mining suffices) and Claim 2 (dataflow encoder-dependent).
134	artifacts/paper_drafts/figure_design_v1.md:106:- X-axis: 4 strategies (Random, BM25-mined, Embedding-distance, Dataflow-aware)
135	artifacts/paper_drafts/figure_design_v1.md:110:- Horizontal dashed line: BM25 retrieval baseline (no training)
136	artifacts/paper_drafts/figure_design_v1.md:116:- Embedding/dataflow seeds: not yet started
137	artifacts/paper_drafts/figure_design_v1.md:131:**Purpose**: Visual evidence for the mechanistic hypothesis (Claim 2). Shows WHY embedding mining works and why dataflow interacts with encoder geometry.
138	artifacts/paper_drafts/figure_design_v1.md:164:- Qwen 2048t: random margin=0.074, embedding margin=0.017, dataflow margin=0.029
139	artifacts/paper_drafts/figure_design_v1.md:165:- StarCoder 2048t: random margin=0.194, embedding margin=0.067, dataflow margin=0.119
140	artifacts/paper_drafts/figure_design_v1.md:166:- SC/Qwen ratio: random=2.61, embedding=3.94, dataflow=4.07
141	artifacts/paper_drafts/figure_design_v1.md:194: │     ─△─ Dataflow
142	artifacts/paper_drafts/figure_design_v1.md:228: │   / ──── Dataflow
143	artifacts/paper_drafts/figure_design_v1.md:264: │  ██ BM25
144	artifacts/paper_drafts/figure_design_v1.md:273:- 3 bars (BM25 baseline, random-trained, embedding-trained)
145	artifacts/paper_drafts/figure_design_v1.md:290:**Purpose**: Disentangle the dataflow strategy's effectiveness from confound variables (repo size, pool size). Addresses the 99.3% rich-dataflow-in-large-repos confound identified in plan_005.
146	artifacts/paper_drafts/figure_design_v1.md:296: │  ██ Rich dataflow (≥5 edges)
147	artifacts/paper_drafts/figure_design_v1.md:304:- Show per-stratum R@1 delta between embedding and dataflow strategies
148	artifacts/paper_drafts/figure_design_v1.md:309:- Confound analysis available: rich-dataflow 99.3% in large/xlarge repos
149	artifacts/paper_drafts/figure_design_v1.md:314:- If dataflow benefit is stratum-dependent, figure is more effective than table
150	artifacts/paper_drafts/figure_design_v1.md:345:- Dataflow-aware: #009E73 (green)
151	artifacts/paper_drafts/figure_design_v1.md:346:- BM25: #CC79A7 (pink/mauve)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1be35b77-dbda-4fe9-9d4d-f8a9b734783f",
  "isSidechain": false,
  "promptId": "e0e0e99b-f04a-440d-b03d-7ba309184820",
  "type": "user",
  "uuid": "f27e2949-efe4-40f7-abee-56e24c7fa5af",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/cf51224d-fd16-44c7-b53d-2f35ec8def65/tool-results/toolu_016CvRLjYwFdQbQsKiN3PEWG.txt",
      "content": "artifacts/paper_drafts/discussion_v2.md:6:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:12:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:14:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:20:Our negative difficulty analysis (Section 4.4) suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether structure-grounded negatives will provide benefit beyond embedding-distance mining.\nartifacts/paper_drafts/discussion_v2.md:22:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:24:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:26:[Omitted long matching line]\nartifacts/paper_drafts/discussion_v2.md:34:**Single task.** We evaluate on code retrieval with contrastive training. Whether structure-grounded negatives similarly benefit other code understanding tasks (fault localization, code summarization, clone detection) remains an open question, though the underlying principle—that inter-procedural data-flow provides an orthogonal signal to text similarity—is task-agnostic.\nartifacts/paper_drafts/discussion_v2.md:36:**Language and tooling dependency.** Our pipeline relies on CodeQL for inter-procedural data-flow extraction and currently supports Python repositories only. Extending to other languages requires language-specific CodeQL queries, and the dependency on a commercial static analysis tool may limit reproducibility. We note that the methodology generalizes to any tool capable of inter-procedural data-flow analysis (e.g., Joern, Soot).\nartifacts/paper_drafts/discussion_v2.md:40:**Structural data coverage.** CodeQL successfully extracts data-flow information for 36% of instances across 123 repositories (93.9% repo coverage; Table 4). The remaining instances fall back to embedding-distance negatives. While our results demonstrate that even partial structural coverage yields measurable improvements, higher extraction success rates would likely amplify the benefit.\nartifacts/paper_drafts/experiment_setup_v1.md:7:[Omitted long matching line]\nartifacts/paper_drafts/experiment_setup_v1.md:17:[Source: plan_018 registry, confirmed identical across all four strategies (random, embedding, dataflow, BM25)]\nartifacts/paper_drafts/experiment_setup_v1.md:59:**Seeds.** 42, 43, 44. The core experiment consists of 3 strategies × 3 seeds × 2 encoders = 18 runs. BM25-mined negatives are evaluated as a supplementary comparison (additional 2 encoders × 3 seeds = 6 runs) [Source: plan_018 registry].\nartifacts/paper_drafts/experiment_setup_v1.md:70:- **Confidence intervals**: bootstrap 95% CIs for pairwise strategy comparisons (embedding vs. random, dataflow vs. random, dataflow vs. embedding).\nartifacts/paper_drafts/method_v1.md:7:We formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\nartifacts/paper_drafts/method_v1.md:13:The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\nartifacts/paper_drafts/method_v1.md:17:### CodeQL Bounded Data-Flow Analysis\nartifacts/paper_drafts/method_v1.md:19:We use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\nartifacts/paper_drafts/method_v1.md:22:- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\nartifacts/paper_drafts/method_v1.md:26:From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\nartifacts/paper_drafts/method_v1.md:30:At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\nartifacts/paper_drafts/method_v1.md:51:We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\nartifacts/paper_drafts/method_v1.md:63:We compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\nartifacts/paper_drafts/method_v1.md:69:### Dataflow-Aware Negatives\nartifacts/paper_drafts/method_v1.md:75:where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\nartifacts/paper_drafts/method_v1.md:79:[Omitted long matching line]\nartifacts/paper_drafts/method_v1.md:81:For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\nartifacts/paper_drafts/method_v1.md:85:[Omitted long matching line]\nartifacts/paper_drafts/method_v1.md:87:### Relationship to BM25 Baselines\nartifacts/paper_drafts/method_v1.md:89:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:5:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:11:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:21:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:23:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:36:| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\nartifacts/paper_drafts/experiments_v1.md:38:| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\nartifacts/paper_drafts/experiments_v1.md:40:| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\nartifacts/paper_drafts/experiments_v1.md:42:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:54:| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\nartifacts/paper_drafts/experiments_v1.md:56:The pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\nartifacts/paper_drafts/experiments_v1.md:84:| BM25 | \\placeholder{X.X%} |\nartifacts/paper_drafts/experiments_v1.md:92:A central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\nartifacts/paper_drafts/experiments_v1.md:101:| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\nartifacts/paper_drafts/experiments_v1.md:107:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:109:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:113:We stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\nartifacts/paper_drafts/experiments_v1.md:119:| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\nartifacts/paper_drafts/experiments_v1.md:120:| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\nartifacts/paper_drafts/experiments_v1.md:123:Confound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\nartifacts/paper_drafts/experiments_v1.md:140:[Omitted long matching line]\nartifacts/paper_drafts/introduction_v1.md:6:In practice, however, lexical similarity is an unreliable proxy for structural relevance: two files may share terminology yet have no functional relationship, while structurally coupled files—connected through data-flow or call dependencies—may use entirely different vocabulary.\nartifacts/paper_drafts/introduction_v1.md:12:These methods demonstrate the value of structural information, yet they apply it exclusively at inference time: the underlying retrieval encoder is trained without structural signal, and its embedding space is shaped solely by textual similarity.\nartifacts/paper_drafts/introduction_v1.md:18:We present a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random sampling, static embedding-distance mining, and structure-grounded negatives derived from inter-procedural data-flow analysis.\nartifacts/paper_drafts/introduction_v1.md:22:Beyond this primary result, we observe that structure-grounded (dataflow) negatives do not consistently outperform embedding mining but exhibit encoder-dependent interaction patterns: analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry—specifically, the degree of embedding space saturation—mediates which strategy is most effective, providing a mechanistic explanation for when and why different mining strategies yield different outcomes.\nartifacts/paper_drafts/introduction_v1.md:28:[Omitted long matching line]\nartifacts/paper_drafts/introduction_v1.md:30:3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \\cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.\nartifacts/paper_drafts/experimental_setup_k_checkpoint.md:16:| m2_embed_verify / dataflow | Qwen | dataflow | step 500 (0.5602) | step 500 (0.5436) | Yes |\nartifacts/paper_drafts/experimental_setup_k_checkpoint.md:19:| plan_013_starcoder / dataflow | StarCoder | dataflow | step 1000 (0.5255) | final (0.5078 > 0.4869@1000) | **No** |\nartifacts/paper_drafts/experimental_setup_k_checkpoint.md:33:[Omitted long matching line]\nartifacts/paper_drafts/bm25_code_review.md:1:# BM25 Negative Mining Code Review\nartifacts/paper_drafts/bm25_code_review.md:3:**File**: `/root/structfuse/scripts/mine_bm25_negatives.py` (251 lines)\nartifacts/paper_drafts/bm25_code_review.md:9:## 1. BM25 索引构建\nartifacts/paper_drafts/bm25_code_review.md:15:| BM25 参数 (k1, b) | ✅ | 使用 `BM25Okapi` 默认值 k1=1.5, b=0.75，标准 IR 参数 |\nartifacts/paper_drafts/bm25_code_review.md:16:| Per-repo 索引 | ✅ | 每个 repo 独立建 BM25 索引，避免跨 repo 污染 |\nartifacts/paper_drafts/bm25_code_review.md:19:**关于 `.split()` tokenization 的说明**: 空白分词对代码不是最优（如 `foo(self,` 作为单一 token），但作为 BM25 lexical baseline，这恰好是正确的设计选择——使用更精细的 code tokenizer 会引入代码特定知识，模糊 \"lexical vs structural\" 的对比边界。\nartifacts/paper_drafts/bm25_code_review.md:27:| 采样策略 | ✅ | Top-K by BM25 score（确定性，非随机采样） |\nartifacts/paper_drafts/bm25_code_review.md:29:| 训练 num_negatives=7 | ✅ | `run_m2_full_bm25_qwen.sh` L72: `--num-negatives 7`，与其他策略一致 |\nartifacts/paper_drafts/bm25_code_review.md:38:| Val record count | ✅ | val_bm25_s42=2980 = val_random_s42=2980 |\nartifacts/paper_drafts/bm25_code_review.md:42:| Schema 一致 | ✅ | 输出字段: query_id, query_tokens, pos_id, pos_tokens, pos_dataflow_distance, neg_candidates, candidate_tokens — 与其他策略完全一致 |\nartifacts/paper_drafts/bm25_code_review.md:43:| Seed 处理 | ✅ | Seed 仅用于选择 reference 文件，BM25 scoring 本身是确定性的，不需要随机种子 |\nartifacts/paper_drafts/bm25_code_review.md:49:| Repo < 2 files | ✅ | `if len(self.all_files) < 2: self.bm25 = None`，安全返回空 |\nartifacts/paper_drafts/bm25_code_review.md:50:| 候选池 < pool_size | ✅ | Fallback: BM25 结果 + 字母序补齐，不会 crash |\nartifacts/paper_drafts/bm25_code_review.md:51:| 空文件 | ✅ | `\"\".split()` → `[]`，BM25Okapi 正常处理，score=0 |\nartifacts/paper_drafts/bm25_code_review.md:61:| 不含 structural info | ✅ | BM25 仅用文件文本内容，无 dataflow/AST 信息 |\nartifacts/paper_drafts/bm25_code_review.md:64:**BM25 vs Embedding 本质区别**: BM25 在原始代码文本上计算词法相似度（TF-IDF weighted），embedding 在 pretrained encoder space 计算语义相似度。两者都不使用 structural information，是正确的 baseline 设计。\nartifacts/paper_drafts/bm25_code_review.md:76:        bm25_instances[idx] = inst  # 使用 reference 的 random negatives\nartifacts/paper_drafts/bm25_code_review.md:80:**影响**: 如果某 repo 目录缺失，该 repo 的所有 instance 会使用 reference（random）的 negatives，而非 BM25 negatives。输出文件不会报错，但这些 instance 实际是 random 策略。\nartifacts/paper_drafts/bm25_code_review.md:82:**当前风险**: **低**。Record counts 完全匹配（11308=11308），说明所有 instance 都被处理。且 overlap 分析显示 BM25 vs random 平均 overlap=15.5%，远低于 100%，说明绝大多数 instance 确实用了 BM25 negatives。\nartifacts/paper_drafts/bm25_code_review.md:90:remaining = [f for f in bm25_idx.all_files if f not in used]\nartifacts/paper_drafts/bm25_code_review.md:94:**影响**: 当 repo 的 .py 文件数 < pool_size+2 时，BM25 结果不够 50 个，补齐用字母序。这对 small repos (46/83 repos, avg 25.3 files) 有影响。\nartifacts/paper_drafts/bm25_code_review.md:96:**当前风险**: **极低**。补齐的文件仍不包含 query 和 positive。训练时从 50 中选 7 个，BM25 top-ranked 的文件会被优先选为 hard negatives（由 hard_negative_mining 模块控制）。字母序 padding 只影响 pool 尾部的 easy negatives。\nartifacts/paper_drafts/bm25_code_review.md:100:### ⚠️ P3: BM25 query 使用原始文件内容而非 mutated query_tokens（设计选择）\nartifacts/paper_drafts/bm25_code_review.md:107:**说明**: BM25 scoring 使用 repo 磁盘上的原始文件内容，而非 reference instance 中的 `query_tokens`（mutated version）。由于 mutations 保留了大部分代码结构，BM25 ranking 差异可忽略。且所有策略的训练数据都使用同一 `query_tokens`，模型看到的输入是一致的。\nartifacts/paper_drafts/bm25_code_review.md:115:来自 `bm25_overlap_stratified.json` (s42, K=7):\nartifacts/paper_drafts/bm25_code_review.md:119:| BM25 vs Random | 15.5% | BM25 与随机有低 overlap，符合预期 |\nartifacts/paper_drafts/bm25_code_review.md:120:| BM25 vs Embedding | 30.6% | BM25 与 embedding 有中等 overlap，合理（都偏好相似文件） |\nartifacts/paper_drafts/bm25_code_review.md:121:| BM25 vs Dataflow | 25.5% | BM25 与 dataflow 低于 embedding，说明 structural info 选择了不同的 negatives |\nartifacts/paper_drafts/bm25_code_review.md:124:- Small (<50 files): overlap 高（BM25 vs embedding: 43.7%）— 候选池小，策略区分度低\nartifacts/paper_drafts/bm25_code_review.md:125:- Medium (50-200): overlap 适中（BM25 vs embedding: 19.1%）\nartifacts/paper_drafts/bm25_code_review.md:126:- Large (200+): overlap 低（BM25 vs embedding: 6.9%）— 策略区分度最高\nartifacts/paper_drafts/bm25_code_review.md:128:结论：overlap 分布合理，BM25 确实提供了与其他策略不同的 negative mining 视角。\nartifacts/paper_drafts/bm25_code_review.md:134:**BM25 Phase 2 训练可以安全进行。** ✅\nartifacts/paper_drafts/bm25_code_review.md:136:代码逻辑正确，数据一致性已验证，无 blocking issues。三个 ⚠️ 均为低风险的设计细节，不影响实验结论的有效性。BM25 作为 lexical baseline 的定位准确——使用标准 BM25Okapi 参数、空白分词、same candidate pool、same training config，与 embedding/dataflow 策略形成了合理的对照。\nartifacts/paper_drafts/related_work_v1.md:5:[Omitted long matching line]\nartifacts/paper_drafts/related_work_v1.md:9:Critically, these graph-guided methods apply structural information exclusively at inference time; the underlying retrieval encoder is trained without structural signal. The encoder's embedding space is therefore optimized solely on textual similarity, potentially conflating lexically similar but structurally unrelated code. Our work addresses this gap by incorporating inter-procedural data-flow information into the training process through structure-grounded hard negative mining.\nartifacts/paper_drafts/related_work_v1.md:15:[Omitted long matching line]\nartifacts/paper_drafts/related_work_v1.md:21:[Omitted long matching line]\nartifacts/paper_drafts/related_work_v1.md:25:[Omitted long matching line]\nartifacts/paper_drafts/introduction_v2.md:12:Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nartifacts/paper_drafts/introduction_v2.md:13:Notably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\nartifacts/paper_drafts/introduction_v2.md:15:We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nartifacts/paper_drafts/introduction_v2.md:16:Using CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nartifacts/paper_drafts/introduction_v2.md:17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that filters structurally connected files from the embedding-distance candidate set.\nartifacts/paper_drafts/introduction_v2.md:22:[Omitted long matching line]\nartifacts/paper_drafts/introduction_v2.md:23:Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\nartifacts/paper_drafts/introduction_v2.md:28:\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\nartifacts/paper_drafts/introduction_v2.md:29:\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\nartifacts/paper_drafts/claim2_wording_review.md:24:| Story Spine - contribution (2) | \"observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis\" | ⚠️ 偏强 | 缺 \"exploratory\" 标签；\"provide mechanistic analysis\" 暗示已完成验证 |\nartifacts/paper_drafts/claim2_wording_review.md:45:| §4.3 Pilot (ii) | \"the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder\" | ✅ 合适 | 限定在 pilot 结果描述 |\nartifacts/paper_drafts/claim2_wording_review.md:47:| §4.4 Mechanistic hypothesis body | \"When the pretrained space is saturated, the encoder has limited room...Embedding-distance negatives provide a direct optimization target...Dataflow-aware negatives...may not align with the encoder's most informative gradient direction\" | ⚠️ 偏强 | 前半段读为已确认的解释（\"the encoder has limited room\"），后半段用 \"may not align\" 有 hedge。整体偏 explanatory 而非 hypothesis |\nartifacts/paper_drafts/claim2_wording_review.md:55:| §5.2 首句 | \"reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit\" | ❌ 过强 | \"reveals\" + \"predicts\" 双重断言 |\nartifacts/paper_drafts/claim2_wording_review.md:156:- 我们提供 testable prediction: pos_sim > 0.98 时 structure-grounded negatives 更有效。这比纯 empirical 结果更有 scientific value\nartifacts/paper_drafts/claim2_wording_review.md:173:- 如果审稿人认为不够，可考虑升级 Claim 3 的呈现方式或添加 BM25 baseline 作为第四个贡献点\nartifacts/paper_drafts/claim2_wording_review.md:182:### 攻击 5: \"Dataflow 两个编码器都不如 embedding，interaction 在哪?\"\nartifacts/paper_drafts/claim2_wording_review.md:183:**预期措辞**: \"Both encoders show dataflow < embedding. Where is the interaction? The pattern is uniformly negative.\"\nartifacts/paper_drafts/claim2_wording_review.md:185:- Interaction 不是 \"dataflow sometimes wins\"，而是 gap magnitude is encoder-dependent (Qwen -1.2pp vs StarCoder -1.0pp, 或 full M2 数据)\nartifacts/paper_drafts/claim2_wording_review.md:187:- 更根本的 interaction 是 dataflow vs random: Qwen +0.8pp, StarCoder -0.5pp (pilot)——方向相反\nartifacts/paper_drafts/claim2_wording_review.md:188:- 但要诚实: 如果 full M2 显示两个编码器 dataflow vs random 都为负，interaction claim 进一步弱化\nartifacts/paper_drafts/figure_design_v1.md:18:│ Bug      │      │ Data-flow    │      │ Mining       │      │ Fine-tuning  │\nartifacts/paper_drafts/figure_design_v1.md:25:                                         │ Dataflow  │\nartifacts/paper_drafts/figure_design_v1.md:30:- Extraction block: CodeQL logo/icon, arrows showing inter-procedural data-flow paths crossing file boundaries, output = Graph G (nodes=files, edges=data-flow)\nartifacts/paper_drafts/figure_design_v1.md:31:- Mining block: 3 parallel branches for the 3 strategies, each with a mini-icon (dice for random, cosine curve for embedding, graph for dataflow). Show query → candidate selection for each\nartifacts/paper_drafts/figure_design_v1.md:38:- Color: 3 distinct colors for the 3 strategies — use Okabe-Ito palette consistently across all figures (orange=#E69F00 for random, blue=#0072B2 for embedding, green=#009E73 for dataflow)\nartifacts/paper_drafts/figure_design_v1.md:49:**Purpose**: Make the 3 strategies intuitive. Directly supports §3.4 and helps readers understand what \"structurally disconnected but textually similar\" means concretely.\nartifacts/paper_drafts/figure_design_v1.md:55:(a) Random               (b) Embedding-distance      (c) Dataflow-aware\nartifacts/paper_drafts/figure_design_v1.md:69:- File nodes arranged as a graph with data-flow edges (solid lines)\nartifacts/paper_drafts/figure_design_v1.md:71:- Gold/positive file (green fill, connected to query via data-flow)\nartifacts/paper_drafts/figure_design_v1.md:74:- (b) Embedding: negatives clustered near query in embedding space (shown as spatial proximity), some connected via data-flow\nartifacts/paper_drafts/figure_design_v1.md:75:- (c) Dataflow: negatives near query in embedding space BUT with no data-flow edges to gold files — dashed lines showing \"no connection\"\nartifacts/paper_drafts/figure_design_v1.md:77:Key visual element: data-flow edges drawn as solid gray lines between connected nodes; absence of edges for dataflow-aware negatives emphasized with ✕ or dotted-line-with-cross.\nartifacts/paper_drafts/figure_design_v1.md:84:- Add a small \"sim(q, f⁻)\" annotation showing relative similarity values\nartifacts/paper_drafts/figure_design_v1.md:85:- Reference style: similar to GraphCodeBERT (Guo et al. 2021) data-flow illustrations\nartifacts/paper_drafts/figure_design_v1.md:94:**Purpose**: Visual summary of Table 1 main results. Supports Claim 1 (embedding mining suffices) and Claim 2 (dataflow encoder-dependent).\nartifacts/paper_drafts/figure_design_v1.md:106:- X-axis: 4 strategies (Random, BM25-mined, Embedding-distance, Dataflow-aware)\nartifacts/paper_drafts/figure_design_v1.md:110:- Horizontal dashed line: BM25 retrieval baseline (no training)\nartifacts/paper_drafts/figure_design_v1.md:116:- Embedding/dataflow seeds: not yet started\nartifacts/paper_drafts/figure_design_v1.md:131:**Purpose**: Visual evidence for the mechanistic hypothesis (Claim 2). Shows WHY embedding mining works and why dataflow interacts with encoder geometry.\nartifacts/paper_drafts/figure_design_v1.md:164:- Qwen 2048t: random margin=0.074, embedding margin=0.017, dataflow margin=0.029\nartifacts/paper_drafts/figure_design_v1.md:165:- StarCoder 2048t: random margin=0.194, embedding margin=0.067, dataflow margin=0.119\nartifacts/paper_drafts/figure_design_v1.md:166:- SC/Qwen ratio: random=2.61, embedding=3.94, dataflow=4.07\nartifacts/paper_drafts/figure_design_v1.md:194: │     ─△─ Dataflow\nartifacts/paper_drafts/figure_design_v1.md:228: │   / ──── Dataflow\nartifacts/paper_drafts/figure_design_v1.md:264: │  ██ BM25\nartifacts/paper_drafts/figure_design_v1.md:273:- 3 bars (BM25 baseline, random-trained, embedding-trained)\nartifacts/paper_drafts/figure_design_v1.md:290:**Purpose**: Disentangle the dataflow strategy's effectiveness from confound variables (repo size, pool size). Addresses the 99.3% rich-dataflow-in-large-repos confound identified in plan_005.\nartifacts/paper_drafts/figure_design_v1.md:296: │  ██ Rich dataflow (≥5 edges)\nartifacts/paper_drafts/figure_design_v1.md:304:- Show per-stratum R@1 delta between embedding and dataflow strategies\nartifacts/paper_drafts/figure_design_v1.md:309:- Confound analysis available: rich-dataflow 99.3% in large/xlarge repos\nartifacts/paper_drafts/figure_design_v1.md:314:- If dataflow benefit is stratum-dependent, figure is more effective than table\nartifacts/paper_drafts/figure_design_v1.md:345:- Dataflow-aware: #009E73 (green)\nartifacts/paper_drafts/figure_design_v1.md:346:- BM25: #CC79A7 (pink/mauve)",
      "numLines": 151,
      "startLine": 1,
      "totalLines": 151
    }
  },
  "sourceToolAssistantUUID": "1be35b77-dbda-4fe9-9d4d-f8a9b734783f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "leafUuid": "f27e2949-efe4-40f7-abee-56e24c7fa5af",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix dataflow-aware strategy description in paper",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Assistant

_source line 41 · 2026-05-15T02:12:34.865Z_

<details><summary>Logged reasoning block</summary>

```text
I need to check method_v1.md more carefully - specifically lines around 69-89 where it describes the "Dataflow-Aware Negatives" section. Let me read that file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f27e2949-efe4-40f7-abee-56e24c7fa5af",
  "isSidechain": false,
  "requestId": "req_011Cb3YYsurcd4uYDV2maupK",
  "type": "assistant",
  "uuid": "d3549127-efa7-4149-8a81-b6b3a4ca15bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jo6brXEvR5W18Gf2rc2QBe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9261,
      "cache_read_input_tokens": 36455,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 36455,
          "cache_creation_input_tokens": 9261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9261
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

_source line 42 · 2026-05-15T02:12:35.816Z_

The method_v1.md file has the most detailed dataflow-aware mechanism description. Let me read the critical section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3549127-efa7-4149-8a81-b6b3a4ca15bf",
  "isSidechain": false,
  "requestId": "req_011Cb3YYsurcd4uYDV2maupK",
  "type": "assistant",
  "uuid": "371afe15-16e0-4e15-8359-a01f8f3d9447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jo6brXEvR5W18Gf2rc2QBe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9261,
      "cache_read_input_tokens": 36455,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 36455,
          "cache_creation_input_tokens": 9261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9261
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

_source line 43 · 2026-05-15T02:12:37.964Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XfB6Bq7TLLxJwFVWAaKpVL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "offset": 60,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "371afe15-16e0-4e15-8359-a01f8f3d9447",
  "isSidechain": false,
  "requestId": "req_011Cb3YYsurcd4uYDV2maupK",
  "type": "assistant",
  "uuid": "d8c19ab5-bd21-4837-b594-7d71010976b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jo6brXEvR5W18Gf2rc2QBe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9261,
      "cache_read_input_tokens": 36455,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 36455,
          "cache_creation_input_tokens": 9261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9261
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

_source line 44 · 2026-05-15T02:12:37.972Z_

<details><summary>↩ Tool result · `toolu_01XfB6Bq7TLLxJwFVWAaKpVL`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8c19ab5-bd21-4837-b594-7d71010976b2",
  "isSidechain": false,
  "promptId": "e0e0e99b-f04a-440d-b03d-7ba309184820",
  "type": "user",
  "uuid": "fda7ef38-4591-4dfc-9787-8e98ebfa0a47",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
      "content": "\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].",
      "numLines": 40,
      "startLine": 60,
      "totalLines": 116
    }
  },
  "sourceToolAssistantUUID": "d8c19ab5-bd21-4837-b594-7d71010976b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T02:13:20.160Z_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the critical issues in method_v1.md:

1. **Line 71**: "This strategy combines embedding distance with structural reachability filtering." — Wrong. The actual mechanism uses BM25, not embedding distance.

2. **Line 77**: The formula uses `sim(E_θ0(q), E_θ0(f))` with `f ∉ R_G(q)` (NOT reachable) — this is wrong in TWO ways:
   - The ranking should use BM25, not embedding similarity
   - The filter should be `f ∈ R_G(q)` (reachable/connected), not `f ∉ R_G(q)` (disconnected)
   
3. **Lines 79 and 85**: Both descriptions claim the method selects negatives that are structurally disconnected and similar in embedding space, but that's backwards—it should be selecting structurally connected candidates ranked by BM25 relevance.

Wait, I'm noticing the user's task mentions modifying `paper_framing.md` in §3.4, but there's also a spawn_worker JSON at the end that seems to reference separate paper_drafts files. Let me clarify what I'm actually being asked to do here—is this one task or two?

Looking more carefully, the spawn_worker appears to be a separate tool invocation for handling the paper_drafts files, while the main request is focused on `paper_framing.md`. I should also check the other files like `method_v1.md` and `figure_design_v1.md` since I found issues there too, and I need to verify the consistency of dataflow-aware strategy mentions throughout the entire document. I'm noticing inconsistencies in figure_design_v1.md and introduction_v2.md too — there are outdated descriptions of the negative sampling strategy that contradict what we established in paper_framing.md, so I should flag those as well. I've identified several inaccuracies in the paper drafts where the descriptions contradict what the code actually does — particularly around how structurally connected files are handled. Since I've already spotted these issues while reviewing, I should go ahead and fix those files too rather than leaving them unresolved.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fda7ef38-4591-4dfc-9787-8e98ebfa0a47",
  "isSidechain": false,
  "requestId": "req_011Cb3YZUWikGTWD2eqvnJrA",
  "type": "assistant",
  "uuid": "5bb6787c-8c4b-4491-adee-54d9d90da304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3FqnwiCYYJ8WUXYqasFSS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 45716,
      "output_tokens": 2211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2211,
          "cache_read_input_tokens": 45716,
          "cache_creation_input_tokens": 1546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1546
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

_source line 46 · 2026-05-15T02:13:29.737Z_

paper_framing.md is fixed. I also found the same incorrect descriptions in the paper_drafts files — the spawn_worker should handle those, but let me flag the specific problems:

**method_v1.md** has the most critical errors:
- Line 71: "combines embedding distance with structural reachability filtering" — should be BM25 + structural connectivity
- Line 77: Formula uses `sim(E_θ0(q), E_θ0(f))` with `f ∉ R_G(q)` — wrong in both ranking (should be BM25) and filter (should be `f ∈ R_G(q)`, connected not disconnected)
- Line 79: "structurally disconnected in the data-flow graph" — should be "structurally connected"
- Line 85: Same "structurally disconnected" error

**introduction_v2.md**:
- Line 13: "filtering such pairs could yield genuinely informative training signal" — implies filtering OUT connected files, but code does the opposite
- Line 17: "filters structurally connected files from the embedding-distance candidate set" — wrong direction

**figure_design_v1.md**:
- Line 49/75/77: Visual description shows "no data-flow edges" for dataflow-aware negatives — should show connected files ranked by BM25

Summary of changes to paper_framing.md:

1. **Formal definition fixed**: `argmax_{x: s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)` → `argmax_{x: reachable_G(x,q) ∧ x ≠ x*} BM25(q, x)`
2. **Added Three-Strategy Difficulty Gradient subsection** clarifying each strategy's mechanism (random = uniform, embedding-distance = cosine similarity, dataflow-aware = structural filtering + BM25 ranking)
3. **Drift-immune note updated** to cover both graph and BM25 ranking as encoder-independent
4. **D041 comment added** at end of file

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bb6787c-8c4b-4491-adee-54d9d90da304",
  "isSidechain": false,
  "requestId": "req_011Cb3YZUWikGTWD2eqvnJrA",
  "type": "assistant",
  "uuid": "7ffd0aa2-8f7a-4491-b26a-d3a83a3a85ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3FqnwiCYYJ8WUXYqasFSS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 45716,
      "output_tokens": 2211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2211,
          "cache_read_input_tokens": 45716,
          "cache_creation_input_tokens": 1546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1546
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
  "leafUuid": "7ffd0aa2-8f7a-4491-b26a-d3a83a3a85ca",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix dataflow-aware strategy description in paper",
  "sessionId": "cf51224d-fd16-44c7-b53d-2f35ec8def65"
}
```

---
