# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性与完整性） **论文：** "Does Type Confusability Drive Schema-Induced Degradation 

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 74
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/9c06470a-a258-40d7-9ddb-7fd9ea965abe.jsonl`
- **Structured JSON:** [`5d5504097196b1569e39.json`](../../sessions/5d/5d5504097196b1569e39.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T00:53:47.691Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T00:53:47.691Z",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）\n\n**论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**Venue：** EMNLP 2026 Main Conference（ARR May 25 cycle）\n**格式要求：** 长文 8 页 + 无限参考文献，ACL 模板，double-blind，mandatory Limitations section，Responsible NLP Research Checklist\n**论文路径：** `projects/schema-dag-extraction/docs/paper/main.tex`（各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex；Limitations 在 main.tex 内）\n\n### 你的审查侧重\n\n**1. 新颖性与贡献**\n- \"首个隔离 type confusability 的控制实验\" 这一 novelty claim 是否成立？是否有遗漏的相关工作？\n- 四个贡献是否 substantive？哪些是增量性的？\n- Multi-channel degradation model 是经验观察还是有理论基础？\n- 负面结果（SDGD）作为贡献的价值？\n\n**2. 相关工作覆盖**\n- LLM-PEE 的对比定位是否充分？\n- 是否遗漏重要相关工作？特别关注：schema decomposition, prompt optimization for IE, LLM calibration\n- Representation degeneration 文献与 centrality confound 的联系是否自然？\n\n**3. 论文结构与写作质量**\n- 注意：当前论文没有 Discussion section（discussion.tex 实际包含的是 Conclusion，仅 1 段）。这是否符合 EMNLP 投稿标准？\n- Limitations section 的覆盖是否充分？\n- Abstract 是否准确概括了论文的主要发现？\n- 各 section 之间的逻辑流是否顺畅？\n\n**4. 格式合规性**\n- Double-blind 匿名性检查（author 字段、self-citation）\n- 是否满足 8 页限制？（请估算各 section 的页面占用）\n- 所有 figures 都在 Appendix——是否应将关键 figures 放入正文？\n- 参考文献格式是否正确？是否有可疑引用？\n- 是否缺少 Ethics Statement 或 Responsible NLP Research Checklist？\n\n**5. 遗漏的参考文献**\n- 检查是否遗漏了应当引用的重要工作\n\n请按以下格式输出审稿报告：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor])\n- Questions (需要作者澄清的)\n- Missing References (如有)\n- Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 简要理由)"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T00:53:47.694Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T00:53:47.694Z",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

## Round 1

72 recorded events

### User

_source line 3 · 2026-05-16T00:53:47.732Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）

**论文：** "Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?"
**Venue：** EMNLP 2026 Main Conference（ARR May 25 cycle）
**格式要求：** 长文 8 页 + 无限参考文献，ACL 模板，double-blind，mandatory Limitations section，Responsible NLP Research Checklist
**论文路径：** `projects/schema-dag-extraction/docs/paper/main.tex`（各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex；Limitations 在 main.tex 内）

### 你的审查侧重

**1. 新颖性与贡献**
- "首个隔离 type confusability 的控制实验" 这一 novelty claim 是否成立？是否有遗漏的相关工作？
- 四个贡献是否 substantive？哪些是增量性的？
- Multi-channel degradation model 是经验观察还是有理论基础？
- 负面结果（SDGD）作为贡献的价值？

**2. 相关工作覆盖**
- LLM-PEE 的对比定位是否充分？
- 是否遗漏重要相关工作？特别关注：schema decomposition, prompt optimization for IE, LLM calibration
- Representation degeneration 文献与 centrality confound 的联系是否自然？

**3. 论文结构与写作质量**
- 注意：当前论文没有 Discussion section（discussion.tex 实际包含的是 Conclusion，仅 1 段）。这是否符合 EMNLP 投稿标准？
- Limitations section 的覆盖是否充分？
- Abstract 是否准确概括了论文的主要发现？
- 各 section 之间的逻辑流是否顺畅？

**4. 格式合规性**
- Double-blind 匿名性检查（author 字段、self-citation）
- 是否满足 8 页限制？（请估算各 section 的页面占用）
- 所有 figures 都在 Appendix——是否应将关键 figures 放入正文？
- 参考文献格式是否正确？是否有可疑引用？
- 是否缺少 Ethics Statement 或 Responsible NLP Research Checklist？

**5. 遗漏的参考文献**
- 检查是否遗漏了应当引用的重要工作

请按以下格式输出审稿报告：
- Summary (2-3 句)
- Strengths (逐条)
- Weaknesses (逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor])
- Questions (需要作者澄清的)
- Missing References (如有)
- Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 简要理由)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "c8b47705-28dd-45f5-a311-61dc2ccca93f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T00:53:47.731Z_

```json
{
  "parentUuid": "c8b47705-28dd-45f5-a311-61dc2ccca93f",
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "201a4b17-73c5-445d-85dd-374eaafef702",
  "timestamp": "2026-05-16T00:53:47.731Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T00:53:47.731Z_

```json
{
  "parentUuid": "201a4b17-73c5-445d-85dd-374eaafef702",
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
  "uuid": "286e0c5f-1da7-4997-a8f6-5b3d43ba67a7",
  "timestamp": "2026-05-16T00:53:47.731Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T00:53:47.731Z_

```json
{
  "parentUuid": "286e0c5f-1da7-4997-a8f6-5b3d43ba67a7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8112cab3-e8cb-42c4-9645-d41cf4e4737f",
  "timestamp": "2026-05-16T00:53:47.731Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
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
  "aiTitle": "Review Round 1 for EMNLP schema extraction paper",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Assistant

_source line 8 · 2026-05-16T00:53:51.421Z_

我开始执行 Round 1 审稿任务。首先加载 review-reviewer-session-start skill，然后搜索 EMNLP 2026 / ACL ARR reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8112cab3-e8cb-42c4-9645-d41cf4e4737f",
  "isSidechain": false,
  "requestId": "req_011Cb5LMhhzWDnLDwFBCSQQE",
  "type": "assistant",
  "uuid": "ac80f380-e517-4107-b77c-059d4aebfe44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcpPn8qSAAVHUcdT35N2cd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13861,
      "cache_read_input_tokens": 11841,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 150,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13861
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

_source line 9 · 2026-05-16T00:53:51.790Z_

<details open><summary>🔧 Tool call — Read · `toolu_016MTZcEHTrSdmWPRHTWxJ5b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac80f380-e517-4107-b77c-059d4aebfe44",
  "isSidechain": false,
  "requestId": "req_011Cb5LMhhzWDnLDwFBCSQQE",
  "type": "assistant",
  "uuid": "fc3362dd-0ebb-454f-9b97-88233e0b77c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcpPn8qSAAVHUcdT35N2cd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13861,
      "cache_read_input_tokens": 11841,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 150,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13861
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

_source line 10 · 2026-05-16T00:53:51.808Z_

<details><summary>↩ Tool result · reported error · `toolu_016MTZcEHTrSdmWPRHTWxJ5b`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc3362dd-0ebb-454f-9b97-88233e0b77c8",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "c96a77d9-7d20-4ab8-a7cd-3973b923fffa",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9.",
  "sourceToolAssistantUUID": "fc3362dd-0ebb-454f-9b97-88233e0b77c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T00:53:54.532Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0126i2FVYWGSfNrigt9K4sFn`</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c96a77d9-7d20-4ab8-a7cd-3973b923fffa",
  "isSidechain": false,
  "requestId": "req_011Cb5LN12nYvjvZmudLrqNR",
  "type": "assistant",
  "uuid": "4102d5ce-b5fc-4432-9834-393274fab012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017knZbrWdSATA5ob5uEhWmr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 25702,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 25702,
          "cache_creation_input_tokens": 227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 227
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

_source line 12 · 2026-05-16T00:53:54.552Z_

<details><summary>↩ Tool result · `toolu_0126i2FVYWGSfNrigt9K4sFn`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4102d5ce-b5fc-4432-9834-393274fab012",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "c1922128-93fa-4ed2-9935-bed9da74a590",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 15,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "4102d5ce-b5fc-4432-9834-393274fab012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T00:53:57.154Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PRbZKGdfkrSaFhVoW3BmqC`</summary>

```json
{
  "pattern": "**/skills/**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1922128-93fa-4ed2-9935-bed9da74a590",
  "isSidechain": false,
  "requestId": "req_011Cb5LNCydLzpaiPwPXiPp1",
  "type": "assistant",
  "uuid": "bba95b8b-1aaa-436d-8321-5eb834d5e9f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wpYmpZDV5K6XjRrsBuT2H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 111,
      "cache_read_input_tokens": 25929,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 25929,
          "cache_creation_input_tokens": 111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 111
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

_source line 14 · 2026-05-16T00:53:57.167Z_

<details><summary>↩ Tool result · `toolu_01PRbZKGdfkrSaFhVoW3BmqC`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bba95b8b-1aaa-436d-8321-5eb834d5e9f1",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "0e5ea798-6293-4cc0-bc6d-770e736cf8ee",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 10,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "bba95b8b-1aaa-436d-8321-5eb834d5e9f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T00:54:00.708Z_

<details><summary>Logged reasoning block</summary>

```text
The skill files don't exist locally. Let me proceed with the review task directly. I need to:

1. Search for EMNLP 2026 / ACL ARR reviewer guidelines
2. Read the paper (main.tex and all section files)
3. Conduct the review

Let me start by reading the paper and searching for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e5ea798-6293-4cc0-bc6d-770e736cf8ee",
  "isSidechain": false,
  "requestId": "req_011Cb5LNQ8M57VxGtoYVgFQD",
  "type": "assistant",
  "uuid": "82241618-40fa-42aa-8542-4c05437d318a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9hSfHmQhyH4FEwznb8xZq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 108,
      "cache_read_input_tokens": 26040,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 26040,
          "cache_creation_input_tokens": 108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 108
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

_source line 16 · 2026-05-16T00:54:01.931Z_

Skill 文件不存在，直接进入审稿流程。先并行读论文各章节和搜索 reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82241618-40fa-42aa-8542-4c05437d318a",
  "isSidechain": false,
  "requestId": "req_011Cb5LNQ8M57VxGtoYVgFQD",
  "type": "assistant",
  "uuid": "eb70e7f8-87fd-419b-b459-4d6b26eb8a58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9hSfHmQhyH4FEwznb8xZq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 108,
      "cache_read_input_tokens": 26040,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 26040,
          "cache_creation_input_tokens": 108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 108
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

_source line 17 · 2026-05-16T00:54:02.704Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FoYPANKpdgjEv7Wav8QJYq`</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb70e7f8-87fd-419b-b459-4d6b26eb8a58",
  "isSidechain": false,
  "requestId": "req_011Cb5LNQ8M57VxGtoYVgFQD",
  "type": "assistant",
  "uuid": "83513975-db93-4f2b-831e-4d85b0711382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9hSfHmQhyH4FEwznb8xZq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 108,
      "cache_read_input_tokens": 26040,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 26040,
          "cache_creation_input_tokens": 108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 108
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

_source line 18 · 2026-05-16T00:54:02.708Z_

<details><summary>↩ Tool result · `toolu_01FoYPANKpdgjEv7Wav8QJYq`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__review_reviewer_post_to_director"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__verify_references"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83513975-db93-4f2b-831e-4d85b0711382",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "fb69188d-b3cf-407b-974c-875dda22839a",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "83513975-db93-4f2b-831e-4d85b0711382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T00:54:04.964Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper files and search for reviewer guidelines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb69188d-b3cf-407b-974c-875dda22839a",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "c1d593e0-7a73-41e7-a0b9-703b34e6e1ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 20 · 2026-05-16T00:54:06.095Z_

开始并行读取论文各章节、搜索 reviewer guidelines、验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1d593e0-7a73-41e7-a0b9-703b34e6e1ac",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "e5de92ad-f9e6-4e2e-895c-a3ecc633fe58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 21 · 2026-05-16T00:54:06.741Z_

<details open><summary>🔧 Tool call — Read · `toolu_017B3yDGK6Gb1vSaJWoGw6gx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5de92ad-f9e6-4e2e-895c-a3ecc633fe58",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "1a4d5442-c405-44bb-85e4-5dabf8266202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 22 · 2026-05-16T00:54:06.755Z_

<details><summary>↩ Tool result · `toolu_017B3yDGK6Gb1vSaJWoGw6gx`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	
15	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	
26	\input{related_work}
27	
28	\input{experimental_setup}
29	
30	\input{results}
31	
32	\input{sdgd_negative}
33	
34	\input{discussion}
35	
36	\section*{Limitations}
37	The primary experiments use Qwen3-32B. Channel~1 (count effect) has been validated on Meta-Llama-3.1-8B-Instruct (recall decline $-$43\,pp, per-batch $r = 0.725$ with Qwen3-32B). Channel~2 was validated cross-model on FewRel RE: Llama-3.1-8B-Instruct shows $\Delta = -27.1$\,pp at count 8 and $-23.9$\,pp at count 16, comparable to Qwen3-32B's $-31.2$\,pp. High-BCS accuracy is model-invariant ($\approx$0.51), with cross-model divergence confined to the low-BCS regime. On Few-NERD NER, the effect was not robustly detectable, likely due to floor effects at 8B scale and the noisier text-match metric. The pairwise confusability signal explains roughly 1.3--1.7\% of the variance in type confusion---entity frequency, prompt position effects, and type definition quality likely contribute to the remaining variance. Our decomposition experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored. We conducted a within-dataset $2\!\times\!2$ factorial analysis (count $\times$ BCS) on Few-NERD; the interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), possibly due to BCS range compression in high-count schemas. The primary evidence for count--confusability interaction remains the $3.4\times$ amplification observed across FewRel schema scales (\S\ref{sec:bcs_controlled}). An intermediate evaluation at 40-relation subsets sampled from the 80-relation pool (accuracy 0.588, BCS $\Delta = -33.3$\,pp at count 8) confirms monotonic decline, but this is not an independent schema---all 40-relation subsets draw from the same 80-type pool, so the 16-to-80 amplification ($3.4\times$) remains a two-point comparison. The $3.4\times$ amplification is a point estimate; propagating the 80-rel CI ([17.7, 42.7]\,pp) against the 9.1\,pp baseline yields a range of $1.9\text{--}4.7\times$. SCS/BCS relies on embedding cosine similarity; alternative metrics such as label entropy or ontological depth may capture complementary dimensions of schema difficulty.
38	
39	\bibliography{references}
40	
41	\appendix
42	
43	\section{Additional Figures}
44	\label{sec:appendix_figures}
45	
46	\begin{table}[h]
47	\centering
48	\small
49	\begin{tabular}{lrr}
50	\toprule
51	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
52	\midrule
53	1 & 0.702 & 0.640 \\
54	64 & 0.273 & 0.304 \\
55	\midrule
56	Decline & $-$43\,pp & $-$34\,pp \\
57	\bottomrule
58	\end{tabular}
59	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
60	\label{tab:cross_model}
61	\end{table}
62	
63	\begin{table}[h]
64	\centering
65	\small
66	\resizebox{\columnwidth}{!}{%
67	\begin{tabular}{crrrrrr}
68	\toprule
69	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
70	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
71	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
72	\midrule
73	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
74	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
75	\bottomrule
76	\end{tabular}}
77	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
78	\label{tab:cross_model_bcs}
79	\end{table}
80	
81	\begin{figure}[h]
82	\centering
83	\includegraphics[width=\columnwidth]{../../figures/paper/fig_count_curves.pdf}
84	\caption{Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases, reflecting same-domain disambiguation benefits (\S\ref{sec:centrality_confound}).}
85	\label{fig:count_curves}
86	\end{figure}
87	
88	\begin{figure}[h]
89	\centering
90	\includegraphics[width=\columnwidth]{../../figures/paper/fig_bcs_scaling.pdf}
91	\caption{BCS-controlled FewRel accuracy. The confusability gap between low-BCS and high-BCS batches widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations ($3.4\times$ amplification).}
92	\label{fig:bcs_scaling}
93	\end{figure}
94	
95	\begin{figure}[h]
96	\centering
97	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
98	\caption{Error taxonomy decomposition. IntraSub (intra-batch substitution) scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic, revealing task-dependent error mechanisms.}
99	\label{fig:error_taxonomy}
100	\end{figure}
101	
102	\end{document}
103	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a4d5442-c405-44bb-85e4-5dabf8266202",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "a768ba3a-1b37-438f-bad8-c60bbd21e9b3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\n\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\nThe primary experiments use Qwen3-32B. Channel~1 (count effect) has been validated on Meta-Llama-3.1-8B-Instruct (recall decline $-$43\\,pp, per-batch $r = 0.725$ with Qwen3-32B). Channel~2 was validated cross-model on FewRel RE: Llama-3.1-8B-Instruct shows $\\Delta = -27.1$\\,pp at count 8 and $-23.9$\\,pp at count 16, comparable to Qwen3-32B's $-31.2$\\,pp. High-BCS accuracy is model-invariant ($\\approx$0.51), with cross-model divergence confined to the low-BCS regime. On Few-NERD NER, the effect was not robustly detectable, likely due to floor effects at 8B scale and the noisier text-match metric. The pairwise confusability signal explains roughly 1.3--1.7\\% of the variance in type confusion---entity frequency, prompt position effects, and type definition quality likely contribute to the remaining variance. Our decomposition experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored. We conducted a within-dataset $2\\!\\times\\!2$ factorial analysis (count $\\times$ BCS) on Few-NERD; the interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), possibly due to BCS range compression in high-count schemas. The primary evidence for count--confusability interaction remains the $3.4\\times$ amplification observed across FewRel schema scales (\\S\\ref{sec:bcs_controlled}). An intermediate evaluation at 40-relation subsets sampled from the 80-relation pool (accuracy 0.588, BCS $\\Delta = -33.3$\\,pp at count 8) confirms monotonic decline, but this is not an independent schema---all 40-relation subsets draw from the same 80-type pool, so the 16-to-80 amplification ($3.4\\times$) remains a two-point comparison. The $3.4\\times$ amplification is a point estimate; propagating the 80-rel CI ([17.7, 42.7]\\,pp) against the 9.1\\,pp baseline yields a range of $1.9\\text{--}4.7\\times$. SCS/BCS relies on embedding cosine similarity; alternative metrics such as label entropy or ontological depth may capture complementary dimensions of schema difficulty.\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_count_curves.pdf}\n\\caption{Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases, reflecting same-domain disambiguation benefits (\\S\\ref{sec:centrality_confound}).}\n\\label{fig:count_curves}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\caption{BCS-controlled FewRel accuracy. The confusability gap between low-BCS and high-BCS batches widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations ($3.4\\times$ amplification).}\n\\label{fig:bcs_scaling}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub (intra-batch substitution) scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic, revealing task-dependent error mechanisms.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\n\\end{document}\n",
      "numLines": 103,
      "startLine": 1,
      "totalLines": 103
    }
  },
  "sourceToolAssistantUUID": "1a4d5442-c405-44bb-85e4-5dabf8266202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T00:54:07.238Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fo6dD3qVLnCkScwTmeYLZB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a768ba3a-1b37-438f-bad8-c60bbd21e9b3",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "e9e4bc79-ff19-4e2f-9f49-1b1c2e68d310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 24 · 2026-05-16T00:54:07.244Z_

<details><summary>↩ Tool result · `toolu_01Fo6dD3qVLnCkScwTmeYLZB`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE but interacting in NER. Confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural bottleneck for decompose-then-merge pipelines in zero-shot IE.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9e4bc79-ff19-4e2f-9f49-1b1c2e68d310",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "74727d02-f8da-45e1-b2cc-daed5b60399e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE but interacting in NER. Confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural bottleneck for decompose-then-merge pipelines in zero-shot IE.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  },
  "sourceToolAssistantUUID": "e9e4bc79-ff19-4e2f-9f49-1b1c2e68d310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T00:54:07.727Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QLLjhRdksijyTFvyYnJg1P`</summary>

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
  "parentUuid": "74727d02-f8da-45e1-b2cc-daed5b60399e",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "ff7f67dc-63c0-4824-a555-d0d083f7e27e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 26 · 2026-05-16T00:54:07.733Z_

<details><summary>↩ Tool result · `toolu_01QLLjhRdksijyTFvyYnJg1P`</summary>

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
12	Our experiments yield five findings: (1)~schema-induced degradation operates through two channels---count-driven recall decline (up to $-$30\,pp) and confusability-driven type confusion---that are separable in RE but interact in NER; (2)~pairwise SCS predicts type confusion across tasks ($r = 0.112$--$0.129$), modest in magnitude but the first factor empirically isolated in controlled zero-shot IE; (3)~confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types; (4)~per-type confusability aggregation is confounded by centrality on homogeneous schemas; and (5)~confusability-aware decomposition fails due to merge amplification (best F1 = 0.32 vs.\ single-pass 0.45), a structural bottleneck for decompose-then-merge pipelines.
13	
14	Our contributions are:
15	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
16	    \item \textbf{Multi-channel degradation model.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, revealing task-dependent interactions between channels.
17	    \item \textbf{Pairwise confusability as a robust predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.
18	    \item \textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types.
19	    \item \textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural bottleneck for decompose-then-merge approaches, with direct implications for the design of schema decomposition methods.
20	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff7f67dc-63c0-4824-a555-d0d083f7e27e",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "d22a37a2-7d35-44e1-8ad8-30852bf983c3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \\citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \\citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \\citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \\emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \\cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nTo answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \\emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \\emph{count curves} that vary schema size while randomizing confusability, and \\emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on three datasets spanning diverse schema structures: Few-NERD \\cite{fewnerd-2021} (66 entity types across 8 domains), FewRel \\cite{fewrel-2018} (80 relation types), and MAVEN \\cite{maven-2020} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.\n\nOur experiments yield five findings: (1)~schema-induced degradation operates through two channels---count-driven recall decline (up to $-$30\\,pp) and confusability-driven type confusion---that are separable in RE but interact in NER; (2)~pairwise SCS predicts type confusion across tasks ($r = 0.112$--$0.129$), modest in magnitude but the first factor empirically isolated in controlled zero-shot IE; (3)~confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types; (4)~per-type confusability aggregation is confounded by centrality on homogeneous schemas; and (5)~confusability-aware decomposition fails due to merge amplification (best F1 = 0.32 vs.\\ single-pass 0.45), a structural bottleneck for decompose-then-merge pipelines.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Multi-channel degradation model.} We provide the first empirical decomposition of schema-induced degradation into count and confusability channels across NER, RE, and ED, revealing task-dependent interactions between channels.\n    \\item \\textbf{Pairwise confusability as a robust predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on three datasets, establishing that confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types.\n    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural bottleneck for decompose-then-merge approaches, with direct implications for the design of schema decomposition methods.\n\\end{enumerate}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "ff7f67dc-63c0-4824-a555-d0d083f7e27e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T00:54:08.102Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QtfMiGcvidRciMsjDBJB4M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d22a37a2-7d35-44e1-8ad8-30852bf983c3",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "4f804df3-8943-4418-9ff7-6d3d6e2bebca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 28 · 2026-05-16T00:54:08.107Z_

<details><summary>↩ Tool result · `toolu_01QtfMiGcvidRciMsjDBJB4M`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Recent surveys categorize LLM-based IE along instruction-tuning and code-generation axes \cite{llm4ie-survey-2024}. Approaches span instruction tuning for unified IE \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided zero-shot extraction \cite{gollie-2024,adelie-2024}, and schema-driven decoding \cite{slot-2025,oneke-2025}. For NER, methods include zero-shot decomposition by entity type \cite{xie-zeroshot-ner-2023,promptner-2023}, ChatGPT distillation \cite{uniner-2024}, bidirectional transformers \cite{gliner-2024,gliner2-2025}, self-improvement \cite{self-improve-ner-2024}, type descriptions \cite{zeroner-2025}, and guided synthesis \cite{guidex-2025,nuner-2024}. Relation extraction benefits from self-prompting \cite{self-prompting-re-2024} and retrieval-augmented code generation \cite{code4uie-2024}. \citet{familiarity-2025} highlight evaluation pitfalls by quantifying label shifts in zero-shot NER. Separately, constrained decoding via JSON schema enforcement \cite{json-schema-bench-2025} guarantees structurally valid outputs; all our experiments use vLLM's constrained JSON decoding (\S\ref{sec:model}).
8	
9	These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. Our work fills both gaps.
10	
11	\subsection{Schema Complexity in IE}
12	\label{sec:rw_schema}
13	
14	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\S\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confusability Scores, directly targeting the Channel~2 degradation mechanism. Our SDGD experiments (\S\ref{sec:sdgd}) further reveal that the merge step---not partitioning quality---is the bottleneck in decompose-then-merge pipelines, a limitation that applies to LLM-PEE's approach as well.
15	
16	Other approaches address schema complexity from different angles: hard negative mining during training \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, event schema decomposition \cite{dee-2024}, multi-agent debate for cross-type IE \cite{crossagentie-2025,cmas-ner-2025}, schema-as-tool parameterization \cite{spt-2025}, on-device schema-aware IE \cite{dlisc-2025}, and schema-constrained knowledge graph generation \cite{kggen-2025}. All treat schema complexity as an engineering problem; we instead treat it as a scientific question about the independent mechanisms by which schema properties degrade extraction.
17	
18	\subsection{Representation Degeneration and Embedding Anisotropy}
19	\label{sec:rw_anisotropy}
20	
21	Our centrality confound analysis (\S\ref{sec:centrality_confound}) connects to the representation degeneration literature. \citet{gao-repr-degen-2019} showed that word embeddings degenerate into narrow cones, and \citet{ethayarajh-contextual-2019} extended this to contextual representations. Crucially, \citet{cai-isotropy-clusters-2021} showed that while the global space is anisotropic, local clusters can be isotropic---directly explaining our MAVEN results where single-ontology types form one dense cluster conflating confusability with centrality. \citet{godey-anisotropy-inherent-2024} proved anisotropy is inherent to self-attention, suggesting the centrality confound persists across architectures. Our work provides the first empirical demonstration that this anisotropy creates a measurable confound in IE schema analysis.
22	
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f804df3-8943-4418-9ff7-6d3d6e2bebca",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "794a1e61-5b0f-4486-aab0-e2c24115a0e7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Training-Free LLM Information Extraction}\n\\label{sec:rw_training_free}\n\nRecent surveys categorize LLM-based IE along instruction-tuning and code-generation axes \\cite{llm4ie-survey-2024}. Approaches span instruction tuning for unified IE \\cite{instructuie-2023}, code-style schema encoding \\cite{knowcoder-2024,codeie-2023}, annotation-guided zero-shot extraction \\cite{gollie-2024,adelie-2024}, and schema-driven decoding \\cite{slot-2025,oneke-2025}. For NER, methods include zero-shot decomposition by entity type \\cite{xie-zeroshot-ner-2023,promptner-2023}, ChatGPT distillation \\cite{uniner-2024}, bidirectional transformers \\cite{gliner-2024,gliner2-2025}, self-improvement \\cite{self-improve-ner-2024}, type descriptions \\cite{zeroner-2025}, and guided synthesis \\cite{guidex-2025,nuner-2024}. Relation extraction benefits from self-prompting \\cite{self-prompting-re-2024} and retrieval-augmented code generation \\cite{code4uie-2024}. \\citet{familiarity-2025} highlight evaluation pitfalls by quantifying label shifts in zero-shot NER. Separately, constrained decoding via JSON schema enforcement \\cite{json-schema-bench-2025} guarantees structurally valid outputs; all our experiments use vLLM's constrained JSON decoding (\\S\\ref{sec:model}).\n\nThese methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. Our work fills both gaps.\n\n\\subsection{Schema Complexity in IE}\n\\label{sec:rw_schema}\n\nThe most directly related work is LLM-PEE \\cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \\emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confusability Scores, directly targeting the Channel~2 degradation mechanism. Our SDGD experiments (\\S\\ref{sec:sdgd}) further reveal that the merge step---not partitioning quality---is the bottleneck in decompose-then-merge pipelines, a limitation that applies to LLM-PEE's approach as well.\n\nOther approaches address schema complexity from different angles: hard negative mining during training \\cite{iepile-2024}, schema definition optimization \\cite{parse-2025}, event schema decomposition \\cite{dee-2024}, multi-agent debate for cross-type IE \\cite{crossagentie-2025,cmas-ner-2025}, schema-as-tool parameterization \\cite{spt-2025}, on-device schema-aware IE \\cite{dlisc-2025}, and schema-constrained knowledge graph generation \\cite{kggen-2025}. All treat schema complexity as an engineering problem; we instead treat it as a scientific question about the independent mechanisms by which schema properties degrade extraction.\n\n\\subsection{Representation Degeneration and Embedding Anisotropy}\n\\label{sec:rw_anisotropy}\n\nOur centrality confound analysis (\\S\\ref{sec:centrality_confound}) connects to the representation degeneration literature. \\citet{gao-repr-degen-2019} showed that word embeddings degenerate into narrow cones, and \\citet{ethayarajh-contextual-2019} extended this to contextual representations. Crucially, \\citet{cai-isotropy-clusters-2021} showed that while the global space is anisotropic, local clusters can be isotropic---directly explaining our MAVEN results where single-ontology types form one dense cluster conflating confusability with centrality. \\citet{godey-anisotropy-inherent-2024} proved anisotropy is inherent to self-attention, suggesting the centrality confound persists across architectures. Our work provides the first empirical demonstration that this anisotropy creates a measurable confound in IE schema analysis.\n\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "4f804df3-8943-4418-9ff7-6d3d6e2bebca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T00:54:08.544Z_

<details open><summary>🔧 Tool call — Read · `toolu_018Fk5jZj6iHYk6CbuggMv6c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "794a1e61-5b0f-4486-aab0-e2c24115a0e7",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "a7f48920-a29f-4025-8216-512bcbc689ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 30 · 2026-05-16T00:54:08.549Z_

<details><summary>↩ Tool result · `toolu_018Fk5jZj6iHYk6CbuggMv6c`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
27	\midrule
28	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
29	FewRel & RE & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
30	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
31	\bottomrule
32	\end{tabular}}
33	\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}
34	\label{tab:datasets}
35	\end{table}
36	
37	\subsection{Schema Confusability Score (SCS)}
38	\label{sec:scs}
39	
40	We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
41	{\small
42	\[
43	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
44	\]
45	}
46	
47	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
48	\[
49	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
50	\]
51	
52	We compute SCS with two embedding models: (1)~Qwen3-32B \cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder. Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time.
53	
54	\subsection{Experimental Design}
55	\label{sec:exp_design}
56	
57	We conduct two complementary experimental paradigms.
58	
59	\paragraph{Experiment 1: Count Curves.}
60	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{1, 2, 6, 12, 22, 44, 64\} for Few-NERD, \{1, 4, 8, 16, 32, 64, 80\} for FewRel, and \{1, 6, 12, 22, 44, 64\} for MAVEN.
61	
62	\paragraph{Experiment 2: BCS-Controlled.}
63	We fix the type count and vary the Batch Confusability Score to isolate the effect of inter-type similarity from schema size. For each count level, we construct one low-BCS batch (types with the lowest pairwise similarities), one high-BCS batch (types with the highest pairwise similarities), and 25 random batches (27 total per count level). We run this paradigm on Few-NERD at count$\,\in\{6, 12\}$ and on FewRel at count$\,\in\{8, 16\}$, the latter evaluated on both a 16-relation pool and the full 80-relation pool. For MAVEN, we conduct analogous BCS-controlled experiments at count$\,\in\{6, 12\}$ with 27 batches per level; however, the same-domain nature of MAVEN's FrameNet-derived types introduces a centrality confound that complicates BCS interpretation. We report these results separately in \S\ref{sec:centrality_confound}.
64	
65	\subsection{Evaluation Metrics}
66	\label{sec:metrics}
67	
68	We use task-appropriate metrics that reflect the distinct nature of each extraction problem.
69	
70	\paragraph{NER (Few-NERD): Text-match F1.}
71	A predicted entity is a true positive if the predicted text string exactly matches (case-insensitive) a gold entity text \emph{and} the predicted type matches the gold type. This text-match evaluation operates at the entity level rather than the token level. We report Precision, Recall, and F1.
72	
73	\paragraph{RE (FewRel): Accuracy.}
74	Each sample has exactly one ground-truth relation. A prediction is correct if the predicted relation label exactly matches the gold label. We report Accuracy.
75	
76	\paragraph{ED (MAVEN): Relaxed F1.}
77	A predicted trigger is a true positive if (a)~any token overlap exists between the predicted trigger span and a gold trigger span, \emph{and} (b)~the predicted event type matches the gold event type. This relaxed matching is necessary because event triggers are inherently ambiguous in boundary (e.g., ``was killed'' vs.\ ``killed''). We report Relaxed F1.
78	
79	The choice of different metrics across tasks reflects their structural differences: NER is span-level extraction where precision--recall trade-offs are informative; RE is a classification task where accuracy directly measures correctness; ED combines trigger identification with type classification, requiring relaxed span matching to avoid penalizing legitimate boundary variation.
80	
81	\subsection{Model and Inference}
82	\label{sec:model}
83	
84	\paragraph{Primary model.}
85	We use Qwen3-32B-FP8 \cite{qwen3-2025}, selected for its strong instruction-following capability, native structured JSON output support, and the practical advantage that the FP8-quantized 32B model fits on a single NVIDIA RTX PRO 6000 Blackwell Server Edition (96\,GB). The model is served via vLLM (v0.20.2) \cite{vllm-2023} with \texttt{max\_model\_len=4096} and \texttt{gpu\_memory\_utilization=0.95}. We use two prompt versions across experiments. The v1 prompt (used for count-curve and BCS-controlled NER experiments) requests start/end character offsets alongside entity text; however, the model fabricates offsets in 96.5\% of predictions, so we evaluate exclusively via text matching (\S\ref{sec:metrics}), which is robust to offset errors. The v2 prompt (used for all subsequent experiments) drops the offset requirement and adds explicit output format constraints and role instructions, doubling precision with minimal recall loss. Both versions provide a JSON-formatted schema listing all type names for the current batch; the model outputs structured JSON containing extracted entities, relations, or events. We use greedy decoding (temperature${}\,=\,0$) and a fixed random seed (42) for all batch sampling and bootstrap resampling, ensuring full reproducibility.
86	
87	\paragraph{Cross-model validation.}
88	To test whether schema-induced degradation generalizes beyond the primary model, we replicate both experimental paradigms on Few-NERD and FewRel using Meta-Llama-3.1-8B-Instruct, a $4\times$ smaller model from a different model family. For NER we use text-match recall (Llama does not reliably produce span offsets); for RE we use accuracy.
89	
90	\paragraph{Statistical estimation.}
91	All key metrics are accompanied by 95\% bootstrap confidence intervals computed from 1{,}000 bootstrap resamples using the percentile method.
92	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7f48920-a29f-4025-8216-512bcbc689ce",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "dc68eb07-0c05-457b-a021-dc5cf43062d5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder. Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix the type count and vary the Batch Confusability Score to isolate the effect of inter-type similarity from schema size. For each count level, we construct one low-BCS batch (types with the lowest pairwise similarities), one high-BCS batch (types with the highest pairwise similarities), and 25 random batches (27 total per count level). We run this paradigm on Few-NERD at count$\\,\\in\\{6, 12\\}$ and on FewRel at count$\\,\\in\\{8, 16\\}$, the latter evaluated on both a 16-relation pool and the full 80-relation pool. For MAVEN, we conduct analogous BCS-controlled experiments at count$\\,\\in\\{6, 12\\}$ with 27 batches per level; however, the same-domain nature of MAVEN's FrameNet-derived types introduces a centrality confound that complicates BCS interpretation. We report these results separately in \\S\\ref{sec:centrality_confound}.\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\nWe use task-appropriate metrics that reflect the distinct nature of each extraction problem.\n\n\\paragraph{NER (Few-NERD): Text-match F1.}\nA predicted entity is a true positive if the predicted text string exactly matches (case-insensitive) a gold entity text \\emph{and} the predicted type matches the gold type. This text-match evaluation operates at the entity level rather than the token level. We report Precision, Recall, and F1.\n\n\\paragraph{RE (FewRel): Accuracy.}\nEach sample has exactly one ground-truth relation. A prediction is correct if the predicted relation label exactly matches the gold label. We report Accuracy.\n\n\\paragraph{ED (MAVEN): Relaxed F1.}\nA predicted trigger is a true positive if (a)~any token overlap exists between the predicted trigger span and a gold trigger span, \\emph{and} (b)~the predicted event type matches the gold event type. This relaxed matching is necessary because event triggers are inherently ambiguous in boundary (e.g., ``was killed'' vs.\\ ``killed''). We report Relaxed F1.\n\nThe choice of different metrics across tasks reflects their structural differences: NER is span-level extraction where precision--recall trade-offs are informative; RE is a classification task where accuracy directly measures correctness; ED combines trigger identification with type classification, requiring relaxed span matching to avoid penalizing legitimate boundary variation.\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\n\\paragraph{Primary model.}\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025}, selected for its strong instruction-following capability, native structured JSON output support, and the practical advantage that the FP8-quantized 32B model fits on a single NVIDIA RTX PRO 6000 Blackwell Server Edition (96\\,GB). The model is served via vLLM (v0.20.2) \\cite{vllm-2023} with \\texttt{max\\_model\\_len=4096} and \\texttt{gpu\\_memory\\_utilization=0.95}. We use two prompt versions across experiments. The v1 prompt (used for count-curve and BCS-controlled NER experiments) requests start/end character offsets alongside entity text; however, the model fabricates offsets in 96.5\\% of predictions, so we evaluate exclusively via text matching (\\S\\ref{sec:metrics}), which is robust to offset errors. The v2 prompt (used for all subsequent experiments) drops the offset requirement and adds explicit output format constraints and role instructions, doubling precision with minimal recall loss. Both versions provide a JSON-formatted schema listing all type names for the current batch; the model outputs structured JSON containing extracted entities, relations, or events. We use greedy decoding (temperature${}\\,=\\,0$) and a fixed random seed (42) for all batch sampling and bootstrap resampling, ensuring full reproducibility.\n\n\\paragraph{Cross-model validation.}\nTo test whether schema-induced degradation generalizes beyond the primary model, we replicate both experimental paradigms on Few-NERD and FewRel using Meta-Llama-3.1-8B-Instruct, a $4\\times$ smaller model from a different model family. For NER we use text-match recall (Llama does not reliably produce span offsets); for RE we use accuracy.\n\n\\paragraph{Statistical estimation.}\nAll key metrics are accompanied by 95\\% bootstrap confidence intervals computed from 1{,}000 bootstrap resamples using the percentile method.\n",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  },
  "sourceToolAssistantUUID": "a7f48920-a29f-4025-8216-512bcbc689ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T00:54:09.022Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CodHqxZxvAjSnJymsKGWdv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc68eb07-0c05-457b-a021-dc5cf43062d5",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "3b257139-d6d0-4fe8-abe9-374f57407ddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 32 · 2026-05-16T00:54:09.027Z_

<details><summary>↩ Tool result · `toolu_01CodHqxZxvAjSnJymsKGWdv`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; see Figure~\ref{fig:count_curves} in the Appendix for visualizations).
8	
9	\paragraph{NER (Few-NERD).}
10	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
11	
12	\paragraph{RE (FewRel).}
13	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)
14	
15	\paragraph{ED (MAVEN).}
16	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \S\ref{sec:centrality_confound}.
17	
18	\paragraph{Cross-model replication.}
19	Channel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\,pp recall decline (0.702 at count${}\,=\,1$ to 0.273 at count${}\,=\,64$), compared to $-$34\,pp for Qwen3-32B (Table~\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.
20	
21	\paragraph{Summary.}
22	Schema size degrades extraction quality for NER and RE (Channel~1: count $\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\S\ref{sec:bcs_controlled}).
23	
24	\subsection{Pairwise Confusability and Type Confusion}
25	\label{sec:pairwise}
26	
27	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
28	
29	\begin{table}[t]
30	\centering
31	\small
32	\resizebox{\columnwidth}{!}{%
33	\begin{tabular}{llrrrrr}
34	\toprule
35	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
36	\midrule
37	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\
38	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\
39	\bottomrule
40	\end{tabular}}
41	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}
42	\label{tab:pairwise}
43	\end{table}
44	
45	The correlations are modest: $r^2 \approx 1.3\text{--}1.7\%$, meaning pairwise confusability explains roughly 1.5\% of the variance in type confusion. Other factors---entity frequency, prompt position effects \cite{lost-in-middle-2024}, and type definition quality---likely contribute to the remaining variance. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix between all type pairs is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\S\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE. Nevertheless, the signal is robust: both correlations survive bootstrap resampling with CIs bounded well above zero, and replicate across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings).
46	
47	Spearman rank correlations from the SCS validation experiment (exp-015) corroborate these findings. Across all type pairs, Qwen3 yields $\rho = 0.168$ ($p = 7.3 \times 10^{-14}$) and MiniLM yields $\rho = 0.144$ ($p = 1.7 \times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\rho = 0.272$ ($p = 5 \times 10^{-5}$) for Qwen3 and $\rho = 0.306$ ($p = 4.6 \times 10^{-6}$) for MiniLM, indicating that among types the model actually confuses, embedding similarity is a stronger predictor.
48	
49	We frame these results as identifying one factor among several that drive type confusion, but the first to be empirically isolated in a controlled zero-shot IE setting. Although pairwise $r^2$ is modest, the signal concentrates among types the model actually confuses ($\rho = 0.27\text{--}0.31$) and compounds at the batch level into accuracy gaps reaching 31.2\,pp (\S\ref{sec:bcs_controlled}). Qwen3 yields stronger overall correlation ($\rho = 0.168$ vs.\ $0.144$), while MiniLM yields a stronger association among nonzero-confusion pairs ($\rho = 0.306$ vs.\ $0.272$); extraction-model embeddings are preferable when available.
50	
51	\subsection{BCS-Controlled Experiments}
52	\label{sec:bcs_controlled}
53	
54	To move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\resizebox{\columnwidth}{!}{%
60	\begin{tabular}{lcrrrr}
61	\toprule
62	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
63	\midrule
64	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
65	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
66	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
67	\bottomrule
68	\end{tabular}}
69	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
70	\label{tab:bcs_controlled}
71	\end{table}
72	
73	At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies this gap to 31.2\,pp (95\% CI: [17.7, 42.7])---a $3.4\times$ amplification ($31.2 / 9.1$; range $1.9\text{--}4.7\times$ given the 80-rel CI). The effect is stable across count levels: at count${}\,=\,16$, the gap remains 31.2\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\,=\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\,pp (count 8) and $-$31.8\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.
74	
75	This amplification has a natural interpretation. A larger type pool provides more opportunities for semantically similar types to co-occur, expanding the confusion space. BCS captures this expanded space: at 80 relations, extreme high-BCS batches pack tightly clustered types that the model cannot reliably distinguish, while the same count of well-separated types preserves near-solo-evaluation accuracy.
76	
77	\paragraph{Cross-model validation.}
78	The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\,pp at count${}\,=\,8$ (low-BCS 78.1\% vs.\ high-BCS 51.0\%) and $-$23.9\,pp at count${}\,=\,16$ (75.5\% vs.\ 51.6\%), reaching 77--87\% of Qwen3-32B's $-$31.2\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\approx$51\% under high confusability (count${}\,=\,8$: 51.0\% vs.\ 51.0\%; count${}\,=\,16$: 51.6\% vs.\ 51.6\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.
79	
80	\subsection{Multi-Channel Degradation}
81	\label{sec:multi_channel}
82	
83	We now decompose extraction errors into an error taxonomy to distinguish the mechanisms behind performance loss. Table~\ref{tab:error_taxonomy} quantifies how each error type scales with BCS.
84	
85	\begin{table}[t]
86	\centering
87	\small
88	\resizebox{\columnwidth}{!}{%
89	\begin{tabular}{llrrrrrrr}
90	\toprule
91	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
92	\cmidrule(lr){3-7}
93	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
94	\midrule
95	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
96	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}10^{-6}$ \\
97	\midrule
98	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
99	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
100	\bottomrule
101	\end{tabular}}
102	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic, revealing task-dependent error mechanisms.}
103	\label{tab:error_taxonomy}
104	\end{table}
105	
106	Three findings emerge. First, intra-batch substitution scales monotonically with BCS in both tasks: NER IntraSub rises from 0\% (solo) to 49.4\% (high BCS) with $\rho = 1.0$ ($p < 0.001$), and RE IntraSub rises from 0\% through 20.3\% (high) to 32.3\% (very high) with $\rho = 0.954$ ($p < 10^{-6}$). Second, 100\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt, never hallucinating types outside the schema. Third, the tasks diverge on missed-entity rates: RE rates remain flat across BCS bins (10.4--15.7\%), but NER rates are substantially higher (42.8--64.8\%) and non-monotonic. This suggests that in span-level extraction, confusable type sets impair entity detection itself, not only type discrimination.
107	
108	The extreme-batch analysis sharpens this picture. At count${}\,=\,6$, high-BCS batches produce $27.5\times$ more confusion than low-BCS batches under extreme selection, versus $1.7\times$ under random batching. At count${}\,=\,12$, the ratios are $9.9\times$ (extreme) versus $2.4\times$ (random). These multiplicative gaps confirm that BCS captures a functionally relevant dimension of schema difficulty, not merely a correlate.
109	
110	Taken together, these results establish two degradation channels: \textbf{Channel~1} (count $\to$ recall decline, \S\ref{sec:count_curves}) and \textbf{Channel~2} (confusability $\to$ type confusion, this section). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that the two channels interact for span-level extraction tasks where type ambiguity and boundary ambiguity are coupled.
111	
112	\subsection{Centrality Confound on Homogeneous Schemas}
113	\label{sec:centrality_confound}
114	
115	Per-type analysis on MAVEN reveals an anomaly: the correlation between mean BCS and per-type error rate is \emph{positive}---Qwen3 $\rho = +0.189$ ($p = 0.021$) and MiniLM $\rho = +0.208$ ($p = 0.011$)---opposite to the negative direction predicted by the confusability hypothesis.
116	
117	This reversal traces to a property of same-domain schemas documented by \citet{cai-isotropy-clusters-2021}: when all types derive from a single ontology (here, FrameNet), their embeddings collapse into a single cluster in representation space. In this regime, a type's mean BCS conflates two distinct properties: (i)~confusability with neighbors, which should increase errors, and (ii)~centrality within the cluster, which correlates with being a well-represented, high-frequency type that LLMs extract reliably. The centrality signal dominates, flipping the aggregate correlation.
118	
119	Critically, the pairwise SCS--confusion correlation remains intact: MAVEN MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10}$), consistent with the values in Table~\ref{tab:pairwise}. The problem lies in the aggregation step (mean BCS per type), not in the pairwise signal itself.
120	
121	Few-NERD, whose 66 types span 8 coarse categories across diverse domains, does not exhibit this confound. Its per-type correlation is $\rho = -0.293$ ($p = 0.02$, $n = 63$), in the expected negative direction: types with higher mean confusability have higher error rates. The cross-domain schema spans multiple embedding clusters, breaking the centrality--confusability conflation.
122	
123	This analysis carries a practical implication: mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas. For same-domain schemas where types form a single semantic cluster, pairwise SCS should be used directly, or the centrality component must be factored out before aggregation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b257139-d6d0-4fe8-abe9-374f57407ddd",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "2e01ad52-dc72-458c-b992-7fec95b24b76",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\nWe first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; see Figure~\\ref{fig:count_curves} in the Appendix for visualizations).\n\n\\paragraph{NER (Few-NERD).}\nRecall generally declines from 0.72 at count${}\\,=\\,1$ to 0.42 at count${}\\,=\\,64$, a 42\\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\\,=\\,22$ to 0.551 at count${}\\,=\\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.\n\n\\paragraph{RE (FewRel).}\nAccuracy drops monotonically from 85.7\\% at count${}\\,=\\,1$ through 58.8\\% at count${}\\,=\\,40$ to 50.4\\% at count${}\\,=\\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\\,=\\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)\n\n\\paragraph{ED (MAVEN).}\nIn contrast to NER and RE, MAVEN relaxed F1 \\emph{increases} from 0.106 at count${}\\,=\\,1$ to 0.247 at count${}\\,=\\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \\S\\ref{sec:centrality_confound}.\n\n\\paragraph{Cross-model replication.}\nChannel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\\,pp recall decline (0.702 at count${}\\,=\\,1$ to 0.273 at count${}\\,=\\,64$), compared to $-$34\\,pp for Qwen3-32B (Table~\\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.\n\n\\paragraph{Summary.}\nSchema size degrades extraction quality for NER and RE (Channel~1: count $\\to$ recall decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}10^{-12}$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are modest: $r^2 \\approx 1.3\\text{--}1.7\\%$, meaning pairwise confusability explains roughly 1.5\\% of the variance in type confusion. Other factors---entity frequency, prompt position effects \\cite{lost-in-middle-2024}, and type definition quality---likely contribute to the remaining variance. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix between all type pairs is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}) provide stronger, interventional evidence for the confusability effect on RE. Nevertheless, the signal is robust: both correlations survive bootstrap resampling with CIs bounded well above zero, and replicate across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings).\n\nSpearman rank correlations from the SCS validation experiment (exp-015) corroborate these findings. Across all type pairs, Qwen3 yields $\\rho = 0.168$ ($p = 7.3 \\times 10^{-14}$) and MiniLM yields $\\rho = 0.144$ ($p = 1.7 \\times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\\rho = 0.272$ ($p = 5 \\times 10^{-5}$) for Qwen3 and $\\rho = 0.306$ ($p = 4.6 \\times 10^{-6}$) for MiniLM, indicating that among types the model actually confuses, embedding similarity is a stronger predictor.\n\nWe frame these results as identifying one factor among several that drive type confusion, but the first to be empirically isolated in a controlled zero-shot IE setting. Although pairwise $r^2$ is modest, the signal concentrates among types the model actually confuses ($\\rho = 0.27\\text{--}0.31$) and compounds at the batch level into accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled}). Qwen3 yields stronger overall correlation ($\\rho = 0.168$ vs.\\ $0.144$), while MiniLM yields a stronger association among nonzero-confusion pairs ($\\rho = 0.306$ vs.\\ $0.272$); extraction-model embeddings are preferable when available.\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nTo move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\nAt the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies this gap to 31.2\\,pp (95\\% CI: [17.7, 42.7])---a $3.4\\times$ amplification ($31.2 / 9.1$; range $1.9\\text{--}4.7\\times$ given the 80-rel CI). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\\,=\\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\\,pp (count 8) and $-$31.8\\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.\n\nThis amplification has a natural interpretation. A larger type pool provides more opportunities for semantically similar types to co-occur, expanding the confusion space. BCS captures this expanded space: at 80 relations, extreme high-BCS batches pack tightly clustered types that the model cannot reliably distinguish, while the same count of well-separated types preserves near-solo-evaluation accuracy.\n\n\\paragraph{Cross-model validation.}\nThe confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\\,pp at count${}\\,=\\,8$ (low-BCS 78.1\\% vs.\\ high-BCS 51.0\\%) and $-$23.9\\,pp at count${}\\,=\\,16$ (75.5\\% vs.\\ 51.6\\%), reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp. Strikingly, high-BCS accuracy is model-invariant: both models converge to $\\approx$51\\% under high confusability (count${}\\,=\\,8$: 51.0\\% vs.\\ 51.0\\%; count${}\\,=\\,16$: 51.6\\% vs.\\ 51.6\\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This pattern indicates that confusable type sets create a task-inherent difficulty floor independent of model scale.\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\nWe now decompose extraction errors into an error taxonomy to distinguish the mechanisms behind performance loss. Table~\\ref{tab:error_taxonomy} quantifies how each error type scales with BCS.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}10^{-6}$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic, revealing task-dependent error mechanisms.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\nThree findings emerge. First, intra-batch substitution scales monotonically with BCS in both tasks: NER IntraSub rises from 0\\% (solo) to 49.4\\% (high BCS) with $\\rho = 1.0$ ($p < 0.001$), and RE IntraSub rises from 0\\% through 20.3\\% (high) to 32.3\\% (very high) with $\\rho = 0.954$ ($p < 10^{-6}$). Second, 100\\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt, never hallucinating types outside the schema. Third, the tasks diverge on missed-entity rates: RE rates remain flat across BCS bins (10.4--15.7\\%), but NER rates are substantially higher (42.8--64.8\\%) and non-monotonic. This suggests that in span-level extraction, confusable type sets impair entity detection itself, not only type discrimination.\n\nThe extreme-batch analysis sharpens this picture. At count${}\\,=\\,6$, high-BCS batches produce $27.5\\times$ more confusion than low-BCS batches under extreme selection, versus $1.7\\times$ under random batching. At count${}\\,=\\,12$, the ratios are $9.9\\times$ (extreme) versus $2.4\\times$ (random). These multiplicative gaps confirm that BCS captures a functionally relevant dimension of schema difficulty, not merely a correlate.\n\nTaken together, these results establish two degradation channels: \\textbf{Channel~1} (count $\\to$ recall decline, \\S\\ref{sec:count_curves}) and \\textbf{Channel~2} (confusability $\\to$ type confusion, this section). In RE, the channels are cleanly separable---confusability drives substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that the two channels interact for span-level extraction tasks where type ambiguity and boundary ambiguity are coupled.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomaly: the correlation between mean BCS and per-type error rate is \\emph{positive}---Qwen3 $\\rho = +0.189$ ($p = 0.021$) and MiniLM $\\rho = +0.208$ ($p = 0.011$)---opposite to the negative direction predicted by the confusability hypothesis.\n\nThis reversal traces to a property of same-domain schemas documented by \\citet{cai-isotropy-clusters-2021}: when all types derive from a single ontology (here, FrameNet), their embeddings collapse into a single cluster in representation space. In this regime, a type's mean BCS conflates two distinct properties: (i)~confusability with neighbors, which should increase errors, and (ii)~centrality within the cluster, which correlates with being a well-represented, high-frequency type that LLMs extract reliably. The centrality signal dominates, flipping the aggregate correlation.\n\nCritically, the pairwise SCS--confusion correlation remains intact: MAVEN MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10}$), consistent with the values in Table~\\ref{tab:pairwise}. The problem lies in the aggregation step (mean BCS per type), not in the pairwise signal itself.\n\nFew-NERD, whose 66 types span 8 coarse categories across diverse domains, does not exhibit this confound. Its per-type correlation is $\\rho = -0.293$ ($p = 0.02$, $n = 63$), in the expected negative direction: types with higher mean confusability have higher error rates. The cross-domain schema spans multiple embedding clusters, breaking the centrality--confusability conflation.\n\nThis analysis carries a practical implication: mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas. For same-domain schemas where types form a single semantic cluster, pairwise SCS should be used directly, or the centrality component must be factored out before aggregation.",
      "numLines": 123,
      "startLine": 1,
      "totalLines": 123
    }
  },
  "sourceToolAssistantUUID": "3b257139-d6d0-4fe8-abe9-374f57407ddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T00:54:09.494Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BjkMMimWdMqCWmLmxocYpZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e01ad52-dc72-458c-b992-7fec95b24b76",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "1cd76b5a-168f-4521-b330-358435acef21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 34 · 2026-05-16T00:54:09.498Z_

<details><summary>↩ Tool result · `toolu_01BjkMMimWdMqCWmLmxocYpZ`</summary>

```text
1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	The multi-channel degradation model (\S\ref{sec:results}) raises an interventional question: if confusability drives type confusion, can we decompose the schema so that confusable types never co-occur in the same prompt?  We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD), a method that uses the pairwise SCS matrix to partition types into low-confusability batches, runs extraction independently on each batch, and merges the results.
5	
6	\paragraph{Decomposition protocol.}
7	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation, following the strategy of \citet{uniner-2024}. Table~\ref{tab:sdgd_results} summarizes the results on Few-NERD.
8	
9	\paragraph{All decomposition modes degrade F1.}
10	Table~\ref{tab:sdgd_results} reports the outcome.  Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368).  SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop.  Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586).  Every decomposition mode falls below the single-pass baseline.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{lrccc}
17	\toprule
18	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
19	\midrule
20	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
21	\midrule
22	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
23	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
24	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
25	\midrule
26	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
27	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
28	\bottomrule
29	\end{tabular}}
30	\caption{Few-NERD extraction under decomposition modes.  V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero).  All decomposition modes produce lower F1 than the single-pass baseline.  More batches amplify false positives through merge.}
31	\label{tab:sdgd_results}
32	\end{table}
33	
34	\paragraph{Merge amplification.}
35	The pattern across modes is consistent: decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563).  The mechanism is straightforward.  When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions.  Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.  Smaller batches amplify the effect: per-type extraction runs the most passes and suffers the worst precision.  This \emph{merge amplification} is a structural consequence of decompose-then-merge pipelines, independent of how the decomposition is constructed.
36	
37	\paragraph{Confidence-gated merge does not help.}
38	A natural remedy is to resolve merge conflicts using model confidence.  Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span.  Confidence gating does improve precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), yielding lower F1 in both modes (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).  The failure is consistent with prior findings that LLM confidence scores are poorly calibrated in generative IE settings \cite{llm-calibration-survey-2024}: poorly calibrated scores discard correct predictions as aggressively as false positives.
39	
40	\paragraph{Connection to prior work and implications.}
41	\citet{llm-pee-2025} independently proposed similarity-based partitioning for event extraction. Our negative result complements their work by identifying the merge step---not partitioning quality---as the bottleneck. SDGD successfully separates confusable types by construction, yet F1 still drops because merge amplification is independent of decomposition quality. This is a general limitation of decompose-then-merge pipelines: future approaches must address cross-batch calibration before decomposition can translate confusability signals into extraction gains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cd76b5a-168f-4521-b330-358435acef21",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "e467bff0-e4ce-43d4-87f4-f67d4046c57e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
      "content": "\\section{Why Naive Decomposition Fails}\n\\label{sec:sdgd}\n\nThe multi-channel degradation model (\\S\\ref{sec:results}) raises an interventional question: if confusability drives type confusion, can we decompose the schema so that confusable types never co-occur in the same prompt?  We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD), a method that uses the pairwise SCS matrix to partition types into low-confusability batches, runs extraction independently on each batch, and merges the results.\n\n\\paragraph{Decomposition protocol.}\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation, following the strategy of \\citet{uniner-2024}. Table~\\ref{tab:sdgd_results} summarizes the results on Few-NERD.\n\n\\paragraph{All decomposition modes degrade F1.}\nTable~\\ref{tab:sdgd_results} reports the outcome.  Single-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368).  SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop.  Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586).  Every decomposition mode falls below the single-pass baseline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes.  V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero).  All decomposition modes produce lower F1 than the single-pass baseline.  More batches amplify false positives through merge.}\n\\label{tab:sdgd_results}\n\\end{table}\n\n\\paragraph{Merge amplification.}\nThe pattern across modes is consistent: decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563).  The mechanism is straightforward.  When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions.  Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.  Smaller batches amplify the effect: per-type extraction runs the most passes and suffers the worst precision.  This \\emph{merge amplification} is a structural consequence of decompose-then-merge pipelines, independent of how the decomposition is constructed.\n\n\\paragraph{Confidence-gated merge does not help.}\nA natural remedy is to resolve merge conflicts using model confidence.  Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span.  Confidence gating does improve precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).  The failure is consistent with prior findings that LLM confidence scores are poorly calibrated in generative IE settings \\cite{llm-calibration-survey-2024}: poorly calibrated scores discard correct predictions as aggressively as false positives.\n\n\\paragraph{Connection to prior work and implications.}\n\\citet{llm-pee-2025} independently proposed similarity-based partitioning for event extraction. Our negative result complements their work by identifying the merge step---not partitioning quality---as the bottleneck. SDGD successfully separates confusable types by construction, yet F1 still drops because merge amplification is independent of decomposition quality. This is a general limitation of decompose-then-merge pipelines: future approaches must address cross-batch calibration before decomposition can translate confusability signals into extraction gains.",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  },
  "sourceToolAssistantUUID": "1cd76b5a-168f-4521-b330-358435acef21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T00:54:10.428Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KBQnPxtGhPbSoga2S9KN9u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e467bff0-e4ce-43d4-87f4-f67d4046c57e",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "76f65a97-0886-4d57-827d-bb8d9bb81e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 36 · 2026-05-16T00:54:10.433Z_

