# Research conversation: <project_context> # 项目: schema-dag-extraction ## 运行环境 - 服务器名: cqa1-38874 - SSH 账户: root（调用 ssh_execute / submit_training

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/0e2349f2-4207-4d96-b1ce-1cf37c2379e5.jsonl`
- **Structured JSON:** [`79d7790f858e54ba53db.json`](../../sessions/79/79d7790f858e54ba53db.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T17:10:38.773Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T17:10:38.773Z",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "content": "&lt;project_context>\n# 项目: schema-dag-extraction\n\n## 运行环境\n- 服务器名: cqa1-38874\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/schema-dag-extraction\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：构建 references.bib\n\n从 literature_map.yaml 和 references_survey.md 构建完整的 BibTeX 文件。\n\n### 输入文件\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml` — 30 条文献条目（含 id, title, venue, year, url）\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md` — 30 篇论文的详细引用信息（含 authors, venue, arXiv/DOI）\n\n### 输出文件\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib`\n\n### 要求\n1. 读取两个输入文件，合并所有唯一论文\n2. 为每篇论文生成标准 BibTeX entry：\n   - bibtex_key 使用 literature_map 中的 `id` 字段（如 `llm-pee-2025`, `uniner-2024`）\n   - 类型：有正式 venue → `@inproceedings` 或 `@article`；arXiv only → `@article`\n   - 必须字段：title, author, year, booktitle/journal, url\n   - 可选字段：doi, pages, volume\n3. **引用信息优先用 references_survey.md**（更详细），literature_map 作为补充\n4. references_survey.md 中有但 literature_map 中没有的论文也要加入（如 InstructUIE, CodeIE, ADELIE, OneKE, GENRE, iNERD, NoiseBench, LRN, GenRES, MultiCoNER2, LLM confidence survey, FaR, LinkNER）\n5. 为 references_survey 中新发现的论文生成合理的 bibtex_key（如 `instructuie-2023`, `codeie-2023`, `adelie-2024`, `oneke-2025`, `genre-2021`, `inerd-2024`, `noisebench-2024`, `lrn-2021`, `genres-2024`, `multiconner2-2023`, `llm-calibration-survey-2024`, `far-calibration-2024`, `linkner-2024`）\n6. 总计应有 ~35-40 个 BibTeX entries\n\n### 格式示例\n```bibtex\n@inproceedings{llm-pee-2025,\n    title = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year = {2025},\n    url = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n```\n\n### 验证\n生成后统计 entry 数量，确保 ≥ 30。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T17:10:38.800Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T17:10:38.800Z",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

## Round 1

59 recorded events

### User

_source line 3 · 2026-05-15T17:10:38.981Z_

&lt;project_context>
# 项目: schema-dag-extraction

## 运行环境
- 服务器名: cqa1-38874
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/schema-dag-extraction


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：构建 references.bib

从 literature_map.yaml 和 references_survey.md 构建完整的 BibTeX 文件。

### 输入文件
1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml` — 30 条文献条目（含 id, title, venue, year, url）
2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md` — 30 篇论文的详细引用信息（含 authors, venue, arXiv/DOI）

