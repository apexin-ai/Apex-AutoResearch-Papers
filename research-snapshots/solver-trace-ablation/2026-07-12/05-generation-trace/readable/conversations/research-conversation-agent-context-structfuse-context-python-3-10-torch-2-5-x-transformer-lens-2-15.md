# Research conversation: <agent_context> 项目：structfuse-context。依赖基线：Python 3.10 + torch 2.5.x + transformer-lens 2.15.0。ACDC 用 Auto-Circuit 替代原始库

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/3a9d1438-71e8-4ba9-9cef-ef13b6ac4891.jsonl`
- **Structured JSON:** [`5cfbb2f20ff008f391b8.json`](../../sessions/5c/5cfbb2f20ff008f391b8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T10:20:03.404Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T10:20:03.404Z",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "content": "&lt;agent_context>\n项目：structfuse-context。依赖基线：Python 3.10 + torch 2.5.x + transformer-lens 2.15.0。ACDC 用 Auto-Circuit 替代原始库。已有 API 调研确认 EAP-IG 和 Edge Pruning 可用于大模型。\n&lt;/agent_context>\n\n&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: cqa1-21977\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：大模型第三方法可行性评估\n\n### 背景\nStructFuse 项目需要在大模型（Qwen-2.5 0.5B / Gemma-2 2B / Llama-3.1 8B）上跑 K=3 edge-level circuit discovery 方法进行跨方法共识投票。\n\n目前确定可用的两个方法：\n1. **EAP-IG**（gradient attribution）— 可扩展到大模型（MIB benchmark 已验证）\n2. **Edge Pruning**（mask optimization）— 原论文有 CodeLlama 实验，可扩展\n\n**ACDC** 在大模型上不可行（GPT-2 Small 都要 ~10h，大模型预估 42-127h/task）。\n**AtP*** 无可用的 edge-level 实现（官方未开源，社区版仅 node-level）。\n\n仅剩 K=2 会导致平凡投票（严重削弱论文贡献），需要找到第三个 edge-level 方法。\n\n### 你需要评估的三条路径\n\n#### (a) AtP* edge-level 自行实现\nAtP* 论文（Kramár et al. 2024, arXiv:2403.00745）的两个核心修改：\n1. **QK-Fix**: 固定 query-key 交互的梯度——对 attention 节点显式线性化 attention probabilities（而非 softmax inputs）\n2. **GradDrop**: 将 residual skip 路径上的 gradient 置零，消除 path-cancellation\n\n评估要点：\n- 在 EAP-IG / TransformerLens 框架上实现这两个修改，改动量多大？\n- 能否在 ≤1 天内完成可靠实现？\n- 需要修改 EAP-IG 的哪些部分？（hook 机制？gradient 计算？）\n- 实现后是否仍属于独立的算法族（vs EAP-IG）？AtP* 的 QK-Fix + GradDrop 是否足以让它成为\"gradient 族的不同子类\"？\n- 算法族分类：gradient（但改进了 linearization 策略，与 EAP-IG 的 IG 积分不同）\n\n#### (b) PAHQ 加速 ACDC\nPAHQ（arXiv:2510.23264）用 mixed-precision 加速 ACDC。\n\n评估要点：\n- 搜索 PAHQ 的代码库（GitHub/arXiv），确认是否开源\n- 确认 PAHQ 是否支持 TransformerLens 模型（还是用其他框架）\n- 能否将 Qwen-2.5 0.5B 上 ACDC 从 ~42-127h 降到 ≤10h/task？\n- 如果 PAHQ 不可用，其他加速 ACDC 的方法？\n- 算法族分类：causal intervention（加速版 ACDC 仍属同一族）\n\n#### (c) MIB 其他 edge-level 方法\nMIB benchmark（arXiv:2504.13151，GitHub: hannamw/MIB-circuit-track）支持多种 circuit discovery 方法。\n\n评估要点：\n- 列出 MIB circuit track 支持的**所有** circuit discovery 方法\n- 逐一标注：\n  - 算法族（gradient / mask optimization / causal intervention / other）\n  - 是否 edge-level（不是 node-level）\n  - 对 0.5B-8B 模型的可扩展性（时间复杂度估计）\n- 重点关注：\n  - **Information Flow Routes (IFR)** — 什么算法族？edge-level？可扩展？\n  - **Uniform Gradient Sampling (UGS)** — 什么算法族？edge-level？可扩展？\n  - **EAP with Optimal Ablations** — 与标准 EAP-IG 有何本质区别？算法族是否不同？\n- 是否存在非 gradient、非 mask-optimization 的 edge-level 方法能扩展到大模型？\n\n### 搜索指引\n1. 搜索 GitHub 上 PAHQ 相关仓库\n2. 读 MIB-circuit-track 的 README 和代码，确认支持的方法列表\n3. 读 PAHQ 论文摘要确认其方法和加速比\n4. 读 IFR / UGS 的原始论文摘要了解算法原理\n5. 确认每个方法是否有 edge-level 支持（不只是 node-level）\n\n### 产出格式\n写一份评估报告到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/LARGE_MODEL_THIRD_METHOD.md`\n\n格式：\n```markdown\n# 大模型第三方法可行性评估\n\n## 路径 (a): AtP* 自行实现\n- **可行性**: 是/否\n- **预估工作量**: X 天\n- **算法族**: ...\n- **具体分析**:（5-10行）\n\n## 路径 (b): PAHQ 加速 ACDC\n- **可行性**: 是/否\n- **预估工作量**: X 天\n- **算法族**: ...\n- **具体分析**:（5-10行）\n\n## 路径 (c): MIB 其他方法\n### 方法列表\n| 方法 | 算法族 | Edge-level? | 大模型可扩展? | 备注 |\n|------|--------|------------|-------------|------|\n| ... | ... | ... | ... | ... |\n\n### 重点评估\n- IFR: ...\n- UGS: ...\n- EAP-OA: ...\n\n## 推荐\n- **首选**: ...\n- **备选**: ...\n- **理由**: ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-12T10:20:03.408Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T10:20:03.408Z",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-12T10:20:03.446Z_

&lt;agent_context>
项目：structfuse-context。依赖基线：Python 3.10 + torch 2.5.x + transformer-lens 2.15.0。ACDC 用 Auto-Circuit 替代原始库。已有 API 调研确认 EAP-IG 和 Edge Pruning 可用于大模型。
&lt;/agent_context>

&lt;project_context>
# 项目: structfuse-context

## 运行环境
- 服务器名: cqa1-21977
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：大模型第三方法可行性评估

### 背景
StructFuse 项目需要在大模型（Qwen-2.5 0.5B / Gemma-2 2B / Llama-3.1 8B）上跑 K=3 edge-level circuit discovery 方法进行跨方法共识投票。

目前确定可用的两个方法：
1. **EAP-IG**（gradient attribution）— 可扩展到大模型（MIB benchmark 已验证）
2. **Edge Pruning**（mask optimization）— 原论文有 CodeLlama 实验，可扩展

**ACDC** 在大模型上不可行（GPT-2 Small 都要 ~10h，大模型预估 42-127h/task）。
**AtP*** 无可用的 edge-level 实现（官方未开源，社区版仅 node-level）。

仅剩 K=2 会导致平凡投票（严重削弱论文贡献），需要找到第三个 edge-level 方法。

### 你需要评估的三条路径

#### (a) AtP* edge-level 自行实现
AtP* 论文（Kramár et al. 2024, arXiv:2403.00745）的两个核心修改：
1. **QK-Fix**: 固定 query-key 交互的梯度——对 attention 节点显式线性化 attention probabilities（而非 softmax inputs）
2. **GradDrop**: 将 residual skip 路径上的 gradient 置零，消除 path-cancellation

评估要点：
- 在 EAP-IG / TransformerLens 框架上实现这两个修改，改动量多大？
- 能否在 ≤1 天内完成可靠实现？
- 需要修改 EAP-IG 的哪些部分？（hook 机制？gradient 计算？）
- 实现后是否仍属于独立的算法族（vs EAP-IG）？AtP* 的 QK-Fix + GradDrop 是否足以让它成为"gradient 族的不同子类"？
- 算法族分类：gradient（但改进了 linearization 策略，与 EAP-IG 的 IG 积分不同）

#### (b) PAHQ 加速 ACDC
PAHQ（arXiv:2510.23264）用 mixed-precision 加速 ACDC。

评估要点：
- 搜索 PAHQ 的代码库（GitHub/arXiv），确认是否开源
- 确认 PAHQ 是否支持 TransformerLens 模型（还是用其他框架）
- 能否将 Qwen-2.5 0.5B 上 ACDC 从 ~42-127h 降到 ≤10h/task？
- 如果 PAHQ 不可用，其他加速 ACDC 的方法？
- 算法族分类：causal intervention（加速版 ACDC 仍属同一族）

#### (c) MIB 其他 edge-level 方法
MIB benchmark（arXiv:2504.13151，GitHub: hannamw/MIB-circuit-track）支持多种 circuit discovery 方法。

评估要点：
- 列出 MIB circuit track 支持的**所有** circuit discovery 方法
- 逐一标注：
  - 算法族（gradient / mask optimization / causal intervention / other）
  - 是否 edge-level（不是 node-level）
  - 对 0.5B-8B 模型的可扩展性（时间复杂度估计）
- 重点关注：
  - **Information Flow Routes (IFR)** — 什么算法族？edge-level？可扩展？
  - **Uniform Gradient Sampling (UGS)** — 什么算法族？edge-level？可扩展？
  - **EAP with Optimal Ablations** — 与标准 EAP-IG 有何本质区别？算法族是否不同？
- 是否存在非 gradient、非 mask-optimization 的 edge-level 方法能扩展到大模型？

### 搜索指引
1. 搜索 GitHub 上 PAHQ 相关仓库
2. 读 MIB-circuit-track 的 README 和代码，确认支持的方法列表
3. 读 PAHQ 论文摘要确认其方法和加速比
4. 读 IFR / UGS 的原始论文摘要了解算法原理
5. 确认每个方法是否有 edge-level 支持（不只是 node-level）

### 产出格式
写一份评估报告到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/LARGE_MODEL_THIRD_METHOD.md`

