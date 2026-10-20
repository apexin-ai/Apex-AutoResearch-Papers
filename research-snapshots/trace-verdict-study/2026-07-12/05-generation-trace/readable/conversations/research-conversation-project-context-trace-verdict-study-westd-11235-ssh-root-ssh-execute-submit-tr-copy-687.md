# Research conversation: <project_context> # 项目: trace-verdict-study ## 运行环境 - 服务器名: westd-11235 - SSH 账户: root（调用 ssh_execute / submit_training_

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/370d5e56-c5ef-4a3c-bd85-5c5c85449231.jsonl`
- **Structured JSON:** [`2a9f2dfa1b2301ad9194.json`](../../sessions/2a/2a9f2dfa1b2301ad9194.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T14:09:35.855Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T14:09:35.855Z",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "content": "&lt;project_context>\n# 项目: trace-verdict-study\n\n## 运行环境\n- 服务器名: westd-11235\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/trace-verdict-study\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：将跨模型泛化文献整合到 literature_map.yaml\n\n### 背景\n之前的 cross-model-trace-lit Worker 找到了 5 篇关于跨模型 SFT 泛化的论文，但结果只留在 Worker 输出中，未写入 literature_map.yaml。需要整合。\n\n### 需要添加的论文（新增 cross-model-generalization category）\n\n1. **Yang et al. (NAACL 2024)** — \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\"\n   - authors: Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng Ann Heng, Wai Lam\n   - arxiv: 2403.09162\n   - role: method-component\n   - key_finding: SFT 后分类任务跨域正迁移，生成任务跨域负迁移\n\n2. **Dong et al. (ACL 2024)** — \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n   - authors: Guanting Dong, Hongyi Yuan, Keming Lu, et al.\n   - arxiv: 2310.05492\n   - role: method-component\n   - key_finding: 更大/更强 base model 在相同 SFT 数据量下性能更优。⚠️ 注意：DeepSeek-Coder-6.7B 预训练 **2T tokens**（不是 1.17T），Qwen 5.5T，比例 2.75x\n\n3. **Ye et al. (EMNLP 2025)** — \"Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels\"\n   - authors: Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan\n   - arxiv: 2509.16596\n   - role: background\n   - key_finding: SFT 中 90% 参数更新不贡献知识增强；知识掌握水平不同的训练数据导致 >12% 性能波动\n\n4. **Hanouneh et al. (arXiv 2025)** — \"From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT\"\n   - authors: Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov（⚠️ 不是 \"NNGPT Team\"）\n   - arxiv: 2605.03686\n   - role: background\n   - key_finding: DeepSeek-Coder-7B-Instruct LoRA 微调做代码分类 80% accuracy\n\n5. **Qwen2.5-Coder Technical Report**\n   - authors: Binyuan Hui, Jian Yang, et al. (Qwen Team)\n   - arxiv: 2409.12186\n   - role: background\n   - key_finding: Qwen2.5-Coder 5.5T tokens 预训练，HumanEval 92.7%\n\n### 步骤\n1. `read_project_file(file=\"literature_map.yaml\", max_chars=0)` 读取当前 map\n2. 在适当位置添加 `cross-model-generalization` category 及 5 篇论文\n3. `save_project_file` 保存\n\n### 注意\n- 保持 YAML 格式一致\n- DeepSeek 预训练数据是 **2T tokens**，不是 1.17T\n- NNGPT 作者是 **Hanouneh, Timofte, Ignatov**，不是 \"NNGPT Team\""
}
```

---

### Runtime record

_source line 2 · 2026-05-15T14:09:35.859Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T14:09:35.859Z",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-15T14:09:35.893Z_

&lt;project_context>
# 项目: trace-verdict-study

## 运行环境
- 服务器名: westd-11235
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/trace-verdict-study


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：将跨模型泛化文献整合到 literature_map.yaml

### 背景
之前的 cross-model-trace-lit Worker 找到了 5 篇关于跨模型 SFT 泛化的论文，但结果只留在 Worker 输出中，未写入 literature_map.yaml。需要整合。

### 需要添加的论文（新增 cross-model-generalization category）

1. **Yang et al. (NAACL 2024)** — "Unveiling the Generalization Power of Fine-Tuned Large Language Models"
   - authors: Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng Ann Heng, Wai Lam
   - arxiv: 2403.09162
   - role: method-component
   - key_finding: SFT 后分类任务跨域正迁移，生成任务跨域负迁移

2. **Dong et al. (ACL 2024)** — "How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition"
   - authors: Guanting Dong, Hongyi Yuan, Keming Lu, et al.
   - arxiv: 2310.05492
   - role: method-component
   - key_finding: 更大/更强 base model 在相同 SFT 数据量下性能更优。⚠️ 注意：DeepSeek-Coder-6.7B 预训练 **2T tokens**（不是 1.17T），Qwen 5.5T，比例 2.75x

3. **Ye et al. (EMNLP 2025)** — "Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels"
   - authors: Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan
   - arxiv: 2509.16596
   - role: background
   - key_finding: SFT 中 90% 参数更新不贡献知识增强；知识掌握水平不同的训练数据导致 >12% 性能波动

4. **Hanouneh et al. (arXiv 2025)** — "From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT"
   - authors: Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov（⚠️ 不是 "NNGPT Team"）
   - arxiv: 2605.03686
   - role: background
   - key_finding: DeepSeek-Coder-7B-Instruct LoRA 微调做代码分类 80% accuracy

5. **Qwen2.5-Coder Technical Report**
   - authors: Binyuan Hui, Jian Yang, et al. (Qwen Team)
   - arxiv: 2409.12186
   - role: background
   - key_finding: Qwen2.5-Coder 5.5T tokens 预训练，HumanEval 92.7%

### 步骤
1. `read_project_file(file="literature_map.yaml", max_chars=0)` 读取当前 map
2. 在适当位置添加 `cross-model-generalization` category 及 5 篇论文
3. `save_project_file` 保存

### 注意
- 保持 YAML 格式一致
- DeepSeek 预训练数据是 **2T tokens**，不是 1.17T
- NNGPT 作者是 **Hanouneh, Timofte, Ignatov**，不是 "NNGPT Team"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c0d844fc-b12d-4112-8dca-0bf81db49181",
  "type": "user",
  "uuid": "33a731a0-da2b-4faf-9ea9-ee9ba74c2c93",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T14:09:35.893Z_

```json
{
  "parentUuid": "33a731a0-da2b-4faf-9ea9-ee9ba74c2c93",
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
  "uuid": "1c4d16a7-a444-4dd8-bc9e-d96f9008560f",
  "timestamp": "2026-05-15T14:09:35.893Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T14:09:35.893Z_

```json
{
  "parentUuid": "1c4d16a7-a444-4dd8-bc9e-d96f9008560f",
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
  "uuid": "a8a11f6c-b18a-46c6-a0d4-3ba15d0d1c41",
  "timestamp": "2026-05-15T14:09:35.893Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T14:09:35.893Z_

```json
{
  "parentUuid": "a8a11f6c-b18a-46c6-a0d4-3ba15d0d1c41",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d0160bf4-92bb-4c99-89df-d3c2b87e9f12",
  "timestamp": "2026-05-15T14:09:35.893Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
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
  "aiTitle": "Integrate cross-model generalization literature into literature_map.yaml",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---

### Assistant

_source line 8 · 2026-05-15T14:09:38.906Z_

我先读取当前的 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0160bf4-92bb-4c99-89df-d3c2b87e9f12",
  "isSidechain": false,
  "requestId": "req_011Cb4VEWQwjuVrE8TrhB41q",
  "type": "assistant",
  "uuid": "2fa4b8db-1100-4ddb-9f8d-9d29e4c6dc6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SunL6x8pcxztGBoEBixTed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11763,
      "cache_read_input_tokens": 11841,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11763
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

_source line 9 · 2026-05-15T14:09:39.654Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017Gg3F7qB4GzjWzryaFrrrK`</summary>

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
  "parentUuid": "2fa4b8db-1100-4ddb-9f8d-9d29e4c6dc6e",
  "isSidechain": false,
  "requestId": "req_011Cb4VEWQwjuVrE8TrhB41q",
  "type": "assistant",
  "uuid": "bd9bf1d3-06f0-4f0d-8ef2-31ad81ed1335",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SunL6x8pcxztGBoEBixTed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11763,
      "cache_read_input_tokens": 11841,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11763
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

_source line 10 · 2026-05-15T14:09:39.661Z_

<details><summary>↩ Tool result · `toolu_017Gg3F7qB4GzjWzryaFrrrK`</summary>

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
  "parentUuid": "bd9bf1d3-06f0-4f0d-8ef2-31ad81ed1335",
  "isSidechain": false,
  "promptId": "c0d844fc-b12d-4112-8dca-0bf81db49181",
  "type": "user",
  "uuid": "0f94753c-d148-450c-9ebf-1e33bc25182c",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "bd9bf1d3-06f0-4f0d-8ef2-31ad81ed1335",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T14:09:43.738Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KGRQ56gB5ruTvt2zR2Gkaq`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f94753c-d148-450c-9ebf-1e33bc25182c",
  "isSidechain": false,
  "requestId": "req_011Cb4VEnjxShNgXQ2zGuoUQ",
  "type": "assistant",
  "uuid": "26ae3e5e-ae46-4b32-8b19-63368bb39d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MfmeiF4AckTTxJzubVtz9L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 23604,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 23604,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
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

_source line 12 · 2026-05-15T14:09:43.753Z_

<details><summary>↩ Tool result · `toolu_01KGRQ56gB5ruTvt2zR2Gkaq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml\", \"content\": \"categories:\\n  execution-trace-llm:\\n    description: \\\"Execution trace 辅助 LLM 代码理解/调试/推理\\\"\\n    papers:\\n      - title: \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\"\\n        authors: \\\"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        role: method-component\\n        key_finding: \\\"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\\\"\\n        metrics:\\n          mbpp_fix_rate_improvement: \\\"+26.1%\\\"\\n          humaneval_fix_rate_improvement: \\\"+14.3%\\\"\\n\\n      - title: \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\\\"\\n        authors: \\\"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\\\"\\n        year: 2025\\n        venue: \\\"Findings of EMNLP 2025\\\"\\n        arxiv_id: \\\"2509.11686\\\"\\n        role: direct-competitor\\n        key_finding: \\\"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Code Execution as Grounded Supervision for LLM Reasoning\\\"\\n        authors: \\\"Dongwon Jung, Wenxuan Zhou, Muhao Chen\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2506.10343\\\"\\n        role: method-component\\n        key_finding: \\\"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\\\"\\n        authors: \\\"Lorenzo Ferrando, Nicola Ferraro, et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2503.05703\\\"\\n        arxiv_id: \\\"2503.05703\\\"\\n        role: method-component\\n        key_finding: \\\"对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。\\\"\\n        metrics:\\n          cruxeval_accuracy: \\\"~80%\\\"\\n          mbpp_accuracy: \\\"~80%\\\"\\n\\n      - title: \\\"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation\\\"\\n        authors: \\\"Mohammad Abdollahi, Khandaker Rifah Tasnia, Soumit Kanti Saha, Jinqiu Yang, Song Wang, Hadi Hemmati\\\"\\n        year: 2025\\n        venue: \\\"arXiv\\\"\\n        arxiv_id: \\\"2512.00215\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)\\\"\\n        authors: \\\"Junkai Chen et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2403.16437\\\"\\n        role: evaluation\\n        key_finding: \\\"REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。\\\"\\n        metrics:\\n          avg_accuracy: \\\"44.4%\\\"\\n          avg_ic_score: \\\"10.3\\\"\\n\\n      - title: \\\"CodeMind: Evaluating Large Language Models for Code Reasoning\\\"\\n        authors: \\\"Changshu Liu et al. (UIUC)\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2402.09664\\\"\\n        role: evaluation\\n        key_finding: \\\"评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\"\\n        authors: \\\"Ruiyang Xu et al. (HKUST)\\\"\\n        year: 2025\\n        venue: \\\"ACL 2025\\\"\\n        arxiv_id: \\\"2408.13001\\\"\\n        role: evaluation\\n        key_finding: \\\"将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。\\\"\\n        metrics:\\n          languages: 19\\n          cross_lang_max_pass1: \\\"34.4%\\\"\\n\\n  code-verdict:\\n    description: \\\"LLM 判断代码 pass/fail、正确性分类、mutation testing\\\"\\n    papers:\\n      - title: \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\"\\n        authors: \\\"iSEngLab (Nanjing University)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\\\"\\n        metrics:\\n          accuracy: \\\"79.7%\\\"\\n          recall: \\\"83.2%\\\"\\n          f1_improvement_from_finetuning: \\\"+10.22%\\\"\\n\\n      - title: \\\"LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\"\\n        authors: \\\"Xin Zhou et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。\\\"\\n        metrics:\\n          accuracy: \\\"84.4%\\\"\\n          f1: \\\"86.5%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment\\\"\\n        authors: \\\"Zhenyu Yang, Jingwen Wu, Zhen Yang, Zhongxing Yu\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2505.02629\\\"\\n        arxiv_id: \\\"2505.02629\\\"\\n        role: direct-competitor\\n        key_finding: \\\"提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。\\\"\\n        metrics:\\n          accuracy_improvement: \\\"+3.1-7.5%\\\"\\n          f1_improvement: \\\"+3.0-7.1%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Calibration and Correctness of Language Models for Code\\\"\\n        authors: \\\"Claudio Spiess, David Gros, et al.\\\"\\n        year: 2025\\n        venue: \\\"ICSE 2025\\\"\\n        arxiv_id: \\\"2402.02047\\\"\\n        role: evaluation\\n        key_finding: \\\"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n        authors: \\\"Christopher Foster et al. (Meta)\\\"\\n        year: 2025\\n        venue: \\\"FSE 2025 (Industry)\\\"\\n        arxiv_id: \\\"2501.12862\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\\\"\\n        metrics:\\n          precision: \\\"0.95\\\"\\n          recall: \\\"0.96\\\"\\n          classes_evaluated: \\\"10795\\\"\\n          test_acceptance_rate: \\\"73%\\\"\\n\\n      - title: \\\"FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning\\\"\\n        authors: \\\"Ratnadira Widyasari et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"SANER 2024\\\"\\n        role: background\\n        key_finding: \\\"融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。\\\"\\n        metrics:\\n          top1_improvement_over_baseline: \\\"+32.3%\\\"\\n          top1_improvement_over_sbfl: \\\"+68.4%\\\"\\n\\n  trace-compression:\\n    description: \\\"Execution trace 的压缩、摘要、抽象方法\\\"\\n    papers:\\n      - title: \\\"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\\\"\\n        authors: \\\"Aashish Yadavally, Yi Li, Tien Nguyen\\\"\\n        year: 2024\\n        venue: \\\"FSE 2024\\\"\\n        role: method-component\\n        key_finding: \\\"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\\\"\\n        metrics:\\n          exact_match: \\\"81.31%\\\"\\n          rouge_lcs: \\\"0.954\\\"\\n          fault_localization_accuracy: \\\"63.88%\\\"\\n\\n      - title: \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\"\\n        authors: \\\"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\\\"\\n        year: 2025\\n        venue: \\\"KnowledgeNLP Workshop @ ACL 2025\\\"\\n        arxiv_id: \\\"2505.04441\\\"\\n        role: background\\n        key_finding: \\\"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\\\"\\n        authors: \\\"Koshi Eguchi, Takuya Akiba\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025 Workshop PRAL\\\"\\n        openreview_id: \\\"pFyBdPyOCQ\\\"\\n        role: method-component\\n        key_finding: \\\"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\\\"\\n        metrics:\\n          cruxeval_o: \\\"70.0%\\\"\\n          livecodebench_execution: \\\"88.3%\\\"\\n\\n      - title: \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\"\\n        authors: \\\"Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu\\\"\\n        year: 2026\\n        venue: \\\"ICSE 2026\\\"\\n        arxiv_id: \\\"2602.06875\\\"\\n        verified: true\\n        role: background\\n        key_finding: \\\"在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。\\\"\\n        metrics:\\n          pass_at_1_improvement: \\\"+34.43%\\\"\\n\\n      - title: \\\"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\\\"\\n        authors: \\\"Jiaqing Wu, Tong Wu, Manqing Zhang, Yunwei Dong, Bo Shen\\\"\\n        year: 2026\\n        venue: \\\"arXiv 2604.02647\\\"\\n        arxiv_id: \\\"2604.02647\\\"\\n        verified: true\\n        role: background\\n        key_finding: \\\"Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。\\\"\\n        metrics:\\n          defects_fixed: \\\"392\\\"\\n\\n      - title: \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\"\\n        authors: \\\"Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, Shuiguang Deng\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2510.18327\\\"\\n        arxiv_id: \\\"2510.18327\\\"\\n        role: background\\n        key_finding: \\\"首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。\\\"\\n        metrics:\\n          repair_accuracy_improvement: \\\"+5.10-60.37%\\\"\\n\\n      - title: \\\"MGDebugger: From Code to Correctness via Hierarchical Debugging\\\"\\n        authors: \\\"Yuling Shi et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2410.01215\\\"\\n        role: background\\n        key_finding: \\\"层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。\\\"\\n        metrics:\\n          humaneval_accuracy: \\\"94.5%\\\"\\n          humaneval_fix_accuracy: \\\"97.6%\\\"\\n\\n  debugging-agents:\\n    description: \\\"LLM 多智能体调试框架\\\"\\n    papers:\\n      - title: \\\"UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging\\\"\\n        authors: \\\"Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2404.17153\\\"\\n        role: background\\n        key_finding: \\\"三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。\\\"\\n        metrics:\\n          defects4j_improvement: \\\"1.25-2.56x\\\"\\n\\n      - title: \\\"Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach\\\"\\n        authors: \\\"Xuanming Zhang, Yuxuan Chen, Yuan Yuan, Minlie Huang\\\"\\n        year: 2025\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv_id: \\\"2410.06949\\\"\\n        role: background\\n        key_finding: \\\"5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。\\\"\\n        metrics:\\n          exception_handling_precision_improvement: \\\"+37%\\\"\\n\\n  sft-classification:\\n    description: \\\"用 SFT 做分类任务的方法论和 findings\\\"\\n    papers:\\n      - title: \\\"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\\\"\\n        authors: \\\"Amirhossein Yousefiramandi, Ciaran Cooney\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2512.12677\\\"\\n        arxiv_id: \\\"2512.12677\\\"\\n        role: method-component\\n        key_finding: \\\"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\\\"\\n        metrics: {}\\n\\n      - title: \\\"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\\\"\\n        authors: \\\"Rohan Deb, Kiran Koshy Thekumparampil, Kousha Kalantari, Gaurush Hiranandani, Shoham Sabach, Branislav Kveton\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025\\\"\\n        arxiv_id: \\\"2505.14826\\\"\\n        role: background\\n        key_finding: \\\"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\\\"\\n        authors: \\\"Martin Juan Jose Bucher, Marco Martini\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2406.08660\\\"\\n        role: background\\n        key_finding: \\\"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\\\"\\n        metrics: {}\\n\\nmeta:\\n  last_updated: \\\"2026-05-15\\\"\\n  total_papers: 26\\n  search_scope: \\\"2024-2026, top ML/NLP/SE venues\\\"\\n  scan_date: \\\"2026-05-15\\\"\\n  scan_queries: 16\\n  key_gaps:\\n    - \\\"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\\\"\\n    - \\\"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\\\"\\n    - \\\"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\\\"\\n    - \\\"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\\\"\\n    - \\\"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\\\"\\n\", \"total_chars\": 14225, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26ae3e5e-ae46-4b32-8b19-63368bb39d0e",
  "isSidechain": false,
  "promptId": "c0d844fc-b12d-4112-8dca-0bf81db49181",
  "type": "user",
  "uuid": "e79fff80-fbf6-4f0f-af3b-45e22327c28d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml\\\", \\\"content\\\": \\\"categories:\\\\n  execution-trace-llm:\\\\n    description: \\\\\\\"Execution trace 辅助 LLM 代码理解/调试/推理\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\\\\\"\\\\n        authors: \\\\\\\"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\\\\\\\"\\\\n        metrics:\\\\n          mbpp_fix_rate_improvement: \\\\\\\"+26.1%\\\\\\\"\\\\n          humaneval_fix_rate_improvement: \\\\\\\"+14.3%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\\\\\\\"\\\\n        authors: \\\\\\\"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"Findings of EMNLP 2025\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2509.11686\\\\\\\"\\\\n        role: direct-competitor\\\\n        key_finding: \\\\\\\"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Code Execution as Grounded Supervision for LLM Reasoning\\\\\\\"\\\\n        authors: \\\\\\\"Dongwon Jung, Wenxuan Zhou, Muhao Chen\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2506.10343\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\\\\\\\"\\\\n        authors: \\\\\\\"Lorenzo Ferrando, Nicola Ferraro, et al.\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv 2503.05703\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2503.05703\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。\\\\\\\"\\\\n        metrics:\\\\n          cruxeval_accuracy: \\\\\\\"~80%\\\\\\\"\\\\n          mbpp_accuracy: \\\\\\\"~80%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation\\\\\\\"\\\\n        authors: \\\\\\\"Mohammad Abdollahi, Khandaker Rifah Tasnia, Soumit Kanti Saha, Jinqiu Yang, Song Wang, Hadi Hemmati\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2512.00215\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)\\\\\\\"\\\\n        authors: \\\\\\\"Junkai Chen et al.\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"arXiv 2403.16437\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。\\\\\\\"\\\\n        metrics:\\\\n          avg_accuracy: \\\\\\\"44.4%\\\\\\\"\\\\n          avg_ic_score: \\\\\\\"10.3\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"CodeMind: Evaluating Large Language Models for Code Reasoning\\\\\\\"\\\\n        authors: \\\\\\\"Changshu Liu et al. (UIUC)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"arXiv 2402.09664\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\\\\\"\\\\n        authors: \\\\\\\"Ruiyang Xu et al. (HKUST)\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ACL 2025\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2408.13001\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。\\\\\\\"\\\\n        metrics:\\\\n          languages: 19\\\\n          cross_lang_max_pass1: \\\\\\\"34.4%\\\\\\\"\\\\n\\\\n  code-verdict:\\\\n    description: \\\\\\\"LLM 判断代码 pass/fail、正确性分类、mutation testing\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\\\\\"\\\\n        authors: \\\\\\\"iSEngLab (Nanjing University)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"IEEE TSE 2024\\\\\\\"\\\\n        role: direct-competitor\\\\n        key_finding: \\\\\\\"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\\\\\\\"\\\\n        metrics:\\\\n          accuracy: \\\\\\\"79.7%\\\\\\\"\\\\n          recall: \\\\\\\"83.2%\\\\\\\"\\\\n          f1_improvement_from_finetuning: \\\\\\\"+10.22%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\\\\\"\\\\n        authors: \\\\\\\"Xin Zhou et al. (SMU)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"IEEE TSE 2024\\\\\\\"\\\\n        role: direct-competitor\\\\n        key_finding: \\\\\\\"用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。\\\\\\\"\\\\n        metrics:\\\\n          accuracy: \\\\\\\"84.4%\\\\\\\"\\\\n          f1: \\\\\\\"86.5%\\\\\\\"\\\\n        novelty_threat: medium\\\\n\\\\n      - title: \\\\\\\"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment\\\\\\\"\\\\n        authors: \\\\\\\"Zhenyu Yang, Jingwen Wu, Zhen Yang, Zhongxing Yu\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv 2505.02629\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2505.02629\\\\\\\"\\\\n        role: direct-competitor\\\\n        key_finding: \\\\\\\"提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。\\\\\\\"\\\\n        metrics:\\\\n          accuracy_improvement: \\\\\\\"+3.1-7.5%\\\\\\\"\\\\n          f1_improvement: \\\\\\\"+3.0-7.1%\\\\\\\"\\\\n        novelty_threat: medium\\\\n\\\\n      - title: \\\\\\\"Calibration and Correctness of Language Models for Code\\\\\\\"\\\\n        authors: \\\\\\\"Claudio Spiess, David Gros, et al.\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ICSE 2025\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2402.02047\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Mutation-Guided LLM-based Test Generation at Meta\\\\\\\"\\\\n        authors: \\\\\\\"Christopher Foster et al. (Meta)\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"FSE 2025 (Industry)\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2501.12862\\\\\\\"\\\\n        role: evaluation\\\\n        key_finding: \\\\\\\"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\\\\\\\"\\\\n        metrics:\\\\n          precision: \\\\\\\"0.95\\\\\\\"\\\\n          recall: \\\\\\\"0.96\\\\\\\"\\\\n          classes_evaluated: \\\\\\\"10795\\\\\\\"\\\\n          test_acceptance_rate: \\\\\\\"73%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning\\\\\\\"\\\\n        authors: \\\\\\\"Ratnadira Widyasari et al. (SMU)\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"SANER 2024\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。\\\\\\\"\\\\n        metrics:\\\\n          top1_improvement_over_baseline: \\\\\\\"+32.3%\\\\\\\"\\\\n          top1_improvement_over_sbfl: \\\\\\\"+68.4%\\\\\\\"\\\\n\\\\n  trace-compression:\\\\n    description: \\\\\\\"Execution trace 的压缩、摘要、抽象方法\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\\\\\\\"\\\\n        authors: \\\\\\\"Aashish Yadavally, Yi Li, Tien Nguyen\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"FSE 2024\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\\\\\\\"\\\\n        metrics:\\\\n          exact_match: \\\\\\\"81.31%\\\\\\\"\\\\n          rouge_lcs: \\\\\\\"0.954\\\\\\\"\\\\n          fault_localization_accuracy: \\\\\\\"63.88%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\\\\\"\\\\n        authors: \\\\\\\"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"KnowledgeNLP Workshop @ ACL 2025\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2505.04441\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\\\\\\\"\\\\n        authors: \\\\\\\"Koshi Eguchi, Takuya Akiba\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ICML 2025 Workshop PRAL\\\\\\\"\\\\n        openreview_id: \\\\\\\"pFyBdPyOCQ\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\\\\\\\"\\\\n        metrics:\\\\n          cruxeval_o: \\\\\\\"70.0%\\\\\\\"\\\\n          livecodebench_execution: \\\\\\\"88.3%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\\\\\"\\\\n        authors: \\\\\\\"Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu\\\\\\\"\\\\n        year: 2026\\\\n        venue: \\\\\\\"ICSE 2026\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2602.06875\\\\\\\"\\\\n        verified: true\\\\n        role: background\\\\n        key_finding: \\\\\\\"在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。\\\\\\\"\\\\n        metrics:\\\\n          pass_at_1_improvement: \\\\\\\"+34.43%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\\\\\\\"\\\\n        authors: \\\\\\\"Jiaqing Wu, Tong Wu, Manqing Zhang, Yunwei Dong, Bo Shen\\\\\\\"\\\\n        year: 2026\\\\n        venue: \\\\\\\"arXiv 2604.02647\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2604.02647\\\\\\\"\\\\n        verified: true\\\\n        role: background\\\\n        key_finding: \\\\\\\"Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。\\\\\\\"\\\\n        metrics:\\\\n          defects_fixed: \\\\\\\"392\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\\\\\"\\\\n        authors: \\\\\\\"Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, Shuiguang Deng\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv 2510.18327\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2510.18327\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。\\\\\\\"\\\\n        metrics:\\\\n          repair_accuracy_improvement: \\\\\\\"+5.10-60.37%\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"MGDebugger: From Code to Correctness via Hierarchical Debugging\\\\\\\"\\\\n        authors: \\\\\\\"Yuling Shi et al.\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"arXiv 2410.01215\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。\\\\\\\"\\\\n        metrics:\\\\n          humaneval_accuracy: \\\\\\\"94.5%\\\\\\\"\\\\n          humaneval_fix_accuracy: \\\\\\\"97.6%\\\\\\\"\\\\n\\\\n  debugging-agents:\\\\n    description: \\\\\\\"LLM 多智能体调试框架\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging\\\\\\\"\\\\n        authors: \\\\\\\"Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2404.17153\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。\\\\\\\"\\\\n        metrics:\\\\n          defects4j_improvement: \\\\\\\"1.25-2.56x\\\\\\\"\\\\n\\\\n      - title: \\\\\\\"Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach\\\\\\\"\\\\n        authors: \\\\\\\"Xuanming Zhang, Yuxuan Chen, Yuan Yuan, Minlie Huang\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2410.06949\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。\\\\\\\"\\\\n        metrics:\\\\n          exception_handling_precision_improvement: \\\\\\\"+37%\\\\\\\"\\\\n\\\\n  sft-classification:\\\\n    description: \\\\\\\"用 SFT 做分类任务的方法论和 findings\\\\\\\"\\\\n    papers:\\\\n      - title: \\\\\\\"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\\\\\\\"\\\\n        authors: \\\\\\\"Amirhossein Yousefiramandi, Ciaran Cooney\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"arXiv 2512.12677\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2512.12677\\\\\\\"\\\\n        role: method-component\\\\n        key_finding: \\\\\\\"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\\\\\\\"\\\\n        authors: \\\\\\\"Rohan Deb, Kiran Koshy Thekumparampil, Kousha Kalantari, Gaurush Hiranandani, Shoham Sabach, Branislav Kveton\\\\\\\"\\\\n        year: 2025\\\\n        venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n        arxiv_id: \\\\\\\"2505.14826\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\n      - title: \\\\\\\"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\\\\\\\"\\\\n        authors: \\\\\\\"Martin Juan Jose Bucher, Marco Martini\\\\\\\"\\\\n        year: 2024\\\\n        venue: \\\\\\\"arXiv 2406.08660\\\\\\\"\\\\n        role: background\\\\n        key_finding: \\\\\\\"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\\\\\\\"\\\\n        metrics: {}\\\\n\\\\nmeta:\\\\n  last_updated: \\\\\\\"2026-05-15\\\\\\\"\\\\n  total_papers: 26\\\\n  search_scope: \\\\\\\"2024-2026, top ML/NLP/SE venues\\\\\\\"\\\\n  scan_date: \\\\\\\"2026-05-15\\\\\\\"\\\\n  scan_queries: 16\\\\n  key_gaps:\\\\n    - \\\\\\\"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\\\\\\\"\\\\n    - \\\\\\\"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\\\\\\\"\\\\n    - \\\\\\\"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\\\\\\\"\\\\n    - \\\\\\\"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\\\\\\\"\\\\n    - \\\\\\\"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 14225, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml\", \"content\": \"categories:\\n  execution-trace-llm:\\n    description: \\\"Execution trace 辅助 LLM 代码理解/调试/推理\\\"\\n    papers:\\n      - title: \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\"\\n        authors: \\\"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        role: method-component\\n        key_finding: \\\"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\\\"\\n        metrics:\\n          mbpp_fix_rate_improvement: \\\"+26.1%\\\"\\n          humaneval_fix_rate_improvement: \\\"+14.3%\\\"\\n\\n      - title: \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\\\"\\n        authors: \\\"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\\\"\\n        year: 2025\\n        venue: \\\"Findings of EMNLP 2025\\\"\\n        arxiv_id: \\\"2509.11686\\\"\\n        role: direct-competitor\\n        key_finding: \\\"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Code Execution as Grounded Supervision for LLM Reasoning\\\"\\n        authors: \\\"Dongwon Jung, Wenxuan Zhou, Muhao Chen\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2506.10343\\\"\\n        role: method-component\\n        key_finding: \\\"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\\\"\\n        authors: \\\"Lorenzo Ferrando, Nicola Ferraro, et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2503.05703\\\"\\n        arxiv_id: \\\"2503.05703\\\"\\n        role: method-component\\n        key_finding: \\\"对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。\\\"\\n        metrics:\\n          cruxeval_accuracy: \\\"~80%\\\"\\n          mbpp_accuracy: \\\"~80%\\\"\\n\\n      - title: \\\"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation\\\"\\n        authors: \\\"Mohammad Abdollahi, Khandaker Rifah Tasnia, Soumit Kanti Saha, Jinqiu Yang, Song Wang, Hadi Hemmati\\\"\\n        year: 2025\\n        venue: \\\"arXiv\\\"\\n        arxiv_id: \\\"2512.00215\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)\\\"\\n        authors: \\\"Junkai Chen et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2403.16437\\\"\\n        role: evaluation\\n        key_finding: \\\"REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。\\\"\\n        metrics:\\n          avg_accuracy: \\\"44.4%\\\"\\n          avg_ic_score: \\\"10.3\\\"\\n\\n      - title: \\\"CodeMind: Evaluating Large Language Models for Code Reasoning\\\"\\n        authors: \\\"Changshu Liu et al. (UIUC)\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2402.09664\\\"\\n        role: evaluation\\n        key_finding: \\\"评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\"\\n        authors: \\\"Ruiyang Xu et al. (HKUST)\\\"\\n        year: 2025\\n        venue: \\\"ACL 2025\\\"\\n        arxiv_id: \\\"2408.13001\\\"\\n        role: evaluation\\n        key_finding: \\\"将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。\\\"\\n        metrics:\\n          languages: 19\\n          cross_lang_max_pass1: \\\"34.4%\\\"\\n\\n  code-verdict:\\n    description: \\\"LLM 判断代码 pass/fail、正确性分类、mutation testing\\\"\\n    papers:\\n      - title: \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\"\\n        authors: \\\"iSEngLab (Nanjing University)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\\\"\\n        metrics:\\n          accuracy: \\\"79.7%\\\"\\n          recall: \\\"83.2%\\\"\\n          f1_improvement_from_finetuning: \\\"+10.22%\\\"\\n\\n      - title: \\\"LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\"\\n        authors: \\\"Xin Zhou et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。\\\"\\n        metrics:\\n          accuracy: \\\"84.4%\\\"\\n          f1: \\\"86.5%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment\\\"\\n        authors: \\\"Zhenyu Yang, Jingwen Wu, Zhen Yang, Zhongxing Yu\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2505.02629\\\"\\n        arxiv_id: \\\"2505.02629\\\"\\n        role: direct-competitor\\n        key_finding: \\\"提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。\\\"\\n        metrics:\\n          accuracy_improvement: \\\"+3.1-7.5%\\\"\\n          f1_improvement: \\\"+3.0-7.1%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Calibration and Correctness of Language Models for Code\\\"\\n        authors: \\\"Claudio Spiess, David Gros, et al.\\\"\\n        year: 2025\\n        venue: \\\"ICSE 2025\\\"\\n        arxiv_id: \\\"2402.02047\\\"\\n        role: evaluation\\n        key_finding: \\\"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n        authors: \\\"Christopher Foster et al. (Meta)\\\"\\n        year: 2025\\n        venue: \\\"FSE 2025 (Industry)\\\"\\n        arxiv_id: \\\"2501.12862\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\\\"\\n        metrics:\\n          precision: \\\"0.95\\\"\\n          recall: \\\"0.96\\\"\\n          classes_evaluated: \\\"10795\\\"\\n          test_acceptance_rate: \\\"73%\\\"\\n\\n      - title: \\\"FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning\\\"\\n        authors: \\\"Ratnadira Widyasari et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"SANER 2024\\\"\\n        role: background\\n        key_finding: \\\"融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。\\\"\\n        metrics:\\n          top1_improvement_over_baseline: \\\"+32.3%\\\"\\n          top1_improvement_over_sbfl: \\\"+68.4%\\\"\\n\\n  trace-compression:\\n    description: \\\"Execution trace 的压缩、摘要、抽象方法\\\"\\n    papers:\\n      - title: \\\"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\\\"\\n        authors: \\\"Aashish Yadavally, Yi Li, Tien Nguyen\\\"\\n        year: 2024\\n        venue: \\\"FSE 2024\\\"\\n        role: method-component\\n        key_finding: \\\"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\\\"\\n        metrics:\\n          exact_match: \\\"81.31%\\\"\\n          rouge_lcs: \\\"0.954\\\"\\n          fault_localization_accuracy: \\\"63.88%\\\"\\n\\n      - title: \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\"\\n        authors: \\\"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\\\"\\n        year: 2025\\n        venue: \\\"KnowledgeNLP Workshop @ ACL 2025\\\"\\n        arxiv_id: \\\"2505.04441\\\"\\n        role: background\\n        key_finding: \\\"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\\\"\\n        authors: \\\"Koshi Eguchi, Takuya Akiba\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025 Workshop PRAL\\\"\\n        openreview_id: \\\"pFyBdPyOCQ\\\"\\n        role: method-component\\n        key_finding: \\\"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\\\"\\n        metrics:\\n          cruxeval_o: \\\"70.0%\\\"\\n          livecodebench_execution: \\\"88.3%\\\"\\n\\n      - title: \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\"\\n        authors: \\\"Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu\\\"\\n        year: 2026\\n        venue: \\\"ICSE 2026\\\"\\n        arxiv_id: \\\"2602.06875\\\"\\n        verified: true\\n        role: background\\n        key_finding: \\\"在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。\\\"\\n        metrics:\\n          pass_at_1_improvement: \\\"+34.43%\\\"\\n\\n      - title: \\\"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\\\"\\n        authors: \\\"Jiaqing Wu, Tong Wu, Manqing Zhang, Yunwei Dong, Bo Shen\\\"\\n        year: 2026\\n        venue: \\\"arXiv 2604.02647\\\"\\n        arxiv_id: \\\"2604.02647\\\"\\n        verified: true\\n        role: background\\n        key_finding: \\\"Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。\\\"\\n        metrics:\\n          defects_fixed: \\\"392\\\"\\n\\n      - title: \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\"\\n        authors: \\\"Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, Shuiguang Deng\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2510.18327\\\"\\n        arxiv_id: \\\"2510.18327\\\"\\n        role: background\\n        key_finding: \\\"首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。\\\"\\n        metrics:\\n          repair_accuracy_improvement: \\\"+5.10-60.37%\\\"\\n\\n      - title: \\\"MGDebugger: From Code to Correctness via Hierarchical Debugging\\\"\\n        authors: \\\"Yuling Shi et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2410.01215\\\"\\n        role: background\\n        key_finding: \\\"层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。\\\"\\n        metrics:\\n          humaneval_accuracy: \\\"94.5%\\\"\\n          humaneval_fix_accuracy: \\\"97.6%\\\"\\n\\n  debugging-agents:\\n    description: \\\"LLM 多智能体调试框架\\\"\\n    papers:\\n      - title: \\\"UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging\\\"\\n        authors: \\\"Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2404.17153\\\"\\n        role: background\\n        key_finding: \\\"三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。\\\"\\n        metrics:\\n          defects4j_improvement: \\\"1.25-2.56x\\\"\\n\\n      - title: \\\"Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach\\\"\\n        authors: \\\"Xuanming Zhang, Yuxuan Chen, Yuan Yuan, Minlie Huang\\\"\\n        year: 2025\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv_id: \\\"2410.06949\\\"\\n        role: background\\n        key_finding: \\\"5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。\\\"\\n        metrics:\\n          exception_handling_precision_improvement: \\\"+37%\\\"\\n\\n  sft-classification:\\n    description: \\\"用 SFT 做分类任务的方法论和 findings\\\"\\n    papers:\\n      - title: \\\"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\\\"\\n        authors: \\\"Amirhossein Yousefiramandi, Ciaran Cooney\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2512.12677\\\"\\n        arxiv_id: \\\"2512.12677\\\"\\n        role: method-component\\n        key_finding: \\\"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\\\"\\n        metrics: {}\\n\\n      - title: \\\"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\\\"\\n        authors: \\\"Rohan Deb, Kiran Koshy Thekumparampil, Kousha Kalantari, Gaurush Hiranandani, Shoham Sabach, Branislav Kveton\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025\\\"\\n        arxiv_id: \\\"2505.14826\\\"\\n        role: background\\n        key_finding: \\\"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\\\"\\n        authors: \\\"Martin Juan Jose Bucher, Marco Martini\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2406.08660\\\"\\n        role: background\\n        key_finding: \\\"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\\\"\\n        metrics: {}\\n\\nmeta:\\n  last_updated: \\\"2026-05-15\\\"\\n  total_papers: 26\\n  search_scope: \\\"2024-2026, top ML/NLP/SE venues\\\"\\n  scan_date: \\\"2026-05-15\\\"\\n  scan_queries: 16\\n  key_gaps:\\n    - \\\"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\\\"\\n    - \\\"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\\\"\\n    - \\\"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\\\"\\n    - \\\"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\\\"\\n    - \\\"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\\\"\\n\", \"total_chars\": 14225, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "26ae3e5e-ae46-4b32-8b19-63368bb39d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
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
  "leafUuid": "e79fff80-fbf6-4f0f-af3b-45e22327c28d",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Integrate cross-model generalization literature into literature_map.yaml",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---

### Assistant

_source line 15 · 2026-05-15T14:09:50.289Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full content. I need to add a `cross-model-generalization` category with 5 papers. Let me prepare the updated YAML and save it.

Let me read the file directly to edit it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e79fff80-fbf6-4f0f-af3b-45e22327c28d",
  "isSidechain": false,
  "requestId": "req_011Cb4VF6Ch77RFwedY9nupE",
  "type": "assistant",
  "uuid": "7c9a9d23-bc85-45d3-934e-ea0c954d2ba5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SraEmgCvXeNabD5ncHQt2m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6969,
      "cache_read_input_tokens": 24055,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 24055,
          "cache_creation_input_tokens": 6969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6969
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

_source line 16 · 2026-05-15T14:09:50.901Z_

现在读取本地文件进行编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c9a9d23-bc85-45d3-934e-ea0c954d2ba5",
  "isSidechain": false,
  "requestId": "req_011Cb4VF6Ch77RFwedY9nupE",
  "type": "assistant",
  "uuid": "d0d0d5f5-0063-4a33-a3b6-d2ddf3376402",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SraEmgCvXeNabD5ncHQt2m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6969,
      "cache_read_input_tokens": 24055,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 24055,
          "cache_creation_input_tokens": 6969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6969
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

_source line 17 · 2026-05-15T14:09:56.017Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XMMiS4qfTTz9LbFFEHASza`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0d0d5f5-0063-4a33-a3b6-d2ddf3376402",
  "isSidechain": false,
  "requestId": "req_011Cb4VF6Ch77RFwedY9nupE",
  "type": "assistant",
  "uuid": "c2018936-3bc3-4501-aa5a-432b2d58eae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SraEmgCvXeNabD5ncHQt2m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6969,
      "cache_read_input_tokens": 24055,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 24055,
          "cache_creation_input_tokens": 6969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6969
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

_source line 18 · 2026-05-15T14:09:56.041Z_

<details><summary>↩ Tool result · `toolu_01XMMiS4qfTTz9LbFFEHASza`</summary>

```text
1	categories:
2	  execution-trace-llm:
3	    description: "Execution trace 辅助 LLM 代码理解/调试/推理"
4	    papers:
5	      - title: "NExT: Teaching Large Language Models to Reason about Code Execution"
6	        authors: "Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)"
7	        year: 2024
8	        venue: "ICML 2024"
9	        role: method-component
10	        key_finding: "自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。"
11	        metrics:
12	          mbpp_fix_rate_improvement: "+26.1%"
13	          humaneval_fix_rate_improvement: "+14.3%"
14	
15	      - title: "Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs"
16	        authors: "Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li"
17	        year: 2025
18	        venue: "Findings of EMNLP 2025"
19	        arxiv_id: "2509.11686"
20	        role: direct-competitor
21	        key_finding: "综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。"
22	        metrics: {}
23	
24	      - title: "Code Execution as Grounded Supervision for LLM Reasoning"
25	        authors: "Dongwon Jung, Wenxuan Zhou, Muhao Chen"
26	        year: 2025
27	        venue: "EMNLP 2025"
28	        arxiv_id: "2506.10343"
29	        role: method-component
30	        key_finding: "用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。"
31	        metrics: {}
32	
33	      - title: "What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces"
34	        authors: "Lorenzo Ferrando, Nicola Ferraro, et al."
35	        year: 2025
36	        venue: "arXiv 2503.05703"
37	        arxiv_id: "2503.05703"
38	        role: method-component
39	        key_finding: "对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。"
40	        metrics:
41	          cruxeval_accuracy: "~80%"
42	          mbpp_accuracy: "~80%"
43	
44	      - title: "Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation"
45	        authors: "Mohammad Abdollahi, Khandaker Rifah Tasnia, Soumit Kanti Saha, Jinqiu Yang, Song Wang, Hadi Hemmati"
46	        year: 2025
47	        venue: "arXiv"
48	        arxiv_id: "2512.00215"
49	        role: evaluation
50	        key_finding: "LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。"
51	        metrics: {}
52	
53	      - title: "Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)"
54	        authors: "Junkai Chen et al."
55	        year: 2024
56	        venue: "arXiv 2403.16437"
57	        role: evaluation
58	        key_finding: "REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。"
59	        metrics:
60	          avg_accuracy: "44.4%"
61	          avg_ic_score: "10.3"
62	
63	      - title: "CodeMind: Evaluating Large Language Models for Code Reasoning"
64	        authors: "Changshu Liu et al. (UIUC)"
65	        year: 2024
66	        venue: "arXiv 2402.09664"
67	        role: evaluation
68	        key_finding: "评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。"
69	        metrics: {}
70	
71	      - title: "CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution"
72	        authors: "Ruiyang Xu et al. (HKUST)"
73	        year: 2025
74	        venue: "ACL 2025"
75	        arxiv_id: "2408.13001"
76	        role: evaluation
77	        key_finding: "将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。"
78	        metrics:
79	          languages: 19
80	          cross_lang_max_pass1: "34.4%"
81	
82	  code-verdict:
83	    description: "LLM 判断代码 pass/fail、正确性分类、mutation testing"
84	    papers:
85	      - title: "APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models"
86	        authors: "iSEngLab (Nanjing University)"
87	        year: 2024
88	        venue: "IEEE TSE 2024"
89	        role: direct-competitor
90	        key_finding: "BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。"
91	        metrics:
92	          accuracy: "79.7%"
93	          recall: "83.2%"
94	          f1_improvement_from_finetuning: "+10.22%"
95	
96	      - title: "LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment"
97	        authors: "Xin Zhou et al. (SMU)"
98	        year: 2024
99	        venue: "IEEE TSE 2024"
100	        role: direct-competitor
101	        key_finding: "用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。"
102	        metrics:
103	          accuracy: "84.4%"
104	          f1: "86.5%"
105	        novelty_threat: medium
106	
107	      - title: "Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment"
108	        authors: "Zhenyu Yang, Jingwen Wu, Zhen Yang, Zhongxing Yu"
109	        year: 2025
110	        venue: "arXiv 2505.02629"
111	        arxiv_id: "2505.02629"
112	        role: direct-competitor
113	        key_finding: "提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。"
114	        metrics:
115	          accuracy_improvement: "+3.1-7.5%"
116	          f1_improvement: "+3.0-7.1%"
117	        novelty_threat: medium
118	
119	      - title: "Calibration and Correctness of Language Models for Code"
120	        authors: "Claudio Spiess, David Gros, et al."
121	        year: 2025
122	        venue: "ICSE 2025"
123	        arxiv_id: "2402.02047"
124	        role: evaluation
125	        key_finding: "代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。"
126	        metrics: {}
127	
128	      - title: "Mutation-Guided LLM-based Test Generation at Meta"
129	        authors: "Christopher Foster et al. (Meta)"
130	        year: 2025
131	        venue: "FSE 2025 (Industry)"
132	        arxiv_id: "2501.12862"
133	        role: evaluation
134	        key_finding: "LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。"
135	        metrics:
136	          precision: "0.95"
137	          recall: "0.96"
138	          classes_evaluated: "10795"
139	          test_acceptance_rate: "73%"
140	
141	      - title: "FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning"
142	        authors: "Ratnadira Widyasari et al. (SMU)"
143	        year: 2024
144	        venue: "SANER 2024"
145	        role: background
146	        key_finding: "融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。"
147	        metrics:
148	          top1_improvement_over_baseline: "+32.3%"
149	          top1_improvement_over_sbfl: "+68.4%"
150	
151	  trace-compression:
152	    description: "Execution trace 的压缩、摘要、抽象方法"
153	    papers:
154	      - title: "Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning"
155	        authors: "Aashish Yadavally, Yi Li, Tien Nguyen"
156	        year: 2024
157	        venue: "FSE 2024"
158	        role: method-component
159	        key_finding: "ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。"
160	        metrics:
161	          exact_match: "81.31%"
162	          rouge_lcs: "0.954"
163	          fault_localization_accuracy: "63.88%"
164	
165	      - title: "Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs"
166	        authors: "Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)"
167	        year: 2025
168	        venue: "KnowledgeNLP Workshop @ ACL 2025"
169	        arxiv_id: "2505.04441"
170	        role: background
171	        key_finding: "直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。"
172	        metrics: {}
173	
174	      - title: "Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)"
175	        authors: "Koshi Eguchi, Takuya Akiba"
176	        year: 2025
177	        venue: "ICML 2025 Workshop PRAL"
178	        openreview_id: "pFyBdPyOCQ"
179	        role: method-component
180	        key_finding: "开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。"
181	        metrics:
182	          cruxeval_o: "70.0%"
183	          livecodebench_execution: "88.3%"
184	
185	      - title: "TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code"
186	        authors: "Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu"
187	        year: 2026
188	        venue: "ICSE 2026"
189	        arxiv_id: "2602.06875"
190	        verified: true
191	        role: background
192	        key_finding: "在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。"
193	        metrics:
194	          pass_at_1_improvement: "+34.43%"
195	
196	      - title: "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate"
197	        authors: "Jiaqing Wu, Tong Wu, Manqing Zhang, Yunwei Dong, Bo Shen"
198	        year: 2026
199	        venue: "arXiv 2604.02647"
200	        arxiv_id: "2604.02647"
201	        verified: true
202	        role: background
203	        key_finding: "Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。"
204	        metrics:
205	          defects_fixed: "392"
206	
207	      - title: "InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration"
208	        authors: "Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, Shuiguang Deng"
209	        year: 2025
210	        venue: "arXiv 2510.18327"
211	        arxiv_id: "2510.18327"
212	        role: background
213	        key_finding: "首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。"
214	        metrics:
215	          repair_accuracy_improvement: "+5.10-60.37%"
216	
217	      - title: "MGDebugger: From Code to Correctness via Hierarchical Debugging"
218	        authors: "Yuling Shi et al."
219	        year: 2024
220	        venue: "arXiv 2410.01215"
221	        role: background
222	        key_finding: "层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。"
223	        metrics:
224	          humaneval_accuracy: "94.5%"
225	          humaneval_fix_accuracy: "97.6%"
226	
227	  debugging-agents:
228	    description: "LLM 多智能体调试框架"
229	    papers:
230	      - title: "UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging"
231	        authors: "Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)"
232	        year: 2025
233	        venue: "EMNLP 2025"
234	        arxiv_id: "2404.17153"
235	        role: background
236	        key_finding: "三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。"
237	        metrics:
238	          defects4j_improvement: "1.25-2.56x"
239	
240	      - title: "Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach"
241	        authors: "Xuanming Zhang, Yuxuan Chen, Yuan Yuan, Minlie Huang"
242	        year: 2025
243	        venue: "ICLR 2025"
244	        arxiv_id: "2410.06949"
245	        role: background
246	        key_finding: "5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。"
247	        metrics:
248	          exception_handling_precision_improvement: "+37%"
249	
250	  sft-classification:
251	    description: "用 SFT 做分类任务的方法论和 findings"
252	    papers:
253	      - title: "Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches"
254	        authors: "Amirhossein Yousefiramandi, Ciaran Cooney"
255	        year: 2025
256	        venue: "arXiv 2512.12677"
257	        arxiv_id: "2512.12677"
258	        role: method-component
259	        key_finding: "对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。"
260	        metrics: {}
261	
262	      - title: "FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain"
263	        authors: "Rohan Deb, Kiran Koshy Thekumparampil, Kousha Kalantari, Gaurush Hiranandani, Shoham Sabach, Branislav Kveton"
264	        year: 2025
265	        venue: "ICML 2025"
266	        arxiv_id: "2505.14826"
267	        role: background
268	        key_finding: "用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。"
269	        metrics: {}
270	
271	      - title: "Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification"
272	        authors: "Martin Juan Jose Bucher, Marco Martini"
273	        year: 2024
274	        venue: "arXiv 2406.08660"
275	        role: background
276	        key_finding: "跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。"
277	        metrics: {}
278	
279	meta:
280	  last_updated: "2026-05-15"
281	  total_papers: 26
282	  search_scope: "2024-2026, top ML/NLP/SE venues"
283	  scan_date: "2026-05-15"
284	  scan_queries: 16
285	  key_gaps:
286	    - "缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白"
287	    - "trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少"
288	    - "SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白"
289	    - "patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别"
290	    - "selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification"
291	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2018936-3bc3-4501-aa5a-432b2d58eae3",
  "isSidechain": false,
  "promptId": "c0d844fc-b12d-4112-8dca-0bf81db49181",
  "type": "user",
  "uuid": "d29ba541-a3d1-4e8a-b887-afc8555f22d7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml",
      "content": "categories:\n  execution-trace-llm:\n    description: \"Execution trace 辅助 LLM 代码理解/调试/推理\"\n    papers:\n      - title: \"NExT: Teaching Large Language Models to Reason about Code Execution\"\n        authors: \"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\"\n        year: 2024\n        venue: \"ICML 2024\"\n        role: method-component\n        key_finding: \"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\"\n        metrics:\n          mbpp_fix_rate_improvement: \"+26.1%\"\n          humaneval_fix_rate_improvement: \"+14.3%\"\n\n      - title: \"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\"\n        authors: \"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\"\n        year: 2025\n        venue: \"Findings of EMNLP 2025\"\n        arxiv_id: \"2509.11686\"\n        role: direct-competitor\n        key_finding: \"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Code Execution as Grounded Supervision for LLM Reasoning\"\n        authors: \"Dongwon Jung, Wenxuan Zhou, Muhao Chen\"\n        year: 2025\n        venue: \"EMNLP 2025\"\n        arxiv_id: \"2506.10343\"\n        role: method-component\n        key_finding: \"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\"\n        metrics: {}\n\n      - title: \"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\"\n        authors: \"Lorenzo Ferrando, Nicola Ferraro, et al.\"\n        year: 2025\n        venue: \"arXiv 2503.05703\"\n        arxiv_id: \"2503.05703\"\n        role: method-component\n        key_finding: \"对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。\"\n        metrics:\n          cruxeval_accuracy: \"~80%\"\n          mbpp_accuracy: \"~80%\"\n\n      - title: \"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation\"\n        authors: \"Mohammad Abdollahi, Khandaker Rifah Tasnia, Soumit Kanti Saha, Jinqiu Yang, Song Wang, Hadi Hemmati\"\n        year: 2025\n        venue: \"arXiv\"\n        arxiv_id: \"2512.00215\"\n        role: evaluation\n        key_finding: \"LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。\"\n        metrics: {}\n\n      - title: \"Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)\"\n        authors: \"Junkai Chen et al.\"\n        year: 2024\n        venue: \"arXiv 2403.16437\"\n        role: evaluation\n        key_finding: \"REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。\"\n        metrics:\n          avg_accuracy: \"44.4%\"\n          avg_ic_score: \"10.3\"\n\n      - title: \"CodeMind: Evaluating Large Language Models for Code Reasoning\"\n        authors: \"Changshu Liu et al. (UIUC)\"\n        year: 2024\n        venue: \"arXiv 2402.09664\"\n        role: evaluation\n        key_finding: \"评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。\"\n        metrics: {}\n\n      - title: \"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\"\n        authors: \"Ruiyang Xu et al. (HKUST)\"\n        year: 2025\n        venue: \"ACL 2025\"\n        arxiv_id: \"2408.13001\"\n        role: evaluation\n        key_finding: \"将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。\"\n        metrics:\n          languages: 19\n          cross_lang_max_pass1: \"34.4%\"\n\n  code-verdict:\n    description: \"LLM 判断代码 pass/fail、正确性分类、mutation testing\"\n    papers:\n      - title: \"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\"\n        authors: \"iSEngLab (Nanjing University)\"\n        year: 2024\n        venue: \"IEEE TSE 2024\"\n        role: direct-competitor\n        key_finding: \"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\"\n        metrics:\n          accuracy: \"79.7%\"\n          recall: \"83.2%\"\n          f1_improvement_from_finetuning: \"+10.22%\"\n\n      - title: \"LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment\"\n        authors: \"Xin Zhou et al. (SMU)\"\n        year: 2024\n        venue: \"IEEE TSE 2024\"\n        role: direct-competitor\n        key_finding: \"用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。\"\n        metrics:\n          accuracy: \"84.4%\"\n          f1: \"86.5%\"\n        novelty_threat: medium\n\n      - title: \"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment\"\n        authors: \"Zhenyu Yang, Jingwen Wu, Zhen Yang, Zhongxing Yu\"\n        year: 2025\n        venue: \"arXiv 2505.02629\"\n        arxiv_id: \"2505.02629\"\n        role: direct-competitor\n        key_finding: \"提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。\"\n        metrics:\n          accuracy_improvement: \"+3.1-7.5%\"\n          f1_improvement: \"+3.0-7.1%\"\n        novelty_threat: medium\n\n      - title: \"Calibration and Correctness of Language Models for Code\"\n        authors: \"Claudio Spiess, David Gros, et al.\"\n        year: 2025\n        venue: \"ICSE 2025\"\n        arxiv_id: \"2402.02047\"\n        role: evaluation\n        key_finding: \"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\"\n        metrics: {}\n\n      - title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n        authors: \"Christopher Foster et al. (Meta)\"\n        year: 2025\n        venue: \"FSE 2025 (Industry)\"\n        arxiv_id: \"2501.12862\"\n        role: evaluation\n        key_finding: \"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\"\n        metrics:\n          precision: \"0.95\"\n          recall: \"0.96\"\n          classes_evaluated: \"10795\"\n          test_acceptance_rate: \"73%\"\n\n      - title: \"FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning\"\n        authors: \"Ratnadira Widyasari et al. (SMU)\"\n        year: 2024\n        venue: \"SANER 2024\"\n        role: background\n        key_finding: \"融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。\"\n        metrics:\n          top1_improvement_over_baseline: \"+32.3%\"\n          top1_improvement_over_sbfl: \"+68.4%\"\n\n  trace-compression:\n    description: \"Execution trace 的压缩、摘要、抽象方法\"\n    papers:\n      - title: \"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\"\n        authors: \"Aashish Yadavally, Yi Li, Tien Nguyen\"\n        year: 2024\n        venue: \"FSE 2024\"\n        role: method-component\n        key_finding: \"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\"\n        metrics:\n          exact_match: \"81.31%\"\n          rouge_lcs: \"0.954\"\n          fault_localization_accuracy: \"63.88%\"\n\n      - title: \"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\"\n        authors: \"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\"\n        year: 2025\n        venue: \"KnowledgeNLP Workshop @ ACL 2025\"\n        arxiv_id: \"2505.04441\"\n        role: background\n        key_finding: \"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\"\n        metrics: {}\n\n      - title: \"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\"\n        authors: \"Koshi Eguchi, Takuya Akiba\"\n        year: 2025\n        venue: \"ICML 2025 Workshop PRAL\"\n        openreview_id: \"pFyBdPyOCQ\"\n        role: method-component\n        key_finding: \"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\"\n        metrics:\n          cruxeval_o: \"70.0%\"\n          livecodebench_execution: \"88.3%\"\n\n      - title: \"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\"\n        authors: \"Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu\"\n        year: 2026\n        venue: \"ICSE 2026\"\n        arxiv_id: \"2602.06875\"\n        verified: true\n        role: background\n        key_finding: \"在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。\"\n        metrics:\n          pass_at_1_improvement: \"+34.43%\"\n\n      - title: \"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\"\n        authors: \"Jiaqing Wu, Tong Wu, Manqing Zhang, Yunwei Dong, Bo Shen\"\n        year: 2026\n        venue: \"arXiv 2604.02647\"\n        arxiv_id: \"2604.02647\"\n        verified: true\n        role: background\n        key_finding: \"Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。\"\n        metrics:\n          defects_fixed: \"392\"\n\n      - title: \"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\"\n        authors: \"Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, Shuiguang Deng\"\n        year: 2025\n        venue: \"arXiv 2510.18327\"\n        arxiv_id: \"2510.18327\"\n        role: background\n        key_finding: \"首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。\"\n        metrics:\n          repair_accuracy_improvement: \"+5.10-60.37%\"\n\n      - title: \"MGDebugger: From Code to Correctness via Hierarchical Debugging\"\n        authors: \"Yuling Shi et al.\"\n        year: 2024\n        venue: \"arXiv 2410.01215\"\n        role: background\n        key_finding: \"层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。\"\n        metrics:\n          humaneval_accuracy: \"94.5%\"\n          humaneval_fix_accuracy: \"97.6%\"\n\n  debugging-agents:\n    description: \"LLM 多智能体调试框架\"\n    papers:\n      - title: \"UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging\"\n        authors: \"Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)\"\n        year: 2025\n        venue: \"EMNLP 2025\"\n        arxiv_id: \"2404.17153\"\n        role: background\n        key_finding: \"三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。\"\n        metrics:\n          defects4j_improvement: \"1.25-2.56x\"\n\n      - title: \"Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach\"\n        authors: \"Xuanming Zhang, Yuxuan Chen, Yuan Yuan, Minlie Huang\"\n        year: 2025\n        venue: \"ICLR 2025\"\n        arxiv_id: \"2410.06949\"\n        role: background\n        key_finding: \"5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。\"\n        metrics:\n          exception_handling_precision_improvement: \"+37%\"\n\n  sft-classification:\n    description: \"用 SFT 做分类任务的方法论和 findings\"\n    papers:\n      - title: \"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\"\n        authors: \"Amirhossein Yousefiramandi, Ciaran Cooney\"\n        year: 2025\n        venue: \"arXiv 2512.12677\"\n        arxiv_id: \"2512.12677\"\n        role: method-component\n        key_finding: \"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\"\n        metrics: {}\n\n      - title: \"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\"\n        authors: \"Rohan Deb, Kiran Koshy Thekumparampil, Kousha Kalantari, Gaurush Hiranandani, Shoham Sabach, Branislav Kveton\"\n        year: 2025\n        venue: \"ICML 2025\"\n        arxiv_id: \"2505.14826\"\n        role: background\n        key_finding: \"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\"\n        metrics: {}\n\n      - title: \"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\"\n        authors: \"Martin Juan Jose Bucher, Marco Martini\"\n        year: 2024\n        venue: \"arXiv 2406.08660\"\n        role: background\n        key_finding: \"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\"\n        metrics: {}\n\nmeta:\n  last_updated: \"2026-05-15\"\n  total_papers: 26\n  search_scope: \"2024-2026, top ML/NLP/SE venues\"\n  scan_date: \"2026-05-15\"\n  scan_queries: 16\n  key_gaps:\n    - \"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\"\n    - \"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\"\n    - \"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\"\n    - \"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\"\n    - \"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\"\n",
      "numLines": 291,
      "startLine": 1,
      "totalLines": 291
    }
  },
  "sourceToolAssistantUUID": "c2018936-3bc3-4501-aa5a-432b2d58eae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "leafUuid": "d29ba541-a3d1-4e8a-b887-afc8555f22d7",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Integrate cross-model generalization literature into literature_map.yaml",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---

### Assistant

_source line 21 · 2026-05-15T14:10:01.238Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to add the `cross-model-generalization` category before the `meta` section. Let me insert it between the `sft-classification` category and the `meta` section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d29ba541-a3d1-4e8a-b887-afc8555f22d7",
  "isSidechain": false,
  "requestId": "req_011Cb4VG1KHFXBtjeTtY7W6m",
  "type": "assistant",
  "uuid": "5ad6f9cb-1c36-4abb-87e5-30bb4c74b5ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSmuJZhYykbxBdDyeR46RS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 31024,
      "output_tokens": 1359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1359,
          "cache_read_input_tokens": 31024,
          "cache_creation_input_tokens": 6739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6739
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

_source line 22 · 2026-05-15T14:10:02.196Z_

在 `sft-classification` 和 `meta` 之间插入新 category，并更新 `total_papers`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ad6f9cb-1c36-4abb-87e5-30bb4c74b5ea",
  "isSidechain": false,
  "requestId": "req_011Cb4VG1KHFXBtjeTtY7W6m",
  "type": "assistant",
  "uuid": "452bb4ad-87c1-4dca-98ee-5e30e96e44f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSmuJZhYykbxBdDyeR46RS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 31024,
      "output_tokens": 1359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1359,
          "cache_read_input_tokens": 31024,
          "cache_creation_input_tokens": 6739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6739
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

_source line 23 · 2026-05-15T14:10:27.733Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01TAmfN9sFfDs6X5F2gQeaPs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml",
  "old_string": "meta:\n  last_updated: \"2026-05-15\"\n  total_papers: 26",
  "new_string": "  cross-model-generalization:\n    description: \"跨模型 SFT 泛化：不同 base model 上 SFT 效果的迁移与差异\"\n    papers:\n      - title: \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\"\n        authors: \"Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng Ann Heng, Wai Lam\"\n        year: 2024\n        venue: \"NAACL 2024\"\n        arxiv_id: \"2403.09162\"\n        role: method-component\n        key_finding: \"SFT 后分类任务跨域正迁移，生成任务跨域负迁移。对 VOTA 的跨模型实验设计有直接参考——verdict 分类属于分类任务，预期正迁移。\"\n        metrics: {}\n\n      - title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n        authors: \"Guanting Dong, Hongyi Yuan, Keming Lu, et al.\"\n        year: 2024\n        venue: \"ACL 2024\"\n        arxiv_id: \"2310.05492\"\n        role: method-component\n        key_finding: \"更大/更强 base model 在相同 SFT 数据量下性能更优。DeepSeek-Coder-6.7B 预训练 2T tokens，Qwen 5.5T，比例 2.75x。对 VOTA 跨模型对比（DeepSeek vs Qwen）提供预训练数据量的基准参考。\"\n        metrics:\n          deepseek_coder_pretrain_tokens: \"2T\"\n          qwen_pretrain_tokens: \"5.5T\"\n\n      - title: \"Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels\"\n        authors: \"Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan\"\n        year: 2025\n        venue: \"EMNLP 2025\"\n        arxiv_id: \"2509.16596\"\n        role: background\n        key_finding: \"SFT 中 90% 参数更新不贡献知识增强；知识掌握水平不同的训练数据导致 >12% 性能波动。对 VOTA 的数据质量控制有参考意义。\"\n        metrics:\n          non_contributing_param_ratio: \"90%\"\n          performance_variation_from_data_quality: \">12%\"\n\n      - title: \"From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT\"\n        authors: \"Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov\"\n        year: 2025\n        venue: \"arXiv 2605.03686\"\n        arxiv_id: \"2605.03686\"\n        role: background\n        key_finding: \"DeepSeek-Coder-7B-Instruct LoRA 微调做代码分类 80% accuracy。验证 DeepSeek-Coder 系列在代码分类 SFT 上的可行性。\"\n        metrics:\n          code_classification_accuracy: \"80%\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, et al. (Qwen Team)\"\n        year: 2024\n        venue: \"arXiv 2409.12186\"\n        arxiv_id: \"2409.12186\"\n        role: background\n        key_finding: \"Qwen2.5-Coder 5.5T tokens 预训练，HumanEval 92.7%。作为 VOTA 跨模型实验的 base model 之一，提供预训练规模和代码能力基准。\"\n        metrics:\n          pretrain_tokens: \"5.5T\"\n          humaneval_pass1: \"92.7%\"\n\nmeta:\n  last_updated: \"2026-05-15\"\n  total_papers: 31"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "452bb4ad-87c1-4dca-98ee-5e30e96e44f7",
  "isSidechain": false,
  "requestId": "req_011Cb4VG1KHFXBtjeTtY7W6m",
  "type": "assistant",
  "uuid": "fab3b5f5-8a44-4676-9609-8ec6b8822979",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSmuJZhYykbxBdDyeR46RS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6739,
      "cache_read_input_tokens": 31024,
      "output_tokens": 1359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1359,
          "cache_read_input_tokens": 31024,
          "cache_creation_input_tokens": 6739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6739
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

_source line 24 · 2026-05-15T14:10:27.792Z_

<details><summary>↩ Tool result · `toolu_01TAmfN9sFfDs6X5F2gQeaPs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fab3b5f5-8a44-4676-9609-8ec6b8822979",
  "isSidechain": false,
  "promptId": "c0d844fc-b12d-4112-8dca-0bf81db49181",
  "type": "user",
  "uuid": "34d53a66-363d-4d41-b538-9490675a6757",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml",
    "oldString": "meta:\n  last_updated: \"2026-05-15\"\n  total_papers: 26",
    "newString": "  cross-model-generalization:\n    description: \"跨模型 SFT 泛化：不同 base model 上 SFT 效果的迁移与差异\"\n    papers:\n      - title: \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\"\n        authors: \"Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng Ann Heng, Wai Lam\"\n        year: 2024\n        venue: \"NAACL 2024\"\n        arxiv_id: \"2403.09162\"\n        role: method-component\n        key_finding: \"SFT 后分类任务跨域正迁移，生成任务跨域负迁移。对 VOTA 的跨模型实验设计有直接参考——verdict 分类属于分类任务，预期正迁移。\"\n        metrics: {}\n\n      - title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n        authors: \"Guanting Dong, Hongyi Yuan, Keming Lu, et al.\"\n        year: 2024\n        venue: \"ACL 2024\"\n        arxiv_id: \"2310.05492\"\n        role: method-component\n        key_finding: \"更大/更强 base model 在相同 SFT 数据量下性能更优。DeepSeek-Coder-6.7B 预训练 2T tokens，Qwen 5.5T，比例 2.75x。对 VOTA 跨模型对比（DeepSeek vs Qwen）提供预训练数据量的基准参考。\"\n        metrics:\n          deepseek_coder_pretrain_tokens: \"2T\"\n          qwen_pretrain_tokens: \"5.5T\"\n\n      - title: \"Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels\"\n        authors: \"Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan\"\n        year: 2025\n        venue: \"EMNLP 2025\"\n        arxiv_id: \"2509.16596\"\n        role: background\n        key_finding: \"SFT 中 90% 参数更新不贡献知识增强；知识掌握水平不同的训练数据导致 >12% 性能波动。对 VOTA 的数据质量控制有参考意义。\"\n        metrics:\n          non_contributing_param_ratio: \"90%\"\n          performance_variation_from_data_quality: \">12%\"\n\n      - title: \"From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT\"\n        authors: \"Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov\"\n        year: 2025\n        venue: \"arXiv 2605.03686\"\n        arxiv_id: \"2605.03686\"\n        role: background\n        key_finding: \"DeepSeek-Coder-7B-Instruct LoRA 微调做代码分类 80% accuracy。验证 DeepSeek-Coder 系列在代码分类 SFT 上的可行性。\"\n        metrics:\n          code_classification_accuracy: \"80%\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, et al. (Qwen Team)\"\n        year: 2024\n        venue: \"arXiv 2409.12186\"\n        arxiv_id: \"2409.12186\"\n        role: background\n        key_finding: \"Qwen2.5-Coder 5.5T tokens 预训练，HumanEval 92.7%。作为 VOTA 跨模型实验的 base model 之一，提供预训练规模和代码能力基准。\"\n        metrics:\n          pretrain_tokens: \"5.5T\"\n          humaneval_pass1: \"92.7%\"\n\nmeta:\n  last_updated: \"2026-05-15\"\n  total_papers: 31",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 276,
        "oldLines": 9,
        "newStart": 276,
        "newLines": 64,
        "lines": [
          "         key_finding: \"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\"",
          "         metrics: {}",
          " ",
          "+  cross-model-generalization:",
          "+    description: \"跨模型 SFT 泛化：不同 base model 上 SFT 效果的迁移与差异\"",
          "+    papers:",
          "+      - title: \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\"",
          "+        authors: \"Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng Ann Heng, Wai Lam\"",
          "+        year: 2024",
          "+        venue: \"NAACL 2024\"",
          "+        arxiv_id: \"2403.09162\"",
          "+        role: method-component",
          "+        key_finding: \"SFT 后分类任务跨域正迁移，生成任务跨域负迁移。对 VOTA 的跨模型实验设计有直接参考——verdict 分类属于分类任务，预期正迁移。\"",
          "+        metrics: {}",
          "+",
          "+      - title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"",
          "+        authors: \"Guanting Dong, Hongyi Yuan, Keming Lu, et al.\"",
          "+        year: 2024",
          "+        venue: \"ACL 2024\"",
          "+        arxiv_id: \"2310.05492\"",
          "+        role: method-component",
          "+        key_finding: \"更大/更强 base model 在相同 SFT 数据量下性能更优。DeepSeek-Coder-6.7B 预训练 2T tokens，Qwen 5.5T，比例 2.75x。对 VOTA 跨模型对比（DeepSeek vs Qwen）提供预训练数据量的基准参考。\"",
          "+        metrics:",
          "+          deepseek_coder_pretrain_tokens: \"2T\"",
          "+          qwen_pretrain_tokens: \"5.5T\"",
          "+",
          "+      - title: \"Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels\"",
          "+        authors: \"Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan\"",
          "+        year: 2025",
          "+        venue: \"EMNLP 2025\"",
          "+        arxiv_id: \"2509.16596\"",
          "+        role: background",
          "+        key_finding: \"SFT 中 90% 参数更新不贡献知识增强；知识掌握水平不同的训练数据导致 >12% 性能波动。对 VOTA 的数据质量控制有参考意义。\"",
          "+        metrics:",
          "+          non_contributing_param_ratio: \"90%\"",
          "+          performance_variation_from_data_quality: \">12%\"",
          "+",
          "+      - title: \"From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT\"",
          "+        authors: \"Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov\"",
          "+        year: 2025",
          "+        venue: \"arXiv 2605.03686\"",
          "+        arxiv_id: \"2605.03686\"",
          "+        role: background",
          "+        key_finding: \"DeepSeek-Coder-7B-Instruct LoRA 微调做代码分类 80% accuracy。验证 DeepSeek-Coder 系列在代码分类 SFT 上的可行性。\"",
          "+        metrics:",
          "+          code_classification_accuracy: \"80%\"",
          "+",
          "+      - title: \"Qwen2.5-Coder Technical Report\"",
          "+        authors: \"Binyuan Hui, Jian Yang, et al. (Qwen Team)\"",
          "+        year: 2024",
          "+        venue: \"arXiv 2409.12186\"",
          "+        arxiv_id: \"2409.12186\"",
          "+        role: background",
          "+        key_finding: \"Qwen2.5-Coder 5.5T tokens 预训练，HumanEval 92.7%。作为 VOTA 跨模型实验的 base model 之一，提供预训练规模和代码能力基准。\"",
          "+        metrics:",
          "+          pretrain_tokens: \"5.5T\"",
          "+          humaneval_pass1: \"92.7%\"",
          "+",
          " meta:",
          "   last_updated: \"2026-05-15\"",
          "-  total_papers: 26",
          "+  total_papers: 31",
          "   search_scope: \"2024-2026, top ML/NLP/SE venues\"",
          "   scan_date: \"2026-05-15\"",
          "   scan_queries: 16"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "fab3b5f5-8a44-4676-9609-8ec6b8822979",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T14:10:30.870Z_

现在用 `save_project_file` 保存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34d53a66-363d-4d41-b538-9490675a6757",
  "isSidechain": false,
  "requestId": "req_011Cb4VJLMKLuh9UYzpxNfT8",
  "type": "assistant",
  "uuid": "54c1afd5-1292-43bf-9d31-021144ba76f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWS5QQaHb4at7hyKjwnUda",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 37763,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 37763,
          "cache_creation_input_tokens": 1429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1429
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

_source line 26 · 2026-05-15T14:10:31.591Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TGjhF6DFh3Ed8wc9V1gHkZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54c1afd5-1292-43bf-9d31-021144ba76f6",
  "isSidechain": false,
  "requestId": "req_011Cb4VJLMKLuh9UYzpxNfT8",
  "type": "assistant",
  "uuid": "64518e20-89be-4425-96ee-5fdace20581a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWS5QQaHb4at7hyKjwnUda",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 37763,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 37763,
          "cache_creation_input_tokens": 1429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1429
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

_source line 27 · 2026-05-15T14:10:31.594Z_

<details><summary>↩ Tool result · `toolu_01TGjhF6DFh3Ed8wc9V1gHkZ`</summary>

````text
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
  "parentUuid": "64518e20-89be-4425-96ee-5fdace20581a",
  "isSidechain": false,
  "promptId": "c0d844fc-b12d-4112-8dca-0bf81db49181",
  "type": "user",
  "uuid": "6ad41750-f328-4a9f-b1ad-a9a588c0321d",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "64518e20-89be-4425-96ee-5fdace20581a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T14:10:38.745Z_

<details><summary>Logged reasoning block</summary>

```text
The `save_project_file` tool has a strict whitelist: memory.md, writing_plan.yaml, paper_framing.md. literature_map.yaml is not in the whitelist. But I already edited the file directly using the Edit tool, so the local file is updated. Let me verify by reading the file to confirm the changes were applied correctly, and then check if there's another way to sync it.

Actually, looking more carefully, the `save_project_file` description says "Other files have dedicated tools". literature_map.yaml might not be writable through this tool. Let me check if the file I edited is the correct one - the path is `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml`, which is the project file path. 

Let me read the file back to confirm the edit went through.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ad41750-f328-4a9f-b1ad-a9a588c0321d",
  "isSidechain": false,
  "requestId": "req_011Cb4VJcjZFHcwHbxYzAZgd",
  "type": "assistant",
  "uuid": "c45847b8-cc10-474b-9c7e-d942db3c6781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Q8yNZFJpKHwz4CgK3SnhU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 39192,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 393,
          "cache_read_input_tokens": 39192,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 379
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

_source line 29 · 2026-05-15T14:10:38.986Z_

`save_project_file` 白名单不包含 literature_map.yaml，但文件已通过 Edit 工具直接修改。验证一下改动是否正确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c45847b8-cc10-474b-9c7e-d942db3c6781",
  "isSidechain": false,
  "requestId": "req_011Cb4VJcjZFHcwHbxYzAZgd",
  "type": "assistant",
  "uuid": "b60bd466-8dcf-4d0f-b160-eaef5619de98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Q8yNZFJpKHwz4CgK3SnhU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 39192,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 393,
          "cache_read_input_tokens": 39192,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 379
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

_source line 30 · 2026-05-15T14:10:39.670Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V9qzPBTzv7W24DEbyBi6R1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml",
  "offset": 275,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b60bd466-8dcf-4d0f-b160-eaef5619de98",
  "isSidechain": false,
  "requestId": "req_011Cb4VJcjZFHcwHbxYzAZgd",
  "type": "assistant",
  "uuid": "78c8f277-ed86-4bfe-8fc9-bfd26d1b0b14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Q8yNZFJpKHwz4CgK3SnhU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 39192,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 393,
          "cache_read_input_tokens": 39192,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 379
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

_source line 31 · 2026-05-15T14:10:39.676Z_

<details><summary>↩ Tool result · `toolu_01V9qzPBTzv7W24DEbyBi6R1`</summary>

```text
275	        role: background
276	        key_finding: "跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。"
277	        metrics: {}
278	
279	  cross-model-generalization:
280	    description: "跨模型 SFT 泛化：不同 base model 上 SFT 效果的迁移与差异"
281	    papers:
282	      - title: "Unveiling the Generalization Power of Fine-Tuned Large Language Models"
283	        authors: "Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng Ann Heng, Wai Lam"
284	        year: 2024
285	        venue: "NAACL 2024"
286	        arxiv_id: "2403.09162"
287	        role: method-component
288	        key_finding: "SFT 后分类任务跨域正迁移，生成任务跨域负迁移。对 VOTA 的跨模型实验设计有直接参考——verdict 分类属于分类任务，预期正迁移。"
289	        metrics: {}
290	
291	      - title: "How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition"
292	        authors: "Guanting Dong, Hongyi Yuan, Keming Lu, et al."
293	        year: 2024
294	        venue: "ACL 2024"
295	        arxiv_id: "2310.05492"
296	        role: method-component
297	        key_finding: "更大/更强 base model 在相同 SFT 数据量下性能更优。DeepSeek-Coder-6.7B 预训练 2T tokens，Qwen 5.5T，比例 2.75x。对 VOTA 跨模型对比（DeepSeek vs Qwen）提供预训练数据量的基准参考。"
298	        metrics:
299	          deepseek_coder_pretrain_tokens: "2T"
300	          qwen_pretrain_tokens: "5.5T"
301	
302	      - title: "Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels"
303	        authors: "Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan"
304	        year: 2025
305	        venue: "EMNLP 2025"
306	        arxiv_id: "2509.16596"
307	        role: background
308	        key_finding: "SFT 中 90% 参数更新不贡献知识增强；知识掌握水平不同的训练数据导致 >12% 性能波动。对 VOTA 的数据质量控制有参考意义。"
309	        metrics:
310	          non_contributing_param_ratio: "90%"
311	          performance_variation_from_data_quality: ">12%"
312	
313	      - title: "From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT"
314	        authors: "Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov"
315	        year: 2025
316	        venue: "arXiv 2605.03686"
317	        arxiv_id: "2605.03686"
318	        role: background
319	        key_finding: "DeepSeek-Coder-7B-Instruct LoRA 微调做代码分类 80% accuracy。验证 DeepSeek-Coder 系列在代码分类 SFT 上的可行性。"
320	        metrics:
321	          code_classification_accuracy: "80%"
322	
323	      - title: "Qwen2.5-Coder Technical Report"
324	        authors: "Binyuan Hui, Jian Yang, et al. (Qwen Team)"
325	        year: 2024
326	        venue: "arXiv 2409.12186"
327	        arxiv_id: "2409.12186"
328	        role: background
329	        key_finding: "Qwen2.5-Coder 5.5T tokens 预训练，HumanEval 92.7%。作为 VOTA 跨模型实验的 base model 之一，提供预训练规模和代码能力基准。"
330	        metrics:
331	          pretrain_tokens: "5.5T"
332	          humaneval_pass1: "92.7%"
333	
334	meta:
335	  last_updated: "2026-05-15"
336	  total_papers: 31
337	  search_scope: "2024-2026, top ML/NLP/SE venues"
338	  scan_date: "2026-05-15"
339	  scan_queries: 16
340	  key_gaps:
341	    - "缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白"
342	    - "trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少"
343	    - "SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白"
344	    - "patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别"
345	    - "selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification"
346	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78c8f277-ed86-4bfe-8fc9-bfd26d1b0b14",
  "isSidechain": false,
  "promptId": "c0d844fc-b12d-4112-8dca-0bf81db49181",
  "type": "user",
  "uuid": "4b1623b6-93b4-44c6-82b2-4c7d6abc4b45",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml",
      "content": "        role: background\n        key_finding: \"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\"\n        metrics: {}\n\n  cross-model-generalization:\n    description: \"跨模型 SFT 泛化：不同 base model 上 SFT 效果的迁移与差异\"\n    papers:\n      - title: \"Unveiling the Generalization Power of Fine-Tuned Large Language Models\"\n        authors: \"Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng Ann Heng, Wai Lam\"\n        year: 2024\n        venue: \"NAACL 2024\"\n        arxiv_id: \"2403.09162\"\n        role: method-component\n        key_finding: \"SFT 后分类任务跨域正迁移，生成任务跨域负迁移。对 VOTA 的跨模型实验设计有直接参考——verdict 分类属于分类任务，预期正迁移。\"\n        metrics: {}\n\n      - title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n        authors: \"Guanting Dong, Hongyi Yuan, Keming Lu, et al.\"\n        year: 2024\n        venue: \"ACL 2024\"\n        arxiv_id: \"2310.05492\"\n        role: method-component\n        key_finding: \"更大/更强 base model 在相同 SFT 数据量下性能更优。DeepSeek-Coder-6.7B 预训练 2T tokens，Qwen 5.5T，比例 2.75x。对 VOTA 跨模型对比（DeepSeek vs Qwen）提供预训练数据量的基准参考。\"\n        metrics:\n          deepseek_coder_pretrain_tokens: \"2T\"\n          qwen_pretrain_tokens: \"5.5T\"\n\n      - title: \"Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels\"\n        authors: \"Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan\"\n        year: 2025\n        venue: \"EMNLP 2025\"\n        arxiv_id: \"2509.16596\"\n        role: background\n        key_finding: \"SFT 中 90% 参数更新不贡献知识增强；知识掌握水平不同的训练数据导致 >12% 性能波动。对 VOTA 的数据质量控制有参考意义。\"\n        metrics:\n          non_contributing_param_ratio: \"90%\"\n          performance_variation_from_data_quality: \">12%\"\n\n      - title: \"From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT\"\n        authors: \"Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov\"\n        year: 2025\n        venue: \"arXiv 2605.03686\"\n        arxiv_id: \"2605.03686\"\n        role: background\n        key_finding: \"DeepSeek-Coder-7B-Instruct LoRA 微调做代码分类 80% accuracy。验证 DeepSeek-Coder 系列在代码分类 SFT 上的可行性。\"\n        metrics:\n          code_classification_accuracy: \"80%\"\n\n      - title: \"Qwen2.5-Coder Technical Report\"\n        authors: \"Binyuan Hui, Jian Yang, et al. (Qwen Team)\"\n        year: 2024\n        venue: \"arXiv 2409.12186\"\n        arxiv_id: \"2409.12186\"\n        role: background\n        key_finding: \"Qwen2.5-Coder 5.5T tokens 预训练，HumanEval 92.7%。作为 VOTA 跨模型实验的 base model 之一，提供预训练规模和代码能力基准。\"\n        metrics:\n          pretrain_tokens: \"5.5T\"\n          humaneval_pass1: \"92.7%\"\n\nmeta:\n  last_updated: \"2026-05-15\"\n  total_papers: 31\n  search_scope: \"2024-2026, top ML/NLP/SE venues\"\n  scan_date: \"2026-05-15\"\n  scan_queries: 16\n  key_gaps:\n    - \"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\"\n    - \"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\"\n    - \"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\"\n    - \"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\"\n    - \"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\"\n",
      "numLines": 72,
      "startLine": 275,
      "totalLines": 346
    }
  },
  "sourceToolAssistantUUID": "78c8f277-ed86-4bfe-8fc9-bfd26d1b0b14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-15T14:10:39.739Z_

```json
{
  "parentUuid": "4b1623b6-93b4-44c6-82b2-4c7d6abc4b45",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "22b595b2-12f6-432d-abf4-28669f7a8ea7",
  "timestamp": "2026-05-15T14:10:39.739Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
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
  "leafUuid": "22b595b2-12f6-432d-abf4-28669f7a8ea7",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Integrate cross-model generalization literature into literature_map.yaml",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---

### Assistant

_source line 35 · 2026-05-15T14:10:44.324Z_

已完成。`cross-model-generalization` category 已添加到 literature_map.yaml，包含 5 篇论文，total_papers 更新为 31。关键细节均已落实：DeepSeek-Coder 预训练 2T tokens、NNGPT 作者为 Hanouneh/Timofte/Ignatov。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22b595b2-12f6-432d-abf4-28669f7a8ea7",
  "isSidechain": false,
  "requestId": "req_011Cb4VKDKRonigVEMznzQ7R",
  "type": "assistant",
  "uuid": "35243216-7a72-4554-bfc2-4190a982e518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLYk9SKuoW5rVi8jam1WyF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2155,
      "cache_read_input_tokens": 39571,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 39571,
          "cache_creation_input_tokens": 2155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2155
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

_source line 36_

```json
{
  "type": "last-prompt",
  "leafUuid": "35243216-7a72-4554-bfc2-4190a982e518",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Integrate cross-model generalization literature into literature_map.yaml",
  "sessionId": "370d5e56-c5ef-4a3c-bd85-5c5c85449231"
}
```

---
