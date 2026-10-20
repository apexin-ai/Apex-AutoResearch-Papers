# Research conversation: <project_context> # 项目: xling_calib_direction ## 运行环境 - 服务器名: westd-13176 - SSH 账户: root（调用 ssh_execute / submit_trainin

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/30b1a6bb-0102-4a5e-a07f-0d6412fb4476.jsonl`
- **Structured JSON:** [`78446718fa0daa8be264.json`](../../sessions/78/78446718fa0daa8be264.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T21:10:40.037Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T21:10:40.037Z",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "content": "&lt;project_context>\n# 项目: xling_calib_direction\n\n## 运行环境\n- 服务器名: westd-13176\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/xling_calib_direction\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：创建 extract_activations_large.py（大模型版本）\n\n### 目标\n基于现有的 `extract_activations.py`，创建一个适配大模型（Qwen3-235B-A22B, Llama 4 Scout）的版本。主要改动：用 `register_forward_hook` 替代 `output_hidden_states=True`，支持 INT4/INT8 量化。\n\n### 现有代码位置\n`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations.py`\n\n先 Read 这个文件了解完整代码结构。\n\n### 关键改动点\n\n1. **register_forward_hook 替代 output_hidden_states**：\n   - `output_hidden_states=True` 会返回所有层的 hidden states，对 94 层模型（Qwen3-235B）内存不可承受\n   - 改为：只对需要的层注册 forward hook，在 hook 中捕获最后一个 token 的 hidden state\n   - Hook 方案：\n     ```python\n     captured = {}\n     def make_hook(layer_idx):\n         def hook_fn(module, input, output):\n             # output 可能是 tuple (hidden_states, ...) 或直接 tensor\n             h = output[0] if isinstance(output, tuple) else output\n             captured[layer_idx] = h[0, -1].detach().cpu().float()\n         return hook_fn\n     \n     handles = []\n     for li in layer_indices:\n         layer_module = model.model.layers[li]  # 适配不同架构\n         handles.append(layer_module.register_forward_hook(make_hook(li)))\n     ```\n   - 推理时不传 `output_hidden_states=True`，从 `captured` dict 读取\n   - 推理结束后移除 hooks：`for h in handles: h.remove()`\n\n2. **量化支持**：\n   - 新增 `--quantization` 参数：none / int4 / int8\n   - INT4 (bitsandbytes 4-bit)：\n     ```python\n     from transformers import BitsAndBytesConfig\n     bnb_config = BitsAndBytesConfig(\n         load_in_4bit=True,\n         bnb_4bit_compute_dtype=torch.bfloat16,\n         bnb_4bit_quant_type=\"nf4\",\n         bnb_4bit_use_double_quant=True,\n     )\n     model = AutoModelForCausalLM.from_pretrained(\n         args.model, quantization_config=bnb_config, device_map=\"auto\", trust_remote_code=True\n     )\n     ```\n   - INT8：\n     ```python\n     bnb_config = BitsAndBytesConfig(load_in_8bit=True)\n     ```\n\n3. **架构自适应**：\n   - 不同模型的 layer 访问路径不同：\n     - Qwen: `model.model.layers[i]`\n     - Llama: `model.model.layers[i]`\n     - 通用方案：尝试 `model.model.layers`，fallback 到 `model.transformer.h` 等\n   - 新增 `--num_layers` 参数（可选），用于覆盖自动检测\n   - 自动检测层数：`model.config.num_hidden_layers`\n\n4. **内存优化**：\n   - 每处理完一定数量样本（如 100）就 `torch.cuda.empty_cache()`\n   - 大模型推理时 batch_size=1 已经是默认\n   - 添加 `--save_interval` 参数：每 N 条增量保存一次（防止 OOM 或中断丢失数据）\n\n5. **保持兼容**：\n   - 输出格式与原版完全一致：`layer{i}_{lang}.pt` 包含 activations 和 labels\n   - 命令行参数保持兼容（model, languages, layers, output_dir, n_shot, max_samples, dtype, subjects）\n   - 新增参数：`--quantization` (none/int4/int8), `--save_interval` (int, default 500)\n\n### 文件写入位置\n写到 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py`\n\n### 代码质量要求\n- 文件顶部写文件注释（说明与 extract_activations.py 的区别、输入输出、关键依赖）\n- 关键函数写 docstring\n- Hook 注册/移除的逻辑必须有注释说明 why（为什么不用 output_hidden_states）\n\n### 验证\n写完后，检查代码语法是否正确（可以用 python -c \"import ast; ast.parse(open('...').read())\"）。"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T21:10:40.041Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T21:10:40.041Z",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-20T21:10:40.083Z_

&lt;project_context>
# 项目: xling_calib_direction

## 运行环境
- 服务器名: westd-13176
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/xling_calib_direction


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：创建 extract_activations_large.py（大模型版本）

### 目标
基于现有的 `extract_activations.py`，创建一个适配大模型（Qwen3-235B-A22B, Llama 4 Scout）的版本。主要改动：用 `register_forward_hook` 替代 `output_hidden_states=True`，支持 INT4/INT8 量化。

### 现有代码位置
`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations.py`

先 Read 这个文件了解完整代码结构。

