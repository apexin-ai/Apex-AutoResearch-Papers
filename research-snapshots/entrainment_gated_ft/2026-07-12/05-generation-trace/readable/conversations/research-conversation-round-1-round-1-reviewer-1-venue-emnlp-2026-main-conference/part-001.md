# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1 **你的审查侧重：方法严谨性 + 实验有效性** ### Venue 信息 - **目标**: EMNLP 2026 Main Conference  — Part 1 of 7

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-round-1-reviewer-1-venue-emnlp-2026-main-conference.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/89/896a8f0544b5fc0e6dc7.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-14T13:01:56.107Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T13:01:56.107Z",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "content": "[Round 1 审稿请求]:\n## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验有效性**\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference\n- **Deadline**: 2026-05-25 (ARR submission)\n- **格式**: ACL 模板, 正文 ≤8 页, mandatory Limitations section, double-blind\n- **附录**: 允许，不计入页数限制，审稿人可选择性参考\n\n### 论文路径\n`projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n\n### 论文概要\n论文研究 hardware-aligned bit-widths {2,4,8,16} 下 per-head KV cache mixed-precision quantization 的问题。核心发现：unconstrained solvers 在该 bit-width 集上 catastrophically fail（Qwen2.5-7B 上 PPL 32-37 vs uniform 4-bit 15.45），原因是 2-bit distortion compounding。提出 cardinality constraint 限制 2-bit head 数量（k≤8），将 PPL 降至 11.23。进一步发现 constrained 条件下 greedy 和 MCKP solver 等价。提出基于 top-5% concentration 的 heterogeneity diagnostic 判断模型是否适合 non-uniform allocation。在 3 个 7B 模型上验证。\n\n### 你需要重点审查的方面\n\n1. **方法 formulation 严谨性**：\n   - MCKP formulation 是否正确？cardinality constraint 的数学表述是否严格？\n   - \"2-bit distortion compounding\" 的解释是否有理论支撑还是仅凭经验？\"non-additive through residual stream\" 的论证是否充分？\n   - Solver equivalence claim（greedy = MCKP under constraint）是否有证明还是仅靠实验验证？\n\n2. **实验设计**：\n   - 仅 3 个 7B 模型是否足够支撑论文 claims？\n   - Evaluation metrics 是否充分（仅 PPL + 4 downstream tasks）？\n   - Calibration data (WikiText-2 train) 与 evaluation data (WikiText-2 test) 来自同一分布——是否有 data leakage 风险？\n   - Profiling setup（独立量化每个 head）的计算成本是否报告？\n   - k 的选择（sweep on calibration data）是否存在 overfitting 风险？\n\n3. **统计可靠性**：\n   - 主要结果是否报告 confidence intervals / error bars？\n   - Multi-seed 实验只在 Qwen hires profiling 上做了 3 seeds，是否足够？\n   - Cross-dataset 实验是否充分验证了 generalization？\n\n4. **Baseline 完整性**：\n   - 是否遗漏了重要的 baseline（如 token-level mixed-precision methods like ZipCache, KIVI 的 per-channel 策略）？\n   - Unconstrained results for Llama/Mistral 被省略是否合理？\n\n5. **格式合规**：\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否存在且充分？\n   - 匿名性是否满足？\n\n请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment（评分 + 置信度）。"
}
```

---


### Runtime record

_source line 2 · 2026-05-14T13:01:56.111Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T13:01:56.111Z",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


## Round 1

## Round 1

79 recorded events


### User

_source line 3 · 2026-05-14T13:01:56.144Z_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验有效性**

### Venue 信息
- **目标**: EMNLP 2026 Main Conference
- **Deadline**: 2026-05-25 (ARR submission)
- **格式**: ACL 模板, 正文 ≤8 页, mandatory Limitations section, double-blind
- **附录**: 允许，不计入页数限制，审稿人可选择性参考

### 论文路径
`projects/ratekv/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）

### 论文概要
论文研究 hardware-aligned bit-widths {2,4,8,16} 下 per-head KV cache mixed-precision quantization 的问题。核心发现：unconstrained solvers 在该 bit-width 集上 catastrophically fail（Qwen2.5-7B 上 PPL 32-37 vs uniform 4-bit 15.45），原因是 2-bit distortion compounding。提出 cardinality constraint 限制 2-bit head 数量（k≤8），将 PPL 降至 11.23。进一步发现 constrained 条件下 greedy 和 MCKP solver 等价。提出基于 top-5% concentration 的 heterogeneity diagnostic 判断模型是否适合 non-uniform allocation。在 3 个 7B 模型上验证。

### 你需要重点审查的方面

1. **方法 formulation 严谨性**：
   - MCKP formulation 是否正确？cardinality constraint 的数学表述是否严格？
   - "2-bit distortion compounding" 的解释是否有理论支撑还是仅凭经验？"non-additive through residual stream" 的论证是否充分？
   - Solver equivalence claim（greedy = MCKP under constraint）是否有证明还是仅靠实验验证？

2. **实验设计**：
   - 仅 3 个 7B 模型是否足够支撑论文 claims？
   - Evaluation metrics 是否充分（仅 PPL + 4 downstream tasks）？
   - Calibration data (WikiText-2 train) 与 evaluation data (WikiText-2 test) 来自同一分布——是否有 data leakage 风险？
   - Profiling setup（独立量化每个 head）的计算成本是否报告？
   - k 的选择（sweep on calibration data）是否存在 overfitting 风险？

3. **统计可靠性**：
   - 主要结果是否报告 confidence intervals / error bars？
   - Multi-seed 实验只在 Qwen hires profiling 上做了 3 seeds，是否足够？
   - Cross-dataset 实验是否充分验证了 generalization？

4. **Baseline 完整性**：
   - 是否遗漏了重要的 baseline（如 token-level mixed-precision methods like ZipCache, KIVI 的 per-channel 策略）？
   - Unconstrained results for Llama/Mistral 被省略是否合理？

5. **格式合规**：
   - 页数是否符合 8 页限制？
   - Limitations section 是否存在且充分？
   - 匿名性是否满足？

请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "d0b16fc9-1da2-45b2-9b95-d7df88931abd",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-14T13:01:56.143Z_