格式：
```markdown
# 大模型第三方法可行性评估

## 路径 (a): AtP* 自行实现
- **可行性**: 是/否
- **预估工作量**: X 天
- **算法族**: ...
- **具体分析**:（5-10行）

## 路径 (b): PAHQ 加速 ACDC
- **可行性**: 是/否
- **预估工作量**: X 天
- **算法族**: ...
- **具体分析**:（5-10行）

## 路径 (c): MIB 其他方法
### 方法列表
| 方法 | 算法族 | Edge-level? | 大模型可扩展? | 备注 |
|------|--------|------------|-------------|------|
| ... | ... | ... | ... | ... |

### 重点评估
- IFR: ...
- UGS: ...
- EAP-OA: ...

## 推荐
- **首选**: ...
- **备选**: ...
- **理由**: ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "type": "user",
  "uuid": "b3f006fd-ff4c-489c-a912-3d298d38f0ba",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T10:20:03.445Z_

```json
{
  "parentUuid": "b3f006fd-ff4c-489c-a912-3d298d38f0ba",
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
  "uuid": "cc91d033-3755-47b0-b4eb-46de2a95e4e8",
  "timestamp": "2026-05-12T10:20:03.445Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T10:20:03.445Z_

```json
{
  "parentUuid": "cc91d033-3755-47b0-b4eb-46de2a95e4e8",
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
  "uuid": "bd062ad9-9777-4077-a318-1034fae55c65",
  "timestamp": "2026-05-12T10:20:03.445Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-12T10:20:03.445Z_

```json
{
  "parentUuid": "bd062ad9-9777-4077-a318-1034fae55c65",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "32c3b652-b428-46ba-b473-dbb2b9f7677a",
  "timestamp": "2026-05-12T10:20:03.445Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
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
  "aiTitle": "Evaluate third method for large model circuit discovery",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891"
}
```

---

### Assistant

_source line 8 · 2026-05-12T10:20:13.055Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate three potential paths for finding a third edge-level circuit discovery method for large models. Let me break this into parallel research tasks:

1. Research AtP* paper and implementation feasibility
2. Research PAHQ paper and code availability
3. Research MIB benchmark methods

Let me launch parallel agents to do this research efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32c3b652-b428-46ba-b473-dbb2b9f7677a",
  "isSidechain": false,
  "requestId": "req_011CaxWJXzA33AnLPXanjGvf",
  "type": "assistant",
  "uuid": "6553807c-7e2f-4090-b23d-3fa28f338c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEGHnPnP3YMknf18sBPYqW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12509,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1207,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12509
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-12T10:20:13.647Z_

I'll research all three paths in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6553807c-7e2f-4090-b23d-3fa28f338c1a",
  "isSidechain": false,
  "requestId": "req_011CaxWJXzA33AnLPXanjGvf",
  "type": "assistant",
  "uuid": "4014be69-9d60-487e-a337-7bfa6f955cf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEGHnPnP3YMknf18sBPYqW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12509,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1207,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12509
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-12T10:20:21.872Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GecBs4pGJL8oUEVAN3u31t`</summary>

```json
{
  "description": "Research AtP* paper feasibility",
  "subagent_type": "general-purpose",
  "prompt": "Research the AtP* (Attribution Patching with QK-Fix and GradDrop) paper by Kramár et al. 2024 (arXiv:2403.00745).\n\nI need to understand:\n1. What exactly are the QK-Fix and GradDrop modifications? How do they work mechanistically?\n2. Is there any open-source implementation of AtP* (edge-level)? Check GitHub for repos.\n3. How would one implement AtP* on top of EAP-IG / TransformerLens? What hooks/gradient modifications are needed?\n4. Is AtP* genuinely a different algorithm from EAP-IG? (EAP-IG uses integrated gradients; AtP* uses single-point gradients with QK-Fix linearization + GradDrop). Are they in the same \"gradient attribution\" family but different enough sub-methods?\n5. Search for \"attribution patching\" \"edge\" implementation on GitHub.\n6. Search for \"atp star\" or \"atp*\" circuit discovery implementation.\n\nUse WebSearch and WebFetch to find the paper, any code repos, and implementation details. Report your findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4014be69-9d60-487e-a337-7bfa6f955cf0",
  "isSidechain": false,
  "requestId": "req_011CaxWJXzA33AnLPXanjGvf",
  "type": "assistant",
  "uuid": "496efde6-8feb-470b-bdfd-921405cd0df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEGHnPnP3YMknf18sBPYqW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12509,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1207,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12509
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T10:20:26.292Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PFRMJwYsJ8M8ALXAYD4ppV`</summary>

```json
{
  "description": "Research PAHQ paper and code",
  "subagent_type": "general-purpose",
  "prompt": "Research PAHQ (arXiv:2510.23264) which claims to accelerate ACDC circuit discovery using mixed-precision.\n\nI need to understand:\n1. Does PAHQ have an open-source code repository? Search GitHub for PAHQ circuit discovery repos.\n2. What speedup does PAHQ claim over standard ACDC?\n3. Does PAHQ work with TransformerLens or its own framework?\n4. Could it bring ACDC runtime on Qwen-2.5 0.5B from ~42-127h down to ≤10h per task?\n5. Is PAHQ edge-level or node-level?\n6. What is the algorithm family - is it still \"causal intervention\" like ACDC?\n\nAlso search for any other methods that accelerate ACDC (e.g., SP-ACDC, hierarchical ACDC, etc.).\n\nUse WebSearch and WebFetch to find the paper abstract, any code repos, and speedup claims. Report concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "496efde6-8feb-470b-bdfd-921405cd0df8",
  "isSidechain": false,
  "requestId": "req_011CaxWJXzA33AnLPXanjGvf",
  "type": "assistant",
  "uuid": "48578bde-8cad-40d4-95e6-0057daa789f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEGHnPnP3YMknf18sBPYqW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12509,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1207,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12509
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T10:20:32.955Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Mc6jCuco2hcvyfJLCfkEYA`</summary>

```json
{
  "description": "Research MIB benchmark methods",
  "subagent_type": "general-purpose",
  "prompt": "Research the MIB (Mechanistic Interpretability Benchmark) circuit track (arXiv:2504.13151, GitHub: hannamw/MIB-circuit-track).\n\nI need a comprehensive list of ALL circuit discovery methods supported by MIB circuit track. For each method:\n1. Algorithm family (gradient attribution / mask optimization / causal intervention / other)\n2. Is it edge-level (not just node-level)?\n3. Scalability to 0.5B-8B models (time complexity)\n\nPay special attention to:\n- **Information Flow Routes (IFR)** — what algorithm family? edge-level? scalable?\n- **Uniform Gradient Sampling (UGS)** — what algorithm family? edge-level? scalable?  \n- **EAP with Optimal Ablations (EAP-OA)** — how is it different from standard EAP-IG? Different algorithm family?\n- Any other methods that are NOT gradient-based and NOT mask-optimization but ARE edge-level\n\nSteps:\n1. WebSearch for \"MIB-circuit-track\" GitHub repo\n2. WebFetch the GitHub repo README to get the full method list\n3. Look at the code structure to see what methods are implemented\n4. WebSearch for IFR (Information Flow Routes) circuit discovery paper\n5. WebSearch for UGS (Uniform Gradient Sampling) circuit discovery paper\n6. WebSearch for \"EAP optimal ablation\" circuit discovery\n\nReport all findings concisely with a table of methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48578bde-8cad-40d4-95e6-0057daa789f6",
  "isSidechain": false,
  "requestId": "req_011CaxWJXzA33AnLPXanjGvf",
  "type": "assistant",
  "uuid": "52e869f6-d419-4e09-bcde-d8146bb5e6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEGHnPnP3YMknf18sBPYqW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12509,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1207,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12509
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T10:22:28.739Z_

<details><summary>↩ Tool result · `toolu_01PFRMJwYsJ8M8ALXAYD4ppV`</summary>

```text
Now I have enough information. Here is my report.

---

## PAHQ (arXiv:2510.23264) - Research Summary

### 1. Open-source code

Yes. GitHub repo: [https://github.com/626619403/PAHQ](https://github.com/626619403/PAHQ). It contains working code with `PAHQ_ACDC/` directory, a modified `transformer_lens/` copy, `run_experiments.sh`, and `requirements.txt`. It is a modification of the original ACDC codebase, not a clean fork.

### 2. Speedup claims

- **Up to 80% runtime reduction** (5x speedup): on GPT-2 small IOI task, standard ACDC took 99:18 min, PAHQ reduced to 20:36 min.
- **~30% memory reduction**: 6.23 GB down to 4.24 GB.
- The speedup comes from mixed-precision quantization of each forward pass, not from changing ACDC's algorithmic structure.

### 3. TransformerLens integration

Yes, PAHQ builds on top of TransformerLens. The repo includes a **modified copy** of TransformerLens that must replace the original installation. This is a concern - it's not a plugin but a fork of the library.

### 4. Can it bring Qwen-2.5 0.5B ACDC from ~42-127h to ≤10h?

**Almost certainly not.** Critical limitations:

- PAHQ was only tested on GPT-2 small (124M params, 12 layers, 12 heads). The largest model tested was GPT-2-XL (1.5B) but **only for KL divergence metrics, not ACDC runtime** - the paper explicitly states "The original ACDC method becomes computationally prohibitive on larger models... we are unable to provide ACDC results on larger models."
- The repo only supports `gpt2`, `attn-only-4l`, and `redwood_attn_2l`.
- PAHQ's 5x speedup on GPT-2 small (99 min -> 20 min) addresses a ~1.5h baseline. Your baseline is 42-127h on Qwen-2.5 0.5B. Even a 5x speedup gives 8-25h, not ≤10h for the worst case.
- PAHQ uses a **modified TransformerLens fork** - adapting it to Qwen architecture would require significant engineering.
- The quantization scheme (FP32 for critical heads, FP8_E4M3 for others, bf16 for non-attention) is GPU-dependent (tested on H20 96GB with FP8 support).

### 5. Edge-level or node-level?

**Edge-level.** The paper states: "automated circuit discovery algorithms typically evaluate only one edge at a time." Each evaluation maintains high precision for the source node's activations of a specific edge e=(u->v).

### 6. Algorithm family

**Still causal intervention / activation patching.** PAHQ does not change ACDC's algorithm. It accelerates each individual patching forward pass by quantizing non-critical components to lower precision. The core loop remains: iterate over edges, patch activations, measure KL divergence, prune.

---

## Other ACDC Acceleration Methods

### EAP / Attribution Patching (arXiv:2310.10348)
- Replaces ACDC's O(|E|) forward passes with **2 forward passes + 1 backward pass** using first-order Taylor approximation.
- Dramatically faster but **less faithful** - it's an approximation, not exact causal intervention.
- Edge-level. Works with TransformerLens.

### CD-T / Efficient Automated Circuit Discovery (arXiv:2407.00886, ICLR 2025)
- Uses Contextual Decomposition for Transformers.
- Claims to reduce runtime **from hours to seconds**.
- Node-level (attention head granularity). 97% ROC AUC on standard benchmarks.
- Different algorithmic family - not activation patching but decomposition-based.

### IBCircuit (arXiv:2602.22581, ICML 2025)
- Information Bottleneck-based optimization framework.
- Injects learnable Gaussian noise; optimizes to preserve informative components.
- Both node and edge level. End-to-end optimization, no need for hand-designed corrupted activations.
- More recent (Feb 2026), potentially more scalable.

### EAP-GP (arXiv:2502.06852)
- Mitigates saturation effects in gradient-based circuit identification (improving EAP-IG).

---

## Bottom Line for Your Use Case

For Qwen-2.5 0.5B circuit discovery in ≤10h per task, PAHQ alone is insufficient. The most promising directions are:

1. **EAP/Attribution Patching**: orders of magnitude faster than ACDC, but approximate. Could serve as a first-pass filter followed by targeted ACDC on a reduced graph.
2. **CD-T**: claims hours-to-seconds reduction, but node-level only.
3. **IBCircuit**: optimization-based, potentially more scalable to larger models, but very new.
4. **Hybrid approach**: Use EAP to identify candidate edges, then run ACDC (possibly PAHQ-accelerated) only on the top-k edges. This is the most realistic path to ≤10h.

PAHQ's 5x speedup is real but modest relative to your target, and the engineering cost of porting its modified TransformerLens fork to Qwen is non-trivial.

agentId: a97febb1e84474d24 (use SendMessage with to: 'a97febb1e84474d24' to continue this agent)
&lt;usage>total_tokens: 29008
tool_uses: 16
duration_ms: 122443&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48578bde-8cad-40d4-95e6-0057daa789f6",
  "isSidechain": false,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "type": "user",
  "uuid": "29341449-43e4-4b3c-883e-715fbcc27a7f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research PAHQ (arXiv:2510.23264) which claims to accelerate ACDC circuit discovery using mixed-precision.\n\nI need to understand:\n1. Does PAHQ have an open-source code repository? Search GitHub for PAHQ circuit discovery repos.\n2. What speedup does PAHQ claim over standard ACDC?\n3. Does PAHQ work with TransformerLens or its own framework?\n4. Could it bring ACDC runtime on Qwen-2.5 0.5B from ~42-127h down to ≤10h per task?\n5. Is PAHQ edge-level or node-level?\n6. What is the algorithm family - is it still \"causal intervention\" like ACDC?\n\nAlso search for any other methods that accelerate ACDC (e.g., SP-ACDC, hierarchical ACDC, etc.).\n\nUse WebSearch and WebFetch to find the paper abstract, any code repos, and speedup claims. Report concisely.",
    "agentId": "a97febb1e84474d24",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information. Here is my report.\n\n---\n\n## PAHQ (arXiv:2510.23264) - Research Summary\n\n### 1. Open-source code\n\nYes. GitHub repo: [https://github.com/626619403/PAHQ](https://github.com/626619403/PAHQ). It contains working code with `PAHQ_ACDC/` directory, a modified `transformer_lens/` copy, `run_experiments.sh`, and `requirements.txt`. It is a modification of the original ACDC codebase, not a clean fork.\n\n### 2. Speedup claims\n\n- **Up to 80% runtime reduction** (5x speedup): on GPT-2 small IOI task, standard ACDC took 99:18 min, PAHQ reduced to 20:36 min.\n- **~30% memory reduction**: 6.23 GB down to 4.24 GB.\n- The speedup comes from mixed-precision quantization of each forward pass, not from changing ACDC's algorithmic structure.\n\n### 3. TransformerLens integration\n\nYes, PAHQ builds on top of TransformerLens. The repo includes a **modified copy** of TransformerLens that must replace the original installation. This is a concern - it's not a plugin but a fork of the library.\n\n### 4. Can it bring Qwen-2.5 0.5B ACDC from ~42-127h to ≤10h?\n\n**Almost certainly not.** Critical limitations:\n\n- PAHQ was only tested on GPT-2 small (124M params, 12 layers, 12 heads). The largest model tested was GPT-2-XL (1.5B) but **only for KL divergence metrics, not ACDC runtime** - the paper explicitly states \"The original ACDC method becomes computationally prohibitive on larger models... we are unable to provide ACDC results on larger models.\"\n- The repo only supports `gpt2`, `attn-only-4l`, and `redwood_attn_2l`.\n- PAHQ's 5x speedup on GPT-2 small (99 min -> 20 min) addresses a ~1.5h baseline. Your baseline is 42-127h on Qwen-2.5 0.5B. Even a 5x speedup gives 8-25h, not ≤10h for the worst case.\n- PAHQ uses a **modified TransformerLens fork** - adapting it to Qwen architecture would require significant engineering.\n- The quantization scheme (FP32 for critical heads, FP8_E4M3 for others, bf16 for non-attention) is GPU-dependent (tested on H20 96GB with FP8 support).\n\n### 5. Edge-level or node-level?\n\n**Edge-level.** The paper states: \"automated circuit discovery algorithms typically evaluate only one edge at a time.\" Each evaluation maintains high precision for the source node's activations of a specific edge e=(u->v).\n\n### 6. Algorithm family\n\n**Still causal intervention / activation patching.** PAHQ does not change ACDC's algorithm. It accelerates each individual patching forward pass by quantizing non-critical components to lower precision. The core loop remains: iterate over edges, patch activations, measure KL divergence, prune.\n\n---\n\n## Other ACDC Acceleration Methods\n\n### EAP / Attribution Patching (arXiv:2310.10348)\n- Replaces ACDC's O(|E|) forward passes with **2 forward passes + 1 backward pass** using first-order Taylor approximation.\n- Dramatically faster but **less faithful** - it's an approximation, not exact causal intervention.\n- Edge-level. Works with TransformerLens.\n\n### CD-T / Efficient Automated Circuit Discovery (arXiv:2407.00886, ICLR 2025)\n- Uses Contextual Decomposition for Transformers.\n- Claims to reduce runtime **from hours to seconds**.\n- Node-level (attention head granularity). 97% ROC AUC on standard benchmarks.\n- Different algorithmic family - not activation patching but decomposition-based.\n\n### IBCircuit (arXiv:2602.22581, ICML 2025)\n- Information Bottleneck-based optimization framework.\n- Injects learnable Gaussian noise; optimizes to preserve informative components.\n- Both node and edge level. End-to-end optimization, no need for hand-designed corrupted activations.\n- More recent (Feb 2026), potentially more scalable.\n\n### EAP-GP (arXiv:2502.06852)\n- Mitigates saturation effects in gradient-based circuit identification (improving EAP-IG).\n\n---\n\n## Bottom Line for Your Use Case\n\nFor Qwen-2.5 0.5B circuit discovery in ≤10h per task, PAHQ alone is insufficient. The most promising directions are:\n\n1. **EAP/Attribution Patching**: orders of magnitude faster than ACDC, but approximate. Could serve as a first-pass filter followed by targeted ACDC on a reduced graph.\n2. **CD-T**: claims hours-to-seconds reduction, but node-level only.\n3. **IBCircuit**: optimization-based, potentially more scalable to larger models, but very new.\n4. **Hybrid approach**: Use EAP to identify candidate edges, then run ACDC (possibly PAHQ-accelerated) only on the top-k edges. This is the most realistic path to ≤10h.\n\nPAHQ's 5x speedup is real but modest relative to your target, and the engineering cost of porting its modified TransformerLens fork to Qwen is non-trivial."
      }
    ],
    "totalDurationMs": 122443,
    "totalTokens": 29008,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1839,
      "cache_read_input_tokens": 25798,
      "output_tokens": 1370,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1370,
          "cache_read_input_tokens": 25798,
          "cache_creation_input_tokens": 1839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1839,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "48578bde-8cad-40d4-95e6-0057daa789f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
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
  "leafUuid": "29341449-43e4-4b3c-883e-715fbcc27a7f",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate third method for large model circuit discovery",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891"
}
```

---

### Tool result

_source line 16 · 2026-05-12T10:23:03.692Z_

<details><summary>↩ Tool result · `toolu_01GecBs4pGJL8oUEVAN3u31t`</summary>

````text
Now I have comprehensive information. Let me compile the findings.

Here are my findings on AtP* (Kramár et al. 2024, arXiv:2403.00745):

---

## 1. QK-Fix and GradDrop: Mechanistic Details

**Two failure modes identified in standard AtP:**

**Failure Mode 1 — Attention Saturation.** Standard AtP uses a first-order Taylor approximation (gradient × activation difference) to estimate each component's causal contribution. For attention heads, this means taking gradients through the softmax. When attention weights are saturated (near 0 or 1), the softmax gradient is nearly flat, making the linear approximation very poor. The gradient says "changing this input barely changes the output," even though a large enough perturbation would move the softmax out of its saturated region.

**QK-Fix solution:** Instead of approximating through the softmax with gradients, QK-Fix *explicitly recomputes* the attention probabilities with corrupted queries/keys while keeping the rest clean. Concretely:

- For **query contributions**: compute `attn_patch = softmax(Q_corrupted · K_clean^T)` and `attn_clean = softmax(Q_clean · K_clean^T)`, then multiply the difference `(attn_patch - attn_clean)` by the downstream gradient `∂L/∂attn|_clean`. This replaces the gradient-through-softmax approximation with an exact computation of the first nonlinearity, then uses gradients only for the remaining (better-behaved) downstream computation.
- For **key contributions**: analogous but more complex — requires measuring how each key's corruption changes attention weights across all queries. Naive implementation is O(T³); an efficient O(T²) variant exists.

The key insight: compute the first nonlinearity (softmax) exactly, then take linear approximations only downstream where they work better.

**Failure Mode 2 — Cancellation.** A node's total effect is the sum of its direct and indirect effects. When these nearly cancel (direct ≈ −indirect), small multiplicative approximation errors can make the estimated total effect orders of magnitude wrong, causing false negatives.

**GradDrop solution:** Run L additional backward passes (one per layer), each time zeroing the gradient at one layer's residual stream output before backpropagating. This isolates contributions that don't route through the dropped layer. The final GradDrop score aggregates absolute values across all these passes:

```
ĉ_GD(n) = (1/(L-1)) · Σ_ℓ |ℐ̂^(AtP+GD_ℓ)(n)|
```

By taking absolute values of each partial estimate and averaging, cancellation between direct and indirect paths is broken. Cost: L extra backward passes (optimizable to (L+1)/2).

**AtP* = AtP + QK-Fix + GradDrop**, costing less than 2× a standard forward pass per prompt pair.

---

## 2. Open-Source Implementations

**Dedicated AtP* repos:**

- **[koayon/atp_star](https://github.com/koayon/atp_star)** — Unofficial PyTorch + NNsight implementation. Implements AtP, AtP+QK-Fix, and full AtP* (with GradDrop). **Node-level only** (not edge-level). Uses NNsight's `model.trace()` for interventions. QK-Fix is implemented by patching Q or K in the QKV tensor and re-running forward passes. GradDrop is implemented by calling `.grad.zero_()` on attention residual dropout inputs and MLP projection outputs at specific layers before backpropagation.

**Edge-level attribution patching repos (no AtP*):**

- **[Aaquib111/edge-attribution-patching](https://github.com/Aaquib111/edge-attribution-patching)** — EAP implementation on TransformerLens. NeurIPS 2024 ATTRIB paper. Edge-level but does **not** include AtP* modifications.
- **[hannamw/eap-ig](https://github.com/hannamw/eap-ig)** — EAP-IG (integrated gradients variant) on TransformerLens. Supports edge-level analysis. Does **not** include AtP*.
- **[UFO-101/auto-circuit](https://github.com/UFO-101/auto-circuit)** — AutoCircuit library. Implements ACDC, EAP, mask gradient, subnetwork probing, etc. Does **not** include AtP* or EAP-IG.

**Bottom line: No existing open-source implementation combines AtP* (QK-Fix + GradDrop) with edge-level attribution.**

---

## 3. Implementing AtP* on Top of EAP-IG / TransformerLens

To add AtP* modifications to an edge-level EAP framework on TransformerLens, you would need:

**For QK-Fix:**
1. Hook into attention heads at the QKV computation level (e.g., `hook_q`, `hook_k` in TransformerLens).
2. Instead of letting gradients flow through `softmax(Q·K^T/√d)`, compute two forward passes: one with corrupted Q (or K) patched in and one clean, both through the actual softmax.
3. Compute `Δattn = softmax(Q_corrupt · K_clean^T/√d) − softmax(Q_clean · K_clean^T/√d)`.
4. Multiply by the gradient of the loss w.r.t. the attention pattern (`hook_attn_scores` or `hook_pattern`).
5. This replaces the standard gradient term for Q/K edges with the explicitly-linearized version.

**For GradDrop:**
1. Register backward hooks on each layer's residual stream output (e.g., `hook_resid_post` at layer ℓ).
2. Run L backward passes, each time zeroing the gradient at a different layer's residual output using a backward hook that returns zeros.
3. Collect the edge attribution scores from each pass, take absolute values, and average.

**Key hooks needed in TransformerLens:**
- `blocks[i].attn.hook_q`, `blocks[i].attn.hook_k` — for QK-Fix forward pass interventions
- `blocks[i].attn.hook_pattern` or `blocks[i].attn.hook_attn_scores` — for reading attention weights and their gradients
- `blocks[i].hook_resid_post` — for GradDrop gradient zeroing (backward hooks)
- Standard EAP edge hooks for computing activation differences × gradients at each edge

The main engineering challenge is that QK-Fix requires additional forward passes (one per attention head being scored, or batched), significantly increasing cost compared to EAP's single-forward-backward paradigm.

---

## 4. Is AtP* Genuinely Different from EAP-IG?

Yes, they are meaningfully different algorithms within the same "gradient-based attribution" family:

| Aspect | EAP-IG | AtP* |
|--------|--------|------|
| **Core technique** | Integrated gradients: average gradients over m interpolation steps between clean and corrupted | Single-point gradient with two targeted fixes |
| **Saturation fix** | Averages over the path, hoping some points escape saturation | Explicitly computes softmax (QK-Fix), bypassing the approximation entirely |
| **Cancellation fix** | None specific | GradDrop: isolates paths by zeroing gradients layer-by-layer |
| **Scope in paper** | Edge-level | Node-level (paper), edge extension discussed in appendix |
| **Cost** | 2m forward + m backward passes | ~2 forward + (L+1) backward passes |
| **Framework** | Applies uniformly to all components | Attention-specific fix (QK-Fix) + general fix (GradDrop) |

**Key distinction:** EAP-IG's integrated gradients can still fail if the entire interpolation path dwells in a saturated softmax region (the straight line from clean to corrupt may stay in a flat zone). AtP*'s QK-Fix avoids this entirely by computing the softmax exactly rather than approximating it. However, EAP-IG naturally handles edges, while AtP* was designed for nodes and requires nontrivial adaptation for edge-level use.

A recent paper, **EAP-GP** (arXiv:2502.06852), proposes a third approach: dynamically adjusting the integration path to avoid saturated regions, achieving up to 17.7% improvement over EAP-IG on circuit faithfulness metrics.

---

## 5-6. GitHub Search Summary

Repositories found:

| Repository | Method | Level | Framework | AtP*? |
|-----------|--------|-------|-----------|-------|
| [koayon/atp_star](https://github.com/koayon/atp_star) | AtP* | Node | NNsight | Yes |
| [Aaquib111/edge-attribution-patching](https://github.com/Aaquib111/edge-attribution-patching) | EAP | Edge | TransformerLens | No |
| [hannamw/eap-ig](https://github.com/hannamw/eap-ig) | EAP-IG | Edge | TransformerLens | No |
| [UFO-101/auto-circuit](https://github.com/UFO-101/auto-circuit) | EAP, ACDC, others | Edge | Custom + TL utils | No |
| [rusheb/arena-hackathon-attribution-patching](https://github.com/rusheb/arena-hackathon-attribution-patching) | AtP variant | Edge | TransformerLens | No |
| [technion-cs-nlp/PEAP](https://github.com/technion-cs-nlp/PEAP) | Position-aware EAP | Edge | TransformerLens | No |

**No repository implements edge-level AtP*.** The only AtP* implementation (koayon/atp_star) is node-level and uses NNsight rather than TransformerLens. An edge-level AtP* implementation would need to be built from scratch, likely by adding QK-Fix and GradDrop modifications to an existing edge-level EAP framework like `hannamw/eap-ig` or `UFO-101/auto-circuit`.

agentId: ae30cbc46732c68a6 (use SendMessage with to: 'ae30cbc46732c68a6' to continue this agent)
&lt;usage>total_tokens: 30821
tool_uses: 18
duration_ms: 161814&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "496efde6-8feb-470b-bdfd-921405cd0df8",
  "isSidechain": false,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "type": "user",
  "uuid": "806e39b6-7986-484c-8c89-850d5cac5afa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the AtP* (Attribution Patching with QK-Fix and GradDrop) paper by Kramár et al. 2024 (arXiv:2403.00745).\n\nI need to understand:\n1. What exactly are the QK-Fix and GradDrop modifications? How do they work mechanistically?\n2. Is there any open-source implementation of AtP* (edge-level)? Check GitHub for repos.\n3. How would one implement AtP* on top of EAP-IG / TransformerLens? What hooks/gradient modifications are needed?\n4. Is AtP* genuinely a different algorithm from EAP-IG? (EAP-IG uses integrated gradients; AtP* uses single-point gradients with QK-Fix linearization + GradDrop). Are they in the same \"gradient attribution\" family but different enough sub-methods?\n5. Search for \"attribution patching\" \"edge\" implementation on GitHub.\n6. Search for \"atp star\" or \"atp*\" circuit discovery implementation.\n\nUse WebSearch and WebFetch to find the paper, any code repos, and implementation details. Report your findings concisely.",
    "agentId": "ae30cbc46732c68a6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the findings.\n\nHere are my findings on AtP* (Kramár et al. 2024, arXiv:2403.00745):\n\n---\n\n## 1. QK-Fix and GradDrop: Mechanistic Details\n\n**Two failure modes identified in standard AtP:**\n\n**Failure Mode 1 — Attention Saturation.** Standard AtP uses a first-order Taylor approximation (gradient × activation difference) to estimate each component's causal contribution. For attention heads, this means taking gradients through the softmax. When attention weights are saturated (near 0 or 1), the softmax gradient is nearly flat, making the linear approximation very poor. The gradient says \"changing this input barely changes the output,\" even though a large enough perturbation would move the softmax out of its saturated region.\n\n**QK-Fix solution:** Instead of approximating through the softmax with gradients, QK-Fix *explicitly recomputes* the attention probabilities with corrupted queries/keys while keeping the rest clean. Concretely:\n\n- For **query contributions**: compute `attn_patch = softmax(Q_corrupted · K_clean^T)` and `attn_clean = softmax(Q_clean · K_clean^T)`, then multiply the difference `(attn_patch - attn_clean)` by the downstream gradient `∂L/∂attn|_clean`. This replaces the gradient-through-softmax approximation with an exact computation of the first nonlinearity, then uses gradients only for the remaining (better-behaved) downstream computation.\n- For **key contributions**: analogous but more complex — requires measuring how each key's corruption changes attention weights across all queries. Naive implementation is O(T³); an efficient O(T²) variant exists.\n\nThe key insight: compute the first nonlinearity (softmax) exactly, then take linear approximations only downstream where they work better.\n\n**Failure Mode 2 — Cancellation.** A node's total effect is the sum of its direct and indirect effects. When these nearly cancel (direct ≈ −indirect), small multiplicative approximation errors can make the estimated total effect orders of magnitude wrong, causing false negatives.\n\n**GradDrop solution:** Run L additional backward passes (one per layer), each time zeroing the gradient at one layer's residual stream output before backpropagating. This isolates contributions that don't route through the dropped layer. The final GradDrop score aggregates absolute values across all these passes:\n\n```\nĉ_GD(n) = (1/(L-1)) · Σ_ℓ |ℐ̂^(AtP+GD_ℓ)(n)|\n```\n\nBy taking absolute values of each partial estimate and averaging, cancellation between direct and indirect paths is broken. Cost: L extra backward passes (optimizable to (L+1)/2).\n\n**AtP* = AtP + QK-Fix + GradDrop**, costing less than 2× a standard forward pass per prompt pair.\n\n---\n\n## 2. Open-Source Implementations\n\n**Dedicated AtP* repos:**\n\n- **[koayon/atp_star](https://github.com/koayon/atp_star)** — Unofficial PyTorch + NNsight implementation. Implements AtP, AtP+QK-Fix, and full AtP* (with GradDrop). **Node-level only** (not edge-level). Uses NNsight's `model.trace()` for interventions. QK-Fix is implemented by patching Q or K in the QKV tensor and re-running forward passes. GradDrop is implemented by calling `.grad.zero_()` on attention residual dropout inputs and MLP projection outputs at specific layers before backpropagation.\n\n**Edge-level attribution patching repos (no AtP*):**\n\n- **[Aaquib111/edge-attribution-patching](https://github.com/Aaquib111/edge-attribution-patching)** — EAP implementation on TransformerLens. NeurIPS 2024 ATTRIB paper. Edge-level but does **not** include AtP* modifications.\n- **[hannamw/eap-ig](https://github.com/hannamw/eap-ig)** — EAP-IG (integrated gradients variant) on TransformerLens. Supports edge-level analysis. Does **not** include AtP*.\n- **[UFO-101/auto-circuit](https://github.com/UFO-101/auto-circuit)** — AutoCircuit library. Implements ACDC, EAP, mask gradient, subnetwork probing, etc. Does **not** include AtP* or EAP-IG.\n\n**Bottom line: No existing open-source implementation combines AtP* (QK-Fix + GradDrop) with edge-level attribution.**\n\n---\n\n## 3. Implementing AtP* on Top of EAP-IG / TransformerLens\n\nTo add AtP* modifications to an edge-level EAP framework on TransformerLens, you would need:\n\n**For QK-Fix:**\n1. Hook into attention heads at the QKV computation level (e.g., `hook_q`, `hook_k` in TransformerLens).\n2. Instead of letting gradients flow through `softmax(Q·K^T/√d)`, compute two forward passes: one with corrupted Q (or K) patched in and one clean, both through the actual softmax.\n3. Compute `Δattn = softmax(Q_corrupt · K_clean^T/√d) − softmax(Q_clean · K_clean^T/√d)`.\n4. Multiply by the gradient of the loss w.r.t. the attention pattern (`hook_attn_scores` or `hook_pattern`).\n5. This replaces the standard gradient term for Q/K edges with the explicitly-linearized version.\n\n**For GradDrop:**\n1. Register backward hooks on each layer's residual stream output (e.g., `hook_resid_post` at layer ℓ).\n2. Run L backward passes, each time zeroing the gradient at a different layer's residual output using a backward hook that returns zeros.\n3. Collect the edge attribution scores from each pass, take absolute values, and average.\n\n**Key hooks needed in TransformerLens:**\n- `blocks[i].attn.hook_q`, `blocks[i].attn.hook_k` — for QK-Fix forward pass interventions\n- `blocks[i].attn.hook_pattern` or `blocks[i].attn.hook_attn_scores` — for reading attention weights and their gradients\n- `blocks[i].hook_resid_post` — for GradDrop gradient zeroing (backward hooks)\n- Standard EAP edge hooks for computing activation differences × gradients at each edge\n\nThe main engineering challenge is that QK-Fix requires additional forward passes (one per attention head being scored, or batched), significantly increasing cost compared to EAP's single-forward-backward paradigm.\n\n---\n\n## 4. Is AtP* Genuinely Different from EAP-IG?\n\nYes, they are meaningfully different algorithms within the same \"gradient-based attribution\" family:\n\n| Aspect | EAP-IG | AtP* |\n|--------|--------|------|\n| **Core technique** | Integrated gradients: average gradients over m interpolation steps between clean and corrupted | Single-point gradient with two targeted fixes |\n| **Saturation fix** | Averages over the path, hoping some points escape saturation | Explicitly computes softmax (QK-Fix), bypassing the approximation entirely |\n| **Cancellation fix** | None specific | GradDrop: isolates paths by zeroing gradients layer-by-layer |\n| **Scope in paper** | Edge-level | Node-level (paper), edge extension discussed in appendix |\n| **Cost** | 2m forward + m backward passes | ~2 forward + (L+1) backward passes |\n| **Framework** | Applies uniformly to all components | Attention-specific fix (QK-Fix) + general fix (GradDrop) |\n\n**Key distinction:** EAP-IG's integrated gradients can still fail if the entire interpolation path dwells in a saturated softmax region (the straight line from clean to corrupt may stay in a flat zone). AtP*'s QK-Fix avoids this entirely by computing the softmax exactly rather than approximating it. However, EAP-IG naturally handles edges, while AtP* was designed for nodes and requires nontrivial adaptation for edge-level use.\n\nA recent paper, **EAP-GP** (arXiv:2502.06852), proposes a third approach: dynamically adjusting the integration path to avoid saturated regions, achieving up to 17.7% improvement over EAP-IG on circuit faithfulness metrics.\n\n---\n\n## 5-6. GitHub Search Summary\n\nRepositories found:\n\n| Repository | Method | Level | Framework | AtP*? |\n|-----------|--------|-------|-----------|-------|\n| [koayon/atp_star](https://github.com/koayon/atp_star) | AtP* | Node | NNsight | Yes |\n| [Aaquib111/edge-attribution-patching](https://github.com/Aaquib111/edge-attribution-patching) | EAP | Edge | TransformerLens | No |\n| [hannamw/eap-ig](https://github.com/hannamw/eap-ig) | EAP-IG | Edge | TransformerLens | No |\n| [UFO-101/auto-circuit](https://github.com/UFO-101/auto-circuit) | EAP, ACDC, others | Edge | Custom + TL utils | No |\n| [rusheb/arena-hackathon-attribution-patching](https://github.com/rusheb/arena-hackathon-attribution-patching) | AtP variant | Edge | TransformerLens | No |\n| [technion-cs-nlp/PEAP](https://github.com/technion-cs-nlp/PEAP) | Position-aware EAP | Edge | TransformerLens | No |\n\n**No repository implements edge-level AtP*.** The only AtP* implementation (koayon/atp_star) is node-level and uses NNsight rather than TransformerLens. An edge-level AtP* implementation would need to be built from scratch, likely by adding QK-Fix and GradDrop modifications to an existing edge-level EAP framework like `hannamw/eap-ig` or `UFO-101/auto-circuit`."
      }
    ],
    "totalDurationMs": 161814,
    "totalTokens": 30821,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 159,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 27085,
      "output_tokens": 2534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1043
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 159,
          "output_tokens": 2534,
          "cache_read_input_tokens": 27085,
          "cache_creation_input_tokens": 1043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1043,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "496efde6-8feb-470b-bdfd-921405cd0df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 17 · 2026-05-12T10:23:56.400Z_

<details><summary>↩ Tool result · `toolu_01Mc6jCuco2hcvyfJLCfkEYA`</summary>

```text
I now have all the information needed. Here is the comprehensive report.

