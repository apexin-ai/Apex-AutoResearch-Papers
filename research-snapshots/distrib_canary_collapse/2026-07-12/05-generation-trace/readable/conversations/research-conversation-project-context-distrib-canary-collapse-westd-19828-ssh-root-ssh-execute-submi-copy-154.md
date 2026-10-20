# Research conversation: <project_context> # 项目: distrib_canary_collapse ## 运行环境 - 服务器名: westd-19828 - SSH 账户: root（调用 ssh_execute / submit_train

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/7eceecc6-27de-492e-95ec-2cafddf74c7f.jsonl`
- **Structured JSON:** [`5be5448f039a164a470f.json`](../../sessions/5b/5be5448f039a164a470f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T18:12:26.697Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T18:12:26.697Z",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "content": "&lt;project_context>\n# 项目: distrib_canary_collapse\n\n## 运行环境\n- 服务器名: westd-19828\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh westd-19828  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/distrib_canary_collapse\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 论文禁止引用 Phase 2 单 seed 的 TY 跨 α 趋势——必须等 D026 multi-seed 数据确认 TY 非单调性是否可复现（原因：Reviewer Loop #7 发现 TY sig rate 跨 α 呈反直觉非单调模式（0%→62.5%→0%→59.4%），T=10 下 TY 自由度极低（df_resid≈6），单 seed 大概率是噪声。若论文引用此趋势，审稿人会攻击。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：从 literature_map.yaml 生成 references.bib\n\n### 目标\n读取 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml`，将所有论文条目转换为 BibTeX 格式，写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib`。\n\n### 步骤\n\n1. 读取 literature_map.yaml\n2. 对每个 paper 条目，生成 BibTeX entry：\n   - bibtex_key = paper 的 `id` 字段\n   - 根据 venue 判断 entry type：\n     - Nature / Science / Annual Review → @article\n     - ICLR / ICML / NeurIPS / AAAI / EMNLP / NAACL / SIGIR → @inproceedings\n     - arXiv → @article（journal = \"arXiv preprint\"）\n     - MDPI Electronics → @article\n     - Journal of the Royal Society Interface → @article\n   - 填充字段：title, author, year, booktitle/journal, url/doi\n   - author 字段格式：Last1, First1 and Last2, First2 and ...（从 authors 字段解析）\n   - 如果有 doi 字段，添加 doi = {}\n   - 如果有 url 字段（arXiv），添加 url = {}\n3. 写入 references.bib，按 category 分组（用 BibTeX 注释分隔）\n4. 验证输出文件语法（确保括号匹配，无遗漏逗号）\n\n### 重要\n- 不要遗漏任何 paper，全部写入\n- BibTeX key 不要修改，直接用 literature_map 中的 id\n- author 字段中 \"et al.\" 处理：如果 authors 含 \"et al.\"，保留已知作者名 + \"and others\"\n- 中文作者名保持原样\n- 确保文件最后以换行结尾\n\n### 格式示例\n```bibtex\n% ============================================================\n% CORE MODEL COLLAPSE\n% ============================================================\n\n@article{shumailov2024curse,\n  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},\n  journal   = {Nature},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2305.17493},\n}\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T18:12:26.700Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T18:12:26.700Z",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-15T18:12:26.734Z_

&lt;project_context>
# 项目: distrib_canary_collapse

## 运行环境
- 服务器名: westd-19828
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh westd-19828  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/distrib_canary_collapse

## ⚠️ 活跃约束（必须遵守）

- **C001**: 论文禁止引用 Phase 2 单 seed 的 TY 跨 α 趋势——必须等 D026 multi-seed 数据确认 TY 非单调性是否可复现（原因：Reviewer Loop #7 发现 TY sig rate 跨 α 呈反直觉非单调模式（0%→62.5%→0%→59.4%），T=10 下 TY 自由度极低（df_resid≈6），单 seed 大概率是噪声。若论文引用此趋势，审稿人会攻击。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：从 literature_map.yaml 生成 references.bib

### 目标
读取 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml`，将所有论文条目转换为 BibTeX 格式，写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib`。

### 步骤

1. 读取 literature_map.yaml
2. 对每个 paper 条目，生成 BibTeX entry：
   - bibtex_key = paper 的 `id` 字段
   - 根据 venue 判断 entry type：
     - Nature / Science / Annual Review → @article
     - ICLR / ICML / NeurIPS / AAAI / EMNLP / NAACL / SIGIR → @inproceedings
     - arXiv → @article（journal = "arXiv preprint"）
     - MDPI Electronics → @article
     - Journal of the Royal Society Interface → @article
   - 填充字段：title, author, year, booktitle/journal, url/doi
   - author 字段格式：Last1, First1 and Last2, First2 and ...（从 authors 字段解析）
   - 如果有 doi 字段，添加 doi = {}
   - 如果有 url 字段（arXiv），添加 url = {}
3. 写入 references.bib，按 category 分组（用 BibTeX 注释分隔）
4. 验证输出文件语法（确保括号匹配，无遗漏逗号）

### 重要
- 不要遗漏任何 paper，全部写入
- BibTeX key 不要修改，直接用 literature_map 中的 id
- author 字段中 "et al." 处理：如果 authors 含 "et al."，保留已知作者名 + "and others"
- 中文作者名保持原样
- 确保文件最后以换行结尾