### 输出文件
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib`

### 要求
1. 读取两个输入文件，合并所有唯一论文
2. 为每篇论文生成标准 BibTeX entry：
   - bibtex_key 使用 literature_map 中的 `id` 字段（如 `llm-pee-2025`, `uniner-2024`）
   - 类型：有正式 venue → `@inproceedings` 或 `@article`；arXiv only → `@article`
   - 必须字段：title, author, year, booktitle/journal, url
   - 可选字段：doi, pages, volume
3. **引用信息优先用 references_survey.md**（更详细），literature_map 作为补充
4. references_survey.md 中有但 literature_map 中没有的论文也要加入（如 InstructUIE, CodeIE, ADELIE, OneKE, GENRE, iNERD, NoiseBench, LRN, GenRES, MultiCoNER2, LLM confidence survey, FaR, LinkNER）
5. 为 references_survey 中新发现的论文生成合理的 bibtex_key（如 `instructuie-2023`, `codeie-2023`, `adelie-2024`, `oneke-2025`, `genre-2021`, `inerd-2024`, `noisebench-2024`, `lrn-2021`, `genres-2024`, `multiconner2-2023`, `llm-calibration-survey-2024`, `far-calibration-2024`, `linkner-2024`）
6. 总计应有 ~35-40 个 BibTeX entries

### 格式示例
```bibtex
@inproceedings{llm-pee-2025,
    title = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
    author = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
    year = {2025},
    url = {https://aclanthology.org/2025.emnlp-main.1743/},
}
```

### 验证
生成后统计 entry 数量，确保 ≥ 30。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "95a4176a-8df6-4b90-89cb-eab6bb5c6e99",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T17:10:38.980Z_

```json
{
  "parentUuid": "95a4176a-8df6-4b90-89cb-eab6bb5c6e99",
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
  "uuid": "eafc61c7-4e59-44a6-94d2-e992a7acbb02",
  "timestamp": "2026-05-15T17:10:38.980Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T17:10:38.980Z_

```json
{
  "parentUuid": "eafc61c7-4e59-44a6-94d2-e992a7acbb02",
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
  "uuid": "f9976f83-0af5-4b0f-87d5-5a46fd81e623",
  "timestamp": "2026-05-15T17:10:38.980Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T17:10:38.980Z_

```json
{
  "parentUuid": "f9976f83-0af5-4b0f-87d5-5a46fd81e623",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cac80550-dfee-4524-8253-eec9bd180be1",
  "timestamp": "2026-05-15T17:10:38.980Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
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
  "aiTitle": "Build BibTeX references from YAML and Markdown",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Assistant

_source line 8 · 2026-05-15T17:10:41.141Z_

Let me read both input files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cac80550-dfee-4524-8253-eec9bd180be1",
  "isSidechain": false,
  "requestId": "req_011Cb4j3GxPdpvEcK91mQXL5",
  "type": "assistant",
  "uuid": "b5c06b67-7190-404e-80ec-6ee4b45a7cf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQ3t1GeLG9YNNr3sF5PyW7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12048,
      "cache_read_input_tokens": 11841,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12048,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 165,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12048
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

_source line 9 · 2026-05-15T17:10:41.697Z_

<details open><summary>🔧 Tool call — Read · `toolu_018an7fJY4aEWLYakLm78EF5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5c06b67-7190-404e-80ec-6ee4b45a7cf9",
  "isSidechain": false,
  "requestId": "req_011Cb4j3GxPdpvEcK91mQXL5",
  "type": "assistant",
  "uuid": "689c0c19-6076-4301-861e-94023b02d4cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQ3t1GeLG9YNNr3sF5PyW7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12048,
      "cache_read_input_tokens": 11841,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12048,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 165,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12048
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

_source line 10 · 2026-05-15T17:10:41.741Z_

<details><summary>↩ Tool result · `toolu_018an7fJY4aEWLYakLm78EF5`</summary>

```text
1	# Literature Map for schema-dag-extraction
2	# Updated: 2026-05-15
3	# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE
4	
5	# =============================================================================
6	# DIRECT COMPETITORS — schema decomposition for LLM-based IE
7	# =============================================================================
8	
9	- id: llm-pee-2025
10	  title: "Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction"
11	  year: 2025
12	  venue: arXiv
13	  url: https://arxiv.org/abs/2503.02628
14	  role: direct-competitor
15	  relevance_note: >
16	    Similarity-based type recall + type-partitioning prompting for massive event types.
17	    Divides candidate types into partitions to reduce prompt length.
18	    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.
19	    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.
20	    Our DAG decomposition is confusability-driven, not just similarity-driven.
21	
22	- id: parse-2025
23	  title: "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction"
24	  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]
25	  year: 2025
26	  venue: EMNLP 2025 Industry
27	  url: https://arxiv.org/abs/2510.08623
28	  role: direct-competitor
29	  relevance_note: >
30	    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.
31	    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.
32	    Treats schema optimization as black-box LLM rewriting, not principled decomposition.
33	    Does NOT model type confusability explicitly.
34	
35	- id: dee-2024
36	  title: "Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs"
37	  year: 2024
38	  venue: arXiv
39	  url: https://arxiv.org/abs/2406.01045
40	  role: direct-competitor
41	  relevance_note: >
42	    Decomposes event extraction into detection + argument extraction.
43	    Dynamic schema-aware RAG for augmented prompts.
44	    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.
45	
46	- id: crossagentie-2025
47	  title: "CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE"
48	  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]
49	  year: 2025
50	  venue: ACL 2025 Findings
51	  url: https://aclanthology.org/2025.findings-acl.718/
52	  role: direct-competitor
53	  relevance_note: >
54	    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)
55	    + inter-group cross-task debate (NER↔RE mutual refinement).
56	    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.
57	    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.
58	    Must clearly differentiate in paper.
59	
60	- id: dlisc-2025
61	  title: "Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs"
62	  year: 2025
63	  venue: arXiv (May 2025)
64	  url: https://arxiv.org/abs/2505.14992
65	  role: direct-competitor
66	  relevance_note: >
67	    Dual-LoRA with Incremental Schema Caching.
68	    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.
69	    Focus on efficiency for on-device LLMs, not confusability analysis.
70	
71	- id: spt-2025
72	  title: "Schema as Parameterized Tools for Universal Information Extraction"
73	  year: 2025
74	  venue: arXiv (June 2025)
75	  url: https://arxiv.org/abs/2506.01276
76	  role: direct-competitor
77	  relevance_note: >
78	    Treats schemas as parameterized tools for LLM tool-calling.
79	    Schema retrieval + generation + infilling. Novel schema-LLM interface.
80	    Does not address type confusability.
81	
82	- id: zeroner-2025
83	  title: "ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions"
84	  year: 2025
85	  venue: ACL 2025 Findings
86	  url: https://aclanthology.org/2025.findings-acl.805/
87	  role: direct-competitor
88	  relevance_note: >
89	    Description-driven: LLM supervision → BERT student for unseen types.
90	    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.
91	    Related to how schema semantics affect extraction quality.
92	
93	- id: cmas-ner-2025
94	  title: "A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition"
95	  year: 2025
96	  venue: TheWebConf 2025
97	  url: https://dl.acm.org/doi/10.1145/3696410.3714923
98	  role: direct-competitor
99	  relevance_note: >
100	    Multi-agent collective intelligence for zero-shot NER.
101	    Addresses context correlation and indiscriminate demonstration problems.
102	    Outperforms on 6 benchmarks including domain-specific and general-domain.
103	
104	# =============================================================================
105	# METHOD COMPONENTS — techniques we build upon or relate to
106	# =============================================================================
107	
108	- id: uniner-2024
109	  title: "UniversalNER: Targeted Distillation from Large Language Models for Open NER"
110	  authors: [Wenxuan Zhou et al.]
111	  year: 2024
112	  venue: ICLR 2024
113	  url: https://arxiv.org/abs/2308.03279
114	  role: method-component
115	  relevance_note: >
116	    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.
117	    UniNER-7B outperforms ChatGPT by 7 F1 points.
118	    Important baseline for universal NER and schema-at-scale challenges.
119	
120	- id: gollie-2024
121	  title: "GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction"
122	  authors: [Oscar Sainz et al.]
123	  year: 2024
124	  venue: ICLR 2024
125	  url: https://hitz-zentroa.github.io/GoLLIE/
126	  role: method-component
127	  relevance_note: >
128	    Code-style schema definitions + annotation guideline following.
129	    Strong zero-shot on unseen IE tasks. Code-Llama based.
130	    Baseline for guideline-driven schema representation.
131	
132	- id: gliner-2024
133	  title: "GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer"
134	  authors: [Urchade Zaratiana et al.]
135	  year: 2024
136	  venue: NAACL 2024
137	  url: https://arxiv.org/abs/2311.08526
138	  role: method-component
139	  relevance_note: >
140	    Compact bidirectional encoder for zero-shot NER with parallel extraction.
141	    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.
142	
143	- id: gliner2-2025
144	  title: "GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface"
145	  authors: [Urchade Zaratiana et al.]
146	  year: 2025
147	  venue: EMNLP 2025 Demo
148	  url: https://arxiv.org/abs/2507.18546
149	  role: method-component
150	  relevance_note: >
151	    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.
152	    Schema-driven interface. Shows schema approach scales to multi-task.
153	
154	- id: kggen-2025
155	  title: "KGGen: Extracting Knowledge Graphs from Plain Text with Language Models"
156	  authors: [Mo et al.]
157	  year: 2025
158	  venue: NeurIPS 2025
159	  url: https://arxiv.org/abs/2502.09956
160	  role: method-component
161	  relevance_note: >
162	    Two-stage decomposition: entities first, then relations.
163	    Entity clustering/deduplication to reduce graph sparsity.
164	    Schema decomposition approach for KG construction.
165	
166	- id: code4uie-2024
167	  title: "Retrieval-Augmented Code Generation for Universal Information Extraction"
168	  authors: [Yucan Guo et al.]
169	  year: 2024
170	  venue: NeurIPS 2024 Workshop
171	  url: https://arxiv.org/abs/2311.02962
172	  role: method-component
173	  relevance_note: >
174	    Python class-based schema definitions + RAG for code generation.
175	    Unified code-style schema for all IE tasks.
176	
177	- id: iepile-2024
178	  title: "IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus"
179	  authors: [Guanzheng Chen et al., ZJU NLP]
180	  year: 2024
181	  venue: ACL 2024
182	  url: https://arxiv.org/abs/2402.14710
183	  role: method-component
184	  relevance_note: >
185	    0.32B token bilingual IE corpus. Hard negative schema construction =
186	    semantically proximate schemas to train type discrimination.
187	    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.
188	    Our contribution is inference-time confusability-aware decomposition (training-free).
189	
190	- id: lost-in-middle-2024
191	  title: "Lost in the Middle: How Language Models Use Long Contexts"
192	  authors: [Nelson F. Liu et al.]
193	  year: 2024
194	  venue: TACL 2024
195	  url: https://arxiv.org/abs/2307.03172
196	  role: method-component
197	  relevance_note: >
198	    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).
199	    Motivates schema decomposition to reduce prompt length.
200	    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.
201	
202	# =============================================================================
203	# ZERO-SHOT NER / RE BASELINES
204	# =============================================================================
205	
206	- id: self-improve-ner-2024
207	  title: "Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models"
208	  year: 2024
209	  venue: NAACL 2024
210	  url: https://arxiv.org/abs/2311.08921
211	  role: background
212	  relevance_note: >
213	    Self-improving framework using LLM self-generated examples for zero-shot NER.
214	
215	- id: self-prompting-re-2024
216	  title: "Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting"
217	  year: 2024
218	  venue: EMNLP 2024 Findings
219	  url: https://arxiv.org/abs/2410.01154
220	  role: background
221	  relevance_note: >
222	    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.
223	    Training-free RE baseline.
224	
225	- id: reasoning-ner-2025
226	  title: "A Reasoning Paradigm for Named Entity Recognition"
227	  year: 2025
228	  venue: arXiv (Nov 2025)
229	  url: https://arxiv.org/abs/2511.11978
230	  role: background
231	  relevance_note: >
232	    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.
233	    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.
234	
235	- id: nuner-2024
236	  title: "NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data"
237	  authors: [Sergei Bogdanov et al., NuMind]
238	  year: 2024
239	  venue: EMNLP 2024
240	  url: https://arxiv.org/abs/2402.15343
241	  role: background
242	  relevance_note: >
243	    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.
244	
245	# =============================================================================
246	# EVALUATION / BENCHMARKING
247	# =============================================================================
248	
249	- id: familiarity-2025
250	  title: "Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data"
251	  year: 2025
252	  venue: NAACL 2025
253	  url: https://arxiv.org/abs/2412.10121
254	  role: evaluation
255	  relevance_note: >
256	    "Familiarity" metric for label shift in synthetic NER data.
257	    Zero-shot NER scores overestimated due to train-eval label overlap.
258	    Quantifies semantic similarity between entity types — related to type confusability.
259	    KEY DIFF: measures evaluation bias, not extraction-time confusability.
260	
261	- id: guidex-2025
262	  title: "GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction"
263	  authors: [Neil Deshpande et al.]
264	  year: 2025
265	  venue: ACL 2025 Findings
266	  url: https://arxiv.org/abs/2506.00649
267	  role: evaluation
268	  relevance_note: >
269	    Auto-generates domain-specific schemas + guidelines + synthetic labels.
270	    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.
271	
272	# =============================================================================
273	# SURVEYS
274	# =============================================================================
275	
276	- id: llm4ie-survey-2024
277	  title: "Large Language Models for Generative Information Extraction: A Survey"
278	  authors: [Derong Xu et al.]
279	  year: 2024
280	  venue: Frontiers of Computer Science
281	  url: https://arxiv.org/abs/2312.17617
282	  role: background
283	  relevance_note: >
284	    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.
285	
286	- id: knowcoder-2024
287	  title: "KnowCoder: Coding Structured Knowledge into LLMs for Universal IE"
288	  year: 2024
289	  venue: ACL 2024
290	  url: https://arxiv.org/abs/2403.07969
291	  role: background
292	  relevance_note: >
293	    Encodes schema knowledge via code structures into LLM.
294	    Related to code-based schema representation.
295	
296	- id: slot-2025
297	  title: "SLOT: Structuring the Output of Large Language Models"
298	  year: 2025
299	  venue: EMNLP 2025 Industry
300	  url: https://aclanthology.org/2025.emnlp-industry.32.pdf
301	  role: background
302	  relevance_note: >
303	    Decouples output formatting from NL task. Model-agnostic structured output.
304	
305	# =============================================================================
306	# EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION
307	# — supports "domain boundary" finding: BCS proxy fails for same-domain schemas
308	# =============================================================================
309	
310	- id: gao-repr-degen-2019
311	  title: "Representation Degeneration Problem in Training Natural Language Generation Models"
312	  authors: [Jun Gao, Di He, Hang Li, Xin Jiang]
313	  year: 2019
314	  venue: ICLR 2019
315	  url: https://arxiv.org/abs/1907.12009
316	  role: theoretical-foundation
317	  relevance_note: >
318	    FOUNDATIONAL. Shows that likelihood maximization + weight tying causes word embeddings
319	    to degenerate into a narrow cone with uniformly high cosine similarity.
320	    Proposed cosine regularization (MLE-CosReg) to widen the cone aperture.
321	    LINK TO OUR WORK: This is the root mechanism behind BCS compression.
322	    When Qwen3-32B encodes 168 same-domain FrameNet types, the degeneration effect
323	    concentrates them into the same narrow cone (cosine ≥ 0.90), destroying BCS discriminability.
324	    Cite as the theoretical explanation for why embedding-based confusability proxies
325	    have a principled failure mode on semantically homogeneous schemas.
326	
327	- id: ethayarajh-contextual-2019
328	  title: "How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings"
329	  authors: [Kawin Ethayarajh]
330	  year: 2019
331	  venue: EMNLP 2019
332	  url: https://aclanthology.org/D19-1006/
333	  role: theoretical-foundation
334	  relevance_note: >
335	    Shows contextualized representations are anisotropic in ALL layers of BERT/ELMo/GPT-2.
336	    Upper layers are more context-specific but still not isotropic.
337	    Introduces quantitative measures of anisotropy (avg cosine sim of random word pairs).
338	    LINK TO OUR WORK: Establishes that anisotropy is pervasive across architectures —
339	    our MAVEN embedding compression is not a Qwen-specific artifact but a general property.
340	    Supports the argument that ANY embedding-based confusability proxy inherits this limitation.
341	
342	- id: cai-isotropy-clusters-2021
343	  title: "Isotropy in the Contextual Embedding Space: Clusters and Manifolds"
344	  authors: [Xingyu Cai, Jiaji Huang, Yuchen Bian, Kenneth Church]
345	  year: 2021
346	  venue: ICLR 2021
347	  url: https://openreview.net/forum?id=xYGNO86OWDH
348	  role: theoretical-foundation
349	  relevance_note: >
350	    ⭐ MOST DIRECTLY RELEVANT. Key insight: global anisotropy is caused by isolated clusters;
351	    WITHIN each cluster, embeddings are locally more isotropic.
352	    Resolution: the high average cosine similarity reported in prior work is an artifact of
353	    mixing embeddings from different clusters — within-cluster geometry is better behaved.
354	    LINK TO OUR WORK: This is the exact mechanism for our "domain boundary" finding.
355	    Cross-domain schemas (ACE vs FewNERD) span DIFFERENT clusters → BCS captures real
356	    inter-cluster distances → proxy works. Same-domain schemas (MAVEN FrameNet types)
357	    fall within ONE cluster → within-cluster variance is low → cosine sim saturates ≥ 0.90
358	    → BCS loses discriminability. Our empirical finding is a direct instantiation of their
359	    theoretical framework applied to type-level (not token-level) embeddings.
360	
361	- id: godey-anisotropy-inherent-2024
362	  title: "Anisotropy Is Inherent to Self-Attention in Transformers"
363	  authors: [Nathan Godey, Éric de la Clergerie, Benoît Sagot]
364	  year: 2024
365	  venue: EACL 2024
366	  url: https://aclanthology.org/2024.eacl-long.3/
367	  role: theoretical-foundation
368	  relevance_note: >
369	    Proves anisotropy is inherent to the self-attention mechanism itself, not just a
370	    consequence of cross-entropy training on long-tailed token distributions.
371	    Observed across modalities (NLP, vision), ruling out data-distribution explanations.
372	    LINK TO OUR WORK: Strengthens the argument that BCS compression is a fundamental
373	    architectural limitation, not fixable by better prompting or model choice.
374	    Supports our position that structural decomposition (SDGD) is necessary precisely
375	    because the embedding space has inherent geometric constraints.
376	
377	- id: rajaee-cluster-isotropy-2021
378	  title: "A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space"
379	  authors: [Sara Rajaee, Mohammad Taher Pilehvar]
380	  year: 2021
381	  venue: ACL 2021
382	  url: https://aclanthology.org/2021.acl-short.73/
383	  role: theoretical-foundation
384	  relevance_note: >
385	    Shows local (within-cluster) assessment of isotropy is more accurate than global assessment.
386	    Cluster-specific dominant directions encode structural (not semantic) information;
387	    removing them improves semantic task performance.
388	    LINK TO OUR WORK: Supports that within a semantic domain (one cluster), the dominant
389	    directions capture domain-level features rather than fine-grained type distinctions.
390	    This explains why MAVEN type embeddings are compressed: the shared "event-ness"
391	    dominates over type-specific semantics in the local embedding geometry.
392	
393	# =============================================================================
394	# NOVELTY THREAT ASSESSMENT (2026-05-15)
395	# =============================================================================
396	#
397	# 1. "Type count vs type confusability" disentangling:
398	#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.
399	#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.
400	#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.
401	#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.
402	#    Our multi-channel degradation model (count + confusability + context) is novel.
403	#
404	# 2. Schema decomposition baselines to compare:
405	#    - LLM-PEE (similarity partitioning) — MUST compare
406	#    - PARSE (LLM-driven schema rewriting) — MUST compare
407	#    - DEE (task-level decomposition) — discuss in related work
408	#    - SPT (schema as tools) — discuss in related work
409	#    - DLISC (Dual-LoRA schema caching) — discuss in related work
410	#
411	# 3. "Lost in the Middle" for IE:
412	#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.
413	#    We can be first to connect positional bias to schema prompt design.
414	#
415	# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):
416	#    Growing area. Position clearly: we reduce confusion proactively via decomposition,
417	#    they resolve it reactively via debate. Complementary, not conflicting.
418	#
419	# 5. Overall novelty position:
420	#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for
421	#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized
422	#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.
423	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "689c0c19-6076-4301-861e-94023b02d4cb",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "f1e7c243-9c1f-4e28-aedf-6fc8d8f37084",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml",
      "content": "# Literature Map for schema-dag-extraction\n# Updated: 2026-05-15\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\n\n# =============================================================================\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\n# =============================================================================\n\n- id: llm-pee-2025\n  title: \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\"\n  year: 2025\n  venue: arXiv\n  url: https://arxiv.org/abs/2503.02628\n  role: direct-competitor\n  relevance_note: >\n    Similarity-based type recall + type-partitioning prompting for massive event types.\n    Divides candidate types into partitions to reduce prompt length.\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\n\n- id: parse-2025\n  title: \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\"\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\n  year: 2025\n  venue: EMNLP 2025 Industry\n  url: https://arxiv.org/abs/2510.08623\n  role: direct-competitor\n  relevance_note: >\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\n    Does NOT model type confusability explicitly.\n\n- id: dee-2024\n  title: \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\"\n  year: 2024\n  venue: arXiv\n  url: https://arxiv.org/abs/2406.01045\n  role: direct-competitor\n  relevance_note: >\n    Decomposes event extraction into detection + argument extraction.\n    Dynamic schema-aware RAG for augmented prompts.\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\n\n- id: crossagentie-2025\n  title: \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\"\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\n  year: 2025\n  venue: ACL 2025 Findings\n  url: https://aclanthology.org/2025.findings-acl.718/\n  role: direct-competitor\n  relevance_note: >\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\n    + inter-group cross-task debate (NER↔RE mutual refinement).\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\n    Must clearly differentiate in paper.\n\n- id: dlisc-2025\n  title: \"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\"\n  year: 2025\n  venue: arXiv (May 2025)\n  url: https://arxiv.org/abs/2505.14992\n  role: direct-competitor\n  relevance_note: >\n    Dual-LoRA with Incremental Schema Caching.\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\n    Focus on efficiency for on-device LLMs, not confusability analysis.\n\n- id: spt-2025\n  title: \"Schema as Parameterized Tools for Universal Information Extraction\"\n  year: 2025\n  venue: arXiv (June 2025)\n  url: https://arxiv.org/abs/2506.01276\n  role: direct-competitor\n  relevance_note: >\n    Treats schemas as parameterized tools for LLM tool-calling.\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\n    Does not address type confusability.\n\n- id: zeroner-2025\n  title: \"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\"\n  year: 2025\n  venue: ACL 2025 Findings\n  url: https://aclanthology.org/2025.findings-acl.805/\n  role: direct-competitor\n  relevance_note: >\n    Description-driven: LLM supervision → BERT student for unseen types.\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\n    Related to how schema semantics affect extraction quality.\n\n- id: cmas-ner-2025\n  title: \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\"\n  year: 2025\n  venue: TheWebConf 2025\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\n  role: direct-competitor\n  relevance_note: >\n    Multi-agent collective intelligence for zero-shot NER.\n    Addresses context correlation and indiscriminate demonstration problems.\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\n\n# =============================================================================\n# METHOD COMPONENTS — techniques we build upon or relate to\n# =============================================================================\n\n- id: uniner-2024\n  title: \"UniversalNER: Targeted Distillation from Large Language Models for Open NER\"\n  authors: [Wenxuan Zhou et al.]\n  year: 2024\n  venue: ICLR 2024\n  url: https://arxiv.org/abs/2308.03279\n  role: method-component\n  relevance_note: >\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\n    Important baseline for universal NER and schema-at-scale challenges.\n\n- id: gollie-2024\n  title: \"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\"\n  authors: [Oscar Sainz et al.]\n  year: 2024\n  venue: ICLR 2024\n  url: https://hitz-zentroa.github.io/GoLLIE/\n  role: method-component\n  relevance_note: >\n    Code-style schema definitions + annotation guideline following.\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\n    Baseline for guideline-driven schema representation.\n\n- id: gliner-2024\n  title: \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\"\n  authors: [Urchade Zaratiana et al.]\n  year: 2024\n  venue: NAACL 2024\n  url: https://arxiv.org/abs/2311.08526\n  role: method-component\n  relevance_note: >\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\n\n- id: gliner2-2025\n  title: \"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\"\n  authors: [Urchade Zaratiana et al.]\n  year: 2025\n  venue: EMNLP 2025 Demo\n  url: https://arxiv.org/abs/2507.18546\n  role: method-component\n  relevance_note: >\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\n    Schema-driven interface. Shows schema approach scales to multi-task.\n\n- id: kggen-2025\n  title: \"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\"\n  authors: [Mo et al.]\n  year: 2025\n  venue: NeurIPS 2025\n  url: https://arxiv.org/abs/2502.09956\n  role: method-component\n  relevance_note: >\n    Two-stage decomposition: entities first, then relations.\n    Entity clustering/deduplication to reduce graph sparsity.\n    Schema decomposition approach for KG construction.\n\n- id: code4uie-2024\n  title: \"Retrieval-Augmented Code Generation for Universal Information Extraction\"\n  authors: [Yucan Guo et al.]\n  year: 2024\n  venue: NeurIPS 2024 Workshop\n  url: https://arxiv.org/abs/2311.02962\n  role: method-component\n  relevance_note: >\n    Python class-based schema definitions + RAG for code generation.\n    Unified code-style schema for all IE tasks.\n\n- id: iepile-2024\n  title: \"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\"\n  authors: [Guanzheng Chen et al., ZJU NLP]\n  year: 2024\n  venue: ACL 2024\n  url: https://arxiv.org/abs/2402.14710\n  role: method-component\n  relevance_note: >\n    0.32B token bilingual IE corpus. Hard negative schema construction =\n    semantically proximate schemas to train type discrimination.\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\n    Our contribution is inference-time confusability-aware decomposition (training-free).\n\n- id: lost-in-middle-2024\n  title: \"Lost in the Middle: How Language Models Use Long Contexts\"\n  authors: [Nelson F. Liu et al.]\n  year: 2024\n  venue: TACL 2024\n  url: https://arxiv.org/abs/2307.03172\n  role: method-component\n  relevance_note: >\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\n    Motivates schema decomposition to reduce prompt length.\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\n\n# =============================================================================\n# ZERO-SHOT NER / RE BASELINES\n# =============================================================================\n\n- id: self-improve-ner-2024\n  title: \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\"\n  year: 2024\n  venue: NAACL 2024\n  url: https://arxiv.org/abs/2311.08921\n  role: background\n  relevance_note: >\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\n\n- id: self-prompting-re-2024\n  title: \"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\"\n  year: 2024\n  venue: EMNLP 2024 Findings\n  url: https://arxiv.org/abs/2410.01154\n  role: background\n  relevance_note: >\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\n    Training-free RE baseline.\n\n- id: reasoning-ner-2025\n  title: \"A Reasoning Paradigm for Named Entity Recognition\"\n  year: 2025\n  venue: arXiv (Nov 2025)\n  url: https://arxiv.org/abs/2511.11978\n  role: background\n  relevance_note: >\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\n\n- id: nuner-2024\n  title: \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\"\n  authors: [Sergei Bogdanov et al., NuMind]\n  year: 2024\n  venue: EMNLP 2024\n  url: https://arxiv.org/abs/2402.15343\n  role: background\n  relevance_note: >\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\n\n# =============================================================================\n# EVALUATION / BENCHMARKING\n# =============================================================================\n\n- id: familiarity-2025\n  title: \"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\"\n  year: 2025\n  venue: NAACL 2025\n  url: https://arxiv.org/abs/2412.10121\n  role: evaluation\n  relevance_note: >\n    \"Familiarity\" metric for label shift in synthetic NER data.\n    Zero-shot NER scores overestimated due to train-eval label overlap.\n    Quantifies semantic similarity between entity types — related to type confusability.\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\n\n- id: guidex-2025\n  title: \"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\"\n  authors: [Neil Deshpande et al.]\n  year: 2025\n  venue: ACL 2025 Findings\n  url: https://arxiv.org/abs/2506.00649\n  role: evaluation\n  relevance_note: >\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\n\n# =============================================================================\n# SURVEYS\n# =============================================================================\n\n- id: llm4ie-survey-2024\n  title: \"Large Language Models for Generative Information Extraction: A Survey\"\n  authors: [Derong Xu et al.]\n  year: 2024\n  venue: Frontiers of Computer Science\n  url: https://arxiv.org/abs/2312.17617\n  role: background\n  relevance_note: >\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\n\n- id: knowcoder-2024\n  title: \"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\"\n  year: 2024\n  venue: ACL 2024\n  url: https://arxiv.org/abs/2403.07969\n  role: background\n  relevance_note: >\n    Encodes schema knowledge via code structures into LLM.\n    Related to code-based schema representation.\n\n- id: slot-2025\n  title: \"SLOT: Structuring the Output of Large Language Models\"\n  year: 2025\n  venue: EMNLP 2025 Industry\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\n  role: background\n  relevance_note: >\n    Decouples output formatting from NL task. Model-agnostic structured output.\n\n# =============================================================================\n# EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n# — supports \"domain boundary\" finding: BCS proxy fails for same-domain schemas\n# =============================================================================\n\n- id: gao-repr-degen-2019\n  title: \"Representation Degeneration Problem in Training Natural Language Generation Models\"\n  authors: [Jun Gao, Di He, Hang Li, Xin Jiang]\n  year: 2019\n  venue: ICLR 2019\n  url: https://arxiv.org/abs/1907.12009\n  role: theoretical-foundation\n  relevance_note: >\n    FOUNDATIONAL. Shows that likelihood maximization + weight tying causes word embeddings\n    to degenerate into a narrow cone with uniformly high cosine similarity.\n    Proposed cosine regularization (MLE-CosReg) to widen the cone aperture.\n    LINK TO OUR WORK: This is the root mechanism behind BCS compression.\n    When Qwen3-32B encodes 168 same-domain FrameNet types, the degeneration effect\n    concentrates them into the same narrow cone (cosine ≥ 0.90), destroying BCS discriminability.\n    Cite as the theoretical explanation for why embedding-based confusability proxies\n    have a principled failure mode on semantically homogeneous schemas.\n\n- id: ethayarajh-contextual-2019\n  title: \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\"\n  authors: [Kawin Ethayarajh]\n  year: 2019\n  venue: EMNLP 2019\n  url: https://aclanthology.org/D19-1006/\n  role: theoretical-foundation\n  relevance_note: >\n    Shows contextualized representations are anisotropic in ALL layers of BERT/ELMo/GPT-2.\n    Upper layers are more context-specific but still not isotropic.\n    Introduces quantitative measures of anisotropy (avg cosine sim of random word pairs).\n    LINK TO OUR WORK: Establishes that anisotropy is pervasive across architectures —\n    our MAVEN embedding compression is not a Qwen-specific artifact but a general property.\n    Supports the argument that ANY embedding-based confusability proxy inherits this limitation.\n\n- id: cai-isotropy-clusters-2021\n  title: \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\"\n  authors: [Xingyu Cai, Jiaji Huang, Yuchen Bian, Kenneth Church]\n  year: 2021\n  venue: ICLR 2021\n  url: https://openreview.net/forum?id=xYGNO86OWDH\n  role: theoretical-foundation\n  relevance_note: >\n    ⭐ MOST DIRECTLY RELEVANT. Key insight: global anisotropy is caused by isolated clusters;\n    WITHIN each cluster, embeddings are locally more isotropic.\n    Resolution: the high average cosine similarity reported in prior work is an artifact of\n    mixing embeddings from different clusters — within-cluster geometry is better behaved.\n    LINK TO OUR WORK: This is the exact mechanism for our \"domain boundary\" finding.\n    Cross-domain schemas (ACE vs FewNERD) span DIFFERENT clusters → BCS captures real\n    inter-cluster distances → proxy works. Same-domain schemas (MAVEN FrameNet types)\n    fall within ONE cluster → within-cluster variance is low → cosine sim saturates ≥ 0.90\n    → BCS loses discriminability. Our empirical finding is a direct instantiation of their\n    theoretical framework applied to type-level (not token-level) embeddings.\n\n- id: godey-anisotropy-inherent-2024\n  title: \"Anisotropy Is Inherent to Self-Attention in Transformers\"\n  authors: [Nathan Godey, Éric de la Clergerie, Benoît Sagot]\n  year: 2024\n  venue: EACL 2024\n  url: https://aclanthology.org/2024.eacl-long.3/\n  role: theoretical-foundation\n  relevance_note: >\n    Proves anisotropy is inherent to the self-attention mechanism itself, not just a\n    consequence of cross-entropy training on long-tailed token distributions.\n    Observed across modalities (NLP, vision), ruling out data-distribution explanations.\n    LINK TO OUR WORK: Strengthens the argument that BCS compression is a fundamental\n    architectural limitation, not fixable by better prompting or model choice.\n    Supports our position that structural decomposition (SDGD) is necessary precisely\n    because the embedding space has inherent geometric constraints.\n\n- id: rajaee-cluster-isotropy-2021\n  title: \"A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space\"\n  authors: [Sara Rajaee, Mohammad Taher Pilehvar]\n  year: 2021\n  venue: ACL 2021\n  url: https://aclanthology.org/2021.acl-short.73/\n  role: theoretical-foundation\n  relevance_note: >\n    Shows local (within-cluster) assessment of isotropy is more accurate than global assessment.\n    Cluster-specific dominant directions encode structural (not semantic) information;\n    removing them improves semantic task performance.\n    LINK TO OUR WORK: Supports that within a semantic domain (one cluster), the dominant\n    directions capture domain-level features rather than fine-grained type distinctions.\n    This explains why MAVEN type embeddings are compressed: the shared \"event-ness\"\n    dominates over type-specific semantics in the local embedding geometry.\n\n# =============================================================================\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\n# =============================================================================\n#\n# 1. \"Type count vs type confusability\" disentangling:\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\n#    Our multi-channel degradation model (count + confusability + context) is novel.\n#\n# 2. Schema decomposition baselines to compare:\n#    - LLM-PEE (similarity partitioning) — MUST compare\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\n#    - DEE (task-level decomposition) — discuss in related work\n#    - SPT (schema as tools) — discuss in related work\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\n#\n# 3. \"Lost in the Middle\" for IE:\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\n#    We can be first to connect positional bias to schema prompt design.\n#\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\n#    they resolve it reactively via debate. Complementary, not conflicting.\n#\n# 5. Overall novelty position:\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\n",
      "numLines": 423,
      "startLine": 1,
      "totalLines": 423
    }
  },
  "sourceToolAssistantUUID": "689c0c19-6076-4301-861e-94023b02d4cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T17:10:42.276Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GkS2AKowSRVBeKDbG3PLYJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1e7c243-9c1f-4e28-aedf-6fc8d8f37084",
  "isSidechain": false,
  "requestId": "req_011Cb4j3GxPdpvEcK91mQXL5",
  "type": "assistant",
  "uuid": "044ed9ad-7295-47b9-976f-b3cf2fa5acde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQ3t1GeLG9YNNr3sF5PyW7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12048,
      "cache_read_input_tokens": 11841,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12048,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 165,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12048
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

