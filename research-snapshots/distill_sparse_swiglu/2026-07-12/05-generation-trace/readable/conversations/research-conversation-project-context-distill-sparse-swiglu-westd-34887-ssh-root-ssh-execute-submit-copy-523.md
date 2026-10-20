# Research conversation: <project_context> # 项目: distill_sparse_swiglu ## 运行环境 - 服务器名: westd-34887 - SSH 账户: root（调用 ssh_execute / submit_trainin

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9.jsonl`
- **Structured JSON:** [`7ca1c18348bd985b91b7.json`](../../sessions/7c/7ca1c18348bd985b91b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T09:39:56.422Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T09:39:56.422Z",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "content": "&lt;project_context>\n# 项目: distill_sparse_swiglu\n\n## 运行环境\n- 服务器名: westd-34887\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/distill_sparse_swiglu/\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 只允许使用 westd-34887 的 cuda:0 和 cuda:1，禁止使用其他 GPU（原因：项目分配 GPU 为 RTX PRO 6000 Blackwell × 2，Reviewer 要求配置 GPU 边界以满足 L1 红线 #4） [来自 D001]\n- **C002**: 所有 GPU 长时间实验必须用 nohup 启动并重定向日志，禁止裸 tmux session（原因：bce_isocompute_s42 和 v2 两次因 tmux session 被挤掉而死，导致 Reviewer Concern #2 完全无防御数据）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：从 literature_map.yaml 生成 references.bib\n\n读取 `literature_map.yaml` 中所有条目，为每篇论文生成一个 BibTeX entry，写入 `references.bib`。\n\n### 输入\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml`\n\n### 输出\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib`\n\n### BibTeX key 命名规则\n- 格式：`{第一作者姓小写}{年份}{关键词}`\n- 例如：`liu2025teal`, `liu2023dejavu`, `xu2026spon`, `jang2017gumbel`, `shazeer2020glu`\n\n### 每个条目格式\n```bibtex\n@article{key,\n  title = {论文标题},\n  author = {Author1 and Author2 and Author3},\n  year = {年份},\n  journal = {venue 或 arXiv preprint arXiv:XXXX.XXXXX},\n  url = {https://arxiv.org/abs/XXXX.XXXXX},  % 如果有 arxiv_id\n}\n```\n- 有明确 venue（如 ICML 2023, NeurIPS 2024, ICLR 2025 等）→ 用 `@inproceedings` + `booktitle`\n- 只有 arXiv → 用 `@article` + `journal = {arXiv preprint arXiv:XXXX.XXXXX}`\n\n### 注意事项\n- 所有条目都视为 verified（literature_map 中的都是人工确认的）\n- 作者列表用 \"and\" 连接\n- 如果 authors 为空列表 `[]`，写 `author = {Unknown}`\n- 确保无重复 key\n- 按 category 分组，用注释分隔\n\n### 操作步骤\n1. Read literature_map.yaml\n2. 解析所有条目（约 30 篇）\n3. 为每篇生成 BibTeX entry\n4. Write 到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib`\n5. 验证文件已写入"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T09:39:56.426Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T09:39:56.426Z",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9"
}
```

---

## Round 1

20 recorded events

### User

_source line 3 · 2026-05-16T09:39:56.491Z_

&lt;project_context>
# 项目: distill_sparse_swiglu

## 运行环境
- 服务器名: westd-34887
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/distill_sparse_swiglu/

## ⚠️ 活跃约束（必须遵守）

- **C001**: 只允许使用 westd-34887 的 cuda:0 和 cuda:1，禁止使用其他 GPU（原因：项目分配 GPU 为 RTX PRO 6000 Blackwell × 2，Reviewer 要求配置 GPU 边界以满足 L1 红线 #4） [来自 D001]
- **C002**: 所有 GPU 长时间实验必须用 nohup 启动并重定向日志，禁止裸 tmux session（原因：bce_isocompute_s42 和 v2 两次因 tmux session 被挤掉而死，导致 Reviewer Concern #2 完全无防御数据）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：从 literature_map.yaml 生成 references.bib

读取 `literature_map.yaml` 中所有条目，为每篇论文生成一个 BibTeX entry，写入 `references.bib`。

### 输入
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml`

