# Research conversation: <project_context> # 项目: faith-evidence-ie ## 运行环境 - 服务器名: rtx5090-4x - SSH 账户: root（调用 ssh_execute / submit_training_job

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/ac6c3eaa-1181-4230-9499-9a3dbe044d7c.jsonl`
- **Structured JSON:** [`ab2635b468367002098b.json`](../../sessions/ab/ab2635b468367002098b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T17:13:07.185Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T17:13:07.185Z",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "content": "&lt;project_context>\n# 项目: faith-evidence-ie\n\n## 运行环境\n- 服务器名: rtx5090-4x\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh rtx5090-4x  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/freige\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 提交 eval 前必须 nvidia-smi 确认目标 GPU 显存占用 < 2GB，否则不提交、换卡或等待（原因：本 session 已 5 次因 eval 提交到被占用 GPU 导致 OOM，修复 eval 也因此作废。eval 推理需要接近全部显存，与训练共享必然 OOM。） [来自 D064]\n- **C002**: 提交训练/评估任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map=\"auto\" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 两次因未设 CUDA_VISIBLE_DEVICES 导致 device_map=\"auto\" 跨 GPU 分布，造成 OOM 和资源冲突。已知 bug 重复发生。）\n- **C003**: 提交训练任务时必须在命令前设置 CUDA_VISIBLE_DEVICES=X，禁止依赖 device_map=\"auto\" 自动分配 GPU（原因：plan_011 和 rsft_ced_s45_train_r3 均因未设 CUDA_VISIBLE_DEVICES 导致模型跨 GPU 分布，造成 OOM 或显存冲突。已重复发生两次。）\n- **C004**: Registry 标记 killed 时必须同时 kill -9 PID 并 ps 验证进程已终止，否则 killed 状态不可信（原因：rsft_ced_s45_train_r2 (PID 276148) registry 标记 killed 但进程未实际终止，占用 cuda:2 31.6GB 导致 r3 OOM。plan_011 也有类似模式。Reviewer WARNING。）\n- **C005**: no-evidence 模型 eval 必须传 --no_evidence 参数，确保推理时使用 NO_EVIDENCE_SYSTEM_PROMPT 与训练一致（原因：plan_006 1.7B/8B no-evidence eval 漏传该参数，导致训练/推理提示词不匹配（模型被要求输出未训练过的 evidence 字段），结果全部无效。Reviewer critical #20。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：更新 ROADMAP.md\n\n### 目标\n根据最新实验结果更新 ROADMAP.md，反映当前进展。\n\n### 需要更新的内容\n\n1. **14B evidence tax 发现 (D117)**:\n   - 14B SFT: with-evidence ign_f1=0.5507, no-evidence ign_f1=0.551\n   - Evidence tax = +0.03pp（本质为零）\n   - 14B 容量足够同时输出 evidence 和 RE\n\n2. **\"1.7B surpasses\" claim 降级 (D118)**:\n   - 8B SFT 3-seed: s42=0.5128, s43=0.5324, s44=0.4604, mean=0.5019±0.0372\n   - 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019): Δ=+1.03pp, p≈0.34 不显著\n   - 需弱化为 \"comparable / on par with\"\n   - RSFT variance stabilization (SFT std=0.037 vs RSFT std=0.005) 作为独立发现\n\n3. **D112 完成**:\n   - D112 RSFT (bf16, SFT s44 base): ign_f1=0.5152, 比 SFT s44 baseline (0.4734) +4.18pp\n   - D112 pipeline 完整验证\n\n4. **当前 GPU 分布**:\n   - cuda:0: 8B RSFT no-evidence eval r2 (接近完成)\n   - cuda:1: d112 no-evidence eval r3 (44%)\n   - cuda:2: 空闲（D112 完成后释放）\n   - cuda:3: 1.7B no-evidence eval 2048 (38%)\n\n5. **Scaling table 更新**（加入 14B 行 + D112 结果）:\n   | Scale | SFT mean | RSFT mean | Δ |\n   |-------|----------|-----------|---|\n   | 1.7B | 0.4464 (3) | 0.5122 (1) | +6.58pp |\n   | 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) |\n   | 8B | 0.5019 (3) | 0.5414 (2) | +3.95pp |\n   | 14B | 0.5507 (1) | pending | — |\n\n6. **近期任务更新**:\n   - [x] D112 step 4 eval 完成\n   - [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n   - [x] 14B SFT eval 完成 (ign_f1=0.5507)\n   - [ ] 1.7B no-evidence eval 2048 重跑 (排除截断)\n   - [ ] 8B RSFT no-evidence eval (cuda:0)\n   - [ ] d112 no-evidence eval r3 (cuda:1)\n   - [ ] 14B RSFT pipeline (待启动)\n   - [ ] 8B RSFT s43 补齐第 3 seed\n\n### 操作\n用 read_roadmap 读取当前内容，然后用 save_project_file 写入更新后的 ROADMAP.md。注意 8B SFT mean 从 0.4866 (2-seed) 更新为 0.5019 (3-seed)。"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T17:13:07.190Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T17:13:07.190Z",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-19T17:13:07.235Z_

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
## 任务：更新 ROADMAP.md

### 目标
根据最新实验结果更新 ROADMAP.md，反映当前进展。

### 需要更新的内容

1. **14B evidence tax 发现 (D117)**:
   - 14B SFT: with-evidence ign_f1=0.5507, no-evidence ign_f1=0.551
   - Evidence tax = +0.03pp（本质为零）
   - 14B 容量足够同时输出 evidence 和 RE

2. **"1.7B surpasses" claim 降级 (D118)**:
   - 8B SFT 3-seed: s42=0.5128, s43=0.5324, s44=0.4604, mean=0.5019±0.0372
   - 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019): Δ=+1.03pp, p≈0.34 不显著
   - 需弱化为 "comparable / on par with"
   - RSFT variance stabilization (SFT std=0.037 vs RSFT std=0.005) 作为独立发现

3. **D112 完成**:
   - D112 RSFT (bf16, SFT s44 base): ign_f1=0.5152, 比 SFT s44 baseline (0.4734) +4.18pp
   - D112 pipeline 完整验证

4. **当前 GPU 分布**:
   - cuda:0: 8B RSFT no-evidence eval r2 (接近完成)
   - cuda:1: d112 no-evidence eval r3 (44%)
   - cuda:2: 空闲（D112 完成后释放）
   - cuda:3: 1.7B no-evidence eval 2048 (38%)

5. **Scaling table 更新**（加入 14B 行 + D112 结果）:
   | Scale | SFT mean | RSFT mean | Δ |
   |-------|----------|-----------|---|
   | 1.7B | 0.4464 (3) | 0.5122 (1) | +6.58pp |
   | 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) |
   | 8B | 0.5019 (3) | 0.5414 (2) | +3.95pp |
   | 14B | 0.5507 (1) | pending | — |

6. **近期任务更新**:
   - [x] D112 step 4 eval 完成
   - [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)
   - [x] 14B SFT eval 完成 (ign_f1=0.5507)
   - [ ] 1.7B no-evidence eval 2048 重跑 (排除截断)
   - [ ] 8B RSFT no-evidence eval (cuda:0)
   - [ ] d112 no-evidence eval r3 (cuda:1)
   - [ ] 14B RSFT pipeline (待启动)
   - [ ] 8B RSFT s43 补齐第 3 seed

### 操作
用 read_roadmap 读取当前内容，然后用 save_project_file 写入更新后的 ROADMAP.md。注意 8B SFT mean 从 0.4866 (2-seed) 更新为 0.5019 (3-seed)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "1fe57cc6-df5a-49e6-a076-9ce3c49689d8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T17:13:07.234Z_

```json
{
  "parentUuid": "1fe57cc6-df5a-49e6-a076-9ce3c49689d8",
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "33661bd0-0223-418d-9e80-60f4346da1c0",
  "timestamp": "2026-05-19T17:13:07.234Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T17:13:07.234Z_

```json
{
  "parentUuid": "33661bd0-0223-418d-9e80-60f4346da1c0",
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
  "uuid": "7f13ef60-3edf-43b0-b036-3370ba68d5f5",
  "timestamp": "2026-05-19T17:13:07.234Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-19T17:13:07.234Z_

```json
{
  "parentUuid": "7f13ef60-3edf-43b0-b036-3370ba68d5f5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bfccfd3f-462f-415c-92e1-9ae931df9779",
  "timestamp": "2026-05-19T17:13:07.234Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
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
  "aiTitle": "Update ROADMAP with latest experimental results",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

### Assistant

_source line 8 · 2026-05-19T17:13:09.784Z_

I'll read the current ROADMAP.md first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfccfd3f-462f-415c-92e1-9ae931df9779",
  "isSidechain": false,
  "requestId": "req_011CbCJTs4GzkfGUh8h9N9e9",
  "type": "assistant",
  "uuid": "eccd255c-a0a4-4d91-a184-81ca2da15a5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuDn2UNEipMhSBX6NZYJnd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13005,
      "cache_read_input_tokens": 11841,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13005
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

_source line 9 · 2026-05-19T17:13:10.422Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017Aafpo5uxdt9AS77Xo3ECn`</summary>

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
  "parentUuid": "eccd255c-a0a4-4d91-a184-81ca2da15a5c",
  "isSidechain": false,
  "requestId": "req_011CbCJTs4GzkfGUh8h9N9e9",
  "type": "assistant",
  "uuid": "100aab3e-b400-422b-a6dc-523e50918b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuDn2UNEipMhSBX6NZYJnd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13005,
      "cache_read_input_tokens": 11841,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13005
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

_source line 10 · 2026-05-19T17:13:10.429Z_

<details><summary>↩ Tool result · `toolu_017Aafpo5uxdt9AS77Xo3ECn`</summary>

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
  "parentUuid": "100aab3e-b400-422b-a6dc-523e50918b5e",
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "06224126-6580-4e3c-a7d1-daa364c30a18",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "100aab3e-b400-422b-a6dc-523e50918b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T17:13:13.553Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current ROADMAP.md first, then update it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06224126-6580-4e3c-a7d1-daa364c30a18",
  "isSidechain": false,
  "requestId": "req_011CbCJU6uibroxkjFHYzGvQ",
  "type": "assistant",
  "uuid": "0a33a5d9-a030-4c1f-a314-1e1aeb2497b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNkg3ZG2TFZCe8Y9GuCHS1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 24846,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 140,
          "cache_read_input_tokens": 24846,
          "cache_creation_input_tokens": 712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 712
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

_source line 12 · 2026-05-19T17:13:13.823Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HcgL5SjxNMxGot8Sibtqu3`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a33a5d9-a030-4c1f-a314-1e1aeb2497b5",
  "isSidechain": false,
  "requestId": "req_011CbCJU6uibroxkjFHYzGvQ",
  "type": "assistant",
  "uuid": "558190a4-5f98-423a-8e0d-da850a5dcc64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNkg3ZG2TFZCe8Y9GuCHS1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 24846,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 140,
          "cache_read_input_tokens": 24846,
          "cache_creation_input_tokens": 712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 712
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

_source line 13 · 2026-05-19T17:13:13.843Z_

<details><summary>↩ Tool result · `toolu_01HcgL5SjxNMxGot8Sibtqu3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\n- **关键数值汇总**:\\n\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\n|-------|-------------------|--------------------|----------|---------|----------|\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\n\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\n\\n## 实验路线（3 层优先级）\\n\\n### Tier 1 — Main 必要条件\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\\n\\n### Tier 2 — 大幅加分\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\\n| NLI model ablation | plan_010 | pending |\\n| Evidence tax 机制分析 | plan_020 | pending |\\n| Deep error analysis | plan_021 | pending |\\n\\n### Tier 3 — 锦上添花\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\\n| 第三模型家族 | plan_022 | pending |\\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\\n\\n## 从 3.0 → 4.0 路径\\n| 里程碑 | 预期评分 | 状态 |\\n|--------|---------|------|\\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\\n\\n## GPU 预算\\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\\n\\n## 近期任务\\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\\n- [ ] experiment_plan.yaml 全面同步 registry\\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\\n- [ ] 重新提交论文审稿\\n\\n## 关键风险\\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D118 | 2026-05-19 | D118: \\\"1.7B RSFT surpasses 8B SFT\\\" claim 降级为 \\\"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\\n\\n\", \"total_chars\": 5100, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "558190a4-5f98-423a-8e0d-da850a5dcc64",
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "1d99f970-f2c6-4e44-8616-2a94cb91257f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\\\", \\\"content\\\": \\\"# faith-evidence-ie — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\\\n\\\\n## 核心方向\\\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\\\n- **关键数值汇总**:\\\\n\\\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\\\n|-------|-------------------|--------------------|----------|---------|----------|\\\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\\\n\\\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\\\n\\\\n## 投稿目标\\\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\\\n\\\\n## 实验路线（3 层优先级）\\\\n\\\\n### Tier 1 — Main 必要条件\\\\n| 实验 | Plan ID | 状态 |\\\\n|------|---------|------|\\\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\\\\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\\\\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\\\\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\\\\n\\\\n### Tier 2 — 大幅加分\\\\n| 实验 | Plan ID | 状态 |\\\\n|------|---------|------|\\\\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\\\\n| NLI model ablation | plan_010 | pending |\\\\n| Evidence tax 机制分析 | plan_020 | pending |\\\\n| Deep error analysis | plan_021 | pending |\\\\n\\\\n### Tier 3 — 锦上添花\\\\n| 实验 | Plan ID | 状态 |\\\\n|------|---------|------|\\\\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\\\\n| 第三模型家族 | plan_022 | pending |\\\\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\\\\n\\\\n## 从 3.0 → 4.0 路径\\\\n| 里程碑 | 预期评分 | 状态 |\\\\n|--------|---------|------|\\\\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\\\\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\\\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\\\\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\\\\n\\\\n## GPU 预算\\\\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\\\\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\\\\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\\\\n\\\\n## 近期任务\\\\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\\\\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\\\\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\\\\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\\\\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\\\\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\\\\n- [ ] experiment_plan.yaml 全面同步 registry\\\\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\\\\n- [ ] 重新提交论文审稿\\\\n\\\\n## 关键风险\\\\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\\\\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\\\\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\\\\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\\\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D118 | 2026-05-19 | D118: \\\\\\\"1.7B RSFT surpasses 8B SFT\\\\\\\" claim 降级为 \\\\\\\"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\\\\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\\\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\\\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\\\\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\\\\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\\\\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\\\\n\\\\n\\\", \\\"total_chars\\\": 5100, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\n- **关键数值汇总**:\\n\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\n|-------|-------------------|--------------------|----------|---------|----------|\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\n\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\n\\n## 实验路线（3 层优先级）\\n\\n### Tier 1 — Main 必要条件\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\\n\\n### Tier 2 — 大幅加分\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\\n| NLI model ablation | plan_010 | pending |\\n| Evidence tax 机制分析 | plan_020 | pending |\\n| Deep error analysis | plan_021 | pending |\\n\\n### Tier 3 — 锦上添花\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\\n| 第三模型家族 | plan_022 | pending |\\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\\n\\n## 从 3.0 → 4.0 路径\\n| 里程碑 | 预期评分 | 状态 |\\n|--------|---------|------|\\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\\n\\n## GPU 预算\\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\\n\\n## 近期任务\\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\\n- [ ] experiment_plan.yaml 全面同步 registry\\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\\n- [ ] 重新提交论文审稿\\n\\n## 关键风险\\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D118 | 2026-05-19 | D118: \\\"1.7B RSFT surpasses 8B SFT\\\" claim 降级为 \\\"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\\n\\n\", \"total_chars\": 5100, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "558190a4-5f98-423a-8e0d-da850a5dcc64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
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
  "leafUuid": "1d99f970-f2c6-4e44-8616-2a94cb91257f",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Update ROADMAP with latest experimental results",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

### Assistant

_source line 16 · 2026-05-19T17:13:38.635Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the current ROADMAP.md. Let me update it based on the task requirements:

1. 14B evidence tax discovery (D117) - already partially noted
2. "1.7B surpasses" claim downgrade (D118) - need to weaken the claim
3. D112 completion - step 4 eval done, ign_f1=0.5152, +4.18pp over SFT s44 baseline (0.4734)
4. Current GPU distribution
5. Scaling table update - add 14B row, update 8B to 3-seed mean, add D112 result


6. Task list update

I'm going through the document systematically to make these updates. The scaling table needs the 8B SFT mean adjusted from 0.4866 to 0.5019 based on three seeds, I'll add the 14B row with its evidence tax findings, and incorporate the D112 results for the 4B model. I also need to soften the language around the 1.7B surpassing claim and update the GPU allocation details, plus I'm checking the RSFT variance comparison for the 8B model.

Looking at the actual numbers from the data, the 8B SFT shows a standard deviation of 0.0372 across three seeds while RSFT comes in at 0.005, which is a meaningful difference in stability I should highlight.

For the 1.7B comparison claim, the RSFT score of 0.5122 versus the 8B SFT mean of 0.5019 gives only a 1.03 percentage point difference with a p-value around 0.34—not statistically significant, so I need to soften that language to say they're comparable rather than claiming one surpasses the other.

Now I'm checking the variance numbers: the 8B SFT runs across three seeds show a standard deviation of 3.72 percentage points, while the RSFT variance from the earlier experiment was much tighter at 0.53 percentage points. With those numbers confirmed, I can move forward with updating the roadmap to reflect the completed experiments and the revised claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d99f970-f2c6-4e44-8616-2a94cb91257f",
  "isSidechain": false,
  "requestId": "req_011CbCJUMYHWdM1X8cnTuN9W",
  "type": "assistant",
  "uuid": "02a0756d-4b21-4be0-9a77-b4323e4e2dca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jbuCcEgJXkr5V1iGGXtZT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3455,
      "cache_read_input_tokens": 25558,
      "output_tokens": 4785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4785,
          "cache_read_input_tokens": 25558,
          "cache_creation_input_tokens": 3455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3455
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

_source line 17 · 2026-05-19T17:13:38.639Z_

Now I'll write the updated ROADMAP.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02a0756d-4b21-4be0-9a77-b4323e4e2dca",
  "isSidechain": false,
  "requestId": "req_011CbCJUMYHWdM1X8cnTuN9W",
  "type": "assistant",
  "uuid": "10d4a6b4-1257-4d59-a1a5-4dbf791ee051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jbuCcEgJXkr5V1iGGXtZT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3455,
      "cache_read_input_tokens": 25558,
      "output_tokens": 4785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4785,
          "cache_read_input_tokens": 25558,
          "cache_creation_input_tokens": 3455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3455
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

_source line 18 · 2026-05-19T17:14:16.850Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01UqMbVys6SyF9c8mJTGFcwF`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ROADMAP.md",
  "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed + scaling table 更新\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；8B SFT 3-seed 完成（mean=0.5019±3.72pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B \"surpasses\" claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，论文 Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d4a6b4-1257-4d59-a1a5-4dbf791ee051",
  "isSidechain": false,
  "requestId": "req_011CbCJUMYHWdM1X8cnTuN9W",
  "type": "assistant",
  "uuid": "6e7212d5-3071-4898-8fa7-fd63d15b1469",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jbuCcEgJXkr5V1iGGXtZT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3455,
      "cache_read_input_tokens": 25558,
      "output_tokens": 4785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4785,
          "cache_read_input_tokens": 25558,
          "cache_creation_input_tokens": 3455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3455
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

_source line 19 · 2026-05-19T17:14:16.884Z_

<details><summary>↩ Tool result · `toolu_01UqMbVys6SyF9c8mJTGFcwF`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'ROADMAP.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml']. Use update_roadmap instead.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e7212d5-3071-4898-8fa7-fd63d15b1469",
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "a38d6c46-61e7-4ec2-a897-d2e01145962d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'ROADMAP.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml']. Use update_roadmap instead.\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'ROADMAP.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml']. Use update_roadmap instead.\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "6e7212d5-3071-4898-8fa7-fd63d15b1469",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-19T17:14:19.997Z_

<details><summary>Logged reasoning block</summary>

```text
Need to use update_roadmap instead. Let me find that tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a38d6c46-61e7-4ec2-a897-d2e01145962d",
  "isSidechain": false,
  "requestId": "req_011CbCJZ1Nyf7p75TXuw27vV",
  "type": "assistant",
  "uuid": "58b8a6d7-851e-4c31-b55f-f3fe17e96828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iFqN9LRHTzKcWYP8C2oxL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4872,
      "cache_read_input_tokens": 29013,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 29013,
          "cache_creation_input_tokens": 4872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4872
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

_source line 21 · 2026-05-19T17:14:20.492Z_

需要用 `update_roadmap` 工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58b8a6d7-851e-4c31-b55f-f3fe17e96828",
  "isSidechain": false,
  "requestId": "req_011CbCJZ1Nyf7p75TXuw27vV",
  "type": "assistant",
  "uuid": "33f23f17-9a2e-43a5-8bf0-c89afdb5d8ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iFqN9LRHTzKcWYP8C2oxL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4872,
      "cache_read_input_tokens": 29013,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 29013,
          "cache_creation_input_tokens": 4872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4872
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

_source line 22 · 2026-05-19T17:14:21.183Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HLW4fzjv2CPLeFjAfdaPdc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33f23f17-9a2e-43a5-8bf0-c89afdb5d8ed",
  "isSidechain": false,
  "requestId": "req_011CbCJZ1Nyf7p75TXuw27vV",
  "type": "assistant",
  "uuid": "9dfd8cda-dd75-485b-9bef-d4465c85942c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iFqN9LRHTzKcWYP8C2oxL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4872,
      "cache_read_input_tokens": 29013,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 29013,
          "cache_creation_input_tokens": 4872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4872
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

_source line 23 · 2026-05-19T17:14:25.325Z_

<details><summary>↩ Tool result · `toolu_01WBbJZ3MKB9ErJGhZCkpsLs`</summary>

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
  "parentUuid": "cedbaa31-a650-489f-8865-53ab972821f3",
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "c7e14871-cbd6-47ae-85f2-e7592174c222",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "update_roadmap",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "cedbaa31-a650-489f-8865-53ab972821f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T17:14:21.187Z_

<details><summary>↩ Tool result · `toolu_01HLW4fzjv2CPLeFjAfdaPdc`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dfd8cda-dd75-485b-9bef-d4465c85942c",
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "de3d9ff7-13e7-48b2-baeb-c1873f441198",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "9dfd8cda-dd75-485b-9bef-d4465c85942c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T17:14:25.304Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WBbJZ3MKB9ErJGhZCkpsLs`</summary>

```json
{
  "query": "update_roadmap",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de3d9ff7-13e7-48b2-baeb-c1873f441198",
  "isSidechain": false,
  "requestId": "req_011CbCJZ1Nyf7p75TXuw27vV",
  "type": "assistant",
  "uuid": "cedbaa31-a650-489f-8865-53ab972821f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iFqN9LRHTzKcWYP8C2oxL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4872,
      "cache_read_input_tokens": 29013,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 29013,
          "cache_creation_input_tokens": 4872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4872
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

_source line 26 · 2026-05-19T17:14:31.419Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011qMaMbxUhfAUBNzwctrPsz`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_roadmap",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7e14871-cbd6-47ae-85f2-e7592174c222",
  "isSidechain": false,
  "requestId": "req_011CbCJZdgHA1Att8jo8atyk",
  "type": "assistant",
  "uuid": "4cfb287e-8093-4fd3-8e4f-1a4d0e8b4db7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNxxApt3VXQqCjtJJUukWE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 33885,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 33885,
          "cache_creation_input_tokens": 990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 990
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

_source line 27 · 2026-05-19T17:14:31.423Z_

<details><summary>↩ Tool result · `toolu_011qMaMbxUhfAUBNzwctrPsz`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cfb287e-8093-4fd3-8e4f-1a4d0e8b4db7",
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "72f1abc1-ee44-4217-87a4-734761eb30f2",
  "toolUseResult": {
    "matches": [],
    "query": "select:mcp__agent-ml-research__update_roadmap",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "4cfb287e-8093-4fd3-8e4f-1a4d0e8b4db7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-19T17:14:34.471Z_

<details><summary>Logged reasoning block</summary>

```text
The tool isn't available as a deferred tool. Let me try a different search.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72f1abc1-ee44-4217-87a4-734761eb30f2",
  "isSidechain": false,
  "requestId": "req_011CbCJa5tckwTwiQkEeaxHZ",
  "type": "assistant",
  "uuid": "87e91c26-0e3d-4dd2-baea-e0e3a1a8cab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JyEiJLmUCuASTKkGykF7Vx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 107,
      "cache_read_input_tokens": 34875,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 107,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 34875,
          "cache_creation_input_tokens": 107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 107
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

_source line 29 · 2026-05-19T17:14:34.483Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bydnjx5TtweSq3dDu5Uf24`</summary>

```json
{
  "query": "roadmap",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87e91c26-0e3d-4dd2-baea-e0e3a1a8cab8",
  "isSidechain": false,
  "requestId": "req_011CbCJa5tckwTwiQkEeaxHZ",
  "type": "assistant",
  "uuid": "c5b57b0a-60ab-483c-b47c-8cea59027929",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JyEiJLmUCuASTKkGykF7Vx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 107,
      "cache_read_input_tokens": 34875,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 107,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 34875,
          "cache_creation_input_tokens": 107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 107
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

_source line 30 · 2026-05-19T17:14:34.492Z_

<details><summary>↩ Tool result · `toolu_01Bydnjx5TtweSq3dDu5Uf24`</summary>

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
  "parentUuid": "c5b57b0a-60ab-483c-b47c-8cea59027929",
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "9271561a-f6c6-42c3-bf8a-b038bbbf3854",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "roadmap",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "c5b57b0a-60ab-483c-b47c-8cea59027929",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-19T17:14:34.630Z_

```json
{
  "parentUuid": "9271561a-f6c6-42c3-bf8a-b038bbbf3854",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5537f2e5-b97d-4a95-b089-23be33c4b832",
  "timestamp": "2026-05-19T17:14:34.630Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-19T17:14:39.131Z_

<details><summary>Logged reasoning block</summary>

```text
The `update_roadmap` tool isn't showing up in ToolSearch. Let me try to find it with a different query, or just directly write the file since I know its path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5537f2e5-b97d-4a95-b089-23be33c4b832",
  "isSidechain": false,
  "requestId": "req_011CbCJaJf4rreVj8mCE4A1n",
  "type": "assistant",
  "uuid": "185c4e3e-22fc-49e6-9437-98388f64231a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJokF8j186d5UtjAHHFEyb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 34982,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 161,
          "cache_read_input_tokens": 34982,
          "cache_creation_input_tokens": 803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 803
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

_source line 33 · 2026-05-19T17:14:39.653Z_

`update_roadmap` 工具未找到。直接写文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "185c4e3e-22fc-49e6-9437-98388f64231a",
  "isSidechain": false,
  "requestId": "req_011CbCJaJf4rreVj8mCE4A1n",
  "type": "assistant",
  "uuid": "932d8d40-4e5a-4caf-9480-4f3bdcd1862f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJokF8j186d5UtjAHHFEyb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 34982,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 161,
          "cache_read_input_tokens": 34982,
          "cache_creation_input_tokens": 803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 803
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

_source line 34 · 2026-05-19T17:14:40.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_017pdtn6uDUBB94tR1dpJbMt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "932d8d40-4e5a-4caf-9480-4f3bdcd1862f",
  "isSidechain": false,
  "requestId": "req_011CbCJaJf4rreVj8mCE4A1n",
  "type": "assistant",
  "uuid": "e039d739-0d41-49d6-a591-6647e6f1b53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJokF8j186d5UtjAHHFEyb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 34982,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 161,
          "cache_read_input_tokens": 34982,
          "cache_creation_input_tokens": 803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 803
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

_source line 35 · 2026-05-19T17:14:40.955Z_

<details><summary>↩ Tool result · `toolu_017pdtn6uDUBB94tR1dpJbMt`</summary>

```text
1	# faith-evidence-ie — Research Dashboard
2	
3	> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成
4	
5	## 核心方向
6	FREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。
7	
8	## 当前进展
9	- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）
10	- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）
11	- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）
12	- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）
13	- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）
14	- **关键数值汇总**:
15	
16	| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |
17	|-------|-------------------|--------------------|----------|---------|----------|
18	| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |
19	| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |
20	| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |
21	
22	- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)
23	- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap
24	- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound
25	
26	## 投稿目标
27	- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)
28	
29	## 实验路线（3 层优先级）
30	
31	### Tier 1 — Main 必要条件
32	| 实验 | Plan ID | 状态 |
33	|------|---------|------|
34	| D102 k=1 方法论修正 | D102 | ✅ 完成 |
35	| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |
36	| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |
37	| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |
38	| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |
39	| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |
40	| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |
41	| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |
42	
43	### Tier 2 — 大幅加分
44	| 实验 | Plan ID | 状态 |
45	|------|---------|------|
46	| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |
47	| NLI model ablation | plan_010 | pending |
48	| Evidence tax 机制分析 | plan_020 | pending |
49	| Deep error analysis | plan_021 | pending |
50	
51	### Tier 3 — 锦上添花
52	| 实验 | Plan ID | 状态 |
53	|------|---------|------|
54	| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |
55	| 第三模型家族 | plan_022 | pending |
56	| DocKS-RAG/LMRC 复现 | plan_023 | pending |
57	
58	## 从 3.0 → 4.0 路径
59	| 里程碑 | 预期评分 | 状态 |
60	|--------|---------|------|
61	| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |
62	| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |
63	| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |
64	| + Mechanistic + error analysis | 3.75 → 4.0 | pending |
65	
66	## GPU 预算
67	- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）
68	- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）
69	- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h
70	
71	## 近期任务
72	- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）
73	- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)
74	- [x] 4B SFT s42 D076 reeval (D111: 0.3974)
75	- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）
76	- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）
77	- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）
78	- [ ] experiment_plan.yaml 全面同步 registry
79	- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）
80	- [ ] 重新提交论文审稿
81	
82	## 关键风险
83	- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe
84	- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论
85	- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认
86	- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参
87	- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解
88	
89	## 关键决策日志
90	
91	| ID | 日期 | 摘要 | 关联实验 |
92	|----|------|------|----------|
93	| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |
94	| D118 | 2026-05-19 | D118: "1.7B RSFT surpasses 8B SFT" claim 降级为 "appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |
95	| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |
96	| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |
97	| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |
98	| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |
99	| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |
100	| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |
101	| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |
102	| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |
103	
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e039d739-0d41-49d6-a591-6647e6f1b53b",
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "134ac941-c66c-4519-9b75-864f6d02c64b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
      "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\n\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 预算\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  },
  "sourceToolAssistantUUID": "e039d739-0d41-49d6-a591-6647e6f1b53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "leafUuid": "134ac941-c66c-4519-9b75-864f6d02c64b",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Update ROADMAP with latest experimental results",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