### 关键改动点

1. **register_forward_hook 替代 output_hidden_states**：
   - `output_hidden_states=True` 会返回所有层的 hidden states，对 94 层模型（Qwen3-235B）内存不可承受
   - 改为：只对需要的层注册 forward hook，在 hook 中捕获最后一个 token 的 hidden state
   - Hook 方案：
     ```python
     captured = {}
     def make_hook(layer_idx):
         def hook_fn(module, input, output):
             # output 可能是 tuple (hidden_states, ...) 或直接 tensor
             h = output[0] if isinstance(output, tuple) else output
             captured[layer_idx] = h[0, -1].detach().cpu().float()
         return hook_fn
     
     handles = []
     for li in layer_indices:
         layer_module = model.model.layers[li]  # 适配不同架构
         handles.append(layer_module.register_forward_hook(make_hook(li)))
     ```
   - 推理时不传 `output_hidden_states=True`，从 `captured` dict 读取
   - 推理结束后移除 hooks：`for h in handles: h.remove()`

2. **量化支持**：
   - 新增 `--quantization` 参数：none / int4 / int8
   - INT4 (bitsandbytes 4-bit)：
     ```python
     from transformers import BitsAndBytesConfig
     bnb_config = BitsAndBytesConfig(
         load_in_4bit=True,
         bnb_4bit_compute_dtype=torch.bfloat16,
         bnb_4bit_quant_type="nf4",
         bnb_4bit_use_double_quant=True,
     )
     model = AutoModelForCausalLM.from_pretrained(
         args.model, quantization_config=bnb_config, device_map="auto", trust_remote_code=True
     )
     ```
   - INT8：
     ```python
     bnb_config = BitsAndBytesConfig(load_in_8bit=True)
     ```

3. **架构自适应**：
   - 不同模型的 layer 访问路径不同：
     - Qwen: `model.model.layers[i]`
     - Llama: `model.model.layers[i]`
     - 通用方案：尝试 `model.model.layers`，fallback 到 `model.transformer.h` 等
   - 新增 `--num_layers` 参数（可选），用于覆盖自动检测
   - 自动检测层数：`model.config.num_hidden_layers`

4. **内存优化**：
   - 每处理完一定数量样本（如 100）就 `torch.cuda.empty_cache()`
   - 大模型推理时 batch_size=1 已经是默认
   - 添加 `--save_interval` 参数：每 N 条增量保存一次（防止 OOM 或中断丢失数据）

5. **保持兼容**：
   - 输出格式与原版完全一致：`layer{i}_{lang}.pt` 包含 activations 和 labels
   - 命令行参数保持兼容（model, languages, layers, output_dir, n_shot, max_samples, dtype, subjects）
   - 新增参数：`--quantization` (none/int4/int8), `--save_interval` (int, default 500)