---

## MIB Circuit Track: Complete Method Inventory

The MIB circuit track (arXiv:2504.13151, ICML 2025) benchmarks circuit discovery on 4 models: **GPT-2 Small (117M), Qwen-2.5 (0.5B), Gemma-2 (2B), Llama-3.1 (8B)**.

### Full Method Table

| # | Method | Abbreviation | Algorithm Family | Edge-Level? | Ablation Type | Forward Passes | Scalability to 0.5B-8B |
|---|--------|-------------|-----------------|-------------|---------------|---------------|----------------------|
| 1 | Random | Random | Stochastic baseline | Yes (edges) | N/A | 0 | Trivial |
| 2 | Exact Activation Patching | EActP | **Causal intervention** (exact indirect effects) | Yes | CF | O(n) where n=edges | **Intractable** at scale (runtime) |
| 3 | Edge Attribution Patching (mean) | EAP (mean) | **Gradient attribution** (1st-order Taylor) | Yes | Mean | O(1) (2 fwd + 1 bwd) | Good |
| 4 | Edge Attribution Patching (CF) | EAP (CF) | **Gradient attribution** | Yes | CF | O(1) | Good |
| 5 | Edge Attribution Patching (OA) | EAP (OA) | **Gradient attribution** + learned ablation values | Yes | Optimal | O(1) + OA precomputation | Good (OA precomp adds cost) |
| 6 | EAP-IG inputs (CF) | EAP-IG-inp | **Gradient attribution** (integrated gradients) | Yes | CF | O(Z), Z=5 steps | Good |
| 7 | EAP-IG activations (CF) | EAP-IG-act | **Gradient attribution** (integrated gradients) | Yes | CF | O(Z*L), L=layers | Moderate (cost grows with depth) |
| 8 | Node Attribution Patching (CF) | NAP (CF) | **Gradient attribution** | No (node) | CF | O(1) | Good |
| 9 | NAP-IG (CF) | NAP-IG | **Gradient attribution** (integrated gradients) | No (node) | CF | O(Z) | Good |
| 10 | Information Flow Routes | IFR | **Activation decomposition / similarity-based** | Yes | None (no ablation) | 1 forward pass | **Excellent** (~100x faster than ACDC) |
| 11 | Uniform Gradient Sampling | UGS | **Mask optimization** (learned continuous edge masks) | Yes | CF | Many (iterative optimization) | **Intractable** at scale (memory) |