<details><summary>↩ Tool result · `toolu_01KBQnPxtGhPbSoga2S9KN9u`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE but interact in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is the bottleneck for decompose-then-merge pipelines. Cross-batch calibration or joint decoding is the key next step.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76f65a97-0886-4d57-827d-bb8d9bb81e38",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "5c839ee6-6131-4be5-aa01-a520e6de54d6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE but interact in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\\Delta = -27$\\,pp), with high-BCS accuracy converging to a model-invariant floor. We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is the bottleneck for decompose-then-merge pipelines. Cross-batch calibration or joint decoding is the key next step.\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  },
  "sourceToolAssistantUUID": "76f65a97-0886-4d57-827d-bb8d9bb81e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T00:54:10.896Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015vwyLyyFyTTjhzYCBQqpds`</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c839ee6-6131-4be5-aa01-a520e6de54d6",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "16c24732-1a52-4c29-858d-afa6d29803ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 38 · 2026-05-16T00:54:11.417Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01F1ToGeckULYTevAHbMyora`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16c24732-1a52-4c29-858d-afa6d29803ec",
  "isSidechain": false,
  "requestId": "req_011Cb5LNogSSnbyU267jTKrA",
  "type": "assistant",
  "uuid": "b17e7c86-dd67-47dc-bcc6-d6eb8021df9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LivFmt1Qty5kLdhUptf933",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 26148,
      "output_tokens": 790,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 790,
          "cache_read_input_tokens": 26148,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2253
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）  **论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\" **Venue：** EMNLP 2026 Main Confer…",
  "leafUuid": "b17e7c86-dd67-47dc-bcc6-d6eb8021df9d",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for EMNLP schema extraction paper",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Tool result