_source line 12_

```json
{
  "type": "last-prompt",
  "leafUuid": "044ed9ad-7295-47b9-976f-b3cf2fa5acde",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Build BibTeX references from YAML and Markdown",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Tool result

_source line 14 · 2026-05-15T17:10:42.617Z_

<details><summary>↩ Tool result · `toolu_01GkS2AKowSRVBeKDbG3PLYJ`</summary>

```text
1	# References Survey for Schema-DAG-Extraction
2	
3	> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)
4	
5	## Required References (14)
6	
7	### 1. LLM-PEE
8	- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction
9	- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
10	- **Venue**: EMNLP 2025 (Main)
11	- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/
12	- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.
13	- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.
14	
15	### 2. GoLLIE
16	- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction
17	- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre
18	- **Venue**: ICLR 2024
19	- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9
20	- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.
21	- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.
22	
23	### 3. GLiNER
24	- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer
25	- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois
26	- **Venue**: NAACL 2024
27	- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/
28	- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.
29	- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.
30	
31	### 4. IEPile
32	- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus
33	- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen
34	- **Venue**: ACL 2024 (Short)
35	- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/
36	- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.
37	- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.
38	
39	### 5. CrossAgentIE
40	- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction
41	- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang
42	- **Venue**: ACL 2025 Findings
43	- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG
44	- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.
45	- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.
46	
47	### 6. InstructUIE
48	- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction
49	- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du
50	- **Venue**: arXiv 2023 (preprint)
51	- **arXiv/DOI**: arXiv:2304.08085
52	- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.
53	- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.
54	
55	### 7. KGGen
56	- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models
57	- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo
58	- **Venue**: NeurIPS 2025
59	- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi
60	- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.
61	- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.
62	
63	### 8. Ethayarajh (2019) — Contextual Anisotropy
64	- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings
65	- **Authors**: Kawin Ethayarajh
66	- **Venue**: EMNLP-IJCNLP 2019
67	- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/
68	- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.
69	- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.
70	
71	### 9. Gao et al. (2019) — Representation Degeneration
72	- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models
73	- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu
74	- **Venue**: ICLR 2019
75	- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm
76	- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.
77	- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.
78	
79	### 10. LLM4IE Survey
80	- **Full title**: Large Language Models for Generative Information Extraction: A Survey
81	- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen
82	- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024
83	- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y
84	- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.
85	- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.
86	
87	### 11. UniNER
88	- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition
89	- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon
90	- **Venue**: ICLR 2024
91	- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p
92	- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.
93	- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.
94	
95	### 12. CMAS-NER
96	- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition
97	- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren
98	- **Venue**: TheWebConf (WWW) 2025
99	- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923
100	- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.
101	- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.
102	
103	### 13. KnowCoder
104	- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction
105	- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
106	- **Venue**: ACL 2024 (Long)
107	- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/
108	- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.
109	- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.
110	
111	### 14. Lost in the Middle
112	- **Full title**: Lost in the Middle: How Language Models Use Long Contexts
113	- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang
114	- **Venue**: TACL 2024, vol. 12, pp. 157-173
115	- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638
116	- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.
117	- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.
118	
119	---
120	
121	## Additional References (7)
122	
123	### 15. CodeIE
124	- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors
125	- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu
126	- **Venue**: ACL 2023 (Long)
127	- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/
128	- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.
129	- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.
130	
131	### 16. ADELIE
132	- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction
133	- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li
134	- **Venue**: EMNLP 2024 (Main)
135	- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/
136	- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.
137	- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.
138	
139	### 17. Decompose, Enrich, and Extract! (DEE)
140	- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs
141	- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li
142	- **Venue**: IEEE ICTAI 2024
143	- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/
144	- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.
145	- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.
146	
147	### 18. OneKE
148	- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System
149	- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen
150	- **Venue**: WWW 2025 (Companion)
151	- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189
152	- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.
153	- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.
154	
155	### 19. Schema as Parameterized Tools (SPT)
156	- **Full title**: Schema as Parameterized Tools for Universal Information Extraction
157	- **Authors**: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu
158	- **Venue**: arXiv preprint, June 2025
159	- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa
160	- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.
161	- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.
162	
163	### 20. PARSE
164	- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction
165	- **Authors**: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla
166	- **Venue**: arXiv preprint (Amazon Science), October 2025
167	- **arXiv/DOI**: arXiv:2510.08623
168	- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.
169	- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.
170	
171	### 21. Familiarity: Zero-Shot NER Label Shift
172	- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data
173	- **Authors**: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik
174	- **Venue**: NAACL 2025
175	- **arXiv/DOI**: arXiv:2412.10121 | https://aclanthology.org/2025.naacl-long.37/
176	- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.
177	- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.
178	
179	---
180	
181	## Direction A: Structured Decoding / Constrained Generation for IE (2)
182	
183	### 22. GENRE — Autoregressive Entity Retrieval
184	- **Full title**: Autoregressive Entity Retrieval
185	- **Authors**: Nicola De Cao, Gautier Izacard, Sebastian Riedel, Fabio Petroni
186	- **Venue**: ICLR 2021
187	- **arXiv/DOI**: arXiv:2010.00904 | https://openreview.net/forum?id=5k8F6UU39V
188	- **Key contribution**: First system to retrieve entities by autoregressively generating their names token-by-token, using constrained beam search over a prefix tree (trie) to guarantee valid entity identifiers. Achieves SOTA on entity disambiguation, end-to-end entity linking, and document retrieval with ~20x smaller memory footprint.
189	- **Relation to our work**: [complement] — Pioneered constrained autoregressive generation for entity-level tasks; the trie-based decoding constraint is analogous to our schema-guided decomposition in restricting the output space to reduce confusion.
190	
191	### 23. iNERD — Informed NER Decoding
192	- **Full title**: Informed Named Entity Recognition Decoding for Generative Language Models
193	- **Authors**: Tobias Deußer, Lars Patrick Hillebrand, Christian Bauckhage, Rafet Sifa
194	- **Venue**: IEEE BigData 2024
195	- **arXiv/DOI**: arXiv:2308.07791 | https://ieeexplore.ieee.org/document/10825603/
196	- **Key contribution**: Treats NER as a generative process with an informed decoding scheme that incorporates entity type constraints into open-ended text generation, eliminating hallucinated entity types and improving extraction precision without fine-tuning.
197	- **Relation to our work**: [complement] — Addresses type confusion at decoding time by constraining valid outputs; complementary to our input-level schema decomposition that reduces confusion before generation.
198	
199	---
200	
201	## Direction B: Classical Label Ambiguity / Type Confusion (2)
202	
203	### 24. NoiseBench
204	- **Full title**: NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition
205	- **Authors**: Elena Merdjanovska, Ansar Aynetdinov, Alan Akbik
206	- **Venue**: EMNLP 2024
207	- **arXiv/DOI**: arXiv:2405.07609 | https://aclanthology.org/2024.emnlp-main.1011/
208	- **Key contribution**: NER benchmark with clean data corrupted by 6 types of real noise (expert, crowdsourcing, automatic annotation, LLM errors). Shows real noise is significantly harder than simulated noise, and SOTA noise-robust models fall far short of upper bounds. Real noise is memorized immediately during training, unlike simulated noise.
209	- **Relation to our work**: [support] — Demonstrates that label noise (including type-level errors) significantly degrades NER, validating that type confusion from ambiguous annotations is a real and underestimated problem.
210	
211	### 25. Label Reasoning Network (LRN) for Fine-grained Entity Typing
212	- **Full title**: Fine-grained Entity Typing via Label Reasoning
213	- **Authors**: Qing Liu, Hongyu Lin, Xinyan Xiao, Xianpei Han, Le Sun, Hua Wu
214	- **Venue**: EMNLP 2021
215	- **arXiv/DOI**: arXiv:2109.05744 | https://aclanthology.org/2021.emnlp-main.378/
216	- **Key contribution**: Proposes Label Reasoning Network that exploits inter-label dependencies (extrinsic and intrinsic) via autoregressive deductive reasoning and bipartite attribute graph inductive reasoning. Effectively handles long-tail and fine-grained types by modeling how types differ from each other rather than classifying independently.
217	- **Relation to our work**: [support] — Directly addresses type confusion in fine-grained entity typing by modeling inter-type dependencies; validates our premise that independent type classification fails when types are semantically proximate.
218	
219	---
220	
221	## Direction C: Evaluation Methodology for IE (2)
222	
223	### 26. GenRES — Rethinking Evaluation for Generative RE
224	- **Full title**: GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models
225	- **Authors**: Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, Jiawei Han
226	- **Venue**: NAACL 2024
227	- **arXiv/DOI**: arXiv:2402.10744 | https://aclanthology.org/2024.naacl-long.155/
228	- **Key contribution**: Shows that traditional exact-match RE metrics are inadequate for evaluating generative RE, as LLMs produce semantically correct but lexically diverse relations. Proposes multi-dimensional assessment covering topic similarity, uniqueness, granularity, factualness, and completeness.
229	- **Relation to our work**: [complement] — Highlights that evaluation metrics themselves can conflate genuine type confusion with legitimate semantic variation; our confusability analysis should account for evaluation-induced noise.
230	
231	### 27. MultiCoNER 2 (SemEval-2023 Task 2)
232	- **Full title**: SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)
233	- **Authors**: Besnik Fetahu, Sudipta Kar, Zhiyu Chen, Oleg Rokhlenko, Shervin Malmasi
234	- **Venue**: SemEval 2023 (co-located with ACL 2023)
235	- **arXiv/DOI**: arXiv:2305.06586 | https://aclanthology.org/2023.semeval-1.310/
236	- **Key contribution**: Shared task on fine-grained multilingual NER across 12 languages with 36 entity types (e.g., WRITTENWORK, VEHICLE, MUSICALGRP). Attracted 47 teams. Shows that fine-grained type distinctions and noisy contexts significantly challenge even strong models, with performance dropping sharply as type granularity increases.
237	- **Relation to our work**: [support] — Large-scale empirical evidence that fine-grained type distinctions degrade NER performance across models and languages, directly supporting our type confusability hypothesis.
238	
239	---
240	
241	## Direction D: LLM Calibration / Confidence Estimation (3)
242	
243	### 28. LLM Confidence & Calibration Survey
244	- **Full title**: A Survey of Confidence Estimation and Calibration in Large Language Models
245	- **Authors**: Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, Iryna Gurevych
246	- **Venue**: NAACL 2024
247	- **arXiv/DOI**: arXiv:2311.08298 | https://aclanthology.org/2024.naacl-long.366/
248	- **Key contribution**: Comprehensive survey of LLM confidence estimation and calibration methods. Shows frequent misalignment between verbalized confidence and accuracy, with confidence clustering in high ranges. Categorizes approaches into training-based calibration, prompting-based calibration, and post-hoc calibration.
249	- **Relation to our work**: [complement] — Provides foundation for confidence-based type disambiguation; miscalibrated LLM confidence on confusable types could inform our decomposition strategy by identifying high-confusion type pairs.
250	
251	### 29. FaR — Fact-and-Reflection Prompting for Calibration
252	- **Full title**: Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models
253	- **Authors**: Xinran Zhao, Hongming Zhang, Xiaoman Pan, Wenlin Yao, Dong Yu, Tongshuang Wu, Jianshu Chen
254	- **Venue**: ACL 2024 Findings
255	- **arXiv/DOI**: arXiv:2402.17124 | https://aclanthology.org/2024.findings-acl.515/
256	- **Key contribution**: Two-step prompting (elicit relevant facts → reflect to generate answer) reduces Expected Calibration Error by 23.5%. Shows that LLMs can verbally express uncertainty in low-confidence scenarios, enabling selective retrieval augmentation for harder instances.
257	- **Relation to our work**: [complement] — Demonstrates that structured prompting improves LLM self-assessment; analogous to our schema decomposition reducing the cognitive load for type discrimination.
258	
259	### 30. LinkNER — Uncertainty-based NER with LLMs
260	- **Full title**: LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty
261	- **Authors**: Zhen Zhang, Yuhua Zhao, Hang Gao, Mengting Hu
262	- **Venue**: WWW 2024
263	- **arXiv/DOI**: arXiv:2402.10573 | https://dl.acm.org/doi/10.1145/3589334.3645414
264	- **Key contribution**: Framework linking fine-tuned local NER models with LLMs via uncertainty estimation (confidence, entropy, MC-Dropout, evidential learning). Routes low-confidence predictions to LLMs for correction, achieving SOTA robustness. Shows that uncertainty signals reliably identify type-confused entities.
265	- **Relation to our work**: [support] — Demonstrates that uncertainty estimation can identify type-confused entities at inference time; our confusability-aware decomposition addresses the same problem at the schema design level.
266	
267	---
268	
269	## Summary Statistics
270	- Total references: **14 required + 7 additional + 9 newly added = 30 total**
271	- Not found: None — all papers verified via web search
272	- Coverage by direction:
273	  - **A. Structured decoding / constrained generation**: #22 GENRE, #23 iNERD
274	  - **B. Classical label ambiguity / type confusion**: #24 NoiseBench, #25 LRN
275	  - **C. Evaluation methodology for IE**: #26 GenRES, #27 MultiCoNER 2
276	  - **D. LLM calibration / confidence estimation**: #28 Geng survey, #29 FaR, #30 LinkNER
277	- Coverage by relation type:
278	  - **Support** (validates our claims): #1, #4, #5, #8, #9, #11, #12, #14, #17, #21, #24, #25, #27, #30 (14 papers)
279	  - **Complement** (orthogonal methods): #2, #6, #7, #10, #13, #15, #18, #19, #20, #22, #23, #26, #28, #29 (14 papers)
280	  - **Contrast** (alternative approaches): #3, #16 (2 papers)
281	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "044ed9ad-7295-47b9-976f-b3cf2fa5acde",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "a4d94f51-1d95-4417-b90a-8c7914a45cfa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/references_survey.md",
      "content": "# References Survey for Schema-DAG-Extraction\n\n> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)\n\n## Required References (14)\n\n### 1. LLM-PEE\n- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\n- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: EMNLP 2025 (Main)\n- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/\n- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.\n- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.\n\n### 2. GoLLIE\n- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\n- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9\n- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.\n- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.\n\n### 3. GLiNER\n- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\n- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/\n- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.\n- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.\n\n### 4. IEPile\n- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\n- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen\n- **Venue**: ACL 2024 (Short)\n- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/\n- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.\n- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.\n\n### 5. CrossAgentIE\n- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\n- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang\n- **Venue**: ACL 2025 Findings\n- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG\n- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.\n- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.\n\n### 6. InstructUIE\n- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\n- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du\n- **Venue**: arXiv 2023 (preprint)\n- **arXiv/DOI**: arXiv:2304.08085\n- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.\n- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.\n\n### 7. KGGen\n- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\n- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo\n- **Venue**: NeurIPS 2025\n- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi\n- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.\n- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.\n\n### 8. Ethayarajh (2019) — Contextual Anisotropy\n- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\n- **Authors**: Kawin Ethayarajh\n- **Venue**: EMNLP-IJCNLP 2019\n- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/\n- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.\n- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.\n\n### 9. Gao et al. (2019) — Representation Degeneration\n- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models\n- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\n- **Venue**: ICLR 2019\n- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm\n- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.\n- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.\n\n### 10. LLM4IE Survey\n- **Full title**: Large Language Models for Generative Information Extraction: A Survey\n- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen\n- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024\n- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y\n- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.\n- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.\n\n### 11. UniNER\n- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\n- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon\n- **Venue**: ICLR 2024\n- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p\n- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.\n- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.\n\n### 12. CMAS-NER\n- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\n- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren\n- **Venue**: TheWebConf (WWW) 2025\n- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923\n- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.\n- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.\n\n### 13. KnowCoder\n- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\n- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue**: ACL 2024 (Long)\n- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/\n- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.\n- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.\n\n### 14. Lost in the Middle\n- **Full title**: Lost in the Middle: How Language Models Use Long Contexts\n- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang\n- **Venue**: TACL 2024, vol. 12, pp. 157-173\n- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638\n- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.\n- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.\n\n---\n\n## Additional References (7)\n\n### 15. CodeIE\n- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\n- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu\n- **Venue**: ACL 2023 (Long)\n- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/\n- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.\n- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.\n\n### 16. ADELIE\n- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction\n- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li\n- **Venue**: EMNLP 2024 (Main)\n- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/\n- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.\n- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.\n\n### 17. Decompose, Enrich, and Extract! (DEE)\n- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\n- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li\n- **Venue**: IEEE ICTAI 2024\n- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/\n- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.\n- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.\n\n### 18. OneKE\n- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\n- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen\n- **Venue**: WWW 2025 (Companion)\n- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189\n- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.\n- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.\n\n### 19. Schema as Parameterized Tools (SPT)\n- **Full title**: Schema as Parameterized Tools for Universal Information Extraction\n- **Authors**: Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, Yong Liu\n- **Venue**: arXiv preprint, June 2025\n- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa\n- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.\n- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.\n\n### 20. PARSE\n- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\n- **Authors**: Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla\n- **Venue**: arXiv preprint (Amazon Science), October 2025\n- **arXiv/DOI**: arXiv:2510.08623\n- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.\n- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.\n\n### 21. Familiarity: Zero-Shot NER Label Shift\n- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\n- **Authors**: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik\n- **Venue**: NAACL 2025\n- **arXiv/DOI**: arXiv:2412.10121 | https://aclanthology.org/2025.naacl-long.37/\n- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.\n- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.\n\n---\n\n## Direction A: Structured Decoding / Constrained Generation for IE (2)\n\n### 22. GENRE — Autoregressive Entity Retrieval\n- **Full title**: Autoregressive Entity Retrieval\n- **Authors**: Nicola De Cao, Gautier Izacard, Sebastian Riedel, Fabio Petroni\n- **Venue**: ICLR 2021\n- **arXiv/DOI**: arXiv:2010.00904 | https://openreview.net/forum?id=5k8F6UU39V\n- **Key contribution**: First system to retrieve entities by autoregressively generating their names token-by-token, using constrained beam search over a prefix tree (trie) to guarantee valid entity identifiers. Achieves SOTA on entity disambiguation, end-to-end entity linking, and document retrieval with ~20x smaller memory footprint.\n- **Relation to our work**: [complement] — Pioneered constrained autoregressive generation for entity-level tasks; the trie-based decoding constraint is analogous to our schema-guided decomposition in restricting the output space to reduce confusion.\n\n### 23. iNERD — Informed NER Decoding\n- **Full title**: Informed Named Entity Recognition Decoding for Generative Language Models\n- **Authors**: Tobias Deußer, Lars Patrick Hillebrand, Christian Bauckhage, Rafet Sifa\n- **Venue**: IEEE BigData 2024\n- **arXiv/DOI**: arXiv:2308.07791 | https://ieeexplore.ieee.org/document/10825603/\n- **Key contribution**: Treats NER as a generative process with an informed decoding scheme that incorporates entity type constraints into open-ended text generation, eliminating hallucinated entity types and improving extraction precision without fine-tuning.\n- **Relation to our work**: [complement] — Addresses type confusion at decoding time by constraining valid outputs; complementary to our input-level schema decomposition that reduces confusion before generation.\n\n---\n\n## Direction B: Classical Label Ambiguity / Type Confusion (2)\n\n### 24. NoiseBench\n- **Full title**: NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition\n- **Authors**: Elena Merdjanovska, Ansar Aynetdinov, Alan Akbik\n- **Venue**: EMNLP 2024\n- **arXiv/DOI**: arXiv:2405.07609 | https://aclanthology.org/2024.emnlp-main.1011/\n- **Key contribution**: NER benchmark with clean data corrupted by 6 types of real noise (expert, crowdsourcing, automatic annotation, LLM errors). Shows real noise is significantly harder than simulated noise, and SOTA noise-robust models fall far short of upper bounds. Real noise is memorized immediately during training, unlike simulated noise.\n- **Relation to our work**: [support] — Demonstrates that label noise (including type-level errors) significantly degrades NER, validating that type confusion from ambiguous annotations is a real and underestimated problem.\n\n### 25. Label Reasoning Network (LRN) for Fine-grained Entity Typing\n- **Full title**: Fine-grained Entity Typing via Label Reasoning\n- **Authors**: Qing Liu, Hongyu Lin, Xinyan Xiao, Xianpei Han, Le Sun, Hua Wu\n- **Venue**: EMNLP 2021\n- **arXiv/DOI**: arXiv:2109.05744 | https://aclanthology.org/2021.emnlp-main.378/\n- **Key contribution**: Proposes Label Reasoning Network that exploits inter-label dependencies (extrinsic and intrinsic) via autoregressive deductive reasoning and bipartite attribute graph inductive reasoning. Effectively handles long-tail and fine-grained types by modeling how types differ from each other rather than classifying independently.\n- **Relation to our work**: [support] — Directly addresses type confusion in fine-grained entity typing by modeling inter-type dependencies; validates our premise that independent type classification fails when types are semantically proximate.\n\n---\n\n## Direction C: Evaluation Methodology for IE (2)\n\n### 26. GenRES — Rethinking Evaluation for Generative RE\n- **Full title**: GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models\n- **Authors**: Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, Jiawei Han\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2402.10744 | https://aclanthology.org/2024.naacl-long.155/\n- **Key contribution**: Shows that traditional exact-match RE metrics are inadequate for evaluating generative RE, as LLMs produce semantically correct but lexically diverse relations. Proposes multi-dimensional assessment covering topic similarity, uniqueness, granularity, factualness, and completeness.\n- **Relation to our work**: [complement] — Highlights that evaluation metrics themselves can conflate genuine type confusion with legitimate semantic variation; our confusability analysis should account for evaluation-induced noise.\n\n### 27. MultiCoNER 2 (SemEval-2023 Task 2)\n- **Full title**: SemEval-2023 Task 2: Fine-grained Multilingual Named Entity Recognition (MultiCoNER 2)\n- **Authors**: Besnik Fetahu, Sudipta Kar, Zhiyu Chen, Oleg Rokhlenko, Shervin Malmasi\n- **Venue**: SemEval 2023 (co-located with ACL 2023)\n- **arXiv/DOI**: arXiv:2305.06586 | https://aclanthology.org/2023.semeval-1.310/\n- **Key contribution**: Shared task on fine-grained multilingual NER across 12 languages with 36 entity types (e.g., WRITTENWORK, VEHICLE, MUSICALGRP). Attracted 47 teams. Shows that fine-grained type distinctions and noisy contexts significantly challenge even strong models, with performance dropping sharply as type granularity increases.\n- **Relation to our work**: [support] — Large-scale empirical evidence that fine-grained type distinctions degrade NER performance across models and languages, directly supporting our type confusability hypothesis.\n\n---\n\n## Direction D: LLM Calibration / Confidence Estimation (3)\n\n### 28. LLM Confidence & Calibration Survey\n- **Full title**: A Survey of Confidence Estimation and Calibration in Large Language Models\n- **Authors**: Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, Iryna Gurevych\n- **Venue**: NAACL 2024\n- **arXiv/DOI**: arXiv:2311.08298 | https://aclanthology.org/2024.naacl-long.366/\n- **Key contribution**: Comprehensive survey of LLM confidence estimation and calibration methods. Shows frequent misalignment between verbalized confidence and accuracy, with confidence clustering in high ranges. Categorizes approaches into training-based calibration, prompting-based calibration, and post-hoc calibration.\n- **Relation to our work**: [complement] — Provides foundation for confidence-based type disambiguation; miscalibrated LLM confidence on confusable types could inform our decomposition strategy by identifying high-confusion type pairs.\n\n### 29. FaR — Fact-and-Reflection Prompting for Calibration\n- **Full title**: Fact-and-Reflection (FaR) Improves Confidence Calibration of Large Language Models\n- **Authors**: Xinran Zhao, Hongming Zhang, Xiaoman Pan, Wenlin Yao, Dong Yu, Tongshuang Wu, Jianshu Chen\n- **Venue**: ACL 2024 Findings\n- **arXiv/DOI**: arXiv:2402.17124 | https://aclanthology.org/2024.findings-acl.515/\n- **Key contribution**: Two-step prompting (elicit relevant facts → reflect to generate answer) reduces Expected Calibration Error by 23.5%. Shows that LLMs can verbally express uncertainty in low-confidence scenarios, enabling selective retrieval augmentation for harder instances.\n- **Relation to our work**: [complement] — Demonstrates that structured prompting improves LLM self-assessment; analogous to our schema decomposition reducing the cognitive load for type discrimination.\n\n### 30. LinkNER — Uncertainty-based NER with LLMs\n- **Full title**: LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty\n- **Authors**: Zhen Zhang, Yuhua Zhao, Hang Gao, Mengting Hu\n- **Venue**: WWW 2024\n- **arXiv/DOI**: arXiv:2402.10573 | https://dl.acm.org/doi/10.1145/3589334.3645414\n- **Key contribution**: Framework linking fine-tuned local NER models with LLMs via uncertainty estimation (confidence, entropy, MC-Dropout, evidential learning). Routes low-confidence predictions to LLMs for correction, achieving SOTA robustness. Shows that uncertainty signals reliably identify type-confused entities.\n- **Relation to our work**: [support] — Demonstrates that uncertainty estimation can identify type-confused entities at inference time; our confusability-aware decomposition addresses the same problem at the schema design level.\n\n---\n\n## Summary Statistics\n- Total references: **14 required + 7 additional + 9 newly added = 30 total**\n- Not found: None — all papers verified via web search\n- Coverage by direction:\n  - **A. Structured decoding / constrained generation**: #22 GENRE, #23 iNERD\n  - **B. Classical label ambiguity / type confusion**: #24 NoiseBench, #25 LRN\n  - **C. Evaluation methodology for IE**: #26 GenRES, #27 MultiCoNER 2\n  - **D. LLM calibration / confidence estimation**: #28 Geng survey, #29 FaR, #30 LinkNER\n- Coverage by relation type:\n  - **Support** (validates our claims): #1, #4, #5, #8, #9, #11, #12, #14, #17, #21, #24, #25, #27, #30 (14 papers)\n  - **Complement** (orthogonal methods): #2, #6, #7, #10, #13, #15, #18, #19, #20, #22, #23, #26, #28, #29 (14 papers)\n  - **Contrast** (alternative approaches): #3, #16 (2 papers)\n",
      "numLines": 281,
      "startLine": 1,
      "totalLines": 281
    }
  },
  "sourceToolAssistantUUID": "044ed9ad-7295-47b9-976f-b3cf2fa5acde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
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
  "leafUuid": "a4d94f51-1d95-4417-b90a-8c7914a45cfa",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Build BibTeX references from YAML and Markdown",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Assistant