### Deep Dives on Requested Methods

**Information Flow Routes (IFR)** -- Ferrando & Voita, EMNLP 2024
- Algorithm family: **Activation decomposition with proximity-based scoring** -- NOT gradient-based, NOT causal intervention, NOT mask optimization. It decomposes the residual stream into per-component contributions and scores edge (u,v) by how similar u's output vector is to v's input vector, using negative L1 distance: `proximity(y_j, x) = max(-||y_j - x||_1 + ||x||_1, 0)`. Based on ALTI (Aggregation of Layer-Wise Token-to-Token Interactions).
- Edge-level: **Yes**.
- Scalability: **Best in class** -- requires only a single forward pass with activation caching, no backprop, no corrupted inputs. Reported ~100x speedup over ACDC. Scales easily to 8B models.
- Weakness: Non-causal (no counterfactual reasoning), so it measures co-occurrence/similarity rather than causal importance. MIB results show it underperforms attribution methods.

**Uniform Gradient Sampling (UGS)** -- Li & Janson, NeurIPS 2024 ("Optimal Ablation for Interpretability")
- Algorithm family: **Mask optimization**. Learns a continuous pruning mask alpha over all model edges. During training, edges with low mask values are ablated more fully. Uses gradient-based optimization to learn mask parameters, sampling ablation coefficients from distributions parameterized by learned theta. Achieves Pareto dominance over ACDC/EAP on small models.
- Edge-level: **Yes**.
- Scalability: **Poor** -- the paper and MIB both note it becomes "intractable with respect to memory requirements as models scale." Not practical for 2B-8B models.
- Same paper as OA (Optimal Ablations).

