# Research conversation: <agent_context> 项目 turn_residual_gating (EMNLP 2026)。核心发现：GAR auxiliary loss 在 TF 训练下 IID GAR~0.50，但 autoregressive mode

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/dc81431a-1b02-4d85-8303-51e0fad97131.jsonl`
- **Structured JSON:** [`96cb35327885c3bda7fd.json`](../../sessions/96/96cb35327885c3bda7fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T06:26:48.158Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T06:26:48.158Z",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "content": "&lt;agent_context>\n项目 turn_residual_gating (EMNLP 2026)。核心发现：GAR auxiliary loss 在 TF 训练下 IID GAR~0.50，但 autoregressive model-gen GAR~0.015 (30x gap)。根因是 exposure bias。需要第二个 auxiliary objective 验证此现象的泛化性。\n\n现有代码结构：\n- src/train_phase2.py — 训练脚本，支持 GAR loss + gate diversity loss\n- src/threadgate.py — gate 机制\n- src/turn_utils.py — turn 标记识别，get_turn_markers()\n- src/eval_model_gen.py — model-gen eval\n\n模型：Qwen2.5-7B-Instruct (28 layers, hidden_size=3584)\n数据：ultrachat_8k (8000 multi-turn conversations)\n&lt;/agent_context>\n\n&lt;project_context>\n# 项目: turn_residual_gating\n\n## 运行环境\n- 服务器名: westd-20861\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/turn_residual_gating\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：Plan_NEW_B — Cross-objective Validation 方案调研与设计（P1）\n\n**目标**：设计一个非 GAR 的 auxiliary objective，重复 \"teacher-forced 成功 / autoregressive 失败\" 模式，证明 exposure bias 对 auxiliary objectives 的破坏是通用现象。\n\n### 背景\n当前论文发现：GAR auxiliary loss 在 teacher-forced 训练时有效（IID GAR ~0.50），但 autoregressive 推理时完全失败（model-gen GAR ~0.015）。根因是 exposure bias——训练时看到的 context 分布与推理时 model-generated 分布不同。\n\n论文需要证明这不是 GAR 特有的问题，而是所有依赖 multi-turn context 的 auxiliary objectives 的通用困境。\n\n### 候选 Objective 分析\n请调研以下候选，评估每个的：\n1. **实现复杂度**（能否在现有代码基础上快速实现）\n2. **可验证性**（能否清晰地测量 TF vs gen 的差异）\n3. **学术说服力**（reviewer 是否认可这个 objective 作为泛化验证）\n4. **预估 GPU 时间**\n\n#### 候选 A: Turn Consistency Loss\n- 鼓励相邻 turn 的 hidden state 余弦相似度\n- auxiliary loss = -cos_sim(h_turn_i, h_turn_{i+1})\n- TF 下应该学到一致性，gen 下分布偏移导致失败\n\n#### 候选 B: Position-aware Attention Target\n- 鼓励 attention 集中在某个特定位置（如 system prompt 或 first user message）\n- 类似 GAR 但目标不同——不是 goal token 而是另一个锚点\n- 如果选这个，与 GAR 可能太相似，reviewer 不认\n\n#### 候选 C: Turn-boundary NTP Loss\n- 在 turn boundary token 上施加额外的 NTP 损失权重\n- 测量 TF vs gen 下 turn boundary 的 NTP loss 差异\n- 简单但可能太 trivial\n\n#### 候选 D: Response Coherence Score\n- 用 sentence embedding 测量回复与 prompt 的语义相关度\n- 更高层次的指标，但实现复杂度高\n\n#### 候选 E: 其他\n- 你在文献中找到的适合此验证的 auxiliary objective\n\n### 调研方法\n1. 读取项目的 `literature_map.yaml` 看是否有相关论文\n2. 用 WebSearch 搜索 \"auxiliary objectives multi-turn dialogue\" / \"exposure bias auxiliary loss\" / \"multi-task learning dialogue generation\"\n3. 评估每个候选的 pros/cons\n\n### 输出格式\n```\n## 推荐方案\n**选择**: [候选 X]\n**理由**: ...\n**实现方案**: ...（具体到修改哪个文件、添加什么 loss）\n**预估成本**: X GPU-h\n**风险**: ...\n\n## 备选方案\n**选择**: [候选 Y]\n**理由**: ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T06:26:48.162Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T06:26:48.162Z",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131"
}
```

---

## Round 1

17 recorded events

### User

_source line 3 · 2026-05-20T06:26:48.202Z_

&lt;agent_context>
项目 turn_residual_gating (EMNLP 2026)。核心发现：GAR auxiliary loss 在 TF 训练下 IID GAR~0.50，但 autoregressive model-gen GAR~0.015 (30x gap)。根因是 exposure bias。需要第二个 auxiliary objective 验证此现象的泛化性。

现有代码结构：
- src/train_phase2.py — 训练脚本，支持 GAR loss + gate diversity loss
- src/threadgate.py — gate 机制
- src/turn_utils.py — turn 标记识别，get_turn_markers()
- src/eval_model_gen.py — model-gen eval

模型：Qwen2.5-7B-Instruct (28 layers, hidden_size=3584)
数据：ultrachat_8k (8000 multi-turn conversations)
&lt;/agent_context>

&lt;project_context>
# 项目: turn_residual_gating

## 运行环境
- 服务器名: westd-20861
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/turn_residual_gating


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：Plan_NEW_B — Cross-objective Validation 方案调研与设计（P1）

**目标**：设计一个非 GAR 的 auxiliary objective，重复 "teacher-forced 成功 / autoregressive 失败" 模式，证明 exposure bias 对 auxiliary objectives 的破坏是通用现象。

### 背景
当前论文发现：GAR auxiliary loss 在 teacher-forced 训练时有效（IID GAR ~0.50），但 autoregressive 推理时完全失败（model-gen GAR ~0.015）。根因是 exposure bias——训练时看到的 context 分布与推理时 model-generated 分布不同。

论文需要证明这不是 GAR 特有的问题，而是所有依赖 multi-turn context 的 auxiliary objectives 的通用困境。

### 候选 Objective 分析
请调研以下候选，评估每个的：
1. **实现复杂度**（能否在现有代码基础上快速实现）
2. **可验证性**（能否清晰地测量 TF vs gen 的差异）
3. **学术说服力**（reviewer 是否认可这个 objective 作为泛化验证）
4. **预估 GPU 时间**

#### 候选 A: Turn Consistency Loss
- 鼓励相邻 turn 的 hidden state 余弦相似度
- auxiliary loss = -cos_sim(h_turn_i, h_turn_{i+1})
- TF 下应该学到一致性，gen 下分布偏移导致失败

#### 候选 B: Position-aware Attention Target
- 鼓励 attention 集中在某个特定位置（如 system prompt 或 first user message）
- 类似 GAR 但目标不同——不是 goal token 而是另一个锚点
- 如果选这个，与 GAR 可能太相似，reviewer 不认

#### 候选 C: Turn-boundary NTP Loss
- 在 turn boundary token 上施加额外的 NTP 损失权重
- 测量 TF vs gen 下 turn boundary 的 NTP loss 差异
- 简单但可能太 trivial

#### 候选 D: Response Coherence Score
- 用 sentence embedding 测量回复与 prompt 的语义相关度
- 更高层次的指标，但实现复杂度高

#### 候选 E: 其他
- 你在文献中找到的适合此验证的 auxiliary objective

### 调研方法
1. 读取项目的 `literature_map.yaml` 看是否有相关论文
2. 用 WebSearch 搜索 "auxiliary objectives multi-turn dialogue" / "exposure bias auxiliary loss" / "multi-task learning dialogue generation"
3. 评估每个候选的 pros/cons

### 输出格式
```
## 推荐方案
**选择**: [候选 X]
**理由**: ...
**实现方案**: ...（具体到修改哪个文件、添加什么 loss）
**预估成本**: X GPU-h
**风险**: ...