_source line 41 · 2026-05-16T00:54:18.234Z_

<details><summary>↩ Tool result · `toolu_015vwyLyyFyTTjhzYCBQqpds`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I've successfully retrieved comprehensive information about ACL ARR 2025 2026 reviewer guidelines. Here are the key findings:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scoring Scale

The review form includes the following recommendation options:

- 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers).
- 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.
- 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.
- 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).

## Criteria for Outstanding Papers

Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.

## Review Guidelines Context

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference. Thus low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/more specialized venues.

The official reviewer guidelines are available at http://aclrollingreview.org/reviewerguidelines and the review form details at http://aclrollingreview.org/reviewform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16c24732-1a52-4c29-858d-afa6d29803ec",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "87a5d8a5-10d5-4623-beb4-52e636ccadbe",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GCAtFDKfMXWt8F976UKe9N",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "ACLRollingReview (@ReviewAcl) / X",
            "url": "https://x.com/reviewacl"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "aclrollingreview/reviewing.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"
          }
        ]
      },
      "I've successfully retrieved comprehensive information about ACL ARR 2025 2026 reviewer guidelines. Here are the key findings:\n\n## Review Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.\n\n## Overall Recommendation Scoring Scale\n\nThe review form includes the following recommendation options:\n\n- 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers).\n- 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.\n- 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.\n- 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).\n\n## Criteria for Outstanding Papers\n\nOutstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing.\n\n## Review Guidelines Context\n\nARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference. Thus low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/more specialized venues.\n\nThe official reviewer guidelines are available at http://aclrollingreview.org/reviewerguidelines and the review form details at http://aclrollingreview.org/reviewform."
    ],
    "durationSeconds": 7.3337225230000005
  },
  "sourceToolAssistantUUID": "16c24732-1a52-4c29-858d-afa6d29803ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T00:54:56.947Z_