**EAP with Optimal Ablations (EAP-OA)** -- how it differs from EAP-IG
- EAP-OA is **NOT a different algorithm family from EAP**. It is standard EAP (gradient attribution, 1st-order Taylor approximation) but uses **optimal ablation values** instead of counterfactual or mean ablation values. The optimal ablation vector a* is precomputed by minimizing expected cross-entropy loss on the task dataset (from Li & Janson 2024).
- vs. EAP-IG: EAP-IG improves the **gradient estimation** (multiple interpolation steps via integrated gradients). EAP-OA improves the **ablation values** (what you replace ablated edges with). They are orthogonal modifications. EAP-IG changes the scoring function; EAP-OA changes what "off" means for an edge.
- Both are gradient attribution family, both are edge-level.

### Methods NOT in MIB Circuit Track

Notably absent: **ACDC** (Conmy et al. 2023), **Subnetwork Probing (SP)**, **HISP**, **Circuit Tracing** (Anthropic 2025). These are not evaluated in MIB.

### Non-Gradient, Non-Mask, Edge-Level Methods

Only **IFR** fits this category in MIB. It is the sole method that is:
- Edge-level
- Not gradient-based
- Not mask optimization
- Not causal intervention (no patching)

**EActP** (exact activation patching) is also non-gradient and edge-level, but it belongs to the **causal intervention** family (it computes exact indirect effects via O(n) forward passes).