### 文件写入位置
写到 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py`

### 代码质量要求
- 文件顶部写文件注释（说明与 extract_activations.py 的区别、输入输出、关键依赖）
- 关键函数写 docstring
- Hook 注册/移除的逻辑必须有注释说明 why（为什么不用 output_hidden_states）

### 验证
写完后，检查代码语法是否正确（可以用 python -c "import ast; ast.parse(open('...').read())"）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f48cdcb1-a57c-4a5a-9a52-ea94439384e7",
  "type": "user",
  "uuid": "e6b0d7ec-70e8-4453-9dd2-1443b00e2349",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T21:10:40.083Z_

```json
{
  "parentUuid": "e6b0d7ec-70e8-4453-9dd2-1443b00e2349",
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
  "uuid": "60e43498-e396-4d5a-9607-164cd55ccebe",
  "timestamp": "2026-05-20T21:10:40.083Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T21:10:40.083Z_

```json
{
  "parentUuid": "60e43498-e396-4d5a-9607-164cd55ccebe",
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
  "uuid": "89e0756f-571b-4da9-8fd2-776bc7af6317",
  "timestamp": "2026-05-20T21:10:40.083Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T21:10:40.083Z_

```json
{
  "parentUuid": "89e0756f-571b-4da9-8fd2-776bc7af6317",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5eb73f58-1896-4336-b214-55a20df9294b",
  "timestamp": "2026-05-20T21:10:40.083Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
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
  "aiTitle": "Create large model activation extraction with hooks and quantization",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476"
}
```

---

### Assistant

_source line 8 · 2026-05-20T21:10:43.406Z_

Let me start by reading the existing `extract_activations.py` to understand the full code structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eb73f58-1896-4336-b214-55a20df9294b",
  "isSidechain": false,
  "requestId": "req_011CbEWPRNUxvte8HGNdeCfM",
  "type": "assistant",
  "uuid": "20de35c2-8af1-4537-909e-179ad3869093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFZPavMtdg597Bd7rhoc4D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12361,
      "cache_read_input_tokens": 11841,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12361
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

_source line 9 · 2026-05-20T21:10:43.805Z_

<details open><summary>🔧 Tool call — Read · `toolu_012iqU7uWRn41CLzSnw2yNe9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20de35c2-8af1-4537-909e-179ad3869093",
  "isSidechain": false,
  "requestId": "req_011CbEWPRNUxvte8HGNdeCfM",
  "type": "assistant",
  "uuid": "6d086895-f7aa-4dc9-bacf-2ce97823a199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFZPavMtdg597Bd7rhoc4D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12361,
      "cache_read_input_tokens": 11841,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12361
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

_source line 10 · 2026-05-20T21:10:43.815Z_

<details><summary>↩ Tool result · `toolu_012iqU7uWRn41CLzSnw2yNe9`</summary>

```text
1	"""
2	Extract residual-stream activations from LLM intermediate layers during MMLU inference.
3	
4	For each (layer, language) pair, saves a .pt file containing:
5	  - activations: Tensor(N, hidden_dim) — last-token hidden state after the transformer layer
6	  - labels: Tensor(N,) — 1 if model answered correctly, 0 otherwise
7	
8	English data: cais/mmlu (all subjects, dev split for few-shot)
9	Non-English:  CohereForAI/Global-MMLU (parallel translated questions)
10	
11	Usage:
12	  python extract_activations.py \
13	    --model Qwen/Qwen2.5-7B-Instruct \
14	    --languages en zh ar hi sw ko \
15	    --layers 0,4,8,12,16,20,24,28,31 \
16	    --output_dir ./activations
17	"""
18	
19	import argparse
20	import os
21	
22	import torch
23	from datasets import load_dataset
24	from transformers import AutoModelForCausalLM, AutoTokenizer
25	from tqdm import tqdm
26	
27	
28	LETTERS = ["A", "B", "C", "D"]
29	
30	
31	def parse_args():
32	    p = argparse.ArgumentParser()
33	    p.add_argument("--model", required=True, help="HuggingFace model name or path")
34	    p.add_argument("--languages", nargs="+", default=["en", "zh", "ar", "hi", "sw", "ko"])
35	    p.add_argument("--layers", default="0,4,8,12,16,20,24,28,31",
36	                   help="Comma-separated transformer layer indices (0-indexed)")
37	    p.add_argument("--output_dir", default="./activations")
38	    p.add_argument("--n_shot", type=int, default=5)
39	    p.add_argument("--max_samples", type=int, default=0, help="0 = all test samples")
40	    p.add_argument("--dtype", default="bfloat16", choices=["float16", "bfloat16"])
41	    p.add_argument("--subjects", nargs="*", default=None,
42	                   help="Restrict to these MMLU subjects (default: all)")
43	    return p.parse_args()
44	
45	
46	# ---------------------------------------------------------------------------
47	# Data loading
48	# ---------------------------------------------------------------------------
49	
50	def load_mmlu(language, split="test"):
51	    """Load an MMLU split. English from cais/mmlu, others from Global-MMLU."""
52	    if language == "en":
53	        return load_dataset("cais/mmlu", "all", split=split)
54	    return load_dataset("CohereForAI/Global-MMLU", language, split=split)
55	
56	
57	def load_mmlu_dev(language):
58	    """Load few-shot exemplars (try 'dev' first, then 'validation')."""
59	    for split_name in ["dev", "validation"]:
60	        try:
61	            return load_mmlu(language, split_name)
62	        except (ValueError, KeyError):
63	            continue
64	    raise RuntimeError(f"No dev/validation split found for '{language}'")
65	
66	
67	def normalize_row(row):
68	    """Normalize a dataset row to {question, choices, answer(int), subject}."""
69	    question = row.get("question", row.get("input", ""))
70	
71	    if "choices" in row and isinstance(row["choices"], list):
72	        choices = list(row["choices"])
73	    else:
74	        choices = [row.get(f"option_{l.lower()}", "") for l in LETTERS]
75	
76	    answer = row.get("answer", row.get("target", 0))
77	    if isinstance(answer, str):
78	        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)
79	
80	    return {
81	        "question": question,
82	        "choices": choices,
83	        "answer": int(answer),
84	        "subject": row.get("subject", "unknown"),
85	    }
86	
87	
88	# ---------------------------------------------------------------------------
89	# Prompt formatting (standard n-shot MMLU)
90	# ---------------------------------------------------------------------------
91	
92	def _format_question(question, choices):
93	    parts = [f"{question}\n"]
94	    for i, c in enumerate(choices):
95	        parts.append(f"{LETTERS[i]}. {c}\n")
96	    return "".join(parts)
97	
98	
99	def build_prompt(row, few_shot_rows, n_shot):
100	    """Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars."""
101	    subject_pretty = row["subject"].replace("_", " ")
102	    lines = [
103	        f"The following are multiple choice questions (with answers) about {subject_pretty}.\n\n"
104	    ]
105	    for fs in few_shot_rows[:n_shot]:
106	        fs = normalize_row(fs) if "choices" not in fs or not isinstance(fs.get("answer"), int) else fs
107	        lines.append(_format_question(fs["question"], fs["choices"]))
108	        lines.append(f"Answer: {LETTERS[fs['answer']]}\n\n")
109	    lines.append(_format_question(row["question"], row["choices"]))
110	    lines.append("Answer:")
111	    return "".join(lines)
112	
113	
114	# ---------------------------------------------------------------------------
115	# Main extraction loop
116	# ---------------------------------------------------------------------------
117	
118	def main():
119	    args = parse_args()
120	    layer_indices = sorted(int(x) for x in args.layers.split(","))
121	    os.makedirs(args.output_dir, exist_ok=True)
122	
123	    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16
124	    print(f"Loading model: {args.model}  dtype={args.dtype}")
125	
126	    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
127	    if tokenizer.pad_token is None:
128	        tokenizer.pad_token = tokenizer.eos_token
129	
130	    model = AutoModelForCausalLM.from_pretrained(
131	        args.model, torch_dtype=dtype, device_map="auto", trust_remote_code=True,
132	    )
133	    model.eval()
134	
135	    n_model_layers = model.config.num_hidden_layers
136	    print(f"Model has {n_model_layers} transformer layers; extracting: {layer_indices}")
137	    for li in layer_indices:
138	        if li < 0 or li >= n_model_layers:
139	            raise ValueError(f"Layer index {li} out of range [0, {n_model_layers})")
140	
141	    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]
142	    print(f"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }")
143	
144	    for lang in args.languages:
145	        print(f"\n{'='*50}")
146	        print(f"  Language: {lang}")
147	        print(f"{'='*50}")
148	
149	        test_ds = load_mmlu(lang, "test")
150	        dev_ds = load_mmlu_dev(lang)
151	
152	        if args.subjects:
153	            test_ds = test_ds.filter(lambda x: x.get("subject") in args.subjects)
154	            dev_ds = dev_ds.filter(lambda x: x.get("subject") in args.subjects)
155	
156	        n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))
157	
158	        dev_by_subject: dict[str, list] = {}
159	        for r in dev_ds:
160	            dev_by_subject.setdefault(r.get("subject", "unknown"), []).append(r)
161	        dev_fallback = list(dev_ds)[:args.n_shot]
162	
163	        storage = {li: {"acts": [], "labels": []} for li in layer_indices}
164	
165	        for i in tqdm(range(n), desc=f"[{lang}]"):
166	            row = normalize_row(test_ds[i])
167	            few_shots = dev_by_subject.get(row["subject"], dev_fallback)
168	            prompt = build_prompt(row, few_shots, args.n_shot)
169	
170	            inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
171	                               max_length=4096).to(model.device)
172	
173	            with torch.no_grad():
174	                out = model(**inputs, output_hidden_states=True)
175	
176	            logits_last = out.logits[0, -1]
177	            choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])
178	            pred = choice_logits.argmax().item()
179	            correct = int(pred == row["answer"])
180	
181	            # hidden_states[0] = embedding output; hidden_states[k+1] = layer k output
182	            for li in layer_indices:
183	                h = out.hidden_states[li + 1][0, -1].cpu().float()
184	                storage[li]["acts"].append(h)
185	                storage[li]["labels"].append(correct)
186	
187	            del out, inputs
188	            if (i + 1) % 200 == 0:
189	                torch.cuda.empty_cache()
190	
191	        for li in layer_indices:
192	            acts = torch.stack(storage[li]["acts"])
193	            labels = torch.tensor(storage[li]["labels"], dtype=torch.long)
194	            path = os.path.join(args.output_dir, f"layer{li}_{lang}.pt")
195	            torch.save({"activations": acts, "labels": labels}, path)
196	            acc = labels.float().mean().item()
197	            print(f"  Layer {li:>2d}: N={len(labels):>5d}  model_acc={acc:.3f}  -> {path}")
198	
199	    print("\nExtraction complete.")
200	
201	
202	if __name__ == "__main__":
203	    main()
204	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d086895-f7aa-4dc9-bacf-2ce97823a199",
  "isSidechain": false,
  "promptId": "f48cdcb1-a57c-4a5a-9a52-ea94439384e7",
  "type": "user",
  "uuid": "fa194187-d46c-4254-b455-939f7d630549",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations.py",
      "content": "\"\"\"\nExtract residual-stream activations from LLM intermediate layers during MMLU inference.\n\nFor each (layer, language) pair, saves a .pt file containing:\n  - activations: Tensor(N, hidden_dim) — last-token hidden state after the transformer layer\n  - labels: Tensor(N,) — 1 if model answered correctly, 0 otherwise\n\nEnglish data: cais/mmlu (all subjects, dev split for few-shot)\nNon-English:  CohereForAI/Global-MMLU (parallel translated questions)\n\nUsage:\n  python extract_activations.py \\\n    --model Qwen/Qwen2.5-7B-Instruct \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,4,8,12,16,20,24,28,31 \\\n    --output_dir ./activations\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (standard n-shot MMLU)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model, torch_dtype=dtype, device_map=\"auto\", trust_remote_code=True,\n    )\n    model.eval()\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    for lang in args.languages:\n        print(f\"\\n{'='*50}\")\n        print(f\"  Language: {lang}\")\n        print(f\"{'='*50}\")\n\n        test_ds = load_mmlu(lang, \"test\")\n        dev_ds = load_mmlu_dev(lang)\n\n        if args.subjects:\n            test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n            dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n        n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n        dev_by_subject: dict[str, list] = {}\n        for r in dev_ds:\n            dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n        dev_fallback = list(dev_ds)[:args.n_shot]\n\n        storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n\n        for i in tqdm(range(n), desc=f\"[{lang}]\"):\n            row = normalize_row(test_ds[i])\n            few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n            prompt = build_prompt(row, few_shots, args.n_shot)\n\n            inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                               max_length=4096).to(model.device)\n\n            with torch.no_grad():\n                out = model(**inputs, output_hidden_states=True)\n\n            logits_last = out.logits[0, -1]\n            choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n            pred = choice_logits.argmax().item()\n            correct = int(pred == row[\"answer\"])\n\n            # hidden_states[0] = embedding output; hidden_states[k+1] = layer k output\n            for li in layer_indices:\n                h = out.hidden_states[li + 1][0, -1].cpu().float()\n                storage[li][\"acts\"].append(h)\n                storage[li][\"labels\"].append(correct)\n\n            del out, inputs\n            if (i + 1) % 200 == 0:\n                torch.cuda.empty_cache()\n\n        for li in layer_indices:\n            acts = torch.stack(storage[li][\"acts\"])\n            labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n            path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n            torch.save({\"activations\": acts, \"labels\": labels}, path)\n            acc = labels.float().mean().item()\n            print(f\"  Layer {li:>2d}: N={len(labels):>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 204,
      "startLine": 1,
      "totalLines": 204
    }
  },
  "sourceToolAssistantUUID": "6d086895-f7aa-4dc9-bacf-2ce97823a199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "leafUuid": "fa194187-d46c-4254-b455-939f7d630549",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Create large model activation extraction with hooks and quantization",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476"
}
```

---

### Assistant

_source line 13 · 2026-05-20T21:10:48.824Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the existing code. Let me create the large model version with the specified changes:

1. `register_forward_hook` instead of `output_hidden_states=True`
2. Quantization support (INT4/INT8 via bitsandbytes)
3. Architecture-adaptive layer access
4. Memory optimizations (save_interval, empty_cache)
5. Compatible output format

Let me write the new file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa194187-d46c-4254-b455-939f7d630549",
  "isSidechain": false,
  "requestId": "req_011CbEWPhf2LP3KE68Lntugg",
  "type": "assistant",
  "uuid": "ff117448-0b46-4827-ba67-370b7421a343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYnXZjVh7SCWY4xgQcZ9qW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 24202,
      "output_tokens": 4381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4381,
          "cache_read_input_tokens": 24202,
          "cache_creation_input_tokens": 2975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2975
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

_source line 14 · 2026-05-20T21:10:49.319Z_

Now I'll create the large model version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff117448-0b46-4827-ba67-370b7421a343",
  "isSidechain": false,
  "requestId": "req_011CbEWPhf2LP3KE68Lntugg",
  "type": "assistant",
  "uuid": "0b342e2f-ef00-44c9-860b-a573d128577e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYnXZjVh7SCWY4xgQcZ9qW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 24202,
      "output_tokens": 4381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4381,
          "cache_read_input_tokens": 24202,
          "cache_creation_input_tokens": 2975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2975
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

_source line 15 · 2026-05-20T21:11:51.299Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Mk7y3nvGBqVThR4dVuFw83`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
  "content": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n    \"\"\"\n    layers = get_layer_modules(model)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # Layer output is (hidden_states, ...) tuple or a bare tensor\n            h = output[0] if isinstance(output, tuple) else output\n            # Capture last token, detach and move to CPU immediately to free GPU memory\n            captured[layer_idx] = h[0, -1].detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= len(layers):\n            raise ValueError(f\"Layer index {li} out of range [0, {len(layers)})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b342e2f-ef00-44c9-860b-a573d128577e",
  "isSidechain": false,
  "requestId": "req_011CbEWPhf2LP3KE68Lntugg",
  "type": "assistant",
  "uuid": "c7160af6-c6eb-49a1-80ae-0cad9bdaa718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYnXZjVh7SCWY4xgQcZ9qW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2975,
      "cache_read_input_tokens": 24202,
      "output_tokens": 4381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4381,
          "cache_read_input_tokens": 24202,
          "cache_creation_input_tokens": 2975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2975
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

_source line 16 · 2026-05-20T21:11:51.330Z_

<details><summary>↩ Tool result · `toolu_01Mk7y3nvGBqVThR4dVuFw83`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7160af6-c6eb-49a1-80ae-0cad9bdaa718",
  "isSidechain": false,
  "promptId": "f48cdcb1-a57c-4a5a-9a52-ea94439384e7",
  "type": "user",
  "uuid": "bf252743-3230-4c87-b105-3ceb4f91ab31",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py",
    "content": "\"\"\"\nExtract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).\n\nDifferences from extract_activations.py:\n  - Uses register_forward_hook instead of output_hidden_states=True.\n    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,\n    which is prohibitive for 94-layer models. Hooks capture only the target layers.\n  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).\n  - Incremental saving via --save_interval to survive OOM or interruption.\n  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).\n\nOutput format is identical to extract_activations.py:\n  layer{i}_{lang}.pt  ->  {\"activations\": Tensor(N, hidden_dim), \"labels\": Tensor(N,)}\n\nDependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm\n\nUsage:\n  python extract_activations_large.py \\\n    --model Qwen/Qwen3-235B-A22B \\\n    --languages en zh ar hi sw ko \\\n    --layers 0,8,16,24,32,48,64,80,93 \\\n    --output_dir ./activations \\\n    --quantization int4 \\\n    --save_interval 200\n\"\"\"\n\nimport argparse\nimport os\n\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\nfrom tqdm import tqdm\n\n\nLETTERS = [\"A\", \"B\", \"C\", \"D\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--model\", required=True, help=\"HuggingFace model name or path\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"en\", \"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])\n    p.add_argument(\"--layers\", default=\"0,4,8,12,16,20,24,28,31\",\n                   help=\"Comma-separated transformer layer indices (0-indexed)\")\n    p.add_argument(\"--output_dir\", default=\"./activations\")\n    p.add_argument(\"--n_shot\", type=int, default=5)\n    p.add_argument(\"--max_samples\", type=int, default=0, help=\"0 = all test samples\")\n    p.add_argument(\"--dtype\", default=\"bfloat16\", choices=[\"float16\", \"bfloat16\"])\n    p.add_argument(\"--subjects\", nargs=\"*\", default=None,\n                   help=\"Restrict to these MMLU subjects (default: all)\")\n    p.add_argument(\"--quantization\", default=\"none\", choices=[\"none\", \"int4\", \"int8\"],\n                   help=\"Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)\")\n    p.add_argument(\"--save_interval\", type=int, default=500,\n                   help=\"Incrementally save every N samples (0 = only save at end)\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef load_mmlu(language, split=\"test\"):\n    \"\"\"Load an MMLU split. English from cais/mmlu, others from Global-MMLU.\"\"\"\n    if language == \"en\":\n        return load_dataset(\"cais/mmlu\", \"all\", split=split)\n    return load_dataset(\"CohereForAI/Global-MMLU\", language, split=split)\n\n\ndef load_mmlu_dev(language):\n    \"\"\"Load few-shot exemplars (try 'dev' first, then 'validation').\"\"\"\n    for split_name in [\"dev\", \"validation\"]:\n        try:\n            return load_mmlu(language, split_name)\n        except (ValueError, KeyError):\n            continue\n    raise RuntimeError(f\"No dev/validation split found for '{language}'\")\n\n\ndef normalize_row(row):\n    \"\"\"Normalize a dataset row to {question, choices, answer(int), subject}.\"\"\"\n    question = row.get(\"question\", row.get(\"input\", \"\"))\n\n    if \"choices\" in row and isinstance(row[\"choices\"], list):\n        choices = list(row[\"choices\"])\n    else:\n        choices = [row.get(f\"option_{l.lower()}\", \"\") for l in LETTERS]\n\n    answer = row.get(\"answer\", row.get(\"target\", 0))\n    if isinstance(answer, str):\n        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)\n\n    return {\n        \"question\": question,\n        \"choices\": choices,\n        \"answer\": int(answer),\n        \"subject\": row.get(\"subject\", \"unknown\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Prompt formatting (identical to extract_activations.py)\n# ---------------------------------------------------------------------------\n\ndef _format_question(question, choices):\n    parts = [f\"{question}\\n\"]\n    for i, c in enumerate(choices):\n        parts.append(f\"{LETTERS[i]}. {c}\\n\")\n    return \"\".join(parts)\n\n\ndef build_prompt(row, few_shot_rows, n_shot):\n    \"\"\"Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars.\"\"\"\n    subject_pretty = row[\"subject\"].replace(\"_\", \" \")\n    lines = [\n        f\"The following are multiple choice questions (with answers) about {subject_pretty}.\\n\\n\"\n    ]\n    for fs in few_shot_rows[:n_shot]:\n        fs = normalize_row(fs) if \"choices\" not in fs or not isinstance(fs.get(\"answer\"), int) else fs\n        lines.append(_format_question(fs[\"question\"], fs[\"choices\"]))\n        lines.append(f\"Answer: {LETTERS[fs['answer']]}\\n\\n\")\n    lines.append(_format_question(row[\"question\"], row[\"choices\"]))\n    lines.append(\"Answer:\")\n    return \"\".join(lines)\n\n\n# ---------------------------------------------------------------------------\n# Model loading with quantization support\n# ---------------------------------------------------------------------------\n\ndef load_model(model_name, dtype, quantization):\n    \"\"\"Load model with optional INT4/INT8 quantization via bitsandbytes.\"\"\"\n    kwargs = dict(device_map=\"auto\", trust_remote_code=True)\n\n    if quantization == \"int4\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    elif quantization == \"int8\":\n        from transformers import BitsAndBytesConfig\n        kwargs[\"quantization_config\"] = BitsAndBytesConfig(load_in_8bit=True)\n    else:\n        kwargs[\"torch_dtype\"] = dtype\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)\n    model.eval()\n    return model\n\n\n# ---------------------------------------------------------------------------\n# Architecture-adaptive layer access\n# ---------------------------------------------------------------------------\n\ndef get_layer_modules(model):\n    \"\"\"Return the nn.ModuleList of transformer layers, adapting to model architecture.\n\n    Tries common attribute paths used by different model families:\n      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)\n      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)\n      - model.gpt_neox.layers   (GPT-NeoX variants)\n    \"\"\"\n    candidates = [\n        (\"model.model.layers\", lambda m: m.model.layers),\n        (\"model.transformer.h\", lambda m: m.transformer.h),\n        (\"model.gpt_neox.layers\", lambda m: m.gpt_neox.layers),\n    ]\n    for path_name, accessor in candidates:\n        try:\n            layers = accessor(model)\n            if hasattr(layers, \"__len__\") and len(layers) > 0:\n                print(f\"  Layer access path: {path_name}  ({len(layers)} layers)\")\n                return layers\n        except AttributeError:\n            continue\n    raise RuntimeError(\n        \"Cannot locate transformer layers. \"\n        \"Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers\"\n    )\n\n\n# ---------------------------------------------------------------------------\n# Forward hook machinery\n# ---------------------------------------------------------------------------\n\ndef register_activation_hooks(model, layer_indices, captured):\n    \"\"\"Register forward hooks on target layers to capture last-token hidden states.\n\n    Why hooks instead of output_hidden_states=True:\n      output_hidden_states materializes ALL layers' hidden states in memory at once.\n      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)\n      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific\n      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.\n    \"\"\"\n    layers = get_layer_modules(model)\n    handles = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # Layer output is (hidden_states, ...) tuple or a bare tensor\n            h = output[0] if isinstance(output, tuple) else output\n            # Capture last token, detach and move to CPU immediately to free GPU memory\n            captured[layer_idx] = h[0, -1].detach().cpu().float()\n        return hook_fn\n\n    for li in layer_indices:\n        if li < 0 or li >= len(layers):\n            raise ValueError(f\"Layer index {li} out of range [0, {len(layers)})\")\n        handles.append(layers[li].register_forward_hook(make_hook(li)))\n\n    return handles\n\n\ndef remove_hooks(handles):\n    for h in handles:\n        h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Incremental save / load\n# ---------------------------------------------------------------------------\n\ndef save_layer_data(storage, layer_indices, lang, output_dir):\n    \"\"\"Save accumulated activations for all target layers.\"\"\"\n    for li in layer_indices:\n        if not storage[li][\"acts\"]:\n            continue\n        acts = torch.stack(storage[li][\"acts\"])\n        labels = torch.tensor(storage[li][\"labels\"], dtype=torch.long)\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        torch.save({\"activations\": acts, \"labels\": labels}, path)\n\n\ndef load_existing_progress(layer_indices, lang, output_dir):\n    \"\"\"Load previously saved data to support resumption after interruption.\"\"\"\n    storage = {li: {\"acts\": [], \"labels\": []} for li in layer_indices}\n    n_existing = 0\n    for li in layer_indices:\n        path = os.path.join(output_dir, f\"layer{li}_{lang}.pt\")\n        if os.path.exists(path):\n            data = torch.load(path, weights_only=True)\n            storage[li][\"acts\"] = list(data[\"activations\"].unbind(0))\n            storage[li][\"labels\"] = data[\"labels\"].tolist()\n            n_existing = max(n_existing, len(storage[li][\"labels\"]))\n    return storage, n_existing\n\n\n# ---------------------------------------------------------------------------\n# Main extraction loop\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n    layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dtype = torch.bfloat16 if args.dtype == \"bfloat16\" else torch.float16\n    print(f\"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}\")\n\n    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = load_model(args.model, dtype, args.quantization)\n\n    n_model_layers = model.config.num_hidden_layers\n    print(f\"Model has {n_model_layers} transformer layers; extracting: {layer_indices}\")\n    for li in layer_indices:\n        if li < 0 or li >= n_model_layers:\n            raise ValueError(f\"Layer index {li} out of range [0, {n_model_layers})\")\n\n    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]\n    print(f\"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }\")\n\n    # Register hooks once — they persist across forward calls\n    captured = {}\n    handles = register_activation_hooks(model, layer_indices, captured)\n\n    try:\n        for lang in args.languages:\n            print(f\"\\n{'='*50}\")\n            print(f\"  Language: {lang}\")\n            print(f\"{'='*50}\")\n\n            test_ds = load_mmlu(lang, \"test\")\n            dev_ds = load_mmlu_dev(lang)\n\n            if args.subjects:\n                test_ds = test_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n                dev_ds = dev_ds.filter(lambda x: x.get(\"subject\") in args.subjects)\n\n            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))\n\n            dev_by_subject: dict[str, list] = {}\n            for r in dev_ds:\n                dev_by_subject.setdefault(r.get(\"subject\", \"unknown\"), []).append(r)\n            dev_fallback = list(dev_ds)[:args.n_shot]\n\n            # Try to resume from existing partial results\n            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)\n            if n_existing > 0:\n                print(f\"  Resuming from sample {n_existing} (found existing data)\")\n\n            for i in tqdm(range(n_existing, n), desc=f\"[{lang}]\", initial=n_existing, total=n):\n                row = normalize_row(test_ds[i])\n                few_shots = dev_by_subject.get(row[\"subject\"], dev_fallback)\n                prompt = build_prompt(row, few_shots, args.n_shot)\n\n                inputs = tokenizer(prompt, return_tensors=\"pt\", truncation=True,\n                                   max_length=4096).to(model.device)\n\n                with torch.no_grad():\n                    # No output_hidden_states — hooks capture what we need\n                    out = model(**inputs)\n\n                logits_last = out.logits[0, -1]\n                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])\n                pred = choice_logits.argmax().item()\n                correct = int(pred == row[\"answer\"])\n\n                for li in layer_indices:\n                    storage[li][\"acts\"].append(captured[li])\n                    storage[li][\"labels\"].append(correct)\n\n                captured.clear()\n                del out, inputs\n\n                if (i + 1) % 100 == 0:\n                    torch.cuda.empty_cache()\n\n                # Incremental save\n                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:\n                    save_layer_data(storage, layer_indices, lang, args.output_dir)\n                    print(f\"  [checkpoint] saved at sample {i + 1}\")\n\n            # Final save for this language\n            save_layer_data(storage, layer_indices, lang, args.output_dir)\n            for li in layer_indices:\n                n_samples = len(storage[li][\"labels\"])\n                if n_samples > 0:\n                    acc = sum(storage[li][\"labels\"]) / n_samples\n                    path = os.path.join(args.output_dir, f\"layer{li}_{lang}.pt\")\n                    print(f\"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> {path}\")\n\n    finally:\n        # Always clean up hooks, even if an exception occurs\n        remove_hooks(handles)\n\n    print(\"\\nExtraction complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c7160af6-c6eb-49a1-80ae-0cad9bdaa718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "leafUuid": "bf252743-3230-4c87-b105-3ceb4f91ab31",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Create large model activation extraction with hooks and quantization",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476"
}
```

---

### Assistant

_source line 19 · 2026-05-20T21:11:54.585Z_

语法检查：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf252743-3230-4c87-b105-3ceb4f91ab31",
  "isSidechain": false,
  "requestId": "req_011CbEWUfqGsL3Tb4CeLfK3U",
  "type": "assistant",
  "uuid": "c878462a-c376-432f-8cf6-e29566746abf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9Np97A5kFQH2EEo88nZWR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4438,
      "cache_read_input_tokens": 27177,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 27177,
          "cache_creation_input_tokens": 4438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4438
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

_source line 20 · 2026-05-20T21:11:55.757Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XHijV6gLxe1nbAsQiU4MTb`</summary>

```json
{
  "command": "python3 -c \"import ast; ast.parse(open('/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py').read()); print('OK')\"",
  "description": "Check Python syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c878462a-c376-432f-8cf6-e29566746abf",
  "isSidechain": false,
  "requestId": "req_011CbEWUfqGsL3Tb4CeLfK3U",
  "type": "assistant",
  "uuid": "be63e0a6-6702-437f-89a7-30135862c561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9Np97A5kFQH2EEo88nZWR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4438,
      "cache_read_input_tokens": 27177,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 27177,
          "cache_creation_input_tokens": 4438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4438
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

_source line 21 · 2026-05-20T21:11:55.938Z_

<details><summary>↩ Tool result · `toolu_01XHijV6gLxe1nbAsQiU4MTb`</summary>

```text
OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be63e0a6-6702-437f-89a7-30135862c561",
  "isSidechain": false,
  "promptId": "f48cdcb1-a57c-4a5a-9a52-ea94439384e7",
  "type": "user",
  "uuid": "9d0d6db0-f76e-4798-a260-32801e7c1149",
  "toolUseResult": {
    "stdout": "OK",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "be63e0a6-6702-437f-89a7-30135862c561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-20T21:12:07.981Z_

文件已创建，语法正确。关键改动：

1. **Hook 替代 output_hidden_states** — 只对目标层注册 `register_forward_hook`，hook 中立即 `.detach().cpu().float()`，推理时不传 `output_hidden_states=True`。hooks 在 `finally` 块中清理。
2. **量化** — `--quantization int4/int8`，通过 `BitsAndBytesConfig` 配置 NF4 双重量化或 LLM.int8。
3. **架构自适应** — `get_layer_modules()` 依次尝试 `model.model.layers` / `model.transformer.h` / `model.gpt_neox.layers`。
4. **增量保存与断点续传** — `--save_interval N` 每 N 条保存一次；启动时自动检测已有 `.pt` 文件并从断点恢复。
5. **输出格式完全兼容** — 同样的 `layer{i}_{lang}.pt`，同样的 `{"activations", "labels"}` 结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d0d6db0-f76e-4798-a260-32801e7c1149",
  "isSidechain": false,
  "requestId": "req_011CbEWV1ViBL1ZxeT72V9WE",
  "type": "assistant",
  "uuid": "3c337bd0-cfda-4ba0-9b8f-90d733b619b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYPJapjrrNQKEQcyDLvyXV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 31615,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 31615,
          "cache_creation_input_tokens": 152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 152
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

_source line 23_

```json
{
  "type": "last-prompt",
  "leafUuid": "3c337bd0-cfda-4ba0-9b8f-90d733b619b3",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Create large model activation extraction with hooks and quantization",
  "sessionId": "30b1a6bb-0102-4a5e-a07f-0d6412fb4476"
}
```

---