<details><summary>↩ Tool result · `toolu_01F1ToGeckULYTevAHbMyora`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 42, \"total_citations\": 54, \"unique_cited_keys\": 42, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 32, \"online_not_found\": 5, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"article\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.08623\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"dlisc-2025\", \"type\": \"article\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\", \"authors\": \"Wen, Zhihao and Liang, Sheng and Wu, Yaxiong and Zhang, Yongyue and Liu, Yong\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.14992\"}, {\"key\": \"spt-2025\", \"type\": \"article\", \"title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"authors\": \"Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2506.01276\"}, {\"key\": \"zeroner-2025\", \"type\": \"inproceedings\", \"title\": \"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\", \"authors\": \"Cocchieri, Alessio and Mart\\\\'\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"cmas-ner-2025\", \"type\": \"inproceedings\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"authors\": \"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"uniner-2024\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gollie-2024\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and Garc\\\\'\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gliner-2024\", \"type\": \"inproceedings\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"authors\": \"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"gliner2-2025\", \"type\": \"inproceedings\", \"title\": \"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\", \"authors\": \"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"kggen-2025\", \"type\": \"inproceedings\", \"title\": \"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\", \"authors\": \"Mo, Belinda and Yu, Kyssen and Kazdan, Joshua and Cabezas, Joan and Mpala, Proud...\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"code4uie-2024\", \"type\": \"inproceedings\", \"title\": \"Retrieval-Augmented Code Generation for Universal Information Extraction\", \"authors\": \"Guo, Yucan and Li, Zixuan and Jin, Xiaolong and Liu, Yantao and Zeng, Yutao and ...\", \"year\": \"2024\", \"venue\": \"NeurIPS 2024 Workshop\"}, {\"key\": \"iepile-2024\", \"type\": \"inproceedings\", \"title\": \"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\", \"authors\": \"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lost-in-middle-2024\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\", \"year\": \"2024\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"self-improve-ner-2024\", \"type\": \"inproceedings\", \"title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"self-prompting-re-2024\", \"type\": \"inproceedings\", \"title\": \"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\", \"authors\": \"Liu, Siyi and Li, Yang and Li, Jiang and Yang, Shan and Lan, Yunshi\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2024\"}, {\"key\": \"nuner-2024\", \"type\": \"inproceedings\", \"title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"authors\": \"Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth\\\\'ee and Crabb\\\\'e,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"familiarity-2025\", \"type\": \"inproceedings\", \"title\": \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training D...\", \"authors\": \"Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Ni...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guidex-2025\", \"type\": \"inproceedings\", \"title\": \"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\", \"authors\": \"De La Fuente, Neil and Sainz, Oscar and Garc\\\\'\\\\ia-Ferrero, Iker and Agirre, Enek...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"llm4ie-survey-2024\", \"type\": \"article\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"authors\": \"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\", \"year\": \"2024\", \"venue\": \"Frontiers of Computer Science\"}, {\"key\": \"knowcoder-2024\", \"type\": \"inproceedings\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"authors\": \"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"slot-2025\", \"type\": \"inproceedings\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"authors\": \"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"gao-repr-degen-2019\", \"type\": \"inproceedings\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"authors\": \"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\", \"year\": \"2019\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"ethayarajh-contextual-2019\", \"type\": \"inproceedings\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"authors\": \"Ethayarajh, Kawin\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"type\": \"inproceedings\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"authors\": \"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"godey-anisotropy-inherent-2024\", \"type\": \"inproceedings\", \"title\": \"Anisotropy Is Inherent to Self-Attention in Transformers\", \"authors\": \"Godey, Nathan and de la Clergerie, \\\\'Eric and Sagot, Beno\\\\^\\\\it\", \"year\": \"2024\", \"venue\": \"Proceedings of the 18th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"instructuie-2023\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"codeie-2023\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"adelie-2024\", \"type\": \"inproceedings\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"authors\": \"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"oneke-2025\", \"type\": \"inproceedings\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"authors\": \"Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and...\", \"year\": \"2025\", \"venue\": \"Companion Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"llm-calibration-survey-2024\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"fewnerd-2021\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"fewrel-2018\", \"type\": \"inproceedings\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"authors\": \"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"maven-2020\", \"type\": \"inproceedings\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"authors\": \"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"qwen3-2025\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"minilm-2019\", \"type\": \"article\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"authors\": \"Reimers, Nils and Gurevych, Iryna\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"vllm-2023\", \"type\": \"inproceedings\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"authors\": \"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 29th Symposium on Operating Systems Principles\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"type\": \"inproceedings\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"promptner-2023\", \"type\": \"article\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"authors\": \"Ashok, Dhananjay and Lipton, Zachary C.\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2305.15444\"}, {\"key\": \"json-schema-bench-2025\", \"type\": \"article\", \"title\": \"Generating Structured Outputs from Language Models: Benchmark and Studies\", \"authors\": \"Li, Saibo and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2501.10868\"}], \"tex_citations\": [{\"key\": \"llm4ie-survey-2024\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"parse-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"llm4ie-survey-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"instructuie-2023\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"knowcoder-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"codeie-2023\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"gollie-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"adelie-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"slot-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oneke-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"promptner-2023\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"gliner-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"gliner2-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"self-improve-ner-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"zeroner-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"guidex-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"nuner-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"self-prompting-re-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"code4uie-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"familiarity-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"json-schema-bench-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"iepile-2024\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"dee-2024\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"crossagentie-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"cmas-ner-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"spt-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"dlisc-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"kggen-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"gao-repr-degen-2019\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"godey-anisotropy-inherent-2024\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"fewnerd-2021\", \"file\": \"experimental_setup.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"experimental_setup.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"experimental_setup.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 52, \"command\": \"cite\"}, {\"key\": \"minilm-2019\", \"file\": \"experimental_setup.tex\", \"line\": 52, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 85, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"experimental_setup.tex\", \"line\": 85, \"command\": \"cite\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"results.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"results.tex\", \"line\": 117, \"command\": \"citet\"}, {\"key\": \"uniner-2024\", \"file\": \"sdgd_negative.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"llm-calibration-survey-2024\", \"file\": \"sdgd_negative.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"sdgd_negative.tex\", \"line\": 41, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"llm-pee-2025\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=liu vs api=2025\"], \"note\": \"\"}, {\"key\": \"parse-2025\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dee-2024\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"crossagentie-2025\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=lu vs api=meng\"], \"note\": \"\"}, {\"key\": \"dlisc-2025\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\", \"status\": \"not_found\", \"confidence\": 0.376, \"matched_title\": \"Findings of the Association for Computational Linguistics: EMNLP 2023\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"spt-2025\", \"title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zeroner-2025\", \"title\": \"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\", \"status\": \"not_found\", \"confidence\": 0.504, \"matched_title\": \"SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"cmas-ner-2025\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uniner-2024\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gollie-2024\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner-2024\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner2-2025\", \"title\": \"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\", \"status\": \"not_found\", \"confidence\": 0.312, \"matched_title\": \"GLiNER-Relex: A Unified Framework for Joint Named Entity Recognition and Relation Extraction\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"kggen-2025\", \"title\": \"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"code4uie-2024\", \"title\": \"Retrieval-Augmented Code Generation for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Retrieval-Augmented Code Generation for Universal Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"iepile-2024\", \"title\": \"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lost-in-middle-2024\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self-improve-ner-2024\", \"title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self-prompting-re-2024\", \"title\": \"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\", \"status\": \"not_found\", \"confidence\": 0.47, \"matched_title\": \"Large language models for generative information extraction: a survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.47 below threshold 0.82\"}, {\"key\": \"nuner-2024\", \"title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"familiarity-2025\", \"title\": \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guidex-2025\", \"title\": \"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=de la fuente vs api=fuente\"], \"note\": \"\"}, {\"key\": \"llm4ie-survey-2024\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large language models for generative information extraction: a survey\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"knowcoder-2024\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"slot-2025\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SLOT: Structuring the Output of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=shen vs api=wang\"], \"note\": \"\"}, {\"key\": \"gao-repr-degen-2019\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ethayarajh-contextual-2019\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"godey-anisotropy-inherent-2024\", \"title\": \"Anisotropy Is Inherent to Self-Attention in Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Anisotropy Is Inherent to Self-Attention in Transformers\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"instructuie-2023\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"codeie-2023\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"adelie-2024\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oneke-2025\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm-calibration-survey-2024\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewnerd-2021\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewrel-2018\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"maven-2020\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3-2025\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"minilm-2019\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vllm-2023\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"promptner-2023\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PromptNER: Prompting For Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"json-schema-bench-2025\", \"title\": \"Generating Structured Outputs from Language Models: Benchmark and Studies\", \"status\": \"not_found\", \"confidence\": 0.328, \"matched_title\": \"Gradient-based learning applied to document recognition\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b17e7c86-dd67-47dc-bcc6-d6eb8021df9d",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "b3247066-7da0-45b6-a16a-6340040719d7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 42, \\\"total_citations\\\": 54, \\\"unique_cited_keys\\\": 42, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 32, \\\"online_not_found\\\": 5, \\\"online_mismatch\\\": 5}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"llm-pee-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"authors\\\": \\\"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"authors\\\": \\\"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.08623\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"authors\\\": \\\"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"authors\\\": \\\"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"dlisc-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\", \\\"authors\\\": \\\"Wen, Zhihao and Liang, Sheng and Wu, Yaxiong and Zhang, Yongyue and Liu, Yong\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.14992\\\"}, {\\\"key\\\": \\\"spt-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Schema as Parameterized Tools for Universal Information Extraction\\\", \\\"authors\\\": \\\"Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2506.01276\\\"}, {\\\"key\\\": \\\"zeroner-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\", \\\"authors\\\": \\\"Cocchieri, Alessio and Mart\\\\\\\\'\\\\\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"authors\\\": \\\"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM Web Conference 2025\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and Garc\\\\\\\\'\\\\\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"authors\\\": \\\"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\", \\\"authors\\\": \\\"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"kggen-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\", \\\"authors\\\": \\\"Mo, Belinda and Yu, Kyssen and Kazdan, Joshua and Cabezas, Joan and Mpala, Proud...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"code4uie-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\", \\\"authors\\\": \\\"Guo, Yucan and Li, Zixuan and Jin, Xiaolong and Liu, Yantao and Zeng, Yutao and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"NeurIPS 2024 Workshop\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\", \\\"authors\\\": \\\"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"authors\\\": \\\"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"self-improve-ner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\", \\\"authors\\\": \\\"Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"self-prompting-re-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\", \\\"authors\\\": \\\"Liu, Siyi and Li, Yang and Li, Jiang and Yang, Shan and Lan, Yunshi\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2024\\\"}, {\\\"key\\\": \\\"nuner-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\", \\\"authors\\\": \\\"Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth\\\\\\\\'ee and Crabb\\\\\\\\'e,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"familiarity-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training D...\\\", \\\"authors\\\": \\\"Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Ni...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guidex-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\", \\\"authors\\\": \\\"De La Fuente, Neil and Sainz, Oscar and Garc\\\\\\\\'\\\\\\\\ia-Ferrero, Iker and Agirre, Enek...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Models for Generative Information Extraction: A Survey\\\", \\\"authors\\\": \\\"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Frontiers of Computer Science\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"authors\\\": \\\"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"authors\\\": \\\"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"authors\\\": \\\"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"authors\\\": \\\"Ethayarajh, Kawin\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"authors\\\": \\\"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"godey-anisotropy-inherent-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Anisotropy Is Inherent to Self-Attention in Transformers\\\", \\\"authors\\\": \\\"Godey, Nathan and de la Clergerie, \\\\\\\\'Eric and Sagot, Beno\\\\\\\\^\\\\\\\\it\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 18th Conference of the European Chapter of the Association fo...\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"authors\\\": \\\"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"authors\\\": \\\"Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Companion Proceedings of the ACM Web Conference 2025\\\"}, {\\\"key\\\": \\\"llm-calibration-survey-2024\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"authors\\\": \\\"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"authors\\\": \\\"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"authors\\\": \\\"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.09388\\\"}, {\\\"key\\\": \\\"minilm-2019\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"authors\\\": \\\"Reimers, Nils and Gurevych, Iryna\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"authors\\\": \\\"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 29th Symposium on Operating Systems Principles\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"authors\\\": \\\"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"authors\\\": \\\"Ashok, Dhananjay and Lipton, Zachary C.\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2305.15444\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Generating Structured Outputs from Language Models: Benchmark and Studies\\\", \\\"authors\\\": \\\"Li, Saibo and others\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2501.10868\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"self-improve-ner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zeroner-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"guidex-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nuner-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"self-prompting-re-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"code4uie-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"familiarity-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"spt-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dlisc-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kggen-2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"godey-anisotropy-inherent-2024\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 52, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"minilm-2019\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 52, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 85, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"file\\\": \\\"experimental_setup.tex\\\", \\\"line\\\": 85, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 117, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"file\\\": \\\"sdgd_negative.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"llm-calibration-survey-2024\\\", \\\"file\\\": \\\"sdgd_negative.tex\\\", \\\"line\\\": 38, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"llm-pee-2025\\\", \\\"file\\\": \\\"sdgd_negative.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"citet\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"llm-pee-2025\\\", \\\"title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=liu vs api=2025\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"parse-2025\\\", \\\"title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dee-2024\\\", \\\"title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"crossagentie-2025\\\", \\\"title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=lu vs api=meng\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dlisc-2025\\\", \\\"title\\\": \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.376, \\\"matched_title\\\": \\\"Findings of the Association for Computational Linguistics: EMNLP 2023\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.38 below threshold 0.82\\\"}, {\\\"key\\\": \\\"spt-2025\\\", \\\"title\\\": \\\"Schema as Parameterized Tools for Universal Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Schema as Parameterized Tools for Universal Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zeroner-2025\\\", \\\"title\\\": \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.504, \\\"matched_title\\\": \\\"SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.50 below threshold 0.82\\\"}, {\\\"key\\\": \\\"cmas-ner-2025\\\", \\\"title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"uniner-2024\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gollie-2024\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gliner-2024\\\", \\\"title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gliner2-2025\\\", \\\"title\\\": \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.312, \\\"matched_title\\\": \\\"GLiNER-Relex: A Unified Framework for Joint Named Entity Recognition and Relation Extraction\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.31 below threshold 0.82\\\"}, {\\\"key\\\": \\\"kggen-2025\\\", \\\"title\\\": \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"code4uie-2024\\\", \\\"title\\\": \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"iepile-2024\\\", \\\"title\\\": \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lost-in-middle-2024\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"self-improve-ner-2024\\\", \\\"title\\\": \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"self-prompting-re-2024\\\", \\\"title\\\": \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.47, \\\"matched_title\\\": \\\"Large language models for generative information extraction: a survey\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.47 below threshold 0.82\\\"}, {\\\"key\\\": \\\"nuner-2024\\\", \\\"title\\\": \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"familiarity-2025\\\", \\\"title\\\": \\\"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guidex-2025\\\", \\\"title\\\": \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=de la fuente vs api=fuente\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llm4ie-survey-2024\\\", \\\"title\\\": \\\"Large Language Models for Generative Information Extraction: A Survey\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large language models for generative information extraction: a survey\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"knowcoder-2024\\\", \\\"title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"slot-2025\\\", \\\"title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SLOT: Structuring the Output of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=shen vs api=wang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gao-repr-degen-2019\\\", \\\"title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ethayarajh-contextual-2019\\\", \\\"title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cai-isotropy-clusters-2021\\\", \\\"title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"godey-anisotropy-inherent-2024\\\", \\\"title\\\": \\\"Anisotropy Is Inherent to Self-Attention in Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Anisotropy Is Inherent to Self-Attention in Transformers\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"instructuie-2023\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"codeie-2023\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"adelie-2024\\\", \\\"title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oneke-2025\\\", \\\"title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"llm-calibration-survey-2024\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fewnerd-2021\\\", \\\"title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-NERD: A Few-shot Named Entity Recognition Dataset\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fewrel-2018\\\", \\\"title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"maven-2020\\\", \\\"title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MAVEN: A Massive General Domain Event Detection Dataset\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen3-2025\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Qwen3 Technical Report\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=team vs api=yang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"minilm-2019\\\", \\\"title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vllm-2023\\\", \\\"title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Memory Management for Large Language Model Serving with PagedAttention\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xie-zeroshot-ner-2023\\\", \\\"title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Empirical Study of Zero-Shot NER with ChatGPT\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"promptner-2023\\\", \\\"title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PromptNER: Prompting For Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"json-schema-bench-2025\\\", \\\"title\\\": \\\"Generating Structured Outputs from Language Models: Benchmark and Studies\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.328, \\\"matched_title\\\": \\\"Gradient-based learning applied to document recognition\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 42, \"total_citations\": 54, \"unique_cited_keys\": 42, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 32, \"online_not_found\": 5, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"article\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.08623\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"dlisc-2025\", \"type\": \"article\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\", \"authors\": \"Wen, Zhihao and Liang, Sheng and Wu, Yaxiong and Zhang, Yongyue and Liu, Yong\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.14992\"}, {\"key\": \"spt-2025\", \"type\": \"article\", \"title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"authors\": \"Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2506.01276\"}, {\"key\": \"zeroner-2025\", \"type\": \"inproceedings\", \"title\": \"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\", \"authors\": \"Cocchieri, Alessio and Mart\\\\'\\\\inez Galindo, Marcos and Frisoni, Giacomo and Moro...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"cmas-ner-2025\", \"type\": \"inproceedings\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"authors\": \"Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maart...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"uniner-2024\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gollie-2024\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and Garc\\\\'\\\\ia-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacall...\", \"year\": \"2024\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"gliner-2024\", \"type\": \"inproceedings\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"authors\": \"Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"gliner2-2025\", \"type\": \"inproceedings\", \"title\": \"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\", \"authors\": \"Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"kggen-2025\", \"type\": \"inproceedings\", \"title\": \"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\", \"authors\": \"Mo, Belinda and Yu, Kyssen and Kazdan, Joshua and Cabezas, Joan and Mpala, Proud...\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"code4uie-2024\", \"type\": \"inproceedings\", \"title\": \"Retrieval-Augmented Code Generation for Universal Information Extraction\", \"authors\": \"Guo, Yucan and Li, Zixuan and Jin, Xiaolong and Liu, Yantao and Zeng, Yutao and ...\", \"year\": \"2024\", \"venue\": \"NeurIPS 2024 Workshop\"}, {\"key\": \"iepile-2024\", \"type\": \"inproceedings\", \"title\": \"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\", \"authors\": \"Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lost-in-middle-2024\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilac...\", \"year\": \"2024\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"self-improve-ner-2024\", \"type\": \"inproceedings\", \"title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"self-prompting-re-2024\", \"type\": \"inproceedings\", \"title\": \"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\", \"authors\": \"Liu, Siyi and Li, Yang and Li, Jiang and Yang, Shan and Lan, Yunshi\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2024\"}, {\"key\": \"nuner-2024\", \"type\": \"inproceedings\", \"title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"authors\": \"Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth\\\\'ee and Crabb\\\\'e,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"familiarity-2025\", \"type\": \"inproceedings\", \"title\": \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training D...\", \"authors\": \"Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Ni...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guidex-2025\", \"type\": \"inproceedings\", \"title\": \"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\", \"authors\": \"De La Fuente, Neil and Sainz, Oscar and Garc\\\\'\\\\ia-Ferrero, Iker and Agirre, Enek...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"llm4ie-survey-2024\", \"type\": \"article\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"authors\": \"Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao,...\", \"year\": \"2024\", \"venue\": \"Frontiers of Computer Science\"}, {\"key\": \"knowcoder-2024\", \"type\": \"inproceedings\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"authors\": \"Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 62nd Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"slot-2025\", \"type\": \"inproceedings\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"authors\": \"Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhic...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"gao-repr-degen-2019\", \"type\": \"inproceedings\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"authors\": \"Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan\", \"year\": \"2019\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"ethayarajh-contextual-2019\", \"type\": \"inproceedings\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"authors\": \"Ethayarajh, Kawin\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"type\": \"inproceedings\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"authors\": \"Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth\", \"year\": \"2021\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"godey-anisotropy-inherent-2024\", \"type\": \"inproceedings\", \"title\": \"Anisotropy Is Inherent to Self-Attention in Transformers\", \"authors\": \"Godey, Nathan and de la Clergerie, \\\\'Eric and Sagot, Beno\\\\^\\\\it\", \"year\": \"2024\", \"venue\": \"Proceedings of the 18th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"instructuie-2023\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"codeie-2023\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"adelie-2024\", \"type\": \"inproceedings\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"authors\": \"Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juan...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"oneke-2025\", \"type\": \"inproceedings\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"authors\": \"Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and...\", \"year\": \"2025\", \"venue\": \"Companion Proceedings of the ACM Web Conference 2025\"}, {\"key\": \"llm-calibration-survey-2024\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"fewnerd-2021\", \"type\": \"inproceedings\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"authors\": \"Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xi...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 59th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"fewrel-2018\", \"type\": \"inproceedings\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"authors\": \"Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiy...\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"maven-2020\", \"type\": \"inproceedings\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"authors\": \"Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu...\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"qwen3-2025\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"minilm-2019\", \"type\": \"article\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"authors\": \"Reimers, Nils and Gurevych, Iryna\", \"year\": \"2019\", \"venue\": \"Proceedings of the 2019 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"vllm-2023\", \"type\": \"inproceedings\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"authors\": \"Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianm...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 29th Symposium on Operating Systems Principles\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"type\": \"inproceedings\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"authors\": \"Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, ...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"promptner-2023\", \"type\": \"article\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"authors\": \"Ashok, Dhananjay and Lipton, Zachary C.\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2305.15444\"}, {\"key\": \"json-schema-bench-2025\", \"type\": \"article\", \"title\": \"Generating Structured Outputs from Language Models: Benchmark and Studies\", \"authors\": \"Li, Saibo and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2501.10868\"}], \"tex_citations\": [{\"key\": \"llm4ie-survey-2024\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"parse-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"llm-pee-2025\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"fewnerd-2021\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"llm4ie-survey-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"instructuie-2023\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"knowcoder-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"codeie-2023\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"gollie-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"adelie-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"slot-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oneke-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"promptner-2023\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"uniner-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"gliner-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"gliner2-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"self-improve-ner-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"zeroner-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"guidex-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"nuner-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"self-prompting-re-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"code4uie-2024\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"familiarity-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"json-schema-bench-2025\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"iepile-2024\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"parse-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"dee-2024\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"crossagentie-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"cmas-ner-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"spt-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"dlisc-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"kggen-2025\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"gao-repr-degen-2019\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"ethayarajh-contextual-2019\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"godey-anisotropy-inherent-2024\", \"file\": \"related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"fewnerd-2021\", \"file\": \"experimental_setup.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"fewrel-2018\", \"file\": \"experimental_setup.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"maven-2020\", \"file\": \"experimental_setup.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 52, \"command\": \"cite\"}, {\"key\": \"minilm-2019\", \"file\": \"experimental_setup.tex\", \"line\": 52, \"command\": \"cite\"}, {\"key\": \"qwen3-2025\", \"file\": \"experimental_setup.tex\", \"line\": 85, \"command\": \"cite\"}, {\"key\": \"vllm-2023\", \"file\": \"experimental_setup.tex\", \"line\": 85, \"command\": \"cite\"}, {\"key\": \"lost-in-middle-2024\", \"file\": \"results.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"file\": \"results.tex\", \"line\": 117, \"command\": \"citet\"}, {\"key\": \"uniner-2024\", \"file\": \"sdgd_negative.tex\", \"line\": 7, \"command\": \"citet\"}, {\"key\": \"llm-calibration-survey-2024\", \"file\": \"sdgd_negative.tex\", \"line\": 38, \"command\": \"cite\"}, {\"key\": \"llm-pee-2025\", \"file\": \"sdgd_negative.tex\", \"line\": 41, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"llm-pee-2025\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=liu vs api=2025\"], \"note\": \"\"}, {\"key\": \"parse-2025\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dee-2024\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"crossagentie-2025\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=lu vs api=meng\"], \"note\": \"\"}, {\"key\": \"dlisc-2025\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\", \"status\": \"not_found\", \"confidence\": 0.376, \"matched_title\": \"Findings of the Association for Computational Linguistics: EMNLP 2023\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"spt-2025\", \"title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Schema as Parameterized Tools for Universal Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zeroner-2025\", \"title\": \"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\", \"status\": \"not_found\", \"confidence\": 0.504, \"matched_title\": \"SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"cmas-ner-2025\", \"title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uniner-2024\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gollie-2024\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner-2024\", \"title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gliner2-2025\", \"title\": \"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\", \"status\": \"not_found\", \"confidence\": 0.312, \"matched_title\": \"GLiNER-Relex: A Unified Framework for Joint Named Entity Recognition and Relation Extraction\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"kggen-2025\", \"title\": \"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"code4uie-2024\", \"title\": \"Retrieval-Augmented Code Generation for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Retrieval-Augmented Code Generation for Universal Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"iepile-2024\", \"title\": \"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lost-in-middle-2024\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self-improve-ner-2024\", \"title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self-prompting-re-2024\", \"title\": \"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\", \"status\": \"not_found\", \"confidence\": 0.47, \"matched_title\": \"Large language models for generative information extraction: a survey\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.47 below threshold 0.82\"}, {\"key\": \"nuner-2024\", \"title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"familiarity-2025\", \"title\": \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guidex-2025\", \"title\": \"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=de la fuente vs api=fuente\"], \"note\": \"\"}, {\"key\": \"llm4ie-survey-2024\", \"title\": \"Large Language Models for Generative Information Extraction: A Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large language models for generative information extraction: a survey\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"knowcoder-2024\", \"title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"slot-2025\", \"title\": \"SLOT: Structuring the Output of Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SLOT: Structuring the Output of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=shen vs api=wang\"], \"note\": \"\"}, {\"key\": \"gao-repr-degen-2019\", \"title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Representation Degeneration Problem in Training Natural Language Generation Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ethayarajh-contextual-2019\", \"title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cai-isotropy-clusters-2021\", \"title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"godey-anisotropy-inherent-2024\", \"title\": \"Anisotropy Is Inherent to Self-Attention in Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Anisotropy Is Inherent to Self-Attention in Transformers\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"instructuie-2023\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"codeie-2023\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"adelie-2024\", \"title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ADELIE: Aligning Large Language Models on Information Extraction\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oneke-2025\", \"title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"llm-calibration-survey-2024\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewnerd-2021\", \"title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-NERD: A Few-shot Named Entity Recognition Dataset\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fewrel-2018\", \"title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"maven-2020\", \"title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MAVEN: A Massive General Domain Event Detection Dataset\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3-2025\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"minilm-2019\", \"title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vllm-2023\", \"title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Memory Management for Large Language Model Serving with PagedAttention\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xie-zeroshot-ner-2023\", \"title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Empirical Study of Zero-Shot NER with ChatGPT\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"promptner-2023\", \"title\": \"PromptNER: Prompting For Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PromptNER: Prompting For Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"json-schema-bench-2025\", \"title\": \"Generating Structured Outputs from Language Models: Benchmark and Studies\", \"status\": \"not_found\", \"confidence\": 0.328, \"matched_title\": \"Gradient-based learning applied to document recognition\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "b17e7c86-dd67-47dc-bcc6-d6eb8021df9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43 · 2026-05-16T00:54:56.954Z_