### Best Overall Performer

**EAP-IG-inputs (CF)** generally performs best across the benchmark, offering the best tradeoff between approximation quality and computational cost.

### Key Sources

- MIB paper: https://arxiv.org/abs/2504.13151
- MIB circuit track code: https://github.com/hannamw/MIB-circuit-track
- IFR paper: https://arxiv.org/abs/2403.00824 (Ferrando & Voita, EMNLP 2024)
- UGS + OA paper: https://arxiv.org/abs/2409.09951 (Li & Janson, NeurIPS 2024)
- EAP-IG paper: Hanna et al. 2024; https://github.com/hannamw/eap-ig
- EAP paper: Syed et al. 2024; https://arxiv.org/abs/2310.10348

agentId: a5eb32e22fc60b16a (use SendMessage with to: 'a5eb32e22fc60b16a' to continue this agent)
&lt;usage>total_tokens: 37053
tool_uses: 23
duration_ms: 203440&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52e869f6-d419-4e09-bcde-d8146bb5e6cc",
  "isSidechain": false,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "type": "user",
  "uuid": "ac726126-ea5b-4d03-a6b7-ca1d046717cd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the MIB (Mechanistic Interpretability Benchmark) circuit track (arXiv:2504.13151, GitHub: hannamw/MIB-circuit-track).\n\nI need a comprehensive list of ALL circuit discovery methods supported by MIB circuit track. For each method:\n1. Algorithm family (gradient attribution / mask optimization / causal intervention / other)\n2. Is it edge-level (not just node-level)?\n3. Scalability to 0.5B-8B models (time complexity)\n\nPay special attention to:\n- **Information Flow Routes (IFR)** — what algorithm family? edge-level? scalable?\n- **Uniform Gradient Sampling (UGS)** — what algorithm family? edge-level? scalable?  \n- **EAP with Optimal Ablations (EAP-OA)** — how is it different from standard EAP-IG? Different algorithm family?\n- Any other methods that are NOT gradient-based and NOT mask-optimization but ARE edge-level\n\nSteps:\n1. WebSearch for \"MIB-circuit-track\" GitHub repo\n2. WebFetch the GitHub repo README to get the full method list\n3. Look at the code structure to see what methods are implemented\n4. WebSearch for IFR (Information Flow Routes) circuit discovery paper\n5. WebSearch for UGS (Uniform Gradient Sampling) circuit discovery paper\n6. WebSearch for \"EAP optimal ablation\" circuit discovery\n\nReport all findings concisely with a table of methods.",
    "agentId": "a5eb32e22fc60b16a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is the comprehensive report.\n\n---\n\n## MIB Circuit Track: Complete Method Inventory\n\nThe MIB circuit track (arXiv:2504.13151, ICML 2025) benchmarks circuit discovery on 4 models: **GPT-2 Small (117M), Qwen-2.5 (0.5B), Gemma-2 (2B), Llama-3.1 (8B)**.\n\n### Full Method Table\n\n| # | Method | Abbreviation | Algorithm Family | Edge-Level? | Ablation Type | Forward Passes | Scalability to 0.5B-8B |\n|---|--------|-------------|-----------------|-------------|---------------|---------------|----------------------|\n| 1 | Random | Random | Stochastic baseline | Yes (edges) | N/A | 0 | Trivial |\n| 2 | Exact Activation Patching | EActP | **Causal intervention** (exact indirect effects) | Yes | CF | O(n) where n=edges | **Intractable** at scale (runtime) |\n| 3 | Edge Attribution Patching (mean) | EAP (mean) | **Gradient attribution** (1st-order Taylor) | Yes | Mean | O(1) (2 fwd + 1 bwd) | Good |\n| 4 | Edge Attribution Patching (CF) | EAP (CF) | **Gradient attribution** | Yes | CF | O(1) | Good |\n| 5 | Edge Attribution Patching (OA) | EAP (OA) | **Gradient attribution** + learned ablation values | Yes | Optimal | O(1) + OA precomputation | Good (OA precomp adds cost) |\n| 6 | EAP-IG inputs (CF) | EAP-IG-inp | **Gradient attribution** (integrated gradients) | Yes | CF | O(Z), Z=5 steps | Good |\n| 7 | EAP-IG activations (CF) | EAP-IG-act | **Gradient attribution** (integrated gradients) | Yes | CF | O(Z*L), L=layers | Moderate (cost grows with depth) |\n| 8 | Node Attribution Patching (CF) | NAP (CF) | **Gradient attribution** | No (node) | CF | O(1) | Good |\n| 9 | NAP-IG (CF) | NAP-IG | **Gradient attribution** (integrated gradients) | No (node) | CF | O(Z) | Good |\n| 10 | Information Flow Routes | IFR | **Activation decomposition / similarity-based** | Yes | None (no ablation) | 1 forward pass | **Excellent** (~100x faster than ACDC) |\n| 11 | Uniform Gradient Sampling | UGS | **Mask optimization** (learned continuous edge masks) | Yes | CF | Many (iterative optimization) | **Intractable** at scale (memory) |\n\n### Deep Dives on Requested Methods\n\n**Information Flow Routes (IFR)** -- Ferrando & Voita, EMNLP 2024\n- Algorithm family: **Activation decomposition with proximity-based scoring** -- NOT gradient-based, NOT causal intervention, NOT mask optimization. It decomposes the residual stream into per-component contributions and scores edge (u,v) by how similar u's output vector is to v's input vector, using negative L1 distance: `proximity(y_j, x) = max(-||y_j - x||_1 + ||x||_1, 0)`. Based on ALTI (Aggregation of Layer-Wise Token-to-Token Interactions).\n- Edge-level: **Yes**.\n- Scalability: **Best in class** -- requires only a single forward pass with activation caching, no backprop, no corrupted inputs. Reported ~100x speedup over ACDC. Scales easily to 8B models.\n- Weakness: Non-causal (no counterfactual reasoning), so it measures co-occurrence/similarity rather than causal importance. MIB results show it underperforms attribution methods.\n\n**Uniform Gradient Sampling (UGS)** -- Li & Janson, NeurIPS 2024 (\"Optimal Ablation for Interpretability\")\n- Algorithm family: **Mask optimization**. Learns a continuous pruning mask alpha over all model edges. During training, edges with low mask values are ablated more fully. Uses gradient-based optimization to learn mask parameters, sampling ablation coefficients from distributions parameterized by learned theta. Achieves Pareto dominance over ACDC/EAP on small models.\n- Edge-level: **Yes**.\n- Scalability: **Poor** -- the paper and MIB both note it becomes \"intractable with respect to memory requirements as models scale.\" Not practical for 2B-8B models.\n- Same paper as OA (Optimal Ablations).\n\n**EAP with Optimal Ablations (EAP-OA)** -- how it differs from EAP-IG\n- EAP-OA is **NOT a different algorithm family from EAP**. It is standard EAP (gradient attribution, 1st-order Taylor approximation) but uses **optimal ablation values** instead of counterfactual or mean ablation values. The optimal ablation vector a* is precomputed by minimizing expected cross-entropy loss on the task dataset (from Li & Janson 2024).\n- vs. EAP-IG: EAP-IG improves the **gradient estimation** (multiple interpolation steps via integrated gradients). EAP-OA improves the **ablation values** (what you replace ablated edges with). They are orthogonal modifications. EAP-IG changes the scoring function; EAP-OA changes what \"off\" means for an edge.\n- Both are gradient attribution family, both are edge-level.\n\n### Methods NOT in MIB Circuit Track\n\nNotably absent: **ACDC** (Conmy et al. 2023), **Subnetwork Probing (SP)**, **HISP**, **Circuit Tracing** (Anthropic 2025). These are not evaluated in MIB.\n\n### Non-Gradient, Non-Mask, Edge-Level Methods\n\nOnly **IFR** fits this category in MIB. It is the sole method that is:\n- Edge-level\n- Not gradient-based\n- Not mask optimization\n- Not causal intervention (no patching)\n\n**EActP** (exact activation patching) is also non-gradient and edge-level, but it belongs to the **causal intervention** family (it computes exact indirect effects via O(n) forward passes).\n\n### Best Overall Performer\n\n**EAP-IG-inputs (CF)** generally performs best across the benchmark, offering the best tradeoff between approximation quality and computational cost.\n\n### Key Sources\n\n- MIB paper: https://arxiv.org/abs/2504.13151\n- MIB circuit track code: https://github.com/hannamw/MIB-circuit-track\n- IFR paper: https://arxiv.org/abs/2403.00824 (Ferrando & Voita, EMNLP 2024)\n- UGS + OA paper: https://arxiv.org/abs/2409.09951 (Li & Janson, NeurIPS 2024)\n- EAP-IG paper: Hanna et al. 2024; https://github.com/hannamw/eap-ig\n- EAP paper: Syed et al. 2024; https://arxiv.org/abs/2310.10348"
      }
    ],
    "totalDurationMs": 203440,
    "totalTokens": 37053,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 34546,
      "output_tokens": 1843,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 663
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1843,
          "cache_read_input_tokens": 34546,
          "cache_creation_input_tokens": 663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 663,
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
      "otherToolCount": 23
    }
  },
  "sourceToolAssistantUUID": "52e869f6-d419-4e09-bcde-d8146bb5e6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
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
  "leafUuid": "ac726126-ea5b-4d03-a6b7-ca1d046717cd",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate third method for large model circuit discovery",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891"
}
```

---

### Assistant

_source line 20 · 2026-05-12T10:24:22.772Z_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive research results from all three agents. Let me synthesize and write the evaluation report.

Key findings:

**Path (a): AtP* self-implementation**
- QK-Fix: explicitly recomputes softmax with corrupted Q/K instead of approximating through gradients
- GradDrop: zeros gradient at each layer's residual stream to break path cancellation
- No edge-level implementation exists (koayon/atp_star is node-level only, uses NNsight)
- Would need to be built from scratch on top of EAP-IG framework


- Distinct from EAP-IG since it uses single-point gradient plus QK-Fix linearization rather than integrated gradients, making it feasible but requiring roughly 1-2 days of implementation work

**Path (b): PAHQ accelerating ACDC**
- Open source implementation available with a 5x speedup on GPT-2 small, though it's only been tested at that scale and the authors note ACDC becomes computationally prohibitive on larger models
- Even with the 5x improvement, running it on the target models would still take 8-25 hours rather than meeting the ≤10h target
- The approach relies on a modified TransformerLens fork that would need porting to Qwen, making it impractical for this use case

**Path (c): MIB methods**
- IFR offers activation decomposition with excellent scalability through a single forward pass but lacks causality and underperforms; UGS requires intractable memory at scale; EAP-OA is just a variant of EAP-IG with different ablation values; EActP is exact but demands O(n) forward passes
- This leaves AtP with self-implementation as the most promising gradient-based approach, or IFR if I'm willing to accept the performance trade-off for scalability and algorithmic diversity

For the voting mechanism, I'm weighing whether to prioritize having three distinct algorithm families—which would mean pairing EAP-IG and Edge Pruning with IFR's activation decomposition approach—or sticking with AtP to stay within the gradient family but with meaningfully different mechanics. IFR's scalability and unique approach are compelling, but its lower performance could undermine the voting consensus. I think I'll write up the report and see how the numbers actually look.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac726126-ea5b-4d03-a6b7-ca1d046717cd",
  "isSidechain": false,
  "requestId": "req_011CaxWbhxQaGEvRHQ4D19n7",
  "type": "assistant",
  "uuid": "ff8864ff-1226-43a9-a328-ea8cd2497efc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135VoavT3dE1Pa6nsnzMfaw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7252,
      "cache_read_input_tokens": 24350,
      "output_tokens": 3707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3707,
          "cache_read_input_tokens": 24350,
          "cache_creation_input_tokens": 7252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7252
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-12T10:24:22.779Z_

Research complete. Writing the evaluation report now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff8864ff-1226-43a9-a328-ea8cd2497efc",
  "isSidechain": false,
  "requestId": "req_011CaxWbhxQaGEvRHQ4D19n7",
  "type": "assistant",
  "uuid": "eb99a2b3-1633-42ea-81eb-67c190f9ad4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135VoavT3dE1Pa6nsnzMfaw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7252,
      "cache_read_input_tokens": 24350,
      "output_tokens": 3707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3707,
          "cache_read_input_tokens": 24350,
          "cache_creation_input_tokens": 7252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7252
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-12T10:25:23.379Z_

<details open><summary>🔧 Tool call — Write · `toolu_01LXGdb1916J5vHqktZZoJ3M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/LARGE_MODEL_THIRD_METHOD.md",
  "content": "# 大模型第三方法可行性评估\n\n## 路径 (a): AtP* 自行实现\n\n- **可行性**: 是（有条件）\n- **预估工作量**: 1.5–2 天\n- **算法族**: Gradient attribution（与 EAP-IG 同族但子类不同）\n\n### 具体分析\n\nAtP* 的两个核心修改原理清晰：\n- **QK-Fix**: 不通过 softmax 反传梯度，而是显式计算 `softmax(Q_corrupt · K_clean^T) − softmax(Q_clean · K_clean^T)` 再乘下游梯度。绕过 attention saturation 问题。\n- **GradDrop**: 每层 residual stream 做一次 backward pass 时将该层梯度置零，收集 L 次 pass 的绝对值均值，打破 direct/indirect effect 的 cancellation。\n\n现有代码情况：\n- `koayon/atp_star`（GitHub）仅实现 **node-level**，且基于 NNsight 而非 TransformerLens。\n- **无任何 edge-level AtP* 开源实现**。需基于 `hannamw/eap-ig` 从零添加 QK-Fix + GradDrop。\n\n实现要点：\n- QK-Fix 需 hook `hook_q`/`hook_k`/`hook_pattern`，对每个 attention head 做额外 forward pass 计算 Δattn。\n- GradDrop 需在 `hook_resid_post` 注册 backward hook 做梯度置零，跑 L 次 backward pass。\n- 主要工程难度：QK-Fix 在 edge-level 下需要为每个 Q/K edge 分别计算，且 GradDrop 的 L 次 backward 增加成本。\n\n**算法独立性判断**：AtP* 与 EAP-IG 同属 gradient attribution 族，但机制差异显著——EAP-IG 用 integrated gradients（多步插值平均），AtP* 用 single-point gradient + 显式 softmax 线性化 + 路径隔离。**作为论文中的\"第三种方法\"，审稿人可能质疑其独立性**，因为本质仍是 gradient × activation difference 的变体。\n\n---\n\n## 路径 (b): PAHQ 加速 ACDC\n\n- **可行性**: 否\n- **预估工作量**: N/A\n- **算法族**: Causal intervention（加速版 ACDC）\n\n### 具体分析\n\nPAHQ（GitHub: `626619403/PAHQ`）已开源，基于 TransformerLens 修改版。核心思想：对 ACDC 每次 patching forward pass 中非关键组件做 mixed-precision 量化（FP8/BF16），关键头保持 FP32。\n\n**加速效果**：GPT-2 Small 上 5x 加速（99min → 20min），内存降 30%。\n\n**无法满足需求的原因**：\n1. 论文明确承认 \"ACDC becomes computationally prohibitive on larger models\"，未提供 0.5B+ 模型的 ACDC 时间数据。\n2. 即使乐观估计 5x 加速：42–127h → 8–25h/task，仍超 10h 目标。\n3. 仅支持 `gpt2`/`attn-only-4l`/`redwood_attn_2l`，移植到 Qwen 架构需大量适配。\n4. 依赖 H20 GPU 的 FP8 支持，硬件限制大。\n\n**其他 ACDC 加速方案**：\n- CD-T（ICLR 2025）声称\"hours to seconds\"但仅 node-level。\n- IBCircuit（ICML 2025）基于 information bottleneck，edge-level，但太新（2026.02），无成熟实现。\n\n结论：ACDC 在 0.5B+ 模型上不可行，加速方案均不足以弥补数量级差距。\n\n---\n\n## 路径 (c): MIB 其他方法\n\n### 方法列表\n\n| 方法 | 算法族 | Edge-level? | 大模型可扩展? | 备注 |\n|------|--------|------------|-------------|------|\n| Random | 随机基线 | ✓ | ✓ | 无意义 |\n| EActP (Exact Act. Patching) | Causal intervention | ✓ | ✗ (O(n) forward) | 与 ACDC 同样不可扩展 |\n| EAP (mean/CF) | Gradient attribution | ✓ | ✓ | EAP-IG 的简化版 |\n| **EAP-OA** | Gradient attribution | ✓ | ✓ | 见下方分析 |\n| **EAP-IG-inputs** | Gradient attribution (IG) | ✓ | ✓ | 已选为方法 1 |\n| EAP-IG-activations | Gradient attribution (IG) | ✓ | 中等 | 成本随层数增长 |\n| NAP / NAP-IG | Gradient attribution | ✗ (node) | ✓ | 非 edge-level |\n| **IFR** | **Activation decomposition** | ✓ | **✓✓ (极佳)** | 见下方分析 |\n| **UGS** | Mask optimization | ✓ | ✗ (内存爆炸) | 见下方分析 |\n\n### 重点评估\n\n**IFR (Information Flow Routes)**\n- **算法族**: Activation decomposition + proximity-based scoring。**与 gradient/mask/causal 三族均不同**。\n- **原理**: 将 residual stream 分解为各组件贡献，用负 L1 距离度量 edge (u→v) 的 proximity: `score(u,v) = max(-||y_u - x_v||_1 + ||x_v||_1, 0)`。基于 ALTI（Ferrando & Voita, EMNLP 2024）。\n- **Edge-level**: ✓\n- **可扩展性**: 极佳——仅需 1 次 forward pass + activation 缓存，无 backprop，无 corrupted input。比 ACDC 快 ~100x。\n- **弱点**: 非因果方法（无反事实推理），MIB 上性能低于 attribution 方法。度量的是\"激活相似度\"而非\"因果重要性\"。\n- **作为第三方法的价值**: 提供完全不同的算法视角（similarity-based vs. gradient-based vs. optimization-based），增强投票多样性。\n\n**UGS (Uniform Gradient Sampling)**\n- **算法族**: Mask optimization（与 Edge Pruning 同族）。\n- **原理**: 学习连续 pruning mask，通过梯度优化 mask 参数，采样 ablation 系数。\n- **Edge-level**: ✓\n- **可扩展性**: ✗。论文和 MIB 均确认 \"intractable with respect to memory requirements as models scale\"。\n- **结论**: 不可用于 0.5B+ 模型。且与 Edge Pruning 同属 mask optimization 族，算法多样性不足。\n\n**EAP-OA (EAP with Optimal Ablations)**\n- **与 EAP-IG 的区别**: EAP-OA 改进的是 **ablation 值**（用预计算的最优 ablation 向量 a* 替代 mean/CF ablation），而非梯度估计方式。EAP-IG 改进的是 **梯度估计**（integrated gradients）。两者正交。\n- **算法族**: 仍是 gradient attribution，与 EAP-IG 同族。\n- **结论**: 可作为 EAP-IG 的增强（EAP-IG + OA），但不构成独立的第三方法。\n\n---\n\n## 推荐\n\n- **首选**: **IFR (Information Flow Routes)**\n  - 唯一满足\"非 gradient、非 mask optimization、edge-level、可扩展到 8B\"全部条件的方法\n  - 算法族（activation decomposition）与 EAP-IG（gradient）和 Edge Pruning（mask optimization）完全不同，三法投票具备方法论多样性\n  - MIB 已有实现（`hannamw/MIB-circuit-track`），无需从零开发\n  - 仅需 1 次 forward pass，计算成本极低\n  - 弱点：非因果方法，faithfulness 可能较低——但在 K=3 共识投票中，diversity 比 individual accuracy 更重要\n\n- **备选**: **AtP* 自行实现**\n  - 作为 Plan B，如果 IFR 在实验中表现太差（投票结果与 EAP-IG/Edge Pruning 严重不一致）\n  - 工作量 ~1.5–2 天，风险在于与 EAP-IG 同属 gradient 族，审稿人可能挑战独立性\n\n- **理由**: 三法投票的论文贡献在于\"不同算法族的方法对 circuit structure 达成共识\"。IFR 提供了第三个完全独立的算法视角。即使 IFR 单独 faithfulness 较低，在共识框架下反而是优势——如果一个 similarity-based 方法也同意 gradient-based 和 optimization-based 方法找到的 edges，这些 edges 的可信度更高。\n\n### 最终方法组合\n\n| K | 方法 | 算法族 | 实现来源 |\n|---|------|--------|---------|\n| 1 | EAP-IG | Gradient attribution (integrated gradients) | `hannamw/eap-ig` |\n| 2 | Edge Pruning | Mask optimization | `UFO-101/auto-circuit` |\n| 3 | **IFR** | **Activation decomposition (proximity-based)** | `hannamw/MIB-circuit-track` |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb99a2b3-1633-42ea-81eb-67c190f9ad4f",
  "isSidechain": false,
  "requestId": "req_011CaxWbhxQaGEvRHQ4D19n7",
  "type": "assistant",
  "uuid": "6db38fdb-a2a7-4a08-8add-77c82dc02eae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135VoavT3dE1Pa6nsnzMfaw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7252,
      "cache_read_input_tokens": 24350,
      "output_tokens": 3707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3707,
          "cache_read_input_tokens": 24350,
          "cache_creation_input_tokens": 7252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7252
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T10:25:23.401Z_