_source line 17 · 2026-05-15T17:12:13.507Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to merge both sources and create a comprehensive BibTeX file. Let me catalog all papers:

From literature_map.yaml (30 entries):
1. llm-pee-2025
2. parse-2025
3. dee-2024
4. crossagentie-2025
5. dlisc-2025
6. spt-2025
7. zeroner-2025
8. cmas-ner-2025
9. uniner-2024
10. gollie-2024
11. gliner-2024
12. gliner2-2025


13. kggen-2025
14. code4uie-2024
15. iepile-2024
16. lost-in-middle-2024
17. self-improve-ner-2024
18. self-prompting-re-2024
19. reasoning-ner-2025
20. nuner-2024
21. familiarity-2025
22. guidex-2025
23. llm4ie-survey-2024
24. knowcoder-2024
25. slot-2025
26. gao-repr-degen-2019
27. ethayarajh-contextual-2019
28. cai-isotropy-clusters-2021
29. god

That's 29 entries so far, and I need to check if there are more papers to include from the second source to complete the full set of 30. I've identified LinkNER as the final missing entry, bringing the total to 43 papers. Now I'm compiling the BibTeX file by cross-referencing the detailed information from the survey with the literature map, and for entries that only appear in the map without full author details, I'll construct reasonable entries based on what's available.