```json
{
  "parentUuid": "d0b16fc9-1da2-45b2-9b95-d7df88931abd",
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
  "uuid": "a8aebd22-c44c-4f52-9cc2-271f02a8760a",
  "timestamp": "2026-05-14T13:01:56.143Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 5 · 2026-05-14T13:01:56.143Z_

```json
{
  "parentUuid": "a8aebd22-c44c-4f52-9cc2-271f02a8760a",
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
  "uuid": "4d54829d-e6a7-4f49-8145-c02793b24d07",
  "timestamp": "2026-05-14T13:01:56.143Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 6 · 2026-05-14T13:01:56.143Z_

```json
{
  "parentUuid": "4d54829d-e6a7-4f49-8145-c02793b24d07",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0c514214-debe-4be8-be25-f0ef7491e0cc",
  "timestamp": "2026-05-14T13:01:56.143Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP paper on KV cache mixed-precision quantization",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


### Assistant

_source line 8 · 2026-05-14T13:01:59.668Z_

我开始执行 Round 1 审稿任务。首先搜索 EMNLP 2026 / ACL ARR 的官方 reviewer guidelines，然后阅读论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c514214-debe-4be8-be25-f0ef7491e0cc",
  "isSidechain": false,
  "requestId": "req_011Cb2WGL6zZ5BHLsPH3uXjQ",
  "type": "assistant",
  "uuid": "0f1ac1fa-6ac4-4020-8ff6-caea8b4bce47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017iN5T7ykhkf7JPveegTw7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14563,
      "cache_read_input_tokens": 11841,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 417,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14563
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

_source line 9 · 2026-05-14T13:02:04.128Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BmL6bTxrJtWTNB4EHpqZJe`</summary>

```json
{
  "description": "Search EMNLP reviewer guidelines",
  "subagent_type": "Explore",
  "prompt": "Search the web for the official ACL ARR (ACL Rolling Review) reviewer guidelines and review form criteria for 2025-2026. I need:\n1. The exact scoring dimensions and their scales (e.g., soundness, excitement/novelty, reproducibility, etc.)\n2. The review form structure (what sections reviewers must fill out)\n3. Any specific criteria for EMNLP 2026 or the latest ARR cycle\n\nUse WebSearch to find:\n- \"ACL ARR review form 2025 2026\"\n- \"ACL Rolling Review reviewer guidelines criteria\"\n- \"EMNLP 2026 reviewer guidelines\"\n\nReturn the full scoring rubric with scale descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f1ac1fa-6ac4-4020-8ff6-caea8b4bce47",
  "isSidechain": false,
  "requestId": "req_011Cb2WGL6zZ5BHLsPH3uXjQ",
  "type": "assistant",
  "uuid": "398f35c1-2765-4d74-970d-f7f046819ec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017iN5T7ykhkf7JPveegTw7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14563,
      "cache_read_input_tokens": 11841,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 417,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14563
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

_source line 10 · 2026-05-14T13:02:04.943Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013hT4XAAWfTxW7JMk9pTFpZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "398f35c1-2765-4d74-970d-f7f046819ec8",
  "isSidechain": false,
  "requestId": "req_011Cb2WGL6zZ5BHLsPH3uXjQ",
  "type": "assistant",
  "uuid": "4493e9d1-2f2d-4941-93ca-52e72b9a6975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017iN5T7ykhkf7JPveegTw7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14563,
      "cache_read_input_tokens": 11841,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 417,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14563
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

_source line 11 · 2026-05-14T13:02:04.947Z_

<details><summary>↩ Tool result · `toolu_013hT4XAAWfTxW7JMk9pTFpZ`</summary>

````text
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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4493e9d1-2f2d-4941-93ca-52e72b9a6975",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "aac58a71-d13e-4a2e-aa18-32abf79f2f60",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references",
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "4493e9d1-2f2d-4941-93ca-52e72b9a6975",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-14T13:04:01.242Z_

<details><summary>↩ Tool result · `toolu_01BmL6bTxrJtWTNB4EHpqZJe`</summary>

```text
Based on all my research, I have gathered comprehensive information about the ACL ARR reviewer guidelines and scoring rubrics for 2025-2026. Here's what I found:

## OFFICIAL ACL ARR REVIEWER SCORING RUBRICS FOR 2025-2026

### Scoring Dimensions Overview

As of February 2025, ARR reviewers provide **three primary scores**:

1. **Soundness** (1-5 scale with half-points)
2. **Excitement** (1-5 scale with half-points)
3. **Overall Assessment/Recommendation** (1-5 scale with half-points)

### Complete Scoring Scales

#### SOUNDNESS SCALE (1-5)
- **5 - Excellent:** "This study is one of the most thorough I have seen, given its type."
- **4 - Strong:** "This study provides sufficient support for all of its claims/arguments."
- **3 - Acceptable/Good:** "This study provides sufficient support for its major claims/arguments, some minor points may need extra support."
- **2 - Borderline:** "Some of the main claims/arguments are not sufficiently supported, there are major technical/methodological problems."
- **1 - Poor/Major Issues:** "This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

**Key Requirement:** Soundness scores must be justified by the text of the review.

#### EXCITEMENT SCALE (1-5)
- **5 - Highly Exciting/Transformative:** "This paper is likely to change its subfield or computational linguistics broadly" OR "I would recommend this paper to others and/or attend its presentation in a conference."
- **4 - Exciting/Strong:** "It changed my thinking on this topic. I would fight for it to be accepted." OR "I would mention this paper to others and/or make an effort to attend its presentation in a conference."
- **3 - Ambivalent/Leaning Positive:** Work is worthy but "not particularly interesting and/or novel."
- **2 - Leaning Negative/Mediocre:** "I am leaning towards rejection, but I can be persuaded." OR "This paper makes marginal contributions."
- **1 - Not Exciting/Poor:** "This paper does not resonate with me, and I don't think it would with others in the *ACL community (e.g., it is in no way related to computational processing of language)."

**Key Requirement:** Excitement is subjective and does not necessarily follow what is popular in the field. Papers may be perceived as exciting because they present conceptual breakthroughs, challenge common assumptions, or have possible impact on communities.

#### OVERALL ASSESSMENT/RECOMMENDATION SCALE (1-5)
- **5 - Consider for Award:** "I think this paper could be considered for an outstanding paper award at an *ACL conference" (top 2.5% papers)
- **4 - Conference:** "I think this paper could be accepted to an *ACL conference"
- **3 - Findings:** "I think this paper could be accepted to the Findings of the ACL"
- **2 - Resubmit Next Cycle:** "I think this paper needs substantial revisions that can be completed by the next ARR cycle"
- **1.5 - Resubmit After Next Cycle:** "I think this paper needs substantial revisions that cannot be completed by the next ARR cycle"
- **1 - Do Not Resubmit:** "This paper has to be fully redone, or it is not relevant to the *ACL community"

**Key Requirement:** This is a composite score reflecting soundness, excitement, novelty, and other impact factors.

### Review Form Structure

**Mandatory Narrative Sections:**
1. Paper Summary
2. Summary of Strengths (major reasons for publication)
3. Summary of Weaknesses (numbered)
4. Comments/Suggestions/Typos

**Additional Assessment Sections:**
5. Limitations and Societal Impact
6. Ethical Concerns (assessed against ACL code of ethics)
7. Needs Ethics Review (determination if special review required)
8. Reproducibility (ability to replicate results)
9. Datasets (value of released datasets, if applicable)
10. Software (value of released code, if applicable)
11. Knowledge of Author Identity (potential identifying information)
12. Best Paper Justification (for award-level recommendations only)

### Additional Scoring Categories in the Review Form

- **Reproducibility** (1-5 scale): Assesses whether there is enough information in the paper for a reader to reproduce the main results
- **Datasets** (1-5 scale): Rates value of released datasets
- **Software** (1-5 scale): Rates value of released code
- **Reviewer Confidence** (mentioned in some cycles): Assesses familiarity with the topic

### EMNLP 2026 Specifics

- EMNLP 2026 uses **ACL Rolling Review (ARR) as the reviewing system**
- Final decisions are made by the EMNLP conference
- Review deadlines: Reviews completed by July 6; meta-reviews by July 29
- Submission and review via OpenReview platform
- Double-blind review process maintained
- All authors expected to sign up as reviewers or serve as Area Chairs/Senior Area Chairs

### Key Reviewer Standards

- Preserve double-blind review: reviewers should not actively try to discover author identity
- Do not let suspicion of author identity affect judgment
- Assess both soundness (technical rigor) and excitement (subjective value) separately
- Provide substantive evidence for all scores
- Follow ACL Code of Ethics

---

Sources:
- [ARR Reviewer Guidelines](http://aclrollingreview.org/reviewerguidelines)
- [Review Form](http://aclrollingreview.org/reviewform)
- [ARR Area Chair Guidelines](http://aclrollingreview.org/acguidelines)
- [How ARR works](http://aclrollingreview.org/reviewing)
- [ACL 2023 Review Form](https://2023.aclweb.org/blog/review-form/)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Rolling Review Main Site](http://aclrollingreview.org/)
- [ARR 2025 May OpenReview](https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "398f35c1-2765-4d74-970d-f7f046819ec8",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "e9a6409f-7f62-4dac-8140-e48f2816f41e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the official ACL ARR (ACL Rolling Review) reviewer guidelines and review form criteria for 2025-2026. I need:\n1. The exact scoring dimensions and their scales (e.g., soundness, excitement/novelty, reproducibility, etc.)\n2. The review form structure (what sections reviewers must fill out)\n3. Any specific criteria for EMNLP 2026 or the latest ARR cycle\n\nUse WebSearch to find:\n- \"ACL ARR review form 2025 2026\"\n- \"ACL Rolling Review reviewer guidelines criteria\"\n- \"EMNLP 2026 reviewer guidelines\"\n\nReturn the full scoring rubric with scale descriptions.",
    "agentId": "ab4b9927defdd3125",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on all my research, I have gathered comprehensive information about the ACL ARR reviewer guidelines and scoring rubrics for 2025-2026. Here's what I found:\n\n## OFFICIAL ACL ARR REVIEWER SCORING RUBRICS FOR 2025-2026\n\n### Scoring Dimensions Overview\n\nAs of February 2025, ARR reviewers provide **three primary scores**:\n\n1. **Soundness** (1-5 scale with half-points)\n2. **Excitement** (1-5 scale with half-points)\n3. **Overall Assessment/Recommendation** (1-5 scale with half-points)\n\n### Complete Scoring Scales\n\n#### SOUNDNESS SCALE (1-5)\n- **5 - Excellent:** \"This study is one of the most thorough I have seen, given its type.\"\n- **4 - Strong:** \"This study provides sufficient support for all of its claims/arguments.\"\n- **3 - Acceptable/Good:** \"This study provides sufficient support for its major claims/arguments, some minor points may need extra support.\"\n- **2 - Borderline:** \"Some of the main claims/arguments are not sufficiently supported, there are major technical/methodological problems.\"\n- **1 - Poor/Major Issues:** \"This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL.\"\n\n**Key Requirement:** Soundness scores must be justified by the text of the review.\n\n#### EXCITEMENT SCALE (1-5)\n- **5 - Highly Exciting/Transformative:** \"This paper is likely to change its subfield or computational linguistics broadly\" OR \"I would recommend this paper to others and/or attend its presentation in a conference.\"\n- **4 - Exciting/Strong:** \"It changed my thinking on this topic. I would fight for it to be accepted.\" OR \"I would mention this paper to others and/or make an effort to attend its presentation in a conference.\"\n- **3 - Ambivalent/Leaning Positive:** Work is worthy but \"not particularly interesting and/or novel.\"\n- **2 - Leaning Negative/Mediocre:** \"I am leaning towards rejection, but I can be persuaded.\" OR \"This paper makes marginal contributions.\"\n- **1 - Not Exciting/Poor:** \"This paper does not resonate with me, and I don't think it would with others in the *ACL community (e.g., it is in no way related to computational processing of language).\"\n\n**Key Requirement:** Excitement is subjective and does not necessarily follow what is popular in the field. Papers may be perceived as exciting because they present conceptual breakthroughs, challenge common assumptions, or have possible impact on communities.\n\n#### OVERALL ASSESSMENT/RECOMMENDATION SCALE (1-5)\n- **5 - Consider for Award:** \"I think this paper could be considered for an outstanding paper award at an *ACL conference\" (top 2.5% papers)\n- **4 - Conference:** \"I think this paper could be accepted to an *ACL conference\"\n- **3 - Findings:** \"I think this paper could be accepted to the Findings of the ACL\"\n- **2 - Resubmit Next Cycle:** \"I think this paper needs substantial revisions that can be completed by the next ARR cycle\"\n- **1.5 - Resubmit After Next Cycle:** \"I think this paper needs substantial revisions that cannot be completed by the next ARR cycle\"\n- **1 - Do Not Resubmit:** \"This paper has to be fully redone, or it is not relevant to the *ACL community\"\n\n**Key Requirement:** This is a composite score reflecting soundness, excitement, novelty, and other impact factors.\n\n### Review Form Structure\n\n**Mandatory Narrative Sections:**\n1. Paper Summary\n2. Summary of Strengths (major reasons for publication)\n3. Summary of Weaknesses (numbered)\n4. Comments/Suggestions/Typos\n\n**Additional Assessment Sections:**\n5. Limitations and Societal Impact\n6. Ethical Concerns (assessed against ACL code of ethics)\n7. Needs Ethics Review (determination if special review required)\n8. Reproducibility (ability to replicate results)\n9. Datasets (value of released datasets, if applicable)\n10. Software (value of released code, if applicable)\n11. Knowledge of Author Identity (potential identifying information)\n12. Best Paper Justification (for award-level recommendations only)\n\n### Additional Scoring Categories in the Review Form\n\n- **Reproducibility** (1-5 scale): Assesses whether there is enough information in the paper for a reader to reproduce the main results\n- **Datasets** (1-5 scale): Rates value of released datasets\n- **Software** (1-5 scale): Rates value of released code\n- **Reviewer Confidence** (mentioned in some cycles): Assesses familiarity with the topic\n\n### EMNLP 2026 Specifics\n\n- EMNLP 2026 uses **ACL Rolling Review (ARR) as the reviewing system**\n- Final decisions are made by the EMNLP conference\n- Review deadlines: Reviews completed by July 6; meta-reviews by July 29\n- Submission and review via OpenReview platform\n- Double-blind review process maintained\n- All authors expected to sign up as reviewers or serve as Area Chairs/Senior Area Chairs\n\n### Key Reviewer Standards\n\n- Preserve double-blind review: reviewers should not actively try to discover author identity\n- Do not let suspicion of author identity affect judgment\n- Assess both soundness (technical rigor) and excitement (subjective value) separately\n- Provide substantive evidence for all scores\n- Follow ACL Code of Ethics\n\n---\n\nSources:\n- [ARR Reviewer Guidelines](http://aclrollingreview.org/reviewerguidelines)\n- [Review Form](http://aclrollingreview.org/reviewform)\n- [ARR Area Chair Guidelines](http://aclrollingreview.org/acguidelines)\n- [How ARR works](http://aclrollingreview.org/reviewing)\n- [ACL 2023 Review Form](https://2023.aclweb.org/blog/review-form/)\n- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [ACL Rolling Review Main Site](http://aclrollingreview.org/)\n- [ARR 2025 May OpenReview](https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay)"
      }
    ],
    "totalDurationMs": 117106,
    "totalTokens": 35228,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 33116,
      "output_tokens": 1558,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 553
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1558,
          "cache_read_input_tokens": 33116,
          "cache_creation_input_tokens": 553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 553,
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
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "398f35c1-2765-4d74-970d-f7f046819ec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 13 · 2026-05-14T13:04:05.538Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the ARR review guidelines and the tools loaded. Now I need to read the paper. Let me start by reading the main tex file and all its component files to understand the full paper. I also need to check the PDF for visual inspection and verify references.

Let me read the paper files and render the PDF in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9a6409f-7f62-4dac-8140-e48f2816f41e",
  "isSidechain": false,
  "requestId": "req_011Cb2WRZ1ssGZ8KnvhGYxz1",
  "type": "assistant",
  "uuid": "d6a8610d-740a-4c30-93cc-1171fe049a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PgoUVbgrQ6KeQPPK2ykzWP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4009,
      "cache_read_input_tokens": 26404,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 26404,
          "cache_creation_input_tokens": 4009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4009
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

_source line 14 · 2026-05-14T13:04:06.079Z_

已获取 ACL ARR 评审标准。现在开始阅读论文全文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6a8610d-740a-4c30-93cc-1171fe049a78",
  "isSidechain": false,
  "requestId": "req_011Cb2WRZ1ssGZ8KnvhGYxz1",
  "type": "assistant",
  "uuid": "73fd91a9-c601-4bba-8e74-43fa1abe5b68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PgoUVbgrQ6KeQPPK2ykzWP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4009,
      "cache_read_input_tokens": 26404,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 26404,
          "cache_creation_input_tokens": 4009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4009
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

_source line 15 · 2026-05-14T13:04:08.070Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HFFnUar1owdaGHK3XqExZV`</summary>

```json
{
  "pattern": "**/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73fd91a9-c601-4bba-8e74-43fa1abe5b68",
  "isSidechain": false,
  "requestId": "req_011Cb2WRZ1ssGZ8KnvhGYxz1",
  "type": "assistant",
  "uuid": "f36ec29c-2359-4a6f-bd97-311e37353457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PgoUVbgrQ6KeQPPK2ykzWP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4009,
      "cache_read_input_tokens": 26404,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 26404,
          "cache_creation_input_tokens": 4009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4009
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

_source line 16 · 2026-05-14T13:04:08.395Z_

<details><summary>↩ Tool result · `toolu_01Knq9V8zFs6uFgspc9xRHr4`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a86b37f-a1e8-4235-ae50-c07c4fa08a4c",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "10f7f16b-0fb8-41d2-91d8-2f41baa6da08",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
    ],
    "durationMs": 14,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7a86b37f-a1e8-4235-ae50-c07c4fa08a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-14T13:04:08.097Z_

<details><summary>↩ Tool result · `toolu_01HFFnUar1owdaGHK3XqExZV`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f36ec29c-2359-4a6f-bd97-311e37353457",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "0840d43f-2d73-440f-bae3-88dce31afab9",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
    ],
    "durationMs": 18,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "f36ec29c-2359-4a6f-bd97-311e37353457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-14T13:04:08.377Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Knq9V8zFs6uFgspc9xRHr4`</summary>

```json
{
  "pattern": "**/docs/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0840d43f-2d73-440f-bae3-88dce31afab9",
  "isSidechain": false,
  "requestId": "req_011Cb2WRZ1ssGZ8KnvhGYxz1",
  "type": "assistant",
  "uuid": "7a86b37f-a1e8-4235-ae50-c07c4fa08a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PgoUVbgrQ6KeQPPK2ykzWP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4009,
      "cache_read_input_tokens": 26404,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 26404,
          "cache_creation_input_tokens": 4009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4009
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference - **Deadline**: 2026-05-25 (ARR submission) - **格式**: ACL 模板, 正文 ≤8 页, mandato…",
  "leafUuid": "10f7f16b-0fb8-41d2-91d8-2f41baa6da08",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP paper on KV cache mixed-precision quantization",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


### Tool call

_source line 21 · 2026-05-14T13:04:12.002Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YBT4sXyHgvcRBCE2BMsRhA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10f7f16b-0fb8-41d2-91d8-2f41baa6da08",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "01a3ce74-9ea5-4e18-a2e1-c8473c5bc95e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 22 · 2026-05-14T13:04:12.016Z_

<details><summary>↩ Tool result · `toolu_01YBT4sXyHgvcRBCE2BMsRhA`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	
11	\title{When Does Non-Uniform KV Cache Quantization Help?\\Cardinality Constraints and a Heterogeneity Diagnostic}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	\input{abstract}
20	\end{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{experiments}
26	\input{analysis}
27	\input{conclusion}
28	
29	\bibliography{references}
30	
31	\input{appendix}
32	
33	\end{document}
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01a3ce74-9ea5-4e18-a2e1-c8473c5bc95e",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "6902cfce-29ab-469f-a394-89bef8a7e3f6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\n\\title{When Does Non-Uniform KV Cache Quantization Help?\\\\Cardinality Constraints and a Heterogeneity Diagnostic}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{analysis}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "01a3ce74-9ea5-4e18-a2e1-c8473c5bc95e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-14T13:04:12.429Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UoMAUxmnM5BAyKGXYQCZPW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6902cfce-29ab-469f-a394-89bef8a7e3f6",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "d04e2809-6612-459f-bdff-3d50d303d112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 24 · 2026-05-14T13:04:16.260Z_

<details><summary>↩ Tool result · `toolu_01783EsWFqc236ZZctpeU7Di`</summary>

```text
1	% Auto-generated from literature_map.yaml (verified=true entries)
2	
3	@inproceedings{liu2024kivi,
4	  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
5	  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
6	  year = {2024},
7	  booktitle = {ICML 2024},
8	  url = {https://arxiv.org/abs/2402.02750},
9	}
10	
11	@inproceedings{hooper2024kvquant,
12	  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
13	  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},
14	  year = {2024},
15	  booktitle = {NeurIPS 2024},
16	  url = {https://arxiv.org/abs/2401.18079},
17	}
18	
19	@inproceedings{lin2024qserve,
20	  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
21	  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},
22	  year = {2025},
23	  booktitle = {MLSys 2025},
24	  url = {https://arxiv.org/abs/2405.04532},
25	}
26	
27	@inproceedings{he2024zipcache,
28	  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},
29	  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},
30	  year = {2024},
31	  booktitle = {NeurIPS 2024},
32	  url = {https://arxiv.org/abs/2405.14256},
33	}
34	
35	@misc{kang2024gear,
36	  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},
37	  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},
38	  year = {2024},
39	  note = {arXiv preprint},
40	  url = {https://arxiv.org/abs/2403.05527},
41	  eprint = {2403.05527},
42	  archivePrefix = {arXiv},
43	}
44	
45	@misc{duanmu2024skvq,
46	  title = {{SKVQ}: Sliding-window Key and Value Cache Quantization for Large Language Models},
47	  author = {Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zhang and Dahua Lin},
48	  year = {2024},
49	  note = {arXiv preprint},
50	  url = {https://arxiv.org/abs/2405.06219},
51	  eprint = {2405.06219},
52	  archivePrefix = {arXiv},
53	}
54	
55	@inproceedings{zhang2023h2o,
56	  title = {{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
57	  author = {Zhenyu Zhang and Ying Sheng and Tianyi Zhou and Tianlong Chen and Lianmin Zheng and Ruisi Cai and Zhao Song and Yuandong Tian and Christopher R{\'{e}} and Clark Barrett and Zhangyang Wang and Beidi Chen},
58	  year = {2023},
59	  booktitle = {NeurIPS 2023},
60	  url = {https://arxiv.org/abs/2306.14048},
61	}
62	
63	@inproceedings{li2024snapkv,
64	  title = {{SnapKV}: {LLM} Knows What You are Looking for Before Generation},
65	  author = {Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locatelli and Hanchen Ye and Tianle Cai and Patrick Lewis and Deming Chen},
66	  year = {2024},
67	  booktitle = {NeurIPS 2024},
68	  url = {https://arxiv.org/abs/2404.14469},
69	}
70	
71	@inproceedings{ge2024fastgen,
72	  title = {Model Tells You What to Discard: Adaptive {KV} Cache Compression for {LLMs}},
73	  author = {Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianfeng Gao},
74	  year = {2024},
75	  booktitle = {ICLR 2024},
76	  url = {https://arxiv.org/abs/2310.01801},
77	}
78	
79	@inproceedings{xiao2024streamingllm,
80	  title = {Efficient Streaming Language Models with Attention Sinks},
81	  author = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},
82	  year = {2024},
83	  booktitle = {ICLR 2024},
84	  url = {https://arxiv.org/abs/2309.17453},
85	}
86	
87	@inproceedings{liu2024scissorhands,
88	  title = {Scissorhands: Exploiting the Persistence of Importance Hypothesis for {LLM} {KV} Cache Compression at Test Time},
89	  author = {Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie and Zhaozhuo Xu and Anastasios Kyrillidis and Anshumali Shrivastava},
90	  year = {2023},
91	  booktitle = {NeurIPS 2023},
92	  url = {https://arxiv.org/abs/2305.17118},
93	}
94	
95	@inproceedings{yang2024pyramidinfer,
96	  title = {{PyramidInfer}: Pyramid {KV} Cache Compression for High-throughput {LLM} Inference},
97	  author = {Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zhao},
98	  year = {2024},
99	  booktitle = {Findings of ACL 2024},
100	  url = {https://arxiv.org/abs/2405.12532},
101	}
102	
103	@misc{zuo2026ratequant,
104	  title = {{RateQuant}: Optimal Mixed-Precision {KV} Cache Quantization via Rate-Distortion Theory},
105	  author = {Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung},
106	  year = {2026},
107	  note = {arXiv preprint},
108	  url = {https://arxiv.org/abs/2605.06675},
109	  eprint = {2605.06675},
110	  archivePrefix = {arXiv},
111	}
112	
113	@misc{lei2026arkv,
114	  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},
115	  author = {Jianlong Lei and Shashikant Ilager},
116	  year = {2026},
117	  note = {arXiv preprint},
118	  url = {https://arxiv.org/abs/2603.08727},
119	  eprint = {2603.08727},
120	  archivePrefix = {arXiv},
121	}
122	
123	@misc{li2025kvmix,
124	  title = {{KVmix}: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for {KV} Cache},
125	  author = {Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang},
126	  year = {2025},
127	  note = {arXiv preprint},
128	  url = {https://arxiv.org/abs/2506.08018},
129	  eprint = {2506.08018},
130	  archivePrefix = {arXiv},
131	}
132	
133	@misc{zhang2025mixkvq,
134	  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},
135	  author = {Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen},
136	  year = {2025},
137	  note = {arXiv preprint},
138	  url = {https://arxiv.org/abs/2512.19206},
139	  eprint = {2512.19206},
140	  archivePrefix = {arXiv},
141	}
142	
143	@inproceedings{kim2024squeezellm,
144	  title = {{SqueezeLLM}: Dense-and-Sparse Quantization},
145	  author = {Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sheng Shen and Michael W. Mahoney and Kurt Keutzer},
146	  year = {2024},
147	  booktitle = {ICML 2024},
148	  url = {https://arxiv.org/abs/2306.07629},
149	}
150	
151	@inproceedings{voita2019analyzing,
152	  title = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
153	  author = {Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov},
154	  year = {2019},
155	  booktitle = {ACL 2019},
156	  url = {https://arxiv.org/abs/1905.09418},
157	}
158	
159	@inproceedings{michel2019sixteen,
160	  title = {Are Sixteen Heads Really Better than One?},
161	  author = {Paul Michel and Omer Levy and Graham Neubig},
162	  year = {2019},
163	  booktitle = {NeurIPS 2019},
164	  url = {https://arxiv.org/abs/1905.10650},
165	}
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9618d9b7-392a-4118-a89e-e7c27089b574",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "9695e153-21a8-469d-86eb-1874e035ab71",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml (verified=true entries)\n\n@inproceedings{liu2024kivi,\n  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},\n  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2402.02750},\n}\n\n@inproceedings{hooper2024kvquant,\n  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},\n  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2401.18079},\n}\n\n@inproceedings{lin2024qserve,\n  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},\n  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},\n  year = {2025},\n  booktitle = {MLSys 2025},\n  url = {https://arxiv.org/abs/2405.04532},\n}\n\n@inproceedings{he2024zipcache,\n  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},\n  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2405.14256},\n}\n\n@misc{kang2024gear,\n  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},\n  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2403.05527},\n  eprint = {2403.05527},\n  archivePrefix = {arXiv},\n}\n\n@misc{duanmu2024skvq,\n  title = {{SKVQ}: Sliding-window Key and Value Cache Quantization for Large Language Models},\n  author = {Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zhang and Dahua Lin},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2405.06219},\n  eprint = {2405.06219},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{zhang2023h2o,\n  title = {{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author = {Zhenyu Zhang and Ying Sheng and Tianyi Zhou and Tianlong Chen and Lianmin Zheng and Ruisi Cai and Zhao Song and Yuandong Tian and Christopher R{\\'{e}} and Clark Barrett and Zhangyang Wang and Beidi Chen},\n  year = {2023},\n  booktitle = {NeurIPS 2023},\n  url = {https://arxiv.org/abs/2306.14048},\n}\n\n@inproceedings{li2024snapkv,\n  title = {{SnapKV}: {LLM} Knows What You are Looking for Before Generation},\n  author = {Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locatelli and Hanchen Ye and Tianle Cai and Patrick Lewis and Deming Chen},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2404.14469},\n}\n\n@inproceedings{ge2024fastgen,\n  title = {Model Tells You What to Discard: Adaptive {KV} Cache Compression for {LLMs}},\n  author = {Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianfeng Gao},\n  year = {2024},\n  booktitle = {ICLR 2024},\n  url = {https://arxiv.org/abs/2310.01801},\n}\n\n@inproceedings{xiao2024streamingllm,\n  title = {Efficient Streaming Language Models with Attention Sinks},\n  author = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},\n  year = {2024},\n  booktitle = {ICLR 2024},\n  url = {https://arxiv.org/abs/2309.17453},\n}\n\n@inproceedings{liu2024scissorhands,\n  title = {Scissorhands: Exploiting the Persistence of Importance Hypothesis for {LLM} {KV} Cache Compression at Test Time},\n  author = {Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie and Zhaozhuo Xu and Anastasios Kyrillidis and Anshumali Shrivastava},\n  year = {2023},\n  booktitle = {NeurIPS 2023},\n  url = {https://arxiv.org/abs/2305.17118},\n}\n\n@inproceedings{yang2024pyramidinfer,\n  title = {{PyramidInfer}: Pyramid {KV} Cache Compression for High-throughput {LLM} Inference},\n  author = {Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zhao},\n  year = {2024},\n  booktitle = {Findings of ACL 2024},\n  url = {https://arxiv.org/abs/2405.12532},\n}\n\n@misc{zuo2026ratequant,\n  title = {{RateQuant}: Optimal Mixed-Precision {KV} Cache Quantization via Rate-Distortion Theory},\n  author = {Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung},\n  year = {2026},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2605.06675},\n  eprint = {2605.06675},\n  archivePrefix = {arXiv},\n}\n\n@misc{lei2026arkv,\n  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},\n  author = {Jianlong Lei and Shashikant Ilager},\n  year = {2026},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2603.08727},\n  eprint = {2603.08727},\n  archivePrefix = {arXiv},\n}\n\n@misc{li2025kvmix,\n  title = {{KVmix}: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for {KV} Cache},\n  author = {Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2506.08018},\n  eprint = {2506.08018},\n  archivePrefix = {arXiv},\n}\n\n@misc{zhang2025mixkvq,\n  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},\n  author = {Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2512.19206},\n  eprint = {2512.19206},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{kim2024squeezellm,\n  title = {{SqueezeLLM}: Dense-and-Sparse Quantization},\n  author = {Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sheng Shen and Michael W. Mahoney and Kurt Keutzer},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2306.07629},\n}\n\n@inproceedings{voita2019analyzing,\n  title = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n  author = {Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov},\n  year = {2019},\n  booktitle = {ACL 2019},\n  url = {https://arxiv.org/abs/1905.09418},\n}\n\n@inproceedings{michel2019sixteen,\n  title = {Are Sixteen Heads Really Better than One?},\n  author = {Paul Michel and Omer Levy and Graham Neubig},\n  year = {2019},\n  booktitle = {NeurIPS 2019},\n  url = {https://arxiv.org/abs/1905.10650},\n}\n",
      "numLines": 166,
      "startLine": 1,
      "totalLines": 166
    }
  },
  "sourceToolAssistantUUID": "9618d9b7-392a-4118-a89e-e7c27089b574",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-14T13:04:12.433Z_

<details><summary>↩ Tool result · `toolu_01UoMAUxmnM5BAyKGXYQCZPW`</summary>

```text
1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
6	However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
7	We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d04e2809-6612-459f-bdff-3d50d303d112",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "4b27b599-4176-49ce-bb95-ef7e9b3f8127",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex",
      "content": "Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\\{2, 4, 8, 16\\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).\nWe trace this failure to \\emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.\nWe show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.\nOn Qwen2.5-7B at $4\\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\\% reduction over uniform 4-bit.\nThe constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\\Delta{=}0.0000$), enabling use of a simple $O(H \\log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).\nHowever, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\\ 7.13).\nWe propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "d04e2809-6612-459f-bdff-3d50d303d112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-14T13:04:12.900Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LrNNzur3CH5XrJ99jD9VHn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b27b599-4176-49ce-bb95-ef7e9b3f8127",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "932d55d3-4b93-4783-94b1-aa24a493c163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 27 · 2026-05-14T13:04:12.904Z_

<details><summary>↩ Tool result · `toolu_01LrNNzur3CH5XrJ99jD9VHn`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.
19	When most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.
20	
21	This observation points to a minimal intervention: cap the number of 2-bit assignments.
22	We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
23	On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 11.23 PPL---a 27.3\% reduction over uniform 4-bit.
24	The constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.
25	This is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.
26	
27	A surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.
28	Constrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).
29	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\S\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm without sacrificing solution quality.
30	A per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
31	
32	However, non-uniform allocation does not help universally.
33	On Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\ uniform 8.47---a marginal 0.2\% improvement.
34	On Mistral-7B-v0.3, it is slightly \emph{worse}: 7.16 vs.\ 7.13.
35	The difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.
36	When there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.
37	
38	This motivates a diagnostic question that prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
39	We propose a heterogeneity diagnostic based on the top-5\% concentration of per-head distortion (\S\ref{sec:heterogeneity}).
40	On our three architectures, the concentration metric---combined with the absolute magnitude of per-head distortion---separates the beneficial case (Qwen, concentration 0.59--0.66, 27.3\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral), across the three tested architectures.
41	The diagnostic reuses profiling data already required by the solver and adds no computational overhead.
42	
43	Our contributions are:
44	\begin{enumerate}[nosep]
45	\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
46	
47	\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\S\ref{sec:solver_equiv}).
48	
49	\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\S\ref{sec:heterogeneity}).
50	\end{enumerate}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "932d55d3-4b93-4783-94b1-aa24a493c163",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "e93e7fbd-a95e-44c2-a999-d0360a531df0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nPer-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.\nRecent work on KV cache quantization explores both uniform schemes~\\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\\cite{zhang2023h2o,li2024snapkv}.\nRateQuant~\\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\\{2,3,4,5,6\\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).\n\nIn practice, hardware-efficient inference requires bit-widths drawn from $\\{2, 4, 8, 16\\}$---the formats natively supported by modern accelerators.\nOn this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.\nOne might expect that exact MCKP solvers would fill this gap.\nThey do not.\nOn Qwen2.5-7B at $4\\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \\emph{far worse} than uniform 4-bit (15.45).\nThe optimization does not merely underperform; it fails catastrophically.\n\nThe root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.\nBoth solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.\nThe additive model predicts $\\sim$11 PPL for these allocations; the actual PPL is $3$--$4\\times$ higher.\nAt 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.\nWhen most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.\n\nThis observation points to a minimal intervention: cap the number of 2-bit assignments.\nWe add a single cardinality constraint $\\sum_h \\mathbb{1}[b_h{=}2] \\leq k$ to the standard MCKP formulation (\\S\\ref{sec:method}).\nOn Qwen2.5-7B, setting $k{=}8$ (7\\% of heads) yields 11.23 PPL---a 27.3\\% reduction over uniform 4-bit.\nThe constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.\nThis is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.\n\nA surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.\nConstrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).\nThe constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\\S\\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \\log H)$ greedy algorithm without sacrificing solution quality.\nA per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\\% of the total improvement (\\S\\ref{sec:solver_equiv}).\n\nHowever, non-uniform allocation does not help universally.\nOn Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\\ uniform 8.47---a marginal 0.2\\% improvement.\nOn Mistral-7B-v0.3, it is slightly \\emph{worse}: 7.16 vs.\\ 7.13.\nThe difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.\nWhen there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.\n\nThis motivates a diagnostic question that prior work does not address: \\emph{when} should a practitioner use per-head mixed-precision quantization?\nWe propose a heterogeneity diagnostic based on the top-5\\% concentration of per-head distortion (\\S\\ref{sec:heterogeneity}).\nOn our three architectures, the concentration metric---combined with the absolute magnitude of per-head distortion---separates the beneficial case (Qwen, concentration 0.59--0.66, 27.3\\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral), across the three tested architectures.\nThe diagnostic reuses profiling data already required by the solver and adds no computational overhead.\n\nOur contributions are:\n\\begin{enumerate}[nosep]\n\\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\\times$ compression (\\S\\ref{sec:compounding}, \\S\\ref{sec:experiments}).\n\n\\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\\S\\ref{sec:solver_equiv}).\n\n\\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\\S\\ref{sec:heterogeneity}).\n\\end{enumerate}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  },
  "sourceToolAssistantUUID": "932d55d3-4b93-4783-94b1-aa24a493c163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-14T13:04:13.370Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XJJTTFe8yWmsMt35bt5hix`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e93e7fbd-a95e-44c2-a999-d0360a531df0",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "b1513cb9-e91f-4425-bca6-65fcc817c8fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 29 · 2026-05-14T13:04:13.374Z_

<details><summary>↩ Tool result · `toolu_01XJJTTFe8yWmsMt35bt5hix`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, and sliding-window adaptation~\cite{duanmu2024skvq}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	
7	\paragraph{KV Cache Eviction.}
8	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
9	Our work focuses exclusively on the quantization allocation problem.
10	
11	\paragraph{Mixed-Precision Rate-Distortion Allocation.}
12	RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure.
13	On hardware-aligned $\{2,4,8,16\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.
14	Related mixed-precision work operates at coarser granularity (layer-level~\cite{li2025kvmix}, memory-budget-level~\cite{lei2026arkv}), at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
15	
16	\paragraph{Attention Head Analysis.}
17	Prior work studies head redundancy and pruning~\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.
18	Our analysis asks a different question: which heads are sensitive to \emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\S\ref{sec:heterogeneity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1513cb9-e91f-4425-bca6-65fcc817c8fe",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "b3ca9d19-db23-4aa7-90b3-37c4f9247caa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, and sliding-window adaptation~\\cite{duanmu2024skvq}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.\n\n\\paragraph{KV Cache Eviction.}\nComplementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\\cite{zhang2023h2o}, per-head important tokens~\\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\\cite{liu2024scissorhands}, attention sinks~\\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\\cite{yang2024pyramidinfer}.\nOur work focuses exclusively on the quantization allocation problem.\n\n\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure.\nOn hardware-aligned $\\{2,4,8,16\\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.\nRelated mixed-precision work operates at coarser granularity (layer-level~\\cite{li2025kvmix}, memory-budget-level~\\cite{lei2026arkv}), at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\n\n\\paragraph{Attention Head Analysis.}\nPrior work studies head redundancy and pruning~\\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.\nOur analysis asks a different question: which heads are sensitive to \\emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "b1513cb9-e91f-4425-bca6-65fcc817c8fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-14T13:04:13.836Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q9hTfzaXbDqjv2UF1aa4tB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3ca9d19-db23-4aa7-90b3-37c4f9247caa",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "a07e8a81-b589-4d8e-a141-20c101011599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 31 · 2026-05-14T13:04:13.840Z_

<details><summary>↩ Tool result · `toolu_01Q9hTfzaXbDqjv2UF1aa4tB`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:formulation}
6	
7	We formulate per-head KV cache quantization as a constrained optimization problem.
8	Let $h \in \{1,\ldots,H\}$ index the KV heads across all layers, $b_h \in \mathcal{B}$ the bit-width assigned to head $h$, and $\mathcal{B} = \{2, 4, 8, 16\}$ the set of hardware-aligned bit-widths.
9	Each head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.
10	Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
11	\begin{equation}
12	\label{eq:objective}
13	\min_{\{b_h\}} \sum_{h=1}^{H} d_h(b_h) \quad \text{s.t.} \quad \frac{1}{H \cdot 16}\sum_{h=1}^{H} b_h \leq R.
14	\end{equation}
15	
16	This is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\mathcal{B}$ to minimize total distortion under a budget.
17	RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
18	Hardware-aligned bit-widths $\{2,4,8,16\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.
19	Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
20	
21	\subsection{PPL-based Per-Head Profiling}
22	\label{sec:profiling}
23	
24	We profile each KV head independently by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
25	This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
26	
27	The optimization in Eq.~\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\sum_h d_h(b_h)$.
28	This holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.
29	At 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.
30	
31	\subsection{Compounding Effect}
32	\label{sec:compounding}
33	
34	When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.
35	The mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.
36	When the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.
37	As the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.
38	
39	\begin{figure}[t]
40	\centering
41	\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
42	\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
43	\label{fig:compounding}
44	\end{figure}
45	
46	Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.
47	On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
48	Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \approx 0$, so most 2-bit assignments appear free to the additive objective.
49	The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
50	
51	This compounding is specific to 2-bit quantization.
52	At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
53	The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.
54	
55	Figure~\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\times$ compression.
56	The curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.
57	
58	\subsection{Cardinality Constraint}
59	\label{sec:cardinality}
60	
61	The compounding effect motivates a simple addition to Eq.~\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.
62	\begin{equation}
63	\label{eq:constraint}
64	\sum_{h=1}^{H} \mathbb{1}[b_h = 2] \leq k.
65	\end{equation}
66	
67	The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
68	For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
69	
70	The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.
71	
72	A natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.
73	On Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\% relative to the bf16 baseline (9.81 $\to$ 12.94), L0H2 by 23.2\% (9.81 $\to$ 12.09), L0H3 by 11.7\% (9.81 $\to$ 10.96).
74	These values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.
75	We verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.
76	No manual exclusion rule is needed; the profiler signal is sufficient.
77	
78	\subsection{Solver Equivalence}
79	\label{sec:solver_equiv}
80	
81	\begin{table}[t]
82	\centering
83	\small
84	\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\protect\footnotemark}
85	\label{tab:solver_equiv}
86	\begin{tabular}{llcccc}
87	\toprule
88	Solver & Constraint & PPL & \multicolumn{3}{c}{Bit distribution} \\
89	 & & & 2-bit & 4-bit & 8/16-bit \\
90	\midrule
91	Greedy & None & 32.45 & 68 & 30 & 14 \\
92	MCKP & None & 36.92 & 75 & 33 & 4 \\
93	Greedy & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
94	MCKP & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
95	Uniform & --- & 15.45 & 0 & 112 & 0 \\
96	\bottomrule
97	\end{tabular}
98	\end{table}
99	\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\times$ 2048 tok) achieves 10.91 (Appendix~\ref{sec:profiling_resolution}).}
100	
101	With the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.
102	Table~\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.
103	We verify this at the per-head level across three models:
104	
105	\begin{itemize}[nosep]
106	\item \textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.
107	\item \textbf{Llama-3.1-8B:} 256/256 heads identical.
108	\item \textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.
109	\end{itemize}
110	
111	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.
112	Without it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.
113	The cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.
114	
115	The practical implication is that practitioners can use the simpler $O(H \log H)$ greedy algorithm instead of MCKP without sacrificing optimality.
116	
117	To verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.
118	Of the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL---0.4\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.
119	Combined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a07e8a81-b589-4d8e-a141-20c101011599",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "d890666e-48f4-42ab-b05d-6f1eaea8db78",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nWe formulate per-head KV cache quantization as a constrained optimization problem.\nLet $h \\in \\{1,\\ldots,H\\}$ index the KV heads across all layers, $b_h \\in \\mathcal{B}$ the bit-width assigned to head $h$, and $\\mathcal{B} = \\{2, 4, 8, 16\\}$ the set of hardware-aligned bit-widths.\nEach head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.\nGiven a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\\times$ compression), we seek the allocation that minimizes total distortion:\n\\begin{equation}\n\\label{eq:objective}\n\\min_{\\{b_h\\}} \\sum_{h=1}^{H} d_h(b_h) \\quad \\text{s.t.} \\quad \\frac{1}{H \\cdot 16}\\sum_{h=1}^{H} b_h \\leq R.\n\\end{equation}\n\nThis is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\\mathcal{B}$ to minimize total distortion under a budget.\nRateQuant~\\cite{zuo2026ratequant} solves this for consecutive bit-widths $\\{2,3,4,5,6\\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).\nHardware-aligned bit-widths $\\{2,4,8,16\\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.\nMoreover, as we show in \\S\\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.\n\n\\subsection{PPL-based Per-Head Profiling}\n\\label{sec:profiling}\n\nWe profile each KV head independently by quantizing it to each $b \\in \\mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\\times$ 2048 tokens from WikiText-2 train.\nThis yields a distortion table of $H \\times |\\mathcal{B}|$ entries that serves as input to the solver.\n\nThe optimization in Eq.~\\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\\sum_h d_h(b_h)$.\nThis holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.\nAt 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.\n\n\\subsection{Compounding Effect}\n\\label{sec:compounding}\n\nWhen many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.\nThe mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.\nWhen the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.\nAs the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_compounding_curve.pdf}\n\\caption{PPL on Qwen2.5-7B ($4\\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}\n\\label{fig:compounding}\n\\end{figure}\n\nUnconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.\nOn Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).\nStandard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \\approx 0$, so most 2-bit assignments appear free to the additive objective.\nThe resulting additive prediction is $\\sum_h d_h(b_h) + \\text{baseline} \\approx 11$ PPL---$3\\text{--}4\\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.\n\nThis compounding is specific to 2-bit quantization.\nAt 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).\nThe qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.\n\nFigure~\\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\\times$ compression.\nThe curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.\n\n\\subsection{Cardinality Constraint}\n\\label{sec:cardinality}\n\nThe compounding effect motivates a simple addition to Eq.~\\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.\n\\begin{equation}\n\\label{eq:constraint}\n\\sum_{h=1}^{H} \\mathbb{1}[b_h = 2] \\leq k.\n\\end{equation}\n\nThe constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\\ref{fig:compounding}).\nFor Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\\sim$7\\% of heads).\n\nThe constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.\n\nA natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.\nOn Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\\% relative to the bf16 baseline (9.81 $\\to$ 12.94), L0H2 by 23.2\\% (9.81 $\\to$ 12.09), L0H3 by 11.7\\% (9.81 $\\to$ 10.96).\nThese values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.\nWe verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.\nNo manual exclusion rule is needed; the profiler signal is sufficient.\n\n\\subsection{Solver Equivalence}\n\\label{sec:solver_equiv}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Solver comparison on Qwen2.5-7B at $4\\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\\leq}8$) makes greedy and MCKP produce identical allocations.\\protect\\footnotemark}\n\\label{tab:solver_equiv}\n\\begin{tabular}{llcccc}\n\\toprule\nSolver & Constraint & PPL & \\multicolumn{3}{c}{Bit distribution} \\\\\n & & & 2-bit & 4-bit & 8/16-bit \\\\\n\\midrule\nGreedy & None & 32.45 & 68 & 30 & 14 \\\\\nMCKP & None & 36.92 & 75 & 33 & 4 \\\\\nGreedy & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\nMCKP & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\nUniform & --- & 15.45 & 0 & 112 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\\times$ 2048 tok) achieves 10.91 (Appendix~\\ref{sec:profiling_resolution}).}\n\nWith the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.\nTable~\\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.\nWe verify this at the per-head level across three models:\n\n\\begin{itemize}[nosep]\n\\item \\textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.\n\\item \\textbf{Llama-3.1-8B:} 256/256 heads identical.\n\\item \\textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.\n\\end{itemize}\n\nThe constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.\nWithout it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.\nThe cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.\n\nThe practical implication is that practitioners can use the simpler $O(H \\log H)$ greedy algorithm instead of MCKP without sacrificing optimality.\n\nTo verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.\nOf the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.018 PPL---0.4\\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.\nCombined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \\log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  },
  "sourceToolAssistantUUID": "a07e8a81-b589-4d8e-a141-20c101011599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-14T13:04:14.347Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RNTGGU5miFxKBahi5qtXPa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d890666e-48f4-42ab-b05d-6f1eaea8db78",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "316f6239-03bd-4493-83d6-bf20926addd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 33 · 2026-05-14T13:04:14.352Z_

<details><summary>↩ Tool result · `toolu_01RNTGGU5miFxKBahi5qtXPa`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate on three architectures spanning different grouped-query attention (GQA) configurations:
9	\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
10	\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
11	and \textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention).
12	This selection covers the two dominant KV head counts (112 vs.\ 256) and both standard and sliding-window attention.
13	
14	\paragraph{Evaluation.}
15	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
16	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
17	
18	\paragraph{Profiling.}
19	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
20	We use two profiling resolutions: \emph{standard} (16 sequences $\times$ 512 tokens) and \emph{high-resolution} (64 sequences $\times$ 2048 tokens), both from WikiText-2 train.
21	Unless marked with $\dagger$, all results use standard-resolution profiling; Appendix~\ref{sec:profiling_resolution} analyzes the effect of resolution.
22	
23	\paragraph{Compression and constraint.}
24	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
25	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).
26	
27	\paragraph{Baselines.}
28	We compare against:
29	(1)~uniform 4-bit quantization;
30	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
31	(3)~unconstrained MCKP allocation;
32	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
33	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
34	
35	\subsection{Main Results}
36	\label{sec:main_results}
37	
38	\begin{table}[t]
39	\centering
40	\small
41	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained allocation fails catastrophically on $\{2,4,8,16\}$; our cardinality constraint restores performance. Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\ddagger$Best $k$ from ablation ($k{=}4$). The $\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}
42	\label{tab:main_results}
43	\begin{tabular}{lcccccc}
44	\toprule
45	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
46	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
47	\midrule
48	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23}$\pm$0.06 \\
49	Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \textbf{8.45}$^\dagger$ \\
50	Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\
51	\bottomrule
52	\end{tabular}
53	\end{table}
54	
55	Table~\ref{tab:main_results} summarizes the main results.
56	On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
57	Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in Appendix~\ref{sec:profiling_resolution}.
58	Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
59	The constraint eliminates this failure mode entirely.
60	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 (std is 1.3\% of the uniform gap), with 90.2\% three-way allocation agreement, confirming profiling stability.
61	
62	On Llama-3.1-8B, the improvement is marginal: 8.45 vs.\ 8.47 (0.2\%).
63	The profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.
64	
65	On Mistral-7B-v0.3, constrained MCKP (7.16, $k{=}4$) is slightly worse than uniform (7.13, $+$0.4\%).
66	This is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.
67	Mistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.
68	
69	Unconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.
70	Figure~\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=\columnwidth]{figures/fig3_allocation_comparison.pdf}
75	\caption{Bit-width allocation on Qwen2.5-7B at 4$\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}
76	\label{fig:allocation}
77	\end{figure}
78	
79	\subsection{Budget Sweep}
80	\label{sec:budget_sweep}
81	
82	\begin{table}[t]
83	\centering
84	\small
85	\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\geq$4$\times$). Standard-resolution profiling; hires results in Appendix~\ref{sec:profiling_resolution}.}
86	\label{tab:budget_sweep}
87	\begin{tabular}{cccc}
88	\toprule
89	Compression & Uniform PPL & Constr.\ MCKP PPL & $\Delta$ PPL \\
90	\midrule
91	2$\times$ & 10.10 & 10.66 & $-$0.56 \\
92	4$\times$ & 15.45 & 11.23 & $+$4.22 \\
93	8$\times$ & 14{,}759 & 907 & $+$13{,}852 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
99	
100	At 2$\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\ 9.81 bf16, $+$0.29).
101	Per-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.
102	
103	At 4$\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement.
104	Hires profiling further reduces this to 10.91 (Appendix~\ref{sec:profiling_resolution}).
105	
106	At 8$\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.
107	However, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.
108	Neither result is practically usable, but the gap demonstrates the protection mechanism at work.
109	
110	\subsection{Heuristic Baselines}
111	\label{sec:heuristic}
112	
113	\begin{table}[t]
114	\centering
115	\small
116	\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral). Llama and Mistral use hires profiling, consistent with Table~\ref{tab:main_results}.}
117	\label{tab:heuristic}
118	\begin{tabular}{lcccc}
119	\toprule
120	Model & MCKP & \multicolumn{2}{c}{L0-random} & Naive \\
121	 & & Median & Mean$\pm$Std & Positional \\
122	\midrule
123	Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
124	Llama-3.1-8B    & 8.45  & 8.62  & 8.62$\pm$0.07  & 8.58 \\
125	Mistral-7B-v0.3 & 7.16  & 7.20  & 7.24$\pm$0.07  & 7.21 \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	Table~\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.
131	
132	On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.
133	
134	On Llama ($k{=}2$), the gap between methods is small: MCKP achieves 8.45 vs.\ L0-random 8.62 and naive positional 8.58.
135	With only 2 heads assigned to 2-bit, the choice of which heads to compress has limited impact, and all methods cluster within 0.17 PPL.
136	MCKP still achieves the best result, but the practical advantage of profiling-guided selection is marginal at this constraint level.
137	
138	On Mistral ($k{=}4$), all non-uniform strategies are worse than uniform 4-bit (7.13): MCKP 7.16, naive 7.21, L0-random median 7.20 (mean 7.24$\pm$0.07).
139	MCKP outperforms both heuristics, but the best non-uniform result (7.16) still exceeds uniform by 0.03 PPL, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.
140	Note that the heuristic baselines use a slightly higher budget (0.256 vs.\ 0.248 for MCKP, a 3\% difference) because integer $k$ does not divide evenly into the target; despite this advantage, they still underperform MCKP, making the comparison conservative.
141	
142	\subsection{Downstream Evaluation}
143	\label{sec:downstream}
144	
145	\begin{table}[t]
146	\centering
147	\small
148	\caption{0-shot accuracy on Qwen2.5-7B at 4$\times$ compression. Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization.}
149	\label{tab:downstream}
150	\begin{tabular}{lcccc}
151	\toprule
152	Task & Baseline & Uniform & MCKP & $\Delta$ vs \\
153	 & (bf16) & (4-bit) & (Ours) & Uniform \\
154	\midrule
155	ARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\
156	HellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\
157	PIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\
158	WinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\
159	\midrule
160	Average    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
165	Table~\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.
166	Constrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\ 0.660), with gains on all four benchmarks.
167	The largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.
168	
169	Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.
170	
171	\subsection{Cross-Dataset Stability}
172	\label{sec:cross_dataset}
173	
174	To verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, at $4\times$ compression.
175	On Qwen2.5-7B, C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\ 15.45 uniform, a 27\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).
176	In the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on the C4 held-out split (vs.\ 35.42 uniform, a 42\% reduction; C4 bf16 baseline on this split is 15.32).
177	All three models show ${>}96\%$ bit-assignment agreement across calibration sources: Qwen 96.4\% (108/112 heads), Llama 97.7\% (250/256), and Mistral 96.5\% (247/256).
178	Qwen's agreement is the most informative, as all 112 heads have variable assignments; on Llama, 253 of 256 heads are forced to 4-bit by the $k{=}2$ constraint, inflating agreement.
179	The cross-dataset results reinforce the heterogeneity-driven narrative: on Qwen, the MCKP benefit is preserved across calibration sources; on Llama and Mistral, the lack of benefit is equally stable---Llama's C4-calibrated MCKP is 0.18 PPL worse than uniform, and Mistral shows similar degradation ($-$0.03 to $-$0.05 PPL).
180	Whether non-uniform allocation helps is determined by the model's intrinsic head sensitivity heterogeneity, not the calibration data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "316f6239-03bd-4493-83d6-bf20926addd3",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "f2294002-693c-4faa-9d1e-7abd72359480",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate on three architectures spanning different grouped-query attention (GQA) configurations:\n\\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\\times$ 4 KV heads = 112 KV heads),\n\\textbf{Llama-3.1-8B} (4:1, 32 $\\times$ 8 = 256 KV heads),\nand \\textbf{Mistral-7B-v0.3} (4:1, 32 $\\times$ 8 = 256 KV heads, sliding window attention).\nThis selection covers the two dominant KV head counts (112 vs.\\ 256) and both standard and sliding-window attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nWe use two profiling resolutions: \\emph{standard} (16 sequences $\\times$ 512 tokens) and \\emph{high-resolution} (64 sequences $\\times$ 2048 tokens), both from WikiText-2 train.\nUnless marked with $\\dagger$, all results use standard-resolution profiling; Appendix~\\ref{sec:profiling_resolution} analyzes the effect of resolution.\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained allocation fails catastrophically on $\\{2,4,8,16\\}$; our cardinality constraint restores performance. Best constrained result per model in \\textbf{bold}. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\\ddagger$Best $k$ from ablation ($k{=}4$). The $\\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{11.23}$\\pm$0.06 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \\textbf{8.45}$^\\dagger$ \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\\dagger\\ddagger}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main_results} summarizes the main results.\nOn Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\\% reduction over uniform 4-bit (15.45).\nHigher-resolution profiling (64 seq $\\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in Appendix~\\ref{sec:profiling_resolution}.\nWithout the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.\nThe constraint eliminates this failure mode entirely.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 (std is 1.3\\% of the uniform gap), with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the improvement is marginal: 8.45 vs.\\ 8.47 (0.2\\%).\nThe profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.\n\nOn Mistral-7B-v0.3, constrained MCKP (7.16, $k{=}4$) is slightly worse than uniform (7.13, $+$0.4\\%).\nThis is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.\nMistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.\n\nUnconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.\nFigure~\\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_allocation_comparison.pdf}\n\\caption{Bit-width allocation on Qwen2.5-7B at 4$\\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}\n\\label{fig:allocation}\n\\end{figure}\n\n\\subsection{Budget Sweep}\n\\label{sec:budget_sweep}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\\geq$4$\\times$). Standard-resolution profiling; hires results in Appendix~\\ref{sec:profiling_resolution}.}\n\\label{tab:budget_sweep}\n\\begin{tabular}{cccc}\n\\toprule\nCompression & Uniform PPL & Constr.\\ MCKP PPL & $\\Delta$ PPL \\\\\n\\midrule\n2$\\times$ & 10.10 & 10.66 & $-$0.56 \\\\\n4$\\times$ & 15.45 & 11.23 & $+$4.22 \\\\\n8$\\times$ & 14{,}759 & 907 & $+$13{,}852 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.\n\nAt 2$\\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\\ 9.81 bf16, $+$0.29).\nPer-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.\n\nAt 4$\\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\\% improvement.\nHires profiling further reduces this to 10.91 (Appendix~\\ref{sec:profiling_resolution}).\n\nAt 8$\\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.\nHowever, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.\nNeither result is practically usable, but the gap demonstrates the protection mechanism at work.\n\n\\subsection{Heuristic Baselines}\n\\label{sec:heuristic}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Constrained MCKP vs.\\ heuristic baselines at 4$\\times$ compression. L0-random reports median and mean$\\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral). Llama and Mistral use hires profiling, consistent with Table~\\ref{tab:main_results}.}\n\\label{tab:heuristic}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & MCKP & \\multicolumn{2}{c}{L0-random} & Naive \\\\\n & & Median & Mean$\\pm$Std & Positional \\\\\n\\midrule\nQwen2.5-7B      & 11.23 & 11.52 & 11.69$\\pm$0.47 & 12.23 \\\\\nLlama-3.1-8B    & 8.45  & 8.62  & 8.62$\\pm$0.07  & 8.58 \\\\\nMistral-7B-v0.3 & 7.16  & 7.20  & 7.24$\\pm$0.07  & 7.21 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.\n\nOn Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.\n\nOn Llama ($k{=}2$), the gap between methods is small: MCKP achieves 8.45 vs.\\ L0-random 8.62 and naive positional 8.58.\nWith only 2 heads assigned to 2-bit, the choice of which heads to compress has limited impact, and all methods cluster within 0.17 PPL.\nMCKP still achieves the best result, but the practical advantage of profiling-guided selection is marginal at this constraint level.\n\nOn Mistral ($k{=}4$), all non-uniform strategies are worse than uniform 4-bit (7.13): MCKP 7.16, naive 7.21, L0-random median 7.20 (mean 7.24$\\pm$0.07).\nMCKP outperforms both heuristics, but the best non-uniform result (7.16) still exceeds uniform by 0.03 PPL, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.\nNote that the heuristic baselines use a slightly higher budget (0.256 vs.\\ 0.248 for MCKP, a 3\\% difference) because integer $k$ does not divide evenly into the target; despite this advantage, they still underperform MCKP, making the comparison conservative.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy on Qwen2.5-7B at 4$\\times$ compression. Constrained MCKP recovers approximately 73\\% of the accuracy lost by uniform 4-bit quantization.}\n\\label{tab:downstream}\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Baseline & Uniform & MCKP & $\\Delta$ vs \\\\\n & (bf16) & (4-bit) & (Ours) & Uniform \\\\\n\\midrule\nARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\\\\nHellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\\\\nPIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\\\\nWinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\\\\n\\midrule\nAverage    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.\nConstrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\\ 0.660), with gains on all four benchmarks.\nThe largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.\n\nConstrained MCKP recovers approximately 73\\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.\n\n\\subsection{Cross-Dataset Stability}\n\\label{sec:cross_dataset}\n\nTo verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, at $4\\times$ compression.\nOn Qwen2.5-7B, C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\\ 15.45 uniform, a 27\\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).\nIn the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on the C4 held-out split (vs.\\ 35.42 uniform, a 42\\% reduction; C4 bf16 baseline on this split is 15.32).\nAll three models show ${>}96\\%$ bit-assignment agreement across calibration sources: Qwen 96.4\\% (108/112 heads), Llama 97.7\\% (250/256), and Mistral 96.5\\% (247/256).\nQwen's agreement is the most informative, as all 112 heads have variable assignments; on Llama, 253 of 256 heads are forced to 4-bit by the $k{=}2$ constraint, inflating agreement.\nThe cross-dataset results reinforce the heterogeneity-driven narrative: on Qwen, the MCKP benefit is preserved across calibration sources; on Llama and Mistral, the lack of benefit is equally stable---Llama's C4-calibrated MCKP is 0.18 PPL worse than uniform, and Mistral shows similar degradation ($-$0.03 to $-$0.05 PPL).\nWhether non-uniform allocation helps is determined by the model's intrinsic head sensitivity heterogeneity, not the calibration data.",
      "numLines": 180,
      "startLine": 1,
      "totalLines": 180
    }
  },
  "sourceToolAssistantUUID": "316f6239-03bd-4493-83d6-bf20926addd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-14T13:04:14.787Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EdKYNEpLgZxQVqhsRAybD2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2294002-693c-4faa-9d1e-7abd72359480",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "58dedf15-23e5-4ef8-9aed-bbf84d0d2ad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 35 · 2026-05-14T13:04:14.791Z_

<details><summary>↩ Tool result · `toolu_01EdKYNEpLgZxQVqhsRAybD2`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across three architectures at $4\times$ compression.
12	Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.
13	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit.
14	Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\ $+$0.38).
15	Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.
16	Here, constrained MCKP is slightly \emph{worse} than uniform ($+$0.13 vs.\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\times$ compression. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok).}
22	\label{tab:heterogeneity}
23	\begin{tabular}{lccccc}
24	\toprule
25	Model & GQA & Top-5\% & $\Delta$ PPL & $\Delta$ PPL & Recommendation \\
26	 & Ratio & Conc. & (Uniform) & (Ours) & \\
27	\midrule
28	Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\
29	Llama-3.1-8B$^\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\
30	Mistral-7B-v0.3$^\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\begin{figure*}[t]
36	\centering
37	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
38	\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}
39	\label{fig:heatmap}
40	\end{figure*}
41	
42	Figure~\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.
43	The contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.
44	
45	\subsection{Diagnostic Framework}
46	\label{sec:diagnostic}
47	
48	The heterogeneity characterization yields a preliminary guideline, based on three architectures, for deciding when non-uniform allocation is worthwhile:
49	
50	\begin{enumerate}[nosep]
51	\item Run per-head profiling as described in \S\ref{sec:profiling}.
52	\item Compute the top-5\% concentration from the resulting distortion table.
53	\item Select allocation strategy:
54	  \begin{itemize}[nosep]
55	  \item Concentration ${>}\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\% PPL improvement).
56	  \item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\% at $4\times$).
57	  \item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).
58	  \end{itemize}
59	\end{enumerate}
60	
61	The diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.
62	This avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.
63	The thresholds above are derived from three architectures and should be validated on a broader set of models before being treated as general rules.
64	Additional analyses---the effect of aggressive compression ratios, profiling resolution and multi-seed stability, per-layer optimality validation, and KV separation ablation---are provided in Appendices~\ref{sec:aggressive}--\ref{sec:kv_separation}.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58dedf15-23e5-4ef8-9aed-bbf84d0d2ad0",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "f312751f-b40a-4e36-b301-60f529a93b70",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across three architectures at $4\\times$ compression.\nQwen2.5-7B exhibits the highest heterogeneity (top-5\\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\\% improvement over uniform 4-bit.\nLlama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\\ $+$0.38).\nMistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.\nHere, constrained MCKP is slightly \\emph{worse} than uniform ($+$0.13 vs.\\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\\times$ compression. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok).}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & GQA & Top-5\\% & $\\Delta$ PPL & $\\Delta$ PPL & Recommendation \\\\\n & Ratio & Conc. & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\\\\nLlama-3.1-8B$^\\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\\\\nMistral-7B-v0.3$^\\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_head_delta_heatmap.pdf}\n\\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}\n\\label{fig:heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.\nThe contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.\n\n\\subsection{Diagnostic Framework}\n\\label{sec:diagnostic}\n\nThe heterogeneity characterization yields a preliminary guideline, based on three architectures, for deciding when non-uniform allocation is worthwhile:\n\n\\begin{enumerate}[nosep]\n\\item Run per-head profiling as described in \\S\\ref{sec:profiling}.\n\\item Compute the top-5\\% concentration from the resulting distortion table.\n\\item Select allocation strategy:\n  \\begin{itemize}[nosep]\n  \\item Concentration ${>}\\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\\% PPL improvement).\n  \\item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\\% at $4\\times$).\n  \\item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).\n  \\end{itemize}\n\\end{enumerate}\n\nThe diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.\nThis avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.\nThe thresholds above are derived from three architectures and should be validated on a broader set of models before being treated as general rules.\nAdditional analyses---the effect of aggressive compression ratios, profiling resolution and multi-seed stability, per-layer optimality validation, and KV separation ablation---are provided in Appendices~\\ref{sec:aggressive}--\\ref{sec:kv_separation}.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  },
  "sourceToolAssistantUUID": "58dedf15-23e5-4ef8-9aed-bbf84d0d2ad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-14T13:04:15.500Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UGFWmMkrPdb5EBjrwWgWVc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f312751f-b40a-4e36-b301-60f529a93b70",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "c3d1b70e-7b68-4099-abc7-371c351e758f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 37 · 2026-05-14T13:04:15.504Z_