<details><summary>↩ Tool result · `toolu_01LXGdb1916J5vHqktZZoJ3M`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/LARGE_MODEL_THIRD_METHOD.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6db38fdb-a2a7-4a08-8add-77c82dc02eae",
  "isSidechain": false,
  "promptId": "f9994110-988a-453d-b9d0-096ddcac193d",
  "type": "user",
  "uuid": "b8dd3ee5-f475-4a9d-949d-506bfcbc74eb",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/LARGE_MODEL_THIRD_METHOD.md",
    "content": "# 大模型第三方法可行性评估\n\n## 路径 (a): AtP* 自行实现\n\n- **可行性**: 是（有条件）\n- **预估工作量**: 1.5–2 天\n- **算法族**: Gradient attribution（与 EAP-IG 同族但子类不同）\n\n### 具体分析\n\nAtP* 的两个核心修改原理清晰：\n- **QK-Fix**: 不通过 softmax 反传梯度，而是显式计算 `softmax(Q_corrupt · K_clean^T) − softmax(Q_clean · K_clean^T)` 再乘下游梯度。绕过 attention saturation 问题。\n- **GradDrop**: 每层 residual stream 做一次 backward pass 时将该层梯度置零，收集 L 次 pass 的绝对值均值，打破 direct/indirect effect 的 cancellation。\n\n现有代码情况：\n- `koayon/atp_star`（GitHub）仅实现 **node-level**，且基于 NNsight 而非 TransformerLens。\n- **无任何 edge-level AtP* 开源实现**。需基于 `hannamw/eap-ig` 从零添加 QK-Fix + GradDrop。\n\n实现要点：\n- QK-Fix 需 hook `hook_q`/`hook_k`/`hook_pattern`，对每个 attention head 做额外 forward pass 计算 Δattn。\n- GradDrop 需在 `hook_resid_post` 注册 backward hook 做梯度置零，跑 L 次 backward pass。\n- 主要工程难度：QK-Fix 在 edge-level 下需要为每个 Q/K edge 分别计算，且 GradDrop 的 L 次 backward 增加成本。\n\n**算法独立性判断**：AtP* 与 EAP-IG 同属 gradient attribution 族，但机制差异显著——EAP-IG 用 integrated gradients（多步插值平均），AtP* 用 single-point gradient + 显式 softmax 线性化 + 路径隔离。**作为论文中的\"第三种方法\"，审稿人可能质疑其独立性**，因为本质仍是 gradient × activation difference 的变体。\n\n---\n\n## 路径 (b): PAHQ 加速 ACDC\n\n- **可行性**: 否\n- **预估工作量**: N/A\n- **算法族**: Causal intervention（加速版 ACDC）\n\n### 具体分析\n\nPAHQ（GitHub: `626619403/PAHQ`）已开源，基于 TransformerLens 修改版。核心思想：对 ACDC 每次 patching forward pass 中非关键组件做 mixed-precision 量化（FP8/BF16），关键头保持 FP32。\n\n**加速效果**：GPT-2 Small 上 5x 加速（99min → 20min），内存降 30%。\n\n**无法满足需求的原因**：\n1. 论文明确承认 \"ACDC becomes computationally prohibitive on larger models\"，未提供 0.5B+ 模型的 ACDC 时间数据。\n2. 即使乐观估计 5x 加速：42–127h → 8–25h/task，仍超 10h 目标。\n3. 仅支持 `gpt2`/`attn-only-4l`/`redwood_attn_2l`，移植到 Qwen 架构需大量适配。\n4. 依赖 H20 GPU 的 FP8 支持，硬件限制大。\n\n**其他 ACDC 加速方案**：\n- CD-T（ICLR 2025）声称\"hours to seconds\"但仅 node-level。\n- IBCircuit（ICML 2025）基于 information bottleneck，edge-level，但太新（2026.02），无成熟实现。\n\n结论：ACDC 在 0.5B+ 模型上不可行，加速方案均不足以弥补数量级差距。\n\n---\n\n## 路径 (c): MIB 其他方法\n\n### 方法列表\n\n| 方法 | 算法族 | Edge-level? | 大模型可扩展? | 备注 |\n|------|--------|------------|-------------|------|\n| Random | 随机基线 | ✓ | ✓ | 无意义 |\n| EActP (Exact Act. Patching) | Causal intervention | ✓ | ✗ (O(n) forward) | 与 ACDC 同样不可扩展 |\n| EAP (mean/CF) | Gradient attribution | ✓ | ✓ | EAP-IG 的简化版 |\n| **EAP-OA** | Gradient attribution | ✓ | ✓ | 见下方分析 |\n| **EAP-IG-inputs** | Gradient attribution (IG) | ✓ | ✓ | 已选为方法 1 |\n| EAP-IG-activations | Gradient attribution (IG) | ✓ | 中等 | 成本随层数增长 |\n| NAP / NAP-IG | Gradient attribution | ✗ (node) | ✓ | 非 edge-level |\n| **IFR** | **Activation decomposition** | ✓ | **✓✓ (极佳)** | 见下方分析 |\n| **UGS** | Mask optimization | ✓ | ✗ (内存爆炸) | 见下方分析 |\n\n### 重点评估\n\n**IFR (Information Flow Routes)**\n- **算法族**: Activation decomposition + proximity-based scoring。**与 gradient/mask/causal 三族均不同**。\n- **原理**: 将 residual stream 分解为各组件贡献，用负 L1 距离度量 edge (u→v) 的 proximity: `score(u,v) = max(-||y_u - x_v||_1 + ||x_v||_1, 0)`。基于 ALTI（Ferrando & Voita, EMNLP 2024）。\n- **Edge-level**: ✓\n- **可扩展性**: 极佳——仅需 1 次 forward pass + activation 缓存，无 backprop，无 corrupted input。比 ACDC 快 ~100x。\n- **弱点**: 非因果方法（无反事实推理），MIB 上性能低于 attribution 方法。度量的是\"激活相似度\"而非\"因果重要性\"。\n- **作为第三方法的价值**: 提供完全不同的算法视角（similarity-based vs. gradient-based vs. optimization-based），增强投票多样性。\n\n**UGS (Uniform Gradient Sampling)**\n- **算法族**: Mask optimization（与 Edge Pruning 同族）。\n- **原理**: 学习连续 pruning mask，通过梯度优化 mask 参数，采样 ablation 系数。\n- **Edge-level**: ✓\n- **可扩展性**: ✗。论文和 MIB 均确认 \"intractable with respect to memory requirements as models scale\"。\n- **结论**: 不可用于 0.5B+ 模型。且与 Edge Pruning 同属 mask optimization 族，算法多样性不足。\n\n**EAP-OA (EAP with Optimal Ablations)**\n- **与 EAP-IG 的区别**: EAP-OA 改进的是 **ablation 值**（用预计算的最优 ablation 向量 a* 替代 mean/CF ablation），而非梯度估计方式。EAP-IG 改进的是 **梯度估计**（integrated gradients）。两者正交。\n- **算法族**: 仍是 gradient attribution，与 EAP-IG 同族。\n- **结论**: 可作为 EAP-IG 的增强（EAP-IG + OA），但不构成独立的第三方法。\n\n---\n\n## 推荐\n\n- **首选**: **IFR (Information Flow Routes)**\n  - 唯一满足\"非 gradient、非 mask optimization、edge-level、可扩展到 8B\"全部条件的方法\n  - 算法族（activation decomposition）与 EAP-IG（gradient）和 Edge Pruning（mask optimization）完全不同，三法投票具备方法论多样性\n  - MIB 已有实现（`hannamw/MIB-circuit-track`），无需从零开发\n  - 仅需 1 次 forward pass，计算成本极低\n  - 弱点：非因果方法，faithfulness 可能较低——但在 K=3 共识投票中，diversity 比 individual accuracy 更重要\n\n- **备选**: **AtP* 自行实现**\n  - 作为 Plan B，如果 IFR 在实验中表现太差（投票结果与 EAP-IG/Edge Pruning 严重不一致）\n  - 工作量 ~1.5–2 天，风险在于与 EAP-IG 同属 gradient 族，审稿人可能挑战独立性\n\n- **理由**: 三法投票的论文贡献在于\"不同算法族的方法对 circuit structure 达成共识\"。IFR 提供了第三个完全独立的算法视角。即使 IFR 单独 faithfulness 较低，在共识框架下反而是优势——如果一个 similarity-based 方法也同意 gradient-based 和 optimization-based 方法找到的 edges，这些 edges 的可信度更高。\n\n### 最终方法组合\n\n| K | 方法 | 算法族 | 实现来源 |\n|---|------|--------|---------|\n| 1 | EAP-IG | Gradient attribution (integrated gradients) | `hannamw/eap-ig` |\n| 2 | Edge Pruning | Mask optimization | `UFO-101/auto-circuit` |\n| 3 | **IFR** | **Activation decomposition (proximity-based)** | `hannamw/MIB-circuit-track` |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "6db38fdb-a2a7-4a08-8add-77c82dc02eae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T10:25:30.334Z_