Working through the entries systematically: the first few papers have conflicting venue information between sources, so I'm prioritizing the survey's more detailed data—using EMNLP 2025 for the first entry rather than arXiv, formatting it as an inproceedings entry. The next entries include an arXiv preprint from Amazon Science, an IEEE ICTAI 2024 conference paper, and an ACL 2025 Findings paper, each with their respective author lists and publication details. Continuing through the papers, I'm seeing UniNER and GoLLiE both appeared at ICLR 2024 with their respective author teams, while GLiNER made it into NAACL 2024. Continuing through the bibliography, I see several more papers spanning 2024 and 2025 across different venues. The iepile paper from ACL 2024 has authors including Hongbin Ye and Huajun Chen, while lost-in-middle is a TACL 2024 article by Liu, Lin, Hewitt and others on context length effects. The remaining entries are from NAACL, EMNLP, and arXiv, mostly without author information listed. Continuing through the bibliography, I see the llm4ie-survey paper completes with its full author list and article designation. Moving on, knowcoder-2024 is a substantial ACL 2024 long paper with a large collaborative team, appearing in both sources. Then there's slot-2025, an EMNLP 2025 industry track entry that only appears in the literature map with no authors attributed. Finally, I'm starting to catalog gao-repr-degen-2019, an ICLR 2019 paper that shows up in both sources. Continuing through the references from the survey document, I'm now cataloging additional papers that only appear there. Moving into papers 31 and 32, which cover instruction-based information extraction and code-based IE approaches from 2023. Continuing through more recent papers on entity recognition and knowledge extraction, including work from ICLR, IEEE BigData, and EMNLP conferences spanning 2021 to 2024. Finishing up the bibliography with entries 42 and 43, then I need to handle the two entries without author information — dlisc-2025 and zeroner-2025 — where I'll create reasonable entries based on the titles provided.