### 格式示例
```bibtex
% ============================================================
% CORE MODEL COLLAPSE
% ============================================================

@article{shumailov2024curse,
  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
  journal   = {Nature},
  year      = {2024},
  url       = {https://arxiv.org/abs/2305.17493},
}
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "001f3045-7b6d-4759-9519-5b6e8b3c60f9",
  "type": "user",
  "uuid": "d3bac40f-92f5-4510-953e-d6bb3cc91df9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T18:12:26.734Z_

```json
{
  "parentUuid": "d3bac40f-92f5-4510-953e-d6bb3cc91df9",
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
  "uuid": "d9af5483-9347-4064-b423-06820a5636ca",
  "timestamp": "2026-05-15T18:12:26.734Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T18:12:26.734Z_

```json
{
  "parentUuid": "d9af5483-9347-4064-b423-06820a5636ca",
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
  "uuid": "beb0c7eb-7330-41f2-a04d-1b68ece8fe5f",
  "timestamp": "2026-05-15T18:12:26.734Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T18:12:26.734Z_

```json
{
  "parentUuid": "beb0c7eb-7330-41f2-a04d-1b68ece8fe5f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "43d55932-3750-4715-97d0-16d8b6da7dc0",
  "timestamp": "2026-05-15T18:12:26.734Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
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
  "aiTitle": "Convert literature_map.yaml to references.bib",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f"
}
```

---

### Assistant

_source line 8 · 2026-05-15T18:12:29.385Z_

Reading the literature map file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43d55932-3750-4715-97d0-16d8b6da7dc0",
  "isSidechain": false,
  "requestId": "req_011Cb4okb1hQ1SHCADNeiiDr",
  "type": "assistant",
  "uuid": "9c03c923-8205-4936-8636-1097931e0ef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2RKsMMAJypT3QzdKCcS3V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12100,
      "cache_read_input_tokens": 11841,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12100,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 96,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12100
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

_source line 9 · 2026-05-15T18:12:29.962Z_

<details open><summary>🔧 Tool call — Read · `toolu_011s9AsBmsqW3mr8YkbEBoEN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c03c923-8205-4936-8636-1097931e0ef8",
  "isSidechain": false,
  "requestId": "req_011Cb4okb1hQ1SHCADNeiiDr",
  "type": "assistant",
  "uuid": "155df436-12e4-4cbf-b838-9532bd58ea45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2RKsMMAJypT3QzdKCcS3V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12100,
      "cache_read_input_tokens": 11841,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12100,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 96,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12100
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

_source line 10 · 2026-05-15T18:12:30.225Z_

<details><summary>↩ Tool result · `toolu_011s9AsBmsqW3mr8YkbEBoEN`</summary>

```text
1	papers:
2	  # ============================================================
3	  # CORE MODEL COLLAPSE
4	  # ============================================================
5	  - id: "shumailov2024curse"
6	    title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
7	    authors: "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson"
8	    venue: "Nature"
9	    year: 2024
10	    url: "https://arxiv.org/abs/2305.17493"
11	    category: "core-collapse"
12	    role: "foundation"
13	    key_findings:
14	      - "定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失"
15	      - "区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）"
16	      - "三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合"
17	      - "在 VAE、GMM、LLM 上均验证了 collapse 的普遍性"
18	    relevance_to_us: "奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段"
19	    metrics_studied: ["perplexity", "distributional tail mass"]
20	
21	  - id: "alemohammad2024mad"
22	    title: "Self-Consuming Generative Models Go MAD"
23	    authors: "Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk"
24	    venue: "ICLR 2024"
25	    year: 2024
26	    url: "https://arxiv.org/abs/2307.01850"
27	    category: "core-collapse"
28	    role: "foundation"
29	    key_findings:
30	      - "提出 Model Autophagy Disorder (MAD) 概念"
31	      - "autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降"
32	      - "在图像生成领域验证 self-consuming loop 的退化效应"
33	    relevance_to_us: "MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上"
34	    metrics_studied: ["FID", "precision", "recall", "diversity"]
35	
36	  - id: "dohmatob2024tale"
37	    title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
38	    authors: "Elvis Dohmatob, Yunzhen Feng, et al."
39	    venue: "ICML 2024"
40	    year: 2024
41	    url: "https://arxiv.org/abs/2402.07043"
42	    category: "core-collapse"
43	    role: "foundation"
44	    key_findings:
45	      - "通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化"
46	      - "发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式"
47	      - "混入少量干净数据可缓解 collapse 并引发 grokking 现象"
48	      - "在 transformer 算术任务和 Llama2 文本生成上验证"
49	    relevance_to_us: "scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为"
50	    metrics_studied: ["test loss", "scaling exponents"]
51	
52	  - id: "dohmatob2025strong"
53	    title: "Strong Model Collapse"
54	    authors: "Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe"
55	    venue: "ICLR 2025 (Spotlight)"
56	    year: 2025
57	    url: "https://arxiv.org/abs/2410.04840"
58	    category: "core-collapse"
59	    role: "foundation"
60	    key_findings:
61	      - "即使合成数据占比极小（1/1000），仍可导致 model collapse"
62	      - "更大的训练集并不能避免 collapse"
63	      - "更大的模型（random projection 近似下）反而可能放大 collapse"
64	      - "存在 interpolation threshold 的 double-descent 现象"
65	    relevance_to_us: "强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感"
66	    metrics_studied: ["test loss", "population risk"]
67	
68	  - id: "guo2024linguistic"
69	    title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
70	    authors: "Yanzhu Guo, Guokan Shang, et al."
71	    venue: "NAACL 2024 Findings"
72	    year: 2024
73	    url: "https://arxiv.org/abs/2311.09807"
74	    category: "core-collapse"
75	    role: "evaluation"
76	    key_findings:
77	      - "递归微调中，linguistic diversity 在连续迭代中持续下降"
78	      - "创造性任务中 diversity 下降最显著"
79	      - "开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系"
80	    relevance_to_us: "其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度"
81	    metrics_studied: ["distinct-n", "type-token ratio", "syntactic diversity", "semantic diversity"]
82	
83	  - id: "briesch2024selfconsuming"
84	    title: "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop"
85	    authors: "Martin Briesch, Dominik Sobania, Franz Rothlauf"
86	    venue: "arXiv (2311.16822)"
87	    year: 2024
88	    url: "https://arxiv.org/abs/2311.16822"
89	    category: "core-collapse"
90	    role: "direct-competitor"
91	    key_findings:
92	      - "首次系统研究 LLM 的 self-consuming training loop"
93	      - "full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降"
94	      - "expanding data cycle（累积）在 50 代内保持 diversity"
95	    relevance_to_us: "其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置"
96	    metrics_studied: ["diversity", "quality"]
97	
98	  - id: "truong2025entropy"
99	    title: "Entropy Collapse: A Universal Failure Mode of Intelligent Systems"
100	    authors: "Truong Xuan Khanh, Truong Quynh Hoa"
101	    venue: "arXiv (2512.12381)"
102	    year: 2025
103	    url: "https://arxiv.org/abs/2512.12381"
104	    category: "core-collapse"
105	    role: "theoretical-foundation"
106	    key_findings:
107	      - "证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats"
108	      - "两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2"
109	      - "因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警"
110	    relevance_to_us: "定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效"
111	    gaps: "理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力"
112	    metrics_studied: ["entropy", "autocorrelation", "variance"]
113	
114	  - id: "wang2026contaminated"
115	    title: "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training"
116	    authors: "Kevin Wang, Hongqian Niu, Didong Li"
117	    venue: "arXiv (2602.16065)"
118	    year: 2026
119	    url: "https://arxiv.org/abs/2602.16065"
120	    category: "core-collapse"
121	    role: "theoretical-foundation"
122	    key_findings:
123	      - "首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛"
124	      - "收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈"
125	      - "突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布"
126	    relevance_to_us: "为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率"
127	    gaps: "universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为"
128	    metrics_studied: ["convergence rate", "population risk"]
129	
130	  - id: "du2026geometric"
131	    title: "Escaping Mode Collapse in LLM Generation via Geometric Regulation"
132	    authors: "Du, Tanaka-Ishii"
133	    venue: "arXiv (2605.00435)"
134	    year: 2026
135	    url: "https://arxiv.org/abs/2605.00435"
136	    category: "core-collapse"
137	    role: "background"
138	    key_findings:
139	      - "将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间"
140	      - "提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions"
141	    relevance_to_us: "针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性"
142	    metrics_studied: ["effective rank proxy", "representation dimensionality"]
143	
144	  - id: "gauthier2026alignment"
145	    title: "Explaining and Preventing Alignment Collapse in Iterative RLHF"
146	    authors: "Gauthier, Bach, Jordan"
147	    venue: "arXiv (2605.04266)"
148	    year: 2026
149	    url: "https://arxiv.org/abs/2605.04266"
150	    category: "core-collapse"
151	    role: "complementary"
152	    key_findings:
153	      - "迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）"
154	      - "用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）"
155	    relevance_to_us: "RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释"
156	    metrics_studied: ["alignment score", "reward model accuracy"]
157	
158	  - id: "shi2026pruning"
159	    title: "Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions"
160	    authors: "Shi et al."
161	    venue: "arXiv (2605.07271)"
162	    year: 2026
163	    url: "https://arxiv.org/abs/2605.07271"
164	    category: "core-collapse"
165	    role: "background"
166	    key_findings:
167	      - "层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase"
168	      - "剪枝 Silent Phase 立即触发 collapse"
169	    relevance_to_us: "架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现"
170	    metrics_studied: ["prediction distribution entropy", "task accuracy"]
171	
172	  - id: "tubingen2026diffusion"
173	    title: "Layer Collapse in Diffusion Language Models"
174	    authors: "Tübingen AI Center et al."
175	    venue: "arXiv (2605.06366)"
176	    year: 2026
177	    url: "https://arxiv.org/abs/2605.06366"
178	    category: "core-collapse"
179	    role: "background"
180	    key_findings:
181	      - "LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导"
182	      - "剪掉此 outlier 导致模型输出退化为重复随机 token"
183	    relevance_to_us: "Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集"
184	    metrics_studied: ["activation magnitude", "output repetition"]
185	
186	  # ============================================================
187	  # CANARY / EARLY WARNING METRICS
188	  # ============================================================
189	  - id: "chen2025scales"
190	    title: "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
191	    authors: "Anonymous"
192	    venue: "arXiv (2510.05133)"
193	    year: 2025
194	    url: "https://arxiv.org/abs/2510.05133"
195	    category: "canary-metrics"
196	    role: "direct-competitor"
197	    key_findings:
198	      - "**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal"
199	      - "20% synthetic data 以下性能稳定，30% 以上退化加速"
200	      - "大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒"
201	      - "推理任务比检索任务更易退化"
202	      - "iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）"
203	    relevance_to_us: "**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架"
204	    metrics_studied: ["ECE", "accuracy", "perplexity"]
205	
206	  - id: "gambetta2024surplexity"
207	    title: "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"
208	    authors: "Daniele Gambetta et al."
209	    venue: "arXiv (2410.12341)"
210	    year: 2024
211	    url: "https://arxiv.org/abs/2410.12341"
212	    category: "canary-metrics"
213	    role: "direct-competitor"
214	    key_findings:
215	      - "提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据"
216	      - "用 semantic networks 分析文本重复性和语义多样性"
217	      - "用 next-token probability 定量衡量 diversity loss"
218	      - "高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜"
219	      - "不需要区分 human vs AI-generated data"
220	    relevance_to_us: "surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角"
221	    metrics_studied: ["surplexity", "semantic network metrics", "next-token probability"]
222	
223	  - id: "qiu2025spectral"
224	    title: "Spectral Alignment as Predictor of Loss Explosion in Neural Network Training"
225	    authors: "Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao"
226	    venue: "arXiv (2510.04202)"
227	    year: 2025
228	    url: "https://arxiv.org/abs/2510.04202"
229	    category: "canary-metrics"
230	    role: "method-component"
231	    key_findings:
232	      - "Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐"
233	      - "SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器"
234	      - "比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败"
235	      - "健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定"
236	    relevance_to_us: "SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel"
237	    metrics_studied: ["spectral alignment", "weight norm", "gradient norm"]
238	
239	  - id: "he2025closer"
240	    title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
241	    authors: "Shiliang He et al."
242	    venue: "NeurIPS 2025 (Spotlight)"
243	    year: 2025
244	    url: "https://arxiv.org/abs/2509.16499"
245	    category: "canary-metrics"
246	    role: "direct-competitor"
247	    key_findings:
248	      - "识别 diffusion model collapse 中的 generalization → memorization 转变"
249	      - "**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**"
250	      - "提出基于 entropy 的数据选择策略，有效缓解 collapse"
251	    relevance_to_us: "data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效"
252	    metrics_studied: ["entropy", "FID", "diversity"]
253	
254	  - id: "ba2024fill"
255	    title: "Fill In The Gaps: Model Calibration and Generalization with Synthetic Data"
256	    authors: "Yang Ba, Michelle V Mancenido, Rong Pan"
257	    venue: "EMNLP 2024"
258	    year: 2024
259	    url: "https://arxiv.org/abs/2410.10864"
260	    category: "canary-metrics"
261	    role: "background"
262	    key_findings:
263	      - "用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins"
264	      - "推导了基于 PAC 框架的 ECE bound"
265	      - "合成数据可改善 calibration 但需精心设计生成策略"
266	    relevance_to_us: "ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据"
267	    metrics_studied: ["ECE", "accuracy"]
268	
269	  - id: "sigma2026spectral"
270	    title: "SIGMA: Scalable Spectral Insights for LLM Model Collapse"
271	    authors: "Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue"
272	    venue: "arXiv (2601.03385)"
273	    year: 2026
274	    url: "https://arxiv.org/abs/2601.03385"
275	    category: "canary-metrics"
276	    role: "direct-competitor"
277	    key_findings:
278	      - "基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样"
279	      - "Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影"
280	      - "随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控"
281	    relevance_to_us: "最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成"
282	    gaps: "未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略"
283	    metrics_studied: ["Gram matrix eigenspectrum", "spectral norm bounds"]
284	
285	  - id: "kalinowski2026topology"
286	    title: "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index"
287	    authors: "Alexander Kalinowski"
288	    venue: "arXiv (2604.26984)"
289	    year: 2026
290	    url: "https://arxiv.org/abs/2604.26984"
291	    category: "canary-metrics"
292	    role: "background"
293	    key_findings:
294	      - "提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建"
295	      - "Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning"
296	      - "拓扑方法捕捉表示空间的各向异性和多尺度结构丧失"
297	    relevance_to_us: "topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由"
298	    gaps: "计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比"
299	    metrics_studied: ["Collapse Index", "persistent homology features"]
300	
301	  - id: "bergsma2026scaling"
302	    title: "Scaling with Collapse: Efficient and Predictable Training of LLM Families"
303	    authors: "Bergsma et al."
304	    venue: "arXiv (2509.25087, rev. Mar 2026)"
305	    year: 2026
306	    url: "https://arxiv.org/abs/2509.25087"
307	    category: "canary-metrics"
308	    role: "background"
309	    key_findings:
310	      - "'Collapse' 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）"
311	      - "deviation-from-collapse 作为训练病理的早期诊断信号"
312	    relevance_to_us: "不同语境下的 'collapse'。但其 '偏离通用轨迹 = 训练出问题' 的监控思路与我们的 canary 理念相似——均从时序异常检测角度切入"
313	    metrics_studied: ["loss curve deviation", "scaling law exponents"]
314	
315	  # ============================================================
316	  # DIVERSITY METRICS (BACKGROUND)
317	  # ============================================================
318	  - id: "zhu2018texygen"
319	    title: "Texygen: A Benchmarking Platform for Text Generation Models"
320	    authors: "Yaoming Zhu et al."
321	    venue: "SIGIR 2018"
322	    year: 2018
323	    url: "https://arxiv.org/abs/1802.01886"
324	    category: "canary-metrics"
325	    role: "background"
326	    key_findings:
327	      - "提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低"
328	      - "成为文本生成多样性评估的标准基准之一"
329	    relevance_to_us: "Self-BLEU 是我们 diversity canary 的经典候选"
330	    metrics_studied: ["Self-BLEU", "BLEU"]
331	
332	  - id: "li2016diversity"
333	    title: "A Diversity-Promoting Objective Function for Neural Conversation Models"
334	    authors: "Jiwei Li et al."
335	    venue: "NAACL 2016"
336	    year: 2016
337	    url: "https://arxiv.org/abs/1510.03055"
338	    category: "canary-metrics"
339	    role: "background"
340	    key_findings:
341	      - "提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性"
342	      - "计算 unique n-gram 数占总 n-gram 数的比例"
343	    relevance_to_us: "distinct-n 是最廉价的 diversity canary 之一，计算开销极低"
344	    metrics_studied: ["distinct-1", "distinct-2"]
345	
346	  # ============================================================
347	  # REPRESENTATION / SPECTRAL COLLAPSE
348	  # ============================================================
349	  - id: "jing2022understanding"
350	    title: "Understanding Dimensional Collapse in Contrastive Self-supervised Learning"
351	    authors: "Li Jing et al."
352	    venue: "ICLR 2022"
353	    year: 2022
354	    url: "https://openreview.net/forum?id=YevsQ05DEN7"
355	    category: "canary-metrics"
356	    role: "method-component"
357	    key_findings:
358	      - "定义 dimensional collapse：embedding 向量只跨越低维子空间"
359	      - "effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量"
360	      - "strong augmentation 和 implicit regularization 驱动低秩解"
361	    relevance_to_us: "effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控"
362	    metrics_studied: ["effective rank", "singular value spectrum"]
363	
364	  - id: "noci2024mind"
365	    title: "Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers"
366	    authors: "Lorenzo Noci et al."
367	    venue: "NeurIPS 2024"
368	    year: 2024
369	    url: "https://arxiv.org/abs/2410.07799"
370	    category: "canary-metrics"
371	    role: "method-component"
372	    key_findings:
373	      - "用 Random Matrix Theory 分析 attention 层的 rank collapse"
374	      - "发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因"
375	      - "rank collapse in depth: 所有 token 沿层收敛到单一表示"
376	    relevance_to_us: "spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作"
377	    metrics_studied: ["spectral gap", "singular values", "effective rank"]
378	
379	  # ============================================================
380	  # DATA MIXING & ACCUMULATION
381	  # ============================================================
382	  - id: "kazdan2025collapse"
383	    title: "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
384	    authors: "Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo"
385	    venue: "ICML 2025"
386	    year: 2025
387	    url: "https://arxiv.org/abs/2410.16713"
388	    category: "data-mixing"
389	    role: "foundation"
390	    key_findings:
391	      - "系统对比 replace vs accumulate 场景"
392	      - "replace → collapse；accumulate → 可避免 collapse"
393	      - "发现 real data 和 synthetic data 之间存在非平凡的交互效应"
394	      - "synthetic data 的价值取决于 real data 的绝对数量"
395	    relevance_to_us: "直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考"
396	    metrics_studied: ["test loss"]
397	
398	  - id: "dey2024breaking"
399	    title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
400	    authors: "Apratim Dey, David Donoho, et al."
401	    venue: "ICML 2024"
402	    year: 2024
403	    url: "https://arxiv.org/abs/2404.01413"
404	    category: "data-mixing"
405	    role: "foundation"
406	    key_findings:
407	      - "替换数据 → 发散 population risk；累积数据 → 避免发散"
408	      - "证明累积策略在多种模型（GMM, HMM, LLM）上有效"
409	    relevance_to_us: "为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子"
410	    metrics_studied: ["population risk"]
411	
412	  - id: "epstein2024howbad"
413	    title: "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"
414	    authors: "Mohamed El Amine Epstein et al."
415	    venue: "arXiv (2404.05090)"
416	    year: 2024
417	    url: "https://arxiv.org/abs/2404.05090"
418	    category: "data-mixing"
419	    role: "background"
420	    key_findings:
421	      - "纯合成数据训练不可避免 collapse"
422	      - "给出 synthetic data 比例上界的估计——低于此比例可避免 collapse"
423	      - "递归训练使原始分布尾部消失"
424	    relevance_to_us: "其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值"
425	    metrics_studied: ["perplexity"]
426	
427	  - id: "fu2025selfconsuming"
428	    title: "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops"
429	    authors: "Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao"
430	    venue: "ICLR 2025"
431	    year: 2025
432	    url: "https://arxiv.org/abs/2502.18865"
433	    category: "data-mixing"
434	    role: "theoretical-foundation"
435	    key_findings:
436	      - "引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析"
437	      - "恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight"
438	      - "模型架构和 real/synthetic 数据比例共同决定 STL 的成败"
439	    relevance_to_us: "为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证"
440	    gaps: "理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构"
441	    metrics_studied: ["generalization bound", "population risk"]
442	
443	  - id: "bakshi2026improvement"
444	    title: "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources"
445	    authors: "Soham Bakshi, Sunrit Chakraborty"
446	    venue: "arXiv (2602.10531)"
447	    year: 2026
448	    url: "https://arxiv.org/abs/2602.10531"
449	    category: "data-mixing"
450	    role: "theoretical-foundation"
451	    key_findings:
452	      - "αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency"
453	      - "当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）"
454	      - "αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime"
455	      - "在 next-token prediction 语言模型上分析完整迭代演化动态"
456	    relevance_to_us: "αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式"
457	    gaps: "理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime"
458	    metrics_studied: ["population risk", "total variation distance"]
459	
460	  - id: "he2025golden"
461	    title: "Golden Ratio Weighting Prevents Model Collapse"
462	    authors: "Shiliang He, Zhongbin Xu, Yan Cheng"
463	    venue: "arXiv (2502.18049)"
464	    year: 2025
465	    url: "https://arxiv.org/abs/2502.18049"
466	    category: "data-mixing"
467	    role: "theoretical-foundation"
468	    key_findings:
469	      - "最优 real data 权重在 Gaussian estimation、GLM、非参数估计中均收敛到黄金比例倒数 1/φ ≈ 0.618"
470	      - "最优权重 w*(λ) 作为正则化参数的函数既非单调也非凸——risk landscape 在 mixing ratio 空间上本身不是单调的"
471	      - "提供了 mixing ratio 非单调性的首个理论框架"
472	    relevance_to_us: "我们在 α-sweep 中观测到的非单调 dose-response（α=0.25 比 α=0.50 collapse 更严重）可视为该理论在 diversity metrics 上的实证验证。论文 Discussion 的理论锚点。"
473	    gaps: "理论基于线性回归和高斯分布，未直接推广到 LLM diversity metrics"
474	    metrics_studied: ["population risk", "optimal weight"]
475	
476	  - id: "xu2025mixing"
477	    title: "Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios"
478	    authors: "Zhongbin Xu, Yan Cheng"
479	    venue: "arXiv (2509.22341)"
480	    year: 2025
481	    url: "https://arxiv.org/abs/2509.22341"
482	    category: "data-mixing"
483	    role: "theoretical-foundation"
484	    key_findings:
485	      - "过参数化 regime（插值学习 + ridge 回归）中分析最优混合比例"
486	      - "插值学习：最优 real data 比例收敛到 1/φ"
487	      - "Ridge 回归：最优比例受谱几何控制，至少为 1/2"
488	      - "w > 1/3 时 variance 随迭代单调递减；w < 1/3 时 variance 可能增长——存在临界阈值"
489	    relevance_to_us: "1/3 临界阈值与我们 α=0.25（real weight=0.75 vs synthetic weight=0.25）处出现最强 collapse 的观测有概念对应。不同 regime 下 variance 行为质变支持我们的 regime-dependent 叙事。"
490	    gaps: "参数空间不完全对齐（他们的 w 是 real data weight，我们的 α 是 synthetic ratio）；未讨论 diversity metrics"
491	    metrics_studied: ["variance", "population risk", "optimal mixing ratio"]
492	
493	  # ============================================================
494	  # MITIGATION & VERIFICATION
495	  # ============================================================
496	  - id: "feng2025escaping"
497	    title: "Escaping Model Collapse via Synthetic Data Verification"
498	    authors: "Yunzhen Feng et al."
499	    venue: "NeurIPS 2025"
500	    year: 2025
501	    url: "https://arxiv.org/abs/2510.16657"
502	    category: "data-mixing"
503	    role: "background"
504	    key_findings:
505	      - "通过外部 verifier（human 或 better model）注入信息可避免 collapse"
506	      - "verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center"
507	      - "除非 verifier 完全可靠，早期收益会 plateau 甚至逆转"
508	    relevance_to_us: "verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention"
509	    metrics_studied: ["test loss"]
510	
511	  - id: "barzilai2025consistency"
512	    title: "When Models Don't Collapse: On the Consistency of Iterative MLE"
513	    authors: "Daniel Barzilai, Ohad Shamir"
514	    venue: "ICML 2025"
515	    year: 2025
516	    url: "https://arxiv.org/abs/2505.19046"
517	    category: "core-collapse"
518	    role: "background"
519	    key_findings:
520	      - "在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse"
521	      - "但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例"
522	    relevance_to_us: "理论上的 collapse 可发生任意快的结论强化了 early warning 的价值"
523	    metrics_studied: []
524	
525	  - id: "dces2026counter"
526	    title: "Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling"
527	    authors: "Anonymous"
528	    venue: "MDPI Electronics (2026)"
529	    year: 2026
530	    url: "https://www.mdpi.com/2079-9292/15/4/869"
531	    category: "data-mixing"
532	    role: "background"
533	    key_findings:
534	      - "提出 DCES（dynamic center-edge sampling）数据选择框架"
535	      - "DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择"
536	    relevance_to_us: "其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考"
537	    metrics_studied: ["ECE", "entropy"]
538	
539	  # ============================================================
540	  # POSITION / SURVEY / EPISTEMICS
541	  # ============================================================
542	  - id: "schaeffer2025position"
543	    title: "Position: Model Collapse Does Not Mean What You Think"
544	    authors: "Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo"
545	    venue: "arXiv (2503.03150)"
546	    year: 2025
547	    url: "https://arxiv.org/abs/2503.03150"
548	    category: "core-collapse"
549	    role: "background"
550	    key_findings:
551	      - "文献中实际包含 8 种不同且有时矛盾的 model collapse 定义"
552	      - "许多 collapse 预测依赖于与现实不符的假设"
553	      - "多种 collapse 场景是可以轻易避免的"
554	    relevance_to_us: "提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标"
555	    metrics_studied: []
556	
557	  - id: "wang2025epistemic"
558	    title: "Epistemic Diversity and Knowledge Collapse in Large Language Models"
559	    authors: "Wang et al."
560	    venue: "arXiv (2510.04226)"
561	    year: 2025
562	    url: "https://arxiv.org/abs/2510.04226"
563	    category: "core-collapse"
564	    role: "background"
565	    key_findings:
566	      - "27 个 LLM 在 155 个主题上的 epistemic diversity 评估"
567	      - "所有模型的 epistemic diversity 低于基本 web 搜索"
568	      - "模型越大 epistemic diversity 反而越低；RAG 有正面效果"
569	    relevance_to_us: "knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic"
570	    metrics_studied: ["epistemic diversity"]
571	
572	  # ============================================================
573	  # METHODOLOGY (GRANGER / LEAD-LAG)
574	  # ============================================================
575	  - id: "shojaie2022granger"
576	    title: "Granger Causality: A Review and Recent Advances"
577	    authors: "Ali Shojaie, Emily B. Fox"
578	    venue: "Annual Review of Statistics and Its Application"
579	    year: 2022
580	    url: "https://arxiv.org/abs/2105.02675"
581	    category: "methodology"
582	    role: "method-component"
583	    key_findings:
584	      - "Granger causality 综述：从经典线性到非线性/neural 方法"
585	      - "Panel data 场景的 Granger causality 扩展"
586	      - "VAR 和 neural Granger causality 的对比"
587	    relevance_to_us: "为我们的 panel Granger causality 分析提供方法论基础"
588	    metrics_studied: []
589	
590	  - id: "marcinkevics2022neural"
591	    title: "Granger Causality Using Neural Networks"
592	    authors: "Raphael Marcinkevics, Julia Vogt"
593	    venue: "arXiv (2208.03703)"
594	    year: 2022
595	    url: "https://arxiv.org/abs/2208.03703"
596	    category: "methodology"
597	    role: "method-component"
598	    key_findings:
599	      - "用 neural network 估计 Granger causality，突破线性假设"
600	      - "两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据"
601	    relevance_to_us: "我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择"
602	    metrics_studied: []
603	
604	  # ============================================================
605	  # EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)
606	  # ============================================================
607	  - id: "scheffer2009early"
608	    title: "Early-warning signals for critical transitions"
609	    authors: "Marten Scheffer, Jordi Bascompte, William A. Brock, Victor Brovkin, Stephen R. Carpenter, Vasilis Dakos, Hermann Held, Egbert H. van Nes, Max Rietkerk, George Sugihara"
610	    venue: "Nature"
611	    year: 2009
612	    doi: "10.1038/nature08227"
613	    category: "early-warning-signals"
614	    role: "theoretical-foundation"
615	    key_findings:
616	      - "复杂系统（生态、气候、金融）在临界转变前存在通用 early warning signals：critical slowing down 导致 autocorrelation 增加、variance 增加、recovery rate 降低"
617	      - "这些 generic indicators 不依赖于系统具体机制，而是源于分岔点附近的数学共性"
618	      - "综述了跨领域的 tipping point 检测方法，建立了 early warning signals 的理论框架"
619	    relevance_to_us: "我们将 token entropy / diversity 下降类比为生态系统 tipping point 前的 early warning signal——diversity collapse 在概念上对应生态系统的 critical transition。Scheffer 的 generic indicator 框架为我们的 multi-metric canary panel 提供跨学科理论基础"
620	    one_line_finding: "复杂系统临界转变前存在通用早期预警信号（critical slowing down），可跨领域检测 tipping point"
621	    metrics_studied: ["autocorrelation", "variance", "recovery rate"]
622	
623	  - id: "scheffer2012anticipating"
624	    title: "Anticipating Critical Transitions"
625	    authors: "Marten Scheffer, Stephen R. Carpenter, Timothy M. Lenton, Jordi Bascompte, William Brock, Vasilis Dakos, Johan van de Koppel, Ingrid A. van de Leemput, Simon A. Levin, Egbert H. van Nes, Mercedes Pascual, John Vandermeer"
626	    venue: "Science"
627	    year: 2012
628	    doi: "10.1126/science.1225244"
629	    category: "early-warning-signals"
630	    role: "theoretical-foundation"
631	    key_findings:
632	      - "整合两条研究线：(1) 揭示网络架构特征导致 tipping points 的结构性原因，(2) 发现接近临界阈值的通用经验指标"
633	      - "Tipping points 既意味着 unwanted collapse 的风险，也意味着 positive change 的机会——关键在于预测能力"
634	      - "提出将网络架构分析与经验预警指标结合的交叉方法论"
635	    relevance_to_us: "将 early warning 从纯统计信号扩展到网络/架构分析——类比我们同时监控输出统计（ECE, entropy）和表征结构（effective rank, spectral）的多层 canary panel 设计。其 'architecture → tipping point' 分析呼应我们对模型内部表征 collapse 的关注"
636	    one_line_finding: "结合网络架构分析与经验预警指标可更有效地预测复杂系统的临界转变"
637	    metrics_studied: ["network architecture features", "empirical early warning indicators"]
638	
639	  - id: "boettiger2012limits"
640	    title: "Quantifying Limits to Detection of Early Warning for Critical Transitions"
641	    authors: "Carl Boettiger, Alan Hastings"
642	    venue: "Journal of the Royal Society Interface"
643	    year: 2012
644	    doi: "10.1098/rsif.2012.0125"
645	    category: "early-warning-signals"
646	    role: "methodological-precedent"
647	    key_findings:
648	      - "用 likelihood ratio 框架量化 early warning signals 的统计检测力——在有限长度时间序列下，EWS 检测力极低"
649	      - "即使系统确实在接近 tipping point，短时间序列中 autocorrelation 增加等 EWS 的统计显著性往往不足以拒绝零假设"
650	      - "检测力取决于时间序列长度、噪声水平、接近临界点的速率——现实数据常处于低检测力 regime"
651	    relevance_to_us: "与 Claim 3（方法选择敏感性）和 plan_009（TY power analysis, T=10 power=0.05-0.20）高度对齐。Boettiger & Hastings 从生态学角度量化了 EWS 在短时间序列下的统计极限，我们在 model collapse 迭代训练语境下独立发现了同样的问题——少数迭代轮次下 canary 检测力不足。他们的 power analysis 框架为我们的统计检测力论证提供了跨学科先例"
652	    one_line_finding: "Early warning signals 在短时间序列下统计检测力极低，量化了 EWS 检测的基本统计极限"
653	    metrics_studied: ["autocorrelation", "variance", "likelihood ratio", "statistical power"]
654	
655	gaps:
656	  - "无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse"
657	  - "ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析"
658	  - "embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过"
659	  - "多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系"
660	  - "alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化"
661	  - "diversity dose-response 非单调性（α=0.25 比 α=0.50 collapse 更严重）无先例报告——He et al. 2025 从理论上预测 risk landscape 非单调，但无人在 LLM diversity 上实证验证"
662	  - "predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益"
663	  - "surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证"
664	  - "跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠"
665	
666	novelty_assessment: |
667	  我们项目的核心 novelty 在于：
668	
669	  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。
670	     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，
671	     但没有人做过系统的 lead-lag 量化分析。
672	
673	  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、
674	     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。
675	     现有工作都是单一指标或最多两三个指标的孤立分析。
676	
677	  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary
678	     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，
679	     但没人研究 canary 在不同 alpha 下的行为。
680	
681	  4. **与已有工作的差异**：
682	     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化
683	     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；
684	       我们将其纳入更广的 panel 并研究其 lead-lag 特性
685	     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标
686	     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；
687	       我们将类似思路迁移到 iterative collapse 场景
688	
689	  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，
690	     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。
691	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "155df436-12e4-4cbf-b838-9532bd58ea45",
  "isSidechain": false,
  "promptId": "001f3045-7b6d-4759-9519-5b6e8b3c60f9",
  "type": "user",
  "uuid": "e042dca9-9cb9-44d0-b91d-10dd8518fa38",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
      "content": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  - id: \"du2026geometric\"\n    title: \"Escaping Mode Collapse in LLM Generation via Geometric Regulation\"\n    authors: \"Du, Tanaka-Ishii\"\n    venue: \"arXiv (2605.00435)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.00435\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间\"\n      - \"提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\"\n    relevance_to_us: \"针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\"\n    metrics_studied: [\"effective rank proxy\", \"representation dimensionality\"]\n\n  - id: \"gauthier2026alignment\"\n    title: \"Explaining and Preventing Alignment Collapse in Iterative RLHF\"\n    authors: \"Gauthier, Bach, Jordan\"\n    venue: \"arXiv (2605.04266)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.04266\"\n    category: \"core-collapse\"\n    role: \"complementary\"\n    key_findings:\n      - \"迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）\"\n      - \"用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）\"\n    relevance_to_us: \"RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释\"\n    metrics_studied: [\"alignment score\", \"reward model accuracy\"]\n\n  - id: \"shi2026pruning\"\n    title: \"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv (2605.07271)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.07271\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase\"\n      - \"剪枝 Silent Phase 立即触发 collapse\"\n    relevance_to_us: \"架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\"\n    metrics_studied: [\"prediction distribution entropy\", \"task accuracy\"]\n\n  - id: \"tubingen2026diffusion\"\n    title: \"Layer Collapse in Diffusion Language Models\"\n    authors: \"Tübingen AI Center et al.\"\n    venue: \"arXiv (2605.06366)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.06366\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导\"\n      - \"剪掉此 outlier 导致模型输出退化为重复随机 token\"\n    relevance_to_us: \"Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集\"\n    metrics_studied: [\"activation magnitude\", \"output repetition\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  - id: \"bergsma2026scaling\"\n    title: \"Scaling with Collapse: Efficient and Predictable Training of LLM Families\"\n    authors: \"Bergsma et al.\"\n    venue: \"arXiv (2509.25087, rev. Mar 2026)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2509.25087\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"'Collapse' 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）\"\n      - \"deviation-from-collapse 作为训练病理的早期诊断信号\"\n    relevance_to_us: \"不同语境下的 'collapse'。但其 '偏离通用轨迹 = 训练出问题' 的监控思路与我们的 canary 理念相似——均从时序异常检测角度切入\"\n    metrics_studied: [\"loss curve deviation\", \"scaling law exponents\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"fu2025selfconsuming\"\n    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18865\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"\n      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"\n      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"\n    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"\n    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"\n    metrics_studied: [\"generalization bound\", \"population risk\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi, Sunrit Chakraborty\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\"\n      - \"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\"\n      - \"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\"\n      - \"在 next-token prediction 语言模型上分析完整迭代演化动态\"\n    relevance_to_us: \"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\"\n    gaps: \"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\"\n    metrics_studied: [\"population risk\", \"total variation distance\"]\n\n  - id: \"he2025golden\"\n    title: \"Golden Ratio Weighting Prevents Model Collapse\"\n    authors: \"Shiliang He, Zhongbin Xu, Yan Cheng\"\n    venue: \"arXiv (2502.18049)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18049\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"最优 real data 权重在 Gaussian estimation、GLM、非参数估计中均收敛到黄金比例倒数 1/φ ≈ 0.618\"\n      - \"最优权重 w*(λ) 作为正则化参数的函数既非单调也非凸——risk landscape 在 mixing ratio 空间上本身不是单调的\"\n      - \"提供了 mixing ratio 非单调性的首个理论框架\"\n    relevance_to_us: \"我们在 α-sweep 中观测到的非单调 dose-response（α=0.25 比 α=0.50 collapse 更严重）可视为该理论在 diversity metrics 上的实证验证。论文 Discussion 的理论锚点。\"\n    gaps: \"理论基于线性回归和高斯分布，未直接推广到 LLM diversity metrics\"\n    metrics_studied: [\"population risk\", \"optimal weight\"]\n\n  - id: \"xu2025mixing\"\n    title: \"Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios\"\n    authors: \"Zhongbin Xu, Yan Cheng\"\n    venue: \"arXiv (2509.22341)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.22341\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"过参数化 regime（插值学习 + ridge 回归）中分析最优混合比例\"\n      - \"插值学习：最优 real data 比例收敛到 1/φ\"\n      - \"Ridge 回归：最优比例受谱几何控制，至少为 1/2\"\n      - \"w > 1/3 时 variance 随迭代单调递减；w < 1/3 时 variance 可能增长——存在临界阈值\"\n    relevance_to_us: \"1/3 临界阈值与我们 α=0.25（real weight=0.75 vs synthetic weight=0.25）处出现最强 collapse 的观测有概念对应。不同 regime 下 variance 行为质变支持我们的 regime-dependent 叙事。\"\n    gaps: \"参数空间不完全对齐（他们的 w 是 real data weight，我们的 α 是 synthetic ratio）；未讨论 diversity metrics\"\n    metrics_studied: [\"variance\", \"population risk\", \"optimal mixing ratio\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\n  # ============================================================\n  # EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)\n  # ============================================================\n  - id: \"scheffer2009early\"\n    title: \"Early-warning signals for critical transitions\"\n    authors: \"Marten Scheffer, Jordi Bascompte, William A. Brock, Victor Brovkin, Stephen R. Carpenter, Vasilis Dakos, Hermann Held, Egbert H. van Nes, Max Rietkerk, George Sugihara\"\n    venue: \"Nature\"\n    year: 2009\n    doi: \"10.1038/nature08227\"\n    category: \"early-warning-signals\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"复杂系统（生态、气候、金融）在临界转变前存在通用 early warning signals：critical slowing down 导致 autocorrelation 增加、variance 增加、recovery rate 降低\"\n      - \"这些 generic indicators 不依赖于系统具体机制，而是源于分岔点附近的数学共性\"\n      - \"综述了跨领域的 tipping point 检测方法，建立了 early warning signals 的理论框架\"\n    relevance_to_us: \"我们将 token entropy / diversity 下降类比为生态系统 tipping point 前的 early warning signal——diversity collapse 在概念上对应生态系统的 critical transition。Scheffer 的 generic indicator 框架为我们的 multi-metric canary panel 提供跨学科理论基础\"\n    one_line_finding: \"复杂系统临界转变前存在通用早期预警信号（critical slowing down），可跨领域检测 tipping point\"\n    metrics_studied: [\"autocorrelation\", \"variance\", \"recovery rate\"]\n\n  - id: \"scheffer2012anticipating\"\n    title: \"Anticipating Critical Transitions\"\n    authors: \"Marten Scheffer, Stephen R. Carpenter, Timothy M. Lenton, Jordi Bascompte, William Brock, Vasilis Dakos, Johan van de Koppel, Ingrid A. van de Leemput, Simon A. Levin, Egbert H. van Nes, Mercedes Pascual, John Vandermeer\"\n    venue: \"Science\"\n    year: 2012\n    doi: \"10.1126/science.1225244\"\n    category: \"early-warning-signals\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"整合两条研究线：(1) 揭示网络架构特征导致 tipping points 的结构性原因，(2) 发现接近临界阈值的通用经验指标\"\n      - \"Tipping points 既意味着 unwanted collapse 的风险，也意味着 positive change 的机会——关键在于预测能力\"\n      - \"提出将网络架构分析与经验预警指标结合的交叉方法论\"\n    relevance_to_us: \"将 early warning 从纯统计信号扩展到网络/架构分析——类比我们同时监控输出统计（ECE, entropy）和表征结构（effective rank, spectral）的多层 canary panel 设计。其 'architecture → tipping point' 分析呼应我们对模型内部表征 collapse 的关注\"\n    one_line_finding: \"结合网络架构分析与经验预警指标可更有效地预测复杂系统的临界转变\"\n    metrics_studied: [\"network architecture features\", \"empirical early warning indicators\"]\n\n  - id: \"boettiger2012limits\"\n    title: \"Quantifying Limits to Detection of Early Warning for Critical Transitions\"\n    authors: \"Carl Boettiger, Alan Hastings\"\n    venue: \"Journal of the Royal Society Interface\"\n    year: 2012\n    doi: \"10.1098/rsif.2012.0125\"\n    category: \"early-warning-signals\"\n    role: \"methodological-precedent\"\n    key_findings:\n      - \"用 likelihood ratio 框架量化 early warning signals 的统计检测力——在有限长度时间序列下，EWS 检测力极低\"\n      - \"即使系统确实在接近 tipping point，短时间序列中 autocorrelation 增加等 EWS 的统计显著性往往不足以拒绝零假设\"\n      - \"检测力取决于时间序列长度、噪声水平、接近临界点的速率——现实数据常处于低检测力 regime\"\n    relevance_to_us: \"与 Claim 3（方法选择敏感性）和 plan_009（TY power analysis, T=10 power=0.05-0.20）高度对齐。Boettiger & Hastings 从生态学角度量化了 EWS 在短时间序列下的统计极限，我们在 model collapse 迭代训练语境下独立发现了同样的问题——少数迭代轮次下 canary 检测力不足。他们的 power analysis 框架为我们的统计检测力论证提供了跨学科先例\"\n    one_line_finding: \"Early warning signals 在短时间序列下统计检测力极低，量化了 EWS 检测的基本统计极限\"\n    metrics_studied: [\"autocorrelation\", \"variance\", \"likelihood ratio\", \"statistical power\"]\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"diversity dose-response 非单调性（α=0.25 比 α=0.50 collapse 更严重）无先例报告——He et al. 2025 从理论上预测 risk landscape 非单调，但无人在 LLM diversity 上实证验证\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
      "numLines": 691,
      "startLine": 1,
      "totalLines": 691
    }
  },
  "sourceToolAssistantUUID": "155df436-12e4-4cbf-b838-9532bd58ea45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
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
  "leafUuid": "e042dca9-9cb9-44d0-b91d-10dd8518fa38",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Convert literature_map.yaml to references.bib",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f"
}
```

---

### Assistant

_source line 13 · 2026-05-15T18:12:34.697Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full literature_map.yaml. Let me parse all the paper entries and generate the BibTeX file. Let me also check what exists at the target directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e042dca9-9cb9-44d0-b91d-10dd8518fa38",
  "isSidechain": false,
  "requestId": "req_011Cb4okqutVuL3ANzbmQYDX",
  "type": "assistant",
  "uuid": "f39ba99c-b21a-4e05-9972-d8829010e2c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPJtkrMn2Aa1bLMp3Fu9Q6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15751,
      "cache_read_input_tokens": 23941,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 23941,
          "cache_creation_input_tokens": 15751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15751
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

_source line 14 · 2026-05-15T18:12:35.049Z_

Now let me check if the target directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f39ba99c-b21a-4e05-9972-d8829010e2c9",
  "isSidechain": false,
  "requestId": "req_011Cb4okqutVuL3ANzbmQYDX",
  "type": "assistant",
  "uuid": "f8a3dfd9-231e-4cc9-acd8-060e096de0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPJtkrMn2Aa1bLMp3Fu9Q6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15751,
      "cache_read_input_tokens": 23941,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 23941,
          "cache_creation_input_tokens": 15751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15751
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

_source line 15 · 2026-05-15T18:12:36.717Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R1wmZYBKLv4sh3u4A6JFKp`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8a3dfd9-231e-4cc9-acd8-060e096de0f5",
  "isSidechain": false,
  "requestId": "req_011Cb4okqutVuL3ANzbmQYDX",
  "type": "assistant",
  "uuid": "4281a07d-245f-4596-afc1-ccd01e64074e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPJtkrMn2Aa1bLMp3Fu9Q6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15751,
      "cache_read_input_tokens": 23941,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 23941,
          "cache_creation_input_tokens": 15751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15751
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

_source line 16 · 2026-05-15T18:12:36.877Z_

<details><summary>↩ Tool result · `toolu_01R1wmZYBKLv4sh3u4A6JFKp`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4281a07d-245f-4596-afc1-ccd01e64074e",
  "isSidechain": false,
  "promptId": "001f3045-7b6d-4759-9519-5b6e8b3c60f9",
  "type": "user",
  "uuid": "f5fd6f93-1797-4c21-a547-8b0902cf9663",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4281a07d-245f-4596-afc1-ccd01e64074e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T18:15:01.733Z_

<details><summary>Logged reasoning block</summary>

```text
The directory exists but is empty. Let me now generate the BibTeX file from the YAML data I've read. Let me carefully parse each entry.

Let me go through each paper:

1. shumailov2024curse - Nature → @article, journal=Nature
2. alemohammad2024mad - ICLR 2024 → @inproceedings, booktitle=ICLR
3. dohmatob2024tale - ICML 2024 → @inproceedings, booktitle=ICML


4. dohmatob2025strong - ICLR 2025 (Spotlight) → @inproceedings, booktitle=ICLR
5. guo2024linguistic - NAACL 2024 Findings → @inproceedings, booktitle=NAACL Findings
6. briesch2024selfconsuming - arXiv (2311.16822) → @article, journal=arXiv preprint arXiv:2311.16822
7. truong2025entropy - arXiv (2512.12381) → @article, journal=arXiv preprint arXiv:2512.12381
8. wang2026contaminated - arXiv (2602.16065) → @article, journal=arXiv preprint arXiv:2602.16065
9. du2026geometric - arXiv (2605.00435) → @article, journal=arXiv preprint arXiv:2605.00435
10. gauthier2026alignment - arXiv (2605.04266) → @article, journal=arXiv preprint arXiv:2605.04266
11. shi2026pruning - arXiv (2605.07271) → @article, journal=arXiv preprint arXiv:2605.07271
12. tubingen2026diffusion - arXiv (2605.06366) → @article, journal=arXiv preprint arXiv:2605.06366

Continuing to map out the remaining bibliography entries, converting each to the appropriate BibTeX format with their respective venues and identifiers. Continuing through the bibliography entries, mapping more papers to their proper citation formats—arXiv preprints with their identifiers, conference proceedings like SIGIR, NAACL, and ICLR with their respective years. Continuing through the bibliography entries, mapping the remaining papers to their proper BibTeX formats—arXiv preprints with their identifiers, conference proceedings for NeurIPS and ICML, and a journal article from Electronics. Now I'm working through the author formatting for the remaining entries, converting them to the "Last, First and Last, First" format. I've got the first few done, and I'm continuing with the rest of the list, handling cases where there are multiple authors or "et al." notations. I'm noticing these are Vietnamese names where Truong is the family name and Xuan Khanh and Quynh Hoa are the given names, so the formatting should reflect that. Moving on to the next entries like Wang, Kevin and Niu, Hongqian, though I'm uncertain about "Du, Tanaka-Ishii" since it appears to only have last names without the corresponding first names in the source data. Continuing through the author name formatting, converting the remaining entries to last name first format where applicable, handling multiple authors by listing them with "and" between each one, and using "and others" for et al. citations. I'm working through the author name formatting for Chinese names, trying to determine the correct family name order. For Li Jing, I need to verify whether it's "Jing, Li" or "Li, Jing" in western academic convention—looking at the actual publication records and BibTeX standards to get this right. Moving on to format the remaining authors in the list, starting with Lorenzo Noci and then the multi-author entry with Kazdan and others. I'm working through how to handle these Chinese names in western academic formatting. "Shi Fu" is ambiguous—it could be family-given or given-family order—but in western papers Chinese authors typically appear as "Family, Given," so I'll format it as Fu, Shi. Continuing with the same pattern for the other authors: Wang, Yingjie and Chen, Yuzhu and Tian, Xinmei and Tao, Dacheng. Moving on to the next entries with standard western name formatting. Continuing through the author name formatting—I'm converting the remaining entries to the standard "Last, First and Last, First" format, working through multi-author papers and handling the longer author lists by converting them to the proper citation style. and Vandermeer, John"

41. "Carl Boettiger, Alan Hastings"
    → "Boettiger, Carl and Hastings, Alan"

For entries with only last names provided, I'll need to work with what's given. Cases like "Du, Tanaka-Ishii" and "Gauthier, Bach, Jordan" appear to list authors by last name only, so I'll keep them in that format rather than trying to restructure them.

Now I'm handling the formatting for entries with "et al." — converting those to use "and others" in the author field. I also need to be mindful of special characters in titles, protecting capitalization with braces where necessary since BibTeX will lowercase titles by default depending on the citation style. Finally, I'm organizing everything into the three specified categories: core model collapse, canary metrics, and diversity. Now I'm working through how to handle the arXiv papers—I'll extract the ID from the venue field and use it in the journal field. For the URL and DOI fields, most papers have arXiv links, though a few older ones only have DOIs. For conference venues, I need to expand the abbreviations into full names for the booktitle field, like ICLR becomes International Conference on Learning Representations. I'm settling on standard conference name formats and need to be careful with capitalization, author formatting, and entry types. I'll protect acronyms and proper nouns in titles with braces to ensure they render correctly in BibTeX.

Writing out the bibliography entries... I'm continuing through the bibliography, completing the previous entry and adding several more papers on model collapse and synthetic data effects in language model training. Finishing up the bibliography entries on data contamination and mode collapse in language models... Finishing up the bibliography entries and realizing I need to be careful with how I format author names in BibTeX—when converting from YAML that just lists last names, I shouldn't add commas within the author field since those are reserved for separating last names from first names.

For institutional authors like Tübingen AI Center, I need to wrap them in double braces and use the proper LaTeX encoding for the umlaut, then add "and others" to indicate the et al. I should also make sure titles are properly protected depending on the bibliography style being used.

Now I'm reviewing the YAML structure to understand how the entries are organized by category—there's the core model collapse section, canary metrics, and diversity metrics—so I can make sure everything is properly formatted and categorized in the final BibTeX file. Looking at the rest of the YAML structure, I can see the categories continue with data mixing and accumulation papers, then mitigation and verification approaches, followed by position papers and epistemics work. There's also methodology sections covering Granger causality and lead-lag analysis, plus early warning signals that seem to be cut off. I'm seeing the structure now—the papers are organized by their comment sections in the YAML, with each section containing specific categories. I need to write out the BibTeX entries organized by these sections, handling the anonymous author entries appropriately. I'm working through the BibTeX formatting now, deciding how to standardize venue names across different conference types. For conference proceedings like NAACL, I'll use the full official names rather than shorthand, and I'm skipping prestige annotations like "Spotlight" since those aren't part of standard citations. Let me finalize the complete entry with consistent formatting for all the papers. I'm going through the bibliography entries now and need to be careful about which fields to use—some papers have DOIs but no URLs, while others only have arXiv links. Let me verify the exact structure of each entry before writing out the complete file. I'm also counting to make sure I have all 41 papers accounted for from the YAML. I'm tallying up the remaining categories: data mixing papers, mitigation strategies, position papers, methodology references, and early warning signals. That brings the total to 41 papers across all sections. Now I'm ready to write out the complete bibliography.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5fd6f93-1797-4c21-a547-8b0902cf9663",
  "isSidechain": false,
  "requestId": "req_011Cb4omLKgTFVv44FsQiUUB",
  "type": "assistant",
  "uuid": "0cfb9691-e60f-4d2d-8ad9-b93bcd6f548b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8dqezSHmdwbNTinVDENcB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 39692,
      "output_tokens": 14591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14591,
          "cache_read_input_tokens": 39692,
          "cache_creation_input_tokens": 187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 187
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

_source line 18 · 2026-05-15T18:15:01.735Z_

Now I'll generate the BibTeX file from all 41 entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cfb9691-e60f-4d2d-8ad9-b93bcd6f548b",
  "isSidechain": false,
  "requestId": "req_011Cb4omLKgTFVv44FsQiUUB",
  "type": "assistant",
  "uuid": "2ba67ade-b719-479b-9493-b19713e3bcec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8dqezSHmdwbNTinVDENcB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 39692,
      "output_tokens": 14591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14591,
          "cache_read_input_tokens": 39692,
          "cache_creation_input_tokens": 187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 187
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

_source line 19 · 2026-05-15T18:16:01.180Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Qjay3ZqWemAwkWqxrL8c4M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib",
  "content": "% ============================================================\n% CORE MODEL COLLAPSE\n% ============================================================\n\n@article{shumailov2024curse,\n  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},\n  journal   = {Nature},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2305.17493},\n}\n\n@inproceedings{alemohammad2024mad,\n  title     = {Self-Consuming Generative Models Go {MAD}},\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@inproceedings{dohmatob2024tale,\n  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025strong,\n  title     = {Strong Model Collapse},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{guo2024linguistic,\n  title     = {The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},\n  author    = {Guo, Yanzhu and Shang, Guokan and others},\n  booktitle = {Findings of the Association for Computational Linguistics: {NAACL}},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.09807},\n}\n\n@article{briesch2024selfconsuming,\n  title     = {Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},\n  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal   = {arXiv preprint arXiv:2311.16822},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.16822},\n}\n\n@article{truong2025entropy,\n  title     = {Entropy Collapse: A Universal Failure Mode of Intelligent Systems},\n  author    = {Truong, Xuan Khanh and Truong, Quynh Hoa},\n  journal   = {arXiv preprint arXiv:2512.12381},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2512.12381},\n}\n\n@article{wang2026contaminated,\n  title     = {Can Generative Artificial Intelligence Survive Data Contamination? {T}heoretical Guarantees under Contaminated Recursive Training},\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  journal   = {arXiv preprint arXiv:2602.16065},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@article{du2026geometric,\n  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},\n  author    = {Du and Tanaka-Ishii},\n  journal   = {arXiv preprint arXiv:2605.00435},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.00435},\n}\n\n@article{gauthier2026alignment,\n  title     = {Explaining and Preventing Alignment Collapse in Iterative {RLHF}},\n  author    = {Gauthier and Bach and Jordan},\n  journal   = {arXiv preprint arXiv:2605.04266},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.04266},\n}\n\n@article{shi2026pruning,\n  title     = {Understanding Performance Collapse in Layer-Pruned {LLMs} via Decision Representation Transitions},\n  author    = {Shi and others},\n  journal   = {arXiv preprint arXiv:2605.07271},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.07271},\n}\n\n@article{tubingen2026diffusion,\n  title     = {Layer Collapse in Diffusion Language Models},\n  author    = {{T{\\\"u}bingen AI Center} and others},\n  journal   = {arXiv preprint arXiv:2605.06366},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.06366},\n}\n\n% ============================================================\n% CANARY / EARLY WARNING METRICS\n% ============================================================\n\n@article{chen2025scales,\n  title     = {Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios},\n  author    = {{Anonymous}},\n  journal   = {arXiv preprint arXiv:2510.05133},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.05133},\n}\n\n@article{gambetta2024surplexity,\n  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author    = {Gambetta, Daniele and others},\n  journal   = {arXiv preprint arXiv:2410.12341},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.12341},\n}\n\n@article{qiu2025spectral,\n  title     = {Spectral Alignment as Predictor of Loss Explosion in Neural Network Training},\n  author    = {Qiu, Haiquan and Wu, You and Tan, Yingjie and Wang, Yaqing and Yao, Quanming},\n  journal   = {arXiv preprint arXiv:2510.04202},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.04202},\n}\n\n@inproceedings{he2025closer,\n  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author    = {He, Shiliang and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2509.16499},\n}\n\n@inproceedings{ba2024fill,\n  title     = {Fill In The Gaps: Model Calibration and Generalization with Synthetic Data},\n  author    = {Ba, Yang and Mancenido, Michelle V and Pan, Rong},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.10864},\n}\n\n@article{sigma2026spectral,\n  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  journal   = {arXiv preprint arXiv:2601.03385},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@article{kalinowski2026topology,\n  title     = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},\n  author    = {Kalinowski, Alexander},\n  journal   = {arXiv preprint arXiv:2604.26984},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2604.26984},\n}\n\n@article{bergsma2026scaling,\n  title     = {Scaling with Collapse: Efficient and Predictable Training of {LLM} Families},\n  author    = {Bergsma and others},\n  journal   = {arXiv preprint arXiv:2509.25087},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2509.25087},\n}\n\n% ============================================================\n% DIVERSITY METRICS (BACKGROUND)\n% ============================================================\n\n@inproceedings{zhu2018texygen,\n  title     = {{Texygen}: A Benchmarking Platform for Text Generation Models},\n  author    = {Zhu, Yaoming and others},\n  booktitle = {International {ACM} {SIGIR} Conference on Research and Development in Information Retrieval},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1802.01886},\n}\n\n@inproceedings{li2016diversity,\n  title     = {A Diversity-Promoting Objective Function for Neural Conversation Models},\n  author    = {Li, Jiwei and others},\n  booktitle = {North American Chapter of the Association for Computational Linguistics},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1510.03055},\n}\n\n% ============================================================\n% REPRESENTATION / SPECTRAL COLLAPSE\n% ============================================================\n\n@inproceedings{jing2022understanding,\n  title     = {Understanding Dimensional Collapse in Contrastive Self-supervised Learning},\n  author    = {Jing, Li and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://openreview.net/forum?id=YevsQ05DEN7},\n}\n\n@inproceedings{noci2024mind,\n  title     = {Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers},\n  author    = {Noci, Lorenzo and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.07799},\n}\n\n% ============================================================\n% DATA MIXING & ACCUMULATION\n% ============================================================\n\n@inproceedings{kazdan2025collapse,\n  title     = {Collapse or Thrive? {P}erils and Promises of Synthetic Data in a Self-Generating World},\n  author    = {Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.16713},\n}\n\n@inproceedings{dey2024breaking,\n  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author    = {Dey, Apratim and Donoho, David and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@article{epstein2024howbad,\n  title     = {How Bad is Training on Synthetic Data? {A} Statistical Analysis of Language Model Collapse},\n  author    = {Epstein, Mohamed El Amine and others},\n  journal   = {arXiv preprint arXiv:2404.05090},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n\n@inproceedings{fu2025selfconsuming,\n  title     = {A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops},\n  author    = {Fu, Shi and Wang, Yingjie and Chen, Yuzhu and Tian, Xinmei and Tao, Dacheng},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.18865},\n}\n\n@article{bakshi2026improvement,\n  title     = {From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources},\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  journal   = {arXiv preprint arXiv:2602.10531},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@article{he2025golden,\n  title     = {Golden Ratio Weighting Prevents Model Collapse},\n  author    = {He, Shiliang and Xu, Zhongbin and Cheng, Yan},\n  journal   = {arXiv preprint arXiv:2502.18049},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.18049},\n}\n\n@article{xu2025mixing,\n  title     = {Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios},\n  author    = {Xu, Zhongbin and Cheng, Yan},\n  journal   = {arXiv preprint arXiv:2509.22341},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2509.22341},\n}\n\n% ============================================================\n% MITIGATION & VERIFICATION\n% ============================================================\n\n@inproceedings{feng2025escaping,\n  title     = {Escaping Model Collapse via Synthetic Data Verification},\n  author    = {Feng, Yunzhen and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.16657},\n}\n\n@inproceedings{barzilai2025consistency,\n  title     = {When Models Don't Collapse: On the Consistency of Iterative {MLE}},\n  author    = {Barzilai, Daniel and Shamir, Ohad},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2505.19046},\n}\n\n@article{dces2026counter,\n  title     = {Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling},\n  author    = {{Anonymous}},\n  journal   = {Electronics},\n  year      = {2026},\n  url       = {https://www.mdpi.com/2079-9292/15/4/869},\n}\n\n% ============================================================\n% POSITION / SURVEY / EPISTEMICS\n% ============================================================\n\n@article{schaeffer2025position,\n  title     = {Position: Model Collapse Does Not Mean What You Think},\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n@article{wang2025epistemic,\n  title     = {Epistemic Diversity and Knowledge Collapse in Large Language Models},\n  author    = {Wang and others},\n  journal   = {arXiv preprint arXiv:2510.04226},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.04226},\n}\n\n% ============================================================\n% METHODOLOGY (GRANGER / LEAD-LAG)\n% ============================================================\n\n@article{shojaie2022granger,\n  title     = {{Granger} Causality: A Review and Recent Advances},\n  author    = {Shojaie, Ali and Fox, Emily B.},\n  journal   = {Annual Review of Statistics and Its Application},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2105.02675},\n}\n\n@article{marcinkevics2022neural,\n  title     = {{Granger} Causality Using Neural Networks},\n  author    = {Marcinkevics, Raphael and Vogt, Julia},\n  journal   = {arXiv preprint arXiv:2208.03703},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2208.03703},\n}\n\n% ============================================================\n% EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)\n% ============================================================\n\n@article{scheffer2009early,\n  title     = {Early-warning signals for critical transitions},\n  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},\n  journal   = {Nature},\n  year      = {2009},\n  doi       = {10.1038/nature08227},\n}\n\n@article{scheffer2012anticipating,\n  title     = {Anticipating Critical Transitions},\n  author    = {Scheffer, Marten and Carpenter, Stephen R. and Lenton, Timothy M. and Bascompte, Jordi and Brock, William and Dakos, Vasilis and van de Koppel, Johan and van de Leemput, Ingrid A. and Levin, Simon A. and van Nes, Egbert H. and Pascual, Mercedes and Vandermeer, John},\n  journal   = {Science},\n  year      = {2012},\n  doi       = {10.1126/science.1225244},\n}\n\n@article{boettiger2012limits,\n  title     = {Quantifying Limits to Detection of Early Warning for Critical Transitions},\n  author    = {Boettiger, Carl and Hastings, Alan},\n  journal   = {Journal of the Royal Society Interface},\n  year      = {2012},\n  doi       = {10.1098/rsif.2012.0125},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ba67ade-b719-479b-9493-b19713e3bcec",
  "isSidechain": false,
  "requestId": "req_011Cb4omLKgTFVv44FsQiUUB",
  "type": "assistant",
  "uuid": "a6ed3910-b0a2-4c14-819c-81420f108199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8dqezSHmdwbNTinVDENcB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 39692,
      "output_tokens": 14591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14591,
          "cache_read_input_tokens": 39692,
          "cache_creation_input_tokens": 187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 187
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

_source line 20 · 2026-05-15T18:16:01.201Z_

<details><summary>↩ Tool result · `toolu_01Qjay3ZqWemAwkWqxrL8c4M`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6ed3910-b0a2-4c14-819c-81420f108199",
  "isSidechain": false,
  "promptId": "001f3045-7b6d-4759-9519-5b6e8b3c60f9",
  "type": "user",
  "uuid": "f859d1d4-9f9f-4179-852e-69eef9e87458",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib",
    "content": "% ============================================================\n% CORE MODEL COLLAPSE\n% ============================================================\n\n@article{shumailov2024curse,\n  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},\n  journal   = {Nature},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2305.17493},\n}\n\n@inproceedings{alemohammad2024mad,\n  title     = {Self-Consuming Generative Models Go {MAD}},\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@inproceedings{dohmatob2024tale,\n  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025strong,\n  title     = {Strong Model Collapse},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{guo2024linguistic,\n  title     = {The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},\n  author    = {Guo, Yanzhu and Shang, Guokan and others},\n  booktitle = {Findings of the Association for Computational Linguistics: {NAACL}},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.09807},\n}\n\n@article{briesch2024selfconsuming,\n  title     = {Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},\n  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal   = {arXiv preprint arXiv:2311.16822},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.16822},\n}\n\n@article{truong2025entropy,\n  title     = {Entropy Collapse: A Universal Failure Mode of Intelligent Systems},\n  author    = {Truong, Xuan Khanh and Truong, Quynh Hoa},\n  journal   = {arXiv preprint arXiv:2512.12381},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2512.12381},\n}\n\n@article{wang2026contaminated,\n  title     = {Can Generative Artificial Intelligence Survive Data Contamination? {T}heoretical Guarantees under Contaminated Recursive Training},\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  journal   = {arXiv preprint arXiv:2602.16065},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@article{du2026geometric,\n  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},\n  author    = {Du and Tanaka-Ishii},\n  journal   = {arXiv preprint arXiv:2605.00435},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.00435},\n}\n\n@article{gauthier2026alignment,\n  title     = {Explaining and Preventing Alignment Collapse in Iterative {RLHF}},\n  author    = {Gauthier and Bach and Jordan},\n  journal   = {arXiv preprint arXiv:2605.04266},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.04266},\n}\n\n@article{shi2026pruning,\n  title     = {Understanding Performance Collapse in Layer-Pruned {LLMs} via Decision Representation Transitions},\n  author    = {Shi and others},\n  journal   = {arXiv preprint arXiv:2605.07271},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.07271},\n}\n\n@article{tubingen2026diffusion,\n  title     = {Layer Collapse in Diffusion Language Models},\n  author    = {{T{\\\"u}bingen AI Center} and others},\n  journal   = {arXiv preprint arXiv:2605.06366},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.06366},\n}\n\n% ============================================================\n% CANARY / EARLY WARNING METRICS\n% ============================================================\n\n@article{chen2025scales,\n  title     = {Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios},\n  author    = {{Anonymous}},\n  journal   = {arXiv preprint arXiv:2510.05133},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.05133},\n}\n\n@article{gambetta2024surplexity,\n  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author    = {Gambetta, Daniele and others},\n  journal   = {arXiv preprint arXiv:2410.12341},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.12341},\n}\n\n@article{qiu2025spectral,\n  title     = {Spectral Alignment as Predictor of Loss Explosion in Neural Network Training},\n  author    = {Qiu, Haiquan and Wu, You and Tan, Yingjie and Wang, Yaqing and Yao, Quanming},\n  journal   = {arXiv preprint arXiv:2510.04202},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.04202},\n}\n\n@inproceedings{he2025closer,\n  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author    = {He, Shiliang and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2509.16499},\n}\n\n@inproceedings{ba2024fill,\n  title     = {Fill In The Gaps: Model Calibration and Generalization with Synthetic Data},\n  author    = {Ba, Yang and Mancenido, Michelle V and Pan, Rong},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.10864},\n}\n\n@article{sigma2026spectral,\n  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  journal   = {arXiv preprint arXiv:2601.03385},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@article{kalinowski2026topology,\n  title     = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},\n  author    = {Kalinowski, Alexander},\n  journal   = {arXiv preprint arXiv:2604.26984},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2604.26984},\n}\n\n@article{bergsma2026scaling,\n  title     = {Scaling with Collapse: Efficient and Predictable Training of {LLM} Families},\n  author    = {Bergsma and others},\n  journal   = {arXiv preprint arXiv:2509.25087},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2509.25087},\n}\n\n% ============================================================\n% DIVERSITY METRICS (BACKGROUND)\n% ============================================================\n\n@inproceedings{zhu2018texygen,\n  title     = {{Texygen}: A Benchmarking Platform for Text Generation Models},\n  author    = {Zhu, Yaoming and others},\n  booktitle = {International {ACM} {SIGIR} Conference on Research and Development in Information Retrieval},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1802.01886},\n}\n\n@inproceedings{li2016diversity,\n  title     = {A Diversity-Promoting Objective Function for Neural Conversation Models},\n  author    = {Li, Jiwei and others},\n  booktitle = {North American Chapter of the Association for Computational Linguistics},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1510.03055},\n}\n\n% ============================================================\n% REPRESENTATION / SPECTRAL COLLAPSE\n% ============================================================\n\n@inproceedings{jing2022understanding,\n  title     = {Understanding Dimensional Collapse in Contrastive Self-supervised Learning},\n  author    = {Jing, Li and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://openreview.net/forum?id=YevsQ05DEN7},\n}\n\n@inproceedings{noci2024mind,\n  title     = {Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers},\n  author    = {Noci, Lorenzo and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.07799},\n}\n\n% ============================================================\n% DATA MIXING & ACCUMULATION\n% ============================================================\n\n@inproceedings{kazdan2025collapse,\n  title     = {Collapse or Thrive? {P}erils and Promises of Synthetic Data in a Self-Generating World},\n  author    = {Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.16713},\n}\n\n@inproceedings{dey2024breaking,\n  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author    = {Dey, Apratim and Donoho, David and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@article{epstein2024howbad,\n  title     = {How Bad is Training on Synthetic Data? {A} Statistical Analysis of Language Model Collapse},\n  author    = {Epstein, Mohamed El Amine and others},\n  journal   = {arXiv preprint arXiv:2404.05090},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n\n@inproceedings{fu2025selfconsuming,\n  title     = {A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops},\n  author    = {Fu, Shi and Wang, Yingjie and Chen, Yuzhu and Tian, Xinmei and Tao, Dacheng},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.18865},\n}\n\n@article{bakshi2026improvement,\n  title     = {From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources},\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  journal   = {arXiv preprint arXiv:2602.10531},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@article{he2025golden,\n  title     = {Golden Ratio Weighting Prevents Model Collapse},\n  author    = {He, Shiliang and Xu, Zhongbin and Cheng, Yan},\n  journal   = {arXiv preprint arXiv:2502.18049},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.18049},\n}\n\n@article{xu2025mixing,\n  title     = {Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios},\n  author    = {Xu, Zhongbin and Cheng, Yan},\n  journal   = {arXiv preprint arXiv:2509.22341},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2509.22341},\n}\n\n% ============================================================\n% MITIGATION & VERIFICATION\n% ============================================================\n\n@inproceedings{feng2025escaping,\n  title     = {Escaping Model Collapse via Synthetic Data Verification},\n  author    = {Feng, Yunzhen and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.16657},\n}\n\n@inproceedings{barzilai2025consistency,\n  title     = {When Models Don't Collapse: On the Consistency of Iterative {MLE}},\n  author    = {Barzilai, Daniel and Shamir, Ohad},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2505.19046},\n}\n\n@article{dces2026counter,\n  title     = {Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling},\n  author    = {{Anonymous}},\n  journal   = {Electronics},\n  year      = {2026},\n  url       = {https://www.mdpi.com/2079-9292/15/4/869},\n}\n\n% ============================================================\n% POSITION / SURVEY / EPISTEMICS\n% ============================================================\n\n@article{schaeffer2025position,\n  title     = {Position: Model Collapse Does Not Mean What You Think},\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n@article{wang2025epistemic,\n  title     = {Epistemic Diversity and Knowledge Collapse in Large Language Models},\n  author    = {Wang and others},\n  journal   = {arXiv preprint arXiv:2510.04226},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.04226},\n}\n\n% ============================================================\n% METHODOLOGY (GRANGER / LEAD-LAG)\n% ============================================================\n\n@article{shojaie2022granger,\n  title     = {{Granger} Causality: A Review and Recent Advances},\n  author    = {Shojaie, Ali and Fox, Emily B.},\n  journal   = {Annual Review of Statistics and Its Application},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2105.02675},\n}\n\n@article{marcinkevics2022neural,\n  title     = {{Granger} Causality Using Neural Networks},\n  author    = {Marcinkevics, Raphael and Vogt, Julia},\n  journal   = {arXiv preprint arXiv:2208.03703},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2208.03703},\n}\n\n% ============================================================\n% EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)\n% ============================================================\n\n@article{scheffer2009early,\n  title     = {Early-warning signals for critical transitions},\n  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},\n  journal   = {Nature},\n  year      = {2009},\n  doi       = {10.1038/nature08227},\n}\n\n@article{scheffer2012anticipating,\n  title     = {Anticipating Critical Transitions},\n  author    = {Scheffer, Marten and Carpenter, Stephen R. and Lenton, Timothy M. and Bascompte, Jordi and Brock, William and Dakos, Vasilis and van de Koppel, Johan and van de Leemput, Ingrid A. and Levin, Simon A. and van Nes, Egbert H. and Pascual, Mercedes and Vandermeer, John},\n  journal   = {Science},\n  year      = {2012},\n  doi       = {10.1126/science.1225244},\n}\n\n@article{boettiger2012limits,\n  title     = {Quantifying Limits to Detection of Early Warning for Critical Transitions},\n  author    = {Boettiger, Carl and Hastings, Alan},\n  journal   = {Journal of the Royal Society Interface},\n  year      = {2012},\n  doi       = {10.1098/rsif.2012.0125},\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "a6ed3910-b0a2-4c14-819c-81420f108199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "leafUuid": "f859d1d4-9f9f-4179-852e-69eef9e87458",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Convert literature_map.yaml to references.bib",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f"
}
```

---

### Assistant

_source line 23 · 2026-05-15T18:16:04.073Z_

验证括号匹配和条目数量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f859d1d4-9f9f-4179-852e-69eef9e87458",
  "isSidechain": false,
  "requestId": "req_011Cb4p2Pv9SX6ZVcyzBeo9k",
  "type": "assistant",
  "uuid": "4e018ad9-3722-4829-9076-8105567bfb05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HqqqQSk4Jb5bAAw8oYBLmF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14630,
      "cache_read_input_tokens": 39879,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 39879,
          "cache_creation_input_tokens": 14630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14630
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

_source line 24 · 2026-05-15T18:16:08.253Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01C26DtHZkVMcMs7y76PxfSp`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper && python3 -c \"\nimport re\n\nwith open('references.bib') as f:\n    content = f.read()\n\n# Count entries\nentries = re.findall(r'@(article|inproceedings)\\{(\\w+)', content)\nprint(f'Total entries: {len(entries)}')\nfor typ, key in entries:\n    print(f'  @{typ}{{{key}}}')\n\n# Check brace balance\ndepth = 0\nfor i, ch in enumerate(content):\n    if ch == '{':\n        depth += 1\n    elif ch == '}':\n        depth -= 1\n    if depth < 0:\n        line = content[:i].count('\\n') + 1\n        print(f'ERROR: unmatched closing brace at line {line}')\n        break\n\nif depth == 0:\n    print('\\nBrace balance: OK')\nelse:\n    print(f'\\nBrace balance: MISMATCH (depth={depth})')\n\"\n",
  "description": "Validate BibTeX brace balance and entry count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e018ad9-3722-4829-9076-8105567bfb05",
  "isSidechain": false,
  "requestId": "req_011Cb4p2Pv9SX6ZVcyzBeo9k",
  "type": "assistant",
  "uuid": "61debc74-c0b4-47fa-98a1-83ac32dedf45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HqqqQSk4Jb5bAAw8oYBLmF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14630,
      "cache_read_input_tokens": 39879,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 39879,
          "cache_creation_input_tokens": 14630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14630
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