### 输出
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib`

### BibTeX key 命名规则
- 格式：`{第一作者姓小写}{年份}{关键词}`
- 例如：`liu2025teal`, `liu2023dejavu`, `xu2026spon`, `jang2017gumbel`, `shazeer2020glu`

### 每个条目格式
```bibtex
@article{key,
  title = {论文标题},
  author = {Author1 and Author2 and Author3},
  year = {年份},
  journal = {venue 或 arXiv preprint arXiv:XXXX.XXXXX},
  url = {https://arxiv.org/abs/XXXX.XXXXX},  % 如果有 arxiv_id
}
```
- 有明确 venue（如 ICML 2023, NeurIPS 2024, ICLR 2025 等）→ 用 `@inproceedings` + `booktitle`
- 只有 arXiv → 用 `@article` + `journal = {arXiv preprint arXiv:XXXX.XXXXX}`

### 注意事项
- 所有条目都视为 verified（literature_map 中的都是人工确认的）
- 作者列表用 "and" 连接
- 如果 authors 为空列表 `[]`，写 `author = {Unknown}`
- 确保无重复 key
- 按 category 分组，用注释分隔

### 操作步骤
1. Read literature_map.yaml
2. 解析所有条目（约 30 篇）
3. 为每篇生成 BibTeX entry
4. Write 到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib`
5. 验证文件已写入

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "69d5d34a-acf2-4701-80e3-1613a01362a6",
  "type": "user",
  "uuid": "276af66c-e8b7-48b8-a2ca-7b08b24faf00",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T09:39:56.490Z_

```json
{
  "parentUuid": "276af66c-e8b7-48b8-a2ca-7b08b24faf00",
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
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "2949d5ac-a383-4804-88cf-190afa4392c6",
  "timestamp": "2026-05-16T09:39:56.490Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T09:39:56.490Z_

```json
{
  "parentUuid": "2949d5ac-a383-4804-88cf-190afa4392c6",
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
  "uuid": "7d2c95f3-3085-40b3-88e5-b2b53b7f8529",
  "timestamp": "2026-05-16T09:39:56.490Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T09:39:56.490Z_

```json
{
  "parentUuid": "7d2c95f3-3085-40b3-88e5-b2b53b7f8529",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "494f7bec-02c6-4419-88e1-275de1a0ade4",
  "timestamp": "2026-05-16T09:39:56.490Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
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
  "aiTitle": "Generate references.bib from literature_map.yaml",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9"
}
```

---

### Assistant

_source line 8 · 2026-05-16T09:39:59.806Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the literature_map.yaml file first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494f7bec-02c6-4419-88e1-275de1a0ade4",
  "isSidechain": false,
  "requestId": "req_011Cb62UmjghirqNUZM3icKs",
  "type": "assistant",
  "uuid": "3eef7ed0-f089-4c31-92f4-879077e29203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SjTi6ZHHtsvM7ipk5Kxgp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 11841,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
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

_source line 9 · 2026-05-16T09:40:00.279Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HQUYBCuKZwXk3Qn7VqrkX8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eef7ed0-f089-4c31-92f4-879077e29203",
  "isSidechain": false,
  "requestId": "req_011Cb62UmjghirqNUZM3icKs",
  "type": "assistant",
  "uuid": "40ca72d4-1ee5-4cef-a150-b5f8578afbf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SjTi6ZHHtsvM7ipk5Kxgp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12053,
      "cache_read_input_tokens": 11841,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12053
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

_source line 10 · 2026-05-16T09:40:00.298Z_

<details><summary>↩ Tool result · `toolu_01HQUYBCuKZwXk3Qn7VqrkX8`</summary>

```text
1	# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction
2	# Last updated: 2026-05-15
3	# Survey scope: 2023-2026, 4 directions
4	
5	# =============================================================================
6	# Direction 1: KL distillation for structured/activation sparsity
7	# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.
8	# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for
9	# learnable bias correction, not predictor training. This is our novelty.
10	# =============================================================================
11	
12	- title: "Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models"
13	  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]
14	  venue: ICML 2026
15	  year: 2026
16	  arxiv_id: "2512.12744"
17	  category: direct-competitor
18	  role: "最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor"
19	  key_finding: "SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销"
20	  relevance_to_us: "SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致"
21	
22	- title: "Compact Language Models via Pruning and Knowledge Distillation"
23	  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]
24	  venue: NeurIPS 2024
25	  year: 2024
26	  arxiv_id: "2407.14679"
27	  category: method-component
28	  role: "KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching"
29	  key_finding: "Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration"
30	  relevance_to_us: "支持我们的核心假设：KL divergence保留output distribution比逐元素BCE更优。Minitron的发现（logit-only KL最优）为我们predictor的KL训练目标提供了理论支撑"
31	
32	- title: "Instruction-Following Pruning for Large Language Models"
33	  authors: [Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du, Ruoming Pang, Shiyu Chang, Tao Lei]
34	  venue: ICML 2025
35	  year: 2025
36	  arxiv_id: "2501.02086"
37	  category: method-component
38	  role: "训练sparse mask predictor的范式——input-dependent mask selection"
39	  key_finding: "训练一个sparse mask predictor以instruction为输入动态选择最相关参数子集，联合优化mask predictor和LLM"
40	  relevance_to_us: "架构上与我们类似（训练predictor生成mask），但目标是instruction-aware weight pruning而非activation sparsity。可参考其predictor-LLM联合优化策略"
41	
42	# =============================================================================
43	# Direction 2: Output distribution preservation in pruning/sparsity
44	# =============================================================================
45	
46	- title: "Distilling to Hybrid Attention Models via KL-Guided Layer Selection"
47	  authors: []
48	  venue: arXiv
49	  year: 2025
50	  arxiv_id: "2512.20569"
51	  category: method-component
52	  role: "KL散度引导layer selection——用distribution差异决定哪些层需要保留"
53	  key_finding: "用KL divergence作为指标选择哪些attention层替换为hybrid attention，通过最小化output distribution变化来指导架构决策"
54	  relevance_to_us: "方法论启示：KL divergence不仅可作为训练loss，还可作为layer-wise重要性指标。我们可用per-layer KL分析哪些层的sparsity对output distribution影响最大"
55	
56	# =============================================================================
57	# Direction 3: SPON和类似的learnable bias correction for sparsity
58	# =============================================================================
59	
60	- title: "Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity"
61	  authors: [Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, Narasimha Reddy]
62	  venue: arXiv
63	  year: 2026
64	  arxiv_id: "2602.00397"
65	  category: direct-competitor
66	  role: "Predictor + error compensation双组件架构——与SPON的bias correction思路互补"
67	  key_finding: "组合三个组件：(1) lightweight expert predictor选择high-importance neurons，(2) error compensation network修正sparsity误差，(3) layer-wise sparsity scheduler分配计算。50% FFN sparsity下达到1.45x prefill加速"
68	  relevance_to_us: "与我们的方案最可比：都用predictor做activation sparsity。我们的差异在于用KL loss训练predictor而非BCE，且不需要额外的error compensation网络（KL loss本身应该能减少distribution shift）"
69	
70	- title: "Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models"
71	  authors: [Tai An, Ruwu Cai, Yanzhe Zhang, Yang Liu, Hao Chen, Pengcheng Xie, Sheng Chang, Yiwu Yao, Gongyi Wang]
72	  venue: arXiv
73	  year: 2025
74	  arxiv_id: "2508.02128"
75	  category: background
76	  role: "N:M structured activation sparsity——hardware-friendly的sparsity pattern"
77	  key_finding: "Training-free的top-k策略在linear projection层内确定N:M activation masks，在2:4/4:8/8:16多种ratio下有效，可与W8A8量化组合"
78	  relevance_to_us: "如果我们的predictor输出改为N:M structured pattern而非unstructured binary mask，可获得更好的hardware加速。值得作为future work"
79	
80	# =============================================================================
81	# Direction 4: Predictor-based activation sparsity (TEAL, DejaVu, PowerInfer等)
82	# =============================================================================
83	
84	- title: "Training-Free Activation Sparsity in Large Language Models"
85	  authors: [James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun]
86	  venue: ICLR 2025 (Spotlight)
87	  year: 2025
88	  arxiv_id: "2408.14690"
89	  category: direct-competitor
90	  role: "TEAL——我们的主要baseline，training-free magnitude pruning"
91	  key_finding: "对所有hidden states施加magnitude-based sparsity（不需训练），在40-50% sparsity下性能降低很小，Llama-2/3和Mistral 7B-70B上验证。50% sparsity下1.8x decoding加速"
92	  relevance_to_us: "TEAL用BCE度量sparsity mask质量（二元对错），我们的核心论点是：BCE只看neuron是否激活的对错，忽略了错误预测对output distribution的差异化影响。KL loss应该能让predictor学到'哪些neuron的错误预测对output影响更大'"
93	
94	- title: "Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time"
95	  authors: [Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, Beidi Chen]
96	  venue: ICML 2023
97	  year: 2023
98	  arxiv_id: "2310.17157"
99	  category: direct-competitor
100	  role: "Predictor-based contextual sparsity的开创性工作——我们的直接对比对象"
101	  key_finding: "用两层MLP predictor预测每层的contextual sparsity pattern（哪些attention heads和MLP neurons可跳过），在OPT-175B上实现2x加速。Predictor用BCE训练"
102	  relevance_to_us: "DejaVu是predictor-based sparsity的baseline。其predictor用BCE训练——我们改用KL loss训练类似的predictor。关键差异：DejaVu在per-neuron level用BCE，我们在output distribution level用KL"
103	
104	- title: "ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models"
105	  authors: [Yash Akhauri, Ahmed F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander M Rush, Safeen Huda, Mohamed S Abdelfattah]
106	  venue: EMNLP 2024
107	  year: 2024
108	  arxiv_id: "2406.16635"
109	  category: direct-competitor
110	  role: "DejaVu的改进——更好的predictor架构和sparsity pattern enforcement"
111	  key_finding: "Shadow predictor超越magnitude-based pruning，context-dependent评估attention head和neuron重要性。比DejaVu端到端精度提升15%，速度提升20%"
112	  relevance_to_us: "ShadowLLM改进了predictor架构但仍用BCE-style loss。我们的改进方向正交：不改predictor架构，改训练loss（BCE→KL）。两种改进可能互补"
113	
114	- title: "SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference"
115	  authors: [Jiho Shin, Hoeseok Yang, Youngmin Yi]
116	  venue: DATE 2025
117	  year: 2025
118	  arxiv_id: "2411.12692"
119	  category: background
120	  role: "Training-free sign-bit predictor——极低开销的sparsity预测"
121	  key_finding: "仅比较input和weight的sign bits预测activation sparsity，无需训练。仅适用于ReLU-based LLMs，不适用SwiGLU"
122	  relevance_to_us: "不适用于SwiGLU模型（我们的目标），但其sign-bit方法的简洁性值得参考。SwiGLU缺乏天然sparsity证明trained predictor的必要性"
123	
124	- title: "SVD Contextual Sparsity Predictors for Fast LLM Inference"
125	  authors: [Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov]
126	  venue: arXiv
127	  year: 2026
128	  arxiv_id: "2603.14110"
129	  category: direct-competitor
130	  role: "Training-free SVD-based sparsity predictor——用gate projection矩阵的SVD做预测"
131	  key_finding: "对ReGLU FFN的gate projection矩阵做truncation-aware SVD构建sparse pattern predictor，90% FFN sparsity下1.8x decoding加速，benchmark降低<1%"
132	  relevance_to_us: "虽然是training-free competitor，但focus在ReGLU（不是SwiGLU）且需要90%天然稀疏性。我们的方法在SwiGLU的50%目标sparsity下工作，使用场景不同"
133	
134	- title: "CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models"
135	  authors: [Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo Tiwari, Azalia Mirhoseini]
136	  venue: arXiv
137	  year: 2024
138	  arxiv_id: "2404.08763"
139	  category: direct-competitor
140	  role: "Contextual thresholding——不训练predictor，用统计threshold做sparsity"
141	  key_finding: "为每个MLP层计算SiLU(x)激活的percentile threshold做sparsification，50% sparsity下性能降低1-2%，无需fine-tuning。Mistral-7B和Llama2-7B上验证"
142	  relevance_to_us: "CATS直接在SwiGLU/SiLU模型上工作，是我们的直接competitor。但CATS是固定threshold不考虑input context，我们的trained predictor是input-dependent的，理论上更优"
143	
144	- title: "R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference"
145	  authors: [Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li]
146	  venue: ICLR 2025
147	  year: 2025
148	  arxiv_id: "2504.19449"
149	  category: background
150	  role: "Training-free rank-aware方法——利用input channel sparsity和SVD"
151	  key_finding: "用SVD分解将input channel sparsity映射到output，无需预测active channels。50% model-level sparsity下43%端到端加速"
152	  relevance_to_us: "Training-free baseline。如果R-Sparse在SwiGLU模型上效果很好，我们需要证明trained KL predictor的额外训练成本是值得的"
153	
154	- title: "Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking"
155	  authors: [Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough]
156	  venue: MLSys 2025
157	  year: 2024
158	  arxiv_id: "2412.01380"
159	  category: direct-competitor
160	  role: "Predictor-free dynamic pruning for SwiGLU——直接针对SwiGLU的magnitude pruning"
161	  key_finding: "Predictor-free方案动态剪枝SwiGLU MLP层，配合LoRA adapter恢复精度。Phi-3-Medium上46%内存减少+40%吞吐提升"
162	  relevance_to_us: "直接针对SwiGLU的competitor。DIP证明SwiGLU的sparsity pattern难以预测（所以放弃predictor），我们的KL-trained predictor需要证明能克服这个挑战"
163	
164	# =============================================================================
165	# 补充：Activation function替换和sparsity增强
166	# =============================================================================
167	
168	- title: "ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models"
169	  authors: [Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C Del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar]
170	  venue: ICLR 2024
171	  year: 2024
172	  arxiv_id: "2310.04564"
173	  category: background
174	  role: "ReLU替换SiLU获得天然sparsity——替代路线"
175	  key_finding: "用ReLU替换SiLU/GELU后continual pretraining，获得天然高稀疏性（>90%），推理计算减少3x"
176	  relevance_to_us: "替代路线：修改activation function vs 训练predictor。我们的定位：不需要修改pretrained模型架构，作为plug-in predictor在现有SwiGLU模型上工作"
177	
178	- title: "Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters"
179	  authors: [Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen]
180	  venue: arXiv
181	  year: 2024
182	  arxiv_id: "2406.05955"
183	  category: background
184	  role: "dReLU获得90%+ sparsity——activation function工程的极致"
185	  key_finding: "提出dReLU使LLM达到近90% sparsity同时保持SOTA性能，2-5x decoding加速"
186	  relevance_to_us: "与ReLU Strikes Back同一思路但更极端。我们不改activation function，这是差异化定位"
187	
188	- title: "ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models"
189	  authors: [Chenyang Song, Xu Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen Chen, Zhiyuan Liu, Guangli Li, Tao Yang, Maosong Sun]
190	  venue: COLING 2025
191	  year: 2025
192	  arxiv_id: "2402.13516"
193	  category: background
194	  role: "Progressive sparsification——渐进式增加sparsity regularization"
195	  key_finding: "三步法：ReLU替换→progressive sparsity regularization（沿sine curve增强）→threshold shifting(FATReLU)。LLaMA2-7B达89.32% sparsity"
196	  relevance_to_us: "ProSparse的progressive training策略可参考：我们的KL predictor训练也可渐进式增加sparsity目标（已在Lagrangian约束中实现）"
197	
198	- title: "Sparsing Law: Towards Large Language Models with Greater Activation Sparsity"
199	  authors: [Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun Deng, Jiansheng Wei, Zhiyuan Liu, Maosong Sun]
200	  venue: arXiv
201	  year: 2024
202	  arxiv_id: "2411.02335"
203	  category: background
204	  role: "Activation sparsity的scaling law——理论基础"
205	  key_finding: "SiLU/SwiGLU的activation ratio随训练递增（变密），ReLU递减（变稀）。Sparsity对parameter scale不敏感，与width-depth ratio线性相关"
206	  relevance_to_us: "理论支撑：SiLU/SwiGLU模型天然不够稀疏（随训练变密），因此需要外部predictor/pruning来获得稀疏性——这是我们工作的motivation之一"
207	
208	- title: "A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering"
209	  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]
210	  venue: Euro-Par 2025
211	  year: 2025
212	  arxiv_id: "2507.14179"
213	  category: background
214	  role: "Clustering-based sparsity prediction——用聚类简化prediction"
215	  key_finding: "将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度"
216	  relevance_to_us: "降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction"
217	
218	- title: "PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU"
219	  authors: [Yixin Song, Zeyu Mi, Haotong Xie, Haibo Chen]
220	  venue: SOSP 2024
221	  year: 2024
222	  arxiv_id: "2312.12456"
223	  category: background
224	  role: "GPU-CPU混合推理利用activation sparsity的开创性系统工作——建立neuron activation power-law分布"
225	  key_finding: "利用LLM neuron activation的power-law分布（少量hot neurons跨input始终激活，大量cold neurons input-dependent），将hot neurons预加载至GPU、cold neurons在CPU计算，配合adaptive sparsity predictor，单RTX 4090上比llama.cpp快11.69x"
226	  relevance_to_us: "PowerInfer的核心假设（neuron activation有power-law locality）直接支持我们predictor的设计：hot neurons无需预测（始终激活），predictor重点预测cold neurons的contextual activation。其adaptive predictor用较小网络预测高稀疏层的思路可参考"
227	
228	- title: "Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity"
229	  authors: [Susav Shrestha, Brad Settlemyer, Nikoli Dryden, Narasimha Reddy]
230	  venue: NeurIPS 2025
231	  year: 2025
232	  arxiv_id: "2505.14884"
233	  category: background
234	  role: "揭示MLP contextual sparsity在batch场景下不可扩展——attention head sparsity更稳定"
235	  key_finding: "首次揭示MLP contextual sparsity的扩展性瓶颈：随batch size增加，batch内不同token的active neuron取并集趋近dense计算，MLP sparsity增益消失。相反attention head sparsity是batch-invariant的。提出Selective Head Attention实现2.2x加速"
236	  relevance_to_us: "对我们工作的重要约束和定位信息：MLP neuron-level contextual sparsity（我们的方法）主要适用于decoding（batch=1）场景。在大batch prefill中需要不同策略。论文中应明确讨论这一适用范围"
237	
238	# =============================================================================
239	# Cluster 2 补充: KL distillation for model compression
240	# =============================================================================
241	
242	- title: "MiniLLM: Knowledge Distillation of Large Language Models"
243	  authors: [Yuxian Gu, Li Dong, Furu Wei, Minlie Huang]
244	  venue: ICLR 2024
245	  year: 2024
246	  arxiv_id: "2306.08543"
247	  category: method-component
248	  role: "Reverse KL divergence用于LLM知识蒸馏——防止student过估计teacher低概率区域"
249	  key_finding: "用reverse KL替代standard forward KL做LLM蒸馏，配合on-policy optimization。Student生成更精确的响应，calibration更好，长文本生成质量更高。从120M到13B规模均有效"
250	  relevance_to_us: "直接支持我们的核心假设：KL divergence比逐元素loss更适合distribution matching。MiniLLM证明KL能保留output distribution的关键特性（calibration、长尾行为），我们将此insight从model-level蒸馏迁移到predictor训练"
251	
252	- title: "DistiLLM: Towards Streamlined Distillation for Large Language Models"
253	  authors: [Jongwoo Ko, Sungnyun Kim, Tianyi Chen, Se-Young Yun]
254	  venue: ICML 2024
255	  year: 2024
256	  arxiv_id: "2402.03898"
257	  category: method-component
258	  role: "Skewed KL divergence解决标准KL梯度不稳定——师生分布差异大时的工程方案"
259	  key_finding: "提出skewed KL loss：混合师生分布p̃=αpT+(1-α)pθ避免pθ(y)≈0时的梯度爆炸。结合skewed forward KL（teacher输出）和skewed reverse KL（student输出），训练效率和蒸馏质量同时提升"
260	  relevance_to_us: "我们的predictor训练中dense teacher和sparse student的output distribution差异可能很大（尤其训练早期），DistiLLM的skewed mixture技术可直接借鉴防止KL loss的梯度不稳定"
261	
262	- title: "Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models"
263	  authors: [Taiqiang Wu, Chaofan Tao, Jiahao Wang, Runming Yang, Zhe Zhao, Ngai Wong]
264	  venue: COLING 2025
265	  year: 2025
266	  arxiv_id: "2404.02657"
267	  category: background
268	  role: "系统分析forward/reverse KL在LLM蒸馏中的行为差异——为KL方向选择提供理论依据"
269	  key_finding: "实证和理论证明FKL和RKL在LLM KD中共享相同优化目标、充分训练后收敛一致，但训练初期行为不同：FKL关注分布头部（高概率token），RKL关注尾部。提出Adaptive KL (AKL)自适应加权组合两者"
270	  relevance_to_us: "为我们选择forward KL提供理论支撑：FKL在训练初期优先拟合高概率token，更适合保留top prediction的准确性——这正是activation sparsity场景需要的（保证最重要neuron的预测正确）"
271	
272	# =============================================================================
273	# 竞争格局总结
274	# =============================================================================
275	#
276	# 我们的独特定位:
277	# 1. 唯一使用KL divergence训练activation sparsity predictor的工作
278	#    - DejaVu/ShadowLLM用BCE训练predictor
279	#    - SPON用KL但训练bias correction而非predictor
280	#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free
281	# 2. 专注SwiGLU模型的50% sparsity目标
282	#    - ReLU/dReLU方案需要替换activation function
283	#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)
284	# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity
285	#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching
286	#    - 我们将此insight应用到predictor训练
287	#
288	# 主要related work定位:
289	# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold
290	# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor
291	# - vs SPON: predictor vs learnable bias; 都用KL但目标不同
292	# - vs DIP: trained predictor vs predictor-free pruning
293	# - vs ReLU/TurboSparse/ProSparse: 不改activation function
294	# - vs Fast Forward: KL loss vs BCE+error compensation
295	# - vs CATS: input-dependent predictor vs fixed percentile threshold
296	
297	# =============================================================================
298	# Cluster 4: Foundational references
299	# =============================================================================
300	
301	- title: "The Llama 3 Herd of Models"
302	  authors: [Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aieleen Lakber, Aimin Chen, Ait Mokhtar Salma, Ajay Menon]
303	  venue: arXiv
304	  year: 2024
305	  arxiv_id: "2407.21783"
306	  category: foundational
307	  role: "主要评估模型架构——SwiGLU FFN的代表性开源LLM"
308	  key_finding: "Llama 3系列采用SwiGLU FFN、GQA、RoPE，从8B到405B参数规模。在15T+ token上训练，性能比肩GPT-4。SwiGLU FFN的标准化使activation sparsity研究有广泛适用性"
309	  relevance_to_us: "我们的predictor专为SwiGLU架构设计，Llama 3是主要目标模型。其FFN结构（gate_proj * up_proj → down_proj）决定了predictor的输入输出接口"
310	
311	- title: "Mistral 7B"
312	  authors: [Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier]
313	  venue: arXiv
314	  year: 2023
315	  arxiv_id: "2310.06825"
316	  category: foundational
317	  role: "评估模型——高效SwiGLU架构的代表，sliding window attention"
318	  key_finding: "Mistral 7B用SwiGLU+GQA+sliding window attention，在所有benchmark上超越Llama 2 13B。证明紧凑SwiGLU模型的高效性"
319	  relevance_to_us: "实验评估的关键模型之一。Mistral的SwiGLU intermediate size=14336（比Llama大），为predictor设计提供不同维度配置的测试场景"
320	
321	- title: "Categorical Reparameterization with Gumbel-Softmax"
322	  authors: [Eric Jang, Shixiang Gu, Ben Poole]
323	  venue: ICLR 2017
324	  year: 2017
325	  arxiv_id: "1611.01144"
326	  category: foundational
327	  role: "Predictor输出离散mask的可微松弛方法——训练时的梯度传播基础"
328	  key_finding: "Gumbel-Softmax提供categorical分布的连续松弛，使离散采样可通过reparameterization trick进行梯度反传。温度τ→0时逼近one-hot"
329	  relevance_to_us: "我们的predictor输出binary activation mask（离散决策），训练时需要梯度流过mask。Gumbel-Softmax或Straight-Through Estimator是使mask可微的标准技术"
330	
331	- title: "GLU Variants Improve Transformer"
332	  authors: [Noam Shazeer]
333	  venue: arXiv
334	  year: 2020
335	  arxiv_id: "2002.05202"
336	  category: foundational
337	  role: "SwiGLU激活函数的提出——定义了我们工作的目标FFN架构"
338	  key_finding: "提出多种GLU变体（GEGLU、SwiGLU等）替代标准FFN中的ReLU，SwiGLU=Swish(xW)⊙(xV)在perplexity上一致优于ReLU/GELU FFN"
339	  relevance_to_us: "SwiGLU是我们工作的架构基础。SwiGLU的gate机制（Swish门控）产生的activation pattern比ReLU更平滑、天然稀疏性更低，这是trained predictor必要性的根本原因"
340	
341	- title: "Pointer Sentinel Mixture Models"
342	  authors: [Stephen Merity, Caiming Xiong, James Bradbury, Richard Socher]
343	  venue: ICLR 2017
344	  year: 2017
345	  arxiv_id: "1609.07843"
346	  category: foundational
347	  role: "WikiText-2/WikiText-103 benchmark的来源——标准language modeling评估数据集"
348	  key_finding: "提出WikiText-2和WikiText-103数据集，包含Wikipedia长文档，token数分别为2M和103M。成为language modeling perplexity评估的标准benchmark"
349	  relevance_to_us: "WikiText-2是我们评估sparsity对perplexity影响的标准benchmark。所有competitor（TEAL、DejaVu、CATS等）均报告WikiText-2 perplexity，确保结果可比"
350	
351	- title: "Distilling the Knowledge in a Neural Network"
352	  authors: [Geoffrey Hinton, Oriol Vinyals, Jeff Dean]
353	  venue: NeurIPS 2014 Workshop
354	  year: 2015
355	  arxiv_id: "1503.02531"
356	  category: foundational
357	  role: "知识蒸馏的奠基工作——soft target训练的理论基础"
358	  key_finding: "Teacher的soft probability outputs（经温度缩放）包含dark knowledge（类间相似性信息），student通过匹配teacher soft targets学到比hard label更丰富的信息"
359	  relevance_to_us: "我们的KL predictor训练本质是知识蒸馏：dense model是teacher，sparse model是student，predictor学习使sparse output distribution匹配dense distribution。Hinton的soft target insight解释了为什么KL优于BCE（保留分布结构）"
360	
361	- title: "Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation"
362	  authors: [Yoshua Bengio, Nicholas Léonard, Aaron Courville]
363	  venue: arXiv
364	  year: 2013
365	  arxiv_id: "1308.3432"
366	  category: foundational
367	  role: "Straight-Through Estimator——离散mask梯度反传的基础方法"
368	  key_finding: "提出Straight-Through Estimator (STE)：前向传播用离散值，反向传播时将梯度直接传过离散节点（视为identity）。为stochastic/discrete neuron的训练提供实用方案"
369	  relevance_to_us: "STE是训练binary mask predictor的另一标准选择（与Gumbel-Softmax互补）。我们的predictor在inference时输出hard binary mask，训练时可用STE或Gumbel-Softmax传梯度"
370	
371	- title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
372	  authors: [Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu]
373	  venue: JMLR
374	  year: 2020
375	  arxiv_id: "1910.10683"
376	  category: foundational
377	  role: "C4数据集的来源——大规模预训练和蒸馏训练的标准数据"
378	  key_finding: "提出T5统一text-to-text框架，系统比较预训练策略。副产品Colossal Clean Crawled Corpus (C4)成为标准预训练/微调数据集，约750GB清洗后的英文网页文本"
379	  relevance_to_us: "C4是我们predictor蒸馏训练的候选数据源。使用与预训练相同分布的数据训练predictor，确保学到的sparsity pattern在实际推理时有效"
380	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40ca72d4-1ee5-4cef-a150-b5f8578afbf8",
  "isSidechain": false,
  "promptId": "69d5d34a-acf2-4701-80e3-1613a01362a6",
  "type": "user",
  "uuid": "af58303c-75cb-4cbc-9033-ed199bcee774",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml",
      "content": "# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction\n# Last updated: 2026-05-15\n# Survey scope: 2023-2026, 4 directions\n\n# =============================================================================\n# Direction 1: KL distillation for structured/activation sparsity\n# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.\n# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for\n# learnable bias correction, not predictor training. This is our novelty.\n# =============================================================================\n\n- title: \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\"\n  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]\n  venue: ICML 2026\n  year: 2026\n  arxiv_id: \"2512.12744\"\n  category: direct-competitor\n  role: \"最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor\"\n  key_finding: \"SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销\"\n  relevance_to_us: \"SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致\"\n\n- title: \"Compact Language Models via Pruning and Knowledge Distillation\"\n  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]\n  venue: NeurIPS 2024\n  year: 2024\n  arxiv_id: \"2407.14679\"\n  category: method-component\n  role: \"KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching\"\n  key_finding: \"Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration\"\n  relevance_to_us: \"支持我们的核心假设：KL divergence保留output distribution比逐元素BCE更优。Minitron的发现（logit-only KL最优）为我们predictor的KL训练目标提供了理论支撑\"\n\n- title: \"Instruction-Following Pruning for Large Language Models\"\n  authors: [Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du, Ruoming Pang, Shiyu Chang, Tao Lei]\n  venue: ICML 2025\n  year: 2025\n  arxiv_id: \"2501.02086\"\n  category: method-component\n  role: \"训练sparse mask predictor的范式——input-dependent mask selection\"\n  key_finding: \"训练一个sparse mask predictor以instruction为输入动态选择最相关参数子集，联合优化mask predictor和LLM\"\n  relevance_to_us: \"架构上与我们类似（训练predictor生成mask），但目标是instruction-aware weight pruning而非activation sparsity。可参考其predictor-LLM联合优化策略\"\n\n# =============================================================================\n# Direction 2: Output distribution preservation in pruning/sparsity\n# =============================================================================\n\n- title: \"Distilling to Hybrid Attention Models via KL-Guided Layer Selection\"\n  authors: []\n  venue: arXiv\n  year: 2025\n  arxiv_id: \"2512.20569\"\n  category: method-component\n  role: \"KL散度引导layer selection——用distribution差异决定哪些层需要保留\"\n  key_finding: \"用KL divergence作为指标选择哪些attention层替换为hybrid attention，通过最小化output distribution变化来指导架构决策\"\n  relevance_to_us: \"方法论启示：KL divergence不仅可作为训练loss，还可作为layer-wise重要性指标。我们可用per-layer KL分析哪些层的sparsity对output distribution影响最大\"\n\n# =============================================================================\n# Direction 3: SPON和类似的learnable bias correction for sparsity\n# =============================================================================\n\n- title: \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\"\n  authors: [Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, Narasimha Reddy]\n  venue: arXiv\n  year: 2026\n  arxiv_id: \"2602.00397\"\n  category: direct-competitor\n  role: \"Predictor + error compensation双组件架构——与SPON的bias correction思路互补\"\n  key_finding: \"组合三个组件：(1) lightweight expert predictor选择high-importance neurons，(2) error compensation network修正sparsity误差，(3) layer-wise sparsity scheduler分配计算。50% FFN sparsity下达到1.45x prefill加速\"\n  relevance_to_us: \"与我们的方案最可比：都用predictor做activation sparsity。我们的差异在于用KL loss训练predictor而非BCE，且不需要额外的error compensation网络（KL loss本身应该能减少distribution shift）\"\n\n- title: \"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models\"\n  authors: [Tai An, Ruwu Cai, Yanzhe Zhang, Yang Liu, Hao Chen, Pengcheng Xie, Sheng Chang, Yiwu Yao, Gongyi Wang]\n  venue: arXiv\n  year: 2025\n  arxiv_id: \"2508.02128\"\n  category: background\n  role: \"N:M structured activation sparsity——hardware-friendly的sparsity pattern\"\n  key_finding: \"Training-free的top-k策略在linear projection层内确定N:M activation masks，在2:4/4:8/8:16多种ratio下有效，可与W8A8量化组合\"\n  relevance_to_us: \"如果我们的predictor输出改为N:M structured pattern而非unstructured binary mask，可获得更好的hardware加速。值得作为future work\"\n\n# =============================================================================\n# Direction 4: Predictor-based activation sparsity (TEAL, DejaVu, PowerInfer等)\n# =============================================================================\n\n- title: \"Training-Free Activation Sparsity in Large Language Models\"\n  authors: [James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun]\n  venue: ICLR 2025 (Spotlight)\n  year: 2025\n  arxiv_id: \"2408.14690\"\n  category: direct-competitor\n  role: \"TEAL——我们的主要baseline，training-free magnitude pruning\"\n  key_finding: \"对所有hidden states施加magnitude-based sparsity（不需训练），在40-50% sparsity下性能降低很小，Llama-2/3和Mistral 7B-70B上验证。50% sparsity下1.8x decoding加速\"\n  relevance_to_us: \"TEAL用BCE度量sparsity mask质量（二元对错），我们的核心论点是：BCE只看neuron是否激活的对错，忽略了错误预测对output distribution的差异化影响。KL loss应该能让predictor学到'哪些neuron的错误预测对output影响更大'\"\n\n- title: \"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\"\n  authors: [Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, Beidi Chen]\n  venue: ICML 2023\n  year: 2023\n  arxiv_id: \"2310.17157\"\n  category: direct-competitor\n  role: \"Predictor-based contextual sparsity的开创性工作——我们的直接对比对象\"\n  key_finding: \"用两层MLP predictor预测每层的contextual sparsity pattern（哪些attention heads和MLP neurons可跳过），在OPT-175B上实现2x加速。Predictor用BCE训练\"\n  relevance_to_us: \"DejaVu是predictor-based sparsity的baseline。其predictor用BCE训练——我们改用KL loss训练类似的predictor。关键差异：DejaVu在per-neuron level用BCE，我们在output distribution level用KL\"\n\n- title: \"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\"\n  authors: [Yash Akhauri, Ahmed F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander M Rush, Safeen Huda, Mohamed S Abdelfattah]\n  venue: EMNLP 2024\n  year: 2024\n  arxiv_id: \"2406.16635\"\n  category: direct-competitor\n  role: \"DejaVu的改进——更好的predictor架构和sparsity pattern enforcement\"\n  key_finding: \"Shadow predictor超越magnitude-based pruning，context-dependent评估attention head和neuron重要性。比DejaVu端到端精度提升15%，速度提升20%\"\n  relevance_to_us: \"ShadowLLM改进了predictor架构但仍用BCE-style loss。我们的改进方向正交：不改predictor架构，改训练loss（BCE→KL）。两种改进可能互补\"\n\n- title: \"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference\"\n  authors: [Jiho Shin, Hoeseok Yang, Youngmin Yi]\n  venue: DATE 2025\n  year: 2025\n  arxiv_id: \"2411.12692\"\n  category: background\n  role: \"Training-free sign-bit predictor——极低开销的sparsity预测\"\n  key_finding: \"仅比较input和weight的sign bits预测activation sparsity，无需训练。仅适用于ReLU-based LLMs，不适用SwiGLU\"\n  relevance_to_us: \"不适用于SwiGLU模型（我们的目标），但其sign-bit方法的简洁性值得参考。SwiGLU缺乏天然sparsity证明trained predictor的必要性\"\n\n- title: \"SVD Contextual Sparsity Predictors for Fast LLM Inference\"\n  authors: [Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov]\n  venue: arXiv\n  year: 2026\n  arxiv_id: \"2603.14110\"\n  category: direct-competitor\n  role: \"Training-free SVD-based sparsity predictor——用gate projection矩阵的SVD做预测\"\n  key_finding: \"对ReGLU FFN的gate projection矩阵做truncation-aware SVD构建sparse pattern predictor，90% FFN sparsity下1.8x decoding加速，benchmark降低<1%\"\n  relevance_to_us: \"虽然是training-free competitor，但focus在ReGLU（不是SwiGLU）且需要90%天然稀疏性。我们的方法在SwiGLU的50%目标sparsity下工作，使用场景不同\"\n\n- title: \"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\"\n  authors: [Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo Tiwari, Azalia Mirhoseini]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2404.08763\"\n  category: direct-competitor\n  role: \"Contextual thresholding——不训练predictor，用统计threshold做sparsity\"\n  key_finding: \"为每个MLP层计算SiLU(x)激活的percentile threshold做sparsification，50% sparsity下性能降低1-2%，无需fine-tuning。Mistral-7B和Llama2-7B上验证\"\n  relevance_to_us: \"CATS直接在SwiGLU/SiLU模型上工作，是我们的直接competitor。但CATS是固定threshold不考虑input context，我们的trained predictor是input-dependent的，理论上更优\"\n\n- title: \"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\"\n  authors: [Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li]\n  venue: ICLR 2025\n  year: 2025\n  arxiv_id: \"2504.19449\"\n  category: background\n  role: \"Training-free rank-aware方法——利用input channel sparsity和SVD\"\n  key_finding: \"用SVD分解将input channel sparsity映射到output，无需预测active channels。50% model-level sparsity下43%端到端加速\"\n  relevance_to_us: \"Training-free baseline。如果R-Sparse在SwiGLU模型上效果很好，我们需要证明trained KL predictor的额外训练成本是值得的\"\n\n- title: \"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\"\n  authors: [Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough]\n  venue: MLSys 2025\n  year: 2024\n  arxiv_id: \"2412.01380\"\n  category: direct-competitor\n  role: \"Predictor-free dynamic pruning for SwiGLU——直接针对SwiGLU的magnitude pruning\"\n  key_finding: \"Predictor-free方案动态剪枝SwiGLU MLP层，配合LoRA adapter恢复精度。Phi-3-Medium上46%内存减少+40%吞吐提升\"\n  relevance_to_us: \"直接针对SwiGLU的competitor。DIP证明SwiGLU的sparsity pattern难以预测（所以放弃predictor），我们的KL-trained predictor需要证明能克服这个挑战\"\n\n# =============================================================================\n# 补充：Activation function替换和sparsity增强\n# =============================================================================\n\n- title: \"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\"\n  authors: [Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C Del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar]\n  venue: ICLR 2024\n  year: 2024\n  arxiv_id: \"2310.04564\"\n  category: background\n  role: \"ReLU替换SiLU获得天然sparsity——替代路线\"\n  key_finding: \"用ReLU替换SiLU/GELU后continual pretraining，获得天然高稀疏性（>90%），推理计算减少3x\"\n  relevance_to_us: \"替代路线：修改activation function vs 训练predictor。我们的定位：不需要修改pretrained模型架构，作为plug-in predictor在现有SwiGLU模型上工作\"\n\n- title: \"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\"\n  authors: [Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2406.05955\"\n  category: background\n  role: \"dReLU获得90%+ sparsity——activation function工程的极致\"\n  key_finding: \"提出dReLU使LLM达到近90% sparsity同时保持SOTA性能，2-5x decoding加速\"\n  relevance_to_us: \"与ReLU Strikes Back同一思路但更极端。我们不改activation function，这是差异化定位\"\n\n- title: \"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\"\n  authors: [Chenyang Song, Xu Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen Chen, Zhiyuan Liu, Guangli Li, Tao Yang, Maosong Sun]\n  venue: COLING 2025\n  year: 2025\n  arxiv_id: \"2402.13516\"\n  category: background\n  role: \"Progressive sparsification——渐进式增加sparsity regularization\"\n  key_finding: \"三步法：ReLU替换→progressive sparsity regularization（沿sine curve增强）→threshold shifting(FATReLU)。LLaMA2-7B达89.32% sparsity\"\n  relevance_to_us: \"ProSparse的progressive training策略可参考：我们的KL predictor训练也可渐进式增加sparsity目标（已在Lagrangian约束中实现）\"\n\n- title: \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\"\n  authors: [Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun Deng, Jiansheng Wei, Zhiyuan Liu, Maosong Sun]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2411.02335\"\n  category: background\n  role: \"Activation sparsity的scaling law——理论基础\"\n  key_finding: \"SiLU/SwiGLU的activation ratio随训练递增（变密），ReLU递减（变稀）。Sparsity对parameter scale不敏感，与width-depth ratio线性相关\"\n  relevance_to_us: \"理论支撑：SiLU/SwiGLU模型天然不够稀疏（随训练变密），因此需要外部predictor/pruning来获得稀疏性——这是我们工作的motivation之一\"\n\n- title: \"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\"\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\n  venue: Euro-Par 2025\n  year: 2025\n  arxiv_id: \"2507.14179\"\n  category: background\n  role: \"Clustering-based sparsity prediction——用聚类简化prediction\"\n  key_finding: \"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\"\n  relevance_to_us: \"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\"\n\n- title: \"PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU\"\n  authors: [Yixin Song, Zeyu Mi, Haotong Xie, Haibo Chen]\n  venue: SOSP 2024\n  year: 2024\n  arxiv_id: \"2312.12456\"\n  category: background\n  role: \"GPU-CPU混合推理利用activation sparsity的开创性系统工作——建立neuron activation power-law分布\"\n  key_finding: \"利用LLM neuron activation的power-law分布（少量hot neurons跨input始终激活，大量cold neurons input-dependent），将hot neurons预加载至GPU、cold neurons在CPU计算，配合adaptive sparsity predictor，单RTX 4090上比llama.cpp快11.69x\"\n  relevance_to_us: \"PowerInfer的核心假设（neuron activation有power-law locality）直接支持我们predictor的设计：hot neurons无需预测（始终激活），predictor重点预测cold neurons的contextual activation。其adaptive predictor用较小网络预测高稀疏层的思路可参考\"\n\n- title: \"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity\"\n  authors: [Susav Shrestha, Brad Settlemyer, Nikoli Dryden, Narasimha Reddy]\n  venue: NeurIPS 2025\n  year: 2025\n  arxiv_id: \"2505.14884\"\n  category: background\n  role: \"揭示MLP contextual sparsity在batch场景下不可扩展——attention head sparsity更稳定\"\n  key_finding: \"首次揭示MLP contextual sparsity的扩展性瓶颈：随batch size增加，batch内不同token的active neuron取并集趋近dense计算，MLP sparsity增益消失。相反attention head sparsity是batch-invariant的。提出Selective Head Attention实现2.2x加速\"\n  relevance_to_us: \"对我们工作的重要约束和定位信息：MLP neuron-level contextual sparsity（我们的方法）主要适用于decoding（batch=1）场景。在大batch prefill中需要不同策略。论文中应明确讨论这一适用范围\"\n\n# =============================================================================\n# Cluster 2 补充: KL distillation for model compression\n# =============================================================================\n\n- title: \"MiniLLM: Knowledge Distillation of Large Language Models\"\n  authors: [Yuxian Gu, Li Dong, Furu Wei, Minlie Huang]\n  venue: ICLR 2024\n  year: 2024\n  arxiv_id: \"2306.08543\"\n  category: method-component\n  role: \"Reverse KL divergence用于LLM知识蒸馏——防止student过估计teacher低概率区域\"\n  key_finding: \"用reverse KL替代standard forward KL做LLM蒸馏，配合on-policy optimization。Student生成更精确的响应，calibration更好，长文本生成质量更高。从120M到13B规模均有效\"\n  relevance_to_us: \"直接支持我们的核心假设：KL divergence比逐元素loss更适合distribution matching。MiniLLM证明KL能保留output distribution的关键特性（calibration、长尾行为），我们将此insight从model-level蒸馏迁移到predictor训练\"\n\n- title: \"DistiLLM: Towards Streamlined Distillation for Large Language Models\"\n  authors: [Jongwoo Ko, Sungnyun Kim, Tianyi Chen, Se-Young Yun]\n  venue: ICML 2024\n  year: 2024\n  arxiv_id: \"2402.03898\"\n  category: method-component\n  role: \"Skewed KL divergence解决标准KL梯度不稳定——师生分布差异大时的工程方案\"\n  key_finding: \"提出skewed KL loss：混合师生分布p̃=αpT+(1-α)pθ避免pθ(y)≈0时的梯度爆炸。结合skewed forward KL（teacher输出）和skewed reverse KL（student输出），训练效率和蒸馏质量同时提升\"\n  relevance_to_us: \"我们的predictor训练中dense teacher和sparse student的output distribution差异可能很大（尤其训练早期），DistiLLM的skewed mixture技术可直接借鉴防止KL loss的梯度不稳定\"\n\n- title: \"Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models\"\n  authors: [Taiqiang Wu, Chaofan Tao, Jiahao Wang, Runming Yang, Zhe Zhao, Ngai Wong]\n  venue: COLING 2025\n  year: 2025\n  arxiv_id: \"2404.02657\"\n  category: background\n  role: \"系统分析forward/reverse KL在LLM蒸馏中的行为差异——为KL方向选择提供理论依据\"\n  key_finding: \"实证和理论证明FKL和RKL在LLM KD中共享相同优化目标、充分训练后收敛一致，但训练初期行为不同：FKL关注分布头部（高概率token），RKL关注尾部。提出Adaptive KL (AKL)自适应加权组合两者\"\n  relevance_to_us: \"为我们选择forward KL提供理论支撑：FKL在训练初期优先拟合高概率token，更适合保留top prediction的准确性——这正是activation sparsity场景需要的（保证最重要neuron的预测正确）\"\n\n# =============================================================================\n# 竞争格局总结\n# =============================================================================\n#\n# 我们的独特定位:\n# 1. 唯一使用KL divergence训练activation sparsity predictor的工作\n#    - DejaVu/ShadowLLM用BCE训练predictor\n#    - SPON用KL但训练bias correction而非predictor\n#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free\n# 2. 专注SwiGLU模型的50% sparsity目标\n#    - ReLU/dReLU方案需要替换activation function\n#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)\n# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity\n#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching\n#    - 我们将此insight应用到predictor训练\n#\n# 主要related work定位:\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\n# - vs DIP: trained predictor vs predictor-free pruning\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\n# - vs Fast Forward: KL loss vs BCE+error compensation\n# - vs CATS: input-dependent predictor vs fixed percentile threshold\n\n# =============================================================================\n# Cluster 4: Foundational references\n# =============================================================================\n\n- title: \"The Llama 3 Herd of Models\"\n  authors: [Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aieleen Lakber, Aimin Chen, Ait Mokhtar Salma, Ajay Menon]\n  venue: arXiv\n  year: 2024\n  arxiv_id: \"2407.21783\"\n  category: foundational\n  role: \"主要评估模型架构——SwiGLU FFN的代表性开源LLM\"\n  key_finding: \"Llama 3系列采用SwiGLU FFN、GQA、RoPE，从8B到405B参数规模。在15T+ token上训练，性能比肩GPT-4。SwiGLU FFN的标准化使activation sparsity研究有广泛适用性\"\n  relevance_to_us: \"我们的predictor专为SwiGLU架构设计，Llama 3是主要目标模型。其FFN结构（gate_proj * up_proj → down_proj）决定了predictor的输入输出接口\"\n\n- title: \"Mistral 7B\"\n  authors: [Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier]\n  venue: arXiv\n  year: 2023\n  arxiv_id: \"2310.06825\"\n  category: foundational\n  role: \"评估模型——高效SwiGLU架构的代表，sliding window attention\"\n  key_finding: \"Mistral 7B用SwiGLU+GQA+sliding window attention，在所有benchmark上超越Llama 2 13B。证明紧凑SwiGLU模型的高效性\"\n  relevance_to_us: \"实验评估的关键模型之一。Mistral的SwiGLU intermediate size=14336（比Llama大），为predictor设计提供不同维度配置的测试场景\"\n\n- title: \"Categorical Reparameterization with Gumbel-Softmax\"\n  authors: [Eric Jang, Shixiang Gu, Ben Poole]\n  venue: ICLR 2017\n  year: 2017\n  arxiv_id: \"1611.01144\"\n  category: foundational\n  role: \"Predictor输出离散mask的可微松弛方法——训练时的梯度传播基础\"\n  key_finding: \"Gumbel-Softmax提供categorical分布的连续松弛，使离散采样可通过reparameterization trick进行梯度反传。温度τ→0时逼近one-hot\"\n  relevance_to_us: \"我们的predictor输出binary activation mask（离散决策），训练时需要梯度流过mask。Gumbel-Softmax或Straight-Through Estimator是使mask可微的标准技术\"\n\n- title: \"GLU Variants Improve Transformer\"\n  authors: [Noam Shazeer]\n  venue: arXiv\n  year: 2020\n  arxiv_id: \"2002.05202\"\n  category: foundational\n  role: \"SwiGLU激活函数的提出——定义了我们工作的目标FFN架构\"\n  key_finding: \"提出多种GLU变体（GEGLU、SwiGLU等）替代标准FFN中的ReLU，SwiGLU=Swish(xW)⊙(xV)在perplexity上一致优于ReLU/GELU FFN\"\n  relevance_to_us: \"SwiGLU是我们工作的架构基础。SwiGLU的gate机制（Swish门控）产生的activation pattern比ReLU更平滑、天然稀疏性更低，这是trained predictor必要性的根本原因\"\n\n- title: \"Pointer Sentinel Mixture Models\"\n  authors: [Stephen Merity, Caiming Xiong, James Bradbury, Richard Socher]\n  venue: ICLR 2017\n  year: 2017\n  arxiv_id: \"1609.07843\"\n  category: foundational\n  role: \"WikiText-2/WikiText-103 benchmark的来源——标准language modeling评估数据集\"\n  key_finding: \"提出WikiText-2和WikiText-103数据集，包含Wikipedia长文档，token数分别为2M和103M。成为language modeling perplexity评估的标准benchmark\"\n  relevance_to_us: \"WikiText-2是我们评估sparsity对perplexity影响的标准benchmark。所有competitor（TEAL、DejaVu、CATS等）均报告WikiText-2 perplexity，确保结果可比\"\n\n- title: \"Distilling the Knowledge in a Neural Network\"\n  authors: [Geoffrey Hinton, Oriol Vinyals, Jeff Dean]\n  venue: NeurIPS 2014 Workshop\n  year: 2015\n  arxiv_id: \"1503.02531\"\n  category: foundational\n  role: \"知识蒸馏的奠基工作——soft target训练的理论基础\"\n  key_finding: \"Teacher的soft probability outputs（经温度缩放）包含dark knowledge（类间相似性信息），student通过匹配teacher soft targets学到比hard label更丰富的信息\"\n  relevance_to_us: \"我们的KL predictor训练本质是知识蒸馏：dense model是teacher，sparse model是student，predictor学习使sparse output distribution匹配dense distribution。Hinton的soft target insight解释了为什么KL优于BCE（保留分布结构）\"\n\n- title: \"Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation\"\n  authors: [Yoshua Bengio, Nicholas Léonard, Aaron Courville]\n  venue: arXiv\n  year: 2013\n  arxiv_id: \"1308.3432\"\n  category: foundational\n  role: \"Straight-Through Estimator——离散mask梯度反传的基础方法\"\n  key_finding: \"提出Straight-Through Estimator (STE)：前向传播用离散值，反向传播时将梯度直接传过离散节点（视为identity）。为stochastic/discrete neuron的训练提供实用方案\"\n  relevance_to_us: \"STE是训练binary mask predictor的另一标准选择（与Gumbel-Softmax互补）。我们的predictor在inference时输出hard binary mask，训练时可用STE或Gumbel-Softmax传梯度\"\n\n- title: \"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer\"\n  authors: [Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu]\n  venue: JMLR\n  year: 2020\n  arxiv_id: \"1910.10683\"\n  category: foundational\n  role: \"C4数据集的来源——大规模预训练和蒸馏训练的标准数据\"\n  key_finding: \"提出T5统一text-to-text框架，系统比较预训练策略。副产品Colossal Clean Crawled Corpus (C4)成为标准预训练/微调数据集，约750GB清洗后的英文网页文本\"\n  relevance_to_us: \"C4是我们predictor蒸馏训练的候选数据源。使用与预训练相同分布的数据训练predictor，确保学到的sparsity pattern在实际推理时有效\"\n",
      "numLines": 380,
      "startLine": 1,
      "totalLines": 380
    }
  },
  "sourceToolAssistantUUID": "40ca72d4-1ee5-4cef-a150-b5f8578afbf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
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
  "leafUuid": "af58303c-75cb-4cbc-9033-ed199bcee774",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate references.bib from literature_map.yaml",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9"
}
```

---

### Assistant

_source line 13 · 2026-05-16T09:40:04.088Z_

Now I'll generate the references.bib file. Let me check if the paper directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af58303c-75cb-4cbc-9033-ed199bcee774",
  "isSidechain": false,
  "requestId": "req_011Cb62V4jtKfHbvE35dkU1g",
  "type": "assistant",
  "uuid": "88b6a55c-fc63-49bb-8758-2a1e6befa3fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F7C2Pw8U6ohPHf4BXwnn7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10447,
      "cache_read_input_tokens": 23894,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 23894,
          "cache_creation_input_tokens": 10447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10447
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

_source line 14 · 2026-05-16T09:40:05.777Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DNBbiBHB7Qxfz28tcLVfqn`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ 2>/dev/null || echo \"NO_DIR\"",
  "description": "Check if paper directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88b6a55c-fc63-49bb-8758-2a1e6befa3fe",
  "isSidechain": false,
  "requestId": "req_011Cb62V4jtKfHbvE35dkU1g",
  "type": "assistant",
  "uuid": "36328a45-43ad-4505-a5db-8862505c129f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F7C2Pw8U6ohPHf4BXwnn7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10447,
      "cache_read_input_tokens": 23894,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 23894,
          "cache_creation_input_tokens": 10447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10447
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

_source line 15 · 2026-05-16T09:40:05.939Z_

<details><summary>↩ Tool result · `toolu_01DNBbiBHB7Qxfz28tcLVfqn`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36328a45-43ad-4505-a5db-8862505c129f",
  "isSidechain": false,
  "promptId": "69d5d34a-acf2-4701-80e3-1613a01362a6",
  "type": "user",
  "uuid": "93ed9617-dcc5-41f5-869a-cf0054108771",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "36328a45-43ad-4505-a5db-8862505c129f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T09:41:19.698Z_

<details open><summary>🔧 Tool call — Write · `toolu_018eheq56sc8Rmph6riJi72C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
  "content": "% =============================================================================\n% Direction 1: KL distillation for structured/activation sparsity\n% =============================================================================\n\n@inproceedings{xu2026spon,\n  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},\n  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},\n  year = {2026},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2512.12744},\n}\n\n@inproceedings{muralidharan2024minitron,\n  title = {Compact Language Models via Pruning and Knowledge Distillation},\n  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2407.14679},\n}\n\n@inproceedings{hou2025instruction,\n  title = {Instruction-Following Pruning for Large Language Models},\n  author = {Bairu Hou and Qibin Chen and Jianyu Wang and Guoli Yin and Chong Wang and Nan Du and Ruoming Pang and Shiyu Chang and Tao Lei},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2501.02086},\n}\n\n% =============================================================================\n% Direction 2: Output distribution preservation in pruning/sparsity\n% =============================================================================\n\n@article{unknown2025distilling,\n  title = {Distilling to Hybrid Attention Models via KL-Guided Layer Selection},\n  author = {Unknown},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2512.20569},\n  url = {https://arxiv.org/abs/2512.20569},\n}\n\n% =============================================================================\n% Direction 3: SPON and learnable bias correction for sparsity\n% =============================================================================\n\n@article{gautam2026fastforward,\n  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},\n  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2602.00397},\n  url = {https://arxiv.org/abs/2602.00397},\n}\n\n@article{an2025amber,\n  title = {Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models},\n  author = {Tai An and Ruwu Cai and Yanzhe Zhang and Yang Liu and Hao Chen and Pengcheng Xie and Sheng Chang and Yiwu Yao and Gongyi Wang},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2508.02128},\n  url = {https://arxiv.org/abs/2508.02128},\n}\n\n% =============================================================================\n% Direction 4: Predictor-based activation sparsity\n% =============================================================================\n\n@inproceedings{liu2025teal,\n  title = {Training-Free Activation Sparsity in Large Language Models},\n  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2408.14690},\n}\n\n@inproceedings{liu2023dejavu,\n  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},\n  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},\n  year = {2023},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2310.17157},\n}\n\n@inproceedings{akhauri2024shadowllm,\n  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},\n  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},\n  year = {2024},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  url = {https://arxiv.org/abs/2406.16635},\n}\n\n@inproceedings{shin2025sparseinfer,\n  title = {SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference},\n  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},\n  year = {2025},\n  booktitle = {Proceedings of the Design, Automation and Test in Europe Conference (DATE)},\n  url = {https://arxiv.org/abs/2411.12692},\n}\n\n@article{serbin2026svdcsp,\n  title = {SVD Contextual Sparsity Predictors for Fast LLM Inference},\n  author = {Georgii Serbin and Kirill Koshkin and Zhongao Sun and Anastasiya Bistrigova and C.C. Korikov},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2603.14110},\n  url = {https://arxiv.org/abs/2603.14110},\n}\n\n@article{lee2024cats,\n  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},\n  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2404.08763},\n  url = {https://arxiv.org/abs/2404.08763},\n}\n\n@inproceedings{zhang2025rsparse,\n  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},\n  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2504.19449},\n}\n\n@inproceedings{federici2025dip,\n  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},\n  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},\n  year = {2024},\n  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},\n  url = {https://arxiv.org/abs/2412.01380},\n}\n\n% =============================================================================\n% Activation function replacement and sparsity enhancement\n% =============================================================================\n\n@inproceedings{mirzadeh2024relu,\n  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},\n  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2310.04564},\n}\n\n@article{song2024turbosparse,\n  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},\n  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2406.05955},\n  url = {https://arxiv.org/abs/2406.05955},\n}\n\n@inproceedings{song2025prosparse,\n  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},\n  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2402.13516},\n}\n\n@article{luo2024sparsinglaw,\n  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},\n  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2411.02335},\n  url = {https://arxiv.org/abs/2411.02335},\n}\n\n@inproceedings{dhar2025clustering,\n  title = {A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering},\n  author = {Nobel Dhar and Bobin Deng and Md Romyull Islam and Xinyue Zhang and Kazi Fahim Ahmad Nasif and Kun Suo},\n  year = {2025},\n  booktitle = {Proceedings of Euro-Par},\n  url = {https://arxiv.org/abs/2507.14179},\n}\n\n@inproceedings{song2024powerinfer,\n  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},\n  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},\n  year = {2024},\n  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},\n  url = {https://arxiv.org/abs/2312.12456},\n}\n\n@inproceedings{shrestha2025polar,\n  title = {Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity},\n  author = {Susav Shrestha and Brad Settlemyer and Nikoli Dryden and Narasimha Reddy},\n  year = {2025},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2505.14884},\n}\n\n% =============================================================================\n% KL distillation for model compression\n% =============================================================================\n\n@inproceedings{gu2024minillm,\n  title = {MiniLLM: Knowledge Distillation of Large Language Models},\n  author = {Yuxian Gu and Li Dong and Furu Wei and Minlie Huang},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2306.08543},\n}\n\n@inproceedings{ko2024distillm,\n  title = {DistiLLM: Towards Streamlined Distillation for Large Language Models},\n  author = {Jongwoo Ko and Sungnyun Kim and Tianyi Chen and Se-Young Yun},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2402.03898},\n}\n\n@inproceedings{wu2025rethinking,\n  title = {Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models},\n  author = {Taiqiang Wu and Chaofan Tao and Jiahao Wang and Runming Yang and Zhe Zhao and Ngai Wong},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2404.02657},\n}\n\n% =============================================================================\n% Foundational references\n% =============================================================================\n\n@article{grattafiori2024llama3,\n  title = {The Llama 3 Herd of Models},\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2407.21783},\n  url = {https://arxiv.org/abs/2407.21783},\n}\n\n@article{jiang2023mistral,\n  title = {Mistral 7B},\n  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2310.06825},\n  url = {https://arxiv.org/abs/2310.06825},\n}\n\n@inproceedings{jang2017gumbel,\n  title = {Categorical Reparameterization with Gumbel-Softmax},\n  author = {Eric Jang and Shixiang Gu and Ben Poole},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1611.01144},\n}\n\n@article{shazeer2020glu,\n  title = {GLU Variants Improve Transformer},\n  author = {Noam Shazeer},\n  year = {2020},\n  journal = {arXiv preprint arXiv:2002.05202},\n  url = {https://arxiv.org/abs/2002.05202},\n}\n\n@inproceedings{merity2017pointer,\n  title = {Pointer Sentinel Mixture Models},\n  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1609.07843},\n}\n\n@inproceedings{hinton2015distilling,\n  title = {Distilling the Knowledge in a Neural Network},\n  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},\n  year = {2015},\n  booktitle = {NeurIPS 2014 Deep Learning Workshop},\n  url = {https://arxiv.org/abs/1503.02531},\n}\n\n@article{bengio2013ste,\n  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},\n  author = {Yoshua Bengio and Nicholas L\\'{e}onard and Aaron Courville},\n  year = {2013},\n  journal = {arXiv preprint arXiv:1308.3432},\n  url = {https://arxiv.org/abs/1308.3432},\n}\n\n@article{raffel2020t5,\n  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},\n  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},\n  year = {2020},\n  journal = {Journal of Machine Learning Research},\n  url = {https://arxiv.org/abs/1910.10683},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93ed9617-dcc5-41f5-869a-cf0054108771",
  "isSidechain": false,
  "requestId": "req_011Cb62VU1rwSVeVrQnGX65i",
  "type": "assistant",
  "uuid": "549b6a5a-35f5-4266-bc71-b790c52d888d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgA76qpx14k6dFuG4njE5m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 158,
      "cache_read_input_tokens": 34341,
      "output_tokens": 4543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4543,
          "cache_read_input_tokens": 34341,
          "cache_creation_input_tokens": 158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 158
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

_source line 17 · 2026-05-16T09:41:19.728Z_

<details><summary>↩ Tool result · `toolu_018eheq56sc8Rmph6riJi72C`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "549b6a5a-35f5-4266-bc71-b790c52d888d",
  "isSidechain": false,
  "promptId": "69d5d34a-acf2-4701-80e3-1613a01362a6",
  "type": "user",
  "uuid": "9ec65782-1926-4273-ba61-208740195a37",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
    "content": "% =============================================================================\n% Direction 1: KL distillation for structured/activation sparsity\n% =============================================================================\n\n@inproceedings{xu2026spon,\n  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},\n  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},\n  year = {2026},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2512.12744},\n}\n\n@inproceedings{muralidharan2024minitron,\n  title = {Compact Language Models via Pruning and Knowledge Distillation},\n  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2407.14679},\n}\n\n@inproceedings{hou2025instruction,\n  title = {Instruction-Following Pruning for Large Language Models},\n  author = {Bairu Hou and Qibin Chen and Jianyu Wang and Guoli Yin and Chong Wang and Nan Du and Ruoming Pang and Shiyu Chang and Tao Lei},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2501.02086},\n}\n\n% =============================================================================\n% Direction 2: Output distribution preservation in pruning/sparsity\n% =============================================================================\n\n@article{unknown2025distilling,\n  title = {Distilling to Hybrid Attention Models via KL-Guided Layer Selection},\n  author = {Unknown},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2512.20569},\n  url = {https://arxiv.org/abs/2512.20569},\n}\n\n% =============================================================================\n% Direction 3: SPON and learnable bias correction for sparsity\n% =============================================================================\n\n@article{gautam2026fastforward,\n  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},\n  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2602.00397},\n  url = {https://arxiv.org/abs/2602.00397},\n}\n\n@article{an2025amber,\n  title = {Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models},\n  author = {Tai An and Ruwu Cai and Yanzhe Zhang and Yang Liu and Hao Chen and Pengcheng Xie and Sheng Chang and Yiwu Yao and Gongyi Wang},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2508.02128},\n  url = {https://arxiv.org/abs/2508.02128},\n}\n\n% =============================================================================\n% Direction 4: Predictor-based activation sparsity\n% =============================================================================\n\n@inproceedings{liu2025teal,\n  title = {Training-Free Activation Sparsity in Large Language Models},\n  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2408.14690},\n}\n\n@inproceedings{liu2023dejavu,\n  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},\n  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},\n  year = {2023},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2310.17157},\n}\n\n@inproceedings{akhauri2024shadowllm,\n  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},\n  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},\n  year = {2024},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  url = {https://arxiv.org/abs/2406.16635},\n}\n\n@inproceedings{shin2025sparseinfer,\n  title = {SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference},\n  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},\n  year = {2025},\n  booktitle = {Proceedings of the Design, Automation and Test in Europe Conference (DATE)},\n  url = {https://arxiv.org/abs/2411.12692},\n}\n\n@article{serbin2026svdcsp,\n  title = {SVD Contextual Sparsity Predictors for Fast LLM Inference},\n  author = {Georgii Serbin and Kirill Koshkin and Zhongao Sun and Anastasiya Bistrigova and C.C. Korikov},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2603.14110},\n  url = {https://arxiv.org/abs/2603.14110},\n}\n\n@article{lee2024cats,\n  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},\n  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2404.08763},\n  url = {https://arxiv.org/abs/2404.08763},\n}\n\n@inproceedings{zhang2025rsparse,\n  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},\n  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2504.19449},\n}\n\n@inproceedings{federici2025dip,\n  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},\n  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},\n  year = {2024},\n  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},\n  url = {https://arxiv.org/abs/2412.01380},\n}\n\n% =============================================================================\n% Activation function replacement and sparsity enhancement\n% =============================================================================\n\n@inproceedings{mirzadeh2024relu,\n  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},\n  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2310.04564},\n}\n\n@article{song2024turbosparse,\n  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},\n  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2406.05955},\n  url = {https://arxiv.org/abs/2406.05955},\n}\n\n@inproceedings{song2025prosparse,\n  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},\n  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2402.13516},\n}\n\n@article{luo2024sparsinglaw,\n  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},\n  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2411.02335},\n  url = {https://arxiv.org/abs/2411.02335},\n}\n\n@inproceedings{dhar2025clustering,\n  title = {A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering},\n  author = {Nobel Dhar and Bobin Deng and Md Romyull Islam and Xinyue Zhang and Kazi Fahim Ahmad Nasif and Kun Suo},\n  year = {2025},\n  booktitle = {Proceedings of Euro-Par},\n  url = {https://arxiv.org/abs/2507.14179},\n}\n\n@inproceedings{song2024powerinfer,\n  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},\n  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},\n  year = {2024},\n  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},\n  url = {https://arxiv.org/abs/2312.12456},\n}\n\n@inproceedings{shrestha2025polar,\n  title = {Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity},\n  author = {Susav Shrestha and Brad Settlemyer and Nikoli Dryden and Narasimha Reddy},\n  year = {2025},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2505.14884},\n}\n\n% =============================================================================\n% KL distillation for model compression\n% =============================================================================\n\n@inproceedings{gu2024minillm,\n  title = {MiniLLM: Knowledge Distillation of Large Language Models},\n  author = {Yuxian Gu and Li Dong and Furu Wei and Minlie Huang},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2306.08543},\n}\n\n@inproceedings{ko2024distillm,\n  title = {DistiLLM: Towards Streamlined Distillation for Large Language Models},\n  author = {Jongwoo Ko and Sungnyun Kim and Tianyi Chen and Se-Young Yun},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2402.03898},\n}\n\n@inproceedings{wu2025rethinking,\n  title = {Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models},\n  author = {Taiqiang Wu and Chaofan Tao and Jiahao Wang and Runming Yang and Zhe Zhao and Ngai Wong},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2404.02657},\n}\n\n% =============================================================================\n% Foundational references\n% =============================================================================\n\n@article{grattafiori2024llama3,\n  title = {The Llama 3 Herd of Models},\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2407.21783},\n  url = {https://arxiv.org/abs/2407.21783},\n}\n\n@article{jiang2023mistral,\n  title = {Mistral 7B},\n  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2310.06825},\n  url = {https://arxiv.org/abs/2310.06825},\n}\n\n@inproceedings{jang2017gumbel,\n  title = {Categorical Reparameterization with Gumbel-Softmax},\n  author = {Eric Jang and Shixiang Gu and Ben Poole},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1611.01144},\n}\n\n@article{shazeer2020glu,\n  title = {GLU Variants Improve Transformer},\n  author = {Noam Shazeer},\n  year = {2020},\n  journal = {arXiv preprint arXiv:2002.05202},\n  url = {https://arxiv.org/abs/2002.05202},\n}\n\n@inproceedings{merity2017pointer,\n  title = {Pointer Sentinel Mixture Models},\n  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1609.07843},\n}\n\n@inproceedings{hinton2015distilling,\n  title = {Distilling the Knowledge in a Neural Network},\n  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},\n  year = {2015},\n  booktitle = {NeurIPS 2014 Deep Learning Workshop},\n  url = {https://arxiv.org/abs/1503.02531},\n}\n\n@article{bengio2013ste,\n  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},\n  author = {Yoshua Bengio and Nicholas L\\'{e}onard and Aaron Courville},\n  year = {2013},\n  journal = {arXiv preprint arXiv:1308.3432},\n  url = {https://arxiv.org/abs/1308.3432},\n}\n\n@article{raffel2020t5,\n  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},\n  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},\n  year = {2020},\n  journal = {Journal of Machine Learning Research},\n  url = {https://arxiv.org/abs/1910.10683},\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "549b6a5a-35f5-4266-bc71-b790c52d888d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
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
  "leafUuid": "9ec65782-1926-4273-ba61-208740195a37",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate references.bib from literature_map.yaml",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9"
}
```

---

### Assistant

_source line 20 · 2026-05-16T09:41:25.323Z_

已写入 `paper/references.bib`，共 30 个条目，按 category 分组，无重复 key。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ec65782-1926-4273-ba61-208740195a37",
  "isSidechain": false,
  "requestId": "req_011Cb62auYueuqbHRzcZE9Aa",
  "type": "assistant",
  "uuid": "4fa27dfe-5de1-4305-9664-5a95608f2c30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqTNodTJGtLbLcCtJiwqAk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4597,
      "cache_read_input_tokens": 34499,
      "output_tokens": 37,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 37,
          "cache_read_input_tokens": 34499,
          "cache_creation_input_tokens": 4597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4597
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

_source line 21_

```json
{
  "type": "last-prompt",
  "leafUuid": "4fa27dfe-5de1-4305-9664-5a95608f2c30",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate references.bib from literature_map.yaml",
  "sessionId": "a9ab8fc3-db8f-4eaf-913a-36b673e9a9a9"
}
```

---