报告已写入 `LARGE_MODEL_THIRD_METHOD.md`。

核心结论：

**首选 IFR**——唯一满足全部条件（edge-level、非 gradient/非 mask optimization、可扩展到 8B）的方法。算法族为 activation decomposition，与 EAP-IG（gradient）和 Edge Pruning（mask optimization）形成三族独立投票。MIB 已有现成实现，仅需 1 次 forward pass。

**PAHQ 不可行**——5x 加速不够弥补 ACDC 在大模型上的数量级瓶颈。**UGS 不可行**——内存爆炸且与 Edge Pruning 同族。**AtP* 可作为备选**但与 EAP-IG 同属 gradient 族，审稿人可能质疑独立性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8dd3ee5-f475-4a9d-949d-506bfcbc74eb",
  "isSidechain": false,
  "requestId": "req_011CaxWi7ywmhuv8F75hXFJ6",
  "type": "assistant",
  "uuid": "ca7d5546-7c50-4810-9920-baa41d6aa9d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Bd5t1WFMqQ8mHkoNxk6i7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3768,
      "cache_read_input_tokens": 31602,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 31602,
          "cache_creation_input_tokens": 3768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3768
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
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
  "leafUuid": "ca7d5546-7c50-4810-9920-baa41d6aa9d1",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate third method for large model circuit discovery",
  "sessionId": "3a9d1438-71e8-4ba9-9cef-ef13b6ac4891"
}
```

---