_source line 25 · 2026-05-15T18:16:08.334Z_

<details><summary>↩ Tool result · `toolu_01C26DtHZkVMcMs7y76PxfSp`</summary>

```text
Total entries: 41
  @article{shumailov2024curse}
  @inproceedings{alemohammad2024mad}
  @inproceedings{dohmatob2024tale}
  @inproceedings{dohmatob2025strong}
  @inproceedings{guo2024linguistic}
  @article{briesch2024selfconsuming}
  @article{truong2025entropy}
  @article{wang2026contaminated}
  @article{du2026geometric}
  @article{gauthier2026alignment}
  @article{shi2026pruning}
  @article{tubingen2026diffusion}
  @article{chen2025scales}
  @article{gambetta2024surplexity}
  @article{qiu2025spectral}
  @inproceedings{he2025closer}
  @inproceedings{ba2024fill}
  @article{sigma2026spectral}
  @article{kalinowski2026topology}
  @article{bergsma2026scaling}
  @inproceedings{zhu2018texygen}
  @inproceedings{li2016diversity}
  @inproceedings{jing2022understanding}
  @inproceedings{noci2024mind}
  @inproceedings{kazdan2025collapse}
  @inproceedings{dey2024breaking}
  @article{epstein2024howbad}
  @inproceedings{fu2025selfconsuming}
  @article{bakshi2026improvement}
  @article{he2025golden}
  @article{xu2025mixing}
  @inproceedings{feng2025escaping}
  @inproceedings{barzilai2025consistency}
  @article{dces2026counter}
  @article{schaeffer2025position}
  @article{wang2025epistemic}
  @article{shojaie2022granger}
  @article{marcinkevics2022neural}
  @article{scheffer2009early}
  @article{scheffer2012anticipating}
  @article{boettiger2012limits}

Brace balance: OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61debc74-c0b4-47fa-98a1-83ac32dedf45",
  "isSidechain": false,
  "promptId": "001f3045-7b6d-4759-9519-5b6e8b3c60f9",
  "type": "user",
  "uuid": "a8d0345d-47ab-4519-a760-b2a2e0da06d6",
  "toolUseResult": {
    "stdout": "Total entries: 41\n  @article{shumailov2024curse}\n  @inproceedings{alemohammad2024mad}\n  @inproceedings{dohmatob2024tale}\n  @inproceedings{dohmatob2025strong}\n  @inproceedings{guo2024linguistic}\n  @article{briesch2024selfconsuming}\n  @article{truong2025entropy}\n  @article{wang2026contaminated}\n  @article{du2026geometric}\n  @article{gauthier2026alignment}\n  @article{shi2026pruning}\n  @article{tubingen2026diffusion}\n  @article{chen2025scales}\n  @article{gambetta2024surplexity}\n  @article{qiu2025spectral}\n  @inproceedings{he2025closer}\n  @inproceedings{ba2024fill}\n  @article{sigma2026spectral}\n  @article{kalinowski2026topology}\n  @article{bergsma2026scaling}\n  @inproceedings{zhu2018texygen}\n  @inproceedings{li2016diversity}\n  @inproceedings{jing2022understanding}\n  @inproceedings{noci2024mind}\n  @inproceedings{kazdan2025collapse}\n  @inproceedings{dey2024breaking}\n  @article{epstein2024howbad}\n  @inproceedings{fu2025selfconsuming}\n  @article{bakshi2026improvement}\n  @article{he2025golden}\n  @article{xu2025mixing}\n  @inproceedings{feng2025escaping}\n  @inproceedings{barzilai2025consistency}\n  @article{dces2026counter}\n  @article{schaeffer2025position}\n  @article{wang2025epistemic}\n  @article{shojaie2022granger}\n  @article{marcinkevics2022neural}\n  @article{scheffer2009early}\n  @article{scheffer2012anticipating}\n  @article{boettiger2012limits}\n\nBrace balance: OK",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "61debc74-c0b4-47fa-98a1-83ac32dedf45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T18:16:11.777Z_

41 条全部写入，括号匹配无误。文件按 9 个 category 分组，BibTeX key 与 literature_map.yaml 中的 id 一一对应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8d0345d-47ab-4519-a760-b2a2e0da06d6",
  "isSidechain": false,
  "requestId": "req_011Cb4p2vQxJQH18JTJiUqjy",
  "type": "assistant",
  "uuid": "9e2401e9-ac1b-42fd-b8eb-b27de492bf0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTXMuNr7hf6zMak6eweBni",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 54509,
      "output_tokens": 55,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 55,
          "cache_read_input_tokens": 54509,
          "cache_creation_input_tokens": 909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 909
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
  "leafUuid": "9e2401e9-ac1b-42fd-b8eb-b27de492bf0b",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Convert literature_map.yaml to references.bib",
  "sessionId": "7eceecc6-27de-492e-95ec-2cafddf74c7f"
}
```

---