Looking at the remaining papers with incomplete author lists, I have partial information for several of them like the ones with "et al." attributions, so I'll use what's available there. For the ones completely missing authors, I'll work with just the titles since that's what the source files provide. I need to find the missing author information for several papers that either have no authors listed or incomplete author lists. Let me search for the ones without any author data first—there are about six papers in that category—and then fill in the partial author lists for the others. I can see one of them links to an arXiv paper, so I should be able to track down the author details through web search. I'm completing the GLiNER2 paper URL and now need to gather the full author lists for these papers. Rather than fetching each one individually, I'll use parallel WebFetch calls to pull the arXiv abstract pages and extract the missing author information efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4d94f51-1d95-4417-b90a-8c7914a45cfa",
  "isSidechain": false,
  "requestId": "req_011Cb4j3YNbE6H9EQpkP365x",
  "type": "assistant",
  "uuid": "487489f0-0e7f-4b1c-9f2a-af9f1df3b130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QW4R2UaZ5wLXfvMsABb7Pr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15333,
      "cache_read_input_tokens": 23889,
      "output_tokens": 4743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4743,
          "cache_read_input_tokens": 23889,
          "cache_creation_input_tokens": 15333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15333
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

_source line 18 · 2026-05-15T17:12:13.512Z_

Let me look up the missing author information for papers that only appear in `literature_map.yaml` without full author details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "487489f0-0e7f-4b1c-9f2a-af9f1df3b130",
  "isSidechain": false,
  "requestId": "req_011Cb4j3YNbE6H9EQpkP365x",
  "type": "assistant",
  "uuid": "df1aff02-2084-4712-ba7f-b491b485ae75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QW4R2UaZ5wLXfvMsABb7Pr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15333,
      "cache_read_input_tokens": 23889,
      "output_tokens": 4743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4743,
          "cache_read_input_tokens": 23889,
          "cache_creation_input_tokens": 15333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15333
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

_source line 19 · 2026-05-15T17:12:13.513Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016u2mArrh3B2H3vHFupE2Yn`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df1aff02-2084-4712-ba7f-b491b485ae75",
  "isSidechain": false,
  "requestId": "req_011Cb4j3YNbE6H9EQpkP365x",
  "type": "assistant",
  "uuid": "642eb5f6-2998-4ca9-abde-f0bcff47d044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QW4R2UaZ5wLXfvMsABb7Pr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15333,
      "cache_read_input_tokens": 23889,
      "output_tokens": 4743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4743,
          "cache_read_input_tokens": 23889,
          "cache_creation_input_tokens": 15333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15333
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

_source line 20 · 2026-05-15T17:12:13.529Z_

<details><summary>↩ Tool result · `toolu_016u2mArrh3B2H3vHFupE2Yn`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "642eb5f6-2998-4ca9-abde-f0bcff47d044",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "66d73f24-6ba1-4c5a-88e8-c846bdd81b64",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "642eb5f6-2998-4ca9-abde-f0bcff47d044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-15T17:12:16.559Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the missing author information for the papers that don't have complete author lists. I'll fetch multiple arXiv pages in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66d73f24-6ba1-4c5a-88e8-c846bdd81b64",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "cfc7c761-b8fa-40f5-85ee-7fd7675252c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 22 · 2026-05-15T17:12:17.015Z_

Fetching missing author info from arXiv/ACL pages in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfc7c761-b8fa-40f5-85ee-7fd7675252c3",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "2faefdf6-19ea-4817-b395-7c928f99c224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 23 · 2026-05-15T17:12:17.974Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EecnhjVi1G56Zud6z9Tujx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.14992",
  "prompt": "Extract the full author list for this paper. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2faefdf6-19ea-4817-b395-7c928f99c224",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "5226fe27-2ec2-4d0a-8de8-cb19615eaa5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 24 · 2026-05-15T17:12:18.526Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013LnckC7nzfoJhGDBBuu9Vc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2311.08921",
  "prompt": "Extract the full author list for this paper. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5226fe27-2ec2-4d0a-8de8-cb19615eaa5a",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "1cbb755c-d524-4da7-b8de-be23d0af9234",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 25 · 2026-05-15T17:12:19.511Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KAhqzSFxYk274tWUnxH2dT`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.01154",
  "prompt": "Extract the full author list for this paper. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cbb755c-d524-4da7-b8de-be23d0af9234",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "b56bfd55-6e92-421d-9a5d-e5fb11ee86a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 26 · 2026-05-15T17:12:19.948Z_

<details><summary>↩ Tool result · `toolu_01EecnhjVi1G56Zud6z9Tujx`</summary>

```text
Based on the webpage content, the full author list for this paper is:

Zhihao Wen, Sheng Liang, Yaxiong Wu, Yongyue Zhang, Yong Liu
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5226fe27-2ec2-4d0a-8de8-cb19615eaa5a",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "1fa1b28b-8f09-4213-97bc-9c4bf81dbc94",
  "toolUseResult": {
    "bytes": 45608,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the webpage content, the full author list for this paper is:\n\nZhihao Wen, Sheng Liang, Yaxiong Wu, Yongyue Zhang, Yong Liu",
    "durationMs": 1962,
    "url": "https://arxiv.org/abs/2505.14992"
  },
  "sourceToolAssistantUUID": "5226fe27-2ec2-4d0a-8de8-cb19615eaa5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T17:12:20.353Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019zm7y8qK6NCDVGmrXAuPxZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.11978",
  "prompt": "Extract the full author list for this paper. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fa1b28b-8f09-4213-97bc-9c4bf81dbc94",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "0765785a-bc4c-4883-9ec7-ca64ca3ebd14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 28 · 2026-05-15T17:12:20.683Z_

<details><summary>↩ Tool result · `toolu_013LnckC7nzfoJhGDBBuu9Vc`</summary>

```text
Based on the webpage content, the full author list for this paper is:

Tingyu Xie, Qi Li, Yan Zhang, Zuozhu Liu, Hongwei Wang
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cbb755c-d524-4da7-b8de-be23d0af9234",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "d2ef8f33-8f5a-43f1-9ed7-3265ee35a82a",
  "toolUseResult": {
    "bytes": 46600,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the webpage content, the full author list for this paper is:\n\nTingyu Xie, Qi Li, Yan Zhang, Zuozhu Liu, Hongwei Wang",
    "durationMs": 2153,
    "url": "https://arxiv.org/abs/2311.08921"
  },
  "sourceToolAssistantUUID": "1cbb755c-d524-4da7-b8de-be23d0af9234",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T17:12:20.836Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Jxu54Pz8GHcRWEuuT6jAeY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.15343",
  "prompt": "Extract the full author list for this paper. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2ef8f33-8f5a-43f1-9ed7-3265ee35a82a",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "395ed6d8-97b3-4787-96e0-d435147b20c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 30 · 2026-05-15T17:12:21.037Z_

<details><summary>↩ Tool result · `toolu_01KAhqzSFxYk274tWUnxH2dT`</summary>

```text
Based on the web page content, the full author list is:

Siyi Liu, Yang Li, Jiang Li, Shan Yang, Yunshi Lan
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b56bfd55-6e92-421d-9a5d-e5fb11ee86a2",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "4513654f-ab87-47c2-9408-b2de58192343",
  "toolUseResult": {
    "bytes": 46536,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content, the full author list is:\n\nSiyi Liu, Yang Li, Jiang Li, Shan Yang, Yunshi Lan",
    "durationMs": 1516,
    "url": "https://arxiv.org/abs/2410.01154"
  },
  "sourceToolAssistantUUID": "b56bfd55-6e92-421d-9a5d-e5fb11ee86a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T17:12:21.315Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LNP7ZFRbnK1brnU6DwXnGK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.00649",
  "prompt": "Extract the full author list for this paper. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4513654f-ab87-47c2-9408-b2de58192343",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "b9a03a6d-5735-43a8-855b-901aefd0c57d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 32 · 2026-05-15T17:12:21.925Z_

<details><summary>↩ Tool result · `toolu_019zm7y8qK6NCDVGmrXAuPxZ`</summary>

```text
Hui Huang, Yanping Chen, Ruizhang Huang, Chuan Lin, Yongbin Qin
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0765785a-bc4c-4883-9ec7-ca64ca3ebd14",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "84f98f03-5239-46c8-ab55-da07edc82e10",
  "toolUseResult": {
    "bytes": 46967,
    "code": 200,
    "codeText": "OK",
    "result": "Hui Huang, Yanping Chen, Ruizhang Huang, Chuan Lin, Yongbin Qin",
    "durationMs": 1570,
    "url": "https://arxiv.org/abs/2511.11978"
  },
  "sourceToolAssistantUUID": "0765785a-bc4c-4883-9ec7-ca64ca3ebd14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T17:12:22.228Z_

<details><summary>↩ Tool result · `toolu_01Jxu54Pz8GHcRWEuuT6jAeY`</summary>

```text
Based on the paper content provided, the full author list is:

Sergei Bogdanov, Alexandre Constantin, Timothée Bernard, Benoit Crabbé, Etienne Bernard
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "395ed6d8-97b3-4787-96e0-d435147b20c7",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "3d5c6d2a-90c1-4d97-bb64-d20f9e2246d6",
  "toolUseResult": {
    "bytes": 44962,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the paper content provided, the full author list is:\n\nSergei Bogdanov, Alexandre Constantin, Timothée Bernard, Benoit Crabbé, Etienne Bernard",
    "durationMs": 1390,
    "url": "https://arxiv.org/abs/2402.15343"
  },
  "sourceToolAssistantUUID": "395ed6d8-97b3-4787-96e0-d435147b20c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T17:12:22.247Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RQhGvY2AoAz7dxGnNURnJs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2311.02962",
  "prompt": "Extract the full author list for this paper. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d5c6d2a-90c1-4d97-bb64-d20f9e2246d6",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "3f017362-9ac0-4a09-abf5-85233cc560ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 35 · 2026-05-15T17:12:22.518Z_

<details><summary>↩ Tool result · `toolu_01LNP7ZFRbnK1brnU6DwXnGK`</summary>

```text
Neil De La Fuente, Oscar Sainz, Iker García-Ferrero, Eneko Agirre
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9a03a6d-5735-43a8-855b-901aefd0c57d",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "082d6845-3d69-49be-8d40-c9e113bea186",
  "toolUseResult": {
    "bytes": 45685,
    "code": 200,
    "codeText": "OK",
    "result": "Neil De La Fuente, Oscar Sainz, Iker García-Ferrero, Eneko Agirre",
    "durationMs": 1200,
    "url": "https://arxiv.org/abs/2506.00649"
  },
  "sourceToolAssistantUUID": "b9a03a6d-5735-43a8-855b-901aefd0c57d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T17:12:22.617Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QYbJMiKFz3yHnAAW6xRkvh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.18546",
  "prompt": "Extract the full author list for this paper. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "082d6845-3d69-49be-8d40-c9e113bea186",
  "isSidechain": false,
  "requestId": "req_011Cb4jAF7D9ipzxfasiusUG",
  "type": "assistant",
  "uuid": "6de836de-eb30-4150-9b01-733ac4050f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRfMf3ZsACya3C9gozS8sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 39222,
      "output_tokens": 752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5254,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 752,
          "cache_read_input_tokens": 39222,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5254
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

_source line 37_

```json
{
  "type": "last-prompt",
  "leafUuid": "6de836de-eb30-4150-9b01-733ac4050f20",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Build BibTeX references from YAML and Markdown",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Tool result

_source line 39 · 2026-05-15T17:12:24.188Z_

<details><summary>↩ Tool result · `toolu_01QYbJMiKFz3yHnAAW6xRkvh`</summary>

```text
Urchade Zaratiana, Gil Pasternak, Oliver Boyd, George Hurn-Maloney, Ash Lewis
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6de836de-eb30-4150-9b01-733ac4050f20",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "5f7c06b1-7d83-4e21-acbf-dbed428aca8b",
  "toolUseResult": {
    "bytes": 45815,
    "code": 200,
    "codeText": "OK",
    "result": "Urchade Zaratiana, Gil Pasternak, Oliver Boyd, George Hurn-Maloney, Ash Lewis",
    "durationMs": 1568,
    "url": "https://arxiv.org/abs/2507.18546"
  },
  "sourceToolAssistantUUID": "6de836de-eb30-4150-9b01-733ac4050f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T17:12:24.300Z_

<details><summary>↩ Tool result · `toolu_01RQhGvY2AoAz7dxGnNURnJs`</summary>