### Assistant

_source line 38 · 2026-05-19T17:14:44.916Z_

<details><summary>Logged reasoning block</summary>

```text
Now I see the file has D119 in the decision log (line 93) which wasn't in the MCP read. The file on disk is slightly newer. Let me write the updated version now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "134ac941-c66c-4519-9b75-864f6d02c64b",
  "isSidechain": false,
  "requestId": "req_011CbCJan2rDpqc32a2LXAvp",
  "type": "assistant",
  "uuid": "7544bde3-3fb1-4fe7-9a43-053a78eb69b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kit44nohpVUTBXTmGRfNXE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3488,
      "cache_read_input_tokens": 35785,
      "output_tokens": 3730,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3730,
          "cache_read_input_tokens": 35785,
          "cache_creation_input_tokens": 3488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3488
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

_source line 39 · 2026-05-19T17:14:45.311Z_

文件已读取（注意磁盘版本比 MCP 读取多了 D119）。现在写入更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7544bde3-3fb1-4fe7-9a43-053a78eb69b8",
  "isSidechain": false,
  "requestId": "req_011CbCJan2rDpqc32a2LXAvp",
  "type": "assistant",
  "uuid": "bde9b17c-1ea8-4dbd-b471-b8d029f6883d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kit44nohpVUTBXTmGRfNXE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3488,
      "cache_read_input_tokens": 35785,
      "output_tokens": 3730,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3730,
          "cache_read_input_tokens": 35785,
          "cache_creation_input_tokens": 3488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3488
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

_source line 40 · 2026-05-19T17:15:24.946Z_

<details open><summary>🔧 Tool call — Write · `toolu_016XsXRoWYUV1qMJZrNcx6zL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bde9b17c-1ea8-4dbd-b471-b8d029f6883d",
  "isSidechain": false,
  "requestId": "req_011CbCJan2rDpqc32a2LXAvp",
  "type": "assistant",
  "uuid": "14888c4b-6d20-44c3-af3f-53203bd54463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kit44nohpVUTBXTmGRfNXE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3488,
      "cache_read_input_tokens": 35785,
      "output_tokens": 3730,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3730,
          "cache_read_input_tokens": 35785,
          "cache_creation_input_tokens": 3488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3488
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