<details><summary>↩ Tool result · `toolu_01UGFWmMkrPdb5EBjrwWgWVc`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.
4	A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\% improvement at $4\times$ compression.
5	Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\Delta = 0.0000$), so a simple $O(H \log H)$ greedy algorithm suffices.
6	The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\ 7.13 PPL).
7	This diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \emph{before deployment} whether non-uniform quantization is worthwhile for a given model.
8	
9	\paragraph{Limitations.}
10	Our study has several limitations that temper the generality of the findings.
11	First, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.
12	Second, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.
13	Third, we report perplexity and downstream accuracy but no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.
14	Fourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.
15	Finally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).
16	
17	\paragraph{Future Work.}
18	Extending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.
19	Integration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (Appendix~\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3d1b70e-7b68-4099-abc7-371c351e758f",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "465b8ce3-4b39-43b2-9d64-63bf883c88b7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.\nA single constraint---limiting simultaneously active 2-bit heads to $k \\leq 8$ (7\\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\\% improvement at $4\\times$ compression.\nUnder the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\\Delta = 0.0000$), so a simple $O(H \\log H)$ greedy algorithm suffices.\nThe benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\\ 7.13 PPL).\nThis diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile for a given model.\n\n\\paragraph{Limitations.}\nOur study has several limitations that temper the generality of the findings.\nFirst, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.\nSecond, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.\nThird, we report perplexity and downstream accuracy but no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.\nFourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.\nFinally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).\n\n\\paragraph{Future Work.}\nExtending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.\nIntegration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (Appendix~\\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "c3d1b70e-7b68-4099-abc7-371c351e758f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-14T13:04:16.182Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WtSyod7KZgvkuAeMewpB8U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "465b8ce3-4b39-43b2-9d64-63bf883c88b7",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "50326500-e0b1-4861-8412-fa33bb129ef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 39 · 2026-05-14T13:04:16.186Z_

<details><summary>↩ Tool result · `toolu_01WtSyod7KZgvkuAeMewpB8U`</summary>

```text
1	\appendix
2	
3	\section{Aggressive Compression}
4	\label{sec:aggressive}
5	
6	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
7	At more aggressive ratios, the picture changes: at $5.3\times$ (average 3 bits), constrained MCKP achieves $45\times$ lower PPL than uniform on Llama (57.60 vs.\ 2643.77) and $44\times$ on Mistral (11.91 vs.\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.
8	At $8\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).
9	The intermediate regime ($5.3\times$) provides the largest relative benefit.
10	
11	\section{Profiling Resolution and Stability}
12	\label{sec:profiling_resolution}
13	
14	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
15	
16	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
17	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
18	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
19	
20	The additional signal changes 8 of 112 head assignments.
21	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
22	
23	\paragraph{Multi-seed stability.}
24	The profiled allocation is stable across calibration subsets.
25	Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%.
26	The bit distribution is identical across all seeds ($\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\}$), and 101 of 112 heads (90.2\%) receive the same assignment in all three runs.
27	This stability confirms that the per-head sensitivity ranking is robust to calibration sampling noise.
28	
29	\paragraph{Per-layer optimality.}
30	To validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).
31	Of the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.
32	All three gaps involve repositioning a 2-bit assignment among heads with near-identical sensitivity within the same layer bit budget.
33	The negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.
34	
35	\section{KV Separation Ablation}
36	\label{sec:kv_separation}
37	
38	We test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.
39	
40	Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).
41	The degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.
42	Meanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.
43	
44	Of the 112 heads, 21 show K$\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.
45	This systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.
46	
47	Joint allocation is sufficient under the current constraint formulation.
48	Separated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50326500-e0b1-4861-8412-fa33bb129ef0",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "9d96ca92-f7ba-480a-b434-3f1dcaee6947",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Aggressive Compression}\n\\label{sec:aggressive}\n\nAt $4\\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.\nAt more aggressive ratios, the picture changes: at $5.3\\times$ (average 3 bits), constrained MCKP achieves $45\\times$ lower PPL than uniform on Llama (57.60 vs.\\ 2643.77) and $44\\times$ on Mistral (11.91 vs.\\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.\nAt $8\\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).\nThe intermediate regime ($5.3\\times$) provides the largest relative benefit.\n\n\\section{Profiling Resolution and Stability}\n\\label{sec:profiling_resolution}\n\nWe compare standard-resolution profiling (16 sequences $\\times$ 512 tokens) against high-resolution profiling (64 sequences $\\times$ 2048 tokens) on Qwen2.5-7B at $4\\times$ compression.\n\nHigh-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).\nRelative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\\% reduction.\nThe improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\\times$ more).\n\nThe additional signal changes 8 of 112 head assignments.\nHigh-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.\n\n\\paragraph{Multi-seed stability.}\nThe profiled allocation is stable across calibration subsets.\nUnder hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \\pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\\%.\nThe bit distribution is identical across all seeds ($\\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\\}$), and 101 of 112 heads (90.2\\%) receive the same assignment in all three runs.\nThis stability confirms that the per-head sensitivity ranking is robust to calibration sampling noise.\n\n\\paragraph{Per-layer optimality.}\nTo validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).\nOf the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.\nAll three gaps involve repositioning a 2-bit assignment among heads with near-identical sensitivity within the same layer bit budget.\nThe negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.\n\n\\section{KV Separation Ablation}\n\\label{sec:kv_separation}\n\nWe test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.\n\nJoint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).\nThe degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.\nMeanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.\n\nOf the 112 heads, 21 show K$\\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.\nThis systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.\n\nJoint allocation is sufficient under the current constraint formulation.\nSeparated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "50326500-e0b1-4861-8412-fa33bb129ef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-14T13:04:16.257Z_

<details open><summary>🔧 Tool call — Read · `toolu_01783EsWFqc236ZZctpeU7Di`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d96ca92-f7ba-480a-b434-3f1dcaee6947",
  "isSidechain": false,
  "requestId": "req_011Cb2WS5eN8PVuuymAsUksp",
  "type": "assistant",
  "uuid": "9618d9b7-392a-4118-a89e-e7c27089b574",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH8HPkzZJmEPhzDmquihJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 30413,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 697,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 701,
          "cache_read_input_tokens": 30413,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 697
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

_source line 41 · 2026-05-14T13:04:16.307Z_

```json
{
  "parentUuid": "9695e153-21a8-469d-86eb-1874e035ab71",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b2eb54b8-ef8d-4eac-b396-daa502284497",
  "timestamp": "2026-05-14T13:04:16.307Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference - **Deadline**: 2026-05-25 (ARR submission) - **格式**: ACL 模板, 正文 ≤8 页, mandato…",
  "leafUuid": "b2eb54b8-ef8d-4eac-b396-daa502284497",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP paper on KV cache mixed-precision quantization",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


### Assistant

_source line 44 · 2026-05-14T13:04:20.293Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read all the paper sections. Let me also render the PDF to check visual formatting, and run reference verification in parallel.

Let me now compile my review. Let me first check the PDF visually and verify references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2eb54b8-ef8d-4eac-b396-daa502284497",
  "isSidechain": false,
  "requestId": "req_011Cb2WSfKur14C1duLniaGW",
  "type": "assistant",
  "uuid": "dc880350-3089-4fe7-8c40-5f0348632e8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwyGLwFtntYscczEnw1AL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18801,
      "cache_read_input_tokens": 31110,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 31110,
          "cache_creation_input_tokens": 18801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18801
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

_source line 45 · 2026-05-14T13:04:21.219Z_

论文全文已读完。现在渲染 PDF 检查排版，并验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc880350-3089-4fe7-8c40-5f0348632e8c",
  "isSidechain": false,
  "requestId": "req_011Cb2WSfKur14C1duLniaGW",
  "type": "assistant",
  "uuid": "481bd019-e743-40a5-9953-f58cdda1073c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwyGLwFtntYscczEnw1AL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18801,
      "cache_read_input_tokens": 31110,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 31110,
          "cache_creation_input_tokens": 18801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18801
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

_source line 46 · 2026-05-14T13:04:23.517Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01Qj2uvP9Gppc2N4aXKtyP4d`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf",
  "pages": "1-12",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "481bd019-e743-40a5-9953-f58cdda1073c",
  "isSidechain": false,
  "requestId": "req_011Cb2WSfKur14C1duLniaGW",
  "type": "assistant",
  "uuid": "d30afa8d-8a44-47cf-b660-9ecbd9fa8a59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwyGLwFtntYscczEnw1AL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18801,
      "cache_read_input_tokens": 31110,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 31110,
          "cache_creation_input_tokens": 18801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18801
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

_source line 47 · 2026-05-14T13:04:23.652Z_

<details><summary>↩ Tool result · `toolu_01Qj2uvP9Gppc2N4aXKtyP4d`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 11 页): 1-12\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d30afa8d-8a44-47cf-b660-9ecbd9fa8a59",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "78f1965a-2f9a-4db9-ad19-f9899ab40fc5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"页码超出范围 (共 11 页): 1-12\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 11 页): 1-12\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "d30afa8d-8a44-47cf-b660-9ecbd9fa8a59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-14T13:04:23.945Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01VPQtqLZvPDn8yKBn8pBXjZ`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78f1965a-2f9a-4db9-ad19-f9899ab40fc5",
  "isSidechain": false,
  "requestId": "req_011Cb2WSfKur14C1duLniaGW",
  "type": "assistant",
  "uuid": "7f5c1fca-9b4b-4f6a-9300-7ba19bfd63da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwyGLwFtntYscczEnw1AL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18801,
      "cache_read_input_tokens": 31110,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 31110,
          "cache_creation_input_tokens": 18801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18801
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

_source line 49 · 2026-05-14T13:04:40.298Z_

<details><summary>↩ Tool result · `toolu_01VPQtqLZvPDn8yKBn8pBXjZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 19, \"total_citations\": 30, \"unique_cited_keys\": 19, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 15, \"online_not_found\": 1, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"liu2024kivi\", \"type\": \"inproceedings\", \"title\": \"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache\", \"authors\": \"Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and V...\", \"year\": \"2024\", \"venue\": \"ICML 2024\"}, {\"key\": \"hooper2024kvquant\", \"type\": \"inproceedings\", \"title\": \"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\", \"authors\": \"Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and ...\", \"year\": \"2024\", \"venue\": \"NeurIPS 2024\"}, {\"key\": \"lin2024qserve\", \"type\": \"inproceedings\", \"title\": \"QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving\", \"authors\": \"Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao an...\", \"year\": \"2025\", \"venue\": \"MLSys 2025\"}, {\"key\": \"he2024zipcache\", \"type\": \"inproceedings\", \"title\": \"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification\", \"authors\": \"Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zh...\", \"year\": \"2024\", \"venue\": \"NeurIPS 2024\"}, {\"key\": \"kang2024gear\", \"type\": \"misc\", \"title\": \"GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM\", \"authors\": \"Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"duanmu2024skvq\", \"type\": \"misc\", \"title\": \"SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models\", \"authors\": \"Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zh...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"zhang2023h2o\", \"type\": \"inproceedings\", \"title\": \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\", \"authors\": \"\", \"year\": \"2023\", \"venue\": \"NeurIPS 2023\"}, {\"key\": \"li2024snapkv\", \"type\": \"inproceedings\", \"title\": \"SnapKV: LLM Knows What You are Looking for Before Generation\", \"authors\": \"Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locate...\", \"year\": \"2024\", \"venue\": \"NeurIPS 2024\"}, {\"key\": \"ge2024fastgen\", \"type\": \"inproceedings\", \"title\": \"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs\", \"authors\": \"Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianf...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"xiao2024streamingllm\", \"type\": \"inproceedings\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"authors\": \"Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"liu2024scissorhands\", \"type\": \"inproceedings\", \"title\": \"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time\", \"authors\": \"Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie an...\", \"year\": \"2023\", \"venue\": \"NeurIPS 2023\"}, {\"key\": \"yang2024pyramidinfer\", \"type\": \"inproceedings\", \"title\": \"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference\", \"authors\": \"Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zh...\", \"year\": \"2024\", \"venue\": \"Findings of ACL 2024\"}, {\"key\": \"zuo2026ratequant\", \"type\": \"misc\", \"title\": \"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\", \"authors\": \"Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"lei2026arkv\", \"type\": \"misc\", \"title\": \"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs\", \"authors\": \"Jianlong Lei and Shashikant Ilager\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"li2025kvmix\", \"type\": \"misc\", \"title\": \"KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\", \"authors\": \"Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"zhang2025mixkvq\", \"type\": \"misc\", \"title\": \"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\", \"authors\": \"Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"kim2024squeezellm\", \"type\": \"inproceedings\", \"title\": \"SqueezeLLM: Dense-and-Sparse Quantization\", \"authors\": \"Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sh...\", \"year\": \"2024\", \"venue\": \"ICML 2024\"}, {\"key\": \"voita2019analyzing\", \"type\": \"inproceedings\", \"title\": \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\", \"authors\": \"Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov\", \"year\": \"2019\", \"venue\": \"ACL 2019\"}, {\"key\": \"michel2019sixteen\", \"type\": \"inproceedings\", \"title\": \"Are Sixteen Heads Really Better than One?\", \"authors\": \"Paul Michel and Omer Levy and Graham Neubig\", \"year\": \"2019\", \"venue\": \"NeurIPS 2019\"}], \"tex_citations\": [{\"key\": \"liu2024kivi\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"hooper2024kvquant\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"lin2024qserve\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"he2024zipcache\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"ge2024fastgen\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"lei2026arkv\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2023h2o\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"li2024snapkv\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zuo2026ratequant\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"liu2024kivi\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"hooper2024kvquant\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"lin2024qserve\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"he2024zipcache\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"kang2024gear\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"duanmu2024skvq\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"zhang2023h2o\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"li2024snapkv\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ge2024fastgen\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"liu2024scissorhands\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"xiao2024streamingllm\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"yang2024pyramidinfer\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"zuo2026ratequant\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"li2025kvmix\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"lei2026arkv\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"kim2024squeezellm\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"zhang2025mixkvq\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"voita2019analyzing\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"michel2019sixteen\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"zuo2026ratequant\", \"file\": \"method.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"zuo2026ratequant\", \"file\": \"experiments.tex\", \"line\": 30, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"liu2024kivi\", \"title\": \"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache\", \"status\": \"not_found\", \"confidence\": 0.335, \"matched_title\": \"Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"hooper2024kvquant\", \"title\": \"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=hooper vs api=gholami\"], \"note\": \"\"}, {\"key\": \"lin2024qserve\", \"title\": \"QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2024zipcache\", \"title\": \"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2024gear\", \"title\": \"GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"duanmu2024skvq\", \"title\": \"SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023h2o\", \"title\": \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2024snapkv\", \"title\": \"SnapKV: LLM Knows What You are Looking for Before Generation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SnapKV: LLM Knows What You are Looking for Before Generation\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=li vs api=cai\"], \"note\": \"\"}, {\"key\": \"ge2024fastgen\", \"title\": \"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2024streamingllm\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Efficient Streaming Language Models with Attention Sinks\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=xiao vs api=leonardo\"], \"note\": \"\"}, {\"key\": \"liu2024scissorhands\", \"title\": \"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2024pyramidinfer\", \"title\": \"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zuo2026ratequant\", \"title\": \"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lei2026arkv\", \"title\": \"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025kvmix\", \"title\": \"KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025mixkvq\", \"title\": \"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2024squeezellm\", \"title\": \"SqueezeLLM: Dense-and-Sparse Quantization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SqueezeLLM: Dense-and-Sparse Quantization\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"voita2019analyzing\", \"title\": \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"michel2019sixteen\", \"title\": \"Are Sixteen Heads Really Better than One?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Are Sixteen Heads Really Better than One?\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f5c1fca-9b4b-4f6a-9300-7ba19bfd63da",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "f4371937-ae52-4fe3-8613-927b3ab798b7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 19, \\\"total_citations\\\": 30, \\\"unique_cited_keys\\\": 19, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 15, \\\"online_not_found\\\": 1, \\\"online_mismatch\\\": 3}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"liu2024kivi\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache\\\", \\\"authors\\\": \\\"Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and V...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICML 2024\\\"}, {\\\"key\\\": \\\"hooper2024kvquant\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\\\", \\\"authors\\\": \\\"Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"NeurIPS 2024\\\"}, {\\\"key\\\": \\\"lin2024qserve\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving\\\", \\\"authors\\\": \\\"Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"MLSys 2025\\\"}, {\\\"key\\\": \\\"he2024zipcache\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification\\\", \\\"authors\\\": \\\"Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"NeurIPS 2024\\\"}, {\\\"key\\\": \\\"kang2024gear\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM\\\", \\\"authors\\\": \\\"Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"duanmu2024skvq\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models\\\", \\\"authors\\\": \\\"Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023h2o\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\\\", \\\"authors\\\": \\\"\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"NeurIPS 2023\\\"}, {\\\"key\\\": \\\"li2024snapkv\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SnapKV: LLM Knows What You are Looking for Before Generation\\\", \\\"authors\\\": \\\"Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locate...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"NeurIPS 2024\\\"}, {\\\"key\\\": \\\"ge2024fastgen\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs\\\", \\\"authors\\\": \\\"Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianf...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"xiao2024streamingllm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Efficient Streaming Language Models with Attention Sinks\\\", \\\"authors\\\": \\\"Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"liu2024scissorhands\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time\\\", \\\"authors\\\": \\\"Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie an...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"NeurIPS 2023\\\"}, {\\\"key\\\": \\\"yang2024pyramidinfer\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference\\\", \\\"authors\\\": \\\"Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of ACL 2024\\\"}, {\\\"key\\\": \\\"zuo2026ratequant\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\\\", \\\"authors\\\": \\\"Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"lei2026arkv\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs\\\", \\\"authors\\\": \\\"Jianlong Lei and Shashikant Ilager\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025kvmix\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\\\", \\\"authors\\\": \\\"Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2025mixkvq\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\\\", \\\"authors\\\": \\\"Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2024squeezellm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SqueezeLLM: Dense-and-Sparse Quantization\\\", \\\"authors\\\": \\\"Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sh...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICML 2024\\\"}, {\\\"key\\\": \\\"voita2019analyzing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\\\", \\\"authors\\\": \\\"Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"ACL 2019\\\"}, {\\\"key\\\": \\\"michel2019sixteen\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Are Sixteen Heads Really Better than One?\\\", \\\"authors\\\": \\\"Paul Michel and Omer Levy and Graham Neubig\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"NeurIPS 2019\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"liu2024kivi\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hooper2024kvquant\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lin2024qserve\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"he2024zipcache\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ge2024fastgen\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lei2026arkv\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023h2o\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2024snapkv\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zuo2026ratequant\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2024kivi\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hooper2024kvquant\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lin2024qserve\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"he2024zipcache\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2024gear\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"duanmu2024skvq\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023h2o\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2024snapkv\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ge2024fastgen\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"liu2024scissorhands\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiao2024streamingllm\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"yang2024pyramidinfer\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zuo2026ratequant\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2025kvmix\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lei2026arkv\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2024squeezellm\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2025mixkvq\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"voita2019analyzing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"michel2019sixteen\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zuo2026ratequant\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zuo2026ratequant\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"liu2024kivi\\\", \\\"title\\\": \\\"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.335, \\\"matched_title\\\": \\\"Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"hooper2024kvquant\\\", \\\"title\\\": \\\"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=hooper vs api=gholami\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lin2024qserve\\\", \\\"title\\\": \\\"QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"he2024zipcache\\\", \\\"title\\\": \\\"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2024gear\\\", \\\"title\\\": \\\"GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"duanmu2024skvq\\\", \\\"title\\\": \\\"SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023h2o\\\", \\\"title\\\": \\\"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2024snapkv\\\", \\\"title\\\": \\\"SnapKV: LLM Knows What You are Looking for Before Generation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SnapKV: LLM Knows What You are Looking for Before Generation\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=li vs api=cai\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ge2024fastgen\\\", \\\"title\\\": \\\"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiao2024streamingllm\\\", \\\"title\\\": \\\"Efficient Streaming Language Models with Attention Sinks\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Streaming Language Models with Attention Sinks\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=xiao vs api=leonardo\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liu2024scissorhands\\\", \\\"title\\\": \\\"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"yang2024pyramidinfer\\\", \\\"title\\\": \\\"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zuo2026ratequant\\\", \\\"title\\\": \\\"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lei2026arkv\\\", \\\"title\\\": \\\"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025kvmix\\\", \\\"title\\\": \\\"KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2025mixkvq\\\", \\\"title\\\": \\\"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2024squeezellm\\\", \\\"title\\\": \\\"SqueezeLLM: Dense-and-Sparse Quantization\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SqueezeLLM: Dense-and-Sparse Quantization\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"voita2019analyzing\\\", \\\"title\\\": \\\"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"michel2019sixteen\\\", \\\"title\\\": \\\"Are Sixteen Heads Really Better than One?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Are Sixteen Heads Really Better than One?\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 19, \"total_citations\": 30, \"unique_cited_keys\": 19, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 15, \"online_not_found\": 1, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"liu2024kivi\", \"type\": \"inproceedings\", \"title\": \"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache\", \"authors\": \"Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and V...\", \"year\": \"2024\", \"venue\": \"ICML 2024\"}, {\"key\": \"hooper2024kvquant\", \"type\": \"inproceedings\", \"title\": \"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\", \"authors\": \"Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and ...\", \"year\": \"2024\", \"venue\": \"NeurIPS 2024\"}, {\"key\": \"lin2024qserve\", \"type\": \"inproceedings\", \"title\": \"QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving\", \"authors\": \"Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao an...\", \"year\": \"2025\", \"venue\": \"MLSys 2025\"}, {\"key\": \"he2024zipcache\", \"type\": \"inproceedings\", \"title\": \"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification\", \"authors\": \"Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zh...\", \"year\": \"2024\", \"venue\": \"NeurIPS 2024\"}, {\"key\": \"kang2024gear\", \"type\": \"misc\", \"title\": \"GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM\", \"authors\": \"Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"duanmu2024skvq\", \"type\": \"misc\", \"title\": \"SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models\", \"authors\": \"Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zh...\", \"year\": \"2024\", \"venue\": \"\"}, {\"key\": \"zhang2023h2o\", \"type\": \"inproceedings\", \"title\": \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\", \"authors\": \"\", \"year\": \"2023\", \"venue\": \"NeurIPS 2023\"}, {\"key\": \"li2024snapkv\", \"type\": \"inproceedings\", \"title\": \"SnapKV: LLM Knows What You are Looking for Before Generation\", \"authors\": \"Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locate...\", \"year\": \"2024\", \"venue\": \"NeurIPS 2024\"}, {\"key\": \"ge2024fastgen\", \"type\": \"inproceedings\", \"title\": \"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs\", \"authors\": \"Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianf...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"xiao2024streamingllm\", \"type\": \"inproceedings\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"authors\": \"Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"liu2024scissorhands\", \"type\": \"inproceedings\", \"title\": \"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time\", \"authors\": \"Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie an...\", \"year\": \"2023\", \"venue\": \"NeurIPS 2023\"}, {\"key\": \"yang2024pyramidinfer\", \"type\": \"inproceedings\", \"title\": \"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference\", \"authors\": \"Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zh...\", \"year\": \"2024\", \"venue\": \"Findings of ACL 2024\"}, {\"key\": \"zuo2026ratequant\", \"type\": \"misc\", \"title\": \"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\", \"authors\": \"Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"lei2026arkv\", \"type\": \"misc\", \"title\": \"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs\", \"authors\": \"Jianlong Lei and Shashikant Ilager\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\": \"li2025kvmix\", \"type\": \"misc\", \"title\": \"KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\", \"authors\": \"Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"zhang2025mixkvq\", \"type\": \"misc\", \"title\": \"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\", \"authors\": \"Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen\", \"year\": \"2025\", \"venue\": \"\"}, {\"key\": \"kim2024squeezellm\", \"type\": \"inproceedings\", \"title\": \"SqueezeLLM: Dense-and-Sparse Quantization\", \"authors\": \"Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sh...\", \"year\": \"2024\", \"venue\": \"ICML 2024\"}, {\"key\": \"voita2019analyzing\", \"type\": \"inproceedings\", \"title\": \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\", \"authors\": \"Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov\", \"year\": \"2019\", \"venue\": \"ACL 2019\"}, {\"key\": \"michel2019sixteen\", \"type\": \"inproceedings\", \"title\": \"Are Sixteen Heads Really Better than One?\", \"authors\": \"Paul Michel and Omer Levy and Graham Neubig\", \"year\": \"2019\", \"venue\": \"NeurIPS 2019\"}], \"tex_citations\": [{\"key\": \"liu2024kivi\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"hooper2024kvquant\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"lin2024qserve\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"he2024zipcache\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"ge2024fastgen\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"lei2026arkv\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zhang2023h2o\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"li2024snapkv\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"zuo2026ratequant\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"cite\"}, {\"key\": \"liu2024kivi\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"hooper2024kvquant\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"lin2024qserve\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"he2024zipcache\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"kang2024gear\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"duanmu2024skvq\", \"file\": \"related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"zhang2023h2o\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"li2024snapkv\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ge2024fastgen\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"liu2024scissorhands\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"xiao2024streamingllm\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"yang2024pyramidinfer\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"zuo2026ratequant\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"li2025kvmix\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"lei2026arkv\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"kim2024squeezellm\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"zhang2025mixkvq\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"cite\"}, {\"key\": \"voita2019analyzing\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"michel2019sixteen\", \"file\": \"related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"zuo2026ratequant\", \"file\": \"method.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"zuo2026ratequant\", \"file\": \"experiments.tex\", \"line\": 30, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"liu2024kivi\", \"title\": \"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache\", \"status\": \"not_found\", \"confidence\": 0.335, \"matched_title\": \"Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"hooper2024kvquant\", \"title\": \"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=hooper vs api=gholami\"], \"note\": \"\"}, {\"key\": \"lin2024qserve\", \"title\": \"QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"he2024zipcache\", \"title\": \"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2024gear\", \"title\": \"GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"duanmu2024skvq\", \"title\": \"SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SKVQ: Sliding-window Key and Value Cache Quantization for Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023h2o\", \"title\": \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2024snapkv\", \"title\": \"SnapKV: LLM Knows What You are Looking for Before Generation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"SnapKV: LLM Knows What You are Looking for Before Generation\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=li vs api=cai\"], \"note\": \"\"}, {\"key\": \"ge2024fastgen\", \"title\": \"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2024streamingllm\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Efficient Streaming Language Models with Attention Sinks\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=xiao vs api=leonardo\"], \"note\": \"\"}, {\"key\": \"liu2024scissorhands\", \"title\": \"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"yang2024pyramidinfer\", \"title\": \"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zuo2026ratequant\", \"title\": \"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lei2026arkv\", \"title\": \"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025kvmix\", \"title\": \"KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2025mixkvq\", \"title\": \"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2024squeezellm\", \"title\": \"SqueezeLLM: Dense-and-Sparse Quantization\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SqueezeLLM: Dense-and-Sparse Quantization\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"voita2019analyzing\", \"title\": \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"michel2019sixteen\", \"title\": \"Are Sixteen Heads Really Better than One?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Are Sixteen Heads Really Better than One?\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "7f5c1fca-9b4b-4f6a-9300-7ba19bfd63da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference - **Deadline**: 2026-05-25 (ARR submission) - **格式**: ACL 模板, 正文 ≤8 页, mandato…",
  "leafUuid": "f4371937-ae52-4fe3-8613-927b3ab798b7",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP paper on KV cache mixed-precision quantization",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


### Assistant

_source line 52 · 2026-05-14T13:04:43.850Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now render the PDF correctly (11 pages).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4371937-ae52-4fe3-8613-927b3ab798b7",
  "isSidechain": false,
  "requestId": "req_011Cb2WURuppLTPb1Tv5BwkW",
  "type": "assistant",
  "uuid": "5c4f5dbf-d132-48c4-b164-75bfad7bac7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ds6oESfE4N59g5t7wqbbrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6274,
      "cache_read_input_tokens": 49911,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 49911,
          "cache_creation_input_tokens": 6274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6274
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

_source line 53 · 2026-05-14T13:04:45.442Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01AfsyBnWbsXrd5T8pKJ41Xv`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf",
  "pages": "1-11",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c4f5dbf-d132-48c4-b164-75bfad7bac7b",
  "isSidechain": false,
  "requestId": "req_011Cb2WURuppLTPb1Tv5BwkW",
  "type": "assistant",
  "uuid": "28e59994-b3b3-47d1-9a78-d90850401f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ds6oESfE4N59g5t7wqbbrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6274,
      "cache_read_input_tokens": 49911,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 49911,
          "cache_creation_input_tokens": 6274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6274
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

_source line 54 · 2026-05-14T13:04:48.105Z_

<details><summary>↩ Tool result · `toolu_01AfsyBnWbsXrd5T8pKJ41Xv`</summary>

```text
Error: result (6,519,905 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763888093.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763888093.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763888093.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28e59994-b3b3-47d1-9a78-d90850401f4c",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "7c6a5269-264c-484c-8bcd-6f5181732b8b",
  "toolUseResult": "Error: result (6,519,905 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763888093.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763888093.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763888093.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 54,
    "serialized_bytes": 6519942,
    "serialized_sha256": "772f6f22fa73783cf996323a73c2b3a081584ff2f3b0df6056e5c34dd0d8e01f",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "28e59994-b3b3-47d1-9a78-d90850401f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 1  **你的审查侧重：方法严谨性 + 实验有效性**  ### Venue 信息 - **目标**: EMNLP 2026 Main Conference - **Deadline**: 2026-05-25 (ARR submission) - **格式**: ACL 模板, 正文 ≤8 页, mandato…",
  "leafUuid": "7c6a5269-264c-484c-8bcd-6f5181732b8b",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP paper on KV cache mixed-precision quantization",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d"
}
```

---


### Assistant

_source line 57 · 2026-05-14T13:04:51.044Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF images are too large to load directly. Let me render a few pages at a time to check formatting visually.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c6a5269-264c-484c-8bcd-6f5181732b8b",
  "isSidechain": false,
  "requestId": "req_011Cb2WV1bcxo9qLy1aQCRD2",
  "type": "assistant",
  "uuid": "6ed50980-646c-4fae-b244-27cd216b57d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1cVmUE4HgHqqVV43HJS11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 56185,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 56185,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 58 · 2026-05-14T13:04:52.131Z_

PDF 太大，分批渲染关键页面检查排版。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ed50980-646c-4fae-b244-27cd216b57d8",
  "isSidechain": false,
  "requestId": "req_011Cb2WV1bcxo9qLy1aQCRD2",
  "type": "assistant",
  "uuid": "fcd4f656-35ba-4bd5-99fe-26a06494e470",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1cVmUE4HgHqqVV43HJS11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 56185,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 56185,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 59 · 2026-05-14T13:04:52.810Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01BiCRA7jW2oTJDZyjugnCXx`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf",
  "pages": "1-3",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcd4f656-35ba-4bd5-99fe-26a06494e470",
  "isSidechain": false,
  "requestId": "req_011Cb2WV1bcxo9qLy1aQCRD2",
  "type": "assistant",
  "uuid": "b00c7786-9389-45a9-8e36-f8df427022d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1cVmUE4HgHqqVV43HJS11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 56185,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 56185,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 60 · 2026-05-14T13:04:53.422Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01GWGry7gpMJhGbJrb4Gu3GT`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf",
  "pages": "8-9",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b00c7786-9389-45a9-8e36-f8df427022d1",
  "isSidechain": false,
  "requestId": "req_011Cb2WV1bcxo9qLy1aQCRD2",
  "type": "assistant",
  "uuid": "6d63d1b3-a614-43d4-8205-f98fd6775c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1cVmUE4HgHqqVV43HJS11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 56185,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 56185,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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


### Large event (continued)

````text
### Tool result

_source line 61 · 2026-05-14T13:04:53.824Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01BiCRA7jW2oTJDZyjugnCXx`&lt;/summary>

```text
Error: result (1,922,701 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763893819.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763893819.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763893819.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b00c7786-9389-45a9-8e36-f8df427022d1",
  "isSidechain": false,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "type": "user",
  "uuid": "c92c76eb-0eb1-4af5-96d1-f85dbb1998da",
  "toolUseResult": "Error: result (1,922,701 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763893819.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763893819.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/957b9df0-67d4-4b3a-8244-4b6f12b8919d/tool-results/mcp-agent-ml-research-pdf_to_images-1778763893819.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p1.png\", \"base64\": \"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HjrPsygAAPGQRQEgNW3evLl06dI1atTQiDJjxozoak8++eTj/2PS0axZs1q1alWvXr0ePXrs2LEj+i0LFizo27dvgwYN2rdv//LLL9tX/3711VePW9avX79r165+/frJ1GSa7777rtacPXv242cyzZNMZf589tln//rrL7vCBx98EI4M1dO8eXPJOQ888MCWLVvM1CZMmNC4ceObbrppyJAhhw8fdjR4//79I0eO7NChg7S5T58+8+fP15ccHzF37lwplAp2ocyU1j927NgLL7wgDahbt66kwenTp99///0e10inTp1uv/12XR1VqlSJrrN06VKtUKxYMZep/fHHH9IS/TP5WTTerPldRHYW3bNnz8CBAxs2bCgLX9bR6dOnTR3H2t+9e7dsrj179qxTp46sx7feestU27hxY7du3WrXrn3nnXcuXLhQP8Lxdns84RUrVtx3330ynVtvvVVW+vjx49955x33GXSZWth14wkntPsAAAJAFgWA1NS/f/+hQ4dKt14jyg033BBdTbr4uXPnNhWqV68uWS5TpkwZMmQwJQULFrQHzjly5EiXLl2kXDr6kh/mzZuXPn36iy+++MsvvzQVJHmaCsaYMWMkUGXPnl1LnnrqKVNz27Zt1113nZZ3795dwlU4Ej+aNm2aM2fOOXPm/P3335J8pD0asTp27JgtWza9hFUmLs1o06aNfES6dOlMYbVq1ewzwDKDUi1jxoyff/65VG7WrJnUuffee81wqVJzypQp2oyuXbuauZB2aqHEDDMpSWXly5eXT5dQ/fvvv48aNUoaI83zsjoOHDggC/PQoUNly5bVKS9evNhRTZKbvlq1alVvq/q/kplFXWbN1yIKW1m0RIkSNWrUuOOOO3Q0I1mz8kHhyNqXRurbJS7myZMnR44cWjJ8+HBZOLJlXnjhhVr40UcfmY/YsmWLTErLv/32W1MuyVM2A2nAjz/+uGrVqvr168urTz/9tPsMxptaOKmNJ+xz9wEABIYsCgCp5uTJk0WKFJFO9rFjx/Lly6f97JjjsjRp0sS8Kv1+yYTSz5ZAKP1vU2jfsnjfffeZQn1macuWLeXPLFmy6NWkkgH046644oqvv/5aCjt37mxKpOaJEydMzWXLlmnNfv366af07t1bgrT+WbNmTVNHAqrkH5m1tWvXXnDBBaawZMmSI0eOPH36tOTh6NCy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mDFjJOvqST+ZO/OcTMkzxYoV+/333827JCVKMpGS6KGJjb/++kuWXoUKFWLeUDpw4MCQxVy5ahw+fLh169amvFSpUnrHo/nQ/v37y+yPGDHCnlqXLl10UvKheg5Q1vv06dP1mtXffvstZlOTnDWPiyj8vywqb5dNRVZKOPLkT3OJb7ly5fRmYHsEZj2fOWzYMC2cP3++KezRo4cW6iNwRo4cqYXmJw/JovL/oUOHOpaJWVDuMxg9tbDnjcf77gMACAxZFAAC1bVrV3PSJkuWLDfccMN3332nL91zzz36QE511VVXSY9czzoaEpwkVdatW9cu1GeHipUrV5YvX1662hKlmjRpkjlzZolGGkSls54vXz59o7REEsKsWbP0ckeRP39+E2Vtzz77rLykecY4cOCAYyiapk2bymf961//sgs7deokEUVyjpZIWnjwwQfNRCRRPProo5kyZWrevPmAAQPk0yU/23cYhiPnu/4fe+cBn9P1//FYP3uWGrUVpVRVtahZq4qiZmpU1WhpS6lqUX/Err23mrErds2G2itEiBGbEIKQRBLi+X/yfDmu+8zEk5vg837llddzzz333LPuud/PPUspCoDwfX1906RJkzlz5goVKrRo0WLw4MEm8zhVaPj8+fO3bt26ffv2CKpIkSKW3bwCbqHm6MIbtJw6tWXLFtxOdqpUQF7qOrQh2lVKc+XKVbFixZw5c6KIIVN9fHyUtwULFqheYsWbb76J8s2dO7fqunQz765pa5klh0lzMotMZi3aqFGjK1euQEOWK1cO1QN6DLq0Q4cO0NjiZ9q0aaoT282sb6E8586dmy5dOuWIinTo0KFhw4ahFinHggULomJPmTJFW6MyZcoEJY+aBsmNVOOmuHWlSpWSJUv2888/iz60k0CroTlZeWL7+BBCCDEGalFCCHlluX79+saNG2GUWx19Ggd2795dpUoVlwRlFYiKw4cPI843btyw6gEiDSJn7dq1Sg/jUKfcZCjpo0ePkHAvLy8EqN2OJZ64fPny8uXLJ06cOHXq1E2bNkHjxcddnEmaM1kEjh8/rn4HBQUhzvv373dm55sX5MKFC5cuXcIPFPHWrVtR1qoT1fRiZeew8hBCCElsUIsSQgixCTTM5s2b161bJ2Lml19+0a4QQwghhBASZ6hFCSGE2GTRokUygnHNmjXBwcFvv/22AV1n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BMRNseWiiYQhQ4bkzp179uzZcSVOGNkJ3FcZ+bXPyTMDQed485NPPlm4cOGQN0slHn766SfSvcnBfffdN3z48GtiI+j69eubNWtWtGjRm2++uWrVql26dLmKRHrJkiW1atWSOmzevPm7774brZiHDh1asGDBunXrJqULFgsLi3jAclGLlAKG2zx58mBPly9fHrrF+FepUiWsh5B7SlMsqA253tN1LXBKxvTp0+XMc0o+dDBq1KiA46PSTtwkEo4ePYo66tq1ayTHHywU77333rPPPjtr1ix7G5yFhYXFtQjLRS1SEM6fPz9//vyhQ4eOGTPmq6++sndSufDXX3+NHDnyVQeDBg366KOPrnaOrj5WrVo1cOBAqRMqJxIXXNcZIJ/jx49/NQbmrQMWFhYWFhYWFgmB5aIWFhYWFhYWFhYWFhYWSQ3LRS0sLCwsLCwsLCwsLCySGpaLWlhYWFhYWFhYWFhYWCQ1LBe1sLCwsLCwsLCwsLCwSGpYLmphYWFhYWFhYWFhYWGR1LBc1CL+OHny5DUX87UFWw9JCf+r3k+fPq3XmVy+fDlWJ8x//fXXxYsXkyZv8QB5S273v1u/1uFw7ty55cuXv/HGG59//jlyFcknFy5c+PLLL/fu3Rv1zOzbt++9994bP378jh07oh654siRIxMnTvzzzz81BHH97LPP/vvf//p8RamXLl26devWxMtYtEABffTD5s2bV69enZDIXbUXCf7555+/rsQ1d03Ot99+O336dP97pxCkyZMnJ71HdJp7w4YNkyZNWrJkSdAZ3E+dOpXEebCwSJ6wXNQinhg9enQgEFi4cOE1FPO1BVsPSQPMl+7duxcpUqRXr17eX7HPxowZU69evXTp0ikNaNCgwY033vjbb7+Fi5OvcufOfffddycwb5988smTTz6ZP3/+F198MYFRKb744otWrVply5YtIcZuFHH8+PGBAwdWrFixWrVqVzsvyRFHjx6tVasWUvryyy+jECpXruz/Pob4Sy+9lCVLFl6GvEU3M2+99Va/fv2++eabwoULE79Y1YmB//znP8Q/dOjQoGO1d+jQIUOGDISQdMj3Dx482K1bt4wZM/LO1KlTEylX0cLs2bNfeeWVf//91/vTjBkz0EWUokePHvGO36y9yPHll182a9Ys4CBt2rSlSpXKkydPoUKFatasiewhh/HOT5Kh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ouPq1avdunWT8/N+vZfdyZgwYUK+fPkoeevWrcObM00hNjLCm63B/QnDRQ0MDAwMDBIGYTmffPPmzZdffrlv374OaX755Zews4uw+4i6Q57lAGhJPHNRr0WHUqVKFW9c1Bs30nJXQ4wR3nVcFEycODEuuOjRo0cbNGgwf/788GZrcH/CcFEDAwMDA4MEwJQpU9atWxc/z/r333/Dzi7CruAGQnw2lDM+/fTT+OeiQPxOxRsXjQtpuavx3nvv3aVcdMWKFXHBRQ0MwgjDRQ0MDAwMDOIb27dvT548eYyHPMOFsLOLcePGkWG4cnNAPDeUMwwXvT9huKjBXYS//vpr69at69at41d5KxRcv379559/3rRp04YNG3bu3Onrgfx///tfdHR0PHhD0GG4qIGBgYGBQbxi79694mY5IiICtUB5q/r7779REfhD5NSpU8VbleD06dPffffd+PHjYWV6vACWsnz5cptTq5s3b+7YsWPChAnoo5cvXw6NXezZs4eSfP3113/88ceJEyckcv78+eK+eJMF5dFq//79+/bt47kLFy5ctGjRb7/9JgmorySgPBKDPmR70JkzZ3gKFHfVqlVqR65vQ+3evVtyEEfTVHnTLdic39JQ//zzD201efLkLVu26C25ZMkSmuWnn34K1hqQzkUjIyM/++wznuLrSyy0R8O6v7DgayNH56Iol5v+H3vvHm9Ttf//L7eQe245Eiq5h8opRRQOiogURVHUcS2km3ggFCGXSEIhci1EuohOUuhyEKKoVCoVIQl1Puv3/M7XY4/fMOdac829rb1tzNcf+7HnWGOOOS7v8R7v17i8hwVzjXDMlgqOINLy9ddfL1y4cMqUKeTfPpxs54e2o5lcIVHnlmw9HjhwwJRXVzHv2LFj2rRpfDeJzpnIw8svv0x/ee+991wcnke+tW/fPj5H61BkcuJNAYFctGgRGUOM08xFDx06tGzZMmXD613vyJEjdNuoU7HPPfecfW+Wv6j4/4pIIIEkCBWxuSjNareLuaqdVnB15CCgHd966y07hAIifgghtUpnTO2++iDygJTClKZPnz579my0TarSP0OAfljlAJHTP0au6LPr168n5N1334Wp8g9/bTpKk1GrhH/yyScZmeeQi4YIESJEiBAZCphVpUqVZCMOGDAAkoll2aJFixw5ctx2223PPPOMfNUMGjQo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9vjiomDv3r25xkU9lb9jx4527drNnTs3R1/6+++/lyhRwsNF40pj9mUDRZQSLnrC9PoImULERSNEiBAhQoTjDD/++GPVqlVtXzsPF3Xck2bNsc/nn3/+ccRFN23a9MQTTxztUpw4yOn6fPPNN487LgrOOuus3OGiN954Yy68xQ+d5mVz0bjIfvEUsyCbXBSGfOedd2azJBGOR0RcNEKECBEiRDjO8N13340YMcJO8XNR0L9/f/1zHHHRvXv3Vq5cOdo8nCrkQn1GXDQA48ePp3Jy+i1xEYaLpqR4KeGiHTt2vOyyy7JZkgiO6xSzbt26d955h7+eIxIPHz78ySefrF69+t13392wYYO9qYf/SSGdX7du3Zqbp3JGXDRChAgRIkQ47hGXixoYLoot8t577z333HP/+te//Ldt3759+vTp06ZN+/zzz5O+EXtly5Ytv//++/z58//5z3+aRVpSNm7cOGXKlJdffpl74j775Zdfzps37/nnn1+7di1FMumUsGnTphT15ptvxiT6+OOPAwrw66+/Ll++/Nlnn6UA+/fv9/y6Y8eOGTNmTJgwYcWKFcauInG1i82bNyvlww8/VAommv34rl27eHzmzJnciW3nyZxiU/hXXnnlu+++S1JNjoNF+MUXX4TP3AbfxVscd5V7yZIlkyZNss+dNvj+++/5lY+lQuyqCF+fNB/G6+TJk996663du3d7DhI/ePDgypUrEZtXX32Vwnue9XDRjz76aHUGjCDR4kqxqyJA3hJJV5hi85l61zfffMPloUOHTHl27txpnjVc9IcffqAMU6dOjXu4caK6Ffbt2/faa685bkvxD5nYp1jPnTtXG7n1djMZxFNvvPGGnQ/CzJfqMxEYpIvPN9/IF5GybNkyz9uPHDnCh1O22bNn+wUjLhe1pdFfPATb1JXpI+SslEQHdNtcFPVCl6SuqHb9mrQ5aOX777+fHGrXrq30gNOw1SPGjRu3ePHikEesn1SAfC53gd7TP0aq0bSofVLefvtteg3/8Fd0lL8k6in9g5zkGh2NuGiECBEiRIhw3CMMF8XIO++886pUqXL66adzOXr0aHMDBuI999zTu3fv8ePHd+jQ4ZRTTnnkkUfiZoVB88wzz1x88cXkMHHixI4dOypOEmYNv2L48tMDDzyANTNq1KiCBQu2adPm22+/NY9jSnbv3r1t27av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
```

---