```text
Based on the webpage content, here is the full author list:

Yucan Guo, Zixuan Li, Xiaolong Jin, Yantao Liu, Yutao Zeng, Wenxuan Liu, Xiang Li, Pan Yang, Long Bai, Jiafeng Guo, Xueqi Cheng
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f017362-9ac0-4a09-abf5-85233cc560ea",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "ad200b65-2dc4-4968-a51e-f2d051a88920",
  "toolUseResult": {
    "bytes": 46677,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the webpage content, here is the full author list:\n\nYucan Guo, Zixuan Li, Xiaolong Jin, Yantao Liu, Yutao Zeng, Wenxuan Liu, Xiang Li, Pan Yang, Long Bai, Jiafeng Guo, Xueqi Cheng",
    "durationMs": 2051,
    "url": "https://arxiv.org/abs/2311.02962"
  },
  "sourceToolAssistantUUID": "3f017362-9ac0-4a09-abf5-85233cc560ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 41 · 2026-05-15T17:12:24.304Z_

```json
{
  "parentUuid": "ad200b65-2dc4-4968-a51e-f2d051a88920",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b9961cd4-878e-4792-b8c9-29be9db82aa6",
  "timestamp": "2026-05-15T17:12:24.304Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 42 · 2026-05-15T17:12:28.232Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also get the missing authors for zeroner-2025 and slot-2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9961cd4-878e-4792-b8c9-29be9db82aa6",
  "isSidechain": false,
  "requestId": "req_011Cb4jB32xQjJQrgaSNwt2z",
  "type": "assistant",
  "uuid": "80f2910e-ce3f-46b0-a160-2eb5f15268fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZSaSQhvXxE7yASMPrcjex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 62,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 44476,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 62,
          "output_tokens": 341,
          "cache_read_input_tokens": 44476,
          "cache_creation_input_tokens": 1347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1347
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

_source line 43 · 2026-05-15T17:12:30.185Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PuSeyjZATrEa2KSUHzydFA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.10121",
  "prompt": "Extract the full author list for this paper titled \"ZeroNER\". Return only the authors as a comma-separated list. If this is the wrong paper (Familiarity), tell me."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80f2910e-ce3f-46b0-a160-2eb5f15268fe",
  "isSidechain": false,
  "requestId": "req_011Cb4jB32xQjJQrgaSNwt2z",
  "type": "assistant",
  "uuid": "2a8b37b3-2486-4f46-9569-492723461d2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZSaSQhvXxE7yASMPrcjex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 62,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 44476,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 62,
          "output_tokens": 341,
          "cache_read_input_tokens": 44476,
          "cache_creation_input_tokens": 1347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1347
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

_source line 44 · 2026-05-15T17:12:31.164Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CbxhBCsmfviPW3bMrYMszy`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-acl.805/",
  "prompt": "Extract the full author list for this paper. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a8b37b3-2486-4f46-9569-492723461d2d",
  "isSidechain": false,
  "requestId": "req_011Cb4jB32xQjJQrgaSNwt2z",
  "type": "assistant",
  "uuid": "f795eac6-0c40-43a3-819b-d7d30e2b9e5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZSaSQhvXxE7yASMPrcjex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 62,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 44476,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 62,
          "output_tokens": 341,
          "cache_read_input_tokens": 44476,
          "cache_creation_input_tokens": 1347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1347
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

_source line 45 · 2026-05-15T17:12:31.721Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0121k6UNaA3ivD915wt8m8f4`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-industry.32/",
  "prompt": "Extract the full author list for this paper about SLOT. Return only the authors as a comma-separated list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f795eac6-0c40-43a3-819b-d7d30e2b9e5a",
  "isSidechain": false,
  "requestId": "req_011Cb4jB32xQjJQrgaSNwt2z",
  "type": "assistant",
  "uuid": "b5b4e1bd-552b-486a-9a81-8e89aafee8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZSaSQhvXxE7yASMPrcjex",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 62,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 44476,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 62,
          "output_tokens": 341,
          "cache_read_input_tokens": 44476,
          "cache_creation_input_tokens": 1347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1347
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

_source line 46 · 2026-05-15T17:12:32.732Z_

<details><summary>↩ Tool result · `toolu_01PuSeyjZATrEa2KSUHzydFA`</summary>

```text
This is the wrong paper. The paper shown is titled "Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data," not "ZeroNER."

The authors of this paper are: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a8b37b3-2486-4f46-9569-492723461d2d",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "b7373f51-e68c-416a-b64b-27744a61f3e5",
  "toolUseResult": {
    "bytes": 47597,
    "code": 200,
    "codeText": "OK",
    "result": "This is the wrong paper. The paper shown is titled \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data,\" not \"ZeroNER.\"\n\nThe authors of this paper are: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan Akbik",
    "durationMs": 2538,
    "url": "https://arxiv.org/abs/2412.10121"
  },
  "sourceToolAssistantUUID": "2a8b37b3-2486-4f46-9569-492723461d2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T17:12:33.346Z_

<details><summary>↩ Tool result · `toolu_01CbxhBCsmfviPW3bMrYMszy`</summary>

```text
Alessio Cocchieri, Marcos Martínez Galindo, Giacomo Frisoni, Gianluca Moro, Claudio Sartori, Giuseppe Tagliavini
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f795eac6-0c40-43a3-819b-d7d30e2b9e5a",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "9f4cf9b8-007b-4fb5-93d0-2b90326755e1",
  "toolUseResult": {
    "bytes": 41520,
    "code": 200,
    "codeText": "OK",
    "result": "Alessio Cocchieri, Marcos Martínez Galindo, Giacomo Frisoni, Gianluca Moro, Claudio Sartori, Giuseppe Tagliavini",
    "durationMs": 2175,
    "url": "https://aclanthology.org/2025.findings-acl.805/"
  },
  "sourceToolAssistantUUID": "f795eac6-0c40-43a3-819b-d7d30e2b9e5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T17:12:33.612Z_

<details><summary>↩ Tool result · `toolu_0121k6UNaA3ivD915wt8m8f4`</summary>

```text
Based on the webpage content, the full author list for the SLOT paper is:

Zhengyuan Shen, Darren Yow-Bang Wang, Soumya Smruti Mishra, Zhichao Xu, Yifei Teng, Haibo Ding
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5b4e1bd-552b-486a-9a81-8e89aafee8c9",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "19acf455-1480-477d-b770-584a8a005426",
  "toolUseResult": {
    "bytes": 41382,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the webpage content, the full author list for the SLOT paper is:\n\nZhengyuan Shen, Darren Yow-Bang Wang, Soumya Smruti Mishra, Zhichao Xu, Yifei Teng, Haibo Ding",
    "durationMs": 1889,
    "url": "https://aclanthology.org/2025.emnlp-industry.32/"
  },
  "sourceToolAssistantUUID": "b5b4e1bd-552b-486a-9a81-8e89aafee8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-15T17:12:59.812Z_

<details><summary>Logged reasoning block</summary>

```text
Wait, for ZeroNER, the URL in the literature_map is https://aclanthology.org/2025.findings-acl.805/, which returned "Alessio Cocchieri, Marcos Martínez Galindo, Giacomo Frisoni, Gianluca Moro, Claudio Sartori, Giuseppe Tagliavini" — but that seems wrong. Let me check.

Actually, I already fetched that URL and got "Alessio Cocchieri, Marcos Martínez Galindo, Giacomo Frisoni, Gianluca Moro, Claudio Sartori, Giuseppe Tagliavini" — let me verify this is the right paper.


The literature_map confirms this is the correct paper with that URL, so I should trust the ACL anthology page and accept these authors as valid.

Now I'm noticing a discrepancy with the Gao representation degeneration paper — the literature_map lists different authors than what appears in the survey, and I need to figure out which is accurate. Checking the arxiv link from the literature_map should clarify whether these are actually two different papers or if there's an error in one of the sources.

Let me also verify the SLOT paper URL since it appears incomplete in the literature_map.

Now I'm checking the author list for that paper against what I fetched from the ACL Anthology page, which shows Zhengyuan Shen, Darren Yow-Bang Wang, Soumya Smruti Mishra, Zhichao Xu, Yifei Teng, and Haibo Ding.

I'll prioritize the survey's author information where it's available, then start constructing the complete BibTeX entries with standardized venue names for each conference. Now I need to write out the complete BibTeX file, but first I should verify that the docs/paper directory exists so I can save it properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19acf455-1480-477d-b770-584a8a005426",
  "isSidechain": false,
  "requestId": "req_011Cb4jBj1XBkjujDQbRpS3w",
  "type": "assistant",
  "uuid": "96e74c9a-6a01-47ff-902e-46eb837ae12a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VRchXgJmPu8kbS1u7XRHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 45823,
      "output_tokens": 1405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1405,
          "cache_read_input_tokens": 45823,
          "cache_creation_input_tokens": 698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 698
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

_source line 50 · 2026-05-15T17:12:59.816Z_

Got all author info. Now let me check the output directory exists and write the BibTeX file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96e74c9a-6a01-47ff-902e-46eb837ae12a",
  "isSidechain": false,
  "requestId": "req_011Cb4jBj1XBkjujDQbRpS3w",
  "type": "assistant",
  "uuid": "23df3e71-e1e7-4f9e-86d7-7e5db79dbc39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VRchXgJmPu8kbS1u7XRHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 45823,
      "output_tokens": 1405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1405,
          "cache_read_input_tokens": 45823,
          "cache_creation_input_tokens": 698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 698
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

_source line 51 · 2026-05-15T17:13:01.599Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gg7QmxJLinGVfk21CdsWnG`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23df3e71-e1e7-4f9e-86d7-7e5db79dbc39",
  "isSidechain": false,
  "requestId": "req_011Cb4jBj1XBkjujDQbRpS3w",
  "type": "assistant",
  "uuid": "734ede5c-e30a-45a9-b7c1-ea063f32c0d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VRchXgJmPu8kbS1u7XRHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 45823,
      "output_tokens": 1405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1405,
          "cache_read_input_tokens": 45823,
          "cache_creation_input_tokens": 698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 698
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

_source line 52 · 2026-05-15T17:13:01.775Z_

<details><summary>↩ Tool result · `toolu_01Gg7QmxJLinGVfk21CdsWnG`</summary>

```text
total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 15 05:30 .
drwxr-xr-x 4 ubuntu ubuntu 4096 May 15 05:30 ..
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "734ede5c-e30a-45a9-b7c1-ea063f32c0d9",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "fbb4b134-ee1d-41d0-8fb4-e62d6a3fd1fd",
  "toolUseResult": {
    "stdout": "total 8\ndrwxr-xr-x 2 ubuntu ubuntu 4096 May 15 05:30 .\ndrwxr-xr-x 4 ubuntu ubuntu 4096 May 15 05:30 ..",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "734ede5c-e30a-45a9-b7c1-ea063f32c0d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T17:14:56.788Z_

<details open><summary>🔧 Tool call — Write · `toolu_01PhZDKTvi4ea7ZY7K5QXqec`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "content": "% References for Schema-DAG-Extraction\n% Generated: 2026-05-15\n% Sources: literature_map.yaml + references_survey.md\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@article{parse-2025,\n    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    journal = {arXiv preprint arXiv:2510.08623},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2510.08623},\n}\n\n@inproceedings{dee-2024,\n    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},\n    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},\n    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2406.01045},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n@article{dlisc-2025,\n    title   = {Effective and Efficient Schema-aware Information Extraction Using On-Device {LLM}s},\n    author  = {Wen, Zhihao and Liang, Sheng and Wu, Yaxiong and Zhang, Yongyue and Liu, Yong},\n    journal = {arXiv preprint arXiv:2505.14992},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.14992},\n}\n\n@article{spt-2025,\n    title   = {Schema as Parameterized Tools for Universal Information Extraction},\n    author  = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal = {arXiv preprint arXiv:2506.01276},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2506.01276},\n}\n\n@inproceedings{zeroner-2025,\n    title     = {{ZeroNER}: Fueling Zero-Shot {NER} via Entity Type Descriptions},\n    author    = {Cocchieri, Alessio and Mart{\\'\\i}nez Galindo, Marcos and Frisoni, Giacomo and Moro, Gianluca and Sartori, Claudio and Tagliavini, Giuseppe},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.805/},\n}\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Efficient Multi-Task {IE} System with Schema-Driven Interface},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2507.18546},\n}\n\n@inproceedings{kggen-2025,\n    title     = {{KGGen}: Extracting Knowledge Graphs from Plain Text with Language Models},\n    author    = {Mo, Belinda and Yu, Kyssen and Kazdan, Joshua and Cabezas, Joan and Mpala, Proud and Yu, Lisa and Cundy, Chris and Kanatsoulis, Charilaos and Koyejo, Sanmi},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2502.09956},\n}\n\n@inproceedings{code4uie-2024,\n    title     = {Retrieval-Augmented Code Generation for Universal Information Extraction},\n    author    = {Guo, Yucan and Li, Zixuan and Jin, Xiaolong and Liu, Yantao and Zeng, Yutao and Liu, Wenxuan and Li, Xiang and Yang, Pan and Bai, Long and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {NeurIPS 2024 Workshop},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.02962},\n}\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large-Scale Schema-Based Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2402.14710},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{self-improve-ner-2024,\n    title     = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08921},\n}\n\n@inproceedings{self-prompting-re-2024,\n    title     = {Unleashing the Power of {LLM}s in Zero-shot Relation Extraction via Self-Prompting},\n    author    = {Liu, Siyi and Li, Yang and Li, Jiang and Yang, Shan and Lan, Yunshi},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2410.01154},\n}\n\n@article{reasoning-ner-2025,\n    title   = {A Reasoning Paradigm for Named Entity Recognition},\n    author  = {Huang, Hui and Chen, Yanping and Huang, Ruizhang and Lin, Chuan and Qin, Yongbin},\n    journal = {arXiv preprint arXiv:2511.11978},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2511.11978},\n}\n\n@inproceedings{nuner-2024,\n    title     = {{NuNER}: Entity Recognition Encoder Pre-training via {LLM}-Annotated Data},\n    author    = {Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth{\\'e}e and Crabb{\\'e}, Benoit and Bernard, Etienne},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2402.15343},\n}\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n@inproceedings{familiarity-2025,\n    title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n    author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n    booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.10121},\n}\n\n@inproceedings{guidex-2025,\n    title     = {{GuideX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},\n    author    = {De La Fuente, Neil and Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agirre, Eneko},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.00649},\n}\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n@inproceedings{gao-repr-degen-2019,\n    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},\n    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1907.12009},\n}\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n@inproceedings{godey-anisotropy-inherent-2024,\n    title     = {Anisotropy Is Inherent to Self-Attention in Transformers},\n    author    = {Godey, Nathan and de la Clergerie, {\\'E}ric and Sagot, Beno{\\^\\i}t},\n    booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.eacl-long.3/},\n}\n\n@inproceedings{rajaee-cluster-isotropy-2021,\n    title     = {A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space},\n    author    = {Rajaee, Sara and Pilehvar, Mohammad Taher},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-short.73/},\n}\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and Yu, Shi and Yan, Yukun and Wang, Shuo and Zhang, Yue and Cao, Shulin and Ren, Weicheng and Gui, Honghao and Bi, Zhen and Huang, Yongfei and Yao, Yuan and Zhang, Ningyu and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n@inproceedings{genre-2021,\n    title     = {Autoregressive Entity Retrieval},\n    author    = {De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://arxiv.org/abs/2010.00904},\n}\n\n@inproceedings{inerd-2024,\n    title     = {Informed Named Entity Recognition Decoding for Generative Language Models},\n    author    = {Deu{\\ss}er, Tobias and Hillebrand, Lars Patrick and Bauckhage, Christian and Sifa, Rafet},\n    booktitle = {Proceedings of the IEEE International Conference on Big Data},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.07791},\n}\n\n@inproceedings{noisebench-2024,\n    title     = {{NoiseBench}: Benchmarking the Impact of Real Label Noise on Named Entity Recognition},\n    author    = {Merdjanovska, Elena and Aynetdinov, Ansar and Akbik, Alan},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.1011/},\n}\n\n@inproceedings{lrn-2021,\n    title     = {Fine-grained Entity Typing via Label Reasoning},\n    author    = {Liu, Qing and Lin, Hongyu and Xiao, Xinyan and Han, Xianpei and Sun, Le and Wu, Hua},\n    booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.emnlp-main.378/},\n}\n\n@inproceedings{genres-2024,\n    title     = {{GenRES}: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models},\n    author    = {Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jiawei},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.naacl-long.155/},\n}\n\n@inproceedings{multiconner2-2023,\n    title     = {{SemEval}-2023 Task 2: Fine-grained Multilingual Named Entity Recognition ({MultiCoNER} 2)},\n    author    = {Fetahu, Besnik and Kar, Sudipta and Chen, Zhiyu and Rokhlenko, Oleg and Malmasi, Shervin},\n    booktitle = {Proceedings of the 17th International Workshop on Semantic Evaluation},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.semeval-1.310/},\n}\n\n@inproceedings{llm-calibration-survey-2024,\n    title     = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n    author    = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.naacl-long.366/},\n}\n\n@inproceedings{far-calibration-2024,\n    title     = {Fact-and-Reflection ({FaR}) Improves Confidence Calibration of Large Language Models},\n    author    = {Zhao, Xinran and Zhang, Hongming and Pan, Xiaoman and Yao, Wenlin and Yu, Dong and Wu, Tongshuang and Chen, Jianshu},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.findings-acl.515/},\n}\n\n@inproceedings{linkner-2024,\n    title     = {{LinkNER}: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty},\n    author    = {Zhang, Zhen and Zhao, Yuhua and Gao, Hang and Hu, Mengting},\n    booktitle = {Proceedings of the ACM Web Conference 2024},\n    year      = {2024},\n    url       = {https://dl.acm.org/doi/10.1145/3589334.3645414},\n    doi       = {10.1145/3589334.3645414},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbb4b134-ee1d-41d0-8fb4-e62d6a3fd1fd",
  "isSidechain": false,
  "requestId": "req_011Cb4jDoEaLv33W9kMRJUJx",
  "type": "assistant",
  "uuid": "83511b62-8cd5-465d-9020-0f694fc57ce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9qz8NwBuVPH7sBPUgQUNV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1472,
      "cache_read_input_tokens": 46521,
      "output_tokens": 6877,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6877,
          "cache_read_input_tokens": 46521,
          "cache_creation_input_tokens": 1472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1472
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

_source line 54_

```json
{
  "type": "last-prompt",
  "leafUuid": "03647d2c-aaf2-43fc-b1f4-0b0b65c50ac0",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Build BibTeX references from YAML and Markdown",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Tool result

_source line 56 · 2026-05-15T17:14:57.012Z_

<details><summary>↩ Tool result · `toolu_01PhZDKTvi4ea7ZY7K5QXqec`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83511b62-8cd5-465d-9020-0f694fc57ce9",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "03647d2c-aaf2-43fc-b1f4-0b0b65c50ac0",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "content": "% References for Schema-DAG-Extraction\n% Generated: 2026-05-15\n% Sources: literature_map.yaml + references_survey.md\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@article{parse-2025,\n    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    journal = {arXiv preprint arXiv:2510.08623},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2510.08623},\n}\n\n@inproceedings{dee-2024,\n    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},\n    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},\n    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2406.01045},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n@article{dlisc-2025,\n    title   = {Effective and Efficient Schema-aware Information Extraction Using On-Device {LLM}s},\n    author  = {Wen, Zhihao and Liang, Sheng and Wu, Yaxiong and Zhang, Yongyue and Liu, Yong},\n    journal = {arXiv preprint arXiv:2505.14992},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.14992},\n}\n\n@article{spt-2025,\n    title   = {Schema as Parameterized Tools for Universal Information Extraction},\n    author  = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal = {arXiv preprint arXiv:2506.01276},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2506.01276},\n}\n\n@inproceedings{zeroner-2025,\n    title     = {{ZeroNER}: Fueling Zero-Shot {NER} via Entity Type Descriptions},\n    author    = {Cocchieri, Alessio and Mart{\\'\\i}nez Galindo, Marcos and Frisoni, Giacomo and Moro, Gianluca and Sartori, Claudio and Tagliavini, Giuseppe},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.805/},\n}\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Efficient Multi-Task {IE} System with Schema-Driven Interface},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2507.18546},\n}\n\n@inproceedings{kggen-2025,\n    title     = {{KGGen}: Extracting Knowledge Graphs from Plain Text with Language Models},\n    author    = {Mo, Belinda and Yu, Kyssen and Kazdan, Joshua and Cabezas, Joan and Mpala, Proud and Yu, Lisa and Cundy, Chris and Kanatsoulis, Charilaos and Koyejo, Sanmi},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2502.09956},\n}\n\n@inproceedings{code4uie-2024,\n    title     = {Retrieval-Augmented Code Generation for Universal Information Extraction},\n    author    = {Guo, Yucan and Li, Zixuan and Jin, Xiaolong and Liu, Yantao and Zeng, Yutao and Liu, Wenxuan and Li, Xiang and Yang, Pan and Bai, Long and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {NeurIPS 2024 Workshop},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.02962},\n}\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large-Scale Schema-Based Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2402.14710},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{self-improve-ner-2024,\n    title     = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08921},\n}\n\n@inproceedings{self-prompting-re-2024,\n    title     = {Unleashing the Power of {LLM}s in Zero-shot Relation Extraction via Self-Prompting},\n    author    = {Liu, Siyi and Li, Yang and Li, Jiang and Yang, Shan and Lan, Yunshi},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2410.01154},\n}\n\n@article{reasoning-ner-2025,\n    title   = {A Reasoning Paradigm for Named Entity Recognition},\n    author  = {Huang, Hui and Chen, Yanping and Huang, Ruizhang and Lin, Chuan and Qin, Yongbin},\n    journal = {arXiv preprint arXiv:2511.11978},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2511.11978},\n}\n\n@inproceedings{nuner-2024,\n    title     = {{NuNER}: Entity Recognition Encoder Pre-training via {LLM}-Annotated Data},\n    author    = {Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth{\\'e}e and Crabb{\\'e}, Benoit and Bernard, Etienne},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2402.15343},\n}\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n@inproceedings{familiarity-2025,\n    title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n    author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n    booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.10121},\n}\n\n@inproceedings{guidex-2025,\n    title     = {{GuideX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},\n    author    = {De La Fuente, Neil and Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agirre, Eneko},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.00649},\n}\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n@inproceedings{gao-repr-degen-2019,\n    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},\n    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1907.12009},\n}\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n@inproceedings{godey-anisotropy-inherent-2024,\n    title     = {Anisotropy Is Inherent to Self-Attention in Transformers},\n    author    = {Godey, Nathan and de la Clergerie, {\\'E}ric and Sagot, Beno{\\^\\i}t},\n    booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.eacl-long.3/},\n}\n\n@inproceedings{rajaee-cluster-isotropy-2021,\n    title     = {A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space},\n    author    = {Rajaee, Sara and Pilehvar, Mohammad Taher},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-short.73/},\n}\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and Yu, Shi and Yan, Yukun and Wang, Shuo and Zhang, Yue and Cao, Shulin and Ren, Weicheng and Gui, Honghao and Bi, Zhen and Huang, Yongfei and Yao, Yuan and Zhang, Ningyu and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n@inproceedings{genre-2021,\n    title     = {Autoregressive Entity Retrieval},\n    author    = {De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://arxiv.org/abs/2010.00904},\n}\n\n@inproceedings{inerd-2024,\n    title     = {Informed Named Entity Recognition Decoding for Generative Language Models},\n    author    = {Deu{\\ss}er, Tobias and Hillebrand, Lars Patrick and Bauckhage, Christian and Sifa, Rafet},\n    booktitle = {Proceedings of the IEEE International Conference on Big Data},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.07791},\n}\n\n@inproceedings{noisebench-2024,\n    title     = {{NoiseBench}: Benchmarking the Impact of Real Label Noise on Named Entity Recognition},\n    author    = {Merdjanovska, Elena and Aynetdinov, Ansar and Akbik, Alan},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.1011/},\n}\n\n@inproceedings{lrn-2021,\n    title     = {Fine-grained Entity Typing via Label Reasoning},\n    author    = {Liu, Qing and Lin, Hongyu and Xiao, Xinyan and Han, Xianpei and Sun, Le and Wu, Hua},\n    booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.emnlp-main.378/},\n}\n\n@inproceedings{genres-2024,\n    title     = {{GenRES}: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models},\n    author    = {Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jiawei},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.naacl-long.155/},\n}\n\n@inproceedings{multiconner2-2023,\n    title     = {{SemEval}-2023 Task 2: Fine-grained Multilingual Named Entity Recognition ({MultiCoNER} 2)},\n    author    = {Fetahu, Besnik and Kar, Sudipta and Chen, Zhiyu and Rokhlenko, Oleg and Malmasi, Shervin},\n    booktitle = {Proceedings of the 17th International Workshop on Semantic Evaluation},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.semeval-1.310/},\n}\n\n@inproceedings{llm-calibration-survey-2024,\n    title     = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n    author    = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.naacl-long.366/},\n}\n\n@inproceedings{far-calibration-2024,\n    title     = {Fact-and-Reflection ({FaR}) Improves Confidence Calibration of Large Language Models},\n    author    = {Zhao, Xinran and Zhang, Hongming and Pan, Xiaoman and Yao, Wenlin and Yu, Dong and Wu, Tongshuang and Chen, Jianshu},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.findings-acl.515/},\n}\n\n@inproceedings{linkner-2024,\n    title     = {{LinkNER}: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty},\n    author    = {Zhang, Zhen and Zhao, Yuhua and Gao, Hang and Hu, Mengting},\n    booktitle = {Proceedings of the ACM Web Conference 2024},\n    year      = {2024},\n    url       = {https://dl.acm.org/doi/10.1145/3589334.3645414},\n    doi       = {10.1145/3589334.3645414},\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "83511b62-8cd5-465d-9020-0f694fc57ce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T17:14:59.856Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XL33yguJzP5J7kAEgpmV7M`</summary>

```json
{
  "command": "grep -c '^@' /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "description": "Count BibTeX entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03647d2c-aaf2-43fc-b1f4-0b0b65c50ac0",
  "isSidechain": false,
  "requestId": "req_011Cb4jNJ4eWcxjdTEC7P2wC",
  "type": "assistant",
  "uuid": "43a9df11-30b2-4304-b7f4-9956c9290016",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoqPYFDK4EMcnJY3rE8SbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6930,
      "cache_read_input_tokens": 47993,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 47993,
          "cache_creation_input_tokens": 6930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6930
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

_source line 58 · 2026-05-15T17:14:59.915Z_

<details><summary>↩ Tool result · `toolu_01XL33yguJzP5J7kAEgpmV7M`</summary>

```text
43
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43a9df11-30b2-4304-b7f4-9956c9290016",
  "isSidechain": false,
  "promptId": "6cb7787f-a3ed-49e8-96d5-e9c9df6f1973",
  "type": "user",
  "uuid": "085dd17d-1b56-4fb7-911c-479f644c2b44",
  "toolUseResult": {
    "stdout": "43",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "43a9df11-30b2-4304-b7f4-9956c9290016",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-15T17:15:06.225Z_

43 个 BibTeX entries，来源分布：

- literature_map.yaml 原有 30 条全部覆盖
- references_survey.md 新增 13 条：`instructuie-2023`, `codeie-2023`, `adelie-2024`, `oneke-2025`, `genre-2021`, `inerd-2024`, `noisebench-2024`, `lrn-2021`, `genres-2024`, `multiconner2-2023`, `llm-calibration-survey-2024`, `far-calibration-2024`, `linkner-2024`

所有 entry 均包含 title、author、year、booktitle/journal、url 必填字段。缺失作者信息已通过 arXiv/ACL Anthology 页面补全。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "085dd17d-1b56-4fb7-911c-479f644c2b44",
  "isSidechain": false,
  "requestId": "req_011Cb4jNWK6ZDWEuz9v51JaR",
  "type": "assistant",
  "uuid": "3c7b6e10-856e-4996-8e47-9808709e458a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MCT8evQf7WrHxaBdii5nsQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 128,
      "cache_read_input_tokens": 54923,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 54923,
          "cache_creation_input_tokens": 128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 128
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
  "leafUuid": "3c7b6e10-856e-4996-8e47-9808709e458a",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Build BibTeX references from YAML and Markdown",
  "sessionId": "0e2349f2-4207-4d96-b1ce-1cf37c2379e5"
}
```

---