```json
{
  "parentUuid": "b3247066-7da0-45b6-a16a-6340040719d7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "104472d6-a668-4f4d-9158-a2726f587b77",
  "timestamp": "2026-05-16T00:54:56.954Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）  **论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\" **Venue：** EMNLP 2026 Main Confer…",
  "leafUuid": "104472d6-a668-4f4d-9158-a2726f587b77",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for EMNLP schema extraction paper",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Assistant

_source line 46 · 2026-05-16T00:55:00.242Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have all the paper content and the reference verification results. Let me now fetch the ACL ARR review form to get the official scoring criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "104472d6-a668-4f4d-9158-a2726f587b77",
  "isSidechain": false,
  "requestId": "req_011Cb5LSoZN9bfyPQAhB9AbX",
  "type": "assistant",
  "uuid": "da7de300-a59d-4489-b324-0dc08bb2cbd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PZM9R7JG63eYWNxXPiXW6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28900,
      "cache_read_input_tokens": 28401,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 28401,
          "cache_creation_input_tokens": 28900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28900
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

_source line 47 · 2026-05-16T00:55:00.754Z_

现在获取 ACL ARR 官方 review form 评分维度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da7de300-a59d-4489-b324-0dc08bb2cbd1",
  "isSidechain": false,
  "requestId": "req_011Cb5LSoZN9bfyPQAhB9AbX",
  "type": "assistant",
  "uuid": "32e38a82-b232-4fce-bd39-dfcd2edbea2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PZM9R7JG63eYWNxXPiXW6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28900,
      "cache_read_input_tokens": 28401,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 28401,
          "cache_creation_input_tokens": 28900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28900
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

_source line 48 · 2026-05-16T00:55:03.827Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RqBNk2AYzVWvprmiZ3DEoK`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall, etc.) 2) The numeric scale for each 3) Description of each score level 4) Any other required fields (confidence, limitations, etc.)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32e38a82-b232-4fce-bd39-dfcd2edbea2e",
  "isSidechain": false,
  "requestId": "req_011Cb5LSoZN9bfyPQAhB9AbX",
  "type": "assistant",
  "uuid": "0bb6844a-4201-4e09-9055-ba67e0fa06d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PZM9R7JG63eYWNxXPiXW6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28900,
      "cache_read_input_tokens": 28401,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 28401,
          "cache_creation_input_tokens": 28900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28900
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

_source line 49 · 2026-05-16T00:55:04.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016e4ejcpwokkZJs6RLtXUAD`</summary>

```json
{
  "query": "EMNLP 2026 submission requirements page limit ethics statement responsible NLP checklist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bb6844a-4201-4e09-9055-ba67e0fa06d0",
  "isSidechain": false,
  "requestId": "req_011Cb5LSoZN9bfyPQAhB9AbX",
  "type": "assistant",
  "uuid": "945badb6-8f6b-445d-8cb3-9bfae09f1447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PZM9R7JG63eYWNxXPiXW6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28900,
      "cache_read_input_tokens": 28401,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 28401,
          "cache_creation_input_tokens": 28900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28900
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

_source line 50 · 2026-05-16T00:55:09.850Z_

<details><summary>↩ Tool result · `toolu_01RqBNk2AYzVWvprmiZ3DEoK`</summary>

```text
# ACL ARR Review Form Criteria and Scales

## Primary Scoring Dimensions

### 1. Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" with unlikely but conceivable gaps
- 3: "Pretty sure" but chance of missing details
- 2: "Willing to defend" evaluation despite likely gaps
- 1: "Not my area" or paper very difficult to understand

### 2. Soundness
**Scale: 1-5 (with half-point increments)**
- 5: Exceptionally thorough study
- 4: Provides sufficient support; extra experiments optional
- 3: Main claims supported; minor details need refinement
- 2: Insufficient support for main claims; major technical problems
- 1: Insufficient rigor or lacks ACL relevance

### 3. Excitement
**Scale: 1-5 (with half-point increments)**
- 5: Highly recommend; would attend presentation
- 4: Would mention to colleagues and effort to attend
- 3: Might mention points; attend if time available
- 2: Doesn't resonate personally but may interest others
- 1: Lacks resonance; unlikely to interest broader community

### 4. Overall Assessment
**Scale: 1-5 (with half-point increments)**
- 5: Award consideration candidate
- 4: Conference acceptance recommended
- 3: Findings track acceptance recommended
- 2: Substantial revisions needed
- 1: Do not resubmit or not ACL-relevant

## Additional Required Fields

- **Paper Summary**
- **Summary of Strengths**
- **Summary of Weaknesses**
- **Comments/Suggestions/Typos**
- **Limitations and Societal Impact** evaluation
- **Ethical Concerns** assessment
- **Reproducibility** (1-5 scale)
- **Datasets** value rating (1-5 scale)
- **Software** value rating (1-5 scale)
- **Author Identity Knowledge** (1-5 scale)
- **Ethics Review** necessity determination
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bb6844a-4201-4e09-9055-ba67e0fa06d0",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "25c5d780-51d5-4126-9705-5af8b6e4c3d8",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL ARR Review Form Criteria and Scales\n\n## Primary Scoring Dimensions\n\n### 1. Reviewer Confidence\n**Scale: 1-5**\n- 5: \"Positive that my evaluation is correct\"\n- 4: \"Quite sure\" with unlikely but conceivable gaps\n- 3: \"Pretty sure\" but chance of missing details\n- 2: \"Willing to defend\" evaluation despite likely gaps\n- 1: \"Not my area\" or paper very difficult to understand\n\n### 2. Soundness\n**Scale: 1-5 (with half-point increments)**\n- 5: Exceptionally thorough study\n- 4: Provides sufficient support; extra experiments optional\n- 3: Main claims supported; minor details need refinement\n- 2: Insufficient support for main claims; major technical problems\n- 1: Insufficient rigor or lacks ACL relevance\n\n### 3. Excitement\n**Scale: 1-5 (with half-point increments)**\n- 5: Highly recommend; would attend presentation\n- 4: Would mention to colleagues and effort to attend\n- 3: Might mention points; attend if time available\n- 2: Doesn't resonate personally but may interest others\n- 1: Lacks resonance; unlikely to interest broader community\n\n### 4. Overall Assessment\n**Scale: 1-5 (with half-point increments)**\n- 5: Award consideration candidate\n- 4: Conference acceptance recommended\n- 3: Findings track acceptance recommended\n- 2: Substantial revisions needed\n- 1: Do not resubmit or not ACL-relevant\n\n## Additional Required Fields\n\n- **Paper Summary**\n- **Summary of Strengths**\n- **Summary of Weaknesses**\n- **Comments/Suggestions/Typos**\n- **Limitations and Societal Impact** evaluation\n- **Ethical Concerns** assessment\n- **Reproducibility** (1-5 scale)\n- **Datasets** value rating (1-5 scale)\n- **Software** value rating (1-5 scale)\n- **Author Identity Knowledge** (1-5 scale)\n- **Ethics Review** necessity determination",
    "durationMs": 6017,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "0bb6844a-4201-4e09-9055-ba67e0fa06d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-16T00:55:13.657Z_

<details><summary>↩ Tool result · `toolu_016e4ejcpwokkZJs6RLtXUAD`</summary>

```text
Web search results for query: "EMNLP 2026 submission requirements page limit ethics statement responsible NLP checklist"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Checklist for Original, First Time Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/OriginalSubmissionChecklist"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guidelines | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/pages/submission-guidelines"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Let me search for the main conference paper submission requirements page to get more specific information about page limits and the responsible NLP checklist.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Responsible NLP Checklist","url":"https://aclanthology.org/attachments/2025.emnlp-main.1625.checklist.pdf"},{"title":"EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices","url":"http://aclrollingreview.org/responsible-nlp-checklist-appendices"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Responsible NLP Research checklist","url":"http://aclrollingreview.org/responsibleNLPresearch/"},{"title":"EMNLP 2025 on X: \"For EMNLP authors, please note that the responsible NLP research checklists will be included with all papers published at EMNLP (and future *CL conferences) as an additional appendix, as per the updated ARR policy: https://t.co/Uwna96UMTT @ReviewAcl\" / X","url":"https://x.com/emnlpmeeting/status/1933196156995063863"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on my web search, here are the key EMNLP 2026 submission requirements regarding page limits, ethics statements, and the responsible NLP checklist:

## Page Limits

Long papers have a limit of 8 pages and short papers 4 pages. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Ethics Statement and Ethical Considerations

Where a paper may raise ethical issues, authors should include an explicit discussion of these issues, which will be taken into account in the review process. Authors will be allowed extra space after the sixth page for an optional broader impact statement or other discussion of ethics. An ethical considerations section is not required, but papers working with sensitive data or on sensitive tasks that do not discuss these issues will not be accepted.

## Responsible NLP Checklist

Both long and short paper submissions should follow all of the ARR submission requirements, including ACL's Publication Ethics Policy and ARR's Ethics Policy including the responsible NLP research checklist.

Authors must complete a responsible NLP research checklist as part of their paper submission. The content of checklists is used in the review process, and incorrect, incomplete or misleading information in the checklist can result in desk rejection.

Starting with EMNLP 2025, the responsible NLP checklist will be included as appendices with their papers, which will continue for EMNLP 2026.

For complete details on all submission requirements, you can visit the official EMNLP 2026 Call for Main Conference Papers at https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "945badb6-8f6b-445d-8cb3-9bfae09f1447",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "4b684f5b-2ebb-450e-8d15-4f06e078333d",
  "toolUseResult": {
    "query": "EMNLP 2026 submission requirements page limit ethics statement responsible NLP checklist",
    "results": [
      {
        "tool_use_id": "srvtoolu_017iiHXdy6PrFhgCXSqXFryH",
        "content": [
          {
            "title": "Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/industry_track/"
          },
          {
            "title": "Confs: 2026 Conference on Empirical Methods in Natural ...",
            "url": "https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"
          },
          {
            "title": "EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X",
            "url": "https://x.com/emnlpmeeting/status/2047977818928320807"
          },
          {
            "title": "Call for workshops: EMNLP & AACL",
            "url": "https://groups.google.com/g/ml-news/c/W-fucfhVto4"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Submission Checklist for Original, First Time Submissions | Computational Linguistics",
            "url": "https://submissions.cljournal.org/index.php/cljournal/OriginalSubmissionChecklist"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "Submission Guidelines | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/pages/submission-guidelines"
          },
          {
            "title": "EMNLP 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=EMNLP%2F2026%2FConference"
          }
        ]
      },
      "Let me search for the main conference paper submission requirements page to get more specific information about page limits and the responsible NLP checklist.",
      {
        "tool_use_id": "srvtoolu_01EM5M5uXh98Lhos4HiWGV4K",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=883"
          },
          {
            "title": "EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/emnlp"
          },
          {
            "title": "EMNLP 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=EMNLP%2F2026%2FConference"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub",
            "url": "https://github.com/acl-org/emnlp-2026"
          },
          {
            "title": "Confs: 2026 Conference on Empirical Methods in Natural ...",
            "url": "https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01WSTcnWDUv26LrB6kxfpozD",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Responsible NLP Checklist",
            "url": "https://aclanthology.org/attachments/2025.emnlp-main.1625.checklist.pdf"
          },
          {
            "title": "EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices",
            "url": "http://aclrollingreview.org/responsible-nlp-checklist-appendices"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "ARR Responsible NLP Research checklist",
            "url": "http://aclrollingreview.org/responsibleNLPresearch/"
          },
          {
            "title": "EMNLP 2025 on X: \"For EMNLP authors, please note that the responsible NLP research checklists will be included with all papers published at EMNLP (and future *CL conferences) as an additional appendix, as per the updated ARR policy: https://t.co/Uwna96UMTT @ReviewAcl\" / X",
            "url": "https://x.com/emnlpmeeting/status/1933196156995063863"
          },
          {
            "title": "Confs: 2026 Conference on Empirical Methods in Natural ...",
            "url": "https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)",
            "url": "http://aclrollingreview.org/incentives2025"
          },
          {
            "title": "Authors Guidelines",
            "url": "http://aclrollingreview.org/authors"
          }
        ]
      },
      "Based on my web search, here are the key EMNLP 2026 submission requirements regarding page limits, ethics statements, and the responsible NLP checklist:\n\n## Page Limits\n\nLong papers have a limit of 8 pages and short papers 4 pages. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.\n\n## Ethics Statement and Ethical Considerations\n\nWhere a paper may raise ethical issues, authors should include an explicit discussion of these issues, which will be taken into account in the review process. Authors will be allowed extra space after the sixth page for an optional broader impact statement or other discussion of ethics. An ethical considerations section is not required, but papers working with sensitive data or on sensitive tasks that do not discuss these issues will not be accepted.\n\n## Responsible NLP Checklist\n\nBoth long and short paper submissions should follow all of the ARR submission requirements, including ACL's Publication Ethics Policy and ARR's Ethics Policy including the responsible NLP research checklist.\n\nAuthors must complete a responsible NLP research checklist as part of their paper submission. The content of checklists is used in the review process, and incorrect, incomplete or misleading information in the checklist can result in desk rejection.\n\nStarting with EMNLP 2025, the responsible NLP checklist will be included as appendices with their papers, which will continue for EMNLP 2026.\n\nFor complete details on all submission requirements, you can visit the official EMNLP 2026 Call for Main Conference Papers at https://2026.emnlp.org/calls/main_conference_papers/"
    ],
    "durationSeconds": 9.385516256999995
  },
  "sourceToolAssistantUUID": "945badb6-8f6b-445d-8cb3-9bfae09f1447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-16T00:56:07.802Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me compile a thorough review. Let me organize my findings:

