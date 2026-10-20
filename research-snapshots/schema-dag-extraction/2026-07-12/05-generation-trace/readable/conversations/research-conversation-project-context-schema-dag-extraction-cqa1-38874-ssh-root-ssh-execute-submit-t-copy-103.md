# Research conversation: <project_context> # 项目: schema-dag-extraction ## 运行环境 - 服务器名: cqa1-38874 - SSH 账户: root（调用 ssh_execute / submit_training

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/38df3856-e893-4a84-8aa9-007fca6d282d.jsonl`
- **Structured JSON:** [`7c43eba8c1824ba5e674.json`](../../sessions/7c/7c43eba8c1824ba5e674.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T19:10:26.023Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T19:10:26.023Z",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "content": "&lt;project_context>\n# 项目: schema-dag-extraction\n\n## 运行环境\n- 服务器名: cqa1-38874\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/schema-dag-extraction\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：撰写 Abstract（~250 words）\n\n论文题目：Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?（EMNLP 2026）\n\n### 写前必读\n1. `Read /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex` — findings + contributions\n2. `Read /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex` — tempered claims\n\n### Abstract 结构（~250 words, 一段）\n\n\\begin{abstract}\n...\n\\end{abstract}\n\n必须覆盖 5 个元素：\n\n1. **Problem**（~40 words）：Training-free LLM IE degrades on complex schemas（NER recall 0.72→0.42, RE accuracy 85.7%→50.4%）。Prior work conflates count and confusability.\n\n2. **Method**（~50 words）：First controlled empirical study isolating type confusability from count. Schema Confusability Score (SCS) + two experimental paradigms (count curves, BCS-controlled) across 3 IE tasks (NER, RE, ED) with 3 datasets.\n\n3. **Findings**（~100 words）：\n   - Two orthogonal channels: count→recall, confusability→type confusion (IntraSub)\n   - Pairwise SCS robust cross-task (r=0.112-0.129, r²≈1.3-1.7%) — \"modest but first empirically isolated\"\n   - BCS amplification 3.4× (9.1pp→31.2pp)\n   - Centrality confound on homogeneous schemas reverses per-type correlation\n\n4. **Negative result**（~30 words）：Confusability-aware decomposition (SDGD) fails due to merge amplification — structural bottleneck for decompose-then-merge pipelines.\n\n5. **Significance**（~30 words）：Practical implications for schema design; identifies merge as the key challenge for decomposition approaches.\n\n### 关键约束\n- r² 必须在 abstract 中出现（DR2 critical fix）\n- 不用 \"significantly\", \"state-of-the-art\", \"consistently outperforms\"\n- MAVEN 的反向趋势不在 abstract 中展开（太细节），但 count degradation 限定为 \"NER and RE\"\n- 数字与 §1 和 §4 完全一致\n- 不引用参考文献（abstract 中不放 \\cite）\n\n### 输出\n写入：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex`\n\n只写 \\begin{abstract}...\\end{abstract} 块。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T19:10:26.026Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T19:10:26.026Z",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-15T19:10:26.060Z_

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
## 任务：撰写 Abstract（~250 words）

论文题目：Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?（EMNLP 2026）

### 写前必读
1. `Read /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex` — findings + contributions
2. `Read /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex` — tempered claims

### Abstract 结构（~250 words, 一段）

\begin{abstract}
...
\end{abstract}

必须覆盖 5 个元素：

1. **Problem**（~40 words）：Training-free LLM IE degrades on complex schemas（NER recall 0.72→0.42, RE accuracy 85.7%→50.4%）。Prior work conflates count and confusability.

2. **Method**（~50 words）：First controlled empirical study isolating type confusability from count. Schema Confusability Score (SCS) + two experimental paradigms (count curves, BCS-controlled) across 3 IE tasks (NER, RE, ED) with 3 datasets.

3. **Findings**（~100 words）：
   - Two orthogonal channels: count→recall, confusability→type confusion (IntraSub)
   - Pairwise SCS robust cross-task (r=0.112-0.129, r²≈1.3-1.7%) — "modest but first empirically isolated"
   - BCS amplification 3.4× (9.1pp→31.2pp)
   - Centrality confound on homogeneous schemas reverses per-type correlation

