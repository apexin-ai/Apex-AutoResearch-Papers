# Research conversation: <project_context> # 项目: gen-depth-contamination ## 运行环境 - 服务器名: cqa1-22115 - SSH 账户: root（调用 ssh_execute / submit_traini — Part 1 of 2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-project-context-gen-depth-contamination-cqa1-22115-ssh-root-ssh-execute-submit-copy-193.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/59/598931d958b2504e9e30.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-25T19:44:16.719Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T19:44:16.719Z",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "content": "&lt;project_context>\n# 项目: gen-depth-contamination\n\n## 运行环境\n- 服务器名: cqa1-22115\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh cqa1-22115  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/gen-depth-contamination\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：附录+Figure 数据源审计（Part 3/3）\n\n### 目标\n审计附录中的所有数字 + 追溯所有 Figure 的数据源到具体文件。\n\n### 你负责的文件\n\n**附录**（读取并提取数字）：\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex`\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex`\n\n**Figure 数据源**（SSH 到服务器追溯）：\n- 服务器：cqa1-22115\n- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- 工作目录：`/root/autodl-tmp/gen-depth-contamination/`\n\n### 附录审计步骤\n1. 读取 appendix.tex 和 appendix_extended.tex\n2. 提取所有数字（超参表、额外实验结果、数据集统计、失败案例统计等）\n3. 用 `read_registry` 验证每个数字\n\n### Figure 数据源追溯步骤\n\n1. **找到所有 Figure 引用**：在所有 .tex 文件中搜索 `\\includegraphics` 或 `figure` 环境，列出所有 figure 文件名\n   ```bash\n   # 在论文目录搜索\n   grep -rn \"includegraphics\\|\\\\\\\\input.*fig\" /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/\n   ```\n\n2. **找到 figure 生成脚本**：SSH 到服务器搜索生成这些 figure 的 Python 脚本\n   ```bash\n   # 搜索绘图脚本\n   find /root/autodl-tmp/gen-depth-contamination/scripts/ -name \"*plot*\" -o -name \"*fig*\" -o -name \"*figure*\" -o -name \"*viz*\" 2>/dev/null\n   grep -rn \"savefig\\|plt.save\" /root/autodl-tmp/gen-depth-contamination/scripts/ 2>/dev/null | head -20\n   ```\n\n3. **追溯数据文件**：对每个绘图脚本，找到它读取的数据文件\n   ```bash\n   # 查看脚本中的数据读取\n   grep -n \"read_csv\\|read_json\\|load\\|open\\|pd.read\" &lt;script_path>\n   ```\n\n4. **验证数据文件存在且内容合理**：\n   ```bash\n   ls -la &lt;data_file>\n   head -5 &lt;data_file>\n   ```\n\n5. **对 Figure caption 中的数字**：追溯到具体数据值\n   - 例如 \"K*=2 for all C4 models\" → 验证 figure 中的数据确实显示 K*=2\n\n### 也检查论文目录中的图片文件\n```bash\nls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/ 2>/dev/null\n# 或\nfind /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ -name \"*.pdf\" -o -name \"*.png\" -o -name \"*.jpg\" 2>/dev/null\n```\n\n### 关键实验 ID 映射（同 Part 1/2）\n- Qwen-1.5B rewrite: mvp_pilot_sat_v1\n- Pythia-1.4B: exp_001_pythia_depth\n- OLMo-1B: exp_002_olmo_depth\n- Filtering: exp_006_graduated_filtering\n- Decoding ablation: exp_003_decoding_ablation, exp_020_pythia_decoding\n- Cross-transfer: exp_013_cross_transfer\n- Neural probe: exp_015_neural_probe\n- Retrain chain: exp_008_retrain_chain_v2\n- arXiv domain: exp_024_arxiv_domain\n- Power curve: exp_028_power_curve\n\n### 输出格式\n保存到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/audit_appendix_figures.md`：\n\n```markdown\n# 附录+Figure 数据源审计\n\n## 附录数字审计\n### 统计\n- 审计数字总数：N\n- 通过：N\n- 问题：N\n\n### 数字清单\n| # | 数字 | 文件:行号 | 上下文 | 来源 | 匹配? |\n|---|------|----------|--------|------|-------|\n\n### 问题列表\n| # | 问题类型 | 位置 | 描述 | 修复方案 |\n|---|---------|------|------|---------|\n\n## Figure 数据源追溯\n| Figure | 文件名 | 生成脚本 | 数据文件 | 数据存在? | caption数字验证 |\n|--------|--------|---------|---------|----------|---------------|\n\n## Figure 数据问题\n| # | Figure | 问题 | 修复方案 |\n|---|--------|------|---------|\n```\n\n### 注意\n- 不修改任何文件——只审计和记录\n- Figure 追溯的重点是确认 \"figure 读的数据文件\" 和 \"registry 记录的 metrics\" 一致\n- 如果发现 figure 脚本硬编码了数字（而非从数据文件读取），这是一个问题"
}
````

---


### Runtime record

_source line 2 · 2026-05-25T19:44:16.726Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T19:44:16.726Z",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


## Round 1

## Round 1

114 recorded events


### User

_source line 3 · 2026-05-25T19:44:16.774Z_

&lt;project_context>
# 项目: gen-depth-contamination

## 运行环境
- 服务器名: cqa1-22115
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh cqa1-22115  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/gen-depth-contamination


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：附录+Figure 数据源审计（Part 3/3）

### 目标
审计附录中的所有数字 + 追溯所有 Figure 的数据源到具体文件。

### 你负责的文件

**附录**（读取并提取数字）：
1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex`
2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex`

**Figure 数据源**（SSH 到服务器追溯）：
- 服务器：cqa1-22115
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 工作目录：`/root/autodl-tmp/gen-depth-contamination/`

### 附录审计步骤
1. 读取 appendix.tex 和 appendix_extended.tex
2. 提取所有数字（超参表、额外实验结果、数据集统计、失败案例统计等）
3. 用 `read_registry` 验证每个数字

### Figure 数据源追溯步骤

1. **找到所有 Figure 引用**：在所有 .tex 文件中搜索 `\includegraphics` 或 `figure` 环境，列出所有 figure 文件名
   ```bash
   # 在论文目录搜索
   grep -rn "includegraphics\|\\\\input.*fig" /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/
   ```

2. **找到 figure 生成脚本**：SSH 到服务器搜索生成这些 figure 的 Python 脚本
   ```bash
   # 搜索绘图脚本
   find /root/autodl-tmp/gen-depth-contamination/scripts/ -name "*plot*" -o -name "*fig*" -o -name "*figure*" -o -name "*viz*" 2>/dev/null
   grep -rn "savefig\|plt.save" /root/autodl-tmp/gen-depth-contamination/scripts/ 2>/dev/null | head -20
   ```

3. **追溯数据文件**：对每个绘图脚本，找到它读取的数据文件
   ```bash
   # 查看脚本中的数据读取
   grep -n "read_csv\|read_json\|load\|open\|pd.read" &lt;script_path>
   ```

4. **验证数据文件存在且内容合理**：
   ```bash
   ls -la &lt;data_file>
   head -5 &lt;data_file>
   ```

5. **对 Figure caption 中的数字**：追溯到具体数据值
   - 例如 "K*=2 for all C4 models" → 验证 figure 中的数据确实显示 K*=2

### 也检查论文目录中的图片文件
```bash
ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/ 2>/dev/null
# 或
find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ -name "*.pdf" -o -name "*.png" -o -name "*.jpg" 2>/dev/null
```

### 关键实验 ID 映射（同 Part 1/2）
- Qwen-1.5B rewrite: mvp_pilot_sat_v1
- Pythia-1.4B: exp_001_pythia_depth
- OLMo-1B: exp_002_olmo_depth
- Filtering: exp_006_graduated_filtering
- Decoding ablation: exp_003_decoding_ablation, exp_020_pythia_decoding
- Cross-transfer: exp_013_cross_transfer
- Neural probe: exp_015_neural_probe
- Retrain chain: exp_008_retrain_chain_v2
- arXiv domain: exp_024_arxiv_domain
- Power curve: exp_028_power_curve

### 输出格式
保存到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/audit_appendix_figures.md`：

```markdown
# 附录+Figure 数据源审计

## 附录数字审计
### 统计
- 审计数字总数：N
- 通过：N
- 问题：N

### 数字清单
| # | 数字 | 文件:行号 | 上下文 | 来源 | 匹配? |
|---|------|----------|--------|------|-------|

### 问题列表
| # | 问题类型 | 位置 | 描述 | 修复方案 |
|---|---------|------|------|---------|

## Figure 数据源追溯
| Figure | 文件名 | 生成脚本 | 数据文件 | 数据存在? | caption数字验证 |
|--------|--------|---------|---------|----------|---------------|

## Figure 数据问题
| # | Figure | 问题 | 修复方案 |
|---|--------|------|---------|
```

### 注意
- 不修改任何文件——只审计和记录
- Figure 追溯的重点是确认 "figure 读的数据文件" 和 "registry 记录的 metrics" 一致
- 如果发现 figure 脚本硬编码了数字（而非从数据文件读取），这是一个问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "a986dfa4-1dfa-4b23-b2bc-4ed67a18bdfb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-25T19:44:16.774Z_

```json
{
  "parentUuid": "a986dfa4-1dfa-4b23-b2bc-4ed67a18bdfb",
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
  "uuid": "ebb4ed74-750e-4031-86fd-4aa7b3ea4079",
  "timestamp": "2026-05-25T19:44:16.774Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-25T19:44:16.774Z_

```json
{
  "parentUuid": "ebb4ed74-750e-4031-86fd-4aa7b3ea4079",
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
  "uuid": "4dc2024f-c7b3-45c7-ad10-2efdb06e3c8d",
  "timestamp": "2026-05-25T19:44:16.774Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-25T19:44:16.774Z_

```json
{
  "parentUuid": "4dc2024f-c7b3-45c7-ad10-2efdb06e3c8d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "73a56063-d3e4-47ae-96d2-e6b6fdcafecc",
  "timestamp": "2026-05-25T19:44:16.774Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
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
  "aiTitle": "Audit appendix and figure data sources",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Assistant

_source line 8 · 2026-05-25T19:44:20.996Z_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task into parallel work streams:

1. Read the appendix files locally
2. Search for figure references in tex files locally
3. Check for figure files locally
4. Read the registry from the server
5. Search for figure generation scripts on the server

Let me start with the local reads and the registry read in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73a56063-d3e4-47ae-96d2-e6b6fdcafecc",
  "isSidechain": false,
  "requestId": "req_011CbPrquvoRd9jWkupkach7",
  "type": "assistant",
  "uuid": "f27b6d92-c086-4f3c-9435-ee9d9c027df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnVmpH5XCTuWNQNL1PpFEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 604,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13219
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

_source line 9 · 2026-05-25T19:44:22.194Z_

开始审计附录数字和追溯 Figure 数据源。先并行读取附录文件、搜索 figure 引用、检查本地图片文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f27b6d92-c086-4f3c-9435-ee9d9c027df6",
  "isSidechain": false,
  "requestId": "req_011CbPrquvoRd9jWkupkach7",
  "type": "assistant",
  "uuid": "b88bd7ec-41d1-47ca-95b0-6273d5b82d1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnVmpH5XCTuWNQNL1PpFEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 604,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13219
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

_source line 10 · 2026-05-25T19:44:22.725Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Xw7to7gQfNdDkpAVvHap2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b88bd7ec-41d1-47ca-95b0-6273d5b82d1e",
  "isSidechain": false,
  "requestId": "req_011CbPrquvoRd9jWkupkach7",
  "type": "assistant",
  "uuid": "b0d3a388-f597-44c4-ade1-53b2301f8ad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnVmpH5XCTuWNQNL1PpFEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 604,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13219
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

_source line 11 · 2026-05-25T19:44:27.295Z_

<details><summary>↩ Tool result · `toolu_016MUfnow2KB6WHqcRRMd4FR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38a7e501-c3a1-4e5b-b341-7570a41cc7e1",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "e715fc5b-5e42-4b93-8e66-cc2fc4709e51",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 26
  },
  "sourceToolAssistantUUID": "38a7e501-c3a1-4e5b-b341-7570a41cc7e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-25T19:44:22.750Z_

<details><summary>↩ Tool result · `toolu_012Xw7to7gQfNdDkpAVvHap2`</summary>

```text
1	\appendix
2	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
3	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
4	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
5	\setlength{\abovecaptionskip}{4pt}
6	\setlength{\belowcaptionskip}{2pt}
7	\section{Supplementary Materials}
8	\label{sec:appendix}
9	
10	This appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.
11	
12	\paragraph{Feature ranking and cross-model consistency.}
13	Table~\ref{tab:top_features} reports per-model single-feature AUC rankings.
14	Surprisal derivative features (\texttt{surp\_d1\_std}, \texttt{surp\_d2\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\rho \geq 0.85$.
15	The rewrite-mode model (Qwen-rw) diverges by placing \texttt{freq\_entropy} first; this reflects a distributional shift that is lexical rather than surprisal-driven.
16	This scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.
17	
18	%%% Feature ranking table (moved from main text)
19	\begin{table}[!htbp]
20	\centering
21	\small
22	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
23	\label{tab:top_features}
24	\resizebox{\columnwidth}{!}{%
25	\begin{tabular}{cllll}
26	\toprule
27	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
28	\midrule
29	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
30	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
31	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
32	\bottomrule
33	\end{tabular}
34	}
35	\end{table}
36	
37	Table~\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.
38	Classifiers trained on continuation-mode generators (Pythia, OLMo, Qwen-cont) transfer well to each other, with off-diagonal accuracy retaining 80--92\% of in-distribution performance.
39	Rewrite-mode classifiers transfer at 61--63\% to other architectures but retain 82\% within Qwen; generation mode is the primary axis of distributional variation, while a Qwen-specific artifact component persists (Section~\ref{sec:discussion}).
40	
41	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
42	\begin{table}[!htbp]
43	  \centering
44	  \small
45	  \caption{Cross-model transfer accuracy matrix. Diagonal (\textbf{bold}): within-model; off-diagonal: cross-model. Retention: Pythia$\leftrightarrow$OLMo 89--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-rw$\to$Pythia/OLMo 61--63\%, Qwen-rw$\to$Qwen-cont 82\%.}
46	  \label{tab:s1_transfer}
47	  \resizebox{\columnwidth}{!}{%
48	  \begin{tabular}{lcccc}
49	    \toprule
50	    \textbf{Train} & Qwen-rw & Pythia & OLMo & Qwen-cont \\
51	    \midrule
52	    Qwen-rw   & \textbf{.423} & .259 & .265 & .347 \\
53	    Pythia    & .272 & \textbf{.386} & .353 & .329 \\
54	    OLMo      & .277 & .345 & \textbf{.382} & .324 \\
55	    Qwen-cont & .344 & .328 & .311 & \textbf{.388} \\
56	    \bottomrule
57	  \end{tabular}}
58	\end{table}
59	
60	\paragraph{Dataset construction.}
61	Table~\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.
62	Each depth level contains 5{,}000 passagesfor a total of 30{,}000 samples across six depths (0--5).
63	Depth~0 consists of human-written seed texts from the C4 English validation split, truncated to 256 subword tokens.
64	Subsequent depths are generated recursively: each depth-$k$ passage is produced by prompting the generator with the corresponding depth-$(k{-}1)$ passage.
65	All six primary configurations (Qwen2.5-1.5B-Instruct rewrite and continuation, Qwen2.5-1.5B base, Qwen2.5-7B, Pythia-1.4B, OLMo-1B; Table~\ref{tab:setup}) share identical depth-0 seeds, differing only in generator model, scale, and prompting strategy.
66	
67	%%% Table S4: Dataset Statistics
68	\begin{table}[!htbp]
69	  \centering
70	  \small
71	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other five configurations share the same corpus structure.}
72	  \label{tab:s4_dataset_stats}
73	  \resizebox{\columnwidth}{!}{%
74	  \begin{tabular}{clrl}
75	    \toprule
76	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
77	    \midrule
78	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
79	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
80	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
81	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
82	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
83	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
84	    \midrule
85	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
86	    \bottomrule
87	  \end{tabular}}
88	\end{table}
89	
90	\FloatBarrier
91	%%% Table S2: Decoding Ablation AUC (exp-003)
92	\begin{table*}[t]
93	  \centering
94	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
95	  \label{tab:s2_decoding}
96	  \footnotesize
97	  \begin{tabular}{lcccc}
98	    \toprule
99	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
100	    \midrule
101	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
102	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
103	    \cmidrule(lr){1-5}
104	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
105	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
106	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
107	    \midrule
108	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
109	    \midrule
110	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
111	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
112	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
113	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
114	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
115	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
116	    \bottomrule
117	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
118	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
119	  \end{tabular}
120	\end{table*}
121	
122	%%% Table S2b: Extended K* CI (all models including new additions)
123	\begin{table*}[t]
124	  \centering
125	  \footnotesize
126	  \caption{Extended pairwise $\auc$ with bootstrap 95\% CIs for all model configurations including new additions.
127	  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.
128	  $\Kempirical = 2$ holds for 6/10 conditions at $\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\Kempirical{=}1$).
129	  95\% bootstrap CIs shown in brackets where available.}
130	  \label{tab:kstar_ci_extended}
131	  \setlength{\tabcolsep}{3.5pt}
132	  \resizebox{\textwidth}{!}{%
133	  \begin{tabular}{lcccccccccc}
134	    \toprule
135	     & Qwen-rw & Pythia & OLMo & Qwen-cont & Qwen-7B$^\ddagger$ & Qwen-base & LLaMA-8B & Mistral-7B & Pythia-6.9B$^\S$ & Gemma-2B \\
136	    \midrule
137	    0v1 & .9956 & .9722 & .9860 & .9971 & .9644\,[.961,.967] & .987\,[.985,.989] & .9224\,[.917,.927] & .9209\,[.919,.923] & .9599 & .953\,[.949,.957] \\
138	    1v2 & \textbf{.6955}\,[.686,.704]$^*$ & \textbf{.6074}\,[.598,.617]$^*$ & .5001\,[.496,.519] & \textbf{.6112}\,[.602,.621]$^*$ & \textbf{.6178}\,[.608,.626]$^*$ & \textbf{.626}\,[.617,.635]$^*$ & \textbf{.6123}\,[.603,.622]$^*$ & .5695\,[.565,.575] & .5955 & .5981\,[.588,.608] \\
139	    2v3 & .5893\,[.580,.599] & .5440\,[.534,.554] & .4973\,[.486,.509] & .5609\,[.551,.571] & .5492\,[.539,.559] & .550\,[.540,.560] & .5273\,[.517,.538] & .5335\,[.528,.538] & .5298 & .534\,[.523,.545] \\
140	    3v4 & .5435 & .5051 & .5034 & .5409 & .5276 & .529\,[.519,.540] & .5168\,[.506,.528] & .5140 & .5135 & .5033\,[.492,.514] \\
141	    4v5 & .5340 & .5079 & .4971 & .5141 & .5085 & .518\,[.508,.529] & .5159\,[.505,.527] & .5184 & ---$^\|$ & .5025\,[.492,.514] \\
142	    \bottomrule
143	    \multicolumn{11}{l}{\scriptsize $^*$Permutation $p < 0.001$ for all boundary comparisons. Bold: $\auc > \theta{=}0.60$.} \\
144	    \multicolumn{11}{l}{\scriptsize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\
145	    \multicolumn{11}{l}{\scriptsize $^\|$$\Kempirical{=}1$; 4v5 not required for boundary determination.} \\
146	    \multicolumn{11}{l}{\scriptsize $^\S$Pythia-6.9B evaluated separately; nucleus sampling ($p{=}0.95$, $T{=}1.0$), same as all other models.}
147	  \end{tabular}}% end resizebox
148	\end{table*}
149	
150	\FloatBarrier
151	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
152	\begin{table}[t]
153	  \centering
154	  \scriptsize
155	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices. Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\sim}$0.33 vs.\ OBD-LightGBM 0.386). Per-depth recall in Table~\ref{tab:s3c_perdepth}.}
156	  \label{tab:s3_llm_zeroshot}
157	
158	  \vspace{0.3em}
159	  \textbf{(a)} GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)
160	  \vspace{1pt}
161	
162	  \begin{tabular}{lcccccc}
163	    \toprule
164	    & \multicolumn{5}{c}{Predicted Depth} & \\
165	    \cmidrule(lr){2-6}
166	    True & 0 & 1 & 2 & 3 & 4 & Rec. \\
167	    \midrule
168	    0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
169	    1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
170	    2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
171	    3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
172	    4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
173	    \bottomrule
174	  \end{tabular}
175	
176	  \vspace{4pt}
177	  \textbf{(b)} Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)
178	  \vspace{1pt}
179	
180	  \begin{tabular}{lcccccc}
181	    \toprule
182	    & \multicolumn{5}{c}{Predicted Depth} & \\
183	    \cmidrule(lr){2-6}
184	    True & 0 & 1 & 2 & 3 & 4 & Rec. \\
185	    \midrule
186	    0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
187	    1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
188	    2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
189	    3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
190	    4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
191	    \bottomrule
192	  \end{tabular}
193	\end{table}
194	
195	\begin{table}[t]
196	  \centering
197	  \small
198	  \caption{Per-depth recall (\%) on balanced test set ($N{=}500$ for GPT-5.5 and OBD; $N{=}499$ for Claude Opus~4.6 after one invalid response). OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
199	  \label{tab:s3c_perdepth}
200	  \resizebox{\columnwidth}{!}{%
201	  \begin{tabular}{lccccc}
202	    \toprule
203	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
204	    \midrule
205	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
206	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
207	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
208	    \bottomrule
209	  \end{tabular}}
210	\end{table}
211	
212	%%% Table: Token Length and EOS Truncation Analysis
213	\begin{table}[t]
214	  \centering
215	  \scriptsize
216	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound}.}
217	  \label{tab:token_length}
218	  \resizebox{\columnwidth}{!}{%
219	  \begin{tabular}{lcccccccc}
220	    \toprule
221	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
222	    \cmidrule(lr){2-7}
223	    \textbf{Model} & D0 & D1 & D2 & D3 & D4 & D5 & \textbf{EOS\%} & \textbf{Sev.} \\
224	    \midrule
225	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
226	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
227	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negl. \\
228	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Mod. \\
229	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
230	    \midrule
231	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
232	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
233	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
234	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
235	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
236	    \bottomrule
237	    \multicolumn{9}{l}{EOS\%: generation terminated via EOS before 256-token limit. Ranges span depths 1--5.}
238	  \end{tabular}}
239	\end{table}
240	
241	\FloatBarrier
242	%%% Table S5: Complete 15-D Feature Descriptions
243	\begin{table*}[t]
244	  \centering
245	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into four groups: surprisal moments (4~dims) and surprisal derivatives (5~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
246	  \label{tab:s5_features}
247	  \begin{tabular}{llp{0.45\textwidth}l}
248	    \toprule
249	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
250	    \midrule
251	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
252	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
253	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
254	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
255	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
256	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
257	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
258	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
259	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
260	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
261	    \midrule
262	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
263	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
264	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
265	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
266	    \midrule
267	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
268	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
269	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
270	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
271	    \bottomrule
272	  \end{tabular}
273	\end{table*}
274	
275	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
276	\begin{table*}[t]
277	\begin{minipage}[t]{0.45\textwidth}
278	  \centering
279	  \small
280	  \captionof{table}{LightGBM hyperparameters for the OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One cumulative binary classifier is trained for each threshold $k$, predicting whether depth $> k$. Pairwise AUCs are derived from adjacent-depth comparisons to evaluate separability. 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
281	  \label{tab:s6_lgbm_params}
282	  \begin{tabular}{ll}
283	    \toprule
284	    \textbf{Parameter} & \textbf{Value} \\
285	    \midrule
286	    \texttt{n\_estimators}      & 200 \\
287	    \texttt{learning\_rate}     & 0.05 \\
288	    \texttt{max\_depth}         & 6 \\
289	    \texttt{num\_leaves}        & 31 \\
290	    \texttt{verbose}            & $-1$ \\
291	    \texttt{n\_jobs}            & $-1$ (all cores) \\
292	    Cross-validation            & 5-fold GroupKFold \\
293	    Grouping key                & \texttt{doc\_id} \\
294	    Objective                   & Binary (per depth pair) \\
295	    \bottomrule
296	  \end{tabular}
297	\end{minipage}\hfill
298	\begin{minipage}[t]{0.52\textwidth}
299	  \centering
300	  \small
301	  \captionof{table}{Neural probe architecture and training details. Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
302	  \label{tab:s7_neural_probe}
303	  \resizebox{\textwidth}{!}{%
304	  \begin{tabular}{ll}
305	    \toprule
306	    \textbf{Component} & \textbf{Details} \\
307	    \midrule
308	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
309	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
310	    Representation    & Last hidden state, attention-masked avg pool \\
311	    Embedding dim     & 1536 / 2048 / 2048 \\
312	    Max sequence len   & 512 tokens \\
313	    \midrule
314	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
315	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
316	    Activations       & ReLU \\
317	    Dropout           & 0.1 (after each hidden layer) \\
318	    Output            & 6-class softmax \\
319	    \midrule
320	    \multicolumn{2}{l}{\textit{Training}} \\
321	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
322	    Loss              & Cross-entropy \\
323	    Batch size        & 256 \\
324	    Max epochs        & 20 \\
325	    Early stopping    & Patience = 5 (validation loss) \\
326	    Cross-validation  & 5-fold GroupKFold \\
327	    \bottomrule
328	  \end{tabular}%
329	  }
330	\end{minipage}
331	\end{table*}
332	
333	\FloatBarrier
334	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
335	\begin{table}[!htbp]
336	  \centering
337	  \scriptsize
338	  \caption{Pairwise AUC with bootstrap 95\% CIs for four of six primary configurations (1{,}000 resamples). All boundary pairs ($\auc > \theta$) $p < 0.01$; OLMo 1v2--4v5 non-significant ($p > 0.09$).}
339	  \label{tab:s8_cv_folds}
340	  \resizebox{\columnwidth}{!}{%
341	  \begin{tabular}{lcccc}
342	    \toprule
343	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
344	    \midrule
345	    0v1 & $.996\;[.995,.997]$ & $.972$ & $.986\;[.984,.988]$ & $.997\;[.996,.998]$ \\
346	    1v2 & $.696\;[.686,.704]$ & $.607\;[.598,.617]$ & $.500\;[.496,.519]$ & $.611\;[.602,.621]$ \\
347	    \cmidrule(lr){1-5}
348	    2v3 & $.589\;[.580,.599]$ & $.544\;[.534,.554]$ & $.497\;[.486,.509]$ & $.561\;[.551,.571]$ \\
349	    3v4 & $.544\;[.533,.555]$ & $.505$ & $.503\;[.491,.513]$ & $.541\;[.531,.551]$ \\
350	    4v5 & $.534\;[.524,.545]$ & $.508$ & $.497\;[.483,.506]$ & $.514\;[.504,.526]$ \\
351	    \bottomrule
352	  \end{tabular}}
353	\end{table}
354	
355	%%% Table S9: Binary Detector Spearman ρ (exp-012)
356	\begin{table}[!htbp]
357	  \centering
358	  \scriptsize
359	  \caption{Spearman $\rho$ between binary detector scores and true depth, and 6-class accuracy. Correlations driven by 0v1; scores do not track depth beyond generation~1. Qwen-rw exhibits reversed sign ($\rho > 0$).}
360	  \label{tab:s9_binary_spearman}
361	  \resizebox{\columnwidth}{!}{%
362	  \begin{tabular}{lcccc}
363	    \toprule
364	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
365	    \midrule
366	    \multicolumn{5}{l}{\textit{Spearman $\rho$}} \\
367	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
368	    \quad log-PPL (obs.)     & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
369	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
370	    \midrule
371	    6-class acc.              & 0.199    & 0.130    & 0.127    & 0.183 \\
372	    \bottomrule
373	    \multicolumn{5}{l}{Random baseline: 0.167} \\
374	  \end{tabular}}
375	\end{table}
376	
377	%%% Table S10: Pythia Decoding Ablation (exp-020)
378	\begin{table}[!htbp]
379	  \centering
380	  \scriptsize
381	  \caption{Pythia-1.4B pairwise $\auc$ under four decoding configs (10K bootstrap). $^\dagger$Greedy triggers repetition collapse (4-gram repeat: $d_0{=}0.01 \to d_1{=}0.72$).}
382	  \label{tab:s10_pythia_decoding}
383	  \resizebox{\columnwidth}{!}{%
384	  \begin{tabular}{lcccc}
385	    \toprule
386	    & \textbf{Greedy}$^\dagger$ & \textbf{$p{=}0.9$} & \textbf{$T{=}0.7$} & \textbf{$T{=}1.2$} \\
387	    \midrule
388	    0v1 & $.999$ & $.995$ & $.997$ & $.993$ \\
389	    1v2 & $.884$ & $.677$ & $.727$ & $.617$ \\
390	    \cmidrule(lr){1-5}
391	    2v3 & $.534$ & $.555$ & $.594^\ddagger$ & $.523$ \\
392	    3v4 & $.523$ & $.530$ & $.570$ & $.517$ \\
393	    4v5 & $.516$ & $.501$ & $.528$ & $.505$ \\
394	    \midrule
395	    $\Kempirical$ & 2 & 2 & 2 & 2 \\
396	    \bottomrule
397	    \multicolumn{5}{l}{${}^{\ddagger}$CI upper 0.606 $> \theta$; point est.\ below.} \\
398	  \end{tabular}}
399	\end{table}
400	
401	%%% Table S11: Length Ablation (exp-021)
402	\begin{table}[!htbp]
403	  \centering
404	  \small
405	  \caption{Pairwise $\auc$ for three segment lengths (Qwen-base, cont.\ mode). $\Kempirical{=}2$ at 128/256; 512 marginal ($^\dagger$CI lower $< \theta$).}
406	  \label{tab:s11_length_ablation}
407	  \begin{tabular}{lccc}
408	    \toprule
409	    & \textbf{128} & \textbf{256} & \textbf{512} \\
410	    \midrule
411	    0v1 & .979 & .991 & .992 \\
412	    1v2 & .622 & .628 & .607$^\dagger$ \\
413	    \cmidrule(lr){1-4}
414	    2v3 & .529 & .556 & .572 \\
415	    3v4 & .535 & .530 & .530 \\
416	    4v5 & .501 & .514 & .518 \\
417	    \midrule
418	    $\Kempirical$ & 2 & 2 & 2$^\dagger$ \\
419	    \bottomrule
420	  \end{tabular}
421	\end{table}
422	
423	%%% Table S12: Domain Ablation
424	\begin{table}[!htbp]
425	  \centering
426	  \small
427	  \caption{Pairwise $\auc$ for three text domains (Qwen-cont). arXiv yields $\Kempirical{=}3$; C4 and Wikipedia $\Kempirical{=}2$.}
428	  \label{tab:s12_domain_ablation}
429	  \begin{tabular}{lccc}
430	    \toprule
431	    & \textbf{C4} & \textbf{Wiki} & \textbf{arXiv} \\
432	    \midrule
433	    0v1 & .997 & .996 & .995 \\
434	    1v2 & .611 & .619 & .858 \\
435	    \cmidrule(lr){1-4}
436	    2v3 & .561 & .550 & .643$^*$ \\
437	    3v4 & .541 & .523 & .544 \\
438	    4v5 & .514 & .514 & .529 \\
439	    \midrule
440	    $\Kempirical$ & 2 & 2 & 3 \\
441	    \bottomrule
442	    \multicolumn{4}{l}{\footnotesize $^*$CI $[.628,.658]$; $p < 0.001$.}
443	  \end{tabular}
444	\end{table}
445	
446	%%% Table S13: Scorer Sensitivity Analysis
447	\begin{table}[!htbp]
448	  \centering
449	  \scriptsize
450	  \caption{Scorer sensitivity: $\Kempirical$ under self- vs.\ cross-scoring. Cross-scoring reduces $\Kempirical$ only for marginal Qwen-cont.}
451	  \label{tab:s13_scorer_sensitivity}
452	  \resizebox{\columnwidth}{!}{%
453	  \begin{tabular}{llcccc}
454	    \toprule
455	    \textbf{Generator} & \textbf{Mode} & \textbf{Self} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Agr.} \\
456	    \midrule
457	    Qwen-Inst & Rewrite & 2 & 2 & 2 & \checkmark \\
458	    Qwen-Inst & Cont.   & 2 & 1 & 1 & $\times$ \\
459	    Qwen-base & Cont.   & 2 & 2 & 2 & \checkmark \\
460	    Pythia    & Cont.   & 2 & 2 & 2 & \checkmark \\
461	    OLMo      & Cont.   & 1 & -- & -- & -- \\
462	    Qwen-7B   & Cont.   & 2 & -- & -- & -- \\
463	    Mistral   & Cont.   & 1 & -- & -- & -- \\
464	    \bottomrule
465	  \end{tabular}}
466	\end{table}
467	
468	\FloatBarrier
469	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0d3a388-f597-44c4-ade1-53b2301f8ad8",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "93a47edc-03a5-4f15-875d-fb416854fd18",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\\appendix\n\\setlength{\\floatsep}{6pt plus 2pt minus 2pt}\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 2pt}\n\\setlength{\\intextsep}{6pt plus 2pt minus 2pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{2pt}\n\\section{Supplementary Materials}\n\\label{sec:appendix}\n\nThis appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.\n\n\\paragraph{Feature ranking and cross-model consistency.}\nTable~\\ref{tab:top_features} reports per-model single-feature AUC rankings.\nSurprisal derivative features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_d2\\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\\rho \\geq 0.85$.\nThe rewrite-mode model (Qwen-rw) diverges by placing \\texttt{freq\\_entropy} first; this reflects a distributional shift that is lexical rather than surprisal-driven.\nThis scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.\n\n%%% Feature ranking table (moved from main text)\n\\begin{table}[!htbp]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\n\\label{tab:top_features}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1 & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\texttt{freq\\_entropy} & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2 & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_std}} \\\\\n3 & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nTable~\\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.\nClassifiers trained on continuation-mode generators (Pythia, OLMo, Qwen-cont) transfer well to each other, with off-diagonal accuracy retaining 80--92\\% of in-distribution performance.\nRewrite-mode classifiers transfer at 61--63\\% to other architectures but retain 82\\% within Qwen; generation mode is the primary axis of distributional variation, while a Qwen-specific artifact component persists (Section~\\ref{sec:discussion}).\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Cross-model transfer accuracy matrix. Diagonal (\\textbf{bold}): within-model; off-diagonal: cross-model. Retention: Pythia$\\leftrightarrow$OLMo 89--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-rw$\\to$Pythia/OLMo 61--63\\%, Qwen-rw$\\to$Qwen-cont 82\\%.}\n  \\label{tab:s1_transfer}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Train} & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{.423} & .259 & .265 & .347 \\\\\n    Pythia    & .272 & \\textbf{.386} & .353 & .329 \\\\\n    OLMo      & .277 & .345 & \\textbf{.382} & .324 \\\\\n    Qwen-cont & .344 & .328 & .311 & \\textbf{.388} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\paragraph{Dataset construction.}\nTable~\\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.\nEach depth level contains 5{,}000 passagesfor a total of 30{,}000 samples across six depths (0--5).\nDepth~0 consists of human-written seed texts from the C4 English validation split, truncated to 256 subword tokens.\nSubsequent depths are generated recursively: each depth-$k$ passage is produced by prompting the generator with the corresponding depth-$(k{-}1)$ passage.\nAll six primary configurations (Qwen2.5-1.5B-Instruct rewrite and continuation, Qwen2.5-1.5B base, Qwen2.5-7B, Pythia-1.4B, OLMo-1B; Table~\\ref{tab:setup}) share identical depth-0 seeds, differing only in generator model, scale, and prompting strategy.\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other five configurations share the same corpus structure.}\n  \\label{tab:s4_dataset_stats}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{clrl}\n    \\toprule\n    \\textbf{Depth} & \\textbf{$N$ samples} & \\textbf{Mean tokens} & \\textbf{Source} \\\\\n    \\midrule\n    0 & 5{,}000 & 147.8 & C4 validation (human) \\\\\n    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\\\\n    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\\\\n    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\\\\n    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Total} & \\multicolumn{2}{l}{30{,}000 samples} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\FloatBarrier\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$. Bottom rows report cross-configuration Spearman $\\rho$ on per-feature discriminative-power rankings.}\n  \\label{tab:s2_decoding}\n  \\footnotesize\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & $.980\\;[.977,\\,.982]$ & $.995\\;[.993,\\,.996]$ & $.988\\;[.986,\\,.990]$ & $.998\\;[.998,\\,.999]$ \\\\\n    1 vs.\\ 2 & $.689\\;[.680,\\,.698]$ & $.687\\;[.677,\\,.695]$ & $.689\\;[.680,\\,.697]$ & $.704\\;[.695,\\,.713]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & $.561\\;[.552,\\,.571]$ & $.592\\;[.582,\\,.601]$\\rlap{$^\\dagger$} & $.590\\;[.581,\\,.600]$ & $.582\\;[.572,\\,.592]$ \\\\\n    3 vs.\\ 4 & $.540\\;[.531,\\,.550]$ & $.547\\;[.537,\\,.557]$ & $.539\\;[.529,\\,.549]$ & $.529\\;[.519,\\,.540]$ \\\\\n    4 vs.\\ 5 & $.514\\;[.503,\\,.524]$ & $.507\\;[.496,\\,.517]^{\\ddagger}$ & $.535\\;[.524,\\,.545]$ & $.524\\;[.513,\\,.535]$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\dagger}$\\,CI upper bound (0.601) marginally exceeds $\\theta{=}0.60$ by 0.001.} \\\\\n    \\multicolumn{5}{l}{${}^{\\ddagger}$\\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S2b: Extended K* CI (all models including new additions)\n\\begin{table*}[t]\n  \\centering\n  \\footnotesize\n  \\caption{Extended pairwise $\\auc$ with bootstrap 95\\% CIs for all model configurations including new additions.\n  This table extends Table~\\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.\n  $\\Kempirical = 2$ holds for 6/10 conditions at $\\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\\Kempirical{=}1$).\n  95\\% bootstrap CIs shown in brackets where available.}\n  \\label{tab:kstar_ci_extended}\n  \\setlength{\\tabcolsep}{3.5pt}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{lcccccccccc}\n    \\toprule\n     & Qwen-rw & Pythia & OLMo & Qwen-cont & Qwen-7B$^\\ddagger$ & Qwen-base & LLaMA-8B & Mistral-7B & Pythia-6.9B$^\\S$ & Gemma-2B \\\\\n    \\midrule\n    0v1 & .9956 & .9722 & .9860 & .9971 & .9644\\,[.961,.967] & .987\\,[.985,.989] & .9224\\,[.917,.927] & .9209\\,[.919,.923] & .9599 & .953\\,[.949,.957] \\\\\n    1v2 & \\textbf{.6955}\\,[.686,.704]$^*$ & \\textbf{.6074}\\,[.598,.617]$^*$ & .5001\\,[.496,.519] & \\textbf{.6112}\\,[.602,.621]$^*$ & \\textbf{.6178}\\,[.608,.626]$^*$ & \\textbf{.626}\\,[.617,.635]$^*$ & \\textbf{.6123}\\,[.603,.622]$^*$ & .5695\\,[.565,.575] & .5955 & .5981\\,[.588,.608] \\\\\n    2v3 & .5893\\,[.580,.599] & .5440\\,[.534,.554] & .4973\\,[.486,.509] & .5609\\,[.551,.571] & .5492\\,[.539,.559] & .550\\,[.540,.560] & .5273\\,[.517,.538] & .5335\\,[.528,.538] & .5298 & .534\\,[.523,.545] \\\\\n    3v4 & .5435 & .5051 & .5034 & .5409 & .5276 & .529\\,[.519,.540] & .5168\\,[.506,.528] & .5140 & .5135 & .5033\\,[.492,.514] \\\\\n    4v5 & .5340 & .5079 & .4971 & .5141 & .5085 & .518\\,[.508,.529] & .5159\\,[.505,.527] & .5184 & ---$^\\|$ & .5025\\,[.492,.514] \\\\\n    \\bottomrule\n    \\multicolumn{11}{l}{\\scriptsize $^*$Permutation $p < 0.001$ for all boundary comparisons. Bold: $\\auc > \\theta{=}0.60$.} \\\\\n    \\multicolumn{11}{l}{\\scriptsize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\\\\n    \\multicolumn{11}{l}{\\scriptsize $^\\|$$\\Kempirical{=}1$; 4v5 not required for boundary determination.} \\\\\n    \\multicolumn{11}{l}{\\scriptsize $^\\S$Pythia-6.9B evaluated separately; nucleus sampling ($p{=}0.95$, $T{=}1.0$), same as all other models.}\n  \\end{tabular}}% end resizebox\n\\end{table*}\n\n\\FloatBarrier\n%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{LLM zero-shot depth classification: $5{\\times}5$ confusion matrices. Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\\sim}$0.33 vs.\\ OBD-LightGBM 0.386). Per-depth recall in Table~\\ref{tab:s3c_perdepth}.}\n  \\label{tab:s3_llm_zeroshot}\n\n  \\vspace{0.3em}\n  \\textbf{(a)} GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{77} & 18 &  4 &  0 &  1 & .770 \\\\\n    1 &  9 & \\textbf{19} & 36 & 24 & 12 & .190 \\\\\n    2 &  8 & 10 & \\textbf{38} & 35 &  9 & .380 \\\\\n    3 & 10 & 16 & 35 & \\textbf{24} & 15 & .240 \\\\\n    4 & 11 & 13 & 50 & 18 &  \\textbf{8} & .080 \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\textbf{(b)} Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{69} & 26 &  3 &  0 &  2 & .690 \\\\\n    1 &  8 & \\textbf{21} & 32 & 11 & 28 & .210 \\\\\n    2 &  6 & 36 & \\textbf{28} &  5 & 25 & .280 \\\\\n    3 &  7 & 20 & 31 & \\textbf{10} & 31 & .100 \\\\\n    4 &  7 & 28 & 22 &  6 & \\textbf{37} & .370 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced test set ($N{=}500$ for GPT-5.5 and OBD; $N{=}499$ for Claude Opus~4.6 after one invalid response). OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\\\\n    \\midrule\n    OBD-LightGBM & \\textbf{96} & \\textbf{39} & 14 & 19 & 22 \\\\\n    GPT-5.5      & 77 & 19 & \\textbf{38} & \\textbf{24} &  8 \\\\\n    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \\textbf{37} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound}.}\n  \\label{tab:token_length}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & D0 & D1 & D2 & D3 & D4 & D5 & \\textbf{EOS\\%} & \\textbf{Sev.} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negl. \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Mod. \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n    \\multicolumn{9}{l}{EOS\\%: generation terminated via EOS before 256-token limit. Ranges span depths 1--5.}\n  \\end{tabular}}\n\\end{table}\n\n\\FloatBarrier\n%%% Table S5: Complete 15-D Feature Descriptions\n\\begin{table*}[t]\n  \\centering\n  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into four groups: surprisal moments (4~dims) and surprisal derivatives (5~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\n  \\label{tab:s5_features}\n  \\begin{tabular}{llp{0.45\\textwidth}l}\n    \\toprule\n    \\textbf{Group} & \\textbf{Feature} & \\textbf{Description} & \\textbf{Range} \\\\\n    \\midrule\n    \\multirow{9}{*}{\\rotatebox[origin=c]{90}{\\textsc{Surprisal}}}\n    & \\texttt{surp\\_mean}   & Mean token surprisal $\\frac{1}{T}\\sum_t -\\log p(x_t \\mid x_{&lt;t})$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_std}    & Standard deviation of token surprisal & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_skew}   & Skewness of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_kurt}   & Excess kurtosis of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_mean} & Mean of first-order surprisal differences $\\Delta s_t = s_{t+1} - s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_std}  & Std of first-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_d1\\_skew} & Skewness of first-order surprisal differences & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_mean} & Mean of second-order differences $\\Delta^2 s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_std}  & Std of second-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Lex}}}\n    & \\texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\\\\n    & \\texttt{hapax\\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\\\\n    & \\texttt{self\\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Freq}}}\n    & \\texttt{freq\\_kurtosis}  & Excess kurtosis of word frequency distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{freq\\_entropy}   & Shannon entropy of word frequencies: $-\\sum p_w \\log_2 p_w$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{low\\_freq\\_ratio} & Proportion of vocabulary with count $\\leq 2$ & $[0, 1]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap\n\\begin{table*}[t]\n\\begin{minipage}[t]{0.45\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{LightGBM hyperparameters for the OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One cumulative binary classifier is trained for each threshold $k$, predicting whether depth $> k$. Pairwise AUCs are derived from adjacent-depth comparisons to evaluate separability. 5-fold GroupKFold cross-validation is grouped by \\texttt{doc\\_id} to prevent data leakage from the same seed document appearing in both train and test.}\n  \\label{tab:s6_lgbm_params}\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Parameter} & \\textbf{Value} \\\\\n    \\midrule\n    \\texttt{n\\_estimators}      & 200 \\\\\n    \\texttt{learning\\_rate}     & 0.05 \\\\\n    \\texttt{max\\_depth}         & 6 \\\\\n    \\texttt{num\\_leaves}        & 31 \\\\\n    \\texttt{verbose}            & $-1$ \\\\\n    \\texttt{n\\_jobs}            & $-1$ (all cores) \\\\\n    Cross-validation            & 5-fold GroupKFold \\\\\n    Grouping key                & \\texttt{doc\\_id} \\\\\n    Objective                   & Binary (per depth pair) \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{minipage}\\hfill\n\\begin{minipage}[t]{0.52\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{Neural probe architecture and training details. Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}\n  \\label{tab:s7_neural_probe}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Component} & \\textbf{Details} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Embedding extraction}} \\\\\n    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\\\\n    Representation    & Last hidden state, attention-masked avg pool \\\\\n    Embedding dim     & 1536 / 2048 / 2048 \\\\\n    Max sequence len   & 512 tokens \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{MLP classifier}} \\\\\n    Architecture      & $d_{\\text{emb}} \\to 512 \\to 256 \\to 6$ \\\\\n    Activations       & ReLU \\\\\n    Dropout           & 0.1 (after each hidden layer) \\\\\n    Output            & 6-class softmax \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Training}} \\\\\n    Optimizer         & Adam ($\\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\\\\n    Loss              & Cross-entropy \\\\\n    Batch size        & 256 \\\\\n    Max epochs        & 20 \\\\\n    Early stopping    & Patience = 5 (validation loss) \\\\\n    Cross-validation  & 5-fold GroupKFold \\\\\n    \\bottomrule\n  \\end{tabular}%\n  }\n\\end{minipage}\n\\end{table*}\n\n\\FloatBarrier\n%%% Table S8: Per-Model Bootstrap CI Results (exp-007)\n\\begin{table}[!htbp]\n  \\centering\n  \\scriptsize\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs for four of six primary configurations (1{,}000 resamples). All boundary pairs ($\\auc > \\theta$) $p < 0.01$; OLMo 1v2--4v5 non-significant ($p > 0.09$).}\n  \\label{tab:s8_cv_folds}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    0v1 & $.996\\;[.995,.997]$ & $.972$ & $.986\\;[.984,.988]$ & $.997\\;[.996,.998]$ \\\\\n    1v2 & $.696\\;[.686,.704]$ & $.607\\;[.598,.617]$ & $.500\\;[.496,.519]$ & $.611\\;[.602,.621]$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.589\\;[.580,.599]$ & $.544\\;[.534,.554]$ & $.497\\;[.486,.509]$ & $.561\\;[.551,.571]$ \\\\\n    3v4 & $.544\\;[.533,.555]$ & $.505$ & $.503\\;[.491,.513]$ & $.541\\;[.531,.551]$ \\\\\n    4v5 & $.534\\;[.524,.545]$ & $.508$ & $.497\\;[.483,.506]$ & $.514\\;[.504,.526]$ \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S9: Binary Detector Spearman ρ (exp-012)\n\\begin{table}[!htbp]\n  \\centering\n  \\scriptsize\n  \\caption{Spearman $\\rho$ between binary detector scores and true depth, and 6-class accuracy. Correlations driven by 0v1; scores do not track depth beyond generation~1. Qwen-rw exhibits reversed sign ($\\rho > 0$).}\n  \\label{tab:s9_binary_spearman}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Spearman $\\rho$}} \\\\\n    \\quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\\\\n    \\quad log-PPL (obs.)     & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\\\\n    \\quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\\\\n    \\midrule\n    6-class acc.              & 0.199    & 0.130    & 0.127    & 0.183 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{Random baseline: 0.167} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S10: Pythia Decoding Ablation (exp-020)\n\\begin{table}[!htbp]\n  \\centering\n  \\scriptsize\n  \\caption{Pythia-1.4B pairwise $\\auc$ under four decoding configs (10K bootstrap). $^\\dagger$Greedy triggers repetition collapse (4-gram repeat: $d_0{=}0.01 \\to d_1{=}0.72$).}\n  \\label{tab:s10_pythia_decoding}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Greedy}$^\\dagger$ & \\textbf{$p{=}0.9$} & \\textbf{$T{=}0.7$} & \\textbf{$T{=}1.2$} \\\\\n    \\midrule\n    0v1 & $.999$ & $.995$ & $.997$ & $.993$ \\\\\n    1v2 & $.884$ & $.677$ & $.727$ & $.617$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.534$ & $.555$ & $.594^\\ddagger$ & $.523$ \\\\\n    3v4 & $.523$ & $.530$ & $.570$ & $.517$ \\\\\n    4v5 & $.516$ & $.501$ & $.528$ & $.505$ \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2 & 2 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\ddagger}$CI upper 0.606 $> \\theta$; point est.\\ below.} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S11: Length Ablation (exp-021)\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three segment lengths (Qwen-base, cont.\\ mode). $\\Kempirical{=}2$ at 128/256; 512 marginal ($^\\dagger$CI lower $< \\theta$).}\n  \\label{tab:s11_length_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{128} & \\textbf{256} & \\textbf{512} \\\\\n    \\midrule\n    0v1 & .979 & .991 & .992 \\\\\n    1v2 & .622 & .628 & .607$^\\dagger$ \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .529 & .556 & .572 \\\\\n    3v4 & .535 & .530 & .530 \\\\\n    4v5 & .501 & .514 & .518 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2$^\\dagger$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n%%% Table S12: Domain Ablation\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three text domains (Qwen-cont). arXiv yields $\\Kempirical{=}3$; C4 and Wikipedia $\\Kempirical{=}2$.}\n  \\label{tab:s12_domain_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{C4} & \\textbf{Wiki} & \\textbf{arXiv} \\\\\n    \\midrule\n    0v1 & .997 & .996 & .995 \\\\\n    1v2 & .611 & .619 & .858 \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .561 & .550 & .643$^*$ \\\\\n    3v4 & .541 & .523 & .544 \\\\\n    4v5 & .514 & .514 & .529 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n    \\multicolumn{4}{l}{\\footnotesize $^*$CI $[.628,.658]$; $p < 0.001$.}\n  \\end{tabular}\n\\end{table}\n\n%%% Table S13: Scorer Sensitivity Analysis\n\\begin{table}[!htbp]\n  \\centering\n  \\scriptsize\n  \\caption{Scorer sensitivity: $\\Kempirical$ under self- vs.\\ cross-scoring. Cross-scoring reduces $\\Kempirical$ only for marginal Qwen-cont.}\n  \\label{tab:s13_scorer_sensitivity}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{llcccc}\n    \\toprule\n    \\textbf{Generator} & \\textbf{Mode} & \\textbf{Self} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Agr.} \\\\\n    \\midrule\n    Qwen-Inst & Rewrite & 2 & 2 & 2 & \\checkmark \\\\\n    Qwen-Inst & Cont.   & 2 & 1 & 1 & $\\times$ \\\\\n    Qwen-base & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    Pythia    & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    OLMo      & Cont.   & 1 & -- & -- & -- \\\\\n    Qwen-7B   & Cont.   & 2 & -- & -- & -- \\\\\n    Mistral   & Cont.   & 1 & -- & -- & -- \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\FloatBarrier\n",
      "numLines": 469,
      "startLine": 1,
      "totalLines": 469
    }
  },
  "sourceToolAssistantUUID": "b0d3a388-f597-44c4-ade1-53b2301f8ad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-25T19:44:23.813Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GBWf42NuBStg4sSnpVbUna`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93a47edc-03a5-4f15-875d-fb416854fd18",
  "isSidechain": false,
  "requestId": "req_011CbPrquvoRd9jWkupkach7",
  "type": "assistant",
  "uuid": "6f936636-2d38-4900-88b4-0babd9e18b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnVmpH5XCTuWNQNL1PpFEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 604,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13219
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

_source line 14 · 2026-05-25T19:44:23.823Z_

<details><summary>↩ Tool result · `toolu_01GBWf42NuBStg4sSnpVbUna`</summary>

```text
1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6862, 0.7037]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--92\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), which enables single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 89--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{table}[h]
16	\centering
17	\caption{Cross-scorer validation. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1. OLMo arXiv cross-scorer confirms $\Kempirical{=}1$ ($p{=}0.510$, n.s.).}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{table}
21	
22	\begin{table}[h]
23	\centering
24	\small
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs). Scorer is statistically significant but explains modest variance ($\eta^2_p{=}.192$) relative to Depth-Pair ($\eta^2_p{=}.998$), which supports near-scorer-independence of depth discrimination.}
26	\label{tab:anova_crossscorer}
27	\begin{tabular}{lrrrr}
28	\toprule
29	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
30	\midrule
31	Generator     & 2  & 926.78  & ${<}.001$  & .885 \\
32	Scorer        & 3  & 19.02  & ${<}.001$  & .192 \\
33	Depth-Pair    & 4  & 24736.10  & ${<}.001$  & .998 \\
34	Gen$\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\
35	Gen$\times$Depth  & 8 & 993.69 & ${<}.001$ & .971 \\
36	Scorer$\times$Depth & 12 & 2.45 & $.005$ & .109 \\
37	Residual      & 240 & & & \\
38	\bottomrule
39	\end{tabular}
40	\end{table}
41	
42	\subsection{Feature Importance Across Decoding Strategies}
43	
44	Feature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\rho = 0.914$), while greedy vs.\ $T{=}1.2$ yields lower correlation ($\rho = 0.53$, nonsignificant after Bonferroni).
45	The depth boundary is robust but the optimal feature subset is strategy-dependent.
46	
47	\subsection{Scale and Neural Probe}
48	\label{sec:extended_neural_probe}
49	
50	Cross-scale validation confirms $\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6178$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$, 0v1 $= 0.9224$) both exceed $\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text.
51	Gemma-2-27B (C4 continuation, Qwen cross-scored) yields $\Kempirical{=}1$ (1v2 $\auc = 0.5894$), consistent with Gemma-2-2B at 5K ($\Kempirical{=}1$, 1v2 $\auc = 0.5981$). The Gemma family produces $\Kempirical{=}1$ at both 2B and 27B; $\Kempirical$ is model-family-dependent rather than scale-dependent.
52	
53	The neural probe yields model-dependent $\Kempirical^{\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia; OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$), consistent with the 15D LightGBM boundary.
54	The 15D generator-agnostic features yield $\Kempirical = 2$ for Pythia and Qwen, while OLMo yields $\Kempirical = 1$ under the standardized pipeline.
55	
56	\subsection{LLM Zero-Shot Baseline}
57	\label{sec:extended_llm}
58	
59	GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10; $N{=}500$) and Claude Opus~4.6 33.1\% (MAE = 1.15; $N{=}499$ after one invalid response) on a balanced test set, comparable to OBD-LightGBM's 38.6\% (95\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\ref{tab:s3_llm_zeroshot}).
60	Per-depth recall confirms convergent failure at depths $\geq 2$ (Section~\ref{sec:why_kstar}).
61	The LLM baseline evaluates depths 0--4 (5-class; Table~\ref{tab:s3_llm_zeroshot}). When probabilities are marginalized to 4 classes ($P(d{\geq}3)$), accuracy rises to 44.4\% but concentrates in the merged class while depths 2--3 collapse to 2--8\%.
62	
63	\subsection{Practical Considerations}
64	
65	All filtering strategies degrade general capabilities (MMLU: 0.6018 $\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\to$ 0.6631--0.6701); our depth-chain setting (${\sim}$83\% synthetic) is an upper bound; in mixed corpora, degradation scales with contamination fraction~\cite{shumailov2024collapse, dohmatob2024model}.
66	$\Kstar$-aware binary filtering reduces MMLU degradation by ${\sim}$50\% ($-$1.53\,pp $\to$ $-$0.77\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).
67	
68	\subsection{Additional Scope Analysis}
69	\label{sec:extended_limitations}
70	
71	\emph{Prompt-chain versus retrain-chain.}
72	Retrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 2v3 $= 0.8888$, 3v4 $= 0.7982$), far exceeding prompt-chain $\Kempirical{=}2$.
73	The elevated signal arises from cumulative model-adaptation artifacts rather than text-intrinsic degradation; prompt-chain $\Kempirical$ is the operationally relevant boundary for data curation.
74	
75	\emph{Threshold sensitivity.}
76	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$ across all configurations (Figure~\ref{fig:kstar_theta}).
77	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
78	
79	\emph{Structural confound: token length.}
80	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
81	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
82	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
83	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
84	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
85	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}); EOS truncation does not drive the boundary.
86	
87	\emph{Graduated filtering.}
88	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
89	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
90	\label{tab:pairwise_significance}
91	
92	\subsection{Dose-Response: Contamination Ratio Effect}
93	\label{sec:dose_response}
94	
95	The main filtering experiments (Section~\ref{sec:filtering}) use the full depth chain (depths 0--5, ${\sim}$83\% synthetic) to maximize effect size.
96	To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
97	
98	\begin{table}[h]
99	\centering
100	\small
101	\caption{MMLU accuracy by contamination ratio (fraction of synthetic data in training set) and filtering strategy. Base model (no fine-tuning): 0.6018. Mean $\pm$ std over 5 seeds.}
102	\label{tab:dose_response}
103	\resizebox{\columnwidth}{!}{%
104	\begin{tabular}{lccc}
105	\toprule
106	\textbf{Strategy} & \textbf{10\%} & \textbf{30\%} & \textbf{50\%} \\
107	\midrule
108	No-filter   & $0.6058 \pm .0002$ & $0.6069 \pm .0007$ & $0.6063 \pm .0013$ \\
109	Binary-ours & $0.6079 \pm .0005$ & $0.6082 \pm .0012$ & $0.6088 \pm .0011$ \\
110	Graduated   & $0.6066 \pm .0011$ & $0.6072 \pm .0008$ & $0.6062 \pm .0009$ \\
111	\bottomrule
112	\end{tabular}}
113	\end{table}
114	
115	{\sloppy At all three contamination ratios, fine-tuning on the mixed corpus yields MMLU above the base model ($0.6018$); the clean-data majority dominates the training signal.
116	Strategy differences are small: binary-ours exceeds no-filter by $0.21$\,pp at 10\% ($p = 0.001$), $0.13$\,pp at 30\% ($p = 0.074$), and $0.25$\,pp at 50\% ($p = 0.038$).
117	While binary reaches statistical significance at 10\% and 50\% due to high power (5 seeds, low variance), the maximum strategy spread remains below 0.3\,pp across all ratios.
118	The strategy ordering (binary $>$ graduated $>$ no-filter) is consistent with the depth-chain setting, but effect sizes are negligible compared to that setting ($-$1.53\,pp no-filter degradation).
119	This demonstrates that $\Kstar$-aware curation provides practical benefit primarily when contamination is severe enough to cause measurable quality degradation.\par}
120	
121	\subsection{Seed Robustness}
122	\label{sec:seed_robustness}
123	
124	Because the random seed governs both corpus sampling and generation quality (not merely CV splits), absolute AUC values are seed-dependent.
125	We re-run three configurations with seed$\,{=}\,123$ (primary: seed$\,{=}\,42$; Table~\ref{tab:seed_robustness}).
126	$\Kempirical$ is stable in 2/3 cases: Pythia-1.4B on Wikipedia yields $\Kempirical{=}1$ under both seeds (1v2 $\Delta = -0.8$\,pp), and Qwen-1.5B on C4 yields $\Kempirical{=}2$ (1v2 $\Delta = +9.0$\,pp, both seeds above $\theta$).
127	Qwen-1.5B on Wikipedia shifts from $\Kempirical{=}2$ to $\Kempirical{=}3$ under seed$\,{=}\,123$, but the 2v3 AUC ($0.6067$) is marginal: one of five folds falls below $\theta$ (fold~5 $= 0.595$), so this does not constitute strong evidence for $\Kempirical{=}3$.
128	The ${\pm}9$\,pp absolute AUC variation across seeds strengthens the methodological case for threshold-based $\Kempirical$ over raw AUC comparisons: the qualitative boundary is robust even when point estimates shift.
129	
130	\begin{table}[h]
131	\centering
132	\footnotesize
133	\caption{Seed robustness: $\Kempirical$ under two random seeds. 1v2 $\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\theta$).}
134	\label{tab:seed_robustness}
135	\resizebox{\columnwidth}{!}{%
136	\begin{tabular}{llcccc}
137	\toprule
138	\textbf{Model} & \textbf{Domain} & \multicolumn{2}{c}{$\Kempirical$} & \textbf{1v2 $\Delta$} & \textbf{Stable?} \\
139	\cmidrule(lr){3-4}
140	 & & seed=42 & seed=123 & & \\
141	\midrule
142	Pythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\,pp & \checkmark \\
143	Qwen-1.5B  & C4        & 2 & 2 & $+9.0$\,pp & \checkmark \\
144	Qwen-1.5B  & Wikipedia & 2 & 3$^\dagger$ & $+8.7$\,pp & $\times$ \\
145	\bottomrule
146	\multicolumn{6}{l}{\footnotesize $^\dagger$2v3 $\auc = 0.6067$; fold 5 $= 0.595 < \theta$. Marginal boundary.}
147	\end{tabular}}
148	\end{table}
149	
150	\subsection{Bonferroni-Corrected Confidence Intervals}
151	\label{sec:bonferroni_ci}
152	
153	To control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\alpha_{\text{corr}} = 0.05 / 10 = 0.005$to obtain 99.5\% confidence intervals ($z = 2.807$).
154	Table~\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\Kempirical$ boundary pair.
155	Seven of ten configurations retain CI lower bounds above $\theta{=}0.60$; three marginal $\Kempirical{=}2$ configurations (Pythia-1.4B, Qwen-cont, LLaMA-8B) see their lower bounds dip below $\theta$ under the stricter criterion ($0.5934$, $0.5976$, and $0.5988$, respectively).
156	These near-misses reflect narrow effect sizes ($\auc - \theta < 0.013$) rather than classification failure: all three retain point estimates above $\theta$, and Qwen-cont and LLaMA-8B retain uncorrected 95\% CI lower bounds above $\theta$ (Pythia-1.4B falls marginally below at $0.5976$).
157	
158	\begin{table}[h]
159	\centering
160	\footnotesize
161	\caption{Bonferroni-corrected 99.5\% confidence intervals for $\Kempirical$ boundary pairs across all 10 configurations. $\alpha_{\text{corr}} = 0.005$; CI computed as $\auc \pm 2.807 \times \hat{\sigma}_{\text{boot}}$. ``Pass $\theta$'': CI lower bound $> 0.60$.}
162	\label{tab:bonferroni_ci}
163	\resizebox{\columnwidth}{!}{%
164	\begin{tabular}{llcccc}
165	\toprule
166	\textbf{Configuration} & \textbf{Boundary} & $\auc$ & $\hat{\sigma}_{\text{boot}}$ & \textbf{99.5\% CI} & \textbf{Pass $\theta$} \\
167	\midrule
168	\multicolumn{6}{l}{\textit{$\Kempirical = 2$ configurations}} \\
169	Qwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\,.708]$ & \checkmark \\
170	Pythia-1.4B               & 1v2 & .6074 & .0050 & $[.593,\,.621]$ & $\times$ \\
171	Qwen-base                 & 1v2 & .6260 & .0047 & $[.613,\,.639]$ & \checkmark \\
172	Qwen-7B$^\ddagger$        & 1v2 & .6178 & .0046 & $[.605,\,.631]$ & \checkmark \\
173	LLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\,.626]$ & $\times$ \\
174	Qwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\,.625]$ & $\times$ \\
175	\midrule
176	\multicolumn{6}{l}{\textit{$\Kempirical = 1$ configurations}} \\
177	OLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\,.989]$ & \checkmark \\
178	Mistral-7B                & 0v1 & .9209 & .0010 & $[.919,\,.923]$ & \checkmark \\
179	Pythia-6.9B$^\S$          & 0v1 & .9599 & .0015$^\dagger$ & $[.956,\,.964]$ & \checkmark \\
180	Gemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\,.958]$ & \checkmark \\
181	\bottomrule
182	\multicolumn{6}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\
183	\multicolumn{6}{l}{\footnotesize $^\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\
184	\multicolumn{6}{l}{\footnotesize $^\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}
185	\end{tabular}}
186	\end{table}
187	
188	\subsection{Cross-Sample Robustness: 5K vs.\ 10K}
189	\label{sec:robustness_10k}
190	
191	The preceding analyses fix the sample pool at $N{=}5{,}000$ passages per depth.
192	To assess between-sample variability, we re-draw an independent $N{=}10{,}000$ sample from C4 using a different random seed and repeat the full OBD pipeline.
193	If $\Kempirical$ and the boundary AUC are driven by the underlying distributional shift rather than by idiosyncrasies of a particular sample, both quantities should remain stable across draws.
194	
195	Table~\ref{tab:robustness_10k} reports the results.
196	For Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9722$ vs.\ $0.9712$), and the boundary 1v2 AUC shifts from $0.6074$ to $0.6175$ ($\Delta = +0.010$).
197	This narrow shift is consistent with natural sampling variability across C4 subsets and does not alter the qualitative depth boundary.
198	The 2v3 pair remains near chance in both draws ($0.54$, $0.54$); depths $\geq 2$ are indistinguishable regardless of sample.
199	Qwen-1.5B (continuation, C4) replicates the same pattern ($\Kempirical{=}2$, 1v2 $\auc = 0.6346$).
200	LLaMA-3.1-8B (continuation, C4) is the sole $\Kempirical{=}2$ configuration where the 10K OOF AUC drops below $\theta$ ($0.5880$; pipeline AUC $= 0.6148$; Bonferroni 99.5\% CI $[0.5776, 0.5978]$); under this stricter criterion $\Kempirical{=}1$.
201	OLMo-1B (continuation, C4) is the only configuration that yields $\Kempirical{=}1$ at both 5K and 10K, with virtually identical depth profiles (0v1 $\auc = 0.9871$ vs.\ $0.9860$; 1v2 $\auc = 0.4984$ vs.\ $0.5001$); the 1v2 AUC at random level is consistent with Qwen cross-scoring, which places OLMo well below the discrimination boundary.
202	Gemma-2-2B is the sole configuration where $\Kempirical$ increases from 5K ($\Kempirical{=}1$, 1v2 $\auc = 0.5981$) to 10K ($\Kempirical{=}2$, 1v2 $\auc = 0.6099$), but the 10K boundary AUC exceeds $\theta$ by only $0.010$, placing this model at the precise $\Kempirical{=}1/2$ boundary.
203	
204	\begin{table}[h]
205	\centering
206	\footnotesize
207	\caption{Cross-sample robustness: pairwise AUC and $\Kempirical$ under 5K and 10K C4 samples drawn with different random seeds. All configurations use continuation mode. $\Kempirical$ is determined by the $\theta{=}0.60$ threshold on 1v2 AUC.}
208	\label{tab:robustness_10k}
209	\resizebox{\columnwidth}{!}{\begin{tabular}{llcccc}
210	\toprule
211	\textbf{Model} & $N$ & \textbf{AUC(0v1)} & \textbf{AUC(1v2)} & \textbf{AUC(2v3)} & $\Kempirical$ \\
212	\midrule
213	Pythia-1.4B cont & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
214	Pythia-1.4B cont & 10K & 0.9712 & 0.6175 & 0.5364 & 2 \\
215	\midrule
216	Qwen-1.5B cont  & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
217	Qwen-1.5B cont  & 10K & 0.9875 & 0.6346 & 0.5616 & 2 \\
218	\midrule
219	LLaMA-8B cont   & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
220	LLaMA-8B cont   & 10K & 0.9282 & 0.5880$^\dagger$ & 0.5247 & 1$^\dagger$ \\
221	\midrule
222	OLMo-1B cont    & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 1 \\
223	OLMo-1B cont    & 10K & 0.9871 & 0.4984 & 0.5059 & 1 \\
224	\midrule
225	Gemma-2-2B cont & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:kstar_ci_extended})} & 1 \\
226	Gemma-2-2B cont & 10K & 0.9534 & 0.6099$^\ddagger$ & 0.5409 & 2$^\ddagger$ \\
227	\bottomrule
228	\multicolumn{6}{l}{\footnotesize $^\dagger$OOF AUC (pipeline AUC $= 0.6148$); Bonferroni 99.5\% CI $[0.5776, 0.5978]$ does not pass $\theta$.} \\
229	\multicolumn{6}{l}{\footnotesize $^\ddagger$Borderline: Bonferroni 99.5\% CI $[0.600,\,0.619]$ (percentile); CI lower $0.0002$ below $\theta$. Sole config where $\Kempirical$ increases from 5K to 10K.} \\
230	\end{tabular}}
231	\end{table}
232	
233	\subsection{Bootstrap $\Kempirical$ Stability}
234	\label{sec:bootstrap_kstar}
235	
236	To assess within-sample stability, we bootstrap-resample the evaluation data (1{,}000 iterations) and recompute $\Kempirical$ for each resample across 10 configurations spanning four domains (Table~\ref{tab:bootstrap_kstar}).
237	Eight of ten configurations yield identical $\Kempirical$ in 100\% of resamples (CI width~0).
238	The two exceptions, Gemma-2-2B on C4 ($\Kempirical{=}1$ in 92.7\%, $\Kempirical{=}2$ in 7.3\%) and LLaMA-8B on Wikipedia ($\Kempirical{=}1$ in 94.3\%, $\Kempirical{=}2$ in 5.7\%), both sit at the $\Kempirical{=}1/2$ boundary with 95\% CIs of width~1, consistent with their marginal 1v2 AUC values.
239	The $\Kempirical \leq 2$ upper bound holds in all resamples across all configurations.
240	
241	Bootstrap CIs capture within-sample stability (resampling from a fixed corpus), while the 5K-vs.-10K comparison (Table~\ref{tab:robustness_10k}) captures between-sample variability (independent draws from the source distribution).
242	Together they bound $\Kempirical$ uncertainty from complementary angles: within-sample stability is high (8/10 at 100\%), and between-sample shifts are limited to boundary configurations (LLaMA-8B, Gemma-2-2B).
243	The main text's 6/10 $\Kempirical{=}2$ count (Section~\ref{sec:kstar_boundary}) is based on the standard $N{=}5{,}000$ setting; the two sample-size-sensitive configurations sit at the $\Kempirical{=}1/2$ boundary in both analyses, and the universal $\Kempirical \leq 2$ bound is unaffected.
244	
245	\begin{table}[h]
246	\centering
247	\footnotesize
248	\caption{Bootstrap $\Kempirical$ stability (1{,}000 resamples). Each row reports the fraction of resamples yielding each $\Kempirical$ value and the resulting 95\% CI. Eight of ten configurations are perfectly stable; two boundary cases show mild variability (CI width~1).}
249	\label{tab:bootstrap_kstar}
250	\resizebox{\columnwidth}{!}{%
251	\begin{tabular}{llccccl}
252	\toprule
253	\textbf{Config} & \textbf{Domain} & $\Kempirical$ & $\Kempirical{=}1$ & $\Kempirical{=}2$ & $\Kempirical{=}3$ & \textbf{95\% CI} \\
254	\midrule
255	Qwen-1.5B   & C4    & 2 & 0\%    & 100\%  & 0\%   & $[2,\,2]$ \\
256	OLMo-1B     & C4    & 1 & 100\%  & 0\%    & 0\%   & $[1,\,1]$ \\
257	Pythia-1.4B  & C4    & 2 & 0\%    & 100\%  & 0\%   & $[2,\,2]$ \\
258	LLaMA-8B    & C4    & 2 & 0.1\%  & 99.9\% & 0\%   & $[2,\,2]$ \\
259	Gemma-2B    & C4    & 1 & 92.7\% & 7.3\%  & 0\%   & $[1,\,2]$ \\
260	LLaMA-8B    & Wiki  & 1 & 94.3\% & 5.7\%  & 0\%   & $[1,\,2]$ \\
261	Mistral-7B   & Wiki  & 1 & 100\%  & 0\%    & 0\%   & $[1,\,1]$ \\
262	LLaMA-8B    & arXiv & 3 & 0\%    & 0\%    & 100\% & $[3,\,3]$ \\
263	OLMo-1B     & arXiv & 1 & 100\%  & 0\%    & 0\%   & $[1,\,1]$ \\
264	Qwen-1.5B   & Code  & 2 & 0\%    & 100\%  & 0\%   & $[2,\,2]$ \\
265	\bottomrule
266	\end{tabular}}
267	\end{table}
268	
269	\subsection{Computational Cost}
270	\label{sec:computation_cost}
271	
272	Per-document inference (Qwen2.5-1.5B scorer, RTX PRO 6000, $N{=}1{,}000$, no batching): scorer log-prob $20.6 \pm 1.9$\,ms, feature extraction $23.4 \pm 6.1$\,ms, LightGBM $0.74 \pm 0.10$\,ms; total $44.7 \pm 7.7$\,ms/doc (${\sim}$22 docs/sec).
273	
274	\subsection{DeBERTa Upper-Bound Comparison}
275	\label{sec:deberta_upperbound}
276	
277	DeBERTa-v3-base fine-tuned on raw text serves as an upper-bound probe (Table~\ref{tab:deberta_vs_obd}).
278	It matches OBD on C4 and Code ($\Kempirical{=}2$) but extends $\Kempirical$ to~4 on arXiv (3v4 $\auc = 0.624$, CI $[0.613, 0.635]$), quantifying the cost of generator-agnostic features at one depth level on structured text.
279	
280	\begin{table}[H]
281	\centering
282	\caption{$\Kempirical$ comparison: OBD (15D) vs.\ DeBERTa-v3-base (Qwen2.5-1.5B base, continuation mode; $\theta{=}0.60$).}
283	\label{tab:deberta_vs_obd}
284	\footnotesize
285	\resizebox{\columnwidth}{!}{%
286	\begin{tabular}{lcccc}
287	\toprule
288	& \multicolumn{2}{c}{\textbf{OBD (15D)}} & \multicolumn{2}{c}{\textbf{DeBERTa}} \\
289	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
290	\textbf{Domain} & $\Kempirical$ & boundary $\auc$ & $\Kempirical$ & boundary $\auc$ \\
291	\midrule
292	C4      & 2 & 0.626~(1v2) & 2 & 0.705~(1v2) \\
293	arXiv   & 3 & 0.643~(2v3) & 4 & 0.624~(3v4) \\
294	Code    & 2 & 0.738~(1v2) & 2 & 0.808~(1v2) \\
295	\bottomrule
296	\end{tabular}}
297	\end{table}
298	
299	\subsection{Cross-Scale Generalization: Gemma-2-27B}
300	\label{sec:gemma27b_transfer}
301	\label{sec:gemma27b_filtering}
302	
303	We extend the transfer matrix (Section~\ref{sec:transfer}) to Gemma-2-27B (C4 continuation, Qwen-1.5B scorer).
304	Table~\ref{tab:gemma27b_transfer} shows 27B$\to$small transfer retains $>$100\% (the 27B model's subtler signal generalizes upward), while small$\to$27B retains only 76.5\%.
305	
306	\begin{table}[H]
307	\centering
308	\small
309	\caption{Cross-scale transfer retention (\%) between Gemma-2-27B and 1B--8B models.}
310	\label{tab:gemma27b_transfer}
311	\resizebox{\columnwidth}{!}{%
312	\begin{tabular}{lcccccc}
313	\toprule
314	\textbf{Train $\backslash$ Test} & \textbf{Gemma-27B} & \textbf{LLaMA-8B} & \textbf{Qwen-1.5B} & \textbf{Pythia-1.4B} & \textbf{OLMo-1B} & \textbf{Avg} \\
315	\midrule
316	Gemma-27B   & --- & 103.6\% & 107.2\% & 103.5\% & 93.1\% & 101.3\% \\
317	LLaMA-8B    & 92.1\% & --- & & & & \\
318	Qwen-1.5B   & 71.3\% & & --- & & & \\
319	Pythia-1.4B  & 80.9\% & & & --- & & \\
320	OLMo-1B     & 77.3\% & & & & --- & \\
321	\midrule
322	\multicolumn{2}{l}{Small$\to$27B avg} & \multicolumn{5}{r}{76.5\%} \\
323	\bottomrule
324	\end{tabular}}
325	\end{table}
326	
327	We also apply the Qwen-1.5B-trained binary classifier to Gemma-2-27B-generated text and fine-tune on the filtered corpus (9 runs, 3 strategies $\times$ 3 seeds; Table~\ref{tab:gemma27b_filtering}).
328	Binary filtering retains or improves both metrics ($+$0.02\,pp MMLU, $+$0.41\,pp HellaSwag); cross-scale robustness holds without retraining.
329	
330	\begin{table}[H]
331	\centering
332	\footnotesize
333	\caption{Filtering Gemma-2-27B text with a Qwen-1.5B-trained OBD classifier.}
334	\label{tab:gemma27b_filtering}
335	\begin{tabular}{lcc}
336	\toprule
337	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
338	\midrule
339	No filter          & 0.5956 & 0.6633 \\
340	Binary-ours        & 0.5958 ($+$0.02\,pp) & 0.6674 ($+$0.41\,pp) \\
341	Graduated          & 0.5953 ($-$0.03\,pp) & 0.6629 ($-$0.04\,pp) \\
342	\bottomrule
343	\end{tabular}
344	\end{table}
345	
346	\subsection{Multi-Source arXiv Validation}
347	\label{sec:arxiv_multi_source}
348	
349	Training a single OBD classifier on arXiv text pooled from three generators (Pythia-1.4B, OLMo-1B, Qwen-1.5B; Qwen cross-scored) yields $\Kempirical{=}3$ (2v3 $\auc = 0.657\;[0.647,\,0.667]$, 1v2 $= 0.858$; Bonferroni $p < 0.005$), matching single-generator results and confirming that the domain ceiling is text-intrinsic.
350	
351	\enlargethispage{2\baselineskip}
352	\section{Use of AI Assistants}
353	\label{app:ai-assistants}
354	
355	The authors used AI-based assistants, including Claude, for coding support, writing assistance (grammar polishing, wording suggestions, LaTeX editing), and literature review during this work.
356	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f936636-2d38-4900-88b4-0babd9e18b60",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "05b24183-7267-4414-86a4-f34c98d284c7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\section{Extended Discussion}\n\\label{sec:extended_discussion}\n\n\\subsection{Theoretical Implications of $\\Kempirical = 2$}\n\nThe DPI guarantees a finite $\\Ktheory$; for general web text, $\\Kempirical \\leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\\Kempirical{=}3$, aligning with model collapse convergence~\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\nDecoding strategy modestly affects signal strength (1v2 $\\auc \\in [0.6862, 0.7037]$) but does not shift the boundary.\n\n\\subsection{Cross-Model Transfer Implications}\n\nCross-model classification retains 80--92\\% accuracy with scorer-invariant feature rankings ($\\rho > 0.90$), which enables single-classifier deployment across generators.\nAbsolute discriminability at the $\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\Kempirical$ from 2 to 1, while rewrite-mode $\\Kempirical = 2$ is preserved.\nModel family similarity modulates transfer (Pythia$\\leftrightarrow$OLMo: 89--92\\% vs.\\ Qwen-cont$\\leftrightarrow$OLMo: 80--85\\%).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scorer validation. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1. OLMo arXiv cross-scorer confirms $\\Kempirical{=}1$ ($p{=}0.510$, n.s.).}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs). Scorer is statistically significant but explains modest variance ($\\eta^2_p{=}.192$) relative to Depth-Pair ($\\eta^2_p{=}.998$), which supports near-scorer-independence of depth discrimination.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.78  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736.10  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.69 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & $.005$ & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Importance Across Decoding Strategies}\n\nFeature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\\rho = 0.914$), while greedy vs.\\ $T{=}1.2$ yields lower correlation ($\\rho = 0.53$, nonsignificant after Bonferroni).\nThe depth boundary is robust but the optimal feature subset is strategy-dependent.\n\n\\subsection{Scale and Neural Probe}\n\\label{sec:extended_neural_probe}\n\nCross-scale validation confirms $\\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6178$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9224$) both exceed $\\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text.\nGemma-2-27B (C4 continuation, Qwen cross-scored) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.5894$), consistent with Gemma-2-2B at 5K ($\\Kempirical{=}1$, 1v2 $\\auc = 0.5981$). The Gemma family produces $\\Kempirical{=}1$ at both 2B and 27B; $\\Kempirical$ is model-family-dependent rather than scale-dependent.\n\nThe neural probe yields model-dependent $\\Kempirical^{\\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia; OLMo yields $\\Kempirical^{\\text{neural}} = 1$ (1v2 $\\auc = 0.5054$), consistent with the 15D LightGBM boundary.\nThe 15D generator-agnostic features yield $\\Kempirical = 2$ for Pythia and Qwen, while OLMo yields $\\Kempirical = 1$ under the standardized pipeline.\n\n\\subsection{LLM Zero-Shot Baseline}\n\\label{sec:extended_llm}\n\nGPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10; $N{=}500$) and Claude Opus~4.6 33.1\\% (MAE = 1.15; $N{=}499$ after one invalid response) on a balanced test set, comparable to OBD-LightGBM's 38.6\\% (95\\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\\ref{tab:s3_llm_zeroshot}).\nPer-depth recall confirms convergent failure at depths $\\geq 2$ (Section~\\ref{sec:why_kstar}).\nThe LLM baseline evaluates depths 0--4 (5-class; Table~\\ref{tab:s3_llm_zeroshot}). When probabilities are marginalized to 4 classes ($P(d{\\geq}3)$), accuracy rises to 44.4\\% but concentrates in the merged class while depths 2--3 collapse to 2--8\\%.\n\n\\subsection{Practical Considerations}\n\nAll filtering strategies degrade general capabilities (MMLU: 0.6018 $\\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\\to$ 0.6631--0.6701); our depth-chain setting (${\\sim}$83\\% synthetic) is an upper bound; in mixed corpora, degradation scales with contamination fraction~\\cite{shumailov2024collapse, dohmatob2024model}.\n$\\Kstar$-aware binary filtering reduces MMLU degradation by ${\\sim}$50\\% ($-$1.53\\,pp $\\to$ $-$0.77\\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).\n\n\\subsection{Additional Scope Analysis}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nRetrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\\Kempirical{\\geq}4$ (1v2 $\\auc = 0.9484$, 2v3 $= 0.8888$, 3v4 $= 0.7982$), far exceeding prompt-chain $\\Kempirical{=}2$.\nThe elevated signal arises from cumulative model-adaptation artifacts rather than text-intrinsic degradation; prompt-chain $\\Kempirical$ is the operationally relevant boundary for data curation.\n\n\\emph{Threshold sensitivity.}\nAt $\\theta = 0.55$, $\\Kempirical = 3$ for Qwen-rewrite/continuation; at $\\theta = 0.70$, $\\Kempirical = 1$ across all configurations (Figure~\\ref{fig:kstar_theta}).\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\emph{Structural confound: token length.}\nIn continuation mode the generation prompt is discarded, so all depths $\\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\\ machine-generated prompt), not structural composition.\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}); EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n\n\\subsection{Dose-Response: Contamination Ratio Effect}\n\\label{sec:dose_response}\n\nThe main filtering experiments (Section~\\ref{sec:filtering}) use the full depth chain (depths 0--5, ${\\sim}$83\\% synthetic) to maximize effect size.\nTo characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\\%, 30\\%, and 50\\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\\ref{tab:dose_response}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMLU accuracy by contamination ratio (fraction of synthetic data in training set) and filtering strategy. Base model (no fine-tuning): 0.6018. Mean $\\pm$ std over 5 seeds.}\n\\label{tab:dose_response}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{10\\%} & \\textbf{30\\%} & \\textbf{50\\%} \\\\\n\\midrule\nNo-filter   & $0.6058 \\pm .0002$ & $0.6069 \\pm .0007$ & $0.6063 \\pm .0013$ \\\\\nBinary-ours & $0.6079 \\pm .0005$ & $0.6082 \\pm .0012$ & $0.6088 \\pm .0011$ \\\\\nGraduated   & $0.6066 \\pm .0011$ & $0.6072 \\pm .0008$ & $0.6062 \\pm .0009$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n{\\sloppy At all three contamination ratios, fine-tuning on the mixed corpus yields MMLU above the base model ($0.6018$); the clean-data majority dominates the training signal.\nStrategy differences are small: binary-ours exceeds no-filter by $0.21$\\,pp at 10\\% ($p = 0.001$), $0.13$\\,pp at 30\\% ($p = 0.074$), and $0.25$\\,pp at 50\\% ($p = 0.038$).\nWhile binary reaches statistical significance at 10\\% and 50\\% due to high power (5 seeds, low variance), the maximum strategy spread remains below 0.3\\,pp across all ratios.\nThe strategy ordering (binary $>$ graduated $>$ no-filter) is consistent with the depth-chain setting, but effect sizes are negligible compared to that setting ($-$1.53\\,pp no-filter degradation).\nThis demonstrates that $\\Kstar$-aware curation provides practical benefit primarily when contamination is severe enough to cause measurable quality degradation.\\par}\n\n\\subsection{Seed Robustness}\n\\label{sec:seed_robustness}\n\nBecause the random seed governs both corpus sampling and generation quality (not merely CV splits), absolute AUC values are seed-dependent.\nWe re-run three configurations with seed$\\,{=}\\,123$ (primary: seed$\\,{=}\\,42$; Table~\\ref{tab:seed_robustness}).\n$\\Kempirical$ is stable in 2/3 cases: Pythia-1.4B on Wikipedia yields $\\Kempirical{=}1$ under both seeds (1v2 $\\Delta = -0.8$\\,pp), and Qwen-1.5B on C4 yields $\\Kempirical{=}2$ (1v2 $\\Delta = +9.0$\\,pp, both seeds above $\\theta$).\nQwen-1.5B on Wikipedia shifts from $\\Kempirical{=}2$ to $\\Kempirical{=}3$ under seed$\\,{=}\\,123$, but the 2v3 AUC ($0.6067$) is marginal: one of five folds falls below $\\theta$ (fold~5 $= 0.595$), so this does not constitute strong evidence for $\\Kempirical{=}3$.\nThe ${\\pm}9$\\,pp absolute AUC variation across seeds strengthens the methodological case for threshold-based $\\Kempirical$ over raw AUC comparisons: the qualitative boundary is robust even when point estimates shift.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Seed robustness: $\\Kempirical$ under two random seeds. 1v2 $\\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\\theta$).}\n\\label{tab:seed_robustness}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\multicolumn{2}{c}{$\\Kempirical$} & \\textbf{1v2 $\\Delta$} & \\textbf{Stable?} \\\\\n\\cmidrule(lr){3-4}\n & & seed=42 & seed=123 & & \\\\\n\\midrule\nPythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\\,pp & \\checkmark \\\\\nQwen-1.5B  & C4        & 2 & 2 & $+9.0$\\,pp & \\checkmark \\\\\nQwen-1.5B  & Wikipedia & 2 & 3$^\\dagger$ & $+8.7$\\,pp & $\\times$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$2v3 $\\auc = 0.6067$; fold 5 $= 0.595 < \\theta$. Marginal boundary.}\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Bonferroni-Corrected Confidence Intervals}\n\\label{sec:bonferroni_ci}\n\nTo control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\\alpha_{\\text{corr}} = 0.05 / 10 = 0.005$to obtain 99.5\\% confidence intervals ($z = 2.807$).\nTable~\\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\\Kempirical$ boundary pair.\nSeven of ten configurations retain CI lower bounds above $\\theta{=}0.60$; three marginal $\\Kempirical{=}2$ configurations (Pythia-1.4B, Qwen-cont, LLaMA-8B) see their lower bounds dip below $\\theta$ under the stricter criterion ($0.5934$, $0.5976$, and $0.5988$, respectively).\nThese near-misses reflect narrow effect sizes ($\\auc - \\theta < 0.013$) rather than classification failure: all three retain point estimates above $\\theta$, and Qwen-cont and LLaMA-8B retain uncorrected 95\\% CI lower bounds above $\\theta$ (Pythia-1.4B falls marginally below at $0.5976$).\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Bonferroni-corrected 99.5\\% confidence intervals for $\\Kempirical$ boundary pairs across all 10 configurations. $\\alpha_{\\text{corr}} = 0.005$; CI computed as $\\auc \\pm 2.807 \\times \\hat{\\sigma}_{\\text{boot}}$. ``Pass $\\theta$'': CI lower bound $> 0.60$.}\n\\label{tab:bonferroni_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Boundary} & $\\auc$ & $\\hat{\\sigma}_{\\text{boot}}$ & \\textbf{99.5\\% CI} & \\textbf{Pass $\\theta$} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 2$ configurations}} \\\\\nQwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\\,.708]$ & \\checkmark \\\\\nPythia-1.4B               & 1v2 & .6074 & .0050 & $[.593,\\,.621]$ & $\\times$ \\\\\nQwen-base                 & 1v2 & .6260 & .0047 & $[.613,\\,.639]$ & \\checkmark \\\\\nQwen-7B$^\\ddagger$        & 1v2 & .6178 & .0046 & $[.605,\\,.631]$ & \\checkmark \\\\\nLLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\\,.626]$ & $\\times$ \\\\\nQwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\\,.625]$ & $\\times$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 1$ configurations}} \\\\\nOLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\\,.989]$ & \\checkmark \\\\\nMistral-7B                & 0v1 & .9209 & .0010 & $[.919,\\,.923]$ & \\checkmark \\\\\nPythia-6.9B$^\\S$          & 0v1 & .9599 & .0015$^\\dagger$ & $[.956,\\,.964]$ & \\checkmark \\\\\nGemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\\,.958]$ & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Cross-Sample Robustness: 5K vs.\\ 10K}\n\\label{sec:robustness_10k}\n\nThe preceding analyses fix the sample pool at $N{=}5{,}000$ passages per depth.\nTo assess between-sample variability, we re-draw an independent $N{=}10{,}000$ sample from C4 using a different random seed and repeat the full OBD pipeline.\nIf $\\Kempirical$ and the boundary AUC are driven by the underlying distributional shift rather than by idiosyncrasies of a particular sample, both quantities should remain stable across draws.\n\nTable~\\ref{tab:robustness_10k} reports the results.\nFor Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9722$ vs.\\ $0.9712$), and the boundary 1v2 AUC shifts from $0.6074$ to $0.6175$ ($\\Delta = +0.010$).\nThis narrow shift is consistent with natural sampling variability across C4 subsets and does not alter the qualitative depth boundary.\nThe 2v3 pair remains near chance in both draws ($0.54$, $0.54$); depths $\\geq 2$ are indistinguishable regardless of sample.\nQwen-1.5B (continuation, C4) replicates the same pattern ($\\Kempirical{=}2$, 1v2 $\\auc = 0.6346$).\nLLaMA-3.1-8B (continuation, C4) is the sole $\\Kempirical{=}2$ configuration where the 10K OOF AUC drops below $\\theta$ ($0.5880$; pipeline AUC $= 0.6148$; Bonferroni 99.5\\% CI $[0.5776, 0.5978]$); under this stricter criterion $\\Kempirical{=}1$.\nOLMo-1B (continuation, C4) is the only configuration that yields $\\Kempirical{=}1$ at both 5K and 10K, with virtually identical depth profiles (0v1 $\\auc = 0.9871$ vs.\\ $0.9860$; 1v2 $\\auc = 0.4984$ vs.\\ $0.5001$); the 1v2 AUC at random level is consistent with Qwen cross-scoring, which places OLMo well below the discrimination boundary.\nGemma-2-2B is the sole configuration where $\\Kempirical$ increases from 5K ($\\Kempirical{=}1$, 1v2 $\\auc = 0.5981$) to 10K ($\\Kempirical{=}2$, 1v2 $\\auc = 0.6099$), but the 10K boundary AUC exceeds $\\theta$ by only $0.010$, placing this model at the precise $\\Kempirical{=}1/2$ boundary.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Cross-sample robustness: pairwise AUC and $\\Kempirical$ under 5K and 10K C4 samples drawn with different random seeds. All configurations use continuation mode. $\\Kempirical$ is determined by the $\\theta{=}0.60$ threshold on 1v2 AUC.}\n\\label{tab:robustness_10k}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & $N$ & \\textbf{AUC(0v1)} & \\textbf{AUC(1v2)} & \\textbf{AUC(2v3)} & $\\Kempirical$ \\\\\n\\midrule\nPythia-1.4B cont & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nPythia-1.4B cont & 10K & 0.9712 & 0.6175 & 0.5364 & 2 \\\\\n\\midrule\nQwen-1.5B cont  & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nQwen-1.5B cont  & 10K & 0.9875 & 0.6346 & 0.5616 & 2 \\\\\n\\midrule\nLLaMA-8B cont   & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nLLaMA-8B cont   & 10K & 0.9282 & 0.5880$^\\dagger$ & 0.5247 & 1$^\\dagger$ \\\\\n\\midrule\nOLMo-1B cont    & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 1 \\\\\nOLMo-1B cont    & 10K & 0.9871 & 0.4984 & 0.5059 & 1 \\\\\n\\midrule\nGemma-2-2B cont & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:kstar_ci_extended})} & 1 \\\\\nGemma-2-2B cont & 10K & 0.9534 & 0.6099$^\\ddagger$ & 0.5409 & 2$^\\ddagger$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$OOF AUC (pipeline AUC $= 0.6148$); Bonferroni 99.5\\% CI $[0.5776, 0.5978]$ does not pass $\\theta$.} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Borderline: Bonferroni 99.5\\% CI $[0.600,\\,0.619]$ (percentile); CI lower $0.0002$ below $\\theta$. Sole config where $\\Kempirical$ increases from 5K to 10K.} \\\\\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Bootstrap $\\Kempirical$ Stability}\n\\label{sec:bootstrap_kstar}\n\nTo assess within-sample stability, we bootstrap-resample the evaluation data (1{,}000 iterations) and recompute $\\Kempirical$ for each resample across 10 configurations spanning four domains (Table~\\ref{tab:bootstrap_kstar}).\nEight of ten configurations yield identical $\\Kempirical$ in 100\\% of resamples (CI width~0).\nThe two exceptions, Gemma-2-2B on C4 ($\\Kempirical{=}1$ in 92.7\\%, $\\Kempirical{=}2$ in 7.3\\%) and LLaMA-8B on Wikipedia ($\\Kempirical{=}1$ in 94.3\\%, $\\Kempirical{=}2$ in 5.7\\%), both sit at the $\\Kempirical{=}1/2$ boundary with 95\\% CIs of width~1, consistent with their marginal 1v2 AUC values.\nThe $\\Kempirical \\leq 2$ upper bound holds in all resamples across all configurations.\n\nBootstrap CIs capture within-sample stability (resampling from a fixed corpus), while the 5K-vs.-10K comparison (Table~\\ref{tab:robustness_10k}) captures between-sample variability (independent draws from the source distribution).\nTogether they bound $\\Kempirical$ uncertainty from complementary angles: within-sample stability is high (8/10 at 100\\%), and between-sample shifts are limited to boundary configurations (LLaMA-8B, Gemma-2-2B).\nThe main text's 6/10 $\\Kempirical{=}2$ count (Section~\\ref{sec:kstar_boundary}) is based on the standard $N{=}5{,}000$ setting; the two sample-size-sensitive configurations sit at the $\\Kempirical{=}1/2$ boundary in both analyses, and the universal $\\Kempirical \\leq 2$ bound is unaffected.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Bootstrap $\\Kempirical$ stability (1{,}000 resamples). Each row reports the fraction of resamples yielding each $\\Kempirical$ value and the resulting 95\\% CI. Eight of ten configurations are perfectly stable; two boundary cases show mild variability (CI width~1).}\n\\label{tab:bootstrap_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccl}\n\\toprule\n\\textbf{Config} & \\textbf{Domain} & $\\Kempirical$ & $\\Kempirical{=}1$ & $\\Kempirical{=}2$ & $\\Kempirical{=}3$ & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen-1.5B   & C4    & 2 & 0\\%    & 100\\%  & 0\\%   & $[2,\\,2]$ \\\\\nOLMo-1B     & C4    & 1 & 100\\%  & 0\\%    & 0\\%   & $[1,\\,1]$ \\\\\nPythia-1.4B  & C4    & 2 & 0\\%    & 100\\%  & 0\\%   & $[2,\\,2]$ \\\\\nLLaMA-8B    & C4    & 2 & 0.1\\%  & 99.9\\% & 0\\%   & $[2,\\,2]$ \\\\\nGemma-2B    & C4    & 1 & 92.7\\% & 7.3\\%  & 0\\%   & $[1,\\,2]$ \\\\\nLLaMA-8B    & Wiki  & 1 & 94.3\\% & 5.7\\%  & 0\\%   & $[1,\\,2]$ \\\\\nMistral-7B   & Wiki  & 1 & 100\\%  & 0\\%    & 0\\%   & $[1,\\,1]$ \\\\\nLLaMA-8B    & arXiv & 3 & 0\\%    & 0\\%    & 100\\% & $[3,\\,3]$ \\\\\nOLMo-1B     & arXiv & 1 & 100\\%  & 0\\%    & 0\\%   & $[1,\\,1]$ \\\\\nQwen-1.5B   & Code  & 2 & 0\\%    & 100\\%  & 0\\%   & $[2,\\,2]$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Computational Cost}\n\\label{sec:computation_cost}\n\nPer-document inference (Qwen2.5-1.5B scorer, RTX PRO 6000, $N{=}1{,}000$, no batching): scorer log-prob $20.6 \\pm 1.9$\\,ms, feature extraction $23.4 \\pm 6.1$\\,ms, LightGBM $0.74 \\pm 0.10$\\,ms; total $44.7 \\pm 7.7$\\,ms/doc (${\\sim}$22 docs/sec).\n\n\\subsection{DeBERTa Upper-Bound Comparison}\n\\label{sec:deberta_upperbound}\n\nDeBERTa-v3-base fine-tuned on raw text serves as an upper-bound probe (Table~\\ref{tab:deberta_vs_obd}).\nIt matches OBD on C4 and Code ($\\Kempirical{=}2$) but extends $\\Kempirical$ to~4 on arXiv (3v4 $\\auc = 0.624$, CI $[0.613, 0.635]$), quantifying the cost of generator-agnostic features at one depth level on structured text.\n\n\\begin{table}[H]\n\\centering\n\\caption{$\\Kempirical$ comparison: OBD (15D) vs.\\ DeBERTa-v3-base (Qwen2.5-1.5B base, continuation mode; $\\theta{=}0.60$).}\n\\label{tab:deberta_vs_obd}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{OBD (15D)}} & \\multicolumn{2}{c}{\\textbf{DeBERTa}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Domain} & $\\Kempirical$ & boundary $\\auc$ & $\\Kempirical$ & boundary $\\auc$ \\\\\n\\midrule\nC4      & 2 & 0.626~(1v2) & 2 & 0.705~(1v2) \\\\\narXiv   & 3 & 0.643~(2v3) & 4 & 0.624~(3v4) \\\\\nCode    & 2 & 0.738~(1v2) & 2 & 0.808~(1v2) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Cross-Scale Generalization: Gemma-2-27B}\n\\label{sec:gemma27b_transfer}\n\\label{sec:gemma27b_filtering}\n\nWe extend the transfer matrix (Section~\\ref{sec:transfer}) to Gemma-2-27B (C4 continuation, Qwen-1.5B scorer).\nTable~\\ref{tab:gemma27b_transfer} shows 27B$\\to$small transfer retains $>$100\\% (the 27B model's subtler signal generalizes upward), while small$\\to$27B retains only 76.5\\%.\n\n\\begin{table}[H]\n\\centering\n\\small\n\\caption{Cross-scale transfer retention (\\%) between Gemma-2-27B and 1B--8B models.}\n\\label{tab:gemma27b_transfer}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Train $\\backslash$ Test} & \\textbf{Gemma-27B} & \\textbf{LLaMA-8B} & \\textbf{Qwen-1.5B} & \\textbf{Pythia-1.4B} & \\textbf{OLMo-1B} & \\textbf{Avg} \\\\\n\\midrule\nGemma-27B   & --- & 103.6\\% & 107.2\\% & 103.5\\% & 93.1\\% & 101.3\\% \\\\\nLLaMA-8B    & 92.1\\% & --- & & & & \\\\\nQwen-1.5B   & 71.3\\% & & --- & & & \\\\\nPythia-1.4B  & 80.9\\% & & & --- & & \\\\\nOLMo-1B     & 77.3\\% & & & & --- & \\\\\n\\midrule\n\\multicolumn{2}{l}{Small$\\to$27B avg} & \\multicolumn{5}{r}{76.5\\%} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nWe also apply the Qwen-1.5B-trained binary classifier to Gemma-2-27B-generated text and fine-tune on the filtered corpus (9 runs, 3 strategies $\\times$ 3 seeds; Table~\\ref{tab:gemma27b_filtering}).\nBinary filtering retains or improves both metrics ($+$0.02\\,pp MMLU, $+$0.41\\,pp HellaSwag); cross-scale robustness holds without retraining.\n\n\\begin{table}[H]\n\\centering\n\\footnotesize\n\\caption{Filtering Gemma-2-27B text with a Qwen-1.5B-trained OBD classifier.}\n\\label{tab:gemma27b_filtering}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nNo filter          & 0.5956 & 0.6633 \\\\\nBinary-ours        & 0.5958 ($+$0.02\\,pp) & 0.6674 ($+$0.41\\,pp) \\\\\nGraduated          & 0.5953 ($-$0.03\\,pp) & 0.6629 ($-$0.04\\,pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Source arXiv Validation}\n\\label{sec:arxiv_multi_source}\n\nTraining a single OBD classifier on arXiv text pooled from three generators (Pythia-1.4B, OLMo-1B, Qwen-1.5B; Qwen cross-scored) yields $\\Kempirical{=}3$ (2v3 $\\auc = 0.657\\;[0.647,\\,0.667]$, 1v2 $= 0.858$; Bonferroni $p < 0.005$), matching single-generator results and confirming that the domain ceiling is text-intrinsic.\n\n\\enlargethispage{2\\baselineskip}\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nThe authors used AI-based assistants, including Claude, for coding support, writing assistance (grammar polishing, wording suggestions, LaTeX editing), and literature review during this work.\n",
      "numLines": 356,
      "startLine": 1,
      "totalLines": 356
    }
  },
  "sourceToolAssistantUUID": "6f936636-2d38-4900-88b4-0babd9e18b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-25T19:44:25.127Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017kP3G9BKH87xpQaKvQ12VM`</summary>

```json
{
  "pattern": "includegraphics|\\\\input.*fig",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05b24183-7267-4414-86a4-f34c98d284c7",
  "isSidechain": false,
  "requestId": "req_011CbPrquvoRd9jWkupkach7",
  "type": "assistant",
  "uuid": "422c8423-9b79-4dfc-a4e5-0bb44b15c06e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnVmpH5XCTuWNQNL1PpFEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 604,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13219
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

_source line 16 · 2026-05-25T19:44:25.145Z_

<details><summary>↩ Tool result · `toolu_017kP3G9BKH87xpQaKvQ12VM`</summary>

```text
docs/paper/experiments_c1.tex:13:\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
docs/paper/experiments_c1.tex:61:\includegraphics[width=0.75\textwidth]{figures/fig_kstar_theta.pdf}
docs/paper/experiments_c1.tex:75:\includegraphics[width=\columnwidth]{figures/fig3_transfer_heatmap.pdf}
docs/paper/experiments_c1.tex:139:\includegraphics[width=\columnwidth]{figures/fig_jsd_decay.pdf}
docs/paper/discussion.tex:17:\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
docs/paper/method.tex:6:\includegraphics[width=\textwidth]{figures/pipeline.pdf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "422c8423-9b79-4dfc-a4e5-0bb44b15c06e",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "9e5a50e5-7f51-4afd-a564-e98a064a306b",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments_c1.tex:13:\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\ndocs/paper/experiments_c1.tex:61:\\includegraphics[width=0.75\\textwidth]{figures/fig_kstar_theta.pdf}\ndocs/paper/experiments_c1.tex:75:\\includegraphics[width=\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\ndocs/paper/experiments_c1.tex:139:\\includegraphics[width=\\columnwidth]{figures/fig_jsd_decay.pdf}\ndocs/paper/discussion.tex:17:\\includegraphics[width=\\columnwidth]{figures/fig_filtering_strategies.pdf}\ndocs/paper/method.tex:6:\\includegraphics[width=\\textwidth]{figures/pipeline.pdf}",
    "numLines": 6
  },
  "sourceToolAssistantUUID": "422c8423-9b79-4dfc-a4e5-0bb44b15c06e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-25T19:44:26.089Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0177fJUeeRFdTr28PeDe163x`</summary>

```json
{
  "pattern": "**/*.{pdf,png,jpg,eps}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e5a50e5-7f51-4afd-a564-e98a064a306b",
  "isSidechain": false,
  "requestId": "req_011CbPrquvoRd9jWkupkach7",
  "type": "assistant",
  "uuid": "ca411a07-af58-48aa-943c-26aef8b04be9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnVmpH5XCTuWNQNL1PpFEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 604,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13219
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

_source line 18 · 2026-05-25T19:44:26.103Z_

<details><summary>↩ Tool result · `toolu_0177fJUeeRFdTr28PeDe163x`</summary>

```text
docs/paper/figures/fig_theta_sensitivity.pdf
docs/paper/figures/fig_feature_ablation.pdf
docs/paper/figures/fig_power_curve.png
docs/paper/figures/fig_retrain_decay.png
docs/paper/figures/_pdf_images/feature_importance_p1.png
docs/paper/figures/feature_importance.pdf
docs/paper/figures/feature_importance.png
docs/paper/figures/olmo_rerun_feature_importance.pdf
docs/paper/figures/cross_model_feature_comparison.pdf
docs/paper/figures/_pdf_images/fig_s1_auc_decay_ci_p1.png
docs/paper/figures/fig_s1_auc_decay_ci.pdf
docs/paper/figures/fig_s1_auc_decay_ci.png
docs/paper/figures/run_20260521_173830_0ae4e3/final_output.png
docs/paper/figures/run_20260521_173830_0ae4e3/diagram_iter_1.png
docs/paper/figures/run_20260521_174045_30d737/final_output.png
docs/paper/figures/run_20260521_174045_30d737/diagram_iter_1.png
docs/paper/_figure_backups/20260524_115454/pipeline.pdf
docs/paper/_figure_backups/20260524_052908/pipeline.pdf
docs/paper/_figure_backups/20260524_052908/fig_kstar_theta.pdf
docs/paper/_figure_backups/20260524_052908/fig_filtering_strategies.pdf
docs/paper/_figure_backups/20260524_052908/fig2_auc_decay.pdf
docs/paper/_figure_backups/20260524_052908/fig3_transfer_heatmap.pdf
docs/paper/_figure_backups/20260524_115454/fig2_auc_decay.pdf
docs/paper/_figure_backups/20260524_115454/fig_filtering_strategies.pdf
docs/paper/_figure_backups/20260524_115454/fig_kstar_theta.pdf
docs/paper/_figure_backups/20260524_115454/fig3_transfer_heatmap.pdf
docs/paper/figures/run_20260524_120320_d63c6f/final_output.png
docs/paper/figures/run_20260524_120320_d63c6f/diagram_iter_1.png
docs/paper/figures/fig_kstar_theta.pdf
docs/paper/figures/fig_kstar_theta.png
docs/paper/figures/run_20260524_120758_24be21/final_output.png
docs/paper/figures/run_20260524_120758_24be21/diagram_iter_1.png
docs/paper/figures/fig2_auc_decay.pdf
docs/paper/figures/fig2_auc_decay.png
docs/paper/figures/fig3_transfer_heatmap.pdf
docs/paper/figures/fig3_transfer_heatmap.png
docs/paper/figures/run_20260524_121205_1ebeee/final_output.png
docs/paper/figures/run_20260524_121205_1ebeee/diagram_iter_1.png
docs/paper/figures/_figure_backups/pipeline_theta055.png
docs/paper/figures/_figure_backups/pipeline_theta055.pdf
docs/paper/figures/pipeline.png
docs/paper/figures/pipeline.pdf
docs/paper/figures/fig_filtering_strategies.pdf
docs/paper/figures/fig_filtering_strategies.png
docs/paper/figures/fig_jsd_decay.pdf
docs/paper/figures/fig_jsd_decay.png
docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca411a07-af58-48aa-943c-26aef8b04be9",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "0ddb0e44-c6e6-4c92-a4b5-e30197b564c8",
  "toolUseResult": {
    "filenames": [
      "docs/paper/figures/fig_theta_sensitivity.pdf",
      "docs/paper/figures/fig_feature_ablation.pdf",
      "docs/paper/figures/fig_power_curve.png",
      "docs/paper/figures/fig_retrain_decay.png",
      "docs/paper/figures/_pdf_images/feature_importance_p1.png",
      "docs/paper/figures/feature_importance.pdf",
      "docs/paper/figures/feature_importance.png",
      "docs/paper/figures/olmo_rerun_feature_importance.pdf",
      "docs/paper/figures/cross_model_feature_comparison.pdf",
      "docs/paper/figures/_pdf_images/fig_s1_auc_decay_ci_p1.png",
      "docs/paper/figures/fig_s1_auc_decay_ci.pdf",
      "docs/paper/figures/fig_s1_auc_decay_ci.png",
      "docs/paper/figures/run_20260521_173830_0ae4e3/final_output.png",
      "docs/paper/figures/run_20260521_173830_0ae4e3/diagram_iter_1.png",
      "docs/paper/figures/run_20260521_174045_30d737/final_output.png",
      "docs/paper/figures/run_20260521_174045_30d737/diagram_iter_1.png",
      "docs/paper/_figure_backups/20260524_115454/pipeline.pdf",
      "docs/paper/_figure_backups/20260524_052908/pipeline.pdf",
      "docs/paper/_figure_backups/20260524_052908/fig_kstar_theta.pdf",
      "docs/paper/_figure_backups/20260524_052908/fig_filtering_strategies.pdf",
      "docs/paper/_figure_backups/20260524_052908/fig2_auc_decay.pdf",
      "docs/paper/_figure_backups/20260524_052908/fig3_transfer_heatmap.pdf",
      "docs/paper/_figure_backups/20260524_115454/fig2_auc_decay.pdf",
      "docs/paper/_figure_backups/20260524_115454/fig_filtering_strategies.pdf",
      "docs/paper/_figure_backups/20260524_115454/fig_kstar_theta.pdf",
      "docs/paper/_figure_backups/20260524_115454/fig3_transfer_heatmap.pdf",
      "docs/paper/figures/run_20260524_120320_d63c6f/final_output.png",
      "docs/paper/figures/run_20260524_120320_d63c6f/diagram_iter_1.png",
      "docs/paper/figures/fig_kstar_theta.pdf",
      "docs/paper/figures/fig_kstar_theta.png",
      "docs/paper/figures/run_20260524_120758_24be21/final_output.png",
      "docs/paper/figures/run_20260524_120758_24be21/diagram_iter_1.png",
      "docs/paper/figures/fig2_auc_decay.pdf",
      "docs/paper/figures/fig2_auc_decay.png",
      "docs/paper/figures/fig3_transfer_heatmap.pdf",
      "docs/paper/figures/fig3_transfer_heatmap.png",
      "docs/paper/figures/run_20260524_121205_1ebeee/final_output.png",
      "docs/paper/figures/run_20260524_121205_1ebeee/diagram_iter_1.png",
      "docs/paper/figures/_figure_backups/pipeline_theta055.png",
      "docs/paper/figures/_figure_backups/pipeline_theta055.pdf",
      "docs/paper/figures/pipeline.png",
      "docs/paper/figures/pipeline.pdf",
      "docs/paper/figures/fig_filtering_strategies.pdf",
      "docs/paper/figures/fig_filtering_strategies.png",
      "docs/paper/figures/fig_jsd_decay.pdf",
      "docs/paper/figures/fig_jsd_decay.png",
      "docs/paper/main.pdf"
    ],
    "durationMs": 10,
    "numFiles": 47,
    "truncated": false
  },
  "sourceToolAssistantUUID": "ca411a07-af58-48aa-943c-26aef8b04be9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-25T19:44:27.290Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016MUfnow2KB6WHqcRRMd4FR`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ddb0e44-c6e6-4c92-a4b5-e30197b564c8",
  "isSidechain": false,
  "requestId": "req_011CbPrquvoRd9jWkupkach7",
  "type": "assistant",
  "uuid": "38a7e501-c3a1-4e5b-b341-7570a41cc7e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnVmpH5XCTuWNQNL1PpFEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 604,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13219
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

_source line 20_

```json
{
  "type": "last-prompt",
  "leafUuid": "e715fc5b-5e42-4b93-8e66-cc2fc4709e51",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit appendix and figure data sources",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Assistant

_source line 22 · 2026-05-25T19:44:39.224Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the appendix files and the figure references. Let me also check for the `tab_crossscorer` table input file, and read the registry. Let me also search for figure generation scripts on the server. Let me do these in parallel.

Let me organize what I have so far:

**Figures referenced in tex files:**
1. `figures/fig2_auc_decay.pdf` - experiments_c1.tex:13


2. `figures/fig_kstar_theta.pdf` - experiments_c1.tex:61
3. `figures/fig3_transfer_heatmap.pdf` - experiments_c1.tex:75
4. `figures/fig_jsd_decay.pdf` - experiments_c1.tex:139
5. `figures/fig_filtering_strategies.pdf` - discussion.tex:17
6. `figures/pipeline.pdf` - method.tex:6

There's also a `\input{tables/tab_crossscorer}` in appendix_extended.tex, and I notice that `fig_theta` exists but isn't referenced anywhere in the tex files.

Now I'm checking through the remaining figures that don't have references yet—there are several sensitivity and ablation studies, power curves, retraining decay plots, and feature importance visualizations across different models. I need to search the registry and locate the figure generation scripts on the server, plus verify that tables/tab_crossscorer file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e715fc5b-5e42-4b93-8e66-cc2fc4709e51",
  "isSidechain": false,
  "requestId": "req_011CbPrrh6ezV5d4V95UHnt3",
  "type": "assistant",
  "uuid": "ded38eab-cd23-4469-8eb2-747923f6245a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wmw8dPH9ia4vkRUVgTdok",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25283,
      "cache_read_input_tokens": 25060,
      "output_tokens": 714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 714,
          "cache_read_input_tokens": 25060,
          "cache_creation_input_tokens": 25283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25283
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

_source line 23 · 2026-05-25T19:44:39.310Z_

Now let me read the registry, check the cross-scorer table file, and search for figure generation scripts on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ded38eab-cd23-4469-8eb2-747923f6245a",
  "isSidechain": false,
  "requestId": "req_011CbPrrh6ezV5d4V95UHnt3",
  "type": "assistant",
  "uuid": "2a729db7-47e7-477e-a8c6-720050f61099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wmw8dPH9ia4vkRUVgTdok",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25283,
      "cache_read_input_tokens": 25060,
      "output_tokens": 714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 714,
          "cache_read_input_tokens": 25060,
          "cache_creation_input_tokens": 25283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25283
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

_source line 24 · 2026-05-25T19:44:39.311Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_016jXcxiSRUrHkuAZujUX6iq`</summary>

```json
{
  "project": "gen-depth-contamination",
  "limit": 0,
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
  "parentUuid": "2a729db7-47e7-477e-a8c6-720050f61099",
  "isSidechain": false,
  "requestId": "req_011CbPrrh6ezV5d4V95UHnt3",
  "type": "assistant",
  "uuid": "0da56f22-770d-428b-a954-115b2882bf0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wmw8dPH9ia4vkRUVgTdok",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25283,
      "cache_read_input_tokens": 25060,
      "output_tokens": 714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 714,
          "cache_read_input_tokens": 25060,
          "cache_creation_input_tokens": 25283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25283
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

_source line 25 · 2026-05-25T19:44:40.360Z_

<details><summary>↩ Tool result · `toolu_016jXcxiSRUrHkuAZujUX6iq`</summary>

```text
Error: result (314,391 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/93bdb0df-e478-43c2-a08d-406b4a0808e1/tool-results/mcp-agent-ml-research-read_registry-1779738280345.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/93bdb0df-e478-43c2-a08d-406b4a0808e1/tool-results/mcp-agent-ml-research-read_registry-1779738280345.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/93bdb0df-e478-43c2-a08d-406b4a0808e1/tool-results/mcp-agent-ml-research-read_registry-1779738280345.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0da56f22-770d-428b-a954-115b2882bf0e",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "7006b28d-337c-4da7-995c-fcd5c81404b8",
  "toolUseResult": "Error: result (314,391 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/93bdb0df-e478-43c2-a08d-406b4a0808e1/tool-results/mcp-agent-ml-research-read_registry-1779738280345.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/93bdb0df-e478-43c2-a08d-406b4a0808e1/tool-results/mcp-agent-ml-research-read_registry-1779738280345.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/93bdb0df-e478-43c2-a08d-406b4a0808e1/tool-results/mcp-agent-ml-research-read_registry-1779738280345.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_014_independent_metrics\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:13:38.986Z\", \"updated_at\": \"2026-05-25T16:06:48.657Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && CUDA_VISIBLE_DEVICES=1 python scripts/exp014_v1_independent_metrics.py 2>&1 | tee results/exp014_v2/independent_metrics.log && CUDA_VISIBLE_DEVICES=1 python scripts/exp014_v1_independent_analysis.py 2>&1 | tee results/exp014_v2/independent_analysis.log\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"255048\", \"log_path\": \"~/runs/gen-depth-contamination/exp_014_independent_metrics.log\", \"submitted_at\": \"2026-05-25T16:06:48.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"补算 6 个与 OBD 15D 特征完全独立的质量指标（GPT-2 Large PPL, MTLD, HD-D, 3/4-gram rep rate, MAUVE, Zipf coefficient），修正 v2 初版的循环论证问题。独立指标与 predicted depth 的 Spearman correlation 应显著（Bonferroni α=0.0083），验证 depth signal 的 ecological validity 不依赖 OBD 自身特征。\", \"parent\": \"exp_014_naturalistic_v2\", \"conclusion\": \"failed\", \"notes\": \"依赖 v2 产出的 cc_predictions.csv，v2 因 FineWeb 下载失败未产出该文件，导致无限 while 循环等待 8h+。PID 234919 已 kill。bash 命令中 $(date) 在构造时被提前展开（每轮打印相同时间戳），需改为单引号转义。\", \"checkpoint_path\": \"N/A (failed, no output)\", \"log_path\": \"~/runs/gen-depth-contamination/exp_014_independent_metrics.log\"}, \"exp_014_naturalistic_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:43:51.317Z\", \"updated_at\": \"2026-05-25T15:43:33.328Z\", \"hypothesis\": \"OBD predicted depth 在 wild web text (FineWeb CC-MAIN-2025-26, 50K docs) 上与 6 个完全独立的质量指标（GPT-2 PPL, MTLD, vocd-D, n-gram repetition, MAUVE, Zipf coefficient）显著相关，验证 depth signal 的 ecological validity。Predicted depth 反映文本与 depth-k 生成文本的相似度，而非声称 CC 文本是 prompt-chain 产物。v1 仅测了 4 个指标（binary_auc/freq_entropy/ttr/cc_depth0_ratio），本次完整覆盖 9 指标 + stratified analysis + bootstrap CI。\", \"parent\": \"exp_014_naturalistic\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python scripts/exp014_naturalistic_v2.py\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"233952\", \"log_path\": \"~/runs/gen-depth-contamination/exp_014_naturalistic_v2.log\", \"submitted_at\": \"2026-05-25T06:51:43.798Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"FineWeb CC-MAIN-2025-26 (50K docs streaming)\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-1.5B-Instruct (scorer) + GPT-2 Large (PPL/MAUVE)\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen_cont_10k (OBD LightGBM trained on Qwen continuation features)\", \"eval_data\": \"FineWeb CC-MAIN-2025-26 50K English docs, 50-1000 words, truncated 256 tokens\", \"wall_clock_seconds\": 31906.8, \"gpu_hours\": 8.86}, \"checkpoint_path\": \"N/A (failed, no output)\", \"log_path\": \"results/exp014_v2/run.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-25T15:43:30.622Z\", \"notes\": \"FineWeb CC-MAIN-2024-51 streaming 下载失败（Server disconnected），脚本静默退出（exit code 0 但无产出）。错误处理缺失：未 raise RuntimeError。已修复脚本增加异常处理。\"}, \"runtime_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T13:11:11.536Z\", \"updated_at\": \"2026-05-25T06:45:44.306Z\", \"spec\": {\"command\": \"python scripts/runtime_benchmark.py\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"232163\", \"log_path\": \"~/runs/gen-depth-contamination/runtime_benchmark.log\", \"submitted_at\": \"2026-05-25T06:37:46.951Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"existing depth chain data\", \"data_count\": 1000, \"model_name\": \"Qwen2.5-1.5B-Instruct + GPT-2 Large + OLMo-1B\", \"seed\": 42, \"wall_clock_seconds\": 289.8, \"gpu_hours\": 0.08}, \"hypothesis\": \"OBD 15D feature extraction + LightGBM classifier 的 per-document inference time 显著低于 neural baselines (Binoculars/DivEye/neural probe)，且 throughput 满足大规模数据审计需求（>100 docs/sec on single GPU）。Reviewer 预期会问计算开销。\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (benchmark, no checkpoint)\", \"log_path\": \"results/runtime_benchmark/run.log\", \"completed_at\": \"2026-05-25T06:42:36.705Z\", \"metrics\": {\"obd_pipeline\": {\"ms_per_doc\": 44.3, \"ms_per_doc_std\": 7.8, \"throughput_docs_per_sec\": 22.6, \"gpu_memory_mb\": 3102, \"breakdown\": {\"scorer_forward_ms\": 20.1, \"cpu_feature_extraction_ms\": 23.4, \"classifier_ms\": 0.77}}, \"binoculars\": {\"ms_per_doc\": 17, \"ms_per_doc_std\": 1.2, \"throughput_docs_per_sec\": 58.8, \"gpu_memory_mb\": 5049}, \"diveye\": {\"ms_per_doc\": 14.2, \"ms_per_doc_std\": 0.2, \"throughput_docs_per_sec\": 70.3, \"gpu_memory_mb\": 3102}, \"neural_probe\": {\"ms_per_doc\": 14.6, \"ms_per_doc_std\": 0.2, \"throughput_docs_per_sec\": 68.3, \"gpu_memory_mb\": 3061}, \"key_finding\": \"OBD ~2.6× slower than baselines due to CPU-side self-BLEU computation (53% of time). But OBD uses less GPU memory than Binoculars (3.1 vs 5.0 GB) and provides 15D interpretable features + ordinal depth estimation vs binary-only detection. 22.6 docs/s = 50K docs in ~37min, practical for large-scale auditing.\"}, \"notes\": \"Hypothesis 被证伪：OBD 44.3ms/doc 是最慢方法（vs DivEye 14.2ms, Neural Probe 14.6ms, Binoculars 17.0ms），throughput 22.6 docs/s 未达假设的 >100 docs/s。瓶颈在 CPU self-BLEU (53%)。Rebuttal framing: OBD trades 2-3× latency for unique depth discrimination capability (K*=2 vs baselines K*=1)，不回避更慢事实，强调功能维度优势。不写入正文，仅 reviewer 显式要求时使用。\"}, \"exp_014_naturalistic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:19:56.644Z\", \"updated_at\": \"2026-05-25T06:43:30.215Z\", \"hypothesis\": \"OBD predicted depth 在 wild web text (FineWeb CC-MAIN-2025-26) 上与独立质量指标（GPT-2 PPL, MTLD, vocd-D, n-gram repetition, MAUVE, Zipf coefficient）显著相关，验证 depth signal 的 ecological validity：depth signal 反映的文本退化模式不仅存在于实验室 prompt-chain，也可在自然 web 文本中观测到。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/gen-depth-contamination/scripts/run_naturalistic_validation.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp014_naturalistic/\"}, \"conclusion\": \"success\", \"metrics\": {\"binary_auc\": 0.9919, \"cc_depth0_ratio\": 0.89, \"freq_entropy_rho\": -0.78, \"ttr_rho\": 0.17, \"note\": \"TTR rho=+0.17 contradicts hypothesis (expected negative). Paper should only report freq_entropy and CC classification, not TTR (or explicitly flag anomalous direction).\"}, \"completed_at\": \"2026-05-20T13:12:42.795Z\"}, \"gemma27b_filtering\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:52:09.087Z\", \"updated_at\": \"2026-05-24T11:40:31.003Z\", \"hypothesis\": \"Binary filtering on Gemma-27B generated contaminated text will still outperform no-filter (MMLU degradation ≤1pp), despite 27B text being harder to detect (cross-scorer K*=1, 0v1 AUC=0.887). This validates OBD binary curation robustness against unknown large generators.\", \"spec\": {\"command\": \"python scripts/exp_expanded_downstream_eval.py (adapted for Gemma-27B filtering)\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_gemma27b_c4/ (5000 Gemma-27B generated docs)\", \"data_count\": \"5000 docs, 9 runs (3 strategies x 3 seeds)\", \"model_name\": \"Gemma-2-27B (generator) + Qwen2.5-1.5B-Instruct (OBD scorer) + GPT-2 (trainee)\", \"seed\": \"42,123,456\", \"gpu\": \"cuda:3\", \"pid\": \"169724\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T11:12:46.050Z\", \"metrics\": {\"results_by_strategy\": {\"no_filter\": {\"mmlu_avg\": 0.5956, \"hellaswag_avg\": 0.6633, \"mmlu_seeds\": [0.596, 0.5954, 0.5953], \"hellaswag_seeds\": [0.6638, 0.6636, 0.6626]}, \"binary_ours\": {\"mmlu_avg\": 0.5958, \"hellaswag_avg\": 0.6674, \"mmlu_seeds\": [0.5975, 0.5946, 0.5953], \"hellaswag_seeds\": [0.6775, 0.662, 0.6626]}, \"graduated_a09\": {\"mmlu_avg\": 0.5953, \"hellaswag_avg\": 0.6629, \"mmlu_seeds\": [0.5954, 0.5953, 0.5953], \"hellaswag_seeds\": [0.6636, 0.6626, 0.6626]}}, \"binary_vs_nofilter_delta\": {\"mmlu\": \"+0.02pp\", \"hellaswag\": \"+0.41pp\"}, \"key_finding\": \"OBD binary filtering on Gemma-27B text (cross-scorer K*=1) does not degrade quality: MMLU delta=+0.02pp, HellaSwag delta=+0.41pp. Filter robust against hard-to-detect 27B contamination. Graduated shows no advantage over binary.\"}}, \"code_domain_olmo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:39:27.111Z\", \"updated_at\": \"2026-05-24T11:40:24.803Z\", \"hypothesis\": \"OLMo-1B on Python Code domain will yield K*=1 (competence-limited, similar to Pythia-1.4B on Code) or K*=2 (reaching Code ceiling). Either outcome strengthens the domain ceiling framework: K*=1 confirms competence limitation pattern, K*=2 confirms ceiling universality.\", \"spec\": {\"command\": \"python scripts/run_code_domain_olmo.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_code_olmo/ (5500 Python code docs x 6 depths)\", \"data_count\": \"5500 docs x 6 depths = 33000 samples\", \"model_name\": \"OLMo-1B (generator) + Qwen2.5-1.5B-Instruct (cross-scorer)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"pid\": \"167297\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T11:12:41.368Z\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9996, \"1v2\": 0.5567, \"2v3\": 0.5, \"3v4\": 0.5, \"4v5\": 0.5}, \"pairwise_jsd\": {\"0v1\": 0.334, \"1v2\": 0.006, \"2v3\": 0.003}, \"ordinal_mae\": 1.289, \"ordinal_accuracy\": 0.346, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"OLMo-1B Code K*=1 (competence-limited). 0v1 near-perfect (0.9996) but 1v2=0.5567 below θ. Completes OLMo 3-domain profile: C4=1, arXiv=1, Code=1 — uniformly competence-limited across all domains.\"}}, \"olmo_arxiv_cross_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T11:00:35.750Z\", \"updated_at\": \"2026-05-24T11:01:18.651Z\", \"hypothesis\": \"OLMo-1B on arXiv with cross-scorer (Qwen-1.5B) will confirm K*=1, consistent with self-scoring. While other models (Qwen, LLaMA, Mistral, Pythia) achieve K*=3 on arXiv, OLMo is competence-limited and cannot sustain distinguishable depth structure beyond generation 1.\", \"conclusion\": \"success\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9994, \"1v2\": 0.4996, \"2v3\": 0.4971, \"3v4\": 0.5091, \"4v5\": 0.536}, \"bootstrap_ci_95\": {\"0v1\": [0.999, 0.9997], \"1v2\": [0.4828, 0.5166], \"2v3\": [0.4796, 0.5138], \"3v4\": [0.4922, 0.5262], \"4v5\": [0.5183, 0.5533]}, \"p_perm\": {\"0v1\": 0.0001, \"1v2\": 0.51, \"2v3\": 0.6267, \"3v4\": 0.1488, \"4v5\": 0.0001}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"OLMo-1B arXiv cross-scorer K*=1 confirmed. 1v2=0.4996 (chance). Sole exception to arXiv ceiling=3. All other models (Qwen/LLaMA/Mistral/Pythia) reach K*=3.\"}, \"spec\": {\"command\": \"python scripts/run_olmo_arxiv_cross_scorer.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_024_arxiv/ (OLMo subset)\", \"data_count\": \"2200 docs x 6 depths\", \"model_name\": \"OLMo-1B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"gpu\": \"cuda:0\", \"checkpoint_path\": \"results/olmo_arxiv_cross_scorer/\", \"log_path\": \"results/olmo_arxiv_cross_scorer/\"}, \"completed_at\": \"2026-05-24T11:01:18.651Z\"}, \"olmo_c4_cross_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:59:03.914Z\", \"updated_at\": \"2026-05-24T10:59:48.614Z\", \"hypothesis\": \"OLMo-1B on C4 with cross-scorer (Qwen-1.5B) will confirm K*=1, matching self-scoring result. This validates OLMo as competence-limited on C4 (ceiling=2 but OLMo only reaches K*=1), completing the OLMo domain profile for the weak model exception narrative.\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.986, \"1v2\": 0.4999, \"2v3\": 0.4982, \"3v4\": 0.5016, \"4v5\": 0.4946}, \"bootstrap_ci_95\": {\"0v1\": [0.9842, 0.9877], \"1v2\": [0.4885, 0.5112], \"2v3\": [0.4869, 0.5096], \"3v4\": [0.4903, 0.513], \"4v5\": [0.483, 0.506]}, \"p_perm\": {\"0v1\": 0.0001, \"1v2\": 0.5056, \"2v3\": 0.6286, \"3v4\": 0.3955, \"4v5\": 0.8183}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"OLMo-1B C4 cross-scorer K*=1. 1v2=0.4999 (chance). Consistent across 3 pipelines. Confirms OLMo as competence-limited weak model.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python scripts/run_olmo_c4_cross_scorer.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_olmo1b_10k/ (reused OLMo C4 data)\", \"data_count\": \"5000 docs x 6 depths\", \"model_name\": \"OLMo-1B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"gpu\": \"cuda:2\", \"checkpoint_path\": \"results/olmo_c4_cross_scorer/\", \"log_path\": \"results/olmo_c4_cross_scorer/\"}, \"completed_at\": \"2026-05-24T10:59:48.614Z\"}, \"arxiv_multi_source\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:26:09.176Z\", \"updated_at\": \"2026-05-24T10:58:24.019Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_arxiv_multi_source_1b5.py\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"165918\", \"log_path\": \"~/runs/gen-depth-contamination/arxiv_multi_source.log\", \"submitted_at\": \"2026-05-24T09:15:24.821Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_024_arxiv/ (2200 docs × 6 depths × 3 generators)\", \"data_count\": \"2200 docs × 6 depths × 3 models = 39600 samples\", \"model_name\": \"Pythia-1.4B + OLMo-1B + Qwen-1.5B (generators), Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/arxiv_multi_source/\", \"wall_clock_seconds\": 3422.1, \"gpu_hours\": 0.95}, \"conclusion\": \"success\", \"hypothesis\": \"ArXiv domain K*=3 is domain-intrinsic (not model-specific): Pythia-1.4B and OLMo-1B on arXiv will also yield K*=3 (matching Qwen-1.5B exp-024), confirming that formulaic academic text structure creates larger per-generation distributional shifts that sustain one additional discriminable depth level beyond web text K*=2.\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9948, \"1v2\": 0.8581, \"2v3\": 0.6436, \"3v4\": 0.544, \"4v5\": 0.5299}, \"bootstrap_ci_bonf_qwen\": {\"2v3\": [0.629, 0.6587]}, \"bootstrap_ci_bonf_pythia\": {\"2v3\": [0.6338, 0.6626]}, \"bootstrap_ci_bonf_pooled\": {\"2v3\": [0.6466, 0.6666]}, \"per_model_2v3_auc\": {\"Qwen-1.5B\": 0.6437, \"Pythia-1.4B\": 0.6484, \"Pooled\": 0.6565}, \"bonf_p_all\": \"<0.005\", \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"K*=3 statistically confirmed across all configs. Per-model: Qwen 2v3 CI [0.629,0.659], Pythia 2v3 CI [0.634,0.663], Pooled 2v3 CI [0.647,0.667]. All CI lower > θ=0.60.\"}, \"completed_at\": \"2026-05-24T10:12:26.970Z\"}, \"wiki_domain_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:46:34.758Z\", \"updated_at\": \"2026-05-24T10:36:29.902Z\", \"hypothesis\": \"LLaMA-3.1-8B on Wikipedia will yield K*=1 (scorer-controlled), consistent with all other models on Wiki. Combined with C4 K*=2 and arXiv K*=3, this completes a 3-domain profile showing the same monotonic domain ceiling pattern as Mistral.\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9321, \"1v2\": 0.5919, \"2v3\": 0.5379, \"3v4\": 0.5105, \"4v5\": 0.5051}, \"bootstrap_ci_bonf\": {\"0v1\": [0.926, 0.938], \"1v2\": [0.5788, 0.6049], \"2v3\": [0.524, 0.5514], \"3v4\": [0.4962, 0.5244], \"4v5\": [0.4908, 0.5193]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.0005, \"3v4\": 0.231, \"4v5\": 1}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"LLaMA-8B Wiki K*=1. NOTE: 1v2 AUC=0.5919, Bonf CI upper=0.6049 marginally crosses θ but point estimate < θ. Borderline case — K*=1 by convention.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing LLaMA-8B Wiki data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_wiki_llama8b/\", \"data_count\": \"5000 docs x 6 depths\", \"model_name\": \"LLaMA-3.1-8B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"data/exp_wiki_llama8b/\", \"log_path\": \"data/exp_wiki_llama8b/\"}, \"completed_at\": \"2026-05-24T09:57:17.414Z\"}, \"wiki_domain_mistral\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:44:10.196Z\", \"updated_at\": \"2026-05-24T10:36:26.391Z\", \"hypothesis\": \"Mistral-7B on Wikipedia will yield K*=1 (scorer-controlled), completing the first 4-domain profile for a single model (Wiki=1, C4=1, Code=2, arXiv=3). This monotonic domain ceiling staircase within one model family is the strongest single-model evidence for domain-dependent K*.\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9614, \"1v2\": 0.5576, \"2v3\": 0.5193, \"3v4\": 0.5172, \"4v5\": 0.5011}, \"bootstrap_ci_bonf\": {\"0v1\": [0.9571, 0.9654], \"1v2\": [0.5434, 0.5716], \"2v3\": [0.5046, 0.5337], \"3v4\": [0.5029, 0.5317], \"4v5\": [0.4866, 0.5155]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.002, \"3v4\": 0.01, \"4v5\": 1}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"Mistral-7B Wiki K*=1 confirmed. 1v2 CI upper=0.5716 < θ=0.60.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing Mistral-7B Wiki data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_wiki_mistral7b/\", \"data_count\": \"5000 docs x 6 depths\", \"model_name\": \"Mistral-7B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_wiki_mistral7b/\", \"log_path\": \"results/exp_wiki_mistral7b/\"}, \"completed_at\": \"2026-05-24T09:57:15.436Z\"}, \"code_domain_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:48:59.617Z\", \"updated_at\": \"2026-05-24T10:36:23.146Z\", \"hypothesis\": \"Qwen2.5-7B on Python Code domain will yield K*=2 (matching Code ceiling=2 from Qwen-1.5B, LLaMA-8B, Mistral-7B), confirming Code ceiling=2 is scale-invariant within the Qwen family. This fills the last \\\"pending\\\" slot in paper_framing for Code domain.\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.905, \"1v2\": 0.7273, \"2v3\": 0.5367, \"3v4\": 0.5088, \"4v5\": 0.5137}, \"bootstrap_ci_bonf\": {\"0v1\": [0.8985, 0.9118], \"1v2\": [0.7153, 0.7389], \"2v3\": [0.5237, 0.5496], \"3v4\": [0.495, 0.5223], \"4v5\": [0.5002, 0.5274]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.0005, \"3v4\": 0.295, \"4v5\": 0.0415}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"Qwen-7B Code K*=2 confirmed. 1v2 AUC=0.7273, well above θ. Scale-invariant within Qwen family.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing Qwen-7B Code data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_code_qwen7b/ (reused from exp_code_qwen7b)\", \"data_count\": \"5500 docs x 6 depths\", \"model_name\": \"Qwen2.5-7B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_code_qwen7b/\", \"log_path\": \"results/exp_code_qwen7b/\"}, \"completed_at\": \"2026-05-24T09:57:13.302Z\"}, \"code_domain_mistral\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:38:44.455Z\", \"updated_at\": \"2026-05-24T10:36:19.220Z\", \"hypothesis\": \"Mistral-7B on Python Code domain will yield K*=2 (matching Code ceiling=2 from Qwen-1.5B and LLaMA-8B), or K*=1 if competence-limited. Combined with Mistral C4 K*=1 and arXiv K*=3, this would demonstrate domain-dependent K* variation within a single model family.\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9189, \"1v2\": 0.615, \"2v3\": 0.5292, \"3v4\": 0.5286, \"4v5\": 0.5099}, \"bootstrap_ci_bonf\": {\"0v1\": [0.9127, 0.9251], \"1v2\": [0.6024, 0.6281], \"2v3\": [0.5155, 0.5426], \"3v4\": [0.5152, 0.5418], \"4v5\": [0.4961, 0.5235]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.0005, \"3v4\": 0.0005, \"4v5\": 0.187}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"Mistral-7B Code K*=2. Bonferroni CI lower=0.6024 > θ=0.60 — statistically confirmed despite borderline AUC. Domain profile: Wiki=1, C4=1, Code=2, arXiv=3.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing Mistral-7B Code data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_code_mistral7b/\", \"data_count\": \"5500 docs x 6 depths\", \"model_name\": \"Mistral-7B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_code_mistral7b/\", \"log_path\": \"results/exp_code_mistral7b/\"}, \"completed_at\": \"2026-05-24T09:57:11.346Z\"}, \"gemma27b_cross_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:41:08.133Z\", \"updated_at\": \"2026-05-24T09:57:19.347Z\", \"hypothesis\": \"Cross-model transfer retention across 18x scale gap (27B to 1.5B) will maintain 80%+ retention, confirming depth signal is text-intrinsic and scale-invariant. OBD classifiers trained on 27B-generated text should generalize to smaller model outputs without retraining.\", \"metrics\": {\"transfer_matrix_accuracy\": {\"Gemma27B→Gemma27B\": 0.3106, \"Gemma27B→LLaMA8B\": 0.3218, \"Gemma27B→Qwen1.5B\": 0.3331, \"Gemma27B→Pythia\": 0.3214, \"Gemma27B→OLMo\": 0.2892, \"LLaMA8B→Gemma27B\": 0.3048, \"Qwen1.5B→Gemma27B\": 0.2693, \"Pythia→Gemma27B\": 0.286, \"OLMo→Gemma27B\": 0.2457}, \"transfer_matrix_mean_auc\": {\"Gemma27B→Gemma27B\": 0.6019, \"Gemma27B→LLaMA8B\": 0.6147, \"Gemma27B→Qwen1.5B\": 0.6274, \"Gemma27B→Pythia\": 0.6166, \"Gemma27B→OLMo\": 0.5934, \"LLaMA8B→Gemma27B\": 0.6037, \"Qwen1.5B→Gemma27B\": 0.5949, \"Pythia→Gemma27B\": 0.5973, \"OLMo→Gemma27B\": 0.5455}, \"retention_27b_to_small\": {\"avg_acc\": \"101.3%\", \"LLaMA8B\": \"103.6%\", \"Qwen1.5B\": \"107.2%\", \"Pythia\": \"103.5%\", \"OLMo\": \"93.1%\"}, \"retention_small_to_27b\": {\"avg_acc\": \"76.5%\", \"LLaMA8B\": \"92.1%\", \"Qwen1.5B\": \"71.3%\", \"Pythia\": \"80.9%\", \"OLMo\": \"77.3%\"}, \"retention_1.5b_inter_model\": \"88.9%\", \"result_path\": \"results/gemma27b_cross_transfer/cross_transfer_gemma27b_matrix.json\", \"key_finding\": \"27B→small retention 101.3% (>100%!): classifier trained on 27B data works BETTER on smaller models. 27B learns universal depth features. Small→27B only 76.5% due to weaker depth signal in 27B text. Strong asymmetry confirms depth signal is text-intrinsic but scale-modulated.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"5x5 cross-transfer matrix analysis (CPU)\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_gemma27b_c4/ + data from Qwen/Pythia/OLMo/LLaMA\", \"data_count\": \"5x5 model pairs, 5000 docs each\", \"model_name\": \"Gemma-2-27B + 4 smaller models, Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/gemma27b_cross_transfer/\", \"log_path\": \"results/gemma27b_cross_transfer/\"}, \"completed_at\": \"2026-05-24T09:57:19.347Z\"}, \"exp_gemma27b_c4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:57:19.726Z\", \"updated_at\": \"2026-05-24T09:13:49.177Z\", \"hypothesis\": \"Gemma-2-27B (27B params, base model) on C4 domain will show slower depth saturation (higher K*) than smaller models due to greater generation capacity, while maintaining the universal depth-dependent distinguishability pattern observed across model families.\", \"metrics\": {\"self_scorer_k_star\": 2, \"self_scorer_pairwise_auc\": {\"0v1\": 0.9695, \"1v2\": 0.6196, \"2v3\": 0.5388, \"3v4\": 0.5069, \"4v5\": 0.5124}, \"self_scorer_bootstrap_ci\": {\"0v1\": {\"auc\": 0.9695, \"ci_lower\": 0.9666, \"ci_upper\": 0.9721, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6196, \"ci_lower\": 0.6096, \"ci_upper\": 0.6296, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5388, \"ci_lower\": 0.5279, \"ci_upper\": 0.549, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5069, \"ci_lower\": 0.4959, \"ci_upper\": 0.5172, \"perm_p\": 0.1099}, \"4v5\": {\"auc\": 0.5124, \"ci_lower\": 0.5012, \"ci_upper\": 0.5234, \"perm_p\": 0.0147}}, \"cross_scorer_k_star\": 1, \"cross_scorer\": \"Qwen2.5-1.5B-Instruct\", \"cross_scorer_pairwise_auc\": {\"0v1\": 0.8871, \"1v2\": 0.5895, \"2v3\": 0.515, \"3v4\": 0.5061, \"4v5\": 0.5108}, \"cross_scorer_bootstrap_ci\": {\"0v1\": {\"auc\": 0.8871, \"ci_lower\": 0.8811, \"ci_upper\": 0.893, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.5895, \"ci_lower\": 0.5795, \"ci_upper\": 0.5997, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.515, \"ci_lower\": 0.5045, \"ci_upper\": 0.5254, \"perm_p\": 0.0027}, \"3v4\": {\"auc\": 0.5061, \"ci_lower\": 0.4952, \"ci_upper\": 0.5165, \"perm_p\": 0.1346}, \"4v5\": {\"auc\": 0.5108, \"ci_lower\": 0.4998, \"ci_upper\": 0.5218, \"perm_p\": 0.0282}}, \"cross_scorer_jsd\": {\"0v1\": 0.0643, \"1v2\": 0.0106, \"2v3\": 0.0049, \"3v4\": 0.0042, \"4v5\": 0.0031}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"Self-scorer K*=2 (1v2 CI lower=0.6096>0.60, robust). Cross-scorer K*=1 (1v2 CI upper=0.5997<0.60). 27B scale does NOT elevate K* — consistent with universal K*<=2 for web text. Cross-scorer gap reflects scale mismatch (1.5B scorer vs 27B generator).\"}, \"spec\": {\"command\": \"python scripts/run_gemma27b_depth.py (depth chain + features + bootstrap CI)\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_gemma27b_c4/ + data/exp_gemma27b_c4_qwen_scorer/\", \"data_count\": \"5000 docs x 6 depths = 30000 samples\", \"model_name\": \"google/gemma-2-27b (generator) + Qwen2.5-1.5B-Instruct (cross-scorer)\", \"seed\": 42, \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"results/exp_gemma27b_c4/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T09:13:49.177Z\"}, \"7b-cross-transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:51:00.658Z\", \"updated_at\": \"2026-05-24T09:01:43.476Z\", \"conclusion\": \"success\", \"metrics\": {\"transfer_matrix_accuracy\": {\"Qwen7B→Qwen7B\": 0.378, \"Qwen7B→LLaMA8B\": 0.312, \"LLaMA8B→Qwen7B\": 0.346, \"LLaMA8B→LLaMA8B\": 0.331}, \"transfer_matrix_mae\": {\"Qwen7B→Qwen7B\": 1.169, \"Qwen7B→LLaMA8B\": 1.51, \"LLaMA8B→Qwen7B\": 1.249, \"LLaMA8B→LLaMA8B\": 1.321}, \"transfer_matrix_tau_b\": {\"Qwen7B→Qwen7B\": 0.463, \"Qwen7B→LLaMA8B\": 0.376, \"LLaMA8B→Qwen7B\": 0.418, \"LLaMA8B→LLaMA8B\": 0.383}, \"transfer_matrix_mean_auc\": {\"Qwen7B→Qwen7B\": 0.64, \"Qwen7B→LLaMA8B\": 0.619, \"LLaMA8B→Qwen7B\": 0.635, \"LLaMA8B→LLaMA8B\": 0.62}, \"transfer_retention\": {\"Qwen→LLaMA_acc\": \"82.7%\", \"Qwen→LLaMA_tau\": \"81.2%\", \"Qwen→LLaMA_auc\": \"85.0%\", \"LLaMA→Qwen_acc\": \"104.4%\", \"LLaMA→Qwen_tau\": \"109.3%\", \"LLaMA→Qwen_auc\": \"111.8%\"}, \"key_finding\": \"7B-scale transfer retention 82-85% (Qwen→LLaMA), consistent with 1.5B-scale patterns (80-92%). LLaMA→Qwen >100% because Qwen signal stronger. Cross-scale transfer universality confirmed.\", \"data_source\": \"Qwen-7B from exp_qwen_cont_10k (subsampled 5K), LLaMA-8B from exp-018. Both Qwen2.5-1.5B cross-scored.\", \"result_path\": \"results/7b_cross_transfer_v2/cross_transfer_7b_full_metrics.json\"}, \"spec\": {\"command\": \"python scripts/run_7b_cross_transfer_v2.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_018_llama8b/features.csv + exp_qwen_cont_10k features\", \"data_count\": \"5000 docs × 6 depths × 2 models\", \"model_name\": \"Qwen2.5-7B + LLaMA-3.1-8B (OBD transfer, no GPU needed)\", \"seed\": 42, \"checkpoint_path\": \"N/A (CPU analysis)\", \"log_path\": \"results/7b_cross_transfer_v2/\"}, \"hypothesis\": \"Cross-model transfer retention at 7B scale (Qwen-7B ↔ LLaMA-8B) will match 1.5B-scale patterns (80-92%), confirming that depth signal is text-intrinsic rather than scale-dependent, and that OBD classifiers trained on one 7B model generalize to another without retraining.\", \"completed_at\": \"2026-05-24T09:01:43.476Z\"}, \"exp_015_neural_probe\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-13T18:53:34.791Z\", \"updated_at\": \"2026-05-23T11:54:24.971Z\", \"hypothesis\": \"Learned representations (frozen LLM → MLP) 的 K* 是否高于 hand-crafted 15D features？若 K*_neural > K*_15D，说明 15D projection 是 K*=2 的部分原因；若相同，加强 information-theoretic impossibility 论证\", \"notes\": \"v4 completed successfully. 3 models: Pythia K*_neural=2, OLMo K*_neural=2, Qwen-cont K*_neural=3. Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055) but only Qwen-cont self-scorer crosses θ=0.60. EXIT_CODE=129 (SIGHUP after completion) did not affect results.\", \"completed_at\": \"2026-05-14T02:58:02.023Z\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 26.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 20.06 MiB is free. Process 55665 has 13.36 GiB memory in use. Process 56371 has 9.09 GiB memory in use. Including non-PyTorch memory, this process has 1\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v4 run in progress (PID 108774, tmux: exp015, westc-26893). Root cause of prior failures: v2=OOM (concurrent exp-006 占 GPU), v3=SIGHUP/EXIT_CODE=129 (SSH 断连，未在 tmux 中)。v4 在 tmux 中安全运行，Pythia 86% → OLMo → Qwen-cont → MLP training。内存管理正确 (del+gc+empty_cache)，6.7GB/24GB。ETA ~25-30min from 09:28 UTC.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:21:59.744073+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:39.481148+00:00\"}]}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:31:35.099Z\"}, \"conclusion\": \"success\", \"metrics\": {\"k_star_qwen\": 3, \"k_star_pythia\": 2, \"k_star_olmo\": 1, \"qwen_pairwise_auc\": {\"0v1\": 0.988, \"1v2\": 0.702, \"2v3\": 0.616, \"3v4\": 0.59, \"4v5\": 0.566}, \"pythia_pairwise_auc\": {\"0v1\": 0.966, \"1v2\": 0.676, \"2v3\": 0.596, \"3v4\": 0.555, \"4v5\": 0.532}, \"olmo_pairwise_auc\": {\"0v1\": 0.9773, \"1v2\": 0.5054, \"2v3\": 0.5056, \"3v4\": 0.5032, \"4v5\": 0.4999}, \"olmo_rerun_source\": \"exp015_olmo_rerun/neural_probe_results.json\", \"notes\": \"OLMo values updated from rerun (self-probe). Original cross-model probe had K*=2 (1v2=0.657) but was superseded by self-probe rerun (K*=1, 1v2=0.5054). Paper Table 3 correctly uses rerun values.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_015_neural_probe.log\", \"spec\": {\"command\": \"python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 8\", \"server\": \"westc-26893\", \"data_path\": \"data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 90000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct (frozen encoder -> MLP probe)\", \"seed\": \"5-fold CV\"}}, \"exp_gemma2b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:00:38.686Z\", \"updated_at\": \"2026-05-23T00:21:06.691Z\", \"hypothesis\": \"Gemma-2-2B 10K sample-size robustness: 5K borderline K*=1 (1v2 AUC=0.5981, just below θ=0.60) should remain K*=1 at 10K, confirming between-sample stability for borderline verdicts. Adds a K*=1 datapoint to the 10K robustness table (currently only K*=2 configs).\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 54709, \"gpu\": \"cuda:3\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_10k/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_10k/run.log\", \"completed_at\": \"2026-05-22T23:16:00.183Z\", \"metrics\": {\"K_star_self\": 2, \"K_star_qwen\": 2, \"scorer\": \"Qwen2.5-1.5B-Instruct (cross-scored)\", \"pairwise_auc_self\": {\"0v1\": 0.9817, \"1v2\": 0.643, \"2v3\": 0.555, \"3v4\": 0.5173, \"4v5\": 0.5101}, \"pairwise_auc_qwen\": {\"0v1\": 0.9533, \"1v2\": 0.6099, \"2v3\": 0.5409, \"3v4\": 0.5174, \"4v5\": 0.5158}, \"bootstrap_ci_1v2\": {\"auc_oof\": 0.6099, \"boot_std\": 0.0034, \"ci_95\": [0.6031, 0.6167], \"ci_995_bonferroni_pct\": [0.5998, 0.6192], \"ci_995_bonferroni_norm\": [0.6003, 0.6196], \"perm_p\": 0.0001, \"bonferroni_pass_pct\": false, \"bonferroni_pass_norm\": true}, \"note\": \"5K K*=1 (1v2=0.5981), 10K Qwen cross-scored K*=2 (1v2=0.6099). Bonferroni split: percentile FAIL (0.5998), normal PASS (0.6003). Extremely borderline.\"}}, \"seed_gemma27b_c4_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:05:43.080Z\", \"updated_at\": \"2026-05-23T00:00:23.931Z\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 26893, \"gpu\": \"cuda:0\"}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma27b_c4/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma27b_c4/\", \"hypothesis\": \"Gemma-2-27B, the largest model tested, will exhibit K*=2 consistent with smaller models, confirming that generational depth saturation is model-scale-invariant for the surprisal-feature OBD pipeline.\", \"completed_at\": \"2026-05-22T23:06:04.697Z\", \"metrics\": {\"K_star\": 1, \"scorer\": \"Qwen2.5-1.5B-Instruct (cross-scored)\", \"pairwise_auc_self\": {\"0v1\": 0.9695, \"1v2\": 0.6196, \"2v3\": 0.5388, \"3v4\": 0.5069, \"4v5\": 0.5124}, \"pairwise_auc_qwen\": {\"0v1\": 0.8874, \"1v2\": 0.5894}, \"note\": \"Self-scored K*=2 (1v2=0.6196), Qwen cross-scored K*=1 (1v2=0.5894 < θ=0.60). Self→Cross inflation: 1v2 Δ=-3.0pp, 0v1 Δ=-8.2pp.\"}}, \"exp_olmo1b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:05:20.014Z\", \"updated_at\": \"2026-05-22T22:34:48.584Z\", \"hypothesis\": \"OLMo-1B on 10K C4 samples will show saturation at depth K*=1, meaning generation-depth signal is only distinguishable between real (depth-0) and first-generation synthetic text, with deeper depths being indistinguishable from each other.\", \"spec\": {\"command\": \"bash /tmp/exp_olmo1b_10k.sh (Phase1: OLMo-1B continuation gen + Phase2: Qwen scorer)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"pid\": 66415, \"data_path\": \"data/olmo1b_c4_10k\", \"data_count\": 10000, \"model_name\": \"allenai/OLMo-1B-hf (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"/tmp/exp_olmo1b_10k.log\", \"checkpoint_path\": \"results/olmo1b_c4_10k/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:34:45.698Z\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9871, \"1v2\": 0.4984, \"2v3\": 0.5059, \"3v4\": 0.5061, \"4v5\": 0.5074}, \"K_star\": 1, \"ordinal_mae\": 1.4145, \"ordinal_accuracy\": 0.3152, \"pairwise_jsd\": {\"0v1\": 0.230018, \"1v2\": 0.001457, \"2v3\": 0.001512, \"3v4\": 0.001413, \"4v5\": 0.001535}, \"top_features\": [\"freq_entropy\", \"surp_d1_mean\", \"freq_kurtosis\", \"surp_d2_mean\", \"surp_d1_skew\"]}}, \"exp_002_olmo_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:24.766Z\", \"updated_at\": \"2026-05-22T22:04:07.552Z\", \"hypothesis\": \"K* 跨模型一致性验证：OLMo-1B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp002_olmo --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"20225\", \"log_path\": \"~/runs/gen-depth-contamination/exp_002_olmo_depth.log\", \"submitted_at\": \"2026-05-13T00:16:07.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/\", \"wall_clock_seconds\": 8384.9, \"gpu_hours\": 2.33}, \"reproduce\": {\"finished_at\": \"2026-05-13T02:31:18.880Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T02:31:19.738113+00:00\"}]}, \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9861, \"1v2\": 0.5001, \"2v3\": 0.4972, \"3v4\": 0.5034, \"4v5\": 0.4971}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:35:52.823Z\", \"parent\": \"exp_001_pythia_depth\"}, \"exp_001_pythia_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:23.803Z\", \"updated_at\": \"2026-05-22T22:04:05.591Z\", \"hypothesis\": \"K* 跨模型一致性验证：Pythia-1.4B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp001_pythia --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"17138\", \"log_path\": \"~/runs/gen-depth-contamination/exp_001_pythia_depth.log\", \"submitted_at\": \"2026-05-12T20:50:31.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"wall_clock_seconds\": 12344.9, \"gpu_hours\": 3.43}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9722, \"1v2\": 0.6074, \"2v3\": 0.544, \"3v4\": 0.5051, \"4v5\": 0.5079}, \"pairwise_auc_std\": {\"0v1\": 0.0039, \"1v2\": 0.0078, \"2v3\": 0.0067, \"3v4\": 0.0032, \"4v5\": 0.0101}, \"bootstrap_ci\": {\"1v2\": {\"auc_oof\": 0.6072, \"boot_mean\": 0.6073, \"boot_std\": 0.005, \"ci_95\": [0.5975, 0.6172], \"ci_995_bonferroni\": [0.5934, 0.621], \"perm_p\": 0.0001, \"bonferroni_pass\": false}}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6539, Qwen-scored 1v2=0.6074.\"}, \"completed_at\": \"2026-05-13T00:16:16.359Z\"}, \"exp_llama8b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:25:55.895Z\", \"updated_at\": \"2026-05-22T20:26:09.870Z\", \"hypothesis\": \"增加 LLaMA-8B C4 样本量从 5k→10k 可将 1v2 bootstrap std 缩小 ~√2 倍，使 Bonferroni 99.5% CI lower bound 恢复到 θ=0.60 以上\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 23232, \"checkpoint_path\": \"results/exp_llama8b_10k/\", \"log_path\": \"/tmp/exp_llama8b_10k.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"AUC_0v1\": 0.9282, \"AUC_1v2\": 0.6148, \"AUC_1v2_oof\": 0.588, \"AUC_2v3\": 0.5247, \"AUC_3v4\": 0.5519, \"AUC_4v5\": 0.5262, \"bootstrap_1v2_oof_auc\": 0.588, \"bootstrap_1v2_95CI\": [0.5809, 0.595], \"bootstrap_1v2_995CI_bonferroni\": [0.5776, 0.5978], \"bonferroni_pass\": false, \"perm_pvalue_1v2\": 0.0001, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"All pairwise AUC from Qwen cross-scoring (Phase 2). Pipeline AUC 1v2=0.6148 (mean-of-folds).\"}, \"completed_at\": \"2026-05-22T19:21:09.215Z\"}, \"exp_pythia14b_c4_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:57:18.681Z\", \"updated_at\": \"2026-05-22T14:59:24.436Z\", \"hypothesis\": \"统一所有 K*=2 configs 的样本量至 10K，避免 selective precision boosting 质疑。Pythia-1.4B 5K 已稳定通过 Bonferroni (CI_lower≈0.641>0.60)，10K 为一致性验证。\", \"spec\": {\"command\": \"python3 scripts/run_pipeline.py --model_path pythia-1.4b --num_samples 10000 --max_depth 5 --batch_size 32 --generation_mode continuation + Phase2 Qwen scorer\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"data/exp_pythia14b_c4_10k\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"/tmp/exp_pythia14b_c4_10k.log\", \"checkpoint_path\": \"results/exp_pythia14b_c4_10k/\"}, \"metrics\": {\"K_star\": 2, \"AUC_0v1\": 0.9712, \"AUC_1v2\": 0.6175, \"AUC_2v3\": 0.5364, \"AUC_3v4\": 0.5134, \"AUC_4v5\": 0.5088, \"bootstrap_1v2_95CI\": [0.6108, 0.6242], \"bootstrap_1v2_995CI_bonferroni\": [0.6078, 0.6273], \"perm_pvalue_1v2\": 0.0001, \"bonferroni_pass\": true, \"top_feature\": \"freq_entropy\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:14:41.623Z\"}, \"exp_qwen_cont_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:27:38.591Z\", \"updated_at\": \"2026-05-22T14:59:22.490Z\", \"hypothesis\": \"增加 Qwen-cont C4 样本量从 5k→10k 可将 1v2 bootstrap std 缩小 ~√2 倍，使 Bonferroni 99.5% CI lower bound 恢复到 θ=0.60 以上\", \"spec\": {\"command\": \"bash /tmp/run_qwen_cont_10k.sh (Phase1: base generation + Phase2: instruct scoring)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_cont_10k\", \"data_count\": 10000, \"model_name\": \"Qwen/Qwen2.5-1.5B (base, continuation) + Qwen/Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_qwen_cont_10k/\", \"log_path\": \"/tmp/exp_qwen_cont_10k_phase1.log\"}, \"metrics\": {\"K_star\": 2, \"AUC_0v1\": 0.9875, \"AUC_1v2\": 0.6346, \"AUC_2v3\": 0.5616, \"AUC_3v4\": 0.5451, \"AUC_4v5\": 0.5254, \"bootstrap_1v2_95CI\": [0.6282, 0.6409], \"bootstrap_1v2_995CI_bonferroni\": [0.6255, 0.6436], \"perm_pvalue_1v2\": 0.0001, \"bonferroni_pass\": true, \"top_feature\": \"freq_entropy\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:47:57.847Z\"}, \"exp_pythia14b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:59:05.554Z\", \"updated_at\": \"2026-05-22T12:00:24.157Z\", \"hypothesis\": \"统一所有 K*=2 configs 样本量至 10K，避免 selective precision boosting 质疑。Pythia-1.4B 5K 已稳定通过 Bonferroni (CI_lower≈0.641>0.60)，10K 为一致性验证。\", \"spec\": {\"command\": \"python3 scripts/run_pipeline.py --model_path pythia-1.4b --num_samples 10000 --max_depth 5 --batch_size 32 --generation_mode continuation + Phase2 Qwen scorer\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"data/exp_pythia14b_c4_10k\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"N/A\", \"note\": \"重复条目，已合并到 exp_pythia14b_c4_10k\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-22T12:00:24.157Z\"}, \"seed_qwen15b_c4_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:11.792Z\", \"updated_at\": \"2026-05-22T06:39:21.815Z\", \"hypothesis\": \"Qwen-1.5B C4 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode rewrite --top_p 0.95 --seed 123 (C4)\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"3156\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_c4_s123/\", \"submitted_at\": \"2026-05-22T03:58:27.354Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_qwen15b_c4_s123\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 123, \"metrics\": {\"K_star\": 2, \"auc_0v1\": 0.9956, \"auc_1v2\": 0.7014, \"auc_2v3\": 0.5911, \"auc_3v4\": 0.5405, \"auc_4v5\": 0.5335}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_c4_s123/\", \"wall_clock_seconds\": 9654.5, \"gpu_hours\": 2.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:39:21.815Z\"}, \"seed_qwen15b_wiki_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:09.969Z\", \"updated_at\": \"2026-05-22T06:39:19.860Z\", \"hypothesis\": \"Qwen-1.5B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode rewrite --top_p 0.95 --seed 123\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"3005\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_wiki_s123/\", \"submitted_at\": \"2026-05-22T03:58:25.151Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_qwen15b_wiki_s123\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 123, \"metrics\": {\"K_star\": 3, \"auc_0v1\": 0.9945, \"auc_1v2\": 0.7059, \"auc_2v3\": 0.6067, \"auc_3v4\": 0.5531, \"auc_4v5\": 0.5292}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_wiki_s123/\", \"wall_clock_seconds\": 9654.7, \"gpu_hours\": 2.68}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T06:39:19.860Z\"}, \"seed_pythia14b_wiki_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:08.091Z\", \"updated_at\": \"2026-05-22T06:39:17.971Z\", \"hypothesis\": \"Pythia-1.4B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode continuation --top_p 0.95 --seed 123 (two-phase: Pythia gen + Qwen score)\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"2863\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_pythia14b_wiki_s123/\", \"submitted_at\": \"2026-05-22T03:58:22.018Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_pythia14b_wiki_s123\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b (generator) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 123, \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9751, \"auc_1v2\": 0.5766, \"auc_2v3\": 0.5318, \"auc_3v4\": 0.5175, \"auc_4v5\": 0.527}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_pythia14b_wiki_s123/\", \"wall_clock_seconds\": 9656.0, \"gpu_hours\": 2.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:39:17.971Z\"}, \"sweep_r10_nofilter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:16:37.475Z\", \"updated_at\": \"2026-05-22T00:54:53.730Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=1 python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"333215\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r10_nofilter.log\", \"submitted_at\": \"2026-05-20T17:16:36.869Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r10_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:16:39.694Z\", \"updated_at\": \"2026-05-22T00:54:52.904Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=2 python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy binary --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"333292\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r10_binary.log\", \"submitted_at\": \"2026-05-20T17:16:39.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r10_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:16:41.394Z\", \"updated_at\": \"2026-05-22T00:54:52.064Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=3 python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy graduated --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"333434\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r10_graduated.log\", \"submitted_at\": \"2026-05-20T17:16:40.993Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r30_nofilter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:16:43.195Z\", \"updated_at\": \"2026-05-22T00:54:44.685Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=0 python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy no_filter --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"223186\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r30_nofilter.log\", \"submitted_at\": \"2026-05-20T17:16:42.824Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_nofilter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:34:33.240Z\", \"updated_at\": \"2026-05-22T00:54:43.784Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_nofilter.log\", \"submitted_at\": \"2026-05-20T17:34:32.842Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:34:35.595Z\", \"updated_at\": \"2026-05-22T00:54:42.896Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy binary --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_binary.log\", \"submitted_at\": \"2026-05-20T17:34:35.217Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:34:37.559Z\", \"updated_at\": \"2026-05-22T00:54:42.034Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy graduated --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_graduated.log\", \"submitted_at\": \"2026-05-20T17:34:37.105Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r30_nofilter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:34:39.366Z\", \"updated_at\": \"2026-05-22T00:54:41.166Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r30_nofilter.log\", \"submitted_at\": \"2026-05-20T17:34:38.989Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_nf\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:35:11.100Z\", \"updated_at\": \"2026-05-22T00:54:40.358Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"338477\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_nf.log\", \"submitted_at\": \"2026-05-20T17:35:10.713Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_bin\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:35:13.515Z\", \"updated_at\": \"2026-05-22T00:54:39.423Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy binary --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"338554\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_bin.log\", \"submitted_at\": \"2026-05-20T17:35:13.136Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_grad\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:35:15.378Z\", \"updated_at\": \"2026-05-22T00:54:37.930Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy graduated --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"338694\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_grad.log\", \"submitted_at\": \"2026-05-20T17:35:14.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r30_nf\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:35:17.531Z\", \"updated_at\": \"2026-05-22T00:54:36.954Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"224549\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r30_nf.log\", \"submitted_at\": \"2026-05-20T17:35:17.149Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_nf_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:44:37.119Z\", \"updated_at\": \"2026-05-22T00:54:36.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"341368\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_nf_v2.log\", \"submitted_at\": \"2026-05-20T17:44:36.698Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r30_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:44:38.912Z\", \"updated_at\": \"2026-05-22T00:54:31.052Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy binary --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"341445\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r30_binary.log\", \"submitted_at\": \"2026-05-20T17:44:38.527Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r30_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:44:40.942Z\", \"updated_at\": \"2026-05-22T00:54:30.235Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy graduated --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"341524\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r30_graduated.log\", \"submitted_at\": \"2026-05-20T17:44:40.527Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r50_nf\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:46:06.026Z\", \"updated_at\": \"2026-05-22T00:54:29.360Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 50 --strategy no_filter --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"225683\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r50_nf.log\", \"submitted_at\": \"2026-05-20T17:46:05.636Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r50_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:49:15.968Z\", \"updated_at\": \"2026-05-22T00:54:28.489Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 50 --strategy binary --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"344316\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r50_binary.log\", \"submitted_at\": \"2026-05-20T17:53:07.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r50_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:53:10.838Z\", \"updated_at\": \"2026-05-22T00:54:27.679Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 50 --strategy graduated --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"344395\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r50_graduated.log\", \"submitted_at\": \"2026-05-20T17:53:10.443Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r100_nf\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:53:12.678Z\", \"updated_at\": \"2026-05-22T00:54:26.843Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 100 --strategy no_filter --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"226555\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r100_nf.log\", \"submitted_at\": \"2026-05-20T17:53:12.278Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r100_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:53:46.876Z\", \"updated_at\": \"2026-05-22T00:54:25.989Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 100 --strategy graduated --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:1\"], \"pid\": \"226991\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r100_graduated.log\", \"submitted_at\": \"2026-05-20T17:53:46.454Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r100_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:53:14.587Z\", \"updated_at\": \"2026-05-22T00:54:25.067Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 100 --strategy binary --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"227976\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r100_binary.log\", \"submitted_at\": \"2026-05-20T18:00:00.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filtering_predict\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:48:51.515Z\", \"updated_at\": \"2026-05-22T00:54:24.104Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && rm -rf /root/autodl-tmp/.hf_cache/models--microsoft--deberta-v3-base/.no_exist && python -c 'from transformers import AutoTokenizer, AutoModelForSequenceClassification; print(\\\\\\\"Downloading deberta-v3-base...\\\\\\\"); AutoTokenizer.from_pretrained(\\\\\\\"microsoft/deberta-v3-base\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"); AutoModelForSequenceClassification.from_pretrained(\\\\\\\"microsoft/deberta-v3-base\\\\\\\", num_labels=6, cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"); print(\\\\\\\"Download complete.\\\\\\\")' && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=2 python scripts/exp_deberta_filtering_predict.py --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"349680\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filtering_predict.log\", \"submitted_at\": \"2026-05-20T18:40:45.030Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filter_no_filter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:11:24.655Z\", \"updated_at\": \"2026-05-22T00:54:23.131Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && export HF_DATASETS_OFFLINE=0 && export HF_HUB_OFFLINE=0 && export TRANSFORMERS_OFFLINE=0 && cd /root/autodl-tmp/gen-depth-contamination && python -u scripts/exp_deberta_filtering_comparison.py --strategy no_filter --device cuda:0 --seed 42\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"353797\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filter_no_filter.log\", \"submitted_at\": \"2026-05-20T19:12:18.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filter_obd_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:11:26.462Z\", \"updated_at\": \"2026-05-22T00:54:18.302Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && export HF_DATASETS_OFFLINE=0 && export HF_HUB_OFFLINE=0 && export TRANSFORMERS_OFFLINE=0 && cd /root/autodl-tmp/gen-depth-contamination && python -u scripts/exp_deberta_filtering_comparison.py --strategy obd_binary --device cuda:0 --seed 42\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"353876\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filter_obd_binary.log\", \"submitted_at\": \"2026-05-20T19:12:21.027Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filter_deberta_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:11:29.363Z\", \"updated_at\": \"2026-05-22T00:54:17.473Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && export HF_DATASETS_OFFLINE=0 && export HF_HUB_OFFLINE=0 && export TRANSFORMERS_OFFLINE=0 && cd /root/autodl-tmp/gen-depth-contamination && python -u scripts/exp_deberta_filtering_comparison.py --strategy deberta_binary --device cuda:0 --seed 42\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"354020\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filter_deberta_binary.log\", \"submitted_at\": \"2026-05-20T19:12:23.647Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filter_deberta_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:26:32.955Z\", \"updated_at\": \"2026-05-22T00:54:16.540Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_DISABLE_XET=1 && python -u scripts/exp_deberta_filtering_comparison.py --strategy deberta_graduated --device cuda:0 --seed 42\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"359411\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filter_deberta_graduated.log\", \"submitted_at\": \"2026-05-20T19:28:15.359Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"seed2_no_filter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:20:45.368Z\", \"updated_at\": \"2026-05-22T00:54:15.656Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 2 --num_seeds 1 --strategy no_filter --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"362953\", \"log_path\": \"~/runs/gen-depth-contamination/seed2_no_filter.log\", \"submitted_at\": \"2026-05-20T20:20:44.951Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"seed2_binary_ours\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:20:47.753Z\", \"updated_at\": \"2026-05-22T00:54:14.713Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 2 --num_seeds 1 --strategy binary_ours --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"363095\", \"log_path\": \"~/runs/gen-depth-contamination/seed2_binary_ours.log\", \"submitted_at\": \"2026-05-20T20:20:47.308Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"seed2_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:20:49.637Z\", \"updated_at\": \"2026-05-22T00:54:13.865Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 2 --num_seeds 1 --strategy graduated --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"363242\", \"log_path\": \"~/runs/gen-depth-contamination/seed2_graduated.log\", \"submitted_at\": \"2026-05-20T20:20:49.203Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"gsm8k_patch_nf_s0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:13:12.767Z\", \"updated_at\": \"2026-05-22T00:54:13.005Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 0 --num_seeds 1 --strategy no_filter --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"368659\", \"log_path\": \"~/runs/gen-depth-contamination/gsm8k_patch_nf_s0.log\", \"submitted_at\": \"2026-05-20T21:13:12.327Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"gsm8k_patch_bo_s0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:13:15.584Z\", \"updated_at\": \"2026-05-22T00:54:12.180Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 0 --num_seeds 1 --strategy binary_ours --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"368799\", \"log_path\": \"~/runs/gen-depth-contamination/gsm8k_patch_bo_s0.log\", \"submitted_at\": \"2026-05-20T21:13:15.174Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"gsm8k_patch_grad_s0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:13:17.809Z\", \"updated_at\": \"2026-05-22T00:54:11.337Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 0 --num_seeds 1 --strategy graduated --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"368942\", \"log_path\": \"~/runs/gen-depth-contamination/gsm8k_patch_grad_s0.log\", \"submitted_at\": \"2026-05-20T21:13:17.386Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"gsm8k-serial-rerun\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:59:44.212Z\", \"updated_at\": \"2026-05-22T00:54:10.300Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 1 --num_seeds 1 --strategy no_filter --skip_base && python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 1 --num_seeds 1 --strategy binary_ours --skip_base && lm_eval --model hf --model_args pretrained=Qwen/Qwen2.5-1.5B --tasks gsm8k --num_fewshot 5 --batch_size auto --device cuda:0 --output_path results/exp_expanded_downstream_eval/base_gsm8k_eval\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"373073\", \"log_path\": \"~/runs/gen-depth-contamination/gsm8k-serial-rerun.log\", \"submitted_at\": \"2026-05-20T21:59:43.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"exp_008_retrain_chain\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:26:02.931Z\", \"updated_at\": \"2026-05-22T00:53:20.061Z\", \"hypothesis\": \"Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain K* ≤ prompt-chain K*=2. 每代独立 LoRA fine-tune 1 epoch on 前代输出，再用 fine-tuned model 生成下一代。验证 prompt-chain 是 conservative upper bound。C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"conclusion\": \"killed\"}, \"exp_olmo_retrain_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:36:11.450Z\", \"updated_at\": \"2026-05-22T00:53:19.065Z\", \"hypothesis\": \"OLMo-1B retrain-chain ecological validity (v2, fix M009 model download): LoRA rank=16, alpha=32, 1 epoch per generation on C4 5K docs. Retrain-chain K* ≤ prompt-chain K*=2, confirming prompt-chain as conservative upper bound. Independent LoRA per generation, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_olmo_retrain_chain\", \"conclusion\": \"killed\", \"notes\": \"Director 决定放弃 OLMo retrain-chain (2026-05-18)。原因：cqa1 两次下载失败（M009 模型权重中断 + 网络端口耗尽），DDL 紧张不再重试。cuda:0 重新分配给 code domain 备用或 Qwen retrain-chain。\"}, \"exp_pythia69b_c4_nuc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:57:54.120Z\", \"updated_at\": \"2026-05-21T23:00:07.454Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上使用 nucleus sampling（非 greedy）的 K*=2，与其他 continuation 模型的 decoding 策略对齐，消除 greedy 高估 confound。生成阶段自评，完成后用 Qwen-1.5B scorer 重跑 features+OBD（方案 2）。\", \"parent\": \"exp_pythia69b_c4_depth_chain_v3\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path ... --scorer_path Qwen2.5-1.5B --num_samples 5000 --max_depth 5 --generation_mode continuation --data_dir data/exp_pythia69b_c4_nuc --results_dir results/exp_pythia69b_c4_nuc\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_pythia69b_c4_nuc\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-6.9b\", \"seed\": \"default\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A (full pipeline: seed->generation->features->OBD)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/pythia69b_nuc_v2.log\", \"checkpoint_path\": \"results/exp_pythia69b_c4_nuc_qwen/\"}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9599, \"1v2\": 0.5955, \"2v3\": 0.5298, \"3v4\": 0.5135}, \"scorer\": \"Qwen-1.5B\", \"theta\": 0.6, \"note\": \"1v2 AUC borderline (0.0045 below threshold)\"}, \"completed_at\": \"2026-05-21T23:00:07.454Z\"}, \"exp_pythia69b_c4_depth_chain_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:21:54.364Z\", \"updated_at\": \"2026-05-21T19:55:37.923Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上的 K*=2，与其他 ≥7B 模型一致，验证 K*=2 不依赖 Qwen 家族。使用 Qwen-1.5B scorer（D095）。\", \"parent\": \"exp_pythia69b_c4_depth_chain_v2\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/snapshots/c0e3eee36dc47af0c49f361c74cfe459c09f7f23 --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --num_samples 5000 --max_depth 5 --batch_size 4 --feat_batch_size 2 --generation_mode continuation --no_sample --data_dir data/exp_pythia69b_c4 --results_dir results/exp_pythia69b_c4\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"395575\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain_v3.log\", \"submitted_at\": \"2026-05-21T03:22:20.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"EleutherAI/pythia-6.9b\", \"model_path\": \"/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/snapshots/c0e3eee36dc47af0c49f361c74cfe459c09f7f23\", \"scorer_path\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"data_path\": \"data/exp_pythia69b_c4\", \"data_count\": 5000, \"seed\": \"default\", \"generation_mode\": \"continuation\", \"no_sample\": true, \"max_depth\": 5, \"checkpoint_source\": \"N/A (full pipeline)\", \"eval_data\": \"N/A (full pipeline: seed->generation->features->OBD)\", \"wall_clock_seconds\": 32849.3, \"gpu_hours\": 9.12}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:29:46.273Z\"}, \"failure_reason\": \"greedy confound (--no_sample): AUC_1v2 inflated to 0.8542, not usable for cross-model comparison. K*=2 under greedy is artifact, not genuine nucleus result.\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T12:29:49.365Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:29:53.480338+00:00\"}]}, \"metrics\": {\"0v1_auc\": 0.9941, \"1v2_auc\": 0.8542, \"2v3_auc\": 0.5373, \"3v4_auc\": 0.5339, \"4v5_auc\": 0.5211, \"kstar_at_060\": 2, \"0v1_jsd\": 0.53459, \"1v2_jsd\": 0.06438, \"2v3_jsd\": 0.00502, \"empty_texts_total\": 144, \"features_rows\": 30000}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_pythia69b_c4/features.csv\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain_v3.log\"}, \"exp_pythia14b_c4_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:10:50.827Z\", \"updated_at\": \"2026-05-21T14:09:26.792Z\", \"hypothesis\": \"Pythia-1.4B C4 depth chain 可复现性验证：标准化 pipeline（Qwen-1.5B scorer）下 K* 值与主表一致。\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path pythia-1.4b --scorer_path Qwen2.5-1.5B --generation_mode continuation --no_sample --data_dir data/exp_pythia14b_c4_rerun --results_dir results/exp_pythia14b_c4_rerun\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_pythia14b_c4_rerun\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": \"default\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_pythia14b_c4_rerun/features.csv\", \"log_path\": \"N/A\", \"NOTE\": \"GREEDY (--no_sample) — not comparable to main table nucleus results\"}, \"completed_at\": \"2026-05-21T14:09:16.827Z\", \"metrics\": {\"0v1_auc\": 0.9979, \"1v2_auc\": 0.8786, \"2v3_auc\": 0.5399, \"3v4_auc\": 0.5062, \"4v5_auc\": 0.5025, \"kstar_at_060\": 2, \"0v1_jsd\": 0.5844, \"1v2_jsd\": 0.0718, \"NOTE\": \"GREEDY decoding -- inflated AUC, not comparable to main table\"}}, \"exp_olmo1b_c4_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:10:33.358Z\", \"updated_at\": \"2026-05-21T11:11:13.525Z\", \"hypothesis\": \"OLMo-1B C4 depth chain 可复现性验证：标准化 pipeline（Qwen-1.5B scorer）下 K* 值与主表一致。\", \"conclusion\": \"negative\", \"metrics\": {\"0v1_auc\": 0.986, \"1v2_auc\": 0.508, \"2v3_auc\": 0.4973, \"3v4_auc\": 0.5024, \"4v5_auc\": 0.4942, \"kstar_at_060\": 1, \"main_table_1v2\": 0.6145, \"delta\": -0.1065}, \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--allenai--OLMo-1B-hf/... --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --no_sample\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"data_path\": \"data/exp_olmo1b_c4_rerun\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": \"default\", \"checkpoint_path\": \"results/exp_olmo1b_c4_rerun/\", \"log_path\": \"results/exp_olmo1b_c4_rerun/experiment_config.json\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"completed_at\": \"2026-05-21T11:11:13.525Z\"}, \"exp_pythia69b_c4_depth_chain_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:23:27.242Z\", \"updated_at\": \"2026-05-21T02:46:08.127Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上的 K*=2，与其他 ≥7B 模型一致，验证 K*=2 不依赖 Qwen 家族。使用 Qwen-1.5B scorer 以匹配主表（D095）。\", \"parent\": \"exp_pythia69b_c4_depth_chain\", \"spec\": {\"model_name\": \"EleutherAI/pythia-6.9b\", \"model_path\": \"/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/snapshots/c0e3eee36dc47af0c49f361c74cfe459c09f7f23\", \"scorer_path\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"data_path\": \"data/exp_pythia69b_c4 (C4 seed from run_pipeline.py)\", \"data_count\": 5000, \"seed\": \"default\", \"generation_mode\": \"continuation\", \"no_sample\": true, \"max_depth\": 5, \"batch_size\": 4, \"feat_batch_size\": 2, \"num_samples\": 5000, \"command\": \"python scripts/run_pipeline.py --model_path .../pythia-6.9b --scorer_path .../Qwen2___5-1___5B --num_samples 5000 --max_depth 5 --generation_mode continuation --no_sample\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"391937\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain_v2.log\", \"submitted_at\": \"2026-05-21T02:23:38Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"N/A (full pipeline re-run, not eval)\", \"eval_data\": \"N/A (full pipeline: seed→generation→features→OBD)\", \"failure_reason\": \"模型文件不完整: 缺少 model-00001-of-00002.safetensors, v1 下载中断仅完成 66%\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 1350.1, \"gpu_hours\": 0.38}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T02:46:08.127Z\"}, \"exp_pythia69b_c4_depth_chain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:47:28.696Z\", \"updated_at\": \"2026-05-21T02:23:07.638Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上的 K*=2，与其他 ≥7B 模型一致，验证 K*=2 不依赖 Qwen 家族。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && cd /root/autodl-tmp/gen-depth-contamination && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_DISABLE_XET=1 && echo '=== Downloading Pythia-6.9B ===' && python -c 'from huggingface_hub import snapshot_download; path=snapshot_download(\\\\\\\"EleutherAI/pythia-6.9b\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"); print(f\\\\\\\"MODEL_PATH={path}\\\\\\\")' && MODEL_PATH=\\\\$(python -c 'from huggingface_hub import snapshot_download; print(snapshot_download(\\\\\\\"EleutherAI/pythia-6.9b\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"))') && echo \\\\\\\"=== Running pipeline with model at \\\\$MODEL_PATH ===\\\\\\\" && mkdir -p data/exp_pythia69b_c4 results/exp_pythia69b_c4 && python scripts/run_pipeline.py --model_path \\\\$MODEL_PATH --data_dir data/exp_pythia69b_c4 --results_dir results/exp_pythia69b_c4 --num_samples 5000 --max_depth 5 --batch_size 4 --feat_batch_size 2 --generation_mode continuation --no_sample\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"390600\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain.log\", \"submitted_at\": \"2026-05-21T01:56:36.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D095 violation: missing --scorer_path, used self-scoring instead of Qwen-1.5B. Killed by Director. Will resubmit as v2.\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 1591.2, \"gpu_hours\": 0.44}, \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-21T01:54:27.864Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && cd /root/autodl-tmp/gen-depth-contamination && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_DISABLE_XET=1 && echo '=== Downloading Pythia-6.9B ===' && python -c 'from huggingface_hub import snapshot_download; path=snapshot_download(\\\\\\\"EleutherAI/pythia-6.9b\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"); print(f\\\\\\\"MODEL_PATH={path}\\\\\\\")' && MODEL_PATH=\\\\$(python -c 'from huggingface_hub import snapshot_download; print(snapshot_download(\\\\\\\"EleutherAI/pythia-6.9b\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"))') && echo \\\\\\\"=== Running pipeline with model at \\\\$MODEL_PATH ===\\\\\\\" && mkdir -p data/exp_pythia69b_c4 results/exp_pythia69b_c4 && python scripts/run_pipeline.py --model_path \\\\$MODEL_PATH --data_dir data/exp_pythia69b_c4 --results_dir results/exp_pythia69b_c4 --num_samples 5000 --max_depth 5 --batch_size 4 --feat_batch_size 2 --generation_mode continuation --no_sample\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\"}, \"pid\": \"390600\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T02:23:07.638Z\"}, \"exp_expanded_downstream_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:02:47.262Z\", \"updated_at\": \"2026-05-21T00:23:17.997Z\", \"hypothesis\": \"K*-guided binary filtering consistently outperforms graduated filtering across a broader set of benchmarks (GSM8K, ARC-Challenge, WinoGrande, TruthfulQA, PIQA), not just MMLU/HellaSwag, validating the generalizability of the filtering consistency claim in Section 5.\", \"spec\": {\"command\": \"python scripts/run_expanded_eval.py (base eval + 3 strategies × 3 seeds LoRA train+eval, 5 benchmarks)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"pid\": \"334626\", \"log_path\": \"cqa1-22115:/root/gen-depth-contamination/results/exp_expanded_downstream_eval/\", \"submitted_at\": \"2026-05-20T17:17:37.434Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 30000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": \"42,123,456\", \"benchmarks\": \"PIQA, TruthfulQA-MC2, WinoGrande, ARC-Challenge, GSM8K\", \"checkpoint_path\": \"cqa1-22115:/root/gen-depth-contamination/results/exp_expanded_downstream_eval/\", \"wall_clock_seconds\": 24379.3, \"gpu_hours\": 6.77}, \"gpus\": [], \"metrics\": {\"metric_standard\": \"PIQA=acc_norm, ARC-C=acc_norm, WinoGrande=acc, TruthfulQA=mc2, GSM8K=exact_match(strict)\", \"base_model\": {\"piqa\": 0.7612, \"arc_c\": 0.5486, \"winogrande\": 0.6456, \"truthfulqa\": 0.4659, \"gsm8k\": 0.6224}, \"no_filter_mean\": {\"piqa\": 0.7519, \"arc_c\": 0.5193, \"winogrande\": 0.6485, \"truthfulqa\": 0.4246, \"gsm8k\": 0.5666}, \"binary_ours_mean\": {\"piqa\": 0.7479, \"arc_c\": 0.5171, \"winogrande\": 0.6406, \"truthfulqa\": 0.4398, \"gsm8k\": 0.5858}, \"graduated_mean\": {\"piqa\": 0.751, \"arc_c\": 0.519, \"winogrande\": 0.6461, \"truthfulqa\": 0.4245, \"gsm8k\": 0.5613}, \"binary_vs_nf_delta\": {\"piqa\": -0.4, \"arc_c\": -0.22, \"winogrande\": -0.79, \"truthfulqa\": 1.52, \"gsm8k\": 1.92}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T00:03:56.750Z\"}, \"exp_deberta_filtering_comparison\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:02:50.271Z\", \"updated_at\": \"2026-05-20T20:08:32.368Z\", \"hypothesis\": \"DeBERTa's higher K* on arXiv (K*=4 vs 15D K*=3) does not yield significantly better downstream performance when used for filtering, validating that the 15D lower bound is practically sufficient.\", \"spec\": {\"command\": \"python scripts/exp_deberta_filtering_comparison.py --strategy {no_filter,obd_binary,deberta_binary,deberta_graduated} --device cuda:0 --seed 42\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/\", \"data_count\": 13200, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 42, \"strategies\": [\"no_filter\", \"obd_binary\", \"deberta_binary\", \"deberta_graduated\"], \"prediction_results\": {\"deberta_accuracy\": 0.5363, \"obd_accuracy\": 0.4741, \"deberta_pred_distribution\": [2184, 1645, 2111, 1971, 1074, 4215], \"obd_pred_distribution\": [2177, 2470, 2196, 1900, 2098, 2359]}, \"lora_config\": {\"rank\": 16, \"alpha\": 32, \"targets\": [\"q_proj\", \"v_proj\"], \"dropout\": 0.05}, \"training_config\": {\"lr\": 0.0002, \"batch_size\": 4, \"grad_accum\": 4, \"epochs\": 1, \"max_length\": 256}, \"gpu_allocation\": {\"no_filter\": \"cuda:1\", \"obd_binary\": \"cuda:2\", \"deberta_binary\": \"cuda:3\", \"deberta_graduated\": \"pending\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_filtering_comparison/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_filtering_comparison/\"}, \"metrics\": {\"no_filter\": {\"mmlu\": 0.5895, \"hellaswag\": 0.6591, \"arc_c\": 0.4352}, \"obd_binary\": {\"mmlu\": 0.588, \"hellaswag\": 0.6599, \"arc_c\": 0.4522}, \"deberta_binary\": {\"mmlu\": 0.587, \"hellaswag\": 0.6593, \"arc_c\": 0.4471}, \"deberta_graduated\": {\"mmlu\": 0.5884, \"hellaswag\": 0.6586, \"arc_c\": 0.442}, \"summary\": \"obd_binary (15D) >= deberta_binary on all 3 benchmarks. DeBERTa K*=4 does not yield better filtering than 15D K*=3. Graduated < binary for both OBD and DeBERTa.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T20:06:51.128Z\"}, \"exp_contamination_rate_sweep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:02:48.807Z\", \"updated_at\": \"2026-05-20T18:02:19.878Z\", \"hypothesis\": \"Binary filtering (remove depth>=1) consistently outperforms graduated filtering across contamination rates (10/30/50/100%), validating that K*=2 provides actionable curation guidance across realistic contamination scenarios, not just at full contamination.\", \"spec\": {\"command\": \"python scripts/contamination_rate_sweep.py (4 rates x 3 strategies = 12 runs)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1,cuda:2,cuda:3\", \"pid\": \"333220,333297,333439\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/contamination_sweep/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"training_config\": \"LoRA rank=16 alpha=32 1epoch\", \"current_round\": \"rate=10% (no_filter:cuda1/binary:cuda2/graduated:cuda3)\", \"remaining_rounds\": \"rate=30%,50%,100%\", \"eval_benchmarks\": \"MMLU-5shot HellaSwag-10shot ARC-Challenge-25shot\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_contamination_rate_sweep/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_contamination_rate_sweep/summary.json\"}, \"metrics\": {\"rate_10\": {\"no_filter\": {\"mmlu\": 0.5878, \"hellaswag\": 0.6652, \"arc_c\": 0.4471}, \"binary\": {\"mmlu\": 0.5868, \"hellaswag\": 0.6709, \"arc_c\": 0.4462}, \"graduated\": {\"mmlu\": 0.5873, \"hellaswag\": 0.6672, \"arc_c\": 0.4428}}, \"rate_30\": {\"no_filter\": {\"mmlu\": 0.5885, \"hellaswag\": 0.6625, \"arc_c\": 0.4334}, \"binary\": {\"mmlu\": 0.5867, \"hellaswag\": 0.6702, \"arc_c\": 0.448}, \"graduated\": {\"mmlu\": 0.5873, \"hellaswag\": 0.664, \"arc_c\": 0.4334}}, \"rate_50\": {\"no_filter\": {\"mmlu\": 0.5858, \"hellaswag\": 0.6582, \"arc_c\": 0.43}, \"binary\": {\"mmlu\": 0.5913, \"hellaswag\": 0.67, \"arc_c\": 0.4505}, \"graduated\": {\"mmlu\": 0.5848, \"hellaswag\": 0.6606, \"arc_c\": 0.4292}}, \"rate_100\": {\"no_filter\": {\"mmlu\": 0.5707, \"hellaswag\": 0.6217, \"arc_c\": 0.3891}, \"binary\": null, \"graduated\": {\"mmlu\": 0.5701, \"hellaswag\": 0.6215, \"arc_c\": 0.3933}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T18:02:19.878Z\"}, \"exp_olmo_retrain_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:47:22.000Z\", \"updated_at\": \"2026-05-20T14:57:53.008Z\", \"hypothesis\": \"OLMo-1B retrain-chain K*>=4 (matching Pythia/Qwen retrain-chain), confirming retrain-chain K* is protocol-determined not architecture-determined. LoRA rank=16, alpha=32, 1 epoch per generation, C4 5K docs, depth 0-4.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python exp_olmo_retrain_v3.py --device cuda:0\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/olmo_retrain_chain\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42}, \"metrics\": {\"k_star\": 4, \"pairwise_auc\": {\"0v1\": 0.9873, \"1v2\": 0.8889, \"2v3\": 0.7036, \"3v4\": 0.6817}, \"bootstrap_ci_10k\": {\"0v1\": {\"mean\": 0.9972, \"ci_95\": [0.9967, 0.9977]}, \"1v2\": {\"mean\": 0.9572, \"ci_95\": [0.9542, 0.9601]}, \"2v3\": {\"mean\": 0.8885, \"ci_95\": [0.8814, 0.8947]}, \"3v4\": {\"mean\": 0.8772, \"ci_95\": [0.8684, 0.8852]}}, \"permutation_test\": {\"0v1\": {\"auc\": 0.9988, \"p\": 0}, \"1v2\": {\"auc\": 0.961, \"p\": 0}, \"2v3\": {\"auc\": 0.8919, \"p\": 0.998}, \"3v4\": {\"auc\": 0.8762, \"p\": 1}}}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/olmo_retrain_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/olmo_retrain_chain\", \"completed_at\": \"2026-05-20T14:57:53.008Z\"}, \"exp_7b_scorer_arxiv\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:33:38.614Z\", \"updated_at\": \"2026-05-20T13:27:43.350Z\", \"hypothesis\": \"Qwen2.5-7B scorer yields same K*=3 as Qwen2.5-1.5B scorer on arXiv depth chains, confirming K* is robust to scorer scale across domains (C4 + arXiv).\", \"parent\": \"exp_024_arxiv_domain\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_arxiv.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_025_pythia_arxiv + /root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_olmo\", \"data_count\": 26400, \"model_name\": \"Qwen2.5-7B + Qwen2.5-1.5B-Instruct (scorers), Pythia-1.4B + OLMo-1B (generators)\", \"seed\": 42, \"checkpoint_source\": \"pretrained (Qwen2.5-7B, Qwen2.5-1.5B-Instruct)\", \"eval_data\": \"arXiv depth chains (Pythia-1.4B + OLMo-1B, depth 0-5, 2200 samples/depth)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T13:24:06.236Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:24:08.238Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T13:24:11.891882+00:00\"}]}, \"metrics\": {\"pythia_arxiv_qwen1b5\": {\"k_star\": 3, \"0v1\": 0.9872, \"1v2\": 0.7938, \"2v3\": 0.6544}, \"olmo_arxiv_qwen1b5\": {\"k_star\": 1, \"0v1\": 0.9954, \"1v2\": 0.5182, \"2v3\": 0.4956}, \"pythia_arxiv_qwen7b\": {\"k_star\": 3, \"0v1\": 0.9844, \"1v2\": 0.7987, \"2v3\": 0.6551}, \"olmo_arxiv_qwen7b\": {\"k_star\": 1, \"0v1\": 0.9941, \"1v2\": 0.5089, \"2v3\": 0.492}, \"summary\": \"7B scorer and 1.5B scorer yield identical K* on arXiv: Pythia=3, OLMo=1. K* robust to 4.7x scorer scale increase across both C4 and arXiv domains.\"}}, \"exp_code_multi_source\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:30:38.921Z\", \"updated_at\": \"2026-05-20T13:12:41.350Z\", \"hypothesis\": \"Code domain multi-source OBD K* preserves single-source ceiling K*=2 when mixing 3 generators (Qwen-7B, LLaMA-8B, Mistral-7B) with unified Qwen2.5-1.5B scorer.\", \"spec\": {\"command\": \"python /root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_code.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_{qwen7b,llama8b,mistral7b}\", \"data_count\": 99000, \"model_name\": \"Qwen2.5-1.5B (scorer)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/data/code_multi_source/\"}, \"metrics\": {\"k_star\": 2, \"generators\": [\"qwen7b\", \"llama8b\", \"mistral7b\"], \"unified_scorer\": \"qwen2.5-1.5b\", \"vocab_only_no_label\": {\"0v1\": 0.7891, \"1v2\": 0.6353, \"2v3\": 0.5121, \"kstar\": 2}, \"vocab_only_with_label\": {\"0v1\": 0.79, \"1v2\": 0.644, \"2v3\": 0.5118, \"kstar\": 2}, \"unified_no_label\": {\"0v1\": 0.9123, \"1v2\": 0.6702, \"2v3\": 0.5013, \"kstar\": 2}, \"unified_with_label\": {\"0v1\": 0.9123, \"1v2\": 0.6803, \"2v3\": 0.5055, \"kstar\": 2}, \"elapsed_seconds\": 2025, \"note\": \"Code multi-source K*=2 matches single-source ceiling across all 4 settings.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:12:41.350Z\"}, \"exp_wiki_multi_source\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:31:50.277Z\", \"updated_at\": \"2026-05-20T13:12:39.770Z\", \"hypothesis\": \"Wiki domain multi-source OBD K* preserves single-source ceiling when mixing 3 generators (Qwen1.5B, LLaMA-8B, Mistral-7B) with unified Qwen2.5-1.5B scorer, consistent with C4 multi-source K*=2 and arXiv multi-source K*=3.\", \"spec\": {\"command\": \"python /root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_wiki.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki,exp_wiki_llama8b,exp_wiki_mistral7b\", \"data_count\": 90000, \"model_name\": \"Qwen2.5-1.5B (scorer)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/data/wiki_multi_source/\"}, \"metrics\": {\"k_star\": 1, \"generators\": [\"qwen1b5\", \"llama8b\", \"mistral7b\"], \"docs_per_generator\": 1000, \"total_rows\": 18000, \"unified_scorer\": \"qwen2.5-1.5b\", \"vocab_only_no_label\": {\"0v1\": 0.7616, \"1v2\": 0.5434, \"2v3\": 0.517, \"kstar\": 1}, \"vocab_only_with_label\": {\"0v1\": 0.7779, \"1v2\": 0.552, \"2v3\": 0.5248, \"kstar\": 1}, \"unified_no_label\": {\"0v1\": 0.9603, \"1v2\": 0.5685, \"2v3\": 0.519, \"kstar\": 1}, \"unified_with_label\": {\"0v1\": 0.9685, \"1v2\": 0.579, \"2v3\": 0.5299, \"kstar\": 1}, \"elapsed_seconds\": 3499, \"note\": \"All 3 generators (qwen1b5/llama8b/mistral7b) participated. K*=1 consistent with cross-scorer single-source results (llama8b K*=1, mistral7b K*=1, qwen K*=2). Mixed pool pulled to K*=1 by majority.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:12:39.770Z\"}, \"exp_7b_scorer_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:37:17.489Z\", \"updated_at\": \"2026-05-20T12:53:09.873Z\", \"hypothesis\": \"Qwen2.5-7B scorer yields same K* as Qwen2.5-1.5B scorer on C4 Pythia-1.4B and OLMo-1B depth chains, confirming K* is robust to scorer scale (4.7x parameter increase).\", \"parent\": \"exp_022_cross_scorer\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True CUDA_VISIBLE_DEVICES=0 python /root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_ablation.py'\", \"server\": \"cqa1-22115\", \"data_path\": \"data_exp020_pythia_greedy + data/olmo_c4_cont\", \"data_count\": 60000, \"model_name\": \"Qwen2.5-7B + Qwen2.5-1.5B-Instruct (scorers)\", \"seed\": 42, \"checkpoint_source\": \"exp_022_cross_scorer (Pythia C4 + OLMo C4 depth chain data)\", \"eval_data\": \"C4 depth 0-5 from Pythia-1.4B and OLMo-1B generators\"}, \"metrics\": {\"pythia_c4__qwen1.5b\": {\"k_star\": 2, \"1v2_auc\": 0.8928, \"1v2_ci\": [0.8865, 0.8989]}, \"olmo_c4__qwen1.5b\": {\"k_star\": 1, \"1v2_auc\": 0.4977, \"1v2_ci\": [0.4865, 0.509]}, \"pythia_c4__qwen7b\": {\"k_star\": 2, \"1v2_auc\": 0.8943, \"1v2_ci\": [0.8881, 0.9005]}, \"olmo_c4__qwen7b\": {\"k_star\": 1, \"1v2_auc\": 0.4965, \"1v2_ci\": [0.485, 0.5078]}, \"match\": \"pythia K*(1.5B)=2 == K*(7B)=2; olmo K*(1.5B)=1 == K*(7B)=1\"}, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_7b_scorer_ablation.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_7b_scorer_ablation/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:53:09.873Z\"}, \"exp_bootstrap_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:51:15.538Z\", \"updated_at\": \"2026-05-20T11:57:24.167Z\", \"hypothesis\": \"10K bootstrap resamples yield tighter CI but no K* verdict flips for borderline Table 2 configurations (LLaMA-8B, Gemma-2-2B, Mistral-7B, 512-tok), confirming robustness of K* assignments at 1K resamples.\", \"spec\": {\"command\": \"python /root/autodl-tmp/gen-depth-contamination/scripts/run_bootstrap_10k.py\", \"server\": \"cqa1-22115\", \"data_path\": \"multiple (exp_018, exp_gemma2b, exp_019, exp_021_512)\", \"data_count\": 40000, \"model_name\": \"LightGBM (CPU-only bootstrap)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k/bootstrap_10k_comparison.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k_log.txt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T11:56:15.385Z\", \"metrics\": {\"configs_tested\": 4, \"configs_missing\": 2, \"results\": {\"llama8b\": {\"auc\": 0.6075, \"ci_1k\": [0.597, 0.617], \"ci_10k\": [0.598, 0.617], \"verdict_1k\": \"BORDERLINE\", \"verdict_10k\": \"BORDERLINE\", \"flipped\": false}, \"gemma2b\": {\"auc\": 0.5981, \"ci_1k\": [0.588, 0.608], \"ci_10k\": [0.588, 0.608], \"verdict_1k\": \"BORDERLINE\", \"verdict_10k\": \"BORDERLINE\", \"flipped\": false}, \"mistral7b\": {\"auc\": 0.5902, \"ci_1k\": [0.58, 0.6], \"ci_10k\": [0.58, 0.6], \"verdict_1k\": \"K*=1\", \"verdict_10k\": \"BORDERLINE\", \"flipped_technical\": true, \"note\": \"CI upper 0.6000→0.6001 (noise, +0.01pp). Point estimate 0.5902 << theta. K*=1 unchanged.\"}, \"512tok\": {\"auc\": 0.6136, \"ci_1k\": [0.604, 0.623], \"ci_10k\": [0.604, 0.623], \"verdict_1k\": \"K*=2\", \"verdict_10k\": \"K*=2\", \"flipped\": false}}, \"missing\": [\"exp_017_qwen_cont (features.csv not on disk)\", \"exp_002_olmo (features.csv not on disk)\"], \"conclusion\": \"No substantive K* flips. 10K CI ~3% tighter. 1K resamples confirmed robust.\"}}, \"exp-014\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:28:44.076Z\", \"updated_at\": \"2026-05-20T11:36:17.784Z\", \"spec\": {\"command\": \"python run_naturalistic_validation.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv\", \"data_count\": 30000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_014_naturalistic/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_014_naturalistic/naturalistic_validation_results.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"OBD depth classifiers trained on synthetic generation-chain data will assign low depth (d0) to most real Common Crawl texts, and predicted AI probability will correlate negatively with vocabulary richness metrics (freq_entropy, TTR), confirming that the 15D feature space captures genuine human-vs-synthetic distributional differences rather than overfitting to synthetic artifacts.\", \"completed_at\": \"2026-05-20T11:29:09.930Z\", \"metrics\": {\"superseded_by\": \"exp_014_naturalistic\", \"note\": \"Stale duplicate. All metrics and results are in exp_014_naturalistic.\"}}, \"exp_gemma2b_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:20:08.546Z\", \"updated_at\": \"2026-05-20T10:07:22.035Z\", \"hypothesis\": \"Gemma-2-2B (6th architecture family) yields K*=2 on C4 web text under continuation mode, consistent with domain ceiling K*=2 observed across 5 other families (Qwen/Pythia/OLMo/LLaMA/Mistral), strengthening the claim that C4 ceiling is architecture-independent.\", \"spec\": {\"command\": \"python /root/autodl-tmp/gen-depth-contamination/scripts/run_gemma2b_depth.py\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": 289968, \"log_path\": \"~/runs/gen-depth-contamination/exp_gemma2b_depth.log\", \"submitted_at\": \"2026-05-20T06:34:42.871Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:0\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/c4_5k\", \"data_count\": 5000, \"model_name\": \"google/gemma-2-2b\", \"seed\": 42, \"wall_clock_seconds\": 11141.9, \"gpu_hours\": 3.09}, \"reproduce\": {\"finished_at\": \"2026-05-20T09:38:23.991Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T09:38:28.803849+00:00\"}]}, \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9534, \"1v2\": 0.5981, \"2v3\": 0.5342, \"3v4\": 0.503, \"4v5\": 0.5026}, \"pairwise_auc_std\": {\"0v1\": 0.003, \"1v2\": 0.008, \"2v3\": 0.013, \"3v4\": 0.003, \"4v5\": 0.013}, \"bootstrap_ci_1v2\": {\"ci_lower\": 0.5882, \"ci_upper\": 0.6076}, \"jsd\": {\"0v1\": 0.09882, \"1v2\": 0.008852, \"2v3\": 0.004904, \"3v4\": 0.003742, \"4v5\": 0.003167}, \"ordinal_mae\": 1.3152, \"ordinal_accuracy\": 0.3321, \"note\": \"K*=1, NOT borderline K*=2. 1v2 AUC=0.5981 < theta=0.60. CI upper=0.6076 crosses theta but point estimate below.\"}, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_depth/summary.txt\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_depth/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T09:40:24.773Z\"}, \"exp_deberta_code_qwen1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:34:21.140Z\", \"updated_at\": \"2026-05-20T09:43:22.944Z\", \"hypothesis\": \"DeBERTa supervised classifier on Code domain yields K*=2 (matching OBD K*=2), confirming representation-independent domain ceiling holds for Code domain (C4 K*=2, wiki K*=3, arXiv K*=3, code K*=2).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python /root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_code.py\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"294849\", \"log_path\": \"~/runs/gen-depth-contamination/exp_deberta_code_qwen1b5.log\", \"submitted_at\": \"2026-05-20T07:33:30.520Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7792.4, \"gpu_hours\": 2.16}, \"reproduce\": {\"finished_at\": \"2026-05-20T09:20:38.702Z\"}, \"metrics\": {\"K_star\": 2, \"theta\": 0.6, \"auc_0v1\": 1, \"auc_1v2\": 0.8076, \"auc_2v3\": 0.5933, \"auc_3v4\": 0.5492, \"auc_4v5\": 0.5311, \"ci_0v1\": [0.9999, 1], \"ci_1v2\": [0.8001, 0.8147], \"ci_2v3\": [0.5847, 0.6018], \"ci_3v4\": [0.541, 0.5573], \"ci_4v5\": [0.5235, 0.5388], \"obd_auc_0v1\": 0.9388, \"obd_auc_1v2\": 0.7382, \"obd_auc_2v3\": 0.53, \"obd_auc_3v4\": 0.5022, \"obd_auc_4v5\": 0.5219, \"elapsed_seconds\": 5780}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_code_qwen1b5/code_qwen1b5.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_deberta_code_qwen1b5.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:43:22.944Z\"}, \"exp_multi_source_arxiv\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:46:18.107Z\", \"updated_at\": \"2026-05-20T08:47:00.705Z\", \"hypothesis\": \"Multi-source OBD K* on arXiv domain preserves domain ceiling K*=3 when mixing 3 generators (Qwen/Pythia/LLaMA-8B) with unified Qwen2.5-1.5B scorer, consistent with single-source arXiv K*=3 and higher than C4 multi-source K*=2, confirming domain hierarchy in multi-source setting.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python scripts/run_multi_source_arxiv.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_024_arxiv + data/exp_025_pythia_arxiv + data/exp_arXiv_llama8b\", \"data_count\": 19800, \"model_name\": \"OBD-LightGBM-15D\", \"seed\": 42, \"checkpoint_path\": \"results/exp_multi_source_arxiv/\", \"log_path\": \"results/exp_multi_source_arxiv/summary.json\"}, \"completed_at\": \"2026-05-20T08:46:51.345Z\", \"metrics\": {\"domain\": \"arxiv\", \"generators\": [\"qwen1b5\", \"pythia1b4\", \"llama8b\"], \"unified_scorer\": \"qwen2.5-1.5b\", \"docs_per_generator\": 1000, \"vocab_only_no_label_0v1\": 0.9431, \"vocab_only_no_label_1v2\": 0.6922, \"vocab_only_no_label_2v3\": 0.589, \"vocab_only_no_label_kstar\": 2, \"vocab_only_with_label_0v1\": 0.9436, \"vocab_only_with_label_1v2\": 0.702, \"vocab_only_with_label_2v3\": 0.5883, \"vocab_only_with_label_kstar\": 2, \"unified_no_label_0v1\": 0.9899, \"unified_no_label_1v2\": 0.8117, \"unified_no_label_2v3\": 0.6247, \"unified_no_label_3v4\": 0.5269, \"unified_no_label_kstar\": 3, \"unified_with_label_0v1\": 0.9911, \"unified_with_label_1v2\": 0.8338, \"unified_with_label_2v3\": 0.6276, \"unified_with_label_2v3_ci\": [0.615, 0.6401], \"unified_with_label_3v4\": 0.533, \"unified_with_label_kstar\": 3}}, \"exp_multi_source_detection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:20:10.182Z\", \"updated_at\": \"2026-05-20T08:00:14.527Z\", \"hypothesis\": \"OBD K* is preserved when training on a mixed pool of outputs from 3 different generators (Qwen-1.5B, Pythia-1.4B, OLMo-1B), and adding generator identity as an extra feature does not improve depth discrimination.\", \"spec\": {\"command\": \"python scripts/run_multi_source.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data_exp016_qwen_base + data_exp020_pythia_greedy + data/olmo_c4_cont\", \"data_count\": 18000, \"model_name\": \"OBD-LightGBM-15D\", \"seed\": 42, \"checkpoint_path\": \"results/exp_multi_source_detection/\", \"log_path\": \"/tmp/multi_source.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T07:01:21.517Z\", \"metrics\": {\"v2_generators\": [\"qwen1b5\", \"pythia1b4\", \"llama8b\"], \"v2_kstar_no_label\": 2, \"v2_kstar_with_label\": 2, \"v2_0v1_auc_no_label\": 0.968, \"v2_0v1_auc_with_label\": 0.9785, \"v2_1v2_auc_no_label\": 0.7144, \"v2_1v2_auc_with_label\": 0.7251, \"v2_2v3_auc_no_label\": 0.5321, \"v2_2v3_auc_with_label\": 0.5362, \"vocab_only_v1_0v1\": 0.8675, \"vocab_only_v1_1v2\": 0.676, \"vocab_only_v1_2v3\": 0.4938, \"vocab_only_v1_kstar\": 2, \"vocab_only_v2_0v1\": 0.8296, \"vocab_only_v2_1v2\": 0.683, \"vocab_only_v2_2v3\": 0.5057, \"vocab_only_v2_kstar\": 2, \"vocab_only_features\": [\"ttr\", \"hapax_ratio\", \"self_bleu\", \"freq_kurtosis\", \"freq_entropy\", \"low_freq_ratio\"], \"scorer_confound_affects_kstar\": false, \"unified_scorer\": \"qwen2.5-1.5b\", \"unified_no_label_0v1\": 0.9663, \"unified_no_label_1v2\": 0.7105, \"unified_no_label_2v3\": 0.519, \"unified_no_label_kstar\": 2, \"unified_with_label_0v1\": 0.9769, \"unified_with_label_1v2\": 0.7183, \"unified_with_label_2v3\": 0.5165, \"unified_with_label_kstar\": 2, \"unified_single_qwen_kstar\": 2, \"unified_single_pythia_kstar\": 2, \"unified_single_llama8b_kstar\": 1, \"unified_single_qwen_1v2\": 0.6306, \"unified_single_pythia_1v2\": 0.8806, \"unified_single_llama8b_1v2\": 0.6077}}, \"exp_changepoint_kstar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:20:11.788Z\", \"updated_at\": \"2026-05-20T07:21:14.637Z\", \"hypothesis\": \"Non-parametric changepoint detection (PELT) on pairwise AUC sequences should recover K* consistent with the fixed θ=0.60 threshold, validating that K* is not an artifact of threshold choice.\", \"spec\": {\"command\": \"python scripts/run_changepoint_kstar.py\", \"server\": \"cqa1-22115\", \"data_path\": \"results/*/pairwise_auc.json\", \"data_count\": 37, \"model_name\": \"ruptures-PELT\", \"seed\": 42, \"checkpoint_path\": \"results/exp_changepoint_kstar/\", \"log_path\": \"/tmp/changepoint_run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"exact_agreement\": 0.459, \"exact_agreement_n\": \"17/37\", \"within_1_agreement\": 0.946, \"within_1_agreement_n\": \"35/37\", \"cp_direction\": \"always_conservative\", \"disagreement_auc_range\": [0.607, 0.654], \"best_penalty\": 0.1, \"methods_tested\": [\"PELT\", \"BinSeg\", \"BottomUp\"], \"bootstrap_samples\": 2000}, \"completed_at\": \"2026-05-20T07:19:41.765Z\"}, \"exp_cross_transfer_llama8b_to_qwen7b_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:01:09.441Z\", \"updated_at\": \"2026-05-20T05:28:46.650Z\", \"spec\": {\"command\": \"python scripts/run_deberta_cross_transfer.py --train_model wiki_llama8b --test_model wiki_qwen7b --gpu 0\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"275361\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_llama8b_to_qwen7b_v2.log\", \"submitted_at\": \"2026-05-20T03:01:08.673Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/wiki_llama8b/ + wiki_qwen7b/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"checkpoint_source\": \"trained from scratch (cross-transfer rerun of crashed v1)\", \"eval_data\": \"wiki_qwen7b depth 0-5, 20000 samples\", \"checkpoint_path\": \"N/A (OOF predictions only)\", \"wall_clock_seconds\": 8858.0, \"gpu_hours\": 2.46}, \"hypothesis\": \"Cross-model transfer: DeBERTa trained on LLaMA-8B wiki depth data can discriminate Qwen-7B wiki depth boundaries (K* transfer). Rerun of exp_cross_transfer_llama8b_to_qwen7b which crashed due to --gpu 1 device error.\", \"parent\": \"exp_cross_transfer_llama8b_to_qwen7b\", \"conclusion\": \"success\", \"metrics\": {\"K_star\": 3, \"2v3_auc_ci_lower\": 0.6124, \"theta\": 0.6, \"margin_pp\": 1.24}, \"completed_at\": \"2026-05-20T05:28:46.650Z\"}, \"exp_deberta_arxiv_qwen1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:12:10.106Z\", \"updated_at\": \"2026-05-20T03:50:38.093Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python scripts/run_deberta_arxiv.py\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"276481\", \"log_path\": \"~/runs/gen-depth-contamination/exp_deberta_arxiv_qwen1b5.log\", \"submitted_at\": \"2026-05-20T03:12:09.627Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_024_arxiv/\", \"data_count\": 13200, \"model_name\": \"DeBERTa-v3-base\", \"seed\": \"5-fold GroupKFold\", \"hyperparams\": {\"epochs\": 3, \"batch_size\": 16, \"grad_accum\": 2, \"lr\": \"2e-5\", \"n_boot\": 10000, \"threshold\": 0.6}, \"checkpoint_path\": \"N/A (OOF predictions only)\", \"wall_clock_seconds\": 2247.8, \"gpu_hours\": 0.62}, \"hypothesis\": \"DeBERTa supervised classifier on arXiv domain yields K*=3 (matching OBD K*=3), confirming representation-independent domain ceiling holds across all 4 domains (C4 K*=2, wiki K*=3, code K*=2, arXiv K*=3).\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:45:52.617Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T03:45:57.340301+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 4, \"0v1_auc\": 0.9997, \"1v2_auc\": 0.9214, \"2v3_auc\": 0.7446, \"3v4_auc\": 0.6238, \"4v5_auc\": 0.5771, \"3v4_ci_lower\": 0.6127, \"3v4_ci_upper\": 0.6349, \"theta\": 0.6}, \"completed_at\": \"2026-05-20T03:49:37.411Z\"}, \"exp_cross_transfer_llama8b_to_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:55:51.478Z\", \"updated_at\": \"2026-05-20T03:00:13.595Z\", \"spec\": {\"command\": \"python scripts/run_deberta_cross_transfer.py --train_model wiki_llama8b --test_model wiki_qwen7b --gpu 1\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"270133\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_llama8b_to_qwen7b.log\", \"submitted_at\": \"2026-05-20T00:55:51.062Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/wiki_llama8b/ + wiki_qwen7b/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"wall_clock_seconds\": 7462.5, \"gpu_hours\": 2.07}, \"hypothesis\": \"Cross-model transfer: DeBERTa trained on LLaMA-8B wiki depth data can discriminate Qwen-7B wiki depth boundaries (K* transfer), testing whether depth features are model-agnostic within wiki domain.\", \"conclusion\": \"failed\", \"failure_reason\": \"AssertionError: Invalid device id — --gpu 1 used but CUDA_VISIBLE_DEVICES only exposed 1 device. Need --gpu 0.\", \"checkpoint_path\": \"N/A - crashed before producing output\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_llama8b_to_qwen7b.log\", \"completed_at\": \"2026-05-20T03:00:13.596Z\"}, \"exp_cross_transfer_qwen7b_to_llama8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:55:49.779Z\", \"updated_at\": \"2026-05-20T02:59:59.419Z\", \"spec\": {\"command\": \"python scripts/run_deberta_cross_transfer.py --train_model wiki_qwen7b --test_model wiki_llama8b --gpu 0\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"270054\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_qwen7b_to_llama8b.log\", \"submitted_at\": \"2026-05-20T00:55:49.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/wiki_qwen7b/ + wiki_llama8b/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"wall_clock_seconds\": 7450.1, \"gpu_hours\": 2.07}, \"hypothesis\": \"Cross-model transfer: DeBERTa trained on Qwen-7B wiki depth data can discriminate LLaMA-8B wiki depth boundaries (K* transfer), testing whether depth features are model-agnostic within wiki domain.\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/wiki_qwen7b__to__wiki_llama8b.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_qwen7b_to_llama8b.log\", \"metrics\": {\"kstar\": 3, \"kstar_indexing\": \"1-indexed\", \"pairwise_auc\": {\"0v1\": 0.9998, \"1v2\": 0.7384, \"2v3\": 0.6278, \"3v4\": 0.587, \"4v5\": 0.5519}, \"elapsed_s\": 3621}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T02:59:59.419Z\"}, \"exp_deberta_cross_transfer_gpu3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:45:58.698Z\", \"updated_at\": \"2026-05-20T00:52:16.950Z\", \"hypothesis\": \"Sub-experiment of exp_deberta_cross_transfer_wiki: GPU3 ran olmo↔llama8b, pythia↔mistral7b pairs (mistral7b pairs were bonus, qwen7b↔llama8b missing).\", \"conclusion\": \"success\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"command\": \"python scripts/run_deberta_cross_transfer.py\", \"pid\": \"208308\", \"data_path\": \"/root/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/gpu3.log\", \"reproduce\": {\"finished_at\": \"2026-05-20T00:50:30.198Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-20T00:50:32.377Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T00:50:36.649085+00:00\"}]}}, \"exp_deberta_cross_transfer_gpu2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:45:57.106Z\", \"updated_at\": \"2026-05-20T00:52:16.211Z\", \"hypothesis\": \"Sub-experiment of exp_deberta_cross_transfer_wiki: GPU2 ran olmo↔qwen7b, pythia→llama8b, llama8b→pythia pairs.\", \"conclusion\": \"success\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"command\": \"python scripts/run_deberta_cross_transfer.py\", \"pid\": \"208307\", \"data_path\": \"/root/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/gpu2.log\", \"reproduce\": {\"finished_at\": \"2026-05-20T00:50:20.459Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-20T00:50:22.410Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T00:50:27.489708+00:00\"}]}}, \"exp_deberta_cross_transfer_gpu1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:45:55.753Z\", \"updated_at\": \"2026-05-20T00:52:15.283Z\", \"hypothesis\": \"Sub-experiment of exp_deberta_cross_transfer_wiki: GPU1 ran pythia↔olmo and pythia↔qwen7b pairs.\", \"conclusion\": \"success\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"command\": \"python scripts/run_deberta_cross_transfer.py\", \"pid\": \"208306\", \"data_path\": \"/root/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/gpu1.log\", \"reproduce\": {\"finished_at\": \"2026-05-20T00:50:07.180Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-20T00:50:09.496Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T00:50:17.409046+00:00\"}]}}, \"exp_deberta_cross_transfer_wiki\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:23:41.514Z\", \"updated_at\": \"2026-05-20T00:45:03.982Z\", \"hypothesis\": \"DeBERTa cross-model transfer on wiki domain: if off-diagonal retention is high (>90%), depth signals are model-family invariant even with neural features; if wiki retention exceeds C4 retention, domain complexity affects transfer more than feature representation.\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\", \"cuda:2\", \"cuda:3\"], \"command\": \"python scripts/run_deberta_cross_transfer.py --all_pairs\", \"pid\": \"208306,208307,208308\", \"data_path\": \"/root/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"total_pairs_expected\": 12, \"completed_pairs\": 10, \"missing_pairs\": [\"qwen7b→llama8b\", \"llama8b→qwen7b\"], \"bonus_pairs\": [\"pythia→mistral7b (K*=2)\", \"mistral7b→pythia (K*=2)\"], \"kstar_distribution\": {\"K*=1\": 3, \"K*=2\": 5, \"K*=3\": 1}, \"kstar_1_pairs\": [\"pythia→olmo\", \"qwen7b→olmo\", \"llama8b→olmo\"], \"kstar_3_pair\": \"pythia→qwen7b\", \"kstar_2_pairs\": [\"olmo→qwen7b\", \"olmo→llama8b\", \"qwen7b→pythia\", \"llama8b→pythia\", \"pythia→llama8b\"], \"pattern\": \"All X→OLMo = K*=1. pythia→qwen7b highest at K*=3. GPU3 ran mistral7b pairs instead of expected qwen7b↔llama8b, causing 2 missing pairs.\", \"json_kstar_fix\": \"3 JSONs fixed +1 (pythia→olmo 0→1, olmo→qwen7b 1→2, olmo→llama8b 1→2)\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"completed_at\": \"2026-05-20T00:44:09.679Z\"}, \"exp_deberta_c4_1b5_qwen_cont\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:14:07.803Z\", \"updated_at\": \"2026-05-20T00:43:44.526Z\", \"hypothesis\": \"C4 1.5B DeBERTa qwen_cont256 config (length-256 continuation): if K*=2, confirms boundary holds across generation strategies (base vs continuation) at 1.5B scale.\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"command\": \"python scripts/run_deberta_c4_1b5.py --config qwen_cont256 --gpu 0\", \"pid\": \"TBD\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_021_length_256/\", \"data_count\": 30000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4_1b5/qwen_cont256_oof.npz\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/deberta_c4_1b5_qwen_cont.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T00:41:45.752Z\", \"metrics\": {\"config\": \"qwen_cont256\", \"kstar\": 2, \"kstar_theta\": 0.6, \"pairwise_auc\": {\"0v1\": 0.9955, \"1v2\": 0.7194, \"2v3\": 0.5954, \"3v4\": 0.5689, \"4v5\": 0.5502}, \"ci_95\": {\"0v1\": [0.9944, 0.9965], \"1v2\": [0.712, 0.7273], \"2v3\": [0.587, 0.6028], \"3v4\": [0.5613, 0.5766], \"4v5\": [0.5431, 0.5577]}, \"obd_baseline\": {\"0v1\": 0.9914, \"1v2\": 0.6282, \"2v3\": 0.5556, \"3v4\": 0.5298, \"4v5\": 0.5137}, \"delta_vs_obd\": {\"1v2\": 0.0912}, \"key_finding\": \"C4 1.5B qwen_cont256 K*=2, boundary holds across continuation generation strategy.\"}}, \"exp_deberta_c4_1b5_pythia\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:14:05.964Z\", \"updated_at\": \"2026-05-20T00:19:10.196Z\", \"hypothesis\": \"C4 1.5B DeBERTa pythia_greedy config: apple-to-apple comparison with OBD Table 2. If K*=2 consistent with qwen_rw, confirms boundary is generator-invariant at 1.5B scale on C4.\", \"spec\": {\"server\": \"westd-42896\", \"gpu\": [\"cuda:1\"], \"command\": \"python scripts/run_deberta_c4_1b5.py --config pythia_greedy --gpu 1\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp020_pythia_greedy/\", \"data_count\": 30000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"checkpoint_path\": \"n/a\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4_1b5/pythia_greedy.json\"}, \"metrics\": {\"config\": \"pythia_greedy\", \"kstar\": 2, \"kstar_theta\": 0.6, \"pairwise_auc\": {\"0v1\": 0.9998, \"1v2\": 0.9284, \"2v3\": 0.5419, \"3v4\": 0.5163, \"4v5\": 0.5098}, \"ci_95\": {\"0v1\": [0.9996, 0.9999], \"1v2\": [0.923, 0.9331], \"2v3\": [0.5354, 0.5486], \"3v4\": [0.509, 0.5237], \"4v5\": [0.5037, 0.516]}, \"obd_baseline\": {\"0v1\": 0.9992, \"1v2\": 0.8838, \"2v3\": 0.5342, \"3v4\": 0.5228, \"4v5\": 0.5162}, \"delta_vs_obd_1v2\": 0.0446, \"training_time_min\": 37.3}, \"conclusion\": \"success\", \"notes\": \"C4 1.5B DeBERTa pythia_greedy K*=2, consistent with qwen_rw K*=2. 1v2 AUC=0.9284 far exceeds OBD 0.8838 (+4.5pp), but 2v3=0.5419 still below θ=0.60, boundary unchanged. Notably pythia_greedy 1v2 much higher than qwen_rw (0.9284 vs 0.7052), likely due to greedy decoding being more distinguishable. OBD baseline also higher for pythia_greedy (0.8838 vs 0.6262). Results on westd-42896.\", \"completed_at\": \"2026-05-20T00:19:10.196Z\"}, \"exp_32b_c4_6class\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:31:06.464Z\", \"updated_at\": \"2026-05-20T00:15:44.463Z\", \"hypothesis\": \"32B DeBERTa 6-class rerun (depth 0-5) to fill 4v5 pair in paper table. If K* remains 2, confirms boundary even with full depth range; 4v5 AUC provides additional evidence of signal decay pattern.\", \"spec\": {\"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"command\": \"python run_deberta_6class.py --config exp_32b_c4\", \"pid\": \"139848\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/c4_32b\", \"data_count\": 30000, \"model_name\": \"microsoft/deberta-v3-base\", \"seed\": 42, \"note\": \"6-class rerun replacing 5-class exp_32b_c4, adds depth_5 for complete 4v5 pair\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4/exp_32b_c4_oof.npz\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/deberta_32b_6class.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T23:34:30.974Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:34:32.906Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:34:36.421721+00:00\"}]}, \"metrics\": {\"config\": \"exp_32b_c4\", \"kstar\": 2, \"kstar_indexing\": \"1-indexed\", \"num_classes\": 6, \"pairwise_auc\": {\"0v1\": 0.9923, \"1v2\": 0.6945, \"2v3\": 0.5978, \"3v4\": 0.5669, \"4v5\": 0.5426}, \"ci_95\": {\"0v1\": [0.991, 0.9936], \"1v2\": [0.6864, 0.7026], \"2v3\": [0.5898, 0.6058], \"3v4\": [0.559, 0.5746], \"4v5\": [0.5351, 0.5501]}, \"training_time_min\": 48.2}, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/deberta_32b_6class.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4/exp_32b_c4_results.json\", \"notes\": \"Cron 误判为 failed（脚本不用 W&B），实际 5-fold 训练全部完成。K*=2 confirmed with 6 classes (depth 0-5)。2v3 AUC=0.5978 刚好低于 θ=0.60。4v5 AUC=0.5426 提供 signal decay 额外证据。\"}, \"exp_deberta_c4_1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:23:40.169Z\", \"updated_at\": \"2026-05-19T23:42:16.799Z\", \"hypothesis\": \"C4 1.5B DeBERTa apple-to-apple comparison with Table 2 OBD results: if DeBERTa K*=2 on same 1.5B C4 data as OBD, confirms boundary is intrinsic; if K*>2, quantifies neural vs handcrafted gap at 1.5B scale.\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-contamination && python scripts/run_deberta_c4_1b5.py --config qwen_rw --gpu 0\", \"pid\": \"255066\", \"data_path\": \"/root/gen-depth-contamination/data/exp016_qwen_base/\", \"data_count\": \"TBD\", \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"metrics\": {\"config\": \"qwen_rw\", \"kstar\": 2, \"kstar_theta\": 0.6, \"pairwise_auc\": {\"0v1\": 0.9923, \"1v2\": 0.7052, \"2v3\": 0.5988, \"3v4\": 0.5698, \"4v5\": 0.5475}, \"ci_95\": {\"0v1\": [0.9907, 0.9937], \"1v2\": [0.6977, 0.7129], \"2v3\": [0.5905, 0.6063], \"3v4\": [0.5626, 0.5774], \"4v5\": [0.5404, 0.5542]}, \"obd_baseline\": {\"0v1\": 0.987, \"1v2\": 0.6262, \"2v3\": 0.5496, \"3v4\": 0.5294, \"4v5\": 0.5182}, \"delta_vs_obd\": {\"1v2\": 0.079}, \"key_finding\": \"C4 1.5B DeBERTa qwen_rw K*=2, matching OBD K*=2. DeBERTa 1v2 +7.9pp vs OBD but does not extend K*. Note: only qwen_rw config done; pythia_greedy running on westd, qwen_cont256 starting on cqa1.\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T23:12:26.218Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:12:26.966Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:12:34.928421+00:00\"}]}, \"notes\": \"Cron 误判为 failed（脚本不用 W&B），实际完成。K*=2 confirmed on C4 1.5B data = OBD K*=2。DeBERTa 1v2 AUC=0.7052 vs OBD 0.6262 (+7.9pp)，但 2v3 仍低于 θ=0.60，无法突破 K* boundary。confirms intrinsic boundary on C4.\"}, \"exp_deberta_upperbound\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:29:11.448Z\", \"updated_at\": \"2026-05-19T22:05:28.928Z\", \"hypothesis\": \"DeBERTa-v3-base fine-tuned ordinal classifier as upper-bound baseline for 15D handcrafted features: if DeBERTa also yields K*=2 on C4 depth chains, the saturation boundary is near-intrinsic to generation process rather than a feature ceiling; if K*=3+, quantifies the gap between handcrafted and neural representations. Uses same 5-fold GroupKFold, pairwise AUC evaluation, θ=0.60 K* criterion.\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_deberta_upperbound.py\", \"pid\": \"167144\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_upperbound.log\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_upperbound/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_upperbound.log\", \"metrics\": {\"wiki_pythia\": {\"kstar\": 3, \"0v1_auc\": 0.9993, \"1v2_auc\": 0.725, \"2v3_auc\": 0.6137, \"3v4_auc\": 0.5733, \"4v5_auc\": 0.5527}, \"wiki_olmo\": {\"kstar\": 1, \"0v1_auc\": 0.9999, \"1v2_auc\": 0.5183, \"2v3_auc\": 0.5048, \"3v4_auc\": 0.5021, \"4v5_auc\": 0.4989}, \"wiki_qwen7b\": {\"kstar\": 3, \"0v1_auc\": 0.9998, \"1v2_auc\": 0.7619, \"2v3_auc\": 0.6108, \"3v4_auc\": 0.5587, \"4v5_auc\": 0.5412}, \"wiki_llama8b\": {\"kstar\": 3, \"0v1_auc\": 0.9997, \"1v2_auc\": 0.7452, \"2v3_auc\": 0.5954, \"3v4_auc\": 0.5601, \"4v5_auc\": 0.5389}, \"wiki_mistral7b\": {\"kstar\": 3, \"0v1_auc\": 0.9998, \"1v2_auc\": 0.7483, \"2v3_auc\": 0.5552, \"3v4_auc\": 0.5434, \"4v5_auc\": 0.5298}, \"obd_baseline_bug_fixed\": true, \"wiki_olmo_obd_rerun\": {\"0v1\": 0.9933, \"1v2\": 0.4983, \"2v3\": 0.5041, \"3v4\": 0.4986, \"4v5\": 0.5089}, \"key_finding\": \"Wiki DeBERTa K*=3 for 4/5 configs (pythia/qwen7b/llama8b/mistral7b), exceeding OBD K*=2. DeBERTa breaks OBD boundary on wiki domain. OLMo K*=1 anomalous (near-random 1v2). OBD baseline bug for olmo fixed (was copy of pythia).\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T21:58:49.707Z\"}, \"exp_32b_c4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:56:48.122Z\", \"updated_at\": \"2026-05-19T21:55:27.105Z\", \"hypothesis\": \"Scale-dependent K* on C4: Qwen2.5-32B fp16 continuation on C4 web text 的 K* 是否仍 = 2？验证 K*=2 dominant mode 在 32B scale 是否稳定（已确认 1.5B/7B/8B/14B 均 K*=2），排除 scale ceiling effect。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_arXiv_llama8b\", \"server\": \"westd-42896\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-42896\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T19:37:31.096Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-32B --data_dir data/exp_32b_c4 --results_dir results/exp_32b_c4 --num_samples 5000 --max_depth 5 --batch_size 2 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"finished_at\": \"2026-05-19T21:33:12.076Z\", \"training_hours\": 49.93}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-32B --data_dir data/exp_32b_c4 --results_dir results/exp_32b_c4 --num_samples 5000 --max_depth 5 --batch_size 2 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:1\"], \"pid\": \"44715\", \"log_path\": \"~/runs/gen-depth-contamination/exp_32b_c4.log\", \"submitted_at\": \"2026-05-18T07:04:19.556Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_32b_c4\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-32B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_32b_c4/\", \"wall_clock_seconds\": 139867.5, \"gpu_hours\": 38.85}, \"pid\": \"14637\", \"log_path\": \"~/runs/gen-depth-contamination/exp_32b_c4.log\", \"notes\": \"Resubmit #2 (2026-05-18T07:05): killed at depth 2 18% per Director, 72h timeout. depth 0-1 complete (5000 lines each), pipeline auto-skips. PID 44715 cuda:1.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T21:33:15.741057+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"lgbm_kstar\": 2, \"deberta_kstar\": 2, \"kstar_theta\": 0.6, \"scale\": \"32B\", \"domain\": \"C4\", \"n_docs\": 5000, \"max_depth\": 5, \"key_finding\": \"Qwen2.5-32B C4 K*=2, confirming scale-invariance of K*=2 dominant mode from 1.5B to 32B. Both LightGBM and DeBERTa classifiers agree on K*=2.\"}, \"completed_at\": \"2026-05-19T21:55:27.105Z\"}, \"exp_deberta_c4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T19:27:44.088Z\", \"updated_at\": \"2026-05-19T20:30:48.238Z\", \"hypothesis\": \"DeBERTa-v3-base fine-tuned on raw text provides an upper-bound for C4 depth distinguishability compared to 15D LightGBM on handcrafted features. Pairwise AUC should exceed LightGBM at all depth pairs since the model has access to full lexical/semantic signal.\", \"parent\": \"exp_deberta_upperbound\", \"spec\": {\"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HOME=/root/autodl-tmp/.hf_cache python scripts/run_deberta_c4.py\", \"pid\": \"130789\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 55000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4/train.log\", \"checkpoint_path\": \"results/exp_deberta_c4/\", \"checkpoint_source\": \"microsoft/deberta-v3-base (pretrained)\", \"eval_data\": \"C4 depth chains (exp_14b_c4: 30k, exp_32b_c4: 25k)\"}, \"conclusion\": \"success\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9941, \"1v2\": 0.6781, \"2v3\": 0.5895, \"3v4\": 0.5651, \"4v5\": 0.5485}, \"ci_95\": {\"0v1\": [0.993, 0.9951], \"1v2\": [0.6696, 0.6866], \"2v3\": [0.5814, 0.5979], \"3v4\": [0.5573, 0.5732], \"4v5\": [0.5411, 0.5562]}, \"f1_at_050\": {\"0v1\": 0.9352, \"1v2\": 0.6751, \"2v3\": 0.6607, \"3v4\": 0.6204, \"4v5\": 0.2869}, \"kstar\": 2, \"kstar_theta\": 0.6, \"config\": \"exp_14b_c4\", \"n_samples\": 30000, \"n_docs\": 5000, \"bootstrap_resamples\": 10000, \"training_time_min\": 48.3}, \"notes\": \"DeBERTa K*=2 = LightGBM K*=2 on C4 14B, confirming representation-independent boundary. 86M-param fine-tuned neural classifier cannot extend K* beyond 2. Worker script reported K*=1 (off-by-one bug in K* calculation logic), corrected to K*=2 based on raw CI data: 1v2 CI lower=0.6696 > θ=0.60.\", \"completed_at\": \"2026-05-19T20:30:48.238Z\"}, \"exp_code_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:30:13.401Z\", \"updated_at\": \"2026-05-19T12:15:37.664Z\", \"hypothesis\": \"Qwen2.5-7B code domain K* measurement: Qwen family scale invariance test on CodeSearchNet Python. Pythia Code K*=1 弱化了跨模型一致性。Qwen-7B 测试两个方向：(1) Qwen 家族内 Code 的 scale invariance（1.5B K*=2, 7B K*=?），(2) 若 LLaMA/Mistral 也 K*=1，Qwen-7B K*=2 能维持 \\\"code-competent models reach K*=2\\\" 叙事。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_code_pythia1b4\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate && HF_ENDPOINT=https://hf-mirror.com python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_code_qwen7b --results_dir results/exp_code_qwen7b --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"114228\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_qwen7b.log\", \"submitted_at\": \"2026-05-19T01:29:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_qwen7b\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"checkpoint_source\": \"exp_code_qwen1b5\", \"eval_data\": \"CodeSearchNet Python 5000 docs\", \"wall_clock_seconds\": 38608.5, \"gpu_hours\": 10.72}, \"notes\": \"Attempts 1-3 failed: huggingface.co unreachable (000), httpx client closed during datasets.load_dataset. Attempt 4 success: copied depth_0.jsonl from exp_code_qwen1b5 (MD5 match), set HF_ENDPOINT=https://hf-mirror.com. PID 114228, GPU util 96%, 15211/24564 MiB. nvidia-smi verified.\", \"reproduce\": {\"finished_at\": \"2026-05-19T12:12:26.097Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:12:28.503Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:12:31.991515+00:00\"}]}, \"metrics\": {\"pairwise_auc\": {\"0v1\": {\"mean\": 0.9051, \"ci95_half\": 0.0043, \"folds\": [0.9073, 0.9012, 0.912, 0.9049, 0.9003]}, \"1v2\": {\"mean\": 0.7276, \"ci95_half\": 0.0055, \"folds\": [0.7377, 0.7254, 0.724, 0.722, 0.7289]}, \"2v3\": {\"mean\": 0.5368, \"ci95_half\": 0.0145, \"folds\": [0.5179, 0.5332, 0.5275, 0.5462, 0.5593]}, \"3v4\": {\"mean\": 0.509, \"ci95_half\": 0.0055, \"folds\": [0.5029, 0.5054, 0.5085, 0.5092, 0.5191]}, \"4v5\": {\"mean\": 0.5139, \"ci95_half\": 0.0128, \"folds\": [0.5016, 0.5317, 0.5264, 0.509, 0.5007]}}, \"pairwise_jsd\": {\"0v1\": 0.061265, \"1v2\": 0.042256, \"2v3\": 0.00413, \"3v4\": 0.003198, \"4v5\": 0.003393}, \"k_star\": 2, \"ordinal\": {\"mae\": 1.2651, \"accuracy\": 0.3423}, \"top_features\": [{\"name\": \"freq_entropy\", \"importance\": 9730}, {\"name\": \"surp_d2_mean\", \"importance\": 9236.2}, {\"name\": \"surp_d1_mean\", \"importance\": 9126.2}, {\"name\": \"surp_d1_skew\", \"importance\": 8833.4}, {\"name\": \"surp_std\", \"importance\": 8110.2}, {\"name\": \"freq_kurtosis\", \"importance\": 7838.6}, {\"name\": \"surp_mean\", \"importance\": 7586}, {\"name\": \"surp_kurt\", \"importance\": 6769.2}, {\"name\": \"hapax_ratio\", \"importance\": 6636.4}, {\"name\": \"ttr\", \"importance\": 6332.6}]}}, \"exp_code_mistral7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:03:15.326Z\", \"updated_at\": \"2026-05-19T11:18:09.305Z\", \"hypothesis\": \"Mistral-7B code domain K* measurement: Mistral-7B-v0.3 continuation on CodeSearchNet Python subset. Mistral 是唯一展现极端 domain dependence 的模型（C4 K*=1, arXiv K*=3）。若 code K*=2（与 Qwen/LLaMA 一致）→ code K* domain-governed, Mistral one-wash 仅限 C4。若 code K*=1 → one-wash 是 model-intrinsic property for non-academic text。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_code_qwen1b5\", \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_code_mistral7b --results_dir results/exp_code_mistral7b --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"107037\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_mistral7b.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_mistral7b\", \"data_count\": 5000, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_source\": \"exp_code_qwen1b5\", \"eval_data\": \"CodeSearchNet Python 5000 docs\"}, \"notes\": \"Log writes to /dev/pts/3 (terminal session), not a file. Progress inferred from data dir: depth_1.jsonl done (5500 lines), depth_2 in progress. No persistent log file for post-mortem analysis.\", \"reproduce\": {\"finished_at\": \"2026-05-19T11:05:15.743Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed. Diagnostic worker dispatched to check logs, partial output, OOM/disk issues.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:05:15.059Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:05:21.025715+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_code_mistral7b/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_code_mistral7b/summary.txt\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9191, \"1v2\": 0.6152, \"2v3\": 0.5293, \"3v4\": 0.5286, \"4v5\": 0.5099}, \"pairwise_auc_ci\": {\"0v1\": 0.0017, \"1v2\": 0.012, \"2v3\": 0.0091, \"3v4\": 0.0104, \"4v5\": 0.006}, \"pairwise_jsd\": {\"0v1\": 0.046984, \"1v2\": 0.011845, \"2v3\": 0.003717, \"3v4\": 0.003206, \"4v5\": 0.003083}, \"ordinal_mae\": 1.3191, \"ordinal_accuracy\": 0.3243, \"top3_features\": [\"freq_entropy\", \"surp_d2_mean\", \"surp_d1_mean\"]}}, \"exp_code_llama8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:36:19.645Z\", \"updated_at\": \"2026-05-19T08:15:39.198Z\", \"hypothesis\": \"Code domain (Python) cross-model K* validation: LLaMA-3.1-8B continuation on CodeSearchNet Python subset (Husain et al. 2019). 验证 code domain K* 跨模型一致性（与 exp_code_qwen1b5 对比）。如果 K* 一致，确认 code domain K* 是 domain-governed 而非 model-specific。5500 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_code_qwen1b5\", \"notes\": \"Generation completed normally (11.37 GPU-hours). Analysis step crashed on M010 bug (int(doc_id) on string 'code_py_0'). Bug was already patched in code (try/except at line 462-466). Worker re-ran analysis only → K*=2 confirmed. Results in results/exp_code_llama8b/.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --data_dir data/exp_code_llama8b --results_dir results/exp_code_llama8b --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"96335\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_llama8b.log\", \"submitted_at\": \"2026-05-18T20:43:36.548Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/code_python_seed\", \"data_count\": 5000, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"exp_code_qwen1b5\", \"eval_data\": \"CodeSearchNet Python 5500 docs\", \"wall_clock_seconds\": 40928.2, \"gpu_hours\": 11.37}, \"reproduce\": {\"finished_at\": \"2026-05-19T08:05:42.229Z\"}, \"failure_reason\": \"Traceback → ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File \\\"/root/autodl-tmp/gen-depth-contamination/scripts/run_pipeline.py\\\", line 462, in run_analysis # Support both integer and string doc_ids ^^^^^^^^^^^^^^^^ ValueError: invalid literal for int() with base 10: 'code_py_0'\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T08:05:44.712Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:05:48.414385+00:00\"}]}, \"metrics\": {\"K_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9161, \"1v2\": 0.7394, \"2v3\": 0.5112, \"3v4\": 0.52, \"4v5\": 0.4996}, \"pairwise_auc_std\": {\"0v1\": 0.004, \"1v2\": 0.0101, \"2v3\": 0.0095, \"3v4\": 0.0137, \"4v5\": 0.0069}, \"pairwise_jsd\": {\"0v1\": 0.060406, \"1v2\": 0.047034, \"2v3\": 0.003473, \"3v4\": 0.003026, \"4v5\": 0.002892}, \"ordinal_mae\": 1.2542, \"ordinal_accuracy\": 0.3485, \"top_features\": [\"freq_entropy\", \"surp_d1_mean\", \"surp_d2_mean\"]}}, \"exp_code_qwen1b5_pythia_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:30:03.239Z\", \"updated_at\": \"2026-05-19T06:55:26.175Z\", \"hypothesis\": \"Code domain scorer confound control: Qwen-1.5B Code K*=2 uses same-family Qwen scorer. D060 Wikipedia showed Qwen scorer inflates AUC by +0.005~0.027. If Pythia-1.4B scorer yields K*=2 on same Qwen Code text, confirms K*=2 is text-intrinsic (not scorer artifact). If K*=1, Qwen Code K*=2 is partially scorer-driven, weakening domain ceiling claim. Cross-family scorer validation on existing exp_code_qwen1b5 depth 0-5 data.\", \"parent\": \"exp_code_qwen1b5\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"spec\": {\"checkpoint_path\": \"results/exp_code_qwen1b5_pythia_scorer/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_qwen1b5_pythia_scorer.log\"}, \"pid\": \"131475\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_qwen1b5_pythia_scorer.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/exp_code_qwen1b5_pythia_scorer.sh\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-19T06:51:51.622Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T06:51:55.524732+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"theta\": 0.6, \"auc_0v1\": 0.9076, \"auc_1v2\": 0.7197, \"auc_2v3\": 0.5308, \"auc_3v4\": 0.5236, \"auc_4v5\": 0.5084, \"jsd_0v1\": 0.065423, \"jsd_1v2\": 0.035809, \"jsd_2v3\": 0.004315, \"jsd_3v4\": 0.003182, \"jsd_4v5\": 0.003047, \"ordinal_mae\": 1.2578, \"ordinal_accuracy\": 0.3433, \"scorer\": \"pythia-1.4b\"}, \"notes\": \"Code domain K*=2 confirmed scorer-independent. Pythia-1.4B scorer reproduces K*=2 on Qwen-1.5B Code text (same as Qwen self-scorer). AUC deltas vs original: 0v1 Δ=-0.031, 1v2 Δ=-0.019 (minor drop, Pythia slightly weaker feature extractor), 2v3 Δ=+0.001 (identical). Boundary transition 1v2→2v3 robust: 0.7197→0.5308, clear drop below θ=0.6. JSD pattern consistent: sharp collapse at depth 2→3. Combined with arXiv cross-scorer results (LLaMA/Mistral K*=3 preserved), confirms generational depth K* is a text-intrinsic property governed by domain complexity, not scorer choice.\", \"completed_at\": \"2026-05-19T06:55:26.175Z\"}, \"exp_pythia_retrain_depth7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:53:18.835Z\", \"updated_at\": \"2026-05-19T03:46:00.139Z\", \"hypothesis\": \"Pythia-1.4B retrain-chain depth extension to 7: 验证 retrain-chain K* >> prompt-chain K* 是否跨模型家族一致（Qwen retrain K*≥7）。如果 Pythia 也 K*≥5-7，confirms retrain artifacts are model-independent。C4 5K docs, LoRA rank=16 alpha=32, depth 0-7。\", \"parent\": \"exp_qwen_retrain_depth7\", \"spec\": {\"command\": \"HF_ENDPOINT=https://hf-mirror.com CUDA_VISIBLE_DEVICES=0 python scripts/exp_pythia_retrain_depth7.py --device cuda:0\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_source\": \"exp_008_retrain_chain depth 0-4 data (extending to depth 5-7)\", \"eval_data\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/features.csv\", \"gpu\": [\"cuda:0\"], \"pid\": \"115855\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_pythia_retrain_depth7_nohup.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_pythia_retrain_depth7\"}, \"notes\": \"Actual log path: /root/autodl-tmp/gen-depth-contamination/logs/exp_pythia_retrain_depth7_nohup.log (not ~/runs/). Fine-tuning 1250 steps completed, currently in generation phase. GPU util 53% normal for Pythia-1.4B small model.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:45:55.351Z\", \"metrics\": {\"kstar\": 7, \"pairwise_auc\": {\"0v1\": 0.9844, \"1v2\": 0.947, \"2v3\": 0.8891, \"3v4\": 0.7999, \"4v5\": 0.6907, \"5v6\": 0.6497, \"6v7\": 0.634}, \"pairwise_auc_ci\": {\"0v1\": [0.9829, 0.9858], \"1v2\": [0.9418, 0.9522], \"2v3\": [0.8822, 0.896], \"3v4\": [0.7951, 0.8047], \"4v5\": [0.688, 0.6934], \"5v6\": [0.6429, 0.6565], \"6v7\": [0.6275, 0.6406]}, \"pairwise_jsd\": {\"0v1\": 0.1775, \"1v2\": 0.1286, \"2v3\": 0.1069, \"3v4\": 0.0643, \"4v5\": 0.0331, \"5v6\": 0.0271, \"6v7\": 0.0138}}}, \"exp_qwen_retrain_depth7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:08:52.105Z\", \"updated_at\": \"2026-05-19T01:10:25.114Z\", \"hypothesis\": \"Qwen2.5-1.5B retrain-chain extended to depth 7: K* measurement at higher depths. Retrain-chain with LoRA rank=16, alpha=32, 1 epoch per generation. Each depth uses independently trained LoRA merged before next generation. C4 5K docs, depth 0-7, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B (self-scoring). Extends exp_qwen_retrain_chain (depth 0-4).\", \"parent\": \"exp_qwen_retrain_chain\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path Qwen2.5-1.5B --max_depth 7 (retrain-chain extension)\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain_ext\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen_retrain_chain\", \"eval_data\": \"C4 5000 docs depth 0-7\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain_ext/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain_ext/summary.json\", \"metrics\": {\"k_star\": 7, \"theta\": 0.6, \"max_depth\": 7, \"analysis_method\": \"5-fold GroupKFold CV\", \"pairwise_auc\": {\"0v1\": {\"mean\": 0.9837, \"std\": 0.0019, \"ci_95\": [0.9821, 0.9854], \"folds\": [0.9832, 0.9821, 0.9837, 0.9823, 0.9873]}, \"1v2\": {\"mean\": 0.8971, \"std\": 0.0025, \"ci_95\": [0.8949, 0.8993], \"folds\": [0.8923, 0.8988, 0.8986, 0.8991, 0.8967]}, \"2v3\": {\"mean\": 0.8098, \"std\": 0.0052, \"ci_95\": [0.8052, 0.8144], \"folds\": [0.8086, 0.8074, 0.818, 0.8024, 0.8128]}, \"3v4\": {\"mean\": 0.76, \"std\": 0.0082, \"ci_95\": [0.7528, 0.7672], \"folds\": [0.7534, 0.7617, 0.7753, 0.7566, 0.7531]}, \"4v5\": {\"mean\": 0.7459, \"std\": 0.0091, \"ci_95\": [0.7379, 0.7538], \"folds\": [0.7429, 0.7562, 0.7521, 0.73, 0.7482]}, \"5v6\": {\"mean\": 0.7017, \"std\": 0.0068, \"ci_95\": [0.6958, 0.7076], \"folds\": [0.7006, 0.7077, 0.7104, 0.6915, 0.6984]}, \"6v7\": {\"mean\": 0.641, \"std\": 0.0039, \"ci_95\": [0.6376, 0.6445], \"folds\": [0.6419, 0.6349, 0.6464, 0.639, 0.643]}}, \"jsd\": {\"0v1\": 0.23005, \"1v2\": 0.103924, \"2v3\": 0.075049, \"3v4\": 0.065398, \"4v5\": 0.060509, \"5v6\": 0.034998, \"6v7\": 0.017652}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:10:20.209Z\", \"notes\": \"Qwen2.5-1.5B retrain-chain K*=7 (all 7 depth pairs AUC > θ=0.60). 6v7 AUC=0.641 (CI [0.638, 0.645]) is the tightest pair but still clears threshold. Depth 0-4 results consistent with exp_qwen_retrain_chain (AUC diff < 0.003). JSD decays from 0.230 (0v1) to 0.018 (6v7), suggesting convergence. AUC decay is sublinear: rapid initial drop (0v1→2v3: ~0.087/step), then deceleration (2v3→4v5: ~0.032/step), with continued decline (4v5→6v7: ~0.052/step). K* ceiling estimated at 7-8 based on extrapolation.\"}, \"exp_code_pythia1b4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:49:01.762Z\", \"updated_at\": \"2026-05-19T00:27:22.456Z\", \"hypothesis\": \"Pythia-1.4B on Code domain (Python/CodeSearchNet) will show K*=2 consistent with Qwen code domain results, indicating generalization depth saturation is model-independent for code data.\", \"parent\": \"exp_code_qwen1b5\", \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_code_pythia1b4 --results_dir results/exp_code_pythia1b4 --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4\", \"data_count\": 5000, \"model_name\": \"Pythia-1.4B\", \"seed\": 42, \"checkpoint_source\": \"exp_code_qwen1b5\", \"eval_data\": \"CodeSearchNet Python 5000 docs\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_code_pythia1b4/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_code_pythia1b4/train.log\", \"metrics\": {\"k_star\": 1, \"theta\": 0.6, \"pairwise_auc\": {\"0v1\": {\"mean\": 0.9592, \"std\": 0.0036, \"folds\": [0.9576, 0.9576, 0.9657, 0.96, 0.9552]}, \"1v2\": {\"mean\": 0.5983, \"std\": 0.005, \"folds\": [0.601, 0.5884, 0.6, 0.5997, 0.6024]}, \"2v3\": {\"mean\": 0.5215, \"std\": 0.0128, \"folds\": [0.5236, 0.5124, 0.5311, 0.5024, 0.5381]}, \"3v4\": {\"mean\": 0.5152, \"std\": 0.012, \"folds\": [0.4981, 0.5327, 0.5092, 0.5123, 0.5238]}, \"4v5\": {\"mean\": 0.5046, \"std\": 0.0137, \"folds\": [0.4983, 0.4822, 0.5074, 0.5224, 0.5128]}}, \"jsd\": {\"0v1\": 0.070173, \"1v2\": 0.008211, \"2v3\": 0.003674, \"3v4\": 0.002902, \"4v5\": 0.002685}, \"ordinal\": {\"mae\": 1.3268, \"accuracy\": 0.3357}, \"top_features\": [\"freq_entropy\", \"surp_d1_mean\", \"surp_d2_mean\", \"surp_mean\", \"surp_d1_skew\"], \"features_csv\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4/features.csv\"}, \"completed_at\": \"2026-05-19T00:25:32.688Z\", \"notes\": \"Pythia-1.4B code domain K*=1 (1v2 AUC=0.5983, 0.17pp below θ=0.60). Hypothesis falsified: expected K*=2 consistent with Qwen. 3/5 folds above θ (0.601, 0.600, 0.602), mean borderline. Parallels Mistral C4 one-wash pattern. Suggests model capability modulates domain ceiling.\"}, \"exp_028_power_curve\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:53:26.909Z\", \"updated_at\": \"2026-05-18T23:01:26.449Z\", \"hypothesis\": \"Subsampling power analysis: K*=2 判定在 C4 上所需的最低样本量。在 n={500,1000,2000,3000,4000,5000} 下 10 次 random resample，每次 5-fold CV 计算 1v2 AUC。输出 power curve（K*=2 判定成功率 vs n）。验证类实验，回应 Reviewer 对 statistical power / sample size adequacy 的质疑。\", \"metrics\": {\"min_n_100pct\": 2000, \"n500_auc\": 0.5808, \"n500_rate\": 0.2, \"n1000_auc\": 0.5911, \"n1000_rate\": 0.3, \"n2000_auc\": 0.6101, \"n2000_rate\": 1, \"n3000_auc\": 0.6166, \"n3000_rate\": 1, \"n4000_auc\": 0.622, \"n4000_rate\": 1, \"n5000_auc\": 0.6288, \"n5000_rate\": 1}, \"conclusion\": \"success\", \"notes\": \"K*=2 detection on C4 requires minimum n=2000 docs for 100% success rate (10/10 resamples). Below n=2000 power drops sharply: n=1000 → 30%, n=500 → 20%. AUC variance monotonically decreases with n (0.018 at n=500 → 0.004 at n=4000). Feature data from exp016_qwen_base (C4, 5000 docs × 6 depths × 15 features). CPU-only, 86s runtime.\", \"spec\": {\"checkpoint_path\": \"N/A (analysis experiment)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_028_power_curve/\", \"command\": \"python scripts/exp_028_power_curve.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv\", \"data_count\": 30000, \"model_name\": \"N/A\", \"seed\": 42}, \"completed_at\": \"2026-05-18T23:01:26.449Z\"}, \"exp_qwen_retrain_chain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:57:56.785Z\", \"updated_at\": \"2026-05-18T22:30:28.719Z\", \"hypothesis\": \"Qwen2.5-1.5B retrain-chain ecological validity: LoRA rank=16, alpha=32, 1 epoch per generation. Retrain-chain K* ≤ prompt-chain K*=2, confirming prompt-chain as conservative upper bound across a second architecture family (Qwen vs Pythia). C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B (self-scoring).\", \"parent\": \"exp_008_retrain_chain_v2\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/qwen_retrain_chain/lora_adapters/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_qwen_retrain_chain.log\"}, \"metrics\": {\"K_star_lower_bound\": 4, \"theta\": 0.6, \"auc_0v1\": 0.9838, \"auc_1v2\": 0.8969, \"auc_2v3\": 0.81, \"auc_3v4\": 0.7624, \"ci_0v1\": [0.982, 0.9855], \"ci_1v2\": [0.8937, 0.9001], \"ci_2v3\": [0.8052, 0.8147], \"ci_3v4\": [0.7543, 0.7706], \"ci_method\": \"5-fold CV\", \"jsd_0v1\": 0.2263, \"jsd_1v2\": 0.1046, \"jsd_2v3\": 0.0752, \"jsd_3v4\": 0.0654}, \"notes\": \"Qwen2.5-1.5B retrain-chain K*≥4 (all 4 pairs AUC >> θ=0.60). Bootstrap CI discarded due to data leakage (resampling broke GroupKFold structure, inflated AUC by +6.4pp). Using fold-based CI instead. Retrain-chain K*≥4 >> prompt-chain K*=2, contradicts conservative-upper-bound hypothesis but confirms retrain produces qualitatively different degradation pattern.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:30:28.719Z\"}, \"exp_code_qwen1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:36:16.788Z\", \"updated_at\": \"2026-05-18T21:45:24.101Z\", \"hypothesis\": \"Code domain (Python) K* measurement: Qwen2.5-1.5B continuation on CodeSearchNet Python subset (Husain et al. 2019). Code 的高度结构化特性（语法约束、缩进、函数签名）应使代际退化慢于 C4 (K*≥2)，可能接近 arXiv (K*=3)。5500 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"notes\": \"Code domain (Python/CodeSearchNet) K*=2, same as C4. 1v2 AUC=0.7382 well above θ, 2v3 drops to 0.5300. Bug fix: run_pipeline.py:462 int(doc_id) patched for string IDs. Top features: freq_entropy, surp_d2_mean, surp_d1_mean. Data source: CodeSearchNet Python subset (Husain et al. 2019).\", \"spec\": {\"checkpoint_path\": \"N/A (pipeline experiment, no model checkpoint)\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_qwen1b5.log\"}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 2, \"theta\": 0.6, \"auc_0v1\": 0.9388, \"auc_1v2\": 0.7382, \"auc_2v3\": 0.53, \"auc_3v4\": 0.5022, \"auc_4v5\": 0.5219, \"ci_0v1\": [0.929, 0.949], \"ci_1v2\": [0.709, 0.767], \"ci_2v3\": [0.514, 0.546], \"jsd_0v1\": 0.0814, \"jsd_1v2\": 0.0443, \"jsd_2v3\": 0.0038, \"ordinal_accuracy\": 0.359, \"ordinal_mae\": 1.204}, \"completed_at\": \"2026-05-18T21:45:24.101Z\"}, \"exp_olmo_retrain_chain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:08:07.671Z\", \"updated_at\": \"2026-05-18T16:27:30.792Z\", \"hypothesis\": \"OLMo-1B retrain-chain (LoRA rank=16, 1 epoch per generation) on C4 produces K* ≤ 2, confirming prompt-chain as conservative upper bound for K*.\", \"parent\": \"exp_002\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_olmo_retrain_chain.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/olmo_retrain_chain\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"checkpoint_source\": \"allenai/OLMo-1B-hf\", \"eval_data\": \"C4 validation (5000 docs)\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T16:27:30.792Z\"}, \"exp_028_subsampling_power\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:30:47.472Z\", \"updated_at\": \"2026-05-18T13:31:41.053Z\", \"hypothesis\": \"C4 K*=2 信号的 minimum sample size: 在 n={1000..5000} 范围内，GroupKFold(5) 1v2 AUC 是否稳定超过 θ=0.60？确定可靠判定 K*=2 所需的最小样本量。\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/c4_power_curve/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/c4_power_curve/power_curve_results.json\", \"metrics\": {\"n_1000\": {\"mean_auc\": 0.608, \"std\": 0.012, \"detection_prob\": 0.9}, \"n_2500\": {\"mean_auc\": 0.618, \"std\": 0.006, \"detection_prob\": 1}, \"n_5000\": {\"mean_auc\": 0.629, \"std\": 0, \"detection_prob\": 1}, \"key_finding\": \"n>=2500 gives 100% reliable K*=2 detection. n=1000 already 90%. Signal is robust, not large-sample artifact.\"}, \"spec\": {\"command\": \"python scripts/c4_power_curve.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/results/ (exp-016 features)\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (scorer)\", \"seed\": \"10 random trials per n\", \"checkpoint_source\": \"exp-016 feature vectors\", \"eval_data\": \"GroupKFold(5) pairwise classification, n={1000..5000}\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T13:31:41.053Z\"}, \"exp_026_arxiv_filtering\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:19:57.768Z\", \"updated_at\": \"2026-05-18T11:20:35.820Z\", \"hypothesis\": \"Graduated depth weighting (α=0.9^d) on arXiv depth chains will outperform both no-filter and binary-cut baselines on downstream benchmarks (MMLU, HellaSwag), because it preserves useful signal from deeper generations while down-weighting accumulated contamination, rather than discarding data entirely.\", \"parent\": \"exp_006_graduated_filtering\", \"spec\": {\"command\": \"bash scripts/run_exp026.sh\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/\", \"data_count\": 13200, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": \"42,123,456,789,1024\", \"gpu\": \"cuda:0,cuda:1,cuda:2\", \"strategies\": \"no_filter,binary,graduated_a09\", \"lora_rank\": 4, \"lora_alpha\": 8, \"pid\": 27516, \"checkpoint_source\": \"lora_merge_per_run\", \"eval_data\": \"mmlu,hellaswag (lm-eval-harness)\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_026_arxiv_filtering.log\", \"metrics\": {\"runs_completed\": \"15/15\", \"strategies\": [\"no_filter\", \"binary\", \"graduated_a09\"], \"seeds\": [42, 123, 456, 789, 1024], \"mmlu\": {\"no_filter\": \"0.5899±0.0008\", \"binary\": \"0.5876±0.0004\", \"graduated_a09\": \"0.5900±0.0011\"}, \"hellaswag\": {\"no_filter\": \"0.6600±0.0002\", \"binary\": \"0.6642±0.0004\", \"graduated_a09\": \"0.6599±0.0003\"}, \"delta_vs_no_filter\": {\"binary_mmlu\": \"-0.0023\", \"binary_hellaswag\": \"+0.0042\", \"graduated_mmlu\": \"+0.0001\", \"graduated_hellaswag\": \"-0.0001\"}, \"key_finding\": \"All three strategies produce nearly identical results. Graduated ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T11:20:35.820Z\"}, \"exp_027_latex_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:19:59.624Z\", \"updated_at\": \"2026-05-18T10:41:35.226Z\", \"hypothesis\": \"arXiv K*=3 不依赖 LaTeX 格式特征。去除 LaTeX markup 后重新提取 15D features 并跑 pairwise classification，K* 应仍=3，排除 LaTeX 语法作为 confound。\", \"parent\": \"exp_024_arxiv_depth_chain\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/summary.txt\", \"metrics\": {\"k_star\": 3, \"k_star_preserved\": true, \"pairwise_auc_original\": {\"0v1\": 0.9948, \"1v2\": 0.8581, \"2v3\": 0.6436, \"3v4\": 0.544, \"4v5\": 0.5299}, \"pairwise_auc_stripped\": {\"0v1\": 0.9948, \"1v2\": 0.8297, \"2v3\": 0.6229, \"3v4\": 0.5468, \"4v5\": 0.5476}, \"auc_delta\": {\"0v1\": 0, \"1v2\": -0.028, \"2v3\": -0.021, \"3v4\": 0.003, \"4v5\": 0.018}, \"latex_reduction_by_depth\": {\"depth_0\": \"0.6%\", \"depth_5\": \"4.4%\"}, \"key_finding\": \"K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still >θ=0.60). LaTeX format is NOT a confound.\"}, \"spec\": {\"command\": \"python scripts/exp027_latex_ablation.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/\", \"data_count\": 13200, \"model_name\": \"Qwen2.5-1.5B (scorer)\", \"seed\": 42, \"checkpoint_source\": \"exp_024_arxiv_depth_chain\", \"eval_data\": \"GroupKFold(5) pairwise classification\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:41:35.226Z\"}, \"exp_025_pythia_filtering\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:04:54.965Z\", \"updated_at\": \"2026-05-18T09:51:02.931Z\", \"hypothesis\": \"Filtering strategy ordering (binary > graduated > no-filter) 在 Pythia-1.4B 上与 Qwen 一致，验证 K*=2 对 curation 策略选择的跨模型预测价值。Pythia-1.4B LoRA rank=8 continued pretraining on C4 depth chain, 3 strategies × 3 seeds, eval MMLU+HellaSwag.\", \"parent\": \"exp_006_graduated_filtering\", \"spec\": {\"command\": \"bash scripts/run_exp025.sh (3 strategies × 3 seeds, 9 runs in 3 batches, 4 GPUs parallel per batch)\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp020_pythia_nuc09/\", \"data_count\": 30000, \"model_name\": \"Pythia-1.4B\", \"seed\": \"42,123,456\", \"checkpoint_source\": \"EleutherAI/pythia-1.4b (HuggingFace, base model for LoRA)\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\"}, \"notes\": \"Data source fixed: greedy → nuc09. Old processes killed (6 procs). Resubmitted 2026-05-18T08:27 via nohup (not submit_training_job). PID 15687, cqa1 cuda:0-3, 9 runs in 3 batches (4 parallel per batch). Cron registered for monitoring.\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_025_pythia_filtering/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp025/\", \"metrics\": {\"runs_completed\": \"9/9\", \"strategies\": [\"no_filter\", \"binary_ours\", \"graduated_a09\"], \"seeds\": [42, 123, 456], \"mmlu\": {\"no_filter\": \"0.2568±0.0012\", \"binary_ours\": \"0.2585±0.0004\", \"graduated_a09\": \"0.2561±0.0009\"}, \"hellaswag\": {\"no_filter\": \"0.5250±0.0008\", \"binary_ours\": \"0.5251±0.0001\", \"graduated_a09\": \"0.5253±0.0007\"}, \"delta_vs_no_filter\": {\"binary_ours_mmlu\": \"+0.0017\", \"binary_ours_hellaswag\": \"+0.0000\", \"graduated_a09_mmlu\": \"-0.0007\", \"graduated_a09_hellaswag\": \"+0.0003\"}, \"key_finding\": \"All three filtering strategies produce nearly identical results on Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering binary>graduated>no_filter NOT confirmed.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T09:51:02.931Z\"}, \"exp_14b_c4\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T14:56:44.366Z\", \"updated_at\": \"2026-05-18T08:37:25.809Z\", \"hypothesis\": \"Scale-dependent K* on C4: Qwen2.5-14B fp16 continuation on C4 web text 的 K* 是否仍 = 2？验证 K*=2 dominant mode 在 14B scale 是否稳定（已确认 1.5B/7B/8B 均 K*=2），排除 scale ceiling effect。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_arXiv_llama8b\", \"server\": \"westd-42896\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-42896\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T17:08:43.246Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-14B --data_dir data/exp_14b_c4 --results_dir results/exp_14b_c4 --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"finished_at\": \"2026-05-18T08:21:21.247Z\", \"training_hours\": 15.21}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-18T05:09:04.625Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:09:08.254971+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:21:24.534646+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-14B --data_dir data/exp_14b_c4 --results_dir results/exp_14b_c4 --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"39497\", \"log_path\": \"~/runs/gen-depth-contamination/exp_14b_c4.log\", \"submitted_at\": \"2026-05-18T05:12:11.079Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11638.0, \"gpu_hours\": 3.23}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9598, \"1v2\": 0.621, \"2v3\": 0.5494, \"3v4\": 0.5243, \"4v5\": 0.5154}, \"pairwise_jsd\": {\"0v1\": 0.1097, \"1v2\": 0.0112, \"2v3\": 0.0062, \"3v4\": 0.0044, \"4v5\": 0.0036}, \"bootstrap_ci\": {\"0v1\": [0.9564, 0.963], \"1v2\": [0.6119, 0.6304], \"2v3\": [0.5392, 0.5594], \"3v4\": [0.514, 0.5346], \"4v5\": [0.5045, 0.5265]}, \"permutation_p\": {\"0v1\": \"<0.001\", \"1v2\": \"<0.001\", \"2v3\": \"<0.001\", \"3v4\": \"<0.001\", \"4v5\": \"<0.001\"}, \"k_star_statistically_confirmed\": true, \"ordinal_mae\": 1.2266, \"ordinal_accuracy\": 0.3497, \"top_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_std\", \"surp_d1_mean\", \"surp_d2_mean\"], \"key_finding\": \"K*=2 confirmed at 14B scale with bootstrap CI. 1v2 CI lower (0.6119) > theta=0.60; 2v3 CI upper (0.5594) < theta=0.60. All permutation p<0.001.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/\"}, \"exp_arXiv_mistral7b_crossscorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:44:21.237Z\", \"updated_at\": \"2026-05-18T03:04:46.219Z\", \"hypothesis\": \"arXiv cross-scorer (Mistral-7B): Pythia scorer 验证 Mistral arXiv K*=3 是否 scorer-independent。\", \"parent\": \"exp_wiki_scorer_confound\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_arXiv_mistral7b_crossscorer && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_mistral7b/depth_\\\\${d}.jsonl data/exp_arXiv_mistral7b_crossscorer/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_arXiv_mistral7b_crossscorer && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_arXiv_mistral7b_crossscorer --results_dir results/exp_arXiv_mistral7b_crossscorer --num_samples 2200 --max_depth 5 --batch_size 16 --generation_mode continuation --skip_generation\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"196053\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_mistral7b_crossscorer.log\", \"submitted_at\": \"2026-05-18T02:44:57.643Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 2200, \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_mistral7b\", \"model_name\": \"Mistral-7B (generator) + Pythia-1.4B (scorer)\", \"seed\": 42, \"checkpoint_source\": \"exp_arXiv_mistral7b\", \"eval_data\": \"arXiv depth 0-5 generated by Mistral-7B (from exp_arXiv_mistral7b)\", \"checkpoint_path\": \"results/exp_arXiv_mistral7b_crossscorer/\", \"wall_clock_seconds\": 1117.5, \"gpu_hours\": 0.31}, \"reproduce\": {\"finished_at\": \"2026-05-18T03:00:29.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T03:00:37.583555+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 3, \"scorer\": \"pythia-1.4b\", \"auc_0v1\": 0.9798, \"auc_1v2\": 0.8141, \"auc_2v3\": 0.6075, \"auc_3v4\": 0.5489, \"auc_4v5\": 0.5391, \"jsd_0v1\": 0.135575, \"jsd_1v2\": 0.078, \"jsd_2v3\": 0.020452, \"jsd_3v4\": 0.010992, \"jsd_4v5\": 0.008831, \"ordinal_mae\": 0.9061, \"ordinal_accuracy\": 0.4412}, \"completed_at\": \"2026-05-18T03:03:35.138Z\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_mistral7b_crossscorer.log\", \"notes\": \"Pythia-1.4B cross-scorer confirms K*=3 for Mistral-7B arXiv, matching Qwen-1.5B original. Max AUC delta = 0.02 (at 2v3). arXiv Mistral K*=3 is scorer-independent. Contrasts with Wikipedia where scorer choice affected K*.\"}, \"exp_arXiv_llama8b_crossscorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:44:19.881Z\", \"updated_at\": \"2026-05-18T03:04:36.609Z\", \"hypothesis\": \"Replacing Qwen-1.5B scorer with Pythia-1.4B on arXiv LLaMA-8B depth 0-5 texts should yield the same K*=3 boundary, because the saturation signal is a genuine property of LLaMA-8B generated text rather than a scorer family artifact\", \"parent\": \"exp_wiki_scorer_confound\", \"spec\": {\"command\": \"skip_generation scoring with Pythia-1.4B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"195907\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_llama8b_crossscorer.log\", \"submitted_at\": \"2026-05-18T02:44:54.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_llama8b_crossscorer/\", \"data_count\": 6, \"model_name\": \"pythia-1.4b\", \"seed\": 42, \"checkpoint_source\": \"exp_arXiv_llama8b\", \"eval_data\": \"arXiv LLaMA-8B depth 0-5 continuations from exp_arXiv_llama8b\", \"checkpoint_path\": \"results/exp_arXiv_llama8b_crossscorer/\", \"wall_clock_seconds\": 1119.6, \"gpu_hours\": 0.31}, \"reproduce\": {\"finished_at\": \"2026-05-18T03:00:23.861Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T03:00:27.320630+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 3, \"auc_0v1\": 0.9629, \"auc_1v2\": 0.8433, \"auc_2v3\": 0.6201, \"auc_3v4\": 0.523, \"auc_4v5\": 0.5245, \"jsd_0v1\": 0.1214, \"jsd_1v2\": 0.0815, \"jsd_2v3\": 0.0195, \"jsd_3v4\": 0.0083, \"jsd_4v5\": 0.0082, \"ordinal_mae\": 0.9025, \"ordinal_accuracy\": 0.4407, \"scorer\": \"pythia-1.4b\"}, \"completed_at\": \"2026-05-18T03:03:34.051Z\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_llama8b_crossscorer.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_llama8b_crossscorer/\"}, \"exp_arXiv_qwen7b_crossscorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:13:55.051Z\", \"updated_at\": \"2026-05-18T03:04:22.586Z\", \"hypothesis\": \"arXiv cross-scorer (7B): Pythia-1.4B scorer 重评 Qwen-7B arXiv depth 0-5。D060 Wiki scorer confound 推导。关键 2v3 AUC ≥0.60 → K*=3 scorer-independent。\", \"parent\": \"exp_wiki_scorer_confound\", \"spec\": {\"command\": \"run_pipeline.py --skip_generation\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"195291\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen7b_crossscorer.log\", \"submitted_at\": \"2026-05-18T02:44:45.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_arXiv_qwen7b_crossscorer\", \"data_count\": 2200, \"model_name\": \"Qwen/Qwen2.5-7B\", \"seed\": 42, \"checkpoint_source\": \"exp_arXiv_qwen7b\", \"eval_data\": \"arXiv Qwen-7B depth 0-5 from exp_arXiv_qwen7b\", \"wall_clock_seconds\": 1156.0, \"gpu_hours\": 0.32, \"checkpoint_path\": \"results/exp_arXiv_qwen7b_crossscorer/\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T02:59:40.126Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"negative\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:18:26.248465+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:59:43.427079+00:00\"}]}, \"notes\": \"Hypothesis rejected: cross-scorer 2v3 AUC=0.5989 < 0.60, K* drops from 3→2. Mild Qwen family bias (~0.027 AUC at 2v3) inflates original K*=3. Scorer-independent K*=2. Borderline: 3/5 folds above 0.60. Depths 0-2 robustly scorer-independent.\", \"metrics\": {\"k_star\": 2, \"auc_0v1\": 0.9575, \"auc_1v2\": 0.8171, \"auc_2v3\": 0.5989, \"auc_3v4\": 0.5417, \"auc_4v5\": 0.5192, \"jsd_0v1\": 0.137085, \"jsd_1v2\": 0.059688, \"jsd_2v3\": 0.013508, \"jsd_3v4\": 0.009125, \"jsd_4v5\": 0.006738, \"ordinal_mae\": 0.9617, \"ordinal_accuracy\": 0.4255}, \"checkpoint_path\": \"N/A (scoring-only experiment, no training checkpoint)\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen7b_crossscorer.log\", \"completed_at\": \"2026-05-18T03:04:01.839Z\"}, \"exp_arXiv_qwen1b5_crossscorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:13:56.083Z\", \"updated_at\": \"2026-05-18T03:02:38.562Z\", \"hypothesis\": \"arXiv cross-scorer (1.5B): Pythia-1.4B scorer 重评 Qwen-1.5B arXiv depth 0-5。验证 K*=3 scorer-independent。\", \"parent\": \"exp_wiki_scorer_confound\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_arXiv_qwen1b5_crossscorer && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/depth_\\\\${d}.jsonl data/exp_arXiv_qwen1b5_crossscorer/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_arXiv_qwen1b5_crossscorer && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_arXiv_qwen1b5_crossscorer --results_dir results/exp_arXiv_qwen1b5_crossscorer --num_samples 2200 --max_depth 5 --batch_size 16 --generation_mode continuation --skip_generation\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"195826\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen1b5_crossscorer.log\", \"submitted_at\": \"2026-05-18T02:44:53.081Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"results/exp_arXiv_qwen1b5_crossscorer/\", \"wall_clock_seconds\": 1065.5, \"gpu_hours\": 0.3}, \"reproduce\": {\"finished_at\": \"2026-05-18T02:59:46.327Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:18:40.560606+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:59:52.404331+00:00\"}]}, \"notes\": \"首次提交因 symlink 问题失败 (EXIT_CODE=1)，Worker 修复后重跑成功 (EXIT_CODE=0)。Pythia-1.4B scorer 重评 Qwen-1.5B arXiv 文本 K*=3，与 Qwen scorer 一致，确认 arXiv K*=3 scorer-independent。\", \"metrics\": {\"k_star\": 3, \"auc_0v1\": 0.9748, \"auc_1v2\": 0.8105, \"auc_2v3\": 0.6317, \"auc_3v4\": 0.5437, \"auc_4v5\": 0.5294, \"jsd_0v1\": 0.154297, \"jsd_1v2\": 0.066782, \"jsd_2v3\": 0.019268, \"jsd_3v4\": 0.008867, \"jsd_4v5\": 0.006991, \"ordinal_mae\": 0.9017, \"ordinal_accuracy\": 0.4402}, \"completed_at\": \"2026-05-18T03:02:38.562Z\"}, \"exp_wiki_scorer_confound_1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:18:37.565Z\", \"updated_at\": \"2026-05-18T01:21:43.381Z\", \"hypothesis\": \"Scorer family bias replication (Qwen-1.5B): 用 Pythia-1.4B 替代 Qwen-1.5B 作为 scorer 重新评分 exp_023_domain_ablation (Qwen-1.5B Wiki depth 0-5) 文本。如果 Pythia scorer 下 K* 仍=2 → confound excluded for both Qwen scales；如果 K*=1 → scorer confound confirmed，与 Qwen-7B 复验一致。\", \"parent\": \"exp_023_domain_ablation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T23:20:01.037Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_wiki_scorer_confound_1b5 && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/depth_\\\\${d}.jsonl data/exp_wiki_scorer_confound_1b5/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_wiki_scorer_confound_1b5 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_wiki_scorer_confound_1b5 --results_dir results/exp_wiki_scorer_confound_1b5 --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-18T01:18:40.529Z\", \"training_hours\": 1.98}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_wiki_scorer_confound_1b5 && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/depth_\\\\${d}.jsonl data/exp_wiki_scorer_confound_1b5/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_wiki_scorer_confound_1b5 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_wiki_scorer_confound_1b5 --results_dir results/exp_wiki_scorer_confound_1b5 --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"180543\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_scorer_confound_1b5.log\", \"submitted_at\": \"2026-05-17T23:22:42.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7140.9, \"gpu_hours\": 1.98}, \"pid\": \"180543\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_scorer_confound_1b5.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:18:44.039720+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"k_star\": 1, \"confound_verdict\": \"confirmed\", \"auc_0v1\": 0.9729, \"auc_1v2\": 0.5994, \"auc_2v3\": 0.533, \"auc_3v4\": 0.5214, \"auc_4v5\": 0.5068, \"jsd_0v1\": 0.0886, \"ordinal_mae\": 1.2995, \"ordinal_accuracy\": 0.3466}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_scorer_confound_1b5/\", \"completed_at\": \"2026-05-18T01:21:43.381Z\"}, \"exp_wiki_scorer_confound\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:35:20.326Z\", \"updated_at\": \"2026-05-17T23:20:31.517Z\", \"hypothesis\": \"Scorer family bias test: Qwen-7B Wikipedia K*=2 是 Qwen-1.5B scorer 的 family bias artifact 还是真实信号？用 Pythia-1.4B 替代 Qwen-1.5B 作为 scorer 重新评分同一批 depth 0-5 文本。如果 Pythia scorer 下 K* 仍=2 → confound excluded；如果 K*=1 → scorer confound confirmed。\", \"parent\": \"exp_wiki_qwen7b\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T22:55:01.348Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_wiki_scorer_confound && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_wiki_qwen7b/depth_\\\\${d}.jsonl data/exp_wiki_scorer_confound/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_wiki_scorer_confound && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_wiki_scorer_confound --results_dir results/exp_wiki_scorer_confound --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T23:13:55.501Z\", \"training_hours\": 0.32}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_wiki_scorer_confound && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_wiki_qwen7b/depth_\\\\${d}.jsonl data/exp_wiki_scorer_confound/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_wiki_scorer_confound && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_wiki_scorer_confound --results_dir results/exp_wiki_scorer_confound --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"178762\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_scorer_confound.log\", \"submitted_at\": \"2026-05-17T22:55:03.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_scorer_confound/\", \"wall_clock_seconds\": 1528.4, \"gpu_hours\": 0.42}, \"pid\": \"178762\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_scorer_confound.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T23:13:58.836236+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"k_star\": 1, \"confound_verdict\": \"confirmed\", \"auc_0v1\": 0.9404, \"auc_1v2\": 0.587, \"auc_2v3\": 0.5456, \"auc_3v4\": 0.525, \"auc_4v5\": 0.5172, \"critical_delta_1v2\": -0.0238}, \"completed_at\": \"2026-05-17T23:20:31.517Z\"}, \"exp_wiki_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:39:29.006Z\", \"updated_at\": \"2026-05-17T22:24:51.126Z\", \"hypothesis\": \"Cross-scale Wikipedia K* validation: Qwen2.5-7B continuation on Wikipedia 的 K* 是否 = 2？Qwen2.5-1.5B 在 Wikipedia K*=2（唯一维持 K*=2 的模型），Pythia/OLMo/均 K*=1。测试 7B 规模是否仍维持 Qwen 家族在 Wikipedia 上的 K*=2 pattern。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_arXiv_qwen7b\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T17:02:41.963Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_wiki_qwen7b --results_dir results/exp_wiki_qwen7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T22:21:53.554Z\", \"training_hours\": 5.32}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_wiki_qwen7b --results_dir results/exp_wiki_qwen7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"732600\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_qwen7b.log\", \"submitted_at\": \"2026-05-17T17:02:43.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19327.6, \"gpu_hours\": 5.37}, \"pid\": \"732600\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_qwen7b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T22:21:56.559363+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 2, \"auc_0v1\": 0.9673, \"auc_1v2\": 0.6108, \"auc_2v3\": 0.5562, \"auc_3v4\": 0.5297, \"auc_4v5\": 0.529, \"jsd_0v1\": 0.083514, \"jsd_1v2\": 0.010991, \"jsd_2v3\": 0.00555, \"jsd_3v4\": 0.004611, \"jsd_4v5\": 0.003894, \"ordinal_mae\": 1.2501, \"ordinal_accuracy\": 0.3532}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_qwen7b\", \"completed_at\": \"2026-05-17T22:24:51.126Z\"}, \"exp_wiki_mistral7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:04:15.959Z\", \"updated_at\": \"2026-05-17T19:53:56.272Z\", \"hypothesis\": \"Mistral-7B Wikipedia K* test: Mistral-7B-v0.3 在 C4 上 K*=1 (text-intrinsic one-wash)。在 Wikipedia domain 上是否仍 K*=1？Pythia/OLMo 在 Wikipedia 均 K*=1，Qwen K*=2。如果 Mistral K*=1 → 确认 one-wash 跨域成立；如果 K*>1 → Wikipedia 有 rescue Mistral 的结构信号（与预期相反）。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_wiki_pythia_v2\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T14:05:42.553Z\", \"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_wiki_mistral7b --results_dir results/exp_wiki_mistral7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T19:50:28.711Z\", \"training_hours\": 5.75}, \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_wiki_mistral7b --results_dir results/exp_wiki_mistral7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"data_path\": \"data/exp_wiki_mistral7b\", \"data_count\": 5000, \"model_name\": \"mistralai/Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_source\": \"pretrained:mistralai/Mistral-7B-v0.3\", \"eval_data\": \"Wikipedia depth 0-5, scorer=Qwen2.5-1.5B\"}, \"pid\": \"41845\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_mistral7b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:50:32.601540+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_mistral7b\", \"metrics\": {\"K_star\": 1, \"ordinal_mae\": 1.3445, \"ordinal_accuracy\": 0.3273, \"auc_0v1\": 0.9607, \"auc_1v2\": 0.5552, \"auc_2v3\": 0.5236, \"auc_3v4\": 0.5181, \"auc_4v5\": 0.5012, \"jsd_0v1\": 0.054134, \"jsd_1v2\": 0.005678, \"jsd_2v3\": 0.003698, \"jsd_3v4\": 0.003459, \"jsd_4v5\": 0.003274}, \"completed_at\": \"2026-05-17T19:53:56.272Z\"}, \"exp_wiki_llama8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:27:37.043Z\", \"updated_at\": \"2026-05-17T19:33:39.300Z\", \"hypothesis\": \"Cross-scale Wikipedia K* validation: LLaMA-3.1-8B continuation on Wikipedia 的 K* 是否 = 2？Pythia-1.4B K*=1, Qwen-1.5B K*=2, OLMo-1B K*=1。测试 8B scale 是否能在 Wikipedia 均质 domain 上维持 K*=2（scale 是否是决定因素）。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_wiki_pythia_v2\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-17T13:29:58.320Z\", \"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --data_dir data/exp_wiki_llama8b --results_dir results/exp_wiki_llama8b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T19:30:35.869Z\", \"training_hours\": 6.01}, \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --data_dir data/exp_wiki_llama8b --results_dir results/exp_wiki_llama8b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"data_path\": \"data/exp_wiki_llama8b\", \"data_count\": 5000, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"pretrained:LLM-Research/Meta-Llama-3.1-8B\", \"eval_data\": \"Wikipedia depth 0-5, scorer=Qwen2.5-1.5B\"}, \"pid\": \"38142\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_llama8b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:30:39.064445+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"ordinal_mae\": 1.2954, \"ordinal_accuracy\": 0.3313, \"auc_0v1\": 0.9316, \"auc_1v2\": 0.5954, \"auc_2v3\": 0.5392, \"auc_3v4\": 0.5221, \"auc_4v5\": 0.5212, \"jsd_0v1\": 0.06169, \"jsd_1v2\": 0.00931}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_llama8b\", \"completed_at\": \"2026-05-17T19:33:39.300Z\"}, \"exp_arXiv_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:56:03.934Z\", \"updated_at\": \"2026-05-17T16:36:58.029Z\", \"hypothesis\": \"Qwen2.5-7B on arXiv abstracts will yield K*=3, validating that structured domain K*=3 is stable within the Qwen family across scales (1.5B vs 7B)\", \"parent\": \"exp_024_arxiv_domain\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T14:08:40.926Z\", \"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_arXiv_qwen7b --results_dir results/exp_arXiv_qwen7b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T16:34:23.946Z\", \"training_hours\": 2.43}, \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_arXiv_qwen7b --results_dir results/exp_arXiv_qwen7b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"data_path\": \"data/exp_arXiv_qwen7b\", \"data_count\": 2200, \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"checkpoint_source\": \"pretrained:Qwen/Qwen2.5-7B\", \"eval_data\": \"arXiv abstracts depth 0-5, scorer=Qwen2.5-1.5B\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_qwen7b\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen7b.log\"}, \"pid\": \"42742\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen7b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T16:34:26.949400+00:00\"}]}, \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.983, \"1v2\": 0.835, \"2v3\": 0.626, \"3v4\": 0.544, \"4v5\": 0.513}, \"pairwise_jsd\": {\"0v1\": 0.1656, \"1v2\": 0.0668, \"2v3\": 0.0156, \"3v4\": 0.0089, \"4v5\": 0.0061}, \"ordinal_mae\": 0.9, \"ordinal_accuracy\": 0.446}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T16:36:58.029Z\"}, \"exp_arXiv_mistral7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:28.299Z\", \"updated_at\": \"2026-05-17T16:28:24.294Z\", \"hypothesis\": \"Mistral-7B arXiv K* test: Mistral-7B-v0.3 在 C4 上 K*=1 (one-wash model)。在 arXiv structured domain 上是否仍 K*=1？如果 K*=1 → 确认 Mistral 的 one-wash 是 text-intrinsic (与 domain 无关)；如果 K*>1 → domain complexity 可以 rescue one-wash models，K* 同时受 model 和 domain 驱动。2200 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_arXiv_olmo\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-17T13:53:18.456Z\", \"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_arXiv_mistral7b --results_dir results/exp_arXiv_mistral7b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T16:25:00.229Z\", \"training_hours\": 2.53}, \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_arXiv_mistral7b --results_dir results/exp_arXiv_mistral7b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"data_path\": \"data/exp_arXiv_mistral7b\", \"data_count\": 2200, \"model_name\": \"mistralai/Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_source\": \"pretrained:mistralai/Mistral-7B-v0.3\", \"eval_data\": \"arXiv abstracts depth 0-5, scorer=Qwen2.5-1.5B\"}, \"pid\": \"40472\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_mistral7b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T16:25:03.226062+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9848, \"1v2\": 0.8201, \"2v3\": 0.6275, \"3v4\": 0.5295, \"4v5\": 0.5295}, \"jsd\": {\"0v1\": 0.14249, \"1v2\": 0.076232, \"2v3\": 0.018972, \"3v4\": 0.009908, \"4v5\": 0.008877}, \"ordinal_mae\": 0.8958, \"ordinal_accuracy\": 0.4474, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_d1_skew\", \"surp_mean\", \"surp_d2_mean\"]}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_mistral7b\", \"completed_at\": \"2026-05-17T16:28:24.294Z\"}, \"exp_arXiv_llama8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:53:57.754Z\", \"updated_at\": \"2026-05-17T14:02:45.388Z\", \"hypothesis\": \"Cross-architecture arXiv K* validation: LLaMA-3.1-8B continuation on arXiv abstracts 的 K* 是否 = 3？验证 structured domain K*=3 在大模型（8B scale）上是否成立，排除小模型 capacity artifact。2200 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_024_arxiv_domain\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T10:59:48.493Z\", \"finished_at\": \"2026-05-17T13:59:25.526Z\", \"training_hours\": 2.99}, \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --data_dir data/exp_arXiv_llama8b --results_dir results/exp_arXiv_llama8b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"27469\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_llama8b.log\", \"submitted_at\": \"2026-05-17T11:23:08.013Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_arXiv_llama8b (seed from exp_024_arxiv/depth_0.jsonl)\", \"data_count\": 2200, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"pretrained:LLM-Research/Meta-Llama-3.1-8B\", \"eval_data\": \"arXiv abstracts depth 0-5, scorer=Qwen2.5-1.5B\", \"wall_clock_seconds\": 9577.4, \"gpu_hours\": 2.66}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:59:27.415949+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 3, \"auc_0v1\": 0.9754, \"auc_1v2\": 0.8447, \"auc_2v3\": 0.6215, \"auc_3v4\": 0.5362, \"auc_4v5\": 0.5331, \"jsd_0v1\": 0.1296, \"jsd_1v2\": 0.0785, \"jsd_2v3\": 0.0177, \"ordinal_acc\": 0.4549, \"ordinal_mae\": 0.8806}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_llama8b/\", \"completed_at\": \"2026-05-17T14:02:45.388Z\"}, \"exp_wiki_pythia_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:40:37.896Z\", \"updated_at\": \"2026-05-17T13:25:22.734Z\", \"hypothesis\": \"Cross-model Wikipedia K* validation (v2 fix): Pythia-1.4B continuation on Wikipedia 的 K* 是否 = 2？使用独立 data_dir 避免 v1 的 data reuse bug，让 pipeline 用 Pythia 重新生成 depth 1-5。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_wiki_pythia\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path ...pythia-1.4b... --generation_mode continuation\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"30942\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_pythia_v2.log\", \"submitted_at\": \"2026-05-17T11:48:32.895Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_wiki_pythia\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"git_commit\": \"0b10b43\", \"checkpoint_source\": \"N/A (generation experiment, not eval)\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 5809.8, \"gpu_hours\": 1.61}, \"reproduce\": {\"finished_at\": \"2026-05-17T13:15:30.480Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:15:32.903668+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.975, \"auc_1v2\": 0.5846, \"auc_2v3\": 0.5445, \"auc_3v4\": 0.5205, \"auc_4v5\": 0.5168, \"jsd_0v1\": 0.080065, \"jsd_1v2\": 0.007773, \"ordinal_acc\": 0.3503}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_pythia_v2/\", \"completed_at\": \"2026-05-17T13:25:22.734Z\"}, \"exp_wiki_olmo_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:40:38.784Z\", \"updated_at\": \"2026-05-17T13:23:57.369Z\", \"hypothesis\": \"Cross-model Wikipedia K* validation (v2 fix): OLMo-1B continuation on Wikipedia 的 K* 是否 = 2？使用独立 data_dir 避免 v1 的 data reuse bug，让 pipeline 用 OLMo 重新生成 depth 1-5。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_wiki_olmo\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path .../allenai/OLMo-1B-hf --generation_mode continuation\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"31084\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_olmo_v2.log\", \"submitted_at\": \"2026-05-17T11:48:36.028Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_wiki_olmo\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"git_commit\": \"0b10b43\", \"checkpoint_source\": \"N/A (generation experiment, not eval)\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 5721.3, \"gpu_hours\": 1.59}, \"reproduce\": {\"finished_at\": \"2026-05-17T13:08:49.908Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:08:52.662189+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9932, \"auc_1v2\": 0.4986, \"auc_2v3\": 0.5012, \"auc_3v4\": 0.5057, \"auc_4v5\": 0.5009, \"jsd_0v1\": 0.1688, \"ordinal_acc\": 0.3227}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_olmo_v2/\", \"completed_at\": \"2026-05-17T13:23:57.369Z\"}, \"exp_arXiv_olmo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:53:55.374Z\", \"updated_at\": \"2026-05-17T12:28:50.616Z\", \"hypothesis\": \"Cross-model arXiv K* validation: OLMo-1B continuation on arXiv abstracts 的 K* 是否 = 3（与 exp-024 Qwen 和 exp-025 Pythia 一致）？验证 structured domain K*=3 跨第三个模型架构（OLMo）的稳定性。2200 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_024_arxiv_domain\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T10:59:47.281Z\", \"finished_at\": \"2026-05-17T12:11:06.144Z\", \"training_hours\": 1.19}, \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir data/exp_arXiv_olmo --results_dir results/exp_arXiv_olmo --num_samples 2200 --max_depth 5 --batch_size 16 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"26733\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_olmo.log\", \"submitted_at\": \"2026-05-17T11:23:00.352Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_arXiv_olmo (seed from exp_024_arxiv/depth_0.jsonl)\", \"data_count\": 2200, \"model_name\": \"OLMo-1B-hf\", \"seed\": 42, \"checkpoint_source\": \"pretrained:allenai/OLMo-1B-hf\", \"eval_data\": \"arXiv abstracts depth 0-5, scorer=Qwen2.5-1.5B\", \"wall_clock_seconds\": 3950.3, \"gpu_hours\": 1.1}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9958, \"auc_1v2\": 0.5034, \"auc_2v3\": 0.5069, \"auc_3v4\": 0.5021, \"auc_4v5\": 0.5037, \"jsd_0v1\": 0.329, \"ordinal_acc\": 0.33}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_olmo/\", \"completed_at\": \"2026-05-17T12:28:50.616Z\"}, \"exp_wiki_olmo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:01.835Z\", \"updated_at\": \"2026-05-17T11:40:31.501Z\", \"hypothesis\": \"OLMo-1B continuation on Wikipedia domain will show K*=2 depth saturation pattern consistent with Qwen2.5-1.5B, demonstrating cross-model generality of the distinguishability decay phenomenon.\", \"parent\": \"exp_023_domain_ablation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-17T10:59:50.182Z\"}, \"spec\": {\"command\": \"python scripts/run_pipeline.py ...\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"27620\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_olmo.log\", \"submitted_at\": \"2026-05-17T11:23:10.688Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"git_commit\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf\", \"eval_data\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"wall_clock_seconds\": 1040.8, \"gpu_hours\": 0.29}, \"conclusion\": \"failed\", \"notes\": \"INVALID: data reuse bug. Shared data_path /root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/ with exp-023 (Qwen). Pipeline skip-if-exists logic reused Qwen-generated depth files instead of generating with OLMo. Results identical to exp-023. M002 lesson: each experiment must use independent data directory.\", \"checkpoint_path\": \"N/A (invalid run)\", \"log_path\": \"/root/runs/gen-depth-contamination/exp_wiki_olmo.log\", \"completed_at\": \"2026-05-17T11:40:31.501Z\"}, \"exp_wiki_pythia\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:00.154Z\", \"updated_at\": \"2026-05-17T11:40:30.671Z\", \"hypothesis\": \"Pythia-1.4B continuation on Wikipedia domain will show K*=2 depth saturation pattern consistent with Qwen2.5-1.5B, demonstrating cross-model generality of the distinguishability decay phenomenon.\", \"parent\": \"exp_023_domain_ablation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-17T10:59:49.483Z\"}, \"spec\": {\"command\": \"python scripts/run_pipeline.py ...\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"26873\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_pythia.log\", \"submitted_at\": \"2026-05-17T11:23:03.344Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"git_commit\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79\", \"eval_data\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"wall_clock_seconds\": 1047.3, \"gpu_hours\": 0.29}, \"conclusion\": \"failed\", \"notes\": \"INVALID: data reuse bug. Shared data_path /root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/ with exp-023 (Qwen). Pipeline skip-if-exists logic reused Qwen-generated depth files instead of generating with Pythia. Results identical to exp-023 (1v2=0.6193, K*=2). M002 lesson: each experiment must use independent data directory.\", \"checkpoint_path\": \"N/A (invalid run)\", \"log_path\": \"/root/runs/gen-depth-contamination/exp_wiki_pythia.log\", \"completed_at\": \"2026-05-17T11:40:30.671Z\"}, \"exp_009_dose_response\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:17:38.441Z\", \"updated_at\": \"2026-05-17T10:24:24.214Z\", \"hypothesis\": \"Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下，graduated filtering 相对 binary filtering 的收益是否随 contamination 增加而扩大？验证 C3 (graduated filtering superiority) 在不同 contamination severity 下的 robustness。3 ratios × 3 strategies (no-filter/binary/graduated) × 5 seeds, continued pretraining Qwen2.5-1.5B, eval MMLU+HellaSwag.\", \"spec\": {\"command\": \"exp009_dose_response.py --ratio {0.1,0.3,0.5}\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": \"0-4\", \"checkpoint_source\": \"N/A (continued pretraining from base)\", \"eval_data\": \"MMLU + HellaSwag (lm-eval-harness)\"}, \"metrics\": {\"total_runs\": 45, \"seeds\": 5, \"ratios\": [0.1, 0.3, 0.5], \"strategies\": [\"no_filter\", \"binary_ours\", \"graduated\"], \"cross_ratio_finding\": \"Binary filtering consistently best across all ratios. Graduated filtering = no_filter at every ratio. Effect size of binary advantage increases with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp). Original C3 hypothesis (graduated > binary) rejected.\", \"gpu_hours_total\": 9.9}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp009_v3_partial_10_30.json\", \"completed_at\": \"2026-05-17T10:24:24.214Z\"}, \"exp_009_dose_50pct_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:13:08.251Z\", \"updated_at\": \"2026-05-17T10:23:52.356Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && python scripts/exp009_dose_response.py --ratio 0.5 --device cuda:0 --num_seeds 5\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"4404\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_50pct_v3.log\", \"submitted_at\": \"2026-05-17T07:05:48.783Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11883.6, \"gpu_hours\": 3.3}, \"hypothesis\": \"50% synthetic injection 下 graduated filtering 应展现最大优势 >=2pp MMLU（v3: fix OOM, auto batch + offline）。半数数据为合成时 binary 激进丢弃导致数据饥饿。\", \"parent\": \"exp_009_dose_50pct_v2\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6063±0.0013\", \"hellaswag\": \"0.6680±0.0005\"}, \"binary_ours\": {\"mmlu\": \"0.6088±0.0011\", \"hellaswag\": \"0.6731±0.0004\"}, \"graduated\": {\"mmlu\": \"0.6062±0.0009\", \"hellaswag\": \"0.6679±0.0002\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0025, \"p_mmlu\": 0.0377, \"delta_hellaswag\": 0.0051, \"p_hellaswag\": 2e-05}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.0026, \"p_mmlu\": 0.0257, \"delta_hellaswag\": -0.0052, \"p_hellaswag\": 3e-05}, \"graduated_vs_nofilter\": {\"delta_mmlu\": -0.0001, \"p_mmlu\": 0.89, \"delta_hellaswag\": -0.0001, \"p_hellaswag\": 0.706}}, \"key_finding\": \"Binary significantly best (HellaSwag p<0.001). Graduated = no_filter exactly.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/ratio_50/\", \"completed_at\": \"2026-05-17T10:23:52.356Z\"}, \"exp_009_dose_30pct_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:13:06.603Z\", \"updated_at\": \"2026-05-17T10:23:51.631Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && python scripts/exp009_dose_response.py --ratio 0.3 --device cuda:0 --num_seeds 5\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"4327\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_30pct_v3.log\", \"submitted_at\": \"2026-05-17T07:05:47.584Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11884.0, \"gpu_hours\": 3.3}, \"hypothesis\": \"30% synthetic injection 下 graduated filtering 优势应 >=1pp MMLU（v3: fix OOM, auto batch + offline）。更高污染率下 binary 丢弃更多可用 gen-1 数据。\", \"parent\": \"exp_009_dose_30pct_v2\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6069±0.0007\", \"hellaswag\": \"0.6664±0.0020\"}, \"binary_ours\": {\"mmlu\": \"0.6082±0.0012\", \"hellaswag\": \"0.6725±0.0007\"}, \"graduated\": {\"mmlu\": \"0.6072±0.0008\", \"hellaswag\": \"0.6665±0.0014\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0013, \"p_mmlu\": 0.0739, \"delta_hellaswag\": 0.0061, \"p_hellaswag\": 0.0036}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.001, \"p_mmlu\": 0.3018, \"delta_hellaswag\": -0.006, \"p_hellaswag\": 0.0009}, \"graduated_vs_nofilter\": {\"delta_mmlu\": 0.0003, \"p_mmlu\": 0.6638, \"delta_hellaswag\": 0.0002, \"p_hellaswag\": 0.6646}}, \"key_finding\": \"Binary best on HellaSwag (p=0.004). Graduated = no_filter.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/ratio_30/\", \"completed_at\": \"2026-05-17T10:23:51.631Z\"}, \"exp_009_dose_10pct_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:13:04.692Z\", \"updated_at\": \"2026-05-17T10:23:50.749Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && python scripts/exp009_dose_response.py --ratio 0.1 --device cuda:0 --num_seeds 5\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"4187\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_10pct_v3.log\", \"submitted_at\": \"2026-05-17T07:05:45.840Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11884.9, \"gpu_hours\": 3.3}, \"hypothesis\": \"10% synthetic injection 下 graduated filtering 应比 binary 保留 >=0.5pp MMLU（v3: fix OOM, auto batch + offline）。低污染时 gen-1 有训练价值，binary 全丢造成数据损失。\", \"parent\": \"exp_009_dose_10pct_v2\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6058±0.0002\", \"hellaswag\": \"0.6689±0.0007\"}, \"binary_ours\": {\"mmlu\": \"0.6079±0.0005\", \"hellaswag\": \"0.6727±0.0008\"}, \"graduated\": {\"mmlu\": \"0.6066±0.0011\", \"hellaswag\": \"0.6700±0.0015\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0021, \"p_mmlu\": 0.001, \"delta_hellaswag\": 0.0038, \"p_hellaswag\": 0.0017}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.0014, \"p_mmlu\": 0.0917, \"delta_hellaswag\": -0.0027, \"p_hellaswag\": 0.0399}, \"graduated_vs_nofilter\": {\"delta_mmlu\": 0.0008, \"p_mmlu\": 0.2706, \"delta_hellaswag\": 0.0011, \"p_hellaswag\": 0.0611}}, \"key_finding\": \"Binary best. Graduated ≈ no_filter.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/ratio_10/\", \"completed_at\": \"2026-05-17T10:23:50.749Z\"}, \"exp_027_retrain_bootstrap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:43:03.273Z\", \"updated_at\": \"2026-05-17T08:18:53.724Z\", \"hypothesis\": \"Retrain-chain 的 pairwise AUC（0v1 到 3v4）在 10000-iteration bootstrap 95% CI 下均显著高于 θ=0.60，确认 K*≥4 具有统计严格性。\", \"parent\": \"exp_008_retrain_chain_v2\", \"spec\": {\"command\": \"python scripts/exp027_retrain_bootstrap.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/features/exp_008_retrain_chain_v2_features.csv\", \"data_count\": 5000, \"model_name\": \"LightGBM (bootstrap analysis)\", \"seed\": 42, \"checkpoint_source\": \"exp_008_retrain_chain_v2 (retrain-chain AUC data)\", \"eval_data\": \"exp_008_retrain_chain_v2 pairwise depth features (0v1, 1v2, 2v3, 3v4)\"}, \"metrics\": {\"bootstrap_iterations\": 10000, \"pairs\": {\"0v1\": {\"auc_point\": 0.9847, \"ci_lower\": 0.9828, \"ci_upper\": 0.9864, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"1v2\": {\"auc_point\": 0.9482, \"ci_lower\": 0.9443, \"ci_upper\": 0.952, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"2v3\": {\"auc_point\": 0.8885, \"ci_lower\": 0.8829, \"ci_upper\": 0.894, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"3v4\": {\"auc_point\": 0.7977, \"ci_lower\": 0.7903, \"ci_upper\": 0.8051, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}}, \"key_finding\": \"All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp027_retrain_bootstrap.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp027_retrain_bootstrap.txt\", \"completed_at\": \"2026-05-17T08:18:53.724Z\"}, \"exp_026_feature_stability_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:09:57.776Z\", \"updated_at\": \"2026-05-17T08:15:28.177Z\", \"hypothesis\": \"Prompt-chain K*=2 边界对 feature 子集选择 robust：即使从 15D 中随机抽取 5/8/10 维子集，Pythia-1.4B prompt-chain 1v2 AUC（baseline ~0.654）仍 > θ=0.60，证明 K*=2 不依赖特定特征组合。\", \"parent\": \"exp_026_feature_stability\", \"metrics\": {\"data_source\": \"exp_001_pythia prompt-chain (K*=2)\", \"results\": {\"15D\": {\"num_tested\": 1, \"num_pass\": 1, \"min_1v2_auc\": 0.6262, \"mean_1v2_auc\": 0.6262}, \"10D\": {\"num_tested\": 5, \"num_pass\": 5, \"min_1v2_auc\": 0.6153, \"mean_1v2_auc\": 0.6191}, \"8D\": {\"num_tested\": 5, \"num_pass\": 5, \"min_1v2_auc\": 0.6056, \"mean_1v2_auc\": 0.6159}, \"5D\": {\"num_tested\": 5, \"num_pass\": 2, \"min_1v2_auc\": 0.5856, \"mean_1v2_auc\": 0.5998}, \"3D_top3\": {\"num_tested\": 1, \"num_pass\": 0, \"min_1v2_auc\": 0.5871, \"mean_1v2_auc\": 0.5871}}, \"key_finding\": \"8+ features sufficient for robust K*=2 (all pass θ=0.60). 5D fragile (2/5 pass). Top-3 alone fails. Feature diversity matters at the K* boundary.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability_v2.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability_v2.json\", \"spec\": {\"command\": \"python scripts/exp026_feature_stability.py --data_source exp_001_pythia\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/features/exp_001_pythia_features.csv\", \"data_count\": 5000, \"model_name\": \"LightGBM\", \"seed\": 42, \"checkpoint_source\": \"exp_001_pythia_depth (prompt-chain features)\", \"eval_data\": \"exp_001_pythia prompt-chain 1v2 features (15D statistical features)\"}, \"completed_at\": \"2026-05-17T08:15:28.177Z\"}, \"exp_026_feature_stability\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:43:01.256Z\", \"updated_at\": \"2026-05-17T08:10:04.334Z\", \"hypothesis\": \"K*=2 对 feature 子集选择 robust：即使从 15D 特征中随机抽取 5/8/10 维子集，1v2 AUC 仍 > θ=0.60，证明 K* 边界不依赖特定特征组合（ad-hoc feature 防御）。\", \"parent\": \"exp_B_14d_ablation\", \"metrics\": {\"data_source\": \"exp_016_qwen_base (prompt-chain, K*=2)\", \"results\": {\"15D\": {\"num_tested\": 1, \"num_kstar_2\": 1, \"min_1v2_auc\": 0.6262, \"mean_1v2_auc\": 0.6262}, \"10D\": {\"num_tested\": 5, \"num_kstar_2\": 5, \"min_1v2_auc\": 0.6153, \"mean_1v2_auc\": 0.6191}, \"8D\": {\"num_tested\": 5, \"num_kstar_2\": 5, \"min_1v2_auc\": 0.6056, \"mean_1v2_auc\": 0.6159}, \"5D\": {\"num_tested\": 5, \"num_kstar_2\": 2, \"min_1v2_auc\": 0.5856, \"mean_1v2_auc\": 0.5998}, \"3D_top3\": {\"num_tested\": 1, \"num_kstar_2\": 0, \"min_1v2_auc\": 0.5871, \"mean_1v2_auc\": 0.5871}}, \"all_above_theta\": false, \"key_finding\": \"Feature selection MATTERS at K*=2 boundary. 15D/10D/8D all robust (min 1v2 AUC > 0.60). 5D random subsets: only 2/5 pass θ=0.60 (min=0.5856). Top-3 features alone (0.5871) fail θ. Contrast with retrain-chain (K*=4) where all subsets trivially passed (min=0.8314).\", \"previous_run_note\": \"v1 used retrain-chain data (K*=4), where all subsets trivially passed with min 1v2 AUC=0.8314. v2 uses prompt-chain data (K*=2) to test boundary robustness.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability.json\", \"spec\": {\"command\": \"python scripts/exp026_feature_stability.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/\", \"data_count\": 5000, \"model_name\": \"LightGBM (feature subset ablation)\", \"seed\": 42, \"checkpoint_source\": \"exp_008_retrain_chain scored features\", \"eval_data\": \"retrain-chain 15D features depth 0-4\"}, \"completed_at\": \"2026-05-17T08:06:40.583Z\"}, \"exp_027\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:09:21.384Z\", \"updated_at\": \"2026-05-17T08:10:03.298Z\", \"hypothesis\": \"Document-level bootstrap CI (10000 iterations) on exp-008 v2 retrain-chain data will confirm that all 4 pairwise AUCs have CI_lower > theta=0.60, supporting K*>=4 with statistical significance.\", \"conclusion\": \"success\", \"checkpoint_path\": \"n/a\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp027.log\", \"completed_at\": \"2026-05-17T08:09:54.196Z\", \"metrics\": {\"kstar_ci\": 4, \"0v1_auc\": 0.9847, \"0v1_ci\": [0.9828, 0.9864], \"0v1_perm_p\": 0.0001, \"1v2_auc\": 0.9482, \"1v2_ci\": [0.9443, 0.952], \"1v2_perm_p\": 0.0001, \"2v3_auc\": 0.8885, \"2v3_ci\": [0.8829, 0.894], \"2v3_perm_p\": 0.0001, \"3v4_auc\": 0.7977, \"3v4_ci\": [0.7903, 0.8051], \"3v4_perm_p\": 0.0001, \"all_ci_lower_above_theta\": true}}, \"exp_005_degradation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T02:40:12.117Z\", \"updated_at\": \"2026-05-17T02:57:38.303Z\", \"spec\": {\"command\": \"python scripts/run_exp005_degradation.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output_dir results_exp005_degradation\", \"server\": \"autodl-4090d\", \"script_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/run_exp005_degradation.py\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation\", \"data_count\": 15000, \"model_name\": \"Pythia-1.4B / OLMo-1B / Qwen-1.5B (3-model comparison)\", \"seed\": 42, \"input_dirs\": [\"results_exp001_pythia\", \"results_exp002_olmo\", \"data\"], \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_005_degradation.log\"}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json\", \"metrics\": {\"cross_model_kendall_tau_by_first_auc\": {\"Pythia_vs_OLMo\": 0.733, \"Pythia_vs_Qwen_rewrite\": 0.467, \"Pythia_vs_Qwen_cont\": 0.695, \"OLMo_vs_Qwen_rewrite\": 0.429, \"OLMo_vs_Qwen_cont\": 0.543, \"Qwen_rewrite_vs_Qwen_cont\": 0.733}, \"cross_model_kendall_tau_by_avg_auc\": {\"Pythia_vs_OLMo\": 0.8476, \"Pythia_vs_Qwen_cont\": 0.7524, \"OLMo_vs_Qwen_cont\": 0.6762}, \"cross_model_spearman_rho_single_feature_auc\": {\"Pythia_vs_OLMo\": 0.95, \"Pythia_vs_Qwen_cont\": 0.9143, \"OLMo_vs_Qwen_cont\": 0.85, \"metric_definition\": \"Spearman ρ on per-feature AUC rankings (each feature independently classifies depth pairs)\"}, \"4model_tau_mean_continuation_by_first_auc\": 0.657, \"4model_tau_mean_all_by_first_auc\": 0.6, \"generation_mode_delta\": {\"Pythia_vs_Qwen\": \"+0.228\", \"OLMo_vs_Qwen\": \"+0.114\"}, \"top3_features_ranking_by_first_auc\": {\"Pythia\": [\"surp_d1_std\", \"surp_d2_std\", \"surp_std\"], \"OLMo\": [\"surp_std\", \"surp_d1_std\", \"surp_d2_std\"], \"Qwen_rewrite\": [\"freq_entropy\", \"surp_std\", \"surp_d1_std\"], \"Qwen_cont\": [\"surp_d1_std\", \"surp_std\", \"surp_d2_std\"]}, \"shared_top_discriminators\": \"surp_d1_std, surp_std, surp_d2_std shared across all architectures (single-feature AUC ranking)\", \"degradation_ordering_consistency\": \"Strong cross-model consistency (ρ≥0.85) on single-feature AUC ranking under controlled generation mode.\", \"residual_architecture_effect\": \"Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\", \"limitation_1v2_weakness\": \"depth-pair level consistency weakest at 1v2 (τ~0.37), near-generational feature importance ordering varies more across models\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:40:50.885Z\", \"notes\": \"4-model τ matrix complete. Generation mode confirmed as primary driver of Qwen divergence (Δτ=+0.23 for Pythia pair). Residual architecture effect ~30-40%. C2 claim: degradation ordering largely consistent under same generation mode, with noted architecture residuals.\", \"hypothesis\": \"递归生成文本在统计特征空间中呈现单调退化趋势（如 perplexity 上升、词汇多样性下降），且退化速率在 K*=2 后显著减缓，这解释了为什么分类器在深代后失去区分力。\", \"parent\": \"mvp_pilot_sat_v1\"}, \"exp_024_arxiv_domain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:43:59.323Z\", \"updated_at\": \"2026-05-17T02:57:37.559Z\", \"hypothesis\": \"Domain ablation: arXiv abstracts 数据下 K*=2 是否成立？验证 K* 跨数据域（C4 vs Wikipedia vs arXiv）的稳定性。Qwen2.5-1.5B base, continuation, nucleus p=0.95 T=1.0, 5K docs, depth 0-5。\", \"spec\": {\"command\": \"bash scripts/exp024_arxiv_domain.sh\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"pid\": 46766, \"log_path\": \"~/runs/gen-depth-contamination/exp_024_arxiv_domain.log\", \"submitted_at\": \"2026-05-16T14:44:07.168Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/\", \"data_count\": 2200, \"model_name\": \"Qwen2.5-1.5B (base)\", \"seed\": 42, \"wall_clock_seconds\": 9545.8, \"gpu_hours\": 2.65}, \"notes\": \"2026-05-16 15:05 重启成功。PID 48295, cuda:2, 73% util。修复：depth_0.jsonl 已有 2200 行 arXiv 数据，prepare_seed_data 行数检查通过后跳过 C4 下载，HF_DATASETS_OFFLINE=1 不再冲突。n_docs=2200。预计 ~20 min 完成剩余 depth。\", \"metrics\": {\"K_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9946, \"1v2\": 0.858, \"2v3\": 0.6427, \"3v4\": 0.5437, \"4v5\": 0.5294}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9946, \"ci_lower\": 0.9929, \"ci_upper\": 0.9961, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.858, \"ci_lower\": 0.848, \"ci_upper\": 0.8679, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.6427, \"ci_lower\": 0.6275, \"ci_upper\": 0.6575, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5437, \"ci_lower\": 0.5276, \"ci_upper\": 0.5598, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5294, \"ci_lower\": 0.5133, \"ci_upper\": 0.5455, \"perm_p\": 0.0006}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_024_arxiv_domain.log\", \"completed_at\": \"2026-05-16T17:23:12.939Z\", \"parent\": \"exp_023_domain_ablation\"}, \"exp_017_qwen_continuation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:41:22.423Z\", \"updated_at\": \"2026-05-17T02:57:37.021Z\", \"hypothesis\": \"Continuation mode 的 K* 应等于 rewrite mode（K*=2），因为 K* 饱和边界是递归生成的文本固有属性，与生成模式（续写 vs 改写）无关——两种模式在深代时都收敛到相同的统计吸引子。\", \"notes\": \"dry-run passed 2026-05-13: model OK (2.9G safetensors), env OK (torch=2.10.0+cu128, transformers=4.57.6), dirs auto-create. Submit command prepared. 等 exp-002 完成后立即提交。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"23758\", \"log_path\": \"~/runs/gen-depth-contamination/exp_017_qwen_continuation.log\", \"submitted_at\": \"2026-05-13T02:35:15Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"max_depth\": 5, \"generation_mode\": \"continuation\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont/\", \"wall_clock_seconds\": 13305.8, \"gpu_hours\": 3.7}, \"log_path\": \"/root/runs/gen-depth-contamination/exp_017_qwen_continuation.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont/\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9972, \"1v2\": 0.6114, \"2v3\": 0.5609, \"3v4\": 0.5408, \"4v5\": 0.5139}, \"pairwise_jsd\": {\"0v1\": 0.28627, \"1v2\": 0.005107, \"2v3\": 0.003603, \"3v4\": 0.003395, \"4v5\": 0.003085}, \"ordinal_mae\": 1.1547, \"ordinal_accuracy\": 0.3819, \"top3_features\": [\"freq_entropy\", \"surp_mean\", \"surp_std\"]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T06:17:00.826Z\", \"parent\": \"mvp_pilot_sat_v1\"}, \"exp_012_binary_confidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:32:09.468Z\", \"updated_at\": \"2026-05-17T02:57:36.098Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp012_ppl_depth_correlation.py --device cuda:0 --n_samples 500 --output_dir artifacts/exp012_results\\\"\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"128209\", \"log_path\": \"~/runs/gen-depth-contamination/exp_012_binary_confidence.log\", \"submitted_at\": \"2026-05-15T23:14:10.207Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 489.8, \"gpu_hours\": 0.14}, \"notes\": \"N=500全量运行。Binary confidence与depth的Spearman ρ弱到中等(|ρ|=0.06-0.46)，6-class accuracy全部≤random baseline。关键发现：0v1 pairwise AUC极高(0.99+)但deeper pairs塌缩到~0.5，证明binary detector只捕捉human/AI边界，无法区分generational depth。Hypothesis验证成功。可视化已生成(exp012_confidence_vs_depth.pdf)。\", \"hypothesis\": \"Binary detector confidence（DivEye log-PPL、Binoculars ratio）与 true generational depth 相关性弱（Spearman rho < 0.3），因为这些检测器将所有合成文本折叠为单一类别，无法区分 gen-1 和 gen-3+，暴露 binary 范式的信息损失。\", \"reproduce\": {\"finished_at\": \"2026-05-15T23:20:30.036Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:20:30.983764+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp012_results/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_012_binary_confidence.log\", \"completed_at\": \"2026-05-15T23:22:19.966Z\", \"metrics\": {\"n_samples\": 500, \"generators\": [\"qwen-rewrite\", \"pythia-1.4b\", \"olmo-1b\", \"qwen-cont\"], \"6class_accuracy\": {\"qwen-rewrite\": 0.1987, \"pythia-1.4b\": 0.1303, \"olmo-1b\": 0.127, \"qwen-cont\": 0.1833, \"random_baseline\": 0.1667}, \"spearman_rho\": {\"qwen-rewrite\": {\"log_ppl_ref\": -0.1233, \"log_ppl_obs\": 0.0815, \"ppl_ratio\": 0.1185}, \"pythia-1.4b\": {\"log_ppl_ref\": -0.2972, \"log_ppl_obs\": -0.4529, \"ppl_ratio\": -0.392}, \"olmo-1b\": {\"log_ppl_ref\": -0.378, \"log_ppl_obs\": -0.4614, \"ppl_ratio\": -0.4068}, \"qwen-cont\": {\"log_ppl_ref\": -0.3887, \"log_ppl_obs\": -0.162, \"ppl_ratio\": -0.058}}, \"binary_detector_kstar\": 1, \"obd_kstar\": 2, \"auc_non_monotonic\": true, \"key_finding\": \"Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but practically weak). AUC non-monotonic — binary detectors cannot maintain depth ordering. Confirms binary confidence ≠ depth estimation.\"}, \"parent\": \"mvp_pilot_sat_v1\"}, \"exp_C_permutation_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:26.152Z\", \"updated_at\": \"2026-05-17T02:57:35.128Z\", \"hypothesis\": \"10K permutation resamples 不应改变任何 K* 结论（所有 p < 0.01 的 pair 仍应 p < 0.01），确认 500 resamples 已有足够精度，K*=2 结论的统计基础稳固。\", \"spec\": {\"command\": \"python scripts/exp_C_permutation_10k.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data + data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 20000, \"model_name\": \"N/A (CPU: permutation test)\", \"seed\": 42, \"note\": \"10K permutation resamples replacing 500, per depth pair per model\"}, \"conclusion\": \"success\", \"metrics\": {\"resamples\": 10000, \"all_boundary_pairs_p\": \"<0.0001\", \"key_finding\": \"10K permutation confirms all boundary p-values well below 0.01. FR-11 resolved.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_C_permutation_10k.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_C_permutation_10k.json\", \"completed_at\": \"2026-05-15T11:20:30.088Z\", \"parent\": \"exp_007_bootstrap_ci\"}, \"exp_009_dose_50pct_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:14:53.711Z\", \"updated_at\": \"2026-05-17T02:57:30.391Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.5 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"86342\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_50pct_v2.log\", \"submitted_at\": \"2026-05-16T23:14:53.568Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_50/\", \"data_count\": 10000, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 4079.2, \"gpu_hours\": 1.13}, \"hypothesis\": \"50% synthetic injection 下 graduated filtering 应展现最大优势 >=2pp MMLU（v2: fix HF mirror）。机制同 v1：半数数据为合成时 binary 激进丢弃导致数据饥饿。\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA OOM during lm_eval MMLU 5-shot (batch_size=8, logits tensor exceeds 24GB)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:52.736Z\", \"parent\": \"exp_009_dose_50pct\"}, \"exp_009_dose_30pct_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:14:51.739Z\", \"updated_at\": \"2026-05-17T02:57:29.467Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.3 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"86196\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_30pct_v2.log\", \"submitted_at\": \"2026-05-16T23:14:51.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_30/\", \"data_count\": 7142, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 4080.4, \"gpu_hours\": 1.13}, \"hypothesis\": \"30% synthetic injection 下 graduated filtering 优势应 >=1pp MMLU（v2: fix HF mirror）。机制同 v1：更高污染率下 binary 丢弃更多可用 gen-1 数据。\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA OOM during lm_eval MMLU 5-shot (batch_size=8, logits tensor exceeds 24GB)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:51.942Z\", \"parent\": \"exp_009_dose_30pct\"}, \"exp_009_dose_10pct_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:14:49.850Z\", \"updated_at\": \"2026-05-17T02:57:28.507Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.1 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"86049\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_10pct_v2.log\", \"submitted_at\": \"2026-05-16T23:14:49.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_10/\", \"data_count\": 5555, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 4081.2, \"gpu_hours\": 1.13}, \"hypothesis\": \"10% synthetic injection 下 graduated filtering 应比 binary 保留 >=0.5pp MMLU（v2: fix HF mirror）。机制同 v1：低污染时 gen-1 有训练价值，binary 全丢造成数据损失。\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA OOM during lm_eval MMLU 5-shot (batch_size=8, logits tensor exceeds 24GB)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:50.958Z\", \"parent\": \"exp_009_dose_10pct\"}, \"exp_009_dose_50pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:22:14.703Z\", \"updated_at\": \"2026-05-17T02:57:28.163Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.5 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"81595\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_50pct.log\", \"submitted_at\": \"2026-05-16T22:23:09.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_50/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 7180.5, \"gpu_hours\": 1.99}, \"hypothesis\": \"50% synthetic injection 下，graduated filtering 应展现最大优势（>=2pp MMLU），因为半数数据为合成时 binary filtering 的激进丢弃导致严重数据饥饿，而 graduated 保留 gen-1 维持训练集规模。\", \"conclusion\": \"failed\", \"failure_reason\": \"HF Hub network instability (httpx client closed)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:50.142Z\", \"parent\": \"exp_006_graduated_filtering\"}, \"exp_009_dose_30pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:22:12.817Z\", \"updated_at\": \"2026-05-17T02:57:27.096Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.3 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"81453\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_30pct.log\", \"submitted_at\": \"2026-05-16T22:23:07.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_30/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 7181.6, \"gpu_hours\": 1.99}, \"hypothesis\": \"30% synthetic injection 下，graduated filtering 优势应大于 10% 场景（>=1pp MMLU），因为更高污染率意味着 binary filtering 丢弃更多可用 gen-1 数据，而 graduated 仅移除 gen-2+ 有害部分。\", \"conclusion\": \"failed\", \"failure_reason\": \"HF Hub network instability (httpx client closed)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:49.399Z\", \"parent\": \"exp_006_graduated_filtering\"}, \"exp_009_dose_10pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:22:10.924Z\", \"updated_at\": \"2026-05-17T02:57:26.151Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.1 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"81311\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_10pct.log\", \"submitted_at\": \"2026-05-16T22:23:05.447Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_10/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 7183.1, \"gpu_hours\": 2.0}, \"hypothesis\": \"10% synthetic injection 下，graduated filtering 应比 binary filtering 保留更多 MMLU 性能（>=0.5pp），因为低污染场景中 gen-1 文本仍有训练价值，binary 全部丢弃造成不必要的数据损失。\", \"conclusion\": \"failed\", \"failure_reason\": \"HF Hub network instability (httpx client closed)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:48.595Z\", \"parent\": \"exp_006_graduated_filtering\"}, \"exp_kstar_theta\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:08:01.704Z\", \"updated_at\": \"2026-05-17T02:56:51.877Z\", \"hypothesis\": \"K*(θ) 曲线在 θ∈[0.55,0.65] 存在 plateau（K* 对阈值不敏感），且 Cohen's h 在 depth=K* 到 depth=K*+1 间降至 < 0.2（小效应量），为 θ=0.60 提供非任意性理论依据。\", \"spec\": {\"command\": \"python scripts/plot_kstar_theta.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/ (bootstrap CI AUCs)\", \"data_count\": 20000, \"model_name\": \"N/A (CPU: K*(θ) visualization)\", \"seed\": \"N/A\", \"note\": \"FR-1 rebuttal: K*(θ) curve for 4 models × 5 depth pairs\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/kstar_theta_curve.pdf\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/plot_kstar_theta.py\", \"metrics\": {\"output_files\": [\"kstar_theta_curve.pdf (32KB)\", \"kstar_theta_curve.png (335KB)\"], \"models\": [\"Qwen-rewrite\", \"Pythia\", \"OLMo\", \"Qwen-cont\"], \"depth_pairs\": 5, \"key_finding\": \"All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5. θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical resolved.\"}, \"completed_at\": \"2026-05-15T15:08:25.181Z\"}, \"exp_022_cross_scorer_matrix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:52:14.132Z\", \"updated_at\": \"2026-05-17T02:56:47.329Z\", \"hypothesis\": \"Self-scoring（generator=scorer）的 K* 和 pairwise AUC 应与 cross-scoring（generator≠scorer）差异 < 0.02，证明 K*=2 不是 scorer-generator familiarity artifact，而是文本本身的可区分性边界。\", \"parent\": \"exp_A_alt_scorer\", \"spec\": {\"command\": \"bash scripts/exp022_cross_scorer_matrix.sh\", \"server\": \"cqa1-22115\", \"data_path\": \"data_exp016_qwen_base + data_exp020_pythia_greedy + data/exp_021_length_256\", \"data_count\": 5000, \"model_name\": \"cross: Qwen2.5-1.5B/Pythia-1.4B/OLMo-1B/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained\", \"eval_data\": \"cross-scorer matrix on existing depth chains\"}, \"notes\": \"2026-05-16 15:05: 双 GPU 并行。cuda:1 跑 2×2 子矩阵 (PID 49787, Qwen-cont/Pythia × Qwen-base/Pythia)。cuda:3 跑 3×4=12 组合 (先跑已缓存模型 6 combo，等下载 Qwen-Instruct/OLMo 后补剩余 6)。OLMo generator 无 depth chain 数据，实际 3 generators × 4 scorers。\", \"conclusion\": \"success\", \"metrics\": {\"total_combos\": 12, \"completed\": 12, \"K_star_distribution\": {\"K2\": 11, \"K1\": 1}, \"matrix\": {\"pythia_greedy×olmo\": {\"K_star\": 2, \"1v2\": 0.8811}, \"pythia_greedy×pythia\": {\"K_star\": 2, \"1v2\": 0.8838}, \"pythia_greedy×qwen_base\": {\"K_star\": 2, \"1v2\": 0.8814}, \"pythia_greedy×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.8818}, \"qwen_base×olmo\": {\"K_star\": 2, \"1v2\": 0.6047}, \"qwen_base×pythia\": {\"K_star\": 2, \"1v2\": 0.617}, \"qwen_base×qwen_base\": {\"K_star\": 2, \"1v2\": 0.6262}, \"qwen_base×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.6273}, \"qwen_cont256×olmo\": {\"K_star\": 2, \"1v2\": 0.6028}, \"qwen_cont256×pythia\": {\"K_star\": 1, \"1v2\": 0.5979}, \"qwen_cont256×qwen_base\": {\"K_star\": 2, \"1v2\": 0.6282}, \"qwen_cont256×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.6072}}, \"key_finding\": \"Scorer independence confirmed: K*=2 in 11/12 combos. Only exception: qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp022_cross_scorer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp022_cross_scorer.log\", \"completed_at\": \"2026-05-16T18:56:44.226Z\"}, \"exp_008_retrain_chain_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:57:55.644Z\", \"updated_at\": \"2026-05-17T00:23:00.448Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp008_retrain_chain.py --device cuda:0\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"77098\", \"log_path\": \"~/runs/gen-depth-contamination/exp_008_retrain_chain_v2.log\", \"submitted_at\": \"2026-05-16T21:57:55.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b + LoRA (rank=16, alpha=32)\", \"seed\": 42, \"checkpoint_source\": \"pretrained + per-generation LoRA fine-tune\", \"eval_data\": \"C4 5K docs, retrain-chain depth 0-4\", \"wall_clock_seconds\": 8704.9, \"gpu_hours\": 2.42}, \"hypothesis\": \"Retrain-chain ecological validity (v2, fix: labels padding bug): Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain K* ≤ prompt-chain K*=2. 每代独立 LoRA fine-tune 1 epoch on 前代输出，再用 fine-tuned model 生成下一代。验证 prompt-chain 是 conservative upper bound。C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_001_pythia_depth\", \"metrics\": {\"k_star\": \">=4\", \"pairwise_auc\": {\"0v1\": 0.9847, \"1v2\": 0.9484, \"2v3\": 0.8888, \"3v4\": 0.7982}, \"pairwise_jsd\": {\"0v1\": 0.17, \"1v2\": 0.12, \"2v3\": 0.064, \"3v4\": 0.04}, \"key_finding\": \"Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic boundary.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/outputs/exp_008_retrain_chain/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T00:23:00.448Z\"}, \"exp-008-retrain-chain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:31:01.383Z\", \"updated_at\": \"2026-05-16T22:16:29.240Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp008_retrain_chain.py --device cuda:0\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"71944\", \"log_path\": \"~/runs/gen-depth-contamination/exp-008-retrain-chain.log\", \"submitted_at\": \"2026-05-16T19:31:01.254Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b + LoRA (rank=16, alpha=32)\", \"seed\": 42, \"checkpoint_source\": \"pretrained + per-generation LoRA fine-tune\", \"eval_data\": \"C4 5K docs, retrain-chain depth 0-4\", \"wall_clock_seconds\": 5771.2, \"gpu_hours\": 1.6}, \"hypothesis\": \"Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain K* ≤ prompt-chain K*=2. 每代独立 LoRA fine-tune 1 epoch on 前代输出，再用 fine-tuned model 生成下一代。验证 prompt-chain 是 conservative upper bound。C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_001_pythia_depth\", \"failure_reason\": \"Traceback → le \\\"/root/miniconda3/lib/python3.12/site-packages/transformers/tokenization_utils_base.py\\\", line 701, in as_tensor return torch.tensor(value, dtype=dtype) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ValueError: expected sequence of length 256 at dim 1 (got 228)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T21:07:12.427Z\", \"notes\": \"2026-05-16: 失败原因——TextDataset.__getitem__ 同时返回变长 input_ids 和 labels，DataCollatorForLanguageModeling 只 pad input_ids，导致 labels 长度不一致无法转 tensor。修复：移除 __getitem__ 中的 labels 字段，让 collator 自动处理。v2 已提交。\"}, \"exp_025_pythia_arxiv\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:16:13.988Z\", \"updated_at\": \"2026-05-16T19:22:57.204Z\", \"hypothesis\": \"Domain × model interaction: Pythia-1.4B on arXiv data 的 K* 是否与 exp-024 (Qwen on arXiv, K*=?) 一致？验证 arXiv domain effect 跨模型一致性，排除 Qwen-specific artifact。Pythia-1.4B continuation, nucleus p=0.95 T=1.0, 2200 docs, depth 0-5, scorer=Qwen2.5-1.5B base。\", \"parent\": \"exp_024_arxiv_domain\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=1 python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --generation_mode continuation --top_p 0.95 --temperature 1.0 --num_samples 2200 --max_depth 5 --batch_size 8 --feat_batch_size 16 --data_dir data/exp_025_pythia_arxiv --results_dir results/exp_025_pythia_arxiv\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"67006\", \"log_path\": \"~/runs/gen-depth-contamination/exp_025_pythia_arxiv.log\", \"submitted_at\": \"2026-05-16T17:59:52.930Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_025_pythia_arxiv/\", \"data_count\": 2200, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_source\": \"pretrained (EleutherAI/pythia-1.4b)\", \"eval_data\": \"arXiv abstracts depth chains (shared seed data from exp-024)\", \"wall_clock_seconds\": 4984.3, \"gpu_hours\": 1.38}, \"reproduce\": {\"finished_at\": \"2026-05-16T18:57:28.981Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:57:30.288692+00:00\"}]}, \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9877, \"1v2\": 0.8047, \"2v3\": 0.6545, \"3v4\": 0.5507, \"4v5\": 0.5287}, \"pairwise_jsd\": {\"0v1\": 0.171338, \"1v2\": 0.057344, \"2v3\": 0.019524, \"3v4\": 0.009917, \"4v5\": 0.008846}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9876, \"ci_lower\": 0.9851, \"ci_upper\": 0.99, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.8047, \"ci_lower\": 0.7934, \"ci_upper\": 0.8162, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.6544, \"ci_lower\": 0.6401, \"ci_upper\": 0.6688, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.55, \"ci_lower\": 0.534, \"ci_upper\": 0.5657, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5284, \"ci_lower\": 0.5122, \"ci_upper\": 0.5443, \"perm_p\": 0.001}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"n_samples\": 2200, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_mean\", \"surp_d1_skew\", \"surp_d1_mean\"], \"ordinal\": {\"MAE\": 0.8518, \"Accuracy\": 0.4545}, \"key_finding\": \"Pythia-1.4B on arXiv yields K*=3, identical to exp-024 (Qwen on arXiv). 2v3 CI lower=0.6401 > θ=0.60. Domain saturation depth is model-invariant for arXiv.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_025_pythia_arxiv/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_025_pythia_arxiv.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T19:22:57.204Z\"}, \"exp_020_pythia_decoding\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:52:13.036Z\", \"updated_at\": \"2026-05-16T17:18:28.366Z\", \"hypothesis\": \"Pythia-1.4B 解码消融：4 个 decoding config (greedy/nuc p=0.9/T=0.7/T=1.2) 的 K* 是否一致？与 exp-003 (Qwen) 平行，验证 decoding 效应跨模型一致性。C4 5K, depth 0-5。\", \"parent\": \"exp_003_decoding_ablation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T04:57:46.476Z\"}, \"spec\": {\"command\": \"nohup bash -c 'CUDA_VISIBLE_DEVICES=2 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache bash scripts/exp020_pythia_decoding.sh' > /tmp/exp020_pythia_decoding.log 2>&1 &\", \"server\": \"cqa1-22115\", \"data_path\": \"data_exp020_pythia_{greedy,nuc09,t07,t12}/\", \"data_count\": 20000, \"model_name\": \"EleutherAI/pythia-1.4b (fp16)\", \"seed\": 42, \"generation_mode\": \"continuation (4 decoding configs: greedy/nuc09/t07/t12)\", \"pid\": 14551, \"log_path\": \"/tmp/exp020_pythia_decoding.log\", \"note\": \"Worker 误用 nohup 而非 submit_training_job，已补注册 cron 监控 (PID 14551)。原 PID 13076 已被 kill。\"}, \"notes\": \"greedy 1v2 AUC=0.8838 调查完成：根因为 Pythia-1.4B greedy 级联重复坍塌（4-gram repeat rate: d0=0.01→d1=0.72→d2=0.81; TTR: d0=0.72→d1=0.19→d2=0.14）。hapax_ratio (d=1.06) 和 low_freq_ratio (d=1.03) 是 top 贡献特征。非 bug，参数正确，无数据泄漏。K*=2 不受影响。建议论文标注为 repetition-dominated regime。| Bootstrap CI (10000 iter): t07 2v3 AUC=0.5939 CI [0.5855, 0.6025] BORDERLINE (CI upper crosses θ); t12 1v2 AUC=0.6170 CI [0.6071, 0.6270] PASS。\", \"conclusion\": \"success\", \"metrics\": {\"greedy\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9992, \"1v2\": 0.8838, \"2v3\": 0.5342, \"3v4\": 0.5228, \"4v5\": 0.5162}}, \"nuc09\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9948, \"1v2\": 0.677, \"2v3\": 0.5549, \"3v4\": 0.5299, \"4v5\": 0.5013}}, \"t07\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9965, \"1v2\": 0.7265, \"2v3\": 0.5941, \"3v4\": 0.5698, \"4v5\": 0.5284}}, \"t12\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9933, \"1v2\": 0.6172, \"2v3\": 0.5226, \"3v4\": 0.517, \"4v5\": 0.5051}}}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp020_pythia_{greedy,nuc09,t07,t12}/\", \"log_path\": \"/tmp/exp020_pythia_decoding.log\", \"completed_at\": \"2026-05-16T14:41:33.153Z\"}, \"exp_021_length_ablation\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T04:52:13.569Z\", \"updated_at\": \"2026-05-16T17:18:21.506Z\", \"hypothesis\": \"文本长度消融：128/256/512 tokens 下 K* 是否稳定？验证 K*=2 不依赖于 256-token 固定长度设定。Qwen2.5-1.5B (base) continuation, C4 5K, depth 0-5。\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T04:57:47.040Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-16T06:23:09.413Z\", \"notes\": \"2026-05-16 retry#2: 用本地 C4 数据修复。数据源=/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/depth_0.jsonl (5000行)，复制到 data/exp_021_length_{128,256,512}/。设置 HF_DATASETS_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 阻断 HF 网络调用，prepare_seed_data 检测到本地文件自动跳过 streaming。PID 20982, tmux session exp_021_length_ablation。\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16: 崩溃原因确认——脚本未执行 `source /etc/network_turbo`，导致 AutoDL 网络代理未启用，HuggingFace C4 数据集下载失败 (RuntimeError: Cannot send a request, as the client has been closed / Errno 99: Cannot assign requested address)。三个长度 (128/256/512) 全部未完成，无任何产出。cuda:3 已空闲。需重跑并修复网络配置。\"}}, \"spec\": {\"command\": \"bash -c \\\"export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/exp021_length_ablation.sh\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"20982\", \"log_path\": \"~/runs/gen-depth-contamination/exp_021_length_ablation.log\", \"submitted_at\": \"2026-05-16T07:13:09.587Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/depth_0.jsonl (local C4, copied to data/exp_021_length_{128,256,512}/)\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (base)\", \"seed\": 42, \"generation_mode\": \"continuation\", \"max_new_tokens\": [128, 256, 512], \"max_depth\": 5, \"batch_size\": 16, \"checkpoint_path\": \"results/exp_021_length_{128,256,512}\", \"description\": \"Retry#2: local C4 data, HF_DATASETS_OFFLINE=1, 3 length configs sequential on cuda:3\", \"wall_clock_seconds\": 29523.5, \"gpu_hours\": 8.2}, \"conclusion\": \"success\", \"metrics\": {\"128tok\": {\"K_star\": 2, \"1v2_auc\": 0.6219}, \"256tok\": {\"K_star\": 2, \"1v2_auc\": 0.6282}, \"512tok\": {\"K_star\": 2, \"1v2_auc\": 0.6073}, \"all_K_star_2\": true, \"bootstrap_ci\": {\"512tok_1v2\": {\"auc\": 0.6073, \"ci_lower\": 0.5979, \"ci_upper\": 0.6166, \"perm_p\": 0.0001, \"verdict\": \"BORDERLINE\"}}}}, \"exp_018_llama8b_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:52:11.229Z\", \"updated_at\": \"2026-05-16T16:18:02.754Z\", \"hypothesis\": \"Cross-family K* 验证：LLaMA-3.1-8B continuation mode 的 K* 是否 = 2？首次超出 Qwen 家族，验证 K* universality 跨模型架构。C4 5K, depth 0-5, scorer=Qwen2.5-1.5B base。\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T04:57:44.549Z\", \"finished_at\": \"2026-05-16T15:35:57.336Z\", \"training_hours\": 10.64}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --generation_mode continuation --num_samples 5000 --max_depth 5 --batch_size 4 --feat_batch_size 8 --data_dir data/exp_018_llama8b --results_dir results/exp_018_llama8b\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0 (RTX 4090D 24GB)\", \"data_path\": \"C4 validation (HuggingFace streaming)\", \"data_count\": 5000, \"model_name\": \"LLaMA-3.1-8B (Meta-Llama-3.1-8B)\", \"scorer\": \"Qwen2.5-1.5B base\", \"seed\": 42, \"generation_mode\": \"continuation\", \"max_depth\": 5, \"batch_size\": 4, \"feat_batch_size\": 8, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_018_llama8b.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b\", \"description\": \"Cross-family K* validation: LLaMA-3.1-8B generates depth chain, Qwen2.5-1.5B base scores surprisal features\"}, \"failure_reason\": \"null — cron 误报，实验实际成功\", \"conclusion\": \"success\", \"pid\": 10403, \"gpu_id\": \"cuda:0\", \"completed_at\": \"2026-05-16T15:35:57.947Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:35:59.527502+00:00\"}]}, \"notes\": \"2026-05-16 日志诊断：实验实际已成功完成(K*=2, AUC 1v2=0.6123)，Pipeline complete 正常退出。被 cron 误判 failed 原因：进程正常结束后 PID 10403 消失，无 sentinel/W&B 信号，监控 5× 检查后 auto-resolve 为 failed。结果文件完整存在于 results/exp_018_llama8b/。应改 conclusion=success。\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9225, \"1v2\": 0.6123, \"2v3\": 0.5274, \"3v4\": 0.5138, \"4v5\": 0.5097}, \"jsd\": {\"0v1\": 0.077, \"1v2\": 0.012, \"2v3\": 0.005}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9224, \"ci_lower\": 0.9174, \"ci_upper\": 0.9272, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6123, \"ci_lower\": 0.6028, \"ci_upper\": 0.6216, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5273, \"ci_lower\": 0.5169, \"ci_upper\": 0.5378, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5168, \"ci_lower\": 0.5062, \"ci_upper\": 0.5275, \"perm_p\": 0.0037}, \"4v5\": {\"auc\": 0.5159, \"ci_lower\": 0.5052, \"ci_upper\": 0.5268, \"perm_p\": 0.0035}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000}}, \"exp_023_domain_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:59:57.643Z\", \"updated_at\": \"2026-05-16T15:25:22.371Z\", \"hypothesis\": \"Domain ablation: Wikipedia 数据下 K*=2 是否成立？验证 K* 跨数据域（C4 vs Wikipedia）的稳定性。Qwen2.5-1.5B base, continuation, nucleus p=0.95 T=1.0, 5K docs, depth 0-5。\", \"spec\": {\"command\": \"bash scripts/exp023_wiki_domain.sh\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"pid\": 39530, \"log_path\": \"~/runs/gen-depth-contamination/exp_023_domain_ablation.log\", \"submitted_at\": \"2026-05-16T12:00:07.999Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (base)\", \"seed\": 42, \"wall_clock_seconds\": 12314.4, \"gpu_hours\": 3.42}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 2, \"1v2_auc\": 0.6193, \"2v3_auc\": 0.5498, \"all_folds_above_060\": true, \"top_feature\": \"freq_entropy\", \"ordinal_accuracy\": 0.377}, \"checkpoint_path\": \"results_exp023_wiki_domain/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_023_domain_ablation.log\", \"completed_at\": \"2026-05-16T15:25:22.371Z\"}, \"exp_019b_mistral_cross_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:22:44.822Z\", \"updated_at\": \"2026-05-16T11:56:59.892Z\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path mistral-7b --scorer_path qwen2.5-1.5b\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"36365\", \"log_path\": \"~/runs/gen-depth-contamination/exp_019b_mistral_cross_scorer.log\", \"submitted_at\": \"2026-05-16T11:23:28.609Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp019b_mistral_cross\", \"data_count\": 5000, \"model_name\": \"mistral-7b-cross-qwen1.5b-scorer\", \"seed\": 42, \"checkpoint_source\": \"exp_019_mistral7b_depth\", \"eval_data\": \"data_exp019b_mistral_cross\", \"wall_clock_seconds\": 1938.5, \"gpu_hours\": 0.54}, \"hypothesis\": \"排除 self-scorer 因素：Mistral-7B depth chain 用 Qwen2.5-1.5B-base 评分后 K* 是否=2？如果 K*=2 则 exp-019 的 K*=1 是 self-scorer artifact；如果 K*=1 则是 Mistral 生成文本的固有特性。\", \"parent\": \"exp_019_mistral7b_depth\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp019b_mistral_cross_scorer\", \"log_path\": \"~/runs/gen-depth-contamination/exp_019b_mistral_cross_scorer.log\", \"completed_at\": \"2026-05-16T11:55:47.111Z\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9209, \"1v2\": 0.5695, \"2v3\": 0.5335, \"3v4\": 0.514, \"4v5\": 0.5184}, \"bootstrap_ci\": {\"0v1\": {\"mean\": 0.9209, \"ci_lower\": 0.9189, \"ci_upper\": 0.9229, \"pass_060\": true}, \"1v2\": {\"mean\": 0.5696, \"ci_lower\": 0.5645, \"ci_upper\": 0.5746, \"pass_060\": false}, \"2v3\": {\"mean\": 0.5335, \"ci_lower\": 0.5283, \"ci_upper\": 0.5382, \"pass_060\": false}, \"3v4\": {\"mean\": 0.514, \"ci_lower\": 0.5063, \"ci_upper\": 0.5213, \"pass_060\": false}, \"4v5\": {\"mean\": 0.5183, \"ci_lower\": 0.5128, \"ci_upper\": 0.5244, \"pass_060\": false}}, \"jsd\": {\"0v1\": 0.08355, \"1v2\": 0.007642, \"2v3\": 0.004752, \"3v4\": 0.004255, \"4v5\": 0.003758}, \"ordinal_mae\": 1.3737, \"ordinal_accuracy\": 0.3179, \"top3_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_d1_mean\"], \"key_finding\": \"Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2 AUC=0.5695 (self-scorer was 0.5935) — cross-scorer LOWER, not higher. Mistral K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact.\"}, \"notes\": \"K*=1 confirmed genuine (not self-scorer artifact). Cross-scorer (Qwen-base) 1v2 AUC=0.5695 CI [0.5645, 0.5746] — 比 self-scorer (0.5935) 更低。换 scorer 后区分度下降，排除 self-scorer inflation 假说。Top-3 features 与 self-scorer 完全一致: freq_entropy, surp_d1_skew, surp_d1_mean。\"}, \"exp_019_mistral7b_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:52:12.077Z\", \"updated_at\": \"2026-05-16T11:28:45.586Z\", \"hypothesis\": \"Cross-family K* 验证：Mistral-7B-v0.3 continuation mode 的 K* 是否 = 2？第二个非 Qwen 家族模型。C4 5K, depth 0-5, scorer=Mistral-7B-v0.3 (self-scorer)。与 exp-001/002/017 self-scoring 方法一致，exp_A_alt_scorer 已证明 scorer 不影响 K*。\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:57:45.553Z\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data_exp019_mistral7b --results_dir results_exp019_mistral7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp019_mistral7b\", \"data_count\": 5000, \"model_name\": \"mistralai/Mistral-7B-v0.3 (fp16)\", \"scorer\": \"Mistral-7B-v0.3 (self-scorer, 与 exp-001/002/017 一致)\", \"seed\": 42, \"generation_mode\": \"continuation\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"pid\": 12147, \"gpu_id\": \"cuda:1\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp019_mistral7b/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/exp019.log\", \"completed_at\": \"2026-05-16T11:17:08.348Z\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9843, \"1v2\": 0.5935, \"2v3\": 0.5402, \"3v4\": 0.5232, \"4v5\": 0.5181}, \"bootstrap_ci_1v2\": {\"ci_lower\": 0.5835, \"ci_upper\": 0.6032, \"p_auc_leq_060\": 0.9017}, \"jsd\": {\"0v1\": 0.124194, \"1v2\": 0.008051, \"2v3\": 0.005047, \"3v4\": 0.004516, \"4v5\": 0.004109}, \"ordinal_mae\": 1.2275, \"ordinal_accuracy\": 0.3567, \"top3_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_d1_mean\"]}, \"notes\": \"K*=1 (非预期的 K*=2)。1v2 AUC=0.5935±0.0054，低于 θ=0.60 阈值仅 0.0065。边界线结果，需 bootstrap CI 确认。0v1 AUC=0.9843 强可区分。Self-scorer (Mistral-7B)。cuda:1 已空闲。\"}, \"exp_016_base_vs_instruct\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:01:55.079Z\", \"updated_at\": \"2026-05-16T05:04:51.120Z\", \"hypothesis\": \"Base vs Instruct K* 对比：Qwen2.5-1.5B (base) continuation mode 的 K* 是否与 exp-017 (Instruct continuation, K*=2) 一致？封堵 \\\"K*=2 是 instruct-tuning 副产物\\\" 攻击面。唯一变量 = base vs instruct。\", \"parent\": \"exp_017_qwen_continuation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westc-26893\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:02:43.478Z\"}, \"completed_at\": \"2026-05-16T03:22:38.539Z\", \"notes\": \"2026-05-16: Resumed on cqa1-22115 (migrated from westc-26893). Depth 0-3 complete, generating depth 4-5. PID=3442 on cuda:0.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16: Resumed on cqa1-22115 (migrated from westc-26893). Depth 0-3 complete, generating depth 4-5. PID=3442 on cuda:0.\"}}, \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data_dir data_exp016_qwen_base --results_dir results_exp016_qwen_base --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B (base, fp16)\", \"seed\": 42, \"generation_mode\": \"continuation\", \"scorer\": \"Qwen2.5-1.5B (base)\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"exp016\", \"log_path\": \"/tmp/exp016.log\", \"note\": \"Retry #1: Resumed on cqa1-22115 after westc-26893 restart. Depth 0-3 migrated via rsync.\", \"checkpoint_source\": \"N/A (standalone generation, not eval)\", \"eval_data\": \"C4 validation 5000 samples\"}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.987, \"1v2\": 0.6262, \"2v3\": 0.5496, \"3v4\": 0.5294, \"4v5\": 0.5182}, \"pairwise_auc_std\": {\"0v1\": 0.0015, \"1v2\": 0.0152, \"2v3\": 0.0067, \"3v4\": 0.0132, \"4v5\": 0.0139}, \"pairwise_jsd\": {\"0v1\": 0.163726, \"1v2\": 0.01081, \"2v3\": 0.005311, \"3v4\": 0.003942, \"4v5\": 0.003522}, \"ordinal_mae\": 1.1691, \"ordinal_accuracy\": 0.3719, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_d1_skew\", \"surp_d1_mean\", \"surp_mean\"], \"n_samples\": 30000, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.987, \"ci_lower\": 0.9853, \"ci_upper\": 0.9885, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.626, \"ci_lower\": 0.6168, \"ci_upper\": 0.6353, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5397, \"ci_upper\": 0.56, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5293, \"ci_lower\": 0.5188, \"ci_upper\": 0.5399, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5181, \"ci_lower\": 0.5075, \"ci_upper\": 0.5288, \"perm_p\": 0.0016}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95% CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015, 0.6213] — no significant base-vs-instruct difference.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base/\", \"log_path\": \"/tmp/exp016.log\"}, \"exp_003_decoding_ablation\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-12T20:06:25.260Z\", \"updated_at\": \"2026-05-16T03:06:04.938Z\", \"hypothesis\": \"解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?）\", \"failure_reason\": \"SSH check failed 5x — last error: Unknown server 'autodl-4090d'. Available: ['westc-26893']\", \"completed_at\": \"2026-05-13T15:35:29.038Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T15:35:30.207607+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:22:20.803872+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: SSH 别名变更 (autodl-4090d → westc-26893)，cron 监控 5 次连不上后标记 failed。初步诊断: 日志在 westc-26893 上可读，config 2 (nucleus_p0.9_t1.0) 已完成并输出 K*=2，config 3 (nucleus_p0.95_t0.7) 在 depth 4 进度 ~90% 时日志截止。实验可能已完成或部分完成。Worker worker_diagnose_exp_003_decoding_ablation_20260513T153757 正在深入诊断。\"}}, \"notes\": \"Server alias 变更 autodl-4090d → westc-26893 导致 cron 误标 failed。实际实验一直正常运行。Config 1 (greedy, K*=2), Config 2 (nuc p=0.9/T=1.0, K*=2), Config 3 (nuc p=0.95/T=0.7, K*=2) 已完成。Config 4 (nuc p=0.95/T=1.2) 运行中。深度分析: 1v2 AUC Δ<0.003 across configs, D016 universality confirmed (all 7 configs > θ=0.60), θ-sensitivity K* profile identical across 3 configs. 分析脚本 scripts/exp003_analyze_all_configs.py 已部署。\", \"spec\": {\"command\": \"python scripts/exp003_analyze_all_configs.py\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"29459\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\", \"data_count\": 4, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"configs\": \"4 ablation configs: greedy, nucleus p=0.9/T=1.0, nucleus p=0.95/T=0.7, nucleus p=0.95/T=1.2\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\", \"log_path_note\": \"server renamed from autodl-4090d to westc-26893\"}, \"metrics\": {\"K_star\": 2, \"K_star_robust\": true, \"bootstrap_ci\": {\"config1_greedy\": {\"0v1\": {\"auc\": 0.9796, \"ci\": [0.9772, 0.982], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6892, \"ci\": [0.6802, 0.6982], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5612, \"ci\": [0.5517, 0.5705], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.5405, \"ci\": [0.5308, 0.5502], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5137, \"ci\": [0.5033, 0.5238], \"perm_p\": 0.0082}}, \"config2_nuc09\": {\"0v1\": {\"auc\": 0.9945, \"ci\": [0.9934, 0.9956], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6862, \"ci\": [0.6774, 0.6951], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5917, \"ci\": [0.5824, 0.601], \"perm_p\": 0, \"note\": \"CI upper crosses theta=0.60\"}, \"3v4\": {\"auc\": 0.5468, \"ci\": [0.5369, 0.5568], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5066, \"ci\": [0.4959, 0.5173], \"perm_p\": 0.1199}}, \"config3_t07\": {\"0v1\": {\"auc\": 0.9877, \"ci\": [0.9857, 0.9896], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6885, \"ci\": [0.6797, 0.697], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5901, \"ci\": [0.5806, 0.5996], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.539, \"ci\": [0.5288, 0.5493], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5348, \"ci\": [0.5243, 0.5454], \"perm_p\": 0}}, \"config4_t12\": {\"0v1\": {\"auc\": 0.9982, \"ci\": [0.9975, 0.9987], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.7037, \"ci\": [0.6945, 0.7126], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.582, \"ci\": [0.5722, 0.5917], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.5293, \"ci\": [0.5185, 0.5399], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5237, \"ci\": [0.5132, 0.5347], \"perm_p\": 0.0001}}, \"resamples\": 10000, \"method\": \"GroupKFold(5) OOF + doc-level bootstrap + label permutation\"}}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:22:19.870Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_analysis.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\", \"conclusion\": \"success\"}, \"exp_004_7b_crossscale\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T11:08:22.198Z\", \"updated_at\": \"2026-05-15T23:37:24.772Z\", \"hypothesis\": \"K*=2 在 7B scale 下是否成立？Qwen2.5-7B continuation mode, C4 5K seeds, scorer=Qwen2.5-1.5B。Reviewer R2 Critical: 现有实验仅 ≤1.5B\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-15T23:11:49.043Z\"}, \"completed_at\": \"2026-05-15T22:26:45.097Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:26:46.220502+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:11:50.215210+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"进程 5 次死亡无 W&B metrics，cron 自动标记 failed。诊断中：Worker worker_diagnose_exp_004_7b_crossscale_20260515T222832 正在查日志。模型加载成功(14530MB)，C4 采样有进度，日志末尾异常出现 transformers 全量模型列表。待诊断完成后确定 root cause 和重试方案。\"}}, \"notes\": \"初始运行因进程死亡 5 次被 cron 标记 failed（原 log: exp004_run.log 无 W&B sentinel）。诊断 Worker 发现数据生成已完成，重跑 feature extraction + classification（exp004_resume_feat.sh）后成功。K*=2 在 7B scale 下确认成立。0v1 AUC=0.964 低于所有 1.5B 模型（>0.99），符合预期：更大模型生成更 human-like 文本。1v2=0.618 仍 >θ=0.60。FR-4 Warning resolved。\", \"spec\": {\"hypothesis\": \"K*=2 在 7B scale 下是否成立？Qwen2.5-7B continuation mode, C4 5K seeds, scorer=Qwen2.5-1.5B\", \"server\": \"westc-26893\", \"model_name\": \"Qwen/Qwen2.5-7B (fp16, 14.5GB) + Qwen2.5-1.5B-Instruct (scorer)\", \"data_count\": 5000, \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/exp004_resume_feat.sh\\\"\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp004_qwen7b\", \"note\": \"Resume: data generation complete, rerunning feature extraction + classification with corrected scorer path. PID 127516.\"}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9644, \"1v2\": 0.6178, \"2v3\": 0.546, \"3v4\": 0.5225, \"4v5\": 0.5091}, \"pairwise_auc_std\": {\"0v1\": 0.0034, \"1v2\": 0.0081, \"2v3\": 0.0028, \"3v4\": 0.0113, \"4v5\": 0.0052}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9638, \"ci_lower\": 0.9607, \"ci_upper\": 0.9665, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6168, \"ci_lower\": 0.6079, \"ci_upper\": 0.6261, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5492, \"ci_lower\": 0.5388, \"ci_upper\": 0.5594, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5276, \"ci_lower\": 0.517, \"ci_upper\": 0.5375, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5085, \"ci_lower\": 0.4988, \"ci_upper\": 0.5191, \"perm_p\": 0.0676}}, \"bootstrap_resamples\": 1000, \"permutation_resamples\": 10000, \"pairwise_jsd\": {\"0v1\": 0.127422, \"1v2\": 0.010114, \"2v3\": 0.004798, \"3v4\": 0.004821, \"4v5\": 0.003335}, \"ordinal_mae\": 1.2156, \"ordinal_accuracy\": 0.3523, \"top_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_std\", \"surp_d1_mean\", \"surp_mean\"], \"key_finding\": \"K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60 (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676). FR-4 Warning resolved.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp004_qwen7b/\", \"log_path\": \"/root/runs/gen-depth-contamination/exp_004_7b_crossscale.log\"}, \"exp_E_paired_stats\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:27.723Z\", \"updated_at\": \"2026-05-15T14:22:43.224Z\", \"hypothesis\": \"C3 filtering 策略间差异是否统计显著？Holm-Bonferroni 多重比较校正 + Cohen's d 效应量（FR-5 Warning）\", \"spec\": {\"command\": \"python scripts/exp_E_paired_stats.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp006_filtering/results/\", \"data_count\": 51, \"model_name\": \"N/A (CPU: paired t-test + Holm-Bonferroni)\", \"seed\": \"N/A\", \"note\": \"6 strategies × 5 seeds, 15 pairwise comparisons, Holm-Bonferroni correction + Cohen's d\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_significant_pairs\": \"8/15\", \"hellaswag_significant_pairs\": \"9/15\", \"binary_ours_vs_all_mmlu\": \"all significant\", \"max_cohen_d_mmlu\": 10.8, \"max_cohen_d_hellaswag\": 8.98, \"graduated_a09_vs_dsir_corrected_p\": 0.0523, \"cohen_d_method\": \"d_av (Lakens 2013)\", \"key_finding\": \"binary-ours significantly outperforms all alternatives on MMLU. On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni cummax bug fixed: MMLU 10/15→8/15. Cohen's d changed to d_av.\", \"bugfix_note\": \"Holm-Bonferroni cummax variable was never updated, causing 2 MMLU pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_E_paired_stats.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_E_paired_stats.json\", \"completed_at\": \"2026-05-15T11:20:31.718Z\", \"notes\": \"Holm-Bonferroni bug fixed: cummax variable was never updated in loop, causing adjusted p-values to lose monotonicity. MMLU significant pairs corrected 10/15→8/15. Cohen's d changed from d_z to d_av (Lakens 2013). d values still large (10.8) due to n=5 tiny within-seed variance — recommend mean_diff as primary effect size in paper.\"}, \"exp_D_obd_n500\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:27.182Z\", \"updated_at\": \"2026-05-15T11:46:23.600Z\", \"hypothesis\": \"OBD-LightGBM 在 N=500 子集上 accuracy 是否仍高于 LLM baselines？验证样本量匹配下的公平比较（FR-12 Warning）\", \"spec\": {\"command\": \"python scripts/exp_D_obd_n500_v2.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia + artifacts/exp011_samples.jsonl\", \"data_count\": 500, \"model_name\": \"N/A (CPU: OBD-LightGBM on N=500 subset)\", \"seed\": 42, \"note\": \"Bootstrap CI for OBD accuracy on same 500 samples as LLM baseline\"}, \"conclusion\": \"success\", \"metrics\": {\"obd_accuracy_final\": 0.38, \"obd_ci\": [0.34, 0.422], \"mcnemar_vs_gpt55_p\": 0.0809, \"mcnemar_vs_claude_p\": 0.0693, \"mcnemar_significant\": false, \"multi_seed_std\": 0, \"per_depth\": {\"d0\": 0.96, \"d1\": 0.39, \"d2\": 0.14, \"d3\": 0.19, \"d4\": 0.22}, \"prob_merge_accuracy\": 0.444, \"prob_merge_d4_bias\": 0.8, \"note\": \"v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant — supports discussion.tex narrative\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_D_obd_n500_v2.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_D_obd_n500_v2.json\", \"completed_at\": \"2026-05-15T11:20:31.077Z\"}, \"exp_B_14d_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:25.666Z\", \"updated_at\": \"2026-05-15T11:20:29.596Z\", \"hypothesis\": \"移除 self_BLEU（14D vs 15D）后 K*=2 是否稳定？排除 self_BLEU information leakage（FR-3 Critical）\", \"spec\": {\"command\": \"python scripts/exp_B_14d_ablation.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data + data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 20000, \"model_name\": \"N/A (CPU: LightGBM 14D vs 15D)\", \"seed\": 42, \"note\": \"Remove self_BLEU, compare 14D vs 15D pairwise AUC and K*\"}, \"conclusion\": \"success\", \"metrics\": {\"result\": \"K*=2 stable across all 4 models after removing self_BLEU (14D)\", \"key_finding\": \"self_BLEU removal does not change K* boundary. FR-3 resolved.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_B_14d_ablation.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_B_14d_ablation.json\", \"completed_at\": \"2026-05-15T11:20:29.596Z\"}, \"exp_A_alt_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:24.715Z\", \"updated_at\": \"2026-05-15T11:19:40.861Z\", \"hypothesis\": \"替代 scorer (Pythia-1.4B, OLMo-1B) 计算 surprisal features 时，K*=2 是否仍成立？验证 K* 不依赖 scorer-generator 匹配（FR-2 Critical）\", \"spec\": {\"command\": \"bash scripts/run_exp_A.sh\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data (Qwen-RW) + data_exp017_qwen_cont (Qwen-cont)\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B + OLMo-1B (as alt scorers) × Qwen-generated data\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"note\": \"4 conditions: {Pythia,OLMo} × {Qwen-RW,Qwen-cont}. Surprisal features computed with alt scorer, LightGBM classification.\"}, \"conclusion\": \"success\", \"metrics\": {\"pythia_qwen_rw\": {\"k_star\": 2, \"auc_0v1\": 0.9923, \"auc_1v2\": 0.7012, \"auc_2v3\": 0.587, \"mae\": 1.006, \"accuracy\": 0.417, \"spearman_rho_vs_baseline\": 0.906}, \"pythia_qwen_cont\": {\"k_star\": 1, \"auc_0v1\": 0.99, \"auc_1v2\": 0.5923, \"auc_2v3\": null, \"mae\": 1.216, \"accuracy\": 0.371, \"spearman_rho_vs_baseline\": 0.942}, \"olmo_qwen_rw\": {\"k_star\": 2, \"auc_0v1\": 0.9918, \"auc_1v2\": 0.6947, \"auc_2v3\": null, \"mae\": 1.016, \"accuracy\": 0.413, \"spearman_rho_vs_baseline\": 0.92}, \"olmo_qwen_cont\": {\"k_star\": 1, \"auc_0v1\": 0.989, \"auc_1v2\": 0.5858, \"auc_2v3\": null, \"mae\": 1.229, \"accuracy\": 0.368, \"spearman_rho_vs_baseline\": 0.902}, \"key_finding\": \"K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1 (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer independence of feature ranking.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_A/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_A/exp_A_alt_scorer.log\", \"completed_at\": \"2026-05-15T11:19:40.861Z\"}, \"exp_006_graduated_filtering\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-13T20:25:52.364Z\", \"updated_at\": \"2026-05-15T09:18:18.667Z\", \"hypothesis\": \"K*-aware graduated filtering (exploiting human/gen-1/gen-2+ trichotomy) yields better downstream LM quality than binary filtering on MMLU and HellaSwag. 6 strategies × 5 seeds × α sweep.\", \"parent\": \"exp_003_decoding_ablation\", \"notes\": \"51/51 COMPLETE. All 6 strategies × 5 seeds + base_model finished 2026-05-15 ~09:10 UTC.\\n\\nFINAL RANKING (MMLU descending):\\n1. binary-ours: 0.5941±0.0008 / 0.6701±0.0006 (BEST)\\n2. binary-drayson: 0.5913±0.0009 / 0.6691±0.0004\\n3. surprisal: 0.5894±0.0009 / 0.6641±0.0006\\n4. graduated_a0.9: 0.5892±0.0008 / 0.6701±0.0007\\n5. graduated_a0.7: 0.5892±0.0014 / 0.6695±0.0004\\n6. graduated_a0.5: 0.5880±0.0013 / 0.6687±0.0008\\n7. graduated_a0.3: 0.5877±0.0013 / 0.6669±0.0005\\n8. graduated_a0.1: 0.5873±0.0019 / 0.6640±0.0009\\n9. dsir: 0.5869±0.0003 / 0.6631±0.0007\\n10. no-filter: 0.5865±0.0010 / 0.6638±0.0008\\nBase: 0.6018 / 0.6821\\n\\nVERSION B fully confirmed. Binary-ours is optimal. Graduated α monotonic. DSIR below all strategies except no-filter.\", \"reproduce\": {\"finished_at\": \"2026-05-14T21:31:53.630Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-14T21:04:20.455Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:04:21.389845+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:32:00.501871+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"RESUMED 05-14 ~21:30 UTC after EXIT_CODE=124 timeout crash. 32/50 runs complete pre-crash. 18 remaining: a0.7(s456/s789/s1024) + a0.9(5) + surprisal(5) + dsir(5). Script has built-in skip logic (checks eval_results.json). Running in tmux:exp006_resume without timeout wrapper. ETA: ~05-15 11:00-12:00 UTC.\"}}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp006_graduated_filtering.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/depth_corpus_30k\", \"data_count\": 30000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": \"42,123,456,789,1024\", \"gpu\": \"cuda:0\", \"checkpoint_source\": \"Qwen/Qwen2.5-1.5B-Instruct (HuggingFace, LoRA fine-tune from base)\", \"eval_data\": \"MMLU (14042 test, 0-shot) + HellaSwag (10042 val, 0-shot) via lm-eval-harness\", \"note\": \"Resumed run. tmux: exp_006_graduated_filtering. 33/50 complete, 17 remaining. ETA ~05-15 07:30-08:30 UTC.\"}, \"conclusion\": \"success\", \"metrics\": {\"total_runs\": 51, \"binary_ours\": {\"mmlu\": \"0.5941±0.0008\", \"hellaswag\": \"0.6701±0.0006\"}, \"binary_drayson\": {\"mmlu\": \"0.5913±0.0009\", \"hellaswag\": \"0.6691±0.0004\"}, \"surprisal\": {\"mmlu\": \"0.5894±0.0009\", \"hellaswag\": \"0.6641±0.0006\"}, \"graduated_a09\": {\"mmlu\": \"0.5892±0.0008\", \"hellaswag\": \"0.6701±0.0007\"}, \"graduated_a07\": {\"mmlu\": \"0.5892±0.0014\", \"hellaswag\": \"0.6695±0.0004\"}, \"graduated_a05\": {\"mmlu\": \"0.5880±0.0013\", \"hellaswag\": \"0.6687±0.0008\"}, \"graduated_a03\": {\"mmlu\": \"0.5877±0.0013\", \"hellaswag\": \"0.6669±0.0005\"}, \"graduated_a01\": {\"mmlu\": \"0.5873±0.0019\", \"hellaswag\": \"0.6640±0.0009\"}, \"dsir\": {\"mmlu\": \"0.5869±0.0003\", \"hellaswag\": \"0.6631±0.0007\"}, \"no_filter\": {\"mmlu\": \"0.5865±0.0010\", \"hellaswag\": \"0.6638±0.0008\"}, \"base_model\": {\"mmlu\": \"0.6018\", \"hellaswag\": \"0.6821\"}, \"best_strategy\": \"binary-ours\", \"key_finding\": \"binary-ours is best filtering strategy. All strategies degrade vs base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR below all other strategies except no-filter.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp006_filtering/results/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_006_graduated_filtering.log\"}, \"exp_007_bootstrap_ci\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:45:50.948Z\", \"updated_at\": \"2026-05-13T23:43:00.694Z\", \"hypothesis\": \"K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\", \"spec\": {\"command\": \"python scripts/bootstrap_ci.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output artifacts/bootstrap_ci_results.json\", \"script_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py\", \"server\": \"autodl-4090d\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\", \"data_count\": 15000, \"model_name\": \"Pythia-1.4B / OLMo-1B / Qwen-1.5B\", \"seed\": 42, \"input_sources\": [\"results_exp001_pythia (exp-001)\", \"results_exp002_olmo (exp-002)\", \"data (mvp-001)\"], \"bootstrap_resamples\": 1000, \"permutation_resamples\": 500, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_007_bootstrap_ci.log\"}, \"metrics\": {\"qwen_rewrite\": {\"0v1\": {\"auc\": 0.9956, \"ci_lower\": 0.9946, \"ci_upper\": 0.9965, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6955, \"ci_lower\": 0.6859, \"ci_upper\": 0.7041, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5893, \"ci_lower\": 0.5795, \"ci_upper\": 0.5991, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5435, \"ci_lower\": 0.5333, \"ci_upper\": 0.5551, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.534, \"ci_lower\": 0.5238, \"ci_upper\": 0.5448, \"perm_p\": 0.002}}, \"pythia_cont\": {\"0v1\": {\"auc\": 0.9932, \"ci_lower\": 0.9921, \"ci_upper\": 0.9943, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6539, \"ci_lower\": 0.6454, \"ci_upper\": 0.663, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5514, \"ci_lower\": 0.5417, \"ci_upper\": 0.5628, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5152, \"ci_lower\": 0.5041, \"ci_upper\": 0.526, \"perm_p\": 0.006}, \"4v5\": {\"auc\": 0.5136, \"ci_lower\": 0.5021, \"ci_upper\": 0.5249, \"perm_p\": 0.008}}, \"olmo_cont\": {\"0v1\": {\"auc\": 0.997, \"ci_lower\": 0.9964, \"ci_upper\": 0.9975, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6145, \"ci_lower\": 0.6045, \"ci_upper\": 0.6247, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5399, \"ci_upper\": 0.5596, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5091, \"ci_lower\": 0.4973, \"ci_upper\": 0.52, \"perm_p\": 0.064}, \"4v5\": {\"auc\": 0.5045, \"ci_lower\": 0.4932, \"ci_upper\": 0.515, \"perm_p\": 0.232}}, \"qwen_cont\": {\"0v1\": {\"auc\": 0.9971, \"ci_lower\": 0.9963, \"ci_upper\": 0.9978, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6112, \"ci_lower\": 0.6015, \"ci_upper\": 0.6213, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5609, \"ci_lower\": 0.5511, \"ci_upper\": 0.5712, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5409, \"ci_lower\": 0.5308, \"ci_upper\": 0.5508, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.5141, \"ci_lower\": 0.5035, \"ci_upper\": 0.5255, \"perm_p\": 0.006}}, \"k_star_robust\": true, \"all_1v2_ci_lower_above_060\": true, \"most_marginal\": \"Qwen-cont CI lower=0.6015, only 0.0015 above threshold\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T03:46:36.617Z\"}, \"exp_011_llm_zeroshot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T08:59:07.954Z\", \"updated_at\": \"2026-05-13T11:34:44.605Z\", \"hypothesis\": \"Frontier LLMs (GPT-5.5, Claude Opus 4.6) cannot reliably estimate generational depth via zero-shot prompting, motivating the need for specialized statistical methods\", \"spec\": {\"command\": \"python3 scripts/exp011_llm_zeroshot.py --model gpt-5.5 && python3 scripts/exp011_llm_zeroshot.py --model claude-opus-4-6 && python3 scripts/exp011_analyze.py\", \"server\": \"autodl-4090d\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"data_count\": 500, \"model_name\": \"GPT-5.5 + Claude Opus 4.6 (zero-shot via OpenRouter)\", \"seed\": 42, \"sampling\": \"100 texts × 5 depths (0-4) from Pythia continuation\", \"scripts\": [\"scripts/exp011_sample_data.py\", \"scripts/exp011_llm_zeroshot.py\", \"scripts/exp011_analyze.py\"], \"samples_path\": \"artifacts/exp011_samples.jsonl\", \"api_base_url\": \"http://47.94.22.126/v1\", \"api_model_ids\": {\"gpt-5.5\": \"openai/gpt-5.5\", \"claude-opus-4-6\": \"claude-opus-4-6\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp011_analysis.json\", \"log_path\": \"N/A (API task)\"}, \"notes\": \"GPT-5.5: 500条, 0 parse failures. Claude Opus 4.6: 500条, 1 parse failure. 两个 frontier LLM 5-class accuracy (~33%) 均低于 OBD-LightGBM (38.6%)。Binary human/AI detection 高 (~88%) 但 fine-grained depth 判断失败。Claude proxy 需用 model ID 'claude-opus-4-6' (无 anthropic/ 前缀)。\", \"metrics\": {\"gpt55_5class_acc\": 0.332, \"gpt55_mae\": 1.102, \"gpt55_spearman\": 0.383, \"gpt55_binary_acc\": 0.878, \"claude_5class_acc\": 0.331, \"claude_mae\": 1.15, \"claude_spearman\": 0.416, \"claude_binary_acc\": 0.882, \"odb_baseline_5class_acc\": 0.386, \"odb_baseline_mae\": 1.107, \"gpt55_per_depth_acc\": {\"depth_0\": 0.77, \"depth_1\": 0.19, \"depth_2\": 0.38, \"depth_3\": 0.24, \"depth_4\": 0.08}, \"claude_per_depth_acc\": {\"depth_0\": 0.69, \"depth_1\": 0.21, \"depth_2\": 0.28, \"depth_3\": 0.101, \"depth_4\": 0.37}, \"n_samples_per_model\": 500, \"key_finding\": \"Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T11:32:56.036Z\"}, \"exp_013_cross_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:50:57.813Z\", \"updated_at\": \"2026-05-13T06:54:11.689Z\", \"spec\": {\"command\": \"python scripts/run_exp013_cross_transfer.py --out_dir artifacts/\", \"server\": \"autodl-4090d\", \"data_path\": \"data/, data_exp001_pythia/, data_exp002_olmo/, data_exp017_qwen_cont/\", \"data_count\": 20000, \"model_name\": \"N/A (CPU classifiers: OBD-LightGBM)\", \"seed\": 42, \"input_sources\": [\"mvp-001 Qwen-rewrite\", \"exp-001 Pythia\", \"exp-002 OLMo\", \"exp-017 Qwen-cont\"], \"checkpoint_path\": \"artifacts/cross_transfer_matrix.json\", \"log_path\": \"N/A (CPU task)\"}, \"hypothesis\": \"Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\", \"metrics\": {\"accuracy_matrix\": {\"Qwen_rw→Qwen_rw\": 0.4229, \"Qwen_rw→Pythia\": 0.259, \"Qwen_rw→OLMo\": 0.2653, \"Qwen_rw→Qwen_cont\": 0.3466, \"Pythia→Qwen_rw\": 0.2718, \"Pythia→Pythia\": 0.3856, \"Pythia→OLMo\": 0.3531, \"Pythia→Qwen_cont\": 0.3287, \"OLMo→Qwen_rw\": 0.2768, \"OLMo→Pythia\": 0.345, \"OLMo→OLMo\": 0.3822, \"OLMo→Qwen_cont\": 0.3244, \"Qwen_cont→Qwen_rw\": 0.344, \"Qwen_cont→Pythia\": 0.3284, \"Qwen_cont→OLMo\": 0.3112, \"Qwen_cont→Qwen_cont\": 0.3875}, \"transfer_retention_accuracy\": {\"Pythia↔OLMo\": \"91-92%\", \"Qwen_rw→Pythia/OLMo\": \"61-63%\", \"Qwen_cont↔Pythia\": \"83-85%\", \"Qwen_cont↔OLMo\": \"80-85%\"}, \"transfer_retention_tau\": {\"Pythia↔OLMo\": \"85-86%\", \"Qwen_rw→Pythia/OLMo\": \"45-50%\", \"Qwen_cont↔others\": \"68-83%\"}, \"mean_pw_auc_matrix\": {\"within_avg\": 0.6099, \"cross_avg\": 0.5905, \"0v1_cross_all_above\": 0.96}, \"key_finding\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T06:53:07.326Z\", \"notes\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Pythia↔OLMo 91-92% retention (architecture-agnostic). Qwen-rewrite catastrophic transfer to other models (61-63%), but Qwen-cont much better (80-85%). 0v1 universally transferable (>0.96 AUC), 1v2+ transfer depends on model family. Rewrite mode overfits style features → continuation mode is canonical condition for cross-model claims.\"}, \"exp_010_ordinal_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:22:42.199Z\", \"updated_at\": \"2026-05-13T04:26:54.571Z\", \"hypothesis\": \"Ordinal structure improves depth classification: ordinal methods should outperform unordered multiclass on MAE\", \"spec\": {\"command\": \"python scripts/run_exp010_ordinal_comparison.py\", \"server\": \"autodl-4090d\", \"data_path\": \"data/features.csv, data_exp001_pythia/features.csv, data_exp002_olmo/features.csv\", \"data_count\": 90000, \"model_name\": \"N/A (CPU classifiers)\", \"seed\": \"N/A\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/ordinal_comparison_results.json\"}, \"metrics\": {\"qwen_rewrite\": {\"obd_lgbm\": {\"accuracy\": 0.4229, \"mae\": 0.9836, \"tau_b\": 0.5518, \"mean_pw_auc\": 0.6214}, \"multiclass_lgbm\": {\"accuracy\": 0.4182, \"mae\": 1.0163, \"tau_b\": 0.5367, \"mean_pw_auc\": 0.6246}, \"ordinal_logreg\": {\"accuracy\": 0.3636, \"mae\": 0.9105, \"tau_b\": 0.563, \"mean_pw_auc\": 0.5022}}, \"pythia\": {\"obd_lgbm\": {\"accuracy\": 0.3856, \"mae\": 1.1072, \"tau_b\": 0.4745, \"mean_pw_auc\": 0.6055}, \"multiclass_lgbm\": {\"accuracy\": 0.3832, \"mae\": 1.1399, \"tau_b\": 0.4622, \"mean_pw_auc\": 0.6062}, \"ordinal_logreg\": {\"accuracy\": 0.3179, \"mae\": 1.022, \"tau_b\": 0.49, \"mean_pw_auc\": 0.4767}}, \"olmo\": {\"obd_lgbm\": {\"accuracy\": 0.3822, \"mae\": 1.1469, \"tau_b\": 0.4683, \"mean_pw_auc\": 0.6015}, \"multiclass_lgbm\": {\"accuracy\": 0.3685, \"mae\": 1.1813, \"tau_b\": 0.4497, \"mean_pw_auc\": 0.5974}, \"ordinal_logreg\": {\"accuracy\": 0.3265, \"mae\": 1.0352, \"tau_b\": 0.4656, \"mean_pw_auc\": 0.4859}}}, \"conclusion\": \"success\", \"notes\": \"Ordinal methods beat multiclass LightGBM on MAE across all 3 datasets. Best MAE consistently from mord LogisticAT, not OBD-LightGBM. However, ordinal_logreg has worst pairwise AUC — it reduces MAE by collapsing predictions toward the center, not by better discrimination.\", \"completed_at\": \"2026-05-13T04:26:54.571Z\"}, \"mvp_pilot_sat_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T11:09:39.193Z\", \"updated_at\": \"2026-05-12T19:25:33.763Z\", \"hypothesis\": \"递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势（K* ≥ 3）\", \"spec\": {\"command\": \"bash /root/autodl-tmp/gen-depth-contamination/run_mvp.sh\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"10619\", \"log_path\": \"~/runs/gen-depth-contamination/mvp_pilot_sat_v1.log\", \"submitted_at\": \"2026-05-12T16:46:33.175Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"wall_clock_seconds\": 9533.4, \"gpu_hours\": 2.65}, \"notes\": \"v2 left-padding rerun, per-fold AUC, full self-BLEU\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T19:25:26.538Z\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9956, \"1v2\": 0.6957, \"2v3\": 0.5893, \"3v4\": 0.5434, \"4v5\": 0.5343}, \"pairwise_auc_std\": {\"0v1\": 0.0005, \"1v2\": 0.0072, \"2v3\": 0.012, \"3v4\": 0.0053, \"4v5\": 0.0091}, \"pairwise_jsd\": {\"0v1\": 0.2669, \"1v2\": 0.0163, \"2v3\": 0.0069, \"3v4\": 0.0047, \"4v5\": 0.0041}, \"k_star\": 2, \"ordinal_mae\": 1.0163, \"ordinal_accuracy\": 0.4182}}}, \"count\": 176, \"total\": 176, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5514}}"
    }
  },
  "sourceToolAssistantUUID": "0da56f22-770d-428b-a954-115b2882bf0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-25T19:44:41.003Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WyqYmDwpB9AyGZDKjzyVDG`</summary>

```json
{
  "pattern": "**/tables/tab_crossscorer*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7006b28d-337c-4da7-995c-fcd5c81404b8",
  "isSidechain": false,
  "requestId": "req_011CbPrrh6ezV5d4V95UHnt3",
  "type": "assistant",
  "uuid": "df8deb54-4cf6-4416-8ab4-b2215d145f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wmw8dPH9ia4vkRUVgTdok",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25283,
      "cache_read_input_tokens": 25060,
      "output_tokens": 714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 714,
          "cache_read_input_tokens": 25060,
          "cache_creation_input_tokens": 25283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25283
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

_source line 27 · 2026-05-25T19:44:41.011Z_

<details><summary>↩ Tool result · `toolu_01WyqYmDwpB9AyGZDKjzyVDG`</summary>

```text
docs/paper/tables/tab_crossscorer.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df8deb54-4cf6-4416-8ab4-b2215d145f48",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "18d9fe54-aa68-4669-b199-7a459e7bf061",
  "toolUseResult": {
    "filenames": [
      "docs/paper/tables/tab_crossscorer.tex"
    ],
    "durationMs": 5,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "df8deb54-4cf6-4416-8ab4-b2215d145f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-25T19:44:41.947Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01D5DWixsF14w9EwEubb9XTR`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination/scripts/ -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18d9fe54-aa68-4669-b199-7a459e7bf061",
  "isSidechain": false,
  "requestId": "req_011CbPrrh6ezV5d4V95UHnt3",
  "type": "assistant",
  "uuid": "aa0f47ef-4962-453a-af7e-1ac71965681c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wmw8dPH9ia4vkRUVgTdok",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25283,
      "cache_read_input_tokens": 25060,
      "output_tokens": 714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 714,
          "cache_read_input_tokens": 25060,
          "cache_creation_input_tokens": 25283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25283
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

_source line 29_

```json
{
  "type": "last-prompt",
  "leafUuid": "aa0f47ef-4962-453a-af7e-1ac71965681c",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit appendix and figure data sources",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Tool result

_source line 31 · 2026-05-25T19:44:42.758Z_

<details><summary>↩ Tool result · `toolu_01D5DWixsF14w9EwEubb9XTR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/scripts/exp_028_power_curve.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/analyze_code_crossmodel.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_olmo_retrain_chain.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/analyze_deberta_results.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_deberta_filtering_comparison.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/analyze_pythia_retrain_depth7.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_olmo_retrain_v3.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_stability_check.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_pythia_retrain_depth7.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/borderline_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_fig_jsd_decay.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/c4_power_curve.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/c4_subsample_control.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_filtering_strategies.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/case_study_refine.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_retrain_decay.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/case_study_select.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_retrain_decay_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/check_doc2000.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_cross_transfer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/check_doc3000.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain_ext.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/check_monotonicity.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_ablation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/collect_exp009_v3.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/extract_texts.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/compute_f1_threshold.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_arxiv.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/cross_scorer_f1.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_group_ablation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/crossscorer_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_analysis.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_arxiv_seed.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_batch.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_code_seed.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_correct.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_wiki_seed.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_bootstrap_10k.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/draw_kstar_theta.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_changepoint_kstar.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/draw_sweep_figure.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp027_retrain_bootstrap.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp007_olmo_rerun_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_pythia.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp008_retrain_chain.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_qwen_cont.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp009_dose_response.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp016_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/gen_case_study_latex.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp018_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/gen_case_study_latex_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp019_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/gen_case_study_latex_v3.py\\n/root/auto\\n\\n... [截断: 输出过长，省略 1277 字符] ...\\n\\namination/scripts/plot_feature_importance.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_fig2_merged.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_14d_ablation_detail.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_deberta_filtering_predict.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_expanded_downstream_eval.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_contamination_rate_sweep.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_upperbound.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_code.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/retrain_chain_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_cross_transfer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_exp013_cross_transfer_olmo_rerun.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_exp013_cross_transfer_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_fi_pythia.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_gemma2b_depth.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_arxiv.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_code.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_unified_scorer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_vocab_only.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_wiki.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_naturalistic_validation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_olmo_ablation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/score_14b_confound.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/semantic_ablation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/semantic_ablation_multi_model.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/theta_sensitivity_c4_wiki.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/compute_missing_tables.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_pipeline.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_llama8b_10k_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/pythia_qwen_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/gemma2b_10k_qwen_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/arxiv_2v3_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/runtime_benchmark.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_kstar.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_gemma27b_depth.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_arxiv_multi_source_1b5.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_cross_transfer_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_gemma27b_cross_transfer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_gemma27b_filtering.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/code_wiki_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/arxiv_multi_source_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_olmo_arxiv_cross_scorer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_olmo_c4_cross_scorer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_naturalistic_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_independent_metrics.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_independent_analysis.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_v1_independent_metrics.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_v1_independent_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa0f47ef-4962-453a-af7e-1ac71965681c",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "13798094-03c5-48b1-a3f5-20b0932352a2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/gen-depth-contamination/scripts/exp_028_power_curve.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/analyze_code_crossmodel.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_olmo_retrain_chain.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/analyze_deberta_results.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_deberta_filtering_comparison.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/analyze_pythia_retrain_depth7.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_olmo_retrain_v3.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_stability_check.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_pythia_retrain_depth7.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/borderline_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_fig_jsd_decay.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/c4_power_curve.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/c4_subsample_control.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_filtering_strategies.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/case_study_refine.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_retrain_decay.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/case_study_select.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_retrain_decay_v2.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/check_doc2000.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_cross_transfer.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/check_doc3000.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain_ext.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/check_monotonicity.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_ablation.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/collect_exp009_v3.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/extract_texts.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/compute_f1_threshold.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_arxiv.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/cross_scorer_f1.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_group_ablation.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/crossscorer_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_analysis.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_arxiv_seed.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_batch.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_code_seed.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_correct.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_wiki_seed.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_bootstrap_10k.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/draw_kstar_theta.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_changepoint_kstar.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/draw_sweep_figure.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp027_retrain_bootstrap.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp007_olmo_rerun_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_pythia.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp008_retrain_chain.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_qwen_cont.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp009_dose_response.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp016_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/gen_case_study_latex.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp018_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/gen_case_study_latex_v2.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp019_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/gen_case_study_latex_v3.py\\\\n/root/auto\\\\n\\\\n... [截断: 输出过长，省略 1277 字符] ...\\\\n\\\\namination/scripts/plot_feature_importance.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_fig2_merged.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_14d_ablation_detail.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_deberta_filtering_predict.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_expanded_downstream_eval.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_contamination_rate_sweep.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_upperbound.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_code.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/retrain_chain_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_cross_transfer.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_exp013_cross_transfer_olmo_rerun.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_exp013_cross_transfer_v2.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_fi_pythia.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_gemma2b_depth.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_arxiv.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_code.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_unified_scorer.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_v2.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_vocab_only.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_wiki.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_naturalistic_validation.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_olmo_ablation.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/score_14b_confound.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/semantic_ablation.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/semantic_ablation_multi_model.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/theta_sensitivity_c4_wiki.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/compute_missing_tables.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_pipeline.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap_v2.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_llama8b_10k_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/pythia_qwen_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/gemma2b_10k_qwen_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/arxiv_2v3_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/runtime_benchmark.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_kstar.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_gemma27b_depth.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_arxiv_multi_source_1b5.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_cross_transfer_v2.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_gemma27b_cross_transfer.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_gemma27b_filtering.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/code_wiki_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/arxiv_multi_source_bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_olmo_arxiv_cross_scorer.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_olmo_c4_cross_scorer.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_naturalistic_v2.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_independent_metrics.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_independent_analysis.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_v1_independent_metrics.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_v1_independent_analysis.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/scripts/exp_028_power_curve.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/analyze_code_crossmodel.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_olmo_retrain_chain.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/analyze_deberta_results.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_deberta_filtering_comparison.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/analyze_pythia_retrain_depth7.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_olmo_retrain_v3.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_stability_check.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_pythia_retrain_depth7.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/borderline_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_fig_jsd_decay.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/c4_power_curve.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/c4_subsample_control.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_filtering_strategies.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/case_study_refine.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_retrain_decay.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/case_study_select.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_retrain_decay_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/check_doc2000.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_cross_transfer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/check_doc3000.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain_ext.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/check_monotonicity.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_ablation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/collect_exp009_v3.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/extract_texts.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/compute_f1_threshold.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_arxiv.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/cross_scorer_f1.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_group_ablation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/crossscorer_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_analysis.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_arxiv_seed.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_batch.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_code_seed.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_correct.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_wiki_seed.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_bootstrap_10k.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/draw_kstar_theta.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_changepoint_kstar.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/draw_sweep_figure.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp027_retrain_bootstrap.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp007_olmo_rerun_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_pythia.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp008_retrain_chain.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_qwen_cont.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp009_dose_response.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp016_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/gen_case_study_latex.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp018_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/gen_case_study_latex_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp019_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/gen_case_study_latex_v3.py\\n/root/auto\\n\\n... [截断: 输出过长，省略 1277 字符] ...\\n\\namination/scripts/plot_feature_importance.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_fig2_merged.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_14d_ablation_detail.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_deberta_filtering_predict.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_expanded_downstream_eval.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_contamination_rate_sweep.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_upperbound.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_code.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/retrain_chain_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_cross_transfer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_exp013_cross_transfer_olmo_rerun.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_exp013_cross_transfer_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_fi_pythia.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_gemma2b_depth.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_arxiv.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_code.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_unified_scorer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_vocab_only.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_wiki.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_naturalistic_validation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_olmo_ablation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/score_14b_confound.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/semantic_ablation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/semantic_ablation_multi_model.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/theta_sensitivity_c4_wiki.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/compute_missing_tables.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_pipeline.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_llama8b_10k_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/pythia_qwen_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/gemma2b_10k_qwen_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/arxiv_2v3_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/runtime_benchmark.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_kstar.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_gemma27b_depth.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_arxiv_multi_source_1b5.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_7b_cross_transfer_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_gemma27b_cross_transfer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_gemma27b_filtering.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/code_wiki_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/arxiv_multi_source_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_olmo_arxiv_cross_scorer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_olmo_c4_cross_scorer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_naturalistic_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_independent_metrics.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_independent_analysis.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_v1_independent_metrics.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp014_v1_independent_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8}}"
    }
  },
  "sourceToolAssistantUUID": "aa0f47ef-4962-453a-af7e-1ac71965681c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 32 · 2026-05-25T19:44:42.762Z_

```json
{
  "parentUuid": "13798094-03c5-48b1-a3f5-20b0932352a2",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e230c8d4-868c-4469-a5d0-4ee5e041d1e0",
  "timestamp": "2026-05-25T19:44:42.762Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 33 · 2026-05-25T19:44:47.303Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a lot of data. Let me now:

1. Read the tab_crossscorer.tex file
2. Launch an agent to process the registry JSON file and extract all relevant metrics
3. Search for savefig calls in the plotting scripts on the server to trace which data files they read

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e230c8d4-868c-4469-a5d0-4ee5e041d1e0",
  "isSidechain": false,
  "requestId": "req_011CbPrspyTJ7tcK6KHrLpRk",
  "type": "assistant",
  "uuid": "c5cd63ce-5aab-40e1-8996-a34dae38d282",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFAMdzRjtavu1oCLwNRtfm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 50343,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1214,
          "cache_read_input_tokens": 50343,
          "cache_creation_input_tokens": 4550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4550
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

_source line 34 · 2026-05-25T19:44:48.284Z_

Let me read the cross-scorer table, search for savefig references in plotting scripts, and process the registry in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5cd63ce-5aab-40e1-8996-a34dae38d282",
  "isSidechain": false,
  "requestId": "req_011CbPrspyTJ7tcK6KHrLpRk",
  "type": "assistant",
  "uuid": "59da9cfa-e304-4dc4-ae90-7f618050bb5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFAMdzRjtavu1oCLwNRtfm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 50343,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1214,
          "cache_read_input_tokens": 50343,
          "cache_creation_input_tokens": 4550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4550
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

_source line 35 · 2026-05-25T19:44:50.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XwbsSJ5nUG5DvhsXGzDdxi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59da9cfa-e304-4dc4-ae90-7f618050bb5c",
  "isSidechain": false,
  "requestId": "req_011CbPrspyTJ7tcK6KHrLpRk",
  "type": "assistant",
  "uuid": "de1d7a41-1c91-4263-a33b-edd1fd6b9566",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFAMdzRjtavu1oCLwNRtfm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 50343,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1214,
          "cache_read_input_tokens": 50343,
          "cache_creation_input_tokens": 4550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4550
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

_source line 36 · 2026-05-25T19:44:50.180Z_

<details><summary>↩ Tool result · `toolu_01XwbsSJ5nUG5DvhsXGzDdxi`</summary>

```text
1	{\small
2	\begin{tabular}{llcccc}
3	\toprule
4	\textbf{Scorer} & \textbf{Gen.\ Data} & $\boldsymbol{K^*}$ & \textbf{AUC(0v1)} & \textbf{AUC(1v2)} & \textbf{Spearman}~$\boldsymbol{\rho}$ \\
5	\midrule
6	% --- Qwen-RW block ---
7	Qwen-1.5B (self) & Qwen-RW & 2 & --- & 0.6955 & --- \\
8	Pythia-1.4B       & Qwen-RW & 2 & 0.9923 & 0.7012 & 0.906 \\
9	OLMo-1B           & Qwen-RW & 2 & 0.9918 & 0.6947 & 0.920 \\
10	\midrule
11	% --- Qwen-cont block ---
12	Qwen-1.5B (self) & Qwen-cont & 2 & --- & 0.6112 & --- \\
13	Pythia-1.4B       & Qwen-cont & \textcolor{red}{1\textsuperscript{$\dagger$}} & 0.9900 & \underline{0.5923} & 0.942 \\
14	OLMo-1B           & Qwen-cont & \textcolor{red}{1\textsuperscript{$\dagger$}} & 0.9890 & \underline{0.5858} & 0.902 \\
15	\midrule
16	% --- Qwen-7B cross-scale block ---
17	Qwen-1.5B        & Qwen-7B-cont & 2 & 0.9644 & 0.6178 & --- \\
18	\midrule
19	% --- OLMo cross-scorer block (all domains) ---
20	Cross-scorer      & OLMo-arXiv   & 1 & 0.999  & 0.500\textsuperscript{n.s.} & --- \\
21	Cross-scorer      & OLMo-Code    & 1 & 0.9996 & 0.557\textsuperscript{n.s.} & --- \\
22	\bottomrule
23	\end{tabular}
24	}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de1d7a41-1c91-4263-a33b-edd1fd6b9566",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "a07630de-484c-49de-9720-2c4d6854be4c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex",
      "content": "{\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Scorer} & \\textbf{Gen.\\ Data} & $\\boldsymbol{K^*}$ & \\textbf{AUC(0v1)} & \\textbf{AUC(1v2)} & \\textbf{Spearman}~$\\boldsymbol{\\rho}$ \\\\\n\\midrule\n% --- Qwen-RW block ---\nQwen-1.5B (self) & Qwen-RW & 2 & --- & 0.6955 & --- \\\\\nPythia-1.4B       & Qwen-RW & 2 & 0.9923 & 0.7012 & 0.906 \\\\\nOLMo-1B           & Qwen-RW & 2 & 0.9918 & 0.6947 & 0.920 \\\\\n\\midrule\n% --- Qwen-cont block ---\nQwen-1.5B (self) & Qwen-cont & 2 & --- & 0.6112 & --- \\\\\nPythia-1.4B       & Qwen-cont & \\textcolor{red}{1\\textsuperscript{$\\dagger$}} & 0.9900 & \\underline{0.5923} & 0.942 \\\\\nOLMo-1B           & Qwen-cont & \\textcolor{red}{1\\textsuperscript{$\\dagger$}} & 0.9890 & \\underline{0.5858} & 0.902 \\\\\n\\midrule\n% --- Qwen-7B cross-scale block ---\nQwen-1.5B        & Qwen-7B-cont & 2 & 0.9644 & 0.6178 & --- \\\\\n\\midrule\n% --- OLMo cross-scorer block (all domains) ---\nCross-scorer      & OLMo-arXiv   & 1 & 0.999  & 0.500\\textsuperscript{n.s.} & --- \\\\\nCross-scorer      & OLMo-Code    & 1 & 0.9996 & 0.557\\textsuperscript{n.s.} & --- \\\\\n\\bottomrule\n\\end{tabular}\n}\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  },
  "sourceToolAssistantUUID": "de1d7a41-1c91-4263-a33b-edd1fd6b9566",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-25T19:44:54.937Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Vw93wRQNRsP7euJfCWkjC4`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"savefig\\|plt.save\\|fig.save\" /root/autodl-tmp/gen-depth-contamination/scripts/plot_fig2_merged.py /root/autodl-tmp/gen-depth-contamination/scripts/plot_fig_jsd_decay.py /root/autodl-tmp/gen-depth-contamination/scripts/plot_filtering_strategies.py /root/autodl-tmp/gen-depth-contamination/scripts/draw_kstar_theta.py /root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap.py /root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap_v2.py /root/autodl-tmp/gen-depth-contamination/scripts/draw_sweep_figure.py /root/autodl-tmp/gen-depth-contamination/scripts/plot_retrain_decay.py /root/autodl-tmp/gen-depth-contamination/scripts/plot_retrain_decay_v2.py /root/autodl-tmp/gen-depth-contamination/scripts/plot_feature_importance.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a07630de-484c-49de-9720-2c4d6854be4c",
  "isSidechain": false,
  "requestId": "req_011CbPrspyTJ7tcK6KHrLpRk",
  "type": "assistant",
  "uuid": "b33f4b72-d1a3-4e96-bc00-c1ebb0a24cfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFAMdzRjtavu1oCLwNRtfm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 50343,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1214,
          "cache_read_input_tokens": 50343,
          "cache_creation_input_tokens": 4550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4550
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

_source line 38 · 2026-05-25T19:44:54.959Z_

<details><summary>↩ Tool result · `toolu_01Vw93wRQNRsP7euJfCWkjC4`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b33f4b72-d1a3-4e96-bc00-c1ebb0a24cfa",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "875f02a7-23e8-4dc4-a83d-7013303c33f5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "b33f4b72-d1a3-4e96-bc00-c1ebb0a24cfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-25T19:45:10.888Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JuDov7daXicZwuFbR7gqHC`</summary>

````json
{
  "description": "Extract registry metrics for audit",
  "prompt": "I need you to extract specific metrics from a large registry JSON file for a paper audit. The file is at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/93bdb0df-e478-43c2-a08d-406b4a0808e1/tool-results/mcp-agent-ml-research-read_registry-1779738280345.txt\n\nThe file format is JSON with schema: {result: string} — the \"result\" value is a JSON string that needs to be parsed again.\n\nPlease extract the following information from ALL experiments in the registry. For each experiment, I need:\n1. experiment_id\n2. status\n3. All metrics (especially pairwise AUC values, K*, accuracy, MMLU, HellaSwag, Spearman rho, bootstrap CIs, etc.)\n4. Any key parameters (model, decoding config, domain, etc.)\n\nFocus especially on these experiment IDs:\n- mvp_pilot_sat_v1 (Qwen-1.5B rewrite)\n- exp_001_pythia_depth (Pythia-1.4B)\n- exp_002_olmo_depth (OLMo-1B)\n- exp_003_decoding_ablation\n- exp_006_graduated_filtering\n- exp_008_retrain_chain_v2\n- exp_011_llm_zeroshot (LLM zero-shot)\n- exp_012_binary_detector\n- exp_013_cross_transfer\n- exp_015_neural_probe\n- exp_020_pythia_decoding\n- exp_024_arxiv_domain\n- exp_028_power_curve\n- Any experiments with \"bootstrap\", \"10k\", \"seed\", \"dose\", \"length\", \"deberta\", \"gemma\", \"llama\", \"mistral\", \"scorer\", \"anova\", \"bonferroni\" in their ID\n\nFor each experiment, output the experiment_id and all its metrics in a structured format. Be thorough - I need every metric value to cross-check against the paper.\n\nOutput format: for each experiment, print:\n```\n=== experiment_id ===\nstatus: ...\nmetrics: {key: value, ...}\nkey_params: {key: value, ...}\n```\n\nThis is a research task - just read and report, don't write any files.",
  "subagent_type": "general-purpose"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "875f02a7-23e8-4dc4-a83d-7013303c33f5",
  "isSidechain": false,
  "requestId": "req_011CbPrspyTJ7tcK6KHrLpRk",
  "type": "assistant",
  "uuid": "81a4aeec-7868-436e-963d-63f99df2835b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFAMdzRjtavu1oCLwNRtfm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4550,
      "cache_read_input_tokens": 50343,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1214,
          "cache_read_input_tokens": 50343,
          "cache_creation_input_tokens": 4550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4550
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

_source line 40_

```json
{
  "type": "last-prompt",
  "leafUuid": "81a4aeec-7868-436e-963d-63f99df2835b",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit appendix and figure data sources",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Tool result

_source line 42 · 2026-05-25T19:50:01.515Z_

<details><summary>↩ Tool result · `toolu_01JuDov7daXicZwuFbR7gqHC`</summary>

```text
No anova/bonferroni-named experiments exist. Now let me compile the complete structured report.

Here is the complete extraction of all requested experiments from the registry (176 total experiments, 90 matched).

---

## PRIMARY EXPERIMENTS (13)

### === mvp_pilot_sat_v1 ===
- **status:** DONE
- **metrics:**
  - pairwise_auc: 0v1=0.9956, 1v2=0.6957, 2v3=0.5893, 3v4=0.5434, 4v5=0.5343
  - pairwise_auc_std: 0v1=0.0005, 1v2=0.0072, 2v3=0.012, 3v4=0.0053, 4v5=0.0091
  - pairwise_jsd: 0v1=0.2669, 1v2=0.0163, 2v3=0.0069, 3v4=0.0047, 4v5=0.0041
  - k_star: 2, ordinal_mae: 1.0163, ordinal_accuracy: 0.4182
- **key_params:** Qwen2.5-1.5B-Instruct rewrite mode, C4, 5K docs, seed=42, gpu_hours=2.65

### === exp_001_pythia_depth ===
- **status:** DONE
- **metrics:**
  - k_star: 2
  - pairwise_auc: 0v1=0.9722, 1v2=0.6074, 2v3=0.544, 3v4=0.5051, 4v5=0.5079
  - pairwise_auc_std: 0v1=0.0039, 1v2=0.0078, 2v3=0.0067, 3v4=0.0032, 4v5=0.0101
  - bootstrap_ci 1v2: auc_oof=0.6072, ci_95=[0.5975, 0.6172], ci_995_bonferroni=[0.5934, 0.621], perm_p=0.0001, bonferroni_pass=false
  - scorer: Qwen2.5-1.5B-Instruct
  - Note: Self-scored 1v2=0.6539, Qwen-scored 1v2=0.6074
- **key_params:** Pythia-1.4B, C4, 5K docs, continuation mode, seed=42, gpu_hours=3.43

### === exp_002_olmo_depth ===
- **status:** DONE
- **metrics:**
  - k_star: 1
  - pairwise_auc: 0v1=0.9861, 1v2=0.5001, 2v3=0.4972, 3v4=0.5034, 4v5=0.4971
  - scorer: Qwen2.5-1.5B-Instruct
  - Note: Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1
- **key_params:** OLMo-1B, C4, 5K docs, continuation mode, seed=42, gpu_hours=2.33

### === exp_003_decoding_ablation ===
- **status:** DONE
- **metrics:**
  - K_star: 2, K_star_robust: true
  - config1_greedy: 0v1=0.9796[0.9772,0.982], 1v2=0.6892[0.6802,0.6982], 2v3=0.5612[0.5517,0.5705], 3v4=0.5405[0.5308,0.5502], 4v5=0.5137[0.5033,0.5238]
  - config2_nuc09: 0v1=0.9945[0.9934,0.9956], 1v2=0.6862[0.6774,0.6951], 2v3=0.5917[0.5824,0.601], 3v4=0.5468[0.5369,0.5568], 4v5=0.5066[0.4959,0.5173]
  - config3_t07: 0v1=0.9877[0.9857,0.9896], 1v2=0.6885[0.6797,0.697], 2v3=0.5901[0.5806,0.5996], 3v4=0.539[0.5288,0.5493], 4v5=0.5348[0.5243,0.5454]
  - config4_t12: 0v1=0.9982[0.9975,0.9987], 1v2=0.7037[0.6945,0.7126], 2v3=0.582[0.5722,0.5917], 3v4=0.5293[0.5185,0.5399], 4v5=0.5237[0.5132,0.5347]
  - 10000 bootstrap resamples, GroupKFold(5) OOF + doc-level bootstrap + label permutation
- **key_params:** Qwen2.5-1.5B-Instruct, 4 configs (greedy/nuc p=0.9/T=0.7/T=1.2), seed=42

### === exp_006_graduated_filtering ===
- **status:** DONE
- **metrics:**
  - total_runs: 51
  - binary_ours: MMLU=0.5941+/-0.0008, HellaSwag=0.6701+/-0.0006
  - binary_drayson: MMLU=0.5913+/-0.0009, HellaSwag=0.6691+/-0.0004
  - surprisal: MMLU=0.5894+/-0.0009, HellaSwag=0.6641+/-0.0006
  - graduated_a09: MMLU=0.5892+/-0.0008, HellaSwag=0.6701+/-0.0007
  - graduated_a07: MMLU=0.5892+/-0.0014, HellaSwag=0.6695+/-0.0004
  - graduated_a05: MMLU=0.5880+/-0.0013, HellaSwag=0.6687+/-0.0008
  - graduated_a03: MMLU=0.5877+/-0.0013, HellaSwag=0.6669+/-0.0005
  - graduated_a01: MMLU=0.5873+/-0.0019, HellaSwag=0.6640+/-0.0009
  - dsir: MMLU=0.5869+/-0.0003, HellaSwag=0.6631+/-0.0007
  - no_filter: MMLU=0.5865+/-0.0010, HellaSwag=0.6638+/-0.0008
  - base_model: MMLU=0.6018, HellaSwag=0.6821
  - best_strategy: binary-ours
- **key_params:** Qwen2.5-1.5B-Instruct, 6 strategies x 5 seeds, C4 30K docs, LoRA fine-tune

### === exp_008_retrain_chain_v2 ===
- **status:** DONE
- **metrics:**
  - k_star: ">=4"
  - pairwise_auc: 0v1=0.9847, 1v2=0.9484, 2v3=0.8888, 3v4=0.7982
  - pairwise_jsd: 0v1=0.17, 1v2=0.12, 2v3=0.064, 3v4=0.04
  - key_finding: Retrain-chain K*>=4, prompt-chain K*=2 is text-intrinsic boundary
- **key_params:** Pythia-1.4B + LoRA (rank=16, alpha=32), C4 5K, depth 0-4, scorer=Qwen2.5-1.5B

### === exp_011_llm_zeroshot ===
- **status:** DONE
- **metrics:**
  - gpt55_5class_acc: 0.332, gpt55_mae: 1.102, gpt55_spearman: 0.383, gpt55_binary_acc: 0.878
  - claude_5class_acc: 0.331, claude_mae: 1.15, claude_spearman: 0.416, claude_binary_acc: 0.882
  - odb_baseline_5class_acc: 0.386, odb_baseline_mae: 1.107
  - gpt55_per_depth_acc: d0=0.77, d1=0.19, d2=0.38, d3=0.24, d4=0.08
  - claude_per_depth_acc: d0=0.69, d1=0.21, d2=0.28, d3=0.101, d4=0.37
  - n_samples_per_model: 500
- **key_params:** GPT-5.5 + Claude Opus 4.6, zero-shot, 500 samples from Pythia continuation

### === exp_012_binary_confidence ===
- **status:** DONE (note: registry ID is exp_012_binary_confidence, not exp_012_binary_detector)
- **metrics:**
  - n_samples: 500, generators: [qwen-rewrite, pythia-1.4b, olmo-1b, qwen-cont]
  - 6class_accuracy: qwen-rw=0.1987, pythia=0.1303, olmo=0.127, qwen-cont=0.1833, random=0.1667
  - spearman_rho: qwen-rw log_ppl_ref=-0.1233 / log_ppl_obs=0.0815 / ppl_ratio=0.1185; pythia log_ppl_ref=-0.2972 / log_ppl_obs=-0.4529 / ppl_ratio=-0.392; olmo log_ppl_ref=-0.378 / log_ppl_obs=-0.4614 / ppl_ratio=-0.4068; qwen-cont log_ppl_ref=-0.3887 / log_ppl_obs=-0.162 / ppl_ratio=-0.058
  - binary_detector_kstar: 1, obd_kstar: 2, auc_non_monotonic: true
- **key_params:** DivEye/Binoculars binary confidence vs depth

### === exp_013_cross_transfer ===
- **status:** DONE
- **metrics:**
  - 4x4 accuracy matrix (selected): Qwen_rw->Qwen_rw=0.4229, Pythia->Pythia=0.3856, OLMo->OLMo=0.3822, Qwen_cont->Qwen_cont=0.3875
  - transfer_retention_accuracy: Pythia<->OLMo 91-92%, Qwen_rw->Pythia/OLMo 61-63%, Qwen_cont<->Pythia 83-85%
  - mean_pw_auc: within_avg=0.6099, cross_avg=0.5905, 0v1_cross_all_above=0.96
  - key_finding: depth signal ~70-85% text-intrinsic + 15-30% model self-familiarity
- **key_params:** 4x4 cross-model transfer (Qwen-rw, Pythia, OLMo, Qwen-cont), OBD-LightGBM

### === exp_015_neural_probe ===
- **status:** DONE
- **metrics:**
  - k_star_qwen: 3, k_star_pythia: 2, k_star_olmo: 1
  - qwen_pairwise_auc: 0v1=0.988, 1v2=0.702, 2v3=0.616, 3v4=0.59, 4v5=0.566
  - pythia_pairwise_auc: 0v1=0.966, 1v2=0.676, 2v3=0.596, 3v4=0.555, 4v5=0.532
  - olmo_pairwise_auc: 0v1=0.9773, 1v2=0.5054, 2v3=0.5056, 3v4=0.5032, 4v5=0.4999
  - Note: OLMo values from rerun (self-probe), K*=1 not K*=2
- **key_params:** Frozen LLM -> MLP probe, Qwen2.5-1.5B-Instruct encoder, 5-fold CV

### === exp_020_pythia_decoding ===
- **status:** DONE
- **metrics:**
  - greedy: K*=2, 0v1=0.9992, 1v2=0.8838, 2v3=0.5342, 3v4=0.5228, 4v5=0.5162
  - nuc09: K*=2, 0v1=0.9948, 1v2=0.677, 2v3=0.5549, 3v4=0.5299, 4v5=0.5013
  - t07: K*=2, 0v1=0.9965, 1v2=0.7265, 2v3=0.5941, 3v4=0.5698, 4v5=0.5284
  - t12: K*=2, 0v1=0.9933, 1v2=0.6172, 2v3=0.5226, 3v4=0.517, 4v5=0.5051
  - Bootstrap: t07 2v3 AUC=0.5939 CI [0.5855,0.6025] BORDERLINE; t12 1v2 AUC=0.617 CI [0.6071,0.627] PASS
  - Note: greedy 1v2=0.8838 due to repetition collapse (4-gram repeat: d0=0.01->d1=0.72->d2=0.81)
- **key_params:** Pythia-1.4B, 4 configs, C4 5K, depth 0-5

### === exp_024_arxiv_domain ===
- **status:** DONE
- **metrics:**
  - K_star: 3
  - pairwise_auc: 0v1=0.9946, 1v2=0.858, 2v3=0.6427, 3v4=0.5437, 4v5=0.5294
  - bootstrap_ci: 0v1 [0.9929,0.9961], 1v2 [0.848,0.8679], 2v3 [0.6275,0.6575], 3v4 [0.5276,0.5598], 4v5 [0.5133,0.5455]
  - All perm_p=0.0001 except 4v5=0.0006
  - 10000 bootstrap + 10000 permutation resamples
  - key_finding: arXiv K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > theta=0.60. First condition with K*>2.
- **key_params:** Qwen2.5-1.5B (base), arXiv, 2200 docs, continuation, nucleus p=0.95 T=1.0

### === exp_028_power_curve ===
- **status:** DONE
- **metrics:**
  - min_n_100pct: 2000
  - n500: AUC=0.5808, rate=0.2; n1000: AUC=0.5911, rate=0.3; n2000: AUC=0.6101, rate=1.0; n3000: AUC=0.6166, rate=1.0; n4000: AUC=0.622, rate=1.0; n5000: AUC=0.6288, rate=1.0
- **key_params:** Subsampling analysis, 10 resamples per n, 5-fold CV, C4 data

---

## SECONDARY EXPERIMENTS (77 matched by keyword)

### Bootstrap/CI experiments

**exp_007_bootstrap_ci** (DONE): 4 model configs, all k_star_robust=true, all_1v2_ci_lower_above_060=true
- qwen_rewrite: 1v2 AUC=0.6955 CI [0.6859,0.7041]
- pythia_cont: 1v2 AUC=0.6539 CI [0.6454,0.663]
- olmo_cont: 1v2 AUC=0.6145 CI [0.6045,0.6247]
- qwen_cont: 1v2 AUC=0.6112 CI [0.6015,0.6213] (most marginal, only 0.0015 above threshold)

**exp_bootstrap_10k** (DONE): 4 configs tested, no substantive K* flips. 10K CI ~3% tighter than 1K.
- llama8b: AUC=0.6075, ci_10k=[0.598,0.617] BORDERLINE
- gemma2b: AUC=0.5981, ci_10k=[0.588,0.608] BORDERLINE
- mistral7b: AUC=0.5902, ci_10k=[0.58,0.6] K*=1
- 512tok: AUC=0.6136, ci_10k=[0.604,0.623] K*=2

**exp_027_retrain_bootstrap** (DONE): 10000 iterations, all 4 retrain-chain pairs CI_lower >> theta=0.60
- 0v1: 0.9847 CI [0.9828,0.9864]; 1v2: 0.9482 CI [0.9443,0.952]; 2v3: 0.8885 CI [0.8829,0.894]; 3v4: 0.7977 CI [0.7903,0.8051]

**exp_C_permutation_10k** (DONE): 10K permutation confirms all boundary p<0.0001

### 10K sample-size experiments

**exp_gemma2b_10k** (DONE): K*_self=2, K*_qwen=2 (borderline). 1v2 AUC=0.6099, Bonf CI percentile FAIL (0.5998), normal PASS (0.6003)
**exp_olmo1b_10k** (DONE): K*=1, 1v2=0.4984 (chance)
**exp_llama8b_10k** (DONE): K*=1, 1v2 oof=0.588, Bonf CI=[0.5776,0.5978], bonferroni_pass=false
**exp_pythia14b_c4_10k** (DONE): K*=2, 1v2=0.6175, Bonf CI=[0.6078,0.6273], bonferroni_pass=true
**exp_qwen_cont_10k** (DONE): K*=2, 1v2=0.6346, Bonf CI=[0.6255,0.6436], bonferroni_pass=true

### Seed experiments

**seed_gemma27b_c4_s42** (DONE): Self K*=2 (1v2=0.6196), Qwen cross K*=1 (1v2=0.5894)
**seed_pythia14b_wiki_s123** (DONE): no metrics recorded (seed=123 replication)
**seed_qwen15b_c4_s123** (DONE): no metrics recorded (seed=123 replication)
**seed_qwen15b_wiki_s123** (DONE): no metrics recorded (seed=123 replication)
**seed2_binary_ours** (PREPARING), **seed2_graduated** (PREPARING), **seed2_no_filter** (PREPARING)

### Dose-response experiments

**exp_009_dose_10pct_v3** (DONE): 5 seeds x 3 strategies. no_filter MMLU=0.6058+/-0.0002, binary_ours=0.6079+/-0.0005, graduated=0.6066+/-0.0011. binary_vs_nofilter delta_mmlu=+0.0021 p=0.001. graduated_vs_binary delta_mmlu=-0.0014 p=0.0917
**exp_009_dose_30pct_v3** (DONE): no_filter MMLU=0.6069+/-0.0007, binary=0.6082+/-0.0012, graduated=0.6072+/-0.0008. binary_vs_nofilter delta_hellaswag=+0.0061 p=0.0036
**exp_009_dose_50pct_v3** (DONE): no_filter MMLU=0.6063+/-0.0013, binary=0.6088+/-0.0011, graduated=0.6062+/-0.0009. binary_vs_nofilter delta_hellaswag=+0.0051 p=2e-05. graduated=no_filter exactly.
**exp_009_dose_response** (DONE): 45 total runs. Binary consistently best. Graduated=no_filter at every ratio. HellaSwag binary advantage: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp. C3 hypothesis (graduated>binary) rejected.

### Length ablation

**exp_021_length_ablation** (DONE): 128tok K*=2 1v2=0.6219, 256tok K*=2 1v2=0.6282, 512tok K*=2 1v2=0.6073. 512tok 1v2 bootstrap BORDERLINE (CI [0.5979,0.6166])

### DeBERTa experiments

**exp_deberta_c4** (DONE): kstar=2, 1v2=0.6781 CI [0.6696,0.6866], 2v3=0.5895 CI [0.5814,0.5979], n=30000
**exp_deberta_c4_1b5** (DONE): kstar=2 (qwen_rw config), 1v2=0.7052, obd_baseline 1v2=0.6262, delta=+7.9pp
**exp_deberta_c4_1b5_pythia** (DONE): kstar=2, 1v2=0.9284 CI [0.923,0.9331], obd_baseline=0.8838, delta=+4.5pp
**exp_deberta_c4_1b5_qwen_cont** (DONE): kstar=2, 1v2=0.7194, obd_baseline=0.6282, delta=+9.1pp
**exp_deberta_code_qwen1b5** (DONE): K*=2, 1v2=0.8076 CI [0.8001,0.8147], obd_1v2=0.7382
**exp_deberta_arxiv_qwen1b5** (DONE): K*=4, 1v2=0.9214, 2v3=0.7446, 3v4=0.6238 CI_lower=0.6127
**exp_deberta_upperbound** (DONE): Wiki: pythia K*=3, olmo K*=1, qwen7b K*=3, llama8b K*=3, mistral7b K*=3. DeBERTa breaks OBD boundary on wiki (K*=3 vs K*=2).
**exp_deberta_filtering_comparison** (DONE): no_filter MMLU=0.5895, obd_binary MMLU=0.588, deberta_binary=0.587, deberta_graduated=0.5884. obd_binary >= deberta on all 3 benchmarks.
**exp_deberta_cross_transfer_wiki** (DONE): 10 pairs, K*=1 for 3 pairs (all X->OLMo), K*=2 for 5 pairs, K*=3 for 1 pair (pythia->qwen7b)
**deberta_filter_***: 5 experiments all PREPARING status

### Gemma experiments

**exp_gemma2b_depth** (DONE): K*=1, 1v2=0.5981 (below theta), CI [0.5882,0.6076]
**exp_gemma27b_c4** (DONE): self_scorer K*=2 (1v2=0.6196 CI [0.6096,0.6296]), cross_scorer K*=1 (1v2=0.5895 CI [0.5795,0.5997])
**gemma27b_cross_transfer** (DONE): 27B->small retention 101.3% (classifier works BETTER). small->27B only 76.5%.
**gemma27b_filtering** (DONE): binary_ours MMLU=0.5958, no_filter=0.5956, delta=+0.02pp. HellaSwag delta=+0.41pp.

### LLaMA experiments

**exp_018_llama8b_depth** (DONE): K*=2, 1v2=0.6123 CI [0.6028,0.6216], 10000 bootstrap+perm
**exp_arXiv_llama8b** (DONE): K*=3, 1v2=0.8447, 2v3=0.6215
**exp_arXiv_llama8b_crossscorer** (DONE): K*=3, scorer=pythia-1.4b, 1v2=0.8433, 2v3=0.6201
**exp_code_llama8b** (DONE): K*=2, 1v2=0.7394
**exp_cross_transfer_llama8b_to_qwen7b_v2** (DONE): K*=3, 2v3 CI_lower=0.6124
**exp_cross_transfer_qwen7b_to_llama8b** (DONE): K*=3, 1v2=0.7384, 2v3=0.6278
**exp_wiki_llama8b** (DONE): K*=1, 1v2=0.5954, Bonf CI upper=0.6049 (borderline)
**wiki_domain_llama** (DONE): K*=1, 1v2=0.5919, Bonf CI [0.5788,0.6049]

### Mistral experiments

**exp_019_mistral7b_depth** (DONE): K*=1, 1v2=0.5935, bootstrap CI [0.5835,0.6032]
**exp_019b_mistral_cross_scorer** (DONE): K*=1, 1v2=0.5695 CI [0.5645,0.5746] (cross-scorer LOWER than self)
**exp_arXiv_mistral7b** (DONE): K*=3, 1v2=0.8201, 2v3=0.6275
**exp_arXiv_mistral7b_crossscorer** (DONE): K*=3, scorer=pythia-1.4b, 1v2=0.8141, 2v3=0.6075
**exp_code_mistral7b** (DONE): K*=2, 1v2=0.6152
**code_domain_mistral** (DONE): K*=2, 1v2=0.615, Bonf CI [0.6024,0.6281]
**exp_wiki_mistral7b** (DONE): K*=1, 1v2=0.5552
**wiki_domain_mistral** (DONE): K*=1, 1v2=0.5576, Bonf CI [0.5434,0.5716]

### Scorer experiments

**exp_A_alt_scorer** (DONE): K* splits by generator not scorer. Qwen-RW->K*=2, Qwen-cont->K*=1 regardless of scorer. Feature importance rho>=0.90 across all 4 conditions.
**exp_7b_scorer_ablation** (DONE): pythia K*(1.5B)=2 == K*(7B)=2; olmo K*(1.5B)=1 == K*(7B)=1
**exp_7b_scorer_arxiv** (DONE): pythia arXiv K*=3 identical for 1.5B vs 7B scorer; olmo arXiv K*=1 identical
**exp_022_cross_scorer_matrix** (DONE): 12 combos, K*=2 in 11/12. Only exception: qwen_cont256 x pythia (1v2=0.5979). Scorer choice delta_1v2 < 0.025.
**exp_wiki_scorer_confound** (DONE): K*=1, confound confirmed, 1v2=0.587 (delta=-0.0238 vs Qwen scorer)
**exp_wiki_scorer_confound_1b5** (DONE): K*=1, confound confirmed, 1v2=0.5994
**exp_arXiv_qwen1b5_crossscorer** (DONE): K*=3, 1v2=0.8105, 2v3=0.6317
**exp_arXiv_qwen7b_crossscorer** (DONE): K*=2 (drops from 3), 2v3=0.5989 < 0.60, mild Qwen family bias ~0.027
**exp_arXiv_mistral7b_crossscorer** (DONE): K*=3, scorer=pythia-1.4b
**exp_arXiv_llama8b_crossscorer** (DONE): K*=3, scorer=pythia-1.4b
**exp_code_qwen1b5_pythia_scorer** (DONE): K*=2, 1v2=0.7197, scorer=pythia-1.4b
**olmo_arxiv_cross_scorer** (DONE): K*=1, 1v2=0.4996 (chance), scorer=Qwen2.5-1.5B-Instruct
**olmo_c4_cross_scorer** (DONE): K*=1, 1v2=0.4999 (chance)

### Cross-scorer OLMo

Both OLMo cross-scorer experiments (arXiv and C4) confirm K*=1 with 1v2 at chance level (~0.50).

---

No experiments with "anova" or "bonferroni" in their IDs were found. Bonferroni corrections appear within experiment metrics (e.g., ci_995_bonferroni fields in exp_001, exp_gemma2b_10k, exp_llama8b_10k, exp_pythia14b_c4_10k, exp_qwen_cont_10k, and bootstrap_ci_bonf in wiki_domain_llama, wiki_domain_mistral, code_domain_mistral).

agentId: a3a23f63b80a1ec4d (use SendMessage with to: 'a3a23f63b80a1ec4d' to continue this agent)
&lt;usage>total_tokens: 94996
tool_uses: 16
duration_ms: 290622&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "81a4aeec-7868-436e-963d-63f99df2835b",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "13dfe777-e948-4fb2-a9a3-52783a7e7c35",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to extract specific metrics from a large registry JSON file for a paper audit. The file is at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/93bdb0df-e478-43c2-a08d-406b4a0808e1/tool-results/mcp-agent-ml-research-read_registry-1779738280345.txt\n\nThe file format is JSON with schema: {result: string} — the \"result\" value is a JSON string that needs to be parsed again.\n\nPlease extract the following information from ALL experiments in the registry. For each experiment, I need:\n1. experiment_id\n2. status\n3. All metrics (especially pairwise AUC values, K*, accuracy, MMLU, HellaSwag, Spearman rho, bootstrap CIs, etc.)\n4. Any key parameters (model, decoding config, domain, etc.)\n\nFocus especially on these experiment IDs:\n- mvp_pilot_sat_v1 (Qwen-1.5B rewrite)\n- exp_001_pythia_depth (Pythia-1.4B)\n- exp_002_olmo_depth (OLMo-1B)\n- exp_003_decoding_ablation\n- exp_006_graduated_filtering\n- exp_008_retrain_chain_v2\n- exp_011_llm_zeroshot (LLM zero-shot)\n- exp_012_binary_detector\n- exp_013_cross_transfer\n- exp_015_neural_probe\n- exp_020_pythia_decoding\n- exp_024_arxiv_domain\n- exp_028_power_curve\n- Any experiments with \"bootstrap\", \"10k\", \"seed\", \"dose\", \"length\", \"deberta\", \"gemma\", \"llama\", \"mistral\", \"scorer\", \"anova\", \"bonferroni\" in their ID\n\nFor each experiment, output the experiment_id and all its metrics in a structured format. Be thorough - I need every metric value to cross-check against the paper.\n\nOutput format: for each experiment, print:\n```\n=== experiment_id ===\nstatus: ...\nmetrics: {key: value, ...}\nkey_params: {key: value, ...}\n```\n\nThis is a research task - just read and report, don't write any files.",
    "agentId": "a3a23f63b80a1ec4d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "No anova/bonferroni-named experiments exist. Now let me compile the complete structured report.\n\nHere is the complete extraction of all requested experiments from the registry (176 total experiments, 90 matched).\n\n---\n\n## PRIMARY EXPERIMENTS (13)\n\n### === mvp_pilot_sat_v1 ===\n- **status:** DONE\n- **metrics:**\n  - pairwise_auc: 0v1=0.9956, 1v2=0.6957, 2v3=0.5893, 3v4=0.5434, 4v5=0.5343\n  - pairwise_auc_std: 0v1=0.0005, 1v2=0.0072, 2v3=0.012, 3v4=0.0053, 4v5=0.0091\n  - pairwise_jsd: 0v1=0.2669, 1v2=0.0163, 2v3=0.0069, 3v4=0.0047, 4v5=0.0041\n  - k_star: 2, ordinal_mae: 1.0163, ordinal_accuracy: 0.4182\n- **key_params:** Qwen2.5-1.5B-Instruct rewrite mode, C4, 5K docs, seed=42, gpu_hours=2.65\n\n### === exp_001_pythia_depth ===\n- **status:** DONE\n- **metrics:**\n  - k_star: 2\n  - pairwise_auc: 0v1=0.9722, 1v2=0.6074, 2v3=0.544, 3v4=0.5051, 4v5=0.5079\n  - pairwise_auc_std: 0v1=0.0039, 1v2=0.0078, 2v3=0.0067, 3v4=0.0032, 4v5=0.0101\n  - bootstrap_ci 1v2: auc_oof=0.6072, ci_95=[0.5975, 0.6172], ci_995_bonferroni=[0.5934, 0.621], perm_p=0.0001, bonferroni_pass=false\n  - scorer: Qwen2.5-1.5B-Instruct\n  - Note: Self-scored 1v2=0.6539, Qwen-scored 1v2=0.6074\n- **key_params:** Pythia-1.4B, C4, 5K docs, continuation mode, seed=42, gpu_hours=3.43\n\n### === exp_002_olmo_depth ===\n- **status:** DONE\n- **metrics:**\n  - k_star: 1\n  - pairwise_auc: 0v1=0.9861, 1v2=0.5001, 2v3=0.4972, 3v4=0.5034, 4v5=0.4971\n  - scorer: Qwen2.5-1.5B-Instruct\n  - Note: Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1\n- **key_params:** OLMo-1B, C4, 5K docs, continuation mode, seed=42, gpu_hours=2.33\n\n### === exp_003_decoding_ablation ===\n- **status:** DONE\n- **metrics:**\n  - K_star: 2, K_star_robust: true\n  - config1_greedy: 0v1=0.9796[0.9772,0.982], 1v2=0.6892[0.6802,0.6982], 2v3=0.5612[0.5517,0.5705], 3v4=0.5405[0.5308,0.5502], 4v5=0.5137[0.5033,0.5238]\n  - config2_nuc09: 0v1=0.9945[0.9934,0.9956], 1v2=0.6862[0.6774,0.6951], 2v3=0.5917[0.5824,0.601], 3v4=0.5468[0.5369,0.5568], 4v5=0.5066[0.4959,0.5173]\n  - config3_t07: 0v1=0.9877[0.9857,0.9896], 1v2=0.6885[0.6797,0.697], 2v3=0.5901[0.5806,0.5996], 3v4=0.539[0.5288,0.5493], 4v5=0.5348[0.5243,0.5454]\n  - config4_t12: 0v1=0.9982[0.9975,0.9987], 1v2=0.7037[0.6945,0.7126], 2v3=0.582[0.5722,0.5917], 3v4=0.5293[0.5185,0.5399], 4v5=0.5237[0.5132,0.5347]\n  - 10000 bootstrap resamples, GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- **key_params:** Qwen2.5-1.5B-Instruct, 4 configs (greedy/nuc p=0.9/T=0.7/T=1.2), seed=42\n\n### === exp_006_graduated_filtering ===\n- **status:** DONE\n- **metrics:**\n  - total_runs: 51\n  - binary_ours: MMLU=0.5941+/-0.0008, HellaSwag=0.6701+/-0.0006\n  - binary_drayson: MMLU=0.5913+/-0.0009, HellaSwag=0.6691+/-0.0004\n  - surprisal: MMLU=0.5894+/-0.0009, HellaSwag=0.6641+/-0.0006\n  - graduated_a09: MMLU=0.5892+/-0.0008, HellaSwag=0.6701+/-0.0007\n  - graduated_a07: MMLU=0.5892+/-0.0014, HellaSwag=0.6695+/-0.0004\n  - graduated_a05: MMLU=0.5880+/-0.0013, HellaSwag=0.6687+/-0.0008\n  - graduated_a03: MMLU=0.5877+/-0.0013, HellaSwag=0.6669+/-0.0005\n  - graduated_a01: MMLU=0.5873+/-0.0019, HellaSwag=0.6640+/-0.0009\n  - dsir: MMLU=0.5869+/-0.0003, HellaSwag=0.6631+/-0.0007\n  - no_filter: MMLU=0.5865+/-0.0010, HellaSwag=0.6638+/-0.0008\n  - base_model: MMLU=0.6018, HellaSwag=0.6821\n  - best_strategy: binary-ours\n- **key_params:** Qwen2.5-1.5B-Instruct, 6 strategies x 5 seeds, C4 30K docs, LoRA fine-tune\n\n### === exp_008_retrain_chain_v2 ===\n- **status:** DONE\n- **metrics:**\n  - k_star: \">=4\"\n  - pairwise_auc: 0v1=0.9847, 1v2=0.9484, 2v3=0.8888, 3v4=0.7982\n  - pairwise_jsd: 0v1=0.17, 1v2=0.12, 2v3=0.064, 3v4=0.04\n  - key_finding: Retrain-chain K*>=4, prompt-chain K*=2 is text-intrinsic boundary\n- **key_params:** Pythia-1.4B + LoRA (rank=16, alpha=32), C4 5K, depth 0-4, scorer=Qwen2.5-1.5B\n\n### === exp_011_llm_zeroshot ===\n- **status:** DONE\n- **metrics:**\n  - gpt55_5class_acc: 0.332, gpt55_mae: 1.102, gpt55_spearman: 0.383, gpt55_binary_acc: 0.878\n  - claude_5class_acc: 0.331, claude_mae: 1.15, claude_spearman: 0.416, claude_binary_acc: 0.882\n  - odb_baseline_5class_acc: 0.386, odb_baseline_mae: 1.107\n  - gpt55_per_depth_acc: d0=0.77, d1=0.19, d2=0.38, d3=0.24, d4=0.08\n  - claude_per_depth_acc: d0=0.69, d1=0.21, d2=0.28, d3=0.101, d4=0.37\n  - n_samples_per_model: 500\n- **key_params:** GPT-5.5 + Claude Opus 4.6, zero-shot, 500 samples from Pythia continuation\n\n### === exp_012_binary_confidence ===\n- **status:** DONE (note: registry ID is exp_012_binary_confidence, not exp_012_binary_detector)\n- **metrics:**\n  - n_samples: 500, generators: [qwen-rewrite, pythia-1.4b, olmo-1b, qwen-cont]\n  - 6class_accuracy: qwen-rw=0.1987, pythia=0.1303, olmo=0.127, qwen-cont=0.1833, random=0.1667\n  - spearman_rho: qwen-rw log_ppl_ref=-0.1233 / log_ppl_obs=0.0815 / ppl_ratio=0.1185; pythia log_ppl_ref=-0.2972 / log_ppl_obs=-0.4529 / ppl_ratio=-0.392; olmo log_ppl_ref=-0.378 / log_ppl_obs=-0.4614 / ppl_ratio=-0.4068; qwen-cont log_ppl_ref=-0.3887 / log_ppl_obs=-0.162 / ppl_ratio=-0.058\n  - binary_detector_kstar: 1, obd_kstar: 2, auc_non_monotonic: true\n- **key_params:** DivEye/Binoculars binary confidence vs depth\n\n### === exp_013_cross_transfer ===\n- **status:** DONE\n- **metrics:**\n  - 4x4 accuracy matrix (selected): Qwen_rw->Qwen_rw=0.4229, Pythia->Pythia=0.3856, OLMo->OLMo=0.3822, Qwen_cont->Qwen_cont=0.3875\n  - transfer_retention_accuracy: Pythia<->OLMo 91-92%, Qwen_rw->Pythia/OLMo 61-63%, Qwen_cont<->Pythia 83-85%\n  - mean_pw_auc: within_avg=0.6099, cross_avg=0.5905, 0v1_cross_all_above=0.96\n  - key_finding: depth signal ~70-85% text-intrinsic + 15-30% model self-familiarity\n- **key_params:** 4x4 cross-model transfer (Qwen-rw, Pythia, OLMo, Qwen-cont), OBD-LightGBM\n\n### === exp_015_neural_probe ===\n- **status:** DONE\n- **metrics:**\n  - k_star_qwen: 3, k_star_pythia: 2, k_star_olmo: 1\n  - qwen_pairwise_auc: 0v1=0.988, 1v2=0.702, 2v3=0.616, 3v4=0.59, 4v5=0.566\n  - pythia_pairwise_auc: 0v1=0.966, 1v2=0.676, 2v3=0.596, 3v4=0.555, 4v5=0.532\n  - olmo_pairwise_auc: 0v1=0.9773, 1v2=0.5054, 2v3=0.5056, 3v4=0.5032, 4v5=0.4999\n  - Note: OLMo values from rerun (self-probe), K*=1 not K*=2\n- **key_params:** Frozen LLM -> MLP probe, Qwen2.5-1.5B-Instruct encoder, 5-fold CV\n\n### === exp_020_pythia_decoding ===\n- **status:** DONE\n- **metrics:**\n  - greedy: K*=2, 0v1=0.9992, 1v2=0.8838, 2v3=0.5342, 3v4=0.5228, 4v5=0.5162\n  - nuc09: K*=2, 0v1=0.9948, 1v2=0.677, 2v3=0.5549, 3v4=0.5299, 4v5=0.5013\n  - t07: K*=2, 0v1=0.9965, 1v2=0.7265, 2v3=0.5941, 3v4=0.5698, 4v5=0.5284\n  - t12: K*=2, 0v1=0.9933, 1v2=0.6172, 2v3=0.5226, 3v4=0.517, 4v5=0.5051\n  - Bootstrap: t07 2v3 AUC=0.5939 CI [0.5855,0.6025] BORDERLINE; t12 1v2 AUC=0.617 CI [0.6071,0.627] PASS\n  - Note: greedy 1v2=0.8838 due to repetition collapse (4-gram repeat: d0=0.01->d1=0.72->d2=0.81)\n- **key_params:** Pythia-1.4B, 4 configs, C4 5K, depth 0-5\n\n### === exp_024_arxiv_domain ===\n- **status:** DONE\n- **metrics:**\n  - K_star: 3\n  - pairwise_auc: 0v1=0.9946, 1v2=0.858, 2v3=0.6427, 3v4=0.5437, 4v5=0.5294\n  - bootstrap_ci: 0v1 [0.9929,0.9961], 1v2 [0.848,0.8679], 2v3 [0.6275,0.6575], 3v4 [0.5276,0.5598], 4v5 [0.5133,0.5455]\n  - All perm_p=0.0001 except 4v5=0.0006\n  - 10000 bootstrap + 10000 permutation resamples\n  - key_finding: arXiv K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > theta=0.60. First condition with K*>2.\n- **key_params:** Qwen2.5-1.5B (base), arXiv, 2200 docs, continuation, nucleus p=0.95 T=1.0\n\n### === exp_028_power_curve ===\n- **status:** DONE\n- **metrics:**\n  - min_n_100pct: 2000\n  - n500: AUC=0.5808, rate=0.2; n1000: AUC=0.5911, rate=0.3; n2000: AUC=0.6101, rate=1.0; n3000: AUC=0.6166, rate=1.0; n4000: AUC=0.622, rate=1.0; n5000: AUC=0.6288, rate=1.0\n- **key_params:** Subsampling analysis, 10 resamples per n, 5-fold CV, C4 data\n\n---\n\n## SECONDARY EXPERIMENTS (77 matched by keyword)\n\n### Bootstrap/CI experiments\n\n**exp_007_bootstrap_ci** (DONE): 4 model configs, all k_star_robust=true, all_1v2_ci_lower_above_060=true\n- qwen_rewrite: 1v2 AUC=0.6955 CI [0.6859,0.7041]\n- pythia_cont: 1v2 AUC=0.6539 CI [0.6454,0.663]\n- olmo_cont: 1v2 AUC=0.6145 CI [0.6045,0.6247]\n- qwen_cont: 1v2 AUC=0.6112 CI [0.6015,0.6213] (most marginal, only 0.0015 above threshold)\n\n**exp_bootstrap_10k** (DONE): 4 configs tested, no substantive K* flips. 10K CI ~3% tighter than 1K.\n- llama8b: AUC=0.6075, ci_10k=[0.598,0.617] BORDERLINE\n- gemma2b: AUC=0.5981, ci_10k=[0.588,0.608] BORDERLINE\n- mistral7b: AUC=0.5902, ci_10k=[0.58,0.6] K*=1\n- 512tok: AUC=0.6136, ci_10k=[0.604,0.623] K*=2\n\n**exp_027_retrain_bootstrap** (DONE): 10000 iterations, all 4 retrain-chain pairs CI_lower >> theta=0.60\n- 0v1: 0.9847 CI [0.9828,0.9864]; 1v2: 0.9482 CI [0.9443,0.952]; 2v3: 0.8885 CI [0.8829,0.894]; 3v4: 0.7977 CI [0.7903,0.8051]\n\n**exp_C_permutation_10k** (DONE): 10K permutation confirms all boundary p<0.0001\n\n### 10K sample-size experiments\n\n**exp_gemma2b_10k** (DONE): K*_self=2, K*_qwen=2 (borderline). 1v2 AUC=0.6099, Bonf CI percentile FAIL (0.5998), normal PASS (0.6003)\n**exp_olmo1b_10k** (DONE): K*=1, 1v2=0.4984 (chance)\n**exp_llama8b_10k** (DONE): K*=1, 1v2 oof=0.588, Bonf CI=[0.5776,0.5978], bonferroni_pass=false\n**exp_pythia14b_c4_10k** (DONE): K*=2, 1v2=0.6175, Bonf CI=[0.6078,0.6273], bonferroni_pass=true\n**exp_qwen_cont_10k** (DONE): K*=2, 1v2=0.6346, Bonf CI=[0.6255,0.6436], bonferroni_pass=true\n\n### Seed experiments\n\n**seed_gemma27b_c4_s42** (DONE): Self K*=2 (1v2=0.6196), Qwen cross K*=1 (1v2=0.5894)\n**seed_pythia14b_wiki_s123** (DONE): no metrics recorded (seed=123 replication)\n**seed_qwen15b_c4_s123** (DONE): no metrics recorded (seed=123 replication)\n**seed_qwen15b_wiki_s123** (DONE): no metrics recorded (seed=123 replication)\n**seed2_binary_ours** (PREPARING), **seed2_graduated** (PREPARING), **seed2_no_filter** (PREPARING)\n\n### Dose-response experiments\n\n**exp_009_dose_10pct_v3** (DONE): 5 seeds x 3 strategies. no_filter MMLU=0.6058+/-0.0002, binary_ours=0.6079+/-0.0005, graduated=0.6066+/-0.0011. binary_vs_nofilter delta_mmlu=+0.0021 p=0.001. graduated_vs_binary delta_mmlu=-0.0014 p=0.0917\n**exp_009_dose_30pct_v3** (DONE): no_filter MMLU=0.6069+/-0.0007, binary=0.6082+/-0.0012, graduated=0.6072+/-0.0008. binary_vs_nofilter delta_hellaswag=+0.0061 p=0.0036\n**exp_009_dose_50pct_v3** (DONE): no_filter MMLU=0.6063+/-0.0013, binary=0.6088+/-0.0011, graduated=0.6062+/-0.0009. binary_vs_nofilter delta_hellaswag=+0.0051 p=2e-05. graduated=no_filter exactly.\n**exp_009_dose_response** (DONE): 45 total runs. Binary consistently best. Graduated=no_filter at every ratio. HellaSwag binary advantage: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp. C3 hypothesis (graduated>binary) rejected.\n\n### Length ablation\n\n**exp_021_length_ablation** (DONE): 128tok K*=2 1v2=0.6219, 256tok K*=2 1v2=0.6282, 512tok K*=2 1v2=0.6073. 512tok 1v2 bootstrap BORDERLINE (CI [0.5979,0.6166])\n\n### DeBERTa experiments\n\n**exp_deberta_c4** (DONE): kstar=2, 1v2=0.6781 CI [0.6696,0.6866], 2v3=0.5895 CI [0.5814,0.5979], n=30000\n**exp_deberta_c4_1b5** (DONE): kstar=2 (qwen_rw config), 1v2=0.7052, obd_baseline 1v2=0.6262, delta=+7.9pp\n**exp_deberta_c4_1b5_pythia** (DONE): kstar=2, 1v2=0.9284 CI [0.923,0.9331], obd_baseline=0.8838, delta=+4.5pp\n**exp_deberta_c4_1b5_qwen_cont** (DONE): kstar=2, 1v2=0.7194, obd_baseline=0.6282, delta=+9.1pp\n**exp_deberta_code_qwen1b5** (DONE): K*=2, 1v2=0.8076 CI [0.8001,0.8147], obd_1v2=0.7382\n**exp_deberta_arxiv_qwen1b5** (DONE): K*=4, 1v2=0.9214, 2v3=0.7446, 3v4=0.6238 CI_lower=0.6127\n**exp_deberta_upperbound** (DONE): Wiki: pythia K*=3, olmo K*=1, qwen7b K*=3, llama8b K*=3, mistral7b K*=3. DeBERTa breaks OBD boundary on wiki (K*=3 vs K*=2).\n**exp_deberta_filtering_comparison** (DONE): no_filter MMLU=0.5895, obd_binary MMLU=0.588, deberta_binary=0.587, deberta_graduated=0.5884. obd_binary >= deberta on all 3 benchmarks.\n**exp_deberta_cross_transfer_wiki** (DONE): 10 pairs, K*=1 for 3 pairs (all X->OLMo), K*=2 for 5 pairs, K*=3 for 1 pair (pythia->qwen7b)\n**deberta_filter_***: 5 experiments all PREPARING status\n\n### Gemma experiments\n\n**exp_gemma2b_depth** (DONE): K*=1, 1v2=0.5981 (below theta), CI [0.5882,0.6076]\n**exp_gemma27b_c4** (DONE): self_scorer K*=2 (1v2=0.6196 CI [0.6096,0.6296]), cross_scorer K*=1 (1v2=0.5895 CI [0.5795,0.5997])\n**gemma27b_cross_transfer** (DONE): 27B->small retention 101.3% (classifier works BETTER). small->27B only 76.5%.\n**gemma27b_filtering** (DONE): binary_ours MMLU=0.5958, no_filter=0.5956, delta=+0.02pp. HellaSwag delta=+0.41pp.\n\n### LLaMA experiments\n\n**exp_018_llama8b_depth** (DONE): K*=2, 1v2=0.6123 CI [0.6028,0.6216], 10000 bootstrap+perm\n**exp_arXiv_llama8b** (DONE): K*=3, 1v2=0.8447, 2v3=0.6215\n**exp_arXiv_llama8b_crossscorer** (DONE): K*=3, scorer=pythia-1.4b, 1v2=0.8433, 2v3=0.6201\n**exp_code_llama8b** (DONE): K*=2, 1v2=0.7394\n**exp_cross_transfer_llama8b_to_qwen7b_v2** (DONE): K*=3, 2v3 CI_lower=0.6124\n**exp_cross_transfer_qwen7b_to_llama8b** (DONE): K*=3, 1v2=0.7384, 2v3=0.6278\n**exp_wiki_llama8b** (DONE): K*=1, 1v2=0.5954, Bonf CI upper=0.6049 (borderline)\n**wiki_domain_llama** (DONE): K*=1, 1v2=0.5919, Bonf CI [0.5788,0.6049]\n\n### Mistral experiments\n\n**exp_019_mistral7b_depth** (DONE): K*=1, 1v2=0.5935, bootstrap CI [0.5835,0.6032]\n**exp_019b_mistral_cross_scorer** (DONE): K*=1, 1v2=0.5695 CI [0.5645,0.5746] (cross-scorer LOWER than self)\n**exp_arXiv_mistral7b** (DONE): K*=3, 1v2=0.8201, 2v3=0.6275\n**exp_arXiv_mistral7b_crossscorer** (DONE): K*=3, scorer=pythia-1.4b, 1v2=0.8141, 2v3=0.6075\n**exp_code_mistral7b** (DONE): K*=2, 1v2=0.6152\n**code_domain_mistral** (DONE): K*=2, 1v2=0.615, Bonf CI [0.6024,0.6281]\n**exp_wiki_mistral7b** (DONE): K*=1, 1v2=0.5552\n**wiki_domain_mistral** (DONE): K*=1, 1v2=0.5576, Bonf CI [0.5434,0.5716]\n\n### Scorer experiments\n\n**exp_A_alt_scorer** (DONE): K* splits by generator not scorer. Qwen-RW->K*=2, Qwen-cont->K*=1 regardless of scorer. Feature importance rho>=0.90 across all 4 conditions.\n**exp_7b_scorer_ablation** (DONE): pythia K*(1.5B)=2 == K*(7B)=2; olmo K*(1.5B)=1 == K*(7B)=1\n**exp_7b_scorer_arxiv** (DONE): pythia arXiv K*=3 identical for 1.5B vs 7B scorer; olmo arXiv K*=1 identical\n**exp_022_cross_scorer_matrix** (DONE): 12 combos, K*=2 in 11/12. Only exception: qwen_cont256 x pythia (1v2=0.5979). Scorer choice delta_1v2 < 0.025.\n**exp_wiki_scorer_confound** (DONE): K*=1, confound confirmed, 1v2=0.587 (delta=-0.0238 vs Qwen scorer)\n**exp_wiki_scorer_confound_1b5** (DONE): K*=1, confound confirmed, 1v2=0.5994\n**exp_arXiv_qwen1b5_crossscorer** (DONE): K*=3, 1v2=0.8105, 2v3=0.6317\n**exp_arXiv_qwen7b_crossscorer** (DONE): K*=2 (drops from 3), 2v3=0.5989 < 0.60, mild Qwen family bias ~0.027\n**exp_arXiv_mistral7b_crossscorer** (DONE): K*=3, scorer=pythia-1.4b\n**exp_arXiv_llama8b_crossscorer** (DONE): K*=3, scorer=pythia-1.4b\n**exp_code_qwen1b5_pythia_scorer** (DONE): K*=2, 1v2=0.7197, scorer=pythia-1.4b\n**olmo_arxiv_cross_scorer** (DONE): K*=1, 1v2=0.4996 (chance), scorer=Qwen2.5-1.5B-Instruct\n**olmo_c4_cross_scorer** (DONE): K*=1, 1v2=0.4999 (chance)\n\n### Cross-scorer OLMo\n\nBoth OLMo cross-scorer experiments (arXiv and C4) confirm K*=1 with 1v2 at chance level (~0.50).\n\n---\n\nNo experiments with \"anova\" or \"bonferroni\" in their IDs were found. Bonferroni corrections appear within experiment metrics (e.g., ci_995_bonferroni fields in exp_001, exp_gemma2b_10k, exp_llama8b_10k, exp_pythia14b_c4_10k, exp_qwen_cont_10k, and bootstrap_ci_bonf in wiki_domain_llama, wiki_domain_mistral, code_domain_mistral)."
      }
    ],
    "totalDurationMs": 290622,
    "totalTokens": 94996,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 412,
      "cache_read_input_tokens": 86460,
      "output_tokens": 8123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 412
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8123,
          "cache_read_input_tokens": 86460,
          "cache_creation_input_tokens": 412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 412,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 1,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "81a4aeec-7868-436e-963d-63f99df2835b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---


### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "leafUuid": "13dfe777-e948-4fb2-a9a3-52783a7e7c35",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit appendix and figure data sources",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Assistant

_source line 45 · 2026-05-25T19:50:05.014Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive registry dump. Let me now look at the figure generation scripts on the server. Let me search for data file reads in each plot script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13dfe777-e948-4fb2-a9a3-52783a7e7c35",
  "isSidechain": false,
  "requestId": "req_011CbPsHKrR66y7CuTdrmdTp",
  "type": "assistant",
  "uuid": "ea163120-9a9c-4e43-bdbd-b1b1e6e467c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D41U39bcSMKh1RuaG9252C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10241,
      "cache_read_input_tokens": 54893,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 683,
          "cache_read_input_tokens": 54893,
          "cache_creation_input_tokens": 10241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10241
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

_source line 46 · 2026-05-25T19:50:06.419Z_

Good, I have the registry data. Now let me trace each figure's generation script and data sources on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea163120-9a9c-4e43-bdbd-b1b1e6e467c0",
  "isSidechain": false,
  "requestId": "req_011CbPsHKrR66y7CuTdrmdTp",
  "type": "assistant",
  "uuid": "65760a95-2af8-4448-9597-1641e1d502dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D41U39bcSMKh1RuaG9252C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10241,
      "cache_read_input_tokens": 54893,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 683,
          "cache_read_input_tokens": 54893,
          "cache_creation_input_tokens": 10241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10241
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

_source line 47 · 2026-05-25T19:50:08.951Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Kpf7YndH8GBvDRkp3eGSb4`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"savefig\" /root/autodl-tmp/gen-depth-contamination/scripts/plot_fig2_merged.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65760a95-2af8-4448-9597-1641e1d502dc",
  "isSidechain": false,
  "requestId": "req_011CbPsHKrR66y7CuTdrmdTp",
  "type": "assistant",
  "uuid": "5e740aee-016c-4e3a-9c2f-b637703af75b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D41U39bcSMKh1RuaG9252C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10241,
      "cache_read_input_tokens": 54893,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 683,
          "cache_read_input_tokens": 54893,
          "cache_creation_input_tokens": 10241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10241
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

_source line 48 · 2026-05-25T19:50:09.356Z_

<details><summary>↩ Tool result · `toolu_01Kpf7YndH8GBvDRkp3eGSb4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"201:    fig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\n202:    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e740aee-016c-4e3a-9c2f-b637703af75b",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "366b80a9-2b3c-4c3c-9ddf-47005684523b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"201:    fig.savefig(pdf_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n202:    fig.savefig(png_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"201:    fig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\n202:    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "5e740aee-016c-4e3a-9c2f-b637703af75b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-25T19:50:09.917Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QxwThEkznTuJRXrVWCYdAT`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"savefig\" /root/autodl-tmp/gen-depth-contamination/scripts/plot_fig_jsd_decay.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "366b80a9-2b3c-4c3c-9ddf-47005684523b",
  "isSidechain": false,
  "requestId": "req_011CbPsHKrR66y7CuTdrmdTp",
  "type": "assistant",
  "uuid": "fdb3b943-d1f6-4769-9e76-e60dd3036c8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D41U39bcSMKh1RuaG9252C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10241,
      "cache_read_input_tokens": 54893,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 683,
          "cache_read_input_tokens": 54893,
          "cache_creation_input_tokens": 10241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10241
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

_source line 50 · 2026-05-25T19:50:10.323Z_

<details><summary>↩ Tool result · `toolu_01QxwThEkznTuJRXrVWCYdAT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"85:fig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\n86:fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdb3b943-d1f6-4769-9e76-e60dd3036c8c",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "1d33c44b-83d0-44a5-a05e-fe28113d815c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"85:fig.savefig(pdf_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n86:fig.savefig(png_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"85:fig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\n86:fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  },
  "sourceToolAssistantUUID": "fdb3b943-d1f6-4769-9e76-e60dd3036c8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-25T19:50:10.880Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01C7LRiNoyQXwDmVv3hiBFvE`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"savefig\" /root/autodl-tmp/gen-depth-contamination/scripts/plot_filtering_strategies.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d33c44b-83d0-44a5-a05e-fe28113d815c",
  "isSidechain": false,
  "requestId": "req_011CbPsHKrR66y7CuTdrmdTp",
  "type": "assistant",
  "uuid": "6f75a167-b3c0-4e26-9538-0922c4064514",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D41U39bcSMKh1RuaG9252C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10241,
      "cache_read_input_tokens": 54893,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 683,
          "cache_read_input_tokens": 54893,
          "cache_creation_input_tokens": 10241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10241
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

_source line 52 · 2026-05-25T19:50:11.284Z_

<details><summary>↩ Tool result · `toolu_01C7LRiNoyQXwDmVv3hiBFvE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"166:    fig.savefig(out_path, dpi=300, bbox_inches=\\\"tight\\\")\\n168:    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f75a167-b3c0-4e26-9538-0922c4064514",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "64c8510f-7588-4f73-bc4f-c9b951dd8912",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"166:    fig.savefig(out_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n168:    fig.savefig(png_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"166:    fig.savefig(out_path, dpi=300, bbox_inches=\\\"tight\\\")\\n168:    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  },
  "sourceToolAssistantUUID": "6f75a167-b3c0-4e26-9538-0922c4064514",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-25T19:50:11.805Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XxZwVXHhHYi8MpvYqkHT2V`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"savefig\" /root/autodl-tmp/gen-depth-contamination/scripts/draw_kstar_theta.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64c8510f-7588-4f73-bc4f-c9b951dd8912",
  "isSidechain": false,
  "requestId": "req_011CbPsHKrR66y7CuTdrmdTp",
  "type": "assistant",
  "uuid": "bad6b848-2175-4a7d-a275-96f73b1a6f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D41U39bcSMKh1RuaG9252C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10241,
      "cache_read_input_tokens": 54893,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 683,
          "cache_read_input_tokens": 54893,
          "cache_creation_input_tokens": 10241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10241
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

_source line 54 · 2026-05-25T19:50:12.211Z_

<details><summary>↩ Tool result · `toolu_01XxZwVXHhHYi8MpvYqkHT2V`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"172:    fig.savefig(out_path, bbox_inches=\\\"tight\\\")\\n173:    fig.savefig(out_path.with_suffix(\\\".png\\\"), bbox_inches=\\\"tight\\\", dpi=300)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bad6b848-2175-4a7d-a275-96f73b1a6f45",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "faf1895b-cc57-4f08-a128-892db034e213",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"172:    fig.savefig(out_path, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n173:    fig.savefig(out_path.with_suffix(\\\\\\\".png\\\\\\\"), bbox_inches=\\\\\\\"tight\\\\\\\", dpi=300)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"172:    fig.savefig(out_path, bbox_inches=\\\"tight\\\")\\n173:    fig.savefig(out_path.with_suffix(\\\".png\\\"), bbox_inches=\\\"tight\\\", dpi=300)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "bad6b848-2175-4a7d-a275-96f73b1a6f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-25T19:50:12.756Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01454hGyGPk6J35y7oQx8LyV`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"savefig\" /root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faf1895b-cc57-4f08-a128-892db034e213",
  "isSidechain": false,
  "requestId": "req_011CbPsHKrR66y7CuTdrmdTp",
  "type": "assistant",
  "uuid": "e5a22ccc-034c-4061-be7e-f9b5e79160f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D41U39bcSMKh1RuaG9252C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10241,
      "cache_read_input_tokens": 54893,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 683,
          "cache_read_input_tokens": 54893,
          "cache_creation_input_tokens": 10241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10241
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

_source line 56 · 2026-05-25T19:50:13.159Z_

<details><summary>↩ Tool result · `toolu_01454hGyGPk6J35y7oQx8LyV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"120:        fig.savefig(out_path, dpi=300, bbox_inches=\\\"tight\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5a22ccc-034c-4061-be7e-f9b5e79160f2",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "e9ef2b32-d5ba-4490-8196-638bcdb8a9c2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"120:        fig.savefig(out_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"120:        fig.savefig(out_path, dpi=300, bbox_inches=\\\"tight\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "e5a22ccc-034c-4061-be7e-f9b5e79160f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 57 · 2026-05-25T19:50:13.163Z_

```json
{
  "parentUuid": "e9ef2b32-d5ba-4490-8196-638bcdb8a9c2",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2cfb405b-128b-4650-88c6-879cf95c6e29",
  "timestamp": "2026-05-25T19:50:13.163Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 58 · 2026-05-25T19:50:16.252Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to look at data sources in each plotting script. Let me read the data-loading parts of each one.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cfb405b-128b-4650-88c6-879cf95c6e29",
  "isSidechain": false,
  "requestId": "req_011CbPsJBYNcgztzU4wXSmNq",
  "type": "assistant",
  "uuid": "e4c69b65-1989-4f67-a01b-3f0c9f0d4bf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhMBKoEnuXniiLTTwpqcEx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 65134,
      "output_tokens": 826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 826,
          "cache_read_input_tokens": 65134,
          "cache_creation_input_tokens": 1557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1557
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

_source line 59 · 2026-05-25T19:50:17.273Z_

Now let me trace data sources in each plotting script by reading key lines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4c69b65-1989-4f67-a01b-3f0c9f0d4bf7",
  "isSidechain": false,
  "requestId": "req_011CbPsJBYNcgztzU4wXSmNq",
  "type": "assistant",
  "uuid": "c0a2710a-25ca-410d-b28e-da467e492546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhMBKoEnuXniiLTTwpqcEx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 65134,
      "output_tokens": 826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 826,
          "cache_read_input_tokens": 65134,
          "cache_creation_input_tokens": 1557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1557
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

_source line 60 · 2026-05-25T19:50:19.108Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JedNN2KHWECAVSZi28oYon`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"read_csv\\|read_json\\|load\\|open\\|json\\|csv\\|data\\|results\\|auc\\|hardcod\" /root/autodl-tmp/gen-depth-contamination/scripts/plot_fig2_merged.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a2710a-25ca-410d-b28e-da467e492546",
  "isSidechain": false,
  "requestId": "req_011CbPsJBYNcgztzU4wXSmNq",
  "type": "assistant",
  "uuid": "19f570e1-d0b9-4526-9e74-980eb9ad7179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhMBKoEnuXniiLTTwpqcEx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 65134,
      "output_tokens": 826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 826,
          "cache_read_input_tokens": 65134,
          "cache_creation_input_tokens": 1557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1557
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

_source line 61 · 2026-05-25T19:50:19.121Z_

<details><summary>↩ Tool result · `toolu_01JedNN2KHWECAVSZi28oYon`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19f570e1-d0b9-4526-9e74-980eb9ad7179",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "920e9b76-80a5-4a73-aab6-293b22a08f00",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "19f570e1-d0b9-4526-9e74-980eb9ad7179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-25T19:50:20.610Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AFfDLu8sH1r8creezmxyGA`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"read_csv\\|read_json\\|load\\|open\\|json\\|csv\\|data\\|results\\|auc\\|hardcod\" /root/autodl-tmp/gen-depth-contamination/scripts/plot_fig_jsd_decay.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "920e9b76-80a5-4a73-aab6-293b22a08f00",
  "isSidechain": false,
  "requestId": "req_011CbPsJBYNcgztzU4wXSmNq",
  "type": "assistant",
  "uuid": "57d49671-ef93-470a-a371-7c1f7b3a592b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhMBKoEnuXniiLTTwpqcEx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 65134,
      "output_tokens": 826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 826,
          "cache_read_input_tokens": 65134,
          "cache_creation_input_tokens": 1557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1557
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

_source line 63 · 2026-05-25T19:50:24.274Z_

<details><summary>↩ Tool result · `toolu_01NXmJ4yvPjAuTrVpfD1nddt`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ae0efe7-714a-4eb5-b96f-416834752c70",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "dfa55791-b1f8-45a7-a5f7-490b61a60c1b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5ae0efe7-714a-4eb5-b96f-416834752c70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-25T19:50:20.623Z_

<details><summary>↩ Tool result · `toolu_01AFfDLu8sH1r8creezmxyGA`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57d49671-ef93-470a-a371-7c1f7b3a592b",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "f344b487-f3a0-4c33-82a7-55dc3a69a2b3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "57d49671-ef93-470a-a371-7c1f7b3a592b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-25T19:50:22.034Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0142WLL2oyhaty8CwhuCsk8P`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"read_csv\\|read_json\\|load\\|open\\|json\\|csv\\|data\\|results\\|auc\\|hardcod\" /root/autodl-tmp/gen-depth-contamination/scripts/plot_filtering_strategies.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f344b487-f3a0-4c33-82a7-55dc3a69a2b3",
  "isSidechain": false,
  "requestId": "req_011CbPsJBYNcgztzU4wXSmNq",
  "type": "assistant",
  "uuid": "4935f560-90a0-4680-819f-1303a077a7f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhMBKoEnuXniiLTTwpqcEx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 65134,
      "output_tokens": 826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 826,
          "cache_read_input_tokens": 65134,
          "cache_creation_input_tokens": 1557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1557
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

_source line 66 · 2026-05-25T19:50:22.047Z_

<details><summary>↩ Tool result · `toolu_0142WLL2oyhaty8CwhuCsk8P`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4935f560-90a0-4680-819f-1303a077a7f9",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "7c52c90d-a9c0-47ed-a097-961431d2c3d6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4935f560-90a0-4680-819f-1303a077a7f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 67 · 2026-05-25T19:50:23.877Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F1JUvp2xoRWQK1QEjAQ9qN`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"read_csv\\|read_json\\|load\\|open\\|json\\|csv\\|data\\|results\\|auc\\|hardcod\" /root/autodl-tmp/gen-depth-contamination/scripts/draw_kstar_theta.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c52c90d-a9c0-47ed-a097-961431d2c3d6",
  "isSidechain": false,
  "requestId": "req_011CbPsJBYNcgztzU4wXSmNq",
  "type": "assistant",
  "uuid": "8db59dde-a642-47a4-9920-8391cfa27d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhMBKoEnuXniiLTTwpqcEx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 65134,
      "output_tokens": 826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 826,
          "cache_read_input_tokens": 65134,
          "cache_creation_input_tokens": 1557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1557
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

_source line 68 · 2026-05-25T19:50:23.889Z_

<details><summary>↩ Tool result · `toolu_01F1JUvp2xoRWQK1QEjAQ9qN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8db59dde-a642-47a4-9920-8391cfa27d7c",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "10fa9726-e896-4a0a-81d1-fb78339993b5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "8db59dde-a642-47a4-9920-8391cfa27d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-25T19:50:24.266Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NXmJ4yvPjAuTrVpfD1nddt`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"read_csv\\|read_json\\|load\\|open\\|json\\|csv\\|data\\|results\\|auc\\|hardcod\" /root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10fa9726-e896-4a0a-81d1-fb78339993b5",
  "isSidechain": false,
  "requestId": "req_011CbPsJBYNcgztzU4wXSmNq",
  "type": "assistant",
  "uuid": "5ae0efe7-714a-4eb5-b96f-416834752c70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhMBKoEnuXniiLTTwpqcEx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 65134,
      "output_tokens": 826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 826,
          "cache_read_input_tokens": 65134,
          "cache_creation_input_tokens": 1557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1557
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

_source line 70_

```json
{
  "type": "last-prompt",
  "leafUuid": "dfa55791-b1f8-45a7-a5f7-490b61a60c1b",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit appendix and figure data sources",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Assistant

_source line 72 · 2026-05-25T19:50:26.963Z_

<details><summary>Logged reasoning block</summary>

```text
The pipe character in the grep patterns is being blocked. Let me use `-e` flags instead of `|`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfa55791-b1f8-45a7-a5f7-490b61a60c1b",
  "isSidechain": false,
  "requestId": "req_011CbPsK1n2V3xzvVhD8xFkA",
  "type": "assistant",
  "uuid": "66c31559-213b-4e02-811e-64274b975ade",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kaXT38BK3HTZFXbSmJvme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 66691,
      "output_tokens": 629,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 629,
          "cache_read_input_tokens": 66691,
          "cache_creation_input_tokens": 1424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1424
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

_source line 73 · 2026-05-25T19:50:27.991Z_

Need to avoid pipe chars in patterns. Let me read the scripts directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66c31559-213b-4e02-811e-64274b975ade",
  "isSidechain": false,
  "requestId": "req_011CbPsK1n2V3xzvVhD8xFkA",
  "type": "assistant",
  "uuid": "633ae2ac-ab0d-4655-8c59-30b1ca0bdfec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kaXT38BK3HTZFXbSmJvme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 66691,
      "output_tokens": 629,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 629,
          "cache_read_input_tokens": 66691,
          "cache_creation_input_tokens": 1424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1424
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

_source line 74 · 2026-05-25T19:50:28.925Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016p3BsqcR5aSmSoVRm7J8Jd`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/plot_fig2_merged.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "633ae2ac-ab0d-4655-8c59-30b1ca0bdfec",
  "isSidechain": false,
  "requestId": "req_011CbPsK1n2V3xzvVhD8xFkA",
  "type": "assistant",
  "uuid": "0f24a810-4455-449b-bab9-4be624325699",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kaXT38BK3HTZFXbSmJvme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 66691,
      "output_tokens": 629,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 629,
          "cache_read_input_tokens": 66691,
          "cache_creation_input_tokens": 1424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1424
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

_source line 75 · 2026-05-25T19:50:29.327Z_

<details><summary>↩ Tool result · `toolu_016p3BsqcR5aSmSoVRm7J8Jd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Merged Figure 2: AUC decay curves with CI shaded bands.\\n\\nCombines the main AUC decay figure and the supplementary CI figure\\ninto a single plot for the main text.\\n\\\"\\\"\\\"\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nPAIR_KEYS = [\\\"0v1\\\", \\\"1v2\\\", \\\"2v3\\\", \\\"3v4\\\", \\\"4v5\\\"]\\nX_LABELS = [\\\"0 vs 1\\\", \\\"1 vs 2\\\", \\\"2 vs 3\\\", \\\"3 vs 4\\\", \\\"4 vs 5\\\"]\\n\\n# ── Curated data: Table 1 models (C4, 5-fold CV) ────────────────────────────\\n# CI: exact where available from bootstrap; estimated (±0.010 / ±0.002 for 0v1)\\n# at non-boundary pairs, consistent with observed bootstrap CI widths.\\nTABLE1 = {\\n    \\\"Qwen-rw\\\": {\\n        \\\"mean\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\n        \\\"ci_lower\\\": [0.9936, 0.686,  0.580,  0.534,  0.524],\\n        \\\"ci_upper\\\": [0.9976, 0.704,  0.599,  0.553,  0.544],\\n    },\\n    \\\"Pythia\\\": {\\n        \\\"mean\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\n        \\\"ci_lower\\\": [0.9912, 0.645,  0.542,  0.505,  0.504],\\n        \\\"ci_upper\\\": [0.9952, 0.663,  0.563,  0.525,  0.524],\\n    },\\n    \\\"OLMo\\\": {\\n        \\\"mean\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\n        \\\"ci_lower\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\n        \\\"ci_upper\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\n    },\\n    \\\"Qwen-cont\\\": {\\n        \\\"mean\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\n        \\\"ci_lower\\\": [0.9951, 0.602,  0.551,  0.531,  0.504],\\n        \\\"ci_upper\\\": [0.9991, 0.621,  0.571,  0.551,  0.524],\\n    },\\n    r\\\"Qwen-7B$^\\\\ddagger$\\\": {\\n        \\\"mean\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\n        \\\"ci_lower\\\": [0.961,  0.608,  0.539,  0.518,  0.499],\\n        \\\"ci_upper\\\": [0.967,  0.626,  0.559,  0.537,  0.518],\\n    },\\n}\\n\\n# ── Additional models with bootstrap CI (all pairs) ─────────────────────────\\nEXTRA_MODELS = {\\n    \\\"LLaMA-8B\\\": {\\n        \\\"mean\\\":     [0.9225, 0.6123, 0.5274, 0.5169, 0.5162],\\n        \\\"ci_lower\\\": [0.9174, 0.6028, 0.5169, 0.5062, 0.5052],\\n        \\\"ci_upper\\\": [0.9272, 0.6216, 0.5378, 0.5275, 0.5268],\\n    },\\n    \\\"Mistral-7B\\\": {\\n        \\\"mean\\\":     [0.9843, 0.5935, 0.5402, 0.5232, 0.5181],\\n        \\\"ci_lower\\\": [0.9824, 0.5835, 0.5301, 0.5128, 0.5070],\\n        \\\"ci_upper\\\": [0.9860, 0.6032, 0.5510, 0.5338, 0.5287],\\n    },\\n}\\n\\n# ── Decoding strategies (per_fold → approximate CI) ─────────────────────────\\nDECODE_FOLD = {\\n    \\\"Greedy\\\": {\\n        \\\"mean\\\": [0.9992, 0.8838, 0.5342, 0.5228, 0.5162],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9996, 0.9991, 0.9992, 0.9996, 0.9984],\\n            \\\"1v2\\\": [0.8906, 0.8766, 0.8847, 0.881, 0.8861],\\n            \\\"2v3\\\": [0.5188, 0.542, 0.5264, 0.5364, 0.5473],\\n            \\\"3v4\\\": [0.5223, 0.5135, 0.5187, 0.5355, 0.5239],\\n            \\\"4v5\\\": [0.5272, 0.5108, 0.5124, 0.5128, 0.5177],\\n        },\\n    },\\n    r\\\"Nuc $p{=}0.9$\\\": {\\n        \\\"mean\\\": [0.9948, 0.677, 0.5549, 0.5299, 0.5013],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9957, 0.9951, 0.9939, 0.9942, 0.9952],\\n            \\\"1v2\\\": [0.6875, 0.6745, 0.6838, 0.6631, 0.6763],\\n            \\\"2v3\\\": [0.548, 0.5563, 0.5534, 0.5638, 0.5531],\\n            \\\"3v4\\\": [0.525, 0.5494, 0.5317, 0.5301, 0.5133],\\n            \\\"4v5\\\": [0.5257, 0.4903, 0.4898, 0.5, 0.5008],\\n        },\\n    },\\n    r\\\"$T{=}0.7$\\\": {\\n        \\\"mean\\\": [0.9965, 0.7265, 0.5941, 0.5698, 0.5284],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9977, 0.9972, 0.9956, 0.9972, 0.995],\\n            \\\"1v2\\\": [0.7367, 0.7367, 0.7255, 0.7121, 0.7214],\\n            \\\"2v3\\\": [0.6009, 0.5951, 0.5954, 0.5754, 0.6036],\\n            \\\"3v4\\\": [0.5521, 0.5739, 0.5801, 0.5784, 0.5643],\\n            \\\"4v5\\\": [0.5209, 0.529, 0.5222, 0.5358, 0.5343],\\n        },\\n    },\\n    r\\\"$T{=}1.2$\\\": {\\n        \\\"mean\\\": [0.9933, 0.6172, 0.5226, 0.517, 0.5051],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9938, 0.9949, 0.9929, 0.9922, 0.9929],\\n            \\\"1v2\\\": [0.6193, 0.5961, 0.6182, 0.6258, 0.6265],\\n            \\\"2v3\\\": [0.5285, 0.5246, 0.5219, 0.5254, 0.5123],\\n            \\\"3v4\\\": [0.5464, 0.5142, 0.4998, 0.5028, 0.5218],\\n            \\\"4v5\\\": [0.5048, 0.5059, 0.5053, 0.4936, 0.5162],\\n        },\\n    },\\n}\\n\\nTABLEAU = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\", \\\"#b07aa1\\\",\\n    \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#edc948\\\", \\\"#f28e2b\\\", \\\"#bab0ac\\\",\\n    \\\"#86bcb6\\\",\\n]\\nMARKERS = [\\\"o\\\", \\\"s\\\", \\\"^\\\", \\\"D\\\", \\\"v\\\", \\\"P\\\", \\\"X\\\", \\\"*\\\", \\\"h\\\", \\\"<\\\", \\\">\\\"]\\n\\n\\ndef fold_ci(folds):\\n    arr = np.array(folds)\\n    m = arr.mean()\\n    se = arr.std(ddof=1) / np.sqrt(len(arr))\\n    return m - 1.96 * se, m + 1.96 * se\\n\\n\\ndef main():\\n    x = np.arange(len(PAIR_KEYS))\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, ax = plt.subplots(figsize=(7, 4.2), constrained_layout=True)\\n\\n    # Reference lines\\n    ax.axhline(0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.608, r\\\"$\\\\theta = 0.60$\\\",\\n            fontsize=8, color=\\\"grey\\\", va=\\\"bottom\\\", ha=\\\"right\\\")\\n    ax.axhline(0.50, color=\\\"lightgrey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.507, \\\"chance\\\",\\n            fontsize=8, color=\\\"silver\\\", va=\\\"bottom\\\", ha=\\\"right\\\")\\n\\n    ci = 0\\n    model_handles = []\\n    decode_handles = []\\n\\n    # ── Model configs (solid + CI bands) ─────────────────────────────────\\n    all_models = {}\\n    all_models.update(TABLE1)\\n    all_models.update(EXTRA_MODELS)\\n\\n    for label, data in all_models.items():\\n        color = TABLEAU[ci % len(TABLEAU)]\\n        marker = MARKERS[ci % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n        lo = data[\\\"ci_lower\\\"]\\n        hi = data[\\\"ci_upper\\\"]\\n\\n        ax.fill_between(x, lo, hi, color=color, alpha=0.18, zorder=2,\\n                         linewidth=0)\\n        line, = ax.plot(x, means, \\\"-\\\", color=color, lw=1.6, marker=marker,\\n                        markersize=4.5, label=label, zorder=3)\\n        model_handles.append(line)\\n        ci += 1\\n\\n    # ── Decoding strategies (dashed, no CI bands) ────────────────────────\\n    for label, data in DECODE_FOLD.items():\\n        color = TABLEAU[ci % len(TABLEAU)]\\n        marker = MARKERS[ci % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n\\n        line, = ax.plot(x, means, \\\"--\\\", color=color, lw=1.4, marker=marker,\\n                        markersize=4, label=label, zorder=3)\\n        decode_handles.append(line)\\n        ci += 1\\n\\n    # ── Axes ─────────────────────────────────────────────────────────────\\n    ax.set_xticks(x)\\n    ax.set_xticklabels(X_LABELS)\\n    ax.set_xlabel(\\\"Depth Pair\\\", fontsize=10.5)\\n    ax.set_ylabel(\\\"Pairwise AUC\\\", fontsize=10.5)\\n    ax.set_ylim(0.45, 1.05)\\n    ax.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\n    ax.tick_params(direction=\\\"in\\\")\\n\\n    # ── Legends ──────────────────────────────────────────────────────────\\n    leg1 = ax.legend(handles=model_handles, title=\\\"Models\\\", title_fontsize=8.5,\\n                     fontsize=7.5, loc=\\\"upper right\\\", bbox_to_anchor=(1.0, 0.98),\\n                     framealpha=0.92, edgecolor=\\\"0.85\\\", handlelength=2.0)\\n    ax.add_artist(leg1)\\n    if decode_handles:\\n        ax.legend(handles=decode_handles, title=\\\"Decoding\\\", title_fontsize=8.5,\\n                  fontsize=7.5, loc=\\\"center right\\\", bbox_to_anchor=(1.0, 0.42),\\n                  framealpha=0.92, edgecolor=\\\"0.85\\\", handlelength=2.0)\\n\\n    # ── Save ─────────────────────────────────────────────────────────────\\n    out_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n\\n    pdf_path = out_dir / \\\"fig2_auc_decay.pdf\\\"\\n    png_path = out_dir / \\\"fig2_auc_decay.png\\\"\\n    fig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    plt.close(fig)\\n\\n    print(f\\\"PDF: {pdf_path} ({pdf_path.stat().st_size/1024:.1f} KB)\\\")\\n    print(f\\\"PNG: {png_path} ({png_path.stat().st_size/1024:.1f} KB)\\\")\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f24a810-4455-449b-bab9-4be624325699",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "98caf926-118d-4e3c-bc27-1cd33971e011",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Merged Figure 2: AUC decay curves with CI shaded bands.\\\\n\\\\nCombines the main AUC decay figure and the supplementary CI figure\\\\ninto a single plot for the main text.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\nPAIR_KEYS = [\\\\\\\"0v1\\\\\\\", \\\\\\\"1v2\\\\\\\", \\\\\\\"2v3\\\\\\\", \\\\\\\"3v4\\\\\\\", \\\\\\\"4v5\\\\\\\"]\\\\nX_LABELS = [\\\\\\\"0 vs 1\\\\\\\", \\\\\\\"1 vs 2\\\\\\\", \\\\\\\"2 vs 3\\\\\\\", \\\\\\\"3 vs 4\\\\\\\", \\\\\\\"4 vs 5\\\\\\\"]\\\\n\\\\n# ── Curated data: Table 1 models (C4, 5-fold CV) ────────────────────────────\\\\n# CI: exact where available from bootstrap; estimated (±0.010 / ±0.002 for 0v1)\\\\n# at non-boundary pairs, consistent with observed bootstrap CI widths.\\\\nTABLE1 = {\\\\n    \\\\\\\"Qwen-rw\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9936, 0.686,  0.580,  0.534,  0.524],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9976, 0.704,  0.599,  0.553,  0.544],\\\\n    },\\\\n    \\\\\\\"Pythia\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9912, 0.645,  0.542,  0.505,  0.504],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9952, 0.663,  0.563,  0.525,  0.524],\\\\n    },\\\\n    \\\\\\\"OLMo\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\\\n    },\\\\n    \\\\\\\"Qwen-cont\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9951, 0.602,  0.551,  0.531,  0.504],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9991, 0.621,  0.571,  0.551,  0.524],\\\\n    },\\\\n    r\\\\\\\"Qwen-7B$^\\\\\\\\ddagger$\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.961,  0.608,  0.539,  0.518,  0.499],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.967,  0.626,  0.559,  0.537,  0.518],\\\\n    },\\\\n}\\\\n\\\\n# ── Additional models with bootstrap CI (all pairs) ─────────────────────────\\\\nEXTRA_MODELS = {\\\\n    \\\\\\\"LLaMA-8B\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9225, 0.6123, 0.5274, 0.5169, 0.5162],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9174, 0.6028, 0.5169, 0.5062, 0.5052],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9272, 0.6216, 0.5378, 0.5275, 0.5268],\\\\n    },\\\\n    \\\\\\\"Mistral-7B\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9843, 0.5935, 0.5402, 0.5232, 0.5181],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9824, 0.5835, 0.5301, 0.5128, 0.5070],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9860, 0.6032, 0.5510, 0.5338, 0.5287],\\\\n    },\\\\n}\\\\n\\\\n# ── Decoding strategies (per_fold → approximate CI) ─────────────────────────\\\\nDECODE_FOLD = {\\\\n    \\\\\\\"Greedy\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": [0.9992, 0.8838, 0.5342, 0.5228, 0.5162],\\\\n        \\\\\\\"folds\\\\\\\": {\\\\n            \\\\\\\"0v1\\\\\\\": [0.9996, 0.9991, 0.9992, 0.9996, 0.9984],\\\\n            \\\\\\\"1v2\\\\\\\": [0.8906, 0.8766, 0.8847, 0.881, 0.8861],\\\\n            \\\\\\\"2v3\\\\\\\": [0.5188, 0.542, 0.5264, 0.5364, 0.5473],\\\\n            \\\\\\\"3v4\\\\\\\": [0.5223, 0.5135, 0.5187, 0.5355, 0.5239],\\\\n            \\\\\\\"4v5\\\\\\\": [0.5272, 0.5108, 0.5124, 0.5128, 0.5177],\\\\n        },\\\\n    },\\\\n    r\\\\\\\"Nuc $p{=}0.9$\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": [0.9948, 0.677, 0.5549, 0.5299, 0.5013],\\\\n        \\\\\\\"folds\\\\\\\": {\\\\n            \\\\\\\"0v1\\\\\\\": [0.9957, 0.9951, 0.9939, 0.9942, 0.9952],\\\\n            \\\\\\\"1v2\\\\\\\": [0.6875, 0.6745, 0.6838, 0.6631, 0.6763],\\\\n            \\\\\\\"2v3\\\\\\\": [0.548, 0.5563, 0.5534, 0.5638, 0.5531],\\\\n            \\\\\\\"3v4\\\\\\\": [0.525, 0.5494, 0.5317, 0.5301, 0.5133],\\\\n            \\\\\\\"4v5\\\\\\\": [0.5257, 0.4903, 0.4898, 0.5, 0.5008],\\\\n        },\\\\n    },\\\\n    r\\\\\\\"$T{=}0.7$\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": [0.9965, 0.7265, 0.5941, 0.5698, 0.5284],\\\\n        \\\\\\\"folds\\\\\\\": {\\\\n            \\\\\\\"0v1\\\\\\\": [0.9977, 0.9972, 0.9956, 0.9972, 0.995],\\\\n            \\\\\\\"1v2\\\\\\\": [0.7367, 0.7367, 0.7255, 0.7121, 0.7214],\\\\n            \\\\\\\"2v3\\\\\\\": [0.6009, 0.5951, 0.5954, 0.5754, 0.6036],\\\\n            \\\\\\\"3v4\\\\\\\": [0.5521, 0.5739, 0.5801, 0.5784, 0.5643],\\\\n            \\\\\\\"4v5\\\\\\\": [0.5209, 0.529, 0.5222, 0.5358, 0.5343],\\\\n        },\\\\n    },\\\\n    r\\\\\\\"$T{=}1.2$\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": [0.9933, 0.6172, 0.5226, 0.517, 0.5051],\\\\n        \\\\\\\"folds\\\\\\\": {\\\\n            \\\\\\\"0v1\\\\\\\": [0.9938, 0.9949, 0.9929, 0.9922, 0.9929],\\\\n            \\\\\\\"1v2\\\\\\\": [0.6193, 0.5961, 0.6182, 0.6258, 0.6265],\\\\n            \\\\\\\"2v3\\\\\\\": [0.5285, 0.5246, 0.5219, 0.5254, 0.5123],\\\\n            \\\\\\\"3v4\\\\\\\": [0.5464, 0.5142, 0.4998, 0.5028, 0.5218],\\\\n            \\\\\\\"4v5\\\\\\\": [0.5048, 0.5059, 0.5053, 0.4936, 0.5162],\\\\n        },\\\\n    },\\\\n}\\\\n\\\\nTABLEAU = [\\\\n    \\\\\\\"#4e79a7\\\\\\\", \\\\\\\"#e15759\\\\\\\", \\\\\\\"#76b7b2\\\\\\\", \\\\\\\"#59a14f\\\\\\\", \\\\\\\"#b07aa1\\\\\\\",\\\\n    \\\\\\\"#ff9da7\\\\\\\", \\\\\\\"#9c755f\\\\\\\", \\\\\\\"#edc948\\\\\\\", \\\\\\\"#f28e2b\\\\\\\", \\\\\\\"#bab0ac\\\\\\\",\\\\n    \\\\\\\"#86bcb6\\\\\\\",\\\\n]\\\\nMARKERS = [\\\\\\\"o\\\\\\\", \\\\\\\"s\\\\\\\", \\\\\\\"^\\\\\\\", \\\\\\\"D\\\\\\\", \\\\\\\"v\\\\\\\", \\\\\\\"P\\\\\\\", \\\\\\\"X\\\\\\\", \\\\\\\"*\\\\\\\", \\\\\\\"h\\\\\\\", \\\\\\\"<\\\\\\\", \\\\\\\">\\\\\\\"]\\\\n\\\\n\\\\ndef fold_ci(folds):\\\\n    arr = np.array(folds)\\\\n    m = arr.mean()\\\\n    se = arr.std(ddof=1) / np.sqrt(len(arr))\\\\n    return m - 1.96 * se, m + 1.96 * se\\\\n\\\\n\\\\ndef main():\\\\n    x = np.arange(len(PAIR_KEYS))\\\\n\\\\n    plt.rcParams.update({\\\\n        \\\\\\\"font.family\\\\\\\": \\\\\\\"serif\\\\\\\",\\\\n        \\\\\\\"font.size\\\\\\\": 10,\\\\n        \\\\\\\"axes.linewidth\\\\\\\": 0.8,\\\\n        \\\\\\\"xtick.major.width\\\\\\\": 0.8,\\\\n        \\\\\\\"ytick.major.width\\\\\\\": 0.8,\\\\n    })\\\\n\\\\n    fig, ax = plt.subplots(figsize=(7, 4.2), constrained_layout=True)\\\\n\\\\n    # Reference lines\\\\n    ax.axhline(0.60, color=\\\\\\\"grey\\\\\\\", ls=\\\\\\\"--\\\\\\\", lw=0.8, zorder=1)\\\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.608, r\\\\\\\"$\\\\\\\\theta = 0.60$\\\\\\\",\\\\n            fontsize=8, color=\\\\\\\"grey\\\\\\\", va=\\\\\\\"bottom\\\\\\\", ha=\\\\\\\"right\\\\\\\")\\\\n    ax.axhline(0.50, color=\\\\\\\"lightgrey\\\\\\\", ls=\\\\\\\"--\\\\\\\", lw=0.8, zorder=1)\\\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.507, \\\\\\\"chance\\\\\\\",\\\\n            fontsize=8, color=\\\\\\\"silver\\\\\\\", va=\\\\\\\"bottom\\\\\\\", ha=\\\\\\\"right\\\\\\\")\\\\n\\\\n    ci = 0\\\\n    model_handles = []\\\\n    decode_handles = []\\\\n\\\\n    # ── Model configs (solid + CI bands) ─────────────────────────────────\\\\n    all_models = {}\\\\n    all_models.update(TABLE1)\\\\n    all_models.update(EXTRA_MODELS)\\\\n\\\\n    for label, data in all_models.items():\\\\n        color = TABLEAU[ci % len(TABLEAU)]\\\\n        marker = MARKERS[ci % len(MARKERS)]\\\\n        means = data[\\\\\\\"mean\\\\\\\"]\\\\n        lo = data[\\\\\\\"ci_lower\\\\\\\"]\\\\n        hi = data[\\\\\\\"ci_upper\\\\\\\"]\\\\n\\\\n        ax.fill_between(x, lo, hi, color=color, alpha=0.18, zorder=2,\\\\n                         linewidth=0)\\\\n        line, = ax.plot(x, means, \\\\\\\"-\\\\\\\", color=color, lw=1.6, marker=marker,\\\\n                        markersize=4.5, label=label, zorder=3)\\\\n        model_handles.append(line)\\\\n        ci += 1\\\\n\\\\n    # ── Decoding strategies (dashed, no CI bands) ────────────────────────\\\\n    for label, data in DECODE_FOLD.items():\\\\n        color = TABLEAU[ci % len(TABLEAU)]\\\\n        marker = MARKERS[ci % len(MARKERS)]\\\\n        means = data[\\\\\\\"mean\\\\\\\"]\\\\n\\\\n        line, = ax.plot(x, means, \\\\\\\"--\\\\\\\", color=color, lw=1.4, marker=marker,\\\\n                        markersize=4, label=label, zorder=3)\\\\n        decode_handles.append(line)\\\\n        ci += 1\\\\n\\\\n    # ── Axes ─────────────────────────────────────────────────────────────\\\\n    ax.set_xticks(x)\\\\n    ax.set_xticklabels(X_LABELS)\\\\n    ax.set_xlabel(\\\\\\\"Depth Pair\\\\\\\", fontsize=10.5)\\\\n    ax.set_ylabel(\\\\\\\"Pairwise AUC\\\\\\\", fontsize=10.5)\\\\n    ax.set_ylim(0.45, 1.05)\\\\n    ax.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\\\n    ax.tick_params(direction=\\\\\\\"in\\\\\\\")\\\\n\\\\n    # ── Legends ──────────────────────────────────────────────────────────\\\\n    leg1 = ax.legend(handles=model_handles, title=\\\\\\\"Models\\\\\\\", title_fontsize=8.5,\\\\n                     fontsize=7.5, loc=\\\\\\\"upper right\\\\\\\", bbox_to_anchor=(1.0, 0.98),\\\\n                     framealpha=0.92, edgecolor=\\\\\\\"0.85\\\\\\\", handlelength=2.0)\\\\n    ax.add_artist(leg1)\\\\n    if decode_handles:\\\\n        ax.legend(handles=decode_handles, title=\\\\\\\"Decoding\\\\\\\", title_fontsize=8.5,\\\\n                  fontsize=7.5, loc=\\\\\\\"center right\\\\\\\", bbox_to_anchor=(1.0, 0.42),\\\\n                  framealpha=0.92, edgecolor=\\\\\\\"0.85\\\\\\\", handlelength=2.0)\\\\n\\\\n    # ── Save ─────────────────────────────────────────────────────────────\\\\n    out_dir = Path(__file__).resolve().parent.parent / \\\\\\\"docs\\\\\\\" / \\\\\\\"paper\\\\\\\" / \\\\\\\"figures\\\\\\\"\\\\n    out_dir.mkdir(parents=True, exist_ok=True)\\\\n\\\\n    pdf_path = out_dir / \\\\\\\"fig2_auc_decay.pdf\\\\\\\"\\\\n    png_path = out_dir / \\\\\\\"fig2_auc_decay.png\\\\\\\"\\\\n    fig.savefig(pdf_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    fig.savefig(png_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close(fig)\\\\n\\\\n    print(f\\\\\\\"PDF: {pdf_path} ({pdf_path.stat().st_size/1024:.1f} KB)\\\\\\\")\\\\n    print(f\\\\\\\"PNG: {png_path} ({png_path.stat().st_size/1024:.1f} KB)\\\\\\\")\\\\n    print(\\\\\\\"OK\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Merged Figure 2: AUC decay curves with CI shaded bands.\\n\\nCombines the main AUC decay figure and the supplementary CI figure\\ninto a single plot for the main text.\\n\\\"\\\"\\\"\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nPAIR_KEYS = [\\\"0v1\\\", \\\"1v2\\\", \\\"2v3\\\", \\\"3v4\\\", \\\"4v5\\\"]\\nX_LABELS = [\\\"0 vs 1\\\", \\\"1 vs 2\\\", \\\"2 vs 3\\\", \\\"3 vs 4\\\", \\\"4 vs 5\\\"]\\n\\n# ── Curated data: Table 1 models (C4, 5-fold CV) ────────────────────────────\\n# CI: exact where available from bootstrap; estimated (±0.010 / ±0.002 for 0v1)\\n# at non-boundary pairs, consistent with observed bootstrap CI widths.\\nTABLE1 = {\\n    \\\"Qwen-rw\\\": {\\n        \\\"mean\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\n        \\\"ci_lower\\\": [0.9936, 0.686,  0.580,  0.534,  0.524],\\n        \\\"ci_upper\\\": [0.9976, 0.704,  0.599,  0.553,  0.544],\\n    },\\n    \\\"Pythia\\\": {\\n        \\\"mean\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\n        \\\"ci_lower\\\": [0.9912, 0.645,  0.542,  0.505,  0.504],\\n        \\\"ci_upper\\\": [0.9952, 0.663,  0.563,  0.525,  0.524],\\n    },\\n    \\\"OLMo\\\": {\\n        \\\"mean\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\n        \\\"ci_lower\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\n        \\\"ci_upper\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\n    },\\n    \\\"Qwen-cont\\\": {\\n        \\\"mean\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\n        \\\"ci_lower\\\": [0.9951, 0.602,  0.551,  0.531,  0.504],\\n        \\\"ci_upper\\\": [0.9991, 0.621,  0.571,  0.551,  0.524],\\n    },\\n    r\\\"Qwen-7B$^\\\\ddagger$\\\": {\\n        \\\"mean\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\n        \\\"ci_lower\\\": [0.961,  0.608,  0.539,  0.518,  0.499],\\n        \\\"ci_upper\\\": [0.967,  0.626,  0.559,  0.537,  0.518],\\n    },\\n}\\n\\n# ── Additional models with bootstrap CI (all pairs) ─────────────────────────\\nEXTRA_MODELS = {\\n    \\\"LLaMA-8B\\\": {\\n        \\\"mean\\\":     [0.9225, 0.6123, 0.5274, 0.5169, 0.5162],\\n        \\\"ci_lower\\\": [0.9174, 0.6028, 0.5169, 0.5062, 0.5052],\\n        \\\"ci_upper\\\": [0.9272, 0.6216, 0.5378, 0.5275, 0.5268],\\n    },\\n    \\\"Mistral-7B\\\": {\\n        \\\"mean\\\":     [0.9843, 0.5935, 0.5402, 0.5232, 0.5181],\\n        \\\"ci_lower\\\": [0.9824, 0.5835, 0.5301, 0.5128, 0.5070],\\n        \\\"ci_upper\\\": [0.9860, 0.6032, 0.5510, 0.5338, 0.5287],\\n    },\\n}\\n\\n# ── Decoding strategies (per_fold → approximate CI) ─────────────────────────\\nDECODE_FOLD = {\\n    \\\"Greedy\\\": {\\n        \\\"mean\\\": [0.9992, 0.8838, 0.5342, 0.5228, 0.5162],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9996, 0.9991, 0.9992, 0.9996, 0.9984],\\n            \\\"1v2\\\": [0.8906, 0.8766, 0.8847, 0.881, 0.8861],\\n            \\\"2v3\\\": [0.5188, 0.542, 0.5264, 0.5364, 0.5473],\\n            \\\"3v4\\\": [0.5223, 0.5135, 0.5187, 0.5355, 0.5239],\\n            \\\"4v5\\\": [0.5272, 0.5108, 0.5124, 0.5128, 0.5177],\\n        },\\n    },\\n    r\\\"Nuc $p{=}0.9$\\\": {\\n        \\\"mean\\\": [0.9948, 0.677, 0.5549, 0.5299, 0.5013],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9957, 0.9951, 0.9939, 0.9942, 0.9952],\\n            \\\"1v2\\\": [0.6875, 0.6745, 0.6838, 0.6631, 0.6763],\\n            \\\"2v3\\\": [0.548, 0.5563, 0.5534, 0.5638, 0.5531],\\n            \\\"3v4\\\": [0.525, 0.5494, 0.5317, 0.5301, 0.5133],\\n            \\\"4v5\\\": [0.5257, 0.4903, 0.4898, 0.5, 0.5008],\\n        },\\n    },\\n    r\\\"$T{=}0.7$\\\": {\\n        \\\"mean\\\": [0.9965, 0.7265, 0.5941, 0.5698, 0.5284],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9977, 0.9972, 0.9956, 0.9972, 0.995],\\n            \\\"1v2\\\": [0.7367, 0.7367, 0.7255, 0.7121, 0.7214],\\n            \\\"2v3\\\": [0.6009, 0.5951, 0.5954, 0.5754, 0.6036],\\n            \\\"3v4\\\": [0.5521, 0.5739, 0.5801, 0.5784, 0.5643],\\n            \\\"4v5\\\": [0.5209, 0.529, 0.5222, 0.5358, 0.5343],\\n        },\\n    },\\n    r\\\"$T{=}1.2$\\\": {\\n        \\\"mean\\\": [0.9933, 0.6172, 0.5226, 0.517, 0.5051],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9938, 0.9949, 0.9929, 0.9922, 0.9929],\\n            \\\"1v2\\\": [0.6193, 0.5961, 0.6182, 0.6258, 0.6265],\\n            \\\"2v3\\\": [0.5285, 0.5246, 0.5219, 0.5254, 0.5123],\\n            \\\"3v4\\\": [0.5464, 0.5142, 0.4998, 0.5028, 0.5218],\\n            \\\"4v5\\\": [0.5048, 0.5059, 0.5053, 0.4936, 0.5162],\\n        },\\n    },\\n}\\n\\nTABLEAU = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\", \\\"#b07aa1\\\",\\n    \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#edc948\\\", \\\"#f28e2b\\\", \\\"#bab0ac\\\",\\n    \\\"#86bcb6\\\",\\n]\\nMARKERS = [\\\"o\\\", \\\"s\\\", \\\"^\\\", \\\"D\\\", \\\"v\\\", \\\"P\\\", \\\"X\\\", \\\"*\\\", \\\"h\\\", \\\"<\\\", \\\">\\\"]\\n\\n\\ndef fold_ci(folds):\\n    arr = np.array(folds)\\n    m = arr.mean()\\n    se = arr.std(ddof=1) / np.sqrt(len(arr))\\n    return m - 1.96 * se, m + 1.96 * se\\n\\n\\ndef main():\\n    x = np.arange(len(PAIR_KEYS))\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, ax = plt.subplots(figsize=(7, 4.2), constrained_layout=True)\\n\\n    # Reference lines\\n    ax.axhline(0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.608, r\\\"$\\\\theta = 0.60$\\\",\\n            fontsize=8, color=\\\"grey\\\", va=\\\"bottom\\\", ha=\\\"right\\\")\\n    ax.axhline(0.50, color=\\\"lightgrey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.507, \\\"chance\\\",\\n            fontsize=8, color=\\\"silver\\\", va=\\\"bottom\\\", ha=\\\"right\\\")\\n\\n    ci = 0\\n    model_handles = []\\n    decode_handles = []\\n\\n    # ── Model configs (solid + CI bands) ─────────────────────────────────\\n    all_models = {}\\n    all_models.update(TABLE1)\\n    all_models.update(EXTRA_MODELS)\\n\\n    for label, data in all_models.items():\\n        color = TABLEAU[ci % len(TABLEAU)]\\n        marker = MARKERS[ci % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n        lo = data[\\\"ci_lower\\\"]\\n        hi = data[\\\"ci_upper\\\"]\\n\\n        ax.fill_between(x, lo, hi, color=color, alpha=0.18, zorder=2,\\n                         linewidth=0)\\n        line, = ax.plot(x, means, \\\"-\\\", color=color, lw=1.6, marker=marker,\\n                        markersize=4.5, label=label, zorder=3)\\n        model_handles.append(line)\\n        ci += 1\\n\\n    # ── Decoding strategies (dashed, no CI bands) ────────────────────────\\n    for label, data in DECODE_FOLD.items():\\n        color = TABLEAU[ci % len(TABLEAU)]\\n        marker = MARKERS[ci % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n\\n        line, = ax.plot(x, means, \\\"--\\\", color=color, lw=1.4, marker=marker,\\n                        markersize=4, label=label, zorder=3)\\n        decode_handles.append(line)\\n        ci += 1\\n\\n    # ── Axes ─────────────────────────────────────────────────────────────\\n    ax.set_xticks(x)\\n    ax.set_xticklabels(X_LABELS)\\n    ax.set_xlabel(\\\"Depth Pair\\\", fontsize=10.5)\\n    ax.set_ylabel(\\\"Pairwise AUC\\\", fontsize=10.5)\\n    ax.set_ylim(0.45, 1.05)\\n    ax.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\n    ax.tick_params(direction=\\\"in\\\")\\n\\n    # ── Legends ──────────────────────────────────────────────────────────\\n    leg1 = ax.legend(handles=model_handles, title=\\\"Models\\\", title_fontsize=8.5,\\n                     fontsize=7.5, loc=\\\"upper right\\\", bbox_to_anchor=(1.0, 0.98),\\n                     framealpha=0.92, edgecolor=\\\"0.85\\\", handlelength=2.0)\\n    ax.add_artist(leg1)\\n    if decode_handles:\\n        ax.legend(handles=decode_handles, title=\\\"Decoding\\\", title_fontsize=8.5,\\n                  fontsize=7.5, loc=\\\"center right\\\", bbox_to_anchor=(1.0, 0.42),\\n                  framealpha=0.92, edgecolor=\\\"0.85\\\", handlelength=2.0)\\n\\n    # ── Save ─────────────────────────────────────────────────────────────\\n    out_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n\\n    pdf_path = out_dir / \\\"fig2_auc_decay.pdf\\\"\\n    png_path = out_dir / \\\"fig2_auc_decay.png\\\"\\n    fig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    plt.close(fig)\\n\\n    print(f\\\"PDF: {pdf_path} ({pdf_path.stat().st_size/1024:.1f} KB)\\\")\\n    print(f\\\"PNG: {png_path} ({png_path.stat().st_size/1024:.1f} KB)\\\")\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "0f24a810-4455-449b-bab9-4be624325699",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-25T19:50:30.068Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017fZs4cWZYSzqFT3hyYGPfD`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/plot_fig_jsd_decay.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98caf926-118d-4e3c-bc27-1cd33971e011",
  "isSidechain": false,
  "requestId": "req_011CbPsK1n2V3xzvVhD8xFkA",
  "type": "assistant",
  "uuid": "7c80efac-fcf6-4b36-b59c-8486961656c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kaXT38BK3HTZFXbSmJvme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 66691,
      "output_tokens": 629,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 629,
          "cache_read_input_tokens": 66691,
          "cache_creation_input_tokens": 1424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1424
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

_source line 77 · 2026-05-25T19:50:30.471Z_

<details><summary>↩ Tool result · `toolu_017fZs4cWZYSzqFT3hyYGPfD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Generate paper figure: JSD decay across generational depth.\\n\\nBlue band = C4 K*=2 models (min-max), with median line.\\nSeparate lines for Mistral-7B (K*=1), arXiv Pythia (K*=3), Retrain-chain (K*>=4).\\n\\nOutput: docs/paper/figures/fig_jsd_decay.{pdf,png}\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nfrom pathlib import Path\\n\\nPAIR_LABELS = [\\\"0 vs 1\\\", \\\"1 vs 2\\\", \\\"2 vs 3\\\", \\\"3 vs 4\\\", \\\"4 vs 5\\\"]\\nx = np.arange(len(PAIR_LABELS))\\n\\n# --- C4 K*=2 models (band) ---\\nc4_k2 = {\\n    \\\"Qwen-1.5B\\\":       [0.163726, 0.010810, 0.005311, 0.003942, 0.003522],\\n    \\\"Qwen-1.5B-cont\\\":  [0.238045, 0.010089, 0.005309, 0.003699, 0.003942],\\n    \\\"LLaMA-8B\\\":        [0.076925, 0.012301, 0.004631, 0.004292, 0.003572],\\n    \\\"Pythia-greedy\\\":    [0.617756, 0.070498, 0.004498, 0.003202, 0.002579],\\n    \\\"Pythia-nuc0.9\\\":    [0.252017, 0.017922, 0.006115, 0.004110, 0.003301],\\n    \\\"Pythia-T0.7\\\":      [0.403980, 0.043741, 0.015638, 0.008836, 0.005122],\\n    \\\"Pythia-T1.2\\\":      [0.166001, 0.009573, 0.003991, 0.003303, 0.003177],\\n    \\\"Qwen-14B\\\":         [0.109700, 0.011200, 0.006200, 0.004400, 0.003600],\\n}\\n\\nc4_arr = np.array(list(c4_k2.values()))\\nc4_median = np.median(c4_arr, axis=0)\\nc4_min = np.min(c4_arr, axis=0)\\nc4_max = np.max(c4_arr, axis=0)\\n\\n# --- Individual lines ---\\nmistral_c4 = [0.124194, 0.008051, 0.005047, 0.004516, 0.004109]\\narxiv_pythia = [0.171338, 0.057344, 0.019524, 0.009917, 0.008846]\\nretrain_chain = [0.169964, 0.129382, 0.107086, 0.064225]\\n\\n# --- Plot ---\\nplt.rcParams.update({\\n    \\\"font.family\\\": \\\"serif\\\",\\n    \\\"font.size\\\": 9,\\n    \\\"axes.linewidth\\\": 0.8,\\n    \\\"xtick.major.width\\\": 0.6,\\n    \\\"ytick.major.width\\\": 0.6,\\n    \\\"xtick.direction\\\": \\\"in\\\",\\n    \\\"ytick.direction\\\": \\\"in\\\",\\n})\\n\\nfig, ax = plt.subplots(figsize=(5.0, 3.5), constrained_layout=True)\\n\\nax.fill_between(x, c4_min, c4_max, color=\\\"#4e79a7\\\", alpha=0.2, zorder=2)\\nax.semilogy(x, c4_median, \\\"-o\\\", color=\\\"#4e79a7\\\", lw=1.8, ms=5,\\n            label=r\\\"C4, $K^*\\\\!=\\\\!2$ (8 models, min-max)\\\", zorder=3)\\n\\nax.semilogy(x, mistral_c4, \\\"--s\\\", color=\\\"#9467bd\\\", lw=1.5, ms=5,\\n            label=r\\\"Mistral-7B, $K^*\\\\!=\\\\!1$\\\", zorder=3)\\n\\nax.semilogy(x, arxiv_pythia, \\\"-^\\\", color=\\\"#2ca02c\\\", lw=1.5, ms=5,\\n            label=r\\\"arXiv Pythia, $K^*\\\\!=\\\\!3$\\\", zorder=3)\\n\\nx_rt = np.arange(len(retrain_chain))\\nax.semilogy(x_rt, retrain_chain, \\\":D\\\", color=\\\"#d62728\\\", lw=1.5, ms=5,\\n            label=r\\\"Retrain-chain, $K^* \\\\geq 4$\\\", zorder=3)\\n\\nax.text(0.55, c4_median[0] * 1.35, \\\"$K^*\\\\\\\\!=\\\\\\\\!2$\\\", fontsize=8.5,\\n        color=\\\"#4e79a7\\\", fontweight=\\\"bold\\\")\\n\\nax.set_xticks(x)\\nax.set_xticklabels(PAIR_LABELS)\\nax.set_xlabel(\\\"Depth Pair\\\")\\nax.set_ylabel(\\\"JSD (log scale)\\\")\\nax.set_ylim(1.5e-3, 0.8)\\nax.set_xlim(-0.15, 4.15)\\n\\nax.legend(fontsize=7.5, loc=\\\"upper right\\\", framealpha=0.9, edgecolor=\\\"0.8\\\")\\n\\nout_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\nout_dir.mkdir(parents=True, exist_ok=True)\\n\\npdf_path = out_dir / \\\"fig_jsd_decay.pdf\\\"\\npng_path = out_dir / \\\"fig_jsd_decay.png\\\"\\nfig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\nfig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\nplt.close(fig)\\n\\nprint(f\\\"PDF: {pdf_path} ({pdf_path.stat().st_size / 1024:.1f} KB)\\\")\\nprint(f\\\"PNG: {png_path} ({png_path.stat().st_size / 1024:.1f} KB)\\\")\\nprint(f\\\"C4 band models ({len(c4_k2)}): {list(c4_k2.keys())}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c80efac-fcf6-4b36-b59c-8486961656c5",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "cdad3822-9886-4730-933b-5f10fa769643",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Generate paper figure: JSD decay across generational depth.\\\\n\\\\nBlue band = C4 K*=2 models (min-max), with median line.\\\\nSeparate lines for Mistral-7B (K*=1), arXiv Pythia (K*=3), Retrain-chain (K*>=4).\\\\n\\\\nOutput: docs/paper/figures/fig_jsd_decay.{pdf,png}\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nfrom pathlib import Path\\\\n\\\\nPAIR_LABELS = [\\\\\\\"0 vs 1\\\\\\\", \\\\\\\"1 vs 2\\\\\\\", \\\\\\\"2 vs 3\\\\\\\", \\\\\\\"3 vs 4\\\\\\\", \\\\\\\"4 vs 5\\\\\\\"]\\\\nx = np.arange(len(PAIR_LABELS))\\\\n\\\\n# --- C4 K*=2 models (band) ---\\\\nc4_k2 = {\\\\n    \\\\\\\"Qwen-1.5B\\\\\\\":       [0.163726, 0.010810, 0.005311, 0.003942, 0.003522],\\\\n    \\\\\\\"Qwen-1.5B-cont\\\\\\\":  [0.238045, 0.010089, 0.005309, 0.003699, 0.003942],\\\\n    \\\\\\\"LLaMA-8B\\\\\\\":        [0.076925, 0.012301, 0.004631, 0.004292, 0.003572],\\\\n    \\\\\\\"Pythia-greedy\\\\\\\":    [0.617756, 0.070498, 0.004498, 0.003202, 0.002579],\\\\n    \\\\\\\"Pythia-nuc0.9\\\\\\\":    [0.252017, 0.017922, 0.006115, 0.004110, 0.003301],\\\\n    \\\\\\\"Pythia-T0.7\\\\\\\":      [0.403980, 0.043741, 0.015638, 0.008836, 0.005122],\\\\n    \\\\\\\"Pythia-T1.2\\\\\\\":      [0.166001, 0.009573, 0.003991, 0.003303, 0.003177],\\\\n    \\\\\\\"Qwen-14B\\\\\\\":         [0.109700, 0.011200, 0.006200, 0.004400, 0.003600],\\\\n}\\\\n\\\\nc4_arr = np.array(list(c4_k2.values()))\\\\nc4_median = np.median(c4_arr, axis=0)\\\\nc4_min = np.min(c4_arr, axis=0)\\\\nc4_max = np.max(c4_arr, axis=0)\\\\n\\\\n# --- Individual lines ---\\\\nmistral_c4 = [0.124194, 0.008051, 0.005047, 0.004516, 0.004109]\\\\narxiv_pythia = [0.171338, 0.057344, 0.019524, 0.009917, 0.008846]\\\\nretrain_chain = [0.169964, 0.129382, 0.107086, 0.064225]\\\\n\\\\n# --- Plot ---\\\\nplt.rcParams.update({\\\\n    \\\\\\\"font.family\\\\\\\": \\\\\\\"serif\\\\\\\",\\\\n    \\\\\\\"font.size\\\\\\\": 9,\\\\n    \\\\\\\"axes.linewidth\\\\\\\": 0.8,\\\\n    \\\\\\\"xtick.major.width\\\\\\\": 0.6,\\\\n    \\\\\\\"ytick.major.width\\\\\\\": 0.6,\\\\n    \\\\\\\"xtick.direction\\\\\\\": \\\\\\\"in\\\\\\\",\\\\n    \\\\\\\"ytick.direction\\\\\\\": \\\\\\\"in\\\\\\\",\\\\n})\\\\n\\\\nfig, ax = plt.subplots(figsize=(5.0, 3.5), constrained_layout=True)\\\\n\\\\nax.fill_between(x, c4_min, c4_max, color=\\\\\\\"#4e79a7\\\\\\\", alpha=0.2, zorder=2)\\\\nax.semilogy(x, c4_median, \\\\\\\"-o\\\\\\\", color=\\\\\\\"#4e79a7\\\\\\\", lw=1.8, ms=5,\\\\n            label=r\\\\\\\"C4, $K^*\\\\\\\\!=\\\\\\\\!2$ (8 models, min-max)\\\\\\\", zorder=3)\\\\n\\\\nax.semilogy(x, mistral_c4, \\\\\\\"--s\\\\\\\", color=\\\\\\\"#9467bd\\\\\\\", lw=1.5, ms=5,\\\\n            label=r\\\\\\\"Mistral-7B, $K^*\\\\\\\\!=\\\\\\\\!1$\\\\\\\", zorder=3)\\\\n\\\\nax.semilogy(x, arxiv_pythia, \\\\\\\"-^\\\\\\\", color=\\\\\\\"#2ca02c\\\\\\\", lw=1.5, ms=5,\\\\n            label=r\\\\\\\"arXiv Pythia, $K^*\\\\\\\\!=\\\\\\\\!3$\\\\\\\", zorder=3)\\\\n\\\\nx_rt = np.arange(len(retrain_chain))\\\\nax.semilogy(x_rt, retrain_chain, \\\\\\\":D\\\\\\\", color=\\\\\\\"#d62728\\\\\\\", lw=1.5, ms=5,\\\\n            label=r\\\\\\\"Retrain-chain, $K^* \\\\\\\\geq 4$\\\\\\\", zorder=3)\\\\n\\\\nax.text(0.55, c4_median[0] * 1.35, \\\\\\\"$K^*\\\\\\\\\\\\\\\\!=\\\\\\\\\\\\\\\\!2$\\\\\\\", fontsize=8.5,\\\\n        color=\\\\\\\"#4e79a7\\\\\\\", fontweight=\\\\\\\"bold\\\\\\\")\\\\n\\\\nax.set_xticks(x)\\\\nax.set_xticklabels(PAIR_LABELS)\\\\nax.set_xlabel(\\\\\\\"Depth Pair\\\\\\\")\\\\nax.set_ylabel(\\\\\\\"JSD (log scale)\\\\\\\")\\\\nax.set_ylim(1.5e-3, 0.8)\\\\nax.set_xlim(-0.15, 4.15)\\\\n\\\\nax.legend(fontsize=7.5, loc=\\\\\\\"upper right\\\\\\\", framealpha=0.9, edgecolor=\\\\\\\"0.8\\\\\\\")\\\\n\\\\nout_dir = Path(__file__).resolve().parent.parent / \\\\\\\"docs\\\\\\\" / \\\\\\\"paper\\\\\\\" / \\\\\\\"figures\\\\\\\"\\\\nout_dir.mkdir(parents=True, exist_ok=True)\\\\n\\\\npdf_path = out_dir / \\\\\\\"fig_jsd_decay.pdf\\\\\\\"\\\\npng_path = out_dir / \\\\\\\"fig_jsd_decay.png\\\\\\\"\\\\nfig.savefig(pdf_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\nfig.savefig(png_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\nplt.close(fig)\\\\n\\\\nprint(f\\\\\\\"PDF: {pdf_path} ({pdf_path.stat().st_size / 1024:.1f} KB)\\\\\\\")\\\\nprint(f\\\\\\\"PNG: {png_path} ({png_path.stat().st_size / 1024:.1f} KB)\\\\\\\")\\\\nprint(f\\\\\\\"C4 band models ({len(c4_k2)}): {list(c4_k2.keys())}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Generate paper figure: JSD decay across generational depth.\\n\\nBlue band = C4 K*=2 models (min-max), with median line.\\nSeparate lines for Mistral-7B (K*=1), arXiv Pythia (K*=3), Retrain-chain (K*>=4).\\n\\nOutput: docs/paper/figures/fig_jsd_decay.{pdf,png}\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nfrom pathlib import Path\\n\\nPAIR_LABELS = [\\\"0 vs 1\\\", \\\"1 vs 2\\\", \\\"2 vs 3\\\", \\\"3 vs 4\\\", \\\"4 vs 5\\\"]\\nx = np.arange(len(PAIR_LABELS))\\n\\n# --- C4 K*=2 models (band) ---\\nc4_k2 = {\\n    \\\"Qwen-1.5B\\\":       [0.163726, 0.010810, 0.005311, 0.003942, 0.003522],\\n    \\\"Qwen-1.5B-cont\\\":  [0.238045, 0.010089, 0.005309, 0.003699, 0.003942],\\n    \\\"LLaMA-8B\\\":        [0.076925, 0.012301, 0.004631, 0.004292, 0.003572],\\n    \\\"Pythia-greedy\\\":    [0.617756, 0.070498, 0.004498, 0.003202, 0.002579],\\n    \\\"Pythia-nuc0.9\\\":    [0.252017, 0.017922, 0.006115, 0.004110, 0.003301],\\n    \\\"Pythia-T0.7\\\":      [0.403980, 0.043741, 0.015638, 0.008836, 0.005122],\\n    \\\"Pythia-T1.2\\\":      [0.166001, 0.009573, 0.003991, 0.003303, 0.003177],\\n    \\\"Qwen-14B\\\":         [0.109700, 0.011200, 0.006200, 0.004400, 0.003600],\\n}\\n\\nc4_arr = np.array(list(c4_k2.values()))\\nc4_median = np.median(c4_arr, axis=0)\\nc4_min = np.min(c4_arr, axis=0)\\nc4_max = np.max(c4_arr, axis=0)\\n\\n# --- Individual lines ---\\nmistral_c4 = [0.124194, 0.008051, 0.005047, 0.004516, 0.004109]\\narxiv_pythia = [0.171338, 0.057344, 0.019524, 0.009917, 0.008846]\\nretrain_chain = [0.169964, 0.129382, 0.107086, 0.064225]\\n\\n# --- Plot ---\\nplt.rcParams.update({\\n    \\\"font.family\\\": \\\"serif\\\",\\n    \\\"font.size\\\": 9,\\n    \\\"axes.linewidth\\\": 0.8,\\n    \\\"xtick.major.width\\\": 0.6,\\n    \\\"ytick.major.width\\\": 0.6,\\n    \\\"xtick.direction\\\": \\\"in\\\",\\n    \\\"ytick.direction\\\": \\\"in\\\",\\n})\\n\\nfig, ax = plt.subplots(figsize=(5.0, 3.5), constrained_layout=True)\\n\\nax.fill_between(x, c4_min, c4_max, color=\\\"#4e79a7\\\", alpha=0.2, zorder=2)\\nax.semilogy(x, c4_median, \\\"-o\\\", color=\\\"#4e79a7\\\", lw=1.8, ms=5,\\n            label=r\\\"C4, $K^*\\\\!=\\\\!2$ (8 models, min-max)\\\", zorder=3)\\n\\nax.semilogy(x, mistral_c4, \\\"--s\\\", color=\\\"#9467bd\\\", lw=1.5, ms=5,\\n            label=r\\\"Mistral-7B, $K^*\\\\!=\\\\!1$\\\", zorder=3)\\n\\nax.semilogy(x, arxiv_pythia, \\\"-^\\\", color=\\\"#2ca02c\\\", lw=1.5, ms=5,\\n            label=r\\\"arXiv Pythia, $K^*\\\\!=\\\\!3$\\\", zorder=3)\\n\\nx_rt = np.arange(len(retrain_chain))\\nax.semilogy(x_rt, retrain_chain, \\\":D\\\", color=\\\"#d62728\\\", lw=1.5, ms=5,\\n            label=r\\\"Retrain-chain, $K^* \\\\geq 4$\\\", zorder=3)\\n\\nax.text(0.55, c4_median[0] * 1.35, \\\"$K^*\\\\\\\\!=\\\\\\\\!2$\\\", fontsize=8.5,\\n        color=\\\"#4e79a7\\\", fontweight=\\\"bold\\\")\\n\\nax.set_xticks(x)\\nax.set_xticklabels(PAIR_LABELS)\\nax.set_xlabel(\\\"Depth Pair\\\")\\nax.set_ylabel(\\\"JSD (log scale)\\\")\\nax.set_ylim(1.5e-3, 0.8)\\nax.set_xlim(-0.15, 4.15)\\n\\nax.legend(fontsize=7.5, loc=\\\"upper right\\\", framealpha=0.9, edgecolor=\\\"0.8\\\")\\n\\nout_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\nout_dir.mkdir(parents=True, exist_ok=True)\\n\\npdf_path = out_dir / \\\"fig_jsd_decay.pdf\\\"\\npng_path = out_dir / \\\"fig_jsd_decay.png\\\"\\nfig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\nfig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\nplt.close(fig)\\n\\nprint(f\\\"PDF: {pdf_path} ({pdf_path.stat().st_size / 1024:.1f} KB)\\\")\\nprint(f\\\"PNG: {png_path} ({png_path.stat().st_size / 1024:.1f} KB)\\\")\\nprint(f\\\"C4 band models ({len(c4_k2)}): {list(c4_k2.keys())}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "7c80efac-fcf6-4b36-b59c-8486961656c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-25T19:50:31.010Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01W2vsLoFF3eAV1t4EyJwFr4`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/plot_filtering_strategies.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdad3822-9886-4730-933b-5f10fa769643",
  "isSidechain": false,
  "requestId": "req_011CbPsK1n2V3xzvVhD8xFkA",
  "type": "assistant",
  "uuid": "66971987-76b0-4b73-870c-f0fc714535cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kaXT38BK3HTZFXbSmJvme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 66691,
      "output_tokens": 629,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 629,
          "cache_read_input_tokens": 66691,
          "cache_creation_input_tokens": 1424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1424
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

_source line 79 · 2026-05-25T19:50:31.412Z_

<details><summary>↩ Tool result · `toolu_01W2vsLoFF3eAV1t4EyJwFr4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Filtering strategy comparison: bar chart of downstream MMLU under different curation methods.\\n\\nInput:  artifacts/*filter*.json, results_*/*filter*.json, or embedded paper data (exp-006)\\nOutput: artifacts/figures/fig_filtering_strategies.pdf\\nDeps:   matplotlib, numpy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nTABLEAU_COLORS = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\",\\n    \\\"#b07aa1\\\", \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#bab0ac\\\",\\n    \\\"#edc948\\\", \\\"#f28e2b\\\",\\n]\\n\\nEMBEDDED_FILTERING = {\\n    \\\"experiment\\\": \\\"exp-006 K*-aware data curation\\\",\\n    \\\"metric\\\": \\\"MMLU (5-shot)\\\",\\n    \\\"strategies\\\": [\\n        {\\\"name\\\": \\\"No filter\\\", \\\"score\\\": 0.5867, \\\"std\\\": 0.0021, \\\"category\\\": \\\"baseline\\\"},\\n        {\\\"name\\\": \\\"DSIR\\\", \\\"score\\\": 0.5867, \\\"std\\\": 0.0019, \\\"category\\\": \\\"baseline\\\"},\\n        {\\\"name\\\": \\\"Surprisal\\\\nselection\\\", \\\"score\\\": 0.5894, \\\"std\\\": 0.0018, \\\"category\\\": \\\"alternative\\\"},\\n        {\\\"name\\\": \\\"Graduated\\\\nweighting\\\", \\\"score\\\": 0.5892, \\\"std\\\": 0.0022, \\\"category\\\": \\\"alternative\\\"},\\n        {\\\"name\\\": \\\"Binary $K^*$\\\\nfiltering\\\", \\\"score\\\": 0.5941, \\\"std\\\": 0.0017, \\\"category\\\": \\\"ours\\\"},\\n    ],\\n}\\n\\n\\ndef discover_filtering_files(root):\\n    \\\"\\\"\\\"Find filtering experiment JSON files.\\\"\\\"\\\"\\n    patterns = [\\n        \\\"artifacts/*filter*.json\\\",\\n        \\\"artifacts/*curation*.json\\\",\\n        \\\"results_*/*filter*.json\\\",\\n        \\\"results/*filter*.json\\\",\\n        \\\"results_*/*curation*.json\\\",\\n    ]\\n    files = set()\\n    for pat in patterns:\\n        files.update(root.glob(pat))\\n    return sorted(files)\\n\\n\\ndef load_filtering_data(json_path):\\n    \\\"\\\"\\\"Load filtering comparison data from JSON.\\\"\\\"\\\"\\n    with open(json_path) as f:\\n        raw = json.load(f)\\n    if \\\"strategies\\\" in raw:\\n        return raw\\n    return None\\n\\n\\ndef parse_args():\\n    parser = argparse.ArgumentParser(description=\\\"Plot filtering strategy comparison\\\")\\n    parser.add_argument(\\\"--data-dir\\\", type=Path,\\n                        default=Path(__file__).resolve().parent.parent,\\n                        help=\\\"Root directory to scan for filtering data\\\")\\n    parser.add_argument(\\\"--output\\\", type=Path, default=None,\\n                        help=\\\"Output PDF path\\\")\\n    parser.add_argument(\\\"--use-embedded\\\", action=\\\"store_true\\\",\\n                        help=\\\"Force use of embedded paper data\\\")\\n    return parser.parse_args()\\n\\n\\ndef main():\\n    args = parse_args()\\n    root = args.data_dir\\n\\n    data = None\\n    if not args.use_embedded:\\n        filter_files = discover_filtering_files(root)\\n        for fp in filter_files:\\n            data = load_filtering_data(fp)\\n            if data is not None:\\n                print(f\\\"Loaded filtering data from {fp}\\\")\\n                break\\n\\n    if data is None:\\n        print(\\\"No filtering JSON found on disk — using embedded paper data\\\")\\n        data = EMBEDDED_FILTERING\\n\\n    strategies = data[\\\"strategies\\\"]\\n    metric_label = data.get(\\\"metric\\\", \\\"MMLU (5-shot)\\\")\\n\\n    names = [s[\\\"name\\\"] for s in strategies]\\n    scores = np.array([s[\\\"score\\\"] for s in strategies])\\n    stds = np.array([s.get(\\\"std\\\", 0) for s in strategies])\\n    categories = [s.get(\\\"category\\\", \\\"other\\\") for s in strategies]\\n\\n    category_colors = {\\n        \\\"baseline\\\": \\\"#bab0ac\\\",\\n        \\\"alternative\\\": \\\"#4e79a7\\\",\\n        \\\"ours\\\": \\\"#e15759\\\",\\n        \\\"other\\\": \\\"#76b7b2\\\",\\n    }\\n    colors = [category_colors.get(c, \\\"#76b7b2\\\") for c in categories]\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 11,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)\\n\\n    x = np.arange(len(names))\\n    bar_width = 0.6\\n    bars = ax.bar(x, scores, bar_width, color=colors, edgecolor=\\\"white\\\",\\n                  linewidth=0.8, zorder=3)\\n\\n    if np.any(stds > 0):\\n        ax.errorbar(x, scores, yerr=1.96 * stds, fmt=\\\"none\\\", ecolor=\\\"#333333\\\",\\n                    elinewidth=1.0, capsize=3, capthick=1.0, zorder=4)\\n\\n    for i, (bar, score) in enumerate(zip(bars, scores)):\\n        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0008,\\n                f\\\"{score:.4f}\\\", ha=\\\"center\\\", va=\\\"bottom\\\", fontsize=9,\\n                fontweight=\\\"bold\\\" if categories[i] == \\\"ours\\\" else \\\"normal\\\")\\n\\n    best_idx = np.argmax(scores)\\n    bars[best_idx].set_edgecolor(\\\"#333333\\\")\\n    bars[best_idx].set_linewidth(1.5)\\n\\n    y_min = min(scores) - 0.006\\n    y_max = max(scores) + 0.005\\n    ax.set_ylim(y_min, y_max)\\n\\n    no_filter_score = next((s[\\\"score\\\"] for s in strategies if \\\"no filter\\\" in s[\\\"name\\\"].lower()), None)\\n    if no_filter_score is not None:\\n        ax.axhline(no_filter_score, color=\\\"#bab0ac\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n        ax.text(len(names) - 0.5, no_filter_score + 0.0003, \\\"no-filter baseline\\\",\\n                fontsize=8, color=\\\"#999999\\\", ha=\\\"right\\\", va=\\\"bottom\\\")\\n\\n    ax.set_xticks(x)\\n    ax.set_xticklabels(names, fontsize=9.5)\\n    ax.set_ylabel(metric_label)\\n    ax.tick_params(direction=\\\"in\\\")\\n    ax.grid(axis=\\\"y\\\", color=\\\"#e0e0e0\\\", linewidth=0.5, zorder=0)\\n\\n    from matplotlib.patches import Patch\\n    legend_elements = [\\n        Patch(facecolor=\\\"#bab0ac\\\", edgecolor=\\\"white\\\", label=\\\"Baseline\\\"),\\n        Patch(facecolor=\\\"#4e79a7\\\", edgecolor=\\\"white\\\", label=\\\"Alternative\\\"),\\n        Patch(facecolor=\\\"#e15759\\\", edgecolor=\\\"white\\\", label=\\\"Ours\\\"),\\n    ]\\n    ax.legend(handles=legend_elements, fontsize=9, loc=\\\"upper left\\\",\\n              framealpha=0.9, edgecolor=\\\"0.8\\\")\\n\\n    if args.output:\\n        out_path = args.output\\n    else:\\n        out_dir = root / \\\"artifacts\\\" / \\\"figures\\\"\\n        out_dir.mkdir(parents=True, exist_ok=True)\\n        out_path = out_dir / \\\"fig_filtering_strategies.pdf\\\"\\n\\n    out_path.parent.mkdir(parents=True, exist_ok=True)\\n    fig.savefig(out_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    png_path = out_path.with_suffix(\\\".png\\\")\\n    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    plt.close(fig)\\n\\n    pdf_size = out_path.stat().st_size\\n    png_size = png_path.stat().st_size\\n    print(f\\\"Strategies: {names}\\\")\\n    print(f\\\"PDF: {pdf_size/1024:.1f} KB | PNG: {png_size/1024:.1f} KB\\\")\\n    assert pdf_size > 3 * 1024, f\\\"PDF too small: {pdf_size}\\\"\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66971987-76b0-4b73-870c-f0fc714535cc",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "7a9f50ad-ac2f-4555-9132-d954db25363c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Filtering strategy comparison: bar chart of downstream MMLU under different curation methods.\\\\n\\\\nInput:  artifacts/*filter*.json, results_*/*filter*.json, or embedded paper data (exp-006)\\\\nOutput: artifacts/figures/fig_filtering_strategies.pdf\\\\nDeps:   matplotlib, numpy\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\nTABLEAU_COLORS = [\\\\n    \\\\\\\"#4e79a7\\\\\\\", \\\\\\\"#e15759\\\\\\\", \\\\\\\"#76b7b2\\\\\\\", \\\\\\\"#59a14f\\\\\\\",\\\\n    \\\\\\\"#b07aa1\\\\\\\", \\\\\\\"#ff9da7\\\\\\\", \\\\\\\"#9c755f\\\\\\\", \\\\\\\"#bab0ac\\\\\\\",\\\\n    \\\\\\\"#edc948\\\\\\\", \\\\\\\"#f28e2b\\\\\\\",\\\\n]\\\\n\\\\nEMBEDDED_FILTERING = {\\\\n    \\\\\\\"experiment\\\\\\\": \\\\\\\"exp-006 K*-aware data curation\\\\\\\",\\\\n    \\\\\\\"metric\\\\\\\": \\\\\\\"MMLU (5-shot)\\\\\\\",\\\\n    \\\\\\\"strategies\\\\\\\": [\\\\n        {\\\\\\\"name\\\\\\\": \\\\\\\"No filter\\\\\\\", \\\\\\\"score\\\\\\\": 0.5867, \\\\\\\"std\\\\\\\": 0.0021, \\\\\\\"category\\\\\\\": \\\\\\\"baseline\\\\\\\"},\\\\n        {\\\\\\\"name\\\\\\\": \\\\\\\"DSIR\\\\\\\", \\\\\\\"score\\\\\\\": 0.5867, \\\\\\\"std\\\\\\\": 0.0019, \\\\\\\"category\\\\\\\": \\\\\\\"baseline\\\\\\\"},\\\\n        {\\\\\\\"name\\\\\\\": \\\\\\\"Surprisal\\\\\\\\nselection\\\\\\\", \\\\\\\"score\\\\\\\": 0.5894, \\\\\\\"std\\\\\\\": 0.0018, \\\\\\\"category\\\\\\\": \\\\\\\"alternative\\\\\\\"},\\\\n        {\\\\\\\"name\\\\\\\": \\\\\\\"Graduated\\\\\\\\nweighting\\\\\\\", \\\\\\\"score\\\\\\\": 0.5892, \\\\\\\"std\\\\\\\": 0.0022, \\\\\\\"category\\\\\\\": \\\\\\\"alternative\\\\\\\"},\\\\n        {\\\\\\\"name\\\\\\\": \\\\\\\"Binary $K^*$\\\\\\\\nfiltering\\\\\\\", \\\\\\\"score\\\\\\\": 0.5941, \\\\\\\"std\\\\\\\": 0.0017, \\\\\\\"category\\\\\\\": \\\\\\\"ours\\\\\\\"},\\\\n    ],\\\\n}\\\\n\\\\n\\\\ndef discover_filtering_files(root):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Find filtering experiment JSON files.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    patterns = [\\\\n        \\\\\\\"artifacts/*filter*.json\\\\\\\",\\\\n        \\\\\\\"artifacts/*curation*.json\\\\\\\",\\\\n        \\\\\\\"results_*/*filter*.json\\\\\\\",\\\\n        \\\\\\\"results/*filter*.json\\\\\\\",\\\\n        \\\\\\\"results_*/*curation*.json\\\\\\\",\\\\n    ]\\\\n    files = set()\\\\n    for pat in patterns:\\\\n        files.update(root.glob(pat))\\\\n    return sorted(files)\\\\n\\\\n\\\\ndef load_filtering_data(json_path):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load filtering comparison data from JSON.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(json_path) as f:\\\\n        raw = json.load(f)\\\\n    if \\\\\\\"strategies\\\\\\\" in raw:\\\\n        return raw\\\\n    return None\\\\n\\\\n\\\\ndef parse_args():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"Plot filtering strategy comparison\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--data-dir\\\\\\\", type=Path,\\\\n                        default=Path(__file__).resolve().parent.parent,\\\\n                        help=\\\\\\\"Root directory to scan for filtering data\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output\\\\\\\", type=Path, default=None,\\\\n                        help=\\\\\\\"Output PDF path\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--use-embedded\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                        help=\\\\\\\"Force use of embedded paper data\\\\\\\")\\\\n    return parser.parse_args()\\\\n\\\\n\\\\ndef main():\\\\n    args = parse_args()\\\\n    root = args.data_dir\\\\n\\\\n    data = None\\\\n    if not args.use_embedded:\\\\n        filter_files = discover_filtering_files(root)\\\\n        for fp in filter_files:\\\\n            data = load_filtering_data(fp)\\\\n            if data is not None:\\\\n                print(f\\\\\\\"Loaded filtering data from {fp}\\\\\\\")\\\\n                break\\\\n\\\\n    if data is None:\\\\n        print(\\\\\\\"No filtering JSON found on disk — using embedded paper data\\\\\\\")\\\\n        data = EMBEDDED_FILTERING\\\\n\\\\n    strategies = data[\\\\\\\"strategies\\\\\\\"]\\\\n    metric_label = data.get(\\\\\\\"metric\\\\\\\", \\\\\\\"MMLU (5-shot)\\\\\\\")\\\\n\\\\n    names = [s[\\\\\\\"name\\\\\\\"] for s in strategies]\\\\n    scores = np.array([s[\\\\\\\"score\\\\\\\"] for s in strategies])\\\\n    stds = np.array([s.get(\\\\\\\"std\\\\\\\", 0) for s in strategies])\\\\n    categories = [s.get(\\\\\\\"category\\\\\\\", \\\\\\\"other\\\\\\\") for s in strategies]\\\\n\\\\n    category_colors = {\\\\n        \\\\\\\"baseline\\\\\\\": \\\\\\\"#bab0ac\\\\\\\",\\\\n        \\\\\\\"alternative\\\\\\\": \\\\\\\"#4e79a7\\\\\\\",\\\\n        \\\\\\\"ours\\\\\\\": \\\\\\\"#e15759\\\\\\\",\\\\n        \\\\\\\"other\\\\\\\": \\\\\\\"#76b7b2\\\\\\\",\\\\n    }\\\\n    colors = [category_colors.get(c, \\\\\\\"#76b7b2\\\\\\\") for c in categories]\\\\n\\\\n    plt.rcParams.update({\\\\n        \\\\\\\"font.family\\\\\\\": \\\\\\\"serif\\\\\\\",\\\\n        \\\\\\\"font.size\\\\\\\": 11,\\\\n        \\\\\\\"axes.linewidth\\\\\\\": 0.8,\\\\n        \\\\\\\"xtick.major.width\\\\\\\": 0.8,\\\\n        \\\\\\\"ytick.major.width\\\\\\\": 0.8,\\\\n    })\\\\n\\\\n    fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)\\\\n\\\\n    x = np.arange(len(names))\\\\n    bar_width = 0.6\\\\n    bars = ax.bar(x, scores, bar_width, color=colors, edgecolor=\\\\\\\"white\\\\\\\",\\\\n                  linewidth=0.8, zorder=3)\\\\n\\\\n    if np.any(stds > 0):\\\\n        ax.errorbar(x, scores, yerr=1.96 * stds, fmt=\\\\\\\"none\\\\\\\", ecolor=\\\\\\\"#333333\\\\\\\",\\\\n                    elinewidth=1.0, capsize=3, capthick=1.0, zorder=4)\\\\n\\\\n    for i, (bar, score) in enumerate(zip(bars, scores)):\\\\n        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0008,\\\\n                f\\\\\\\"{score:.4f}\\\\\\\", ha=\\\\\\\"center\\\\\\\", va=\\\\\\\"bottom\\\\\\\", fontsize=9,\\\\n                fontweight=\\\\\\\"bold\\\\\\\" if categories[i] == \\\\\\\"ours\\\\\\\" else \\\\\\\"normal\\\\\\\")\\\\n\\\\n    best_idx = np.argmax(scores)\\\\n    bars[best_idx].set_edgecolor(\\\\\\\"#333333\\\\\\\")\\\\n    bars[best_idx].set_linewidth(1.5)\\\\n\\\\n    y_min = min(scores) - 0.006\\\\n    y_max = max(scores) + 0.005\\\\n    ax.set_ylim(y_min, y_max)\\\\n\\\\n    no_filter_score = next((s[\\\\\\\"score\\\\\\\"] for s in strategies if \\\\\\\"no filter\\\\\\\" in s[\\\\\\\"name\\\\\\\"].lower()), None)\\\\n    if no_filter_score is not None:\\\\n        ax.axhline(no_filter_score, color=\\\\\\\"#bab0ac\\\\\\\", ls=\\\\\\\"--\\\\\\\", lw=0.8, zorder=1)\\\\n        ax.text(len(names) - 0.5, no_filter_score + 0.0003, \\\\\\\"no-filter baseline\\\\\\\",\\\\n                fontsize=8, color=\\\\\\\"#999999\\\\\\\", ha=\\\\\\\"right\\\\\\\", va=\\\\\\\"bottom\\\\\\\")\\\\n\\\\n    ax.set_xticks(x)\\\\n    ax.set_xticklabels(names, fontsize=9.5)\\\\n    ax.set_ylabel(metric_label)\\\\n    ax.tick_params(direction=\\\\\\\"in\\\\\\\")\\\\n    ax.grid(axis=\\\\\\\"y\\\\\\\", color=\\\\\\\"#e0e0e0\\\\\\\", linewidth=0.5, zorder=0)\\\\n\\\\n    from matplotlib.patches import Patch\\\\n    legend_elements = [\\\\n        Patch(facecolor=\\\\\\\"#bab0ac\\\\\\\", edgecolor=\\\\\\\"white\\\\\\\", label=\\\\\\\"Baseline\\\\\\\"),\\\\n        Patch(facecolor=\\\\\\\"#4e79a7\\\\\\\", edgecolor=\\\\\\\"white\\\\\\\", label=\\\\\\\"Alternative\\\\\\\"),\\\\n        Patch(facecolor=\\\\\\\"#e15759\\\\\\\", edgecolor=\\\\\\\"white\\\\\\\", label=\\\\\\\"Ours\\\\\\\"),\\\\n    ]\\\\n    ax.legend(handles=legend_elements, fontsize=9, loc=\\\\\\\"upper left\\\\\\\",\\\\n              framealpha=0.9, edgecolor=\\\\\\\"0.8\\\\\\\")\\\\n\\\\n    if args.output:\\\\n        out_path = args.output\\\\n    else:\\\\n        out_dir = root / \\\\\\\"artifacts\\\\\\\" / \\\\\\\"figures\\\\\\\"\\\\n        out_dir.mkdir(parents=True, exist_ok=True)\\\\n        out_path = out_dir / \\\\\\\"fig_filtering_strategies.pdf\\\\\\\"\\\\n\\\\n    out_path.parent.mkdir(parents=True, exist_ok=True)\\\\n    fig.savefig(out_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    png_path = out_path.with_suffix(\\\\\\\".png\\\\\\\")\\\\n    fig.savefig(png_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close(fig)\\\\n\\\\n    pdf_size = out_path.stat().st_size\\\\n    png_size = png_path.stat().st_size\\\\n    print(f\\\\\\\"Strategies: {names}\\\\\\\")\\\\n    print(f\\\\\\\"PDF: {pdf_size/1024:.1f} KB | PNG: {png_size/1024:.1f} KB\\\\\\\")\\\\n    assert pdf_size > 3 * 1024, f\\\\\\\"PDF too small: {pdf_size}\\\\\\\"\\\\n    print(\\\\\\\"OK\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Filtering strategy comparison: bar chart of downstream MMLU under different curation methods.\\n\\nInput:  artifacts/*filter*.json, results_*/*filter*.json, or embedded paper data (exp-006)\\nOutput: artifacts/figures/fig_filtering_strategies.pdf\\nDeps:   matplotlib, numpy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nTABLEAU_COLORS = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\",\\n    \\\"#b07aa1\\\", \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#bab0ac\\\",\\n    \\\"#edc948\\\", \\\"#f28e2b\\\",\\n]\\n\\nEMBEDDED_FILTERING = {\\n    \\\"experiment\\\": \\\"exp-006 K*-aware data curation\\\",\\n    \\\"metric\\\": \\\"MMLU (5-shot)\\\",\\n    \\\"strategies\\\": [\\n        {\\\"name\\\": \\\"No filter\\\", \\\"score\\\": 0.5867, \\\"std\\\": 0.0021, \\\"category\\\": \\\"baseline\\\"},\\n        {\\\"name\\\": \\\"DSIR\\\", \\\"score\\\": 0.5867, \\\"std\\\": 0.0019, \\\"category\\\": \\\"baseline\\\"},\\n        {\\\"name\\\": \\\"Surprisal\\\\nselection\\\", \\\"score\\\": 0.5894, \\\"std\\\": 0.0018, \\\"category\\\": \\\"alternative\\\"},\\n        {\\\"name\\\": \\\"Graduated\\\\nweighting\\\", \\\"score\\\": 0.5892, \\\"std\\\": 0.0022, \\\"category\\\": \\\"alternative\\\"},\\n        {\\\"name\\\": \\\"Binary $K^*$\\\\nfiltering\\\", \\\"score\\\": 0.5941, \\\"std\\\": 0.0017, \\\"category\\\": \\\"ours\\\"},\\n    ],\\n}\\n\\n\\ndef discover_filtering_files(root):\\n    \\\"\\\"\\\"Find filtering experiment JSON files.\\\"\\\"\\\"\\n    patterns = [\\n        \\\"artifacts/*filter*.json\\\",\\n        \\\"artifacts/*curation*.json\\\",\\n        \\\"results_*/*filter*.json\\\",\\n        \\\"results/*filter*.json\\\",\\n        \\\"results_*/*curation*.json\\\",\\n    ]\\n    files = set()\\n    for pat in patterns:\\n        files.update(root.glob(pat))\\n    return sorted(files)\\n\\n\\ndef load_filtering_data(json_path):\\n    \\\"\\\"\\\"Load filtering comparison data from JSON.\\\"\\\"\\\"\\n    with open(json_path) as f:\\n        raw = json.load(f)\\n    if \\\"strategies\\\" in raw:\\n        return raw\\n    return None\\n\\n\\ndef parse_args():\\n    parser = argparse.ArgumentParser(description=\\\"Plot filtering strategy comparison\\\")\\n    parser.add_argument(\\\"--data-dir\\\", type=Path,\\n                        default=Path(__file__).resolve().parent.parent,\\n                        help=\\\"Root directory to scan for filtering data\\\")\\n    parser.add_argument(\\\"--output\\\", type=Path, default=None,\\n                        help=\\\"Output PDF path\\\")\\n    parser.add_argument(\\\"--use-embedded\\\", action=\\\"store_true\\\",\\n                        help=\\\"Force use of embedded paper data\\\")\\n    return parser.parse_args()\\n\\n\\ndef main():\\n    args = parse_args()\\n    root = args.data_dir\\n\\n    data = None\\n    if not args.use_embedded:\\n        filter_files = discover_filtering_files(root)\\n        for fp in filter_files:\\n            data = load_filtering_data(fp)\\n            if data is not None:\\n                print(f\\\"Loaded filtering data from {fp}\\\")\\n                break\\n\\n    if data is None:\\n        print(\\\"No filtering JSON found on disk — using embedded paper data\\\")\\n        data = EMBEDDED_FILTERING\\n\\n    strategies = data[\\\"strategies\\\"]\\n    metric_label = data.get(\\\"metric\\\", \\\"MMLU (5-shot)\\\")\\n\\n    names = [s[\\\"name\\\"] for s in strategies]\\n    scores = np.array([s[\\\"score\\\"] for s in strategies])\\n    stds = np.array([s.get(\\\"std\\\", 0) for s in strategies])\\n    categories = [s.get(\\\"category\\\", \\\"other\\\") for s in strategies]\\n\\n    category_colors = {\\n        \\\"baseline\\\": \\\"#bab0ac\\\",\\n        \\\"alternative\\\": \\\"#4e79a7\\\",\\n        \\\"ours\\\": \\\"#e15759\\\",\\n        \\\"other\\\": \\\"#76b7b2\\\",\\n    }\\n    colors = [category_colors.get(c, \\\"#76b7b2\\\") for c in categories]\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 11,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)\\n\\n    x = np.arange(len(names))\\n    bar_width = 0.6\\n    bars = ax.bar(x, scores, bar_width, color=colors, edgecolor=\\\"white\\\",\\n                  linewidth=0.8, zorder=3)\\n\\n    if np.any(stds > 0):\\n        ax.errorbar(x, scores, yerr=1.96 * stds, fmt=\\\"none\\\", ecolor=\\\"#333333\\\",\\n                    elinewidth=1.0, capsize=3, capthick=1.0, zorder=4)\\n\\n    for i, (bar, score) in enumerate(zip(bars, scores)):\\n        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0008,\\n                f\\\"{score:.4f}\\\", ha=\\\"center\\\", va=\\\"bottom\\\", fontsize=9,\\n                fontweight=\\\"bold\\\" if categories[i] == \\\"ours\\\" else \\\"normal\\\")\\n\\n    best_idx = np.argmax(scores)\\n    bars[best_idx].set_edgecolor(\\\"#333333\\\")\\n    bars[best_idx].set_linewidth(1.5)\\n\\n    y_min = min(scores) - 0.006\\n    y_max = max(scores) + 0.005\\n    ax.set_ylim(y_min, y_max)\\n\\n    no_filter_score = next((s[\\\"score\\\"] for s in strategies if \\\"no filter\\\" in s[\\\"name\\\"].lower()), None)\\n    if no_filter_score is not None:\\n        ax.axhline(no_filter_score, color=\\\"#bab0ac\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n        ax.text(len(names) - 0.5, no_filter_score + 0.0003, \\\"no-filter baseline\\\",\\n                fontsize=8, color=\\\"#999999\\\", ha=\\\"right\\\", va=\\\"bottom\\\")\\n\\n    ax.set_xticks(x)\\n    ax.set_xticklabels(names, fontsize=9.5)\\n    ax.set_ylabel(metric_label)\\n    ax.tick_params(direction=\\\"in\\\")\\n    ax.grid(axis=\\\"y\\\", color=\\\"#e0e0e0\\\", linewidth=0.5, zorder=0)\\n\\n    from matplotlib.patches import Patch\\n    legend_elements = [\\n        Patch(facecolor=\\\"#bab0ac\\\", edgecolor=\\\"white\\\", label=\\\"Baseline\\\"),\\n        Patch(facecolor=\\\"#4e79a7\\\", edgecolor=\\\"white\\\", label=\\\"Alternative\\\"),\\n        Patch(facecolor=\\\"#e15759\\\", edgecolor=\\\"white\\\", label=\\\"Ours\\\"),\\n    ]\\n    ax.legend(handles=legend_elements, fontsize=9, loc=\\\"upper left\\\",\\n              framealpha=0.9, edgecolor=\\\"0.8\\\")\\n\\n    if args.output:\\n        out_path = args.output\\n    else:\\n        out_dir = root / \\\"artifacts\\\" / \\\"figures\\\"\\n        out_dir.mkdir(parents=True, exist_ok=True)\\n        out_path = out_dir / \\\"fig_filtering_strategies.pdf\\\"\\n\\n    out_path.parent.mkdir(parents=True, exist_ok=True)\\n    fig.savefig(out_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    png_path = out_path.with_suffix(\\\".png\\\")\\n    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    plt.close(fig)\\n\\n    pdf_size = out_path.stat().st_size\\n    png_size = png_path.stat().st_size\\n    print(f\\\"Strategies: {names}\\\")\\n    print(f\\\"PDF: {pdf_size/1024:.1f} KB | PNG: {png_size/1024:.1f} KB\\\")\\n    assert pdf_size > 3 * 1024, f\\\"PDF too small: {pdf_size}\\\"\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "66971987-76b0-4b73-870c-f0fc714535cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-25T19:50:31.816Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PLzTtH2Z2VQy8EwGpyuUH3`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/draw_kstar_theta.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a9f50ad-ac2f-4555-9132-d954db25363c",
  "isSidechain": false,
  "requestId": "req_011CbPsK1n2V3xzvVhD8xFkA",
  "type": "assistant",
  "uuid": "cce48959-f444-4b9b-9e96-e8f376b7457f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kaXT38BK3HTZFXbSmJvme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 66691,
      "output_tokens": 629,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 629,
          "cache_read_input_tokens": 66691,
          "cache_creation_input_tokens": 1424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1424
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

_source line 81 · 2026-05-25T19:50:32.223Z_

<details><summary>↩ Tool result · `toolu_01PLzTtH2Z2VQy8EwGpyuUH3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Figure 3: two-panel K*(theta) figure.\\n\\nPanel (a): Pairwise AUC profile across depth pairs (C4 configs)\\nPanel (b): K*(theta) sensitivity\\n\\nOutput: docs/paper/figures/fig_kstar_theta.pdf\\n\\\"\\\"\\\"\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nPAIR_KEYS = [\\\"0v1\\\", \\\"1v2\\\", \\\"2v3\\\", \\\"3v4\\\", \\\"4v5\\\"]\\n\\nMODELS = {\\n    \\\"Qwen-rw\\\": {\\n        \\\"mean\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\n        \\\"ci_lower\\\": [0.9946, 0.6859, 0.5795, 0.5333, 0.5238],\\n        \\\"ci_upper\\\": [0.9976, 0.7041, 0.5991, 0.5551, 0.5448],\\n    },\\n    \\\"Pythia\\\": {\\n        \\\"mean\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\n        \\\"ci_lower\\\": [0.9921, 0.6454, 0.5417, 0.5041, 0.5021],\\n        \\\"ci_upper\\\": [0.9943, 0.6630, 0.5628, 0.5260, 0.5249],\\n    },\\n    \\\"OLMo\\\": {\\n        \\\"mean\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\n        \\\"ci_lower\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\n        \\\"ci_upper\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\n    },\\n    \\\"Qwen-cont\\\": {\\n        \\\"mean\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\n        \\\"ci_lower\\\": [0.9963, 0.6015, 0.5511, 0.5308, 0.5035],\\n        \\\"ci_upper\\\": [0.9978, 0.6213, 0.5712, 0.5508, 0.5255],\\n    },\\n    \\\"Qwen-7B\\\": {\\n        \\\"mean\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\n        \\\"ci_lower\\\": [0.9610, 0.6080, 0.5390, 0.5180, 0.4990],\\n        \\\"ci_upper\\\": [0.9670, 0.6260, 0.5590, 0.5370, 0.5180],\\n    },\\n}\\n\\nTABLEAU = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\", \\\"#b07aa1\\\",\\n    \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#bab0ac\\\", \\\"#edc948\\\", \\\"#f28e2b\\\",\\n]\\nMARKERS = [\\\"o\\\", \\\"s\\\", \\\"^\\\", \\\"D\\\", \\\"v\\\", \\\"P\\\", \\\"X\\\", \\\"*\\\", \\\"h\\\", \\\"<\\\"]\\n\\n\\ndef compute_kstar(ci_lowers, theta):\\n    k = 0\\n    for v in ci_lowers:\\n        if v >= theta:\\n            k += 1\\n        else:\\n            break\\n    return k\\n\\n\\ndef main():\\n    x = np.arange(len(PAIR_KEYS))\\n    thetas = np.arange(0.50, 0.751, 0.005)\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.direction\\\": \\\"in\\\",\\n        \\\"ytick.direction\\\": \\\"in\\\",\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 3.5),\\n                                      gridspec_kw={\\\"width_ratios\\\": [1, 1.15]})\\n\\n    # ── Panel (a): Pairwise AUC profile ─────────────────────────────────\\n    ax_a.axhline(0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax_a.text(4.05, 0.607, r\\\"$\\\\theta = 0.60$\\\", fontsize=8, color=\\\"grey\\\",\\n              va=\\\"bottom\\\", ha=\\\"right\\\")\\n\\n    ax_a.axvspan(1.5, 2.5, color=\\\"#4e79a7\\\", alpha=0.06, zorder=0)\\n    ax_a.annotate(r\\\"$K^*\\\\!=\\\\!2$\\\", xy=(1.7, 0.68), fontsize=8, color=\\\"#4e79a7\\\",\\n                  alpha=0.7)\\n\\n    for i, (name, data) in enumerate(MODELS.items()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        marker = MARKERS[i % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n        lo = data[\\\"ci_lower\\\"]\\n        hi = data[\\\"ci_upper\\\"]\\n\\n        ax_a.fill_between(x, lo, hi, color=color, alpha=0.15, linewidth=0)\\n        ax_a.plot(x, means, \\\"-\\\", color=color, lw=1.6, marker=marker,\\n                  markersize=4.5, label=name, zorder=3)\\n\\n    ax_a.set_xticks(x)\\n    ax_a.set_xticklabels(PAIR_KEYS)\\n    ax_a.set_xlabel(\\\"Depth pair\\\")\\n    ax_a.set_ylabel(\\\"Pairwise AUC\\\")\\n    ax_a.set_ylim(0.47, 1.02)\\n    ax_a.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\n    ax_a.legend(fontsize=7.5, loc=\\\"upper right\\\", framealpha=0.92,\\n                edgecolor=\\\"0.85\\\", handlelength=2.0)\\n    ax_a.set_title(r\\\"$\\\\bf{(a)}$\\\" + \\\" Pairwise AUC profile\\\", fontsize=10,\\n                   loc=\\\"left\\\", pad=6)\\n\\n    # ── Panel (b): K*(θ) sensitivity ────────────────────────────────────\\n    all_kstar = {}\\n    for name, data in MODELS.items():\\n        ci_lo = data[\\\"ci_lower\\\"]\\n        ks = [compute_kstar(ci_lo, t) for t in thetas]\\n        all_kstar[name] = ks\\n\\n    kstar_arr = np.array(list(all_kstar.values()))\\n    k_min = kstar_arr.min(axis=0)\\n    k_max = kstar_arr.max(axis=0)\\n\\n    mask_23 = (k_min >= 2) & (k_max <= 3) & (k_min != k_max)\\n    mask_2  = (k_min == 2) & (k_max == 2)\\n\\n    for j in range(len(thetas)):\\n        if mask_23[j]:\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\n                         color=\\\"#cccccc\\\", alpha=0.5, linewidth=0, zorder=0)\\n        if mask_2[j]:\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\n                         color=\\\"#b8d4e3\\\", alpha=0.5, linewidth=0, zorder=0)\\n\\n    for i, (name, ks) in enumerate(all_kstar.items()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        ax_b.step(thetas, ks, where=\\\"post\\\", label=name,\\n                  linewidth=1.6, color=color)\\n\\n    ax_b.axvline(x=0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, alpha=0.7)\\n    ax_b.text(0.605, 5.15, r\\\"$\\\\theta=0.60$\\\", color=\\\"grey\\\", fontsize=8,\\n              va=\\\"top\\\")\\n\\n    import matplotlib.patches as mpatches\\n    legend_patches = [\\n        mpatches.Patch(color=\\\"#cccccc\\\", alpha=0.5, label=r\\\"$K^*\\\\!\\\\in\\\\!\\\\{2,3\\\\}$ (all models)\\\"),\\n        mpatches.Patch(color=\\\"#b8d4e3\\\", alpha=0.5, label=r\\\"$K^*\\\\!=\\\\!2$ (all models)\\\"),\\n    ]\\n    handles_lines = []\\n    for i, name in enumerate(all_kstar.keys()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        h = plt.Line2D([0], [0], color=color, lw=1.6, label=name)\\n        handles_lines.append(h)\\n\\n    ax_b.legend(handles=legend_patches + handles_lines, fontsize=7.5,\\n                loc=\\\"upper right\\\", framealpha=0.92, edgecolor=\\\"0.85\\\")\\n\\n    ax_b.set_xlabel(r\\\"Threshold $\\\\theta$\\\")\\n    ax_b.set_ylabel(r\\\"$K^*(\\\\theta)$\\\")\\n    ax_b.set_xlim(0.495, 0.755)\\n    max_k = max(len(v) for v in MODELS.values())\\n    ax_b.set_ylim(-0.2, max_k + 0.5)\\n    ax_b.set_yticks(range(max_k + 1))\\n    ax_b.grid(axis=\\\"y\\\", color=\\\"#e0e0e0\\\", linewidth=0.5)\\n    ax_b.set_title(r\\\"$\\\\bf{(b)}$\\\" + r\\\" $K^*(\\\\theta)$ sensitivity\\\", fontsize=10,\\n                   loc=\\\"left\\\", pad=6)\\n\\n    fig.tight_layout()\\n\\n    out_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n    out_path = out_dir / \\\"fig_kstar_theta.pdf\\\"\\n\\n    fig.savefig(out_path, bbox_inches=\\\"tight\\\")\\n    fig.savefig(out_path.with_suffix(\\\".png\\\"), bbox_inches=\\\"tight\\\", dpi=300)\\n    plt.close(fig)\\n\\n    print(f\\\"Models: {list(MODELS.keys())}\\\")\\n    print(f\\\"Saved: {out_path}\\\")\\n    pdf_size = out_path.stat().st_size\\n    assert pdf_size > 3 * 1024, f\\\"PDF too small: {pdf_size}\\\"\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce48959-f444-4b9b-9e96-e8f376b7457f",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "50edd2b6-e9c5-43de-b52a-bed960abc633",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Figure 3: two-panel K*(theta) figure.\\\\n\\\\nPanel (a): Pairwise AUC profile across depth pairs (C4 configs)\\\\nPanel (b): K*(theta) sensitivity\\\\n\\\\nOutput: docs/paper/figures/fig_kstar_theta.pdf\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\nPAIR_KEYS = [\\\\\\\"0v1\\\\\\\", \\\\\\\"1v2\\\\\\\", \\\\\\\"2v3\\\\\\\", \\\\\\\"3v4\\\\\\\", \\\\\\\"4v5\\\\\\\"]\\\\n\\\\nMODELS = {\\\\n    \\\\\\\"Qwen-rw\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9946, 0.6859, 0.5795, 0.5333, 0.5238],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9976, 0.7041, 0.5991, 0.5551, 0.5448],\\\\n    },\\\\n    \\\\\\\"Pythia\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9921, 0.6454, 0.5417, 0.5041, 0.5021],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9943, 0.6630, 0.5628, 0.5260, 0.5249],\\\\n    },\\\\n    \\\\\\\"OLMo\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\\\n    },\\\\n    \\\\\\\"Qwen-cont\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9963, 0.6015, 0.5511, 0.5308, 0.5035],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9978, 0.6213, 0.5712, 0.5508, 0.5255],\\\\n    },\\\\n    \\\\\\\"Qwen-7B\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9610, 0.6080, 0.5390, 0.5180, 0.4990],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9670, 0.6260, 0.5590, 0.5370, 0.5180],\\\\n    },\\\\n}\\\\n\\\\nTABLEAU = [\\\\n    \\\\\\\"#4e79a7\\\\\\\", \\\\\\\"#e15759\\\\\\\", \\\\\\\"#76b7b2\\\\\\\", \\\\\\\"#59a14f\\\\\\\", \\\\\\\"#b07aa1\\\\\\\",\\\\n    \\\\\\\"#ff9da7\\\\\\\", \\\\\\\"#9c755f\\\\\\\", \\\\\\\"#bab0ac\\\\\\\", \\\\\\\"#edc948\\\\\\\", \\\\\\\"#f28e2b\\\\\\\",\\\\n]\\\\nMARKERS = [\\\\\\\"o\\\\\\\", \\\\\\\"s\\\\\\\", \\\\\\\"^\\\\\\\", \\\\\\\"D\\\\\\\", \\\\\\\"v\\\\\\\", \\\\\\\"P\\\\\\\", \\\\\\\"X\\\\\\\", \\\\\\\"*\\\\\\\", \\\\\\\"h\\\\\\\", \\\\\\\"<\\\\\\\"]\\\\n\\\\n\\\\ndef compute_kstar(ci_lowers, theta):\\\\n    k = 0\\\\n    for v in ci_lowers:\\\\n        if v >= theta:\\\\n            k += 1\\\\n        else:\\\\n            break\\\\n    return k\\\\n\\\\n\\\\ndef main():\\\\n    x = np.arange(len(PAIR_KEYS))\\\\n    thetas = np.arange(0.50, 0.751, 0.005)\\\\n\\\\n    plt.rcParams.update({\\\\n        \\\\\\\"font.family\\\\\\\": \\\\\\\"serif\\\\\\\",\\\\n        \\\\\\\"font.size\\\\\\\": 10,\\\\n        \\\\\\\"axes.linewidth\\\\\\\": 0.8,\\\\n        \\\\\\\"xtick.direction\\\\\\\": \\\\\\\"in\\\\\\\",\\\\n        \\\\\\\"ytick.direction\\\\\\\": \\\\\\\"in\\\\\\\",\\\\n        \\\\\\\"xtick.major.width\\\\\\\": 0.8,\\\\n        \\\\\\\"ytick.major.width\\\\\\\": 0.8,\\\\n    })\\\\n\\\\n    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 3.5),\\\\n                                      gridspec_kw={\\\\\\\"width_ratios\\\\\\\": [1, 1.15]})\\\\n\\\\n    # ── Panel (a): Pairwise AUC profile ─────────────────────────────────\\\\n    ax_a.axhline(0.60, color=\\\\\\\"grey\\\\\\\", ls=\\\\\\\"--\\\\\\\", lw=0.8, zorder=1)\\\\n    ax_a.text(4.05, 0.607, r\\\\\\\"$\\\\\\\\theta = 0.60$\\\\\\\", fontsize=8, color=\\\\\\\"grey\\\\\\\",\\\\n              va=\\\\\\\"bottom\\\\\\\", ha=\\\\\\\"right\\\\\\\")\\\\n\\\\n    ax_a.axvspan(1.5, 2.5, color=\\\\\\\"#4e79a7\\\\\\\", alpha=0.06, zorder=0)\\\\n    ax_a.annotate(r\\\\\\\"$K^*\\\\\\\\!=\\\\\\\\!2$\\\\\\\", xy=(1.7, 0.68), fontsize=8, color=\\\\\\\"#4e79a7\\\\\\\",\\\\n                  alpha=0.7)\\\\n\\\\n    for i, (name, data) in enumerate(MODELS.items()):\\\\n        color = TABLEAU[i % len(TABLEAU)]\\\\n        marker = MARKERS[i % len(MARKERS)]\\\\n        means = data[\\\\\\\"mean\\\\\\\"]\\\\n        lo = data[\\\\\\\"ci_lower\\\\\\\"]\\\\n        hi = data[\\\\\\\"ci_upper\\\\\\\"]\\\\n\\\\n        ax_a.fill_between(x, lo, hi, color=color, alpha=0.15, linewidth=0)\\\\n        ax_a.plot(x, means, \\\\\\\"-\\\\\\\", color=color, lw=1.6, marker=marker,\\\\n                  markersize=4.5, label=name, zorder=3)\\\\n\\\\n    ax_a.set_xticks(x)\\\\n    ax_a.set_xticklabels(PAIR_KEYS)\\\\n    ax_a.set_xlabel(\\\\\\\"Depth pair\\\\\\\")\\\\n    ax_a.set_ylabel(\\\\\\\"Pairwise AUC\\\\\\\")\\\\n    ax_a.set_ylim(0.47, 1.02)\\\\n    ax_a.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\\\n    ax_a.legend(fontsize=7.5, loc=\\\\\\\"upper right\\\\\\\", framealpha=0.92,\\\\n                edgecolor=\\\\\\\"0.85\\\\\\\", handlelength=2.0)\\\\n    ax_a.set_title(r\\\\\\\"$\\\\\\\\bf{(a)}$\\\\\\\" + \\\\\\\" Pairwise AUC profile\\\\\\\", fontsize=10,\\\\n                   loc=\\\\\\\"left\\\\\\\", pad=6)\\\\n\\\\n    # ── Panel (b): K*(θ) sensitivity ────────────────────────────────────\\\\n    all_kstar = {}\\\\n    for name, data in MODELS.items():\\\\n        ci_lo = data[\\\\\\\"ci_lower\\\\\\\"]\\\\n        ks = [compute_kstar(ci_lo, t) for t in thetas]\\\\n        all_kstar[name] = ks\\\\n\\\\n    kstar_arr = np.array(list(all_kstar.values()))\\\\n    k_min = kstar_arr.min(axis=0)\\\\n    k_max = kstar_arr.max(axis=0)\\\\n\\\\n    mask_23 = (k_min >= 2) & (k_max <= 3) & (k_min != k_max)\\\\n    mask_2  = (k_min == 2) & (k_max == 2)\\\\n\\\\n    for j in range(len(thetas)):\\\\n        if mask_23[j]:\\\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\\\n                         color=\\\\\\\"#cccccc\\\\\\\", alpha=0.5, linewidth=0, zorder=0)\\\\n        if mask_2[j]:\\\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\\\n                         color=\\\\\\\"#b8d4e3\\\\\\\", alpha=0.5, linewidth=0, zorder=0)\\\\n\\\\n    for i, (name, ks) in enumerate(all_kstar.items()):\\\\n        color = TABLEAU[i % len(TABLEAU)]\\\\n        ax_b.step(thetas, ks, where=\\\\\\\"post\\\\\\\", label=name,\\\\n                  linewidth=1.6, color=color)\\\\n\\\\n    ax_b.axvline(x=0.60, color=\\\\\\\"grey\\\\\\\", ls=\\\\\\\"--\\\\\\\", lw=0.8, alpha=0.7)\\\\n    ax_b.text(0.605, 5.15, r\\\\\\\"$\\\\\\\\theta=0.60$\\\\\\\", color=\\\\\\\"grey\\\\\\\", fontsize=8,\\\\n              va=\\\\\\\"top\\\\\\\")\\\\n\\\\n    import matplotlib.patches as mpatches\\\\n    legend_patches = [\\\\n        mpatches.Patch(color=\\\\\\\"#cccccc\\\\\\\", alpha=0.5, label=r\\\\\\\"$K^*\\\\\\\\!\\\\\\\\in\\\\\\\\!\\\\\\\\{2,3\\\\\\\\}$ (all models)\\\\\\\"),\\\\n        mpatches.Patch(color=\\\\\\\"#b8d4e3\\\\\\\", alpha=0.5, label=r\\\\\\\"$K^*\\\\\\\\!=\\\\\\\\!2$ (all models)\\\\\\\"),\\\\n    ]\\\\n    handles_lines = []\\\\n    for i, name in enumerate(all_kstar.keys()):\\\\n        color = TABLEAU[i % len(TABLEAU)]\\\\n        h = plt.Line2D([0], [0], color=color, lw=1.6, label=name)\\\\n        handles_lines.append(h)\\\\n\\\\n    ax_b.legend(handles=legend_patches + handles_lines, fontsize=7.5,\\\\n                loc=\\\\\\\"upper right\\\\\\\", framealpha=0.92, edgecolor=\\\\\\\"0.85\\\\\\\")\\\\n\\\\n    ax_b.set_xlabel(r\\\\\\\"Threshold $\\\\\\\\theta$\\\\\\\")\\\\n    ax_b.set_ylabel(r\\\\\\\"$K^*(\\\\\\\\theta)$\\\\\\\")\\\\n    ax_b.set_xlim(0.495, 0.755)\\\\n    max_k = max(len(v) for v in MODELS.values())\\\\n    ax_b.set_ylim(-0.2, max_k + 0.5)\\\\n    ax_b.set_yticks(range(max_k + 1))\\\\n    ax_b.grid(axis=\\\\\\\"y\\\\\\\", color=\\\\\\\"#e0e0e0\\\\\\\", linewidth=0.5)\\\\n    ax_b.set_title(r\\\\\\\"$\\\\\\\\bf{(b)}$\\\\\\\" + r\\\\\\\" $K^*(\\\\\\\\theta)$ sensitivity\\\\\\\", fontsize=10,\\\\n                   loc=\\\\\\\"left\\\\\\\", pad=6)\\\\n\\\\n    fig.tight_layout()\\\\n\\\\n    out_dir = Path(__file__).resolve().parent.parent / \\\\\\\"docs\\\\\\\" / \\\\\\\"paper\\\\\\\" / \\\\\\\"figures\\\\\\\"\\\\n    out_dir.mkdir(parents=True, exist_ok=True)\\\\n    out_path = out_dir / \\\\\\\"fig_kstar_theta.pdf\\\\\\\"\\\\n\\\\n    fig.savefig(out_path, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    fig.savefig(out_path.with_suffix(\\\\\\\".png\\\\\\\"), bbox_inches=\\\\\\\"tight\\\\\\\", dpi=300)\\\\n    plt.close(fig)\\\\n\\\\n    print(f\\\\\\\"Models: {list(MODELS.keys())}\\\\\\\")\\\\n    print(f\\\\\\\"Saved: {out_path}\\\\\\\")\\\\n    pdf_size = out_path.stat().st_size\\\\n    assert pdf_size > 3 * 1024, f\\\\\\\"PDF too small: {pdf_size}\\\\\\\"\\\\n    print(\\\\\\\"OK\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Figure 3: two-panel K*(theta) figure.\\n\\nPanel (a): Pairwise AUC profile across depth pairs (C4 configs)\\nPanel (b): K*(theta) sensitivity\\n\\nOutput: docs/paper/figures/fig_kstar_theta.pdf\\n\\\"\\\"\\\"\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nPAIR_KEYS = [\\\"0v1\\\", \\\"1v2\\\", \\\"2v3\\\", \\\"3v4\\\", \\\"4v5\\\"]\\n\\nMODELS = {\\n    \\\"Qwen-rw\\\": {\\n        \\\"mean\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\n        \\\"ci_lower\\\": [0.9946, 0.6859, 0.5795, 0.5333, 0.5238],\\n        \\\"ci_upper\\\": [0.9976, 0.7041, 0.5991, 0.5551, 0.5448],\\n    },\\n    \\\"Pythia\\\": {\\n        \\\"mean\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\n        \\\"ci_lower\\\": [0.9921, 0.6454, 0.5417, 0.5041, 0.5021],\\n        \\\"ci_upper\\\": [0.9943, 0.6630, 0.5628, 0.5260, 0.5249],\\n    },\\n    \\\"OLMo\\\": {\\n        \\\"mean\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\n        \\\"ci_lower\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\n        \\\"ci_upper\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\n    },\\n    \\\"Qwen-cont\\\": {\\n        \\\"mean\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\n        \\\"ci_lower\\\": [0.9963, 0.6015, 0.5511, 0.5308, 0.5035],\\n        \\\"ci_upper\\\": [0.9978, 0.6213, 0.5712, 0.5508, 0.5255],\\n    },\\n    \\\"Qwen-7B\\\": {\\n        \\\"mean\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\n        \\\"ci_lower\\\": [0.9610, 0.6080, 0.5390, 0.5180, 0.4990],\\n        \\\"ci_upper\\\": [0.9670, 0.6260, 0.5590, 0.5370, 0.5180],\\n    },\\n}\\n\\nTABLEAU = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\", \\\"#b07aa1\\\",\\n    \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#bab0ac\\\", \\\"#edc948\\\", \\\"#f28e2b\\\",\\n]\\nMARKERS = [\\\"o\\\", \\\"s\\\", \\\"^\\\", \\\"D\\\", \\\"v\\\", \\\"P\\\", \\\"X\\\", \\\"*\\\", \\\"h\\\", \\\"<\\\"]\\n\\n\\ndef compute_kstar(ci_lowers, theta):\\n    k = 0\\n    for v in ci_lowers:\\n        if v >= theta:\\n            k += 1\\n        else:\\n            break\\n    return k\\n\\n\\ndef main():\\n    x = np.arange(len(PAIR_KEYS))\\n    thetas = np.arange(0.50, 0.751, 0.005)\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.direction\\\": \\\"in\\\",\\n        \\\"ytick.direction\\\": \\\"in\\\",\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 3.5),\\n                                      gridspec_kw={\\\"width_ratios\\\": [1, 1.15]})\\n\\n    # ── Panel (a): Pairwise AUC profile ─────────────────────────────────\\n    ax_a.axhline(0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax_a.text(4.05, 0.607, r\\\"$\\\\theta = 0.60$\\\", fontsize=8, color=\\\"grey\\\",\\n              va=\\\"bottom\\\", ha=\\\"right\\\")\\n\\n    ax_a.axvspan(1.5, 2.5, color=\\\"#4e79a7\\\", alpha=0.06, zorder=0)\\n    ax_a.annotate(r\\\"$K^*\\\\!=\\\\!2$\\\", xy=(1.7, 0.68), fontsize=8, color=\\\"#4e79a7\\\",\\n                  alpha=0.7)\\n\\n    for i, (name, data) in enumerate(MODELS.items()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        marker = MARKERS[i % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n        lo = data[\\\"ci_lower\\\"]\\n        hi = data[\\\"ci_upper\\\"]\\n\\n        ax_a.fill_between(x, lo, hi, color=color, alpha=0.15, linewidth=0)\\n        ax_a.plot(x, means, \\\"-\\\", color=color, lw=1.6, marker=marker,\\n                  markersize=4.5, label=name, zorder=3)\\n\\n    ax_a.set_xticks(x)\\n    ax_a.set_xticklabels(PAIR_KEYS)\\n    ax_a.set_xlabel(\\\"Depth pair\\\")\\n    ax_a.set_ylabel(\\\"Pairwise AUC\\\")\\n    ax_a.set_ylim(0.47, 1.02)\\n    ax_a.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\n    ax_a.legend(fontsize=7.5, loc=\\\"upper right\\\", framealpha=0.92,\\n                edgecolor=\\\"0.85\\\", handlelength=2.0)\\n    ax_a.set_title(r\\\"$\\\\bf{(a)}$\\\" + \\\" Pairwise AUC profile\\\", fontsize=10,\\n                   loc=\\\"left\\\", pad=6)\\n\\n    # ── Panel (b): K*(θ) sensitivity ────────────────────────────────────\\n    all_kstar = {}\\n    for name, data in MODELS.items():\\n        ci_lo = data[\\\"ci_lower\\\"]\\n        ks = [compute_kstar(ci_lo, t) for t in thetas]\\n        all_kstar[name] = ks\\n\\n    kstar_arr = np.array(list(all_kstar.values()))\\n    k_min = kstar_arr.min(axis=0)\\n    k_max = kstar_arr.max(axis=0)\\n\\n    mask_23 = (k_min >= 2) & (k_max <= 3) & (k_min != k_max)\\n    mask_2  = (k_min == 2) & (k_max == 2)\\n\\n    for j in range(len(thetas)):\\n        if mask_23[j]:\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\n                         color=\\\"#cccccc\\\", alpha=0.5, linewidth=0, zorder=0)\\n        if mask_2[j]:\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\n                         color=\\\"#b8d4e3\\\", alpha=0.5, linewidth=0, zorder=0)\\n\\n    for i, (name, ks) in enumerate(all_kstar.items()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        ax_b.step(thetas, ks, where=\\\"post\\\", label=name,\\n                  linewidth=1.6, color=color)\\n\\n    ax_b.axvline(x=0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, alpha=0.7)\\n    ax_b.text(0.605, 5.15, r\\\"$\\\\theta=0.60$\\\", color=\\\"grey\\\", fontsize=8,\\n              va=\\\"top\\\")\\n\\n    import matplotlib.patches as mpatches\\n    legend_patches = [\\n        mpatches.Patch(color=\\\"#cccccc\\\", alpha=0.5, label=r\\\"$K^*\\\\!\\\\in\\\\!\\\\{2,3\\\\}$ (all models)\\\"),\\n        mpatches.Patch(color=\\\"#b8d4e3\\\", alpha=0.5, label=r\\\"$K^*\\\\!=\\\\!2$ (all models)\\\"),\\n    ]\\n    handles_lines = []\\n    for i, name in enumerate(all_kstar.keys()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        h = plt.Line2D([0], [0], color=color, lw=1.6, label=name)\\n        handles_lines.append(h)\\n\\n    ax_b.legend(handles=legend_patches + handles_lines, fontsize=7.5,\\n                loc=\\\"upper right\\\", framealpha=0.92, edgecolor=\\\"0.85\\\")\\n\\n    ax_b.set_xlabel(r\\\"Threshold $\\\\theta$\\\")\\n    ax_b.set_ylabel(r\\\"$K^*(\\\\theta)$\\\")\\n    ax_b.set_xlim(0.495, 0.755)\\n    max_k = max(len(v) for v in MODELS.values())\\n    ax_b.set_ylim(-0.2, max_k + 0.5)\\n    ax_b.set_yticks(range(max_k + 1))\\n    ax_b.grid(axis=\\\"y\\\", color=\\\"#e0e0e0\\\", linewidth=0.5)\\n    ax_b.set_title(r\\\"$\\\\bf{(b)}$\\\" + r\\\" $K^*(\\\\theta)$ sensitivity\\\", fontsize=10,\\n                   loc=\\\"left\\\", pad=6)\\n\\n    fig.tight_layout()\\n\\n    out_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n    out_path = out_dir / \\\"fig_kstar_theta.pdf\\\"\\n\\n    fig.savefig(out_path, bbox_inches=\\\"tight\\\")\\n    fig.savefig(out_path.with_suffix(\\\".png\\\"), bbox_inches=\\\"tight\\\", dpi=300)\\n    plt.close(fig)\\n\\n    print(f\\\"Models: {list(MODELS.keys())}\\\")\\n    print(f\\\"Saved: {out_path}\\\")\\n    pdf_size = out_path.stat().st_size\\n    assert pdf_size > 3 * 1024, f\\\"PDF too small: {pdf_size}\\\"\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  },
  "sourceToolAssistantUUID": "cce48959-f444-4b9b-9e96-e8f376b7457f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-25T19:50:32.303Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01T5PsFBy5TT181dsYcKsmQf`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50edd2b6-e9c5-43de-b52a-bed960abc633",
  "isSidechain": false,
  "requestId": "req_011CbPsK1n2V3xzvVhD8xFkA",
  "type": "assistant",
  "uuid": "61db2708-e3ec-40d4-8797-08919cc6cd45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kaXT38BK3HTZFXbSmJvme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1424,
      "cache_read_input_tokens": 66691,
      "output_tokens": 629,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 629,
          "cache_read_input_tokens": 66691,
          "cache_creation_input_tokens": 1424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1424
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

_source line 83_

```json
{
  "type": "last-prompt",
  "leafUuid": "61db2708-e3ec-40d4-8797-08919cc6cd45",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Runtime record

_source line 84_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit appendix and figure data sources",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1"
}
```

---


### Tool result

_source line 85 · 2026-05-25T19:50:32.768Z_

<details><summary>↩ Tool result · `toolu_01T5PsFBy5TT181dsYcKsmQf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Transfer heatmap v2: K* accuracy + AUC(0v1) for 3-model cross-transfer.\\\"\\\"\\\"\\n\\nimport json\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport matplotlib.patches as mpatches\\nimport numpy as np\\nfrom pathlib import Path\\n\\nROOT = Path(__file__).resolve().parent.parent\\n\\n\\ndef main():\\n    data_path = ROOT / \\\"results\\\" / \\\"exp013_olmo_rerun_v2\\\" / \\\"transfer_matrix.json\\\"\\n    with open(data_path) as f:\\n        data = json.load(f)\\n\\n    models = data[\\\"models\\\"]\\n    self_kstar = data[\\\"self_kstar\\\"]\\n    n = len(models)\\n\\n    auc_matrix = np.zeros((n, n))\\n    kstar_matrix = np.zeros((n, n), dtype=int)\\n    correct_matrix = np.zeros((n, n), dtype=bool)\\n\\n    for i, train_m in enumerate(models):\\n        for j, test_m in enumerate(models):\\n            cell = data[\\\"matrix\\\"][train_m][test_m]\\n            auc_matrix[i, j] = cell[\\\"pairwise_auc\\\"][\\\"0v1\\\"]\\n            kstar_matrix[i, j] = cell[\\\"kstar\\\"]\\n            if i == j:\\n                correct_matrix[i, j] = True\\n            else:\\n                correct_matrix[i, j] = (cell[\\\"kstar\\\"] == self_kstar[test_m])\\n\\n    agg_acc = data[\\\"aggregate_accuracy\\\"]\\n    correct_count = data[\\\"correct\\\"]\\n    total_count = data[\\\"total\\\"]\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.6,\\n        \\\"xtick.major.width\\\": 0.6,\\n        \\\"ytick.major.width\\\": 0.6,\\n        \\\"mathtext.fontset\\\": \\\"cm\\\",\\n    })\\n\\n    fig, ax = plt.subplots(figsize=(3.3, 3.1))\\n\\n    DIAG_COLOR = \\\"#D0D0D0\\\"\\n    CORRECT_COLOR = \\\"#8FCA8F\\\"\\n    INCORRECT_COLOR = \\\"#E8908A\\\"\\n\\n    for i in range(n):\\n        for j in range(n):\\n            if i == j:\\n                color = DIAG_COLOR\\n            elif correct_matrix[i, j]:\\n                color = CORRECT_COLOR\\n            else:\\n                color = INCORRECT_COLOR\\n\\n            rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1,\\n                                 facecolor=color, edgecolor=\\\"white\\\", linewidth=2)\\n            ax.add_patch(rect)\\n\\n            auc_val = auc_matrix[i, j]\\n            ax.text(j, i - 0.13, f\\\"{auc_val:.3f}\\\", ha=\\\"center\\\", va=\\\"center\\\",\\n                    fontsize=10, fontweight=\\\"bold\\\" if i == j else \\\"normal\\\",\\n                    color=\\\"#1a1a1a\\\")\\n\\n            k_pred = kstar_matrix[i, j]\\n            if i == j:\\n                label = r\\\"$K\\\\!^*\\\\!=\\\\!%d$\\\" % k_pred\\n            else:\\n                if correct_matrix[i, j]:\\n                    mark = r\\\"$\\\\checkmark$\\\"\\n                else:\\n                    mark = r\\\"$\\\\times$\\\"\\n                label = r\\\"$K\\\\!^*\\\\!=\\\\!%d$ %s\\\" % (k_pred, mark)\\n\\n            ax.text(j, i + 0.23, label, ha=\\\"center\\\", va=\\\"center\\\",\\n                    fontsize=9, color=\\\"#555555\\\")\\n\\n    ax.set_xlim(-0.5, n - 0.5)\\n    ax.set_ylim(n - 0.5, -0.5)\\n    ax.set_xticks(range(n))\\n    ax.set_xticklabels(models, fontsize=10)\\n    ax.set_yticks(range(n))\\n    ax.set_yticklabels(models, fontsize=10)\\n    ax.set_xlabel(\\\"Test model\\\", fontsize=10, labelpad=4)\\n    ax.set_ylabel(\\\"Train model\\\", fontsize=10, labelpad=4)\\n    ax.tick_params(direction=\\\"in\\\", length=0)\\n    for spine in ax.spines.values():\\n        spine.set_visible(False)\\n\\n    ax.set_title(\\n        r\\\"Cross-model $K\\\\!^*$ transfer  (acc = %d/%d = %.1f%%)\\\"\\n        % (correct_count, total_count, agg_acc * 100),\\n        fontsize=10, pad=8)\\n\\n    legend_patches = [\\n        mpatches.Patch(facecolor=DIAG_COLOR, edgecolor=\\\"#999\\\", linewidth=0.5, label=\\\"Self\\\"),\\n        mpatches.Patch(facecolor=CORRECT_COLOR, edgecolor=\\\"#999\\\", linewidth=0.5, label=\\\"Correct\\\"),\\n        mpatches.Patch(facecolor=INCORRECT_COLOR, edgecolor=\\\"#999\\\", linewidth=0.5, label=\\\"Incorrect\\\"),\\n    ]\\n    ax.legend(handles=legend_patches, loc=\\\"lower center\\\",\\n              bbox_to_anchor=(0.5, -0.30), ncol=3, fontsize=8.5,\\n              frameon=False, handlelength=1.2, handletextpad=0.4,\\n              columnspacing=1.0)\\n\\n    out_dir = ROOT / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n\\n    for suffix in [\\\".pdf\\\", \\\".png\\\"]:\\n        out_path = out_dir / f\\\"fig3_transfer_heatmap{suffix}\\\"\\n        fig.savefig(out_path, dpi=300, bbox_inches=\\\"tight\\\")\\n        size_kb = out_path.stat().st_size / 1024\\n        print(f\\\"Saved: {out_path} ({size_kb:.1f} KB)\\\")\\n\\n    plt.close(fig)\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61db2708-e3ec-40d4-8797-08919cc6cd45",
  "isSidechain": false,
  "promptId": "ca02e7d0-e281-46ee-a0ff-5f844ea17db7",
  "type": "user",
  "uuid": "ab2a42ef-0400-4e5a-b1f6-3ea3dd0b8252",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Transfer heatmap v2: K* accuracy + AUC(0v1) for 3-model cross-transfer.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nimport matplotlib.patches as mpatches\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\nROOT = Path(__file__).resolve().parent.parent\\\\n\\\\n\\\\ndef main():\\\\n    data_path = ROOT / \\\\\\\"results\\\\\\\" / \\\\\\\"exp013_olmo_rerun_v2\\\\\\\" / \\\\\\\"transfer_matrix.json\\\\\\\"\\\\n    with open(data_path) as f:\\\\n        data = json.load(f)\\\\n\\\\n    models = data[\\\\\\\"models\\\\\\\"]\\\\n    self_kstar = data[\\\\\\\"self_kstar\\\\\\\"]\\\\n    n = len(models)\\\\n\\\\n    auc_matrix = np.zeros((n, n))\\\\n    kstar_matrix = np.zeros((n, n), dtype=int)\\\\n    correct_matrix = np.zeros((n, n), dtype=bool)\\\\n\\\\n    for i, train_m in enumerate(models):\\\\n        for j, test_m in enumerate(models):\\\\n            cell = data[\\\\\\\"matrix\\\\\\\"][train_m][test_m]\\\\n            auc_matrix[i, j] = cell[\\\\\\\"pairwise_auc\\\\\\\"][\\\\\\\"0v1\\\\\\\"]\\\\n            kstar_matrix[i, j] = cell[\\\\\\\"kstar\\\\\\\"]\\\\n            if i == j:\\\\n                correct_matrix[i, j] = True\\\\n            else:\\\\n                correct_matrix[i, j] = (cell[\\\\\\\"kstar\\\\\\\"] == self_kstar[test_m])\\\\n\\\\n    agg_acc = data[\\\\\\\"aggregate_accuracy\\\\\\\"]\\\\n    correct_count = data[\\\\\\\"correct\\\\\\\"]\\\\n    total_count = data[\\\\\\\"total\\\\\\\"]\\\\n\\\\n    plt.rcParams.update({\\\\n        \\\\\\\"font.family\\\\\\\": \\\\\\\"serif\\\\\\\",\\\\n        \\\\\\\"font.size\\\\\\\": 10,\\\\n        \\\\\\\"axes.linewidth\\\\\\\": 0.6,\\\\n        \\\\\\\"xtick.major.width\\\\\\\": 0.6,\\\\n        \\\\\\\"ytick.major.width\\\\\\\": 0.6,\\\\n        \\\\\\\"mathtext.fontset\\\\\\\": \\\\\\\"cm\\\\\\\",\\\\n    })\\\\n\\\\n    fig, ax = plt.subplots(figsize=(3.3, 3.1))\\\\n\\\\n    DIAG_COLOR = \\\\\\\"#D0D0D0\\\\\\\"\\\\n    CORRECT_COLOR = \\\\\\\"#8FCA8F\\\\\\\"\\\\n    INCORRECT_COLOR = \\\\\\\"#E8908A\\\\\\\"\\\\n\\\\n    for i in range(n):\\\\n        for j in range(n):\\\\n            if i == j:\\\\n                color = DIAG_COLOR\\\\n            elif correct_matrix[i, j]:\\\\n                color = CORRECT_COLOR\\\\n            else:\\\\n                color = INCORRECT_COLOR\\\\n\\\\n            rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1,\\\\n                                 facecolor=color, edgecolor=\\\\\\\"white\\\\\\\", linewidth=2)\\\\n            ax.add_patch(rect)\\\\n\\\\n            auc_val = auc_matrix[i, j]\\\\n            ax.text(j, i - 0.13, f\\\\\\\"{auc_val:.3f}\\\\\\\", ha=\\\\\\\"center\\\\\\\", va=\\\\\\\"center\\\\\\\",\\\\n                    fontsize=10, fontweight=\\\\\\\"bold\\\\\\\" if i == j else \\\\\\\"normal\\\\\\\",\\\\n                    color=\\\\\\\"#1a1a1a\\\\\\\")\\\\n\\\\n            k_pred = kstar_matrix[i, j]\\\\n            if i == j:\\\\n                label = r\\\\\\\"$K\\\\\\\\!^*\\\\\\\\!=\\\\\\\\!%d$\\\\\\\" % k_pred\\\\n            else:\\\\n                if correct_matrix[i, j]:\\\\n                    mark = r\\\\\\\"$\\\\\\\\checkmark$\\\\\\\"\\\\n                else:\\\\n                    mark = r\\\\\\\"$\\\\\\\\times$\\\\\\\"\\\\n                label = r\\\\\\\"$K\\\\\\\\!^*\\\\\\\\!=\\\\\\\\!%d$ %s\\\\\\\" % (k_pred, mark)\\\\n\\\\n            ax.text(j, i + 0.23, label, ha=\\\\\\\"center\\\\\\\", va=\\\\\\\"center\\\\\\\",\\\\n                    fontsize=9, color=\\\\\\\"#555555\\\\\\\")\\\\n\\\\n    ax.set_xlim(-0.5, n - 0.5)\\\\n    ax.set_ylim(n - 0.5, -0.5)\\\\n    ax.set_xticks(range(n))\\\\n    ax.set_xticklabels(models, fontsize=10)\\\\n    ax.set_yticks(range(n))\\\\n    ax.set_yticklabels(models, fontsize=10)\\\\n    ax.set_xlabel(\\\\\\\"Test model\\\\\\\", fontsize=10, labelpad=4)\\\\n    ax.set_ylabel(\\\\\\\"Train model\\\\\\\", fontsize=10, labelpad=4)\\\\n    ax.tick_params(direction=\\\\\\\"in\\\\\\\", length=0)\\\\n    for spine in ax.spines.values():\\\\n        spine.set_visible(False)\\\\n\\\\n    ax.set_title(\\\\n        r\\\\\\\"Cross-model $K\\\\\\\\!^*$ transfer  (acc = %d/%d = %.1f%%)\\\\\\\"\\\\n        % (correct_count, total_count, agg_acc * 100),\\\\n        fontsize=10, pad=8)\\\\n\\\\n    legend_patches = [\\\\n        mpatches.Patch(facecolor=DIAG_COLOR, edgecolor=\\\\\\\"#999\\\\\\\", linewidth=0.5, label=\\\\\\\"Self\\\\\\\"),\\\\n        mpatches.Patch(facecolor=CORRECT_COLOR, edgecolor=\\\\\\\"#999\\\\\\\", linewidth=0.5, label=\\\\\\\"Correct\\\\\\\"),\\\\n        mpatches.Patch(facecolor=INCORRECT_COLOR, edgecolor=\\\\\\\"#999\\\\\\\", linewidth=0.5, label=\\\\\\\"Incorrect\\\\\\\"),\\\\n    ]\\\\n    ax.legend(handles=legend_patches, loc=\\\\\\\"lower center\\\\\\\",\\\\n              bbox_to_anchor=(0.5, -0.30), ncol=3, fontsize=8.5,\\\\n              frameon=False, handlelength=1.2, handletextpad=0.4,\\\\n              columnspacing=1.0)\\\\n\\\\n    out_dir = ROOT / \\\\\\\"docs\\\\\\\" / \\\\\\\"paper\\\\\\\" / \\\\\\\"figures\\\\\\\"\\\\n    out_dir.mkdir(parents=True, exist_ok=True)\\\\n\\\\n    for suffix in [\\\\\\\".pdf\\\\\\\", \\\\\\\".png\\\\\\\"]:\\\\n        out_path = out_dir / f\\\\\\\"fig3_transfer_heatmap{suffix}\\\\\\\"\\\\n        fig.savefig(out_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n        size_kb = out_path.stat().st_size / 1024\\\\n        print(f\\\\\\\"Saved: {out_path} ({size_kb:.1f} KB)\\\\\\\")\\\\n\\\\n    plt.close(fig)\\\\n    print(\\\\\\\"OK\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Transfer heatmap v2: K* accuracy + AUC(0v1) for 3-model cross-transfer.\\\"\\\"\\\"\\n\\nimport json\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport matplotlib.patches as mpatches\\nimport numpy as np\\nfrom pathlib import Path\\n\\nROOT = Path(__file__).resolve().parent.parent\\n\\n\\ndef main():\\n    data_path = ROOT / \\\"results\\\" / \\\"exp013_olmo_rerun_v2\\\" / \\\"transfer_matrix.json\\\"\\n    with open(data_path) as f:\\n        data = json.load(f)\\n\\n    models = data[\\\"models\\\"]\\n    self_kstar = data[\\\"self_kstar\\\"]\\n    n = len(models)\\n\\n    auc_matrix = np.zeros((n, n))\\n    kstar_matrix = np.zeros((n, n), dtype=int)\\n    correct_matrix = np.zeros((n, n), dtype=bool)\\n\\n    for i, train_m in enumerate(models):\\n        for j, test_m in enumerate(models):\\n            cell = data[\\\"matrix\\\"][train_m][test_m]\\n            auc_matrix[i, j] = cell[\\\"pairwise_auc\\\"][\\\"0v1\\\"]\\n            kstar_matrix[i, j] = cell[\\\"kstar\\\"]\\n            if i == j:\\n                correct_matrix[i, j] = True\\n            else:\\n                correct_matrix[i, j] = (cell[\\\"kstar\\\"] == self_kstar[test_m])\\n\\n    agg_acc = data[\\\"aggregate_accuracy\\\"]\\n    correct_count = data[\\\"correct\\\"]\\n    total_count = data[\\\"total\\\"]\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.6,\\n        \\\"xtick.major.width\\\": 0.6,\\n        \\\"ytick.major.width\\\": 0.6,\\n        \\\"mathtext.fontset\\\": \\\"cm\\\",\\n    })\\n\\n    fig, ax = plt.subplots(figsize=(3.3, 3.1))\\n\\n    DIAG_COLOR = \\\"#D0D0D0\\\"\\n    CORRECT_COLOR = \\\"#8FCA8F\\\"\\n    INCORRECT_COLOR = \\\"#E8908A\\\"\\n\\n    for i in range(n):\\n        for j in range(n):\\n            if i == j:\\n                color = DIAG_COLOR\\n            elif correct_matrix[i, j]:\\n                color = CORRECT_COLOR\\n            else:\\n                color = INCORRECT_COLOR\\n\\n            rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1,\\n                                 facecolor=color, edgecolor=\\\"white\\\", linewidth=2)\\n            ax.add_patch(rect)\\n\\n            auc_val = auc_matrix[i, j]\\n            ax.text(j, i - 0.13, f\\\"{auc_val:.3f}\\\", ha=\\\"center\\\", va=\\\"center\\\",\\n                    fontsize=10, fontweight=\\\"bold\\\" if i == j else \\\"normal\\\",\\n                    color=\\\"#1a1a1a\\\")\\n\\n            k_pred = kstar_matrix[i, j]\\n            if i == j:\\n                label = r\\\"$K\\\\!^*\\\\!=\\\\!%d$\\\" % k_pred\\n            else:\\n                if correct_matrix[i, j]:\\n                    mark = r\\\"$\\\\checkmark$\\\"\\n                else:\\n                    mark = r\\\"$\\\\times$\\\"\\n                label = r\\\"$K\\\\!^*\\\\!=\\\\!%d$ %s\\\" % (k_pred, mark)\\n\\n            ax.text(j, i + 0.23, label, ha=\\\"center\\\", va=\\\"center\\\",\\n                    fontsize=9, color=\\\"#555555\\\")\\n\\n    ax.set_xlim(-0.5, n - 0.5)\\n    ax.set_ylim(n - 0.5, -0.5)\\n    ax.set_xticks(range(n))\\n    ax.set_xticklabels(models, fontsize=10)\\n    ax.set_yticks(range(n))\\n    ax.set_yticklabels(models, fontsize=10)\\n    ax.set_xlabel(\\\"Test model\\\", fontsize=10, labelpad=4)\\n    ax.set_ylabel(\\\"Train model\\\", fontsize=10, labelpad=4)\\n    ax.tick_params(direction=\\\"in\\\", length=0)\\n    for spine in ax.spines.values():\\n        spine.set_visible(False)\\n\\n    ax.set_title(\\n        r\\\"Cross-model $K\\\\!^*$ transfer  (acc = %d/%d = %.1f%%)\\\"\\n        % (correct_count, total_count, agg_acc * 100),\\n        fontsize=10, pad=8)\\n\\n    legend_patches = [\\n        mpatches.Patch(facecolor=DIAG_COLOR, edgecolor=\\\"#999\\\", linewidth=0.5, label=\\\"Self\\\"),\\n        mpatches.Patch(facecolor=CORRECT_COLOR, edgecolor=\\\"#999\\\", linewidth=0.5, label=\\\"Correct\\\"),\\n        mpatches.Patch(facecolor=INCORRECT_COLOR, edgecolor=\\\"#999\\\", linewidth=0.5, label=\\\"Incorrect\\\"),\\n    ]\\n    ax.legend(handles=legend_patches, loc=\\\"lower center\\\",\\n              bbox_to_anchor=(0.5, -0.30), ncol=3, fontsize=8.5,\\n              frameon=False, handlelength=1.2, handletextpad=0.4,\\n              columnspacing=1.0)\\n\\n    out_dir = ROOT / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n\\n    for suffix in [\\\".pdf\\\", \\\".png\\\"]:\\n        out_path = out_dir / f\\\"fig3_transfer_heatmap{suffix}\\\"\\n        fig.savefig(out_path, dpi=300, bbox_inches=\\\"tight\\\")\\n        size_kb = out_path.stat().st_size / 1024\\n        print(f\\\"Saved: {out_path} ({size_kb:.1f} KB)\\\")\\n\\n    plt.close(fig)\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  },
  "sourceToolAssistantUUID": "61db2708-e3ec-40d4-8797-08919cc6cd45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 86 · 2026-05-25T19:50:32.773Z_

```json
{
  "parentUuid": "ab2a42ef-0400-4e5a-b1f6-3ea3dd0b8252",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "aae45e12-1cac-4a36-a93c-19d029d8618b",
  "timestamp": "2026-05-25T19:50:32.773Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 87 · 2026-05-25T19:57:49.188Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the figure generation scripts. Let me analyze each one:

1. **plot_fig2_merged.py** (→ fig2_auc_decay.pdf): **HARDCODED DATA** - All AUC values are embedded directly in the script (TABLE1, EXTRA_MODELS, DECODE_FOLD dicts). No data files read.

2. **plot_fig_jsd_decay.py** (→ fig_jsd_decay.pdf): **HARDCODED DATA** - All JSD values are embedded directly (c4_k2, mistral_c4, arxiv_pythia, retrain_chain dicts). No data files read.
   
3. **plot_filtering_strategies.py** (→ fig_filtering_strategies.pdf): **PARTIALLY HARDCODED** - Has embedded filtering results with fallback logic that checks for JSON files first, but defaults to hardcoded values like "No filter" = 0.5867, "DSIR" = 0.5867, "Surprisal" = 0.5894, "Graduated" = 0.5892, "Binary K*" = 0.5941.

4. **draw_kstar_theta.py** (→ fig_kstar_theta.pdf): **HARDCODED DATA** - All AUC values and confidence intervals are embedded directly in the script.

5. **transfer_heatmap_v2.py** (→ fig3_transfer_heatmap.pdf): **READS DATA FILE** - Loads transfer_matrix.json from results/exp013_olmo_rerun_v2/, making it the only script that actually reads from disk.

Now I need to verify whether the transfer matrix file exists on the server, track down where the pipeline figure comes from, and cross-check the hardcoded numbers against the actual registry values. I'm also noticing a potential issue with plot_fig2_merged.py where the Pythia table uses self-scored values instead of the Q-scored values that appear in the paper's supplementary tables.

Looking more closely at the discrepancy: the figure script has Pythia 1v2 = 0.6539 (self-scored from exp_007_bootstrap_ci), but the paper's Table S8 shows 0.607 [0.598, 0.617] for the same comparison. This is a significant mismatch that needs clarification—either the figure is using outdated values or there's a fundamental inconsistency between what the paper reports and what the visualization displays. I'm noticing a key inconsistency: the extended table in the appendix shows Pythia's 1v2 score as .6074 with Qwen cross-scoring, but the figure uses 0.6539 from self-scoring. This suggests the figure might intentionally display each model's self-scored performance while the tables present cross-scored comparisons, though I need to verify whether this distinction is deliberate or an oversight.

Looking more closely at the figure script, I'm finding that the values don't align cleanly with either the self-scored or Qwen-scored registry entries—OLMo's 0.5079 in the figure falls between its self-scored 0.6145 and Qwen-scored 0.5001, which suggests there may be a third scoring source or calculation method I'm missing. I'm noticing the figure shows OLMo 1v2=0.5079 with CI [0.4908, 0.5251], but the appendix tables report 0.500 with CI [0.496, 0.519]—the confidence intervals overlap but the point estimates diverge, suggesting they might be using different scorers or bootstrap procedures. Let me trace back through the figure script to see what's actually being plotted.

For Pythia, there's a clear discrepancy: the appendix tables show 1v2=0.6074 when Qwen-scored, but the figure shows 0.6539 when self-scored—these are definitely different values for the same model. I need to check the figure caption and main text to understand which scorer the figure is supposed to use, and whether the figure script comments about Table 1 models and cross-fold CV explain this difference.

Looking at the other models in the figure, Qwen-cont's 1v2=0.6112 matches the registry, suggesting it uses self-scoring. For OLMo, the 0v1=0.9860 aligns with the Qwen-scored value, but the 1v2=0.5079 doesn't quite match the Qwen-scored 0.5001—this might indicate a different experimental run or an OLMo rerun. I should check the draw_kstar_theta.py script to see what data it's actually pulling, since it has overlapping values like Pythia's self-scored means. Looking at the OLMo self-scored value of 0.6145 versus the figure's 0.5079, there's a clear mismatch — the figure appears to be showing Qwen-scored results instead, though with wider confidence intervals than expected. The Pythia discrepancy is more concerning though: 0.6539 in the figure versus 0.6074 in the table is a much larger gap that suggests either different data sources or a calculation error. I'm wondering if the figures intentionally display self-scored results while the tables show something else, or if there's been a data inconsistency I need to track down. Looking at the actual data from the plotting script, I can see the discrepancies now — Pythia's figure values come from self-scored results rather than cross-scored, while OLMo's values don't match the table exactly, suggesting it might be using a different bootstrap sample or an earlier run.

For the filtering experiment, the embedded values in the code differ slightly from what's in the registry, which could mean the figure is pulling from a separate JSON file if one exists. And checking the JSD values against the registry shows similar small mismatches that I need to trace back to their source.

Looking at the JSD data more closely, the figure shows Qwen-1.5B with values like 0.163726 and 0.010810, but the registry entry for mvp_pilot_sat_v1 has completely different numbers like 0.2669 and 0.0163. The model names might not be matching up exactly—the registry has Qwen2.5-1.5B-Instruct while the figure just says Qwen-1.5B—so these could be different experiments entirely, or there might be multiple ways the JSD is being calculated.

Let me check if the pipeline.pdf figure has a generation script and look at experiments_c1.tex to understand what's actually being plotted.

I've found enough to start documenting the audit. The main issues are clear: fig2_auc_decay.pdf has hardcoded values that don't match the registry data (Pythia 1v2 shows 0.6539 in the figure but 0.6074 in the table, OLMo 1v2 shows 0.5079 versus 0.5001), and fig_jsd_decay.pdf also has hardcoded JSD values that don't align with the pairwise_jsd values in the registry. Now I'm checking the appendix table values against what's in the registry—the top_features section lists Spearman correlations of 0.95, 0.91, and 0.85 for different model pairs, but I need to verify these match the cross-model comparisons recorded in the experiments rather than the cross-scorer correlations that are also documented.

Looking at the transfer accuracy matrix in the appendix, the self-accuracy values for each model are closely matching the registry entries when rounded—Qwen-rw at 0.423 versus 0.4229, Pythia at 0.386 versus 0.3856, OLMo at 0.382 versus 0.3822, and Qwen-cont at 0.388 versus 0.3875.

The off-diagonal transfer values show Qwen-rw transferring to Pythia at 0.259, to OLMo at 0.265, and to Qwen-cont at 0.347, though I'd need the full transfer matrix from the registry to verify these since the experiment only provides aggregated retention percentages.

Now looking at the dataset statistics—there are 5,000 samples per depth level for 30,000 total, with a mean token count of 147.8 at depth 0. This is interesting because it differs from the token length table which shows 191 tokens for Qwen-rw at the same depth, suggesting these might be measuring different aspects of the data.

The discrepancy makes sense once I account for the tokenization method—the dataset stats use whitespace tokenization while the token length table uses subword tokenization, explaining why 147.8 whitespace tokens corresponds to 191 subword tokens.

Now checking the decoding ablation results from the registry against the table values. The greedy decoding config shows 0v1 accuracy of 0.9796 which rounds to 0.980, and 1v2 accuracy of 0.6892 rounding to 0.689—both match the table. Moving to the nucleus sampling config with p=0.9, the registry shows 0v1 at 0.9945 and 1v2 at 0.6862, which I need to verify against the table values.

The 0v1 value rounds correctly to 0.995, and the confidence interval upper bound of 0.9956 rounds to 0.996 as shown in the table. However, there's a minor rounding inconsistency with the 1v2 metric—0.6862 should round down to 0.686, but the table displays 0.687 instead.

Now I'm checking the next configuration. The 0v1 value of 0.9877 rounds correctly to 0.988, and the 1v2 value of 0.6885 is right on the boundary—it could round to either 0.688 or 0.689 depending on the rounding method used, though the table shows 0.689.

For config4_t12, both values check out: 0.9982 rounds to 0.998 and 0.7037 rounds to 0.704. Now I'm looking at the cross-configuration Spearman correlations to see how different methods compare to each other—Greedy shows strong agreement with T=0.7 at 0.914 but weaker agreement with T=1.2 at 0.532, while the nucleotide method at p=0.9 correlates highly with T=1.2 at 0.893.

The T=0.7 vs T=1.2 correlation of 0.668 isn't directly in the registry, so I'd need to pull that from the raw experiment outputs. Moving to the extended K* confidence interval table, I'm spot-checking several entries across different models—Qwen-rw, Pythia, and OLMo all match between the registry and table values, including the confidence intervals for the 1v2 comparisons.

But I'm noticing Qwen-base appears in the table with a 1v2 value of 0.626[0.617,0.635], and I can't find a corresponding experiment in the registry for it—it might exist as a separate entry I haven't located yet.

Now checking the LLaMA-8B results: the registry shows a 0v1 confidence interval of [0.9174, 0.9272], and the extended table lists 0.9224, which aligns with the bootstrap mean—essentially the same value. The 1v2 comparison checks out at 0.6123 across both sources. Moving on to verify Mistral-7B next.

For Mistral-7B 0v1, I'm seeing a major discrepancy: the extended table shows 0.9209 with CI [0.919, 0.923], but plot_fig2_merged.py reports 0.9843—these are drastically different values and I need to figure out which source is correct. I'm noticing the figure script defines Mistral-7B with a mean of 0.9843 for the first metric, but I need to figure out which scoring method this corresponds to and why it differs so much from the 0.9209 value in the extended table. So the figure displays self-scored values for Mistral (1v2=0.5935, 0v1=0.9843), while the extended table shows cross-scored values (1v2=0.5695, 0v1=0.9209) — they're measuring different things, which explains the discrepancy.

Now looking at Pythia and OLMo, the figure shows 1v2=0.6539 for Pythia but the extended table has 0.6074, and for OLMo the figure shows 0.5079 which doesn't match either the self-scored value of 0.6145 or the Qwen cross-scored 0.5001. There might be a separate OLMo rerun that's creating this mismatch. Looking at the bootstrap results in the extended table, OLMo shows 1v2=.500 with confidence intervals [.496,.519], but the figure displays .5079 with wider intervals [.4908,.5251]—suggesting they might be using different bootstrap configurations or sample sizes. There's a clear discrepancy between the figure value (.5079) and what's documented in the table (.500/.5001).

Now examining the filtering figure results across different filtering methods to see how they compare. Now I'm noticing the standard deviation values are roughly twice as large in the embedded data compared to the registry — the ratio is around 2, which suggests they might be measuring different things. If there are 5 seeds, the relationship between standard deviation and standard error would be std/√5 ≈ sem, so the embedded data could be reporting raw standard deviation while the registry reports standard error or vice versa.

The mean values themselves show only minor differences (0.5867 vs 0.5865), but I need to check what the paper's discussion actually references in the figure and whether those values align with the embedded data.

Now I'm going through the appendix to verify those numbers against the registry. For the extended discussion section, I'm checking claims like the decoding strategy's effect on signal strength—the 1v2 AUC range of [0.6862, 0.7037] matches what I'm finding in the registry data. I should continue spot-checking the cross-model comparisons and then compile my findings into a report. The 89-92% range for Pythia↔OLMo is actually correct when I calculate it from the raw matrix values, so the paper's numbers check out even though the registry shows 91-92%. Now I'm looking at the Qwen-7B metrics in the extended neural probe section. Looking at the Gemma-2-27B results, there's a tiny discrepancy between the paper's reported 0.5894 and the registry's 0.5895—just a rounding difference. The Gemma-2-2B at 5K checkpoint matches perfectly at 0.5981. For the neural probe analysis, I'm verifying the K* values: Qwen shows K*=3, Pythia shows K*=2, and OLMo shows K*=1 with a 1v2 AUC of 0.5054, all confirmed in the registry.

Now checking the zero-shot LLM results. GPT-5.5 achieved 33.2% accuracy with an MAE of 1.10 across 500 samples, which aligns with the registry values. Claude Opus 4.6 came in at 33.1% accuracy with an MAE of 1.15, and the sample count shows 499 valid responses after filtering out one invalid entry. Moving on to verify the OBD-LightGBM results.

For the practical considerations section, I'm cross-referencing the MMLU and HellaSwag performance drops. The base model MMLU score of 0.6018 drops to a range of 0.5865–0.5941 depending on the filtering approach, and HellaSwag similarly declines from 0.6821 to 0.6631–0.6701, all matching the registry values from the experiments. Now I'm verifying the MMLU degradation calculations—the binary filtering approach reduces the performance drop from 1.53 percentage points down to 0.77 percentage points, which works out to roughly a 50% improvement. For the retraining chain experiment, I'm checking the pairwise AUC scores across different generation comparisons, and all three values match what's reported in the registry.

Looking at the threshold sensitivity analysis, I need to verify how the K* values shift as I adjust θ—at 0.55, both Qwen variants show K*=3 since their 2v3 AUC scores exceed that threshold, but at 0.70 the picture changes and K* drops to 1 across configurations, though I should double-check whether the confidence interval bounds affect this conclusion for Qwen-rewrite.

For token stability across depths 1–5, the data confirms mean counts stay tightly clustered—Qwen-rewrite ranges only 2 tokens, Pythia maxes out at 4, and Qwen-continuation shows slightly more variation at 6 tokens. Now I'm examining the dose-response patterns to see how performance scales with different parameter counts. Now I'm verifying the 50% dose results match the registry, and checking the statistical comparisons—the binary approach outperforms no-filter by 0.21 percentage points at 10% dosage with p=0.001, while at 30% the improvement is 0.13 percentage points but the p-value isn't recorded in the registry.

Moving to seed robustness, I'm examining how different random seeds affect model behavior across configurations: Pythia-1.4B on Wikipedia stays consistent at K*=1 regardless of seed with minimal variation, while Qwen-1.5B shows more sensitivity—it maintains K*=2 on C4 across both seeds but shifts to K*=3 on Wikipedia when using seed 123.

Now checking the registry entries for these seed variants—they're marked as completed but the metrics aren't showing up, so I'll need to cross-reference against the actual experiment output files to verify the values.

For the Bonferroni correction, I'm confirming the critical z-value of 2.807 for α/2 = 0.0025 to achieve 99.5% confidence intervals, and spot-checking the Qwen-rw results where the 1v2 difference of 0.6955 with bootstrap standard error of 0.0046 produces a CI of [0.683, 0.708] that passes validation.

Now I'm verifying the remaining model comparisons—Pythia, LLaMA, and Qwen-cont—by recalculating their confidence intervals from the point estimates and standard errors to confirm they match the reported table values. Now I'm verifying the 10K robustness results by cross-checking the registry values against the reported metrics—Pythia-1.4B shows consistent K*=2 selection across both 5K and 10K runs with the expected AUC shifts, and Qwen-1.5B cont on C4 also matches the documented K*=2 configuration. The OLMo-1B results check out across both dataset sizes, and Gemma-2-2B shows a clear shift in optimal K* from 1 to 2 as we move from 5K to 10K tokens. Now I'm verifying the bootstrap stability analysis, which shows that most model configurations maintain consistent K* values across resamples. I'm seeing that only 7 configurations actually hit exactly 100%, with LLaMA-8B C4 at 99.9% — so the claim of "eight of ten" seems to rely on rounding that borderline case up. Then looking at the computational costs, the scorer takes about 20.6 milliseconds, feature extraction around 23.4 milliseconds, and LightGBM is nearly instantaneous at 0.74 milliseconds, totaling roughly 44.7 milliseconds per operation.

Now I'm checking the DeBERTa results against the paper's claims. The C4 dataset shows OBD achieving a boundary AUC of 0.626 while DeBERTa reaches 0.705, and I can cross-reference this with the registry experiment which reports similar numbers — 0.6262 for the baseline and 0.7052 for DeBERTa.

For the arXiv dataset, the paper reports OBD at K*=3 with a boundary AUC of 0.643, while DeBERTa achieves 0.624 at K*=4. The registry data confirms the DeBERTa result of 0.6238, which rounds to 0.624.

Now looking at the Code dataset results: OBD reaches a boundary AUC of 0.738 at K*=2, and DeBERTa gets 0.808 at the same K*. Both values match what's in the table.

Moving on to the Gemma-27B transfer experiments, I'm checking the transfer performance metrics across different target models.

For the reverse direction (small models to 27B), I'm noticing a discrepancy—the individual model scores average to 80.4%, but the table shows 76.5%. Let me figure out where this mismatch is coming from. the average is computed differently, perhaps weighted or using different metrics. Or maybe there's an error in the table values.

Actually wait, let me re-check. The table only shows one value per row for Small→27B:
- LLaMA: 92.1%
- Qwen-1.5B: 71.3%
- Pythia: 80.9%
- OLMo: 77.3%

Average: (92.1+71.3+80.9+77.3)/4 = 80.4%

But the table bottom row says "Small→27B avg: 76.5%". This is a DISCREPANCY. 80.4% ≠ 76.5%.

The registry says 76.5% which matches the table, but the individual values don't add up. Either some individual values are wrong, or the average is computed with different values that aren't shown. There might be a fifth model not displayed, or they're using a different calculation method like geometric mean or accuracy retention instead of AUC retention.

Now looking at the Gemma-27B filtering results, I see the baseline performance metrics and how the different filtering approaches affect them—the binary approach shows modest improvements while the graduated approach shows a slight dip on one metric.

For the arXiv multi-source data, I need to verify the K*=3 values against the registry to see if there are any inconsistencies there as well.

Now I'm looking at the cross-scorer table results, comparing performance metrics across different model pairs like Pythia and OLMo paired with Qwen variants, tracking their K* values and AUC scores across different classification thresholds. Looking at the cross-scorer results for OLMo variants, the arXiv version shows K*=1 with a non-significant AUC of 0.500, which matches the registry entry. However, the OLMo-Code results show K*=1 with AUC=0.557, but I'm not finding a direct registry match for this—it might be from a separate experiment or there could be a mismatch between the table and registry data. Now I'm verifying the confusion matrices from the appendix against the registry values. The GPT-5.5 results check out—accuracy of 0.332 and MAE of 1.102 match what I have recorded, and the per-class recall values align with the matrix rows.

For Claude's matrix, the accuracy of 0.331 and MAE of 1.15 are confirmed, but I'm noticing that with N=499 total samples, one class only has 99 entries instead of the expected 100, which explains the slightly different sample distribution. 10/99 = 0.10101..., which should round to 0.101 at three decimal places, but the table shows 0.100 — looks like a minor rounding inconsistency there. The registry correctly has d3=0.101. For d4, I get 37/100=0.370, which checks out. Overall accuracy across all depths is 165/499=0.331, matching the expected value.

Now looking at the s3c_perdepth tab, I see OBD has d0=96 and d1=39.

Continuing with the remaining depths, I'm adding up the per-depth values: 96+39+14+19+22=190. If these represent percentages of 100 samples each, the overall accuracy should be 190/500=38.0%, but the registry shows 0.386. There's a discrepancy here — either the individual depth values have some rounding involved, or there's a slight mismatch in how they're being calculated. There's a discrepancy here—the per-depth recalls sum to 190, giving 38.0% accuracy, but the reported value is 38.6%. This could mean either the table values are slightly rounded or there's a mismatch in how the classes are being counted. Let me check if OBD might be evaluated differently across the experiments, since the main results use 6 depth classes while the LLM baselines use 5. Hmm, but the LLM zero-shot section says "comparable to OBD-LightGBM's 38.6% (95% CI: [0.340, 0.422])". The CI [0.340, 0.422] covers 38.0%, so maybe the point estimate 38.6% comes from a slightly different evaluation (perhaps not the same test subset). But the per-depth recalls in tab:s3c_perdepth imply 38.0%, not 38.6%.

OK, this is another small discrepancy.

Actually, wait. Let me reconsider. Maybe the recall values are rounded to integer percentages in the table, but the actual values give 38.6%. For example, if d0 recall is 96.0%, that's 96 correct out of 100, and d1 recall is 39.4%, that's 39 correct rounded from 39.4. But with 100 samples per class, recall values should be exact integers—39 correct out of 100 is exactly 39%, not 39.4%. So either the recalls are exact, or the sample count per depth isn't exactly 100. In any case, the 0.6 percentage point discrepancy between 38.0% and 38.6% is worth noting.

Now I'm checking the Pythia decoding results from the registry against the table values to verify they match. Now I'm checking the t12 results against the table values with T=1.2, and all the rounded comparisons match up correctly. I'm also verifying that the greedy mechanism triggers the expected repetition collapse pattern where d0 transitions to d1 at 0.72, which aligns with the footnote in the table.

Moving into the length ablation experiments, I'm seeing consistent K* values of 2 across different sequence lengths, with the 1v2 scores ranging from about 0.607 to 0.628, and these all round correctly to the table values. The 0v1 metrics show increasing performance with longer sequences but I can't cross-reference those from the registry data available.

For the domain ablation, the C4 results align with the Qwen-cont baseline from the main experiment, and I'm starting to verify the arXiv results where the 1v2 score is 0.858.

Wait, I'm noticing something odd here—the table caption says "Qwen-cont" but the actual registry experiment uses the base model, not the Instruct variant. Let me figure out if this is a labeling issue or if there's a real discrepancy between what the table claims and what the experiment actually ran. The C4 value of .611 matches the Qwen-Instruct continuation results perfectly, but the registry shows exp_024 uses the base model instead. I'm wondering if there are separate arXiv experiments for each variant, or if there's a mislabeling somewhere—the .858 arXiv value aligns with exp_024's results, which suggests the table might be showing base model results despite the "Qwen-cont" label.

Now looking at the scorer sensitivity table, I'm checking how different models respond when paired with different scorers. The Qwen-Instruct rewrite shows consistent agreement across all three scorers, which matches the registry. The continuation variant shows disagreement between self-scoring and cross-scoring, and that also aligns with what's recorded. For the base model, I see consistent agreement again, though I need to verify the full set of cross-scorer combinations in the registry.

Pythia maintains K*=2 across all conditions, both self and cross-scored, which checks out. But OLMo is creating some confusion—the table shows self-scored K*=1, yet the registry experiment notes a different result with K*=2 for the 1v2 comparison, and then K*=1 when Qwen-scored it. There's a discrepancy I need to resolve here.

Looking deeper, there was apparently an OLMo rerun that produced different results, and the registry is referencing those updated values where the self-probe gave K*=1. So the table's Self=1 for OLMo likely reflects this rerun data, not the original experiment. K*=1 makes sense. But wait, that interpretation breaks down when I look at Pythia—both Qwen-scored and self-scored give K*=2, yet the table shows Self=2 for Pythia. For OLMo, if "Self" means Qwen-scored, then K*=1 matches the table, but that's a confusing column name. Looking at the headers more carefully, "Self" likely means "scored by itself," so I need to reconsider what each column actually represents.

If "Self" means the model scoring itself, then for OLMo the self-scored result should be K*=2, but the table shows K*=1—that's inconsistent. Unless "Self" actually means "scored by the default scorer (Qwen)," which would make OLMo Self = K*=1 correct. But then for Pythia, both Qwen-scored and Pythia-scored give K*=2, so they'd both show the same value anyway.

Looking more carefully at the table structure, the columns after "Self" are labeled "Pythia" and "OLMo," indicating those are the scorers. So "Self" should mean the model scores itself. The registry shows OLMo self-scored at K*=2, but the appendix table shows K*=1—there's a real discrepancy here, though the broader discussion suggests scorer sensitivity mainly affects Qwen models.

Now I'm checking whether the OLMo values might have changed after a rerun. The figure script uses different values than what I'd expect from the registry, and the cross-scorer table shows "self" means the generator and scorer are the same model. For OLMo specifically, I need to figure out which values are actually being used.

Looking at the ANOVA results for the cross-scorer analysis...

the sample size calculation checks out at 300 observations, but I'm trying to verify the factor levels match the design—there should be 3 generators, 4 scorers, and 5 depth-pairs to get those degrees of freedom, though the generator count seems off based on what I'm seeing in the cross-scorer table. I'm realizing there's likely a three-way interaction term between generator, scorer, and depth that accounts for 24 degrees of freedom, which means the residual of 240 is actually 264 minus that interaction term—so the model is using the three-way interaction as the error term, which is a valid ANOVA setup. Now let me move forward with the analysis.

The pipeline diagram appears to be a conceptual illustration rather than a generated figure, so there's no underlying script to track. I'm also noticing several figure files in the directory that aren't referenced anywhere in the manuscript—theta sensitivity, feature ablation, power curves, retraining decay, and various feature importance plots—which suggests these might be leftover from earlier analyses or alternative approaches that didn't make it into the final write-up.

More importantly, I'm catching a discrepancy: the AUC decay figure uses self-scored Pythia values while the extended table uses Qwen-scored values, which means the figure and tables are actually showing different numbers for the same model. I need to check the figure captions in the main text to see if this inconsistency is acknowledged or if it's an oversight.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aae45e12-1cac-4a36-a93c-19d029d8618b",
  "isSidechain": false,
  "requestId": "req_011CbPsKdRQBwUB5BLM7Kj78",
  "type": "assistant",
  "uuid": "808e27bb-4da8-495a-9a41-5e599b2b3164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019X4z95PgMqwVMeqtk6cRLv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15984,
      "cache_read_input_tokens": 68115,
      "output_tokens": 22561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22561,
          "cache_read_input_tokens": 68115,
          "cache_creation_input_tokens": 15984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15984
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

_source line 88 · 2026-05-25T19:57:49.190Z_

Let me check the main text to understand what scorer the figure claims to use, and verify the transfer matrix JSON exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "808e27bb-4da8-495a-9a41-5e599b2b3164",
  "isSidechain": false,
  "requestId": "req_011CbPsKdRQBwUB5BLM7Kj78",
  "type": "assistant",
  "uuid": "7734b6a3-af6a-4fa5-8a0d-56a4421890ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019X4z95PgMqwVMeqtk6cRLv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15984,
      "cache_read_input_tokens": 68115,
      "output_tokens": 22561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22561,
          "cache_read_input_tokens": 68115,
          "cache_creation_input_tokens": 15984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15984
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

_source line 89 · 2026-05-25T19:57:49.468Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DJTa1z6HYsYy2kBjMFp2SC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7734b6a3-af6a-4fa5-8a0d-56a4421890ed",
  "isSidechain": false,
  "requestId": "req_011CbPsKdRQBwUB5BLM7Kj78",
  "type": "assistant",
  "uuid": "b5827637-b1bb-4c14-893d-1f251081441f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "93bdb0df-e478-43c2-a08d-406b4a0808e1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019X4z95PgMqwVMeqtk6cRLv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15984,
      "cache_read_input_tokens": 68115,
      "output_tokens": 22561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22561,
          "cache_read_input_tokens": 68115,
          "cache_creation_input_tokens": 15984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15984
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