## Key observations from reading the paper:

### Novelty & Contributions
1. The claim "first controlled empirical study isolating type confusability from type count" - this is the core novelty claim. Need to assess if this is truly novel.
2. Four contributions listed in introduction
3. SCS/BCS metric is essentially just cosine similarity between embeddings - very simple
4. The multi-channel degradation model is an empirical observation framework, not a theoretical model
5. The negative result (SDGD) is interesting but the merge amplification finding is somewhat expected


6. The paper structure is unconventional - there's no dedicated Discussion section, just a single-paragraph Conclusion, and all figures are relegated to the appendix rather than integrated into the main text. The related work section covers LLM-PEE positioning well but misses some relevant work on prompt optimization for IE and schema decomposition in structured prediction. The Limitations section exists but is compressed into one dense paragraph, making it hard to parse the key constraints.

Now I'm estimating the page count by examining the content volume across sections - the abstract, five main sections of text, and five tables in the body add up to something quite dense, and I'm trying to figure out if this fits within the 8-page limit given the amount of material.

Looking at the critical issues, the biggest problem is that all the key visualizations - the count curves, BCS scaling, and error taxonomy - are stuck in the appendix when they should be in the main body where reviewers will actually see them. Beyond that, the discussion section is essentially nonexistent, just a 5-line conclusion, which leaves no room to interpret what these nuanced findings across the three tasks actually mean or to offer concrete recommendations. And the pairwise SCS correlation is troublingly weak at only 1.3-1.7% r².

The 3.4× amplification claim that anchors the whole paper is also concerning because it's really just a two-point comparison between the 16-rel and 80-rel pools, with the 40-rel point not being truly independent since it uses subsets of the larger pool. I also need to add the Responsible NLP Research Checklist that ARR and EMNLP require.

On the should-fix side, using different evaluation metrics across tasks - text-match F1 for NER versus accuracy for the others - makes it harder to compare results meaningfully.

The prompt inconsistency is problematic too: v1 had 96.5% fabricated offsets, so the NER count-curve results are built on a known-flawed prompt. MAVEN actually shows the opposite pattern for ED (improvement rather than degradation with more types), which partially undermines the schema-induced degradation narrative even though the centrality confound explanation accounts for it. The FewRel setup also merges training and validation splits for the 80-relation pool, creating a non-standard test configuration that deserves more visibility. And the primary experiments rely on a single model, Qwen3-32B.

The cross-model validation with Llama-3.1-8B shows mixed results—the NER findings don't robustly transfer to the 8B scale on Few-NERD. Calling the degradation framework a "model" is also an overstatement since it's really just a categorization of error patterns without formal parameters or predictive capability. The limitations section reads as one dense block when it should be broken into distinct points, there are a handful of reference verification issues, and the SDGD abbreviation appears inconsistently between the title context and Section 6 where it's formally introduced.

Looking at the reference gaps, I'm noticing several areas where the paper could strengthen its positioning: schema decomposition work beyond DEE and the 2024 LLM-PEE paper, prompt optimization literature beyond PARSE, broader LLM calibration research on structured generation, existing work on label confusion in classification tasks, and curriculum learning approaches that use embedding similarity for difficulty scoring. The claim about being the first to isolate type confusability in a controlled experiment needs more careful verification—while the paper does position itself well against LLM-PEE by separating count from confusability effects, I should check whether other papers have specifically studied type confusability. The reference verification also flagged some entries that couldn't be found online. The decomposition result being negative is actually informative even if somewhat expected, which pushes this toward a borderline accept—the experimental rigor is solid and the research question matters, but the weak correlations and presentation gaps (missing figures, no discussion section) hold it back. Before I finalize my assessment, I should check if there are any references I might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b684f5b-2ebb-450e-8d15-4f06e078333d",
  "isSidechain": false,
  "requestId": "req_011Cb5LU2zGwWWP5sah4Ud6e",
  "type": "assistant",
  "uuid": "5b8ae5ec-4eee-4968-adef-d6a5a91b4d96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ni556HnDMtC3VTxTsJDaJ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2883,
      "cache_read_input_tokens": 57301,
      "output_tokens": 2017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2017,
          "cache_read_input_tokens": 57301,
          "cache_creation_input_tokens": 2883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2883
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

_source line 53 · 2026-05-16T00:56:07.819Z_

搜索可能遗漏的相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b8ae5ec-4eee-4968-adef-d6a5a91b4d96",
  "isSidechain": false,
  "requestId": "req_011Cb5LU2zGwWWP5sah4Ud6e",
  "type": "assistant",
  "uuid": "73286d5d-b2aa-4b4e-babc-2c3b348cef69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ni556HnDMtC3VTxTsJDaJ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2883,
      "cache_read_input_tokens": 57301,
      "output_tokens": 2017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2017,
          "cache_read_input_tokens": 57301,
          "cache_creation_input_tokens": 2883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2883
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