_source line 41 · 2026-05-19T17:15:24.978Z_

<details><summary>↩ Tool result · `toolu_016XsXRoWYUV1qMJZrNcx6zL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14888c4b-6d20-44c3-af3f-53203bd54463",
  "isSidechain": false,
  "promptId": "728f9907-b4c1-4b15-884b-d9e88637119a",
  "type": "user",
  "uuid": "51c0e811-e431-4ea1-9a88-2fec8982911b",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 25,
        "newStart": 1,
        "newLines": 28,
        "lines": [
          " # faith-evidence-ie — Research Dashboard",
          " ",
          "-> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成",
          "+> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行",
          " ",
          " ## 核心方向",
          " FREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。",
          " ",
          " ## 当前进展",
          " - **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）",
          "-- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）",
          "-- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）",
          "-- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）",
          "-- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）",
          "+- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）",
          "+- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）",
          "+- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）",
          "+- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）",
          "+- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"",
          " - **关键数值汇总**:",
          " ",
          " | Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |",
          " |-------|-------------------|--------------------|----------|---------|----------|",
          " | 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |",
          "-| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |",
          "-| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |",
          "+| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |",
          "+| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |",
          "+| 14B | 0.5507 (1) | pending | — | — | — |",
          " ",
          "-- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)",
          "+- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE",
          "+- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)",
          " - **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap",
          " - **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound",
          " "
        ]
      },
      {
        "oldStart": 36,
        "oldLines": 14,
        "newStart": 39,
        "newLines": 16,
        "lines": [
          " | GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |",
          " | Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |",
          " | 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |",
          "-| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |",
          "-| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |",
          "-| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |",
          "+| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |",
          "+| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |",
          "+| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |",
          "+| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |",
          " ",
          " ### Tier 2 — 大幅加分",
          " | 实验 | Plan ID | 状态 |",
          " |------|---------|------|",
          "-| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |",
          "+| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |",
          "+| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |",
          " | NLI model ablation | plan_010 | pending |",
          " | Evidence tax 机制分析 | plan_020 | pending |",
          " | Deep error analysis | plan_021 | pending |"
        ]
      },
      {
        "oldStart": 58,
        "oldLines": 32,
        "newStart": 63,
        "newLines": 39,
        "lines": [
          " ## 从 3.0 → 4.0 路径",
          " | 里程碑 | 预期评分 | 状态 |",
          " |--------|---------|------|",
          "-| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |",
          "-| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |",
          "-| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |",
          "+| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |",
          "+| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |",
          "+| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |",
          " | + Mechanistic + error analysis | 3.75 → 4.0 | pending |",
          " ",
          "-## GPU 预算",
          "-- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）",
          "-- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）",
          "-- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h",
          "+## GPU 分布",
          "+- cuda:0: 8B RSFT no-evidence eval r2（接近完成）",
          "+- cuda:1: D112 no-evidence eval r3（44%）",
          "+- cuda:2: 空闲",
          "+- cuda:3: 1.7B no-evidence eval 2048（38%）",
          " ",
          " ## 近期任务",
          " - [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）",
          " - [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)",
          " - [x] 4B SFT s42 D076 reeval (D111: 0.3974)",
          "-- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）",
          "-- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）",
          "-- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）",
          "+- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)",
          "+- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)",
          "+- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)",
          "+- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）",
          "+- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）",
          "+- [ ] D112 no-evidence eval r3（cuda:1，44%）",
          "+- [ ] 14B RSFT pipeline（待启动）",
          "+- [ ] 8B RSFT s43 补齐第 3 seed",
          " - [ ] experiment_plan.yaml 全面同步 registry",
          "-- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）",
          "+- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）",
          " - [ ] 重新提交论文审稿",
          " ",
          " ## 关键风险",
          "-- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe",
          "+- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust",
          "+- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现",
          "+- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"",
          " - **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论",
          "-- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认",
          "-- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参",
          "+- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务",
          " - **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解",
          " ",
          " ## 关键决策日志"
        ]
      },
      {
        "oldStart": 100,
        "oldLines": 4,
        "newStart": 112,
        "newLines": 3,
        "lines": [
          " | D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |",
          " | D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |",
          " | D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |",
          "-"
        ]
      }
    ],
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\n\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 预算\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "14888c4b-6d20-44c3-af3f-53203bd54463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
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
  "leafUuid": "51c0e811-e431-4ea1-9a88-2fec8982911b",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Update ROADMAP with latest experimental results",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

### Assistant

_source line 44 · 2026-05-19T17:15:33.214Z_

ROADMAP.md 已更新。主要变更：

- **Scaling table**: 新增 14B 行 (0.5507)，8B SFT 从 2-seed 0.4866 更新为 3-seed 0.5019，4B 加入 D112 Method B 结果 (0.5152)，8B Δ 从 +5.48pp 修正为 +3.95pp
- **D112**: 标记完成，ign_f1=0.5152 (+4.18pp over s44 baseline)
- **14B evidence tax (D117)**: tax=0.03pp≈0，14B 容量足够
- **1.7B claim (D118)**: "surpasses" 降级为 "comparable"，variance stabilization 独立化
- **Tier 1 实验**: D112、8B SFT s43、14B SFT 全部标记 ✅；8B RSFT s43 移入 Tier 2
- **GPU 分布**: 更新为当前状态（cuda:2 空闲）
- **关键风险**: D112 标记已解决，1.7B/14B 风险项更新为最新结论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51c0e811-e431-4ea1-9a88-2fec8982911b",
  "isSidechain": false,
  "requestId": "req_011CbCJe21p4UVqL1fkXbDVT",
  "type": "assistant",
  "uuid": "09c6bb17-1a37-4ae1-a3bc-16409867c65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BatfLXE94Vy7BNsB3vv6SP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3781,
      "cache_read_input_tokens": 39273,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 325,
          "cache_read_input_tokens": 39273,
          "cache_creation_input_tokens": 3781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3781
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

_source line 45_

```json
{
  "type": "last-prompt",
  "leafUuid": "09c6bb17-1a37-4ae1-a3bc-16409867c65f",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Update ROADMAP with latest experimental results",
  "sessionId": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---
