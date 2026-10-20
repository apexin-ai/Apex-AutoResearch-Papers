# Research conversation: <project_context> # 项目: faith-evidence-ie ## 运行环境 - 服务器名: rtx5090-4x - SSH 账户: root（调用 ssh_execute / submit_training_job

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/d1967b82-9b64-485b-8419-ac1a11ebeb1d.jsonl`
- **Structured JSON:** [`4787b1301631b4716213.json`](../../sessions/47/4787b1301631b4716213.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T20:13:18.236Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T20:13:18.236Z",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "content": "&lt;project_context>\n# 项目: faith-evidence-ie\n\n## 运行环境\n- 服务器名: rtx5090-4x\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh rtx5090-4x  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/freige\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 提交 eval 前必须 nvidia-smi 确认目标 GPU 显存占用 < 2GB，否则不提交、换卡或等待（原因：本 session 已 5 次因 eval 提交到被占用 GPU 导致 OOM，修复 eval 也因此作废。eval 推理需要接近全部显存，与训练共享必然 OOM。） [来自 D064]\n- **C002**: 提交训练/评估任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map=\"auto\" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 两次因未设 CUDA_VISIBLE_DEVICES 导致 device_map=\"auto\" 跨 GPU 分布，造成 OOM 和资源冲突。已知 bug 重复发生。）\n- **C003**: 提交训练任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map=\"auto\" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 均因未设 CUDA_VISIBLE_DEVICES 导致模型跨 GPU 分布，造成 OOM 或显存冲突。已重复发生两次。）\n- **C004**: Registry 标记 killed 时必须同时 kill -9 PID 并 ps 验证进程已终止，否则 killed 状态不可信（原因：rsft_ced_s45_train_r2 (PID 276148) registry 标记 killed 但进程未实际终止，占用 cuda:2 31.6GB 导致 r3 OOM。plan_011 也有类似模式。Reviewer WARNING。）\n- **C005**: no-evidence 模型 eval 必须传 --no_evidence 参数，确保推理时使用 NO_EVIDENCE_SYSTEM_PROMPT 与训练一致（原因：plan_006 1.7B/8B no-evidence eval 漏传该参数，导致训练/推理提示词不匹配（模型被要求输出未训练过的 evidence 字段），结果全部无效。Reviewer critical #20。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n文献联动任务：检查最新 eval 结果与已有文献的关联。\n\n## 背景\n两个 eval 刚完成：\n1. **Random RSFT k=1 eval**: ign_f1=0.4114, 远低于 CED k=1 (0.4596), gap=4.82pp\n   - 证实 CED scoring precision 是关键差异因子\n2. **GRPO bf16 ckpt-100 eval**: ign_f1=0.4431, 超越 SFT baseline (0.4057) +3.74pp\n   - GRPO 在学习有效信号，非 catastrophic forgetting\n\n## 任务\n1. 读取 `literature_map.yaml`（用 read_project_file）\n2. 检查是否有 direct-competitor 论文报告了类似的 ablation（random vs scored selection for RSFT/rejection sampling）\n3. 检查是否有论文报告了 GRPO 在 IE/NLP 任务上的 learning curve 特征\n4. 如果 map 中缺少相关论文（特别是关于 rejection sampling selection strategy ablation 的），用 WebSearch 搜索：\n   - \"rejection sampling selection strategy ablation language model\"\n   - \"GRPO document relation extraction\"\n   - \"scored vs random rejection sampling fine-tuning\"\n5. 将新发现的论文信息（title, venue, year, 关键发现）写入返回文字中，建议是否需要加入 literature_map\n\n## 产出\n一段汇总文字，包含：\n- literature_map 中相关论文列表\n- 搜索到的新相关论文\n- 是否建议更新 literature_map"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T20:13:18.240Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T20:13:18.240Z",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-18T20:13:18.277Z_

&lt;project_context>
# 项目: faith-evidence-ie

## 运行环境
- 服务器名: rtx5090-4x
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh rtx5090-4x  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/freige

## ⚠️ 活跃约束（必须遵守）

- **C001**: 提交 eval 前必须 nvidia-smi 确认目标 GPU 显存占用 < 2GB，否则不提交、换卡或等待（原因：本 session 已 5 次因 eval 提交到被占用 GPU 导致 OOM，修复 eval 也因此作废。eval 推理需要接近全部显存，与训练共享必然 OOM。） [来自 D064]
- **C002**: 提交训练/评估任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map="auto" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 两次因未设 CUDA_VISIBLE_DEVICES 导致 device_map="auto" 跨 GPU 分布，造成 OOM 和资源冲突。已知 bug 重复发生。）
- **C003**: 提交训练任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map="auto" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 均因未设 CUDA_VISIBLE_DEVICES 导致模型跨 GPU 分布，造成 OOM 或显存冲突。已重复发生两次。）
- **C004**: Registry 标记 killed 时必须同时 kill -9 PID 并 ps 验证进程已终止，否则 killed 状态不可信（原因：rsft_ced_s45_train_r2 (PID 276148) registry 标记 killed 但进程未实际终止，占用 cuda:2 31.6GB 导致 r3 OOM。plan_011 也有类似模式。Reviewer WARNING。）
- **C005**: no-evidence 模型 eval 必须传 --no_evidence 参数，确保推理时使用 NO_EVIDENCE_SYSTEM_PROMPT 与训练一致（原因：plan_006 1.7B/8B no-evidence eval 漏传该参数，导致训练/推理提示词不匹配（模型被要求输出未训练过的 evidence 字段），结果全部无效。Reviewer critical #20。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
文献联动任务：检查最新 eval 结果与已有文献的关联。

## 背景
两个 eval 刚完成：
1. **Random RSFT k=1 eval**: ign_f1=0.4114, 远低于 CED k=1 (0.4596), gap=4.82pp
   - 证实 CED scoring precision 是关键差异因子
2. **GRPO bf16 ckpt-100 eval**: ign_f1=0.4431, 超越 SFT baseline (0.4057) +3.74pp
   - GRPO 在学习有效信号，非 catastrophic forgetting

## 任务
1. 读取 `literature_map.yaml`（用 read_project_file）
2. 检查是否有 direct-competitor 论文报告了类似的 ablation（random vs scored selection for RSFT/rejection sampling）
3. 检查是否有论文报告了 GRPO 在 IE/NLP 任务上的 learning curve 特征
4. 如果 map 中缺少相关论文（特别是关于 rejection sampling selection strategy ablation 的），用 WebSearch 搜索：
   - "rejection sampling selection strategy ablation language model"
   - "GRPO document relation extraction"
   - "scored vs random rejection sampling fine-tuning"
5. 将新发现的论文信息（title, venue, year, 关键发现）写入返回文字中，建议是否需要加入 literature_map

## 产出
一段汇总文字，包含：
- literature_map 中相关论文列表
- 搜索到的新相关论文
- 是否建议更新 literature_map

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "type": "user",
  "uuid": "f3a7df4a-4b25-4798-98e4-58f262a997cf",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T20:13:18.276Z_

```json
{
  "parentUuid": "f3a7df4a-4b25-4798-98e4-58f262a997cf",
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
  "uuid": "89e4afe5-6fb0-463c-a9d1-58a812ceeded",
  "timestamp": "2026-05-18T20:13:18.276Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T20:13:18.276Z_

```json
{
  "parentUuid": "89e4afe5-6fb0-463c-a9d1-58a812ceeded",
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
  "uuid": "047eaf12-0b38-40b7-b540-8de56c69171e",
  "timestamp": "2026-05-18T20:13:18.276Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-18T20:13:18.276Z_

```json
{
  "parentUuid": "047eaf12-0b38-40b7-b540-8de56c69171e",
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
  "uuid": "4554d635-d7e4-454c-8e43-7bd005d7b8c3",
  "timestamp": "2026-05-18T20:13:18.276Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-18T20:13:18.276Z_

```json
{
  "parentUuid": "4554d635-d7e4-454c-8e43-7bd005d7b8c3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4f32d6ef-eb2c-407f-b501-390a6ac053b1",
  "timestamp": "2026-05-18T20:13:18.276Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
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
  "aiTitle": "Check eval results against literature map",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---

### Assistant

_source line 9 · 2026-05-18T20:13:21.938Z_

我来执行这个文献联动任务。先读取 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f32d6ef-eb2c-407f-b501-390a6ac053b1",
  "isSidechain": false,
  "requestId": "req_011CbAePspdHikZnTTBjRt56",
  "type": "assistant",
  "uuid": "db864802-2aa1-4065-97d0-3ffcf80c3aee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcAzTTniwFiLns3TWshheH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13814,
      "cache_read_input_tokens": 11447,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13814
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

_source line 10 · 2026-05-18T20:13:22.800Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HmwBybk75XRKRpgHtr8XH7`</summary>

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
  "parentUuid": "db864802-2aa1-4065-97d0-3ffcf80c3aee",
  "isSidechain": false,
  "requestId": "req_011CbAePspdHikZnTTBjRt56",
  "type": "assistant",
  "uuid": "edd120a8-e336-4d0f-9420-4baf624c141a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcAzTTniwFiLns3TWshheH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13814,
      "cache_read_input_tokens": 11447,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13814
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

_source line 11 · 2026-05-18T20:13:22.813Z_

<details><summary>↩ Tool result · `toolu_01HmwBybk75XRKRpgHtr8XH7`</summary>

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
  "parentUuid": "edd120a8-e336-4d0f-9420-4baf624c141a",
  "isSidechain": false,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "type": "user",
  "uuid": "2b65b1f6-43dc-4fb6-bd17-c5c7b7d3793d",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "edd120a8-e336-4d0f-9420-4baf624c141a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-18T20:13:26.489Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the literature_map.yaml file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b65b1f6-43dc-4fb6-bd17-c5c7b7d3793d",
  "isSidechain": false,
  "requestId": "req_011CbAeQDRqiaX1FHLF2pePh",
  "type": "assistant",
  "uuid": "16425e98-089e-43fb-aa71-e944700c4815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJ75ij2KnUCzrF7ZHnvxkx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 25261,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 136,
          "cache_read_input_tokens": 25261,
          "cache_creation_input_tokens": 460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 460
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

_source line 13 · 2026-05-18T20:13:26.776Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YWERTfVbWKiJyruMgMb8wS`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16425e98-089e-43fb-aa71-e944700c4815",
  "isSidechain": false,
  "requestId": "req_011CbAeQDRqiaX1FHLF2pePh",
  "type": "assistant",
  "uuid": "bce7834d-1a4a-45d4-b5ac-cb0261caeec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJ75ij2KnUCzrF7ZHnvxkx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 25261,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 136,
          "cache_read_input_tokens": 25261,
          "cache_creation_input_tokens": 460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 460
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

_source line 14 · 2026-05-18T20:13:27.121Z_

<details><summary>↩ Tool result · `toolu_01YWERTfVbWKiJyruMgMb8wS`</summary>

```text
Error: result (115,494 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bce7834d-1a4a-45d4-b5ac-cb0261caeec3",
  "isSidechain": false,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "type": "user",
  "uuid": "0fe962f9-6851-455e-90fb-c393e9cb02c5",
  "toolUseResult": "Error: result (115,494 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion; +6 papers from evidence cost literature scan; +11 papers from related work foundational survey)\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\n    key_finding: >\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\n    relevance_to_ced_stabilizer: >\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\n\\n  - title: \\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\"\\n    authors: Guanning Zeng et al.\\n    year: 2025\\n    venue: arXiv 2511.03710\\n    url: https://arxiv.org/abs/2511.03710\\n    category: reward_diversity\\n    role: theoretical_support\\n    key_finding: >\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\n      构造可证明更低 variance 的 policy gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\n\\n  - title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2502.18770\\n    url: https://arxiv.org/abs/2502.18770\\n    category: reward_diversity\\n    role: background\\n    key_finding: >\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\n      且 evidence quality 的渐进提升符合\\\"先快后慢\\\"的 reward shaping 原则。\\n\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\n\\n  - title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: ByteDance Seed, Tsinghua AIR\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2503.14476\\n    category: mode_collapse_prevention\\n    role: key_baseline\\n    key_finding: >\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\\n    relevance_to_ced_stabilizer: >\\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\\n\\n  - title: \\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\"\\n    authors: Liu et al.\\n    year: 2025\\n    venue: COLM 2025\\n    url: https://arxiv.org/abs/2503.20783\\n    category: mode_collapse_prevention\\n    role: related_analysis\\n    key_finding: >\\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\\n    relevance_to_ced_stabilizer: >\\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\\n\\n  - title: \\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2504.19599\\n    category: mode_collapse_prevention\\n    role: alternative_framework\\n    key_finding: >\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\n    relevance_to_ced_stabilizer: >\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\n\\n  - title: \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\"\\n    authors: Jian Hu et al.\\n    year: 2025\\n    venue: arXiv 2501.03262\\n    url: https://arxiv.org/abs/2501.03262\\n    category: mode_collapse_prevention\\n    role: related_method\\n    key_finding: >\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\n\\n  - title: \\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\"\\n    authors: Henglin Liu et al.\\n    year: 2025\\n    venue: arXiv 2512.21514\\n    url: https://arxiv.org/abs/2512.21514\\n    category: mode_collapse_prevention\\n    role: parallel_work\\n    key_finding: >\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\n    relevance_to_ced_stabilizer: >\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\n      都是通过 reward 层面结构化信号维持输出多样性。\\n\\n  - title: \\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2601.23135\\n    url: https://arxiv.org/abs/2601.23135\\n    category: mode_collapse_prevention\\n    role: theoretical_support\\n    key_finding: >\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\n      收益由 prompt 间平均 reward std 刻画。\\n    relevance_to_ced_stabilizer: >\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\n\\n  # === Category 3: Contrastive Rewards in RL ===\\n\\n  - title: \\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\"\\n    authors: Shen, Zhang et al.\\n    year: 2024\\n    venue: arXiv 2403.07708\\n    url: https://arxiv.org/abs/2403.07708\\n    category: contrastive_reward\\n    role: closest_contrastive_precedent\\n    key_finding: >\\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\\n    relevance_to_ced_stabilizer: >\\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\\n      stabilizing 机制相通但实现路径根本不同。\\n\\n  - title: \\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\n    category: contrastive_reward\\n    role: related_method\\n    key_finding: >\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\n      带来更稳定的 PPO 训练 return 和 reward。\\n    relevance_to_ced_stabilizer: >\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\n\\n  - title: \\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\n    category: contrastive_reward\\n    role: background\\n    key_finding: >\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\n    relevance_to_ced_stabilizer: >\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\n\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\n\\n  - title: \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ACL 2025\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\n    category: evidence_reward\\n    role: related_method\\n    key_finding: >\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\n    relevance_to_ced_stabilizer: >\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\n\\n  - title: \\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://aclanthology.org/2024.eacl-long.102/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\n    relevance_to_ced_stabilizer: >\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\n\\n  - title: \\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: PMC/Bioinformatics 2024\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\n    relevance_to_ced_stabilizer: >\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\n\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\n\\n  - title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: OpenReview\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\n    category: multi_objective_rl\\n    role: related_analysis\\n    key_finding: >\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\n      用 constrained MDP 防止超出适当边界。\\n    relevance_to_ced_stabilizer: >\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\n      可能是 CED 稳定性的另一个理论解释角度。\\n\\n  - title: \\\"On-Policy RL with Optimal Reward Baseline\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2505.23585\\n    url: https://arxiv.org/abs/2505.23585\\n    category: multi_objective_rl\\n    role: theoretical_support\\n    key_finding: >\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\n      有效稳定训练并促进更多样的 policy exploration。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\n\\n  # === Category 6: RSFT Methodology & Theory ===\\n\\n  - title: \\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\"\\n    authors: Xiao et al.\\n    year: 2025\\n    venue: arXiv 2504.11343\\n    url: https://arxiv.org/abs/2504.11343\\n    category: rsft_methodology\\n    role: key_theoretical_support\\n    key_finding: >\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\\n    relevance_to_rsft_docre: >\\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\\n      强化了 offline RSFT 的合理性。\\n\\n  - title: \\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\"\\n    authors: Jie Deng et al.\\n    year: 2026\\n    venue: arXiv 2602.04391\\n    url: https://arxiv.org/abs/2602.04391\\n    category: rsft_methodology\\n    role: method_component\\n    key_finding: >\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\n    relevance_to_rsft_docre: >\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\n      融合方式需要重新设计。\\n\\n  - title: \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\n    category: rsft_methodology\\n    role: theoretical_support\\n    key_finding: >\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\n    relevance_to_rsft_docre: >\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\n      隐式执行了 constrained policy optimization，\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\n\\n  # === Category 7: RL for Information Extraction ===\\n\\n  - title: \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\"\\n    authors: Runpeng Dai, Tong Zheng et al.\\n    year: 2025\\n    venue: arXiv 2507.04642\\n    url: https://arxiv.org/abs/2507.04642\\n    category: rl_for_ie\\n    role: direct_competitor\\n    key_finding: >\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\\n    results:\\n      sem2010_in_domain: 91.8\\n      sem2010_ood: 66.5\\n      mdkg_in_domain: 88.1\\n      mdkg_ood: 65.8\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      最直接竞争者。关键差异与讨论：\\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\\\"句子级简单 reward 可行，文档级需要 CED\\\"的论点。\\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\\n\\n  - title: \\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\"\\n    authors: Anonymous\\n    year: 2026\\n    venue: arXiv 2603.09478\\n    url: https://arxiv.org/abs/2603.09478\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\n      两阶段训练：SFT cold-start + GRPO RL。\\n    relevance_to_rsft_docre: >\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\n\\n  - title: \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\"\\n    authors: Jianwen Luo et al.\\n    year: 2025\\n    venue: EMNLP 2025 Findings\\n    url: https://2025.emnlp.org/program/find_papers/\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\n    relevance_to_rsft_docre: >\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\n      且使用 offline RSFT 而非 online RL。\\n\\n  - title: \\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\"\\n    authors: Zepeng Ding et al.\\n    year: 2024\\n    venue: arXiv 2406.11455\\n    url: https://arxiv.org/abs/2406.11455\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\n    relevance_to_rsft_docre: >\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\n\\n  - title: \\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\"\\n    authors: Haoran Luo et al.\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2507.21892\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\n    relevance_to_rsft_docre: >\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\n      我们关注 DocRE 的训练优化，应用场景不同。\\n\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\n\\n  - title: \\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.08143\\n    url: https://arxiv.org/abs/2511.08143\\n    category: llm_docre\\n    role: key_baseline\\n    key_finding: >\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\\n    results:\\n      docred_dev_f1: 47.82\\n      docred_test_f1: 48.34\\n      re_docred_dev_f1: 55.94\\n      re_docred_test_f1: 54.80\\n      backbone: LLaMA3-8B\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\\n\\n  - title: \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\"\\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\\n    year: 2024\\n    venue: arXiv 2408.13889\\n    url: https://arxiv.org/abs/2408.13889\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\\n    results:\\n      docred_dev_ign_f1: 58.16\\n      docred_dev_f1: 59.97\\n      docred_test_ign_f1: 58.49\\n      docred_test_f1: 60.52\\n      re_docred_test_ign_f1: 74.08\\n      re_docred_test_f1: 74.63\\n      backbone: BERT classifier + LLM\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\\n\\n  - title: \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NLPCC 2025\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\n      再用 CoT 验证过滤不满足规则的 triple。\\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\\n    results:\\n      note: \\\"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\\n\\n  - title: \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.00757\\n    url: https://arxiv.org/abs/2508.00757\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\n      预训练于 136K 文档的大规模 RE 数据。\\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\\n    results:\\n      re_docred_dev_f1: 77.76\\n      re_docred_test_f1: 77.83\\n      re_docred_zero_shot_test_f1: 17.32\\n      fredo_in_domain_1doc_f1: 13.00\\n      fredo_in_domain_3doc_f1: 15.71\\n      backbone: \\\"dual-encoder (few hundred M params)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\\n\\n  - title: \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2403.14888\\n    url: https://arxiv.org/abs/2403.14888\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\\n    results:\\n      re_docred_dev_f1_mistral: 53.01\\n      re_docred_test_f1_mistral: 51.91\\n      re_docred_dev_f1_vicuna: 54.29\\n      re_docred_test_f1_vicuna: 53.84\\n      docred_dev_f1_llama3: 45.76\\n      docred_test_f1_llama3: 45.96\\n      re_docred_dev_f1_llama3: 52.28\\n      re_docred_test_f1_llama3: 51.97\\n      backbone: \\\"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\n\\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\\n  # (NEW - 2026-05-15 evidence generation survey)\\n\\n  - title: \\\"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\\\"\\n    authors: Sprague et al.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2410.21333\\n    category: evidence_generation_tradeoff\\n    role: key_evidence\\n    key_finding: >\\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\\n    relevance_to_evidence_tradeoff: >\\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\\\"显式推理\\\"，\\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\\n      Related Work 引用点：evidence generation 作为 structured explanation，\\n      与 CoT 共享\\\"显式推理降低主任务性能\\\"的普遍模式。\\n\\n  - title: \\\"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\"\\n    authors: Xie et al. (Google Research)\\n    year: 2022\\n    venue: ACL Findings 2022\\n    url: https://arxiv.org/abs/2106.08657\\n    category: evidence_generation_tradeoff\\n    role: closest_docre_precedent\\n    key_finding: >\\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\\n    relevance_to_evidence_tradeoff: >\\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\\n      而非 joint generation——暗示 joint generation 会引入 noise。\\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\\n\\n  - title: \\\"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\\\"\\n    authors: Resck, Raimundo, Poco\\n    year: 2024\\n    venue: NAACL Findings 2024\\n    url: https://arxiv.org/abs/2404.03098\\n    category: evidence_generation_tradeoff\\n    role: formal_framework\\n    key_finding: >\\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\\n      但存在 Pareto optimal 解平衡两者。\\n    relevance_to_evidence_tradeoff: >\\n      提供了 performance-explainability trade-off 的形式化框架。\\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\\n\\n  - title: \\\"The Decreasing Value of Chain of Thought in Prompting\\\"\\n    authors: Meincke, Mollick, Mollick, Shapiro\\n    year: 2025\\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\\n    category: evidence_generation_tradeoff\\n    role: empirical_support\\n    key_finding: >\\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\\n      （variability 增加导致原本正确的被改错）。\\n    relevance_to_evidence_tradeoff: >\\n      支持\\\"更强的 SFT 模型不需要在生成时显式输出 evidence\\\"的论点。\\n      我们的 evidence-only SFT 的性能下降符合\\\"显式推理的边际收益递减\\\"模式。\\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\\n\\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\\n\\n  - title: \\\"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\\\"\\n    authors: Jiang, Chen et al.\\n    year: 2023\\n    venue: NeurIPS 2023\\n    url: https://arxiv.org/abs/2301.12618\\n    category: negative_transfer\\n    role: theoretical_framework\\n    key_finding: >\\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\\n    relevance_to_evidence_tradeoff: >\\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\\\"拖累\\\"RE。\\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\\n      inference-time verification，避免了 training-time 的 negative transfer。\\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\\n\\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\\n\\n  - title: \\\"Correctness is not Faithfulness in RAG Attributions\\\"\\n    authors: Wallat, Heuss, de Rijke, Anand\\n    year: 2024\\n    venue: SIGIR 2025\\n    url: https://arxiv.org/abs/2412.18004\\n    category: faithfulness_accuracy_tradeoff\\n    role: key_conceptual_framework\\n    key_finding: >\\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\\n    relevance_to_evidence_tradeoff: >\\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\\n      同时不牺牲 RE accuracy。\\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\\n\\n  - title: \\\"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\\\"\\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\\n    year: 2024\\n    venue: TACL 2024\\n    url: https://arxiv.org/abs/2307.16877\\n    category: faithfulness_accuracy_tradeoff\\n    role: evaluation_framework\\n    key_finding: >\\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\\n    relevance_to_evidence_tradeoff: >\\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\\\"同时输出正确 triples 和\\n      faithful evidence\\\"是 multi-objective optimization 问题。\\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\\n\\n  - title: \\\"Towards Faithful Model Explanation in NLP: A Survey\\\"\\n    authors: Lyu, Havaldar, Stein et al.\\n    year: 2024\\n    venue: Computational Linguistics (MIT Press)\\n    url: https://aclanthology.org/2024.cl-2.6/\\n    category: faithfulness_accuracy_tradeoff\\n    role: comprehensive_survey\\n    key_finding: >\\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\\n      识别了 faithfulness-performance trade-off 作为核心挑战：\\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\\n    relevance_to_evidence_tradeoff: >\\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\\n      我们的 CED reranker 正是该综述建议的\\\"post-hoc verification\\\"方向的具体实例。\\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\\n\\n  # === Category 12: Reranking / Verification as Bridge ===\\n\\n  - title: \\\"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\\\"\\n    authors: Yehudai, Carmeli, Mass et al.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2401.14367\\n    category: reranking_verification_bridge\\n    role: methodological_precedent\\n    key_finding: >\\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\\n    relevance_to_evidence_tradeoff: >\\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\\n      在不牺牲主任务质量的前提下确保 grounding quality。\\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\\n\\n  # === Category 13: Evidence-Grounded RL (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\\\"\\n    authors: Ben Tamo, Lu, Marteau, Nnamdi, Wang\\n    year: 2026\\n    venue: arXiv 2603.19532\\n    url: https://arxiv.org/abs/2603.19532\\n    category: evidence_grounded_rl\\n    role: closest_competitor\\n    key_finding: >\\n      用 GRPO 同时优化 grounding（evidence entailment）和 correctness（答案准确性）。\\n      在 cardiac diagnosis（Llama-3.2-3B）上 F1@3 从 37.0→54.5，grounding 从 47.6→78.2，\\n      hallucination 降 5 倍。在 legal reasoning（Llama-3.1-8B）上 faithfulness 从 32.8%→67.6%。\\n      核心：证据一致性 reward 不牺牲 task accuracy 的前提下大幅提升 faithfulness。\\n    relevance_to_freige: >\\n      **最直接的 novelty 威胁。** EvidenceRL 与 FREIGE 共享核心 idea：用 GRPO + evidence faithfulness reward\\n      训练更可靠的模型。关键差异：(1) EvidenceRL 在 QA 域（cardiac/legal），不涉及 DocRE 的 structured output；\\n      (2) EvidenceRL 未报告 evidence generation 的 performance cost（evidence tax）——它的 grounding 和\\n      correctness 同时提升，而我们发现 DocRE 中两者存在 ~8pp 张力；\\n      (3) EvidenceRL 不涉及 task decoupling 现象（QLoRA-specific）；\\n      (4) EvidenceRL 无 inference-time reranking（CED reranker）。\\n      定位策略：EvidenceRL 证明 evidence-grounded RL 在 QA 域有效，\\n      我们揭示 DocRE structured output 带来的独特挑战（evidence tax、task decoupling）和解法（CED reranker）。\\n\\n  # === Category 14: Multi-Objective GRPO (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: Ichihara, Jinnai, Morimura, Sakamoto, Mitsuhashi, Uchibe\\n    year: 2025\\n    venue: arXiv 2509.22047\\n    url: https://arxiv.org/abs/2509.22047\\n    category: multi_objective_grpo\\n    role: related_method\\n    key_finding: >\\n      GRPO 在多目标设置下易发生 reward hacking——只优化一个目标而牺牲其他目标。\\n      MO-GRPO 用 variance-based normalization 自动平衡多个 reward function 的权重，\\n      在多臂赌博机、控制、机器翻译、指令遵从四个域上实现稳定学习。\\n    relevance_to_freige: >\\n      CED reward 本质是多目标（extraction F1 + evidence quality）。MO-GRPO 的分析\\n      解释了为什么单一 extraction F1 reward 下模型可能 hack 到 \\\"忽略 evidence 只抽 triple\\\" 的策略。\\n      CED 从 reward 设计端解决，MO-GRPO 从算法端解决，互补视角。\\n\\n  - title: \\\"Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization\\\"\\n    authors: Bai, Liu, Zhuang, Zhou, Weng, Chen, Wang, Cai\\n    year: 2026\\n    venue: arXiv 2605.13641\\n    url: https://arxiv.org/abs/2605.13641\\n    category: multi_objective_grpo\\n    role: related_method\\n    key_finding: >\\n      GRPO 聚合 mixed-reward 时直接求和再归一化会淹没弱信号 reward 维度。\\n      RDPO 用 Magnitude-Aware Quantile normalization + Mahalanobis whitening\\n      去相关 reward 子空间，改善 LLM post-training 的多目标平衡。\\n    relevance_to_freige: >\\n      CED reward 的 evidence quality 维度与 extraction F1 天然低相关（r<0.3），\\n      RDPO 的理论预测这种低相关多维 reward 更易优化。\\n      为 CED 的 training-stabilizing 效果提供另一个理论解释角度。\\n\\n  # === Category 15: GRPO Theory (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"GRPO is Secretly a Process Reward Model\\\"\\n    authors: Sullivan, Koller\\n    year: 2025\\n    venue: under review at ICML 2026\\n    url: https://arxiv.org/abs/2509.21154\\n    category: grpo_theory\\n    role: theoretical_insight\\n    key_finding: >\\n      证明 GRPO + ORM 在特定条件下等价于 PRM-aware RL objective。\\n      提出 λ-GRPO 修正 GRPO 在不均匀 process step 上的 deficiency，\\n      在 downstream reasoning 上超越标准 GRPO 且训练更快收敛。\\n    relevance_to_freige: >\\n      DocRE structured output（multi-triple generation）可视为多步 process。\\n      GRPO 隐式的 PRM 性质可能解释了为什么 extraction-only reward\\n      在文档级 multi-triple 场景下训练信号不足——单一 outcome reward\\n      无法为每个 triple 的生成步骤提供有效 process-level credit assignment。\\n      CED 通过 evidence quality 为每个 triple 提供了更细粒度的信号，\\n      等效于增强了 process-level reward 的分辨率。\\n\\n  - title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: Wang et al. (23 authors)\\n    year: 2026\\n    venue: arXiv 2604.13602\\n    url: https://arxiv.org/abs/2604.13602\\n    category: grpo_theory\\n    role: theoretical_framework\\n    key_finding: >\\n      提出 Proxy Compression Hypothesis (PCH)：reward hacking 源于 objective compression、\\n      optimization amplification、evaluator-policy co-adaptation 三者交互。\\n      识别了 perception-reasoning decoupling 作为多模态中 reward hacking 的表现之一。\\n    relevance_to_freige: >\\n      PCH 框架可解释我们观察到的 extraction-evidence decoupling：\\n      QLoRA 的 compressed representation space 下，模型可能将 extraction 和 evidence\\n      两个子目标压缩到部分重叠的 proxy 空间，导致 optimization amplification\\n      使模型专注于更容易优化的 extraction 而忽略 evidence。\\n      bf16 下不复现可能因为 full-rank update 的 representation space 更充裕。\\n\\n  # === Category 16: Training Precision & RL Stability (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"Defeating the Training-Inference Mismatch via FP16\\\"\\n    authors: Qi, Liu, Zhou, Pang, Du, Lee, Lin\\n    year: 2025\\n    venue: arXiv 2510.26788\\n    url: https://arxiv.org/abs/2510.26788\\n    category: training_precision_rl\\n    role: key_evidence\\n    key_finding: >\\n      BF16 在 RL fine-tuning 中引入大的 rounding error 导致 training-inference 不一致，\\n      BF16 训练常在 150-600 步崩溃。仅切换到 FP16 即可消除不一致，\\n      提供更稳定训练、更快收敛和更优性能，只需改几行代码。\\n    relevance_to_freige: >\\n      直接相关我们的 QLoRA GRPO 不稳定性发现。QLoRA 在 4-bit 量化基础上\\n      使用 bf16/fp16 adapter，量化+低精度的 compounding error 可能是\\n      task decoupling 现象的底层原因之一。该论文提供了 precision-instability\\n      的机制解释，支持我们 \\\"QLoRA-specific decoupling\\\" 的发现——\\n      低精度 representation 放大了多目标 RL 中子任务间的 gradient 干扰。\\n\\n  # === Category 17: RL for Scientific IE (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"R²GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO\\\"\\n    authors: Li, Di, Liu, Jing, Qiu, Chen\\n    year: 2025\\n    venue: arXiv 2505.22068\\n    url: https://arxiv.org/abs/2505.22068\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：MimicSFT（structured reasoning template，无需高质量 CoT 数据）\\n      + R²GRPO（relevance reward + rule-mining reward），\\n      在科学信息抽取 RE benchmark 上超越 baseline LLM 和 specialized supervised model。\\n    relevance_to_freige: >\\n      R²GRPO 的 rule-based reward 设计与我们的 CED reward 有相似动机——\\n      都是引入 task-specific 结构化 reward 替代单纯 F1 metric reward。\\n      差异：R²GRPO 的 rule 是 dataset-level 频繁模式（类似 Ru-LLM），\\n      CED 是 instance-level evidence faithfulness 判别。\\n      R²GRPO 未涉及 evidence generation 或 DocRE。\\n\\n  # === Category 18: LLM Alignment for IE (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\"\\n    authors: Qi, Peng, Wang, Xu, Hou, Li\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://arxiv.org/abs/2405.05008\\n    category: llm_ie_alignment\\n    role: key_baseline\\n    key_finding: >\\n      构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。\\n      支持 closed/open/on-demand IE 三种模式。\\n      基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。\\n    relevance_to_freige: >\\n      ADELIE 是 IE alignment 的代表性工作，用 SFT+DPO 替代 RSFT+GRPO。\\n      我们的工作与 ADELIE 在 training paradigm 上有可比性——\\n      ADELIE 用 DPO（offline preference optimization），我们用 RSFT（offline rejection sampling）。\\n      关键差异：ADELIE 覆盖通用 IE，不涉及 evidence generation 或 DocRE-specific challenges；\\n      我们专注于 DocRE + evidence grounding 的 trade-off。\\n\\n  # === Category 19: Unfaithful Reasoning / Post-Rationalization (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"Chain-of-Thought Is Not Explainability\\\"\\n    authors: Barez et al.\\n    year: 2025\\n    venue: Oxford WhiteBox Technical Report\\n    url: https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf\\n    category: unfaithful_reasoning\\n    role: conceptual_support\\n    key_finding: >\\n      CoT 仅仅 rationalize（事后合理化）而非 report（忠实报告）模型的真实决策过程。\\n      小的操纵即可改变 CoT 的推理链但不改变模型实际决策。\\n      模型会 silently correct 错误而不在 CoT 中体现。\\n    relevance_to_freige: >\\n      支持我们 evidence generation 分析的一个维度：模型生成的 evidence sentences\\n      可能是 post-rationalization 而非真正驱动 RE 决策的信号。\\n      CED reranker 用 NLI verification 检查 evidence 的实际 entailment\\n      而非信任模型自报告的 evidence，本质上是对 post-rationalization 的防御。\\n\\n  - title: \\\"Characterizing Large Language Models as Rationalizers of Knowledge-Grounded Dialogue\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ACL Findings 2024\\n    url: https://aclanthology.org/2024.findings-acl.484.pdf\\n    category: unfaithful_reasoning\\n    role: empirical_evidence\\n    key_finding: >\\n      LLM 在 knowledge-grounded dialogue 中普遍表现为 rationalizer 而非 faithful reasoner，\\n      模型的 explanation 与其实际使用的 knowledge evidence 不一致。\\n    relevance_to_freige: >\\n      与我们的发现呼应：DocRE 中模型可能输出看似合理的 evidence sentences\\n      但实际 RE 决策并不依赖这些 evidence。这解释了为什么 joint evidence+RE 生成\\n      对 RE 性能有负面影响——模型在学习生成 \\\"合理化解释\\\" 而非 \\\"可靠推理\\\"。\\n\\n  # === Category 20: Latent vs Explicit Reasoning Trade-off (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning\\\"\\n    authors: Chen, Zhao, Xia, Lu, Wang, Chen, Zhang, Wang, Li, Shen\\n    year: 2025\\n    venue: arXiv 2505.16782\\n    url: https://arxiv.org/abs/2505.16782\\n    category: latent_vs_explicit_reasoning\\n    role: survey\\n    key_finding: >\\n      Latent CoT 将推理从显式 token generation 解耦到 hidden state computation，\\n      在多项任务上达到与显式 CoT 相当或更优的性能，同时推理速度提升 20 倍以上。\\n      显式 CoT 的 sequential token-level 推理是 applicability 的瓶颈。\\n    relevance_to_freige: >\\n      为 evidence generation trade-off 提供更广泛的理论视角：\\n      evidence sentences 作为显式推理步骤（类似 CoT tokens）可能不是最优的推理形式。\\n      我们的 CED reranker 可被视为将 evidence reasoning 从 generation-time 显式推理\\n      转移到 inference-time 的 NLI-based 验证——类似 latent-to-explicit 的范式转换，\\n      但方向相反：不是让推理隐式化，而是让验证外部化。\\n\\n  # =========================================================================\\n  # Related Work Survey (2026-05-15): 5 directions for FREIGE paper\\n  # =========================================================================\\n\\n  # === Category 21: Evidence-Based / Faithful DocRE (Direction 1) ===\\n\\n  - title: \\\"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\\\"\\n    authors: Youmi Ma, An Wang, Naoaki Okazaki\\n    year: 2023\\n    venue: EACL 2023\\n    url: https://arxiv.org/abs/2302.08675\\n    category: evidence_based_docre\\n    role: direct-competitor\\n    key_finding: >\\n      用 evidence 信息作为监督信号引导 DocRE 系统的 attention module 关注 evidence sentences。\\n      提出 evidence retrieval (ER) self-training 策略，在无 evidence 标注的大规模数据上自动生成\\n      silver evidence 训练 ER。DocRED 上 RE 和 ER 均达 SOTA。\\n      解决了 evidence retrieval 的两大问题：高内存消耗和标注有限。\\n    relevance_to_freige: >\\n      最重要的 evidence-based DocRE 先驱工作。DREEAM 用 evidence 引导 attention（encoder-based），\\n      我们用 evidence 引导 RL reward（generative LLM）。关键代际差异：\\n      (1) DREEAM 是 encoder-based（BERT/RoBERTa），我们是 LLM generative；\\n      (2) DREEAM 的 evidence 用于注意力监督，我们的 evidence 用于 reward 设计和 CED reranking；\\n      (3) DREEAM 未量化 evidence 对 RE 的 performance cost。\\n      Related Work 必引：evidence-based DocRE 的代表性工作。\\n\\n  - title: \\\"DocGNRE: Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models\\\"\\n    authors: Junpeng Li, Zixia Jia, Zilong Zheng\\n    year: 2023\\n    venue: EMNLP 2023\\n    url: https://arxiv.org/abs/2311.07314\\n    category: evidence_based_docre\\n    role: method-component\\n    key_finding: >\\n      用 LLM（ChatGPT）+ NLI 模块半自动生成 relation triples，增强 DocRE 数据集。\\n      特别擅长 re-annotating long-tail relation types。提供四个增强训练数据集。\\n      解决了 vanilla in-context learning 无法处理 DocRE 大量细粒度 relation types 的问题。\\n    relevance_to_freige: >\\n      DocGNRE 的 NLI 验证模块与我们 CED reranker 的 NLI scoring 思路类似——\\n      都用 NLI 检查生成内容是否被文档支持。差异：DocGNRE 用 NLI 过滤数据增强，\\n      我们用 NLI 做 inference-time reranking。DocGNRE 关注数据质量，我们关注训练范式。\\n\\n  - title: \\\"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction\\\"\\n    authors: Khai Phan Tran, Xue Li\\n    year: 2025\\n    venue: arXiv 2504.06529\\n    url: https://arxiv.org/abs/2504.06529\\n    category: evidence_based_docre\\n    role: direct-competitor\\n    key_finding: >\\n      用 attentional graph-based 架构捕捉同文档内语义相似实体对间的协作模式。\\n      文档转化为 bipartite graph（entity pair nodes + sentence nodes），\\n      三子图：Entity Pair 子图建模协作、Entity Pair-Sentence 子图捕捉语义关系、\\n      Sentence 子图辅助共指推理。在 DocRED 上 evidence retrieval 和 RE 均有提升。\\n    relevance_to_freige: >\\n      CDER 是最新的 encoder-based evidence retrieval 方法，验证了 evidence 对 DocRE 的价值。\\n      与我们的关键差异：(1) CDER 是 encoder-based pipeline，我们是 LLM generative；\\n      (2) CDER 用 evidence 作为输入特征，我们用 evidence quality 作为 reward/reranking 信号；\\n      (3) CDER 未探索 evidence generation 的 performance cost。\\n\\n  - title: \\\"Evidence-aware Document-level Relation Extraction\\\"\\n    authors: Xu T, Hua W, Qu J, Li Z, Xu J, Liu A et al.\\n    year: 2022\\n    venue: CIKM 2022\\n    url: https://dl.acm.org/doi/10.1145/3511808.3557313\\n    category: evidence_based_docre\\n    role: background\\n    key_finding: >\\n      将 evidence sentence selection 建模为序列决策问题，\\n      用 RL 机制选择支撑关系的 evidence sentences。\\n      在 DocRED 上验证 evidence-aware 方法的有效性。\\n    relevance_to_freige: >\\n      早期将 RL 用于 DocRE evidence 的工作。其 RL 用于 evidence selection 策略，\\n      我们的 RL 用于整体模型微调（GRPO/RSFT）。证实 RL+evidence+DocRE 的组合有研究价值。\\n\\n  # === Category 22: Faithfulness Cost in NLP (Direction 2) ===\\n\\n  - title: \\\"Does Faithfulness Conflict with Plausibility? An Empirical Study in Explainable AI across NLP Tasks\\\"\\n    authors: Xiaolei Lu, Jianghong Ma\\n    year: 2024\\n    venue: arXiv 2404.00140\\n    url: https://arxiv.org/abs/2404.00140\\n    category: faithfulness_cost\\n    role: evaluation\\n    key_finding: >\\n      在 sentiment analysis、intent detection、topic labeling 三个 NLP 任务上\\n      系统比较 faithfulness 和 plausibility 的关系。传统 perturbation-based 方法\\n      （Shapley value、LIME）可同时达到较高 faithfulness 和 plausibility。\\n      关键发现：faithfulness 和 plausibility 并非必然冲突，\\n      可通过双目标优化同时提升。\\n    relevance_to_freige: >\\n      提供了 faithfulness-plausibility 关系的实证基础。我们的 evidence generation\\n      可视为 plausibility（evidence 看起来合理）vs faithfulness（evidence 真正驱动 RE）的张力。\\n      CED reranker 的 NLI verification 本质上是在检查 faithfulness 而非仅 plausibility。\\n\\n  - title: \\\"Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2402.04614\\n    url: https://arxiv.org/abs/2402.04614\\n    category: faithfulness_cost\\n    role: key_evidence\\n    key_finding: >\\n      LLM 擅长生成 plausible 的解释，但这些解释不一定 faithful——\\n      不与 LLM 的实际推理过程对齐。Self-explanations 的 reliability 存疑。\\n      LLM 的解释行为更像 post-hoc rationalization 而非真实推理报告。\\n    relevance_to_freige: >\\n      直接支持我们的核心论点：要求 LLM 在 DocRE 中同时生成 evidence 可能\\n      只是让模型学会 post-hoc rationalize，而非真正基于 evidence 做 RE。\\n      CED reranker 的外部 NLI verification 正是为了对抗这种 unreliable self-explanation。\\n\\n  - title: \\\"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: EMNLP 2025\\n    url: https://aclanthology.org/2025.emnlp-main.504.pdf\\n    category: faithfulness_cost\\n    role: evaluation\\n    key_finding: >\\n      通过 unlearning 推理步骤来衡量 CoT 的 faithfulness。\\n      如果 unlearn 某个推理步骤后模型行为不变，说明该步骤不 faithful。\\n      揭示了 CoT 推理步骤的 faithfulness 在不同任务和模型间差异巨大。\\n    relevance_to_freige: >\\n      提供了量化 faithfulness 的方法论。可用类似思路评估我们模型生成的 evidence\\n      是否真正影响 RE 决策。CED reranker 的 evidence corruption test\\n      本质上是这种 faithfulness 检验的 inference-time 版本。\\n\\n  # === Category 23: LoRA/QLoRA Training Artifacts (Direction 3) ===\\n\\n  - title: \\\"LoRA vs Full Fine-tuning: An Illusion of Equivalence\\\"\\n    authors: Reece Shuttleworth, Jacob Andreas, Antonio Torralba, Pratyusha Sharma\\n    year: 2024\\n    venue: arXiv 2410.21228\\n    url: https://arxiv.org/abs/2410.21228\\n    category: lora_qlora_artifacts\\n    role: key_evidence\\n    key_finding: >\\n      LoRA 和 full fine-tuning 产生结构上根本不同的权重矩阵。LoRA 引入 intruder dimensions——\\n      奇异值分解中出现新的高秩奇异向量（与预训练权重高度不相似）。Full fine-tuning 不会。\\n      LoRA 的 forgetting 几乎全部集中在 intruder dimensions。\\n      缩小 intruder dimensions 的奇异值可显著恢复预训练分布建模能力，\\n      同时仅微小影响下游任务性能。\\n    relevance_to_freige: >\\n      直接解释我们的 QLoRA GRPO decoupling 现象。LoRA/QLoRA 的 intruder dimensions\\n      可能是 extraction-evidence decoupling 的结构性原因：\\n      4-bit 量化 + LoRA 低秩约束导致 extraction 和 evidence 任务被迫共享\\n      有限的 intruder dimensions，当 RL 优化 amplify 这些维度时，\\n      两个任务的 gradient 在 intruder space 中产生干扰导致 decoupling。\\n      bf16 full fine-tuning 无 intruder dimensions 问题，因此不复现。\\n\\n  - title: \\\"The Impact of LoRA on the Emergence of Clusters in Transformers\\\"\\n    authors: Hugo Koubbi, Louis Hernandez, Matthieu Boussard\\n    year: 2024\\n    venue: arXiv 2402.15415\\n    url: https://arxiv.org/abs/2402.15415\\n    category: lora_qlora_artifacts\\n    role: theoretical_support\\n    key_finding: >\\n      用 mean-field self-attention toy model 研究 LoRA fine-tuning 的 forgetting 机制。\\n      LoRA 作为低秩扰动作用于交互粒子系统（tokens）。\\n      发现关于扰动范数和 Transformer 深度的 phase transition：\\n      超过某个阈值后从 non-forgetting 转变为 forgetting behavior。\\n      理论上界 time-to-deviation 与扰动大小和谱特性相关。\\n    relevance_to_freige: >\\n      提供了 LoRA forgetting 的理论框架。我们的 QLoRA GRPO decoupling 可能\\n      对应 phase transition 的临界区域——4-bit 量化使扰动有效范数增大，\\n      加上 GRPO 的 online 更新持续增大扰动，更容易触发 forgetting/decoupling phase transition。\\n      bf16 下扰动范数更可控，因此保持在 non-forgetting phase。\\n\\n  - title: \\\"QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs\\\"\\n    authors: NVIDIA, MIT, HKU, THU\\n    year: 2025\\n    venue: arXiv 2510.11696\\n    url: https://arxiv.org/abs/2510.11696\\n    category: lora_qlora_artifacts\\n    role: direct-competitor\\n    key_finding: >\\n      标准量化引入静态确定性噪声，对 RL 后期训练不利。但精确控制的量化噪声\\n      可通过增加 policy entropy 促进探索。Adaptive Quantization Noise (AQN) 机制\\n      动态调整噪声。结合 NVFP4 + LoRA 实现 1.5x rollout 加速。\\n      首次在单张 H100 上实现 32B LLM 的 RL 训练。\\n    relevance_to_freige: >\\n      QeRL 证明量化噪声可以被利用而非消除。与我们的发现互补：\\n      我们发现 QLoRA 的量化在多目标 RL 中导致 task decoupling（负面影响），\\n      QeRL 发现适当控制的量化噪声可促进单目标 exploration（正面利用）。\\n      差异在于：单目标场景下噪声促进探索有益，\\n      多目标场景下噪声加剧不同子任务间的 gradient 干扰。\\n\\n  - title: \\\"The Impact of Quantization on Large Reasoning Model Reinforcement Learning\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025 Workshop (Efficient Reasoning)\\n    url: https://arxiv.org/abs/2511.15694\\n    category: lora_qlora_artifacts\\n    role: key_evidence\\n    key_finding: >\\n      系统评估量化对 LRM RL 训练的影响。发现 quantization-aware RL training\\n      反而损害学习过程，PTQ 和 QLoRA 表现更好。\\n      post-RL 量化模型和 quantization-aware RL 模型在推理性能上存在显著差距。\\n    relevance_to_freige: >\\n      直接支持我们的观察：QLoRA GRPO 训练不稳定可能源于\\n      quantization 和 RL 优化的复杂交互。该论文在数学推理任务上的发现\\n      与我们在 DocRE 上的 task decoupling 观察一致——\\n      量化在 RL 训练过程中引入系统性干扰。\\n\\n  # === Category 24: GRPO / Online RL for NLP Beyond RLHF (Direction 4) ===\\n\\n  - title: \\\"ReasoningNER: A Reasoning Paradigm for Named Entity Recognition\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.11978\\n    url: https://arxiv.org/abs/2511.11978\\n    category: grpo_nlp_applications\\n    role: direct-competitor\\n    key_finding: >\\n      三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement。\\n      用 composite reward（entity F1 + format compliance）训练 GRPO policy。\\n      ReasoningNER-8B 零样本超 GPT-4 12.3 F1、超 DeepSeek-R1-32B 8.4 F1，\\n      1.7B 版本超 DeepSeek-R1-8B 10.5 F1。\\n    relevance_to_freige: >\\n      GRPO 成功应用于 IE（NER）的案例。NER reward 结构相对简单（entity-level F1），\\n      reward variance 天然较高（不同 span 组合产生多样 F1 分数）。\\n      再次支持：结构简单的 IE 任务 GRPO 成功，\\n      文档级多 triple + evidence 的复杂任务需要额外设计（CED/RSFT）。\\n\\n  - title: \\\"Posterior-GRPO: Rewarding Reasoning Processes in Code Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.05170\\n    url: https://arxiv.org/abs/2508.05170\\n    category: grpo_nlp_applications\\n    role: method-component\\n    key_finding: >\\n      在代码生成中仅对成功输出的推理过程施加 process-based reward（条件 reward），\\n      有效抑制 reward hacking——模型不能通过错误推理碰巧生成正确代码来获得高 reward。\\n      通过将 reward 条件化于最终正确性，对齐内部推理与代码正确性。\\n    relevance_to_freige: >\\n      P-GRPO 的\\\"仅对成功输出奖励推理过程\\\"与我们 RSFT 的 rejection sampling 理念一致——\\n      都是只从高质量输出中学习。P-GRPO 的 conditional reward 思路可启发 CED 改进：\\n      只在 RE 正确时奖励 evidence quality，避免\\\"evidence 好但 RE 错\\\"的情况。\\n\\n  # === Category 25: Rejection Sampling Fine-Tuning / Offline RL (Direction 5) ===\\n\\n  - title: \\\"OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2412.16145\\n    url: https://arxiv.org/abs/2412.16145\\n    category: rsft_offline_rl\\n    role: direct-competitor\\n    key_finding: >\\n      基于 maximum entropy RL 的 offline 方法，联合学习 policy model 和 value function，\\n      优化 soft Bellman Equation。无需 paired preference data，\\n      实现更好的 credit assignment。学到的 value function 可免费引导 test-time tree search。\\n      在 GSM8K、MATH、ALFWorld 上超越现有 offline 方法。\\n    relevance_to_freige: >\\n      OREO 提供了比简单 RSFT 更理论化的 offline RL 框架。\\n      我们的 RSFT 可视为 OREO 的特例（无 value function，简单 threshold filtering）。\\n      Future work 方向：用 OREO 替代简单 RSFT 可能进一步提升 DocRE 性能。\\n\\n  - title: \\\"PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning\\\"\\n    authors: Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian\\n    year: 2026\\n    venue: arXiv 2601.14716\\n    url: https://arxiv.org/abs/2601.14716\\n    category: rsft_offline_rl\\n    role: key_evidence\\n    key_finding: >\\n      基于 Qwen2.5-32B 的数学推理模型。核心创新是 offline RL 方法，\\n      在训练稳定性和效率上优于 GRPO 等 online RL。\\n      AIME 2024 平均 90.9%，AIME 2025 平均 85.6%，\\n      在 Qwen2.5-32B post-training 中达 SOTA。\\n    relevance_to_freige: >\\n      强有力证据支持 offline RL > online RL 的论点。\\n      PCL-Reasoner 在数学推理上用 offline RL 超越 GRPO，\\n      与我们在 DocRE 上 RSFT 超越 GRPO 的发现一致。\\n      两个独立领域的 converging evidence 增强了\\n      \\\"structured output 任务中 offline 方法优于 online GRPO\\\"的普遍性论述。\\n\\n  - title: \\\"RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: NAACL 2024 Findings\\n    url: https://arxiv.org/abs/2402.10038\\n    category: rsft_offline_rl\\n    role: method-component\\n    key_finding: >\\n      系统性结合 rejection sampling 和 DPO。从 SFT 模型采样 k 个 response per prompt，\\n      根据 reward 分布识别 contrastive pairs，用 DPO 对齐。\\n      在有限资源环境下有效微调 LLM，超越独立的 RS、PPO 和 DPO。\\n    relevance_to_freige: >\\n      RS-DPO 提供了 rejection sampling 和 preference optimization 的桥梁方法。\\n      我们的 RSFT 只用正样本训练（SFT loss），RS-DPO 进一步利用负样本构造 preference pair。\\n      Future work 方向：可考虑用 RS-DPO 方式利用 RSFT rejected 样本做 DPO。\\n\\n  - title: \\\"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: TMLR 2024\\n    url: https://arxiv.org/abs/2304.06767\\n    category: rsft_offline_rl\\n    role: background\\n    key_finding: >\\n      RAFT 是 rejection sampling fine-tuning 的标准化框架：迭代式 generate → rank → filter → SFT。\\n      每轮生成 n 个 response，用 reward model 排序，取 top-k 做 SFT。\\n      在文本生成和对话上验证有效性，提供了 RSFT 的 canonical 实现。\\n    relevance_to_freige: >\\n      我们的 RSFT pipeline 直接基于 RAFT 框架。差异在于：\\n      (1) 我们用 verifiable reward（F1 score）替代 learned reward model；\\n      (2) 我们的 filtering 基于 extraction F1 threshold 而非 top-k ranking；\\n      (3) 我们额外引入 CED reward 维度用于 inference-time reranking。\\n\\n  # === Category 7: Evidence-based DocRE (Expanded) ===\\n\\n  - title: \\\"EAAGRE: Evidence and Axial Attention Guided Document-level Relation Extraction\\\"\\n    authors: Unknown (Computer Speech and Language)\\n    year: 2024\\n    venue: Computer Speech and Language 2024\\n    url: https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116\\n    category: evidence_docre\\n    role: related_method\\n    key_finding: >\\n      联合考虑 evidence information 和 relation triple 的全局交互。\\n      直接引导 PLM encoder 最后一层的 top-k token attention 到 evidence sentences，\\n      不引入额外可训练参数。Axial attention 建模 relation triple 之间的全局相互依赖。\\n    relevance_to_freige: >\\n      与 DREEAM 属于同一 evidence-guided attention 范式。\\n      EAAGRE 的无参数 evidence attention 与我们 CED reranker 的 post-hoc 方式形成对比——\\n      前者在 encoder 内部注入 evidence signal，后者在 generation 后验证。\\n      证明 evidence 信号无论注入位置都能提升 DocRE 性能。\\n\\n  - title: \\\"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction\\\"\\n    authors: Yanxu Mao et al.\\n    year: 2024\\n    venue: arXiv 2407.21384\\n    url: https://arxiv.org/abs/2407.21384\\n    category: evidence_docre\\n    role: related_method\\n    key_finding: >\\n      用 GCN 构建多权重矩阵引导 attention 到 evidence sentences。\\n      采用 Teacher-Student 框架：Teacher 在全监督数据上推断 evidence 并分配 token 权重，\\n      Student 用这些权重作为监督信号训练。\\n    relevance_to_freige: >\\n      GEGA 的 Teacher-Student evidence distillation 与我们的 CED reranker 在动机上一致——\\n      都试图把 evidence quality 信号从外部注入 RE 系统。\\n      差异在于 GEGA 在 training-time 蒸馏，我们在 inference-time rerank。\\n\\n  - title: \\\"KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities\\\"\\n    authors: Chengcheng Mai et al.\\n    year: 2025\\n    venue: IJCAI 2025\\n    url: https://arxiv.org/abs/2501.00571\\n    category: evidence_docre\\n    role: related_method\\n    key_finding: >\\n      通过外部知识库检索增强 DocRE 推理。构建 document graph 并用共指消解增强，\\n      检索外部知识扩展为 document knowledge graph，并用知识过滤去除无关知识。\\n      Axial attention 建立跨句逻辑推理。\\n    relevance_to_freige: >\\n      KnowRA 代表 DocRE 中\\\"更多外部信号\\\"路线，与我们\\\"让模型自己生成 evidence\\\"路线形成对比。\\n      我们的工作表明 evidence generation 有固有代价（faithfulness tax），\\n      KnowRA 绕过这个问题通过检索而非生成。\\n\\n  # === Category 8: Faithfulness in Structured Output / Evidence Quality ===\\n\\n  - title: \\\"G&O: A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction\\\"\\n    authors: Yinghao Li et al.\\n    year: 2024\\n    venue: arXiv 2402.13364\\n    url: https://arxiv.org/abs/2402.13364\\n    category: faithfulness_structured\\n    role: related_method\\n    key_finding: >\\n      将 structured IE 拆为两步：先用自然语言生成内容，再组织为目标结构。\\n      G&O 有效分离内容生成和结构化过程，减轻同时完成两个正交任务的压力。\\n      在 zero-shot NER 和 RE 上显著提升 LLM 性能。\\n    relevance_to_freige: >\\n      直接支持我们的核心发现：要求模型同时做 relation extraction 和 evidence generation\\n      相当于同时做内容生成+结构化，两个任务存在固有冲突。\\n      G&O 的 decouple 策略与我们观察到的 task decoupling 现象相呼应，\\n      但 G&O 是 prompting 层面的解耦，我们发现 RL training 中的自发解耦。\\n\\n  - title: \\\"Improved Evidence Extraction and Metrics for Document Inconsistency Detection with LLMs\\\"\\n    authors: Nelvin Tan et al.\\n    year: 2026\\n    venue: arXiv 2601.02627\\n    url: https://arxiv.org/abs/2601.02627\\n    category: faithfulness_structured\\n    role: related_method\\n    key_finding: >\\n      引入新的 evidence extraction 评估指标和 redact-and-retry 框架。\\n      提出 constrained filtering 方法，显著优于直接 prompting 的 evidence extraction。\\n      发布新的 semi-synthetic 数据集用于评估 evidence extraction。\\n    relevance_to_freige: >\\n      为 evidence extraction 质量评估提供新指标框架。\\n      我们的 EDCR 指标从 DocRE 角度评估 evidence quality，\\n      该工作从 document inconsistency 角度评估——两者互补。\\n      其 redact-and-retry 框架可启发 CED reranker 的迭代改进策略。\\n\\n  - title: \\\"Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis\\\"\\n    authors: Unknown\\n    year: 2026\\n    venue: arXiv 2602.10881\\n    url: https://arxiv.org/abs/2602.10881\\n    category: faithfulness_structured\\n    role: supporting_evidence\\n    key_finding: >\\n      LLM 在结构化 evidence extraction 中存在系统性 structural breakdown：\\n      role reversal、cross-analysis binding drift、instance compression、numeric misattribution。\\n      当任务需要稳定绑定 variables/roles/methods/effect-sizes 时性能急剧下降。\\n    relevance_to_freige: >\\n      强化我们的核心论点：LLM 生成结构化 evidence 存在系统性困难。\\n      我们发现的 faithfulness tax 可视为这类 structural failure 在 DocRE 场景的具体表现——\\n      模型在维持 relation extraction 准确性的同时难以忠实绑定 evidence sentences。\\n\\n  - title: \\\"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion (APIE)\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: AAAI 2026\\n    url: https://arxiv.org/abs/2508.10036\\n    category: faithfulness_structured\\n    role: related_method\\n    key_finding: >\\n      提出 dual-component uncertainty metric 量化 LLM 在 IE 中的 Format Uncertainty\\n      （结构语法困难）和 Content Uncertainty（语义不一致）。\\n      利用 introspective confusion 主动选择 few-shot examples 提升 IE 性能。\\n    relevance_to_freige: >\\n      APIE 的 format vs content uncertainty 分解与我们观察到的 RE vs evidence 冲突类似——\\n      format uncertainty 对应 structured output 的结构要求，\\n      content uncertainty 对应 evidence faithfulness。\\n      为理解 faithfulness tax 的来源提供额外理论视角。\\n\\n  # === Category 9: RLHF/GRPO for Structured Tasks (Expanded) ===\\n\\n  - title: \\\"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models\\\"\\n    authors: Jixiao Zhang, Chunsheng Zuo\\n    year: 2025\\n    venue: EMNLP 2025\\n    url: https://arxiv.org/abs/2504.09696\\n    category: grpo_structured\\n    role: related_method\\n    key_finding: >\\n      增强 GRPO：(1) length-regularized rewards 鼓励简洁性；\\n      (2) 对错误解的显式惩罚提升精度；\\n      (3) difficulty-aware advantage reweighting 增强泛化。\\n      解决 GRPO 的 reward sparsity、verbosity 和难度忽视问题。\\n    relevance_to_freige: >\\n      GRPO-LEAD 的 length penalty 与我们观察到的 evidence generation 增加输出长度导致性能下降相关。\\n      其 difficulty-aware reweighting 可启发 CED reward 对不同难度 relation triple 的差异化处理。\\n      但 GRPO-LEAD 针对数学推理的单一任务，我们面对 multi-objective（RE + evidence）。\\n\\n  - title: \\\"E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: ICLR 2026\\n    url: https://arxiv.org/pdf/2510.24694\\n    category: grpo_structured\\n    role: closest_prior_work\\n    key_finding: >\\n      提出 entity-aware reward function，对 negative samples 基于 entity match rate 给 partial credit。\\n      利用 ground-truth entities 作为 factual correctness 的 proxy，\\n      区分 \\\"near-miss\\\"（中间推理正确但最终答案错误）和完全失败。\\n    relevance_to_freige: >\\n      E-GRPO 的 entity-aware partial credit 与我们 CED reward 的设计理念高度一致——\\n      都是引入 task-specific fine-grained reward signal 替代 binary reward。\\n      差异在于 E-GRPO 用 entity match 作为 reward，我们用 evidence quality (NLI-based)。\\n      E-GRPO 是 training-time reward，CED 是 inference-time reranking。\\n\\n  - title: \\\"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\\\"\\n    authors: Hangzhan Jin et al.\\n    year: 2025\\n    venue: arXiv 2508.16546\\n    url: https://arxiv.org/abs/2508.16546\\n    category: grpo_structured\\n    role: supporting_evidence\\n    key_finding: >\\n      RL-FT 可恢复 SFT 导致的大部分 OOD 性能损失，但当 SFT 造成严重 overfitting 时 RL 无法完全恢复。\\n      OOD 性能退化和恢复主要与 singular vector 方向旋转相关，而非 singular value 变化。\\n      恢复 top 20% singular values 对应方向可恢复 70-80% OOD 性能。\\n    relevance_to_freige: >\\n      解释我们的 RSFT→GRPO pipeline 设计合理性。\\n      RSFT（SFT 变体）可能引入 distribution shift，后续 GRPO 可部分修复。\\n      但如果 RSFT 过度拟合单一任务（如只优化 F1），GRPO 的修复能力有限——\\n      这与我们观察到的 QLoRA GRPO 中 task decoupling 一致。\\n\\n  - title: \\\"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: Springer 2025\\n    url: https://link.springer.com/chapter/10.1007/978-3-032-21300-6_50\\n    category: grpo_structured\\n    role: related_method\\n    key_finding: >\\n      将多目标强化学习应用于事件抽取，在 instruction-tuned LLM 基础上用 RL 优化抽取性能。\\n      证明 RL 在 IE 任务中可以有效提升 LLM 的结构化输出质量。\\n    relevance_to_freige: >\\n      与我们的 GRPO for DocRE 属于同一 paradigm——用 RL 优化 IE 任务的 LLM。\\n      事件抽取的多目标（trigger identification + argument extraction）\\n      与 DocRE 的多目标（relation extraction + evidence generation）有结构相似性。\\n\\n  # === Category 10: QLoRA vs Full Fine-tuning (Expanded) ===\\n\\n  - title: \\\"How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness\\\"\\n    authors: Darshita Rathore et al.\\n    year: 2025\\n    venue: IJCNLP-AACL 2025\\n    url: https://arxiv.org/abs/2512.15634\\n    category: qlora_fft_gap\\n    role: supporting_evidence\\n    key_finding: >\\n      中等 rank (r=32-64) 在表征能力和稳定性之间达到最佳平衡。\\n      LoRA 在某些推理任务上可与 full fine-tuning 媲美甚至超越。\\n      跨域评估时 LoRA-tuned 模型展现出 robust generalization，\\n      表明 LoRA 学习的是可迁移的抽象技能而非记忆领域特定事实。\\n    relevance_to_freige: >\\n      为我们的 QLoRA rank 选择提供实证指导。\\n      我们使用的 QLoRA (r=16) 可能处于 rank 不足区间，\\n      解释为何 QLoRA GRPO 出现 task decoupling——rank 太低无法同时编码两个任务的更新。\\n      建议未来实验尝试 r=32-64 观察是否缓解 decoupling。\\n\\n  - title: \\\"RandLoRA: Full-rank Parameter-Efficient Fine-tuning of Large Models\\\"\\n    authors: Paul Albert et al.\\n    year: 2025\\n    venue: ICLR 2025\\n    url: https://arxiv.org/abs/2502.00987\\n    category: qlora_fft_gap\\n    role: related_method\\n    key_finding: >\\n      通过学习 fixed random matrices 的 diagonal scaling 实现 full-rank 更新，\\n      保持参数效率同时突破 low-rank 限制。\\n      在 vision-language 任务上显著缩小甚至消除 standard fine-tuning 与 LoRA 的性能差距。\\n    relevance_to_freige: >\\n      直接回应我们的 QLoRA 限制问题。\\n      如果 QLoRA 的 low-rank 约束导致 multi-objective GRPO 中 task decoupling，\\n      RandLoRA 的 full-rank PEFT 可能是解决方案——\\n      在保持内存效率的同时提供足够的表征能力同时编码 RE 和 evidence generation。\\n\\n  # === Category 11: Multi-task Learning Trade-offs in IE (Expanded) ===\\n\\n  - title: \\\"C-LoRAE: Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for Unified Multimodal Information Extraction\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2505.06303\\n    url: https://arxiv.org/abs/2505.06303\\n    category: mtl_ie_tradeoff\\n    role: closest_prior_work\\n    key_finding: >\\n      扩展 LoRA 引入 universal expert（跨任务共享知识）和 task-specific experts。\\n      用 mutual information maximization 促进 expert 间信息交换。\\n      Achievement-based multi-task loss 根据当前各任务性能动态平衡训练进度。\\n    relevance_to_freige: >\\n      C-LoRAE 的 universal + task-specific expert 架构直接对应我们的 RE + evidence 多任务设定。\\n      其 achievement-based loss 可启发 CED reward 中 RE 和 evidence 维度的动态权重调整。\\n      C-LoRAE 从架构层面解决 gradient conflict，我们从 reward design 层面解决。\\n\\n  - title: \\\"Ortho-LoRA: Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection\\\"\\n    authors: Ziyu Yang et al.\\n    year: 2026\\n    venue: arXiv 2601.09684\\n    url: https://arxiv.org/abs/2601.09684\\n    category: mtl_ie_tradeoff\\n    role: related_method\\n    key_finding: >\\n      针对 LoRA 的 bipartite 结构设计 gradient projection 方法。\\n      动态将冲突任务梯度投影到彼此的正交补空间，在 LoRA 固有子空间内解决冲突。\\n      解决 multi-task LoRA 中的 negative transfer 问题。\\n    relevance_to_freige: >\\n      直接解释我们的 QLoRA GRPO task decoupling：\\n      RE 和 evidence generation 的 gradient 在 low-rank 空间中冲突，\\n      QLoRA 的有限容量加剧这种冲突导致 task 自发解耦。\\n      Ortho-LoRA 的正交投影方法可作为 QLoRA GRPO 的改进方向。\\n\\n  - title: \\\"Proactive Gradient Conflict Mitigation in Multi-Task Learning: A Sparse Training Perspective\\\"\\n    authors: Zhi Zhang et al.\\n    year: 2024\\n    venue: arXiv 2411.18615\\n    url: https://arxiv.org/abs/2411.18615\\n    category: mtl_ie_tradeoff\\n    role: supporting_evidence\\n    key_finding: >\\n      从 Sparse Training 角度缓解 gradient conflict：\\n      选择原始模型参数子集同时学习多任务，冻结其余参数。\\n      将高维空间优化问题转为低维问题，限制每个任务的 gradient update 影响范围。\\n      可与 gradient manipulation 技术结合进一步提升效果。\\n    relevance_to_freige: >\\n      QLoRA 本质上就是一种 sparse training（只更新 low-rank adapter），\\n      但 sparse training 的 proactive conflict mitigation 需要 task-aware 的参数选择，\\n      而 QLoRA 的参数选择是 task-agnostic 的。\\n      这解释了为什么 QLoRA 在 multi-objective GRPO 中表现不如预期——\\n      它的 sparsity 模式不是为多任务优化设计的。\\n\\n  # === Category 12: Generative IE Surveys ===\\n\\n  - title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n    authors: Unknown\\n    year: 2024\\n    venue: Frontiers of Computer Science 2024\\n    url: https://arxiv.org/abs/2312.17617\\n    category: survey\\n    role: survey\\n    key_finding: >\\n      全面综述 LLM 在 IE 各子任务（NER、RE、EE 等）中的应用。\\n      按 IE 子任务和技术分类，实证分析最先进方法和新兴趋势。\\n      指出 LLM-based IE 面临 structured output 质量和效率挑战。\\n    relevance_to_freige: >\\n      为我们的工作提供 broader context。FREIGE 属于 generative IE 范式——\\n      用 LLM 生成结构化 RE 输出。该 survey 的分类框架帮助定位 FREIGE 在 generative IE 生态中的位置：\\n      我们是首个系统研究 generative DocRE 中 evidence generation 代价的工作。\\n\\n  # === Category 13: Inference-Time Reranking / Best-of-N (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment\\\"\\n    authors: Audrey Huang et al.\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://arxiv.org/abs/2503.21878\\n    category: inference_time_reranking\\n    role: key_baseline\\n    key_finding: >\\n      Best-of-N sampling provably suffers from reward hacking when N is large.\\n      提出 InferenceTimePessimism 算法，通过 pessimism in the face of uncertainty\\n      实现 scaling-monotonic 性能（性能不随 N 增大而退化）。\\n      强调 pre-trained policy 对高质量 response 的 coverage 是 BoN 成功的关键。\\n    relevance_to_freige: >\\n      直接对应 CED reranker 的理论基础。CED 作为 inference-time reward model 选择最佳候选，\\n      该论文的 pessimism 原则可指导 CED reranker 的 threshold 设计——\\n      避免过度信任 CED score 导致 reward hacking。\\n\\n  - title: \\\"Inference-Time Reward Hacking in Large Language Models\\\"\\n    authors: Yiwei Chen et al.\\n    year: 2025\\n    venue: NeurIPS 2025 Spotlight\\n    url: https://arxiv.org/abs/2506.19248\\n    category: inference_time_reranking\\n    role: related_analysis\\n    key_finding: >\\n      证明 BoN 中 true reward 先升后降的 hacking pattern 是所有 inference-time 机制的固有属性。\\n      提出 Best-of-Poisson (BoP) 高效近似最优 reward-KL tradeoff policy，\\n      以及 HedgeTune 自动寻找最优 inference-time 参数。\\n    relevance_to_freige: >\\n      CED reranker 本质上是 inference-time 对齐。此论文警示：\\n      即使 CED score 是高质量 reward，过度优化（选 N 过大）仍可能退化。\\n      HedgeTune 的思路可用于自动选择 CED reranker 的最优 N。\\n\\n  - title: \\\"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models\\\"\\n    authors: Yinlam Chow et al.\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://arxiv.org/abs/2412.15287\\n    category: inference_time_reranking\\n    role: method_component\\n    key_finding: >\\n      提出 inference-aware fine-tuning 范式：训练时直接优化 BoN inference 策略的性能。\\n      设计 imitation learning 和 RL 方法克服 BoN 中不可微的 argmax 操作。\\n      BoN-aware 模型隐式学习 exploration-exploitation meta-strategy，\\n      交替生成最优 response 和多样性 response。\\n    relevance_to_freige: >\\n      FREIGE 的 RSFT+CED reranker 是 train-then-rerank 两阶段。\\n      此论文暗示更优方案：将 CED reranker 信号直接融入训练目标，\\n      使模型生成 BoN-aware 的多样输出而非事后选择。\\n\\n  - title: \\\"Evaluation of Best-of-N Sampling Strategies for Language Model Alignment\\\"\\n    authors: Yuki Ichihara et al.\\n    year: 2025\\n    venue: TMLR 2025\\n    url: https://arxiv.org/abs/2502.12668\\n    category: inference_time_reranking\\n    role: evaluation\\n    key_finding: >\\n      系统评估 BoN 采样的 reward hacking 问题。\\n      提出 Stochastic Regularized BoN (SRBoN) 有理论保证的方法。\\n      发现简单的 Sentence Length Regularized BoN 也能获得 comparable 性能。\\n    relevance_to_freige: >\\n      CED reranker 的 regularization 策略参考。\\n      FREIGE 中 CED score 作为 evidence quality proxy，\\n      可借鉴 SRBoN 的正则化思路防止 CED reranker over-optimize evidence 而牺牲 extraction quality。\\n\\n  - title: \\\"Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment\\\"\\n    authors: Yuu Jinnai et al.\\n    year: 2024\\n    venue: NAACL 2025\\n    url: https://arxiv.org/abs/2404.01054\\n    category: inference_time_reranking\\n    role: related_method\\n    key_finding: >\\n      MBR-BoN：用 Minimum Bayes Risk 目标作为 proximity regularizer 缓解 reward hacking。\\n      MBR 目标量化 response 与 reference policy 的接近程度。\\n      在 AlpacaFarm 和 hh-rlhf 上优于 vanilla BoN 和 MBR decoding。\\n    relevance_to_freige: >\\n      CED reranker 可借鉴 MBR 正则化——在选择最高 CED score 候选时，\\n      同时考虑候选与 base policy 的接近程度，防止选择过度偏离 extraction pattern 的输出。\\n\\n  # === Category 14: RSFT Methodology Advances (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners\\\"\\n    authors: Hyung Won Chung et al.\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2505.16322\\n    category: rsft_methodology\\n    role: related_method\\n    key_finding: >\\n      RFT/RSFT 的随机数据采样导致训练不均衡——已解决的样本被过度训练，困难样本训练不足。\\n      AdaSTaR 引入两个自适应采样原则：(1) diversity sampling 促进均衡，\\n      (2) curriculum sampling 根据模型能力动态调整数据难度。\\n      在 6 个 benchmark 全部取得最优，训练 FLOPs 平均减少 58.6%。\\n    relevance_to_freige: >\\n      直接适用于 FREIGE 的 RSFT 阶段。当前 RSFT 随机采样 CED-filtered 数据，\\n      AdaSTaR 的 curriculum 策略可优化采样——先训简单 relation pair，再逐步引入困难的多跳关系。\\n      其 diversity sampling 也可缓解 RSFT 数据中 relation type 分布不均的问题。\\n\\n  - title: \\\"RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning\\\"\\n    authors: Unknown\\n    year: 2026\\n    venue: arXiv 2601.09253\\n    url: https://arxiv.org/abs/2601.09253\\n    category: rsft_methodology\\n    role: direct_competitor\\n    key_finding: >\\n      RSFT 的 hard rejection 丢弃大量计算昂贵的负样本。\\n      RIFT 保留所有轨迹，用标量 reward 重新加权 loss，\\n      正 reward 样本鼓励正确行为，负 reward 样本提供反向梯度。\\n      引入 stabilized loss 解决 naive reward integration 的训练坍塌问题。\\n    relevance_to_freige: >\\n      FREIGE 的 RSFT 同样面临 hard rejection 的效率问题——大量生成但 CED 不达标的样本被丢弃。\\n      RIFT 的 soft reweighting 可替代 binary CED 筛选：\\n      用 CED score 作为连续 reward 加权 SFT loss，充分利用所有生成样本。\\n\\n  # === Category 15: NLI for Evidence Scoring / Faithfulness (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"FaithLens: Detecting and Explaining Faithfulness Hallucination\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2512.20182\\n    url: https://arxiv.org/abs/2512.20182\\n    category: faithfulness_nli\\n    role: method_component\\n    key_finding: >\\n      8B 参数模型通过合成训练数据 + rule-based RL 优化，\\n      在 12 个 faithfulness 检测任务上超越 GPT-4.1 和 o3。\\n      联合预测 binary label 和生成解释，提升可信度。\\n    relevance_to_freige: >\\n      FaithLens 的方法验证了 CED 的核心假设：小模型可以做高质量 faithfulness 判断。\\n      其 rule-based RL 训练策略可启发 CED reward model 的进一步优化——\\n      除 NLI entailment score 外，加入 explanation quality reward。\\n\\n  - title: \\\"PrefixNLI: Detecting Factual Inconsistencies as Soon as They Arise\\\"\\n    authors: Sapir Harary et al.\\n    year: 2025\\n    venue: arXiv 2511.01359\\n    url: https://arxiv.org/abs/2511.01359\\n    category: faithfulness_nli\\n    role: method_component\\n    key_finding: >\\n      将 NLI 从完整句子推广到任意文本前缀，训练 MiniTruePrefixes 模型。\\n      在 prefix-level entailment 上超越 baseline NLI 模型 5-14 F1。\\n      集成到 controlled decoding 框架后，LLaMA-3.2-3B 匹配 8B 模型的 faithfulness。\\n    relevance_to_freige: >\\n      PrefixNLI 可强化 CED 的实时性：不必等生成完成再评估 evidence faithfulness，\\n      在 autoregressive 生成过程中即时检测 unfaithful evidence。\\n      可作为 GRPO training 中的 token-level reward signal。\\n\\n  - title: \\\"Revisiting NLI: Towards Cost-Effective and Human-Aligned Metrics for Evaluating LLMs in Question Answering\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2511.07659\\n    url: https://arxiv.org/abs/2511.07659\\n    category: faithfulness_nli\\n    role: evaluation\\n    key_finding: >\\n      轻量 NLI scoring + 简单 lexical-match flag 在 long-form QA 上匹配 GPT-4o 准确率 (89.9%)，\\n      参数量少几个数量级。引入 DIVER-QA benchmark（3000 样本，人工标注）。\\n    relevance_to_freige: >\\n      直接支持 CED 的设计选择：用轻量 NLI 模型（而非昂贵 LLM）评估 evidence quality。\\n      DIVER-QA 的评估方法可迁移到 DocRE evidence evaluation，\\n      验证 CED score 与人类判断的一致性。\\n\\n  - title: \\\"Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards\\\"\\n    authors: Manveer Singh Tamber et al.\\n    year: 2025\\n    venue: EMNLP Industry 2025\\n    url: https://arxiv.org/abs/2505.04847\\n    category: faithfulness_nli\\n    role: evaluation\\n    key_finding: >\\n      FaithJudge 框架：利用多样化人工标注 hallucination 样本池改进 LLM-as-judge 评估。\\n      建立 evolving leaderboard 跟踪 LLM 在 RAG faithfulness 上的表现。\\n      覆盖 summarization、QA、data-to-text 三类任务。\\n    relevance_to_freige: >\\n      提供 faithfulness evaluation 的 benchmark 框架。\\n      FREIGE 的 EDCR 指标衡量 evidence-extraction decoupling，\\n      FaithJudge 的人工标注方法可用于验证 EDCR 指标的有效性。\\n\\n  # === Category 16: Evidence-Grounded DocRE Recent Work (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\\\"\\n    authors: Xu et al.\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://proceedings.mlr.press/v267/xu25am.html\\n    category: llm_docre\\n    role: direct_competitor\\n    key_finding: >\\n      构建 Document-level Knowledge Graph 捕获实体间结构信息，\\n      结合 Sentence-level Semantic RAG 检索相关上下文语义信息。\\n      设计 hybrid-prompt tuning 方法在 LLM 上集成结构和语义理解。\\n    relevance_to_freige: >\\n      ICML 2025 的 LLM-based DocRE 方法。与 FREIGE 的区别：\\n      DocKS-RAG 用 retrieval 增强输入，FREIGE 用 evidence generation 增强输出。\\n      DocKS-RAG 不显式生成 evidence，而 FREIGE 将 evidence 作为显式输出。\\n\\n  - title: \\\"COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction\\\"\\n    authors: Unknown\\n    year: 2024\\n    venue: IEEE IJCNN 2024\\n    url: https://ieeexplore.ieee.org/document/10650330/\\n    category: evidence_based_docre\\n    role: direct_competitor\\n    key_finding: >\\n      提出高效 two-hop reasoning 表示，由 evidence prediction 和 RE 联合监督。\\n      修正 Adaptive Focal Loss 解决类别不均衡。\\n      Weighted Fusion Layer 优化 evidence 利用。\\n    relevance_to_freige: >\\n      与 FREIGE 同属 evidence-enhanced DocRE，但方法路线不同：\\n      COREX 是 discriminative 模型用 evidence 注意力引导，\\n      FREIGE 是 generative 模型显式生成 evidence text。\\n      COREX 的 evidence-RE 联合训练与 FREIGE 的多任务 GRPO 思路类似。\\n\\n  - title: \\\"Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: Computers 2025\\n    url: https://www.mdpi.com/2073-431X/15/3/178\\n    category: evidence_based_docre\\n    role: related_method\\n    key_finding: >\\n      AEVS 框架：anchor discovery → grounded extraction → verification → supplement。\\n      为每个三元组提供 character-level provenance，使 faithfulness 可验证。\\n      Hallucination rate 0.23-20.23%，每样本 2.83-4.28 次 LLM 调用。\\n    relevance_to_freige: >\\n      AEVS 的 provenance tracking 理念与 FREIGE 的 evidence generation 一致——\\n      都试图让 extraction 结果可溯源。区别：AEVS 用 anchor 约束生成，\\n      FREIGE 用 CED reward 训练模型自主生成 faithful evidence。\\n      AEVS 的 verification 步骤类似 CED 的 entailment 检验。\\n\\n  # === Category 17: QLoRA/Quantization Fine-tuning Artifacts (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"Accurate and Efficient Fine-Tuning of Quantized Large Language Models Through Optimal Balance in Adaptation\\\"\\n    authors: Ao Shen, Qiang Wang, Zhiquan Lai, Xionglve Li, Dongsheng Li\\n    year: 2024\\n    venue: TACL 2025\\n    url: https://arxiv.org/abs/2407.17029\\n    category: lora_qlora_artifacts\\n    role: related_analysis\\n    key_finding: >\\n      识别量化 LLM + LoRA 的不平衡问题：adapter 输入输出过于复杂而有效可训练性不足，导致欠拟合。\\n      Q-BLoRA 简化 adapter 输入输出同时增大 rank 缓解欠拟合。\\n      QA-BLoRA 进一步支持低精度部署。\\n    relevance_to_freige: >\\n      直接解释 FREIGE 中 QLoRA GRPO 导致 evidence-extraction decoupling 的机制：\\n      量化权重的有限表征精度 + LoRA 的 rank 限制 = 双重欠拟合，\\n      多任务（RE + evidence）在此瓶颈下竞争导致任务自发解耦。\\n      Q-BLoRA 的 balanced adaptation 可能缓解此问题。\\n\\n  - title: \\\"CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2501.18475\\n    url: https://arxiv.org/abs/2501.18475\\n    category: lora_qlora_artifacts\\n    role: related_method\\n    key_finding: >\\n      QLoRA 中量化误差影响 LoRA 训练。CLoQ 用校准数据集最小化原始 LLM 与量化+LoRA 版本的\\n      逐层差异，闭式构造最优 LoRA 初始化，无需反向传播。\\n      在 ultra low-bit 宽度下显著优于现有方法。\\n    relevance_to_freige: >\\n      CLoQ 的初始化策略可缓解 FREIGE 中 QLoRA GRPO 的起点问题——\\n      更好的 LoRA 初始化 → 更小的量化-原始模型差距 → \\n      GRPO 训练起步时 RE 和 evidence 任务的表征空间更均衡，可能减轻 decoupling。\\n\\n  # =========================================================================\\n  # 2026-05-16 增量扫描: Evidence-Grounded DocRE + Faithfulness Cost +\\n  #   QLoRA/PEFT RL Artifacts + RLVR for IE + Reward Hacking Decoupling\\n  # =========================================================================\\n\\n  # === Category 26: Evidence-Supervised DocRE (NEW - 2026-05-16 scan) ===\\n\\n  - title: \\\"ESTR-DocRE: an evidence-supervised transformer reasoning framework for document-level relation extraction\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: \\\"Journal of King Saud University - Computer and Information Sciences (Springer)\\\"\\n    url: https://link.springer.com/article/10.1007/s44443-025-00331-9\\n    category: evidence_supervised_docre\\n    role: direct_competitor\\n    key_finding: >\\n      统一 evidence awareness 和 cross-entity logical reasoning。ESRM 模块通过 adaptive relevance scoring\\n      提取关键 evidence sentences 并用 multi-head attention 融合 entity representations；TDRM 模块\\n      构建 entity pair joint representations 并通过 transformer 实现跨 pair 信息交换支持 multi-hop reasoning。\\n      四个 DocRE benchmark 上一致优于 strong baselines。\\n    relevance_to_freige: >\\n      与 FREIGE Claim 1 最相关的传统方法 baseline。ESTR-DocRE 用 supervised evidence signals 指导 DocRE，\\n      但仍是 discriminative 范式（非 LLM generative）。FREIGE 的差异化：(1) 用 LLM + GRPO 做 evidence-grounded\\n      generative DocRE；(2) 揭示 evidence generation 的 performance cost（evidence tax）——ESTR-DocRE\\n      未报告 evidence 监督对 RE 性能的影响方向。\\n\\n  - title: \\\"Dual reasoning enhanced document-level relation extraction\\\"\\n    authors: Unknown\\n    year: 2026\\n    venue: \\\"Neural Computing and Applications (Springer)\\\"\\n    url: https://link.springer.com/article/10.1007/s00521-026-12099-8\\n    category: evidence_supervised_docre\\n    role: related_method\\n    key_finding: >\\n      双推理增强 DocRE：GRM（两阶段 GCN + multi-head attention + entity co-occurrence guidance）\\n      和 TRM（Transformer contextual fusion for entity pair interaction）。\\n      解决传统方法难以综合利用完整文档上下文的问题。\\n    relevance_to_freige: >\\n      又一个证据驱动的 DocRE 方法，但仍是 discriminative pipeline。\\n      FREIGE 的 generative 范式和 evidence tax 发现是明确差异化点。\\n\\n  # === Category 27: Faithfulness Benchmarking (NEW - 2026-05-16 scan) ===\\n\\n  - title: \\\"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning\\\"\\n    authors: Unknown\\n    year: 2026\\n    venue: ICLR 2026\\n    url: https://arxiv.org/abs/2510.04040\\n    category: faithfulness_benchmark\\n    role: evaluation\\n    key_finding: >\\n      首个 instance-level CoT faithfulness benchmark。FINE-CoT 包含 1000+ trajectories（4 个 LLM × 4 个 domain），\\n      300+ unfaithful instances with fine-grained causes and step-level evidence。\\n      系统评估 11 种检测方法（counterfactual, logit-based, LLM-as-judge）。\\n      LLM-as-judge 一致优于其他方法；logit-based 最差。\\n    relevance_to_freige: >\\n      为 FREIGE Claim 1（evidence tax）提供方法论支撑：FaithCoT-Bench 的 faithfulness 定义和\\n      评估方法可用于评估 FREIGE 的 evidence generation 是否 faithful。\\n      不过 FaithCoT-Bench 关注 CoT 推理的 faithfulness，而 FREIGE 关注 structured evidence extraction\\n      的 faithfulness，两者的 faithfulness 概念有交叉但不完全相同。\\n\\n  - title: \\\"C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning\\\"\\n    authors: Avni Mittal, Rauno Arike\\n    year: 2026\\n    venue: arXiv 2603.05167\\n    url: https://arxiv.org/abs/2603.05167\\n    category: faithfulness_benchmark\\n    role: evaluation\\n    key_finding: >\\n      从 PRM800K 构建 benchmark，评估两个互补 faithfulness 维度：\\n      causality（每步是否 logically follow 前文）和 coverage（关键中间推理是否缺失）。\\n      通过 controlled perturbations 创建 causal error + coverage deletion 样本。\\n      三个 frontier judges 在三个任务上排名不稳定，无单一 judge 主导所有设置。\\n    relevance_to_freige: >\\n      Coverage faithfulness 维度与 FREIGE evidence completeness 概念相关——\\n      evidence 是否覆盖了支持 relation 的所有关键 reasoning steps。\\n      可作为 FREIGE evaluation 方法论的理论支撑。\\n\\n  # === Category 28: Quantization + RL Training Stability (NEW - 2026-05-16 scan) ===\\n\\n  - title: \\\"QuRL: Efficient Reinforcement Learning with Quantized Rollout\\\"\\n    authors: Yuhang Li, Reena Elangovan, Xin Dong, Priyadarshini Panda, Brucek Khailany\\n    year: 2026\\n    venue: ICLR 2026\\n    url: https://arxiv.org/abs/2602.13953\\n    category: quantization_rl_stability\\n    role: related_method\\n    key_finding: >\\n      量化 rollout 加速 RL 训练（rollout 占总训练时间 70%）。提出 Adaptive Clipping Range (ACR)\\n      动态调整 clipping ratio 缓解 full-precision actor 与 quantized actor 之间的 policy ratio 偏移，\\n      防止长期训练崩溃。INT8/FP8 量化实现 20-80% rollout 加速。\\n      关键发现：decoupled PPO objective 在长 horizon 下导致 training collapse，\\n      表现为 quantized actor 和 full-precision actor 之间 divergence 指数增长。\\n    relevance_to_freige: >\\n      直接解释 FREIGE Claim 2（QLoRA GRPO decoupling）的机制：QuRL 发现量化 actor 和\\n      full-precision actor 之间的 divergence 在长训练中指数增长——这正是 QLoRA GRPO 中\\n      quantized base model 和 LoRA adapter 之间 decoupling 的理论基础。\\n      ACR 方法可作为缓解 evidence-extraction decoupling 的 potential intervention。\\n\\n  - title: \\\"QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training-Inference Mismatch\\\"\\n    authors: Unknown\\n    year: 2026\\n    venue: arXiv 2604.07853\\n    url: https://arxiv.org/abs/2604.07853\\n    category: quantization_rl_stability\\n    role: related_method\\n    key_finding: >\\n      量化 rollout 中 long-form responses 产生 repetitive garbled tokens (error tokens)。\\n      QaRL 用 TBPO (Trust-Band Policy Optimization) 的 sequence-level dual clipping 约束更新在 trust region 内。\\n      Qwen3-30B-A3B MoE 上比 quantized-rollout baseline 高 +5.5。\\n    relevance_to_freige: >\\n      QaRL 的 error token failure mode 与 FREIGE 中 QLoRA GRPO evidence generation\\n      出现 hallucinated/garbled evidence 的现象类似——都是量化精度不足导致\\n      生成质量退化。TBPO 的 trust-band 约束思路可用于 stabilize evidence generation。\\n\\n  - title: \\\"Parameter-Efficient Continual Fine-Tuning: A Survey\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2504.13822\\n    url: https://arxiv.org/abs/2504.13822\\n    category: peft_forgetting\\n    role: background\\n    key_finding: >\\n      系统综述 PECFT 方法如何在参数高效微调下缓解 catastrophic forgetting。\\n      PEFT 冻结大部分参数保留旧任务知识，但连续微调多任务仍有 forgetting 问题。\\n      CL-Plugins 等方法结合 adapter modules 和 continual learning 策略。\\n    relevance_to_freige: >\\n      为 FREIGE Claim 2 提供 survey-level context：QLoRA 的 PEFT 特性在多任务\\n      （RE + evidence）连续优化中的 forgetting 行为——当 GRPO 先学会 RE 再学 evidence 时，\\n      PEFT 的有限参数空间是否导致 evidence 知识被覆盖。\\n\\n  # === Category 29: RL vs Forgetting (NEW - 2026-05-16 scan) ===\\n\\n  - title: \\\"Reinforcement Fine-Tuning Naturally Mitigates Forgetting in Continual Post-Training\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2507.05386\\n    url: https://arxiv.org/abs/2507.05386\\n    category: rl_vs_forgetting\\n    role: related_analysis\\n    key_finding: >\\n      对比 SFT 和 RFT：SFT 导致 catastrophic forgetting，而 RFT 的梯度更新被 reward variance\\n      自然缩放，形成 data-dependent regularizer 保护已有知识。\\n      Qwen2.5-VL-7B-Instruct 上 7 个多模态任务验证。\\n      还提出 rollout-based instance filtering 提升 RFT 稳定性和效率。\\n    relevance_to_freige: >\\n      与 FREIGE Claim 2 形成重要对话：如果 RFT（RL fine-tuning）本身就比 SFT 更抗 forgetting，\\n      那么 FREIGE 观察到的 evidence-extraction decoupling 更可能是 QLoRA-specific 而非 RL-generic。\\n      这强化了 Claim 2 的 QLoRA-specific 定位。\\n\\n  - title: \\\"Why Reinforcement Fine-Tuning Enables MLLMs Preserve Prior Knowledge Better: A Data Perspective\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2506.23508\\n    url: https://arxiv.org/abs/2506.23508\\n    category: rl_vs_forgetting\\n    role: related_analysis\\n    key_finding: >\\n      SFT 快速习得新任务但导致 catastrophic forgetting；RFT 学习更慢但更好保留先验知识。\\n      从数据视角分析：RFT 主要强化与 base model 概率分布自然对齐的 correct samples，\\n      对先验知识的干扰更弱。\\n    relevance_to_freige: >\\n      进一步支持 Claim 2 的 QLoRA-specific 归因：full-precision RL 应当保留先验知识，\\n      如果 QLoRA RL 出现 decoupling 则说明量化是 key enabler。\\n      FREIGE 可引用此论文论证 \\\"RL 本身不导致 decoupling，QLoRA 的量化瓶颈才是\\\"。\\n\\n  - title: \\\"RL's Razor: Why Online Reinforcement Learning Forgets Less\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2509.04259\\n    url: https://arxiv.org/abs/2509.04259\\n    category: rl_vs_forgetting\\n    role: related_analysis\\n    key_finding: >\\n      理论分析 online RL 为何比其他方法更能缓解 catastrophic forgetting。\\n    relevance_to_freige: >\\n      与上述两篇共同构成 \\\"RL 不 forget\\\" 的证据链，强化 FREIGE 的论点：\\n      observed decoupling 是 QLoRA 量化约束而非 RL training 本身导致。\\n\\n  # === Category 30: RLVR for General Domains (NEW - 2026-05-16 scan) ===\\n\\n  - title: \\\"RLPR: Extrapolating RLVR to General Domains without Verifiers\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2506.18254\\n    url: https://arxiv.org/abs/2506.18254\\n    category: rlvr_general_domains\\n    role: method_component\\n    key_finding: >\\n      RLVR 成功局限于 math/code（依赖 domain-specific verifiers）。RLPR 用 LLM 自身 token\\n      probability 作为 reward signal 替代外部 verifier，prob-to-reward + stabilizing methods\\n      解决 noisy probability reward 的高方差。7 个 benchmark 上持续提升推理能力。\\n    relevance_to_freige: >\\n      FREIGE 也面临 verifier 设计问题——DocRE 的 evidence quality 难以用简单 rule-based reward 验证。\\n      RLPR 的 self-probability reward 思路可作为替代 CED reranker 的 training-time evidence reward。\\n\\n  - title: \\\"From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation (RLVRR)\\\"\\n    authors: Unknown\\n    year: 2026\\n    venue: ICLR 2026\\n    url: https://arxiv.org/abs/2601.18533\\n    category: rlvr_general_domains\\n    role: method_component\\n    key_finding: >\\n      RLVRR 从 high-quality references 中提取 ordered linguistic signals（reward chain），\\n      分解为 content（关键词确定性验证）和 style（LLM-based 风格验证）两个维度。\\n      在 10+ benchmarks 上大幅超越 10× 数据的 SFT 和先进 reward models。\\n    relevance_to_freige: >\\n      RLVRR 的 reward chain（将 dot supervision 分解为 content + style 序列）与 FREIGE\\n      的 CED reranker 理念相关——都试图从 coarse reward 中提取 fine-grained signal。\\n      RLVRR 的 content verification 可作为 evidence faithfulness reward 的替代设计。\\n\\n  - title: \\\"RL-Struct: A Lightweight Reinforcement Learning Framework for Reliable Structured Output in LLMs\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2512.00319\\n    url: https://arxiv.org/abs/2512.00319\\n    category: rl_for_ie\\n    role: method_component\\n    key_finding: >\\n      轻量级 RL 框架用于提升 LLM structured output 的可靠性。\\n      用 rule-based reward functions 提升结构合规性、数据有效性和整体准确性。\\n    relevance_to_freige: >\\n      与 FREIGE 共享 \\\"RL for structured IE output\\\" 的范式。RL-Struct 关注 structural reliability，\\n      FREIGE 进一步关注 evidence grounding。可作为 FREIGE 方法论的基础参考。\\n\\n  # === Category 31: Reward Hacking Diagnostics (NEW - 2026-05-16 scan) ===\\n\\n  - title: \\\"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\\\"\\n    authors: Yuchun Miao et al.\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://arxiv.org/abs/2501.19358\\n    category: reward_hacking_diagnostics\\n    role: related_method\\n    key_finding: >\\n      发现 Energy Loss Phenomenon：LLM 最后一层的 energy loss（L1 norm 差值）在 RL 训练中\\n      持续增加，过度增加标志 reward hacking。理论证明 energy loss 增加降低 contextual relevance 上界。\\n      提出 EPPO（Energy loss-aware PPO）在 reward 计算中惩罚 energy loss 增加。\\n      EPPO 可解释为 entropy-regularized RL。\\n    relevance_to_freige: >\\n      与 FREIGE Claim 4（EDCR 双层诊断工具）直接相关：energy loss 是另一种 representation-level\\n      diagnostic for reward hacking。EDCR 从 evidence-relation consistency 角度诊断，\\n      EPPO 从 hidden state energy 角度诊断——互补的诊断信号。\\n      FREIGE 可引用 EPPO 作为 \\\"diagnostic signals for RL training health\\\" 的同类工作。\\n\\n  - title: \\\"Reward Hacking Mitigation using Verifiable Composite Rewards\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2509.15557\\n    url: https://arxiv.org/abs/2509.15557\\n    category: reward_hacking_diagnostics\\n    role: related_method\\n    key_finding: >\\n      识别两种 reward hacking 行为：(1) 无推理直接给答案；(2) 非标准推理格式绕过 reward 机制。\\n      composite reward function 结合 correctness incentives + 结构性 penalties 缓解 hacking。\\n      二值 reward（非连续）更稳定——连续 reward 的 smooth gradients 被 exploit。\\n      augmenting verifiable outcome rewards with explicit penalties 将 hacking 从 0.23-0.60 降至 ≤0.06。\\n    relevance_to_freige: >\\n      与 FREIGE 的 evidence reward design 直接相关：FREIGE 的 extraction-only hack\\n      （忽略 evidence 只抽 triple）就是这里说的第一种 hacking 模式。\\n      composite reward 的 explicit penalty 思路验证了 CED reward 设计的合理性。\\n\\n  # === Category 32: Quantization + RL Precision Mismatch (NEW - 2026-05-16 targeted expansion) ===\\n\\n  - title: \\\"FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning\\\"\\n    authors: Zhaopeng Qiu, Shuang Yu, Jingqi Zhang, Shuai Zhang, Xue Huang, Jingyi Yang, Junjie Lai\\n    year: 2026\\n    venue: arXiv 2601.18150\\n    url: https://arxiv.org/abs/2601.18150\\n    category: quantization_rl_stability\\n    role: related_method\\n    key_finding: >\\n      FP8 RL 训练中 policy weights 每步变化需重复量化同步，低精度 rollout 偏离高精度 policy\\n      导致 train-inference mismatch 和训练不稳定。MoE 架构中精度差异导致 expert routing 不一致，\\n      routing inconsistencies 随训练累积使 mismatch KL 逐渐增大。\\n      通过 importance-sampling-based rollout correction 缓解，实现 44% rollout 加速。\\n    relevance_to_freige: >\\n      FP8-RL 揭示的 train-inference precision mismatch 机制直接映射到 FREIGE 的 QLoRA GRPO 场景：\\n      QLoRA 中 4-bit base + bf16 LoRA 的精度不对称与 FP8-RL 中 FP8 rollout + bf16 train 的模式相同。\\n      两者都导致 policy divergence 随训练累积——这是 evidence-extraction decoupling 的底层机制之一。\\n\\n  - title: \\\"Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow\\\"\\n    authors: Haocheng Xi, Charlie Ruan, Peiyuan Liao, Yujun Lin, Han Cai, Yilong Zhao, Shuo Yang, Kurt Keutzer, Song Han, Ligeng Zhu\\n    year: 2026\\n    venue: arXiv 2601.14243\\n    url: https://arxiv.org/abs/2601.14243\\n    category: quantization_rl_stability\\n    role: related_method\\n    key_finding: >\\n      BF16-train + FP8-rollout 策略导致严重训练不稳定和灾难性准确率崩溃（catastrophic accuracy collapse），\\n      根因是 off-policy 性质引入的训练-推理数值 mismatch。统一 FP8 精度消除此差异，\\n      实现 41% training 加速和 16% 端到端加速，同时维持稳定收敛。\\n    relevance_to_freige: >\\n      Jet-RL 的 \\\"catastrophic accuracy collapse\\\" 与 FREIGE 中 QLoRA GRPO 的 evidence 生成退化高度类似：\\n      两者都是精度不对称导致的 off-policy 效应。Jet-RL 证明统一精度可消除此问题——\\n      这支持 FREIGE C2 中 \\\"bf16 下不复现 decoupling\\\" 的观察：bf16 full fine-tuning 消除了精度不对称。\\n\\n  - title: \\\"BitRL: Reinforcement Learning with 1-bit Quantized Language Models for Resource-Constrained Edge Deployment\\\"\\n    authors: Md. Ashiq Ul Islam Sajid, Mohammad Sakib Mahmood, Md. Tareq Hasan, Md Abdur Rahim, Rafat Ara, Md. Arafat Hossain\\n    year: 2026\\n    venue: arXiv 2604.24273\\n    url: https://arxiv.org/abs/2604.24273\\n    category: quantization_rl_stability\\n    role: background\\n    key_finding: >\\n      首个系统性框架将 1-bit 量化 LLM（BitNet b1.58，三值权重）与 RL 结合。\\n      理论分析将三值量化建模为 structured parameter perturbation，推导 quantized policy gradient 的收敛界。\\n      揭示极端量化下 exploration-stability 的 trade-off——极低精度限制探索能力但保持训练稳定。\\n      维持 85-98% 的 task performance。\\n    relevance_to_freige: >\\n      BitRL 从理论角度证明量化是 \\\"structured perturbation\\\"——这为 FREIGE C2 提供了理论框架：\\n      QLoRA 的 4-bit 量化在 GRPO 的 multi-objective 优化中充当 perturbation，\\n      当 perturbation 幅度超过多任务目标的 gradient resolution 时导致 task decoupling。\\n\\n  # === Category 33: Multi-Task LoRA Decoupling (NEW - 2026-05-16 targeted expansion) ===\\n\\n  - title: \\\"FlyLoRA: Boosting Task Decoupling and Parameter Efficiency via Implicit Rank-Wise Mixture-of-Experts\\\"\\n    authors: Heming Zou, Yunliang Zang, Wutong Xu, Yao Zhu, Xiangyang Ji\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2510.08396\\n    category: multi_task_lora_decoupling\\n    role: related_method\\n    key_finding: >\\n      传统 LoRA 共享单一低秩 adapter 导致 parameter interference 和次优性能。\\n      FlyLoRA 用 implicit rank-wise MoE 实现 intra-task decoupling（细粒度 expert 分配减少干扰），\\n      inter-task decoupling 利用 random projection 的正交性使不同 LoRA 组件在不相关子空间运作。\\n      无需额外 router 参数，超越 MoE-based LoRA 的效率。\\n    relevance_to_freige: >\\n      FlyLoRA 的 rank-wise decoupling 直接解释 FREIGE C2 中 QLoRA rank 不足导致 task decoupling 的机制：\\n      当 LoRA rank 太低，RE 和 evidence extraction 两个任务的 gradient updates 在有限 rank 空间中竞争，\\n      FlyLoRA 的解决方案（分配不同 rank 给不同任务）验证了 rank capacity 是 decoupling 的关键因素。\\n\\n  - title: \\\"Decomposing the Basic Abilities of Large Language Models: Mitigating Cross-Task Interference in Multi-Task Instruct-Tuning\\\"\\n    authors: Bing Wang, Ximing Li, Changchun Li, Jinjin Chi, Gang Niu, Masashi Sugiyama\\n    year: 2026\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2605.05676\\n    category: multi_task_lora_decoupling\\n    role: theoretical_support\\n    key_finding: >\\n      多任务 instruct-tuning 中 cross-task interference 源于共享参数上的梯度冲突。\\n      发现 LLM 编码若干正交 basic abilities，任何任务可表示为这些 abilities 的线性组合。\\n      BADIT 将参数分解为正交高奇异值 LoRA experts，在训练中通过球面聚类强制正交性。\\n      在 SuperNI benchmark 上 6 个 LLM 上超越 SOTA。\\n    relevance_to_freige: >\\n      BADIT 的 \\\"tasks as linear combinations of orthogonal abilities\\\" 框架直接适用于 FREIGE：\\n      RE 和 evidence extraction 可视为两个需要部分重叠 abilities 的任务。\\n      当 QLoRA 的低 rank 限制无法同时表达两组 abilities 时，模型被迫 decouple——\\n      这是 C2 (evidence-extraction decoupling) 的 formal explanation。\\n\\n  - title: \\\"Addressing Task Conflicts in LLMs Multi-Task Fine-Tuning with Task-Specific Subnetwork Refinement\\\"\\n    authors: Wang Y., Wan C., Tian X. et al.\\n    year: 2025\\n    venue: Machine Learning (Springer) 2025\\n    url: https://link.springer.com/article/10.1007/s10994-025-06885-z\\n    category: multi_task_lora_decoupling\\n    role: related_analysis\\n    key_finding: >\\n      多任务 LLM 微调中不同任务的子网络独立运作且重叠极少。\\n      任务冲突的根因是传统训练对所有参数统一更新，一个任务的梯度破坏另一个任务的专用子网络。\\n      TSSR 通过选择性精炼各任务关联子网络缓解冲突。\\n    relevance_to_freige: >\\n      TSSR 的 \\\"subnetworks operate largely independently\\\" 发现解释了为什么 FREIGE 中\\n      RE 和 evidence extraction 在 QLoRA 受限参数空间下自发形成独立子网络（decoupling）。\\n      在 full bf16 fine-tuning 的更大参数空间中，两个子网络有足够容量共存而不冲突。\\n\\n  # === Category 34: Multi-Task RL Gradient Imbalance (NEW - 2026-05-16 targeted expansion) ===\\n\\n  - title: \\\"Imbalanced Gradients in RL Post-Training of Multi-Task LLMs\\\"\\n    authors: Runzhe Wu, Ankur Samanta, Ayush Jain, Scott Fujimoto, Jeongyeol Kwon, Ben Kretzu, Youliang Yu, Kaveh Hassani, Boris Vidolov, Yonathan Efroni\\n    year: 2025\\n    venue: Findings of EACL 2026\\n    url: https://arxiv.org/abs/2510.19178\\n    category: multi_task_rl_gradient_imbalance\\n    role: closest_prior_work\\n    key_finding: >\\n      多任务 RL post-training 中某些任务产生显著更大的梯度，偏置更新方向。\\n      大梯度任务不一定获得更大学习收益——gradient magnitude 与 performance improvement 不相关。\\n      常见训练统计量（reward, advantage, token length）无法解释此不平衡，\\n      暗示不平衡源于 inherent task differences。\\n    relevance_to_freige: >\\n      最直接相关 C2 和 C3。FREIGE 中 RE 和 evidence extraction 在 GRPO 训练中的 gradient imbalance\\n      正是此论文描述的现象：extraction 任务可能产生主导梯度，压制 evidence generation 的学习——\\n      这是 task decoupling 的 gradient-level 解释。该论文呼吁 \\\"principled gradient-level corrections\\\"，\\n      CED reward 本质上是一种 task-level correction 机制。\\n\\n  - title: \\\"Stabilizing Reinforcement Learning with LLMs: Formulation and Practices\\\"\\n    authors: Chujie Zheng et al. (Alibaba Qwen Team)\\n    year: 2025\\n    venue: arXiv 2512.01374\\n    url: https://arxiv.org/abs/2512.01374\\n    category: quantization_rl_stability\\n    role: theoretical_support\\n    key_finding: >\\n      通过一阶近似证明 sequence-level reward 可用 surrogate token-level objective 优化，\\n      但前提是 training-inference discrepancy 和 policy staleness 最小化。\\n      Token-level importance sampling 是校正 train-inference 差异的必要组件——移除后训练崩溃。\\n      30B MoE 模型上数十万 GPU 小时的实验验证。\\n    relevance_to_freige: >\\n      理论支持 FREIGE C2：QLoRA 的量化引入的 training-inference discrepancy 违反了\\n      token-level surrogate 有效的前提条件，导致 GRPO 训练不稳定。\\n      bf16 full fine-tuning 满足最小 discrepancy 条件，因此训练稳定且不出现 decoupling。\\n\\n  # === Category 35: Faithfulness Decay & Evidence Grounding (NEW - 2026-05-16 targeted expansion) ===\\n\\n  - title: \\\"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\\\"\\n    authors: Donald Ye et al.\\n    year: 2026\\n    venue: arXiv 2602.11201\\n    url: https://arxiv.org/abs/2602.11201\\n    category: faithfulness_decay\\n    role: related_analysis\\n    key_finding: >\\n      提出 Normalized Logit Difference Decay (NLDD) 度量 CoT 推理步骤的 faithfulness。\\n      发现 Reasoning Horizon (k*) 在链长度的 70-85% 处，超过后推理 token 对最终答案几乎无影响。\\n      模型可以编码正确的内部表征但完全无法完成任务——accuracy alone does not reveal faithfulness。\\n    relevance_to_freige: >\\n      与 FREIGE C1 (faithfulness cost) 和 C4 (EDCR 诊断) 相关：\\n      faithfulness decay 现象说明模型内部表征和外部输出之间存在系统性偏差，\\n      EDCR 的 evidence-relation consistency 诊断本质上在检测类似的 faithfulness decay——\\n      当 evidence 与 relation 预测 decouple 时，模型的 reasoning chain 变得 unfaithful。\\n\\n  - title: \\\"The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input\\\"\\n    authors: Google DeepMind\\n    year: 2025\\n    venue: arXiv 2501.03200\\n    url: https://arxiv.org/abs/2501.03200\\n    category: faithfulness_decay\\n    role: background\\n    key_finding: >\\n      大规模 benchmark 评估 LLM 在长文档中的 grounding 能力。860 public + 859 private 样例，\\n      要求生成完全 grounded 在提供文档中的长文本回复。使用多 judge 聚合评分缓解评估偏差。\\n      当前最佳模型 faithfulness 得分 ~0.88，说明 grounding 仍是显著挑战。\\n    relevance_to_freige: >\\n      FACTS Grounding 是 faithfulness 评估的重要 benchmark，验证了 FREIGE 的核心前提：\\n      即使最强 LLM 在 grounding 任务上也远未完美（~12% failure rate），\\n      这证明 evidence-grounded IE 中 faithfulness 约束确实会带来 performance cost (C1)。\\n\\n  # === Category 36: Evidence Cost in Generative IE (NEW - 2026-05-16 evidence cost scan) ===\\n\\n  - title: \\\"It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers\\\"\\n    authors: Zheng Tang, Mihai Surdeanu\\n    year: 2023\\n    venue: Computational Linguistics, Vol. 49, Issue 1\\n    url: https://aclanthology.org/2023.cl-1.3/\\n    category: evidence_cost_generative_ie\\n    role: direct_competitor\\n    key_finding: >\\n      Joint training of relation classifier + explanation sequence labeler (extractive rationale)。\\n      Joint training 不仅不损害 RE，反而提升 ~4% F1 on CoNLL04。\\n      Explanation classifier 操作在 extractive features 上，保证 faithfulness。\\n    relevance_to_freige: >\\n      最直接的对比论文。与 FREIGE 形成关键对照：\\n      Two Flints 在 sentence-level extractive discriminative 设定下发现 joint evidence+RE 有益；\\n      FREIGE 在 document-level generative SFT 设定下发现 joint evidence+RE 有害 (-7.7 F1)。\\n      这个差异揭示了 generative vs discriminative、sentence vs document level 的关键区别。\\n\\n  - title: \\\"Robust Explanation for Free or At the Cost of Faithfulness\\\"\\n    authors: Zeren Tan, Yang Tian\\n    year: 2023\\n    venue: ICML 2023\\n    url: https://proceedings.mlr.press/v202/tan23a.html\\n    category: evidence_cost_generative_ie\\n    role: theoretical_foundation\\n    key_finding: >\\n      首次理论证明 robustness-faithfulness trade-off 存在。\\n      Robust model 可免费获得 robust explanation；non-robust model 提升 explanation robustness\\n      需牺牲 faithfulness。对 SmoothGrad 等 6 种方法验证了该 trade-off。\\n    relevance_to_freige: >\\n      提供 \\\"faithfulness 有代价\\\" 的理论框架。虽然研究 post-hoc explanation 而非 generative evidence，\\n      但核心洞察一致：追求可解释性/忠实性可能需要牺牲其他性能维度。\\n      FREIGE 的 evidence tax 是这一理论在 generative IE 中的实证体现。\\n\\n  - title: \\\"Rationalization for Explainable NLP: A Survey\\\"\\n    authors: Sai Gurrapu et al.\\n    year: 2023\\n    venue: Frontiers in AI\\n    url: https://www.frontiersin.org/articles/10.3389/frai.2023.1225093/full\\n    category: evidence_cost_generative_ie\\n    role: background_survey\\n    key_finding: >\\n      首个 NLP rationalization 综述。列出 desiderata: \\\"rationale extraction should not hurt task performance\\\"。\\n      将 rationalization 分为 extractive 和 abstractive 两类，覆盖 2007-2023 文献。\\n      识别了 attention-based rationale 中 noisy rationale 和 prediction accuracy 之间的 trade-off。\\n    relevance_to_freige: >\\n      明确了 \\\"不应损害主任务\\\" 是学界共识 desiderata。但没有论文系统量化违反这一 desiderata 的程度。\\n      FREIGE 的 -7.7 F1 evidence tax 直接挑战了这一假设，证明在 generative SFT 中该 desiderata 不成立。\\n\\n  - title: \\\"Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction\\\"\\n    authors: Xilai Yin et al.\\n    year: 2023\\n    venue: EMNLP 2023 Findings\\n    url: https://aclanthology.org/2023.findings-emnlp.153/\\n    category: evidence_cost_generative_ie\\n    role: related_method\\n    key_finding: >\\n      CoT-ER: 用 LLM 先生成 task-specific evidence，再 CoT 推理做 few-shot RE。\\n      0% training data 下与 fully-supervised SOTA 竞争力相当（FewRel 1.0/2.0）。\\n    relevance_to_freige: >\\n      在 prompting 设定下 evidence+CoT 对 RE 有益。\\n      与 FREIGE SFT 设定下 evidence 有害形成对比——说明 evidence cost 可能是\\n      SFT 训练 specific 的问题（output format 约束 vs prompting 引导）。\\n\\n  - title: \\\"Entity and Evidence Guided Relation Extraction for DocRED\\\"\\n    authors: Kevin Huang et al.\\n    year: 2021\\n    venue: RepL4NLP @ ACL 2021\\n    url: https://aclanthology.org/2021.repl4nlp-1.30/\\n    category: evidence_cost_generative_ie\\n    role: direct_competitor\\n    key_finding: >\\n      E2GRE: DocRE 上首个 joint evidence prediction + relation extraction 框架。\\n      利用 entity-guided input 和 pretrained LM attention 作为 evidence 特征。\\n      Joint training 在 RE 和 evidence prediction 上均有增益，达到 DocRED leaderboard SOTA。\\n    relevance_to_freige: >\\n      DocRE 上 joint evidence+RE 的先驱工作。但使用 encoder-based discriminative 模型，\\n      evidence 是 binary sentence classification（非 text generation）。\\n      他们发现 joint 有益，与 FREIGE generative 设定下的发现相反——\\n      核心区别在于 discriminative attention supervision vs generative output format constraint。\\n\\n  - title: \\\"Revisiting Relation Extraction in the era of Large Language Models\\\"\\n    authors: Somin Wadhwa, Silvio Amir, Byron Wallace\\n    year: 2023\\n    venue: ACL 2023\\n    url: https://aclanthology.org/2023.acl-long.868/\\n    category: evidence_cost_generative_ie\\n    role: background\\n    key_finding: >\\n      系统评估 GPT-3 和 Flan-T5 在标准 RE 任务上的表现。\\n      Few-shot GPT-3 接近 SOTA，但 exact match 低估 generative RE 性能，需 human evaluation。\\n      建立了 LLM-based generative RE 的 evaluation methodology。\\n    relevance_to_freige: >\\n      建立了 LLM generative RE 的 baseline context，验证了 seq2seq RE 的可行性。\\n      FREIGE 在此基础上进一步探索了加入 evidence 生成后的性能变化。\\n\\n  # =========================================================================\\n  # 2026-05-16 Related Work Survey Expansion (literature scan for paper)\\n  # =========================================================================\\n\\n  # === Category 37: DocRE Foundational Benchmarks & Baselines ===\\n\\n  - title: \\\"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\\\"\\n    authors: Yuan Yao, Deming Ye, Peng Li, Xu Han, Yankai Lin, Zhenghao Liu, Zhiyuan Liu, Lixin Huang, Jie Zhou, Maosong Sun\\n    year: 2019\\n    venue: ACL 2019\\n    url: https://aclanthology.org/P19-1074/\\n    category: docre_foundational\\n    role: foundational_dataset\\n    key_finding: >\\n      首个大规模 document-level RE 数据集，从 Wikipedia 构建。5,053 篇文档，96 种关系，\\n      标注了 named entities、relations 和 supporting evidence sentences。\\n      超过 40% 的关系需要跨句推理（cross-sentence reasoning）。\\n    relevance_to_freige: >\\n      FREIGE 的主要评测数据集。DocRED 的 evidence annotation 是本项目\\n      evidence generation 研究的基础——衡量 evidence cost 和 evidence quality 均基于此标注。\\n\\n  - title: \\\"Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction\\\"\\n    authors: Qingyu Tan, Lu Xu, Lidong Bing, Hwee Tou Ng, Sharifah Mahani Aljunied\\n    year: 2022\\n    venue: EMNLP 2022\\n    url: https://aclanthology.org/2022.emnlp-main.580/\\n    category: docre_foundational\\n    role: dataset_revision\\n    key_finding: >\\n      发现 DocRED 标注存在大量 false negatives（漏标关系），重新标注 4,053 篇文档，\\n      构建 Re-DocRED。模型在 Re-DocRED 上 F1 提升约 13 点，\\n      说明原始 DocRED 的评测结果受 annotation incompleteness 严重影响。\\n    relevance_to_freige: >\\n      FREIGE 在 Re-DocRED 上评测可获得更可靠的性能数据。\\n      Re-DocRED 的 evidence annotation 也更完整，对 evidence quality 评估更公平。\\n\\n  - title: \\\"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\\\"\\n    authors: Wenxuan Zhou, Kevin Huang, Tengyu Ma, Jing Huang\\n    year: 2021\\n    venue: AAAI 2021\\n    url: https://arxiv.org/abs/2010.11304\\n    category: docre_foundational\\n    role: key_baseline\\n    key_finding: >\\n      ATLOP：引入 adaptive thresholding 替代固定阈值处理 multi-label 分类，\\n      加 localized context pooling 用 attention 聚合 entity mention-level 上下文。\\n      成为 DocRE 标准 baseline，后续几乎所有 encoder-based 方法都以此为起点。\\n    relevance_to_freige: >\\n      DocRE 领域最重要的 baseline 之一。FREIGE 的 LLM-based 方法需要与\\n      ATLOP 及其后续改进（DREEAM, SAIS 等）进行性能对比和定位。\\n\\n  - title: \\\"Document-level Relation Extraction as Semantic Segmentation\\\"\\n    authors: Ningyu Zhang, Xiang Chen, Xin Xie, Shumin Deng, Chuanqi Tan, Mosha Chen, Fei Huang, Luo Si, Huajun Chen\\n    year: 2021\\n    venue: IJCAI 2021\\n    url: https://arxiv.org/abs/2106.03618\\n    category: docre_foundational\\n    role: key_baseline\\n    key_finding: >\\n      DocuNet：将 DocRE 建模为 semantic segmentation 问题，用 entity-level 关系矩阵\\n      作为 segmentation map，U-Net 架构捕获局部和全局依赖。\\n      在 DocRED 上显著超越 ATLOP。\\n    relevance_to_freige: >\\n      encoder-based DocRE 的重要 baseline，代表了非 LLM 方法的性能上界。\\n      与 ATLOP 一起构成 FREIGE related work 中 discriminative DocRE 的对比参照。\\n\\n  # === Category 38: Evidence-Supervised DocRE (Classic Methods) ===\\n\\n  - title: \\\"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\\\"\\n    authors: Ruoting Xie, Jingqi Wang, Wei Cai, Runxin Xu, Baobao Chang\\n    year: 2022\\n    venue: NAACL 2022\\n    url: https://aclanthology.org/2022.naacl-main.171/\\n    category: evidence_supervised_docre\\n    role: direct_competitor\\n    key_finding: >\\n      通过 supervising intermediate steps（evidence retrieval）来提升 DocRE。\\n      两阶段 evidence retrieval：pooled evidence retrieval 区分有/无 supporting sentences 的 entity pairs，\\n      fine-grained evidence retrieval 为每个 relation 生成 interpretable evidence。\\n      在 DocRED/CDR/GDA 三个 benchmark 上达到 SOTA，evidence F1 超越 runner-up 5.04%。\\n    relevance_to_freige: >\\n      最直接的 prior work——同时做 RE 和 evidence prediction 的代表方法。\\n      关键区别：SAIS 是 encoder-based discriminative model 用 attention supervision，\\n      FREIGE 是 generative LLM 用 text-level evidence generation。\\n      SAIS 发现 evidence supervision 提升 RE，而 FREIGE 发现 generative evidence 有 ~8pp cost，\\n      这个差异正是 FREIGE 论文的核心发现之一。\\n\\n  # === Category 39: Knowledge Distillation for DocRE ===\\n\\n  - title: \\\"Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation\\\"\\n    authors: Qingyu Tan, Ruidan He, Lidong Bing, Hwee Tou Ng\\n    year: 2022\\n    venue: Findings of ACL 2022\\n    url: https://aclanthology.org/2022.findings-acl.132/\\n    category: knowledge_distillation_docre\\n    role: background\\n    key_finding: >\\n      KD-DocRE：用 axial attention 学习 entity pair 间依赖关系，\\n      adaptive focal loss 解决类别不均衡，knowledge distillation 弥合\\n      人工标注和远程监督数据的差异。DocRED leaderboard 上超越前 SOTA 1.36 F1。\\n    relevance_to_freige: >\\n      KD 方法在 DocRE 中有效，暗示了 FREIGE 的 RSFT（rejection sampling fine-tuning）\\n      本质上也是一种 self-distillation——用模型自身的高质量输出训练自身。\\n      但 KD-DocRE 是 encoder-based discriminative，FREIGE 是 generative paradigm。\\n\\n  - title: \\\"Document-level Relation Extraction with Progressive Self-distillation\\\"\\n    authors: Zhenlan Zhai, Shang Gao, Leilei Gan, Shan Zhao\\n    year: 2024\\n    venue: ACM TOIS 2024\\n    url: https://dl.acm.org/doi/10.1145/3656168\\n    category: knowledge_distillation_docre\\n    role: related_method\\n    key_finding: >\\n      PSD：online self-knowledge distillation 用过去预测作为 soft labels，\\n      无需额外 teacher model，单次训练即可完成。\\n      渐进式 soft label 平滑 hard label 的噪声，提升 DocRE 性能。\\n    relevance_to_freige: >\\n      Self-distillation 思路与 FREIGE 的 RSFT 有共通之处——\\n      都是利用模型自身能力产生训练信号。但 PSD 是 discriminative 模型的 label smoothing，\\n      RSFT 是 generative 模型的 output selection，机制不同。\\n\\n  # === Category 40: Evaluation for Generative RE ===\\n\\n  - title: \\\"GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\\\"\\n    authors: Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, Jiawei Han\\n    year: 2024\\n    venue: NAACL 2024\\n    url: https://aclanthology.org/2024.naacl-long.155/\\n    category: evaluation_generative_re\\n    role: evaluation_method\\n    key_finding: >\\n      传统 precision/recall 基于 exact match 无法公平评估 generative RE——\\n      LLM 输出的关系在语义上正确但与参考标注不完全匹配。\\n      提出 multi-dimensional 评估框架：topic similarity, uniqueness, granularity,\\n      factualness, completeness。发现 human-annotated relations 自身也有不完整性。\\n    relevance_to_freige: >\\n      FREIGE 使用 generative RE format，GenRES 的发现验证了\\n      exact match F1 可能低估 generative RE 性能。论文中需讨论此 evaluation limitation。\\n      但 FREIGE 的 re-DocRED evaluation 已有较完善的标签，影响可能较小。\\n\\n  # === Category 41: Self-Training / Bootstrapping for LLM Reasoning ===\\n\\n  - title: \\\"STaR: Bootstrapping Reasoning With Reasoning\\\"\\n    authors: Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman\\n    year: 2022\\n    venue: NeurIPS 2022\\n    url: https://arxiv.org/abs/2203.14465\\n    category: self_training_bootstrapping\\n    role: method_component\\n    key_finding: >\\n      Self-Taught Reasoner：迭代式 bootstrapping——生成 rationale 回答问题，\\n      答对的保留，答错的用 rationalization（给正确答案生成事后 rationale）补充，\\n      然后 fine-tune 模型。循环迭代使模型逐渐学会更难的推理。\\n    relevance_to_freige: >\\n      STaR 的 iterative bootstrapping 是 FREIGE RSFT 的理论先驱——\\n      RSFT 本质上是 STaR 的一个 iteration（生成、筛选正确输出、fine-tune）。\\n      但 FREIGE 加入了 evidence quality 作为额外筛选维度，\\n      不只看 answer correctness 还看 evidence faithfulness。\\n\\n  - title: \\\"Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models\\\"\\n    authors: Zixiang Chen, Yihe Deng, Huizhuo Yuan, Kaixuan Ji, Quanquan Gu\\n    year: 2024\\n    venue: ICML 2024\\n    url: https://arxiv.org/abs/2401.01335\\n    category: self_training_bootstrapping\\n    role: related_method\\n    key_finding: >\\n      SPIN：LLM 通过 self-play 机制与自身过去版本对弈来提升——\\n      区分自身生成的 response 和 human-annotated response。\\n      全局最优在 LLM policy 与目标分布对齐时达到。\\n      性能超越 DPO + GPT-4 偏好数据。\\n    relevance_to_freige: >\\n      SPIN 的 self-play 和 FREIGE 的 RSFT 都是利用模型自身输出进行训练的方法，\\n      但方向不同：SPIN 学习区分 self vs human，RSFT 选择 self 中的最优。\\n      理论上 SPIN 可应用于 DocRE 的 evidence 生成质量提升。\\n\", \"total_chars\": 109145, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "bce7834d-1a4a-45d4-b5ac-cb0261caeec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "leafUuid": "0fe962f9-6851-455e-90fb-c393e9cb02c5",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Check eval results against literature map",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---

### Assistant

_source line 17 · 2026-05-18T20:13:29.893Z_

<details><summary>Logged reasoning block</summary>

```text
The file is very large. Let me use a subagent to analyze it and also do the web searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fe962f9-6851-455e-90fb-c393e9cb02c5",
  "isSidechain": false,
  "requestId": "req_011CbAeQXbjFpQAwzaAoah7n",
  "type": "assistant",
  "uuid": "c6b5e472-5fdf-4a72-b3e1-1ef9b35c759c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfzeAWXcoxbazKP1DNcyUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 25721,
      "output_tokens": 965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 965,
          "cache_read_input_tokens": 25721,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 648
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

_source line 18 · 2026-05-18T20:13:30.900Z_

文件很大，我启动两个并行 agent：一个分析 literature_map，一个做 web 搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6b5e472-5fdf-4a72-b3e1-1ef9b35c759c",
  "isSidechain": false,
  "requestId": "req_011CbAeQXbjFpQAwzaAoah7n",
  "type": "assistant",
  "uuid": "329405f9-4e54-4293-9d7a-3653e10b1d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfzeAWXcoxbazKP1DNcyUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 25721,
      "output_tokens": 965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 965,
          "cache_read_input_tokens": 25721,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 648
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

_source line 19 · 2026-05-18T20:13:40.716Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TdaoHhSBZv6q1v4M67PdWe`</summary>

```json
{
  "description": "Analyze literature_map.yaml",
  "prompt": "I need you to analyze a literature_map.yaml file that was saved as JSON. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt\n\nIt's JSON with schema: {result: string} where result contains the YAML content as a string.\n\nI need you to find:\n\n1. **All papers with role \"direct-competitor\"** — list their title, venue, year, and any notes about rejection sampling / selection strategy ablations.\n\n2. **All papers that discuss rejection sampling, RSFT, or scored/random selection strategies** — regardless of role. Look for keywords like \"rejection sampling\", \"RSFT\", \"best-of-n\", \"scored selection\", \"random selection\", \"selection strategy\" in titles, abstracts, notes, or relevance fields.\n\n3. **All papers that discuss GRPO (Group Relative Policy Optimization)** or reinforcement learning for IE/NLP structured tasks — look for \"GRPO\", \"group relative policy\", \"reinforcement learning\" + \"information extraction\" or \"relation extraction\".\n\n4. **All papers about learning curves or training dynamics of RL methods on NLP tasks**.\n\nFor each found paper, extract: title, venue, year, role, and the relevant text snippet that matched.\n\nPlease be thorough — read the full content, don't just sample. Report your findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "329405f9-4e54-4293-9d7a-3653e10b1d84",
  "isSidechain": false,
  "requestId": "req_011CbAeQXbjFpQAwzaAoah7n",
  "type": "assistant",
  "uuid": "7f1d8d2f-09bb-4dfc-9cd5-f8320b14c4a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfzeAWXcoxbazKP1DNcyUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 25721,
      "output_tokens": 965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 965,
          "cache_read_input_tokens": 25721,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 648
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

_source line 20 · 2026-05-18T20:13:50.555Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SRdtPZtKh9qGziiKuzzp4q`</summary>

```json
{
  "description": "Web search for related papers",
  "prompt": "I need you to search the web for academic papers related to three specific topics. Use WebSearch for each query.\n\nContext: We are working on a project about information extraction (IE) using LLMs, specifically:\n- We use \"rejection sampling fine-tuning\" (RSFT) where we score model outputs and select the best ones for training\n- We just showed that CED-scored selection (k=1) gets ign_f1=0.4596 vs random selection (k=1) gets 0.4114 — a 4.82pp gap proving scoring precision matters\n- We also use GRPO (Group Relative Policy Optimization) for RL training on IE tasks, and it's showing positive learning (ign_f1=0.4431 vs SFT baseline 0.4057)\n\nPlease search for:\n\n1. WebSearch: \"rejection sampling selection strategy ablation language model fine-tuning\"\n2. WebSearch: \"GRPO information extraction relation extraction NLP\"\n3. WebSearch: \"scored vs random rejection sampling fine-tuning LLM\"\n4. WebSearch: \"best-of-n sampling strategy comparison fine-tuning\"\n5. WebSearch: \"reinforcement learning document relation extraction\"\n\nFor each search, extract the most relevant papers found (title, authors if available, venue, year, key findings). Focus on papers that:\n- Compare scored vs random selection in rejection sampling / best-of-n\n- Apply GRPO specifically to structured NLP tasks (IE, NER, RE)\n- Study training dynamics / learning curves of RL methods on NLP\n\nReturn a structured list of all relevant papers found, with their key findings summarized in 1-2 sentences each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f1d8d2f-09bb-4dfc-9cd5-f8320b14c4a0",
  "isSidechain": false,
  "requestId": "req_011CbAeQXbjFpQAwzaAoah7n",
  "type": "assistant",
  "uuid": "1a558972-8afa-4724-b007-5e35b19c99a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfzeAWXcoxbazKP1DNcyUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 25721,
      "output_tokens": 965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 965,
          "cache_read_input_tokens": 25721,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 648
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

_source line 21 · 2026-05-18T20:15:43.878Z_

<details><summary>↩ Tool result · `toolu_01SRdtPZtKh9qGziiKuzzp4q`</summary>

```text
Here is the structured compilation of all relevant papers found across the five search queries.

---

## Category 1: Rejection Sampling / Selection Strategy Ablation

### 1.1 "A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce"
- **Authors:** Liu et al.
- **Venue/Year:** arXiv 2504.11343, 2025
- **Key findings:** A simple rejection sampling baseline (RAFT) that trains only on positively rewarded samples yields competitive performance to GRPO and PPO. Ablation reveals GRPO's main advantage comes from discarding prompts with entirely incorrect responses, not from reward normalization. Introduces Reinforce-Rej, a minimal variant that filters both entirely correct and incorrect samples, improving KL efficiency and entropy stability.
- **Relevance:** Directly compares scored vs. filtered rejection sampling against RL methods, with detailed ablation on what makes selection matter.

### 1.2 "Scaling Relationship on Learning Mathematical Reasoning with Large Language Models" (RFT)
- **Authors:** Yuan et al.
- **Venue/Year:** arXiv 2308.01825, 2023 (ICLR-level impact)
- **Key findings:** The key factor in rejection sampling augmented data is the number of **distinct reasoning paths**, not just correctness. RFT augments datasets with multiple model-generated correct chains per example. On GSM8K, combining rejection samples from multiple models pushes LLaMA-7B from 35.9% (SFT) to 49.3% accuracy.
- **Relevance:** Foundational work showing that selection diversity/quality in rejection sampling dramatically impacts fine-tuning outcomes.

### 1.3 "RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment"
- **Authors:** Dong, Xiong et al.
- **Venue/Year:** Semantic Scholar / arXiv, 2023
- **Key findings:** RAFT iteratively generates n responses per prompt, filters out those with incorrect answers, and fine-tunes on accepted samples. Demonstrates that reward-ranked selection is a simple but effective alternative to full RL-based alignment.
- **Relevance:** Direct baseline for comparing scored selection (reward-ranked) vs. simpler filtering strategies.

### 1.4 "RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models"
- **Authors:** Khaki et al.
- **Venue/Year:** arXiv 2402.10038, 2024
- **Key findings:** Ablation studies show RS-DPO is more robust to reward model quality variations than PPO. Performance is sensitive to rejection threshold (eta) and temperature (tau); lowering threshold generally improves performance but going too low hurts. Lower temperature increases sample size and enhances performance.
- **Relevance:** Detailed ablation on how selection threshold/scoring quality affects rejection sampling outcomes.

### 1.5 "Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning"
- **Authors:** (Not specified in results)
- **Venue/Year:** arXiv 2602.04391, 2026
- **Key findings:** TrajFusion consistently outperforms standard RFT, particularly on challenging and long-form reasoning problems. Proposes fusing partial correct trajectories rather than only selecting complete correct ones.
- **Relevance:** Shows limitations of simple best-of-n selection and proposes improvements beyond binary accept/reject.

### 1.6 "RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning"
- **Authors:** (Not specified in results)
- **Venue/Year:** arXiv 2601.09253, 2026
- **Key findings:** Instead of discarding rejected samples, repurposes them via reward-informed training signals, extracting value from negative examples that standard rejection sampling throws away.
- **Relevance:** Addresses the waste inherent in rejection sampling by using scoring to inform training even on rejected samples.

---

## Category 2: Best-of-N Sampling Strategy

### 2.1 "Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models"
- **Authors:** (Not specified in results)
- **Venue/Year:** ICLR 2025 (arXiv 2412.15287)
- **Key findings:** First imitation learning and RL methods for BoN-aware fine-tuning. BoN-aware models learn a meta-strategy interleaving best responses with diverse responses (exploration-exploitation trade-off). Improves Gemma 2B BoN32 on MATH from 26.8% to 30.8%, and pass@32 from 60.0% to 67.0%.
- **Relevance:** Shows that training strategy should be aware of the inference-time selection mechanism, directly relevant to how RSFT selection strategy interacts with training.

---

## Category 3: GRPO and RL for LLMs

### 3.1 "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
- **Authors:** DeepSeek-AI
- **Venue/Year:** arXiv 2501.12948, 2025
- **Key findings:** Introduces GRPO for training reasoning LLMs with verifiable binary rewards. GRPO eliminates the critic network, instead estimating baselines from group scores. Combined with chain-of-thought format and strong pre-training, achieves state-of-the-art reasoning performance.
- **Relevance:** The foundational GRPO paper; critical reference for any GRPO-based training.

### 3.2 "Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification"
- **Authors:** (Not specified in results)
- **Venue/Year:** arXiv 2503.06639, 2025
- **Key findings:** GRPO is asymptotically equivalent to an oracle policy gradient algorithm and achieves asymptotically optimal performance within a broad class of policy gradient algorithms. Provides theoretical grounding for GRPO's empirical success.
- **Relevance:** Theoretical analysis of why GRPO works, useful for justifying its use in IE tasks.

### 3.3 "GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control"
- **Authors:** (Not specified in results)
- **Venue/Year:** arXiv 2508.03772, 2025
- **Key findings:** Addresses two issues with GRPO: gradient conflicts and policy collapse, through conflict-aware updates and entropy control. Proposes practical stabilization techniques.
- **Relevance:** Relevant if GRPO training shows instability on IE tasks.

### 3.4 "From Absolute to Relative: Rethinking Reward Shaping in Group-Based Reinforcement Learning"
- **Authors:** (Not specified in results)
- **Venue/Year:** arXiv 2601.23058, 2026
- **Key findings:** Rethinks how rewards should be shaped in group-based RL settings like GRPO, comparing absolute vs. relative reward designs.
- **Relevance:** Relevant to CED-scored reward design choices in your RSFT pipeline.

---

## Category 4: RL for Document-Level Relation Extraction

### 4.1 "A Reinforcement Learning Framework for N-Ary Document-Level Relation Extraction"
- **Authors:** (Not specified in results)
- **Venue/Year:** IEEE Xplore, 2024
- **Key findings:** RL-based relation classifier training framework adapts binary document-level RE to handle complex N-ary relations, reducing noise from distant supervision or irrelevant sentences.
- **Relevance:** Direct precedent for using RL in document-level relation extraction.

### 4.2 "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction"
- **Authors:** (Not specified in results)
- **Venue/Year:** arXiv 2302.08675, 2023
- **Key findings:** Guides attention with evidence sentences to improve document-level RE. Uses evidence-aware mechanisms for better extraction.
- **Relevance:** Evidence-guided approach to DocRE, related to your "faith-evidence" project framing.

### 4.3 "Evidence-aware Document-level Relation Extraction"
- **Authors:** (Not specified in results)
- **Venue/Year:** OpenReview (appears conference-submitted)
- **Key findings:** Explicitly models evidence awareness in document-level RE, connecting evidence identification with relation extraction.
- **Relevance:** Directly relevant to your project's evidence-aware IE approach.

### 4.4 "Reward-based Input Construction for Cross-document Relation Extraction"
- **Authors:** (Not specified in results)
- **Venue/Year:** arXiv 2405.20649, 2024
- **Key findings:** Uses RL to train input sentence selection modules for cross-document RE, where relation prediction scores serve as rewards.
- **Relevance:** Uses reward/RL signals specifically for selecting inputs in relation extraction.

### 4.5 "A Hierarchical Framework for Relation Extraction with Reinforcement Learning"
- **Authors:** Takanobu et al.
- **Venue/Year:** arXiv 1811.03925, 2018
- **Key findings:** Decomposes joint entity-relation extraction into two-level RL policies: high-level for relation detection, low-level for entity extraction. Pioneering work on RL for structured IE.
- **Relevance:** Early but foundational work on RL applied to joint extraction tasks.

### 4.6 "Adaptive Reinforcement Learning Planning: Harnessing Large Language Models for Complex Information Extraction"
- **Authors:** (Not specified in results)
- **Venue/Year:** arXiv 2406.11455, 2024
- **Key findings:** Divides extraction into classification of relations/events and extraction of entities in multiple orderly steps. Uses RL for adaptive planning in complex IE with LLMs.
- **Relevance:** Most directly relevant to your project: RL + LLM for information extraction, addressing false positives and missing elements.

---

## Summary of Key Gaps and Positioning

Based on these searches:

1. **Scored vs. random rejection sampling:** Paper 1.1 (Liu et al. 2025) and 1.2 (Yuan et al. 2023) are the closest comparisons, but neither tests on IE/RE tasks. Your 4.82pp gap (CED-scored vs random, k=1) would be a novel datapoint for structured extraction tasks.

2. **GRPO for IE:** No paper was found applying GRPO specifically to information extraction, NER, or relation extraction. All existing GRPO work targets math reasoning or coding. Your GRPO-for-IE results (ign_f1=0.4431 vs SFT 0.4057) appear to be a novel application.

3. **RL for DocRE:** Papers 4.1-4.6 show precedent for RL in document RE, but all use older RL formulations (not GRPO/PPO on LLMs). The combination of modern LLM-based GRPO with document-level IE is under-explored.

Sources:
- [A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce](https://arxiv.org/html/2504.11343v1)
- [Scaling Relationship on Learning Mathematical Reasoning with Large Language Models](https://arxiv.org/abs/2308.01825)
- [RS-DPO: A Hybrid Rejection Sampling and DPO Method](https://arxiv.org/html/2402.10038v1)
- [Beyond Rejection Sampling: Trajectory Fusion](https://arxiv.org/pdf/2602.04391)
- [RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning](https://arxiv.org/pdf/2601.09253)
- [Inference-Aware Fine-Tuning for Best-of-N Sampling (ICLR 2025)](https://arxiv.org/abs/2412.15287)
- [DeepSeek-R1: Incentivizing Reasoning via RL](https://arxiv.org/html/2501.12948v1)
- [RL with Verifiable Rewards: GRPO's Effective Loss](https://arxiv.org/abs/2503.06639v1)
- [GTPO: Stabilizing GRPO](https://arxiv.org/html/2508.03772v4)
- [From Absolute to Relative: Rethinking Reward Shaping in Group-Based RL](https://arxiv.org/pdf/2601.23058)
- [RL Framework for N-Ary Document-Level RE (IEEE)](https://ieeexplore.ieee.org/document/10549760/)
- [DREEAM: Guiding Attention with Evidence for DocRE](https://arxiv.org/pdf/2302.08675)
- [Evidence-aware Document-level Relation Extraction](https://openreview.net/forum?id=JMyPmI06JN)
- [Reward-based Input Construction for Cross-document RE](https://arxiv.org/pdf/2405.20649)
- [A Hierarchical Framework for RE with RL](https://arxiv.org/pdf/1811.03925)
- [Adaptive RL Planning for Complex IE](https://arxiv.org/pdf/2406.11455)
- [RAFT: Reward rAnked FineTuning](https://www.semanticscholar.org/paper/RAFT:-Reward-rAnked-FineTuning-for-Generative-Model-Dong-Xiong/3ab661db57d924f4ff1706e05ac807873ca00e0a)
- [GRPO Overview (EmergentMind)](https://www.emergentmind.com/topics/group-based-relative-policy-optimization-grpo)
- [Reinforcement Learning Enhanced LLMs Survey](https://arxiv.org/html/2412.10400v3)

agentId: a078767b7109b67ae (use SendMessage with to: 'a078767b7109b67ae' to continue this agent)
&lt;usage>total_tokens: 29952
tool_uses: 11
duration_ms: 113316&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a558972-8afa-4724-b007-5e35b19c99a7",
  "isSidechain": false,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "type": "user",
  "uuid": "82449437-7c90-43c1-a33b-c70f28f5a069",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to search the web for academic papers related to three specific topics. Use WebSearch for each query.\n\nContext: We are working on a project about information extraction (IE) using LLMs, specifically:\n- We use \"rejection sampling fine-tuning\" (RSFT) where we score model outputs and select the best ones for training\n- We just showed that CED-scored selection (k=1) gets ign_f1=0.4596 vs random selection (k=1) gets 0.4114 — a 4.82pp gap proving scoring precision matters\n- We also use GRPO (Group Relative Policy Optimization) for RL training on IE tasks, and it's showing positive learning (ign_f1=0.4431 vs SFT baseline 0.4057)\n\nPlease search for:\n\n1. WebSearch: \"rejection sampling selection strategy ablation language model fine-tuning\"\n2. WebSearch: \"GRPO information extraction relation extraction NLP\"\n3. WebSearch: \"scored vs random rejection sampling fine-tuning LLM\"\n4. WebSearch: \"best-of-n sampling strategy comparison fine-tuning\"\n5. WebSearch: \"reinforcement learning document relation extraction\"\n\nFor each search, extract the most relevant papers found (title, authors if available, venue, year, key findings). Focus on papers that:\n- Compare scored vs random selection in rejection sampling / best-of-n\n- Apply GRPO specifically to structured NLP tasks (IE, NER, RE)\n- Study training dynamics / learning curves of RL methods on NLP\n\nReturn a structured list of all relevant papers found, with their key findings summarized in 1-2 sentences each.",
    "agentId": "a078767b7109b67ae",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the structured compilation of all relevant papers found across the five search queries.\n\n---\n\n## Category 1: Rejection Sampling / Selection Strategy Ablation\n\n### 1.1 \"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\"\n- **Authors:** Liu et al.\n- **Venue/Year:** arXiv 2504.11343, 2025\n- **Key findings:** A simple rejection sampling baseline (RAFT) that trains only on positively rewarded samples yields competitive performance to GRPO and PPO. Ablation reveals GRPO's main advantage comes from discarding prompts with entirely incorrect responses, not from reward normalization. Introduces Reinforce-Rej, a minimal variant that filters both entirely correct and incorrect samples, improving KL efficiency and entropy stability.\n- **Relevance:** Directly compares scored vs. filtered rejection sampling against RL methods, with detailed ablation on what makes selection matter.\n\n### 1.2 \"Scaling Relationship on Learning Mathematical Reasoning with Large Language Models\" (RFT)\n- **Authors:** Yuan et al.\n- **Venue/Year:** arXiv 2308.01825, 2023 (ICLR-level impact)\n- **Key findings:** The key factor in rejection sampling augmented data is the number of **distinct reasoning paths**, not just correctness. RFT augments datasets with multiple model-generated correct chains per example. On GSM8K, combining rejection samples from multiple models pushes LLaMA-7B from 35.9% (SFT) to 49.3% accuracy.\n- **Relevance:** Foundational work showing that selection diversity/quality in rejection sampling dramatically impacts fine-tuning outcomes.\n\n### 1.3 \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\"\n- **Authors:** Dong, Xiong et al.\n- **Venue/Year:** Semantic Scholar / arXiv, 2023\n- **Key findings:** RAFT iteratively generates n responses per prompt, filters out those with incorrect answers, and fine-tunes on accepted samples. Demonstrates that reward-ranked selection is a simple but effective alternative to full RL-based alignment.\n- **Relevance:** Direct baseline for comparing scored selection (reward-ranked) vs. simpler filtering strategies.\n\n### 1.4 \"RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models\"\n- **Authors:** Khaki et al.\n- **Venue/Year:** arXiv 2402.10038, 2024\n- **Key findings:** Ablation studies show RS-DPO is more robust to reward model quality variations than PPO. Performance is sensitive to rejection threshold (eta) and temperature (tau); lowering threshold generally improves performance but going too low hurts. Lower temperature increases sample size and enhances performance.\n- **Relevance:** Detailed ablation on how selection threshold/scoring quality affects rejection sampling outcomes.\n\n### 1.5 \"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** arXiv 2602.04391, 2026\n- **Key findings:** TrajFusion consistently outperforms standard RFT, particularly on challenging and long-form reasoning problems. Proposes fusing partial correct trajectories rather than only selecting complete correct ones.\n- **Relevance:** Shows limitations of simple best-of-n selection and proposes improvements beyond binary accept/reject.\n\n### 1.6 \"RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** arXiv 2601.09253, 2026\n- **Key findings:** Instead of discarding rejected samples, repurposes them via reward-informed training signals, extracting value from negative examples that standard rejection sampling throws away.\n- **Relevance:** Addresses the waste inherent in rejection sampling by using scoring to inform training even on rejected samples.\n\n---\n\n## Category 2: Best-of-N Sampling Strategy\n\n### 2.1 \"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** ICLR 2025 (arXiv 2412.15287)\n- **Key findings:** First imitation learning and RL methods for BoN-aware fine-tuning. BoN-aware models learn a meta-strategy interleaving best responses with diverse responses (exploration-exploitation trade-off). Improves Gemma 2B BoN32 on MATH from 26.8% to 30.8%, and pass@32 from 60.0% to 67.0%.\n- **Relevance:** Shows that training strategy should be aware of the inference-time selection mechanism, directly relevant to how RSFT selection strategy interacts with training.\n\n---\n\n## Category 3: GRPO and RL for LLMs\n\n### 3.1 \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n- **Authors:** DeepSeek-AI\n- **Venue/Year:** arXiv 2501.12948, 2025\n- **Key findings:** Introduces GRPO for training reasoning LLMs with verifiable binary rewards. GRPO eliminates the critic network, instead estimating baselines from group scores. Combined with chain-of-thought format and strong pre-training, achieves state-of-the-art reasoning performance.\n- **Relevance:** The foundational GRPO paper; critical reference for any GRPO-based training.\n\n### 3.2 \"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** arXiv 2503.06639, 2025\n- **Key findings:** GRPO is asymptotically equivalent to an oracle policy gradient algorithm and achieves asymptotically optimal performance within a broad class of policy gradient algorithms. Provides theoretical grounding for GRPO's empirical success.\n- **Relevance:** Theoretical analysis of why GRPO works, useful for justifying its use in IE tasks.\n\n### 3.3 \"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** arXiv 2508.03772, 2025\n- **Key findings:** Addresses two issues with GRPO: gradient conflicts and policy collapse, through conflict-aware updates and entropy control. Proposes practical stabilization techniques.\n- **Relevance:** Relevant if GRPO training shows instability on IE tasks.\n\n### 3.4 \"From Absolute to Relative: Rethinking Reward Shaping in Group-Based Reinforcement Learning\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** arXiv 2601.23058, 2026\n- **Key findings:** Rethinks how rewards should be shaped in group-based RL settings like GRPO, comparing absolute vs. relative reward designs.\n- **Relevance:** Relevant to CED-scored reward design choices in your RSFT pipeline.\n\n---\n\n## Category 4: RL for Document-Level Relation Extraction\n\n### 4.1 \"A Reinforcement Learning Framework for N-Ary Document-Level Relation Extraction\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** IEEE Xplore, 2024\n- **Key findings:** RL-based relation classifier training framework adapts binary document-level RE to handle complex N-ary relations, reducing noise from distant supervision or irrelevant sentences.\n- **Relevance:** Direct precedent for using RL in document-level relation extraction.\n\n### 4.2 \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** arXiv 2302.08675, 2023\n- **Key findings:** Guides attention with evidence sentences to improve document-level RE. Uses evidence-aware mechanisms for better extraction.\n- **Relevance:** Evidence-guided approach to DocRE, related to your \"faith-evidence\" project framing.\n\n### 4.3 \"Evidence-aware Document-level Relation Extraction\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** OpenReview (appears conference-submitted)\n- **Key findings:** Explicitly models evidence awareness in document-level RE, connecting evidence identification with relation extraction.\n- **Relevance:** Directly relevant to your project's evidence-aware IE approach.\n\n### 4.4 \"Reward-based Input Construction for Cross-document Relation Extraction\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** arXiv 2405.20649, 2024\n- **Key findings:** Uses RL to train input sentence selection modules for cross-document RE, where relation prediction scores serve as rewards.\n- **Relevance:** Uses reward/RL signals specifically for selecting inputs in relation extraction.\n\n### 4.5 \"A Hierarchical Framework for Relation Extraction with Reinforcement Learning\"\n- **Authors:** Takanobu et al.\n- **Venue/Year:** arXiv 1811.03925, 2018\n- **Key findings:** Decomposes joint entity-relation extraction into two-level RL policies: high-level for relation detection, low-level for entity extraction. Pioneering work on RL for structured IE.\n- **Relevance:** Early but foundational work on RL applied to joint extraction tasks.\n\n### 4.6 \"Adaptive Reinforcement Learning Planning: Harnessing Large Language Models for Complex Information Extraction\"\n- **Authors:** (Not specified in results)\n- **Venue/Year:** arXiv 2406.11455, 2024\n- **Key findings:** Divides extraction into classification of relations/events and extraction of entities in multiple orderly steps. Uses RL for adaptive planning in complex IE with LLMs.\n- **Relevance:** Most directly relevant to your project: RL + LLM for information extraction, addressing false positives and missing elements.\n\n---\n\n## Summary of Key Gaps and Positioning\n\nBased on these searches:\n\n1. **Scored vs. random rejection sampling:** Paper 1.1 (Liu et al. 2025) and 1.2 (Yuan et al. 2023) are the closest comparisons, but neither tests on IE/RE tasks. Your 4.82pp gap (CED-scored vs random, k=1) would be a novel datapoint for structured extraction tasks.\n\n2. **GRPO for IE:** No paper was found applying GRPO specifically to information extraction, NER, or relation extraction. All existing GRPO work targets math reasoning or coding. Your GRPO-for-IE results (ign_f1=0.4431 vs SFT 0.4057) appear to be a novel application.\n\n3. **RL for DocRE:** Papers 4.1-4.6 show precedent for RL in document RE, but all use older RL formulations (not GRPO/PPO on LLMs). The combination of modern LLM-based GRPO with document-level IE is under-explored.\n\nSources:\n- [A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce](https://arxiv.org/html/2504.11343v1)\n- [Scaling Relationship on Learning Mathematical Reasoning with Large Language Models](https://arxiv.org/abs/2308.01825)\n- [RS-DPO: A Hybrid Rejection Sampling and DPO Method](https://arxiv.org/html/2402.10038v1)\n- [Beyond Rejection Sampling: Trajectory Fusion](https://arxiv.org/pdf/2602.04391)\n- [RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning](https://arxiv.org/pdf/2601.09253)\n- [Inference-Aware Fine-Tuning for Best-of-N Sampling (ICLR 2025)](https://arxiv.org/abs/2412.15287)\n- [DeepSeek-R1: Incentivizing Reasoning via RL](https://arxiv.org/html/2501.12948v1)\n- [RL with Verifiable Rewards: GRPO's Effective Loss](https://arxiv.org/abs/2503.06639v1)\n- [GTPO: Stabilizing GRPO](https://arxiv.org/html/2508.03772v4)\n- [From Absolute to Relative: Rethinking Reward Shaping in Group-Based RL](https://arxiv.org/pdf/2601.23058)\n- [RL Framework for N-Ary Document-Level RE (IEEE)](https://ieeexplore.ieee.org/document/10549760/)\n- [DREEAM: Guiding Attention with Evidence for DocRE](https://arxiv.org/pdf/2302.08675)\n- [Evidence-aware Document-level Relation Extraction](https://openreview.net/forum?id=JMyPmI06JN)\n- [Reward-based Input Construction for Cross-document RE](https://arxiv.org/pdf/2405.20649)\n- [A Hierarchical Framework for RE with RL](https://arxiv.org/pdf/1811.03925)\n- [Adaptive RL Planning for Complex IE](https://arxiv.org/pdf/2406.11455)\n- [RAFT: Reward rAnked FineTuning](https://www.semanticscholar.org/paper/RAFT:-Reward-rAnked-FineTuning-for-Generative-Model-Dong-Xiong/3ab661db57d924f4ff1706e05ac807873ca00e0a)\n- [GRPO Overview (EmergentMind)](https://www.emergentmind.com/topics/group-based-relative-policy-optimization-grpo)\n- [Reinforcement Learning Enhanced LLMs Survey](https://arxiv.org/html/2412.10400v3)"
      }
    ],
    "totalDurationMs": 113316,
    "totalTokens": 29952,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3584,
      "cache_read_input_tokens": 22917,
      "output_tokens": 3450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3584
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3450,
          "cache_read_input_tokens": 22917,
          "cache_creation_input_tokens": 3584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3584,
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
  "sourceToolAssistantUUID": "1a558972-8afa-4724-b007-5e35b19c99a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
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
  "leafUuid": "82449437-7c90-43c1-a33b-c70f28f5a069",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Check eval results against literature map",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---

### Tool result

_source line 24 · 2026-05-18T20:16:34.097Z_

<details><summary>↩ Tool result · `toolu_01TdaoHhSBZv6q1v4M67PdWe`</summary>

```text
Now I have all the data. Let me compile the complete findings.

---

## Complete Analysis Results

### CATEGORY 1: Papers with role "direct-competitor" (or "direct_competitor")

The literature map uses two variants: `direct-competitor` (hyphen) and `direct_competitor` (underscore). Combined, there are **13 direct competitor papers**:

| # | Title | Venue | Year | Category | Notes on rejection sampling / selection strategy |
|---|-------|-------|------|----------|--------------------------------------------------|
| 1 | **DREEAM**: Guiding Attention with Evidence for Improving Document-Level Relation Extraction | EACL 2023 | 2023 | evidence_based_docre | None |
| 2 | **CDER**: Collaborative Evidence Retrieval for Document-level Relation Extraction | arXiv 2504.06529 | 2025 | evidence_based_docre | None |
| 3 | **QeRL**: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs | arXiv 2510.11696 | 2025 | lora_qlora_artifacts | None |
| 4 | **ReasoningNER**: A Reasoning Paradigm for Named Entity Recognition | arXiv 2511.11978 | 2025 | grpo_nlp_applications | Contains "reward variance" keyword in broader text (GRPO composite reward design) but no explicit rejection sampling ablation |
| 5 | **OREO**: Offline Reinforcement Learning for LLM Multi-Step Reasoning | arXiv 2412.16145 | 2024 | rsft_offline_rl | Mentions RSFT context (offline RL vs RSFT comparison) |
| 6 | **R1-RE**: Cross-Domain Relation Extraction with RLVR | arXiv 2507.04642 | 2025 | rl_for_ie | RSFT context (GRPO + verifiable reward for RE); F1-based reward design but no selection strategy ablation reported |
| 7 | **RIFT**: Repurposing Negative Samples via Reward-Informed Fine-Tuning | arXiv 2601.09253 | 2026 | rsft_methodology | Directly about RSFT's limitations (hard rejection discards negative samples); proposes reward-informed reweighting instead |
| 8 | **DocKS-RAG**: Optimizing Document-Level RE through LLM-Enhanced Hybrid Prompt Tuning | ICML 2025 | 2025 | llm_docre | None |
| 9 | **COREX**: Document-level RE with Consistent Two-Hop Reasoning and Evidence Sentence Prediction | IEEE IJCNN 2024 | 2024 | evidence_based_docre | None |
| 10 | **ESTR-DocRE**: Evidence-supervised Transformer Reasoning Framework for DocRE | J. King Saud Univ. (Springer) | 2025 | evidence_supervised_docre | None |
| 11 | **It Takes Two Flints to Make a Fire**: Multitask Learning of Neural Relation and Explanation Classifiers | Computational Linguistics 49(1) | 2023 | evidence_cost_generative_ie | None |
| 12 | **Entity and Evidence Guided Relation Extraction for DocRED** (E2GRE) | RepL4NLP @ ACL 2021 | 2021 | evidence_cost_generative_ie | None |
| 13 | **SAIS**: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction | NAACL 2022 | 2022 | evidence_supervised_docre | None |

Additionally, several papers have `closest_prior_work` or `closest_competitor` roles:
- **GDPO** (ICML 2026) -- closest_prior_work, reward_diversity
- **E-GRPO** (ICLR 2026) -- closest_prior_work, grpo_structured
- **EvidenceRL** (arXiv 2603.19532, 2026) -- closest_competitor, evidence_grounded_rl
- **Improving RLHF Using Contrastive Rewards** (arXiv 2403.07708, 2024) -- closest_contrastive_precedent
- **Eider** (ACL Findings 2022) -- closest_docre_precedent
- **C-LoRAE** (arXiv 2505.06303, 2025) -- closest_prior_work, mtl_ie_tradeoff
- **Imbalanced Gradients in RL Post-Training** (Findings of EACL 2026) -- closest_prior_work

---

### CATEGORY 2: Papers discussing rejection sampling / RSFT / scored-random selection strategies

**32 papers** matched. The most directly relevant ones:

**Core RSFT methodology papers:**
1. **A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce** (arXiv 2504.11343, 2025) -- role: key_theoretical_support. Key insight: RAFT (simple rejection sampling) matches GRPO/PPO in math reasoning. GRPO's advantage mainly comes from discarding all-wrong prompts, not reward normalization. Proposes Reinforce-Rej filtering all-correct and all-wrong samples.
2. **Beyond Rejection Sampling: Trajectory Fusion (TrajFusion)** (arXiv 2602.04391, 2026) -- role: method_component. Traditional RSFT discards wrong trajectories; TrajFusion interleaves error and correct trajectories.
3. **Rejection Sampling Based Fine Tuning Secretly Performs PPO** (ICML 2025, 2025) -- role: theoretical_support. Establishes theoretical equivalence between RSFT and PPO under marginal KL constraints.
4. **RAFT: Reward rAnked FineTuning** (TMLR 2024, 2024) -- role: background. Canonical RSFT framework: iterative generate-rank-filter-SFT.
5. **RS-DPO: Hybrid Rejection Sampling and DPO** (NAACL 2024 Findings, 2024) -- role: method-component. Systematically combines rejection sampling with DPO using reward-based contrastive pair selection.
6. **RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning** (arXiv 2601.09253, 2026) -- role: direct_competitor. Addresses RSFT's waste of negative samples through reward-weighted loss.
7. **AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners** (NeurIPS 2025, 2025) -- role: related_method. RSFT's random sampling leads to training imbalance; proposes diversity + curriculum sampling, reducing FLOPs by 58.6%.

**Best-of-N papers:**
8. **Is Best-of-N the Best of Them?** (ICML 2025, 2025) -- role: key_baseline. BoN suffers from reward hacking at large N; proposes InferenceTimePessimism.
9. **Inference-Aware Fine-Tuning for Best-of-N** (ICLR 2025, 2024) -- role: method_component. Trains model to optimize BoN inference performance; learns exploration-exploitation meta-strategy.
10. **Evaluation of Best-of-N Sampling Strategies** (TMLR 2025, 2025) -- role: evaluation. Systematic BoN evaluation; proposes Stochastic Regularized BoN.
11. **Regularized Best-of-N with MBR Objective** (NAACL 2025, 2024) -- role: related_method. MBR-BoN uses Minimum Bayes Risk as proximity regularizer.

The remaining 21 papers mention RSFT tangentially in their broader context (e.g., LLM-based DocRE methods, IE alignment, knowledge distillation for DocRE, self-training).

---

### CATEGORY 3: Papers about GRPO or RL for IE/NLP structured tasks

**50 papers** matched. Organized by sub-theme:

**GRPO for IE specifically (most relevant):**
1. **R1-RE** (arXiv 2507.04642, 2025) -- direct_competitor. First RLVR (GRPO + verifiable reward) for relation extraction. F1-based reward design.
2. **ReasoningNER** (arXiv 2511.11978, 2025) -- direct-competitor. GRPO for NER with composite reward (entity F1 + format compliance).
3. **R2GRPO** (arXiv 2505.22068, 2025) -- related_method. MimicSFT + relevance/rule-mining reward GRPO for scientific IE.
4. **MORE-R1** (arXiv 2603.09478, 2026) -- related_method. GRPO for multimodal RE with progressive sample-mixing.
5. **REAR** (EMNLP 2025 Findings) -- related_method. RL reasoning optimization for event argument extraction.
6. **Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective RL** (Springer 2025) -- related_method.
7. **EvidenceRL** (arXiv 2603.19532, 2026) -- closest_competitor. GRPO optimizing both grounding (evidence entailment) and correctness. F1@3 from 37.0->54.5, grounding from 47.6->78.2. Hallucination reduced 5x.

**GRPO stability / mode collapse / reward design:**
8. **GDPO** (ICML 2026) -- closest_prior_work. Multi-reward GRPO normalization collapse; per-reward independent normalization.
9. **DRA-GRPO** (arXiv 2505.09655, 2025) -- Diversity-aware reward adjustment using submodular mutual information.
10. **DAPO** (NeurIPS 2025) -- key_baseline. Entropy collapse diagnosis; Clip-Higher + Dynamic Sampling.
11. **Dr. GRPO** (COLM 2025) -- Difficulty bias from std normalization; proposes unbiased Monte Carlo advantage.
12. **DiverseGRPO** (arXiv 2512.21514, 2025) -- Mode collapse in image generation GRPO.
13. **Why GRPO Needs Normalization** (arXiv 2601.23135, 2025) -- reward_std drives convergence rate.
14. **GVPO** (NeurIPS 2025) -- Variance-based exploration-exploitation balance.
15. **E-GRPO** (ICLR 2026) -- closest_prior_work. Entity-aware reward giving partial credit to near-miss negative samples.
16. **GRPO-LEAD** (EMNLP 2025) -- Length-regularized rewards + difficulty-aware advantage reweighting.

**Multi-objective GRPO:**
17. **MO-GRPO** (arXiv 2509.22047, 2025) -- Reward hacking in multi-objective GRPO; variance-based normalization.
18. **RDPO** (arXiv 2605.13641, 2026) -- Decorrelated reward subspace optimization.

**GRPO theory:**
19. **GRPO is Secretly a Process Reward Model** (under review ICML 2026) -- GRPO + ORM equivalence to PRM-aware RL; lambda-GRPO.
20. **Reward Hacking in the Era of Large Models** (arXiv 2604.13602, 2026) -- Proxy Compression Hypothesis.

**Contrastive reward for RL:**
21. **Improving RLHF Using Contrastive Rewards** (arXiv 2403.07708, 2024) -- closest_contrastive_precedent. Offline baseline response for contrastive penalty in PPO.

**RL training stability / quantization:**
22-31. Multiple papers on quantization-aware RL (QuRL, QaRL, FP8-RL, Jet-RL, BitRL), training precision (FP16 vs BF16), stabilization formulations.

**Multi-task RL / gradient imbalance:**
32. **Imbalanced Gradients in RL Post-Training of Multi-Task LLMs** (Findings of EACL 2026) -- closest_prior_work. Gradient magnitude vs performance improvement uncorrelated.

Plus ~18 more papers in supporting roles (LoRA theory, PEFT, self-training, ADELIE, etc.)

---

### CATEGORY 4: Papers about learning curves / training dynamics of RL for NLP

**17 papers** matched. The most directly relevant:

1. **DAPO** (NeurIPS 2025) -- Entropy collapse dynamics; frac_zero prompt filtering. "accuracy=0 or 1 prompts produce zero gradients, reducing effective batch size."
2. **Dr. GRPO** (COLM 2025) -- std(r)->0 causes advantage explosion; frac_zero_std->0.8 under extraction-only reward.
3. **Why GRPO Needs Normalization** (arXiv 2601.23135, 2025) -- reward_std governs convergence rate; higher reward_std = faster convergence.
4. **Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards** (arXiv 2511.03710, 2025) -- Per-prompt mean baseline inaccurate at low generation count; James-Stein shrinkage reduces gradient variance.
5. **GVPO** (NeurIPS 2025) -- Variance term naturally balances exploration/exploitation, maintaining moderate entropy.
6. **DiverseGRPO** (arXiv 2512.21514, 2025) -- GRPO output homogenization in later training stages.
7. **Reward Shaping to Mitigate Reward Hacking** (arXiv 2502.18770, 2025) -- Reward should be bounded, fast-growing then slow-converging.
8. **R1-RE** (arXiv 2507.04642, 2025) -- No catastrophic forgetting after GRPO training on sentence-level RE; performance on MATH-500/IFEval/GPQA maintained or improved.
9. **Reinforcement Fine-Tuning Naturally Mitigates Forgetting** (arXiv 2507.05386, 2025) -- RFT gradients scaled by reward variance act as data-dependent regularizer.
10. **The Energy Loss Phenomenon in RLHF** (ICML 2025) -- L1 norm divergence in last layer increases during RL training; excessive increase signals reward hacking.
11. **Defeating the Training-Inference Mismatch via FP16** (arXiv 2510.26788, 2025) -- BF16 causes collapse at 150-600 steps in RL fine-tuning.
12. **QuRL** (ICLR 2026) -- Quantized actor divergence grows exponentially causing training collapse in long-horizon RL.
13. **RL Is Neither a Panacea Nor a Mirage** (arXiv 2508.16546, 2025) -- RL-FT recovers most OOD performance loss from SFT; recovery correlates with singular vector direction rotation.
14. **The Impact of LoRA on Cluster Emergence** (arXiv 2402.15415, 2024) -- Phase transition from non-forgetting to forgetting as perturbation norm increases.
15. **Posterior-GRPO** (arXiv 2508.05170, 2025) -- Conditional reward suppresses reward hacking dynamics.
16. **MO-GRPO** (arXiv 2509.22047, 2025) -- Multi-objective reward hacking dynamics.
17. **Regularized BoN with MBR** (NAACL 2025, 2024) -- Reward hacking dynamics in BoN scaling.

agentId: a4b1818a3cd108cba (use SendMessage with to: 'a4b1818a3cd108cba' to continue this agent)
&lt;usage>total_tokens: 53933
tool_uses: 13
duration_ms: 173373&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f1d8d2f-09bb-4dfc-9cd5-f8320b14c4a0",
  "isSidechain": false,
  "promptId": "00163f99-7857-4276-afc6-24e9276d86ac",
  "type": "user",
  "uuid": "045b4c90-1bd5-4fd5-9bdd-69b2c99e7639",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to analyze a literature_map.yaml file that was saved as JSON. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/d1967b82-9b64-485b-8419-ac1a11ebeb1d/tool-results/mcp-agent-ml-research-read_project_file-1779135207105.txt\n\nIt's JSON with schema: {result: string} where result contains the YAML content as a string.\n\nI need you to find:\n\n1. **All papers with role \"direct-competitor\"** — list their title, venue, year, and any notes about rejection sampling / selection strategy ablations.\n\n2. **All papers that discuss rejection sampling, RSFT, or scored/random selection strategies** — regardless of role. Look for keywords like \"rejection sampling\", \"RSFT\", \"best-of-n\", \"scored selection\", \"random selection\", \"selection strategy\" in titles, abstracts, notes, or relevance fields.\n\n3. **All papers that discuss GRPO (Group Relative Policy Optimization)** or reinforcement learning for IE/NLP structured tasks — look for \"GRPO\", \"group relative policy\", \"reinforcement learning\" + \"information extraction\" or \"relation extraction\".\n\n4. **All papers about learning curves or training dynamics of RL methods on NLP tasks**.\n\nFor each found paper, extract: title, venue, year, role, and the relevant text snippet that matched.\n\nPlease be thorough — read the full content, don't just sample. Report your findings in a structured format.",
    "agentId": "a4b1818a3cd108cba",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data. Let me compile the complete findings.\n\n---\n\n## Complete Analysis Results\n\n### CATEGORY 1: Papers with role \"direct-competitor\" (or \"direct_competitor\")\n\nThe literature map uses two variants: `direct-competitor` (hyphen) and `direct_competitor` (underscore). Combined, there are **13 direct competitor papers**:\n\n| # | Title | Venue | Year | Category | Notes on rejection sampling / selection strategy |\n|---|-------|-------|------|----------|--------------------------------------------------|\n| 1 | **DREEAM**: Guiding Attention with Evidence for Improving Document-Level Relation Extraction | EACL 2023 | 2023 | evidence_based_docre | None |\n| 2 | **CDER**: Collaborative Evidence Retrieval for Document-level Relation Extraction | arXiv 2504.06529 | 2025 | evidence_based_docre | None |\n| 3 | **QeRL**: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs | arXiv 2510.11696 | 2025 | lora_qlora_artifacts | None |\n| 4 | **ReasoningNER**: A Reasoning Paradigm for Named Entity Recognition | arXiv 2511.11978 | 2025 | grpo_nlp_applications | Contains \"reward variance\" keyword in broader text (GRPO composite reward design) but no explicit rejection sampling ablation |\n| 5 | **OREO**: Offline Reinforcement Learning for LLM Multi-Step Reasoning | arXiv 2412.16145 | 2024 | rsft_offline_rl | Mentions RSFT context (offline RL vs RSFT comparison) |\n| 6 | **R1-RE**: Cross-Domain Relation Extraction with RLVR | arXiv 2507.04642 | 2025 | rl_for_ie | RSFT context (GRPO + verifiable reward for RE); F1-based reward design but no selection strategy ablation reported |\n| 7 | **RIFT**: Repurposing Negative Samples via Reward-Informed Fine-Tuning | arXiv 2601.09253 | 2026 | rsft_methodology | Directly about RSFT's limitations (hard rejection discards negative samples); proposes reward-informed reweighting instead |\n| 8 | **DocKS-RAG**: Optimizing Document-Level RE through LLM-Enhanced Hybrid Prompt Tuning | ICML 2025 | 2025 | llm_docre | None |\n| 9 | **COREX**: Document-level RE with Consistent Two-Hop Reasoning and Evidence Sentence Prediction | IEEE IJCNN 2024 | 2024 | evidence_based_docre | None |\n| 10 | **ESTR-DocRE**: Evidence-supervised Transformer Reasoning Framework for DocRE | J. King Saud Univ. (Springer) | 2025 | evidence_supervised_docre | None |\n| 11 | **It Takes Two Flints to Make a Fire**: Multitask Learning of Neural Relation and Explanation Classifiers | Computational Linguistics 49(1) | 2023 | evidence_cost_generative_ie | None |\n| 12 | **Entity and Evidence Guided Relation Extraction for DocRED** (E2GRE) | RepL4NLP @ ACL 2021 | 2021 | evidence_cost_generative_ie | None |\n| 13 | **SAIS**: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction | NAACL 2022 | 2022 | evidence_supervised_docre | None |\n\nAdditionally, several papers have `closest_prior_work` or `closest_competitor` roles:\n- **GDPO** (ICML 2026) -- closest_prior_work, reward_diversity\n- **E-GRPO** (ICLR 2026) -- closest_prior_work, grpo_structured\n- **EvidenceRL** (arXiv 2603.19532, 2026) -- closest_competitor, evidence_grounded_rl\n- **Improving RLHF Using Contrastive Rewards** (arXiv 2403.07708, 2024) -- closest_contrastive_precedent\n- **Eider** (ACL Findings 2022) -- closest_docre_precedent\n- **C-LoRAE** (arXiv 2505.06303, 2025) -- closest_prior_work, mtl_ie_tradeoff\n- **Imbalanced Gradients in RL Post-Training** (Findings of EACL 2026) -- closest_prior_work\n\n---\n\n### CATEGORY 2: Papers discussing rejection sampling / RSFT / scored-random selection strategies\n\n**32 papers** matched. The most directly relevant ones:\n\n**Core RSFT methodology papers:**\n1. **A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce** (arXiv 2504.11343, 2025) -- role: key_theoretical_support. Key insight: RAFT (simple rejection sampling) matches GRPO/PPO in math reasoning. GRPO's advantage mainly comes from discarding all-wrong prompts, not reward normalization. Proposes Reinforce-Rej filtering all-correct and all-wrong samples.\n2. **Beyond Rejection Sampling: Trajectory Fusion (TrajFusion)** (arXiv 2602.04391, 2026) -- role: method_component. Traditional RSFT discards wrong trajectories; TrajFusion interleaves error and correct trajectories.\n3. **Rejection Sampling Based Fine Tuning Secretly Performs PPO** (ICML 2025, 2025) -- role: theoretical_support. Establishes theoretical equivalence between RSFT and PPO under marginal KL constraints.\n4. **RAFT: Reward rAnked FineTuning** (TMLR 2024, 2024) -- role: background. Canonical RSFT framework: iterative generate-rank-filter-SFT.\n5. **RS-DPO: Hybrid Rejection Sampling and DPO** (NAACL 2024 Findings, 2024) -- role: method-component. Systematically combines rejection sampling with DPO using reward-based contrastive pair selection.\n6. **RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning** (arXiv 2601.09253, 2026) -- role: direct_competitor. Addresses RSFT's waste of negative samples through reward-weighted loss.\n7. **AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners** (NeurIPS 2025, 2025) -- role: related_method. RSFT's random sampling leads to training imbalance; proposes diversity + curriculum sampling, reducing FLOPs by 58.6%.\n\n**Best-of-N papers:**\n8. **Is Best-of-N the Best of Them?** (ICML 2025, 2025) -- role: key_baseline. BoN suffers from reward hacking at large N; proposes InferenceTimePessimism.\n9. **Inference-Aware Fine-Tuning for Best-of-N** (ICLR 2025, 2024) -- role: method_component. Trains model to optimize BoN inference performance; learns exploration-exploitation meta-strategy.\n10. **Evaluation of Best-of-N Sampling Strategies** (TMLR 2025, 2025) -- role: evaluation. Systematic BoN evaluation; proposes Stochastic Regularized BoN.\n11. **Regularized Best-of-N with MBR Objective** (NAACL 2025, 2024) -- role: related_method. MBR-BoN uses Minimum Bayes Risk as proximity regularizer.\n\nThe remaining 21 papers mention RSFT tangentially in their broader context (e.g., LLM-based DocRE methods, IE alignment, knowledge distillation for DocRE, self-training).\n\n---\n\n### CATEGORY 3: Papers about GRPO or RL for IE/NLP structured tasks\n\n**50 papers** matched. Organized by sub-theme:\n\n**GRPO for IE specifically (most relevant):**\n1. **R1-RE** (arXiv 2507.04642, 2025) -- direct_competitor. First RLVR (GRPO + verifiable reward) for relation extraction. F1-based reward design.\n2. **ReasoningNER** (arXiv 2511.11978, 2025) -- direct-competitor. GRPO for NER with composite reward (entity F1 + format compliance).\n3. **R2GRPO** (arXiv 2505.22068, 2025) -- related_method. MimicSFT + relevance/rule-mining reward GRPO for scientific IE.\n4. **MORE-R1** (arXiv 2603.09478, 2026) -- related_method. GRPO for multimodal RE with progressive sample-mixing.\n5. **REAR** (EMNLP 2025 Findings) -- related_method. RL reasoning optimization for event argument extraction.\n6. **Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective RL** (Springer 2025) -- related_method.\n7. **EvidenceRL** (arXiv 2603.19532, 2026) -- closest_competitor. GRPO optimizing both grounding (evidence entailment) and correctness. F1@3 from 37.0->54.5, grounding from 47.6->78.2. Hallucination reduced 5x.\n\n**GRPO stability / mode collapse / reward design:**\n8. **GDPO** (ICML 2026) -- closest_prior_work. Multi-reward GRPO normalization collapse; per-reward independent normalization.\n9. **DRA-GRPO** (arXiv 2505.09655, 2025) -- Diversity-aware reward adjustment using submodular mutual information.\n10. **DAPO** (NeurIPS 2025) -- key_baseline. Entropy collapse diagnosis; Clip-Higher + Dynamic Sampling.\n11. **Dr. GRPO** (COLM 2025) -- Difficulty bias from std normalization; proposes unbiased Monte Carlo advantage.\n12. **DiverseGRPO** (arXiv 2512.21514, 2025) -- Mode collapse in image generation GRPO.\n13. **Why GRPO Needs Normalization** (arXiv 2601.23135, 2025) -- reward_std drives convergence rate.\n14. **GVPO** (NeurIPS 2025) -- Variance-based exploration-exploitation balance.\n15. **E-GRPO** (ICLR 2026) -- closest_prior_work. Entity-aware reward giving partial credit to near-miss negative samples.\n16. **GRPO-LEAD** (EMNLP 2025) -- Length-regularized rewards + difficulty-aware advantage reweighting.\n\n**Multi-objective GRPO:**\n17. **MO-GRPO** (arXiv 2509.22047, 2025) -- Reward hacking in multi-objective GRPO; variance-based normalization.\n18. **RDPO** (arXiv 2605.13641, 2026) -- Decorrelated reward subspace optimization.\n\n**GRPO theory:**\n19. **GRPO is Secretly a Process Reward Model** (under review ICML 2026) -- GRPO + ORM equivalence to PRM-aware RL; lambda-GRPO.\n20. **Reward Hacking in the Era of Large Models** (arXiv 2604.13602, 2026) -- Proxy Compression Hypothesis.\n\n**Contrastive reward for RL:**\n21. **Improving RLHF Using Contrastive Rewards** (arXiv 2403.07708, 2024) -- closest_contrastive_precedent. Offline baseline response for contrastive penalty in PPO.\n\n**RL training stability / quantization:**\n22-31. Multiple papers on quantization-aware RL (QuRL, QaRL, FP8-RL, Jet-RL, BitRL), training precision (FP16 vs BF16), stabilization formulations.\n\n**Multi-task RL / gradient imbalance:**\n32. **Imbalanced Gradients in RL Post-Training of Multi-Task LLMs** (Findings of EACL 2026) -- closest_prior_work. Gradient magnitude vs performance improvement uncorrelated.\n\nPlus ~18 more papers in supporting roles (LoRA theory, PEFT, self-training, ADELIE, etc.)\n\n---\n\n### CATEGORY 4: Papers about learning curves / training dynamics of RL for NLP\n\n**17 papers** matched. The most directly relevant:\n\n1. **DAPO** (NeurIPS 2025) -- Entropy collapse dynamics; frac_zero prompt filtering. \"accuracy=0 or 1 prompts produce zero gradients, reducing effective batch size.\"\n2. **Dr. GRPO** (COLM 2025) -- std(r)->0 causes advantage explosion; frac_zero_std->0.8 under extraction-only reward.\n3. **Why GRPO Needs Normalization** (arXiv 2601.23135, 2025) -- reward_std governs convergence rate; higher reward_std = faster convergence.\n4. **Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards** (arXiv 2511.03710, 2025) -- Per-prompt mean baseline inaccurate at low generation count; James-Stein shrinkage reduces gradient variance.\n5. **GVPO** (NeurIPS 2025) -- Variance term naturally balances exploration/exploitation, maintaining moderate entropy.\n6. **DiverseGRPO** (arXiv 2512.21514, 2025) -- GRPO output homogenization in later training stages.\n7. **Reward Shaping to Mitigate Reward Hacking** (arXiv 2502.18770, 2025) -- Reward should be bounded, fast-growing then slow-converging.\n8. **R1-RE** (arXiv 2507.04642, 2025) -- No catastrophic forgetting after GRPO training on sentence-level RE; performance on MATH-500/IFEval/GPQA maintained or improved.\n9. **Reinforcement Fine-Tuning Naturally Mitigates Forgetting** (arXiv 2507.05386, 2025) -- RFT gradients scaled by reward variance act as data-dependent regularizer.\n10. **The Energy Loss Phenomenon in RLHF** (ICML 2025) -- L1 norm divergence in last layer increases during RL training; excessive increase signals reward hacking.\n11. **Defeating the Training-Inference Mismatch via FP16** (arXiv 2510.26788, 2025) -- BF16 causes collapse at 150-600 steps in RL fine-tuning.\n12. **QuRL** (ICLR 2026) -- Quantized actor divergence grows exponentially causing training collapse in long-horizon RL.\n13. **RL Is Neither a Panacea Nor a Mirage** (arXiv 2508.16546, 2025) -- RL-FT recovers most OOD performance loss from SFT; recovery correlates with singular vector direction rotation.\n14. **The Impact of LoRA on Cluster Emergence** (arXiv 2402.15415, 2024) -- Phase transition from non-forgetting to forgetting as perturbation norm increases.\n15. **Posterior-GRPO** (arXiv 2508.05170, 2025) -- Conditional reward suppresses reward hacking dynamics.\n16. **MO-GRPO** (arXiv 2509.22047, 2025) -- Multi-objective reward hacking dynamics.\n17. **Regularized BoN with MBR** (NAACL 2025, 2024) -- Reward hacking dynamics in BoN scaling."
      }
    ],
    "totalDurationMs": 173373,
    "totalTokens": 53933,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3508,
      "cache_read_input_tokens": 46405,
      "output_tokens": 4019,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3508
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4019,
          "cache_read_input_tokens": 46405,
          "cache_creation_input_tokens": 3508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3508,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 0,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "7f1d8d2f-09bb-4dfc-9cd5-f8320b14c4a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T20:16:39.606Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize the findings from both agents into a clear summary for the user.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "045b4c90-1bd5-4fd5-9bdd-69b2c99e7639",
  "isSidechain": false,
  "requestId": "req_011CbAeeK3KTuYv8aZ2AYYib",
  "type": "assistant",
  "uuid": "f42b8162-7890-43e1-b229-447fa92597a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01We2eUspU6cuNSdau7tMQmZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3548,
      "cache_creation_input_tokens": 5086,
      "cache_read_input_tokens": 26369,
      "output_tokens": 2007,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3548,
          "output_tokens": 2007,
          "cache_read_input_tokens": 26369,
          "cache_creation_input_tokens": 5086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5086
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

_source line 26 · 2026-05-18T20:17:21.896Z_

## 文献联动分析结果

### 一、literature_map 中已有的相关论文

**Rejection Sampling / Selection Strategy 相关（7篇核心）：**
- **RAFT** (TMLR 2024) — 经典 RSFT 框架：迭代 generate-rank-filter-SFT
- **A Minimalist Approach** (arXiv 2504.11343, 2025) — key_theoretical_support。RAFT 匹配 GRPO/PPO 性能，GRPO 优势主要来自丢弃全错 prompt 而非 reward normalization
- **RS-DPO** (NAACL 2024 Findings) — 系统组合 rejection sampling + DPO，有 threshold/temperature 敏感性 ablation
- **RIFT** (arXiv 2601.09253, 2026) — direct_competitor。指出 RSFT 丢弃负样本的浪费，提出 reward-informed reweighting
- **AdaSTaR** (NeurIPS 2025) — RSFT random sampling 导致训练不平衡，提出 diversity + curriculum sampling，减少 58.6% FLOPs
- **TrajFusion** (arXiv 2602.04391, 2026) — 超越 binary accept/reject，融合部分正确轨迹
- **Rejection Sampling Secretly Performs PPO** (ICML 2025) — RSFT 与 PPO 在 marginal KL 约束下理论等价

**GRPO for IE 相关（7篇核心）：**
- **R1-RE** (arXiv 2507.04642, 2025) — direct_competitor。首个 RLVR (GRPO + verifiable reward) 用于 RE
- **ReasoningNER** (arXiv 2511.11978, 2025) — direct-competitor。GRPO 用于 NER，composite reward
- **EvidenceRL** (arXiv 2603.19532, 2026) — closest_competitor。GRPO 同时优化 grounding + correctness，hallucination 减少 5x
- **E-GRPO** (ICLR 2026) — closest_prior_work。Entity-aware reward 给 near-miss 负样本部分分数
- **GDPO** (ICML 2026) — closest_prior_work。多 reward GRPO 归一化 collapse 问题
- **R2GRPO** (arXiv 2505.22068, 2025) — MimicSFT + relevance/rule-mining reward 用于科学 IE
- **MORE-R1** (arXiv 2603.09478, 2026) — GRPO 用于多模态 RE

**训练动态 / Learning Curve 相关（5篇核心）：**
- **DAPO** (NeurIPS 2025) — entropy collapse 诊断；accuracy=0/1 prompt 产生零梯度
- **Dr. GRPO** (COLM 2025) — std(r)→0 导致 advantage explosion
- **Defeating the Training-Inference Mismatch via FP16** (arXiv 2510.26788, 2025) — BF16 在 150-600 steps 导致 collapse（与你们 GRPO bf16 实验直接相关）
- **RFT Naturally Mitigates Forgetting** (arXiv 2507.05386, 2025) — RFT 梯度被 reward variance 缩放，充当 regularizer
- **R1-RE** — GRPO 训练后 sentence-level RE 无 catastrophic forgetting

### 二、Web 搜索新发现（map 中可能缺少的）

| 论文 | Venue/Year | 关键发现 | 是否建议加入 map |
|------|-----------|---------|----------------|
| **RFT (Yuan et al.)** "Scaling Relationship on Learning Mathematical Reasoning" | arXiv 2308.01825, 2023 | rejection sampling 关键因子是 distinct reasoning paths 数量而非仅正确性；LLaMA-7B GSM8K 35.9%→49.3% | **是** — selection quality/diversity 的基础性证据，支撑 CED vs random 实验 |
| **GTPO** "Stabilizing GRPO via Gradient and Entropy Control" | arXiv 2508.03772, 2025 | 解决 GRPO gradient conflicts + policy collapse | 检查是否已在 map — 如无则加入 |
| **GRPO Effective Loss** (arXiv 2503.06639, 2025) | arXiv, 2025 | GRPO 渐近等价于 oracle policy gradient，理论最优性证明 | 检查是否已在 map |
| **Reward-based Input Construction for Cross-doc RE** | arXiv 2405.20649, 2024 | RL 训练 input sentence selection for RE | **是** — RL + RE 的直接先例 |
| **Adaptive RL Planning for Complex IE** | arXiv 2406.11455, 2024 | RL + LLM for IE，address false positives | **是** — RL + LLM IE 的最相关先例 |
| **Hierarchical Framework for RE with RL** (Takanobu et al.) | arXiv 1811.03925, 2018 | 早期 RL for joint entity-relation extraction | 可选 — 经典但较老 |

### 三、与实验结果的文献关联

**Random vs CED RSFT (gap=4.82pp)：**
- literature_map 已覆盖 RSFT 方法论论文（RAFT, AdaSTaR, RIFT），但**缺少 RFT (Yuan et al. 2023) 这篇 selection quality 的基础性实证**。该论文证明 distinct reasoning paths > random sampling，直接支撑 CED scoring 的价值。
- 无论文在 IE 任务上做过 scored vs random ablation — 你们的 4.82pp gap 是该领域的新数据点。

**GRPO bf16 ckpt-100 (+3.74pp over SFT)：**
- R1-RE 报告了 GRPO 在 sentence-level RE 上无 catastrophic forgetting，但未报告 learning curve。
- BF16 collapse 论文 (arXiv 2510.26788) 值得关注 — 需监控 GRPO 训练后期是否出现类似 collapse。
- EvidenceRL 是最直接的对比对象（也用 GRPO 优化 evidence grounding）。

### 四、建议

**建议更新 literature_map：**
1. 加入 **RFT (Yuan et al. 2023)** — role: theoretical_support，category: rsft_methodology。selection diversity/quality 的基础性证据。
2. 加入 **Reward-based Input Construction for Cross-doc RE** (2024) — role: related_method，category: rl_for_ie
3. 加入 **Adaptive RL Planning for Complex IE** (2024) — role: related_method，category: rl_for_ie
4. 检查 **GTPO** 和 **GRPO Effective Loss** 是否已在 map 中，如无则补充

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f42b8162-7890-43e1-b229-447fa92597a2",
  "isSidechain": false,
  "requestId": "req_011CbAeeK3KTuYv8aZ2AYYib",
  "type": "assistant",
  "uuid": "1d0e1b9c-8437-4907-9c32-cd4ac4c459f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01We2eUspU6cuNSdau7tMQmZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3548,
      "cache_creation_input_tokens": 5086,
      "cache_read_input_tokens": 26369,
      "output_tokens": 2007,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3548,
          "output_tokens": 2007,
          "cache_read_input_tokens": 26369,
          "cache_creation_input_tokens": 5086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5086
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

_source line 27_

```json
{
  "type": "last-prompt",
  "leafUuid": "1d0e1b9c-8437-4907-9c32-cd4ac4c459f5",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Check eval results against literature map",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "leafUuid": "1d0e1b9c-8437-4907-9c32-cd4ac4c459f5",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Check eval results against literature map",
  "sessionId": "d1967b82-9b64-485b-8419-ac1a11ebeb1d"
}
```

---