4. **Negative result**（~30 words）：Confusability-aware decomposition (SDGD) fails due to merge amplification — structural bottleneck for decompose-then-merge pipelines.

5. **Significance**（~30 words）：Practical implications for schema design; identifies merge as the key challenge for decomposition approaches.

### 关键约束
- r² 必须在 abstract 中出现（DR2 critical fix）
- 不用 "significantly", "state-of-the-art", "consistently outperforms"
- MAVEN 的反向趋势不在 abstract 中展开（太细节），但 count degradation 限定为 "NER and RE"
- 数字与 §1 和 §4 完全一致
- 不引用参考文献（abstract 中不放 \cite）

### 输出
写入：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex`

只写 \begin{abstract}...\end{abstract} 块。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "cc1da8f5-8a4f-40f4-9e3e-d195f4b47f92",
  "type": "user",
  "uuid": "0fce55f4-1c47-47a3-9148-fb711f405b53",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T19:10:26.060Z_

```json
{
  "parentUuid": "0fce55f4-1c47-47a3-9148-fb711f405b53",
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
  "uuid": "962f7540-66fd-4c19-b37b-0f4643133868",
  "timestamp": "2026-05-15T19:10:26.060Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T19:10:26.060Z_

```json
{
  "parentUuid": "962f7540-66fd-4c19-b37b-0f4643133868",
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
  "uuid": "1e207a54-e464-4a0f-82e9-f1d53afdb8ba",
  "timestamp": "2026-05-15T19:10:26.060Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T19:10:26.060Z_

```json
{
  "parentUuid": "1e207a54-e464-4a0f-82e9-f1d53afdb8ba",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fec8d4f6-dd4d-4735-8eb8-bc1e15a2e634",
  "timestamp": "2026-05-15T19:10:26.060Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
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
  "aiTitle": "Write paper abstract for schema-DAG extraction study",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d"
}
```

---

### Assistant

_source line 8 · 2026-05-15T19:10:29.526Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the introduction and conclusion files first to ensure consistency with the claims and numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fec8d4f6-dd4d-4735-8eb8-bc1e15a2e634",
  "isSidechain": false,
  "requestId": "req_011Cb4tB4ZnPB27NFzb77aP6",
  "type": "assistant",
  "uuid": "79d07f30-7e57-4c92-a0f6-58f0df986848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qxeZDQ9HFpTDvvvYYqLV6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11898,
      "cache_read_input_tokens": 11841,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 191,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11898
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

_source line 9 · 2026-05-15T19:10:30.075Z_

<details open><summary>🔧 Tool call — Read · `toolu_012wqJocKQDRALdriXf3hm4C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79d07f30-7e57-4c92-a0f6-58f0df986848",
  "isSidechain": false,
  "requestId": "req_011Cb4tB4ZnPB27NFzb77aP6",
  "type": "assistant",
  "uuid": "ad9da2d6-6b25-4763-a611-6621dae56930",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qxeZDQ9HFpTDvvvYYqLV6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11898,
      "cache_read_input_tokens": 11841,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 191,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11898
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

_source line 10 · 2026-05-15T19:10:30.094Z_

<details><summary>↩ Tool result · `toolu_012wqJocKQDRALdriXf3hm4C`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	To answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \emph{count curves} that vary schema size while randomizing confusability, and \emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on three datasets spanning diverse schema structures: Few-NERD \cite{fewnerd-2021} (66 entity types across 8 domains), FewRel \cite{fewrel-2018} (80 relation types), and MAVEN \cite{maven-2020} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.
11	
12	Five findings emerge from our experiments.
13	
14	First, schema-induced degradation operates through two orthogonal channels. \textbf{Channel~1} (count $\to$ recall decline): increasing the number of types in the prompt reduces recall for NER and RE, as more candidate types compete for the model's attention. \textbf{Channel~2} (confusability $\to$ type confusion): semantically similar types trigger intra-batch substitution errors (IntraSub), where the model assigns an entity or relation to a neighboring type in embedding space. These channels are mechanistically distinct---Channel~1 reflects capacity limitations, Channel~2 reflects semantic indistinguishability---and both contribute to the overall degradation pattern.
15	
16	Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD (Pearson $r = 0.112$, $p < 10^{-12}$) and MAVEN ($r = 0.129$, $p < 10^{-10}$), embedding similarity between type pairs correlates with confusion rates, and this signal replicates across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings). The effect is modest in magnitude: pairwise confusability explains roughly 1.3--1.7\% of the variance in type confusion ($r^2 \approx 0.013\text{--}0.017$). Entity frequency, prompt position effects \cite{lost-in-middle-2024}, and type definition quality jointly account for the remainder. Nevertheless, this is the first factor to be empirically isolated in controlled zero-shot IE experiments, and the signal survives bootstrap resampling with confidence intervals bounded well above zero.
17	
18	Third, confusability effects amplify with schema scale. In BCS-controlled FewRel experiments, switching from low-confusability to high-confusability type batches reduces accuracy by 9.1 percentage points at the 16-relation scale, but the gap widens to 31.2\,pp at 80 relations (95\% CI: [17.7, 42.7])---a $3.4\times$ amplification. Larger type pools provide more opportunities for semantically similar types to co-occur, expanding the confusion space.
19	
20	Fourth, per-type confusability aggregation is confounded on homogeneous schemas. On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation between mean BCS and per-type error rate reverses sign ($\rho = +0.189$, $p = 0.021$), opposite to the predicted direction. This centrality confound arises because, in single-cluster embedding spaces \cite{cai-isotropy-clusters-2021}, a type's mean similarity conflates confusability with centrality---a property associated with well-represented types that LLMs extract reliably. The pairwise SCS signal remains intact ($r = 0.129$, CI: [0.104, 0.156]), confirming that the confound lies in the aggregation step, not in the underlying pairwise relationship. Few-NERD, whose types span multiple domains, does not exhibit this confound ($\rho = -0.293$, $p = 0.02$).
21	
22	Fifth, confusability-aware schema decomposition fails to improve extraction. Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types into different batches, yet every decomposition mode---including random batching and per-type extraction---produces lower F1 than single-pass extraction (best decomposition F1 = 0.320 vs.\ single-pass F1 = 0.445). The bottleneck is \emph{merge amplification}: when the same text is processed across multiple extraction passes, the union merge step accumulates contradictory predictions, destroying precision. This structural limitation applies to any decompose-then-merge pipeline, including the partitioning approach of \citet{llm-pee-2025}.
23	
24	Our contributions are:
25	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
26	    \item \textbf{Multi-channel degradation model.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, showing that these channels are mechanistically distinct.
27	    \item \textbf{Pairwise confusability as a robust predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.
28	    \item \textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types.
29	    \item \textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural bottleneck for decompose-then-merge approaches, with direct implications for the design of schema decomposition methods.
30	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad9da2d6-6b25-4763-a611-6621dae56930",
  "isSidechain": false,
  "promptId": "cc1da8f5-8a4f-40f4-9e3e-d195f4b47f92",
  "type": "user",
  "uuid": "9125288b-d588-4da7-9c84-024dcc2881c8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \\citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \\citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \\citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \\emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \\cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \\emph{count curves} that vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on three datasets spanning diverse schema structures: Few-NERD \\cite{fewnerd-2021} (66 entity types across 8 domains), FewRel \\cite{fewrel-2018} (80 relation types), and MAVEN \\cite{maven-2020} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.\n\nFive findings emerge from our experiments.\n\nFirst, schema-induced degradation operates through two orthogonal channels. \\textbf{Channel~1} (count $\\to$ recall decline): increasing the number of types in the prompt reduces recall for NER and RE, as more candidate types compete for the model's attention. \\textbf{Channel~2} (confusability $\\to$ type confusion): semantically similar types trigger intra-batch substitution errors (IntraSub), where the model assigns an entity or relation to a neighboring type in embedding space. These channels are mechanistically distinct---Channel~1 reflects capacity limitations, Channel~2 reflects semantic indistinguishability---and both contribute to the overall degradation pattern.\n\nSecond, pairwise SCS is a robust predictor of type confusion. Across Few-NERD (Pearson $r = 0.112$, $p < 10^{-12}$) and MAVEN ($r = 0.129$, $p < 10^{-10}$), embedding similarity between type pairs correlates with confusion rates, and this signal replicates across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings). The effect is modest in magnitude: pairwise confusability explains roughly 1.3--1.7\\% of the variance in type confusion ($r^2 \\approx 0.013\\text{--}0.017$). Entity frequency, prompt position effects \\cite{lost-in-middle-2024}, and type definition quality jointly account for the remainder. Nevertheless, this is the first factor to be empirically isolated in controlled zero-shot IE experiments, and the signal survives bootstrap resampling with confidence intervals bounded well above zero.\n\nThird, confusability effects amplify with schema scale. In BCS-controlled FewRel experiments, switching from low-confusability to high-confusability type batches reduces accuracy by 9.1 percentage points at the 16-relation scale, but the gap widens to 31.2\\,pp at 80 relations (95\\% CI: [17.7, 42.7])---a $3.4\\times$ amplification. Larger type pools provide more opportunities for semantically similar types to co-occur, expanding the confusion space.\n\nFourth, per-type confusability aggregation is confounded on homogeneous schemas. On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation between mean BCS and per-type error rate reverses sign ($\\rho = +0.189$, $p = 0.021$), opposite to the predicted direction. This centrality confound arises because, in single-cluster embedding spaces \\cite{cai-isotropy-clusters-2021}, a type's mean similarity conflates confusability with centrality---a property associated with well-represented types that LLMs extract reliably. The pairwise SCS signal remains intact ($r = 0.129$, CI: [0.104, 0.156]), confirming that the confound lies in the aggregation step, not in the underlying pairwise relationship. Few-NERD, whose types span multiple domains, does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$).\n\nFifth, confusability-aware schema decomposition fails to improve extraction. Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types into different batches, yet every decomposition mode---including random batching and per-type extraction---produces lower F1 than single-pass extraction (best decomposition F1 = 0.320 vs.\\ single-pass F1 = 0.445). The bottleneck is \\emph{merge amplification}: when the same text is processed across multiple extraction passes, the union merge step accumulates contradictory predictions, destroying precision. This structural limitation applies to any decompose-then-merge pipeline, including the partitioning approach of \\citet{llm-pee-2025}.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Multi-channel degradation model.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, showing that these channels are mechanistically distinct.\n    \\item \\textbf{Pairwise confusability as a robust predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types.\n    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural bottleneck for decompose-then-merge approaches, with direct implications for the design of schema decomposition methods.\n\\end{enumerate}",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  },
  "sourceToolAssistantUUID": "ad9da2d6-6b25-4763-a611-6621dae56930",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T19:10:30.450Z_

<details><summary>↩ Tool result · `toolu_01Sp2EvL7hopeBp6rqCjNfzS`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented a controlled empirical study isolating the factors behind schema-induced degradation in training-free LLM information extraction. Our experiments across NER, RE, and ED reveal that degradation operates through two orthogonal channels: a count channel, where increasing the number of candidate types suppresses recall, and a confusability channel, where semantically similar types trigger intra-batch substitution errors. These channels are mechanistically distinct---the first reflects capacity limitations as types compete for attention, the second reflects semantic indistinguishability regardless of schema size.
5	
6	Pairwise type confusability, quantified by the Schema Confusability Score, is a partial but robust predictor of type confusion. The signal is modest in magnitude ($r^2 \approx 1.3\text{--}1.7\%$), yet it replicates across three tasks, two embedding spaces, and survives bootstrap resampling---making it the first factor to be empirically isolated in controlled zero-shot IE experiments. Entity frequency, prompt position, and type definition quality account for the remaining variance; disentangling these factors is an open problem. We further identify a centrality confound that reverses per-type aggregation on same-domain schemas, a methodological finding relevant to any embedding-based schema analysis.
7	
8	Our Schema-DAG-Guided Decomposition experiments yield an informative negative result: separating confusable types into different batches does not improve extraction, because merge amplification destroys precision across all decomposition strategies. This structural bottleneck applies broadly to decompose-then-merge pipelines.
9	
10	Several limitations bound our findings. All experiments use a single model (Qwen3-32B); multi-model validation is an immediate priority. Future work should address the merge bottleneck directly---calibration-based cross-batch consistency, joint decoding over decomposed outputs, or confidence-weighted merging with better-calibrated scores---to translate confusability signals into extraction gains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab7cb7ad-b7f2-4898-a29c-92c814ebd8d2",
  "isSidechain": false,
  "promptId": "cc1da8f5-8a4f-40f4-9e3e-d195f4b47f92",
  "type": "user",
  "uuid": "b0cba8ab-39f7-42e1-b945-9d23b7f04d8d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a controlled empirical study isolating the factors behind schema-induced degradation in training-free LLM information extraction. Our experiments across NER, RE, and ED reveal that degradation operates through two orthogonal channels: a count channel, where increasing the number of candidate types suppresses recall, and a confusability channel, where semantically similar types trigger intra-batch substitution errors. These channels are mechanistically distinct---the first reflects capacity limitations as types compete for attention, the second reflects semantic indistinguishability regardless of schema size.\n\nPairwise type confusability, quantified by the Schema Confusability Score, is a partial but robust predictor of type confusion. The signal is modest in magnitude ($r^2 \\approx 1.3\\text{--}1.7\\%$), yet it replicates across three tasks, two embedding spaces, and survives bootstrap resampling---making it the first factor to be empirically isolated in controlled zero-shot IE experiments. Entity frequency, prompt position, and type definition quality account for the remaining variance; disentangling these factors is an open problem. We further identify a centrality confound that reverses per-type aggregation on same-domain schemas, a methodological finding relevant to any embedding-based schema analysis.\n\nOur Schema-DAG-Guided Decomposition experiments yield an informative negative result: separating confusable types into different batches does not improve extraction, because merge amplification destroys precision across all decomposition strategies. This structural bottleneck applies broadly to decompose-then-merge pipelines.\n\nSeveral limitations bound our findings. All experiments use a single model (Qwen3-32B); multi-model validation is an immediate priority. Future work should address the merge bottleneck directly---calibration-based cross-batch consistency, joint decoding over decomposed outputs, or confidence-weighted merging with better-calibrated scores---to translate confusability signals into extraction gains.",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "ab7cb7ad-b7f2-4898-a29c-92c814ebd8d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T19:10:30.440Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Sp2EvL7hopeBp6rqCjNfzS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9125288b-d588-4da7-9c84-024dcc2881c8",
  "isSidechain": false,
  "requestId": "req_011Cb4tB4ZnPB27NFzb77aP6",
  "type": "assistant",
  "uuid": "ab7cb7ad-b7f2-4898-a29c-92c814ebd8d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qxeZDQ9HFpTDvvvYYqLV6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11898,
      "cache_read_input_tokens": 11841,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 191,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11898
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

_source line 13_

```json
{
  "type": "last-prompt",
  "leafUuid": "b0cba8ab-39f7-42e1-b945-9d23b7f04d8d",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Write paper abstract for schema-DAG extraction study",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d"
}
```

---

### Assistant

_source line 15 · 2026-05-15T19:10:32.722Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me also check if abstract.tex already exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0cba8ab-39f7-42e1-b945-9d23b7f04d8d",
  "isSidechain": false,
  "requestId": "req_011Cb4tBPXJURmiJdrHBMV1u",
  "type": "assistant",
  "uuid": "64547daa-f90e-450f-8eca-61a5a1366e60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKuvmLt1UWSSiyYHnJh8Wx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2811,
      "cache_read_input_tokens": 23739,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2811,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 23739,
          "cache_creation_input_tokens": 2811,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2811
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

_source line 16 · 2026-05-15T19:10:33.217Z_

Now let me check if the abstract file already exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64547daa-f90e-450f-8eca-61a5a1366e60",
  "isSidechain": false,
  "requestId": "req_011Cb4tBPXJURmiJdrHBMV1u",
  "type": "assistant",
  "uuid": "661b80ec-2f3f-4395-9469-9753926cadda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKuvmLt1UWSSiyYHnJh8Wx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2811,
      "cache_read_input_tokens": 23739,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2811,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 23739,
          "cache_creation_input_tokens": 2811,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2811
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

_source line 17 · 2026-05-15T19:10:34.102Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01E9vhBCaRaUoks27ps2t4wY`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex 2>/dev/null; echo \"EXIT:$?\"",
  "description": "Check if abstract.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "661b80ec-2f3f-4395-9469-9753926cadda",
  "isSidechain": false,
  "requestId": "req_011Cb4tBPXJURmiJdrHBMV1u",
  "type": "assistant",
  "uuid": "9aa7c836-9da5-4f37-ae2c-0eee1535b0d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKuvmLt1UWSSiyYHnJh8Wx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2811,
      "cache_read_input_tokens": 23739,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2811,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 23739,
          "cache_creation_input_tokens": 2811,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2811
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

_source line 18 · 2026-05-15T19:10:34.303Z_

<details><summary>↩ Tool result · `toolu_01E9vhBCaRaUoks27ps2t4wY`</summary>

```text
EXIT:2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aa7c836-9da5-4f37-ae2c-0eee1535b0d3",
  "isSidechain": false,
  "promptId": "cc1da8f5-8a4f-40f4-9e3e-d195f4b47f92",
  "type": "user",
  "uuid": "cf12b212-abce-44d5-9eeb-d9bb82ca390c",
  "toolUseResult": {
    "stdout": "EXIT:2",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9aa7c836-9da5-4f37-ae2c-0eee1535b0d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T19:11:17.853Z_

<details><summary>Logged reasoning block</summary>

```text
The file doesn't exist. Let me now draft the abstract carefully, making sure to:

1. Cover all 5 elements (Problem, Method, Findings, Negative result, Significance)
2. Include r² values (DR2 critical fix)
3. Match numbers exactly with §1: NER recall 0.72→0.42, RE accuracy 85.7%→50.4%, r=0.112-0.129, r²≈0.013-0.017 (1.3-1.7%), BCS amplification 3.4× (9.1pp→31.2pp)


4. No "significantly", "state-of-the-art", "consistently outperforms"
5. No \cite references
6. MAVEN reversal not expanded
7. Count degradation limited to "NER and RE"
8. ~250 words, one paragraph

Now I'm drafting the abstract with these constraints in mind—keeping it to a single paragraph around 250 words, avoiding superlatives and citations, and sticking precisely to the numerical results from the main text. The pairwise confusability metric explains a small but meaningful slice of the variance in type confusion errors, and this effect intensifies dramatically as schemas grow larger—accuracy drops by over 20 percentage points when scaling from 16 to 80 types. I'm also noting that a centrality confound affects how we aggregate results on uniform schemas, though the core pairwise signal holds up. On the practical side, my attempt to mitigate confusability through schema decomposition backfired because merging predictions across batches amplified errors and tanked precision, revealing a fundamental limitation in decompose-then-merge approaches.

These results point to concrete design principles for zero-shot extraction and highlight merge amplification as the critical bottleneck that needs solving before decomposition strategies can actually work. design two experimental paradigms—count curves and BCS-controlled batches—across three tasks (NER, RE, event detection) and three datasets. Our experiments reveal that schema-induced degradation operates through two orthogonal channels: a count channel that suppresses recall in NER and RE as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors. Pairwise SCS predicts type confusion across tasks (Pearson $r = 0.112$--$0.129$), explaining 1.3--1.7\% of variance in type confusion ($r^2 \approx 0.013$--$0.017$)—modest in magnitude but the first factor empirically isolated in controlled zero-shot IE experiments. Confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. Beyond the count effect, I'm also uncovering a centrality confound that actually reverses how we aggregate per-type confusability on homogeneous schemas, though the pairwise signal stays robust. When I apply confusability-aware decomposition, the results are telling: merging predictions destroys precision regardless of decomposition strategy, which points to a fundamental structural limitation in decompose-then-merge approaches. This suggests schema design choices matter significantly, and merge amplification is really the core bottleneck we need to address for these decomposition methods to work better. leaving the mechanisms behind this degradation unclear." = ~15. Total ~54... hmm, that's a bit over 40 for Problem. But we can count the "Prior work" sentence as part of Problem since it sets up the gap.

Let me just count the total more carefully...

Actually let me just write it carefully and count at the end. Let me aim for ~250 words.

Draft:

Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms behind this degradation unclear. We conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks (NER, RE, event detection) and three datasets. We introduce the Schema Confusability Score to quantify pairwise semantic overlap between types, then design two complementary experimental paradigms: one that varies schema size while randomizing confusability, and another that fixes size while varying confusability. Our experiments uncover two distinct degradation channels---a count effect that suppresses recall as candidate types increase, and a confusability effect where semantically similar types cause substitution errors. Pairwise confusability predicts type confusion across tasks, though the effect size is modest. Confusability effects amplify substantially as schema size grows from 16 to 80 types, with accuracy gaps widening significantly. We also identify a centrality confound that reverses per-type confusability...

Actually, I realize the next thinking is continuing from where the current rewritten thinking left off. The current rewritten thinking ends mid-sentence: "We further identify a centrality confound that reverses per-type confusability"

The next thinking continues with "aggregation on homogeneous schemas while the pairwise signal remains intact."

So I need to complete that sentence and then add the new material about SDGD and merge amplification.

Let me rewrite just the next chunk:

The centrality confound reverses per-type confusability aggregation on homogeneous schemas, though the pairwise signal persists. Our confusability-aware decomposition approach reveals that merge amplification destroys precision across all strategies, exposing a fundamental bottleneck in decompose-then-merge pipelines. These results have direct implications for schema design and identify merge amplification as the critical obstacle preventing decomposition methods from scaling in zero-shot IE. We find that a confusability channel emerges where semantically similar types cause substitution errors within batches, and pairwise SCS scores predict type confusion across tasks with modest but meaningful correlations—the first empirically isolated factor in controlled zero-shot IE experiments. These confusability effects intensify significantly as schema size increases. Now I'm verifying that all the key numbers from the paper are properly cited and positioned throughout the text—checking that the NER and RE performance drops, correlation coefficients, variance explained, and the amplification factor all appear in the right places without redundancy.

I'm reconsidering the word count; 267 words is close enough to the ~250 target since abstracts typically allow some flexibility around that threshold. I should finalize the version and make sure the LaTeX formatting uses proper em dashes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf12b212-abce-44d5-9eeb-d9bb82ca390c",
  "isSidechain": false,
  "requestId": "req_011Cb4tBfvXfkqXnJ2Cuf2DT",
  "type": "assistant",
  "uuid": "25cbecbf-2119-439d-925c-e56aa69fc75f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G11TQAAFERL89Scv7k7NvR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 183,
      "cache_read_input_tokens": 26550,
      "output_tokens": 4164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4164,
          "cache_read_input_tokens": 26550,
          "cache_creation_input_tokens": 183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 183
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

_source line 20 · 2026-05-15T19:11:17.855Z_

Now I'll write the abstract, carefully matching all numbers from the introduction and following the structural constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25cbecbf-2119-439d-925c-e56aa69fc75f",
  "isSidechain": false,
  "requestId": "req_011Cb4tBfvXfkqXnJ2Cuf2DT",
  "type": "assistant",
  "uuid": "b4978636-6a11-4c11-a438-42a54a51a853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G11TQAAFERL89Scv7k7NvR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 183,
      "cache_read_input_tokens": 26550,
      "output_tokens": 4164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4164,
          "cache_read_input_tokens": 26550,
          "cache_creation_input_tokens": 183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 183
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

_source line 21 · 2026-05-15T19:11:22.374Z_

<details open><summary>🔧 Tool call — Write · `toolu_01RH2HzWBHyEm3v49StxJQKN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms behind this degradation unclear. We conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks (NER, RE, event detection) and three datasets. We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic overlap between types and design two complementary experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two orthogonal degradation channels: a count channel that suppresses recall in NER and RE as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors. Pairwise SCS predicts type confusion across tasks (Pearson $r = 0.112$--$0.129$, $r^2 \\approx 0.013$--$0.017$)---modest in magnitude but the first factor empirically isolated in controlled zero-shot IE experiments. Confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. We further identify a centrality confound that reverses per-type confusability aggregation on homogeneous schemas while the pairwise signal remains intact. Our confusability-aware decomposition (SDGD) yields an informative negative result: merge amplification destroys precision across all decomposition strategies, revealing a structural bottleneck for decompose-then-merge pipelines. These findings carry practical implications for schema design and identify merge amplification as the key obstacle for decomposition approaches in zero-shot IE.\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4978636-6a11-4c11-a438-42a54a51a853",
  "isSidechain": false,
  "requestId": "req_011Cb4tBfvXfkqXnJ2Cuf2DT",
  "type": "assistant",
  "uuid": "b07ef4df-c771-42a4-bc21-0af0e60dc580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G11TQAAFERL89Scv7k7NvR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 183,
      "cache_read_input_tokens": 26550,
      "output_tokens": 4164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4164,
          "cache_read_input_tokens": 26550,
          "cache_creation_input_tokens": 183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 183
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

_source line 22 · 2026-05-15T19:11:22.393Z_

<details><summary>↩ Tool result · `toolu_01RH2HzWBHyEm3v49StxJQKN`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b07ef4df-c771-42a4-bc21-0af0e60dc580",
  "isSidechain": false,
  "promptId": "cc1da8f5-8a4f-40f4-9e3e-d195f4b47f92",
  "type": "user",
  "uuid": "b9058795-4987-4069-8eb9-2d8a5e9e3c6a",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms behind this degradation unclear. We conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks (NER, RE, event detection) and three datasets. We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic overlap between types and design two complementary experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two orthogonal degradation channels: a count channel that suppresses recall in NER and RE as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors. Pairwise SCS predicts type confusion across tasks (Pearson $r = 0.112$--$0.129$, $r^2 \\approx 0.013$--$0.017$)---modest in magnitude but the first factor empirically isolated in controlled zero-shot IE experiments. Confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. We further identify a centrality confound that reverses per-type confusability aggregation on homogeneous schemas while the pairwise signal remains intact. Our confusability-aware decomposition (SDGD) yields an informative negative result: merge amplification destroys precision across all decomposition strategies, revealing a structural bottleneck for decompose-then-merge pipelines. These findings carry practical implications for schema design and identify merge amplification as the key obstacle for decomposition approaches in zero-shot IE.\n\\end{abstract}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "b07ef4df-c771-42a4-bc21-0af0e60dc580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "leafUuid": "b9058795-4987-4069-8eb9-2d8a5e9e3c6a",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Write paper abstract for schema-DAG extraction study",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d"
}
```

---

### Assistant

_source line 25 · 2026-05-15T19:11:28.685Z_

已写入 `abstract.tex`。约 260 words，覆盖全部 5 个元素。数字核对：

| 指标 | Abstract | §1 一致性 |
|------|----------|-----------|
| NER recall 0.72→0.42 | ✓ | ✓ |
| RE accuracy 85.7%→50.4% | ✓ | ✓ |
| r = 0.112–0.129 | ✓ | ✓ |
| r² ≈ 0.013–0.017 | ✓ (DR2 fix) | ✓ |
| 3.4× amplification, 9.1→31.2 pp | ✓ | ✓ |
| Count degradation限定NER and RE | ✓ | ✓ |
| 无 \cite、无禁用词 | ✓ | — |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9058795-4987-4069-8eb9-2d8a5e9e3c6a",
  "isSidechain": false,
  "requestId": "req_011Cb4tFDeLc46ksBuG3qqt2",
  "type": "assistant",
  "uuid": "6fc311f8-8eeb-462e-9df4-8448a0b8ec9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkiBSTcyyNXD4n5e22jN64",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4214,
      "cache_read_input_tokens": 26733,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 26733,
          "cache_creation_input_tokens": 4214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4214
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

_source line 26_

```json
{
  "type": "last-prompt",
  "leafUuid": "6fc311f8-8eeb-462e-9df4-8448a0b8ec9c",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Write paper abstract for schema-DAG extraction study",
  "sessionId": "38df3856-e893-4a84-8aa9-007fca6d282d"
}
```

---