## 备选方案
**选择**: [候选 Y]
**理由**: ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d3848ac0-795e-4374-b606-f54948e9f197",
  "type": "user",
  "uuid": "e3c52ce4-db07-4aea-9aa9-9e86ddc4cd1e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T06:26:48.201Z_

```json
{
  "parentUuid": "e3c52ce4-db07-4aea-9aa9-9e86ddc4cd1e",
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
  "uuid": "eb4e6a07-a024-40a8-b930-035fda9a4504",
  "timestamp": "2026-05-20T06:26:48.201Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T06:26:48.201Z_

```json
{
  "parentUuid": "eb4e6a07-a024-40a8-b930-035fda9a4504",
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
  "uuid": "53f02bdb-13f1-4e15-ac32-a908805fab87",
  "timestamp": "2026-05-20T06:26:48.201Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T06:26:48.201Z_

```json
{
  "parentUuid": "53f02bdb-13f1-4e15-ac32-a908805fab87",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4d7b7c68-3230-421a-9633-174e287d7170",
  "timestamp": "2026-05-20T06:26:48.201Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
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
  "aiTitle": "Design cross-objective validation for exposure bias",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131"
}
```

---

### Assistant

_source line 8 · 2026-05-20T06:26:52.924Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to research and design a cross-objective validation scheme for their EMNLP 2026 paper. They need a non-GAR auxiliary objective that reproduces the "teacher-forced success / autoregressive failure" pattern to prove exposure bias is a general problem for auxiliary objectives.

Let me start by:
1. Reading the project's literature_map.yaml and relevant files to understand current state
2. Searching for related literature
3. Evaluating the candidates

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d7b7c68-3230-421a-9633-174e287d7170",
  "isSidechain": false,
  "requestId": "req_011CbDLzDCZaJjygADWBndL9",
  "type": "assistant",
  "uuid": "caf6c74d-76e9-464b-a171-f906d78e1d57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLugu4hBXpUy6zoVFPeKMP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13421,
      "cache_read_input_tokens": 11841,
      "output_tokens": 950,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 950,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13421
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

_source line 9 · 2026-05-20T06:26:53.517Z_

先读项目现有代码和文献，再做文献调研。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caf6c74d-76e9-464b-a171-f906d78e1d57",
  "isSidechain": false,
  "requestId": "req_011CbDLzDCZaJjygADWBndL9",
  "type": "assistant",
  "uuid": "bb724ab6-e404-413e-b291-e9f186283b36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLugu4hBXpUy6zoVFPeKMP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13421,
      "cache_read_input_tokens": 11841,
      "output_tokens": 950,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 950,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13421
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

_source line 10 · 2026-05-20T06:26:59.917Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01QW9iBQ2sLbHuXvpFii2tki`</summary>

```json
{
  "description": "Read project code and config",
  "subagent_type": "Explore",
  "prompt": "I need to understand the turn_residual_gating project structure. Read these files and report their key contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml (if exists)\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/src/train_phase2.py — focus on the loss computation, especially how GAR loss is computed and added\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/src/threadgate.py — the gate mechanism\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/src/turn_utils.py — turn marker identification\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/src/eval_model_gen.py — how model-gen evaluation works\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/experiment_plan.yaml — current experiment plan\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md — current findings\n\nFor each file, report: key functions, loss computation logic, what data structures are used, and any relevant implementation details that would affect adding a new auxiliary objective.\n\nSearch breadth: very thorough"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb724ab6-e404-413e-b291-e9f186283b36",
  "isSidechain": false,
  "requestId": "req_011CbDLzDCZaJjygADWBndL9",
  "type": "assistant",
  "uuid": "017e1f55-6ca9-432a-be9d-5452f8cbdf8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLugu4hBXpUy6zoVFPeKMP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13421,
      "cache_read_input_tokens": 11841,
      "output_tokens": 950,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 950,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13421
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

_source line 11 · 2026-05-20T06:27:05.021Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LN5LATfu47PC14T62LLbEe`</summary>

```json
{
  "description": "Literature search on auxiliary objectives",
  "subagent_type": "general-purpose",
  "prompt": "I'm working on an EMNLP 2026 paper about exposure bias in multi-turn dialogue. Our core finding: GAR (Goal-Aware Residual) auxiliary loss works under teacher-forcing (IID GAR ~0.50) but fails under autoregressive generation (model-gen GAR ~0.015). We need to show this is a general phenomenon, not specific to GAR.\n\nPlease do web searches for:\n1. \"auxiliary objectives multi-turn dialogue exposure bias\"\n2. \"multi-task learning dialogue generation auxiliary loss\"\n3. \"exposure bias auxiliary objectives language model\"\n4. \"turn-level objectives dialogue systems\"\n5. \"consistency loss dialogue generation\"\n\nFor each search, report the most relevant papers and their key ideas. I'm looking for:\n- Other auxiliary objectives that have been proposed for multi-turn dialogue\n- Any work that has already studied exposure bias effects on auxiliary objectives\n- Turn-level consistency or coherence objectives\n- Attention-based auxiliary objectives in dialogue\n\nSummarize findings in under 300 words, focusing on what objectives exist and whether anyone has already shown exposure bias breaks them."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "017e1f55-6ca9-432a-be9d-5452f8cbdf8c",
  "isSidechain": false,
  "requestId": "req_011CbDLzDCZaJjygADWBndL9",
  "type": "assistant",
  "uuid": "d950e453-1bd8-4f89-b093-c4af4a20b4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLugu4hBXpUy6zoVFPeKMP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13421,
      "cache_read_input_tokens": 11841,
      "output_tokens": 950,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 950,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13421
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

_source line 12 · 2026-05-20T06:27:40.348Z_

<details><summary>↩ Tool result · `toolu_01LN5LATfu47PC14T62LLbEe`</summary>

```text
Here is the summary of findings:

---

**Existing auxiliary objectives for multi-turn dialogue fall into several categories:**

1. **Span prediction / response selection** -- MTTOD uses span prediction; RSTOD uses response selection as auxiliary tasks alongside LM loss. These are trained under teacher-forcing and evaluated on gold context.

2. **KL-based latent objectives** -- VHRED and DialogVED use KL divergence between approximate and true posterior distributions as auxiliary loss for sentence-level next-utterance prediction.

3. **Emotion / persona reconstruction** -- Multi-task frameworks jointly train generation + emotion classification (weighted losses) or persona reconstruction as auxiliary tasks.

4. **Turn-level coherence scoring** -- ECoh (2024) proposes turn-level coherence evaluation; other work uses discourse-level CCA objectives. These measure where conversations break down but are evaluation metrics, not training losses.

5. **Bag-of-Keywords loss** -- BoK (2025) introduces keyword-prediction auxiliary loss for interpretable dialogue generation.

6. **Consistency objectives** -- D-SMART, Midi-Tuning, and skeleton-guided generation address multi-turn consistency, but through architectural changes (structured memory, reasoning trees), not auxiliary training losses.

**On exposure bias breaking auxiliary objectives specifically:** UBARv2 and TA&AT directly study exposure bias in task-oriented dialogue and propose scheduled sampling / session-level sampling to mitigate it. The "Adaptive Bridge" paper (2021) learns to switch between ground-truth and generated context during training. However, **no paper was found that explicitly demonstrates auxiliary objectives collapsing under autoregressive generation** -- the existing work focuses on the primary generation loss degrading, not on auxiliary metrics (like GAR) specifically failing. This is the gap your paper can claim.

The 39% average performance drop in multi-turn generation tasks (from the consistency literature) provides useful supporting evidence that the distribution shift is severe, even if those papers don't frame it as auxiliary-objective collapse.

Sources:
- [UBARv2: Mitigating Exposure Bias in Task-Oriented Dialogs](https://arxiv.org/pdf/2209.07239)
- [TA&AT: Turn-Level Auxiliary Tasks and Scheduled Sampling](https://arxiv.org/pdf/2401.15626)
- [Adaptive Bridge between Training and Inference for Dialogue](https://arxiv.org/pdf/2110.11560)
- [BoK: Bag-of-Keywords Loss for Dialogue](https://arxiv.org/pdf/2501.10328)
- [ECoh: Turn-level Coherence Evaluation](https://arxiv.org/html/2407.11660v1)
- [Rethinking Exposure Bias in Language Modeling](https://arxiv.org/abs/1910.11235)
- [Quantifying Exposure Bias for Neural Language Generation](https://arxiv.org/pdf/1905.10617)
- [Multi-task Emotion-Aware Dialogue Generation](https://arxiv.org/pdf/2105.11696)
- [D-SMART: Dynamic Structured Memory for Dialogue Consistency](https://arxiv.org/pdf/2510.13363)
- [Midi-Tuning for Multi-Turn Dialogue](https://arxiv.org/html/2402.06967)
- [Fine-Tuning LLMs for Multi-Turn with KL Divergence](https://dl.acm.org/doi/10.1145/3651671.3651702)

agentId: a2e0698f28a03c6ba (use SendMessage with to: 'a2e0698f28a03c6ba' to continue this agent)
&lt;usage>total_tokens: 22134
tool_uses: 6
duration_ms: 35323&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d950e453-1bd8-4f89-b093-c4af4a20b4c4",
  "isSidechain": false,
  "promptId": "d3848ac0-795e-4374-b606-f54948e9f197",
  "type": "user",
  "uuid": "90dcc19e-af0f-46bd-9c72-625d3f0ae4d9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm working on an EMNLP 2026 paper about exposure bias in multi-turn dialogue. Our core finding: GAR (Goal-Aware Residual) auxiliary loss works under teacher-forcing (IID GAR ~0.50) but fails under autoregressive generation (model-gen GAR ~0.015). We need to show this is a general phenomenon, not specific to GAR.\n\nPlease do web searches for:\n1. \"auxiliary objectives multi-turn dialogue exposure bias\"\n2. \"multi-task learning dialogue generation auxiliary loss\"\n3. \"exposure bias auxiliary objectives language model\"\n4. \"turn-level objectives dialogue systems\"\n5. \"consistency loss dialogue generation\"\n\nFor each search, report the most relevant papers and their key ideas. I'm looking for:\n- Other auxiliary objectives that have been proposed for multi-turn dialogue\n- Any work that has already studied exposure bias effects on auxiliary objectives\n- Turn-level consistency or coherence objectives\n- Attention-based auxiliary objectives in dialogue\n\nSummarize findings in under 300 words, focusing on what objectives exist and whether anyone has already shown exposure bias breaks them.",
    "agentId": "a2e0698f28a03c6ba",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the summary of findings:\n\n---\n\n**Existing auxiliary objectives for multi-turn dialogue fall into several categories:**\n\n1. **Span prediction / response selection** -- MTTOD uses span prediction; RSTOD uses response selection as auxiliary tasks alongside LM loss. These are trained under teacher-forcing and evaluated on gold context.\n\n2. **KL-based latent objectives** -- VHRED and DialogVED use KL divergence between approximate and true posterior distributions as auxiliary loss for sentence-level next-utterance prediction.\n\n3. **Emotion / persona reconstruction** -- Multi-task frameworks jointly train generation + emotion classification (weighted losses) or persona reconstruction as auxiliary tasks.\n\n4. **Turn-level coherence scoring** -- ECoh (2024) proposes turn-level coherence evaluation; other work uses discourse-level CCA objectives. These measure where conversations break down but are evaluation metrics, not training losses.\n\n5. **Bag-of-Keywords loss** -- BoK (2025) introduces keyword-prediction auxiliary loss for interpretable dialogue generation.\n\n6. **Consistency objectives** -- D-SMART, Midi-Tuning, and skeleton-guided generation address multi-turn consistency, but through architectural changes (structured memory, reasoning trees), not auxiliary training losses.\n\n**On exposure bias breaking auxiliary objectives specifically:** UBARv2 and TA&AT directly study exposure bias in task-oriented dialogue and propose scheduled sampling / session-level sampling to mitigate it. The \"Adaptive Bridge\" paper (2021) learns to switch between ground-truth and generated context during training. However, **no paper was found that explicitly demonstrates auxiliary objectives collapsing under autoregressive generation** -- the existing work focuses on the primary generation loss degrading, not on auxiliary metrics (like GAR) specifically failing. This is the gap your paper can claim.\n\nThe 39% average performance drop in multi-turn generation tasks (from the consistency literature) provides useful supporting evidence that the distribution shift is severe, even if those papers don't frame it as auxiliary-objective collapse.\n\nSources:\n- [UBARv2: Mitigating Exposure Bias in Task-Oriented Dialogs](https://arxiv.org/pdf/2209.07239)\n- [TA&AT: Turn-Level Auxiliary Tasks and Scheduled Sampling](https://arxiv.org/pdf/2401.15626)\n- [Adaptive Bridge between Training and Inference for Dialogue](https://arxiv.org/pdf/2110.11560)\n- [BoK: Bag-of-Keywords Loss for Dialogue](https://arxiv.org/pdf/2501.10328)\n- [ECoh: Turn-level Coherence Evaluation](https://arxiv.org/html/2407.11660v1)\n- [Rethinking Exposure Bias in Language Modeling](https://arxiv.org/abs/1910.11235)\n- [Quantifying Exposure Bias for Neural Language Generation](https://arxiv.org/pdf/1905.10617)\n- [Multi-task Emotion-Aware Dialogue Generation](https://arxiv.org/pdf/2105.11696)\n- [D-SMART: Dynamic Structured Memory for Dialogue Consistency](https://arxiv.org/pdf/2510.13363)\n- [Midi-Tuning for Multi-Turn Dialogue](https://arxiv.org/html/2402.06967)\n- [Fine-Tuning LLMs for Multi-Turn with KL Divergence](https://dl.acm.org/doi/10.1145/3651671.3651702)"
      }
    ],
    "totalDurationMs": 35323,
    "totalTokens": 22134,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 17318,
      "output_tokens": 829,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3160
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 827,
          "output_tokens": 829,
          "cache_read_input_tokens": 17318,
          "cache_creation_input_tokens": 3160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3160,
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
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "d950e453-1bd8-4f89-b093-c4af4a20b4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T06:27:56.056Z_

<details><summary>↩ Tool result · `toolu_01QW9iBQ2sLbHuXvpFii2tki`</summary>

````text
Perfect! Now I have a comprehensive understanding of the project. Let me compile a detailed report of the key contents.

## Project Structure Report: turn_residual_gating

### 1. **Literature Map Overview** (literature_map.yaml)

The project is contextualized within 6 research categories:

- **Layer Importance**: Foundation work on transformer layer redundancy (Gromov et al. ICLR 2025, Men et al. ShortGPT)
- **Multi-Turn Attention**: Core diagnostic papers including Dongre et al. (2026) defining GAR metric and identifying attention channel closure
- **Residual Gating**: Method components (Mixture-of-Depths, CALM, FlexiDepth, SkipNet) and direct competitors
- **Attention Manipulation**: Long-context solutions (ALiBi, Positional Interpolation, YaRN, Attention Sinks)
- **Theoretical Foundations**: Transformer circuits framework (Elhage et al.), residual stream analysis
- **Exposure Bias**: Core literature on train-test distribution mismatch (Bengio et al. 2015, Ranzato et al. 2016, Professor Forcing)
- **Gradient Conflict / MTL**: Multi-task learning conflict resolution (PCGrad, GradNorm, CAGrad, Nash-MTL)
- **Residual Scaling**: Zero-init methods (ReZero, Fixup)
- **Evaluation Benchmarks**: MT-Bench-101, MultiChallenge, WildBench

### 2. **Train Phase 2 Loss Computation** (train_phase2.py)

**Key Functions:**
- `MultiTurnDataset`: Loads ultrachat data, applies chat template, detects turn boundaries, builds turn features
- `log_gate_stats()`: Logs per-layer gate values (mean, std, min, max)
- `main()`: Main training loop with three loss components

**Loss Computation Logic (lines 249-274):**

```python
# Three-part loss function:
l_ntp = outputs.loss  # Cross-entropy on assistant tokens only

# GAR loss (differentiable)
gar_per_turn = []
for pos in assistant_last_positions:
    gar_val = measurer.compute_gar_differentiable(goal_pos, [pos])
    gar_per_turn.append(gar_val)
l_gar = compute_gar_loss(gar_per_turn, epsilon=args.gar_epsilon, mode=args.gar_loss_mode, target=args.gar_target)

# Gate diversity loss (regularization)
per_layer_means = [gate_values[layer_idx].mean() for layer_idx in sorted_layers]
current_gate_std = torch.stack(per_layer_means).std()
l_gate_div = F.relu(torch.tensor(args.min_gate_std) - current_gate_std)  # Triggers only if std < threshold

# Total loss
loss = l_ntp + args.lambda_gar * l_gar + args.lambda_gate_div * l_gate_div
```

**Key Design Choices:**
- Uses gradient accumulation (default 8 steps)
- Separate parameter groups for LoRA and gate parameters with different learning rates
- `measure_only=False` for GARMeasurer to enable differentiable GAR computation
- Gate hooks capture per-token per-layer gate values for statistics
- MSE_target mode (bidirectional) is the only successfully training loss (v7 configuration)

### 3. **ThreadGate Architecture** (threadgate.py)

**Core Components:**

- **TurnEmbedding**: Embeds turn_distance and turn_index separately (half_dim each, max_distance=32, total=16-dim)
- **GateNetwork**: Per-layer gating module receiving:
  - Input: hidden_state (projected to LORA_RANK=16 via down_proj)
  - Turn features: turn_distance, turn_index embeddings
  - Mechanism: `[proj(x_l); turn_emb(t_d, t_i)] → fc1 (ReLU) → fc2 (sigmoid) → gate ∈ [0,1]`
  - Init bias=1.5 typically sets gate ≈ 0.82 initially

- **UniformGateNetwork**: Same architecture but uses constant_vector instead of turn_embedding (ablation variant)

**Gating Mechanism (residual connection hooks):**
```python
# Per-layer forward hook:
gate = gates[i](layer_input, turn_features)
f_x = layer_output - layer_input  # Residual component
gated = layer_input + gate * f_x   # ReZero-style: x + g·f(x)
```

**Critical Implementation Detail:** Gate acts as multiplicative scaling of the residual contribution. When gate→0, layer becomes no-op (preserves input). When gate→1, layer operates normally.

### 4. **Turn Marker Identification** (turn_utils.py)

**Key Functions:**

- `get_turn_markers()`: Auto-detects format (ChatML with `<|im_start|>`/`<|im_end|>` vs Llama3 with `<|start_header_id|>`/`<|eot_id|>`)
- `detect_turn_boundaries()`: Returns comprehensive turn structure:
  - `turns`: List of turn dicts with role, start, end, content_start, content_end
  - `goal_token_positions`: System prompt + first user query tokens (GAR-ours definition)
  - `assistant_last_token_positions`: Last token of each assistant response (query positions)
  - `turn_distance_map`: Token distance from nearest turn boundary
  - `turn_index_map`: Which turn number each token belongs to

- `build_turn_features()`: Creates per-token turn_distance and turn_index tensors for the gate input

**Data Structures:**
- All return torch tensors (1D for per-token features)
- Turn distance resets to 0 at each boundary marker
- Turn index increments on start markers

### 5. **GAR Loss Computation** (gar.py)

**GARMeasurer Class:**
- Hooks into attention modules to capture attention weights
- `compute_gar()`: Non-differentiable version (used for evaluation)
- `compute_gar_differentiable()`: Computes goal attention ratio on the fly during training

**GAR Formula:**
```
GAR = (1 / L·H·|Q|) Σ_layer Σ_head Σ_query Σ_goal attention[query, goal]
```
Where Q = query positions (assistant last tokens), goals = goal tokens (system + first user)

**compute_gar_loss() Function (6 modes):**

1. **pairwise** (v1-v2): `Σ_i relu(GAR[i-1] - GAR[i] - epsilon)` — minimize consecutive drops
2. **cumulative** (v1-v2): `Σ_i relu(GAR[0] - GAR[i] - epsilon)` — all turns vs first turn
3. **maximize** (v3-v5): `-mean(GAR)` — unbounded upward, causes identity collapse
4. **smooth_saturation** (v6): `-target * tanh(mean_GAR / target)` — bounded but still monotonic→collapse
5. **hinge_target** (v1-v2): `relu(target - mean_GAR)` — zero gradient when GAR ≥ target
6. **mse_target** (v7, FINAL): `(mean_GAR - target)²` — **bidirectional, only mode that trains successfully**

### 6. **Model-Gen Evaluation** (eval_phase2_gar.py)

**Evaluation Workflow:**

1. **Conversation Generation**: Uses base model to generate multi-turn conversations on 5 system prompts × 10 questions
2. **Gate Loading**: Loads trained gate parameters from checkpoint
3. **Hook Registration**: Registers gating hooks on model layers
4. **Per-Turn GAR Measurement**: For each assistant turn, computes GAR with gating active
5. **Dual GAR Variants**:
   - GAR-ours: goal = system + first user, query = last token per assistant turn
   - GAR-Dongre: goal = system only, query = all tokens per assistant turn
6. **NTP Perplexity**: Computes on assistant-only tokens with gating active
7. **Gate Profiling** (optional): Extracts per-turn per-layer gate values and dynamic range

**Key Data Structures:**
- `gate_values_ref`: Mutable container to capture gates during forward pass
- `turn_features_ref`: Carries turn-distance/turn-index tensors through forward hooks
- Returns JSON with GAR curves, PPL, gate profiles

**Critical Measurement Context**: All eval metrics **include active gating** (hooks modify residual connections)

### 7. **Core Findings Summary** (memory.md & paper_framing.md)

**Central Discovery (M017 corrected):**
- **30× Training-Inference GAR Gap**: Models train GAR-ours to 0.48-0.50 on same-distribution (ultrachat) text but collapse to 0.016-0.025 on model-generated text
- **Root Cause**: Exposure bias (teacher-forcing distribution shift), NOT gradient conflict or gating design
- **PCGrad Proof (D028)**: Gradient direction conflict is inconsequential—consuming conflict after removal yields IID PPL 2.780 vs v7 2.784 (diff 0.004, no improvement)

**Four-Way Ablation Results (D033, same protocol):**
| Model | GAR-ours (IID) | GAR-ours (model-gen) | PPL (IID) |
|-------|---|---|---|
| ThreadGate (v7) | 0.5035 | 0.0157 | 2.78 |
| UniformGate | 0.505 | 0.0149 | 2.78 |
| LoRA-only | 0.498 | 0.0245 | 2.78 |
| Baseline | 0.012 | — | — |

**Key Mechanism Insights:**
- NTP gradients dominate gate updates (7.5→14.7× magnitude ratio over GAR gradients)
- 27/28 layers show gate conditioning reversal: turn1 gate < turn21 gate (Wilcoxon p<10⁻⁷), meaning gates suppress early turns where GAR is high
- Gate attenuation at inference: mean gate = 0.93-0.98 (only 2-7% residual blocking), insufficient to shift attention patterns

### 8. **Configuration** (config.py)

```python
MODEL_NAME = "/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct"
LORA_RANK = 16
GATE_HIDDEN_DIM = 64
MAX_TURN_DISTANCE = 32
TURN_EMBED_DIM = 16
GAR_EPSILON = 0.001
GAR_LAMBDA = 1.0  # Weight for GAR loss
LEARNING_RATE = 2e-4
BATCH_SIZE = 1
GRADIENT_ACCUMULATION = 8
MAX_SEQ_LEN = 2048
NUM_EPOCHS = 3
SEED = 42
INIT_BIAS = 1.5  # Sets initial gate ≈ 0.82 via sigmoid
GAR_LOSS_MODE = "mse_target"  # Only mode that converges
GAR_TARGET = 0.5  # MSE target for mean GAR
LAMBDA_GATE_DIV = 1.0  # Weight for gate diversity regularizer
MIN_GATE_STD = 0.05  # Threshold for triggering gate_div loss
```

### 9. **Status & Current Training** (report.md)

- v8b SS (scheduled sampling) training in progress on westd-20861 GPU
- Early signal: TF_L_GAR drops 67%, but SS_L_GAR drops only 10% — direct exposure bias measurement
- Plan: v8b eval → Plan_022 λ_GAR sensitivity → seed variations → Llama-3.1-8B validation

---

## Summary for Adding New Auxiliary Objectives

To add a new auxiliary objective to this framework, you'll need to:

1. **Create differentiable loss function** in gar.py (following compute_gar_loss pattern with mode parameter)
2. **Add command-line argument** in train_phase2.py for the new loss weight (λ parameter)
3. **Integrate into loss computation** (line 274) as: `loss = l_ntp + λ_new * l_new + args.lambda_gate_div * l_gate_div`
4. **Use GARMeasurer.measure()` context manager** to capture attention for metric computation
5. **Log metrics** alongside l_ntp, l_gar, l_gate_div in training loop
6. **Consider gradient conflict**: Expect NTP dominance (~10-15× magnitude) and potential direction conflicts unless using gradient surgery techniques
7. **Evaluate on both IID and model-gen distributions** to measure exposure bias impact on new objective
8. **Account for initialization**: init_bias=1.5 controls gate starting point; tune for new loss dynamics

The code architecture is well-structured for adding auxiliary objectives—the loss, gating, and measurement systems are cleanly separated with clear extension points.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "017e1f55-6ca9-432a-be9d-5452f8cbdf8c",
  "isSidechain": false,
  "promptId": "d3848ac0-795e-4374-b606-f54948e9f197",
  "type": "user",
  "uuid": "ba5d5f66-eb32-48f4-ad32-65b274bdb785",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the turn_residual_gating project structure. Read these files and report their key contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml (if exists)\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/src/train_phase2.py — focus on the loss computation, especially how GAR loss is computed and added\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/src/threadgate.py — the gate mechanism\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/src/turn_utils.py — turn marker identification\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/src/eval_model_gen.py — how model-gen evaluation works\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/experiment_plan.yaml — current experiment plan\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md — current findings\n\nFor each file, report: key functions, loss computation logic, what data structures are used, and any relevant implementation details that would affect adding a new auxiliary objective.\n\nSearch breadth: very thorough",
    "agentId": "af03cd2d0d4f3cc5d",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have a comprehensive understanding of the project. Let me compile a detailed report of the key contents.\n\n## Project Structure Report: turn_residual_gating\n\n### 1. **Literature Map Overview** (literature_map.yaml)\n\nThe project is contextualized within 6 research categories:\n\n- **Layer Importance**: Foundation work on transformer layer redundancy (Gromov et al. ICLR 2025, Men et al. ShortGPT)\n- **Multi-Turn Attention**: Core diagnostic papers including Dongre et al. (2026) defining GAR metric and identifying attention channel closure\n- **Residual Gating**: Method components (Mixture-of-Depths, CALM, FlexiDepth, SkipNet) and direct competitors\n- **Attention Manipulation**: Long-context solutions (ALiBi, Positional Interpolation, YaRN, Attention Sinks)\n- **Theoretical Foundations**: Transformer circuits framework (Elhage et al.), residual stream analysis\n- **Exposure Bias**: Core literature on train-test distribution mismatch (Bengio et al. 2015, Ranzato et al. 2016, Professor Forcing)\n- **Gradient Conflict / MTL**: Multi-task learning conflict resolution (PCGrad, GradNorm, CAGrad, Nash-MTL)\n- **Residual Scaling**: Zero-init methods (ReZero, Fixup)\n- **Evaluation Benchmarks**: MT-Bench-101, MultiChallenge, WildBench\n\n### 2. **Train Phase 2 Loss Computation** (train_phase2.py)\n\n**Key Functions:**\n- `MultiTurnDataset`: Loads ultrachat data, applies chat template, detects turn boundaries, builds turn features\n- `log_gate_stats()`: Logs per-layer gate values (mean, std, min, max)\n- `main()`: Main training loop with three loss components\n\n**Loss Computation Logic (lines 249-274):**\n\n```python\n# Three-part loss function:\nl_ntp = outputs.loss  # Cross-entropy on assistant tokens only\n\n# GAR loss (differentiable)\ngar_per_turn = []\nfor pos in assistant_last_positions:\n    gar_val = measurer.compute_gar_differentiable(goal_pos, [pos])\n    gar_per_turn.append(gar_val)\nl_gar = compute_gar_loss(gar_per_turn, epsilon=args.gar_epsilon, mode=args.gar_loss_mode, target=args.gar_target)\n\n# Gate diversity loss (regularization)\nper_layer_means = [gate_values[layer_idx].mean() for layer_idx in sorted_layers]\ncurrent_gate_std = torch.stack(per_layer_means).std()\nl_gate_div = F.relu(torch.tensor(args.min_gate_std) - current_gate_std)  # Triggers only if std < threshold\n\n# Total loss\nloss = l_ntp + args.lambda_gar * l_gar + args.lambda_gate_div * l_gate_div\n```\n\n**Key Design Choices:**\n- Uses gradient accumulation (default 8 steps)\n- Separate parameter groups for LoRA and gate parameters with different learning rates\n- `measure_only=False` for GARMeasurer to enable differentiable GAR computation\n- Gate hooks capture per-token per-layer gate values for statistics\n- MSE_target mode (bidirectional) is the only successfully training loss (v7 configuration)\n\n### 3. **ThreadGate Architecture** (threadgate.py)\n\n**Core Components:**\n\n- **TurnEmbedding**: Embeds turn_distance and turn_index separately (half_dim each, max_distance=32, total=16-dim)\n- **GateNetwork**: Per-layer gating module receiving:\n  - Input: hidden_state (projected to LORA_RANK=16 via down_proj)\n  - Turn features: turn_distance, turn_index embeddings\n  - Mechanism: `[proj(x_l); turn_emb(t_d, t_i)] → fc1 (ReLU) → fc2 (sigmoid) → gate ∈ [0,1]`\n  - Init bias=1.5 typically sets gate ≈ 0.82 initially\n\n- **UniformGateNetwork**: Same architecture but uses constant_vector instead of turn_embedding (ablation variant)\n\n**Gating Mechanism (residual connection hooks):**\n```python\n# Per-layer forward hook:\ngate = gates[i](layer_input, turn_features)\nf_x = layer_output - layer_input  # Residual component\ngated = layer_input + gate * f_x   # ReZero-style: x + g·f(x)\n```\n\n**Critical Implementation Detail:** Gate acts as multiplicative scaling of the residual contribution. When gate→0, layer becomes no-op (preserves input). When gate→1, layer operates normally.\n\n### 4. **Turn Marker Identification** (turn_utils.py)\n\n**Key Functions:**\n\n- `get_turn_markers()`: Auto-detects format (ChatML with `<|im_start|>`/`<|im_end|>` vs Llama3 with `<|start_header_id|>`/`<|eot_id|>`)\n- `detect_turn_boundaries()`: Returns comprehensive turn structure:\n  - `turns`: List of turn dicts with role, start, end, content_start, content_end\n  - `goal_token_positions`: System prompt + first user query tokens (GAR-ours definition)\n  - `assistant_last_token_positions`: Last token of each assistant response (query positions)\n  - `turn_distance_map`: Token distance from nearest turn boundary\n  - `turn_index_map`: Which turn number each token belongs to\n\n- `build_turn_features()`: Creates per-token turn_distance and turn_index tensors for the gate input\n\n**Data Structures:**\n- All return torch tensors (1D for per-token features)\n- Turn distance resets to 0 at each boundary marker\n- Turn index increments on start markers\n\n### 5. **GAR Loss Computation** (gar.py)\n\n**GARMeasurer Class:**\n- Hooks into attention modules to capture attention weights\n- `compute_gar()`: Non-differentiable version (used for evaluation)\n- `compute_gar_differentiable()`: Computes goal attention ratio on the fly during training\n\n**GAR Formula:**\n```\nGAR = (1 / L·H·|Q|) Σ_layer Σ_head Σ_query Σ_goal attention[query, goal]\n```\nWhere Q = query positions (assistant last tokens), goals = goal tokens (system + first user)\n\n**compute_gar_loss() Function (6 modes):**\n\n1. **pairwise** (v1-v2): `Σ_i relu(GAR[i-1] - GAR[i] - epsilon)` — minimize consecutive drops\n2. **cumulative** (v1-v2): `Σ_i relu(GAR[0] - GAR[i] - epsilon)` — all turns vs first turn\n3. **maximize** (v3-v5): `-mean(GAR)` — unbounded upward, causes identity collapse\n4. **smooth_saturation** (v6): `-target * tanh(mean_GAR / target)` — bounded but still monotonic→collapse\n5. **hinge_target** (v1-v2): `relu(target - mean_GAR)` — zero gradient when GAR ≥ target\n6. **mse_target** (v7, FINAL): `(mean_GAR - target)²` — **bidirectional, only mode that trains successfully**\n\n### 6. **Model-Gen Evaluation** (eval_phase2_gar.py)\n\n**Evaluation Workflow:**\n\n1. **Conversation Generation**: Uses base model to generate multi-turn conversations on 5 system prompts × 10 questions\n2. **Gate Loading**: Loads trained gate parameters from checkpoint\n3. **Hook Registration**: Registers gating hooks on model layers\n4. **Per-Turn GAR Measurement**: For each assistant turn, computes GAR with gating active\n5. **Dual GAR Variants**:\n   - GAR-ours: goal = system + first user, query = last token per assistant turn\n   - GAR-Dongre: goal = system only, query = all tokens per assistant turn\n6. **NTP Perplexity**: Computes on assistant-only tokens with gating active\n7. **Gate Profiling** (optional): Extracts per-turn per-layer gate values and dynamic range\n\n**Key Data Structures:**\n- `gate_values_ref`: Mutable container to capture gates during forward pass\n- `turn_features_ref`: Carries turn-distance/turn-index tensors through forward hooks\n- Returns JSON with GAR curves, PPL, gate profiles\n\n**Critical Measurement Context**: All eval metrics **include active gating** (hooks modify residual connections)\n\n### 7. **Core Findings Summary** (memory.md & paper_framing.md)\n\n**Central Discovery (M017 corrected):**\n- **30× Training-Inference GAR Gap**: Models train GAR-ours to 0.48-0.50 on same-distribution (ultrachat) text but collapse to 0.016-0.025 on model-generated text\n- **Root Cause**: Exposure bias (teacher-forcing distribution shift), NOT gradient conflict or gating design\n- **PCGrad Proof (D028)**: Gradient direction conflict is inconsequential—consuming conflict after removal yields IID PPL 2.780 vs v7 2.784 (diff 0.004, no improvement)\n\n**Four-Way Ablation Results (D033, same protocol):**\n| Model | GAR-ours (IID) | GAR-ours (model-gen) | PPL (IID) |\n|-------|---|---|---|\n| ThreadGate (v7) | 0.5035 | 0.0157 | 2.78 |\n| UniformGate | 0.505 | 0.0149 | 2.78 |\n| LoRA-only | 0.498 | 0.0245 | 2.78 |\n| Baseline | 0.012 | — | — |\n\n**Key Mechanism Insights:**\n- NTP gradients dominate gate updates (7.5→14.7× magnitude ratio over GAR gradients)\n- 27/28 layers show gate conditioning reversal: turn1 gate < turn21 gate (Wilcoxon p<10⁻⁷), meaning gates suppress early turns where GAR is high\n- Gate attenuation at inference: mean gate = 0.93-0.98 (only 2-7% residual blocking), insufficient to shift attention patterns\n\n### 8. **Configuration** (config.py)\n\n```python\nMODEL_NAME = \"/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct\"\nLORA_RANK = 16\nGATE_HIDDEN_DIM = 64\nMAX_TURN_DISTANCE = 32\nTURN_EMBED_DIM = 16\nGAR_EPSILON = 0.001\nGAR_LAMBDA = 1.0  # Weight for GAR loss\nLEARNING_RATE = 2e-4\nBATCH_SIZE = 1\nGRADIENT_ACCUMULATION = 8\nMAX_SEQ_LEN = 2048\nNUM_EPOCHS = 3\nSEED = 42\nINIT_BIAS = 1.5  # Sets initial gate ≈ 0.82 via sigmoid\nGAR_LOSS_MODE = \"mse_target\"  # Only mode that converges\nGAR_TARGET = 0.5  # MSE target for mean GAR\nLAMBDA_GATE_DIV = 1.0  # Weight for gate diversity regularizer\nMIN_GATE_STD = 0.05  # Threshold for triggering gate_div loss\n```\n\n### 9. **Status & Current Training** (report.md)\n\n- v8b SS (scheduled sampling) training in progress on westd-20861 GPU\n- Early signal: TF_L_GAR drops 67%, but SS_L_GAR drops only 10% — direct exposure bias measurement\n- Plan: v8b eval → Plan_022 λ_GAR sensitivity → seed variations → Llama-3.1-8B validation\n\n---\n\n## Summary for Adding New Auxiliary Objectives\n\nTo add a new auxiliary objective to this framework, you'll need to:\n\n1. **Create differentiable loss function** in gar.py (following compute_gar_loss pattern with mode parameter)\n2. **Add command-line argument** in train_phase2.py for the new loss weight (λ parameter)\n3. **Integrate into loss computation** (line 274) as: `loss = l_ntp + λ_new * l_new + args.lambda_gate_div * l_gate_div`\n4. **Use GARMeasurer.measure()` context manager** to capture attention for metric computation\n5. **Log metrics** alongside l_ntp, l_gar, l_gate_div in training loop\n6. **Consider gradient conflict**: Expect NTP dominance (~10-15× magnitude) and potential direction conflicts unless using gradient surgery techniques\n7. **Evaluate on both IID and model-gen distributions** to measure exposure bias impact on new objective\n8. **Account for initialization**: init_bias=1.5 controls gate starting point; tune for new loss dynamics\n\nThe code architecture is well-structured for adding auxiliary objectives—the loss, gating, and measurement systems are cleanly separated with clear extension points."
      }
    ],
    "totalDurationMs": 56132,
    "totalTokens": 76715,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11019,
      "cache_read_input_tokens": 62361,
      "output_tokens": 3328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3328,
          "cache_read_input_tokens": 62361,
          "cache_creation_input_tokens": 11019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11019,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 1,
      "bashCount": 1,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "017e1f55-6ca9-432a-be9d-5452f8cbdf8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "leafUuid": "ba5d5f66-eb32-48f4-ad32-65b274bdb785",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Design cross-objective validation for exposure bias",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131"
}
```

---

### Assistant

_source line 16 · 2026-05-20T06:28:46.461Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information about the project. Let me analyze the candidates:

**Key constraints:**
1. The new objective must depend on multi-turn context (so exposure bias can break it)
2. Must be differentiable and trainable
3. Must show clear TF success / gen failure pattern
4. Must be sufficiently different from GAR to convince reviewers
5. Must be implementable in existing codebase quickly

Let me evaluate each candidate:

**Candidate A: Turn Consistency Loss**
- cos_sim(h_turn_i, h_turn_{i+1}) — measures hidden state similarity between adjacent turns


- This approach is straightforward and clearly depends on multi-turn context, with the intuition that coherent conversations should maintain correlated hidden states. However, the direction is ambiguous—should adjacent turns be similar or different given that users and assistants have different roles—and the signal could be noisy. I'd need to extract hidden states at turn boundaries using the existing turn detection utilities and hook into the model to capture them. Under teacher forcing, the hidden states would come from gold context and show consistent patterns, while under generation with drifted context, they'd diverge, which should expose the exposure bias gap.

**Candidate B: Position-aware Attention**
- This would encourage attention to a specific anchor rather than goal tokens, but it's too similar to GAR for independent validation.

**Candidate C: Turn-boundary NTP Loss**
- Adding extra NTP weight on turn boundary tokens is simple but feels too trivial—it's just reweighting the existing loss rather than introducing a genuinely new objective.

**Candidate D: Response Coherence Score**
- Using sentence embedding similarity is too complex and requires an external model that's hard to make differentiable.

**Candidate E: Other options from literature**

I'm leaning toward **Turn Consistency Loss (A)** with a more refined formulation. The core requirement is an objective that captures multi-turn properties and depends on contextual information across turns.

The idea is to measure cosine similarity of hidden representations at the last token of consecutive assistant turns. During teacher forcing, the model sees gold user messages between turns so the hidden state trajectory stays predictable, but during generation, it sees its own outputs and the representations drift.

What would really strengthen this is choosing something fundamentally different from GAR's attention-based approach—measuring hidden state space coherence at turn boundaries instead. This avoids the critique that I'm just measuring the same mechanism with a different target.

**Turn-boundary Representation Similarity (TRS)** might be the cleanest approach: comparing the hidden representations at each assistant turn's final token...

Actually, I think **Turn Consistency Loss** is more trainable and compelling. For adjacent assistant turns, I'd compute cosine similarity of their last-token hidden states and minimize the loss when they diverge. Under teacher forcing the model learns to maintain consistent representations, but under generation the distribution shift causes them to degrade—exactly the behavior I want to measure.

This approach is stronger academically because it uses a different mechanism than GAR (hidden states versus attention patterns), it's straightforward to implement, and turn coherence is well-established in dialogue literature. Most importantly, it's clearly vulnerable to exposure bias since it depends on multi-turn context.

Looking at what would make the strongest paper, I need the second objective to come from a different family than attention-based methods like GAR, be well-grounded in prior work, and have a clear measurable signal in both training and generation settings. A representation-based objective would give the paper two distinct methodological families to contrast.

Turn-boundary NTP loss is compelling because the model's ability to predict turn transitions degrades when it sees generated rather than gold context, creating a measurable loss difference—but it's really just the primary objective evaluated at specific positions rather than a true auxiliary objective, which might weaken the framing.

So I'm going with Turn-level Representation Coherence as my primary recommendation: I'll extract hidden states from the final token of each assistant turn, compute cosine similarity between consecutive turns' representations, and minimize the deviation from high coherence. The implementation is straightforward since turn boundaries are already detected and hidden states are available from the forward pass—just a small addition to the training loop. This approach targets a different mechanism than attention-based methods, has solid grounding in dialogue coherence research, and should show clear divergence between teacher-forced and generated settings with negligible computational overhead.

But I need to step back and make sure this actually fits the requirements. The task is asking for an auxiliary objective that succeeds under teacher-forced training but fails under generation—something that would train the model but expose the exposure bias problem. So I need to verify that Turn Consistency Loss actually exhibits this pattern: it should be trainable as a loss function, perform well when the model sees gold previous turns during training, but degrade when the model must rely on its own generated outputs during inference.

I should also check whether scheduled sampling is already being used in the v8b variant mentioned in the agent output, since that's a known exposure bias mitigation. If scheduled sampling already addresses the TCS gap, that would strengthen the argument that this is a general phenomenon worth studying.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba5d5f66-eb32-48f4-ad32-65b274bdb785",
  "isSidechain": false,
  "requestId": "req_011CbDM5DFfrPPtEs9dtyNFc",
  "type": "assistant",
  "uuid": "f446417c-522e-4d4e-bb9e-82515f724b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6YgdbPxohawYZWLkW43NW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 4304,
      "cache_read_input_tokens": 25262,
      "output_tokens": 3358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4304,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 933,
          "output_tokens": 3358,
          "cache_read_input_tokens": 25262,
          "cache_creation_input_tokens": 4304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4304
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

_source line 17 · 2026-05-20T06:29:16.772Z_

信息收集完毕。基于代码结构、现有实验和文献调研，分析如下：

---

## 推荐方案

**选择**: 候选 A — Turn-level Representation Coherence (TRC)

**理由**:
1. **机制正交**：GAR 测量 attention 空间的 goal-token 注意力分配；TRC 测量 hidden state 空间的 turn 间表示一致性。两个不同的特征空间，reviewer 无法用"同一机制的变体"来驳回。
2. **exposure bias 预测清晰**：TF 下模型看到 gold context，相邻 turn 的 hidden state 应收敛到一致的表示流形；gen 下 context 漂移，hidden state 轨迹发散——预期 TRC 指标同样出现 TF/gen gap。
3. **文献无先例**：调研结果确认，现有论文（UBARv2, TA&AT, Adaptive Bridge）只研究主 loss 的 exposure bias 退化，**没有人展示过 auxiliary objective 在 autoregressive generation 下坍塌**。两个不同族的 objective 同时坍塌，这个 claim 很强。
4. **实现极简**：`detect_turn_boundaries()` 已返回 `assistant_last_token_positions`，`model(..., output_hidden_states=True)` 已可获取 hidden states，新增代码约 30-40 行。

**具体公式**:
```
TRC_i = cos_sim(h^L_t_i, h^L_t_{i+1})   # L = final layer, t_i = assistant turn i 的 last token position
L_TRC = (mean(TRC) - τ)²                  # MSE target mode, τ=0.85 (初始值，可调)
```

用 MSE target 与 GAR 保持一致的 loss mode（v7 的成功经验）。

**实现方案**:

| 修改文件 | 内容 |
|---------|------|
| `src/train_phase2.py` | 添加 `--lambda_trc`, `--trc_target` 参数；loss 计算处提取 `outputs.hidden_states[-1]` 在 `assistant_last_positions` 处的向量，计算相邻 pair 的 cos_sim，MSE loss |
| `src/eval_model_gen.py` | 在 model-gen eval 中同样测量 TRC（hidden state cos_sim），与 GAR 并列报告 |
| `src/train_phase2.py` (logging) | 添加 `trc/train`, `trc/mean_cos_sim` 到 wandb log |

**关键实现细节**:
- 只需 `outputs.hidden_states[-1]`（最后一层），不需要全层；`output_hidden_states=True` 在现有代码中已有条件使用
- 至少需要 2 个 assistant turn 才能计算 TRC，单 turn 样本跳过此 loss
- 不需要 GARMeasurer 或 attention hooks——纯粹从 hidden states 计算

**预估成本**: ~3 GPU-h（与 v7 训练等价，TRC 计算开销可忽略；额外开销仅来自 `output_hidden_states=True` 的内存占用，Qwen2.5-7B 28 层约多 ~2GB）

**风险**:
- 相邻 turn 的 cos_sim 初始值可能已经很高（同一 conversation 的 hidden states 本身就相似），导致 TRC 的 TF/gen gap 不够显著 → 缓解：先做 baseline 测量，调整 target τ
- 如果 hidden state 空间的 exposure bias 效应弱于 attention 空间 → 这本身也是有价值的阴性结果（说明 exposure bias 的影响是 mechanism-dependent）

---

## 备选方案

**选择**: 候选 C 变体 — Turn-Boundary Prediction Loss (TBP)

**理由**: 不作为训练 loss，而是作为**诊断指标**。测量 turn boundary token 位置上的 NTP cross-entropy，比较 TF 和 gen 两种 context 下的差异。

优势：零实现成本（只需在 eval 时过滤位置）；能直观展示 exposure bias 在 turn 切换点最严重。

劣势：不是 trainable auxiliary objective，说服力弱于 TRC。但可以作为 paper 中的 supplementary analysis。

---

**建议执行顺序**:
1. 先在 v7 checkpoint 上做 **baseline TRC 测量**（TF 和 gen），确认 gap 存在
2. 确认 gap 后再加 TRC loss 训练新版本（v10）
3. 同时收集 TBP 诊断数据作为 supplementary

需要我开始实现 TRC 的 baseline 测量代码吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f446417c-522e-4d4e-bb9e-82515f724b9e",
  "isSidechain": false,
  "requestId": "req_011CbDM5DFfrPPtEs9dtyNFc",
  "type": "assistant",
  "uuid": "af7d1a5f-0b04-4ae3-a912-5a495f88794d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6YgdbPxohawYZWLkW43NW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 933,
      "cache_creation_input_tokens": 4304,
      "cache_read_input_tokens": 25262,
      "output_tokens": 3358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4304,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 933,
          "output_tokens": 3358,
          "cache_read_input_tokens": 25262,
          "cache_creation_input_tokens": 4304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4304
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

_source line 18_

```json
{
  "type": "last-prompt",
  "leafUuid": "af7d1a5f-0b04-4ae3-a912-5a495f88794d",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Design cross-objective validation for exposure bias",
  "sessionId": "dc81431a-1b02-4d85-8303-51e0fad97131"
}
```

---