_source line 54 · 2026-05-16T00:56:07.938Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XYvk7kE2orpnB73RtFs35d`</summary>

```json
{
  "query": "label confusion type confusion information extraction LLM schema complexity controlled experiment 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73286d5d-b2aa-4b4e-babc-2c3b348cef69",
  "isSidechain": false,
  "requestId": "req_011Cb5LU2zGwWWP5sah4Ud6e",
  "type": "assistant",
  "uuid": "948b012d-dff9-4786-993e-ab4b5218badc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ni556HnDMtC3VTxTsJDaJ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2883,
      "cache_read_input_tokens": 57301,
      "output_tokens": 2017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2017,
          "cache_read_input_tokens": 57301,
          "cache_creation_input_tokens": 2883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2883
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

_source line 55 · 2026-05-16T00:56:07.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016oLwf3GjPmgx8XEqmq9uEA`</summary>

```json
{
  "query": "prompt optimization schema decomposition zero-shot NER RE calibration structured generation 2024 2025 ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "948b012d-dff9-4786-993e-ab4b5218badc",
  "isSidechain": false,
  "requestId": "req_011Cb5LU2zGwWWP5sah4Ud6e",
  "type": "assistant",
  "uuid": "242e349b-89e7-4c6f-9c96-1d4e4ae46fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ni556HnDMtC3VTxTsJDaJ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2883,
      "cache_read_input_tokens": 57301,
      "output_tokens": 2017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2017,
          "cache_read_input_tokens": 57301,
          "cache_creation_input_tokens": 2883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2883
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

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）  **论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\" **Venue：** EMNLP 2026 Main Confer…",
  "leafUuid": "242e349b-89e7-4c6f-9c96-1d4e4ae46fd1",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for EMNLP schema extraction paper",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Tool result

_source line 58 · 2026-05-16T00:56:15.255Z_

<details><summary>↩ Tool result · `toolu_016oLwf3GjPmgx8XEqmq9uEA`</summary>

```text
Web search results for query: "prompt optimization schema decomposition zero-shot NER RE calibration structured generation 2024 2025 ACL EMNLP"

Links: [{"title":"PAFT: Prompt-Agnostic Fine-Tuning","url":"https://aclanthology.org/2025.emnlp-main.37.pdf"},{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"},{"title":"Reverse Prompt Engineering: A Zero-Shot, Genetic ...","url":"https://aclanthology.org/2025.emnlp-main.1333.pdf"},{"title":"GREATERPROMPT: A Unified, Customizable, and High- ...","url":"https://aclanthology.org/2025.acl-demo.39.pdf"},{"title":"ZERA: Zero-init Instruction Evolving Refinement Agent","url":"https://aclanthology.org/2025.emnlp-main.1190.pdf"},{"title":"GLiNER2: An Efficient Multi-Task Information Extraction ...","url":"https://aclanthology.org/2025.emnlp-demos.10.pdf"},{"title":"A Category-Theoretic Approach to Neural-Symbolic Task ...","url":"https://aclanthology.org/2025.findings-emnlp.1157.pdf"},{"title":"Achieving Superior Intent Extraction through Decomposition","url":"https://aclanthology.org/2025.emnlp-main.949.pdf"},{"title":"Discrete Prompt Optimization via Constrained Generation for Zero-shot Re-ranker - ACL Anthology","url":"https://aclanthology.org/2023.findings-acl.61/"},{"title":"GRASP: Replace Redundant Layers with Adaptive ...","url":"https://aclanthology.org/2025.emnlp-main.1338.pdf"}]

I've performed a web search for your query about prompt optimization, schema decomposition, zero-shot NER/RE, calibration, and structured generation from 2024-2025 ACL/EMNLP conferences. Here are the relevant findings:

## Key Papers and Systems Found:

**Prompt Optimization and Structured Generation:**

1. **GREATERPROMPT**: A unified prompt optimization tool that supports both gradient-based optimization and zero-shot optimized prompts, presented at ACL 2025.

2. **ZERA** (Zero-init Instruction Evolving Refinement Agent): Develops structured prompts via principle-based optimization, published at EMNLP 2025.

3. **Reverse Prompt Engineering**: A zero-shot, genetic algorithm approach presented at EMNLP 2025.

**NER and Information Extraction:**

4. **GLiNER2**: An efficient multi-task information extraction system for named entity recognition, published as a demo at EMNLP 2025.

5. **GLiREL**: A generalist model for zero-shot relation extraction.

**Schema Decomposition and Task Planning:**

6. A category-theoretic approach features LLM decomposition of natural language tasks into structured specifications with verification to ensure constraint satisfaction, presented at EMNLP 2025 Findings.

7. Papers on schema linking for NL-to-SQL and prompt optimization for conversational agents were accepted at EMNLP 2025 Industry Track.

These recent works demonstrate significant progress in combining prompt optimization with structured output generation, zero-shot learning capabilities, and task decomposition techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "242e349b-89e7-4c6f-9c96-1d4e4ae46fd1",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "6fcb76df-0046-45d6-924c-e12cb45934fa",
  "toolUseResult": {
    "query": "prompt optimization schema decomposition zero-shot NER RE calibration structured generation 2024 2025 ACL EMNLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_014aWqSjhe2prjXcTqtNVGrE",
        "content": [
          {
            "title": "PAFT: Prompt-Agnostic Fine-Tuning",
            "url": "https://aclanthology.org/2025.emnlp-main.37.pdf"
          },
          {
            "title": "Accepted Industry Track Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/ind_papers/"
          },
          {
            "title": "Reverse Prompt Engineering: A Zero-Shot, Genetic ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1333.pdf"
          },
          {
            "title": "GREATERPROMPT: A Unified, Customizable, and High- ...",
            "url": "https://aclanthology.org/2025.acl-demo.39.pdf"
          },
          {
            "title": "ZERA: Zero-init Instruction Evolving Refinement Agent",
            "url": "https://aclanthology.org/2025.emnlp-main.1190.pdf"
          },
          {
            "title": "GLiNER2: An Efficient Multi-Task Information Extraction ...",
            "url": "https://aclanthology.org/2025.emnlp-demos.10.pdf"
          },
          {
            "title": "A Category-Theoretic Approach to Neural-Symbolic Task ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.1157.pdf"
          },
          {
            "title": "Achieving Superior Intent Extraction through Decomposition",
            "url": "https://aclanthology.org/2025.emnlp-main.949.pdf"
          },
          {
            "title": "Discrete Prompt Optimization via Constrained Generation for Zero-shot Re-ranker - ACL Anthology",
            "url": "https://aclanthology.org/2023.findings-acl.61/"
          },
          {
            "title": "GRASP: Replace Redundant Layers with Adaptive ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1338.pdf"
          }
        ]
      },
      "I've performed a web search for your query about prompt optimization, schema decomposition, zero-shot NER/RE, calibration, and structured generation from 2024-2025 ACL/EMNLP conferences. Here are the relevant findings:\n\n## Key Papers and Systems Found:\n\n**Prompt Optimization and Structured Generation:**\n\n1. **GREATERPROMPT**: A unified prompt optimization tool that supports both gradient-based optimization and zero-shot optimized prompts, presented at ACL 2025.\n\n2. **ZERA** (Zero-init Instruction Evolving Refinement Agent): Develops structured prompts via principle-based optimization, published at EMNLP 2025.\n\n3. **Reverse Prompt Engineering**: A zero-shot, genetic algorithm approach presented at EMNLP 2025.\n\n**NER and Information Extraction:**\n\n4. **GLiNER2**: An efficient multi-task information extraction system for named entity recognition, published as a demo at EMNLP 2025.\n\n5. **GLiREL**: A generalist model for zero-shot relation extraction.\n\n**Schema Decomposition and Task Planning:**\n\n6. A category-theoretic approach features LLM decomposition of natural language tasks into structured specifications with verification to ensure constraint satisfaction, presented at EMNLP 2025 Findings.\n\n7. Papers on schema linking for NL-to-SQL and prompt optimization for conversational agents were accepted at EMNLP 2025 Industry Track.\n\nThese recent works demonstrate significant progress in combining prompt optimization with structured output generation, zero-shot learning capabilities, and task decomposition techniques."
    ],
    "durationSeconds": 7.305110951000009
  },
  "sourceToolAssistantUUID": "242e349b-89e7-4c6f-9c96-1d4e4ae46fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-16T00:56:17.028Z_

<details><summary>↩ Tool result · `toolu_01XYvk7kE2orpnB73RtFs35d`</summary>

```text
Web search results for query: "label confusion type confusion information extraction LLM schema complexity controlled experiment 2024 2025"

Links: [{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"ClinicalNLP 2025 The 7th Workshop on Clinical Natural Language Processing","url":"https://aclanthology.org/2025.clinicalnlp-1.pdf"},{"title":"From LLMs to Knowledge Graphs: Building Production-Ready Graph Systems in 2025 | by Claudiu Branzan | Medium","url":"https://medium.com/@claudiubranzan/from-llms-to-knowledge-graphs-building-production-ready-graph-systems-in-2025-2b4aff1ec99a"},{"title":"Few-Shot Relation Extraction via Two-Stage Knowledge- ...","url":"https://www.ijcai.org/proceedings/2025/0897.pdf"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Leveraging large language models for structured information extraction from pathology reports - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2153353925001075"},{"title":"GitHub - azminewasi/Awesome-LLMs-ICLR-24: It is a comprehensive resource hub compiling all LLM papers accepted at the International Conference on Learning Representations (ICLR) in 2024. · GitHub","url":"https://github.com/azminewasi/Awesome-LLMs-ICLR-24"},{"title":"LLM-TEXT2KG 2025: 4th International Workshop on LLM-Integrated Knowledge Graph Generation from Text (Text2KG)","url":"https://aiisc.ai/text2kg2025/"}]

I've found several highly relevant results for your search query on label confusion, type confusion, information extraction, LLM schema complexity, and controlled experiments from 2024-2025. Here are the key findings:

## Research on Confusion in LLM-based Information Extraction

The challenge in information extraction is not just choosing the correct label from a list, but instead involves generating a complex, composite structure with both correct content and valid syntax, and existing methods do not account for the model's uncertainty in generating a well-formed structure, a frequent point of failure for LLMs in IE.

A dual-level uncertainty framework tailors specifically for structured generation by decomposing uncertainty into two orthogonal dimensions: syntactic fidelity and semantic uncertainty, allowing distinction between a model that is confused about the content and one that is confused about the format.

## Schema Complexity Issues

LLMs struggle with complex schemas, exhibiting substantial performance gaps compared to traditional methods, particularly for nested entity recognition. Common error patterns include missing spans, incorrect types, and schema non-adherence, with GPT-4 showing an 11.97% invalid response rate for complex extraction tasks.

## Label and Type Confusion in Practice

When CSV-formatted metadata was input into LLMs for information extraction, the models frequently confused technical and descriptive metadata across different features, particularly when tasked with extracting a large number of features simultaneously. JSON Schema specification for JSON-formatted data allows for a structured representation of both technical and descriptive metadata, and when the metadata was provided to LLMs as JSON Schema, it significantly improved their ability to correctly process the metadata information.

These studies represent recent controlled experiments examining confusion patterns in LLM-based information extraction systems with varying schema complexity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "948b012d-dff9-4786-993e-ab4b5218badc",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "6d1c937c-1494-4877-9cd3-cfcc302acd54",
  "toolUseResult": {
    "query": "label confusion type confusion information extraction LLM schema complexity controlled experiment 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GiUCazHCzRenCSSerCKxPi",
        "content": [
          {
            "title": "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction",
            "url": "https://arxiv.org/html/2510.08623v1"
          },
          {
            "title": "Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion",
            "url": "https://arxiv.org/html/2508.10036v1"
          },
          {
            "title": "ClinicalNLP 2025 The 7th Workshop on Clinical Natural Language Processing",
            "url": "https://aclanthology.org/2025.clinicalnlp-1.pdf"
          },
          {
            "title": "From LLMs to Knowledge Graphs: Building Production-Ready Graph Systems in 2025 | by Claudiu Branzan | Medium",
            "url": "https://medium.com/@claudiubranzan/from-llms-to-knowledge-graphs-building-production-ready-graph-systems-in-2025-2b4aff1ec99a"
          },
          {
            "title": "Few-Shot Relation Extraction via Two-Stage Knowledge- ...",
            "url": "https://www.ijcai.org/proceedings/2025/0897.pdf"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for ...",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"
          },
          {
            "title": "SLOT: Structuring the Output of Large Language Models",
            "url": "https://aclanthology.org/2025.emnlp-industry.32.pdf"
          },
          {
            "title": "Leveraging large language models for structured information extraction from pathology reports - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2153353925001075"
          },
          {
            "title": "GitHub - azminewasi/Awesome-LLMs-ICLR-24: It is a comprehensive resource hub compiling all LLM papers accepted at the International Conference on Learning Representations (ICLR) in 2024. · GitHub",
            "url": "https://github.com/azminewasi/Awesome-LLMs-ICLR-24"
          },
          {
            "title": "LLM-TEXT2KG 2025: 4th International Workshop on LLM-Integrated Knowledge Graph Generation from Text (Text2KG)",
            "url": "https://aiisc.ai/text2kg2025/"
          }
        ]
      },
      "I've found several highly relevant results for your search query on label confusion, type confusion, information extraction, LLM schema complexity, and controlled experiments from 2024-2025. Here are the key findings:\n\n## Research on Confusion in LLM-based Information Extraction\n\nThe challenge in information extraction is not just choosing the correct label from a list, but instead involves generating a complex, composite structure with both correct content and valid syntax, and existing methods do not account for the model's uncertainty in generating a well-formed structure, a frequent point of failure for LLMs in IE.\n\nA dual-level uncertainty framework tailors specifically for structured generation by decomposing uncertainty into two orthogonal dimensions: syntactic fidelity and semantic uncertainty, allowing distinction between a model that is confused about the content and one that is confused about the format.\n\n## Schema Complexity Issues\n\nLLMs struggle with complex schemas, exhibiting substantial performance gaps compared to traditional methods, particularly for nested entity recognition. Common error patterns include missing spans, incorrect types, and schema non-adherence, with GPT-4 showing an 11.97% invalid response rate for complex extraction tasks.\n\n## Label and Type Confusion in Practice\n\nWhen CSV-formatted metadata was input into LLMs for information extraction, the models frequently confused technical and descriptive metadata across different features, particularly when tasked with extracting a large number of features simultaneously. JSON Schema specification for JSON-formatted data allows for a structured representation of both technical and descriptive metadata, and when the metadata was provided to LLMs as JSON Schema, it significantly improved their ability to correctly process the metadata information.\n\nThese studies represent recent controlled experiments examining confusion patterns in LLM-based information extraction systems with varying schema complexity."
    ],
    "durationSeconds": 9.084836637
  },
  "sourceToolAssistantUUID": "948b012d-dff9-4786-993e-ab4b5218badc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-16T00:56:20.428Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also check one more potentially missing reference - the "Reflect then Learn" paper seems very relevant as it explicitly studies "introspective confusion" for IE.

Let me also search for one more potential missing reference area: curriculum learning / difficulty metrics for NLP/IE based on embedding similarity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d1c937c-1494-4877-9cd3-cfcc302acd54",
  "isSidechain": false,
  "requestId": "req_011Cb5LYhvSu6sH9Ye4wWHmb",
  "type": "assistant",
  "uuid": "fa2eee19-f50f-475a-b958-55bd0b6ee938",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wbHam8yqmDt6wmHzahzAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 60184,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 241,
          "cache_read_input_tokens": 60184,
          "cache_creation_input_tokens": 3018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3018
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

_source line 61 · 2026-05-16T00:56:21.412Z_

发现了一个高度相关的遗漏文献。进一步确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa2eee19-f50f-475a-b958-55bd0b6ee938",
  "isSidechain": false,
  "requestId": "req_011Cb5LYhvSu6sH9Ye4wWHmb",
  "type": "assistant",
  "uuid": "40088d55-e5d9-416f-9181-0f322fcabf9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wbHam8yqmDt6wmHzahzAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 60184,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 241,
          "cache_read_input_tokens": 60184,
          "cache_creation_input_tokens": 3018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3018
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

_source line 62 · 2026-05-16T00:56:22.037Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VcLAcnNMj6UXVtFPLJFr5R`</summary>

```json
{
  "query": "\"Reflect then Learn\" \"Active Prompting\" \"Information Extraction\" \"Introspective Confusion\" 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40088d55-e5d9-416f-9181-0f322fcabf9a",
  "isSidechain": false,
  "requestId": "req_011Cb5LYhvSu6sH9Ye4wWHmb",
  "type": "assistant",
  "uuid": "43ae904f-106d-45f2-8b4d-c341d03893c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wbHam8yqmDt6wmHzahzAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 60184,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 241,
          "cache_read_input_tokens": 60184,
          "cache_creation_input_tokens": 3018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3018
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

_source line 63 · 2026-05-16T00:56:22.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EM8JBSx1UfmEaYHXV7zGQC`</summary>

```json
{
  "query": "structured prediction label set size effect NLP LLM type inventory scaling 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43ae904f-106d-45f2-8b4d-c341d03893c8",
  "isSidechain": false,
  "requestId": "req_011Cb5LYhvSu6sH9Ye4wWHmb",
  "type": "assistant",
  "uuid": "16e29c8a-1c94-4490-9f1e-44721f641754",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wbHam8yqmDt6wmHzahzAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 60184,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 241,
          "cache_read_input_tokens": 60184,
          "cache_creation_input_tokens": 3018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3018
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

_source line 64 · 2026-05-16T00:56:26.638Z_

<details><summary>↩ Tool result · `toolu_01VcLAcnNMj6UXVtFPLJFr5R`</summary>

```text
Web search results for query: ""Reflect then Learn" "Active Prompting" "Information Extraction" "Introspective Confusion" 2025 arXiv"

Links: [{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"[2508.10036] Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/abs/2508.10036"},{"title":"Reflect Then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40796"}]

I found the research paper you're looking for! 

"Reflect then Learn" introduces Active Prompting for Information Extraction (APIE), a novel active prompting framework guided by a principle termed introspective confusion. The paper addresses how Large Language Models show potential for few-shot information extraction, yet their performance is sensitive to in-context example selection, with conventional strategies overlooking confusion from both semantic content and generation of well-structured formats.

The method empowers an LLM to assess its own confusion through a dual-component uncertainty metric that quantifies both Format Uncertainty (difficulty in generating correct syntax) and Content Uncertainty (inconsistency in extracted semantics).

The paper demonstrates extensive empirical validation across four benchmark datasets and four LLMs, establishing a new state-of-the-art for training-free universal information extraction.

The paper was uploaded to arXiv on August 10, 2025 (arxiv ID: 2508.10036) and has since been accepted to the AAAI Conference on Artificial Intelligence (AAAI-26).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43ae904f-106d-45f2-8b4d-c341d03893c8",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "e82f67e9-e4e5-498a-83ff-442f67042c22",
  "toolUseResult": {
    "query": "\"Reflect then Learn\" \"Active Prompting\" \"Information Extraction\" \"Introspective Confusion\" 2025 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H8zKo7vig9RDRsNaDFbvWG",
        "content": [
          {
            "title": "Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion",
            "url": "https://arxiv.org/html/2508.10036v1"
          },
          {
            "title": "[2508.10036] Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion",
            "url": "https://arxiv.org/abs/2508.10036"
          },
          {
            "title": "Reflect Then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40796"
          }
        ]
      },
      "I found the research paper you're looking for! \n\n\"Reflect then Learn\" introduces Active Prompting for Information Extraction (APIE), a novel active prompting framework guided by a principle termed introspective confusion. The paper addresses how Large Language Models show potential for few-shot information extraction, yet their performance is sensitive to in-context example selection, with conventional strategies overlooking confusion from both semantic content and generation of well-structured formats.\n\nThe method empowers an LLM to assess its own confusion through a dual-component uncertainty metric that quantifies both Format Uncertainty (difficulty in generating correct syntax) and Content Uncertainty (inconsistency in extracted semantics).\n\nThe paper demonstrates extensive empirical validation across four benchmark datasets and four LLMs, establishing a new state-of-the-art for training-free universal information extraction.\n\nThe paper was uploaded to arXiv on August 10, 2025 (arxiv ID: 2508.10036) and has since been accepted to the AAAI Conference on Artificial Intelligence (AAAI-26)."
    ],
    "durationSeconds": 4.598185979000002
  },
  "sourceToolAssistantUUID": "43ae904f-106d-45f2-8b4d-c341d03893c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-16T00:56:29.635Z_

<details><summary>↩ Tool result · `toolu_01EM8JBSx1UfmEaYHXV7zGQC`</summary>

```text
Web search results for query: "structured prediction label set size effect NLP LLM type inventory scaling 2023 2024 2025"

Links: [{"title":"Large language model - Wikipedia","url":"https://en.wikipedia.org/wiki/Large_language_model"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"The best NLP papers of 2024 - The best NLP papers","url":"https://thebestnlppapers.com/nlp/papers/2024/"},{"title":"Scaling Laws for LLMs: From GPT-3 to o3","url":"https://cameronrwolfe.substack.com/p/llm-scaling-laws"},{"title":"Unlocking Complex AI Challenges with Structured Prediction and Large Language Models - David Maiolo","url":"https://www.davidmaiolo.com/2024/03/10/structured-prediction-large-language-models-ai/"},{"title":"Published in Transactions on Machine Learning Research (MM/YYYY)","url":"https://assets.amazon.science/f1/0c/5f8a587c452d9b1c687f70b731ab/large-language-models-llms-on-tabular-data-prediction-generation-and-understanding-a-survey.pdf"},{"title":"Revisiting Scaling Laws for Language Models","url":"https://aclanthology.org/2025.acl-long.1163.pdf"},{"title":"Can Pre-training Indicators Reliably Predict Fine-tuning ...","url":"https://arxiv.org/pdf/2504.12491"},{"title":"When Scale is Fixed: Revisiting Pre-training Indicators for LLM Fine-tuning Performance","url":"https://arxiv.org/html/2504.12491v2"},{"title":"LLM Model Size: 2026 Comparison Chart & Performance Guide | Label Your Data","url":"https://labelyourdata.com/articles/llm-fine-tuning/llm-model-size"}]

Based on the web search results, here's what I found related to your query about structured prediction, label set size effects, and NLP/LLM scaling:

## General LLM Scaling Research (2023-2025)

The search results reveal significant developments in LLM scaling and fine-tuning research during this period. In 2024, major labs began making their training pipelines more sophisticated by focusing on synthetic data, optimizing data mixes, using domain-specific data, and adding dedicated long-context training stages.

## Structured Prediction with LLMs

Integrating LLMs into structured prediction workflows involves utilizing these models' pre-trained knowledge bases as a foundation upon which specialized, task-specific models can be built, often entailing fine-tuning a pre-trained LLM on a smaller, domain-specific dataset. A specific example is semantic role labeling—an NLP task that involves identifying predicate-argument structures in sentences—where LLMs can be fine-tuned to understand grammatical structure and infer latent semantic relationships.

## Pre-training and Fine-tuning Performance

Recent 2024-2025 research has focused on predicting fine-tuning outcomes. While LLMs demonstrably improve on supervised fine-tuning tasks with increasing scale, the substantial costs associated with larger models strongly motivate performance optimization at a fixed size.

However, I did not find specific research in these results directly addressing the effects of label set size on structured prediction tasks in the 2023-2025 timeframe. The results focus more broadly on scaling laws, fine-tuning strategies, and general LLM development rather than the specific relationship between label set size and structured prediction performance you inquired about.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16e29c8a-1c94-4490-9f1e-44721f641754",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "201ee41f-94ab-4d9b-b419-16f4be4286c1",
  "toolUseResult": {
    "query": "structured prediction label set size effect NLP LLM type inventory scaling 2023 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013yibiddPdGPARhn8s5N6fK",
        "content": [
          {
            "title": "Large language model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Large_language_model"
          },
          {
            "title": "The State Of LLMs 2025: Progress, Progress, and Predictions",
            "url": "https://magazine.sebastianraschka.com/p/state-of-llms-2025"
          },
          {
            "title": "The best NLP papers of 2024 - The best NLP papers",
            "url": "https://thebestnlppapers.com/nlp/papers/2024/"
          },
          {
            "title": "Scaling Laws for LLMs: From GPT-3 to o3",
            "url": "https://cameronrwolfe.substack.com/p/llm-scaling-laws"
          },
          {
            "title": "Unlocking Complex AI Challenges with Structured Prediction and Large Language Models - David Maiolo",
            "url": "https://www.davidmaiolo.com/2024/03/10/structured-prediction-large-language-models-ai/"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (MM/YYYY)",
            "url": "https://assets.amazon.science/f1/0c/5f8a587c452d9b1c687f70b731ab/large-language-models-llms-on-tabular-data-prediction-generation-and-understanding-a-survey.pdf"
          },
          {
            "title": "Revisiting Scaling Laws for Language Models",
            "url": "https://aclanthology.org/2025.acl-long.1163.pdf"
          },
          {
            "title": "Can Pre-training Indicators Reliably Predict Fine-tuning ...",
            "url": "https://arxiv.org/pdf/2504.12491"
          },
          {
            "title": "When Scale is Fixed: Revisiting Pre-training Indicators for LLM Fine-tuning Performance",
            "url": "https://arxiv.org/html/2504.12491v2"
          },
          {
            "title": "LLM Model Size: 2026 Comparison Chart & Performance Guide | Label Your Data",
            "url": "https://labelyourdata.com/articles/llm-fine-tuning/llm-model-size"
          }
        ]
      },
      "Based on the web search results, here's what I found related to your query about structured prediction, label set size effects, and NLP/LLM scaling:\n\n## General LLM Scaling Research (2023-2025)\n\nThe search results reveal significant developments in LLM scaling and fine-tuning research during this period. In 2024, major labs began making their training pipelines more sophisticated by focusing on synthetic data, optimizing data mixes, using domain-specific data, and adding dedicated long-context training stages.\n\n## Structured Prediction with LLMs\n\nIntegrating LLMs into structured prediction workflows involves utilizing these models' pre-trained knowledge bases as a foundation upon which specialized, task-specific models can be built, often entailing fine-tuning a pre-trained LLM on a smaller, domain-specific dataset. A specific example is semantic role labeling—an NLP task that involves identifying predicate-argument structures in sentences—where LLMs can be fine-tuned to understand grammatical structure and infer latent semantic relationships.\n\n## Pre-training and Fine-tuning Performance\n\nRecent 2024-2025 research has focused on predicting fine-tuning outcomes. While LLMs demonstrably improve on supervised fine-tuning tasks with increasing scale, the substantial costs associated with larger models strongly motivate performance optimization at a fixed size.\n\nHowever, I did not find specific research in these results directly addressing the effects of label set size on structured prediction tasks in the 2023-2025 timeframe. The results focus more broadly on scaling laws, fine-tuning strategies, and general LLM development rather than the specific relationship between label set size and structured prediction performance you inquired about."
    ],
    "durationSeconds": 6.756136140999995
  },
  "sourceToolAssistantUUID": "16e29c8a-1c94-4490-9f1e-44721f641754",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）  **论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\" **Venue：** EMNLP 2026 Main Confer…",
  "leafUuid": "201ee41f-94ab-4d9b-b419-16f4be4286c1",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for EMNLP schema extraction paper",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Assistant

_source line 68 · 2026-05-16T00:57:06.862Z_

<details><summary>Logged reasoning block</summary>

```text
The "Reflect then Learn" paper (AAAI 2026, arXiv 2508.10036) is highly relevant but was published in August 2025, which is after the ARR May 2025 submission deadline. Since this paper is for the May 2025 ARR cycle, papers published after May 2025 wouldn't need to be cited. Actually wait, the paper's submission is for "ARR May 25 cycle" which could mean May 2025. But the current date is May 2026 according to system context. Let me re-read: "EMNLP 2026 Main Conference（ARR May 25 cycle）". 

Given that the venue is EMNLP 2026 and we're currently in May 2026, the "May 25 cycle" likely refers to a deadline around May 25, 2026, which means the August 2025 paper would definitely be available and relevant to cite.

The "Reflect then Learn" paper touches on confusion and example selection, but it's focused on uncertainty-driven active learning rather than schema type confusability specifically, so while tangentially related, it's not a critical omission.

Now I'm organizing the full review with summaries, strengths, weaknesses with severity labels, questions, missing references, and an overall assessment. I'm also calculating the page count more precisely by going through each section—the abstract, introduction with its enumerated list, related work subsections, and experimental sections.

Looking at the page breakdown, the main body appears to exceed the 8-page limit when I add up the introduction, related work, experimental setup with tables, results with multiple tables, the SDGD negative section, and conclusion. But I need to clarify the ARR submission guidelines on what counts toward the page limit and whether the limitations section is included in that count. Looking at the page count more carefully, the main body text is quite dense with five tables distributed throughout, putting the paper right around or slightly over the eight-page limit. I notice there's a citation issue to clarify—the reference key "minilm-2019" actually points to Sentence-BERT rather than the all-MiniLM-L6-v2 model, which is a separate distilled variant. Now I'm ready to write the comprehensive review. The full title is "MiniLM: Deep Self-Knowledge Distillation for Task-Agnostic Compression of Pre-Trained Transformers" by Wang et al. (2020), which is the more precise citation, though the conflation with Sentence-BERT is understandable given that all-MiniLM-L6-v2 is a sentence-transformers model. Now I'm compiling the full review after verifying all 42 bibliography entries—32 confirmed, 5 not yet indexed online (likely very recent papers), and 5 with minor author name variations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "201ee41f-94ab-4d9b-b419-16f4be4286c1",
  "isSidechain": false,
  "requestId": "req_011Cb5LZdrQM71y2yr1fSwWG",
  "type": "assistant",
  "uuid": "9672084d-8969-4bc6-b336-2ba84a974a01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t2bodDCu6u9r8em4gebSW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2575,
      "cache_read_input_tokens": 63202,
      "output_tokens": 9095,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2575,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9095,
          "cache_read_input_tokens": 63202,
          "cache_creation_input_tokens": 2575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2575
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

_source line 69 · 2026-05-16T00:59:02.594Z_

已完成论文全文阅读、官方评分标准获取、引用验证和遗漏文献搜索。现在撰写完整审稿报告。

---

## ACL ARR Review — Reviewer 2

**Paper:** "Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?"
**Venue:** EMNLP 2026 Main Conference (ARR May cycle)

---

## Summary

本文研究 training-free LLM 信息抽取中，prompt schema 的 type count 和 type confusability 如何独立影响抽取性能。作者引入 Schema Confusability Score (SCS/BCS)，设计 count curve 和 BCS-controlled 两套实验范式，在 NER/RE/ED 三个任务上隔离出 count-driven recall decline（Channel 1）和 confusability-driven type confusion（Channel 2）两条退化通道，并证明 confusability-aware decomposition 因 merge amplification 而失败。实验设计严谨，研究问题明确，但核心发现的 effect size 偏弱（pairwise r² < 2%），关键 amplification claim 依赖两点比较，且论文在呈现上存在明显缺陷（正文无 figure、无 Discussion section）。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计出色（count curve + BCS-controlled），bootstrap CI 规范。但 pairwise SCS 解释力极弱（r² < 2%），3.4× amplification 基于两点比较，中间点非独立。MAVEN 结果反向，削弱了统一叙事 |
| **Excitement** | 3/5 | 研究问题重要且先前未被系统研究，controlled experiment 的思路值得推广。但结论以描述性发现为主，缺乏可操作的方法论贡献（SDGD 失败、未提出替代方案） |
| **Overall** | 3/5 | Findings track 可接收水平。实验设计强于结论强度，呈现问题可修复但需实质工作 |
| **Confidence** | 4/5 | 熟悉 LLM-based IE 和 zero-shot extraction 文献 |
| **Reproducibility** | 4/5 | 固定 seed、报告 CI、详细描述实验配置，但代码/数据未提供 |

---

## Strengths

**S1. 实验设计精良，因果推断层次清晰。** Count curve（Experiment 1）提供 correlational evidence，BCS-controlled（Experiment 2）提供 interventional evidence，从观察到干预逐步升级。这种设计在 LLM IE 文献中属于首次，远优于先前仅报告"schema 越大性能越差"的工作（§3.3, §4.3）。

**S2. Centrality confound 的发现极有价值。** §4.5 揭示 same-domain schema（MAVEN）中 mean BCS 与 error rate 正相关这一反直觉现象，追溯到 representation degeneration 文献（Cai et al., 2021），并给出 pairwise vs. aggregated 指标使用的具体建议。这个发现对未来研究的 metric 设计有直接指导意义。

**S3. Cross-model validation 设计合理。** 在不同模型家族（Qwen3-32B vs. Llama-3.1-8B）上复现两条 channel，特别是 high-BCS accuracy 收敛到 ~51% 的 model-invariant floor（Table A2），构成了强有力的证据表明这是 task-inherent 而非 model-specific difficulty。

**S4. Negative result（SDGD）报告诚实且信息量大。** §5 系统地测试了四种 decomposition mode，明确定位 merge amplification 为瓶颈，且 confidence-gated merge 也失败。这比简单宣称"decomposition works"更有价值，为后续工作指明了 cross-batch calibration 的方向。

**S5. 相关工作覆盖广泛且定位准确。** 与 LLM-PEE 的三点区分（§2.2）清晰有力，representation degeneration 文献（§2.3）与 centrality confound 的联系有机自然。

---

## Weaknesses

**W1 [Must-Fix] 正文零 figure，关键结果缺乏视觉呈现。**
- 具体位置：main.tex §Appendix；Figure 1-3 全部在 Appendix
- 问题：Count-degradation curves（Fig 1）、BCS scaling（Fig 2）、error taxonomy（Fig 3）是论文核心发现的直接可视化，却全部放在 Appendix。正文仅有 5 张 table，读者必须反复翻到附录才能理解结果。这不仅是呈现偏好问题——EMNLP reviewer 阅读正文时无法看到论文最核心的 evidence。
- 为什么影响接收：严重降低可读性和说服力。Reviewer 评估 paper 时主要看正文 8 页，Appendix 是补充材料。
- 建议：将 Fig 1（count curves）和 Fig 2（BCS scaling）移入正文 §4.1 和 §4.3，适当压缩 Related Work 或 Experimental Setup 文字腾出空间。

**W2 [Must-Fix] Pairwise SCS 解释力极弱（r² = 1.3–1.7%），但 framing 有 overclaiming 嫌疑。**
- 具体位置：§4.2, Table 2
- 问题：Pairwise SCS 仅解释 ~1.5% 的 type confusion variance。论文将其定位为"the first factor empirically isolated in controlled zero-shot IE"（§4.2 末段），但解释力如此之低，实际 utility 存疑。后文说"the signal concentrates among types the model actually confuses (ρ = 0.27–0.31)"——这是 conditioning on the outcome（仅看非零 confusion pair），有 selection bias 风险，不能作为强化证据。
- 为什么影响接收：Contribution 2 声称"pairwise confusability as a robust predictor"，但 r² < 2% 很难称 "robust"。如果 98%+ 的 variance 来自其他因素，这一 predictor 的实际价值需要更审慎的 framing。
- 建议：(1) 将"robust predictor"改为"statistically significant but weak predictor"或类似表述；(2) 讨论什么因素可能解释剩余 98% variance（当前仅一句提及 entity frequency、prompt position、type definition quality）；(3) 对 conditioning on nonzero confusion 的 selection bias 做 explicit caveat。

**W3 [Must-Fix] 3.4× amplification 的核心 claim 基于两点比较，统计支撑不足。**
- 具体位置：§4.3, Table 3；Limitations 段
- 问题：论文最有冲击力的数字"confusability effects amplify 3.4× as schema size grows from 16 to 80 types"来自 16-rel pool（Δ = 9.1 pp，无 CI）和 80-rel pool（Δ = 31.2 pp）的比较。(a) 16-rel 条件仅用一个 extreme batch（论文承认"bootstrap CIs require multiple batches"），无法量化不确定性；(b) 中间 40-rel 点来自 80-rel pool 的子集，非独立验证；(c) Limitations 中计算的 range 1.9–4.7× 是从 80-rel CI propagate 而来，未考虑 16-rel 的不确定性（因为 16-rel 无 CI）。
- 为什么影响接收：这是 abstract、introduction、contribution 3 中反复强调的核心 finding，但其统计基础是一个无 CI 的 point estimate 和一个有 CI 的 point estimate 的比值。
- 建议：(1) 在 16-rel 条件下增加多组 batch 以获得 CI；(2) 增加 32-rel 或其他中间规模的独立 schema pool 验证 monotonic amplification；(3) 至少在正文中明确标注 16-rel Δ 无 CI 这一局限，而非仅在 Limitations 中提及。

**W4 [Should-Fix] 无 Discussion section，Conclusion 仅 1 段 5 行。**
- 具体位置：discussion.tex（实际内容为 §6 Conclusion）
- 问题：对于一篇在 3 个任务上呈现复杂、甚至矛盾结果（MAVEN 反向趋势、NER channel 交互、SDGD 失败）的论文，缺乏 Discussion section 是严重缺陷。当前 Conclusion 仅罗列发现，未讨论：(a) two-channel model 的理论解释或与 attention mechanism 的联系；(b) 对 IE pipeline 设计的具体指导；(c) SCS 作为 schema difficulty metric 的实际应用场景；(d) SDGD 失败后的具体替代方案（"cross-batch calibration or joint decoding"过于笼统）。
- 建议：增加独立 Discussion section（~0.5 页），讨论上述要点。

**W5 [Should-Fix] MAVEN ED 结果与论文主 narrative 矛盾，处理不够充分。**
- 具体位置：§4.1 ED 段落, §4.5
- 问题：论文标题问"Does Type Confusability Drive Schema-Induced Degradation?"，但 MAVEN 上 schema 增大反而提升性能。虽然 §4.5 给出 centrality confound 解释，但这本质上说明 BCS 在 same-domain schema 上失效。换言之，SCS/BCS 作为 confusability metric 的适用范围被限制在 cross-domain schema，这大幅缩小了方法的 generalizability。论文未充分讨论这一限制的影响。
- 建议：在正文中明确 SCS/BCS 的适用条件和边界，讨论 same-domain schema 的替代指标。

**W6 [Should-Fix] v1 vs v2 prompt 不一致，影响 NER 实验可比性。**
- 具体位置：§3.5
- 问题：Count-curve 和 BCS-controlled NER 实验使用 v1 prompt（96.5% offset fabrication），后续实验使用 v2 prompt（precision 翻倍）。这意味着 §4.1 NER count curves 的绝对数值在 v1 下被 inflate（over-prediction → high recall at low count），与后续 v2 实验不可直接比较。Cross-model comparison（Table A1）也承认 v1 vs v2 差异（0.72 vs 0.64 at count=1）。
- 建议：(a) 在 §4.1 开头明确标注所用 prompt 版本及其影响；(b) 如有条件，用 v2 prompt 复现 count curves 以确认趋势一致性。

**W7 [Should-Fix] Limitations section 结构差。**
- 具体位置：main.tex L36-37
- 问题：Limitations 是一个约 20 行的单一密集段落，包含至少 8 个不同 limitation，难以阅读和评估每个 limitation 的严重程度。
- 建议：用编号列表或分段组织，区分 scope limitations（单模型为主）、statistical limitations（两点比较）、metric limitations（SCS 局限性）。

**W8 [Should-Fix] `minilm-2019` 引用指向 Sentence-BERT (Reimers & Gurevych, 2019)，但实际使用的 all-MiniLM-L6-v2 并非 Sentence-BERT。**
- 具体位置：§3.2, references.bib
- 问题：all-MiniLM-L6-v2 是基于 MiniLM (Wang et al., 2020) 的 distilled 模型，在 sentence-transformers 框架下发布。引用 Sentence-BERT 论文作为 all-MiniLM-L6-v2 的来源不够准确。
- 建议：改引 MiniLM 原始论文或 sentence-transformers 工具论文。

**W9 [Minor] 缺少 Responsible NLP Research Checklist。**
- 具体位置：main.tex 全文
- 问题：ARR 要求提交 Responsible NLP Research Checklist，当前稿件中未包含。自 EMNLP 2025 起，checklist 会作为 appendix 随论文发表。
- 建议：补充 checklist。

**W10 [Minor] FewRel 数据使用非标准拆分。**
- 具体位置：§3.1 FewRel 段
- 问题：合并 training + validation split 获取 80 relation pool，test labels 不可用。这使得实验与 FewRel benchmark 的标准设置不可比。
- 建议：在 §3.1 中更显著地讨论这一非标准拆分及其对结果泛化性的影响。

**W11 [Minor] Contribution 1 用"model"描述经验分类。**
- 具体位置：§1 Contribution 1
- 问题："Multi-channel degradation model"暗示有 formal model（参数、预测），但实际是对 error types 的经验性分类。
- 建议：改为"multi-channel degradation framework"或"decomposition"。

---

## Questions for Authors

**Q1.** 16-rel BCS-controlled 条件为何仅用一个 extreme batch per BCS level？增加 batch 数以获得 CI 的技术障碍是什么？

**Q2.** MAVEN 上 pairwise SCS 仍然 predictive（r = 0.129），但 BCS aggregation 失效。是否尝试过 residualized BCS（去除 centrality component 后的 confusability）？如果有，结果如何？

**Q3.** v1 prompt 的 96.5% offset fabrication 是否影响了 model 的 type discrimination behavior（例如，model 在 fabricate offset 时是否也更容易 confuse types）？是否有 evidence 排除 prompt artifact？

**Q4.** SDGD 实验仅在 Few-NERD (NER) 上进行。鉴于 RE 上 Channel 2 更 cleanly separable，为什么不在 FewRel 上也测试 SDGD？RE 上 merge amplification 是否同样严重？

**Q5.** 论文使用 greedy decoding (temperature=0)。是否探索过 non-zero temperature + 多次采样对 type confusion 行为的影响？这可能影响 confusability channel 的强度。

---

## Missing References

1. **"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion"** (AAAI 2026, arXiv:2508.10036)——该工作显式建模 IE 中的 confusion（包括 content uncertainty 和 format uncertainty），与本文的 type confusion 分析高度相关，应在 Related Work §2.1 讨论。

2. **MiniLM 原始论文**：Wang et al. (2020), "MiniLM: Deep Self-Knowledge Distillation for Task-Agnostic Compression of Pre-Trained Transformers" (NeurIPS 2020)——当前 bib 用 Sentence-BERT 引用 all-MiniLM-L6-v2 不准确。

3. 建议考虑引用 **prompt sensitivity / prompt robustness** 相关工作（如 Sclar et al., 2024, "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design", TACL），因为 v1 vs v2 prompt 差异本身就是 prompt sensitivity 的体现。

---

## 引用验证结果

经 OpenAlex 自动验证 42 条引用：32 条 verified，5 条 minor author name format mismatch（API parsing 差异，非实质错误），5 条未找到（`dlisc-2025`, `zeroner-2025`, `gliner2-2025`, `self-prompting-re-2024`, `json-schema-bench-2025`——可能为极新 arXiv preprint 尚未索引）。无 orphan 或 missing bib entries。总体引用质量良好。

---

## Overall Assessment

**Borderline (3/5)** — 推荐 Findings track 接收，正文投稿需实质修改后可考虑主会议。

**理由：** 本文提出了一个重要且先前未被系统研究的问题（count vs. confusability 的独立效应），实验设计（controlled BCS experiments、cross-model validation）在 LLM IE 文献中是最严谨的之一。Centrality confound 和 merge amplification 的发现对后续工作有直接指导价值。

但论文的核心量化发现偏弱：pairwise predictor 的 r² < 2% 限制了其实际 utility，3.4× amplification 基于统计基础不完整的两点比较，MAVEN 上 SCS/BCS 失效限制了 generalizability。这些加上呈现层面的严重缺陷（正文无 figure、无 Discussion、单段 Conclusion）使得当前版本不具备主会议竞争力。如果 (1) 将核心 figure 移入正文、(2) 加强 16-rel CI 和 amplification claim 的统计支撑、(3) 增加 Discussion section，可上升至 weak accept 水平。

---

现在将审稿报告提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9672084d-8969-4bc6-b336-2ba84a974a01",
  "isSidechain": false,
  "requestId": "req_011Cb5LZdrQM71y2yr1fSwWG",
  "type": "assistant",
  "uuid": "3910bce6-6860-45d1-a61b-7a724f92aa39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t2bodDCu6u9r8em4gebSW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2575,
      "cache_read_input_tokens": 63202,
      "output_tokens": 9095,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2575,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9095,
          "cache_read_input_tokens": 63202,
          "cache_creation_input_tokens": 2575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2575
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

_source line 70 · 2026-05-16T00:59:32.890Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01Bts9eZ7A4SyU8gNgo9YCBZ`</summary>

```json
{
  "text": "## ACL ARR Review — Reviewer 2（新颖性与完整性）\n\n**Paper:** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\n---\n\n## Summary\n\n本文研究 training-free LLM 信息抽取中，prompt schema 的 type count 和 type confusability 如何独立影响抽取性能。作者引入 Schema Confusability Score (SCS/BCS)，设计 count curve 和 BCS-controlled 两套实验范式，在 NER/RE/ED 三个任务上隔离出 count-driven recall decline（Channel 1）和 confusability-driven type confusion（Channel 2）两条退化通道，并证明 confusability-aware decomposition 因 merge amplification 而失败。实验设计严谨，研究问题明确，但核心发现的 effect size 偏弱（pairwise r² < 2%），关键 amplification claim 依赖两点比较，且论文在呈现上存在明显缺陷（正文无 figure、无 Discussion section）。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验设计出色（count curve + BCS-controlled），bootstrap CI 规范。但 pairwise SCS 解释力极弱（r² < 2%），3.4× amplification 基于两点比较，中间点非独立。MAVEN 结果反向，削弱统一叙事 |\n| **Excitement** | 3/5 | 研究问题重要且先前未被系统研究，controlled experiment 思路值得推广。但结论以描述性发现为主，缺乏可操作的方法论贡献（SDGD 失败、未提出替代方案） |\n| **Overall** | 3/5 | Findings track 可接收水平。实验设计强于结论强度，呈现问题可修复但需实质工作 |\n| **Confidence** | 4/5 | 熟悉 LLM-based IE 和 zero-shot extraction 文献 |\n| **Reproducibility** | 4/5 | 固定 seed、报告 CI、详细描述实验配置，但代码/数据未提供 |\n\n---\n\n## Strengths\n\n**S1. 实验设计精良，因果推断层次清晰。** Count curve 提供 correlational evidence，BCS-controlled 提供 interventional evidence，逐步升级。这在 LLM IE 文献中属于首次。\n\n**S2. Centrality confound 的发现极有价值。** §4.5 揭示 same-domain schema 中 mean BCS 与 error rate 正相关的反直觉现象，追溯到 representation degeneration 文献，对后续 metric 设计有直接指导。\n\n**S3. Cross-model validation 设计合理。** 不同模型家族上复现两条 channel，特别是 high-BCS accuracy 收敛到 ~51% 的 model-invariant floor。\n\n**S4. Negative result（SDGD）报告诚实且有信息量。** 系统测试四种 decomposition mode，明确定位 merge amplification 为瓶颈。\n\n**S5. 相关工作覆盖广泛，与 LLM-PEE 的三点区分清晰有力。**\n\n---\n\n## Weaknesses\n\n**W1 [Must-Fix] 正文零 figure，关键结果缺乏视觉呈现。** Count curves、BCS scaling、error taxonomy 三张核心 figure 全在 Appendix。Reviewer 评估正文 8 页时无法看到最核心的 evidence。建议将 Fig 1 和 Fig 2 移入正文。\n\n**W2 [Must-Fix] Pairwise SCS 解释力极弱（r² = 1.3–1.7%），framing 有 overclaiming 嫌疑。** Contribution 2 声称\"robust predictor\"，但 r² < 2%。Conditioning on nonzero confusion pairs（ρ = 0.27–0.31）有 selection bias 风险。建议改为\"statistically significant but weak predictor\"，详细讨论剩余 98% variance 来源。\n\n**W3 [Must-Fix] 3.4× amplification 核心 claim 基于两点比较，统计支撑不足。** 16-rel 条件仅一个 extreme batch（无 CI），中间 40-rel 来自 80-rel pool 子集（非独立）。建议增加 16-rel 多 batch + 独立中间规模验证。\n\n**W4 [Should-Fix] 无 Discussion section，Conclusion 仅 1 段 5 行。** 对于呈现复杂、矛盾结果的论文，缺乏对 theoretical implications、practical guidelines、替代方案的讨论。\n\n**W5 [Should-Fix] MAVEN 结果与主 narrative 矛盾，SCS/BCS 适用范围被限制在 cross-domain schema，generalizability 大幅缩小。**\n\n**W6 [Should-Fix] v1 vs v2 prompt 不一致，NER count curves 使用 known-flawed v1 prompt（96.5% offset fabrication），影响可比性。**\n\n**W7 [Should-Fix] Limitations section 单段 ~20 行，结构差，难以评估各 limitation 严重程度。**\n\n**W8 [Should-Fix] `minilm-2019` 引用指向 Sentence-BERT，但实际使用 all-MiniLM-L6-v2（应引 MiniLM 原始论文）。**\n\n**W9 [Minor] 缺少 Responsible NLP Research Checklist。**\n\n**W10 [Minor] FewRel 合并 train+val split 为非标准设置，讨论不够显著。**\n\n**W11 [Minor] \"Multi-channel degradation model\"用\"model\"描述经验分类，建议改为\"framework\"。**\n\n---\n\n## Questions for Authors\n\nQ1. 16-rel 条件为何仅一个 extreme batch？增加 batch 获 CI 的技术障碍是什么？\nQ2. 是否尝试过 residualized BCS（去除 centrality component）？\nQ3. v1 prompt 的 offset fabrication 是否影响 type discrimination behavior？\nQ4. SDGD 为何仅在 NER 上测试？RE 上 merge amplification 是否同样严重？\nQ5. 是否探索过 non-zero temperature 对 type confusion 的影响？\n\n---\n\n## Missing References\n\n1. \"Reflect then Learn: Active Prompting for IE Guided by Introspective Confusion\" (AAAI 2026) — 显式建模 IE 中的 confusion，高度相关。\n2. MiniLM 原始论文 (Wang et al., 2020, NeurIPS) — 当前引用 Sentence-BERT 不准确。\n3. Prompt sensitivity 文献（如 Sclar et al., 2024, TACL）— v1 vs v2 差异本身体现 prompt sensitivity。\n\n## 引用验证\n\n42 条引用均有 bib entry 且被引用，无 orphan/missing。32 条 OpenAlex verified，5 条 author name format mismatch（非实质错误），5 条可能因极新未索引。总体引用质量良好。\n\n---\n\n## Overall Assessment\n\n**Borderline (3/5)** — 推荐 Findings track 接收，主会议需实质修改。\n\n实验设计是 LLM IE 文献中最严谨的之一，centrality confound 和 merge amplification 发现有指导价值。但 pairwise predictor r² < 2%、amplification 两点比较统计不足、MAVEN 上 metric 失效限制 generalizability，加上正文无 figure / 无 Discussion 的呈现缺陷，当前版本不具备主会议竞争力。修复 W1-W3 + W4 后可上升至 weak accept。",
  "reviewer_id": "2",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3910bce6-6860-45d1-a61b-7a724f92aa39",
  "isSidechain": false,
  "requestId": "req_011Cb5LZdrQM71y2yr1fSwWG",
  "type": "assistant",
  "uuid": "9ce9dd0e-6e4f-4119-82f9-27b3ac42fcf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t2bodDCu6u9r8em4gebSW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2575,
      "cache_read_input_tokens": 63202,
      "output_tokens": 9095,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2575,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9095,
          "cache_read_input_tokens": 63202,
          "cache_creation_input_tokens": 2575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2575
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

_source line 71_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性与完整性）  **论文：** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\" **Venue：** EMNLP 2026 Main Confer…",
  "leafUuid": "9ce9dd0e-6e4f-4119-82f9-27b3ac42fcf9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Review Round 1 for EMNLP schema extraction paper",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe"
}
```

---

### Tool result

_source line 73 · 2026-05-16T00:59:36.695Z_

<details><summary>↩ Tool result · `toolu_01Bts9eZ7A4SyU8gNgo9YCBZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ce9dd0e-6e4f-4119-82f9-27b3ac42fcf9",
  "isSidechain": false,
  "promptId": "26bafe21-e8e6-4100-b03b-b2431e032197",
  "type": "user",
  "uuid": "071bd483-51e7-4c66-a7d4-17ab105777e0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "9ce9dd0e-6e4f-4119-82f9-27b3ac42fcf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 74 · 2026-05-16T00:59:36.700Z_

```json
{
  "parentUuid": "071bd483-51e7-4c66-a7d4-17ab105777e0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f7635f50-6a60-4690-b580-c3b9bc41c669",
  "timestamp": "2026-05-16T00:59:36.700Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_reviewer_2_302b64f9",
  "sessionId": "9c06470a-a258-40d7-9ddb-7fd9ea965abe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---
