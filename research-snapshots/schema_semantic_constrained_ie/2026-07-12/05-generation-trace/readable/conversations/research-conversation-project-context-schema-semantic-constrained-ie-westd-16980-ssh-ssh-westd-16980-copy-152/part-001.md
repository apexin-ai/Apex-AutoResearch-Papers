# Research conversation: <project_context> # 项目: schema_semantic_constrained_ie ## 运行环境 - 服务器名: westd-16980 - SSH 连接命令: ssh westd-16980 # 必须用此命令， — Part 1 of 2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-project-context-schema-semantic-constrained-ie-westd-16980-ssh-ssh-westd-16980-copy-152.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/5c/5ca47bf74623621f2541.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-23T05:47:43.619Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T05:47:43.619Z",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "content": "&lt;project_context>\n# 项目: schema_semantic_constrained_ie\n\n## 运行环境\n- 服务器名: westd-16980\n- SSH 连接命令: ssh westd-16980  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/schema_semantic_constrained_ie\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：DocRED INT4 量化对比实验（westd-16980）\n\n### 优先级 1：检查 DocRED LoRA checkpoint 并启动实验\n\n1. SSH 到 westd-16980，确认 DocRED LoRA merged checkpoint 存在：\n```bash\nls -la /root/autodl-tmp/checkpoints/qwen_lora_docred_merged/ 2>/dev/null\nls -la /root/autodl-tmp/checkpoints/llama_lora_docred_merged/ 2>/dev/null\n```\n\n2. 如果两个 checkpoint 都在，**并行启动两个实验**：\n\n**cuda:0 — Qwen DocRED INT4**：\n```bash\nCUDA_VISIBLE_DEVICES=0 python量化脚本\n```\n- 量化 `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged/` → `/root/autodl-tmp/models/Qwen3-8B-DocRED-FT-AWQ-INT4/`\n- 然后跑 DocRED S1 constrained eval（用已有的推理脚本，改模型路径）\n\n**cuda:1 — Llama DocRED INT4**：\n```bash\nCUDA_VISIBLE_DEVICES=1 python量化脚本\n```\n- 量化 `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` → `/root/autodl-tmp/models/Llama-8B-DocRED-FT-AWQ-INT4/`\n- 然后跑 DocRED S1 constrained eval\n\n3. 量化脚本参考（与 SciERC INT4 相同方式）：\n\n先检查 SciERC INT4 量化时使用的脚本：\n```bash\ncat /root/schema_semantic_constrained_ie/scripts/quantize_8b.py 2>/dev/null\ncat /root/schema_semantic_constrained_ie/scripts/quantize_llama_8b.py 2>/dev/null\n```\n\n复用脚本逻辑，修改模型路径和输出路径。校准数据换成 DocRED：\n```bash\nfind /root/schema_semantic_constrained_ie/data/ -name \"*docred*test*\" -o -name \"*docred*dev*\" 2>/dev/null | head -5\n```\n\n4. 推理完成后运行 violation_checker：\n\n先找 DocRED 的 gold 和 ontology 文件：\n```bash\nfind /root/schema_semantic_constrained_ie/ -name \"*docred*gold*\" -o -name \"*docred*test*.jsonl\" -o -name \"*docred*dev*.jsonl\" 2>/dev/null | head -10\nfind /root/schema_semantic_constrained_ie/ -name \"ontology_constraints*docred*\" 2>/dev/null | head -5\n```\n\n**注意**：DocRED 可能是 200-doc 子集（与已有 70B 实验一致）。检查已有实验用的 gold 文件路径。\n\n5. DocRED FP16 baseline 需要从 registry 查询：\n```bash\n# 用 read_registry 查 DocRED FP16 S1 结果\n# 可能的实验名：phase2_docred_full_s1, w5_lora_docred_constrained_eval 等\n```\n\n6. 更新 registry 并报告 FP16 vs INT4 对比表（与 SciERC 格式一致）。\n\n7. 如果 DocRED LoRA checkpoint 不在 westd-16980 上，**不要 SCP**（会影响 westd-21461 正在跑的实验），直接报告无法执行。\n\n### 重要\n- 使用 submit_training_job 提交长时间任务\n- 量化约 30min/模型，推理时间取决于 DocRED 数据量\n- 两个实验并行：cuda:0 Qwen, cuda:1 Llama\n"
}
````

---


### Runtime record

_source line 2 · 2026-05-23T05:47:43.624Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T05:47:43.624Z",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


## Round 1

## Round 1

203 recorded events


### User

_source line 3 · 2026-05-23T05:47:43.679Z_

&lt;project_context>
# 项目: schema_semantic_constrained_ie

## 运行环境
- 服务器名: westd-16980
- SSH 连接命令: ssh westd-16980  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/schema_semantic_constrained_ie


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：DocRED INT4 量化对比实验（westd-16980）

### 优先级 1：检查 DocRED LoRA checkpoint 并启动实验

1. SSH 到 westd-16980，确认 DocRED LoRA merged checkpoint 存在：
```bash
ls -la /root/autodl-tmp/checkpoints/qwen_lora_docred_merged/ 2>/dev/null
ls -la /root/autodl-tmp/checkpoints/llama_lora_docred_merged/ 2>/dev/null
```

2. 如果两个 checkpoint 都在，**并行启动两个实验**：

**cuda:0 — Qwen DocRED INT4**：
```bash
CUDA_VISIBLE_DEVICES=0 python量化脚本
```
- 量化 `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged/` → `/root/autodl-tmp/models/Qwen3-8B-DocRED-FT-AWQ-INT4/`
- 然后跑 DocRED S1 constrained eval（用已有的推理脚本，改模型路径）

**cuda:1 — Llama DocRED INT4**：
```bash
CUDA_VISIBLE_DEVICES=1 python量化脚本
```
- 量化 `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` → `/root/autodl-tmp/models/Llama-8B-DocRED-FT-AWQ-INT4/`
- 然后跑 DocRED S1 constrained eval

3. 量化脚本参考（与 SciERC INT4 相同方式）：

先检查 SciERC INT4 量化时使用的脚本：
```bash
cat /root/schema_semantic_constrained_ie/scripts/quantize_8b.py 2>/dev/null
cat /root/schema_semantic_constrained_ie/scripts/quantize_llama_8b.py 2>/dev/null
```

复用脚本逻辑，修改模型路径和输出路径。校准数据换成 DocRED：
```bash
find /root/schema_semantic_constrained_ie/data/ -name "*docred*test*" -o -name "*docred*dev*" 2>/dev/null | head -5
```

4. 推理完成后运行 violation_checker：

先找 DocRED 的 gold 和 ontology 文件：
```bash
find /root/schema_semantic_constrained_ie/ -name "*docred*gold*" -o -name "*docred*test*.jsonl" -o -name "*docred*dev*.jsonl" 2>/dev/null | head -10
find /root/schema_semantic_constrained_ie/ -name "ontology_constraints*docred*" 2>/dev/null | head -5
```

**注意**：DocRED 可能是 200-doc 子集（与已有 70B 实验一致）。检查已有实验用的 gold 文件路径。

5. DocRED FP16 baseline 需要从 registry 查询：
```bash
# 用 read_registry 查 DocRED FP16 S1 结果
# 可能的实验名：phase2_docred_full_s1, w5_lora_docred_constrained_eval 等
```

6. 更新 registry 并报告 FP16 vs INT4 对比表（与 SciERC 格式一致）。

7. 如果 DocRED LoRA checkpoint 不在 westd-16980 上，**不要 SCP**（会影响 westd-21461 正在跑的实验），直接报告无法执行。

### 重要
- 使用 submit_training_job 提交长时间任务
- 量化约 30min/模型，推理时间取决于 DocRED 数据量
- 两个实验并行：cuda:0 Qwen, cuda:1 Llama


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "c47786d1-3403-4c62-86e3-a31950284553",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-23T05:47:43.678Z_

```json
{
  "parentUuid": "c47786d1-3403-4c62-86e3-a31950284553",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b2ab21ca-df9e-47b1-97d2-99ed38cbc66e",
  "timestamp": "2026-05-23T05:47:43.678Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-23T05:47:43.678Z_

```json
{
  "parentUuid": "b2ab21ca-df9e-47b1-97d2-99ed38cbc66e",
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
  "uuid": "6a863599-5bde-4317-ba81-24205e69c11a",
  "timestamp": "2026-05-23T05:47:43.678Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-23T05:47:43.679Z_

```json
{
  "parentUuid": "6a863599-5bde-4317-ba81-24205e69c11a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "29e9efd1-96b4-4e87-82b5-24521c7c5177",
  "timestamp": "2026-05-23T05:47:43.679Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
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
  "aiTitle": "DocRED INT4 quantization comparison experiments",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Assistant

_source line 8 · 2026-05-23T05:47:45.873Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by checking the server for the DocRED LoRA merged checkpoints and gathering necessary information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29e9efd1-96b4-4e87-82b5-24521c7c5177",
  "isSidechain": false,
  "requestId": "req_011CbJyS8vGb6vmhfvP7cPrj",
  "type": "assistant",
  "uuid": "6381c050-0852-4bac-abd7-b59327b17f32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArAzxE4C9JxFxGus77sypg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12690,
      "cache_read_input_tokens": 11841,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 197,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12690
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

_source line 9 · 2026-05-23T05:47:46.986Z_

先连接服务器检查 checkpoint 和现有脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6381c050-0852-4bac-abd7-b59327b17f32",
  "isSidechain": false,
  "requestId": "req_011CbJyS8vGb6vmhfvP7cPrj",
  "type": "assistant",
  "uuid": "15f5c30c-c58f-41d6-a5c5-c20040fa1cf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArAzxE4C9JxFxGus77sypg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12690,
      "cache_read_input_tokens": 11841,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 197,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12690
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

_source line 10 · 2026-05-23T05:47:48.964Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EiGBCoVn32bCRooU22njVk`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15f5c30c-c58f-41d6-a5c5-c20040fa1cf1",
  "isSidechain": false,
  "requestId": "req_011CbJyS8vGb6vmhfvP7cPrj",
  "type": "assistant",
  "uuid": "add76c54-16e5-4c3e-9c8f-063d2db9c058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArAzxE4C9JxFxGus77sypg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12690,
      "cache_read_input_tokens": 11841,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 197,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12690
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

_source line 11 · 2026-05-23T05:47:48.982Z_

<details><summary>↩ Tool result · `toolu_01EiGBCoVn32bCRooU22njVk`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "parentUuid": "add76c54-16e5-4c3e-9c8f-063d2db9c058",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "6cd65e65-a84e-4514-9cda-bb27fa25e60c",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 26
  },
  "sourceToolAssistantUUID": "add76c54-16e5-4c3e-9c8f-063d2db9c058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 12 · 2026-05-23T05:47:51.533Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by checking the checkpoints, existing scripts, and registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cd65e65-a84e-4514-9cda-bb27fa25e60c",
  "isSidechain": false,
  "requestId": "req_011CbJySXM9fReUxnQispM6r",
  "type": "assistant",
  "uuid": "2bdc59dd-43d8-4756-8c86-8402ea698bbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEcxq6KUp9Q9Egzmtbr92Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 24531,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1888
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

_source line 13 · 2026-05-23T05:47:53.082Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013rHVFfDjkXwrt6mSxbLDh9`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -la /root/autodl-tmp/checkpoints/qwen_lora_docred_merged/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bdc59dd-43d8-4756-8c86-8402ea698bbf",
  "isSidechain": false,
  "requestId": "req_011CbJySXM9fReUxnQispM6r",
  "type": "assistant",
  "uuid": "f5ca72a6-3272-4cc1-80c7-05299f9a2140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEcxq6KUp9Q9Egzmtbr92Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 24531,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1888
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

_source line 14 · 2026-05-23T05:47:53.102Z_

<details><summary>↩ Tool result · `toolu_013rHVFfDjkXwrt6mSxbLDh9`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5ca72a6-3272-4cc1-80c7-05299f9a2140",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "9df3484d-388b-42ff-9e41-8417945d597a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f5ca72a6-3272-4cc1-80c7-05299f9a2140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-23T05:47:54.005Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LmJX9jQddpw4RduRXabXx6`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -la /root/autodl-tmp/checkpoints/llama_lora_docred_merged/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9df3484d-388b-42ff-9e41-8417945d597a",
  "isSidechain": false,
  "requestId": "req_011CbJySXM9fReUxnQispM6r",
  "type": "assistant",
  "uuid": "f98c963c-b8ff-44ea-98dd-7c2e4f595448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEcxq6KUp9Q9Egzmtbr92Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 24531,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1888
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

_source line 16 · 2026-05-23T05:47:54.016Z_

<details><summary>↩ Tool result · `toolu_01LmJX9jQddpw4RduRXabXx6`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f98c963c-b8ff-44ea-98dd-7c2e4f595448",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "f1ce69f7-2eb6-416d-99e5-d71ee61beea6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f98c963c-b8ff-44ea-98dd-7c2e4f595448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-23T05:47:55.479Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PBDiAdii4b8JvY7unfJr5i`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/scripts/quantize_8b.py 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1ce69f7-2eb6-416d-99e5-d71ee61beea6",
  "isSidechain": false,
  "requestId": "req_011CbJySXM9fReUxnQispM6r",
  "type": "assistant",
  "uuid": "648cb5af-542c-4817-b998-a5de704733e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEcxq6KUp9Q9Egzmtbr92Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 24531,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1888
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

_source line 18 · 2026-05-23T05:47:55.488Z_

<details><summary>↩ Tool result · `toolu_01PBDiAdii4b8JvY7unfJr5i`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "648cb5af-542c-4817-b998-a5de704733e5",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "3aa1bcdd-97c4-41aa-8a05-c8e8fe9c1335",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "648cb5af-542c-4817-b998-a5de704733e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-23T05:47:56.428Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01C4sNqsHrV4iMHSyV6PEgQH`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/scripts/quantize_llama_8b.py 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aa1bcdd-97c4-41aa-8a05-c8e8fe9c1335",
  "isSidechain": false,
  "requestId": "req_011CbJySXM9fReUxnQispM6r",
  "type": "assistant",
  "uuid": "defbb036-8316-49b1-96f5-5b6da321a49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEcxq6KUp9Q9Egzmtbr92Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 24531,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1888
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

_source line 20 · 2026-05-23T05:47:56.437Z_

<details><summary>↩ Tool result · `toolu_01C4sNqsHrV4iMHSyV6PEgQH`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "defbb036-8316-49b1-96f5-5b6da321a49f",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "65d31d21-4a1e-4f7d-9ab5-38abce9460bd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "defbb036-8316-49b1-96f5-5b6da321a49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-23T05:47:56.832Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011jfLLZQEWDM88vWR5LkzuS`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "status": "DONE"
  },
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65d31d21-4a1e-4f7d-9ab5-38abce9460bd",
  "isSidechain": false,
  "requestId": "req_011CbJySXM9fReUxnQispM6r",
  "type": "assistant",
  "uuid": "be239056-b46b-4152-9d65-510bd6422853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEcxq6KUp9Q9Egzmtbr92Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 24531,
      "output_tokens": 531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 531,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1888
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

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "be239056-b46b-4152-9d65-510bd6422853",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "DocRED INT4 quantization comparison experiments",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Tool result

_source line 24 · 2026-05-23T05:47:57.500Z_

<details><summary>↩ Tool result · `toolu_011jfLLZQEWDM88vWR5LkzuS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:58:33.950Z\", \"updated_at\": \"2026-05-23T05:35:25.774Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"w5_llama_lora_scierc_constrained_eval\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}, \"conclusion\": \"success\"}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:58:51.930Z\", \"updated_at\": \"2026-05-23T05:35:24.911Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"d066_beam_sweep\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}, \"conclusion\": \"success\"}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T05:14:38.851Z\", \"updated_at\": \"2026-05-23T05:15:20.167Z\", \"hypothesis\": \"GoLLIE-7B achieves low schema violation rates on SciERC zero-shot because it outputs very conservatively (few entities, almost no relations), resulting in trivially low violation rates but extremely poor recall and F1.\", \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T00:41:26.371Z\", \"updated_at\": \"2026-05-23T02:30:50.739Z\", \"hypothesis\": \"Full S1 (grammar+semantic) constraints on 70B ZS DocRED should achieve DR close to semantic_only (1.66%) since grammar adds zero DR contribution in ZS setting. R_F1 should remain ~13 (matching unconstrained 13.25). This completes the ZS DocRED ablation matrix.\", \"parent\": \"eval_70b_zs_docred_200_unconstrained\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:35:19.975Z\", \"updated_at\": \"2026-05-23T01:55:24.472Z\", \"hypothesis\": \"Grammar-only constraints on 70B LoRA DocRED will eliminate RV violations but not reduce DR, mirroring the SciERC ablation pattern where grammar layer provides zero DR contribution at fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}, \"conclusion\": \"negative\"}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:35:17.601Z\", \"updated_at\": \"2026-05-23T01:20:56.659Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA DocRED will reduce DR violations from unconstrained baseline (DR=0.88%) with minimal F1 impact, isolating the semantic layer's contribution in document-level RE at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T22:55:27.332Z\", \"updated_at\": \"2026-05-23T00:38:42.757Z\", \"hypothesis\": \"70B ZS DocRED unconstrained 200-doc baseline to complete the ablation matrix. Expect DR~15% and R-F1~13 consistent with prior 99-doc measurement, providing matched-subset comparison for semantic_only (DR=1.66%) and grammar_only experiments.\", \"parent\": \"70b_docred_unconstrained\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T21:24:11.190Z\", \"updated_at\": \"2026-05-23T00:37:43.935Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS DocRED will show minimal DR reduction (similar to SciERC 70B ZS pattern where grammar_only DR≈unconstrained), confirming that grammar layer's negligible contribution at 70B scale generalizes across datasets.\", \"parent\": \"r16_70b_docred_zs_s1\", \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}, \"conclusion\": \"negative\"}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:35:21.150Z\", \"updated_at\": \"2026-05-22T22:55:11.458Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS DocRED will significantly reduce DR violations from zero-shot baseline, demonstrating the semantic layer's effectiveness on document-level RE without fine-tuning.\", \"parent\": \"70b_docred_unconstrained\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:15:28.977Z\", \"updated_at\": \"2026-05-22T21:21:11.254Z\", \"hypothesis\": \"70B LoRA DocRED with beam search (k=4) + full_s1 on 200-doc subset will achieve DR=0% and CF≈0% while maintaining R-F1 comparable to greedy S1 (43.95), consistent with 8B beam search pattern.\", \"parent\": \"eval_70b_lora_docred_200_s1_constrained\", \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}, \"conclusion\": \"success\"}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:13:55.324Z\", \"updated_at\": \"2026-05-22T20:31:32.878Z\", \"hypothesis\": \"70B LoRA SciERC with grammar-only constrained decoding will reduce DR violations compared to unconstrained (DR=1.5%) but less than full_s1 (DR=0%), isolating grammar layer's independent contribution at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:45:13.928Z\", \"updated_at\": \"2026-05-22T20:30:18.431Z\", \"hypothesis\": \"Independent 70B ZS SciERC unconstrained baseline to verify prior DR and R-F1 numbers from r16_70b_scierc_zs_s1 experiment. Expect DR~6-8% and R-F1~11 consistent with earlier measurements.\", \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:04:58.305Z\", \"updated_at\": \"2026-05-22T20:30:16.494Z\", \"hypothesis\": \"Full S2 constrained decoding on 70B LoRA SciERC achieves DR=0% like S1, with potentially fewer CF violations due to S2's enhanced cross-field consistency checking. R-F1 should be comparable to S1 (44.53-44.81).\", \"parent\": \"eval_70b_lora_scierc_s1_constrained\", \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:04:55.672Z\", \"updated_at\": \"2026-05-22T20:30:13.188Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA SciERC will reduce DR from 1.5% (unconstrained) toward 0%, consistent with the 70B ZS pattern where semantic layer is the primary DR reduction mechanism. Without grammar layer, some RV violations may appear.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T16:48:40.066Z\", \"updated_at\": \"2026-05-22T18:16:23.650Z\", \"hypothesis\": \"Shuffling entity type order in the constraint schema (seed=42) does not significantly change constrained decoding results (R-F1 within ±0.5pp, violation rates identical), confirming that OntoCoDec is order-invariant. This addresses R19-W3 reviewer concern about entity registry ordering sensitivity.\", \"parent\": \"w5_lora_scierc_constrained_eval\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T14:39:36.807Z\", \"updated_at\": \"2026-05-22T18:09:49.840Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS will reduce DR partially (similar to 8B pattern: ~24% reduction) without eliminating RV/ET, isolating semantic layer's independent contribution at 70B scale.\", \"parent\": \"r16_70b_scierc_zs_s1\", \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T14:39:44.901Z\", \"updated_at\": \"2026-05-22T18:09:48.056Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS reduce domain-range violations compared to unconstrained baseline (DR=6.41%) but less effectively than full_s1 (DR=0%), isolating grammar layer's contribution to constraint enforcement.\", \"conclusion\": \"negative\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T14:39:43.218Z\", \"updated_at\": \"2026-05-22T18:04:29.880Z\", \"hypothesis\": \"70B LoRA fine-tuned model with beam search (k=4) and full_s1 constrained decoding on SciERC achieves DR=0% and CF=0%, matching 8B beam search behavior, while maintaining or improving extraction F1.\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T15:48:16.222Z\", \"updated_at\": \"2026-05-22T16:27:25.157Z\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}, \"conclusion\": \"negative\", \"hypothesis\": \"TCR reranking on beam4 outputs will change beam selection for LLaMA-SciERC by penalizing constraint-violating candidates, improving DR violation rate and overall F1 compared to vanilla beam4.\"}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T14:37:32.074Z\", \"updated_at\": \"2026-05-22T15:49:03.706Z\", \"hypothesis\": \"TCR (Type Consistency Reranking) with beam search (k=4) on Qwen3-8B LoRA SciERC will reduce domain/range violations compared to standard beam search by reranking candidates based on type consistency scores, while maintaining or improving Entity/Relation F1.\", \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}, \"parent\": \"d066_beam_sweep\"}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T13:29:07.493Z\", \"updated_at\": \"2026-05-22T13:30:06.224Z\", \"hypothesis\": \"vLLM's guided_json (JSON schema-constrained decoding) produces equivalent violation rates and F1 scores to our XGrammar grammar-only ablation, confirming that guided_json ≈ GCD (grammar-constrained decoding) without semantic constraints.\", \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:47:05.464Z\", \"updated_at\": \"2026-05-22T10:34:22.854Z\", \"hypothesis\": \"70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve DR→0% while maintaining R-F1 comparable to unconstrained, confirming scale-independent constraint composability on DocRED at 70B scale\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T23:44:23.637Z\", \"updated_at\": \"2026-05-22T10:34:14.027Z\", \"hypothesis\": \"Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\", \"notes\": \"全部 8 配置完成 + eval 齐全。beam8 con: E-F1=66.36, R-F1=43.65, DR=0%, CF=0%, avg_time=5.058s。Pareto optimal: k=2 con (E-F1=67.71, R-F1=44.60, DR=0%)。k=8 相比 k=2 F1 下降 ~1.3pp 且推理慢 46%，收益递减明确。可入稿。\", \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}, \"conclusion\": \"success\"}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T06:34:25.909Z\", \"updated_at\": \"2026-05-22T07:36:58.067Z\", \"hypothesis\": \"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\", \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}, \"parent\": \"w5_llama_docred_lora_training\"}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T10:54:02.910Z\", \"updated_at\": \"2026-05-22T07:36:56.885Z\", \"hypothesis\": \"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\", \"parent\": \"w5_llama_docred_lora_training\", \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}, \"conclusion\": \"success\"}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-22T07:36:54.996Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\", \"parent\": \"w5_qwen_docred_lora_training\", \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}, \"conclusion\": \"success\"}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:44:36.469Z\", \"updated_at\": \"2026-05-22T07:36:52.623Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen FT SciERC will show high DR (comparable to or worse than unconstrained), proving grammar layer is prerequisite for vocabulary membership enforcement\", \"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}, \"conclusion\": \"success\"}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:44:39.235Z\", \"updated_at\": \"2026-05-22T07:36:49.828Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama FT SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T04:06:11.811Z\", \"updated_at\": \"2026-05-22T07:09:22.684Z\", \"hypothesis\": \"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale\", \"parent\": \"r16_70b_lora_docred\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}}, \"eval_70b_lora_scierc_s1_constrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:46:31.480Z\", \"updated_at\": \"2026-05-22T06:47:38.556Z\", \"hypothesis\": \"70B LoRA SciERC with Full S1 constrained decoding will achieve DR→0% while maintaining R-F1 comparable to unconstrained (44.73), confirming scale-independent constraint effectiveness at 70B with fine-tuning\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}, \"conclusion\": \"success\"}}, \"count\": 30, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6556}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be239056-b46b-4152-9d65-510bd6422853",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "4815b05a-bfb5-4288-94cf-068d87de1f66",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"sf2_llama_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T04:58:33.950Z\\\", \\\"updated_at\\\": \\\"2026-05-23T05:35:25.774Z\\\", \\\"hypothesis\\\": \\\"AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly affect constraint enforcement on SciERC S1\\\", \\\"parent\\\": \\\"w5_llama_lora_scierc_constrained_eval\\\", \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.94, \\\"R-F1\\\": 43.98, \\\"E-F1\\\": 67.54, \\\"samples\\\": 551, \\\"R-P\\\": 40.47, \\\"R-R\\\": 48.15, \\\"E-P\\\": 65.51, \\\"E-R\\\": 69.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sf2_qwen_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T04:58:51.930Z\\\", \\\"updated_at\\\": \\\"2026-05-23T05:35:24.911Z\\\", \\\"hypothesis\\\": \\\"AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement on SciERC S1\\\", \\\"parent\\\": \\\"d066_beam_sweep\\\", \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 1.1, \\\"R-F1\\\": 41.71, \\\"E-F1\\\": 67.05, \\\"samples\\\": 551, \\\"R-P\\\": 38.52, \\\"R-R\\\": 45.48, \\\"E-P\\\": 64.76, \\\"E-R\\\": 69.52}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sf2_gollie_scierc_violation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T05:14:38.851Z\\\", \\\"updated_at\\\": \\\"2026-05-23T05:15:20.167Z\\\", \\\"hypothesis\\\": \\\"GoLLIE-7B achieves low schema violation rates on SciERC zero-shot because it outputs very conservatively (few entities, almost no relations), resulting in trivially low violation rates but extremely poor recall and F1.\\\", \\\"metrics\\\": {\\\"GoLLIE_ZS\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.83, \\\"E_F1\\\": 9.17, \\\"R_F1\\\": 0, \\\"pred_ents\\\": 241, \\\"pred_rels\\\": 5, \\\"docs_with_output\\\": 54}, \\\"OntoCoDec_Qwen_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.61, \\\"E_F1\\\": 66.43, \\\"R_F1\\\": 43.69}, \\\"OntoCoDec_Llama_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.62, \\\"E_F1\\\": 67.09, \\\"R_F1\\\": 45.47}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_zs_docred_200_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T00:41:26.371Z\\\", \\\"updated_at\\\": \\\"2026-05-23T02:30:50.739Z\\\", \\\"hypothesis\\\": \\\"Full S1 (grammar+semantic) constraints on 70B ZS DocRED should achieve DR close to semantic_only (1.66%) since grammar adds zero DR contribution in ZS setting. R_F1 should remain ~13 (matching unconstrained 13.25). This completes the ZS DocRED ablation matrix.\\\", \\\"parent\\\": \\\"eval_70b_zs_docred_200_unconstrained\\\", \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 5.34, \\\"E-F1\\\": 70.05, \\\"R-F1\\\": 13.25, \\\"PF%\\\": 0, \\\"entities_pred\\\": 3234, \\\"relations_pred\\\": 2637, \\\"triples_checked\\\": 2642}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T20:35:19.975Z\\\", \\\"updated_at\\\": \\\"2026-05-23T01:55:24.472Z\\\", \\\"hypothesis\\\": \\\"Grammar-only constraints on 70B LoRA DocRED will eliminate RV violations but not reduce DR, mirroring the SciERC ablation pattern where grammar layer provides zero DR contribution at fine-tuned scale.\\\", \\\"parent\\\": \\\"eval_70b_lora_docred_200_unconstrained\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 10.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.38, \\\"CF_pct\\\": 0.06, \\\"E_F1\\\": 80.13, \\\"E_P\\\": 85.16, \\\"E_R\\\": 75.66, \\\"R_F1\\\": 43.96, \\\"R_P\\\": 39.78, \\\"R_R\\\": 49.11, \\\"entities_pred\\\": 3362, \\\"relations_pred\\\": 3154}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_70b_lora_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T20:35:17.601Z\\\", \\\"updated_at\\\": \\\"2026-05-23T01:20:56.659Z\\\", \\\"hypothesis\\\": \\\"Semantic-only constraints on 70B LoRA DocRED will reduce DR violations from unconstrained baseline (DR=0.88%) with minimal F1 impact, isolating the semantic layer's contribution in document-level RE at 70B fine-tuned scale.\\\", \\\"parent\\\": \\\"eval_70b_lora_docred_200_unconstrained\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 11, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.51, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.21, \\\"E_F1\\\": 80.06, \\\"E_P\\\": 85.21, \\\"E_R\\\": 75.5, \\\"R_F1\\\": 43.61, \\\"R_P\\\": 39.44, \\\"R_R\\\": 48.75, \\\"entities_pred\\\": 3351, \\\"relations_pred\\\": 3148}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_zs_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T22:55:27.332Z\\\", \\\"updated_at\\\": \\\"2026-05-23T00:38:42.757Z\\\", \\\"hypothesis\\\": \\\"70B ZS DocRED unconstrained 200-doc baseline to complete the ablation matrix. Expect DR~15% and R-F1~13 consistent with prior 99-doc measurement, providing matched-subset comparison for semantic_only (DR=1.66%) and grammar_only experiments.\\\", \\\"parent\\\": \\\"70b_docred_unconstrained\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities_pred\\\": 3242, \\\"relations_pred\\\": 2637, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 7.88, \\\"DR_pct\\\": 13.45, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 8, \\\"E_F1\\\": 70.14, \\\"E_P\\\": 75.85, \\\"E_R\\\": 65.23, \\\"R_F1\\\": 13.25, \\\"R_P\\\": 12.97, \\\"R_R\\\": 13.54}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_zs_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T21:24:11.190Z\\\", \\\"updated_at\\\": \\\"2026-05-23T00:37:43.935Z\\\", \\\"hypothesis\\\": \\\"Grammar-only constraints on 70B ZS DocRED will show minimal DR reduction (similar to SciERC 70B ZS pattern where grammar_only DR≈unconstrained), confirming that grammar layer's negligible contribution at 70B scale generalizes across datasets.\\\", \\\"parent\\\": \\\"r16_70b_docred_zs_s1\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 1, \\\"entities_pred\\\": 3221, \\\"relations_pred\\\": 2609, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 17.03, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"E_F1\\\": 70.12, \\\"E_P\\\": 75.88, \\\"E_R\\\": 65.17, \\\"R_F1\\\": 13.23, \\\"R_P\\\": 12.99, \\\"R_R\\\": 13.47}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_70b_zs_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T20:35:21.150Z\\\", \\\"updated_at\\\": \\\"2026-05-22T22:55:11.458Z\\\", \\\"hypothesis\\\": \\\"Semantic-only constraints on 70B ZS DocRED will significantly reduce DR violations from zero-shot baseline, demonstrating the semantic layer's effectiveness on document-level RE without fine-tuning.\\\", \\\"parent\\\": \\\"70b_docred_unconstrained\\\", \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities\\\": 3240, \\\"relations\\\": 2596, \\\"ET_pct\\\": 0.12, \\\"RV_pct\\\": 8.24, \\\"DR_pct\\\": 1.66, \\\"CF_count\\\": 132, \\\"CF_pct\\\": 4.07, \\\"E_F1\\\": 70.1, \\\"E_P\\\": 75.87, \\\"E_R\\\": 65.15, \\\"R_F1\\\": 13.05, \\\"R_P\\\": 12.88, \\\"R_R\\\": 13.23, \\\"fuzzy_matches\\\": 8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T17:15:28.977Z\\\", \\\"updated_at\\\": \\\"2026-05-22T21:21:11.254Z\\\", \\\"hypothesis\\\": \\\"70B LoRA DocRED with beam search (k=4) + full_s1 on 200-doc subset will achieve DR=0% and CF≈0% while maintaining R-F1 comparable to greedy S1 (43.95), consistent with 8B beam search pattern.\\\", \\\"parent\\\": \\\"eval_70b_lora_docred_200_s1_constrained\\\", \\\"metrics\\\": {\\\"E-F1\\\": 85.57, \\\"E-P\\\": 85.45, \\\"E-R\\\": 85.68, \\\"R-F1\\\": 48.14, \\\"R-P\\\": 44.24, \\\"R-R\\\": 52.79, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"parse_fail\\\": \\\"1/200 (0.5%)\\\", \\\"entities_pred\\\": 3790, \\\"relations_pred\\\": 3030}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T17:13:55.324Z\\\", \\\"updated_at\\\": \\\"2026-05-22T20:31:32.878Z\\\", \\\"hypothesis\\\": \\\"70B LoRA SciERC with grammar-only constrained decoding will reduce DR violations compared to unconstrained (DR=1.5%) but less than full_s1 (DR=0%), isolating grammar layer's independent contribution at 70B fine-tuned scale.\\\", \\\"parent\\\": \\\"eval_70b_lora_scierc_unconstrained\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"json_failure_rate\\\": 0, \\\"entities\\\": 1805, \\\"relations\\\": 1133, \\\"entity_type_violations\\\": 0, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocab_violations\\\": 0, \\\"relation_vocab_violation_rate\\\": 0, \\\"domain_range_violations\\\": 17, \\\"domain_range_violation_rate\\\": 0.015, \\\"cross_field_consistency_violations\\\": 0, \\\"fuzzy_relation_matches\\\": 0, \\\"entity_P\\\": 0.6272, \\\"entity_R\\\": 0.6707, \\\"entity_F1\\\": 0.6482, \\\"relation_P\\\": 0.4152, \\\"relation_R\\\": 0.4825, \\\"relation_F1\\\": 0.4463}}, \\\"eval_70b_zs_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T18:45:13.928Z\\\", \\\"updated_at\\\": \\\"2026-05-22T20:30:18.431Z\\\", \\\"hypothesis\\\": \\\"Independent 70B ZS SciERC unconstrained baseline to verify prior DR and R-F1 numbers from r16_70b_scierc_zs_s1 experiment. Expect DR~6-8% and R-F1~11 consistent with earlier measurements.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 2353, \\\"relations\\\": 1483, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.6, \\\"DR_pct\\\": 6.4, \\\"CF_count\\\": 0, \\\"E_F1\\\": 35.22, \\\"E_P\\\": 30.13, \\\"E_R\\\": 42.38, \\\"R_F1\\\": 11.23, \\\"R_P\\\": 9.31, \\\"R_R\\\": 14.17, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_full_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T18:04:58.305Z\\\", \\\"updated_at\\\": \\\"2026-05-22T20:30:16.494Z\\\", \\\"hypothesis\\\": \\\"Full S2 constrained decoding on 70B LoRA SciERC achieves DR=0% like S1, with potentially fewer CF violations due to S2's enhanced cross-field consistency checking. R-F1 should be comparable to S1 (44.53-44.81).\\\", \\\"parent\\\": \\\"eval_70b_lora_scierc_s1_constrained\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1531, \\\"relations\\\": 1027, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 18, \\\"E_F1\\\": 62.35, \\\"E_P\\\": 65.44, \\\"E_R\\\": 59.53, \\\"R_F1\\\": 36.28, \\\"R_P\\\": 35.35, \\\"R_R\\\": 37.27, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T18:04:55.672Z\\\", \\\"updated_at\\\": \\\"2026-05-22T20:30:13.188Z\\\", \\\"hypothesis\\\": \\\"Semantic-only constraints on 70B LoRA SciERC will reduce DR from 1.5% (unconstrained) toward 0%, consistent with the 70B ZS pattern where semantic layer is the primary DR reduction mechanism. Without grammar layer, some RV violations may appear.\\\", \\\"parent\\\": \\\"eval_70b_lora_scierc_unconstrained\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1806, \\\"relations\\\": 1133, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.6, \\\"CF_count\\\": 9, \\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"parse_fail_pct\\\": 0}}, \\\"entity_order_ablation_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T16:48:40.066Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:16:23.650Z\\\", \\\"hypothesis\\\": \\\"Shuffling entity type order in the constraint schema (seed=42) does not significantly change constrained decoding results (R-F1 within ±0.5pp, violation rates identical), confirming that OntoCoDec is order-invariant. This addresses R19-W3 reviewer concern about entity registry ordering sensitivity.\\\", \\\"parent\\\": \\\"w5_lora_scierc_constrained_eval\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 67.05, \\\"E_P\\\": 65.23, \\\"E_R\\\": 68.98, \\\"R_F1\\\": 43.77, \\\"R_P\\\": 40.78, \\\"R_R\\\": 47.23, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 21, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1784, \\\"relations\\\": 1128, \\\"corrected_original_R_F1\\\": 43.77, \\\"corrected_original_E_F1\\\": 67.05, \\\"corrected_original_DR_pct\\\": 0, \\\"corrected_original_CF_count\\\": 21, \\\"corrected_delta_R_F1\\\": 0, \\\"corrected_delta_E_F1\\\": 0, \\\"raw_output_identical\\\": true, \\\"parsed_output_identical\\\": true, \\\"note\\\": \\\"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\\\"}}, \\\"eval_70b_zs_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T14:39:36.807Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:09:49.840Z\\\", \\\"hypothesis\\\": \\\"Semantic-only constraints on 70B ZS will reduce DR partially (similar to 8B pattern: ~24% reduction) without eliminating RV/ET, isolating semantic layer's independent contribution at 70B scale.\\\", \\\"parent\\\": \\\"r16_70b_scierc_zs_s1\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.37, \\\"DR_pct\\\": 1.01, \\\"RV_pct\\\": 0.6, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 76, \\\"samples\\\": 551}}, \\\"eval_70b_zs_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T14:39:44.901Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:09:48.056Z\\\", \\\"hypothesis\\\": \\\"Grammar-only constraints on 70B ZS reduce domain-range violations compared to unconstrained baseline (DR=6.41%) but less effectively than full_s1 (DR=0%), isolating grammar layer's contribution to constraint enforcement.\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.23, \\\"DR_pct\\\": 6.33, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 0, \\\"samples\\\": 551}}, \\\"eval_70b_lora_scierc_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T14:39:43.218Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:04:29.880Z\\\", \\\"hypothesis\\\": \\\"70B LoRA fine-tuned model with beam search (k=4) and full_s1 constrained decoding on SciERC achieves DR=0% and CF=0%, matching 8B beam search behavior, while maintaining or improving extraction F1.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 64.89, \\\"E_P\\\": 62.29, \\\"E_R\\\": 67.72, \\\"R_F1\\\": 44.81, \\\"R_P\\\": 39.45, \\\"R_R\\\": 51.85, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 1, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1839, \\\"relations\\\": 1283}}, \\\"tcr_beam4_llama_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T15:48:16.222Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:27:25.157Z\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1803, \\\"relations\\\": 1194, \\\"entity_type_violations\\\": \\\"0/1803 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1194 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"13/1194 (1.1%)\\\", \\\"cross_field_consistency\\\": 0, \\\"DR_pct\\\": 1.09, \\\"E_F1\\\": 68.02, \\\"E_P\\\": 65.88, \\\"E_R\\\": 70.29, \\\"R_F1\\\": 46.05, \\\"R_P\\\": 41.83, \\\"R_R\\\": 51.23, \\\"tcr_changed_selection\\\": \\\"0/551 (0.0%)\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"TCR reranking on beam4 outputs will change beam selection for LLaMA-SciERC by penalizing constraint-violating candidates, improving DR violation rate and overall F1 compared to vanilla beam4.\\\"}, \\\"tcr_beam4_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T14:37:32.074Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:49:03.706Z\\\", \\\"hypothesis\\\": \\\"TCR (Type Consistency Reranking) with beam search (k=4) on Qwen3-8B LoRA SciERC will reduce domain/range violations compared to standard beam search by reranking candidates based on type consistency scores, while maintaining or improving Entity/Relation F1.\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1802, \\\"relations\\\": 1250, \\\"entity_type_violations\\\": \\\"0/1802 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1250 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"23/1250 (1.8%)\\\", \\\"cross_field_consistency_violations\\\": 1, \\\"DR_pct\\\": 1.84, \\\"E_P\\\": 65.05, \\\"E_R\\\": 69.64, \\\"E_F1\\\": 67.26, \\\"R_P\\\": 39.36, \\\"R_R\\\": 50.51, \\\"R_F1\\\": 44.24, \\\"TCR_changed_selection\\\": \\\"0/551 (0.0%)\\\", \\\"all_candidates_TCR_1.0\\\": true}, \\\"parent\\\": \\\"d066_beam_sweep\\\"}, \\\"vllm_guided_json_scierc_zs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T13:29:07.493Z\\\", \\\"updated_at\\\": \\\"2026-05-22T13:30:06.224Z\\\", \\\"hypothesis\\\": \\\"vLLM's guided_json (JSON schema-constrained decoding) produces equivalent violation rates and F1 scores to our XGrammar grammar-only ablation, confirming that guided_json ≈ GCD (grammar-constrained decoding) without semantic constraints.\\\", \\\"metrics\\\": {\\\"DR%\\\": 15.26, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.04, \\\"R-F1\\\": 8.75, \\\"E-F1\\\": 30.91, \\\"parse_fail%\\\": 0, \\\"total_samples\\\": 551, \\\"total_entities\\\": 2485, \\\"total_relations\\\": 1724, \\\"inference_time_s\\\": 108.5}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T05:47:05.464Z\\\", \\\"updated_at\\\": \\\"2026-05-22T10:34:22.854Z\\\", \\\"hypothesis\\\": \\\"70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve DR→0% while maintaining R-F1 comparable to unconstrained, confirming scale-independent constraint composability on DocRED at 70B scale\\\", \\\"parent\\\": \\\"eval_70b_lora_docred_200_unconstrained\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 79.38, \\\"E_P\\\": 85.24, \\\"E_R\\\": 74.28, \\\"R_F1\\\": 43.95, \\\"R_P\\\": 40.48, \\\"R_R\\\": 48.08, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.18, \\\"parse_fail_pct\\\": 12.5, \\\"samples\\\": 200}}, \\\"d066_beam_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T23:44:23.637Z\\\", \\\"updated_at\\\": \\\"2026-05-22T10:34:14.027Z\\\", \\\"hypothesis\\\": \\\"Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\\\", \\\"notes\\\": \\\"全部 8 配置完成 + eval 齐全。beam8 con: E-F1=66.36, R-F1=43.65, DR=0%, CF=0%, avg_time=5.058s。Pareto optimal: k=2 con (E-F1=67.71, R-F1=44.60, DR=0%)。k=8 相比 k=2 F1 下降 ~1.3pp 且推理慢 46%，收益递减明确。可入稿。\\\", \\\"metrics\\\": {\\\"scierc_qwen3_8b\\\": {\\\"k1_unc\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 2.11, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.494}, \\\"k1_con\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.5, \\\"avg_time\\\": 2.932}, \\\"k2_unc\\\": {\\\"E_F1\\\": 67.79, \\\"R_F1\\\": 44.75, \\\"DR_pct\\\": 1.54, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.954}, \\\"k2_con\\\": {\\\"E_F1\\\": 67.71, \\\"R_F1\\\": 44.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.11, \\\"avg_time\\\": 3.463}, \\\"k4_unc\\\": {\\\"E_F1\\\": 67.49, \\\"R_F1\\\": 43.72, \\\"DR_pct\\\": 1.89, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 3.485}, \\\"k4_con\\\": {\\\"E_F1\\\": 67.22, \\\"R_F1\\\": 43.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.069}, \\\"k8_unc\\\": {\\\"E_F1\\\": 66.4, \\\"R_F1\\\": 43.17, \\\"DR_pct\\\": 1.77, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.194}, \\\"k8_con\\\": {\\\"E_F1\\\": 66.36, \\\"R_F1\\\": 43.65, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 5.058}}, \\\"pareto_optimal\\\": \\\"k=2 con\\\", \\\"best_E_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 67.79}, \\\"best_R_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 44.75}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"w8_llama_docred_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T06:34:25.909Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:58.067Z\\\", \\\"hypothesis\\\": \\\"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"R_F1\\\": 43.72, \\\"R_P\\\": 38.57, \\\"R_R\\\": 50.44, \\\"parse_fail_pct\\\": 2.3, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\\\"}, \\\"parent\\\": \\\"w5_llama_docred_lora_training\\\"}, \\\"w8_llama_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T10:54:02.910Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:56.885Z\\\", \\\"hypothesis\\\": \\\"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\\\", \\\"parent\\\": \\\"w5_llama_docred_lora_training\\\", \\\"metrics\\\": {\\\"R_F1\\\": 43.85, \\\"R_P\\\": 38.85, \\\"R_R\\\": 50.31, \\\"parse_fail_pct\\\": 2.4, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"w8_qwen_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T10:08:59.297Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:54.996Z\\\", \\\"hypothesis\\\": \\\"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\\\", \\\"parent\\\": \\\"w5_qwen_docred_lora_training\\\", \\\"metrics\\\": {\\\"R_F1\\\": 40.85, \\\"R_P\\\": 36.33, \\\"R_R\\\": 46.65, \\\"parse_fail_pct\\\": 7.52, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_qwen_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T03:44:36.469Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:52.623Z\\\", \\\"hypothesis\\\": \\\"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen FT SciERC will show high DR (comparable to or worse than unconstrained), proving grammar layer is prerequisite for vocabulary membership enforcement\\\", \\\"metrics\\\": {\\\"E_F1\\\": 64.4, \\\"E_P\\\": 66.8, \\\"E_R\\\": 62.16, \\\"R_F1\\\": 41.16, \\\"R_P\\\": 38.24, \\\"R_R\\\": 44.56, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 95.5, \\\"CF_pct\\\": 0.09, \\\"parse_fail_pct\\\": 9.1, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_llama_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-21T03:44:39.235Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:49.828Z\\\", \\\"hypothesis\\\": \\\"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama FT SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\\\", \\\"metrics\\\": {\\\"E_F1\\\": 36.66, \\\"E_P\\\": 67.47, \\\"E_R\\\": 25.16, \\\"R_F1\\\": 19.95, \\\"R_P\\\": 41.42, \\\"R_R\\\": 13.14, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 15.2, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 50.8, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T04:06:11.811Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:09:22.684Z\\\", \\\"hypothesis\\\": \\\"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale\\\", \\\"parent\\\": \\\"r16_70b_lora_docred\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 80.34, \\\"E_P\\\": 85.13, \\\"E_R\\\": 76.05, \\\"R_F1\\\": 43.8, \\\"R_P\\\": 39.6, \\\"R_R\\\": 48.99, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.57, \\\"DR_pct\\\": 0.22, \\\"CF_pct\\\": 0.06, \\\"parse_fail_pct\\\": 10, \\\"samples\\\": 200, \\\"relations\\\": 3159, \\\"RV_count\\\": 18, \\\"DR_count\\\": 7, \\\"CF_count\\\": 2}}, \\\"eval_70b_lora_scierc_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-22T05:46:31.480Z\\\", \\\"updated_at\\\": \\\"2026-05-22T06:47:38.556Z\\\", \\\"hypothesis\\\": \\\"70B LoRA SciERC with Full S1 constrained decoding will achieve DR→0% while maintaining R-F1 comparable to unconstrained (44.73), confirming scale-independent constraint effectiveness at 70B with fine-tuning\\\", \\\"parent\\\": \\\"eval_70b_lora_scierc_unconstrained\\\", \\\"metrics\\\": {\\\"entity_f1\\\": 0.6476, \\\"entity_precision\\\": 0.6266, \\\"entity_recall\\\": 0.6701, \\\"relation_f1\\\": 0.4453, \\\"relation_precision\\\": 0.4149, \\\"relation_recall\\\": 0.4805, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 15, \\\"parse_fail_pct\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"num_samples\\\": 551, \\\"num_entities\\\": 1805, \\\"num_relations\\\": 1129}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 30, \\\"total\\\": 158, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.6556}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:58:33.950Z\", \"updated_at\": \"2026-05-23T05:35:25.774Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"w5_llama_lora_scierc_constrained_eval\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}, \"conclusion\": \"success\"}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T04:58:51.930Z\", \"updated_at\": \"2026-05-23T05:35:24.911Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"d066_beam_sweep\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}, \"conclusion\": \"success\"}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T05:14:38.851Z\", \"updated_at\": \"2026-05-23T05:15:20.167Z\", \"hypothesis\": \"GoLLIE-7B achieves low schema violation rates on SciERC zero-shot because it outputs very conservatively (few entities, almost no relations), resulting in trivially low violation rates but extremely poor recall and F1.\", \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T00:41:26.371Z\", \"updated_at\": \"2026-05-23T02:30:50.739Z\", \"hypothesis\": \"Full S1 (grammar+semantic) constraints on 70B ZS DocRED should achieve DR close to semantic_only (1.66%) since grammar adds zero DR contribution in ZS setting. R_F1 should remain ~13 (matching unconstrained 13.25). This completes the ZS DocRED ablation matrix.\", \"parent\": \"eval_70b_zs_docred_200_unconstrained\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:35:19.975Z\", \"updated_at\": \"2026-05-23T01:55:24.472Z\", \"hypothesis\": \"Grammar-only constraints on 70B LoRA DocRED will eliminate RV violations but not reduce DR, mirroring the SciERC ablation pattern where grammar layer provides zero DR contribution at fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}, \"conclusion\": \"negative\"}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:35:17.601Z\", \"updated_at\": \"2026-05-23T01:20:56.659Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA DocRED will reduce DR violations from unconstrained baseline (DR=0.88%) with minimal F1 impact, isolating the semantic layer's contribution in document-level RE at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T22:55:27.332Z\", \"updated_at\": \"2026-05-23T00:38:42.757Z\", \"hypothesis\": \"70B ZS DocRED unconstrained 200-doc baseline to complete the ablation matrix. Expect DR~15% and R-F1~13 consistent with prior 99-doc measurement, providing matched-subset comparison for semantic_only (DR=1.66%) and grammar_only experiments.\", \"parent\": \"70b_docred_unconstrained\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T21:24:11.190Z\", \"updated_at\": \"2026-05-23T00:37:43.935Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS DocRED will show minimal DR reduction (similar to SciERC 70B ZS pattern where grammar_only DR≈unconstrained), confirming that grammar layer's negligible contribution at 70B scale generalizes across datasets.\", \"parent\": \"r16_70b_docred_zs_s1\", \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}, \"conclusion\": \"negative\"}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T20:35:21.150Z\", \"updated_at\": \"2026-05-22T22:55:11.458Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS DocRED will significantly reduce DR violations from zero-shot baseline, demonstrating the semantic layer's effectiveness on document-level RE without fine-tuning.\", \"parent\": \"70b_docred_unconstrained\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:15:28.977Z\", \"updated_at\": \"2026-05-22T21:21:11.254Z\", \"hypothesis\": \"70B LoRA DocRED with beam search (k=4) + full_s1 on 200-doc subset will achieve DR=0% and CF≈0% while maintaining R-F1 comparable to greedy S1 (43.95), consistent with 8B beam search pattern.\", \"parent\": \"eval_70b_lora_docred_200_s1_constrained\", \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}, \"conclusion\": \"success\"}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:13:55.324Z\", \"updated_at\": \"2026-05-22T20:31:32.878Z\", \"hypothesis\": \"70B LoRA SciERC with grammar-only constrained decoding will reduce DR violations compared to unconstrained (DR=1.5%) but less than full_s1 (DR=0%), isolating grammar layer's independent contribution at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:45:13.928Z\", \"updated_at\": \"2026-05-22T20:30:18.431Z\", \"hypothesis\": \"Independent 70B ZS SciERC unconstrained baseline to verify prior DR and R-F1 numbers from r16_70b_scierc_zs_s1 experiment. Expect DR~6-8% and R-F1~11 consistent with earlier measurements.\", \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:04:58.305Z\", \"updated_at\": \"2026-05-22T20:30:16.494Z\", \"hypothesis\": \"Full S2 constrained decoding on 70B LoRA SciERC achieves DR=0% like S1, with potentially fewer CF violations due to S2's enhanced cross-field consistency checking. R-F1 should be comparable to S1 (44.53-44.81).\", \"parent\": \"eval_70b_lora_scierc_s1_constrained\", \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:04:55.672Z\", \"updated_at\": \"2026-05-22T20:30:13.188Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA SciERC will reduce DR from 1.5% (unconstrained) toward 0%, consistent with the 70B ZS pattern where semantic layer is the primary DR reduction mechanism. Without grammar layer, some RV violations may appear.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T16:48:40.066Z\", \"updated_at\": \"2026-05-22T18:16:23.650Z\", \"hypothesis\": \"Shuffling entity type order in the constraint schema (seed=42) does not significantly change constrained decoding results (R-F1 within ±0.5pp, violation rates identical), confirming that OntoCoDec is order-invariant. This addresses R19-W3 reviewer concern about entity registry ordering sensitivity.\", \"parent\": \"w5_lora_scierc_constrained_eval\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T14:39:36.807Z\", \"updated_at\": \"2026-05-22T18:09:49.840Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS will reduce DR partially (similar to 8B pattern: ~24% reduction) without eliminating RV/ET, isolating semantic layer's independent contribution at 70B scale.\", \"parent\": \"r16_70b_scierc_zs_s1\", \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T14:39:44.901Z\", \"updated_at\": \"2026-05-22T18:09:48.056Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS reduce domain-range violations compared to unconstrained baseline (DR=6.41%) but less effectively than full_s1 (DR=0%), isolating grammar layer's contribution to constraint enforcement.\", \"conclusion\": \"negative\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T14:39:43.218Z\", \"updated_at\": \"2026-05-22T18:04:29.880Z\", \"hypothesis\": \"70B LoRA fine-tuned model with beam search (k=4) and full_s1 constrained decoding on SciERC achieves DR=0% and CF=0%, matching 8B beam search behavior, while maintaining or improving extraction F1.\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T15:48:16.222Z\", \"updated_at\": \"2026-05-22T16:27:25.157Z\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}, \"conclusion\": \"negative\", \"hypothesis\": \"TCR reranking on beam4 outputs will change beam selection for LLaMA-SciERC by penalizing constraint-violating candidates, improving DR violation rate and overall F1 compared to vanilla beam4.\"}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T14:37:32.074Z\", \"updated_at\": \"2026-05-22T15:49:03.706Z\", \"hypothesis\": \"TCR (Type Consistency Reranking) with beam search (k=4) on Qwen3-8B LoRA SciERC will reduce domain/range violations compared to standard beam search by reranking candidates based on type consistency scores, while maintaining or improving Entity/Relation F1.\", \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}, \"parent\": \"d066_beam_sweep\"}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T13:29:07.493Z\", \"updated_at\": \"2026-05-22T13:30:06.224Z\", \"hypothesis\": \"vLLM's guided_json (JSON schema-constrained decoding) produces equivalent violation rates and F1 scores to our XGrammar grammar-only ablation, confirming that guided_json ≈ GCD (grammar-constrained decoding) without semantic constraints.\", \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:47:05.464Z\", \"updated_at\": \"2026-05-22T10:34:22.854Z\", \"hypothesis\": \"70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve DR→0% while maintaining R-F1 comparable to unconstrained, confirming scale-independent constraint composability on DocRED at 70B scale\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T23:44:23.637Z\", \"updated_at\": \"2026-05-22T10:34:14.027Z\", \"hypothesis\": \"Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\", \"notes\": \"全部 8 配置完成 + eval 齐全。beam8 con: E-F1=66.36, R-F1=43.65, DR=0%, CF=0%, avg_time=5.058s。Pareto optimal: k=2 con (E-F1=67.71, R-F1=44.60, DR=0%)。k=8 相比 k=2 F1 下降 ~1.3pp 且推理慢 46%，收益递减明确。可入稿。\", \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}, \"conclusion\": \"success\"}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T06:34:25.909Z\", \"updated_at\": \"2026-05-22T07:36:58.067Z\", \"hypothesis\": \"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\", \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}, \"parent\": \"w5_llama_docred_lora_training\"}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T10:54:02.910Z\", \"updated_at\": \"2026-05-22T07:36:56.885Z\", \"hypothesis\": \"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\", \"parent\": \"w5_llama_docred_lora_training\", \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}, \"conclusion\": \"success\"}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-22T07:36:54.996Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\", \"parent\": \"w5_qwen_docred_lora_training\", \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}, \"conclusion\": \"success\"}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:44:36.469Z\", \"updated_at\": \"2026-05-22T07:36:52.623Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen FT SciERC will show high DR (comparable to or worse than unconstrained), proving grammar layer is prerequisite for vocabulary membership enforcement\", \"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}, \"conclusion\": \"success\"}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:44:39.235Z\", \"updated_at\": \"2026-05-22T07:36:49.828Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama FT SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T04:06:11.811Z\", \"updated_at\": \"2026-05-22T07:09:22.684Z\", \"hypothesis\": \"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale\", \"parent\": \"r16_70b_lora_docred\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}}, \"eval_70b_lora_scierc_s1_constrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T05:46:31.480Z\", \"updated_at\": \"2026-05-22T06:47:38.556Z\", \"hypothesis\": \"70B LoRA SciERC with Full S1 constrained decoding will achieve DR→0% while maintaining R-F1 comparable to unconstrained (44.73), confirming scale-independent constraint effectiveness at 70B with fine-tuning\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}, \"conclusion\": \"success\"}}, \"count\": 30, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6556}}"
    }
  },
  "sourceToolAssistantUUID": "be239056-b46b-4152-9d65-510bd6422853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "leafUuid": "4815b05a-bfb5-4288-94cf-068d87de1f66",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "DocRED INT4 quantization comparison experiments",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Assistant

_source line 27 · 2026-05-23T05:48:02.586Z_

<details><summary>Logged reasoning block</summary>

```text
The `2>/dev/null` redirect causes the ssh_read_only to fail because of the `>` metacharacter. Let me retry without the redirect. Also, I need to check the registry for DocRED FP16 baseline results. Let me also look for the quantization scripts and DocRED data.

Let me retry the SSH commands without redirects, and also search for more relevant registry entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4815b05a-bfb5-4288-94cf-068d87de1f66",
  "isSidechain": false,
  "requestId": "req_011CbJyT9hvsChETFh3fpQuF",
  "type": "assistant",
  "uuid": "230bfa7f-8073-43ee-9d40-50a40b3e6495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFxRTQ58Tndjj2PQ33pkNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11620,
      "cache_read_input_tokens": 26419,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 26419,
          "cache_creation_input_tokens": 11620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11620
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

_source line 28 · 2026-05-23T05:48:04.070Z_

重试 SSH 命令（不用重定向）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "230bfa7f-8073-43ee-9d40-50a40b3e6495",
  "isSidechain": false,
  "requestId": "req_011CbJyT9hvsChETFh3fpQuF",
  "type": "assistant",
  "uuid": "dd30bd12-82ce-4f51-ae79-5dcda0f767ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFxRTQ58Tndjj2PQ33pkNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11620,
      "cache_read_input_tokens": 26419,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 26419,
          "cache_creation_input_tokens": 11620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11620
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

_source line 29 · 2026-05-23T05:48:05.729Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EqSvL6ECg6V6zn6Lhnxbiq`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -la /root/autodl-tmp/checkpoints/qwen_lora_docred_merged/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd30bd12-82ce-4f51-ae79-5dcda0f767ee",
  "isSidechain": false,
  "requestId": "req_011CbJyT9hvsChETFh3fpQuF",
  "type": "assistant",
  "uuid": "8f6597c3-0081-4436-bea4-486cb7186041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFxRTQ58Tndjj2PQ33pkNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11620,
      "cache_read_input_tokens": 26419,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 26419,
          "cache_creation_input_tokens": 11620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11620
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

_source line 30 · 2026-05-23T05:48:05.968Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016C6t9qbfNPLme2aB5ptwoB`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -la /root/autodl-tmp/checkpoints/llama_lora_docred_merged/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f6597c3-0081-4436-bea4-486cb7186041",
  "isSidechain": false,
  "requestId": "req_011CbJyT9hvsChETFh3fpQuF",
  "type": "assistant",
  "uuid": "172d0300-edcd-4fda-a058-f5374c1c7ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFxRTQ58Tndjj2PQ33pkNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11620,
      "cache_read_input_tokens": 26419,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 26419,
          "cache_creation_input_tokens": 11620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11620
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

_source line 31 · 2026-05-23T05:48:06.958Z_

<details><summary>↩ Tool result · `toolu_01EqSvL6ECg6V6zn6Lhnxbiq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16013164\\ndrwxr-xr-x  2 root root       4096 May 16 04:01 .\\ndrwxr-xr-x 11 root root       4096 May 21 20:01 ..\\n-rw-r--r--  1 root root        707 May 16 04:01 added_tokens.json\\n-rw-r--r--  1 root root       4168 May 16 04:01 chat_template.jinja\\n-rw-r--r--  1 root root       1538 May 16 04:01 config.json\\n-rw-r--r--  1 root root        214 May 16 04:01 generation_config.json\\n-rw-r--r--  1 root root    1671853 May 16 04:01 merges.txt\\n-rw-r--r--  1 root root 4902257696 May 16 04:01 model-00001-of-00004.safetensors\\n-rw-r--r--  1 root root 4915960368 May 16 04:01 model-00002-of-00004.safetensors\\n-rw-r--r--  1 root root 4983068496 May 16 04:01 model-00003-of-00004.safetensors\\n-rw-r--r--  1 root root 1580230264 May 16 04:01 model-00004-of-00004.safetensors\\n-rw-r--r--  1 root root      32914 May 16 04:01 model.safetensors.index.json\\n-rw-r--r--  1 root root        613 May 16 04:01 special_tokens_map.json\\n-rw-r--r--  1 root root   11422654 May 16 04:01 tokenizer.json\\n-rw-r--r--  1 root root       5404 May 16 04:01 tokenizer_config.json\\n-rw-r--r--  1 root root    2776833 May 16 04:01 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f6597c3-0081-4436-bea4-486cb7186041",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "6964d3e3-b98e-47f9-95e3-cb5ff4db228a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 16013164\\\\ndrwxr-xr-x  2 root root       4096 May 16 04:01 .\\\\ndrwxr-xr-x 11 root root       4096 May 21 20:01 ..\\\\n-rw-r--r--  1 root root        707 May 16 04:01 added_tokens.json\\\\n-rw-r--r--  1 root root       4168 May 16 04:01 chat_template.jinja\\\\n-rw-r--r--  1 root root       1538 May 16 04:01 config.json\\\\n-rw-r--r--  1 root root        214 May 16 04:01 generation_config.json\\\\n-rw-r--r--  1 root root    1671853 May 16 04:01 merges.txt\\\\n-rw-r--r--  1 root root 4902257696 May 16 04:01 model-00001-of-00004.safetensors\\\\n-rw-r--r--  1 root root 4915960368 May 16 04:01 model-00002-of-00004.safetensors\\\\n-rw-r--r--  1 root root 4983068496 May 16 04:01 model-00003-of-00004.safetensors\\\\n-rw-r--r--  1 root root 1580230264 May 16 04:01 model-00004-of-00004.safetensors\\\\n-rw-r--r--  1 root root      32914 May 16 04:01 model.safetensors.index.json\\\\n-rw-r--r--  1 root root        613 May 16 04:01 special_tokens_map.json\\\\n-rw-r--r--  1 root root   11422654 May 16 04:01 tokenizer.json\\\\n-rw-r--r--  1 root root       5404 May 16 04:01 tokenizer_config.json\\\\n-rw-r--r--  1 root root    2776833 May 16 04:01 vocab.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.21}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 16013164\\ndrwxr-xr-x  2 root root       4096 May 16 04:01 .\\ndrwxr-xr-x 11 root root       4096 May 21 20:01 ..\\n-rw-r--r--  1 root root        707 May 16 04:01 added_tokens.json\\n-rw-r--r--  1 root root       4168 May 16 04:01 chat_template.jinja\\n-rw-r--r--  1 root root       1538 May 16 04:01 config.json\\n-rw-r--r--  1 root root        214 May 16 04:01 generation_config.json\\n-rw-r--r--  1 root root    1671853 May 16 04:01 merges.txt\\n-rw-r--r--  1 root root 4902257696 May 16 04:01 model-00001-of-00004.safetensors\\n-rw-r--r--  1 root root 4915960368 May 16 04:01 model-00002-of-00004.safetensors\\n-rw-r--r--  1 root root 4983068496 May 16 04:01 model-00003-of-00004.safetensors\\n-rw-r--r--  1 root root 1580230264 May 16 04:01 model-00004-of-00004.safetensors\\n-rw-r--r--  1 root root      32914 May 16 04:01 model.safetensors.index.json\\n-rw-r--r--  1 root root        613 May 16 04:01 special_tokens_map.json\\n-rw-r--r--  1 root root   11422654 May 16 04:01 tokenizer.json\\n-rw-r--r--  1 root root       5404 May 16 04:01 tokenizer_config.json\\n-rw-r--r--  1 root root    2776833 May 16 04:01 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"
    }
  },
  "sourceToolAssistantUUID": "8f6597c3-0081-4436-bea4-486cb7186041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 32 · 2026-05-23T05:48:07.490Z_

<details><summary>↩ Tool result · `toolu_016C6t9qbfNPLme2aB5ptwoB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 15701056\\ndrwxr-xr-x  2 root root       4096 May 16 03:53 .\\ndrwxr-xr-x 11 root root       4096 May 21 20:01 ..\\n-rw-r--r--  1 root root       4614 May 16 03:53 chat_template.jinja\\n-rw-r--r--  1 root root        868 May 16 03:53 config.json\\n-rw-r--r--  1 root root        184 May 16 03:53 generation_config.json\\n-rw-r--r--  1 root root 4976698672 May 16 03:53 model-00001-of-00004.safetensors\\n-rw-r--r--  1 root root 4999802720 May 16 03:53 model-00002-of-00004.safetensors\\n-rw-r--r--  1 root root 4915916176 May 16 03:53 model-00003-of-00004.safetensors\\n-rw-r--r--  1 root root 1168138808 May 16 03:53 model-00004-of-00004.safetensors\\n-rw-r--r--  1 root root      23986 May 16 03:53 model.safetensors.index.json\\n-rw-r--r--  1 root root        296 May 16 03:53 special_tokens_map.json\\n-rw-r--r--  1 root root   17209920 May 16 03:53 tokenizer.json\\n-rw-r--r--  1 root root      50525 May 16 03:53 tokenizer_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "172d0300-edcd-4fda-a058-f5374c1c7ec2",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "14b03f42-7a7b-451d-b2c1-f60503b55136",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 15701056\\\\ndrwxr-xr-x  2 root root       4096 May 16 03:53 .\\\\ndrwxr-xr-x 11 root root       4096 May 21 20:01 ..\\\\n-rw-r--r--  1 root root       4614 May 16 03:53 chat_template.jinja\\\\n-rw-r--r--  1 root root        868 May 16 03:53 config.json\\\\n-rw-r--r--  1 root root        184 May 16 03:53 generation_config.json\\\\n-rw-r--r--  1 root root 4976698672 May 16 03:53 model-00001-of-00004.safetensors\\\\n-rw-r--r--  1 root root 4999802720 May 16 03:53 model-00002-of-00004.safetensors\\\\n-rw-r--r--  1 root root 4915916176 May 16 03:53 model-00003-of-00004.safetensors\\\\n-rw-r--r--  1 root root 1168138808 May 16 03:53 model-00004-of-00004.safetensors\\\\n-rw-r--r--  1 root root      23986 May 16 03:53 model.safetensors.index.json\\\\n-rw-r--r--  1 root root        296 May 16 03:53 special_tokens_map.json\\\\n-rw-r--r--  1 root root   17209920 May 16 03:53 tokenizer.json\\\\n-rw-r--r--  1 root root      50525 May 16 03:53 tokenizer_config.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 15701056\\ndrwxr-xr-x  2 root root       4096 May 16 03:53 .\\ndrwxr-xr-x 11 root root       4096 May 21 20:01 ..\\n-rw-r--r--  1 root root       4614 May 16 03:53 chat_template.jinja\\n-rw-r--r--  1 root root        868 May 16 03:53 config.json\\n-rw-r--r--  1 root root        184 May 16 03:53 generation_config.json\\n-rw-r--r--  1 root root 4976698672 May 16 03:53 model-00001-of-00004.safetensors\\n-rw-r--r--  1 root root 4999802720 May 16 03:53 model-00002-of-00004.safetensors\\n-rw-r--r--  1 root root 4915916176 May 16 03:53 model-00003-of-00004.safetensors\\n-rw-r--r--  1 root root 1168138808 May 16 03:53 model-00004-of-00004.safetensors\\n-rw-r--r--  1 root root      23986 May 16 03:53 model.safetensors.index.json\\n-rw-r--r--  1 root root        296 May 16 03:53 special_tokens_map.json\\n-rw-r--r--  1 root root   17209920 May 16 03:53 tokenizer.json\\n-rw-r--r--  1 root root      50525 May 16 03:53 tokenizer_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  },
  "sourceToolAssistantUUID": "172d0300-edcd-4fda-a058-f5374c1c7ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-23T05:48:07.557Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MrPjJrN2Ldf72KHrwBf9jZ`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/scripts/quantize_8b.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14b03f42-7a7b-451d-b2c1-f60503b55136",
  "isSidechain": false,
  "requestId": "req_011CbJyT9hvsChETFh3fpQuF",
  "type": "assistant",
  "uuid": "62f0d503-fb29-4c1d-bc76-5cf09ebd26e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFxRTQ58Tndjj2PQ33pkNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11620,
      "cache_read_input_tokens": 26419,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 26419,
          "cache_creation_input_tokens": 11620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11620
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

_source line 34 · 2026-05-23T05:48:07.798Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0171TtxWorLanFgDcxZGEYVk`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/scripts/quantize_llama_8b.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62f0d503-fb29-4c1d-bc76-5cf09ebd26e5",
  "isSidechain": false,
  "requestId": "req_011CbJyT9hvsChETFh3fpQuF",
  "type": "assistant",
  "uuid": "7585cc16-496d-46ef-abc1-b5eed7418c17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFxRTQ58Tndjj2PQ33pkNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11620,
      "cache_read_input_tokens": 26419,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 26419,
          "cache_creation_input_tokens": 11620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11620
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

_source line 35 · 2026-05-23T05:48:08.041Z_

<details><summary>↩ Tool result · `toolu_01MrPjJrN2Ldf72KHrwBf9jZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Quantize fine-tuned Qwen3-8B (merged checkpoint) to AWQ INT4.\\\"\\\"\\\"\\nimport json\\nfrom awq import AutoAWQForCausalLM\\nfrom transformers import AutoTokenizer\\n\\nmodel_path = \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged/\\\"\\nquant_path = \\\"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\\\"\\n\\nprint(f\\\"Loading model from {model_path}\\\")\\nmodel = AutoAWQForCausalLM.from_pretrained(model_path)\\ntokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\n\\n# Use SciERC data for calibration (JSONL format)\\ncalib_data = []\\nwith open(\\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\") as f:\\n    for line in f:\\n        line = line.strip()\\n        if not line:\\n            continue\\n        doc = json.loads(line)\\n        for sent in doc.get(\\\"sentences\\\", []):\\n            text = \\\" \\\".join(sent)\\n            if text.strip():\\n                calib_data.append(text)\\n            if len(calib_data) >= 128:\\n                break\\n        if len(calib_data) >= 128:\\n            break\\n\\nprint(f\\\"Calibration samples: {len(calib_data)}\\\")\\n\\nquant_config = {\\\"zero_point\\\": True, \\\"q_group_size\\\": 128, \\\"w_bit\\\": 4, \\\"version\\\": \\\"GEMM\\\"}\\nprint(\\\"Starting quantization...\\\")\\nmodel.quantize(tokenizer, quant_config=quant_config, calib_data=calib_data)\\n\\nprint(f\\\"Saving to {quant_path}\\\")\\nmodel.save_quantized(quant_path)\\ntokenizer.save_pretrained(quant_path)\\nprint(\\\"Done!\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62f0d503-fb29-4c1d-bc76-5cf09ebd26e5",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "fc2d93d9-850a-48b9-bf31-b425d0a05581",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Quantize fine-tuned Qwen3-8B (merged checkpoint) to AWQ INT4.\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport json\\\\nfrom awq import AutoAWQForCausalLM\\\\nfrom transformers import AutoTokenizer\\\\n\\\\nmodel_path = \\\\\\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged/\\\\\\\"\\\\nquant_path = \\\\\\\"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\\\\\\\"\\\\n\\\\nprint(f\\\\\\\"Loading model from {model_path}\\\\\\\")\\\\nmodel = AutoAWQForCausalLM.from_pretrained(model_path)\\\\ntokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\\\n\\\\n# Use SciERC data for calibration (JSONL format)\\\\ncalib_data = []\\\\nwith open(\\\\\\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\\\\\") as f:\\\\n    for line in f:\\\\n        line = line.strip()\\\\n        if not line:\\\\n            continue\\\\n        doc = json.loads(line)\\\\n        for sent in doc.get(\\\\\\\"sentences\\\\\\\", []):\\\\n            text = \\\\\\\" \\\\\\\".join(sent)\\\\n            if text.strip():\\\\n                calib_data.append(text)\\\\n            if len(calib_data) >= 128:\\\\n                break\\\\n        if len(calib_data) >= 128:\\\\n            break\\\\n\\\\nprint(f\\\\\\\"Calibration samples: {len(calib_data)}\\\\\\\")\\\\n\\\\nquant_config = {\\\\\\\"zero_point\\\\\\\": True, \\\\\\\"q_group_size\\\\\\\": 128, \\\\\\\"w_bit\\\\\\\": 4, \\\\\\\"version\\\\\\\": \\\\\\\"GEMM\\\\\\\"}\\\\nprint(\\\\\\\"Starting quantization...\\\\\\\")\\\\nmodel.quantize(tokenizer, quant_config=quant_config, calib_data=calib_data)\\\\n\\\\nprint(f\\\\\\\"Saving to {quant_path}\\\\\\\")\\\\nmodel.save_quantized(quant_path)\\\\ntokenizer.save_pretrained(quant_path)\\\\nprint(\\\\\\\"Done!\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Quantize fine-tuned Qwen3-8B (merged checkpoint) to AWQ INT4.\\\"\\\"\\\"\\nimport json\\nfrom awq import AutoAWQForCausalLM\\nfrom transformers import AutoTokenizer\\n\\nmodel_path = \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged/\\\"\\nquant_path = \\\"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\\\"\\n\\nprint(f\\\"Loading model from {model_path}\\\")\\nmodel = AutoAWQForCausalLM.from_pretrained(model_path)\\ntokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\n\\n# Use SciERC data for calibration (JSONL format)\\ncalib_data = []\\nwith open(\\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\") as f:\\n    for line in f:\\n        line = line.strip()\\n        if not line:\\n            continue\\n        doc = json.loads(line)\\n        for sent in doc.get(\\\"sentences\\\", []):\\n            text = \\\" \\\".join(sent)\\n            if text.strip():\\n                calib_data.append(text)\\n            if len(calib_data) >= 128:\\n                break\\n        if len(calib_data) >= 128:\\n            break\\n\\nprint(f\\\"Calibration samples: {len(calib_data)}\\\")\\n\\nquant_config = {\\\"zero_point\\\": True, \\\"q_group_size\\\": 128, \\\"w_bit\\\": 4, \\\"version\\\": \\\"GEMM\\\"}\\nprint(\\\"Starting quantization...\\\")\\nmodel.quantize(tokenizer, quant_config=quant_config, calib_data=calib_data)\\n\\nprint(f\\\"Saving to {quant_path}\\\")\\nmodel.save_quantized(quant_path)\\ntokenizer.save_pretrained(quant_path)\\nprint(\\\"Done!\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  },
  "sourceToolAssistantUUID": "62f0d503-fb29-4c1d-bc76-5cf09ebd26e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-23T05:48:08.569Z_

<details><summary>↩ Tool result · `toolu_0171TtxWorLanFgDcxZGEYVk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"1\\\"\\n\\nimport json\\nfrom awq import AutoAWQForCausalLM\\nfrom transformers import AutoTokenizer\\n\\nmodel_path = \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged/\\\"\\nquant_path = \\\"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\\\"\\n\\nprint(f\\\"Loading model from {model_path}\\\")\\nmodel = AutoAWQForCausalLM.from_pretrained(model_path)\\ntokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\n\\nquant_config = {\\\"zero_point\\\": True, \\\"q_group_size\\\": 128, \\\"w_bit\\\": 4, \\\"version\\\": \\\"GEMM\\\"}\\n\\n# Build calibration data from SciERC test set\\ncalib_data = []\\ndata_file = \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\"\\nwith open(data_file) as f:\\n    for line in f:\\n        line = line.strip()\\n        if not line:\\n            continue\\n        doc = json.loads(line)\\n        for sent_tokens in doc.get(\\\"sentences\\\", []):\\n            text = \\\" \\\".join(sent_tokens)\\n            if len(text) > 20:\\n                calib_data.append(text)\\n            if len(calib_data) >= 128:\\n                break\\n        if len(calib_data) >= 128:\\n            break\\n\\nprint(f\\\"Calibration samples: {len(calib_data)}\\\")\\nprint(f\\\"Sample: {calib_data[0][:100]}...\\\")\\n\\nprint(\\\"Quantizing...\\\")\\nmodel.quantize(tokenizer, quant_config=quant_config, calib_data=calib_data)\\n\\nos.makedirs(quant_path, exist_ok=True)\\nmodel.save_quantized(quant_path)\\ntokenizer.save_pretrained(quant_path)\\nprint(f\\\"Quantization complete! Saved to {quant_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7585cc16-496d-46ef-abc1-b5eed7418c17",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "0fb5fad7-4f4f-47d1-ad9e-c6e8429643db",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"import os\\\\nos.environ[\\\\\\\"CUDA_VISIBLE_DEVICES\\\\\\\"] = \\\\\\\"1\\\\\\\"\\\\n\\\\nimport json\\\\nfrom awq import AutoAWQForCausalLM\\\\nfrom transformers import AutoTokenizer\\\\n\\\\nmodel_path = \\\\\\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged/\\\\\\\"\\\\nquant_path = \\\\\\\"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\\\\\\\"\\\\n\\\\nprint(f\\\\\\\"Loading model from {model_path}\\\\\\\")\\\\nmodel = AutoAWQForCausalLM.from_pretrained(model_path)\\\\ntokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\\\n\\\\nquant_config = {\\\\\\\"zero_point\\\\\\\": True, \\\\\\\"q_group_size\\\\\\\": 128, \\\\\\\"w_bit\\\\\\\": 4, \\\\\\\"version\\\\\\\": \\\\\\\"GEMM\\\\\\\"}\\\\n\\\\n# Build calibration data from SciERC test set\\\\ncalib_data = []\\\\ndata_file = \\\\\\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\\\\\"\\\\nwith open(data_file) as f:\\\\n    for line in f:\\\\n        line = line.strip()\\\\n        if not line:\\\\n            continue\\\\n        doc = json.loads(line)\\\\n        for sent_tokens in doc.get(\\\\\\\"sentences\\\\\\\", []):\\\\n            text = \\\\\\\" \\\\\\\".join(sent_tokens)\\\\n            if len(text) > 20:\\\\n                calib_data.append(text)\\\\n            if len(calib_data) >= 128:\\\\n                break\\\\n        if len(calib_data) >= 128:\\\\n            break\\\\n\\\\nprint(f\\\\\\\"Calibration samples: {len(calib_data)}\\\\\\\")\\\\nprint(f\\\\\\\"Sample: {calib_data[0][:100]}...\\\\\\\")\\\\n\\\\nprint(\\\\\\\"Quantizing...\\\\\\\")\\\\nmodel.quantize(tokenizer, quant_config=quant_config, calib_data=calib_data)\\\\n\\\\nos.makedirs(quant_path, exist_ok=True)\\\\nmodel.save_quantized(quant_path)\\\\ntokenizer.save_pretrained(quant_path)\\\\nprint(f\\\\\\\"Quantization complete! Saved to {quant_path}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"1\\\"\\n\\nimport json\\nfrom awq import AutoAWQForCausalLM\\nfrom transformers import AutoTokenizer\\n\\nmodel_path = \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged/\\\"\\nquant_path = \\\"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\\\"\\n\\nprint(f\\\"Loading model from {model_path}\\\")\\nmodel = AutoAWQForCausalLM.from_pretrained(model_path)\\ntokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\\n\\nquant_config = {\\\"zero_point\\\": True, \\\"q_group_size\\\": 128, \\\"w_bit\\\": 4, \\\"version\\\": \\\"GEMM\\\"}\\n\\n# Build calibration data from SciERC test set\\ncalib_data = []\\ndata_file = \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\"\\nwith open(data_file) as f:\\n    for line in f:\\n        line = line.strip()\\n        if not line:\\n            continue\\n        doc = json.loads(line)\\n        for sent_tokens in doc.get(\\\"sentences\\\", []):\\n            text = \\\" \\\".join(sent_tokens)\\n            if len(text) > 20:\\n                calib_data.append(text)\\n            if len(calib_data) >= 128:\\n                break\\n        if len(calib_data) >= 128:\\n            break\\n\\nprint(f\\\"Calibration samples: {len(calib_data)}\\\")\\nprint(f\\\"Sample: {calib_data[0][:100]}...\\\")\\n\\nprint(\\\"Quantizing...\\\")\\nmodel.quantize(tokenizer, quant_config=quant_config, calib_data=calib_data)\\n\\nos.makedirs(quant_path, exist_ok=True)\\nmodel.save_quantized(quant_path)\\ntokenizer.save_pretrained(quant_path)\\nprint(f\\\"Quantization complete! Saved to {quant_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  },
  "sourceToolAssistantUUID": "7585cc16-496d-46ef-abc1-b5eed7418c17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 37 · 2026-05-23T05:48:08.612Z_

```json
{
  "parentUuid": "0fb5fad7-4f4f-47d1-ad9e-c6e8429643db",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e8ccfed4-7e4a-46b3-bf94-63d1d0cb7f36",
  "timestamp": "2026-05-23T05:48:08.612Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 38 · 2026-05-23T05:48:13.076Z_

<details><summary>Logged reasoning block</summary>

```text
Both checkpoints exist. Now I need to:
1. Find DocRED data for calibration
2. Find the existing inference/eval scripts
3. Check DocRED FP16 baselines from registry
4. Create quantization scripts for DocRED

Let me search for DocRED data and the inference scripts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8ccfed4-7e4a-46b3-bf94-63d1d0cb7f36",
  "isSidechain": false,
  "requestId": "req_011CbJyTymAPTGCp7amdVhFo",
  "type": "assistant",
  "uuid": "c67f8a91-367b-4628-8798-f61e5177e2bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVEAvCzRoEAnvvLsbM3p8W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 38039,
      "output_tokens": 600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 600,
          "cache_read_input_tokens": 38039,
          "cache_creation_input_tokens": 3261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3261
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

_source line 39 · 2026-05-23T05:48:13.905Z_

两个 checkpoint 都在。现在查找 DocRED 数据文件和推理脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c67f8a91-367b-4628-8798-f61e5177e2bd",
  "isSidechain": false,
  "requestId": "req_011CbJyTymAPTGCp7amdVhFo",
  "type": "assistant",
  "uuid": "e0819319-d23c-401c-9625-8d6c494a1b9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVEAvCzRoEAnvvLsbM3p8W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 38039,
      "output_tokens": 600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 600,
          "cache_read_input_tokens": 38039,
          "cache_creation_input_tokens": 3261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3261
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

_source line 40 · 2026-05-23T05:48:14.402Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JJyTQjXEG9CxMSYjMHixPu`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0819319-d23c-401c-9625-8d6c494a1b9f",
  "isSidechain": false,
  "requestId": "req_011CbJyTymAPTGCp7amdVhFo",
  "type": "assistant",
  "uuid": "16fd1faf-c466-451b-984c-f8686c7fe1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVEAvCzRoEAnvvLsbM3p8W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 38039,
      "output_tokens": 600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 600,
          "cache_read_input_tokens": 38039,
          "cache_creation_input_tokens": 3261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3261
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

_source line 41 · 2026-05-23T05:48:14.406Z_

<details><summary>↩ Tool result · `toolu_01JJyTQjXEG9CxMSYjMHixPu`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16fd1faf-c466-451b-984c-f8686c7fe1e8",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "fc18be66-50e9-4461-9550-bf7fa50a9d22",
  "toolUseResult": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 26
  },
  "sourceToolAssistantUUID": "16fd1faf-c466-451b-984c-f8686c7fe1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-23T05:48:15.430Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KTUb2KL4WgshJgYHXX8nm5`</summary>

```json
{
  "server": "westd-16980",
  "command": "find /root/schema_semantic_constrained_ie/data/ -name \"*docred*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc18be66-50e9-4461-9550-bf7fa50a9d22",
  "isSidechain": false,
  "requestId": "req_011CbJyTymAPTGCp7amdVhFo",
  "type": "assistant",
  "uuid": "27959082-c2ea-46c0-a069-b5af13f93447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVEAvCzRoEAnvvLsbM3p8W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 38039,
      "output_tokens": 600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 600,
          "cache_read_input_tokens": 38039,
          "cache_creation_input_tokens": 3261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3261
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

_source line 43 · 2026-05-23T05:48:15.877Z_

<details><summary>↩ Tool result · `toolu_01KTUb2KL4WgshJgYHXX8nm5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27959082-c2ea-46c0-a069-b5af13f93447",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "5e72eb9d-6b5a-4778-94ea-10f7202091dd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  },
  "sourceToolAssistantUUID": "27959082-c2ea-46c0-a069-b5af13f93447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-23T05:48:17.062Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VDd8SmPw2MFLdTCM9YsR4E`</summary>

```json
{
  "server": "westd-16980",
  "command": "find /root/schema_semantic_constrained_ie/ -name \"eval_d064*\" -o -name \"run_*constrained*\" -o -name \"run_*inference*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e72eb9d-6b5a-4778-94ea-10f7202091dd",
  "isSidechain": false,
  "requestId": "req_011CbJyTymAPTGCp7amdVhFo",
  "type": "assistant",
  "uuid": "36b80bf7-c2f8-4cee-bccd-9b1d3645e098",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVEAvCzRoEAnvvLsbM3p8W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 38039,
      "output_tokens": 600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 600,
          "cache_read_input_tokens": 38039,
          "cache_creation_input_tokens": 3261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3261
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

_source line 45 · 2026-05-23T05:48:17.519Z_

<details><summary>↩ Tool result · `toolu_01VDd8SmPw2MFLdTCM9YsR4E`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/__pycache__/run_constrained_extraction.cpython-312.pyc\\n/root/schema_semantic_constrained_ie/__pycache__/run_constrained_extraction.cpython-310.pyc\\n/root/schema_semantic_constrained_ie/run_constrained_extraction.py\\n/root/schema_semantic_constrained_ie/scripts/eval_d064.py\\n/root/schema_semantic_constrained_ie/run_constrained_extraction.py.bak\\n/root/schema_semantic_constrained_ie/run_constrained_extraction.py.bak_mistral\\n/root/schema_semantic_constrained_ie/run_r4_constrained_after.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36b80bf7-c2f8-4cee-bccd-9b1d3645e098",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "a6841272-0d85-43a4-b228-7a6b6b5839b6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/schema_semantic_constrained_ie/__pycache__/run_constrained_extraction.cpython-312.pyc\\\\n/root/schema_semantic_constrained_ie/__pycache__/run_constrained_extraction.cpython-310.pyc\\\\n/root/schema_semantic_constrained_ie/run_constrained_extraction.py\\\\n/root/schema_semantic_constrained_ie/scripts/eval_d064.py\\\\n/root/schema_semantic_constrained_ie/run_constrained_extraction.py.bak\\\\n/root/schema_semantic_constrained_ie/run_constrained_extraction.py.bak_mistral\\\\n/root/schema_semantic_constrained_ie/run_r4_constrained_after.sh\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/__pycache__/run_constrained_extraction.cpython-312.pyc\\n/root/schema_semantic_constrained_ie/__pycache__/run_constrained_extraction.cpython-310.pyc\\n/root/schema_semantic_constrained_ie/run_constrained_extraction.py\\n/root/schema_semantic_constrained_ie/scripts/eval_d064.py\\n/root/schema_semantic_constrained_ie/run_constrained_extraction.py.bak\\n/root/schema_semantic_constrained_ie/run_constrained_extraction.py.bak_mistral\\n/root/schema_semantic_constrained_ie/run_r4_constrained_after.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  },
  "sourceToolAssistantUUID": "36b80bf7-c2f8-4cee-bccd-9b1d3645e098",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-23T05:48:17.709Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018xJhrahfH6DGUZxdxCRBhL`</summary>

```json
{
  "server": "westd-16980",
  "command": "find /root/schema_semantic_constrained_ie/ -name \"ontology_constraints*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6841272-0d85-43a4-b228-7a6b6b5839b6",
  "isSidechain": false,
  "requestId": "req_011CbJyTymAPTGCp7amdVhFo",
  "type": "assistant",
  "uuid": "02b3b347-29f6-4844-b660-7eec457935ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVEAvCzRoEAnvvLsbM3p8W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 38039,
      "output_tokens": 600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 600,
          "cache_read_input_tokens": 38039,
          "cache_creation_input_tokens": 3261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3261
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

_source line 47 · 2026-05-23T05:48:18.170Z_

<details><summary>↩ Tool result · `toolu_018xJhrahfH6DGUZxdxCRBhL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\\n/root/schema_semantic_constrained_ie/data/ace05/ontology_constraints_ace05.json\\n/root/schema_semantic_constrained_ie/data/wikievents/ontology_constraints_wikievents.json\\n/root/schema_semantic_constrained_ie/ontology_constraints.json\\n/root/schema_semantic_constrained_ie/ontology_constraints_shuffled.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02b3b347-29f6-4844-b660-7eec457935ab",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "9dbab786-7a2c-4b1e-b573-ad035124b897",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\\\\n/root/schema_semantic_constrained_ie/data/ace05/ontology_constraints_ace05.json\\\\n/root/schema_semantic_constrained_ie/data/wikievents/ontology_constraints_wikievents.json\\\\n/root/schema_semantic_constrained_ie/ontology_constraints.json\\\\n/root/schema_semantic_constrained_ie/ontology_constraints_shuffled.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json\\n/root/schema_semantic_constrained_ie/data/ace05/ontology_constraints_ace05.json\\n/root/schema_semantic_constrained_ie/data/wikievents/ontology_constraints_wikievents.json\\n/root/schema_semantic_constrained_ie/ontology_constraints.json\\n/root/schema_semantic_constrained_ie/ontology_constraints_shuffled.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  },
  "sourceToolAssistantUUID": "02b3b347-29f6-4844-b660-7eec457935ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-23T05:48:18.578Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Vg7NeGdt6Gm4PAzvDq6K7t`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "status": "DONE"
  },
  "limit": 30,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dbab786-7a2c-4b1e-b573-ad035124b897",
  "isSidechain": false,
  "requestId": "req_011CbJyTymAPTGCp7amdVhFo",
  "type": "assistant",
  "uuid": "2b42b33e-a151-43aa-b99e-d2b6a56476a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVEAvCzRoEAnvvLsbM3p8W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3261,
      "cache_read_input_tokens": 38039,
      "output_tokens": 600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 600,
          "cache_read_input_tokens": 38039,
          "cache_creation_input_tokens": 3261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3261
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

_source line 49_

```json
{
  "type": "last-prompt",
  "leafUuid": "2b42b33e-a151-43aa-b99e-d2b6a56476a6",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "DocRED INT4 quantization comparison experiments",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Tool result

_source line 51 · 2026-05-23T05:48:19.312Z_

<details><summary>↩ Tool result · `toolu_01Vg7NeGdt6Gm4PAzvDq6K7t`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:58:33.950Z\", \"updated_at\": \"2026-05-23T05:35:25.774Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"w5_llama_lora_scierc_constrained_eval\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test (551 docs)\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}, \"log_path\": \"outputs/sf2_llama_int4_scierc_s1/violation_report.json\", \"checkpoint_path\": \"outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:32:49.329Z\"}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:58:51.930Z\", \"updated_at\": \"2026-05-23T05:35:24.911Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test 551 sentences\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}, \"log_path\": \"outputs/sf2_qwen_int4_scierc_s1/violation_report.json\", \"checkpoint_path\": \"outputs/sf2_qwen_int4_scierc_s1/output.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:32:46.404Z\"}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:14:38.851Z\", \"updated_at\": \"2026-05-23T05:15:20.167Z\", \"hypothesis\": \"GoLLIE-7B achieves low schema violation rates on SciERC zero-shot because it outputs very conservatively (few entities, almost no relations), resulting in trivially low violation rates but extremely poor recall and F1.\", \"spec\": {\"command\": \"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 100, \"model_name\": \"GoLLIE-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/gollie_model/\", \"eval_data\": \"SciERC test (100 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/gollie_model/\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\"}, \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:15:20.167Z\"}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T00:41:26.371Z\", \"updated_at\": \"2026-05-23T02:30:50.739Z\", \"hypothesis\": \"Full S1 (grammar+semantic) constraints on 70B ZS DocRED should achieve DR close to semantic_only (1.66%) since grammar adds zero DR contribution in ZS setting. R_F1 should remain ~13 (matching unconstrained 13.25). This completes the ZS DocRED ablation matrix.\", \"parent\": \"eval_70b_zs_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 88678, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_full_s1.log\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/70b_zs_docred_200_full_s1.jsonl\", \"log_path\": \"/tmp/70b_zs_docred_200_full_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T02:30:50.739Z\"}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:35:19.975Z\", \"updated_at\": \"2026-05-23T01:55:24.472Z\", \"hypothesis\": \"Grammar-only constraints on 70B LoRA DocRED will eliminate RV violations but not reduce DR, mirroring the SciERC ablation pattern where grammar layer provides zero DR contribution at fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 984253, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_grammar_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T01:55:24.472Z\"}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:35:17.601Z\", \"updated_at\": \"2026-05-23T01:20:56.659Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA DocRED will reduce DR violations from unconstrained baseline (DR=0.88%) with minimal F1 impact, isolating the semantic layer's contribution in document-level RE at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 983803, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T01:20:56.659Z\"}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:55:27.332Z\", \"updated_at\": \"2026-05-23T00:38:42.757Z\", \"hypothesis\": \"70B ZS DocRED unconstrained 200-doc baseline to complete the ablation matrix. Expect DR~15% and R-F1~13 consistent with prior 99-doc measurement, providing matched-subset comparison for semantic_only (DR=1.66%) and grammar_only experiments.\", \"parent\": \"70b_docred_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 84588, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_unconstrained.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T00:38:42.757Z\"}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:24:11.190Z\", \"updated_at\": \"2026-05-23T00:37:43.935Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS DocRED will show minimal DR reduction (similar to SciERC 70B ZS pattern where grammar_only DR≈unconstrained), confirming that grammar layer's negligible contribution at 70B scale generalizes across datasets.\", \"parent\": \"r16_70b_docred_zs_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"eval_data\": \"DocRED dev 200-doc subset\", \"checkpoint_source\": \"n/a (zero-shot)\", \"log_path\": \"/tmp/70b_zs_docred_200_grammar_only.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T00:37:43.935Z\"}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:35:21.150Z\", \"updated_at\": \"2026-05-22T22:55:11.458Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS DocRED will significantly reduce DR violations from zero-shot baseline, demonstrating the semantic layer's effectiveness on document-level RE without fine-tuning.\", \"parent\": \"70b_docred_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:55:11.459Z\"}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:15:28.977Z\", \"updated_at\": \"2026-05-22T21:21:11.254Z\", \"hypothesis\": \"70B LoRA DocRED with beam search (k=4) + full_s1 on 200-doc subset will achieve DR=0% and CF≈0% while maintaining R-F1 comparable to greedy S1 (43.95), consistent with 8B beam search pattern.\", \"parent\": \"eval_70b_lora_docred_200_s1_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 70638, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\", \"log_path\": \"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\", \"note\": \"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\"}, \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:21:11.254Z\"}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:13:55.324Z\", \"updated_at\": \"2026-05-22T20:31:32.878Z\", \"hypothesis\": \"70B LoRA SciERC with grammar-only constrained decoding will reduce DR violations compared to unconstrained (DR=1.5%) but less than full_s1 (DR=0%), isolating grammar layer's independent contribution at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_grammar_only.log\", \"pid\": 70175}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}, \"completed_at\": \"2026-05-22T18:44:02.122Z\"}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:45:13.928Z\", \"updated_at\": \"2026-05-22T20:30:18.431Z\", \"hypothesis\": \"Independent 70B ZS SciERC unconstrained baseline to verify prior DR and R-F1 numbers from r16_70b_scierc_zs_s1 experiment. Expect DR~6-8% and R-F1~11 consistent with earlier measurements.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 74572, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_scierc_unconstrained.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}, \"completed_at\": \"2026-05-22T20:30:18.431Z\"}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:04:58.305Z\", \"updated_at\": \"2026-05-22T20:30:16.494Z\", \"hypothesis\": \"Full S2 constrained decoding on 70B LoRA SciERC achieves DR=0% like S1, with potentially fewer CF violations due to S2's enhanced cross-field consistency checking. R-F1 should be comparable to S1 (44.53-44.81).\", \"parent\": \"eval_70b_lora_scierc_s1_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 972139, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_full_s2.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}, \"completed_at\": \"2026-05-22T20:30:16.494Z\"}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:04:55.672Z\", \"updated_at\": \"2026-05-22T20:30:13.188Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA SciERC will reduce DR from 1.5% (unconstrained) toward 0%, consistent with the 70B ZS pattern where semantic layer is the primary DR reduction mechanism. Without grammar layer, some RV violations may appear.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 971668, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}, \"completed_at\": \"2026-05-22T20:30:13.188Z\"}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:48:40.066Z\", \"updated_at\": \"2026-05-22T18:16:23.650Z\", \"hypothesis\": \"Shuffling entity type order in the constraint schema (seed=42) does not significantly change constrained decoding results (R-F1 within ±0.5pp, violation rates identical), confirming that OntoCoDec is order-invariant. This addresses R19-W3 reviewer concern about entity registry ordering sensitivity.\", \"parent\": \"w5_lora_scierc_constrained_eval\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 967058, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/entity_order_shuffled_qwen_scierc.log\", \"shuffle_seed\": 42, \"original_entity_order\": [\"Task\", \"Method\", \"Material\", \"Metric\", \"OtherScientificTerm\", \"Generic\"], \"shuffled_entity_order\": [\"Metric\", \"Method\", \"Material\", \"OtherScientificTerm\", \"Task\", \"Generic\"], \"original_relation_order\": [\"Used-for\", \"Feature-of\", \"Hyponym-of\", \"Part-of\", \"Compare\", \"Conjunction\", \"Evaluate-for\"], \"shuffled_relation_order\": [\"Conjunction\", \"Evaluate-for\", \"Compare\", \"Part-of\", \"Feature-of\", \"Hyponym-of\", \"Used-for\"]}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}, \"completed_at\": \"2026-05-22T18:04:14.919Z\"}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:39:36.807Z\", \"updated_at\": \"2026-05-22T18:09:49.840Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS will reduce DR partially (similar to 8B pattern: ~24% reduction) without eliminating RV/ET, isolating semantic layer's independent contribution at 70B scale.\", \"parent\": \"r16_70b_scierc_zs_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"r16_70b_scierc_zs_s1\", \"eval_data\": \"scierc test set (551 docs)\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}, \"completed_at\": \"2026-05-22T18:09:49.840Z\"}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:39:44.901Z\", \"updated_at\": \"2026-05-22T18:09:48.056Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS reduce domain-range violations compared to unconstrained baseline (DR=6.41%) but less effectively than full_s1 (DR=0%), isolating grammar layer's contribution to constraint enforcement.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_grammar_only.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}, \"completed_at\": \"2026-05-22T18:09:48.056Z\"}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:39:43.218Z\", \"updated_at\": \"2026-05-22T18:04:29.880Z\", \"hypothesis\": \"70B LoRA fine-tuned model with beam search (k=4) and full_s1 constrained decoding on SciERC achieves DR=0% and CF=0%, matching 8B beam search behavior, while maintaining or improving extraction F1.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_beam4_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}, \"completed_at\": \"2026-05-22T18:04:29.880Z\"}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:48:16.222Z\", \"updated_at\": \"2026-05-22T16:27:25.157Z\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/beam4_tcr_llama_scierc.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}, \"conclusion\": \"negative\", \"hypothesis\": \"TCR reranking on beam4 outputs will change beam selection for LLaMA-SciERC by penalizing constraint-violating candidates, improving DR violation rate and overall F1 compared to vanilla beam4.\", \"completed_at\": \"2026-05-22T16:27:25.157Z\"}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:37:32.074Z\", \"updated_at\": \"2026-05-22T15:49:03.706Z\", \"hypothesis\": \"TCR (Type Consistency Reranking) with beam search (k=4) on Qwen3-8B LoRA SciERC will reduce domain/range violations compared to standard beam search by reranking candidates based on type consistency scores, while maintaining or improving Entity/Relation F1.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/beam_tcr_run.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T15:37:47.865Z\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}, \"parent\": \"d066_beam_sweep\"}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T13:29:07.493Z\", \"updated_at\": \"2026-05-22T13:30:06.224Z\", \"hypothesis\": \"vLLM's guided_json (JSON schema-constrained decoding) produces equivalent violation rates and F1 scores to our XGrammar grammar-only ablation, confirming that guided_json ≈ GCD (grammar-constrained decoding) without semantic constraints.\", \"spec\": {\"command\": \"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 0}, \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"log_path\": \"/tmp/vllm_guided_json_eval.log\", \"completed_at\": \"2026-05-22T13:30:06.224Z\"}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:47:05.464Z\", \"updated_at\": \"2026-05-22T10:34:22.854Z\", \"hypothesis\": \"70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve DR→0% while maintaining R-F1 comparable to unconstrained, confirming scale-independent constraint composability on DocRED at 70B scale\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": \"11466\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"200 (first 200 docs)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\", \"log_path\": \"westd-21461:/tmp/constrained_inference.log\"}, \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\", \"log_path\": \"westd-21461:/tmp/constrained_inference.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:34:01.646Z\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:44:23.637Z\", \"updated_at\": \"2026-05-22T10:34:14.027Z\", \"hypothesis\": \"Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\", \"spec\": {\"command\": \"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\", \"server\": \"westd-16980 + westd-21461\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"note\": \"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\"}, \"notes\": \"全部 8 配置完成 + eval 齐全。beam8 con: E-F1=66.36, R-F1=43.65, DR=0%, CF=0%, avg_time=5.058s。Pareto optimal: k=2 con (E-F1=67.71, R-F1=44.60, DR=0%)。k=8 相比 k=2 F1 下降 ~1.3pp 且推理慢 46%，收益递减明确。可入稿。\", \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}, \"conclusion\": \"success\", \"checkpoint_path\": \"parent experiment - see child experiments for individual outputs\", \"log_path\": \"parent experiment - see child experiments for individual logs\", \"completed_at\": \"2026-05-22T10:34:14.027Z\"}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.909Z\", \"updated_at\": \"2026-05-22T07:36:58.067Z\", \"hypothesis\": \"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"/tmp/w8_llama_docred_ft_grammar_only.log\", \"completed_at\": \"2026-05-16T12:31:33.933Z\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}, \"parent\": \"w5_llama_docred_lora_training\"}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:54:02.910Z\", \"updated_at\": \"2026-05-22T07:36:56.885Z\", \"hypothesis\": \"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\", \"parent\": \"w5_llama_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:49:59.199Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:50:01.253379+00:00\"}]}, \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"outputs/w8_llama_docred_ft_semantic_only.jsonl\", \"completed_at\": \"2026-05-16T16:55:22.088Z\"}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-22T07:36:54.996Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:18:27.113Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:18:29.130284+00:00\"}]}, \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:22:28.075Z\"}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:36.469Z\", \"updated_at\": \"2026-05-22T07:36:52.623Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen FT SciERC will show high DR (comparable to or worse than unconstrained), proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\"}, \"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:46.097Z\"}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:39.235Z\", \"updated_at\": \"2026-05-22T07:36:49.828Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama FT SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\"}, \"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:50.516Z\"}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:06:11.811Z\", \"updated_at\": \"2026-05-22T07:09:22.684Z\", \"hypothesis\": \"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale\", \"parent\": \"r16_70b_lora_docred\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\"run_constrained_extraction.py\\\", run_name=\\\"__main__\\\")'\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"998 (truncated to 200)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}, \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_unconstrained.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_unconstrained.log\", \"completed_at\": \"2026-05-22T07:09:22.684Z\"}, \"eval_70b_lora_scierc_s1_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:46:31.480Z\", \"updated_at\": \"2026-05-22T06:47:38.556Z\", \"hypothesis\": \"70B LoRA SciERC with Full S1 constrained decoding will achieve DR→0% while maintaining R-F1 comparable to unconstrained (44.73), confirming scale-independent constraint effectiveness at 70B with fine-tuning\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\"}, \"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:47:38.556Z\"}}, \"count\": 30, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7174}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b42b33e-a151-43aa-b99e-d2b6a56476a6",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "090f94ff-8ec3-40bf-a112-e44c822cf1fb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"sf2_llama_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T04:58:33.950Z\\\", \\\"updated_at\\\": \\\"2026-05-23T05:35:25.774Z\\\", \\\"hypothesis\\\": \\\"AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly affect constraint enforcement on SciERC S1\\\", \\\"parent\\\": \\\"w5_llama_lora_scierc_constrained_eval\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-SciERC-FT-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\\\", \\\"eval_data\\\": \\\"SciERC test (551 docs)\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.94, \\\"R-F1\\\": 43.98, \\\"E-F1\\\": 67.54, \\\"samples\\\": 551, \\\"R-P\\\": 40.47, \\\"R-R\\\": 48.15, \\\"E-P\\\": 65.51, \\\"E-R\\\": 69.7}, \\\"log_path\\\": \\\"outputs/sf2_llama_int4_scierc_s1/violation_report.json\\\", \\\"checkpoint_path\\\": \\\"outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T05:32:49.329Z\\\"}, \\\"sf2_qwen_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T04:58:51.930Z\\\", \\\"updated_at\\\": \\\"2026-05-23T05:35:24.911Z\\\", \\\"hypothesis\\\": \\\"AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement on SciERC S1\\\", \\\"parent\\\": \\\"d066_beam_sweep\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-SciERC-FT-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\\\", \\\"eval_data\\\": \\\"SciERC test 551 sentences\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 1.1, \\\"R-F1\\\": 41.71, \\\"E-F1\\\": 67.05, \\\"samples\\\": 551, \\\"R-P\\\": 38.52, \\\"R-R\\\": 45.48, \\\"E-P\\\": 64.76, \\\"E-R\\\": 69.52}, \\\"log_path\\\": \\\"outputs/sf2_qwen_int4_scierc_s1/violation_report.json\\\", \\\"checkpoint_path\\\": \\\"outputs/sf2_qwen_int4_scierc_s1/output.jsonl\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T05:32:46.404Z\\\"}, \\\"sf2_gollie_scierc_violation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T05:14:38.851Z\\\", \\\"updated_at\\\": \\\"2026-05-23T05:15:20.167Z\\\", \\\"hypothesis\\\": \\\"GoLLIE-7B achieves low schema violation rates on SciERC zero-shot because it outputs very conservatively (few entities, almost no relations), resulting in trivially low violation rates but extremely poor recall and F1.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"GoLLIE-7B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/gollie_model/\\\", \\\"eval_data\\\": \\\"SciERC test (100 docs)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gollie_model/\\\", \\\"log_path\\\": \\\"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\\\"}, \\\"metrics\\\": {\\\"GoLLIE_ZS\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.83, \\\"E_F1\\\": 9.17, \\\"R_F1\\\": 0, \\\"pred_ents\\\": 241, \\\"pred_rels\\\": 5, \\\"docs_with_output\\\": 54}, \\\"OntoCoDec_Qwen_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.61, \\\"E_F1\\\": 66.43, \\\"R_F1\\\": 43.69}, \\\"OntoCoDec_Llama_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.62, \\\"E_F1\\\": 67.09, \\\"R_F1\\\": 45.47}}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T05:15:20.167Z\\\"}, \\\"eval_70b_zs_docred_200_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T00:41:26.371Z\\\", \\\"updated_at\\\": \\\"2026-05-23T02:30:50.739Z\\\", \\\"hypothesis\\\": \\\"Full S1 (grammar+semantic) constraints on 70B ZS DocRED should achieve DR close to semantic_only (1.66%) since grammar adds zero DR contribution in ZS setting. R_F1 should remain ~13 (matching unconstrained 13.25). This completes the ZS DocRED ablation matrix.\\\", \\\"parent\\\": \\\"eval_70b_zs_docred_200_unconstrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 88678, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_full_s1.log\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 5.34, \\\"E-F1\\\": 70.05, \\\"R-F1\\\": 13.25, \\\"PF%\\\": 0, \\\"entities_pred\\\": 3234, \\\"relations_pred\\\": 2637, \\\"triples_checked\\\": 2642}, \\\"checkpoint_path\\\": \\\"/root/schema_semantic_constrained_ie/outputs/70b_zs_docred_200_full_s1.jsonl\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_full_s1.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T02:30:50.739Z\\\"}, \\\"eval_70b_lora_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T20:35:19.975Z\\\", \\\"updated_at\\\": \\\"2026-05-23T01:55:24.472Z\\\", \\\"hypothesis\\\": \\\"Grammar-only constraints on 70B LoRA DocRED will eliminate RV violations but not reduce DR, mirroring the SciERC ablation pattern where grammar layer provides zero DR contribution at fine-tuned scale.\\\", \\\"parent\\\": \\\"eval_70b_lora_docred_200_unconstrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 984253, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_docred_200_grammar_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 10.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.38, \\\"CF_pct\\\": 0.06, \\\"E_F1\\\": 80.13, \\\"E_P\\\": 85.16, \\\"E_R\\\": 75.66, \\\"R_F1\\\": 43.96, \\\"R_P\\\": 39.78, \\\"R_R\\\": 49.11, \\\"entities_pred\\\": 3362, \\\"relations_pred\\\": 3154}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-23T01:55:24.472Z\\\"}, \\\"eval_70b_lora_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T20:35:17.601Z\\\", \\\"updated_at\\\": \\\"2026-05-23T01:20:56.659Z\\\", \\\"hypothesis\\\": \\\"Semantic-only constraints on 70B LoRA DocRED will reduce DR violations from unconstrained baseline (DR=0.88%) with minimal F1 impact, isolating the semantic layer's contribution in document-level RE at 70B fine-tuned scale.\\\", \\\"parent\\\": \\\"eval_70b_lora_docred_200_unconstrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 983803, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_docred_200_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 11, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.51, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.21, \\\"E_F1\\\": 80.06, \\\"E_P\\\": 85.21, \\\"E_R\\\": 75.5, \\\"R_F1\\\": 43.61, \\\"R_P\\\": 39.44, \\\"R_R\\\": 48.75, \\\"entities_pred\\\": 3351, \\\"relations_pred\\\": 3148}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T01:20:56.659Z\\\"}, \\\"eval_70b_zs_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T22:55:27.332Z\\\", \\\"updated_at\\\": \\\"2026-05-23T00:38:42.757Z\\\", \\\"hypothesis\\\": \\\"70B ZS DocRED unconstrained 200-doc baseline to complete the ablation matrix. Expect DR~15% and R-F1~13 consistent with prior 99-doc measurement, providing matched-subset comparison for semantic_only (DR=1.66%) and grammar_only experiments.\\\", \\\"parent\\\": \\\"70b_docred_unconstrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 84588, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_unconstrained.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities_pred\\\": 3242, \\\"relations_pred\\\": 2637, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 7.88, \\\"DR_pct\\\": 13.45, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 8, \\\"E_F1\\\": 70.14, \\\"E_P\\\": 75.85, \\\"E_R\\\": 65.23, \\\"R_F1\\\": 13.25, \\\"R_P\\\": 12.97, \\\"R_R\\\": 13.54}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-23T00:38:42.757Z\\\"}, \\\"eval_70b_zs_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T21:24:11.190Z\\\", \\\"updated_at\\\": \\\"2026-05-23T00:37:43.935Z\\\", \\\"hypothesis\\\": \\\"Grammar-only constraints on 70B ZS DocRED will show minimal DR reduction (similar to SciERC 70B ZS pattern where grammar_only DR≈unconstrained), confirming that grammar layer's negligible contribution at 70B scale generalizes across datasets.\\\", \\\"parent\\\": \\\"r16_70b_docred_zs_s1\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"eval_data\\\": \\\"DocRED dev 200-doc subset\\\", \\\"checkpoint_source\\\": \\\"n/a (zero-shot)\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_grammar_only.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 1, \\\"entities_pred\\\": 3221, \\\"relations_pred\\\": 2609, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 17.03, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"E_F1\\\": 70.12, \\\"E_P\\\": 75.88, \\\"E_R\\\": 65.17, \\\"R_F1\\\": 13.23, \\\"R_P\\\": 12.99, \\\"R_R\\\": 13.47}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-23T00:37:43.935Z\\\"}, \\\"eval_70b_zs_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T20:35:21.150Z\\\", \\\"updated_at\\\": \\\"2026-05-22T22:55:11.458Z\\\", \\\"hypothesis\\\": \\\"Semantic-only constraints on 70B ZS DocRED will significantly reduce DR violations from zero-shot baseline, demonstrating the semantic layer's effectiveness on document-level RE without fine-tuning.\\\", \\\"parent\\\": \\\"70b_docred_unconstrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities\\\": 3240, \\\"relations\\\": 2596, \\\"ET_pct\\\": 0.12, \\\"RV_pct\\\": 8.24, \\\"DR_pct\\\": 1.66, \\\"CF_count\\\": 132, \\\"CF_pct\\\": 4.07, \\\"E_F1\\\": 70.1, \\\"E_P\\\": 75.87, \\\"E_R\\\": 65.15, \\\"R_F1\\\": 13.05, \\\"R_P\\\": 12.88, \\\"R_R\\\": 13.23, \\\"fuzzy_matches\\\": 8}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T22:55:11.459Z\\\"}, \\\"eval_70b_lora_docred_200_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T17:15:28.977Z\\\", \\\"updated_at\\\": \\\"2026-05-22T21:21:11.254Z\\\", \\\"hypothesis\\\": \\\"70B LoRA DocRED with beam search (k=4) + full_s1 on 200-doc subset will achieve DR=0% and CF≈0% while maintaining R-F1 comparable to greedy S1 (43.95), consistent with 8B beam search pattern.\\\", \\\"parent\\\": \\\"eval_70b_lora_docred_200_s1_constrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\\\", \\\"pid\\\": 70638, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\\\", \\\"note\\\": \\\"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.57, \\\"E-P\\\": 85.45, \\\"E-R\\\": 85.68, \\\"R-F1\\\": 48.14, \\\"R-P\\\": 44.24, \\\"R-R\\\": 52.79, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"parse_fail\\\": \\\"1/200 (0.5%)\\\", \\\"entities_pred\\\": 3790, \\\"relations_pred\\\": 3030}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T21:21:11.254Z\\\"}, \\\"eval_70b_lora_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T17:13:55.324Z\\\", \\\"updated_at\\\": \\\"2026-05-22T20:31:32.878Z\\\", \\\"hypothesis\\\": \\\"70B LoRA SciERC with grammar-only constrained decoding will reduce DR violations compared to unconstrained (DR=1.5%) but less than full_s1 (DR=0%), isolating grammar layer's independent contribution at 70B fine-tuned scale.\\\", \\\"parent\\\": \\\"eval_70b_lora_scierc_unconstrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_grammar_only.log\\\", \\\"pid\\\": 70175}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"json_failure_rate\\\": 0, \\\"entities\\\": 1805, \\\"relations\\\": 1133, \\\"entity_type_violations\\\": 0, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocab_violations\\\": 0, \\\"relation_vocab_violation_rate\\\": 0, \\\"domain_range_violations\\\": 17, \\\"domain_range_violation_rate\\\": 0.015, \\\"cross_field_consistency_violations\\\": 0, \\\"fuzzy_relation_matches\\\": 0, \\\"entity_P\\\": 0.6272, \\\"entity_R\\\": 0.6707, \\\"entity_F1\\\": 0.6482, \\\"relation_P\\\": 0.4152, \\\"relation_R\\\": 0.4825, \\\"relation_F1\\\": 0.4463}, \\\"completed_at\\\": \\\"2026-05-22T18:44:02.122Z\\\"}, \\\"eval_70b_zs_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T18:45:13.928Z\\\", \\\"updated_at\\\": \\\"2026-05-22T20:30:18.431Z\\\", \\\"hypothesis\\\": \\\"Independent 70B ZS SciERC unconstrained baseline to verify prior DR and R-F1 numbers from r16_70b_scierc_zs_s1 experiment. Expect DR~6-8% and R-F1~11 consistent with earlier measurements.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\\\", \\\"pid\\\": 74572, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_scierc_unconstrained.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 2353, \\\"relations\\\": 1483, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.6, \\\"DR_pct\\\": 6.4, \\\"CF_count\\\": 0, \\\"E_F1\\\": 35.22, \\\"E_P\\\": 30.13, \\\"E_R\\\": 42.38, \\\"R_F1\\\": 11.23, \\\"R_P\\\": 9.31, \\\"R_R\\\": 14.17, \\\"parse_fail_pct\\\": 0}, \\\"completed_at\\\": \\\"2026-05-22T20:30:18.431Z\\\"}, \\\"eval_70b_lora_scierc_full_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T18:04:58.305Z\\\", \\\"updated_at\\\": \\\"2026-05-22T20:30:16.494Z\\\", \\\"hypothesis\\\": \\\"Full S2 constrained decoding on 70B LoRA SciERC achieves DR=0% like S1, with potentially fewer CF violations due to S2's enhanced cross-field consistency checking. R-F1 should be comparable to S1 (44.53-44.81).\\\", \\\"parent\\\": \\\"eval_70b_lora_scierc_s1_constrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 972139, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_full_s2.log\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1531, \\\"relations\\\": 1027, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 18, \\\"E_F1\\\": 62.35, \\\"E_P\\\": 65.44, \\\"E_R\\\": 59.53, \\\"R_F1\\\": 36.28, \\\"R_P\\\": 35.35, \\\"R_R\\\": 37.27, \\\"parse_fail_pct\\\": 0}, \\\"completed_at\\\": \\\"2026-05-22T20:30:16.494Z\\\"}, \\\"eval_70b_lora_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T18:04:55.672Z\\\", \\\"updated_at\\\": \\\"2026-05-22T20:30:13.188Z\\\", \\\"hypothesis\\\": \\\"Semantic-only constraints on 70B LoRA SciERC will reduce DR from 1.5% (unconstrained) toward 0%, consistent with the 70B ZS pattern where semantic layer is the primary DR reduction mechanism. Without grammar layer, some RV violations may appear.\\\", \\\"parent\\\": \\\"eval_70b_lora_scierc_unconstrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 971668, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_semantic_only.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1806, \\\"relations\\\": 1133, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.6, \\\"CF_count\\\": 9, \\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"parse_fail_pct\\\": 0}, \\\"completed_at\\\": \\\"2026-05-22T20:30:13.188Z\\\"}, \\\"entity_order_ablation_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:48:40.066Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:16:23.650Z\\\", \\\"hypothesis\\\": \\\"Shuffling entity type order in the constraint schema (seed=42) does not significantly change constrained decoding results (R-F1 within ±0.5pp, violation rates identical), confirming that OntoCoDec is order-invariant. This addresses R19-W3 reviewer concern about entity registry ordering sensitivity.\\\", \\\"parent\\\": \\\"w5_lora_scierc_constrained_eval\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 967058, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-LoRA-SciERC-merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"log_path\\\": \\\"/tmp/entity_order_shuffled_qwen_scierc.log\\\", \\\"shuffle_seed\\\": 42, \\\"original_entity_order\\\": [\\\"Task\\\", \\\"Method\\\", \\\"Material\\\", \\\"Metric\\\", \\\"OtherScientificTerm\\\", \\\"Generic\\\"], \\\"shuffled_entity_order\\\": [\\\"Metric\\\", \\\"Method\\\", \\\"Material\\\", \\\"OtherScientificTerm\\\", \\\"Task\\\", \\\"Generic\\\"], \\\"original_relation_order\\\": [\\\"Used-for\\\", \\\"Feature-of\\\", \\\"Hyponym-of\\\", \\\"Part-of\\\", \\\"Compare\\\", \\\"Conjunction\\\", \\\"Evaluate-for\\\"], \\\"shuffled_relation_order\\\": [\\\"Conjunction\\\", \\\"Evaluate-for\\\", \\\"Compare\\\", \\\"Part-of\\\", \\\"Feature-of\\\", \\\"Hyponym-of\\\", \\\"Used-for\\\"]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 67.05, \\\"E_P\\\": 65.23, \\\"E_R\\\": 68.98, \\\"R_F1\\\": 43.77, \\\"R_P\\\": 40.78, \\\"R_R\\\": 47.23, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 21, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1784, \\\"relations\\\": 1128, \\\"corrected_original_R_F1\\\": 43.77, \\\"corrected_original_E_F1\\\": 67.05, \\\"corrected_original_DR_pct\\\": 0, \\\"corrected_original_CF_count\\\": 21, \\\"corrected_delta_R_F1\\\": 0, \\\"corrected_delta_E_F1\\\": 0, \\\"raw_output_identical\\\": true, \\\"parsed_output_identical\\\": true, \\\"note\\\": \\\"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\\\"}, \\\"completed_at\\\": \\\"2026-05-22T18:04:14.919Z\\\"}, \\\"eval_70b_zs_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T14:39:36.807Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:09:49.840Z\\\", \\\"hypothesis\\\": \\\"Semantic-only constraints on 70B ZS will reduce DR partially (similar to 8B pattern: ~24% reduction) without eliminating RV/ET, isolating semantic layer's independent contribution at 70B scale.\\\", \\\"parent\\\": \\\"r16_70b_scierc_zs_s1\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"r16_70b_scierc_zs_s1\\\", \\\"eval_data\\\": \\\"scierc test set (551 docs)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/eval_70b_zs_scierc_semantic_only.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.37, \\\"DR_pct\\\": 1.01, \\\"RV_pct\\\": 0.6, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 76, \\\"samples\\\": 551}, \\\"completed_at\\\": \\\"2026-05-22T18:09:49.840Z\\\"}, \\\"eval_70b_zs_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T14:39:44.901Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:09:48.056Z\\\", \\\"hypothesis\\\": \\\"Grammar-only constraints on 70B ZS reduce domain-range violations compared to unconstrained baseline (DR=6.41%) but less effectively than full_s1 (DR=0%), isolating grammar layer's contribution to constraint enforcement.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/eval_70b_zs_scierc_grammar_only.log\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.23, \\\"DR_pct\\\": 6.33, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 0, \\\"samples\\\": 551}, \\\"completed_at\\\": \\\"2026-05-22T18:09:48.056Z\\\"}, \\\"eval_70b_lora_scierc_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T14:39:43.218Z\\\", \\\"updated_at\\\": \\\"2026-05-22T18:04:29.880Z\\\", \\\"hypothesis\\\": \\\"70B LoRA fine-tuned model with beam search (k=4) and full_s1 constrained decoding on SciERC achieves DR=0% and CF=0%, matching 8B beam search behavior, while maintaining or improving extraction F1.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_beam4_s1.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 64.89, \\\"E_P\\\": 62.29, \\\"E_R\\\": 67.72, \\\"R_F1\\\": 44.81, \\\"R_P\\\": 39.45, \\\"R_R\\\": 51.85, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 1, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1839, \\\"relations\\\": 1283}, \\\"completed_at\\\": \\\"2026-05-22T18:04:29.880Z\\\"}, \\\"tcr_beam4_llama_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:48:16.222Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:27:25.157Z\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/beam4_tcr_llama_scierc.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1803, \\\"relations\\\": 1194, \\\"entity_type_violations\\\": \\\"0/1803 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1194 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"13/1194 (1.1%)\\\", \\\"cross_field_consistency\\\": 0, \\\"DR_pct\\\": 1.09, \\\"E_F1\\\": 68.02, \\\"E_P\\\": 65.88, \\\"E_R\\\": 70.29, \\\"R_F1\\\": 46.05, \\\"R_P\\\": 41.83, \\\"R_R\\\": 51.23, \\\"tcr_changed_selection\\\": \\\"0/551 (0.0%)\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"TCR reranking on beam4 outputs will change beam selection for LLaMA-SciERC by penalizing constraint-violating candidates, improving DR violation rate and overall F1 compared to vanilla beam4.\\\", \\\"completed_at\\\": \\\"2026-05-22T16:27:25.157Z\\\"}, \\\"tcr_beam4_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T14:37:32.074Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:49:03.706Z\\\", \\\"hypothesis\\\": \\\"TCR (Type Consistency Reranking) with beam search (k=4) on Qwen3-8B LoRA SciERC will reduce domain/range violations compared to standard beam search by reranking candidates based on type consistency scores, while maintaining or improving Entity/Relation F1.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-LoRA-SciERC-merged\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"log_path\\\": \\\"/tmp/beam_tcr_run.log\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-22T15:37:47.865Z\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1802, \\\"relations\\\": 1250, \\\"entity_type_violations\\\": \\\"0/1802 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1250 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"23/1250 (1.8%)\\\", \\\"cross_field_consistency_violations\\\": 1, \\\"DR_pct\\\": 1.84, \\\"E_P\\\": 65.05, \\\"E_R\\\": 69.64, \\\"E_F1\\\": 67.26, \\\"R_P\\\": 39.36, \\\"R_R\\\": 50.51, \\\"R_F1\\\": 44.24, \\\"TCR_changed_selection\\\": \\\"0/551 (0.0%)\\\", \\\"all_candidates_TCR_1.0\\\": true}, \\\"parent\\\": \\\"d066_beam_sweep\\\"}, \\\"vllm_guided_json_scierc_zs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T13:29:07.493Z\\\", \\\"updated_at\\\": \\\"2026-05-22T13:30:06.224Z\\\", \\\"hypothesis\\\": \\\"vLLM's guided_json (JSON schema-constrained decoding) produces equivalent violation rates and F1 scores to our XGrammar grammar-only ablation, confirming that guided_json ≈ GCD (grammar-constrained decoding) without semantic constraints.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B\\\", \\\"seed\\\": 0}, \\\"metrics\\\": {\\\"DR%\\\": 15.26, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.04, \\\"R-F1\\\": 8.75, \\\"E-F1\\\": 30.91, \\\"parse_fail%\\\": 0, \\\"total_samples\\\": 551, \\\"total_entities\\\": 2485, \\\"total_relations\\\": 1724, \\\"inference_time_s\\\": 108.5}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"N/A (eval-only experiment)\\\", \\\"log_path\\\": \\\"/tmp/vllm_guided_json_eval.log\\\", \\\"completed_at\\\": \\\"2026-05-22T13:30:06.224Z\\\"}, \\\"eval_70b_lora_docred_200_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T05:47:05.464Z\\\", \\\"updated_at\\\": \\\"2026-05-22T10:34:22.854Z\\\", \\\"hypothesis\\\": \\\"70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve DR→0% while maintaining R-F1 comparable to unconstrained, confirming scale-independent constraint composability on DocRED at 70B scale\\\", \\\"parent\\\": \\\"eval_70b_lora_docred_200_unconstrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"11466\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": \\\"200 (first 200 docs)\\\", \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/tmp/constrained_inference.log\\\"}, \\\"checkpoint_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/tmp/constrained_inference.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T10:34:01.646Z\\\", \\\"metrics\\\": {\\\"E_F1\\\": 79.38, \\\"E_P\\\": 85.24, \\\"E_R\\\": 74.28, \\\"R_F1\\\": 43.95, \\\"R_P\\\": 40.48, \\\"R_R\\\": 48.08, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.18, \\\"parse_fail_pct\\\": 12.5, \\\"samples\\\": 200}}, \\\"d066_beam_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T23:44:23.637Z\\\", \\\"updated_at\\\": \\\"2026-05-22T10:34:14.027Z\\\", \\\"hypothesis\\\": \\\"Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\\\", \\\"spec\\\": {\\\"command\\\": \\\"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\\\", \\\"server\\\": \\\"westd-16980 + westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"note\\\": \\\"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\\\"}, \\\"notes\\\": \\\"全部 8 配置完成 + eval 齐全。beam8 con: E-F1=66.36, R-F1=43.65, DR=0%, CF=0%, avg_time=5.058s。Pareto optimal: k=2 con (E-F1=67.71, R-F1=44.60, DR=0%)。k=8 相比 k=2 F1 下降 ~1.3pp 且推理慢 46%，收益递减明确。可入稿。\\\", \\\"metrics\\\": {\\\"scierc_qwen3_8b\\\": {\\\"k1_unc\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 2.11, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.494}, \\\"k1_con\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.5, \\\"avg_time\\\": 2.932}, \\\"k2_unc\\\": {\\\"E_F1\\\": 67.79, \\\"R_F1\\\": 44.75, \\\"DR_pct\\\": 1.54, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.954}, \\\"k2_con\\\": {\\\"E_F1\\\": 67.71, \\\"R_F1\\\": 44.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.11, \\\"avg_time\\\": 3.463}, \\\"k4_unc\\\": {\\\"E_F1\\\": 67.49, \\\"R_F1\\\": 43.72, \\\"DR_pct\\\": 1.89, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 3.485}, \\\"k4_con\\\": {\\\"E_F1\\\": 67.22, \\\"R_F1\\\": 43.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.069}, \\\"k8_unc\\\": {\\\"E_F1\\\": 66.4, \\\"R_F1\\\": 43.17, \\\"DR_pct\\\": 1.77, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.194}, \\\"k8_con\\\": {\\\"E_F1\\\": 66.36, \\\"R_F1\\\": 43.65, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 5.058}}, \\\"pareto_optimal\\\": \\\"k=2 con\\\", \\\"best_E_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 67.79}, \\\"best_R_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 44.75}}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"parent experiment - see child experiments for individual outputs\\\", \\\"log_path\\\": \\\"parent experiment - see child experiments for individual logs\\\", \\\"completed_at\\\": \\\"2026-05-22T10:34:14.027Z\\\"}, \\\"w8_llama_docred_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T06:34:25.909Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:58.067Z\\\", \\\"hypothesis\\\": \\\"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"llama_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"w5_llama_docred_lora\\\", \\\"eval_data\\\": \\\"docred_dev_998\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"log_path\\\": \\\"/tmp/w8_llama_docred_ft_grammar_only.log\\\", \\\"completed_at\\\": \\\"2026-05-16T12:31:33.933Z\\\", \\\"metrics\\\": {\\\"R_F1\\\": 43.72, \\\"R_P\\\": 38.57, \\\"R_R\\\": 50.44, \\\"parse_fail_pct\\\": 2.3, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\\\"}, \\\"parent\\\": \\\"w5_llama_docred_lora_training\\\"}, \\\"w8_llama_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T10:54:02.910Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:56.885Z\\\", \\\"hypothesis\\\": \\\"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\\\", \\\"parent\\\": \\\"w5_llama_docred_lora_training\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\\\\\"\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": 1, \\\"pid\\\": 361202, \\\"model_name\\\": \\\"Llama-3.1-8B-LoRA-DocRED\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-16T16:49:59.199Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-16T16:50:01.253379+00:00\\\"}]}, \\\"metrics\\\": {\\\"R_F1\\\": 43.85, \\\"R_P\\\": 38.85, \\\"R_R\\\": 50.31, \\\"parse_fail_pct\\\": 2.4, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"log_path\\\": \\\"outputs/w8_llama_docred_ft_semantic_only.jsonl\\\", \\\"completed_at\\\": \\\"2026-05-16T16:55:22.088Z\\\"}, \\\"w8_qwen_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T10:08:59.297Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:54.996Z\\\", \\\"hypothesis\\\": \\\"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\\\", \\\"parent\\\": \\\"w5_qwen_docred_lora_training\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"qwen_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"qwen_lora_docred_merged\\\", \\\"eval_data\\\": \\\"docred_test_998\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"log_path\\\": \\\"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-16T16:18:27.113Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-16T16:18:29.130284+00:00\\\"}]}, \\\"metrics\\\": {\\\"R_F1\\\": 40.85, \\\"R_P\\\": 36.33, \\\"R_R\\\": 46.65, \\\"parse_fail_pct\\\": 7.52, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-16T16:22:28.075Z\\\"}, \\\"r16_trie_qwen_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T03:44:36.469Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:52.623Z\\\", \\\"hypothesis\\\": \\\"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen FT SciERC will show high DR (comparable to or worse than unconstrained), proving grammar layer is prerequisite for vocabulary membership enforcement\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B (fine-tuned)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 64.4, \\\"E_P\\\": 66.8, \\\"E_R\\\": 62.16, \\\"R_F1\\\": 41.16, \\\"R_P\\\": 38.24, \\\"R_R\\\": 44.56, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 95.5, \\\"CF_pct\\\": 0.09, \\\"parse_fail_pct\\\": 9.1, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-21T04:59:46.097Z\\\"}, \\\"r16_trie_llama_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T03:44:39.235Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:36:49.828Z\\\", \\\"hypothesis\\\": \\\"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama FT SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (fine-tuned)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 36.66, \\\"E_P\\\": 67.47, \\\"E_R\\\": 25.16, \\\"R_F1\\\": 19.95, \\\"R_P\\\": 41.42, \\\"R_R\\\": 13.14, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 15.2, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 50.8, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-21T04:59:50.516Z\\\"}, \\\"eval_70b_lora_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T04:06:11.811Z\\\", \\\"updated_at\\\": \\\"2026-05-22T07:09:22.684Z\\\", \\\"hypothesis\\\": \\\"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale\\\", \\\"parent\\\": \\\"r16_70b_lora_docred\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\\\\\"run_constrained_extraction.py\\\\\\\", run_name=\\\\\\\"__main__\\\\\\\")'\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": \\\"998 (truncated to 200)\\\", \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 80.34, \\\"E_P\\\": 85.13, \\\"E_R\\\": 76.05, \\\"R_F1\\\": 43.8, \\\"R_P\\\": 39.6, \\\"R_R\\\": 48.99, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.57, \\\"DR_pct\\\": 0.22, \\\"CF_pct\\\": 0.06, \\\"parse_fail_pct\\\": 10, \\\"samples\\\": 200, \\\"relations\\\": 3159, \\\"RV_count\\\": 18, \\\"DR_count\\\": 7, \\\"CF_count\\\": 2}, \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_unconstrained.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_unconstrained.log\\\", \\\"completed_at\\\": \\\"2026-05-22T07:09:22.684Z\\\"}, \\\"eval_70b_lora_scierc_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T05:46:31.480Z\\\", \\\"updated_at\\\": \\\"2026-05-22T06:47:38.556Z\\\", \\\"hypothesis\\\": \\\"70B LoRA SciERC with Full S1 constrained decoding will achieve DR→0% while maintaining R-F1 comparable to unconstrained (44.73), confirming scale-independent constraint effectiveness at 70B with fine-tuning\\\", \\\"parent\\\": \\\"eval_70b_lora_scierc_unconstrained\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\\\"}, \\\"metrics\\\": {\\\"entity_f1\\\": 0.6476, \\\"entity_precision\\\": 0.6266, \\\"entity_recall\\\": 0.6701, \\\"relation_f1\\\": 0.4453, \\\"relation_precision\\\": 0.4149, \\\"relation_recall\\\": 0.4805, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 15, \\\"parse_fail_pct\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"num_samples\\\": 551, \\\"num_entities\\\": 1805, \\\"num_relations\\\": 1129}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T06:47:38.556Z\\\"}}, \\\"count\\\": 30, \\\"total\\\": 158, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7174}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:58:33.950Z\", \"updated_at\": \"2026-05-23T05:35:25.774Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"w5_llama_lora_scierc_constrained_eval\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test (551 docs)\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}, \"log_path\": \"outputs/sf2_llama_int4_scierc_s1/violation_report.json\", \"checkpoint_path\": \"outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:32:49.329Z\"}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:58:51.930Z\", \"updated_at\": \"2026-05-23T05:35:24.911Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test 551 sentences\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}, \"log_path\": \"outputs/sf2_qwen_int4_scierc_s1/violation_report.json\", \"checkpoint_path\": \"outputs/sf2_qwen_int4_scierc_s1/output.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:32:46.404Z\"}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:14:38.851Z\", \"updated_at\": \"2026-05-23T05:15:20.167Z\", \"hypothesis\": \"GoLLIE-7B achieves low schema violation rates on SciERC zero-shot because it outputs very conservatively (few entities, almost no relations), resulting in trivially low violation rates but extremely poor recall and F1.\", \"spec\": {\"command\": \"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 100, \"model_name\": \"GoLLIE-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/gollie_model/\", \"eval_data\": \"SciERC test (100 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/gollie_model/\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\"}, \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:15:20.167Z\"}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T00:41:26.371Z\", \"updated_at\": \"2026-05-23T02:30:50.739Z\", \"hypothesis\": \"Full S1 (grammar+semantic) constraints on 70B ZS DocRED should achieve DR close to semantic_only (1.66%) since grammar adds zero DR contribution in ZS setting. R_F1 should remain ~13 (matching unconstrained 13.25). This completes the ZS DocRED ablation matrix.\", \"parent\": \"eval_70b_zs_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 88678, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_full_s1.log\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/70b_zs_docred_200_full_s1.jsonl\", \"log_path\": \"/tmp/70b_zs_docred_200_full_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T02:30:50.739Z\"}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:35:19.975Z\", \"updated_at\": \"2026-05-23T01:55:24.472Z\", \"hypothesis\": \"Grammar-only constraints on 70B LoRA DocRED will eliminate RV violations but not reduce DR, mirroring the SciERC ablation pattern where grammar layer provides zero DR contribution at fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 984253, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_grammar_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T01:55:24.472Z\"}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:35:17.601Z\", \"updated_at\": \"2026-05-23T01:20:56.659Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA DocRED will reduce DR violations from unconstrained baseline (DR=0.88%) with minimal F1 impact, isolating the semantic layer's contribution in document-level RE at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 983803, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T01:20:56.659Z\"}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:55:27.332Z\", \"updated_at\": \"2026-05-23T00:38:42.757Z\", \"hypothesis\": \"70B ZS DocRED unconstrained 200-doc baseline to complete the ablation matrix. Expect DR~15% and R-F1~13 consistent with prior 99-doc measurement, providing matched-subset comparison for semantic_only (DR=1.66%) and grammar_only experiments.\", \"parent\": \"70b_docred_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 84588, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_unconstrained.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T00:38:42.757Z\"}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:24:11.190Z\", \"updated_at\": \"2026-05-23T00:37:43.935Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS DocRED will show minimal DR reduction (similar to SciERC 70B ZS pattern where grammar_only DR≈unconstrained), confirming that grammar layer's negligible contribution at 70B scale generalizes across datasets.\", \"parent\": \"r16_70b_docred_zs_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"eval_data\": \"DocRED dev 200-doc subset\", \"checkpoint_source\": \"n/a (zero-shot)\", \"log_path\": \"/tmp/70b_zs_docred_200_grammar_only.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T00:37:43.935Z\"}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:35:21.150Z\", \"updated_at\": \"2026-05-22T22:55:11.458Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS DocRED will significantly reduce DR violations from zero-shot baseline, demonstrating the semantic layer's effectiveness on document-level RE without fine-tuning.\", \"parent\": \"70b_docred_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:55:11.459Z\"}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:15:28.977Z\", \"updated_at\": \"2026-05-22T21:21:11.254Z\", \"hypothesis\": \"70B LoRA DocRED with beam search (k=4) + full_s1 on 200-doc subset will achieve DR=0% and CF≈0% while maintaining R-F1 comparable to greedy S1 (43.95), consistent with 8B beam search pattern.\", \"parent\": \"eval_70b_lora_docred_200_s1_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 70638, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\", \"log_path\": \"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\", \"note\": \"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\"}, \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:21:11.254Z\"}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:13:55.324Z\", \"updated_at\": \"2026-05-22T20:31:32.878Z\", \"hypothesis\": \"70B LoRA SciERC with grammar-only constrained decoding will reduce DR violations compared to unconstrained (DR=1.5%) but less than full_s1 (DR=0%), isolating grammar layer's independent contribution at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_grammar_only.log\", \"pid\": 70175}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}, \"completed_at\": \"2026-05-22T18:44:02.122Z\"}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:45:13.928Z\", \"updated_at\": \"2026-05-22T20:30:18.431Z\", \"hypothesis\": \"Independent 70B ZS SciERC unconstrained baseline to verify prior DR and R-F1 numbers from r16_70b_scierc_zs_s1 experiment. Expect DR~6-8% and R-F1~11 consistent with earlier measurements.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 74572, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_scierc_unconstrained.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}, \"completed_at\": \"2026-05-22T20:30:18.431Z\"}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:04:58.305Z\", \"updated_at\": \"2026-05-22T20:30:16.494Z\", \"hypothesis\": \"Full S2 constrained decoding on 70B LoRA SciERC achieves DR=0% like S1, with potentially fewer CF violations due to S2's enhanced cross-field consistency checking. R-F1 should be comparable to S1 (44.53-44.81).\", \"parent\": \"eval_70b_lora_scierc_s1_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 972139, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_full_s2.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}, \"completed_at\": \"2026-05-22T20:30:16.494Z\"}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:04:55.672Z\", \"updated_at\": \"2026-05-22T20:30:13.188Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA SciERC will reduce DR from 1.5% (unconstrained) toward 0%, consistent with the 70B ZS pattern where semantic layer is the primary DR reduction mechanism. Without grammar layer, some RV violations may appear.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 971668, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}, \"completed_at\": \"2026-05-22T20:30:13.188Z\"}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:48:40.066Z\", \"updated_at\": \"2026-05-22T18:16:23.650Z\", \"hypothesis\": \"Shuffling entity type order in the constraint schema (seed=42) does not significantly change constrained decoding results (R-F1 within ±0.5pp, violation rates identical), confirming that OntoCoDec is order-invariant. This addresses R19-W3 reviewer concern about entity registry ordering sensitivity.\", \"parent\": \"w5_lora_scierc_constrained_eval\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 967058, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/entity_order_shuffled_qwen_scierc.log\", \"shuffle_seed\": 42, \"original_entity_order\": [\"Task\", \"Method\", \"Material\", \"Metric\", \"OtherScientificTerm\", \"Generic\"], \"shuffled_entity_order\": [\"Metric\", \"Method\", \"Material\", \"OtherScientificTerm\", \"Task\", \"Generic\"], \"original_relation_order\": [\"Used-for\", \"Feature-of\", \"Hyponym-of\", \"Part-of\", \"Compare\", \"Conjunction\", \"Evaluate-for\"], \"shuffled_relation_order\": [\"Conjunction\", \"Evaluate-for\", \"Compare\", \"Part-of\", \"Feature-of\", \"Hyponym-of\", \"Used-for\"]}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}, \"completed_at\": \"2026-05-22T18:04:14.919Z\"}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:39:36.807Z\", \"updated_at\": \"2026-05-22T18:09:49.840Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS will reduce DR partially (similar to 8B pattern: ~24% reduction) without eliminating RV/ET, isolating semantic layer's independent contribution at 70B scale.\", \"parent\": \"r16_70b_scierc_zs_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"r16_70b_scierc_zs_s1\", \"eval_data\": \"scierc test set (551 docs)\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}, \"completed_at\": \"2026-05-22T18:09:49.840Z\"}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:39:44.901Z\", \"updated_at\": \"2026-05-22T18:09:48.056Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS reduce domain-range violations compared to unconstrained baseline (DR=6.41%) but less effectively than full_s1 (DR=0%), isolating grammar layer's contribution to constraint enforcement.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_grammar_only.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}, \"completed_at\": \"2026-05-22T18:09:48.056Z\"}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:39:43.218Z\", \"updated_at\": \"2026-05-22T18:04:29.880Z\", \"hypothesis\": \"70B LoRA fine-tuned model with beam search (k=4) and full_s1 constrained decoding on SciERC achieves DR=0% and CF=0%, matching 8B beam search behavior, while maintaining or improving extraction F1.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_beam4_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}, \"completed_at\": \"2026-05-22T18:04:29.880Z\"}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:48:16.222Z\", \"updated_at\": \"2026-05-22T16:27:25.157Z\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/beam4_tcr_llama_scierc.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}, \"conclusion\": \"negative\", \"hypothesis\": \"TCR reranking on beam4 outputs will change beam selection for LLaMA-SciERC by penalizing constraint-violating candidates, improving DR violation rate and overall F1 compared to vanilla beam4.\", \"completed_at\": \"2026-05-22T16:27:25.157Z\"}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:37:32.074Z\", \"updated_at\": \"2026-05-22T15:49:03.706Z\", \"hypothesis\": \"TCR (Type Consistency Reranking) with beam search (k=4) on Qwen3-8B LoRA SciERC will reduce domain/range violations compared to standard beam search by reranking candidates based on type consistency scores, while maintaining or improving Entity/Relation F1.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/beam_tcr_run.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T15:37:47.865Z\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}, \"parent\": \"d066_beam_sweep\"}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T13:29:07.493Z\", \"updated_at\": \"2026-05-22T13:30:06.224Z\", \"hypothesis\": \"vLLM's guided_json (JSON schema-constrained decoding) produces equivalent violation rates and F1 scores to our XGrammar grammar-only ablation, confirming that guided_json ≈ GCD (grammar-constrained decoding) without semantic constraints.\", \"spec\": {\"command\": \"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 0}, \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"log_path\": \"/tmp/vllm_guided_json_eval.log\", \"completed_at\": \"2026-05-22T13:30:06.224Z\"}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:47:05.464Z\", \"updated_at\": \"2026-05-22T10:34:22.854Z\", \"hypothesis\": \"70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve DR→0% while maintaining R-F1 comparable to unconstrained, confirming scale-independent constraint composability on DocRED at 70B scale\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": \"11466\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"200 (first 200 docs)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\", \"log_path\": \"westd-21461:/tmp/constrained_inference.log\"}, \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\", \"log_path\": \"westd-21461:/tmp/constrained_inference.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:34:01.646Z\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:44:23.637Z\", \"updated_at\": \"2026-05-22T10:34:14.027Z\", \"hypothesis\": \"Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\", \"spec\": {\"command\": \"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\", \"server\": \"westd-16980 + westd-21461\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"note\": \"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\"}, \"notes\": \"全部 8 配置完成 + eval 齐全。beam8 con: E-F1=66.36, R-F1=43.65, DR=0%, CF=0%, avg_time=5.058s。Pareto optimal: k=2 con (E-F1=67.71, R-F1=44.60, DR=0%)。k=8 相比 k=2 F1 下降 ~1.3pp 且推理慢 46%，收益递减明确。可入稿。\", \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}, \"conclusion\": \"success\", \"checkpoint_path\": \"parent experiment - see child experiments for individual outputs\", \"log_path\": \"parent experiment - see child experiments for individual logs\", \"completed_at\": \"2026-05-22T10:34:14.027Z\"}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.909Z\", \"updated_at\": \"2026-05-22T07:36:58.067Z\", \"hypothesis\": \"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"/tmp/w8_llama_docred_ft_grammar_only.log\", \"completed_at\": \"2026-05-16T12:31:33.933Z\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}, \"parent\": \"w5_llama_docred_lora_training\"}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:54:02.910Z\", \"updated_at\": \"2026-05-22T07:36:56.885Z\", \"hypothesis\": \"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\", \"parent\": \"w5_llama_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:49:59.199Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:50:01.253379+00:00\"}]}, \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"outputs/w8_llama_docred_ft_semantic_only.jsonl\", \"completed_at\": \"2026-05-16T16:55:22.088Z\"}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-22T07:36:54.996Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:18:27.113Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:18:29.130284+00:00\"}]}, \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:22:28.075Z\"}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:36.469Z\", \"updated_at\": \"2026-05-22T07:36:52.623Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen FT SciERC will show high DR (comparable to or worse than unconstrained), proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\"}, \"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:46.097Z\"}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:39.235Z\", \"updated_at\": \"2026-05-22T07:36:49.828Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama FT SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\"}, \"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:50.516Z\"}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:06:11.811Z\", \"updated_at\": \"2026-05-22T07:09:22.684Z\", \"hypothesis\": \"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale\", \"parent\": \"r16_70b_lora_docred\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\"run_constrained_extraction.py\\\", run_name=\\\"__main__\\\")'\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"998 (truncated to 200)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}, \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_unconstrained.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_unconstrained.log\", \"completed_at\": \"2026-05-22T07:09:22.684Z\"}, \"eval_70b_lora_scierc_s1_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:46:31.480Z\", \"updated_at\": \"2026-05-22T06:47:38.556Z\", \"hypothesis\": \"70B LoRA SciERC with Full S1 constrained decoding will achieve DR→0% while maintaining R-F1 comparable to unconstrained (44.73), confirming scale-independent constraint effectiveness at 70B with fine-tuning\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\"}, \"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:47:38.556Z\"}}, \"count\": 30, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7174}}"
    }
  },
  "sourceToolAssistantUUID": "2b42b33e-a151-43aa-b99e-d2b6a56476a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "leafUuid": "090f94ff-8ec3-40bf-a112-e44c822cf1fb",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "DocRED INT4 quantization comparison experiments",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Assistant

_source line 54 · 2026-05-23T05:48:31.123Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Both checkpoints exist. Now I need to:

1. Find the DocRED FP16 baseline results for 8B models
2. Check DocRED data files
3. Look at existing quantization scripts to adapt for DocRED

Let me search the registry for DocRED FP16 S1 constrained eval results for 8B models, and also check the DocRED data format.

From the registry results I can see:
- `w8_llama_docred_ft_grammar_only`: R_F1=43.72 (998 samples, grammar_only)


- `w8_llama_docred_ft_semantic_only`: R_F1=43.85 (998 samples, semantic_only)
- `w8_qwen_docred_ft_semantic_only`: R_F1=40.85 (998 samples, semantic_only)

But I need the full_s1 constrained baselines. Let me search for those. The parent experiments are `w5_llama_docred_lora_training` and `w5_qwen_docred_lora_training`. I should look for `w5_lora_docred_constrained_eval` or similar to find the baseline numbers I'm looking for.

I also need to figure out which DocRED data file to use—whether that's the full dev.json with 998 documents or a smaller 200-document subset—and make sure the dataset size matches what was used for the SciERC INT4 experiments, which had 551 samples from the full test set.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "090f94ff-8ec3-40bf-a112-e44c822cf1fb",
  "isSidechain": false,
  "requestId": "req_011CbJyUm1EmwC64B1TVGfyM",
  "type": "assistant",
  "uuid": "0062cfff-b5ac-42c4-8008-afdd8304b508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uN3G2zvYhss7nVN7U6PSD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24937,
      "cache_read_input_tokens": 41300,
      "output_tokens": 736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 736,
          "cache_read_input_tokens": 41300,
          "cache_creation_input_tokens": 24937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24937
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

_source line 55 · 2026-05-23T05:48:31.134Z_

需要找 DocRED 8B FP16 S1 baseline 和 DocRED 数据文件信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0062cfff-b5ac-42c4-8008-afdd8304b508",
  "isSidechain": false,
  "requestId": "req_011CbJyUm1EmwC64B1TVGfyM",
  "type": "assistant",
  "uuid": "7a70ae3e-6060-471d-a510-fdf20ff64e59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uN3G2zvYhss7nVN7U6PSD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24937,
      "cache_read_input_tokens": 41300,
      "output_tokens": 736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 736,
          "cache_read_input_tokens": 41300,
          "cache_creation_input_tokens": 24937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24937
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

_source line 56 · 2026-05-23T05:48:33.031Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01H7QuMX9omP89o2Pv4uSG5u`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "limit": 50,
  "fields": [
    "status",
    "metrics",
    "spec",
    "conclusion"
  ],
  "filters": {
    "status": "DONE"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a70ae3e-6060-471d-a510-fdf20ff64e59",
  "isSidechain": false,
  "requestId": "req_011CbJyUm1EmwC64B1TVGfyM",
  "type": "assistant",
  "uuid": "ccb78df5-3724-4849-b3ab-16d87078171e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uN3G2zvYhss7nVN7U6PSD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24937,
      "cache_read_input_tokens": 41300,
      "output_tokens": 736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 736,
          "cache_read_input_tokens": 41300,
          "cache_creation_input_tokens": 24937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24937
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

_source line 57 · 2026-05-23T05:48:33.782Z_

<details><summary>↩ Tool result · `toolu_01H7QuMX9omP89o2Pv4uSG5u`</summary>

```text
&lt;persisted-output>
Output too large (54.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bcaaae93-c135-4568-bb9e-6ae384bb4c94/tool-results/toolu_01H7QuMX9omP89o2Pv4uSG5u.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test (551 docs)\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}, \"conclusion\": \"success\"}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test 551 sentences\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}, \"conclusion\": \"success\"}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/golli
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccb78df5-3724-4849-b3ab-16d87078171e",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "979e3af4-f255-4a5f-bff5-8770aab40ac0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"sf2_llama_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-SciERC-FT-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\\\", \\\"eval_data\\\": \\\"SciERC test (551 docs)\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.94, \\\"R-F1\\\": 43.98, \\\"E-F1\\\": 67.54, \\\"samples\\\": 551, \\\"R-P\\\": 40.47, \\\"R-R\\\": 48.15, \\\"E-P\\\": 65.51, \\\"E-R\\\": 69.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sf2_qwen_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-SciERC-FT-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\\\", \\\"eval_data\\\": \\\"SciERC test 551 sentences\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 1.1, \\\"R-F1\\\": 41.71, \\\"E-F1\\\": 67.05, \\\"samples\\\": 551, \\\"R-P\\\": 38.52, \\\"R-R\\\": 45.48, \\\"E-P\\\": 64.76, \\\"E-R\\\": 69.52}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sf2_gollie_scierc_violation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"GoLLIE-7B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/gollie_model/\\\", \\\"eval_data\\\": \\\"SciERC test (100 docs)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gollie_model/\\\", \\\"log_path\\\": \\\"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\\\"}, \\\"metrics\\\": {\\\"GoLLIE_ZS\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.83, \\\"E_F1\\\": 9.17, \\\"R_F1\\\": 0, \\\"pred_ents\\\": 241, \\\"pred_rels\\\": 5, \\\"docs_with_output\\\": 54}, \\\"OntoCoDec_Qwen_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.61, \\\"E_F1\\\": 66.43, \\\"R_F1\\\": 43.69}, \\\"OntoCoDec_Llama_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.62, \\\"E_F1\\\": 67.09, \\\"R_F1\\\": 45.47}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_zs_docred_200_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 88678, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_full_s1.log\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 5.34, \\\"E-F1\\\": 70.05, \\\"R-F1\\\": 13.25, \\\"PF%\\\": 0, \\\"entities_pred\\\": 3234, \\\"relations_pred\\\": 2637, \\\"triples_checked\\\": 2642}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 984253, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_docred_200_grammar_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 10.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.38, \\\"CF_pct\\\": 0.06, \\\"E_F1\\\": 80.13, \\\"E_P\\\": 85.16, \\\"E_R\\\": 75.66, \\\"R_F1\\\": 43.96, \\\"R_P\\\": 39.78, \\\"R_R\\\": 49.11, \\\"entities_pred\\\": 3362, \\\"relations_pred\\\": 3154}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_70b_lora_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 983803, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_docred_200_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 11, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.51, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.21, \\\"E_F1\\\": 80.06, \\\"E_P\\\": 85.21, \\\"E_R\\\": 75.5, \\\"R_F1\\\": 43.61, \\\"R_P\\\": 39.44, \\\"R_R\\\": 48.75, \\\"entities_pred\\\": 3351, \\\"relations_pred\\\": 3148}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_zs_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 84588, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_unconstrained.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities_pred\\\": 3242, \\\"relations_pred\\\": 2637, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 7.88, \\\"DR_pct\\\": 13.45, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 8, \\\"E_F1\\\": 70.14, \\\"E_P\\\": 75.85, \\\"E_R\\\": 65.23, \\\"R_F1\\\": 13.25, \\\"R_P\\\": 12.97, \\\"R_R\\\": 13.54}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_zs_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"eval_data\\\": \\\"DocRED dev 200-doc subset\\\", \\\"checkpoint_source\\\": \\\"n/a (zero-shot)\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_grammar_only.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 1, \\\"entities_pred\\\": 3221, \\\"relations_pred\\\": 2609, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 17.03, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"E_F1\\\": 70.12, \\\"E_P\\\": 75.88, \\\"E_R\\\": 65.17, \\\"R_F1\\\": 13.23, \\\"R_P\\\": 12.99, \\\"R_R\\\": 13.47}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_70b_zs_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities\\\": 3240, \\\"relations\\\": 2596, \\\"ET_pct\\\": 0.12, \\\"RV_pct\\\": 8.24, \\\"DR_pct\\\": 1.66, \\\"CF_count\\\": 132, \\\"CF_pct\\\": 4.07, \\\"E_F1\\\": 70.1, \\\"E_P\\\": 75.87, \\\"E_R\\\": 65.15, \\\"R_F1\\\": 13.05, \\\"R_P\\\": 12.88, \\\"R_R\\\": 13.23, \\\"fuzzy_matches\\\": 8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\\\", \\\"pid\\\": 70638, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\\\", \\\"note\\\": \\\"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.57, \\\"E-P\\\": 85.45, \\\"E-R\\\": 85.68, \\\"R-F1\\\": 48.14, \\\"R-P\\\": 44.24, \\\"R-R\\\": 52.79, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"parse_fail\\\": \\\"1/200 (0.5%)\\\", \\\"entities_pred\\\": 3790, \\\"relations_pred\\\": 3030}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_grammar_only.log\\\", \\\"pid\\\": 70175}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"json_failure_rate\\\": 0, \\\"entities\\\": 1805, \\\"relations\\\": 1133, \\\"entity_type_violations\\\": 0, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocab_violations\\\": 0, \\\"relation_vocab_violation_rate\\\": 0, \\\"domain_range_violations\\\": 17, \\\"domain_range_violation_rate\\\": 0.015, \\\"cross_field_consistency_violations\\\": 0, \\\"fuzzy_relation_matches\\\": 0, \\\"entity_P\\\": 0.6272, \\\"entity_R\\\": 0.6707, \\\"entity_F1\\\": 0.6482, \\\"relation_P\\\": 0.4152, \\\"relation_R\\\": 0.4825, \\\"relation_F1\\\": 0.4463}}, \\\"eval_70b_zs_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\\\", \\\"pid\\\": 74572, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_scierc_unconstrained.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 2353, \\\"relations\\\": 1483, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.6, \\\"DR_pct\\\": 6.4, \\\"CF_count\\\": 0, \\\"E_F1\\\": 35.22, \\\"E_P\\\": 30.13, \\\"E_R\\\": 42.38, \\\"R_F1\\\": 11.23, \\\"R_P\\\": 9.31, \\\"R_R\\\": 14.17, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_full_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 972139, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_full_s2.log\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1531, \\\"relations\\\": 1027, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 18, \\\"E_F1\\\": 62.35, \\\"E_P\\\": 65.44, \\\"E_R\\\": 59.53, \\\"R_F1\\\": 36.28, \\\"R_P\\\": 35.35, \\\"R_R\\\": 37.27, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 971668, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_semantic_only.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1806, \\\"relations\\\": 1133, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.6, \\\"CF_count\\\": 9, \\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"parse_fail_pct\\\": 0}}, \\\"entity_order_ablation_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 967058, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-LoRA-SciERC-merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"log_path\\\": \\\"/tmp/entity_order_shuffled_qwen_scierc.log\\\", \\\"shuffle_seed\\\": 42, \\\"original_entity_order\\\": [\\\"Task\\\", \\\"Method\\\", \\\"Material\\\", \\\"Metric\\\", \\\"OtherScientificTerm\\\", \\\"Generic\\\"], \\\"shuffled_entity_order\\\": [\\\"Metric\\\", \\\"Method\\\", \\\"Material\\\", \\\"OtherScientificTerm\\\", \\\"Task\\\", \\\"Generic\\\"], \\\"original_relation_order\\\": [\\\"Used-for\\\", \\\"Feature-of\\\", \\\"Hyponym-of\\\", \\\"Part-of\\\", \\\"Compare\\\", \\\"Conjunction\\\", \\\"Evaluate-for\\\"], \\\"shuffled_relation_order\\\": [\\\"Conjunction\\\", \\\"Evaluate-for\\\", \\\"Compare\\\", \\\"Part-of\\\", \\\"Feature-of\\\", \\\"Hyponym-of\\\", \\\"Used-for\\\"]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 67.05, \\\"E_P\\\": 65.23, \\\"E_R\\\": 68.98, \\\"R_F1\\\": 43.77, \\\"R_P\\\": 40.78, \\\"R_R\\\": 47.23, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 21, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1784, \\\"relations\\\": 1128, \\\"corrected_original_R_F1\\\": 43.77, \\\"corrected_original_E_F1\\\": 67.05, \\\"corrected_original_DR_pct\\\": 0, \\\"corrected_original_CF_count\\\": 21, \\\"corrected_delta_R_F1\\\": 0, \\\"corrected_delta_E_F1\\\": 0, \\\"raw_output_identical\\\": true, \\\"parsed_output_identical\\\": true, \\\"note\\\": \\\"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\\\"}}, \\\"eval_70b_zs_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"r16_70b_scierc_zs_s1\\\", \\\"eval_data\\\": \\\"scierc test set (551 docs)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/eval_70b_zs_scierc_semantic_only.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.37, \\\"DR_pct\\\": 1.01, \\\"RV_pct\\\": 0.6, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 76, \\\"samples\\\": 551}}, \\\"eval_70b_zs_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/eval_70b_zs_scierc_grammar_only.log\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.23, \\\"DR_pct\\\": 6.33, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 0, \\\"samples\\\": 551}}, \\\"eval_70b_lora_scierc_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_beam4_s1.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 64.89, \\\"E_P\\\": 62.29, \\\"E_R\\\": 67.72, \\\"R_F1\\\": 44.81, \\\"R_P\\\": 39.45, \\\"R_R\\\": 51.85, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 1, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1839, \\\"relations\\\": 1283}}, \\\"tcr_beam4_llama_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/beam4_tcr_llama_scierc.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1803, \\\"relations\\\": 1194, \\\"entity_type_violations\\\": \\\"0/1803 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1194 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"13/1194 (1.1%)\\\", \\\"cross_field_consistency\\\": 0, \\\"DR_pct\\\": 1.09, \\\"E_F1\\\": 68.02, \\\"E_P\\\": 65.88, \\\"E_R\\\": 70.29, \\\"R_F1\\\": 46.05, \\\"R_P\\\": 41.83, \\\"R_R\\\": 51.23, \\\"tcr_changed_selection\\\": \\\"0/551 (0.0%)\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"tcr_beam4_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-LoRA-SciERC-merged\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"log_path\\\": \\\"/tmp/beam_tcr_run.log\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1802, \\\"relations\\\": 1250, \\\"entity_type_violations\\\": \\\"0/1802 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1250 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"23/1250 (1.8%)\\\", \\\"cross_field_consistency_violations\\\": 1, \\\"DR_pct\\\": 1.84, \\\"E_P\\\": 65.05, \\\"E_R\\\": 69.64, \\\"E_F1\\\": 67.26, \\\"R_P\\\": 39.36, \\\"R_R\\\": 50.51, \\\"R_F1\\\": 44.24, \\\"TCR_changed_selection\\\": \\\"0/551 (0.0%)\\\", \\\"all_candidates_TCR_1.0\\\": true}}, \\\"vllm_guided_json_scierc_zs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B\\\", \\\"seed\\\": 0}, \\\"metrics\\\": {\\\"DR%\\\": 15.26, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.04, \\\"R-F1\\\": 8.75, \\\"E-F1\\\": 30.91, \\\"parse_fail%\\\": 0, \\\"total_samples\\\": 551, \\\"total_entities\\\": 2485, \\\"total_relations\\\": 1724, \\\"inference_time_s\\\": 108.5}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"11466\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": \\\"200 (first 200 docs)\\\", \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/tmp/constrained_inference.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 79.38, \\\"E_P\\\": 85.24, \\\"E_R\\\": 74.28, \\\"R_F1\\\": 43.95, \\\"R_P\\\": 40.48, \\\"R_R\\\": 48.08, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.18, \\\"parse_fail_pct\\\": 12.5, \\\"samples\\\": 200}}, \\\"d066_beam_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\\\", \\\"server\\\": \\\"westd-16980 + westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"note\\\": \\\"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\\\"}, \\\"metrics\\\": {\\\"scierc_qwen3_8b\\\": {\\\"k1_unc\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 2.11, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.494}, \\\"k1_con\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.5, \\\"avg_time\\\": 2.932}, \\\"k2_unc\\\": {\\\"E_F1\\\": 67.79, \\\"R_F1\\\": 44.75, \\\"DR_pct\\\": 1.54, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.954}, \\\"k2_con\\\": {\\\"E_F1\\\": 67.71, \\\"R_F1\\\": 44.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.11, \\\"avg_time\\\": 3.463}, \\\"k4_unc\\\": {\\\"E_F1\\\": 67.49, \\\"R_F1\\\": 43.72, \\\"DR_pct\\\": 1.89, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 3.485}, \\\"k4_con\\\": {\\\"E_F1\\\": 67.22, \\\"R_F1\\\": 43.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.069}, \\\"k8_unc\\\": {\\\"E_F1\\\": 66.4, \\\"R_F1\\\": 43.17, \\\"DR_pct\\\": 1.77, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.194}, \\\"k8_con\\\": {\\\"E_F1\\\": 66.36, \\\"R_F1\\\": 43.65, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 5.058}}, \\\"pareto_optimal\\\": \\\"k=2 con\\\", \\\"best_E_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 67.79}, \\\"best_R_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 44.75}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"w8_llama_docred_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"llama_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"w5_llama_docred_lora\\\", \\\"eval_data\\\": \\\"docred_dev_998\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"R_F1\\\": 43.72, \\\"R_P\\\": 38.57, \\\"R_R\\\": 50.44, \\\"parse_fail_pct\\\": 2.3, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\\\"}}, \\\"w8_llama_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\\\\\"\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": 1, \\\"pid\\\": 361202, \\\"model_name\\\": \\\"Llama-3.1-8B-LoRA-DocRED\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 43.85, \\\"R_P\\\": 38.85, \\\"R_R\\\": 50.31, \\\"parse_fail_pct\\\": 2.4, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"w8_qwen_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"qwen_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"qwen_lora_docred_merged\\\", \\\"eval_data\\\": \\\"docred_test_998\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"log_path\\\": \\\"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 40.85, \\\"R_P\\\": 36.33, \\\"R_R\\\": 46.65, \\\"parse_fail_pct\\\": 7.52, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_qwen_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B (fine-tuned)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 64.4, \\\"E_P\\\": 66.8, \\\"E_R\\\": 62.16, \\\"R_F1\\\": 41.16, \\\"R_P\\\": 38.24, \\\"R_R\\\": 44.56, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 95.5, \\\"CF_pct\\\": 0.09, \\\"parse_fail_pct\\\": 9.1, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_llama_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (fine-tuned)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 36.66, \\\"E_P\\\": 67.47, \\\"E_R\\\": 25.16, \\\"R_F1\\\": 19.95, \\\"R_P\\\": 41.42, \\\"R_R\\\": 13.14, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 15.2, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 50.8, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\\\\\"run_constrained_extraction.py\\\\\\\", run_name=\\\\\\\"__main__\\\\\\\")'\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": \\\"998 (truncated to 200)\\\", \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 80.34, \\\"E_P\\\": 85.13, \\\"E_R\\\": 76.05, \\\"R_F1\\\": 43.8, \\\"R_P\\\": 39.6, \\\"R_R\\\": 48.99, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.57, \\\"DR_pct\\\": 0.22, \\\"CF_pct\\\": 0.06, \\\"parse_fail_pct\\\": 10, \\\"samples\\\": 200, \\\"relations\\\": 3159, \\\"RV_count\\\": 18, \\\"DR_count\\\": 7, \\\"CF_count\\\": 2}}, \\\"eval_70b_lora_scierc_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\\\"}, \\\"metrics\\\": {\\\"entity_f1\\\": 0.6476, \\\"entity_precision\\\": 0.6266, \\\"entity_recall\\\": 0.6701, \\\"relation_f1\\\": 0.4453, \\\"relation_precision\\\": 0.4149, \\\"relation_recall\\\": 0.4805, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 15, \\\"parse_fail_pct\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"num_samples\\\": 551, \\\"num_entities\\\": 1805, \\\"num_relations\\\": 1129}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"scierc test (551 sentences)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 1.5, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1806, \\\"relations\\\": 1133}}, \\\"r16_70b_docred_zs_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"model_path\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 69.11, \\\"R_F1\\\": 13.05, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.04, \\\"parse_fail_pct\\\": 0.1, \\\"samples\\\": 998, \\\"total_entities\\\": 16599, \\\"total_triples\\\": 13239, \\\"baseline_unc_DR_pct\\\": 14.98, \\\"baseline_unc_R_F1\\\": 13.01, \\\"note\\\": \\\"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\\\"}}, \\\"d066_sweep_llama_beam8_unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --output_file /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\\\", \\\"server\\\": \\\"westd-16980 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 755444. Relay from Llama beam2 s1 (success).\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam8_unc.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 85.77, \\\"E_P\\\": 85.7, \\\"E_R\\\": 85.84, \\\"R_F1\\\": 51.97, \\\"R_P\\\": 49.76, \\\"R_R\\\": 54.38, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.05, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.07, \\\"parse_fail_pct\\\": 0.5, \\\"total_samples\\\": 200, \\\"total_entities_pred\\\": 3788, \\\"total_relations_pred\\\": 2779}}, \\\"d066_sweep_llama_beam2_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --max_samples 200 --seed 42\\\", \\\"server\\\": \\\"westd-16980 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 750801. Relay from Llama beam2 unc (success).\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam2_full_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam2_s1.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 85.6, \\\"E_P\\\": 85.29, \\\"E_R\\\": 85.92, \\\"R_F1\\\": 51.17, \\\"R_P\\\": 48.51, \\\"R_R\\\": 54.14, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"parse_fail_pct\\\": 0.5, \\\"total_samples\\\": 200, \\\"total_entities_pred\\\": 3814, \\\"total_relations_pred\\\": 2839}}, \\\"d066_sweep_llama_docred_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_constrained.jsonl\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam4_s1.log\\\", \\\"metrics\\\": {\\\"E-F1\\\": 85.61, \\\"E-P\\\": 85.48, \\\"E-R\\\": 85.73, \\\"R-F1\\\": 51.89, \\\"R-P\\\": 51.59, \\\"R-R\\\": 52.2, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"PF%\\\": 0.5, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"samples\\\": 200, \\\"parse_fail\\\": 1}, \\\"command\\\": \\\"d066 beam sweep llama docred beam4 s1 (completed, retroactive fix)\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct + LoRA\\\", \\\"seed\\\": 42}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E-F1\\\": 85.61, \\\"E-P\\\": 85.48, \\\"E-R\\\": 85.73, \\\"R-F1\\\": 51.89, \\\"R-P\\\": 51.59, \\\"R-R\\\": 52.2, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"samples\\\": 200, \\\"parse_fail\\\": 1}}, \\\"r16_70b_lora_docred\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 scripts/train_lora_70b_docred.py\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/sft_train_llama.jsonl\\\", \\\"data_count\\\": 3053, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/train.log\\\", \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/sft_dev_llama.jsonl\\\", \\\"pid\\\": 839375, \\\"gpu_ids\\\": [1], \\\"note\\\": \\\"Restarted from scratch (previous run killed, empty checkpoint dir). LoRA r=16 alpha=32 on q/k/v/o_proj. bs=1 grad_accum=8 lr=2e-5 3epochs. ~10.4h ETA.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_loss\\\": 0.0635, \\\"token_acc\\\": 97.94, \\\"steps_completed\\\": 1146, \\\"epochs\\\": 3, \\\"train_loss_start\\\": 0.147, \\\"train_loss_end\\\": 0.056}}, \\\"r16_70b_lora_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 train_70b_lora.py --dataset scierc --model_path /root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ-INT4 --output_dir /root/autodl-tmp/checkpoints/70b_lora_scierc --epochs 3 --lr 2e-4 --lora_r 16 --lora_alpha 32\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/sft/scierc_sft_train.jsonl\\\", \\\"data_count\\\": 1762, \\\"model_name\\\": \\\"Llama-3.3-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/train.log\\\", \\\"pid\\\": 836206, \\\"gpu_ids\\\": [0, 1]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_loss\\\": 0.0611, \\\"token_acc\\\": 97.78, \\\"steps_completed\\\": 663, \\\"epochs\\\": 3, \\\"train_loss_start\\\": 0.183, \\\"train_loss_end\\\": 0.041}}, \\\"r16_70b_scierc_zs_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 808988, \\\"data_path\\\": \\\"SciERC test set (551 sentences)\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"model_path\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (ZS eval)\\\", \\\"log_path\\\": \\\"/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 35.19, \\\"R_F1\\\": 11.24, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 3.5, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"baseline_unc_E_F1\\\": 35.21, \\\"baseline_unc_R_F1\\\": 11.15, \\\"baseline_unc_DR_pct\\\": 6.41, \\\"baseline_unc_RV_pct\\\": 0.61, \\\"baseline_unc_CF_pct\\\": 0}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r14_qwen_docred_beam4_998\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl --device cuda:0 --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Qwen3-8B (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 58.19, \\\"R_F1\\\": 8.72, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 4.94, \\\"parse_fail_pct\\\": 3.51, \\\"samples\\\": 998, \\\"success\\\": 963, \\\"fail\\\": 35}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_llama_zs_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama ZS)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_llama_zs.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 23.23, \\\"R_F1\\\": 2.9, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 84.4, \\\"CF_pct\\\": 0.36, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_qwen_zs_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen ZS)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_qwen_zs.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 30.97, \\\"R_F1\\\": 8.64, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 29.3, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r14_llama_docred_beam4_998\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --output_path /root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.jsonl --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"R_F1\\\": 8.83, \\\"E_F1\\\": 57.81, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 1, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"parse_fail_pct\\\": 3.91, \\\"samples\\\": 998, \\\"success\\\": 959, \\\"fail\\\": 39, \\\"baseline_ZS_greedy_R_F1\\\": 6.27, \\\"baseline_ZS_greedy_E_F1\\\": 54.93, \\\"baseline_ZS_greedy_DR_pct\\\": 2.55, \\\"baseline_ZS_greedy_CF_pct\\\": 8.54}}, \\\"d066_sweep_llama_scierc_beam8_s1_551\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam8_full_s1.jsonl\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"llama_lora_scierc_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"scierc test set (551 sentences)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E-F1\\\": 67.51, \\\"E-P\\\": 64.99, \\\"E-R\\\": 70.23, \\\"R-F1\\\": 44.95, \\\"R-P\\\": 40.1, \\\"R-R\\\": 51.13, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0, \\\"samples\\\": 551, \\\"note\\\": \\\"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\\\"}}, \\\"d066_sweep_llama_scierc_beam4_s1_551\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E-F1\\\": 68.06, \\\"E-P\\\": 65.96, \\\"E-R\\\": 70.29, \\\"R-F1\\\": 46.18, \\\"R-P\\\": 42.1, \\\"R-R\\\": 51.13, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"parse_fail\\\": 0, \\\"samples\\\": 551, \\\"note\\\": \\\"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"llama_lora_scierc_merged\\\", \\\"seed\\\": 42}}, \\\"d066_sweep_llama_docred_beam4_unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_unconstrained.jsonl\\\", \\\"server\\\": \\\"westd-16980 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 761033. Relay from Llama beam8 unc (success).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.67, \\\"R-F1\\\": 52.65, \\\"DR_pct\\\": 0.04, \\\"CF_pct\\\": 0.08, \\\"PF_pct\\\": 0.5, \\\"samples\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d066_sweep_llama_docred_beam1_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\\\", \\\"server\\\": \\\"westd-21461 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 209444. Relay from beam1 unc (success).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.43, \\\"R-F1\\\": 47.35, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.19, \\\"PF_pct\\\": 2, \\\"samples\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d066_sweep_llama_beam8_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\\\", \\\"server\\\": \\\"westd-16980 GPU0\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 756540. Relay after GPU0 freed.\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.76, \\\"R-F1\\\": 51.74, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0.5, \\\"samples\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d065_qwen_greedy_4096_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --decoding_strategy greedy --max_new_tokens 4096 --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --output_file /root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096_rerun.jsonl --seed 42\\\", \\\"server\\\": \\\"westd-21461 GPU0\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Qwen3-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (998 docs, constrained decoding inference)\\\", \\\"note\\\": \\\"Rerun after dual-process corruption. PID 194615.\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 81.87, \\\"R-F1\\\": 40.79, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.22, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"PF_pct\\\": 8.52, \\\"samples\\\": 998}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d066_sweep_llama_scierc_beam2_s1_551\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"llama_lora_scierc_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"scierc test set (551 sentences)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entity_f1\\\": 68.34, \\\"entity_p\\\": 66.59, \\\"entity_r\\\": 70.17, \\\"relation_f1\\\": 46.12, \\\"relation_p\\\": 42.73, \\\"relation_r\\\": 50.1, \\\"parse_fail_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.17, \\\"note\\\": \\\"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\\\"}}, \\\"d066_sweep_llama_scierc_beam1_unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-21461 GPU1\\\", \\\"data_path\\\": \\\"data/scierc/test.json (551 docs)\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA SciERC (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"data/scierc/test.json\\\", \\\"note\\\": \\\"PID 205314. Relay from Qwen beam8 s1 SciERC (success).\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unconstrained.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unc.log\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"total\\\": 275, \\\"success\\\": 275, \\\"fail\\\": 0, \\\"output_file\\\": \\\"llama_scierc_beam1_unconstrained.jsonl\\\", \\\"note\\\": \\\"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\\\"}}}, \\\"count\\\": 50, \\\"total\\\": 158, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4881}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test (551 docs)\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}, \"conclusion\": \"success\"}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test 551 sentences\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}, \"conclusion\": \"success\"}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 100, \"model_name\": \"GoLLIE-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/gollie_model/\", \"eval_data\": \"SciERC test (100 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/gollie_model/\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\"}, \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 88678, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_full_s1.log\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 984253, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_grammar_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}, \"conclusion\": \"negative\"}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 983803, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 84588, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_unconstrained.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"eval_data\": \"DocRED dev 200-doc subset\", \"checkpoint_source\": \"n/a (zero-shot)\", \"log_path\": \"/tmp/70b_zs_docred_200_grammar_only.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}, \"conclusion\": \"negative\"}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 70638, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\", \"log_path\": \"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\", \"note\": \"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\"}, \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}, \"conclusion\": \"success\"}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_grammar_only.log\", \"pid\": 70175}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 74572, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_scierc_unconstrained.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 972139, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_full_s2.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 971668, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 967058, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/entity_order_shuffled_qwen_scierc.log\", \"shuffle_seed\": 42, \"original_entity_order\": [\"Task\", \"Method\", \"Material\", \"Metric\", \"OtherScientificTerm\", \"Generic\"], \"shuffled_entity_order\": [\"Metric\", \"Method\", \"Material\", \"OtherScientificTerm\", \"Task\", \"Generic\"], \"original_relation_order\": [\"Used-for\", \"Feature-of\", \"Hyponym-of\", \"Part-of\", \"Compare\", \"Conjunction\", \"Evaluate-for\"], \"shuffled_relation_order\": [\"Conjunction\", \"Evaluate-for\", \"Compare\", \"Part-of\", \"Feature-of\", \"Hyponym-of\", \"Used-for\"]}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"r16_70b_scierc_zs_s1\", \"eval_data\": \"scierc test set (551 docs)\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_grammar_only.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_beam4_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/beam4_tcr_llama_scierc.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}, \"conclusion\": \"negative\"}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/beam_tcr_run.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 0}, \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": \"11466\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"200 (first 200 docs)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\", \"log_path\": \"westd-21461:/tmp/constrained_inference.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"spec\": {\"command\": \"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\", \"server\": \"westd-16980 + westd-21461\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"note\": \"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\"}, \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}, \"conclusion\": \"success\"}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}, \"conclusion\": \"success\"}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}, \"conclusion\": \"success\"}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\"}, \"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}, \"conclusion\": \"success\"}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\"}, \"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\"run_constrained_extraction.py\\\", run_name=\\\"__main__\\\")'\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"998 (truncated to 200)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}}, \"eval_70b_lora_scierc_s1_constrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\"}, \"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}, \"conclusion\": \"success\"}, \"eval_70b_lora_scierc_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"scierc test (551 sentences)\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.5, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1806, \"relations\": 1133}}, \"r16_70b_docred_zs_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 69.11, \"R_F1\": 13.05, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.04, \"parse_fail_pct\": 0.1, \"samples\": 998, \"total_entities\": 16599, \"total_triples\": 13239, \"baseline_unc_DR_pct\": 14.98, \"baseline_unc_R_F1\": 13.01, \"note\": \"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\"}}, \"d066_sweep_llama_beam8_unc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --output_file /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 755444. Relay from Llama beam2 s1 (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam8_unc.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.77, \"E_P\": 85.7, \"E_R\": 85.84, \"R_F1\": 51.97, \"R_P\": 49.76, \"R_R\": 54.38, \"DR_pct\": 0, \"CF_pct\": 0.05, \"ET_pct\": 0, \"RV_pct\": 0.07, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3788, \"total_relations_pred\": 2779}}, \"d066_sweep_llama_beam2_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --max_samples 200 --seed 42\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 750801. Relay from Llama beam2 unc (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam2_full_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam2_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.6, \"E_P\": 85.29, \"E_R\": 85.92, \"R_F1\": 51.17, \"R_P\": 48.51, \"R_R\": 54.14, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3814, \"total_relations_pred\": 2839}}, \"d066_sweep_llama_docred_beam4_s1\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_constrained.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam4_s1.log\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR%\": 0, \"CF%\": 0, \"PF%\": 0.5, \"ET%\": 0, \"RV%\": 0, \"samples\": 200, \"parse_fail\": 1}, \"command\": \"d066 beam sweep llama docred beam4 s1 (completed, retroactive fix)\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B-Instruct + LoRA\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"ET_pct\": 0, \"RV_pct\": 0, \"samples\": 200, \"parse_fail\": 1}}, \"r16_70b_lora_docred\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 scripts/train_lora_70b_docred.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/sft_train_llama.jsonl\", \"data_count\": 3053, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/train.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"/root/schema_semantic_constrained_ie/data/docred/sft_dev_llama.jsonl\", \"pid\": 839375, \"gpu_ids\": [1], \"note\": \"Restarted from scratch (previous run killed, empty checkpoint dir). LoRA r=16 alpha=32 on q/k/v/o_proj. bs=1 grad_accum=8 lr=2e-5 3epochs. ~10.4h ETA.\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0635, \"token_acc\": 97.94, \"steps_completed\": 1146, \"epochs\": 3, \"train_loss_start\": 0.147, \"train_loss_end\": 0.056}}, \"r16_70b_lora_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 train_70b_lora.py --dataset scierc --model_path /root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ-INT4 --output_dir /root/autodl-tmp/checkpoints/70b_lora_scierc --epochs 3 --lr 2e-4 --lora_r 16 --lora_alpha 32\", \"server\": \"westd-16980\", \"data_path\": \"data/sft/scierc_sft_train.jsonl\", \"data_count\": 1762, \"model_name\": \"Llama-3.3-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/train.log\", \"pid\": 836206, \"gpu_ids\": [0, 1]}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0611, \"token_acc\": 97.78, \"steps_completed\": 663, \"epochs\": 3, \"train_loss_start\": 0.183, \"train_loss_end\": 0.041}}, \"r16_70b_scierc_zs_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 808988, \"data_path\": \"SciERC test set (551 sentences)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A (ZS eval)\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log\"}, \"metrics\": {\"E_F1\": 35.19, \"R_F1\": 11.24, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 3.5, \"parse_fail_pct\": 0, \"samples\": 551, \"baseline_unc_E_F1\": 35.21, \"baseline_unc_R_F1\": 11.15, \"baseline_unc_DR_pct\": 6.41, \"baseline_unc_RV_pct\": 0.61, \"baseline_unc_CF_pct\": 0}, \"conclusion\": \"success\"}, \"r14_qwen_docred_beam4_998\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl --device cuda:0 --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"E_F1\": 58.19, \"R_F1\": 8.72, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 4.94, \"parse_fail_pct\": 3.51, \"samples\": 998, \"success\": 963, \"fail\": 35}, \"conclusion\": \"success\"}, \"r16_trie_llama_zs_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_zs.log\"}, \"metrics\": {\"E_F1\": 23.23, \"R_F1\": 2.9, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 84.4, \"CF_pct\": 0.36, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\"}, \"r16_trie_qwen_zs_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_zs.log\"}, \"metrics\": {\"E_F1\": 30.97, \"R_F1\": 8.64, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 29.3, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\"}, \"r14_llama_docred_beam4_998\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --output_path /root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.jsonl --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.log\"}, \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 8.83, \"E_F1\": 57.81, \"DR_pct\": 0, \"CF_pct\": 1, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 3.91, \"samples\": 998, \"success\": 959, \"fail\": 39, \"baseline_ZS_greedy_R_F1\": 6.27, \"baseline_ZS_greedy_E_F1\": 54.93, \"baseline_ZS_greedy_DR_pct\": 2.55, \"baseline_ZS_greedy_CF_pct\": 8.54}}, \"d066_sweep_llama_scierc_beam8_s1_551\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam8_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 67.51, \"E-P\": 64.99, \"E-R\": 70.23, \"R-F1\": 44.95, \"R-P\": 40.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0, \"samples\": 551, \"note\": \"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\"}}, \"d066_sweep_llama_scierc_beam4_s1_551\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 68.06, \"E-P\": 65.96, \"E-R\": 70.29, \"R-F1\": 46.18, \"R-P\": 42.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"parse_fail\": 0, \"samples\": 551, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42}}, \"d066_sweep_llama_docred_beam4_unc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 761033. Relay from Llama beam8 unc (success).\"}, \"metrics\": {\"E-F1\": 85.67, \"R-F1\": 52.65, \"DR_pct\": 0.04, \"CF_pct\": 0.08, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\"}, \"d066_sweep_llama_docred_beam1_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 209444. Relay from beam1 unc (success).\"}, \"metrics\": {\"E-F1\": 85.43, \"R-F1\": 47.35, \"DR_pct\": 0, \"CF_pct\": 0.19, \"PF_pct\": 2, \"samples\": 200}, \"conclusion\": \"success\"}, \"d066_sweep_llama_beam8_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-16980 GPU0\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 756540. Relay after GPU0 freed.\"}, \"metrics\": {\"E-F1\": 85.76, \"R-F1\": 51.74, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\"}, \"d065_qwen_greedy_4096_r2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --decoding_strategy greedy --max_new_tokens 4096 --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --output_file /root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096_rerun.jsonl --seed 42\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (998 docs, constrained decoding inference)\", \"note\": \"Rerun after dual-process corruption. PID 194615.\"}, \"metrics\": {\"E-F1\": 81.87, \"R-F1\": 40.79, \"DR_pct\": 0, \"CF_pct\": 0.22, \"ET_pct\": 0, \"RV_pct\": 0, \"PF_pct\": 8.52, \"samples\": 998}, \"conclusion\": \"success\"}, \"d066_sweep_llama_scierc_beam2_s1_551\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"conclusion\": \"success\", \"metrics\": {\"entity_f1\": 68.34, \"entity_p\": 66.59, \"entity_r\": 70.17, \"relation_f1\": 46.12, \"relation_p\": 42.73, \"relation_r\": 50.1, \"parse_fail_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.17, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}}, \"d066_sweep_llama_scierc_beam1_unc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --seed 42\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/scierc/test.json (551 docs)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B LoRA SciERC (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/scierc/test.json\", \"note\": \"PID 205314. Relay from Qwen beam8 s1 SciERC (success).\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unconstrained.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unc.log\"}, \"conclusion\": \"failed\", \"metrics\": {\"total\": 275, \"success\": 275, \"fail\": 0, \"output_file\": \"llama_scierc_beam1_unconstrained.jsonl\", \"note\": \"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\"}}}, \"count\": 50, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4881}}"
    }
  },
  "sourceToolAssistantUUID": "ccb78df5-3724-4849-b3ab-16d87078171e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-23T05:48:34.036Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013P4ASSdqa7tf3MjdGaNczd`</summary>

```json
{
  "server": "westd-16980",
  "command": "ls -la /root/schema_semantic_constrained_ie/data/docred/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "979e3af4-f255-4a5f-bff5-8770aab40ac0",
  "isSidechain": false,
  "requestId": "req_011CbJyUm1EmwC64B1TVGfyM",
  "type": "assistant",
  "uuid": "2f89a17a-d57d-4e1f-9268-c33e7a13530c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uN3G2zvYhss7nVN7U6PSD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24937,
      "cache_read_input_tokens": 41300,
      "output_tokens": 736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 736,
          "cache_read_input_tokens": 41300,
          "cache_creation_input_tokens": 24937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24937
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

_source line 59 · 2026-05-23T05:48:34.258Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016VSbU5cFdc26qGP3fq2kjB`</summary>

```json
{
  "server": "westd-16980",
  "command": "head -5 /root/schema_semantic_constrained_ie/data/docred/dev.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f89a17a-d57d-4e1f-9268-c33e7a13530c",
  "isSidechain": false,
  "requestId": "req_011CbJyUm1EmwC64B1TVGfyM",
  "type": "assistant",
  "uuid": "4c877fd2-a296-4377-ac39-dbdf34353070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uN3G2zvYhss7nVN7U6PSD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24937,
      "cache_read_input_tokens": 41300,
      "output_tokens": 736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 736,
          "cache_read_input_tokens": 41300,
          "cache_creation_input_tokens": 24937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24937
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

_source line 60_

```json
{
  "type": "last-prompt",
  "leafUuid": "4c877fd2-a296-4377-ac39-dbdf34353070",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "DocRED INT4 quantization comparison experiments",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Tool result

_source line 62 · 2026-05-23T05:48:34.492Z_

<details><summary>↩ Tool result · `toolu_013P4ASSdqa7tf3MjdGaNczd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 66716\\ndrwxr-xr-x 3 root root     4096 May 16 02:09 .\\ndrwxr-xr-x 9 root root      145 May 19 12:16 ..\\ndrwxr-xr-x 3 root root       33 May 14 01:42 .cache\\n-rw-r--r-- 1 root root  4287303 May 14 01:43 dev.json\\n-rw-r--r-- 1 root root    63528 May 14 01:47 ontology_constraints_docred.json\\n-rw-r--r-- 1 root root     2452 May 14 01:43 rel_info.json\\n-rw-r--r-- 1 root root  6186654 May 16 01:51 sft_dev.jsonl\\n-rw-r--r-- 1 root root  6352322 May 16 02:09 sft_dev_llama.jsonl\\n-rw-r--r-- 1 root root 18933693 May 16 01:51 sft_train.jsonl\\n-rw-r--r-- 1 root root 19440491 May 16 02:09 sft_train_llama.jsonl\\n-rw-r--r-- 1 root root 13029595 May 14 01:43 train_annotated.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f89a17a-d57d-4e1f-9268-c33e7a13530c",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "a5a40337-8f75-4848-ab41-2c078248654f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 66716\\\\ndrwxr-xr-x 3 root root     4096 May 16 02:09 .\\\\ndrwxr-xr-x 9 root root      145 May 19 12:16 ..\\\\ndrwxr-xr-x 3 root root       33 May 14 01:42 .cache\\\\n-rw-r--r-- 1 root root  4287303 May 14 01:43 dev.json\\\\n-rw-r--r-- 1 root root    63528 May 14 01:47 ontology_constraints_docred.json\\\\n-rw-r--r-- 1 root root     2452 May 14 01:43 rel_info.json\\\\n-rw-r--r-- 1 root root  6186654 May 16 01:51 sft_dev.jsonl\\\\n-rw-r--r-- 1 root root  6352322 May 16 02:09 sft_dev_llama.jsonl\\\\n-rw-r--r-- 1 root root 18933693 May 16 01:51 sft_train.jsonl\\\\n-rw-r--r-- 1 root root 19440491 May 16 02:09 sft_train_llama.jsonl\\\\n-rw-r--r-- 1 root root 13029595 May 14 01:43 train_annotated.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 66716\\ndrwxr-xr-x 3 root root     4096 May 16 02:09 .\\ndrwxr-xr-x 9 root root      145 May 19 12:16 ..\\ndrwxr-xr-x 3 root root       33 May 14 01:42 .cache\\n-rw-r--r-- 1 root root  4287303 May 14 01:43 dev.json\\n-rw-r--r-- 1 root root    63528 May 14 01:47 ontology_constraints_docred.json\\n-rw-r--r-- 1 root root     2452 May 14 01:43 rel_info.json\\n-rw-r--r-- 1 root root  6186654 May 16 01:51 sft_dev.jsonl\\n-rw-r--r-- 1 root root  6352322 May 16 02:09 sft_dev_llama.jsonl\\n-rw-r--r-- 1 root root 18933693 May 16 01:51 sft_train.jsonl\\n-rw-r--r-- 1 root root 19440491 May 16 02:09 sft_train_llama.jsonl\\n-rw-r--r-- 1 root root 13029595 May 14 01:43 train_annotated.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  },
  "sourceToolAssistantUUID": "2f89a17a-d57d-4e1f-9268-c33e7a13530c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-23T05:48:38.764Z_

<details><summary>↩ Tool result · `toolu_016VSbU5cFdc26qGP3fq2kjB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[{\\\"vertexSet\\\": [[{\\\"pos\\\": [0, 2], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 4, \\\"name\\\": \\\"Skai TV\\\"}, {\\\"pos\\\": [0, 2], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 0, \\\"name\\\": \\\"Skai TV\\\"}, {\\\"pos\\\": [3, 5], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 5, \\\"name\\\": \\\"Skai TV\\\"}], [{\\\"name\\\": \\\"Greek\\\", \\\"pos\\\": [4, 5], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Piraeus\\\", \\\"pos\\\": [14, 15], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Skai Group\\\", \\\"pos\\\": [5, 7], \\\"sent_id\\\": 1, \\\"type\\\": \\\"ORG\\\"}], [{\\\"pos\\\": [8, 12], \\\"type\\\": \\\"TIME\\\", \\\"sent_id\\\": 2, \\\"name\\\": \\\"1st of April 2006\\\"}], [{\\\"name\\\": \\\"Athens\\\", \\\"pos\\\": [14, 15], \\\"sent_id\\\": 2, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Nova\\\", \\\"pos\\\": [16, 17], \\\"sent_id\\\": 3, \\\"type\\\": \\\"ORG\\\"}], [{\\\"pos\\\": [18, 20], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 3, \\\"name\\\": \\\"Cosmote TV\\\"}], [{\\\"pos\\\": [7, 8], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 4, \\\"name\\\": \\\"Digea\\\"}], [{\\\"name\\\": \\\"Greece\\\", \\\"pos\\\": [20, 21], \\\"sent_id\\\": 4, \\\"type\\\": \\\"LOC\\\"}, {\\\"name\\\": \\\"Greece\\\", \\\"pos\\\": [5, 6], \\\"sent_id\\\": 6, \\\"type\\\": \\\"LOC\\\"}], [{\\\"sent_id\\\": 5, \\\"type\\\": \\\"MISC\\\", \\\"pos\\\": [13, 14], \\\"name\\\": \\\"Greek\\\"}]], \\\"labels\\\": [{\\\"r\\\": \\\"P17\\\", \\\"h\\\": 2, \\\"t\\\": 9, \\\"evidence\\\": [0, 4]}, {\\\"r\\\": \\\"P17\\\", \\\"h\\\": 3, \\\"t\\\": 9, \\\"evidence\\\": [0, 1, 4]}, {\\\"r\\\": \\\"P17\\\", \\\"h\\\": 5, \\\"t\\\": 9, \\\"evidence\\\": [0, 2, 4]}, {\\\"r\\\": \\\"P159\\\", \\\"h\\\": 0, \\\"t\\\": 2, \\\"evidence\\\": [0]}, {\\\"r\\\": \\\"P127\\\", \\\"h\\\": 0, \\\"t\\\": 3, \\\"evidence\\\": [0, 1]}, {\\\"r\\\": \\\"P159\\\", \\\"h\\\": 0, \\\"t\\\": 5, \\\"evidence\\\": [0, 2]}, {\\\"r\\\": \\\"P17\\\", \\\"h\\\": 0, \\\"t\\\": 9, \\\"evidence\\\": [0, 4, 5, 6]}], \\\"title\\\": \\\"Skai TV\\\", \\\"sents\\\": [[\\\"Skai\\\", \\\"TV\\\", \\\"is\\\", \\\"a\\\", \\\"Greek\\\", \\\"free\\\", \\\"-\\\", \\\"to\\\", \\\"-\\\", \\\"air\\\", \\\"television\\\", \\\"network\\\", \\\"based\\\", \\\"in\\\", \\\"Piraeus\\\", \\\".\\\"], [\\\"It\\\", \\\"is\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Skai\\\", \\\"Group\\\", \\\",\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"largest\\\", \\\"media\\\", \\\"groups\\\", \\\"in\\\", \\\"the\\\", \\\"country\\\", \\\".\\\"], [\\\"It\\\", \\\"was\\\", \\\"relaunched\\\", \\\"in\\\", \\\"its\\\", \\\"present\\\", \\\"form\\\", \\\"on\\\", \\\"1st\\\", \\\"of\\\", \\\"April\\\", \\\"2006\\\", \\\"in\\\", \\\"the\\\", \\\"Athens\\\", \\\"metropolitan\\\", \\\"area\\\", \\\",\\\", \\\"and\\\", \\\"gradually\\\", \\\"spread\\\", \\\"its\\\", \\\"coverage\\\", \\\"nationwide\\\", \\\".\\\"], [\\\"Besides\\\", \\\"digital\\\", \\\"terrestrial\\\", \\\"transmission\\\", \\\",\\\", \\\"it\\\", \\\"is\\\", \\\"available\\\", \\\"on\\\", \\\"the\\\", \\\"subscription\\\", \\\"-\\\", \\\"based\\\", \\\"encrypted\\\", \\\"services\\\", \\\"of\\\", \\\"Nova\\\", \\\"and\\\", \\\"Cosmote\\\", \\\"TV\\\", \\\".\\\"], [\\\"Skai\\\", \\\"TV\\\", \\\"is\\\", \\\"also\\\", \\\"a\\\", \\\"member\\\", \\\"of\\\", \\\"Digea\\\", \\\",\\\", \\\"a\\\", \\\"consortium\\\", \\\"of\\\", \\\"private\\\", \\\"television\\\", \\\"networks\\\", \\\"introducing\\\", \\\"digital\\\", \\\"terrestrial\\\", \\\"transmission\\\", \\\"in\\\", \\\"Greece\\\", \\\".\\\"], [\\\"At\\\", \\\"launch\\\", \\\",\\\", \\\"Skai\\\", \\\"TV\\\", \\\"opted\\\", \\\"for\\\", \\\"dubbing\\\", \\\"all\\\", \\\"foreign\\\", \\\"language\\\", \\\"content\\\", \\\"into\\\", \\\"Greek\\\", \\\",\\\", \\\"instead\\\", \\\"of\\\", \\\"using\\\", \\\"subtitles\\\", \\\".\\\"], [\\\"This\\\", \\\"is\\\", \\\"very\\\", \\\"uncommon\\\", \\\"in\\\", \\\"Greece\\\", \\\"for\\\", \\\"anything\\\", \\\"except\\\", \\\"documentaries\\\", \\\"(\\\", \\\"using\\\", \\\"voiceover\\\", \\\"dubbing\\\", \\\")\\\", \\\"and\\\", \\\"children\\\", \\\"'s\\\", \\\"programmes\\\", \\\"(\\\", \\\"using\\\", \\\"lip\\\", \\\"-\\\", \\\"synced\\\", \\\"dubbing\\\", \\\")\\\", \\\",\\\", \\\"so\\\", \\\"after\\\", \\\"intense\\\", \\\"criticism\\\", \\\"the\\\", \\\"station\\\", \\\"switched\\\", \\\"to\\\", \\\"using\\\", \\\"subtitles\\\", \\\"for\\\", \\\"almost\\\", \\\"all\\\", \\\"foreign\\\", \\\"shows\\\", \\\".\\\"]]}, {\\\"vertexSet\\\": [[{\\\"pos\\\": [0, 2], \\\"type\\\": \\\"LOC\\\", \\\"sent_id\\\": 0, \\\"name\\\": \\\"Washington Place\\\"}, {\\\"name\\\": \\\"William Washington House\\\", \\\"pos\\\": [3, 6], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}, {\\\"pos\\\": [0, 2], \\\"type\\\": \\\"LOC\\\", \\\"sent_id\\\": 1, \\\"name\\\": \\\"Washington Place\\\"}, {\\\"pos\\\": [17, 19], \\\"type\\\": \\\"LOC\\\", \\\"sent_id\\\": 3, \\\"name\\\": \\\"Washington Place\\\"}, {\\\"pos\\\": [0, 2], \\\"type\\\": \\\"LOC\\\", \\\"sent_id\\\": 4, \\\"name\\\": \\\"Washington Place\\\"}], [{\\\"name\\\": \\\"Emancipation Proclamation\\\", \\\"pos\\\": [19, 21], \\\"sent_id\\\": 0, \\\"type\\\": \\\"MISC\\\"}], [{\\\"pos\\\": [22, 23], \\\"type\\\": \\\"TIME\\\", \\\"sent_id\\\": 0, \\\"name\\\": \\\"1863\\\"}, {\\\"pos\\\": [13, 14], \\\"type\\\": \\\"TIME\\\", \\\"sent_id\\\": 1, \\\"name\\\": \\\"1863\\\"}], [{\\\"name\\\": \\\"Hampshire County\\\", \\\"pos\\\": [24, 26], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"West Virginia\\\", \\\"pos\\\": [27, 29], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}, {\\\"name\\\": \\\"West Virginia\\\", \\\"pos\\\": [30, 32], \\\"sent_id\\\": 2, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"United States\\\", \\\"pos\\\": [30, 32], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"William\\\", \\\"pos\\\": [5, 6], \\\"sent_id\\\": 1, \\\"type\\\": \\\"PER\\\"}], [{\\\"pos\\\": [7, 9], \\\"type\\\": \\\"PER\\\", \\\"sent_id\\\": 1, \\\"name\\\": \\\"Annie Washington\\\"}], [{\\\"name\\\": \\\"Romney\\\", \\\"pos\\\": [11, 12], \\\"sent_id\\\": 2, \\\"type\\\": \\\"LOC\\\"}, {\\\"name\\\": \\\"Romney\\\", \\\"pos\\\": [11, 12], \\\"sent_id\\\": 1, \\\"type\\\": \\\"LOC\\\"}, {\\n\\n... [截断: 输出过长，省略 4279303 字符] ...\\n\\n\\\"6\\\", \\\",\\\", \\\"2011\\\", \\\"as\\\", \\\"a\\\", \\\"promotional\\\", \\\"single\\\", \\\".\\\"], [\\\"It\\\", \\\"was\\\", \\\"released\\\", \\\"as\\\", \\\"the\\\", \\\"third\\\", \\\"and\\\", \\\"final\\\", \\\"single\\\", \\\"from\\\", \\\"the\\\", \\\"album\\\", \\\"in\\\", \\\"the\\\", \\\"United\\\", \\\"States\\\", \\\",\\\", \\\"on\\\", \\\"September\\\", \\\"24\\\", \\\",\\\", \\\"2012\\\", \\\".\\\"], [\\\"The\\\", \\\"song\\\", \\\"was\\\", \\\"written\\\", \\\"by\\\", \\\"DeGraw\\\", \\\"and\\\", \\\"produced\\\", \\\"by\\\", \\\"Butch\\\", \\\"Walker\\\", \\\".\\\"], [\\\"The\\\", \\\"song\\\", \\\"finds\\\", \\\"DeGraw\\\", \\\"promising\\\", \\\"his\\\", \\\"girl\\\", \\\"everlasting\\\", \\\"love\\\", \\\",\\\", \\\"and\\\", \\\"when\\\", \\\"she\\\", \\\"needs\\\", \\\"someone\\\", \\\"he\\\", \\\"'ll\\\", \\\"always\\\", \\\"be\\\", \\\"there\\\", \\\"fighting\\\", \\\"for\\\", \\\"her\\\", \\\".\\\"], [\\\"The\\\", \\\"song\\\", \\\"has\\\", \\\"charted\\\", \\\"inside\\\", \\\"the\\\", \\\"top\\\", \\\"-\\\", \\\"forty\\\", \\\"on\\\", \\\"the\\\", \\\"Dutch\\\", \\\"chart\\\", \\\"and\\\", \\\"has\\\", \\\"also\\\", \\\"charted\\\", \\\"on\\\", \\\"the\\\", \\\"UK\\\", \\\"Singles\\\", \\\"Chart\\\", \\\"and\\\", \\\"the\\\", \\\"Adult\\\", \\\"Pop\\\", \\\"Songs\\\", \\\"chart\\\", \\\".\\\"], [\\\"DeGraw\\\", \\\"appeared\\\", \\\"on\\\", \\\"the\\\", \\\"last\\\", \\\"episode\\\", \\\"of\\\", \\\"One\\\", \\\"Tree\\\", \\\"Hill\\\", \\\"and\\\", \\\"performed\\\", \\\"the\\\", \\\"track\\\", \\\".\\\"]]}, {\\\"vertexSet\\\": [[{\\\"name\\\": \\\"Paul E. Pfeifer\\\", \\\"pos\\\": [0, 3], \\\"sent_id\\\": 0, \\\"type\\\": \\\"PER\\\"}, {\\\"name\\\": \\\"Pfeifer\\\", \\\"pos\\\": [0, 1], \\\"sent_id\\\": 7, \\\"type\\\": \\\"PER\\\"}, {\\\"type\\\": \\\"PER\\\", \\\"pos\\\": [0, 1], \\\"name\\\": \\\"Pfeifer\\\", \\\"sent_id\\\": 2}, {\\\"type\\\": \\\"PER\\\", \\\"pos\\\": [0, 1], \\\"name\\\": \\\"Pfeifer\\\", \\\"sent_id\\\": 8}], [{\\\"type\\\": \\\"TIME\\\", \\\"pos\\\": [5, 9], \\\"name\\\": \\\"October 15, 1942\\\", \\\"sent_id\\\": 0}], [{\\\"name\\\": \\\"American\\\", \\\"pos\\\": [12, 13], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Ohio General Assembly\\\", \\\"pos\\\": [7, 10], \\\"sent_id\\\": 1, \\\"type\\\": \\\"ORG\\\"}], [{\\\"name\\\": \\\"Ohio Republican party\\\", \\\"pos\\\": [15, 18], \\\"sent_id\\\": 1, \\\"type\\\": \\\"ORG\\\"}], [{\\\"name\\\": \\\"Supreme Court of Ohio\\\", \\\"pos\\\": [27, 31], \\\"sent_id\\\": 1, \\\"type\\\": \\\"ORG\\\"}], [{\\\"name\\\": \\\"Bucyrus\\\", \\\"pos\\\": [4, 5], \\\"sent_id\\\": 2, \\\"type\\\": \\\"LOC\\\"}, {\\\"name\\\": \\\"Bucyrus\\\", \\\"pos\\\": [10, 11], \\\"sent_id\\\": 3, \\\"type\\\": \\\"LOC\\\"}], [{\\\"type\\\": \\\"TIME\\\", \\\"pos\\\": [6, 7], \\\"name\\\": \\\"1942\\\", \\\"sent_id\\\": 2}], [{\\\"name\\\": \\\"Yorkshire\\\", \\\"pos\\\": [7, 8], \\\"sent_id\\\": 4, \\\"type\\\": \\\"LOC\\\"}], [{\\\"type\\\": \\\"TIME\\\", \\\"pos\\\": [16, 17], \\\"name\\\": \\\"1963\\\", \\\"sent_id\\\": 5}], [{\\\"name\\\": \\\"Ohio State University\\\", \\\"pos\\\": [18, 21], \\\"sent_id\\\": 5, \\\"type\\\": \\\"ORG\\\"}], [{\\\"type\\\": \\\"TIME\\\", \\\"pos\\\": [1, 2], \\\"name\\\": \\\"1966\\\", \\\"sent_id\\\": 6}], [{\\\"name\\\": \\\"College of Law\\\", \\\"pos\\\": [11, 14], \\\"sent_id\\\": 6, \\\"type\\\": \\\"ORG\\\"}], [{\\\"name\\\": \\\"Crawford County\\\", \\\"pos\\\": [6, 8], \\\"sent_id\\\": 7, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Julia\\\", \\\"pos\\\": [4, 5], \\\"sent_id\\\": 8, \\\"type\\\": \\\"PER\\\"}], [{\\\"name\\\": \\\"three\\\", \\\"pos\\\": [6, 7], \\\"sent_id\\\": 8, \\\"type\\\": \\\"NUM\\\"}], [{\\\"name\\\": \\\"four\\\", \\\"pos\\\": [9, 10], \\\"sent_id\\\": 8, \\\"type\\\": \\\"NUM\\\"}]], \\\"labels\\\": [{\\\"r\\\": \\\"P569\\\", \\\"h\\\": 0, \\\"t\\\": 7, \\\"evidence\\\": [0, 2]}, {\\\"r\\\": \\\"P69\\\", \\\"h\\\": 0, \\\"t\\\": 10, \\\"evidence\\\": [2, 5]}, {\\\"r\\\": \\\"P69\\\", \\\"h\\\": 0, \\\"t\\\": 12, \\\"evidence\\\": [2, 6]}, {\\\"r\\\": \\\"P102\\\", \\\"h\\\": 0, \\\"t\\\": 4, \\\"evidence\\\": [0, 1]}, {\\\"r\\\": \\\"P19\\\", \\\"h\\\": 0, \\\"t\\\": 6, \\\"evidence\\\": [2]}, {\\\"r\\\": \\\"P27\\\", \\\"h\\\": 0, \\\"t\\\": 2, \\\"evidence\\\": [0]}, {\\\"r\\\": \\\"P569\\\", \\\"h\\\": 0, \\\"t\\\": 1, \\\"evidence\\\": [0]}], \\\"title\\\": \\\"Paul Pfeifer\\\", \\\"sents\\\": [[\\\"Paul\\\", \\\"E.\\\", \\\"Pfeifer\\\", \\\"(\\\", \\\"born\\\", \\\"October\\\", \\\"15\\\", \\\",\\\", \\\"1942\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"American\\\", \\\"jurist\\\", \\\".\\\"], [\\\"He\\\", \\\"served\\\", \\\"in\\\", \\\"both\\\", \\\"houses\\\", \\\"of\\\", \\\"the\\\", \\\"Ohio\\\", \\\"General\\\", \\\"Assembly\\\", \\\"as\\\", \\\"a\\\", \\\"member\\\", \\\"of\\\", \\\"the\\\", \\\"Ohio\\\", \\\"Republican\\\", \\\"party\\\", \\\"and\\\", \\\"was\\\", \\\"most\\\", \\\"recently\\\", \\\"an\\\", \\\"Associate\\\", \\\"Justice\\\", \\\"of\\\", \\\"the\\\", \\\"Supreme\\\", \\\"Court\\\", \\\"of\\\", \\\"Ohio\\\", \\\".\\\"], [\\\"Pfeifer\\\", \\\"was\\\", \\\"born\\\", \\\"in\\\", \\\"Bucyrus\\\", \\\"in\\\", \\\"1942\\\", \\\".\\\"], [\\\"He\\\", \\\"grew\\\", \\\"up\\\", \\\"on\\\", \\\"his\\\", \\\"family\\\", \\\"'s\\\", \\\"dairy\\\", \\\"farm\\\", \\\"near\\\", \\\"Bucyrus\\\", \\\".\\\"], [\\\"As\\\", \\\"a\\\", \\\"teenager\\\", \\\",\\\", \\\"he\\\", \\\"raised\\\", \\\"purebred\\\", \\\"Yorkshire\\\", \\\"hogs\\\", \\\"to\\\", \\\"finance\\\", \\\"his\\\", \\\"college\\\", \\\"education\\\", \\\".\\\"], [\\\"He\\\", \\\"earned\\\", \\\"a\\\", \\\"bachelor\\\", \\\"of\\\", \\\"arts\\\", \\\"degree\\\", \\\"in\\\", \\\"economics\\\", \\\",\\\", \\\"political\\\", \\\"science\\\", \\\",\\\", \\\"and\\\", \\\"history\\\", \\\"in\\\", \\\"1963\\\", \\\"from\\\", \\\"Ohio\\\", \\\"State\\\", \\\"University\\\", \\\".\\\"], [\\\"In\\\", \\\"1966\\\", \\\",\\\", \\\"he\\\", \\\"also\\\", \\\"earned\\\", \\\"a\\\", \\\"law\\\", \\\"degree\\\", \\\"from\\\", \\\"the\\\", \\\"College\\\", \\\"of\\\", \\\"Law\\\", \\\".\\\"], [\\\"Pfeifer\\\", \\\"owns\\\", \\\"a\\\", \\\"cattle\\\", \\\"farm\\\", \\\"in\\\", \\\"Crawford\\\", \\\"County\\\", \\\",\\\", \\\"near\\\", \\\"his\\\", \\\"childhood\\\", \\\"home\\\", \\\".\\\"], [\\\"Pfeifer\\\", \\\"and\\\", \\\"his\\\", \\\"wife\\\", \\\"Julia\\\", \\\"have\\\", \\\"three\\\", \\\"children\\\", \\\"and\\\", \\\"four\\\", \\\"grandchildren\\\", \\\".\\\"]]}]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.26}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c877fd2-a296-4377-ac39-dbdf34353070",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "c9b5044b-0e0a-4631-80e8-05f191506efa",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[{\\\\\\\"vertexSet\\\\\\\": [[{\\\\\\\"pos\\\\\\\": [0, 2], \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\", \\\\\\\"sent_id\\\\\\\": 4, \\\\\\\"name\\\\\\\": \\\\\\\"Skai TV\\\\\\\"}, {\\\\\\\"pos\\\\\\\": [0, 2], \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\", \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"name\\\\\\\": \\\\\\\"Skai TV\\\\\\\"}, {\\\\\\\"pos\\\\\\\": [3, 5], \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\", \\\\\\\"sent_id\\\\\\\": 5, \\\\\\\"name\\\\\\\": \\\\\\\"Skai TV\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Greek\\\\\\\", \\\\\\\"pos\\\\\\\": [4, 5], \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Piraeus\\\\\\\", \\\\\\\"pos\\\\\\\": [14, 15], \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Skai Group\\\\\\\", \\\\\\\"pos\\\\\\\": [5, 7], \\\\\\\"sent_id\\\\\\\": 1, \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\"}], [{\\\\\\\"pos\\\\\\\": [8, 12], \\\\\\\"type\\\\\\\": \\\\\\\"TIME\\\\\\\", \\\\\\\"sent_id\\\\\\\": 2, \\\\\\\"name\\\\\\\": \\\\\\\"1st of April 2006\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Athens\\\\\\\", \\\\\\\"pos\\\\\\\": [14, 15], \\\\\\\"sent_id\\\\\\\": 2, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Nova\\\\\\\", \\\\\\\"pos\\\\\\\": [16, 17], \\\\\\\"sent_id\\\\\\\": 3, \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\"}], [{\\\\\\\"pos\\\\\\\": [18, 20], \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\", \\\\\\\"sent_id\\\\\\\": 3, \\\\\\\"name\\\\\\\": \\\\\\\"Cosmote TV\\\\\\\"}], [{\\\\\\\"pos\\\\\\\": [7, 8], \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\", \\\\\\\"sent_id\\\\\\\": 4, \\\\\\\"name\\\\\\\": \\\\\\\"Digea\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Greece\\\\\\\", \\\\\\\"pos\\\\\\\": [20, 21], \\\\\\\"sent_id\\\\\\\": 4, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}, {\\\\\\\"name\\\\\\\": \\\\\\\"Greece\\\\\\\", \\\\\\\"pos\\\\\\\": [5, 6], \\\\\\\"sent_id\\\\\\\": 6, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"sent_id\\\\\\\": 5, \\\\\\\"type\\\\\\\": \\\\\\\"MISC\\\\\\\", \\\\\\\"pos\\\\\\\": [13, 14], \\\\\\\"name\\\\\\\": \\\\\\\"Greek\\\\\\\"}]], \\\\\\\"labels\\\\\\\": [{\\\\\\\"r\\\\\\\": \\\\\\\"P17\\\\\\\", \\\\\\\"h\\\\\\\": 2, \\\\\\\"t\\\\\\\": 9, \\\\\\\"evidence\\\\\\\": [0, 4]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P17\\\\\\\", \\\\\\\"h\\\\\\\": 3, \\\\\\\"t\\\\\\\": 9, \\\\\\\"evidence\\\\\\\": [0, 1, 4]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P17\\\\\\\", \\\\\\\"h\\\\\\\": 5, \\\\\\\"t\\\\\\\": 9, \\\\\\\"evidence\\\\\\\": [0, 2, 4]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P159\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 2, \\\\\\\"evidence\\\\\\\": [0]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P127\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 3, \\\\\\\"evidence\\\\\\\": [0, 1]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P159\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 5, \\\\\\\"evidence\\\\\\\": [0, 2]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P17\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 9, \\\\\\\"evidence\\\\\\\": [0, 4, 5, 6]}], \\\\\\\"title\\\\\\\": \\\\\\\"Skai TV\\\\\\\", \\\\\\\"sents\\\\\\\": [[\\\\\\\"Skai\\\\\\\", \\\\\\\"TV\\\\\\\", \\\\\\\"is\\\\\\\", \\\\\\\"a\\\\\\\", \\\\\\\"Greek\\\\\\\", \\\\\\\"free\\\\\\\", \\\\\\\"-\\\\\\\", \\\\\\\"to\\\\\\\", \\\\\\\"-\\\\\\\", \\\\\\\"air\\\\\\\", \\\\\\\"television\\\\\\\", \\\\\\\"network\\\\\\\", \\\\\\\"based\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"Piraeus\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"It\\\\\\\", \\\\\\\"is\\\\\\\", \\\\\\\"part\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"Skai\\\\\\\", \\\\\\\"Group\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"one\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"largest\\\\\\\", \\\\\\\"media\\\\\\\", \\\\\\\"groups\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"country\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"It\\\\\\\", \\\\\\\"was\\\\\\\", \\\\\\\"relaunched\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"its\\\\\\\", \\\\\\\"present\\\\\\\", \\\\\\\"form\\\\\\\", \\\\\\\"on\\\\\\\", \\\\\\\"1st\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"April\\\\\\\", \\\\\\\"2006\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"Athens\\\\\\\", \\\\\\\"metropolitan\\\\\\\", \\\\\\\"area\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"gradually\\\\\\\", \\\\\\\"spread\\\\\\\", \\\\\\\"its\\\\\\\", \\\\\\\"coverage\\\\\\\", \\\\\\\"nationwide\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"Besides\\\\\\\", \\\\\\\"digital\\\\\\\", \\\\\\\"terrestrial\\\\\\\", \\\\\\\"transmission\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"it\\\\\\\", \\\\\\\"is\\\\\\\", \\\\\\\"available\\\\\\\", \\\\\\\"on\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"subscription\\\\\\\", \\\\\\\"-\\\\\\\", \\\\\\\"based\\\\\\\", \\\\\\\"encrypted\\\\\\\", \\\\\\\"services\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"Nova\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"Cosmote\\\\\\\", \\\\\\\"TV\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"Skai\\\\\\\", \\\\\\\"TV\\\\\\\", \\\\\\\"is\\\\\\\", \\\\\\\"also\\\\\\\", \\\\\\\"a\\\\\\\", \\\\\\\"member\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"Digea\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"a\\\\\\\", \\\\\\\"consortium\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"private\\\\\\\", \\\\\\\"television\\\\\\\", \\\\\\\"networks\\\\\\\", \\\\\\\"introducing\\\\\\\", \\\\\\\"digital\\\\\\\", \\\\\\\"terrestrial\\\\\\\", \\\\\\\"transmission\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"Greece\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"At\\\\\\\", \\\\\\\"launch\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"Skai\\\\\\\", \\\\\\\"TV\\\\\\\", \\\\\\\"opted\\\\\\\", \\\\\\\"for\\\\\\\", \\\\\\\"dubbing\\\\\\\", \\\\\\\"all\\\\\\\", \\\\\\\"foreign\\\\\\\", \\\\\\\"language\\\\\\\", \\\\\\\"content\\\\\\\", \\\\\\\"into\\\\\\\", \\\\\\\"Greek\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"instead\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"using\\\\\\\", \\\\\\\"subtitles\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"This\\\\\\\", \\\\\\\"is\\\\\\\", \\\\\\\"very\\\\\\\", \\\\\\\"uncommon\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"Greece\\\\\\\", \\\\\\\"for\\\\\\\", \\\\\\\"anything\\\\\\\", \\\\\\\"except\\\\\\\", \\\\\\\"documentaries\\\\\\\", \\\\\\\"(\\\\\\\", \\\\\\\"using\\\\\\\", \\\\\\\"voiceover\\\\\\\", \\\\\\\"dubbing\\\\\\\", \\\\\\\")\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"children\\\\\\\", \\\\\\\"'s\\\\\\\", \\\\\\\"programmes\\\\\\\", \\\\\\\"(\\\\\\\", \\\\\\\"using\\\\\\\", \\\\\\\"lip\\\\\\\", \\\\\\\"-\\\\\\\", \\\\\\\"synced\\\\\\\", \\\\\\\"dubbing\\\\\\\", \\\\\\\")\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"so\\\\\\\", \\\\\\\"after\\\\\\\", \\\\\\\"intense\\\\\\\", \\\\\\\"criticism\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"station\\\\\\\", \\\\\\\"switched\\\\\\\", \\\\\\\"to\\\\\\\", \\\\\\\"using\\\\\\\", \\\\\\\"subtitles\\\\\\\", \\\\\\\"for\\\\\\\", \\\\\\\"almost\\\\\\\", \\\\\\\"all\\\\\\\", \\\\\\\"foreign\\\\\\\", \\\\\\\"shows\\\\\\\", \\\\\\\".\\\\\\\"]]}, {\\\\\\\"vertexSet\\\\\\\": [[{\\\\\\\"pos\\\\\\\": [0, 2], \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\", \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"name\\\\\\\": \\\\\\\"Washington Place\\\\\\\"}, {\\\\\\\"name\\\\\\\": \\\\\\\"William Washington House\\\\\\\", \\\\\\\"pos\\\\\\\": [3, 6], \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}, {\\\\\\\"pos\\\\\\\": [0, 2], \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\", \\\\\\\"sent_id\\\\\\\": 1, \\\\\\\"name\\\\\\\": \\\\\\\"Washington Place\\\\\\\"}, {\\\\\\\"pos\\\\\\\": [17, 19], \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\", \\\\\\\"sent_id\\\\\\\": 3, \\\\\\\"name\\\\\\\": \\\\\\\"Washington Place\\\\\\\"}, {\\\\\\\"pos\\\\\\\": [0, 2], \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\", \\\\\\\"sent_id\\\\\\\": 4, \\\\\\\"name\\\\\\\": \\\\\\\"Washington Place\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Emancipation Proclamation\\\\\\\", \\\\\\\"pos\\\\\\\": [19, 21], \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"type\\\\\\\": \\\\\\\"MISC\\\\\\\"}], [{\\\\\\\"pos\\\\\\\": [22, 23], \\\\\\\"type\\\\\\\": \\\\\\\"TIME\\\\\\\", \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"name\\\\\\\": \\\\\\\"1863\\\\\\\"}, {\\\\\\\"pos\\\\\\\": [13, 14], \\\\\\\"type\\\\\\\": \\\\\\\"TIME\\\\\\\", \\\\\\\"sent_id\\\\\\\": 1, \\\\\\\"name\\\\\\\": \\\\\\\"1863\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Hampshire County\\\\\\\", \\\\\\\"pos\\\\\\\": [24, 26], \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"West Virginia\\\\\\\", \\\\\\\"pos\\\\\\\": [27, 29], \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}, {\\\\\\\"name\\\\\\\": \\\\\\\"West Virginia\\\\\\\", \\\\\\\"pos\\\\\\\": [30, 32], \\\\\\\"sent_id\\\\\\\": 2, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"United States\\\\\\\", \\\\\\\"pos\\\\\\\": [30, 32], \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"William\\\\\\\", \\\\\\\"pos\\\\\\\": [5, 6], \\\\\\\"sent_id\\\\\\\": 1, \\\\\\\"type\\\\\\\": \\\\\\\"PER\\\\\\\"}], [{\\\\\\\"pos\\\\\\\": [7, 9], \\\\\\\"type\\\\\\\": \\\\\\\"PER\\\\\\\", \\\\\\\"sent_id\\\\\\\": 1, \\\\\\\"name\\\\\\\": \\\\\\\"Annie Washington\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Romney\\\\\\\", \\\\\\\"pos\\\\\\\": [11, 12], \\\\\\\"sent_id\\\\\\\": 2, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}, {\\\\\\\"name\\\\\\\": \\\\\\\"Romney\\\\\\\", \\\\\\\"pos\\\\\\\": [11, 12], \\\\\\\"sent_id\\\\\\\": 1, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}, {\\\\n\\\\n... [截断: 输出过长，省略 4279303 字符] ...\\\\n\\\\n\\\\\\\"6\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"2011\\\\\\\", \\\\\\\"as\\\\\\\", \\\\\\\"a\\\\\\\", \\\\\\\"promotional\\\\\\\", \\\\\\\"single\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"It\\\\\\\", \\\\\\\"was\\\\\\\", \\\\\\\"released\\\\\\\", \\\\\\\"as\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"third\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"final\\\\\\\", \\\\\\\"single\\\\\\\", \\\\\\\"from\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"album\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"United\\\\\\\", \\\\\\\"States\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"on\\\\\\\", \\\\\\\"September\\\\\\\", \\\\\\\"24\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"2012\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"The\\\\\\\", \\\\\\\"song\\\\\\\", \\\\\\\"was\\\\\\\", \\\\\\\"written\\\\\\\", \\\\\\\"by\\\\\\\", \\\\\\\"DeGraw\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"produced\\\\\\\", \\\\\\\"by\\\\\\\", \\\\\\\"Butch\\\\\\\", \\\\\\\"Walker\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"The\\\\\\\", \\\\\\\"song\\\\\\\", \\\\\\\"finds\\\\\\\", \\\\\\\"DeGraw\\\\\\\", \\\\\\\"promising\\\\\\\", \\\\\\\"his\\\\\\\", \\\\\\\"girl\\\\\\\", \\\\\\\"everlasting\\\\\\\", \\\\\\\"love\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"when\\\\\\\", \\\\\\\"she\\\\\\\", \\\\\\\"needs\\\\\\\", \\\\\\\"someone\\\\\\\", \\\\\\\"he\\\\\\\", \\\\\\\"'ll\\\\\\\", \\\\\\\"always\\\\\\\", \\\\\\\"be\\\\\\\", \\\\\\\"there\\\\\\\", \\\\\\\"fighting\\\\\\\", \\\\\\\"for\\\\\\\", \\\\\\\"her\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"The\\\\\\\", \\\\\\\"song\\\\\\\", \\\\\\\"has\\\\\\\", \\\\\\\"charted\\\\\\\", \\\\\\\"inside\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"top\\\\\\\", \\\\\\\"-\\\\\\\", \\\\\\\"forty\\\\\\\", \\\\\\\"on\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"Dutch\\\\\\\", \\\\\\\"chart\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"has\\\\\\\", \\\\\\\"also\\\\\\\", \\\\\\\"charted\\\\\\\", \\\\\\\"on\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"UK\\\\\\\", \\\\\\\"Singles\\\\\\\", \\\\\\\"Chart\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"Adult\\\\\\\", \\\\\\\"Pop\\\\\\\", \\\\\\\"Songs\\\\\\\", \\\\\\\"chart\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"DeGraw\\\\\\\", \\\\\\\"appeared\\\\\\\", \\\\\\\"on\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"last\\\\\\\", \\\\\\\"episode\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"One\\\\\\\", \\\\\\\"Tree\\\\\\\", \\\\\\\"Hill\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"performed\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"track\\\\\\\", \\\\\\\".\\\\\\\"]]}, {\\\\\\\"vertexSet\\\\\\\": [[{\\\\\\\"name\\\\\\\": \\\\\\\"Paul E. Pfeifer\\\\\\\", \\\\\\\"pos\\\\\\\": [0, 3], \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"type\\\\\\\": \\\\\\\"PER\\\\\\\"}, {\\\\\\\"name\\\\\\\": \\\\\\\"Pfeifer\\\\\\\", \\\\\\\"pos\\\\\\\": [0, 1], \\\\\\\"sent_id\\\\\\\": 7, \\\\\\\"type\\\\\\\": \\\\\\\"PER\\\\\\\"}, {\\\\\\\"type\\\\\\\": \\\\\\\"PER\\\\\\\", \\\\\\\"pos\\\\\\\": [0, 1], \\\\\\\"name\\\\\\\": \\\\\\\"Pfeifer\\\\\\\", \\\\\\\"sent_id\\\\\\\": 2}, {\\\\\\\"type\\\\\\\": \\\\\\\"PER\\\\\\\", \\\\\\\"pos\\\\\\\": [0, 1], \\\\\\\"name\\\\\\\": \\\\\\\"Pfeifer\\\\\\\", \\\\\\\"sent_id\\\\\\\": 8}], [{\\\\\\\"type\\\\\\\": \\\\\\\"TIME\\\\\\\", \\\\\\\"pos\\\\\\\": [5, 9], \\\\\\\"name\\\\\\\": \\\\\\\"October 15, 1942\\\\\\\", \\\\\\\"sent_id\\\\\\\": 0}], [{\\\\\\\"name\\\\\\\": \\\\\\\"American\\\\\\\", \\\\\\\"pos\\\\\\\": [12, 13], \\\\\\\"sent_id\\\\\\\": 0, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Ohio General Assembly\\\\\\\", \\\\\\\"pos\\\\\\\": [7, 10], \\\\\\\"sent_id\\\\\\\": 1, \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Ohio Republican party\\\\\\\", \\\\\\\"pos\\\\\\\": [15, 18], \\\\\\\"sent_id\\\\\\\": 1, \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Supreme Court of Ohio\\\\\\\", \\\\\\\"pos\\\\\\\": [27, 31], \\\\\\\"sent_id\\\\\\\": 1, \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Bucyrus\\\\\\\", \\\\\\\"pos\\\\\\\": [4, 5], \\\\\\\"sent_id\\\\\\\": 2, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}, {\\\\\\\"name\\\\\\\": \\\\\\\"Bucyrus\\\\\\\", \\\\\\\"pos\\\\\\\": [10, 11], \\\\\\\"sent_id\\\\\\\": 3, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"type\\\\\\\": \\\\\\\"TIME\\\\\\\", \\\\\\\"pos\\\\\\\": [6, 7], \\\\\\\"name\\\\\\\": \\\\\\\"1942\\\\\\\", \\\\\\\"sent_id\\\\\\\": 2}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Yorkshire\\\\\\\", \\\\\\\"pos\\\\\\\": [7, 8], \\\\\\\"sent_id\\\\\\\": 4, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"type\\\\\\\": \\\\\\\"TIME\\\\\\\", \\\\\\\"pos\\\\\\\": [16, 17], \\\\\\\"name\\\\\\\": \\\\\\\"1963\\\\\\\", \\\\\\\"sent_id\\\\\\\": 5}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Ohio State University\\\\\\\", \\\\\\\"pos\\\\\\\": [18, 21], \\\\\\\"sent_id\\\\\\\": 5, \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\"}], [{\\\\\\\"type\\\\\\\": \\\\\\\"TIME\\\\\\\", \\\\\\\"pos\\\\\\\": [1, 2], \\\\\\\"name\\\\\\\": \\\\\\\"1966\\\\\\\", \\\\\\\"sent_id\\\\\\\": 6}], [{\\\\\\\"name\\\\\\\": \\\\\\\"College of Law\\\\\\\", \\\\\\\"pos\\\\\\\": [11, 14], \\\\\\\"sent_id\\\\\\\": 6, \\\\\\\"type\\\\\\\": \\\\\\\"ORG\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Crawford County\\\\\\\", \\\\\\\"pos\\\\\\\": [6, 8], \\\\\\\"sent_id\\\\\\\": 7, \\\\\\\"type\\\\\\\": \\\\\\\"LOC\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"Julia\\\\\\\", \\\\\\\"pos\\\\\\\": [4, 5], \\\\\\\"sent_id\\\\\\\": 8, \\\\\\\"type\\\\\\\": \\\\\\\"PER\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"three\\\\\\\", \\\\\\\"pos\\\\\\\": [6, 7], \\\\\\\"sent_id\\\\\\\": 8, \\\\\\\"type\\\\\\\": \\\\\\\"NUM\\\\\\\"}], [{\\\\\\\"name\\\\\\\": \\\\\\\"four\\\\\\\", \\\\\\\"pos\\\\\\\": [9, 10], \\\\\\\"sent_id\\\\\\\": 8, \\\\\\\"type\\\\\\\": \\\\\\\"NUM\\\\\\\"}]], \\\\\\\"labels\\\\\\\": [{\\\\\\\"r\\\\\\\": \\\\\\\"P569\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 7, \\\\\\\"evidence\\\\\\\": [0, 2]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P69\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 10, \\\\\\\"evidence\\\\\\\": [2, 5]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P69\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 12, \\\\\\\"evidence\\\\\\\": [2, 6]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P102\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 4, \\\\\\\"evidence\\\\\\\": [0, 1]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P19\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 6, \\\\\\\"evidence\\\\\\\": [2]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P27\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 2, \\\\\\\"evidence\\\\\\\": [0]}, {\\\\\\\"r\\\\\\\": \\\\\\\"P569\\\\\\\", \\\\\\\"h\\\\\\\": 0, \\\\\\\"t\\\\\\\": 1, \\\\\\\"evidence\\\\\\\": [0]}], \\\\\\\"title\\\\\\\": \\\\\\\"Paul Pfeifer\\\\\\\", \\\\\\\"sents\\\\\\\": [[\\\\\\\"Paul\\\\\\\", \\\\\\\"E.\\\\\\\", \\\\\\\"Pfeifer\\\\\\\", \\\\\\\"(\\\\\\\", \\\\\\\"born\\\\\\\", \\\\\\\"October\\\\\\\", \\\\\\\"15\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"1942\\\\\\\", \\\\\\\")\\\\\\\", \\\\\\\"is\\\\\\\", \\\\\\\"an\\\\\\\", \\\\\\\"American\\\\\\\", \\\\\\\"jurist\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"He\\\\\\\", \\\\\\\"served\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"both\\\\\\\", \\\\\\\"houses\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"Ohio\\\\\\\", \\\\\\\"General\\\\\\\", \\\\\\\"Assembly\\\\\\\", \\\\\\\"as\\\\\\\", \\\\\\\"a\\\\\\\", \\\\\\\"member\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"Ohio\\\\\\\", \\\\\\\"Republican\\\\\\\", \\\\\\\"party\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"was\\\\\\\", \\\\\\\"most\\\\\\\", \\\\\\\"recently\\\\\\\", \\\\\\\"an\\\\\\\", \\\\\\\"Associate\\\\\\\", \\\\\\\"Justice\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"Supreme\\\\\\\", \\\\\\\"Court\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"Ohio\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"Pfeifer\\\\\\\", \\\\\\\"was\\\\\\\", \\\\\\\"born\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"Bucyrus\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"1942\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"He\\\\\\\", \\\\\\\"grew\\\\\\\", \\\\\\\"up\\\\\\\", \\\\\\\"on\\\\\\\", \\\\\\\"his\\\\\\\", \\\\\\\"family\\\\\\\", \\\\\\\"'s\\\\\\\", \\\\\\\"dairy\\\\\\\", \\\\\\\"farm\\\\\\\", \\\\\\\"near\\\\\\\", \\\\\\\"Bucyrus\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"As\\\\\\\", \\\\\\\"a\\\\\\\", \\\\\\\"teenager\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"he\\\\\\\", \\\\\\\"raised\\\\\\\", \\\\\\\"purebred\\\\\\\", \\\\\\\"Yorkshire\\\\\\\", \\\\\\\"hogs\\\\\\\", \\\\\\\"to\\\\\\\", \\\\\\\"finance\\\\\\\", \\\\\\\"his\\\\\\\", \\\\\\\"college\\\\\\\", \\\\\\\"education\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"He\\\\\\\", \\\\\\\"earned\\\\\\\", \\\\\\\"a\\\\\\\", \\\\\\\"bachelor\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"arts\\\\\\\", \\\\\\\"degree\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"economics\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"political\\\\\\\", \\\\\\\"science\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"history\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"1963\\\\\\\", \\\\\\\"from\\\\\\\", \\\\\\\"Ohio\\\\\\\", \\\\\\\"State\\\\\\\", \\\\\\\"University\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"In\\\\\\\", \\\\\\\"1966\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"he\\\\\\\", \\\\\\\"also\\\\\\\", \\\\\\\"earned\\\\\\\", \\\\\\\"a\\\\\\\", \\\\\\\"law\\\\\\\", \\\\\\\"degree\\\\\\\", \\\\\\\"from\\\\\\\", \\\\\\\"the\\\\\\\", \\\\\\\"College\\\\\\\", \\\\\\\"of\\\\\\\", \\\\\\\"Law\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"Pfeifer\\\\\\\", \\\\\\\"owns\\\\\\\", \\\\\\\"a\\\\\\\", \\\\\\\"cattle\\\\\\\", \\\\\\\"farm\\\\\\\", \\\\\\\"in\\\\\\\", \\\\\\\"Crawford\\\\\\\", \\\\\\\"County\\\\\\\", \\\\\\\",\\\\\\\", \\\\\\\"near\\\\\\\", \\\\\\\"his\\\\\\\", \\\\\\\"childhood\\\\\\\", \\\\\\\"home\\\\\\\", \\\\\\\".\\\\\\\"], [\\\\\\\"Pfeifer\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"his\\\\\\\", \\\\\\\"wife\\\\\\\", \\\\\\\"Julia\\\\\\\", \\\\\\\"have\\\\\\\", \\\\\\\"three\\\\\\\", \\\\\\\"children\\\\\\\", \\\\\\\"and\\\\\\\", \\\\\\\"four\\\\\\\", \\\\\\\"grandchildren\\\\\\\", \\\\\\\".\\\\\\\"]]}]\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.26}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[{\\\"vertexSet\\\": [[{\\\"pos\\\": [0, 2], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 4, \\\"name\\\": \\\"Skai TV\\\"}, {\\\"pos\\\": [0, 2], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 0, \\\"name\\\": \\\"Skai TV\\\"}, {\\\"pos\\\": [3, 5], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 5, \\\"name\\\": \\\"Skai TV\\\"}], [{\\\"name\\\": \\\"Greek\\\", \\\"pos\\\": [4, 5], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Piraeus\\\", \\\"pos\\\": [14, 15], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Skai Group\\\", \\\"pos\\\": [5, 7], \\\"sent_id\\\": 1, \\\"type\\\": \\\"ORG\\\"}], [{\\\"pos\\\": [8, 12], \\\"type\\\": \\\"TIME\\\", \\\"sent_id\\\": 2, \\\"name\\\": \\\"1st of April 2006\\\"}], [{\\\"name\\\": \\\"Athens\\\", \\\"pos\\\": [14, 15], \\\"sent_id\\\": 2, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Nova\\\", \\\"pos\\\": [16, 17], \\\"sent_id\\\": 3, \\\"type\\\": \\\"ORG\\\"}], [{\\\"pos\\\": [18, 20], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 3, \\\"name\\\": \\\"Cosmote TV\\\"}], [{\\\"pos\\\": [7, 8], \\\"type\\\": \\\"ORG\\\", \\\"sent_id\\\": 4, \\\"name\\\": \\\"Digea\\\"}], [{\\\"name\\\": \\\"Greece\\\", \\\"pos\\\": [20, 21], \\\"sent_id\\\": 4, \\\"type\\\": \\\"LOC\\\"}, {\\\"name\\\": \\\"Greece\\\", \\\"pos\\\": [5, 6], \\\"sent_id\\\": 6, \\\"type\\\": \\\"LOC\\\"}], [{\\\"sent_id\\\": 5, \\\"type\\\": \\\"MISC\\\", \\\"pos\\\": [13, 14], \\\"name\\\": \\\"Greek\\\"}]], \\\"labels\\\": [{\\\"r\\\": \\\"P17\\\", \\\"h\\\": 2, \\\"t\\\": 9, \\\"evidence\\\": [0, 4]}, {\\\"r\\\": \\\"P17\\\", \\\"h\\\": 3, \\\"t\\\": 9, \\\"evidence\\\": [0, 1, 4]}, {\\\"r\\\": \\\"P17\\\", \\\"h\\\": 5, \\\"t\\\": 9, \\\"evidence\\\": [0, 2, 4]}, {\\\"r\\\": \\\"P159\\\", \\\"h\\\": 0, \\\"t\\\": 2, \\\"evidence\\\": [0]}, {\\\"r\\\": \\\"P127\\\", \\\"h\\\": 0, \\\"t\\\": 3, \\\"evidence\\\": [0, 1]}, {\\\"r\\\": \\\"P159\\\", \\\"h\\\": 0, \\\"t\\\": 5, \\\"evidence\\\": [0, 2]}, {\\\"r\\\": \\\"P17\\\", \\\"h\\\": 0, \\\"t\\\": 9, \\\"evidence\\\": [0, 4, 5, 6]}], \\\"title\\\": \\\"Skai TV\\\", \\\"sents\\\": [[\\\"Skai\\\", \\\"TV\\\", \\\"is\\\", \\\"a\\\", \\\"Greek\\\", \\\"free\\\", \\\"-\\\", \\\"to\\\", \\\"-\\\", \\\"air\\\", \\\"television\\\", \\\"network\\\", \\\"based\\\", \\\"in\\\", \\\"Piraeus\\\", \\\".\\\"], [\\\"It\\\", \\\"is\\\", \\\"part\\\", \\\"of\\\", \\\"the\\\", \\\"Skai\\\", \\\"Group\\\", \\\",\\\", \\\"one\\\", \\\"of\\\", \\\"the\\\", \\\"largest\\\", \\\"media\\\", \\\"groups\\\", \\\"in\\\", \\\"the\\\", \\\"country\\\", \\\".\\\"], [\\\"It\\\", \\\"was\\\", \\\"relaunched\\\", \\\"in\\\", \\\"its\\\", \\\"present\\\", \\\"form\\\", \\\"on\\\", \\\"1st\\\", \\\"of\\\", \\\"April\\\", \\\"2006\\\", \\\"in\\\", \\\"the\\\", \\\"Athens\\\", \\\"metropolitan\\\", \\\"area\\\", \\\",\\\", \\\"and\\\", \\\"gradually\\\", \\\"spread\\\", \\\"its\\\", \\\"coverage\\\", \\\"nationwide\\\", \\\".\\\"], [\\\"Besides\\\", \\\"digital\\\", \\\"terrestrial\\\", \\\"transmission\\\", \\\",\\\", \\\"it\\\", \\\"is\\\", \\\"available\\\", \\\"on\\\", \\\"the\\\", \\\"subscription\\\", \\\"-\\\", \\\"based\\\", \\\"encrypted\\\", \\\"services\\\", \\\"of\\\", \\\"Nova\\\", \\\"and\\\", \\\"Cosmote\\\", \\\"TV\\\", \\\".\\\"], [\\\"Skai\\\", \\\"TV\\\", \\\"is\\\", \\\"also\\\", \\\"a\\\", \\\"member\\\", \\\"of\\\", \\\"Digea\\\", \\\",\\\", \\\"a\\\", \\\"consortium\\\", \\\"of\\\", \\\"private\\\", \\\"television\\\", \\\"networks\\\", \\\"introducing\\\", \\\"digital\\\", \\\"terrestrial\\\", \\\"transmission\\\", \\\"in\\\", \\\"Greece\\\", \\\".\\\"], [\\\"At\\\", \\\"launch\\\", \\\",\\\", \\\"Skai\\\", \\\"TV\\\", \\\"opted\\\", \\\"for\\\", \\\"dubbing\\\", \\\"all\\\", \\\"foreign\\\", \\\"language\\\", \\\"content\\\", \\\"into\\\", \\\"Greek\\\", \\\",\\\", \\\"instead\\\", \\\"of\\\", \\\"using\\\", \\\"subtitles\\\", \\\".\\\"], [\\\"This\\\", \\\"is\\\", \\\"very\\\", \\\"uncommon\\\", \\\"in\\\", \\\"Greece\\\", \\\"for\\\", \\\"anything\\\", \\\"except\\\", \\\"documentaries\\\", \\\"(\\\", \\\"using\\\", \\\"voiceover\\\", \\\"dubbing\\\", \\\")\\\", \\\"and\\\", \\\"children\\\", \\\"'s\\\", \\\"programmes\\\", \\\"(\\\", \\\"using\\\", \\\"lip\\\", \\\"-\\\", \\\"synced\\\", \\\"dubbing\\\", \\\")\\\", \\\",\\\", \\\"so\\\", \\\"after\\\", \\\"intense\\\", \\\"criticism\\\", \\\"the\\\", \\\"station\\\", \\\"switched\\\", \\\"to\\\", \\\"using\\\", \\\"subtitles\\\", \\\"for\\\", \\\"almost\\\", \\\"all\\\", \\\"foreign\\\", \\\"shows\\\", \\\".\\\"]]}, {\\\"vertexSet\\\": [[{\\\"pos\\\": [0, 2], \\\"type\\\": \\\"LOC\\\", \\\"sent_id\\\": 0, \\\"name\\\": \\\"Washington Place\\\"}, {\\\"name\\\": \\\"William Washington House\\\", \\\"pos\\\": [3, 6], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}, {\\\"pos\\\": [0, 2], \\\"type\\\": \\\"LOC\\\", \\\"sent_id\\\": 1, \\\"name\\\": \\\"Washington Place\\\"}, {\\\"pos\\\": [17, 19], \\\"type\\\": \\\"LOC\\\", \\\"sent_id\\\": 3, \\\"name\\\": \\\"Washington Place\\\"}, {\\\"pos\\\": [0, 2], \\\"type\\\": \\\"LOC\\\", \\\"sent_id\\\": 4, \\\"name\\\": \\\"Washington Place\\\"}], [{\\\"name\\\": \\\"Emancipation Proclamation\\\", \\\"pos\\\": [19, 21], \\\"sent_id\\\": 0, \\\"type\\\": \\\"MISC\\\"}], [{\\\"pos\\\": [22, 23], \\\"type\\\": \\\"TIME\\\", \\\"sent_id\\\": 0, \\\"name\\\": \\\"1863\\\"}, {\\\"pos\\\": [13, 14], \\\"type\\\": \\\"TIME\\\", \\\"sent_id\\\": 1, \\\"name\\\": \\\"1863\\\"}], [{\\\"name\\\": \\\"Hampshire County\\\", \\\"pos\\\": [24, 26], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"West Virginia\\\", \\\"pos\\\": [27, 29], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}, {\\\"name\\\": \\\"West Virginia\\\", \\\"pos\\\": [30, 32], \\\"sent_id\\\": 2, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"United States\\\", \\\"pos\\\": [30, 32], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"William\\\", \\\"pos\\\": [5, 6], \\\"sent_id\\\": 1, \\\"type\\\": \\\"PER\\\"}], [{\\\"pos\\\": [7, 9], \\\"type\\\": \\\"PER\\\", \\\"sent_id\\\": 1, \\\"name\\\": \\\"Annie Washington\\\"}], [{\\\"name\\\": \\\"Romney\\\", \\\"pos\\\": [11, 12], \\\"sent_id\\\": 2, \\\"type\\\": \\\"LOC\\\"}, {\\\"name\\\": \\\"Romney\\\", \\\"pos\\\": [11, 12], \\\"sent_id\\\": 1, \\\"type\\\": \\\"LOC\\\"}, {\\n\\n... [截断: 输出过长，省略 4279303 字符] ...\\n\\n\\\"6\\\", \\\",\\\", \\\"2011\\\", \\\"as\\\", \\\"a\\\", \\\"promotional\\\", \\\"single\\\", \\\".\\\"], [\\\"It\\\", \\\"was\\\", \\\"released\\\", \\\"as\\\", \\\"the\\\", \\\"third\\\", \\\"and\\\", \\\"final\\\", \\\"single\\\", \\\"from\\\", \\\"the\\\", \\\"album\\\", \\\"in\\\", \\\"the\\\", \\\"United\\\", \\\"States\\\", \\\",\\\", \\\"on\\\", \\\"September\\\", \\\"24\\\", \\\",\\\", \\\"2012\\\", \\\".\\\"], [\\\"The\\\", \\\"song\\\", \\\"was\\\", \\\"written\\\", \\\"by\\\", \\\"DeGraw\\\", \\\"and\\\", \\\"produced\\\", \\\"by\\\", \\\"Butch\\\", \\\"Walker\\\", \\\".\\\"], [\\\"The\\\", \\\"song\\\", \\\"finds\\\", \\\"DeGraw\\\", \\\"promising\\\", \\\"his\\\", \\\"girl\\\", \\\"everlasting\\\", \\\"love\\\", \\\",\\\", \\\"and\\\", \\\"when\\\", \\\"she\\\", \\\"needs\\\", \\\"someone\\\", \\\"he\\\", \\\"'ll\\\", \\\"always\\\", \\\"be\\\", \\\"there\\\", \\\"fighting\\\", \\\"for\\\", \\\"her\\\", \\\".\\\"], [\\\"The\\\", \\\"song\\\", \\\"has\\\", \\\"charted\\\", \\\"inside\\\", \\\"the\\\", \\\"top\\\", \\\"-\\\", \\\"forty\\\", \\\"on\\\", \\\"the\\\", \\\"Dutch\\\", \\\"chart\\\", \\\"and\\\", \\\"has\\\", \\\"also\\\", \\\"charted\\\", \\\"on\\\", \\\"the\\\", \\\"UK\\\", \\\"Singles\\\", \\\"Chart\\\", \\\"and\\\", \\\"the\\\", \\\"Adult\\\", \\\"Pop\\\", \\\"Songs\\\", \\\"chart\\\", \\\".\\\"], [\\\"DeGraw\\\", \\\"appeared\\\", \\\"on\\\", \\\"the\\\", \\\"last\\\", \\\"episode\\\", \\\"of\\\", \\\"One\\\", \\\"Tree\\\", \\\"Hill\\\", \\\"and\\\", \\\"performed\\\", \\\"the\\\", \\\"track\\\", \\\".\\\"]]}, {\\\"vertexSet\\\": [[{\\\"name\\\": \\\"Paul E. Pfeifer\\\", \\\"pos\\\": [0, 3], \\\"sent_id\\\": 0, \\\"type\\\": \\\"PER\\\"}, {\\\"name\\\": \\\"Pfeifer\\\", \\\"pos\\\": [0, 1], \\\"sent_id\\\": 7, \\\"type\\\": \\\"PER\\\"}, {\\\"type\\\": \\\"PER\\\", \\\"pos\\\": [0, 1], \\\"name\\\": \\\"Pfeifer\\\", \\\"sent_id\\\": 2}, {\\\"type\\\": \\\"PER\\\", \\\"pos\\\": [0, 1], \\\"name\\\": \\\"Pfeifer\\\", \\\"sent_id\\\": 8}], [{\\\"type\\\": \\\"TIME\\\", \\\"pos\\\": [5, 9], \\\"name\\\": \\\"October 15, 1942\\\", \\\"sent_id\\\": 0}], [{\\\"name\\\": \\\"American\\\", \\\"pos\\\": [12, 13], \\\"sent_id\\\": 0, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Ohio General Assembly\\\", \\\"pos\\\": [7, 10], \\\"sent_id\\\": 1, \\\"type\\\": \\\"ORG\\\"}], [{\\\"name\\\": \\\"Ohio Republican party\\\", \\\"pos\\\": [15, 18], \\\"sent_id\\\": 1, \\\"type\\\": \\\"ORG\\\"}], [{\\\"name\\\": \\\"Supreme Court of Ohio\\\", \\\"pos\\\": [27, 31], \\\"sent_id\\\": 1, \\\"type\\\": \\\"ORG\\\"}], [{\\\"name\\\": \\\"Bucyrus\\\", \\\"pos\\\": [4, 5], \\\"sent_id\\\": 2, \\\"type\\\": \\\"LOC\\\"}, {\\\"name\\\": \\\"Bucyrus\\\", \\\"pos\\\": [10, 11], \\\"sent_id\\\": 3, \\\"type\\\": \\\"LOC\\\"}], [{\\\"type\\\": \\\"TIME\\\", \\\"pos\\\": [6, 7], \\\"name\\\": \\\"1942\\\", \\\"sent_id\\\": 2}], [{\\\"name\\\": \\\"Yorkshire\\\", \\\"pos\\\": [7, 8], \\\"sent_id\\\": 4, \\\"type\\\": \\\"LOC\\\"}], [{\\\"type\\\": \\\"TIME\\\", \\\"pos\\\": [16, 17], \\\"name\\\": \\\"1963\\\", \\\"sent_id\\\": 5}], [{\\\"name\\\": \\\"Ohio State University\\\", \\\"pos\\\": [18, 21], \\\"sent_id\\\": 5, \\\"type\\\": \\\"ORG\\\"}], [{\\\"type\\\": \\\"TIME\\\", \\\"pos\\\": [1, 2], \\\"name\\\": \\\"1966\\\", \\\"sent_id\\\": 6}], [{\\\"name\\\": \\\"College of Law\\\", \\\"pos\\\": [11, 14], \\\"sent_id\\\": 6, \\\"type\\\": \\\"ORG\\\"}], [{\\\"name\\\": \\\"Crawford County\\\", \\\"pos\\\": [6, 8], \\\"sent_id\\\": 7, \\\"type\\\": \\\"LOC\\\"}], [{\\\"name\\\": \\\"Julia\\\", \\\"pos\\\": [4, 5], \\\"sent_id\\\": 8, \\\"type\\\": \\\"PER\\\"}], [{\\\"name\\\": \\\"three\\\", \\\"pos\\\": [6, 7], \\\"sent_id\\\": 8, \\\"type\\\": \\\"NUM\\\"}], [{\\\"name\\\": \\\"four\\\", \\\"pos\\\": [9, 10], \\\"sent_id\\\": 8, \\\"type\\\": \\\"NUM\\\"}]], \\\"labels\\\": [{\\\"r\\\": \\\"P569\\\", \\\"h\\\": 0, \\\"t\\\": 7, \\\"evidence\\\": [0, 2]}, {\\\"r\\\": \\\"P69\\\", \\\"h\\\": 0, \\\"t\\\": 10, \\\"evidence\\\": [2, 5]}, {\\\"r\\\": \\\"P69\\\", \\\"h\\\": 0, \\\"t\\\": 12, \\\"evidence\\\": [2, 6]}, {\\\"r\\\": \\\"P102\\\", \\\"h\\\": 0, \\\"t\\\": 4, \\\"evidence\\\": [0, 1]}, {\\\"r\\\": \\\"P19\\\", \\\"h\\\": 0, \\\"t\\\": 6, \\\"evidence\\\": [2]}, {\\\"r\\\": \\\"P27\\\", \\\"h\\\": 0, \\\"t\\\": 2, \\\"evidence\\\": [0]}, {\\\"r\\\": \\\"P569\\\", \\\"h\\\": 0, \\\"t\\\": 1, \\\"evidence\\\": [0]}], \\\"title\\\": \\\"Paul Pfeifer\\\", \\\"sents\\\": [[\\\"Paul\\\", \\\"E.\\\", \\\"Pfeifer\\\", \\\"(\\\", \\\"born\\\", \\\"October\\\", \\\"15\\\", \\\",\\\", \\\"1942\\\", \\\")\\\", \\\"is\\\", \\\"an\\\", \\\"American\\\", \\\"jurist\\\", \\\".\\\"], [\\\"He\\\", \\\"served\\\", \\\"in\\\", \\\"both\\\", \\\"houses\\\", \\\"of\\\", \\\"the\\\", \\\"Ohio\\\", \\\"General\\\", \\\"Assembly\\\", \\\"as\\\", \\\"a\\\", \\\"member\\\", \\\"of\\\", \\\"the\\\", \\\"Ohio\\\", \\\"Republican\\\", \\\"party\\\", \\\"and\\\", \\\"was\\\", \\\"most\\\", \\\"recently\\\", \\\"an\\\", \\\"Associate\\\", \\\"Justice\\\", \\\"of\\\", \\\"the\\\", \\\"Supreme\\\", \\\"Court\\\", \\\"of\\\", \\\"Ohio\\\", \\\".\\\"], [\\\"Pfeifer\\\", \\\"was\\\", \\\"born\\\", \\\"in\\\", \\\"Bucyrus\\\", \\\"in\\\", \\\"1942\\\", \\\".\\\"], [\\\"He\\\", \\\"grew\\\", \\\"up\\\", \\\"on\\\", \\\"his\\\", \\\"family\\\", \\\"'s\\\", \\\"dairy\\\", \\\"farm\\\", \\\"near\\\", \\\"Bucyrus\\\", \\\".\\\"], [\\\"As\\\", \\\"a\\\", \\\"teenager\\\", \\\",\\\", \\\"he\\\", \\\"raised\\\", \\\"purebred\\\", \\\"Yorkshire\\\", \\\"hogs\\\", \\\"to\\\", \\\"finance\\\", \\\"his\\\", \\\"college\\\", \\\"education\\\", \\\".\\\"], [\\\"He\\\", \\\"earned\\\", \\\"a\\\", \\\"bachelor\\\", \\\"of\\\", \\\"arts\\\", \\\"degree\\\", \\\"in\\\", \\\"economics\\\", \\\",\\\", \\\"political\\\", \\\"science\\\", \\\",\\\", \\\"and\\\", \\\"history\\\", \\\"in\\\", \\\"1963\\\", \\\"from\\\", \\\"Ohio\\\", \\\"State\\\", \\\"University\\\", \\\".\\\"], [\\\"In\\\", \\\"1966\\\", \\\",\\\", \\\"he\\\", \\\"also\\\", \\\"earned\\\", \\\"a\\\", \\\"law\\\", \\\"degree\\\", \\\"from\\\", \\\"the\\\", \\\"College\\\", \\\"of\\\", \\\"Law\\\", \\\".\\\"], [\\\"Pfeifer\\\", \\\"owns\\\", \\\"a\\\", \\\"cattle\\\", \\\"farm\\\", \\\"in\\\", \\\"Crawford\\\", \\\"County\\\", \\\",\\\", \\\"near\\\", \\\"his\\\", \\\"childhood\\\", \\\"home\\\", \\\".\\\"], [\\\"Pfeifer\\\", \\\"and\\\", \\\"his\\\", \\\"wife\\\", \\\"Julia\\\", \\\"have\\\", \\\"three\\\", \\\"children\\\", \\\"and\\\", \\\"four\\\", \\\"grandchildren\\\", \\\".\\\"]]}]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.26}}"
    }
  },
  "sourceToolAssistantUUID": "4c877fd2-a296-4377-ac39-dbdf34353070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 64 · 2026-05-23T05:48:38.770Z_

```json
{
  "parentUuid": "c9b5044b-0e0a-4631-80e8-05f191506efa",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "013bf1d6-80a3-4e9a-94fd-ae38a502674a",
  "timestamp": "2026-05-23T05:48:38.770Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "leafUuid": "013bf1d6-80a3-4e9a-94fd-ae38a502674a",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "DocRED INT4 quantization comparison experiments",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Assistant

_source line 67 · 2026-05-23T05:48:46.889Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to find the DocRED FP16 S1 baselines for the 8B models. Let me search for the specific experiments. The registry output was too large, so let me read the saved file or search more specifically.

From the data I already have, the DocRED dev.json has 998 docs. Previous experiments used:
- 200-doc subset (for 70B experiments)
- 998 full dev set (for 8B experiments like w8_llama_docred_ft_grammar_only)

Let me search for the 8B DocRED FP16 S1 constrained results. I need experiments like:


- w5_lora_docred_constrained_eval (Qwen)
- w5_llama_docred_constrained_eval (Llama)

Or the equivalent full_s1 runs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "013bf1d6-80a3-4e9a-94fd-ae38a502674a",
  "isSidechain": false,
  "requestId": "req_011CbJyWC9MV5XZmCPCzxjjr",
  "type": "assistant",
  "uuid": "5cd8cbd8-f47d-49a5-97e1-87fa123a2716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bjmqL6SqGQnFJS1TdTUid",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9161,
      "cache_read_input_tokens": 66237,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 429,
          "cache_read_input_tokens": 66237,
          "cache_creation_input_tokens": 9161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9161
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

_source line 68 · 2026-05-23T05:48:47.285Z_

需要找 8B DocRED FP16 S1 baseline。读取保存的完整 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cd8cbd8-f47d-49a5-97e1-87fa123a2716",
  "isSidechain": false,
  "requestId": "req_011CbJyWC9MV5XZmCPCzxjjr",
  "type": "assistant",
  "uuid": "a9804396-0d6f-4587-bdc5-fbb3c1f07285",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bjmqL6SqGQnFJS1TdTUid",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9161,
      "cache_read_input_tokens": 66237,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 429,
          "cache_read_input_tokens": 66237,
          "cache_creation_input_tokens": 9161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9161
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

_source line 69 · 2026-05-23T05:48:51.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_013Sr4gX6VKaFHndc4ZSpWeX`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bcaaae93-c135-4568-bb9e-6ae384bb4c94/tool-results/toolu_01H7QuMX9omP89o2Pv4uSG5u.txt",
  "offset": 0,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9804396-0d6f-4587-bdc5-fbb3c1f07285",
  "isSidechain": false,
  "requestId": "req_011CbJyWC9MV5XZmCPCzxjjr",
  "type": "assistant",
  "uuid": "9a65401c-24fe-4389-9a20-39cc39a71833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bjmqL6SqGQnFJS1TdTUid",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9161,
      "cache_read_input_tokens": 66237,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 429,
          "cache_read_input_tokens": 66237,
          "cache_creation_input_tokens": 9161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9161
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

_source line 70 · 2026-05-23T05:48:52.032Z_

<details><summary>↩ Tool result · `toolu_013Sr4gX6VKaFHndc4ZSpWeX`</summary>

```text
0	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test (551 docs)\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}, \"conclusion\": \"success\"}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test 551 sentences\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}, \"conclusion\": \"success\"}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 100, \"model_name\": \"GoLLIE-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/gollie_model/\", \"eval_data\": \"SciERC test (100 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/gollie_model/\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\"}, \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 88678, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_full_s1.log\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 984253, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_grammar_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}, \"conclusion\": \"negative\"}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 983803, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 84588, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_unconstrained.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"eval_data\": \"DocRED dev 200-doc subset\", \"checkpoint_source\": \"n/a (zero-shot)\", \"log_path\": \"/tmp/70b_zs_docred_200_grammar_only.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}, \"conclusion\": \"negative\"}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 70638, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\", \"log_path\": \"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\", \"note\": \"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\"}, \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}, \"conclusion\": \"success\"}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_grammar_only.log\", \"pid\": 70175}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 74572, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_scierc_unconstrained.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 972139, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_full_s2.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 971668, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 967058, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/entity_order_shuffled_qwen_scierc.log\", \"shuffle_seed\": 42, \"original_entity_order\": [\"Task\", \"Method\", \"Material\", \"Metric\", \"OtherScientificTerm\", \"Generic\"], \"shuffled_entity_order\": [\"Metric\", \"Method\", \"Material\", \"OtherScientificTerm\", \"Task\", \"Generic\"], \"original_relation_order\": [\"Used-for\", \"Feature-of\", \"Hyponym-of\", \"Part-of\", \"Compare\", \"Conjunction\", \"Evaluate-for\"], \"shuffled_relation_order\": [\"Conjunction\", \"Evaluate-for\", \"Compare\", \"Part-of\", \"Feature-of\", \"Hyponym-of\", \"Used-for\"]}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"r16_70b_scierc_zs_s1\", \"eval_data\": \"scierc test set (551 docs)\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_grammar_only.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_beam4_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/beam4_tcr_llama_scierc.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}, \"conclusion\": \"negative\"}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/beam_tcr_run.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 0}, \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": \"11466\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"200 (first 200 docs)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\", \"log_path\": \"westd-21461:/tmp/constrained_inference.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"spec\": {\"command\": \"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\", \"server\": \"westd-16980 + westd-21461\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"note\": \"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\"}, \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}, \"conclusion\": \"success\"}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}, \"conclusion\": \"success\"}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}, \"conclusion\": \"success\"}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\"}, \"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}, \"conclusion\": \"success\"}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\"}, \"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\"run_constrained_extraction.py\\\", run_name=\\\"__main__\\\")'\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"998 (truncated to 200)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}}, \"eval_70b_lora_scierc_s1_constrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\"}, \"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}, \"conclusion\": \"success\"}, \"eval_70b_lora_scierc_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"scierc test (551 sentences)\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.5, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1806, \"relations\": 1133}}, \"r16_70b_docred_zs_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 69.11, \"R_F1\": 13.05, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.04, \"parse_fail_pct\": 0.1, \"samples\": 998, \"total_entities\": 16599, \"total_triples\": 13239, \"baseline_unc_DR_pct\": 14.98, \"baseline_unc_R_F1\": 13.01, \"note\": \"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\"}}, \"d066_sweep_llama_beam8_unc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --output_file /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 755444. Relay from Llama beam2 s1 (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam8_unc.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.77, \"E_P\": 85.7, \"E_R\": 85.84, \"R_F1\": 51.97, \"R_P\": 49.76, \"R_R\": 54.38, \"DR_pct\": 0, \"CF_pct\": 0.05, \"ET_pct\": 0, \"RV_pct\": 0.07, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3788, \"total_relations_pred\": 2779}}, \"d066_sweep_llama_beam2_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --max_samples 200 --seed 42\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 750801. Relay from Llama beam2 unc (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam2_full_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam2_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.6, \"E_P\": 85.29, \"E_R\": 85.92, \"R_F1\": 51.17, \"R_P\": 48.51, \"R_R\": 54.14, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3814, \"total_relations_pred\": 2839}}, \"d066_sweep_llama_docred_beam4_s1\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_constrained.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam4_s1.log\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR%\": 0, \"CF%\": 0, \"PF%\": 0.5, \"ET%\": 0, \"RV%\": 0, \"samples\": 200, \"parse_fail\": 1}, \"command\": \"d066 beam sweep llama docred beam4 s1 (completed, retroactive fix)\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B-Instruct + LoRA\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"ET_pct\": 0, \"RV_pct\": 0, \"samples\": 200, \"parse_fail\": 1}}, \"r16_70b_lora_docred\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 scripts/train_lora_70b_docred.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/sft_train_llama.jsonl\", \"data_count\": 3053, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/train.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"/root/schema_semantic_constrained_ie/data/docred/sft_dev_llama.jsonl\", \"pid\": 839375, \"gpu_ids\": [1], \"note\": \"Restarted from scratch (previous run killed, empty checkpoint dir). LoRA r=16 alpha=32 on q/k/v/o_proj. bs=1 grad_accum=8 lr=2e-5 3epochs. ~10.4h ETA.\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0635, \"token_acc\": 97.94, \"steps_completed\": 1146, \"epochs\": 3, \"train_loss_start\": 0.147, \"train_loss_end\": 0.056}}, \"r16_70b_lora_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 train_70b_lora.py --dataset scierc --model_path /root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ-INT4 --output_dir /root/autodl-tmp/checkpoints/70b_lora_scierc --epochs 3 --lr 2e-4 --lora_r 16 --lora_alpha 32\", \"server\": \"westd-16980\", \"data_path\": \"data/sft/scierc_sft_train.jsonl\", \"data_count\": 1762, \"model_name\": \"Llama-3.3-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/train.log\", \"pid\": 836206, \"gpu_ids\": [0, 1]}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0611, \"token_acc\": 97.78, \"steps_completed\": 663, \"epochs\": 3, \"train_loss_start\": 0.183, \"train_loss_end\": 0.041}}, \"r16_70b_scierc_zs_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 808988, \"data_path\": \"SciERC test set (551 sentences)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A (ZS eval)\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log\"}, \"metrics\": {\"E_F1\": 35.19, \"R_F1\": 11.24, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 3.5, \"parse_fail_pct\": 0, \"samples\": 551, \"baseline_unc_E_F1\": 35.21, \"baseline_unc_R_F1\": 11.15, \"baseline_unc_DR_pct\": 6.41, \"baseline_unc_RV_pct\": 0.61, \"baseline_unc_CF_pct\": 0}, \"conclusion\": \"success\"}, \"r14_qwen_docred_beam4_998\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl --device cuda:0 --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"E_F1\": 58.19, \"R_F1\": 8.72, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 4.94, \"parse_fail_pct\": 3.51, \"samples\": 998, \"success\": 963, \"fail\": 35}, \"conclusion\": \"success\"}, \"r16_trie_llama_zs_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_zs.log\"}, \"metrics\": {\"E_F1\": 23.23, \"R_F1\": 2.9, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 84.4, \"CF_pct\": 0.36, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\"}, \"r16_trie_qwen_zs_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_zs.log\"}, \"metrics\": {\"E_F1\": 30.97, \"R_F1\": 8.64, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 29.3, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\"}, \"r14_llama_docred_beam4_998\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --output_path /root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.jsonl --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.log\"}, \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 8.83, \"E_F1\": 57.81, \"DR_pct\": 0, \"CF_pct\": 1, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 3.91, \"samples\": 998, \"success\": 959, \"fail\": 39, \"baseline_ZS_greedy_R_F1\": 6.27, \"baseline_ZS_greedy_E_F1\": 54.93, \"baseline_ZS_greedy_DR_pct\": 2.55, \"baseline_ZS_greedy_CF_pct\": 8.54}}, \"d066_sweep_llama_scierc_beam8_s1_551\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam8_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 67.51, \"E-P\": 64.99, \"E-R\": 70.23, \"R-F1\": 44.95, \"R-P\": 40.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0, \"samples\": 551, \"note\": \"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\"}}, \"d066_sweep_llama_scierc_beam4_s1_551\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 68.06, \"E-P\": 65.96, \"E-R\": 70.29, \"R-F1\": 46.18, \"R-P\": 42.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"parse_fail\": 0, \"samples\": 551, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42}}, \"d066_sweep_llama_docred_beam4_unc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 761033. Relay from Llama beam8 unc (success).\"}, \"metrics\": {\"E-F1\": 85.67, \"R-F1\": 52.65, \"DR_pct\": 0.04, \"CF_pct\": 0.08, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\"}, \"d066_sweep_llama_docred_beam1_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 209444. Relay from beam1 unc (success).\"}, \"metrics\": {\"E-F1\": 85.43, \"R-F1\": 47.35, \"DR_pct\": 0, \"CF_pct\": 0.19, \"PF_pct\": 2, \"samples\": 200}, \"conclusion\": \"success\"}, \"d066_sweep_llama_beam8_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-16980 GPU0\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 756540. Relay after GPU0 freed.\"}, \"metrics\": {\"E-F1\": 85.76, \"R-F1\": 51.74, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\"}, \"d065_qwen_greedy_4096_r2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --decoding_strategy greedy --max_new_tokens 4096 --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --output_file /root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096_rerun.jsonl --seed 42\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (998 docs, constrained decoding inference)\", \"note\": \"Rerun after dual-process corruption. PID 194615.\"}, \"metrics\": {\"E-F1\": 81.87, \"R-F1\": 40.79, \"DR_pct\": 0, \"CF_pct\": 0.22, \"ET_pct\": 0, \"RV_pct\": 0, \"PF_pct\": 8.52, \"samples\": 998}, \"conclusion\": \"success\"}, \"d066_sweep_llama_scierc_beam2_s1_551\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"conclusion\": \"success\", \"metrics\": {\"entity_f1\": 68.34, \"entity_p\": 66.59, \"entity_r\": 70.17, \"relation_f1\": 46.12, \"relation_p\": 42.73, \"relation_r\": 50.1, \"parse_fail_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.17, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}}, \"d066_sweep_llama_scierc_beam1_unc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --seed 42\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/scierc/test.json (551 docs)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B LoRA SciERC (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/scierc/test.json\", \"note\": \"PID 205314. Relay from Qwen beam8 s1 SciERC (success).\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unconstrained.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unc.log\"}, \"conclusion\": \"failed\", \"metrics\": {\"total\": 275, \"success\": 275, \"fail\": 0, \"output_file\": \"llama_scierc_beam1_unconstrained.jsonl\", \"note\": \"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\"}}}, \"count\": 50, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4881}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a65401c-24fe-4389-9a20-39cc39a71833",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "625832cb-5960-46e4-8a26-e368c7cbd214",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bcaaae93-c135-4568-bb9e-6ae384bb4c94/tool-results/toolu_01H7QuMX9omP89o2Pv4uSG5u.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"sf2_llama_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-SciERC-FT-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\\\", \\\"eval_data\\\": \\\"SciERC test (551 docs)\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.94, \\\"R-F1\\\": 43.98, \\\"E-F1\\\": 67.54, \\\"samples\\\": 551, \\\"R-P\\\": 40.47, \\\"R-R\\\": 48.15, \\\"E-P\\\": 65.51, \\\"E-R\\\": 69.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sf2_qwen_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-SciERC-FT-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\\\", \\\"eval_data\\\": \\\"SciERC test 551 sentences\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 1.1, \\\"R-F1\\\": 41.71, \\\"E-F1\\\": 67.05, \\\"samples\\\": 551, \\\"R-P\\\": 38.52, \\\"R-R\\\": 45.48, \\\"E-P\\\": 64.76, \\\"E-R\\\": 69.52}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sf2_gollie_scierc_violation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"GoLLIE-7B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/gollie_model/\\\", \\\"eval_data\\\": \\\"SciERC test (100 docs)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gollie_model/\\\", \\\"log_path\\\": \\\"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\\\"}, \\\"metrics\\\": {\\\"GoLLIE_ZS\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.83, \\\"E_F1\\\": 9.17, \\\"R_F1\\\": 0, \\\"pred_ents\\\": 241, \\\"pred_rels\\\": 5, \\\"docs_with_output\\\": 54}, \\\"OntoCoDec_Qwen_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.61, \\\"E_F1\\\": 66.43, \\\"R_F1\\\": 43.69}, \\\"OntoCoDec_Llama_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.62, \\\"E_F1\\\": 67.09, \\\"R_F1\\\": 45.47}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_zs_docred_200_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 88678, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_full_s1.log\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 5.34, \\\"E-F1\\\": 70.05, \\\"R-F1\\\": 13.25, \\\"PF%\\\": 0, \\\"entities_pred\\\": 3234, \\\"relations_pred\\\": 2637, \\\"triples_checked\\\": 2642}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 984253, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_docred_200_grammar_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 10.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.38, \\\"CF_pct\\\": 0.06, \\\"E_F1\\\": 80.13, \\\"E_P\\\": 85.16, \\\"E_R\\\": 75.66, \\\"R_F1\\\": 43.96, \\\"R_P\\\": 39.78, \\\"R_R\\\": 49.11, \\\"entities_pred\\\": 3362, \\\"relations_pred\\\": 3154}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_70b_lora_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 983803, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_docred_200_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 11, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.51, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.21, \\\"E_F1\\\": 80.06, \\\"E_P\\\": 85.21, \\\"E_R\\\": 75.5, \\\"R_F1\\\": 43.61, \\\"R_P\\\": 39.44, \\\"R_R\\\": 48.75, \\\"entities_pred\\\": 3351, \\\"relations_pred\\\": 3148}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_zs_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 84588, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_unconstrained.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities_pred\\\": 3242, \\\"relations_pred\\\": 2637, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 7.88, \\\"DR_pct\\\": 13.45, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 8, \\\"E_F1\\\": 70.14, \\\"E_P\\\": 75.85, \\\"E_R\\\": 65.23, \\\"R_F1\\\": 13.25, \\\"R_P\\\": 12.97, \\\"R_R\\\": 13.54}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_zs_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"eval_data\\\": \\\"DocRED dev 200-doc subset\\\", \\\"checkpoint_source\\\": \\\"n/a (zero-shot)\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_grammar_only.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 1, \\\"entities_pred\\\": 3221, \\\"relations_pred\\\": 2609, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 17.03, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"E_F1\\\": 70.12, \\\"E_P\\\": 75.88, \\\"E_R\\\": 65.17, \\\"R_F1\\\": 13.23, \\\"R_P\\\": 12.99, \\\"R_R\\\": 13.47}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_70b_zs_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities\\\": 3240, \\\"relations\\\": 2596, \\\"ET_pct\\\": 0.12, \\\"RV_pct\\\": 8.24, \\\"DR_pct\\\": 1.66, \\\"CF_count\\\": 132, \\\"CF_pct\\\": 4.07, \\\"E_F1\\\": 70.1, \\\"E_P\\\": 75.87, \\\"E_R\\\": 65.15, \\\"R_F1\\\": 13.05, \\\"R_P\\\": 12.88, \\\"R_R\\\": 13.23, \\\"fuzzy_matches\\\": 8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\\\", \\\"pid\\\": 70638, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\\\", \\\"note\\\": \\\"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.57, \\\"E-P\\\": 85.45, \\\"E-R\\\": 85.68, \\\"R-F1\\\": 48.14, \\\"R-P\\\": 44.24, \\\"R-R\\\": 52.79, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"parse_fail\\\": \\\"1/200 (0.5%)\\\", \\\"entities_pred\\\": 3790, \\\"relations_pred\\\": 3030}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_grammar_only.log\\\", \\\"pid\\\": 70175}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"json_failure_rate\\\": 0, \\\"entities\\\": 1805, \\\"relations\\\": 1133, \\\"entity_type_violations\\\": 0, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocab_violations\\\": 0, \\\"relation_vocab_violation_rate\\\": 0, \\\"domain_range_violations\\\": 17, \\\"domain_range_violation_rate\\\": 0.015, \\\"cross_field_consistency_violations\\\": 0, \\\"fuzzy_relation_matches\\\": 0, \\\"entity_P\\\": 0.6272, \\\"entity_R\\\": 0.6707, \\\"entity_F1\\\": 0.6482, \\\"relation_P\\\": 0.4152, \\\"relation_R\\\": 0.4825, \\\"relation_F1\\\": 0.4463}}, \\\"eval_70b_zs_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\\\", \\\"pid\\\": 74572, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_scierc_unconstrained.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 2353, \\\"relations\\\": 1483, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.6, \\\"DR_pct\\\": 6.4, \\\"CF_count\\\": 0, \\\"E_F1\\\": 35.22, \\\"E_P\\\": 30.13, \\\"E_R\\\": 42.38, \\\"R_F1\\\": 11.23, \\\"R_P\\\": 9.31, \\\"R_R\\\": 14.17, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_full_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 972139, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_full_s2.log\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1531, \\\"relations\\\": 1027, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 18, \\\"E_F1\\\": 62.35, \\\"E_P\\\": 65.44, \\\"E_R\\\": 59.53, \\\"R_F1\\\": 36.28, \\\"R_P\\\": 35.35, \\\"R_R\\\": 37.27, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 971668, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_semantic_only.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1806, \\\"relations\\\": 1133, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.6, \\\"CF_count\\\": 9, \\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"parse_fail_pct\\\": 0}}, \\\"entity_order_ablation_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 967058, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-LoRA-SciERC-merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"log_path\\\": \\\"/tmp/entity_order_shuffled_qwen_scierc.log\\\", \\\"shuffle_seed\\\": 42, \\\"original_entity_order\\\": [\\\"Task\\\", \\\"Method\\\", \\\"Material\\\", \\\"Metric\\\", \\\"OtherScientificTerm\\\", \\\"Generic\\\"], \\\"shuffled_entity_order\\\": [\\\"Metric\\\", \\\"Method\\\", \\\"Material\\\", \\\"OtherScientificTerm\\\", \\\"Task\\\", \\\"Generic\\\"], \\\"original_relation_order\\\": [\\\"Used-for\\\", \\\"Feature-of\\\", \\\"Hyponym-of\\\", \\\"Part-of\\\", \\\"Compare\\\", \\\"Conjunction\\\", \\\"Evaluate-for\\\"], \\\"shuffled_relation_order\\\": [\\\"Conjunction\\\", \\\"Evaluate-for\\\", \\\"Compare\\\", \\\"Part-of\\\", \\\"Feature-of\\\", \\\"Hyponym-of\\\", \\\"Used-for\\\"]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 67.05, \\\"E_P\\\": 65.23, \\\"E_R\\\": 68.98, \\\"R_F1\\\": 43.77, \\\"R_P\\\": 40.78, \\\"R_R\\\": 47.23, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 21, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1784, \\\"relations\\\": 1128, \\\"corrected_original_R_F1\\\": 43.77, \\\"corrected_original_E_F1\\\": 67.05, \\\"corrected_original_DR_pct\\\": 0, \\\"corrected_original_CF_count\\\": 21, \\\"corrected_delta_R_F1\\\": 0, \\\"corrected_delta_E_F1\\\": 0, \\\"raw_output_identical\\\": true, \\\"parsed_output_identical\\\": true, \\\"note\\\": \\\"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\\\"}}, \\\"eval_70b_zs_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"r16_70b_scierc_zs_s1\\\", \\\"eval_data\\\": \\\"scierc test set (551 docs)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/eval_70b_zs_scierc_semantic_only.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.37, \\\"DR_pct\\\": 1.01, \\\"RV_pct\\\": 0.6, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 76, \\\"samples\\\": 551}}, \\\"eval_70b_zs_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/eval_70b_zs_scierc_grammar_only.log\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"R_F1\\\": 11.23, \\\"DR_pct\\\": 6.33, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 0, \\\"samples\\\": 551}}, \\\"eval_70b_lora_scierc_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_beam4_s1.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 64.89, \\\"E_P\\\": 62.29, \\\"E_R\\\": 67.72, \\\"R_F1\\\": 44.81, \\\"R_P\\\": 39.45, \\\"R_R\\\": 51.85, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 1, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1839, \\\"relations\\\": 1283}}, \\\"tcr_beam4_llama_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/beam4_tcr_llama_scierc.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1803, \\\"relations\\\": 1194, \\\"entity_type_violations\\\": \\\"0/1803 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1194 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"13/1194 (1.1%)\\\", \\\"cross_field_consistency\\\": 0, \\\"DR_pct\\\": 1.09, \\\"E_F1\\\": 68.02, \\\"E_P\\\": 65.88, \\\"E_R\\\": 70.29, \\\"R_F1\\\": 46.05, \\\"R_P\\\": 41.83, \\\"R_R\\\": 51.23, \\\"tcr_changed_selection\\\": \\\"0/551 (0.0%)\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"tcr_beam4_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-LoRA-SciERC-merged\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"log_path\\\": \\\"/tmp/beam_tcr_run.log\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1802, \\\"relations\\\": 1250, \\\"entity_type_violations\\\": \\\"0/1802 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1250 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"23/1250 (1.8%)\\\", \\\"cross_field_consistency_violations\\\": 1, \\\"DR_pct\\\": 1.84, \\\"E_P\\\": 65.05, \\\"E_R\\\": 69.64, \\\"E_F1\\\": 67.26, \\\"R_P\\\": 39.36, \\\"R_R\\\": 50.51, \\\"R_F1\\\": 44.24, \\\"TCR_changed_selection\\\": \\\"0/551 (0.0%)\\\", \\\"all_candidates_TCR_1.0\\\": true}}, \\\"vllm_guided_json_scierc_zs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B\\\", \\\"seed\\\": 0}, \\\"metrics\\\": {\\\"DR%\\\": 15.26, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.04, \\\"R-F1\\\": 8.75, \\\"E-F1\\\": 30.91, \\\"parse_fail%\\\": 0, \\\"total_samples\\\": 551, \\\"total_entities\\\": 2485, \\\"total_relations\\\": 1724, \\\"inference_time_s\\\": 108.5}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"11466\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": \\\"200 (first 200 docs)\\\", \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/tmp/constrained_inference.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 79.38, \\\"E_P\\\": 85.24, \\\"E_R\\\": 74.28, \\\"R_F1\\\": 43.95, \\\"R_P\\\": 40.48, \\\"R_R\\\": 48.08, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.18, \\\"parse_fail_pct\\\": 12.5, \\\"samples\\\": 200}}, \\\"d066_beam_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\\\", \\\"server\\\": \\\"westd-16980 + westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"note\\\": \\\"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\\\"}, \\\"metrics\\\": {\\\"scierc_qwen3_8b\\\": {\\\"k1_unc\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 2.11, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.494}, \\\"k1_con\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.5, \\\"avg_time\\\": 2.932}, \\\"k2_unc\\\": {\\\"E_F1\\\": 67.79, \\\"R_F1\\\": 44.75, \\\"DR_pct\\\": 1.54, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.954}, \\\"k2_con\\\": {\\\"E_F1\\\": 67.71, \\\"R_F1\\\": 44.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.11, \\\"avg_time\\\": 3.463}, \\\"k4_unc\\\": {\\\"E_F1\\\": 67.49, \\\"R_F1\\\": 43.72, \\\"DR_pct\\\": 1.89, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 3.485}, \\\"k4_con\\\": {\\\"E_F1\\\": 67.22, \\\"R_F1\\\": 43.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.069}, \\\"k8_unc\\\": {\\\"E_F1\\\": 66.4, \\\"R_F1\\\": 43.17, \\\"DR_pct\\\": 1.77, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.194}, \\\"k8_con\\\": {\\\"E_F1\\\": 66.36, \\\"R_F1\\\": 43.65, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 5.058}}, \\\"pareto_optimal\\\": \\\"k=2 con\\\", \\\"best_E_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 67.79}, \\\"best_R_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 44.75}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"w8_llama_docred_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"llama_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"w5_llama_docred_lora\\\", \\\"eval_data\\\": \\\"docred_dev_998\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"R_F1\\\": 43.72, \\\"R_P\\\": 38.57, \\\"R_R\\\": 50.44, \\\"parse_fail_pct\\\": 2.3, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\\\"}}, \\\"w8_llama_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\\\\\"\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": 1, \\\"pid\\\": 361202, \\\"model_name\\\": \\\"Llama-3.1-8B-LoRA-DocRED\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 43.85, \\\"R_P\\\": 38.85, \\\"R_R\\\": 50.31, \\\"parse_fail_pct\\\": 2.4, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"w8_qwen_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"qwen_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"qwen_lora_docred_merged\\\", \\\"eval_data\\\": \\\"docred_test_998\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"log_path\\\": \\\"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 40.85, \\\"R_P\\\": 36.33, \\\"R_R\\\": 46.65, \\\"parse_fail_pct\\\": 7.52, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_qwen_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B (fine-tuned)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 64.4, \\\"E_P\\\": 66.8, \\\"E_R\\\": 62.16, \\\"R_F1\\\": 41.16, \\\"R_P\\\": 38.24, \\\"R_R\\\": 44.56, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 95.5, \\\"CF_pct\\\": 0.09, \\\"parse_fail_pct\\\": 9.1, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_llama_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (fine-tuned)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 36.66, \\\"E_P\\\": 67.47, \\\"E_R\\\": 25.16, \\\"R_F1\\\": 19.95, \\\"R_P\\\": 41.42, \\\"R_R\\\": 13.14, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 15.2, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 50.8, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\\\\\"run_constrained_extraction.py\\\\\\\", run_name=\\\\\\\"__main__\\\\\\\")'\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": \\\"998 (truncated to 200)\\\", \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 80.34, \\\"E_P\\\": 85.13, \\\"E_R\\\": 76.05, \\\"R_F1\\\": 43.8, \\\"R_P\\\": 39.6, \\\"R_R\\\": 48.99, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.57, \\\"DR_pct\\\": 0.22, \\\"CF_pct\\\": 0.06, \\\"parse_fail_pct\\\": 10, \\\"samples\\\": 200, \\\"relations\\\": 3159, \\\"RV_count\\\": 18, \\\"DR_count\\\": 7, \\\"CF_count\\\": 2}}, \\\"eval_70b_lora_scierc_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\\\"}, \\\"metrics\\\": {\\\"entity_f1\\\": 0.6476, \\\"entity_precision\\\": 0.6266, \\\"entity_recall\\\": 0.6701, \\\"relation_f1\\\": 0.4453, \\\"relation_precision\\\": 0.4149, \\\"relation_recall\\\": 0.4805, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 15, \\\"parse_fail_pct\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"num_samples\\\": 551, \\\"num_entities\\\": 1805, \\\"num_relations\\\": 1129}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_70b_lora_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"scierc test (551 sentences)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 1.5, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1806, \\\"relations\\\": 1133}}, \\\"r16_70b_docred_zs_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"model_path\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 69.11, \\\"R_F1\\\": 13.05, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.04, \\\"parse_fail_pct\\\": 0.1, \\\"samples\\\": 998, \\\"total_entities\\\": 16599, \\\"total_triples\\\": 13239, \\\"baseline_unc_DR_pct\\\": 14.98, \\\"baseline_unc_R_F1\\\": 13.01, \\\"note\\\": \\\"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\\\"}}, \\\"d066_sweep_llama_beam8_unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --output_file /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\\\", \\\"server\\\": \\\"westd-16980 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 755444. Relay from Llama beam2 s1 (success).\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam8_unc.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 85.77, \\\"E_P\\\": 85.7, \\\"E_R\\\": 85.84, \\\"R_F1\\\": 51.97, \\\"R_P\\\": 49.76, \\\"R_R\\\": 54.38, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.05, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.07, \\\"parse_fail_pct\\\": 0.5, \\\"total_samples\\\": 200, \\\"total_entities_pred\\\": 3788, \\\"total_relations_pred\\\": 2779}}, \\\"d066_sweep_llama_beam2_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --max_samples 200 --seed 42\\\", \\\"server\\\": \\\"westd-16980 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 750801. Relay from Llama beam2 unc (success).\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam2_full_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam2_s1.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E_F1\\\": 85.6, \\\"E_P\\\": 85.29, \\\"E_R\\\": 85.92, \\\"R_F1\\\": 51.17, \\\"R_P\\\": 48.51, \\\"R_R\\\": 54.14, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"parse_fail_pct\\\": 0.5, \\\"total_samples\\\": 200, \\\"total_entities_pred\\\": 3814, \\\"total_relations_pred\\\": 2839}}, \\\"d066_sweep_llama_docred_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_constrained.jsonl\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam4_s1.log\\\", \\\"metrics\\\": {\\\"E-F1\\\": 85.61, \\\"E-P\\\": 85.48, \\\"E-R\\\": 85.73, \\\"R-F1\\\": 51.89, \\\"R-P\\\": 51.59, \\\"R-R\\\": 52.2, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"PF%\\\": 0.5, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"samples\\\": 200, \\\"parse_fail\\\": 1}, \\\"command\\\": \\\"d066 beam sweep llama docred beam4 s1 (completed, retroactive fix)\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct + LoRA\\\", \\\"seed\\\": 42}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E-F1\\\": 85.61, \\\"E-P\\\": 85.48, \\\"E-R\\\": 85.73, \\\"R-F1\\\": 51.89, \\\"R-P\\\": 51.59, \\\"R-R\\\": 52.2, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"samples\\\": 200, \\\"parse_fail\\\": 1}}, \\\"r16_70b_lora_docred\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 scripts/train_lora_70b_docred.py\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/sft_train_llama.jsonl\\\", \\\"data_count\\\": 3053, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/train.log\\\", \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/sft_dev_llama.jsonl\\\", \\\"pid\\\": 839375, \\\"gpu_ids\\\": [1], \\\"note\\\": \\\"Restarted from scratch (previous run killed, empty checkpoint dir). LoRA r=16 alpha=32 on q/k/v/o_proj. bs=1 grad_accum=8 lr=2e-5 3epochs. ~10.4h ETA.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_loss\\\": 0.0635, \\\"token_acc\\\": 97.94, \\\"steps_completed\\\": 1146, \\\"epochs\\\": 3, \\\"train_loss_start\\\": 0.147, \\\"train_loss_end\\\": 0.056}}, \\\"r16_70b_lora_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 train_70b_lora.py --dataset scierc --model_path /root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ-INT4 --output_dir /root/autodl-tmp/checkpoints/70b_lora_scierc --epochs 3 --lr 2e-4 --lora_r 16 --lora_alpha 32\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/sft/scierc_sft_train.jsonl\\\", \\\"data_count\\\": 1762, \\\"model_name\\\": \\\"Llama-3.3-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/train.log\\\", \\\"pid\\\": 836206, \\\"gpu_ids\\\": [0, 1]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_loss\\\": 0.0611, \\\"token_acc\\\": 97.78, \\\"steps_completed\\\": 663, \\\"epochs\\\": 3, \\\"train_loss_start\\\": 0.183, \\\"train_loss_end\\\": 0.041}}, \\\"r16_70b_scierc_zs_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 808988, \\\"data_path\\\": \\\"SciERC test set (551 sentences)\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"model_path\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (ZS eval)\\\", \\\"log_path\\\": \\\"/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 35.19, \\\"R_F1\\\": 11.24, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 3.5, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"baseline_unc_E_F1\\\": 35.21, \\\"baseline_unc_R_F1\\\": 11.15, \\\"baseline_unc_DR_pct\\\": 6.41, \\\"baseline_unc_RV_pct\\\": 0.61, \\\"baseline_unc_CF_pct\\\": 0}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r14_qwen_docred_beam4_998\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl --device cuda:0 --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Qwen3-8B (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 58.19, \\\"R_F1\\\": 8.72, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 4.94, \\\"parse_fail_pct\\\": 3.51, \\\"samples\\\": 998, \\\"success\\\": 963, \\\"fail\\\": 35}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_llama_zs_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama ZS)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_llama_zs.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 23.23, \\\"R_F1\\\": 2.9, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 84.4, \\\"CF_pct\\\": 0.36, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r16_trie_qwen_zs_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen ZS)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_qwen_zs.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 30.97, \\\"R_F1\\\": 8.64, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 29.3, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551}, \\\"conclusion\\\": \\\"success\\\"}, \\\"r14_llama_docred_beam4_998\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --output_path /root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.jsonl --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"R_F1\\\": 8.83, \\\"E_F1\\\": 57.81, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 1, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"parse_fail_pct\\\": 3.91, \\\"samples\\\": 998, \\\"success\\\": 959, \\\"fail\\\": 39, \\\"baseline_ZS_greedy_R_F1\\\": 6.27, \\\"baseline_ZS_greedy_E_F1\\\": 54.93, \\\"baseline_ZS_greedy_DR_pct\\\": 2.55, \\\"baseline_ZS_greedy_CF_pct\\\": 8.54}}, \\\"d066_sweep_llama_scierc_beam8_s1_551\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam8_full_s1.jsonl\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"llama_lora_scierc_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"scierc test set (551 sentences)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E-F1\\\": 67.51, \\\"E-P\\\": 64.99, \\\"E-R\\\": 70.23, \\\"R-F1\\\": 44.95, \\\"R-P\\\": 40.1, \\\"R-R\\\": 51.13, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0, \\\"samples\\\": 551, \\\"note\\\": \\\"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\\\"}}, \\\"d066_sweep_llama_scierc_beam4_s1_551\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"E-F1\\\": 68.06, \\\"E-P\\\": 65.96, \\\"E-R\\\": 70.29, \\\"R-F1\\\": 46.18, \\\"R-P\\\": 42.1, \\\"R-R\\\": 51.13, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"parse_fail\\\": 0, \\\"samples\\\": 551, \\\"note\\\": \\\"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"llama_lora_scierc_merged\\\", \\\"seed\\\": 42}}, \\\"d066_sweep_llama_docred_beam4_unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_unconstrained.jsonl\\\", \\\"server\\\": \\\"westd-16980 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 761033. Relay from Llama beam8 unc (success).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.67, \\\"R-F1\\\": 52.65, \\\"DR_pct\\\": 0.04, \\\"CF_pct\\\": 0.08, \\\"PF_pct\\\": 0.5, \\\"samples\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d066_sweep_llama_docred_beam1_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\\\", \\\"server\\\": \\\"westd-21461 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 209444. Relay from beam1 unc (success).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.43, \\\"R-F1\\\": 47.35, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.19, \\\"PF_pct\\\": 2, \\\"samples\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d066_sweep_llama_beam8_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\\\", \\\"server\\\": \\\"westd-16980 GPU0\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 756540. Relay after GPU0 freed.\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.76, \\\"R-F1\\\": 51.74, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0.5, \\\"samples\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d065_qwen_greedy_4096_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --decoding_strategy greedy --max_new_tokens 4096 --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --output_file /root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096_rerun.jsonl --seed 42\\\", \\\"server\\\": \\\"westd-21461 GPU0\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Qwen3-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (998 docs, constrained decoding inference)\\\", \\\"note\\\": \\\"Rerun after dual-process corruption. PID 194615.\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 81.87, \\\"R-F1\\\": 40.79, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.22, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"PF_pct\\\": 8.52, \\\"samples\\\": 998}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d066_sweep_llama_scierc_beam2_s1_551\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"llama_lora_scierc_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"scierc test set (551 sentences)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"entity_f1\\\": 68.34, \\\"entity_p\\\": 66.59, \\\"entity_r\\\": 70.17, \\\"relation_f1\\\": 46.12, \\\"relation_p\\\": 42.73, \\\"relation_r\\\": 50.1, \\\"parse_fail_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.17, \\\"note\\\": \\\"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\\\"}}, \\\"d066_sweep_llama_scierc_beam1_unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-21461 GPU1\\\", \\\"data_path\\\": \\\"data/scierc/test.json (551 docs)\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA SciERC (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"data/scierc/test.json\\\", \\\"note\\\": \\\"PID 205314. Relay from Qwen beam8 s1 SciERC (success).\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unconstrained.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unc.log\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"total\\\": 275, \\\"success\\\": 275, \\\"fail\\\": 0, \\\"output_file\\\": \\\"llama_scierc_beam1_unconstrained.jsonl\\\", \\\"note\\\": \\\"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\\\"}}}, \\\"count\\\": 50, \\\"total\\\": 158, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4881}}\"}",
      "numLines": 1,
      "startLine": 0,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "9a65401c-24fe-4389-9a20-39cc39a71833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 71_

```json
{
  "type": "last-prompt",
  "leafUuid": "625832cb-5960-46e4-8a26-e368c7cbd214",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "DocRED INT4 quantization comparison experiments",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Assistant

_source line 73 · 2026-05-23T05:49:36.355Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a more complete picture. Let me find the DocRED 8B FP16 S1 constrained baselines:

Looking at registry entries:
- `d065_qwen_greedy_4096_r2`: Qwen FT DocRED full_s1, 998 docs → R-F1=40.79, DR=0%, CF=0.22%
- `d066_sweep_llama_docred_beam1_s1`: Llama FT DocRED full_s1 beam1, 200 docs → R-F1=47.35, DR=0%


- I need to track down the Llama FP16 S1 variant on the full 998 docs, and I'm noticing `w5_lora_docred_constrained_eval` was referenced as a parent but hasn't shown up yet. I also see there are separate grammar_only and semantic_only modes, but I need the combined full_s1 configuration.

Now I'm thinking through the sample counts for the INT4 experiments. SciERC used 551 samples for quantization testing, while the 8B FP16 DocRED runs used the full 998-doc dev set. The 200-doc subset only appeared in the 70B experiments, so I should check whether that constraint applies here or if I should stick with the full set. I'm planning to create the quantization scripts based on the SciERC approach, run them in parallel across both GPUs, then evaluate with the full_s1 constrained eval on whichever sample size is appropriate.

But I'm noticing the baseline results are inconsistent—some Llama runs used 200 docs while others used 998—so I need to find which FP16 baseline I should actually be matching for a fair INT4 comparison.

For SciERC, the INT4 experiments align better with their FP16 counterparts: Qwen shows a small drop from 42.95 to 41.71 in R-F1, while Llama drops from 45.47 to 43.98, both evaluated on the same 551-document set.

Now I'm looking for the FP16 baselines for DocRED to ensure I'm comparing INT4 results against the right sample counts. I found a Qwen FT baseline on the full dataset with 998 docs reaching 40.79 R-F1, and there's a Llama beam search variant I should check more carefully. (=greedy) with full_s1, 200 docs, R-F1=47.35

The problem is the sample counts differ. I think the best approach is:
- For Qwen: use 998 docs (matching d065_qwen_greedy_4096_r2)
- For Llama: need to find the 998-doc full_s1 baseline, or use 200-doc

Actually, let me search more specifically. I see experiments `w5_lora_docred_constrained_eval` mentioned but not in the first 50 results. Let me look for older experiments.

Actually, looking at the Llama DocRED:
- `w8_llama_docred_ft_grammar_only` (grammar_only, 998 docs) has R_F1=43.72
- `w8_llama_docred_ft_semantic_only` (semantic_only, 998 docs) has R_F1=43.85

But I need full_s1. The beam sweep had `d066_sweep_llama_docred_beam1_s1` at 200 docs with R-F1=47.35, which shows the same discrepancy. For a fair INT4 comparison, I should standardize on 998 docs across both models—that gives me Qwen's FP16 baseline at R-F1=40.79 to work against.

Now I need to find the Llama 998-doc full_s1 baseline. Let me search the registry more carefully or check if I need to run it myself. I should also plan the quantization and evaluation scripts for DocRED, keeping in mind that the calibration data format differs from SciERC—DocRED uses a `sents` field with token lists rather than `sentences`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "625832cb-5960-46e4-8a26-e368c7cbd214",
  "isSidechain": false,
  "requestId": "req_011CbJyXAtUWNhyaMRyCSysx",
  "type": "assistant",
  "uuid": "3cbd2e75-57cd-4dbd-a228-f8a150a116e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2hUHJbeHTzS6TNpUbaV6q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24930,
      "cache_read_input_tokens": 75398,
      "output_tokens": 2133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2133,
          "cache_read_input_tokens": 75398,
          "cache_creation_input_tokens": 24930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24930
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

_source line 74 · 2026-05-23T05:49:37.089Z_

需要查找 Llama DocRED FP16 S1 998-doc baseline 和 GPU 状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cbd2e75-57cd-4dbd-a228-f8a150a116e7",
  "isSidechain": false,
  "requestId": "req_011CbJyXAtUWNhyaMRyCSysx",
  "type": "assistant",
  "uuid": "53eb7f5a-9720-4e3b-ae22-36b43a566339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2hUHJbeHTzS6TNpUbaV6q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24930,
      "cache_read_input_tokens": 75398,
      "output_tokens": 2133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2133,
          "cache_read_input_tokens": 75398,
          "cache_creation_input_tokens": 24930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24930
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

_source line 75 · 2026-05-23T05:49:38.431Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01VGEKe2Wwwsi7ew1k4P8Pj9`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "limit": 50,
  "fields": [
    "status",
    "metrics",
    "spec"
  ],
  "filters": {
    "status": "DONE"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53eb7f5a-9720-4e3b-ae22-36b43a566339",
  "isSidechain": false,
  "requestId": "req_011CbJyXAtUWNhyaMRyCSysx",
  "type": "assistant",
  "uuid": "f254f02d-9813-4fe4-9b43-4bdc17367910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2hUHJbeHTzS6TNpUbaV6q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24930,
      "cache_read_input_tokens": 75398,
      "output_tokens": 2133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2133,
          "cache_read_input_tokens": 75398,
          "cache_creation_input_tokens": 24930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24930
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

_source line 76 · 2026-05-23T05:49:39.139Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MqNHmnwPjXEN7dgDChitn5`</summary>

```json
{
  "server": "westd-16980",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f254f02d-9813-4fe4-9b43-4bdc17367910",
  "isSidechain": false,
  "requestId": "req_011CbJyXAtUWNhyaMRyCSysx",
  "type": "assistant",
  "uuid": "e156d2e9-5462-4746-9bb8-52d7060438c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2hUHJbeHTzS6TNpUbaV6q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24930,
      "cache_read_input_tokens": 75398,
      "output_tokens": 2133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2133,
          "cache_read_input_tokens": 75398,
          "cache_creation_input_tokens": 24930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24930
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

_source line 77 · 2026-05-23T05:49:39.169Z_

<details><summary>↩ Tool result · `toolu_01VGEKe2Wwwsi7ew1k4P8Pj9`</summary>

```text
&lt;persisted-output>
Output too large (52.7KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bcaaae93-c135-4568-bb9e-6ae384bb4c94/tool-results/toolu_01VGEKe2Wwwsi7ew1k4P8Pj9.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test (551 docs)\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test 551 sentences\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f254f02d-9813-4fe4-9b43-4bdc17367910",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "7593e37b-7bcb-4101-bd1a-f9782c523162",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"sf2_llama_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-SciERC-FT-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\\\", \\\"eval_data\\\": \\\"SciERC test (551 docs)\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.94, \\\"R-F1\\\": 43.98, \\\"E-F1\\\": 67.54, \\\"samples\\\": 551, \\\"R-P\\\": 40.47, \\\"R-R\\\": 48.15, \\\"E-P\\\": 65.51, \\\"E-R\\\": 69.7}}, \\\"sf2_qwen_int4_scierc_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-SciERC-FT-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\\\", \\\"eval_data\\\": \\\"SciERC test 551 sentences\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 1.1, \\\"R-F1\\\": 41.71, \\\"E-F1\\\": 67.05, \\\"samples\\\": 551, \\\"R-P\\\": 38.52, \\\"R-R\\\": 45.48, \\\"E-P\\\": 64.76, \\\"E-R\\\": 69.52}}, \\\"sf2_gollie_scierc_violation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/processed_data/test.json\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"GoLLIE-7B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/gollie_model/\\\", \\\"eval_data\\\": \\\"SciERC test (100 docs)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gollie_model/\\\", \\\"log_path\\\": \\\"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\\\"}, \\\"metrics\\\": {\\\"GoLLIE_ZS\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.83, \\\"E_F1\\\": 9.17, \\\"R_F1\\\": 0, \\\"pred_ents\\\": 241, \\\"pred_rels\\\": 5, \\\"docs_with_output\\\": 54}, \\\"OntoCoDec_Qwen_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.61, \\\"E_F1\\\": 66.43, \\\"R_F1\\\": 43.69}, \\\"OntoCoDec_Llama_FT_S1\\\": {\\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.62, \\\"E_F1\\\": 67.09, \\\"R_F1\\\": 45.47}}}, \\\"eval_70b_zs_docred_200_full_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 88678, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_full_s1.log\\\"}, \\\"metrics\\\": {\\\"DR%\\\": 0, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 5.34, \\\"E-F1\\\": 70.05, \\\"R-F1\\\": 13.25, \\\"PF%\\\": 0, \\\"entities_pred\\\": 3234, \\\"relations_pred\\\": 2637, \\\"triples_checked\\\": 2642}}, \\\"eval_70b_lora_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 984253, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_docred_200_grammar_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 10.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.38, \\\"CF_pct\\\": 0.06, \\\"E_F1\\\": 80.13, \\\"E_P\\\": 85.16, \\\"E_R\\\": 75.66, \\\"R_F1\\\": 43.96, \\\"R_P\\\": 39.78, \\\"R_R\\\": 49.11, \\\"entities_pred\\\": 3362, \\\"relations_pred\\\": 3154}}, \\\"eval_70b_lora_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 983803, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_docred_200_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_fail_pct\\\": 11, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.51, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.21, \\\"E_F1\\\": 80.06, \\\"E_P\\\": 85.21, \\\"E_R\\\": 75.5, \\\"R_F1\\\": 43.61, \\\"R_P\\\": 39.44, \\\"R_R\\\": 48.75, \\\"entities_pred\\\": 3351, \\\"relations_pred\\\": 3148}}, \\\"eval_70b_zs_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 84588, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_unconstrained.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities_pred\\\": 3242, \\\"relations_pred\\\": 2637, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 7.88, \\\"DR_pct\\\": 13.45, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 8, \\\"E_F1\\\": 70.14, \\\"E_P\\\": 75.85, \\\"E_R\\\": 65.23, \\\"R_F1\\\": 13.25, \\\"R_P\\\": 12.97, \\\"R_R\\\": 13.54}}, \\\"eval_70b_zs_docred_200_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"eval_data\\\": \\\"DocRED dev 200-doc subset\\\", \\\"checkpoint_source\\\": \\\"n/a (zero-shot)\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_grammar_only.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 1, \\\"entities_pred\\\": 3221, \\\"relations_pred\\\": 2609, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 17.03, \\\"CF_count\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"E_F1\\\": 70.12, \\\"E_P\\\": 75.88, \\\"E_R\\\": 65.17, \\\"R_F1\\\": 13.23, \\\"R_P\\\": 12.99, \\\"R_R\\\": 13.47}}, \\\"eval_70b_zs_docred_200_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"DocRED dev 200 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_docred_200_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 200, \\\"parse_failures\\\": 0, \\\"entities\\\": 3240, \\\"relations\\\": 2596, \\\"ET_pct\\\": 0.12, \\\"RV_pct\\\": 8.24, \\\"DR_pct\\\": 1.66, \\\"CF_count\\\": 132, \\\"CF_pct\\\": 4.07, \\\"E_F1\\\": 70.1, \\\"E_P\\\": 75.87, \\\"E_R\\\": 65.15, \\\"R_F1\\\": 13.05, \\\"R_P\\\": 12.88, \\\"R_R\\\": 13.23, \\\"fuzzy_matches\\\": 8}}, \\\"eval_70b_lora_docred_200_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\\\", \\\"pid\\\": 70638, \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\\\", \\\"note\\\": \\\"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.57, \\\"E-P\\\": 85.45, \\\"E-R\\\": 85.68, \\\"R-F1\\\": 48.14, \\\"R-P\\\": 44.24, \\\"R-R\\\": 52.79, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"parse_fail\\\": \\\"1/200 (0.5%)\\\", \\\"entities_pred\\\": 3790, \\\"relations_pred\\\": 3030}}, \\\"eval_70b_lora_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_grammar_only.log\\\", \\\"pid\\\": 70175}, \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"json_failure_rate\\\": 0, \\\"entities\\\": 1805, \\\"relations\\\": 1133, \\\"entity_type_violations\\\": 0, \\\"entity_type_violation_rate\\\": 0, \\\"relation_vocab_violations\\\": 0, \\\"relation_vocab_violation_rate\\\": 0, \\\"domain_range_violations\\\": 17, \\\"domain_range_violation_rate\\\": 0.015, \\\"cross_field_consistency_violations\\\": 0, \\\"fuzzy_relation_matches\\\": 0, \\\"entity_P\\\": 0.6272, \\\"entity_R\\\": 0.6707, \\\"entity_F1\\\": 0.6482, \\\"relation_P\\\": 0.4152, \\\"relation_R\\\": 0.4825, \\\"relation_F1\\\": 0.4463}}, \\\"eval_70b_zs_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\\\", \\\"pid\\\": 74572, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/tmp/70b_zs_scierc_unconstrained.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 2353, \\\"relations\\\": 1483, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.6, \\\"DR_pct\\\": 6.4, \\\"CF_count\\\": 0, \\\"E_F1\\\": 35.22, \\\"E_P\\\": 30.13, \\\"E_R\\\": 42.38, \\\"R_F1\\\": 11.23, \\\"R_P\\\": 9.31, \\\"R_R\\\": 14.17, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_full_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 972139, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_full_s2.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1531, \\\"relations\\\": 1027, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 18, \\\"E_F1\\\": 62.35, \\\"E_P\\\": 65.44, \\\"E_R\\\": 59.53, \\\"R_F1\\\": 36.28, \\\"R_P\\\": 35.35, \\\"R_R\\\": 37.27, \\\"parse_fail_pct\\\": 0}}, \\\"eval_70b_lora_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 971668, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1806, \\\"relations\\\": 1133, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0.6, \\\"CF_count\\\": 9, \\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"parse_fail_pct\\\": 0}}, \\\"entity_order_ablation_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 967058, \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-LoRA-SciERC-merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"log_path\\\": \\\"/tmp/entity_order_shuffled_qwen_scierc.log\\\", \\\"shuffle_seed\\\": 42, \\\"original_entity_order\\\": [\\\"Task\\\", \\\"Method\\\", \\\"Material\\\", \\\"Metric\\\", \\\"OtherScientificTerm\\\", \\\"Generic\\\"], \\\"shuffled_entity_order\\\": [\\\"Metric\\\", \\\"Method\\\", \\\"Material\\\", \\\"OtherScientificTerm\\\", \\\"Task\\\", \\\"Generic\\\"], \\\"original_relation_order\\\": [\\\"Used-for\\\", \\\"Feature-of\\\", \\\"Hyponym-of\\\", \\\"Part-of\\\", \\\"Compare\\\", \\\"Conjunction\\\", \\\"Evaluate-for\\\"], \\\"shuffled_relation_order\\\": [\\\"Conjunction\\\", \\\"Evaluate-for\\\", \\\"Compare\\\", \\\"Part-of\\\", \\\"Feature-of\\\", \\\"Hyponym-of\\\", \\\"Used-for\\\"]}, \\\"metrics\\\": {\\\"E_F1\\\": 67.05, \\\"E_P\\\": 65.23, \\\"E_R\\\": 68.98, \\\"R_F1\\\": 43.77, \\\"R_P\\\": 40.78, \\\"R_R\\\": 47.23, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 21, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1784, \\\"relations\\\": 1128, \\\"corrected_original_R_F1\\\": 43.77, \\\"corrected_original_E_F1\\\": 67.05, \\\"corrected_original_DR_pct\\\": 0, \\\"corrected_original_CF_count\\\": 21, \\\"corrected_delta_R_F1\\\": 0, \\\"corrected_delta_E_F1\\\": 0, \\\"raw_output_identical\\\": true, \\\"parsed_output_identical\\\": true, \\\"note\\\": \\\"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\\\"}}, \\\"eval_70b_zs_scierc_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"r16_70b_scierc_zs_s1\\\", \\\"eval_data\\\": \\\"scierc test set (551 docs)\\\", \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/eval_70b_zs_scierc_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 11.37, \\\"DR_pct\\\": 1.01, \\\"RV_pct\\\": 0.6, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 76, \\\"samples\\\": 551}}, \\\"eval_70b_zs_scierc_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/eval_70b_zs_scierc_grammar_only.log\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 11.23, \\\"DR_pct\\\": 6.33, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 0, \\\"samples\\\": 551}}, \\\"eval_70b_lora_scierc_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test 551 docs\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"log_path\\\": \\\"/tmp/70b_lora_scierc_beam4_s1.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 64.89, \\\"E_P\\\": 62.29, \\\"E_R\\\": 67.72, \\\"R_F1\\\": 44.81, \\\"R_P\\\": 39.45, \\\"R_R\\\": 51.85, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_count\\\": 1, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1839, \\\"relations\\\": 1283}}, \\\"tcr_beam4_llama_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"N/A (eval-only)\\\", \\\"log_path\\\": \\\"/tmp/beam4_tcr_llama_scierc.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1803, \\\"relations\\\": 1194, \\\"entity_type_violations\\\": \\\"0/1803 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1194 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"13/1194 (1.1%)\\\", \\\"cross_field_consistency\\\": 0, \\\"DR_pct\\\": 1.09, \\\"E_F1\\\": 68.02, \\\"E_P\\\": 65.88, \\\"E_R\\\": 70.29, \\\"R_F1\\\": 46.05, \\\"R_P\\\": 41.83, \\\"R_R\\\": 51.23, \\\"tcr_changed_selection\\\": \\\"0/551 (0.0%)\\\"}}, \\\"tcr_beam4_qwen_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B-LoRA-SciERC-merged\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\\\", \\\"log_path\\\": \\\"/tmp/beam_tcr_run.log\\\"}, \\\"metrics\\\": {\\\"samples\\\": 551, \\\"json_failures\\\": 0, \\\"entities\\\": 1802, \\\"relations\\\": 1250, \\\"entity_type_violations\\\": \\\"0/1802 (0.0%)\\\", \\\"relation_vocab_violations\\\": \\\"0/1250 (0.0%)\\\", \\\"domain_range_violations\\\": \\\"23/1250 (1.8%)\\\", \\\"cross_field_consistency_violations\\\": 1, \\\"DR_pct\\\": 1.84, \\\"E_P\\\": 65.05, \\\"E_R\\\": 69.64, \\\"E_F1\\\": 67.26, \\\"R_P\\\": 39.36, \\\"R_R\\\": 50.51, \\\"R_F1\\\": 44.24, \\\"TCR_changed_selection\\\": \\\"0/551 (0.0%)\\\", \\\"all_candidates_TCR_1.0\\\": true}}, \\\"vllm_guided_json_scierc_zs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B\\\", \\\"seed\\\": 0}, \\\"metrics\\\": {\\\"DR%\\\": 15.26, \\\"RV%\\\": 0, \\\"ET%\\\": 0, \\\"CF%\\\": 0.04, \\\"R-F1\\\": 8.75, \\\"E-F1\\\": 30.91, \\\"parse_fail%\\\": 0, \\\"total_samples\\\": 551, \\\"total_entities\\\": 2485, \\\"total_relations\\\": 1724, \\\"inference_time_s\\\": 108.5}}, \\\"eval_70b_lora_docred_200_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"11466\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": \\\"200 (first 200 docs)\\\", \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/tmp/constrained_inference.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 79.38, \\\"E_P\\\": 85.24, \\\"E_R\\\": 74.28, \\\"R_F1\\\": 43.95, \\\"R_P\\\": 40.48, \\\"R_R\\\": 48.08, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.18, \\\"parse_fail_pct\\\": 12.5, \\\"samples\\\": 200}}, \\\"d066_beam_sweep\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\\\", \\\"server\\\": \\\"westd-16980 + westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"note\\\": \\\"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\\\"}, \\\"metrics\\\": {\\\"scierc_qwen3_8b\\\": {\\\"k1_unc\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 2.11, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.494}, \\\"k1_con\\\": {\\\"E_F1\\\": 66.88, \\\"R_F1\\\": 42.95, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.5, \\\"avg_time\\\": 2.932}, \\\"k2_unc\\\": {\\\"E_F1\\\": 67.79, \\\"R_F1\\\": 44.75, \\\"DR_pct\\\": 1.54, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 2.954}, \\\"k2_con\\\": {\\\"E_F1\\\": 67.71, \\\"R_F1\\\": 44.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.11, \\\"avg_time\\\": 3.463}, \\\"k4_unc\\\": {\\\"E_F1\\\": 67.49, \\\"R_F1\\\": 43.72, \\\"DR_pct\\\": 1.89, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 3.485}, \\\"k4_con\\\": {\\\"E_F1\\\": 67.22, \\\"R_F1\\\": 43.6, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.069}, \\\"k8_unc\\\": {\\\"E_F1\\\": 66.4, \\\"R_F1\\\": 43.17, \\\"DR_pct\\\": 1.77, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 4.194}, \\\"k8_con\\\": {\\\"E_F1\\\": 66.36, \\\"R_F1\\\": 43.65, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"avg_time\\\": 5.058}}, \\\"pareto_optimal\\\": \\\"k=2 con\\\", \\\"best_E_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 67.79}, \\\"best_R_F1\\\": {\\\"config\\\": \\\"k=2 unc\\\", \\\"value\\\": 44.75}}}, \\\"w8_llama_docred_ft_grammar_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"llama_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"w5_llama_docred_lora\\\", \\\"eval_data\\\": \\\"docred_dev_998\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 43.72, \\\"R_P\\\": 38.57, \\\"R_R\\\": 50.44, \\\"parse_fail_pct\\\": 2.3, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\\\"}}, \\\"w8_llama_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\\\\\"\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": 1, \\\"pid\\\": 361202, \\\"model_name\\\": \\\"Llama-3.1-8B-LoRA-DocRED\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 43.85, \\\"R_P\\\": 38.85, \\\"R_R\\\": 50.31, \\\"parse_fail_pct\\\": 2.4, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\\\"}}, \\\"w8_qwen_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"qwen_lora_docred_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"qwen_lora_docred_merged\\\", \\\"eval_data\\\": \\\"docred_test_998\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"log_path\\\": \\\"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 40.85, \\\"R_P\\\": 36.33, \\\"R_R\\\": 46.65, \\\"parse_fail_pct\\\": 7.52, \\\"samples\\\": 998, \\\"note\\\": \\\"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\\\"}}, \\\"r16_trie_qwen_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B (fine-tuned)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 64.4, \\\"E_P\\\": 66.8, \\\"E_R\\\": 62.16, \\\"R_F1\\\": 41.16, \\\"R_P\\\": 38.24, \\\"R_R\\\": 44.56, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 95.5, \\\"CF_pct\\\": 0.09, \\\"parse_fail_pct\\\": 9.1, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\\\"}}, \\\"r16_trie_llama_ft_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (fine-tuned)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 36.66, \\\"E_P\\\": 67.47, \\\"E_R\\\": 25.16, \\\"R_F1\\\": 19.95, \\\"R_P\\\": 41.42, \\\"R_R\\\": 13.14, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 15.2, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 50.8, \\\"samples\\\": 551, \\\"note\\\": \\\"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\\\"}}, \\\"eval_70b_lora_docred_200_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\\\\\"run_constrained_extraction.py\\\\\\\", run_name=\\\\\\\"__main__\\\\\\\")'\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": \\\"998 (truncated to 200)\\\", \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\\\", \\\"eval_data\\\": \\\"DocRED dev (200-doc subset)\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 80.34, \\\"E_P\\\": 85.13, \\\"E_R\\\": 76.05, \\\"R_F1\\\": 43.8, \\\"R_P\\\": 39.6, \\\"R_R\\\": 48.99, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.57, \\\"DR_pct\\\": 0.22, \\\"CF_pct\\\": 0.06, \\\"parse_fail_pct\\\": 10, \\\"samples\\\": 200, \\\"relations\\\": 3159, \\\"RV_count\\\": 18, \\\"DR_count\\\": 7, \\\"CF_count\\\": 2}}, \\\"eval_70b_lora_scierc_s1_constrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"SciERC test (551 sentences)\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\\\"}, \\\"metrics\\\": {\\\"entity_f1\\\": 0.6476, \\\"entity_precision\\\": 0.6266, \\\"entity_recall\\\": 0.6701, \\\"relation_f1\\\": 0.4453, \\\"relation_precision\\\": 0.4149, \\\"relation_recall\\\": 0.4805, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_count\\\": 15, \\\"parse_fail_pct\\\": 0, \\\"fuzzy_matches\\\": 0, \\\"num_samples\\\": 551, \\\"num_entities\\\": 1805, \\\"num_relations\\\": 1129}}, \\\"eval_70b_lora_scierc_unconstrained\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-AWQ-INT4 + LoRA r16\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\\\", \\\"eval_data\\\": \\\"scierc test (551 sentences)\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 64.86, \\\"E_P\\\": 62.74, \\\"E_R\\\": 67.12, \\\"R_F1\\\": 44.73, \\\"R_P\\\": 41.61, \\\"R_R\\\": 48.36, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 1.5, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"entities\\\": 1806, \\\"relations\\\": 1133}}, \\\"r16_70b_docred_zs_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"model_path\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 69.11, \\\"R_F1\\\": 13.05, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 0.04, \\\"parse_fail_pct\\\": 0.1, \\\"samples\\\": 998, \\\"total_entities\\\": 16599, \\\"total_triples\\\": 13239, \\\"baseline_unc_DR_pct\\\": 14.98, \\\"baseline_unc_R_F1\\\": 13.01, \\\"note\\\": \\\"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\\\"}}, \\\"d066_sweep_llama_beam8_unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --output_file /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\\\", \\\"server\\\": \\\"westd-16980 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 755444. Relay from Llama beam2 s1 (success).\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam8_unc.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 85.77, \\\"E_P\\\": 85.7, \\\"E_R\\\": 85.84, \\\"R_F1\\\": 51.97, \\\"R_P\\\": 49.76, \\\"R_R\\\": 54.38, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.05, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0.07, \\\"parse_fail_pct\\\": 0.5, \\\"total_samples\\\": 200, \\\"total_entities_pred\\\": 3788, \\\"total_relations_pred\\\": 2779}}, \\\"d066_sweep_llama_beam2_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --max_samples 200 --seed 42\\\", \\\"server\\\": \\\"westd-16980 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 750801. Relay from Llama beam2 unc (success).\\\", \\\"checkpoint_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam2_full_s1.jsonl\\\", \\\"log_path\\\": \\\"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam2_s1.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 85.6, \\\"E_P\\\": 85.29, \\\"E_R\\\": 85.92, \\\"R_F1\\\": 51.17, \\\"R_P\\\": 48.51, \\\"R_R\\\": 54.14, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"parse_fail_pct\\\": 0.5, \\\"total_samples\\\": 200, \\\"total_entities_pred\\\": 3814, \\\"total_relations_pred\\\": 2839}}, \\\"d066_sweep_llama_docred_beam4_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_constrained.jsonl\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam4_s1.log\\\", \\\"metrics\\\": {\\\"E-F1\\\": 85.61, \\\"E-P\\\": 85.48, \\\"E-R\\\": 85.73, \\\"R-F1\\\": 51.89, \\\"R-P\\\": 51.59, \\\"R-R\\\": 52.2, \\\"DR%\\\": 0, \\\"CF%\\\": 0, \\\"PF%\\\": 0.5, \\\"ET%\\\": 0, \\\"RV%\\\": 0, \\\"samples\\\": 200, \\\"parse_fail\\\": 1}, \\\"command\\\": \\\"d066 beam sweep llama docred beam4 s1 (completed, retroactive fix)\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct + LoRA\\\", \\\"seed\\\": 42}, \\\"metrics\\\": {\\\"E-F1\\\": 85.61, \\\"E-P\\\": 85.48, \\\"E-R\\\": 85.73, \\\"R-F1\\\": 51.89, \\\"R-P\\\": 51.59, \\\"R-R\\\": 52.2, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0.5, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"samples\\\": 200, \\\"parse_fail\\\": 1}}, \\\"r16_70b_lora_docred\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 scripts/train_lora_70b_docred.py\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/sft_train_llama.jsonl\\\", \\\"data_count\\\": 3053, \\\"model_name\\\": \\\"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_docred/train.log\\\", \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"eval_data\\\": \\\"/root/schema_semantic_constrained_ie/data/docred/sft_dev_llama.jsonl\\\", \\\"pid\\\": 839375, \\\"gpu_ids\\\": [1], \\\"note\\\": \\\"Restarted from scratch (previous run killed, empty checkpoint dir). LoRA r=16 alpha=32 on q/k/v/o_proj. bs=1 grad_accum=8 lr=2e-5 3epochs. ~10.4h ETA.\\\"}, \\\"metrics\\\": {\\\"eval_loss\\\": 0.0635, \\\"token_acc\\\": 97.94, \\\"steps_completed\\\": 1146, \\\"epochs\\\": 3, \\\"train_loss_start\\\": 0.147, \\\"train_loss_end\\\": 0.056}}, \\\"r16_70b_lora_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 train_70b_lora.py --dataset scierc --model_path /root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ-INT4 --output_dir /root/autodl-tmp/checkpoints/70b_lora_scierc --epochs 3 --lr 2e-4 --lora_r 16 --lora_alpha 32\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/sft/scierc_sft_train.jsonl\\\", \\\"data_count\\\": 1762, \\\"model_name\\\": \\\"Llama-3.3-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/checkpoints/70b_lora_scierc/train.log\\\", \\\"pid\\\": 836206, \\\"gpu_ids\\\": [0, 1]}, \\\"metrics\\\": {\\\"eval_loss\\\": 0.0611, \\\"token_acc\\\": 97.78, \\\"steps_completed\\\": 663, \\\"epochs\\\": 3, \\\"train_loss_start\\\": 0.183, \\\"train_loss_end\\\": 0.041}}, \\\"r16_70b_scierc_zs_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 808988, \\\"data_path\\\": \\\"SciERC test set (551 sentences)\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-70B-Instruct-AWQ-INT4\\\", \\\"model_path\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (ZS eval)\\\", \\\"log_path\\\": \\\"/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 35.19, \\\"R_F1\\\": 11.24, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 3.5, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551, \\\"baseline_unc_E_F1\\\": 35.21, \\\"baseline_unc_R_F1\\\": 11.15, \\\"baseline_unc_DR_pct\\\": 6.41, \\\"baseline_unc_RV_pct\\\": 0.61, \\\"baseline_unc_CF_pct\\\": 0}}, \\\"r14_qwen_docred_beam4_998\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl --device cuda:0 --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Qwen3-8B (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A (zero-shot)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.log\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 58.19, \\\"R_F1\\\": 8.72, \\\"DR_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"CF_pct\\\": 4.94, \\\"parse_fail_pct\\\": 3.51, \\\"samples\\\": 998, \\\"success\\\": 963, \\\"fail\\\": 35}}, \\\"r16_trie_llama_zs_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama ZS)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_llama_zs.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 23.23, \\\"R_F1\\\": 2.9, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 84.4, \\\"CF_pct\\\": 0.36, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551}}, \\\"r16_trie_qwen_zs_scierc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen ZS)\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 241846, \\\"data_path\\\": \\\"data/scierc/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Qwen3-8B (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (trie eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r16_trie_qwen_zs.log\\\"}, \\\"metrics\\\": {\\\"E_F1\\\": 30.97, \\\"R_F1\\\": 8.64, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 29.3, \\\"CF_pct\\\": 0, \\\"parse_fail_pct\\\": 0, \\\"samples\\\": 551}}, \\\"r14_llama_docred_beam4_998\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --output_path /root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.jsonl --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Llama-3.1-8B-Instruct (zero-shot)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.log\\\"}, \\\"metrics\\\": {\\\"R_F1\\\": 8.83, \\\"E_F1\\\": 57.81, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 1, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"parse_fail_pct\\\": 3.91, \\\"samples\\\": 998, \\\"success\\\": 959, \\\"fail\\\": 39, \\\"baseline_ZS_greedy_R_F1\\\": 6.27, \\\"baseline_ZS_greedy_E_F1\\\": 54.93, \\\"baseline_ZS_greedy_DR_pct\\\": 2.55, \\\"baseline_ZS_greedy_CF_pct\\\": 8.54}}, \\\"d066_sweep_llama_scierc_beam8_s1_551\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam8_full_s1.jsonl\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"llama_lora_scierc_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"scierc test set (551 sentences)\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 67.51, \\\"E-P\\\": 64.99, \\\"E-R\\\": 70.23, \\\"R-F1\\\": 44.95, \\\"R-P\\\": 40.1, \\\"R-R\\\": 51.13, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0, \\\"samples\\\": 551, \\\"note\\\": \\\"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\\\"}}, \\\"d066_sweep_llama_scierc_beam4_s1_551\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"E-F1\\\": 68.06, \\\"E-P\\\": 65.96, \\\"E-R\\\": 70.29, \\\"R-F1\\\": 46.18, \\\"R-P\\\": 42.1, \\\"R-R\\\": 51.13, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"parse_fail\\\": 0, \\\"samples\\\": 551, \\\"note\\\": \\\"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\\\", \\\"server\\\": \\\"westd-21461\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"llama_lora_scierc_merged\\\", \\\"seed\\\": 42}}, \\\"d066_sweep_llama_docred_beam4_unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_unconstrained.jsonl\\\", \\\"server\\\": \\\"westd-16980 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 761033. Relay from Llama beam8 unc (success).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.67, \\\"R-F1\\\": 52.65, \\\"DR_pct\\\": 0.04, \\\"CF_pct\\\": 0.08, \\\"PF_pct\\\": 0.5, \\\"samples\\\": 200}}, \\\"d066_sweep_llama_docred_beam1_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\\\", \\\"server\\\": \\\"westd-21461 GPU1\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 209444. Relay from beam1 unc (success).\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.43, \\\"R-F1\\\": 47.35, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.19, \\\"PF_pct\\\": 2, \\\"samples\\\": 200}}, \\\"d066_sweep_llama_beam8_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\\\", \\\"server\\\": \\\"westd-16980 GPU0\\\", \\\"data_path\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (200-doc subset)\\\", \\\"note\\\": \\\"PID 756540. Relay after GPU0 freed.\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 85.76, \\\"R-F1\\\": 51.74, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0, \\\"PF_pct\\\": 0.5, \\\"samples\\\": 200}}, \\\"d065_qwen_greedy_4096_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --decoding_strategy greedy --max_new_tokens 4096 --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --output_file /root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096_rerun.jsonl --seed 42\\\", \\\"server\\\": \\\"westd-21461 GPU0\\\", \\\"data_path\\\": \\\"data/docred/dev.json\\\", \\\"data_count\\\": 998, \\\"model_name\\\": \\\"Qwen3-8B LoRA DocRED (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\\\", \\\"eval_data\\\": \\\"data/docred/dev.json (998 docs, constrained decoding inference)\\\", \\\"note\\\": \\\"Rerun after dual-process corruption. PID 194615.\\\"}, \\\"metrics\\\": {\\\"E-F1\\\": 81.87, \\\"R-F1\\\": 40.79, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.22, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"PF_pct\\\": 8.52, \\\"samples\\\": 998}}, \\\"d066_sweep_llama_scierc_beam2_s1_551\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\\\", \\\"server\\\": \\\"westd-16980\\\", \\\"data_path\\\": \\\"data/processed_data/test.json\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"llama_lora_scierc_merged\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"scierc test set (551 sentences)\\\"}, \\\"metrics\\\": {\\\"entity_f1\\\": 68.34, \\\"entity_p\\\": 66.59, \\\"entity_r\\\": 70.17, \\\"relation_f1\\\": 46.12, \\\"relation_p\\\": 42.73, \\\"relation_r\\\": 50.1, \\\"parse_fail_pct\\\": 0, \\\"ET_pct\\\": 0, \\\"RV_pct\\\": 0, \\\"DR_pct\\\": 0, \\\"CF_pct\\\": 0.17, \\\"note\\\": \\\"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\\\"}}, \\\"d066_sweep_llama_scierc_beam1_unc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --seed 42\\\", \\\"server\\\": \\\"westd-21461 GPU1\\\", \\\"data_path\\\": \\\"data/scierc/test.json (551 docs)\\\", \\\"data_count\\\": 551, \\\"model_name\\\": \\\"Llama-3.1-8B LoRA SciERC (merged)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\\", \\\"eval_data\\\": \\\"data/scierc/test.json\\\", \\\"note\\\": \\\"PID 205314. Relay from Qwen beam8 s1 SciERC (success).\\\", \\\"checkpoint_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unconstrained.jsonl\\\", \\\"log_path\\\": \\\"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unc.log\\\"}, \\\"metrics\\\": {\\\"total\\\": 275, \\\"success\\\": 275, \\\"fail\\\": 0, \\\"output_file\\\": \\\"llama_scierc_beam1_unconstrained.jsonl\\\", \\\"note\\\": \\\"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\\\"}}}, \\\"count\\\": 50, \\\"total\\\": 158, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4672}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test (551 docs)\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test 551 sentences\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 100, \"model_name\": \"GoLLIE-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/gollie_model/\", \"eval_data\": \"SciERC test (100 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/gollie_model/\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\"}, \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 88678, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_full_s1.log\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 984253, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_grammar_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 983803, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 84588, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_unconstrained.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"eval_data\": \"DocRED dev 200-doc subset\", \"checkpoint_source\": \"n/a (zero-shot)\", \"log_path\": \"/tmp/70b_zs_docred_200_grammar_only.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 70638, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\", \"log_path\": \"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\", \"note\": \"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\"}, \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_grammar_only.log\", \"pid\": 70175}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 74572, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_scierc_unconstrained.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 972139, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_full_s2.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 971668, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_semantic_only.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 967058, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/entity_order_shuffled_qwen_scierc.log\", \"shuffle_seed\": 42, \"original_entity_order\": [\"Task\", \"Method\", \"Material\", \"Metric\", \"OtherScientificTerm\", \"Generic\"], \"shuffled_entity_order\": [\"Metric\", \"Method\", \"Material\", \"OtherScientificTerm\", \"Task\", \"Generic\"], \"original_relation_order\": [\"Used-for\", \"Feature-of\", \"Hyponym-of\", \"Part-of\", \"Compare\", \"Conjunction\", \"Evaluate-for\"], \"shuffled_relation_order\": [\"Conjunction\", \"Evaluate-for\", \"Compare\", \"Part-of\", \"Feature-of\", \"Hyponym-of\", \"Used-for\"]}, \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"r16_70b_scierc_zs_s1\", \"eval_data\": \"scierc test set (551 docs)\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_semantic_only.log\"}, \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_grammar_only.log\"}, \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_beam4_s1.log\"}, \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/beam4_tcr_llama_scierc.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/beam_tcr_run.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 0}, \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": \"11466\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"200 (first 200 docs)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\", \"log_path\": \"westd-21461:/tmp/constrained_inference.log\"}, \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"spec\": {\"command\": \"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\", \"server\": \"westd-16980 + westd-21461\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"note\": \"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\"}, \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\"}, \"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\"}, \"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\"run_constrained_extraction.py\\\", run_name=\\\"__main__\\\")'\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"998 (truncated to 200)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\"}, \"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}}, \"eval_70b_lora_scierc_s1_constrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\"}, \"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}}, \"eval_70b_lora_scierc_unconstrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"scierc test (551 sentences)\"}, \"metrics\": {\"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.5, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1806, \"relations\": 1133}}, \"r16_70b_docred_zs_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\"}, \"metrics\": {\"E_F1\": 69.11, \"R_F1\": 13.05, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.04, \"parse_fail_pct\": 0.1, \"samples\": 998, \"total_entities\": 16599, \"total_triples\": 13239, \"baseline_unc_DR_pct\": 14.98, \"baseline_unc_R_F1\": 13.01, \"note\": \"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\"}}, \"d066_sweep_llama_beam8_unc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --output_file /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 755444. Relay from Llama beam2 s1 (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam8_unc.log\"}, \"metrics\": {\"E_F1\": 85.77, \"E_P\": 85.7, \"E_R\": 85.84, \"R_F1\": 51.97, \"R_P\": 49.76, \"R_R\": 54.38, \"DR_pct\": 0, \"CF_pct\": 0.05, \"ET_pct\": 0, \"RV_pct\": 0.07, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3788, \"total_relations_pred\": 2779}}, \"d066_sweep_llama_beam2_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --max_samples 200 --seed 42\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 750801. Relay from Llama beam2 unc (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam2_full_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam2_s1.log\"}, \"metrics\": {\"E_F1\": 85.6, \"E_P\": 85.29, \"E_R\": 85.92, \"R_F1\": 51.17, \"R_P\": 48.51, \"R_R\": 54.14, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3814, \"total_relations_pred\": 2839}}, \"d066_sweep_llama_docred_beam4_s1\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_constrained.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam4_s1.log\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR%\": 0, \"CF%\": 0, \"PF%\": 0.5, \"ET%\": 0, \"RV%\": 0, \"samples\": 200, \"parse_fail\": 1}, \"command\": \"d066 beam sweep llama docred beam4 s1 (completed, retroactive fix)\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B-Instruct + LoRA\", \"seed\": 42}, \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"ET_pct\": 0, \"RV_pct\": 0, \"samples\": 200, \"parse_fail\": 1}}, \"r16_70b_lora_docred\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 scripts/train_lora_70b_docred.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/sft_train_llama.jsonl\", \"data_count\": 3053, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/train.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"/root/schema_semantic_constrained_ie/data/docred/sft_dev_llama.jsonl\", \"pid\": 839375, \"gpu_ids\": [1], \"note\": \"Restarted from scratch (previous run killed, empty checkpoint dir). LoRA r=16 alpha=32 on q/k/v/o_proj. bs=1 grad_accum=8 lr=2e-5 3epochs. ~10.4h ETA.\"}, \"metrics\": {\"eval_loss\": 0.0635, \"token_acc\": 97.94, \"steps_completed\": 1146, \"epochs\": 3, \"train_loss_start\": 0.147, \"train_loss_end\": 0.056}}, \"r16_70b_lora_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 train_70b_lora.py --dataset scierc --model_path /root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ-INT4 --output_dir /root/autodl-tmp/checkpoints/70b_lora_scierc --epochs 3 --lr 2e-4 --lora_r 16 --lora_alpha 32\", \"server\": \"westd-16980\", \"data_path\": \"data/sft/scierc_sft_train.jsonl\", \"data_count\": 1762, \"model_name\": \"Llama-3.3-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/train.log\", \"pid\": 836206, \"gpu_ids\": [0, 1]}, \"metrics\": {\"eval_loss\": 0.0611, \"token_acc\": 97.78, \"steps_completed\": 663, \"epochs\": 3, \"train_loss_start\": 0.183, \"train_loss_end\": 0.041}}, \"r16_70b_scierc_zs_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 808988, \"data_path\": \"SciERC test set (551 sentences)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A (ZS eval)\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log\"}, \"metrics\": {\"E_F1\": 35.19, \"R_F1\": 11.24, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 3.5, \"parse_fail_pct\": 0, \"samples\": 551, \"baseline_unc_E_F1\": 35.21, \"baseline_unc_R_F1\": 11.15, \"baseline_unc_DR_pct\": 6.41, \"baseline_unc_RV_pct\": 0.61, \"baseline_unc_CF_pct\": 0}}, \"r14_qwen_docred_beam4_998\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl --device cuda:0 --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"E_F1\": 58.19, \"R_F1\": 8.72, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 4.94, \"parse_fail_pct\": 3.51, \"samples\": 998, \"success\": 963, \"fail\": 35}}, \"r16_trie_llama_zs_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_zs.log\"}, \"metrics\": {\"E_F1\": 23.23, \"R_F1\": 2.9, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 84.4, \"CF_pct\": 0.36, \"parse_fail_pct\": 0, \"samples\": 551}}, \"r16_trie_qwen_zs_scierc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_zs.log\"}, \"metrics\": {\"E_F1\": 30.97, \"R_F1\": 8.64, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 29.3, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551}}, \"r14_llama_docred_beam4_998\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --output_path /root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.jsonl --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.log\"}, \"metrics\": {\"R_F1\": 8.83, \"E_F1\": 57.81, \"DR_pct\": 0, \"CF_pct\": 1, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 3.91, \"samples\": 998, \"success\": 959, \"fail\": 39, \"baseline_ZS_greedy_R_F1\": 6.27, \"baseline_ZS_greedy_E_F1\": 54.93, \"baseline_ZS_greedy_DR_pct\": 2.55, \"baseline_ZS_greedy_CF_pct\": 8.54}}, \"d066_sweep_llama_scierc_beam8_s1_551\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam8_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"metrics\": {\"E-F1\": 67.51, \"E-P\": 64.99, \"E-R\": 70.23, \"R-F1\": 44.95, \"R-P\": 40.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0, \"samples\": 551, \"note\": \"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\"}}, \"d066_sweep_llama_scierc_beam4_s1_551\": {\"status\": \"DONE\", \"metrics\": {\"E-F1\": 68.06, \"E-P\": 65.96, \"E-R\": 70.29, \"R-F1\": 46.18, \"R-P\": 42.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"parse_fail\": 0, \"samples\": 551, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42}}, \"d066_sweep_llama_docred_beam4_unc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 761033. Relay from Llama beam8 unc (success).\"}, \"metrics\": {\"E-F1\": 85.67, \"R-F1\": 52.65, \"DR_pct\": 0.04, \"CF_pct\": 0.08, \"PF_pct\": 0.5, \"samples\": 200}}, \"d066_sweep_llama_docred_beam1_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 209444. Relay from beam1 unc (success).\"}, \"metrics\": {\"E-F1\": 85.43, \"R-F1\": 47.35, \"DR_pct\": 0, \"CF_pct\": 0.19, \"PF_pct\": 2, \"samples\": 200}}, \"d066_sweep_llama_beam8_s1\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-16980 GPU0\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 756540. Relay after GPU0 freed.\"}, \"metrics\": {\"E-F1\": 85.76, \"R-F1\": 51.74, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"samples\": 200}}, \"d065_qwen_greedy_4096_r2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --decoding_strategy greedy --max_new_tokens 4096 --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --output_file /root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096_rerun.jsonl --seed 42\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (998 docs, constrained decoding inference)\", \"note\": \"Rerun after dual-process corruption. PID 194615.\"}, \"metrics\": {\"E-F1\": 81.87, \"R-F1\": 40.79, \"DR_pct\": 0, \"CF_pct\": 0.22, \"ET_pct\": 0, \"RV_pct\": 0, \"PF_pct\": 8.52, \"samples\": 998}}, \"d066_sweep_llama_scierc_beam2_s1_551\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"metrics\": {\"entity_f1\": 68.34, \"entity_p\": 66.59, \"entity_r\": 70.17, \"relation_f1\": 46.12, \"relation_p\": 42.73, \"relation_r\": 50.1, \"parse_fail_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.17, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}}, \"d066_sweep_llama_scierc_beam1_unc\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --seed 42\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/scierc/test.json (551 docs)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B LoRA SciERC (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/scierc/test.json\", \"note\": \"PID 205314. Relay from Qwen beam8 s1 SciERC (success).\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unconstrained.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unc.log\"}, \"metrics\": {\"total\": 275, \"success\": 275, \"fail\": 0, \"output_file\": \"llama_scierc_beam1_unconstrained.jsonl\", \"note\": \"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\"}}}, \"count\": 50, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4672}}"
    }
  },
  "sourceToolAssistantUUID": "f254f02d-9813-4fe4-9b43-4bdc17367910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 78_

```json
{
  "type": "last-prompt",
  "leafUuid": "7593e37b-7bcb-4101-bd1a-f9782c523162",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "DocRED INT4 quantization comparison experiments",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94"
}
```

---


### Tool result

_source line 80 · 2026-05-23T05:49:39.669Z_

<details><summary>↩ Tool result · `toolu_01MqNHmnwPjXEN7dgDChitn5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 MiB, 97887 MiB, 0 %\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 MiB, 97887 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e156d2e9-5462-4746-9bb8-52d7060438c2",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "5987fb70-73c9-4ff1-9995-6e64a66712d2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 MiB, 97887 MiB, 0 %\\\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 MiB, 97887 MiB, 0 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 MiB, 97887 MiB, 0 %\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 MiB, 97887 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  },
  "sourceToolAssistantUUID": "e156d2e9-5462-4746-9bb8-52d7060438c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 81 · 2026-05-23T05:50:03.588Z_

<details><summary>Logged reasoning block</summary>

```text
Good - both GPUs are free on westd-16980. Now let me search for the Llama DocRED FP16 full_s1 998-doc baseline. I need to search further in the registry. Let me grep for relevant experiment names.

From the data I've collected, I need to find `w5_llama_docred_lora_training` and its child experiment for full_s1 constrained eval. Let me search the full registry file.

Actually, from the GoLLIE comparison experiment `sf2_gollie_scierc_violation`, I can see that the DocRED constrained baselines for SciERC mention:


- OntoCoDec_Qwen_FT_S1: E_F1=66.43, R_F1=43.69
- OntoCoDec_Llama_FT_S1: E_F1=67.09, R_F1=45.47

But those are SciERC results, not DocRED. I need the DocRED FP16 S1 baselines instead. From the registry, I found the Qwen DocRED FP16 S1 baseline (d065_qwen_greedy_4096_r2) with R-F1=40.79 on 998 docs, but I still need to locate the corresponding Llama baseline. I've seen `d066_sweep_llama_docred_beam1_s1` with R-F1=47.35 on 200 docs, and also beam1 greedy s1 on 998 docs must exist somewhere. Let me search for experiments with "w5_llama_docred" or "w5_qwen_docred" in the registry by reading the registry file directly.

Actually, I don't need to be too precise about finding the exact FP16 baselines right now. I know:
1. For Qwen DocRED FP16 full_s1 (998 docs): R-F1 = 40.79 (from d065_qwen_greedy_4096_r2)
2. For Llama DocRED FP16 full_s1: need to find

Let me just proceed with the tasks. I can create quantization scripts, run them in parallel, then handle inference and evaluation. For the calibration data, since DocRED uses `sents` as a list of token lists, I'll need to adapt the SciERC calibration approach. I'll leverage the existing `run_constrained_extraction.py` with DocRED settings for evaluation, similar to how the current experiments are structured.

My plan is to create quantization scripts for both Qwen and Llama using their respective DocRED checkpoints and data, run them in parallel on separate GPUs, then execute full_s1 constrained evaluation on the DocRED dev set. Writing quantization scripts...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5987fb70-73c9-4ff1-9995-6e64a66712d2",
  "isSidechain": false,
  "requestId": "req_011CbJyagY248CZkNJ9USsd9",
  "type": "assistant",
  "uuid": "e4121b68-6fb9-4cc6-8ab9-372957edcf93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G45bE5d3UuXYf33WuB5QbX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3401,
      "cache_read_input_tokens": 100328,
      "output_tokens": 1350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1350,
          "cache_read_input_tokens": 100328,
          "cache_creation_input_tokens": 3401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3401
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

_source line 82 · 2026-05-23T05:50:04.530Z_

两个 GPU 都空闲。现在搜索 Llama DocRED FP16 S1 baseline，并检查已有推理命令格式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4121b68-6fb9-4cc6-8ab9-372957edcf93",
  "isSidechain": false,
  "requestId": "req_011CbJyagY248CZkNJ9USsd9",
  "type": "assistant",
  "uuid": "7a6d0664-5c8b-47e2-a063-0352a0194b0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G45bE5d3UuXYf33WuB5QbX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3401,
      "cache_read_input_tokens": 100328,
      "output_tokens": 1350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1350,
          "cache_read_input_tokens": 100328,
          "cache_creation_input_tokens": 3401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3401
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

_source line 83 · 2026-05-23T05:50:09.627Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JMsttRJCg1vxJLF8Y4YLSC`</summary>

```json
{
  "pattern": "w5_llama_docred|w5_qwen_docred|llama_docred.*full_s1|qwen_docred.*full_s1",
  "path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bcaaae93-c135-4568-bb9e-6ae384bb4c94/tool-results/toolu_01VGEKe2Wwwsi7ew1k4P8Pj9.txt",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a6d0664-5c8b-47e2-a063-0352a0194b0c",
  "isSidechain": false,
  "requestId": "req_011CbJyagY248CZkNJ9USsd9",
  "type": "assistant",
  "uuid": "fd247c65-7889-4f9a-b9f6-ff2495680822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G45bE5d3UuXYf33WuB5QbX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3401,
      "cache_read_input_tokens": 100328,
      "output_tokens": 1350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1350,
          "cache_read_input_tokens": 100328,
          "cache_creation_input_tokens": 3401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3401
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

_source line 84 · 2026-05-23T05:50:09.650Z_

<details><summary>↩ Tool result · `toolu_01JMsttRJCg1vxJLF8Y4YLSC`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd247c65-7889-4f9a-b9f6-ff2495680822",
  "isSidechain": false,
  "promptId": "653b1e00-ae6c-4abc-8f0e-00ce6f68e849",
  "type": "user",
  "uuid": "5cf17891-c142-4a4c-bd78-0e6ffaecdedd",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "fd247c65-7889-4f9a-b9f6-ff2495680822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-23T05:50:10.335Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016DfcXvXYL5Sc5eRkjh5oDD`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/scripts/eval_d064.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cf17891-c142-4a4c-bd78-0e6ffaecdedd",
  "isSidechain": false,
  "requestId": "req_011CbJyagY248CZkNJ9USsd9",
  "type": "assistant",
  "uuid": "34c68d2a-e110-40a4-b2f8-6de589b983df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bcaaae93-c135-4568-bb9e-6ae384bb4c94",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G45bE5d3UuXYf33WuB5QbX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3401,
      "cache_read_input_tokens": 100328,
      "output_tokens": 1350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1350,
          "cache_read_input_tokens": 100328,
          "cache_creation_input_tokens": 3401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3401
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
