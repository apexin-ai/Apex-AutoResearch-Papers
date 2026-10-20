# Research conversation: [Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证） ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantizatio — Part 1 of 2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-2-round-2-reviewer-1-when-does-non-uniform-kv-cache-quantizatio.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/21/21a589f852113f345294.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-15T15:25:16.362Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T15:25:16.362Z",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "content": "[Round 2 审稿请求]:\n## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）\n\n### 论文信息\n- **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\n- **路径**: `projects/ratekv/docs/paper/main.tex`（模块化: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）\n- **目标 venue**: EMNLP 2026 Main Conference\n- **格式要求**: ACL template, 正文 ≤8 页（不含 references/limitations/appendix）, double-blind (ARR)\n- **截止日期**: 2026-05-25\n\n### 你的审查侧重\n\n**核心关注**：技术声明的严谨性和实验证据的充分性。\n\n重点审查以下方面：\n\n1. **Compounding claim 的因果论证**：论文声称 2-bit distortion compounding 是 unconstrained solver 失败的根因。super-additivity 数据 (1.56×–4.89×) 是否足以支撑因果而非仅为相关？是否有替代解释？\n\n2. **N=1 Spread 泛化性**：7 个模型中仅 Qwen2.5-7B 展示 spread pattern 且获益。这个 contribution 的泛化性如何？是否本质上是一个 model-specific finding？\n\n3. **Decision rule 拟合风险**：2 个自由参数 (concentration threshold ~0.50, t1/t5 ~0.70) 在 7 个样本上 7/7 正确分类，且正样本仅 1 个。这是否构成严重的 overfitting 风险？thresholds 的 sensitivity 如何？\n\n4. **KIVI 对比的公平性和意义**：KIVI+MCKP = KIVI alone (9.90)，论文将自身方法定位为 \"symmetric-only\" 环境有价值。这一定位是否合理？symmetric-only 的实际应用场景有多广？\n\n5. **统计可靠性**：\n   - 3-seed stability (10.99±0.06) 是否足够？\n   - Cross-dataset agreement (96-97%) 的统计显著性\n   - Downstream eval 仅 0-shot，无 confidence intervals\n\n6. **实验覆盖**：\n   - 是否缺少重要 baseline（如其他 mixed-precision KV cache 方法）？\n   - 模型规模上限 14B，是否足以支撑结论？\n   - 长文本评估仅 Qwen+Llama 两个模型\n\n7. **Runtime benchmark caveat**：仅 PyTorch-level simulation，8.5% overhead upper bound。对实际部署意味着什么？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary (2-3 句)\n\n## Strengths\n- S1: ...\n- S2: ...\n\n## Weaknesses (按严重程度排序)\n- W1 [critical/major/minor]: ...\n- W2: ...\n\n## Questions (需要作者回答)\n- Q1: ...\n\n## Missing References (如有)\n\n## Overall Assessment\nScore: [strong reject / weak reject / borderline / weak accept / strong accept]\nConfidence: [low / medium / high]\n```"
}
````

---


### Runtime record

_source line 2 · 2026-05-15T15:25:16.366Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T15:25:16.366Z",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


## Round 1

## Round 1

94 recorded events


### User

_source line 3 · 2026-05-15T15:25:16.398Z_

[Round 2 审稿请求]:
## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）

### 论文信息
- **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic
- **路径**: `projects/ratekv/docs/paper/main.tex`（模块化: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, conclusion.tex, appendix.tex）
- **目标 venue**: EMNLP 2026 Main Conference
- **格式要求**: ACL template, 正文 ≤8 页（不含 references/limitations/appendix）, double-blind (ARR)
- **截止日期**: 2026-05-25

### 你的审查侧重

**核心关注**：技术声明的严谨性和实验证据的充分性。

重点审查以下方面：

1. **Compounding claim 的因果论证**：论文声称 2-bit distortion compounding 是 unconstrained solver 失败的根因。super-additivity 数据 (1.56×–4.89×) 是否足以支撑因果而非仅为相关？是否有替代解释？

2. **N=1 Spread 泛化性**：7 个模型中仅 Qwen2.5-7B 展示 spread pattern 且获益。这个 contribution 的泛化性如何？是否本质上是一个 model-specific finding？

3. **Decision rule 拟合风险**：2 个自由参数 (concentration threshold ~0.50, t1/t5 ~0.70) 在 7 个样本上 7/7 正确分类，且正样本仅 1 个。这是否构成严重的 overfitting 风险？thresholds 的 sensitivity 如何？

4. **KIVI 对比的公平性和意义**：KIVI+MCKP = KIVI alone (9.90)，论文将自身方法定位为 "symmetric-only" 环境有价值。这一定位是否合理？symmetric-only 的实际应用场景有多广？

5. **统计可靠性**：
   - 3-seed stability (10.99±0.06) 是否足够？
   - Cross-dataset agreement (96-97%) 的统计显著性
   - Downstream eval 仅 0-shot，无 confidence intervals

6. **实验覆盖**：
   - 是否缺少重要 baseline（如其他 mixed-precision KV cache 方法）？
   - 模型规模上限 14B，是否足以支撑结论？
   - 长文本评估仅 Qwen+Llama 两个模型

7. **Runtime benchmark caveat**：仅 PyTorch-level simulation，8.5% overhead upper bound。对实际部署意味着什么？

### 输出格式

请按以下结构输出审稿意见：

```
## Summary (2-3 句)

## Strengths
- S1: ...
- S2: ...

## Weaknesses (按严重程度排序)
- W1 [critical/major/minor]: ...
- W2: ...

## Questions (需要作者回答)
- Q1: ...

## Missing References (如有)

## Overall Assessment
Score: [strong reject / weak reject / borderline / weak accept / strong accept]
Confidence: [low / medium / high]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "69216ab7-0d55-4ce1-bd6d-2b4cda5c4a97",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-15T15:25:16.397Z_

```json
{
  "parentUuid": "69216ab7-0d55-4ce1-bd6d-2b4cda5c4a97",
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
  "uuid": "ac5d7656-22ba-4212-a8a4-3054206531bf",
  "timestamp": "2026-05-15T15:25:16.397Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 5 · 2026-05-15T15:25:16.397Z_

```json
{
  "parentUuid": "ac5d7656-22ba-4212-a8a4-3054206531bf",
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
  "uuid": "0981c2a8-ae1e-4b81-afd6-b5fe3661c072",
  "timestamp": "2026-05-15T15:25:16.397Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 6 · 2026-05-15T15:25:16.397Z_

```json
{
  "parentUuid": "0981c2a8-ae1e-4b81-afd6-b5fe3661c072",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "13be7569-e14b-4e8a-bd21-7b16793500f4",
  "timestamp": "2026-05-15T15:25:16.397Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
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
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Assistant

_source line 8 · 2026-05-15T15:25:24.484Z_

<details><summary>Logged reasoning block</summary>

```text
The user (Review Director) is asking me to perform Round 2 review of the paper "When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic" for EMNLP 2026. I need to:

1. First, follow the session start skill and Step 0 (search for EMNLP 2026 / ACL ARR reviewer guidelines)
2. Read the paper via pdf_to_images
3. Conduct a thorough review focusing on the 7 specific areas the Director highlighted


4. Now I'll search for the relevant reviewer guidelines and pull up the paper to begin my analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13be7569-e14b-4e8a-bd21-7b16793500f4",
  "isSidechain": false,
  "requestId": "req_011Cb4b1CzXt82ADwiXvT2Yi",
  "type": "assistant",
  "uuid": "ada337ce-4b33-4ffc-9609-401fc0c691c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KTzMnmawxb16T33jTqhRC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14909,
      "cache_read_input_tokens": 11841,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14909
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

_source line 9 · 2026-05-15T15:25:24.521Z_

开始 Round 2 审稿。先搜索 EMNLP 2026 / ACL ARR reviewer guidelines，同时渲染论文 PDF。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ada337ce-4b33-4ffc-9609-401fc0c691c3",
  "isSidechain": false,
  "requestId": "req_011Cb4b1CzXt82ADwiXvT2Yi",
  "type": "assistant",
  "uuid": "036d8282-ae19-4b1e-a17d-231d4840f961",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KTzMnmawxb16T33jTqhRC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14909,
      "cache_read_input_tokens": 11841,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14909
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

_source line 10 · 2026-05-15T15:25:24.554Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015f32WurXLXUXhWn2TuoQkW`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "036d8282-ae19-4b1e-a17d-231d4840f961",
  "isSidechain": false,
  "requestId": "req_011Cb4b1CzXt82ADwiXvT2Yi",
  "type": "assistant",
  "uuid": "b4c73521-9c43-4d8a-807e-02d03a977627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KTzMnmawxb16T33jTqhRC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14909,
      "cache_read_input_tokens": 11841,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14909
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

_source line 11 · 2026-05-15T15:25:24.560Z_

<details><summary>↩ Tool result · `toolu_015f32WurXLXUXhWn2TuoQkW`</summary>

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
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__review_reviewer_post_to_director"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4c73521-9c43-4d8a-807e-02d03a977627",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "200c7b0e-413d-4071-96bd-29baa4f082ce",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "b4c73521-9c43-4d8a-807e-02d03a977627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-15T15:25:27.750Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WYQHMa4X8EXaHf9fxg7cBm`</summary>

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
  "parentUuid": "200c7b0e-413d-4071-96bd-29baa4f082ce",
  "isSidechain": false,
  "requestId": "req_011Cb4b1pPWvcFGByEMya8VZ",
  "type": "assistant",
  "uuid": "c6522f2a-f972-4d5d-a108-8712df03db3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmrrDkbvifwG8hbXXcE9Rf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 26750,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 187,
          "cache_read_input_tokens": 26750,
          "cache_creation_input_tokens": 1476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1476
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

_source line 13 · 2026-05-15T15:25:28.888Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01LQEsYw29KK3MYpBs2WiG26`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf",
  "pages": "1-10",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6522f2a-f972-4d5d-a108-8712df03db3c",
  "isSidechain": false,
  "requestId": "req_011Cb4b1pPWvcFGByEMya8VZ",
  "type": "assistant",
  "uuid": "0ff3e2aa-c094-48d4-b54c-c71dad34d526",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmrrDkbvifwG8hbXXcE9Rf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 26750,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 187,
          "cache_read_input_tokens": 26750,
          "cache_creation_input_tokens": 1476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1476
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

_source line 14 · 2026-05-15T15:25:37.647Z_

<details><summary>↩ Tool result · `toolu_01WYQHMa4X8EXaHf9fxg7cBm`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

I've found comprehensive information about ACL ARR 2025-2026 reviewer guidelines and scoring criteria. Here's a summary of the key information:

## ARR Reviewer Guidelines & Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

**Soundness Score:** The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

**Excitement Score:** Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Overall Recommendation Scale

The recommendation scale includes: 2 = Resubmit next cycle (paper needs substantial revisions by next ARR cycle), 1.5 = Resubmit after next cycle (substantial revisions cannot be completed by next cycle), and 1 = Do not resubmit (paper must be fully redone or not relevant to the *ACL community).

## Reviewer Accountability Policies

Starting in May 2025, ARR adopts the new policy on 'highly irresponsible' (meta-)reviewers. The program chairs and ARR EiCs will consider egregious cases including extremely terse reviews, unprofessional tone, and LLM-generated reviews. The 'highly irresponsible' reviewers or chairs may have their work desk-rejected from the current cycle, and ineligible for resubmission or commitment during the following ARR cycle.

## Reproducibility Assessment

Reviewers assess whether there is enough information in the paper for a reader to reproduce the main results, use results presented in the paper in future work (e.g., as a baseline), or build upon this work.

You can access the full reviewer guidelines at aclrollingreview.org/reviewerguidelines and the review form at aclrollingreview.org/reviewform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6522f2a-f972-4d5d-a108-8712df03db3c",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "608440c8-8dce-4cdc-9deb-454309394b39",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_0118zdDw7qPLbqcYfQwnd3oT",
        "content": [
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "Main Conference - ACL 2026",
            "url": "https://2026.aclweb.org/calls/main_conference_papers/"
          }
        ]
      },
      "I've found comprehensive information about ACL ARR 2025-2026 reviewer guidelines and scoring criteria. Here's a summary of the key information:\n\n## ARR Reviewer Guidelines & Requirements\n\nAll reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.\n\n## Review Scoring System\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n**Soundness Score:** The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.\n\n**Excitement Score:** Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.\n\n## Overall Recommendation Scale\n\nThe recommendation scale includes: 2 = Resubmit next cycle (paper needs substantial revisions by next ARR cycle), 1.5 = Resubmit after next cycle (substantial revisions cannot be completed by next cycle), and 1 = Do not resubmit (paper must be fully redone or not relevant to the *ACL community).\n\n## Reviewer Accountability Policies\n\nStarting in May 2025, ARR adopts the new policy on 'highly irresponsible' (meta-)reviewers. The program chairs and ARR EiCs will consider egregious cases including extremely terse reviews, unprofessional tone, and LLM-generated reviews. The 'highly irresponsible' reviewers or chairs may have their work desk-rejected from the current cycle, and ineligible for resubmission or commitment during the following ARR cycle.\n\n## Reproducibility Assessment\n\nReviewers assess whether there is enough information in the paper for a reader to reproduce the main results, use results presented in the paper in future work (e.g., as a baseline), or build upon this work.\n\nYou can access the full reviewer guidelines at aclrollingreview.org/reviewerguidelines and the review form at aclrollingreview.org/reviewform."
    ],
    "durationSeconds": 9.889497352000001
  },
  "sourceToolAssistantUUID": "c6522f2a-f972-4d5d-a108-8712df03db3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-15T15:25:41.526Z_

<details><summary>↩ Tool result · `toolu_01LQEsYw29KK3MYpBs2WiG26`</summary>

```text
Error: result (8,894,986 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778858741510.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778858741510.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ff3e2aa-c094-48d4-b54c-c71dad34d526",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "8f4635aa-5706-4ca8-8cdb-0744683ebf1c",
  "toolUseResult": "Error: result (8,894,986 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778858741510.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778858741510.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 15,
    "serialized_bytes": 8895023,
    "serialized_sha256": "b55beb50cc6f64f2bc5b8d1e075c4b678c05163cc359383deb02f6924c29849a",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "0ff3e2aa-c094-48d4-b54c-c71dad34d526",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "8f4635aa-5706-4ca8-8cdb-0744683ebf1c",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Assistant

_source line 18 · 2026-05-15T15:25:47.515Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF rendering was too large to return directly. Let me fetch the review form details and read the PDF images. I need to read the rendered images from the output directory and also get the full review form from ACL ARR.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f4635aa-5706-4ca8-8cdb-0744683ebf1c",
  "isSidechain": false,
  "requestId": "req_011Cb4b34hGPSw4P6N9eAhDo",
  "type": "assistant",
  "uuid": "f64297ca-b4e8-47f1-8bc9-f8dce872934a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114GNUYY5XVivgmaJoX8DT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1654,
      "cache_read_input_tokens": 28226,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 28226,
          "cache_creation_input_tokens": 1654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1654
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

_source line 19 · 2026-05-15T15:25:48.367Z_

PDF 渲染完成但结果太大。让我获取 ACL ARR review form 详细评分标准，同时逐页查看论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f64297ca-b4e8-47f1-8bc9-f8dce872934a",
  "isSidechain": false,
  "requestId": "req_011Cb4b34hGPSw4P6N9eAhDo",
  "type": "assistant",
  "uuid": "4544661f-b78c-4e5f-8cb7-40c3172fed4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114GNUYY5XVivgmaJoX8DT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1654,
      "cache_read_input_tokens": 28226,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 28226,
          "cache_creation_input_tokens": 1654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1654
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

_source line 20 · 2026-05-15T15:25:48.647Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J7sYbkjWiBYUbuuK3CxPQT`</summary>

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
  "parentUuid": "4544661f-b78c-4e5f-8cb7-40c3172fed4f",
  "isSidechain": false,
  "requestId": "req_011Cb4b34hGPSw4P6N9eAhDo",
  "type": "assistant",
  "uuid": "675b2b00-77e9-49cf-b33f-74f14be90b61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114GNUYY5XVivgmaJoX8DT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1654,
      "cache_read_input_tokens": 28226,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 28226,
          "cache_creation_input_tokens": 1654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1654
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

_source line 21 · 2026-05-15T15:25:48.650Z_

<details><summary>↩ Tool result · `toolu_01J7sYbkjWiBYUbuuK3CxPQT`</summary>

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
  "parentUuid": "675b2b00-77e9-49cf-b33f-74f14be90b61",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "cf225a5f-6ada-46c2-8a76-ebc842e6a265",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "675b2b00-77e9-49cf-b33f-74f14be90b61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-15T15:25:53.417Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0183makVqgrFtZBi1z9vsZWz`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (numeric ranges), and descriptions. Include soundness, excitement, overall recommendation, confidence, reproducibility, and any other dimensions. Return the full scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf225a5f-6ada-46c2-8a76-ebc842e6a265",
  "isSidechain": false,
  "requestId": "req_011Cb4b3bEJk2JJNrBXR4EhZ",
  "type": "assistant",
  "uuid": "97bcd2d9-9031-4c62-b43d-36f98552794c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vNU7yFopecChsg6upEpD6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 29880,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 29880,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 23 · 2026-05-15T15:25:54.069Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ALRjhJBpK8s2rpezJvixva`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/ 2>/dev/null | head -20",
  "description": "List rendered PDF page images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97bcd2d9-9031-4c62-b43d-36f98552794c",
  "isSidechain": false,
  "requestId": "req_011Cb4b3bEJk2JJNrBXR4EhZ",
  "type": "assistant",
  "uuid": "ae0d3adf-2567-4f9b-aaed-1521eee850a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vNU7yFopecChsg6upEpD6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 29880,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 29880,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 24 · 2026-05-15T15:25:54.235Z_

<details><summary>↩ Tool result · `toolu_01ALRjhJBpK8s2rpezJvixva`</summary>

```text
main_p1.png
main_p10.png
main_p2.png
main_p3.png
main_p4.png
main_p5.png
main_p6.png
main_p7.png
main_p8.png
main_p9.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae0d3adf-2567-4f9b-aaed-1521eee850a1",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "39a2efcf-a82a-40ee-a3f3-f20b83be64dc",
  "toolUseResult": {
    "stdout": "main_p1.png\nmain_p10.png\nmain_p2.png\nmain_p3.png\nmain_p4.png\nmain_p5.png\nmain_p6.png\nmain_p7.png\nmain_p8.png\nmain_p9.png",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ae0d3adf-2567-4f9b-aaed-1521eee850a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-15T15:26:02.622Z_

<details><summary>↩ Tool result · `toolu_0183makVqgrFtZBi1z9vsZWz`</summary>

```text
# ACL Rolling Review Form - Complete Scoring Rubric

## 1. **Reviewer Confidence**
Scale: 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims."
- **3:** "Acceptable: This study provides sufficient support for its main claims."
- **2:** "Poor: Some of the main claims are not sufficiently supported."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend presentation."
- **4:** "Exciting: I would mention this paper to others and/or make effort to attend."
- **3:** "Interesting: I might mention some points or attend if time permits."
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1:** "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5:** "Consider for Award: Could be considered for outstanding paper award (top 2.5%)."
- **4.5:** "Borderline Award"
- **4:** "Conference: Could be accepted to an *ACL conference."
- **3.5:** "Borderline Conference"
- **3:** "Findings: Could be accepted to the Findings of the ACL."
- **2.5:** "Borderline Findings"
- **2:** "Resubmit next cycle: Needs substantial revisions."
- **1.5:** "Resubmit after next cycle: Major revisions needed."
- **1:** "Do not resubmit: Not relevant to *ACL community."

## 5. **Reproducibility**
Scale: 1-5
- **5:** "They could easily reproduce the results."
- **4:** "They could mostly reproduce the results."
- **3:** "They could reproduce with some difficulty."
- **2:** "They would be hard pressed to reproduce the results."
- **1:** "They would not be able to reproduce."

## 6. **Datasets Value**
Scale: 1-5
- **5:** "Enabling: Should affect research project choices."
- **4:** "Useful: Would recommend to other researchers."
- **3:** "Potentially useful: Someone might find useful."
- **2:** "Documentary: Useful for replication purposes."
- **1:** "No usable datasets submitted."

## 7. **Software Value**
Scale: 1-5
- **5:** "Enabling: Should affect research project choices."
- **4:** "Useful: Would recommend to other researchers."
- **3:** "Potentially useful: Someone might find useful."
- **2:** "Documentary: Useful for replication purposes."
- **1:** "No usable software released."

## 8. **Author Identity Knowledge**
Scale: 1-5
- **5:** "Know/can guess author name from submission violation."
- **4:** "From preprint or allowed workshop paper."
- **3:** "From submission contents itself."
- **2:** "From social media/talk/informal communication."
- **1:** "No educated guess about author identity."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97bcd2d9-9031-4c62-b43d-36f98552794c",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "62eca255-3476-4ad8-9861-bdf1d98792d3",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Complete Scoring Rubric\n\n## 1. **Reviewer Confidence**\nScale: 1-5\n- **5:** \"Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- **4:** \"Quite sure. I tried to check the important points carefully.\"\n- **3:** \"Pretty sure, but there's a chance I missed something.\"\n- **2:** \"Willing to defend my evaluation, but it is fairly likely that I missed some details.\"\n- **1:** \"Not my area, or paper is very hard to understand.\"\n\n## 2. **Soundness**\nScale: 1-5 (with .5 increments)\n- **5:** \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n- **4:** \"Strong: This study provides sufficient support for all of its claims.\"\n- **3:** \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2:** \"Poor: Some of the main claims are not sufficiently supported.\"\n- **1:** \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n## 3. **Excitement**\nScale: 1-5 (with .5 increments)\n- **5:** \"Highly Exciting: I would recommend this paper to others and/or attend presentation.\"\n- **4:** \"Exciting: I would mention this paper to others and/or make effort to attend.\"\n- **3:** \"Interesting: I might mention some points or attend if time permits.\"\n- **2:** \"Potentially Interesting: this paper does not resonate with me, but it might with others.\"\n- **1:** \"Not Exciting: this paper does not resonate with me.\"\n\n## 4. **Overall Assessment**\nScale: 1-5 (with .5 increments)\n- **5:** \"Consider for Award: Could be considered for outstanding paper award (top 2.5%).\"\n- **4.5:** \"Borderline Award\"\n- **4:** \"Conference: Could be accepted to an *ACL conference.\"\n- **3.5:** \"Borderline Conference\"\n- **3:** \"Findings: Could be accepted to the Findings of the ACL.\"\n- **2.5:** \"Borderline Findings\"\n- **2:** \"Resubmit next cycle: Needs substantial revisions.\"\n- **1.5:** \"Resubmit after next cycle: Major revisions needed.\"\n- **1:** \"Do not resubmit: Not relevant to *ACL community.\"\n\n## 5. **Reproducibility**\nScale: 1-5\n- **5:** \"They could easily reproduce the results.\"\n- **4:** \"They could mostly reproduce the results.\"\n- **3:** \"They could reproduce with some difficulty.\"\n- **2:** \"They would be hard pressed to reproduce the results.\"\n- **1:** \"They would not be able to reproduce.\"\n\n## 6. **Datasets Value**\nScale: 1-5\n- **5:** \"Enabling: Should affect research project choices.\"\n- **4:** \"Useful: Would recommend to other researchers.\"\n- **3:** \"Potentially useful: Someone might find useful.\"\n- **2:** \"Documentary: Useful for replication purposes.\"\n- **1:** \"No usable datasets submitted.\"\n\n## 7. **Software Value**\nScale: 1-5\n- **5:** \"Enabling: Should affect research project choices.\"\n- **4:** \"Useful: Would recommend to other researchers.\"\n- **3:** \"Potentially useful: Someone might find useful.\"\n- **2:** \"Documentary: Useful for replication purposes.\"\n- **1:** \"No usable software released.\"\n\n## 8. **Author Identity Knowledge**\nScale: 1-5\n- **5:** \"Know/can guess author name from submission violation.\"\n- **4:** \"From preprint or allowed workshop paper.\"\n- **3:** \"From submission contents itself.\"\n- **2:** \"From social media/talk/informal communication.\"\n- **1:** \"No educated guess about author identity.\"",
    "durationMs": 9201,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "97bcd2d9-9031-4c62-b43d-36f98552794c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 26 · 2026-05-15T15:26:05.612Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the ACL ARR review form criteria and the PDF images. Let me read the paper pages now. I'll read them in batches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62eca255-3476-4ad8-9861-bdf1d98792d3",
  "isSidechain": false,
  "requestId": "req_011Cb4b4cfA9bcXf8RaXfGDQ",
  "type": "assistant",
  "uuid": "55e5e591-c745-418e-877f-1a6432f7560f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRpthr2tT8eQEJvrwbjnaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 30580,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 100,
          "output_tokens": 470,
          "cache_read_input_tokens": 30580,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
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

_source line 27 · 2026-05-15T15:26:06.573Z_

现在逐页阅读论文。先看前5页（title, abstract, intro, related work, method）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55e5e591-c745-418e-877f-1a6432f7560f",
  "isSidechain": false,
  "requestId": "req_011Cb4b4cfA9bcXf8RaXfGDQ",
  "type": "assistant",
  "uuid": "46028919-e65e-4f63-abac-42879845e2e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRpthr2tT8eQEJvrwbjnaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 30580,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 100,
          "output_tokens": 470,
          "cache_read_input_tokens": 30580,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
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

_source line 28 · 2026-05-15T15:26:07.064Z_

<details open><summary>🔧 Tool call — Read · `toolu_016AKhEEvUuejLzogdzev356`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46028919-e65e-4f63-abac-42879845e2e9",
  "isSidechain": false,
  "requestId": "req_011Cb4b4cfA9bcXf8RaXfGDQ",
  "type": "assistant",
  "uuid": "a0d89845-919f-4357-9cb3-7c73dd9a38aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRpthr2tT8eQEJvrwbjnaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 30580,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 100,
          "output_tokens": 470,
          "cache_read_input_tokens": 30580,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
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

_source line 29 · 2026-05-15T15:26:07.590Z_

<details open><summary>🔧 Tool call — Read · `toolu_016zXkmmaCVVng3gNf8i9Z5z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0d89845-919f-4357-9cb3-7c73dd9a38aa",
  "isSidechain": false,
  "requestId": "req_011Cb4b4cfA9bcXf8RaXfGDQ",
  "type": "assistant",
  "uuid": "b208a91a-80c0-4fbb-99b6-86187133c6fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRpthr2tT8eQEJvrwbjnaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 30580,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 100,
          "output_tokens": 470,
          "cache_read_input_tokens": 30580,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
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

_source line 30 · 2026-05-15T15:26:08.546Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PbmcUL4erw27TiNZSpWXB3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b208a91a-80c0-4fbb-99b6-86187133c6fb",
  "isSidechain": false,
  "requestId": "req_011Cb4b4cfA9bcXf8RaXfGDQ",
  "type": "assistant",
  "uuid": "a4200954-aab1-4555-96d8-3d4e59f31f24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRpthr2tT8eQEJvrwbjnaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 30580,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 100,
          "output_tokens": 470,
          "cache_read_input_tokens": 30580,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
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

_source line 31 · 2026-05-15T15:26:08.985Z_

<details open><summary>🔧 Tool call — Read · `toolu_019ebLrXXBYzrP16Jg4wJa8H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4200954-aab1-4555-96d8-3d4e59f31f24",
  "isSidechain": false,
  "requestId": "req_011Cb4b4cfA9bcXf8RaXfGDQ",
  "type": "assistant",
  "uuid": "68c76bed-0bae-46b4-a7f1-b774ae82e6e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRpthr2tT8eQEJvrwbjnaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 30580,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 100,
          "output_tokens": 470,
          "cache_read_input_tokens": 30580,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
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

_source line 32 · 2026-05-15T15:26:09.660Z_

<details open><summary>🔧 Tool call — Read · `toolu_0121XvWcuXzNFkBVD7b7cMof`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68c76bed-0bae-46b4-a7f1-b774ae82e6e6",
  "isSidechain": false,
  "requestId": "req_011Cb4b4cfA9bcXf8RaXfGDQ",
  "type": "assistant",
  "uuid": "557cc031-16e9-49f0-9141-5ceaba0f303a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRpthr2tT8eQEJvrwbjnaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 100,
      "cache_creation_input_tokens": 1206,
      "cache_read_input_tokens": 30580,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 100,
          "output_tokens": 470,
          "cache_read_input_tokens": 30580,
          "cache_creation_input_tokens": 1206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1206
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

_source line 33 · 2026-05-15T15:26:10.632Z_

<details><summary>↩ Tool result · `toolu_016AKhEEvUuejLzogdzev356`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0d89845-919f-4357-9cb3-7c73dd9a38aa",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "1da6a9d9-125d-4639-83cc-89b74bc02fef",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 608726
    }
  },
  "sourceToolAssistantUUID": "a0d89845-919f-4357-9cb3-7c73dd9a38aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "f819cb98-3af1-4df3-a0ed-edf3e4dcc656",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Tool result

_source line 36 · 2026-05-15T15:26:11.511Z_

<details><summary>↩ Tool result · `toolu_016zXkmmaCVVng3gNf8i9Z5z`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b208a91a-80c0-4fbb-99b6-86187133c6fb",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "f819cb98-3af1-4df3-a0ed-edf3e4dcc656",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 627765
    }
  },
  "sourceToolAssistantUUID": "b208a91a-80c0-4fbb-99b6-86187133c6fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "f819cb98-3af1-4df3-a0ed-edf3e4dcc656",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Tool result

_source line 39 · 2026-05-15T15:26:13.124Z_

<details><summary>↩ Tool result · `toolu_01PbmcUL4erw27TiNZSpWXB3`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4200954-aab1-4555-96d8-3d4e59f31f24",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "21c42521-6c3a-4311-b13c-2eca4b78f539",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 722518
    }
  },
  "sourceToolAssistantUUID": "a4200954-aab1-4555-96d8-3d4e59f31f24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "21c42521-6c3a-4311-b13c-2eca4b78f539",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Tool result

_source line 42 · 2026-05-15T15:26:13.518Z_

<details><summary>↩ Tool result · `toolu_019ebLrXXBYzrP16Jg4wJa8H`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68c76bed-0bae-46b4-a7f1-b774ae82e6e6",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "7dfee8ea-134c-4e5f-a5b7-b68e7a678d5d",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 680705
    }
  },
  "sourceToolAssistantUUID": "68c76bed-0bae-46b4-a7f1-b774ae82e6e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-15T15:26:13.531Z_

<details><summary>↩ Tool result · `toolu_0121XvWcuXzNFkBVD7b7cMof`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "557cc031-16e9-49f0-9141-5ceaba0f303a",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "a256be48-98fa-448e-9fa1-93798b864252",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 654221
    }
  },
  "sourceToolAssistantUUID": "557cc031-16e9-49f0-9141-5ceaba0f303a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 44 · 2026-05-15T15:26:13.535Z_

```json
{
  "parentUuid": "a256be48-98fa-448e-9fa1-93798b864252",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "52fc7537-3ae1-4b77-b580-106c58526361",
  "timestamp": "2026-05-15T15:26:13.535Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "52fc7537-3ae1-4b77-b580-106c58526361",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Assistant

_source line 47 · 2026-05-15T15:26:17.238Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the remaining pages of the paper (pages 6-10) to get the full picture before writing my review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52fc7537-3ae1-4b77-b580-106c58526361",
  "isSidechain": false,
  "requestId": "req_011Cb4b5RLYfkgAdadzoyKMd",
  "type": "assistant",
  "uuid": "ea8329e5-4210-444f-8abe-e0848ca72d4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mux3EUsgUABAD1b6WJ1up",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 31786,
      "output_tokens": 453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 453,
          "cache_read_input_tokens": 31786,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 48 · 2026-05-15T15:26:18.412Z_

继续阅读后半部分（experiments, analysis, conclusion）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea8329e5-4210-444f-8abe-e0848ca72d4f",
  "isSidechain": false,
  "requestId": "req_011Cb4b5RLYfkgAdadzoyKMd",
  "type": "assistant",
  "uuid": "c3572327-a302-4a9a-bb72-ce2d3b2d4b50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mux3EUsgUABAD1b6WJ1up",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 31786,
      "output_tokens": 453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 453,
          "cache_read_input_tokens": 31786,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 49 · 2026-05-15T15:26:18.946Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GoGE1RxtfB2iP8CRbb7LTY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3572327-a302-4a9a-bb72-ce2d3b2d4b50",
  "isSidechain": false,
  "requestId": "req_011Cb4b5RLYfkgAdadzoyKMd",
  "type": "assistant",
  "uuid": "b1202646-89a4-4781-bb7c-c96d827df138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mux3EUsgUABAD1b6WJ1up",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 31786,
      "output_tokens": 453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 453,
          "cache_read_input_tokens": 31786,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 50 · 2026-05-15T15:26:19.643Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NaWCngZcC4PwJ9eQhEaic3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1202646-89a4-4781-bb7c-c96d827df138",
  "isSidechain": false,
  "requestId": "req_011Cb4b5RLYfkgAdadzoyKMd",
  "type": "assistant",
  "uuid": "7f6efe64-0483-47a9-988c-2be34bdd7820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mux3EUsgUABAD1b6WJ1up",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 31786,
      "output_tokens": 453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 453,
          "cache_read_input_tokens": 31786,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 51 · 2026-05-15T15:26:20.192Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P6AeRdrTNnihrZGKVwvgt1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f6efe64-0483-47a9-988c-2be34bdd7820",
  "isSidechain": false,
  "requestId": "req_011Cb4b5RLYfkgAdadzoyKMd",
  "type": "assistant",
  "uuid": "5954823b-a42d-4c39-bf7c-13a6515faf55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mux3EUsgUABAD1b6WJ1up",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 31786,
      "output_tokens": 453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 453,
          "cache_read_input_tokens": 31786,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 52 · 2026-05-15T15:26:20.685Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ff8kNq3o8NbyGqjX7EWBkH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5954823b-a42d-4c39-bf7c-13a6515faf55",
  "isSidechain": false,
  "requestId": "req_011Cb4b5RLYfkgAdadzoyKMd",
  "type": "assistant",
  "uuid": "75108575-0ff5-42f6-9600-b9fd705b5ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mux3EUsgUABAD1b6WJ1up",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 31786,
      "output_tokens": 453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 453,
          "cache_read_input_tokens": 31786,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 53 · 2026-05-15T15:26:21.135Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YAhNECNkaD1QnuUVs18s1f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75108575-0ff5-42f6-9600-b9fd705b5ff3",
  "isSidechain": false,
  "requestId": "req_011Cb4b5RLYfkgAdadzoyKMd",
  "type": "assistant",
  "uuid": "2b89636e-752e-40fd-ae1b-cd9b77fb3219",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mux3EUsgUABAD1b6WJ1up",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 31786,
      "output_tokens": 453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 453,
          "cache_read_input_tokens": 31786,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 54 · 2026-05-15T15:26:21.807Z_

<details><summary>↩ Tool result · `toolu_01GoGE1RxtfB2iP8CRbb7LTY`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1202646-89a4-4781-bb7c-c96d827df138",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "d5d955e4-10f0-4aa4-bf24-d2946bbe5b9c",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 689757
    }
  },
  "sourceToolAssistantUUID": "b1202646-89a4-4781-bb7c-c96d827df138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
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
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "d5d955e4-10f0-4aa4-bf24-d2946bbe5b9c",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Tool result

_source line 57 · 2026-05-15T15:26:23.458Z_

<details><summary>↩ Tool result · `toolu_01NaWCngZcC4PwJ9eQhEaic3`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f6efe64-0483-47a9-988c-2be34bdd7820",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "4b84c0ca-d530-47cf-b87f-6a2a4b8256ac",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 654280
    }
  },
  "sourceToolAssistantUUID": "7f6efe64-0483-47a9-988c-2be34bdd7820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "4b84c0ca-d530-47cf-b87f-6a2a4b8256ac",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Tool result

_source line 60 · 2026-05-15T15:26:24.822Z_

<details><summary>↩ Tool result · `toolu_01P6AeRdrTNnihrZGKVwvgt1`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5954823b-a42d-4c39-bf7c-13a6515faf55",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "6352401e-bf76-4cd2-a25c-e2ffde8d1d05",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 663664
    }
  },
  "sourceToolAssistantUUID": "5954823b-a42d-4c39-bf7c-13a6515faf55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "6352401e-bf76-4cd2-a25c-e2ffde8d1d05",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Tool result

_source line 63 · 2026-05-15T15:26:25.359Z_

<details><summary>↩ Tool result · `toolu_01Ff8kNq3o8NbyGqjX7EWBkH`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75108575-0ff5-42f6-9600-b9fd705b5ff3",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "54d7ceb5-9945-4892-8936-8e3eb0197425",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 749512
    }
  },
  "sourceToolAssistantUUID": "75108575-0ff5-42f6-9600-b9fd705b5ff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-15T15:26:25.372Z_

<details><summary>↩ Tool result · `toolu_01YAhNECNkaD1QnuUVs18s1f`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b89636e-752e-40fd-ae1b-cd9b77fb3219",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "42a24394-963a-412f-9b85-28e1f2034c72",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 618367
    }
  },
  "sourceToolAssistantUUID": "2b89636e-752e-40fd-ae1b-cd9b77fb3219",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "42a24394-963a-412f-9b85-28e1f2034c72",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Assistant

_source line 67 · 2026-05-15T15:26:31.375Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper. Let me also check if there are more pages (appendix). The paper seems to have 10 pages, with pages 9-10 being references and appendix. Let me check if there are more pages beyond 10.

Actually, looking at page 10, I can see there's an Appendix section starting at the bottom with sections A (Compounding Curve), B (Heuristic Baselines), C (Allocation Visualization), D (Per-Head Sensitivity Heatmap), E (Granularity Tradeoff). These seem to be referenced in the paper. Let me render additional pages if they exist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42a24394-963a-412f-9b85-28e1f2034c72",
  "isSidechain": false,
  "requestId": "req_011Cb4b6HwL3R2zwLnWYR5mG",
  "type": "assistant",
  "uuid": "4863db9d-c7ae-4bab-849a-2db05138e22b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iMqkLQttBkrRLe3DtZ5Ly",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2372,
      "cache_read_input_tokens": 34379,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 34379,
          "cache_creation_input_tokens": 2372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2372
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

_source line 68 · 2026-05-15T15:26:32.341Z_

检查是否有更多附录页面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4863db9d-c7ae-4bab-849a-2db05138e22b",
  "isSidechain": false,
  "requestId": "req_011Cb4b6HwL3R2zwLnWYR5mG",
  "type": "assistant",
  "uuid": "c5c23c10-0d71-4de3-b273-43ff0e0d8fdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iMqkLQttBkrRLe3DtZ5Ly",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2372,
      "cache_read_input_tokens": 34379,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 34379,
          "cache_creation_input_tokens": 2372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2372
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

_source line 69 · 2026-05-15T15:26:33.026Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01J3YCiwNTBoZKZjYiQeytdD`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf",
  "pages": "11-15",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5c23c10-0d71-4de3-b273-43ff0e0d8fdd",
  "isSidechain": false,
  "requestId": "req_011Cb4b6HwL3R2zwLnWYR5mG",
  "type": "assistant",
  "uuid": "015a2a2b-8136-4f92-a717-ffe13406ea2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iMqkLQttBkrRLe3DtZ5Ly",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2372,
      "cache_read_input_tokens": 34379,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 34379,
          "cache_creation_input_tokens": 2372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2372
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

_source line 70 · 2026-05-15T15:26:33.054Z_

<details><summary>↩ Tool result · `toolu_01J3YCiwNTBoZKZjYiQeytdD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 13 页): 11-15\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "015a2a2b-8136-4f92-a717-ffe13406ea2a",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "74c05248-5f39-46f7-86c5-99869b4d0002",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"页码超出范围 (共 13 页): 11-15\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 13 页): 11-15\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "015a2a2b-8136-4f92-a717-ffe13406ea2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-15T15:26:37.113Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01LggdVZ63xv75pLTNvL1EA4`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf",
  "pages": "11-13",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74c05248-5f39-46f7-86c5-99869b4d0002",
  "isSidechain": false,
  "requestId": "req_011Cb4b6rrV6MD7ZsnY4NZYf",
  "type": "assistant",
  "uuid": "2f537d9b-743b-4b1f-a73a-2537789c2645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8W5p82DE4su6F7EpD4EaH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 372,
      "cache_read_input_tokens": 36751,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 36751,
          "cache_creation_input_tokens": 372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 372
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

_source line 72 · 2026-05-15T15:26:38.440Z_

<details><summary>↩ Tool result · `toolu_01LggdVZ63xv75pLTNvL1EA4`</summary>

```text
Error: result (2,400,847 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778858798433.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778858798433.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f537d9b-743b-4b1f-a73a-2537789c2645",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "4b66352b-c1e7-410d-b8dc-d79eba2d9409",
  "toolUseResult": "Error: result (2,400,847 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778858798433.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778858798433.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 72,
    "serialized_bytes": 2400884,
    "serialized_sha256": "0976fc665246672b08988e6042c3c2600c49628667de3d0968595a586cb2b865",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "2f537d9b-743b-4b1f-a73a-2537789c2645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 73_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "4b66352b-c1e7-410d-b8dc-d79eba2d9409",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 74_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Tool call

_source line 75 · 2026-05-15T15:26:41.849Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019r4ZyPNZrjcTfZozSqsXFe`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p1*.png 2>/dev/null",
  "description": "Check for appendix page images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b66352b-c1e7-410d-b8dc-d79eba2d9409",
  "isSidechain": false,
  "requestId": "req_011Cb4b7FqrHY7UBCZDqxchx",
  "type": "assistant",
  "uuid": "c626178c-e6b1-47c6-90fe-44d6a4b67049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016D9J6SGerQh3FHhQCfuc8w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 37123,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 37123,
          "cache_creation_input_tokens": 541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 541
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

_source line 76 · 2026-05-15T15:26:41.900Z_

<details><summary>↩ Tool result · `toolu_019r4ZyPNZrjcTfZozSqsXFe`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p13.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c626178c-e6b1-47c6-90fe-44d6a4b67049",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "8bd37285-c6e1-4f63-a0a3-55199979854e",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p1.png\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p10.png\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p11.png\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p12.png\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p13.png",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c626178c-e6b1-47c6-90fe-44d6a4b67049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 77 · 2026-05-15T15:26:41.902Z_

```json
{
  "parentUuid": "8bd37285-c6e1-4f63-a0a3-55199979854e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b4ae4ddf-a6bd-4d6f-8968-9fcf09f92758",
  "timestamp": "2026-05-15T15:26:41.902Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Tool call

_source line 78 · 2026-05-15T15:26:45.221Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AYq6emTKmzzLUbFjZ9SoPJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4ae4ddf-a6bd-4d6f-8968-9fcf09f92758",
  "isSidechain": false,
  "requestId": "req_011Cb4b7X2uN97BRkGiscQ5v",
  "type": "assistant",
  "uuid": "9568e95d-5677-4cca-bcee-b8b97df53606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cz9dnpTaQDoCtodRNgMVQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 37664,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 37664,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 79 · 2026-05-15T15:26:46.040Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JVTY87sQyxvkdvYjTrFTtN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9568e95d-5677-4cca-bcee-b8b97df53606",
  "isSidechain": false,
  "requestId": "req_011Cb4b7X2uN97BRkGiscQ5v",
  "type": "assistant",
  "uuid": "c05abed1-8e97-44c8-8781-897405e0d4de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cz9dnpTaQDoCtodRNgMVQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 37664,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 37664,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 80 · 2026-05-15T15:26:46.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q7ZKT3j4Zwmez9KyzuPFHc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c05abed1-8e97-44c8-8781-897405e0d4de",
  "isSidechain": false,
  "requestId": "req_011Cb4b7X2uN97BRkGiscQ5v",
  "type": "assistant",
  "uuid": "ae8ddb1e-ce75-437f-b5ae-592ff1c9f563",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cz9dnpTaQDoCtodRNgMVQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 37664,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 37664,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 81 · 2026-05-15T15:26:47.873Z_

<details><summary>↩ Tool result · `toolu_01AYq6emTKmzzLUbFjZ9SoPJ`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9568e95d-5677-4cca-bcee-b8b97df53606",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "5c3a4b5e-76b3-4588-853f-7b5d173bac79",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 572787
    }
  },
  "sourceToolAssistantUUID": "9568e95d-5677-4cca-bcee-b8b97df53606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 82_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "5c3a4b5e-76b3-4588-853f-7b5d173bac79",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Tool result

_source line 84 · 2026-05-15T15:26:49.009Z_

<details><summary>↩ Tool result · `toolu_01JVTY87sQyxvkdvYjTrFTtN`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c05abed1-8e97-44c8-8781-897405e0d4de",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "6c4d0e88-b187-443b-b1d0-e455d58447e3",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 677784
    }
  },
  "sourceToolAssistantUUID": "c05abed1-8e97-44c8-8781-897405e0d4de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-15T15:26:49.023Z_

<details><summary>↩ Tool result · `toolu_01Q7ZKT3j4Zwmez9KyzuPFHc`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae8ddb1e-ce75-437f-b5ae-592ff1c9f563",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "fefbd1de-e02a-4d7a-b44c-aa45c1209938",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 549409
    }
  },
  "sourceToolAssistantUUID": "ae8ddb1e-ce75-437f-b5ae-592ff1c9f563",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 86_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "fefbd1de-e02a-4d7a-b44c-aa45c1209938",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 87_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Assistant

_source line 88 · 2026-05-15T15:27:53.952Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have read all 13 pages of the paper thoroughly. Let me synthesize my review. Let me carefully go through the Director's specific review focus areas:

## Paper Summary
The paper proposes a cardinality-constrained approach to per-head KV cache quantization. The key insight is that 2-bit quantization distortions compound super-additively, so limiting the number of 2-bit head assignments via a cardinality constraint prevents catastrophic failure. They formulate this as an MCKP (Multiple-Choice Knapsack Problem) and show it matches greedy allocation on all tested architectures.

They also propose a "heterogeneity diagnostic" based on concentration and distribution shape (t1/t5 ratio) to predict when non-uniform allocation helps:


- **Spread**: high concentration + high t1/t5 → benefit (only Qwen2.5-7B)
- **Spike**: high concentration + low t1/t5 → no benefit (Yi-1.5, Llama)
- **Flat**: low concentration → no benefit (Mistral, Gemma-2, Qwen-14B, Pythia)

### Now let me go through the 7 review focus areas:

**1. Compounding claim — causal vs. correlational**
The paper claims 2-bit distortion compounding is the root cause of unconstrained solver failure. Looking at the evidence they present, particularly the super-additivity measurements showing 1.56×–4× effects, I need to assess whether this is truly causal or just correlated with the performance degradation.

The "restoring additivity" experiment is compelling—when they apply the cardinality constraint, results return to the additive regime, which supports the causal narrative. The U-shaped curve in Figure 1 showing PPL degradation as more 2-bit heads get assigned also fits this story. They've identified a plausible mechanism through the residual stream, but I'm noticing they don't rigorously rule out alternative explanations like numerical instability at 2-bit precision itself rather than the compounding effect. The super-additivity profiling comes from just one model (Qwen2.5-7B), yet they're generalizing the claim across all models. For a systems paper, the causal argument is reasonably solid, though not airtight.

**2. N=

1 Spread generalizability**

This is a major limitation. Only Qwen2.5-7B exhibits the "spread" pattern and actually benefits from non-uniform allocation—the other six models show either "spike" or "flat" patterns instead. So their core contribution essentially rests on validating non-uniform allocation against a single model, giving them just one positive example out of seven. They do acknowledge this in their limitations section, noting that the spread pattern is based on N=1 and the seven-model evaluation is directional rather than robust.

**3. Decision rule overfitting risk**

With only two free parameters (concentration threshold around 0.50 and t1/t5 ratio around 0.70) classifying seven data points with perfect accuracy, where only one is actually a positive case, this looks statistically suspicious from an overfitting perspective.

The positive class has just one example, making it impossible to validate where the decision boundary should actually be. They don't report any cross-validation, leave-one-out testing, or sensitivity analysis, and those thresholds are suspiciously round numbers. Framing this as a "joint empirical decision rule" when you only have one positive example to learn from essentially makes it unfalsifiable within their evaluated models.

**4. KIVI comparison fairness**

They claim KIVI combined with their method equals KIVI alone at 9.90 PPL on Qwen, positioning their approach as complementary rather than competitive. But KIVI uses asymmetric per-channel quantization which is orthogonal to their work, and their "symmetric-only" framing raises a practical question about whether anyone actually uses symmetric-only KV cache quantization in real deployments.

**5. Statistical reliability**

The stability numbers are limited—only 10.99±0.06 for constrained MCKP on one model with 3 seeds. Cross-dataset agreement hits 96-97% but without statistical significance testing, and the downstream evaluations are 0-shot only with no confidence intervals. The actual performance deltas in Table 3 are tiny—ARC-C shifts between +1.2 and -0.6, HS between +0.6 and -0.6—well within noise margins.

**6. Experiment coverage**

They're missing comparisons with other mixed-precision methods like KV quantization approaches that would provide better context for their contribution.

The evaluation is also limited in scope: models max out at 14B with no evidence the approach scales to 70B+ where KV cache compression actually matters most. Long context testing only covers 2 models at 8K tokens, which is still relatively short by modern standards, and there's no comparison against other KV cache compression techniques like token eviction combined with quantization.

**7. Runtime benchmark**

The benchmarking is purely PyTorch simulation with an 8.5% overhead ceiling and no actual CUDA kernel implementation. They mention production inference engines with fused kernels would change things significantly, but that caveat really undermines the practical value of the work.

Let me dig into the actual numbers more carefully now. Looking at Table 1 on page 5, I'm seeing the solver comparison results on Qwen2.5-7B at 4× compression—Greedy achieves 32.45 PPL unconstrained while MCKP gets 36.92, but when they add the k≤8 constraint both methods converge around 10.91-11.23 PPL, which is much tighter than I initially thought. uniform 4-bit

Wait, I need to re-read Table 1 more carefully from the image. Let me think about what I remember:

From page 5:
- Table 1: Solver comparison on Qwen2.5-7B at 4× compression
- Qwen2.5-7B with 112 KV heads, k=5 (7% of heads)
- Unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL
- Unconstrained MCKP assigns 75 heads and achieves 36.92 — far worse than uniform 4-bit (15.45)
- With the constraint, both greedy (11.23) and MCKP (10.91) produce identical allocations

Now looking at the broader experimental results across the model suite. Table 2 shows PPL on WikiText-2 at 4× compression, where Qwen2.5-7B benefits significantly from constrained allocation (dropping from 32.45 to 10.91), but the other six models show minimal gains. Tables 3 and 4 then examine downstream task performance and head sensitivity patterns — the downstream accuracy differences are negligible, while the sensitivity analysis reveals that Qwen2.5-7B has the highest concentration of important heads (0.60 in the top 5%) compared to models like Yi-1.5-9B (0.71).

Now I'm looking at the runtime benchmarks to understand the actual latency implications. The baseline bf16 shows 45.86ms for prefill and 33.78ms per decode token, but the 4-bit quantization actually increases these numbers rather than decreasing them, which seems counterintuitive at first glance.

Looking at the perplexity results across different context lengths, I notice the Qwen model shows interesting behavior where MCKP maintains consistent performance at 8K context while uniform quantization degrades significantly. This suggests the method is handling longer sequences better than simpler approaches.

I think I have enough to structure a comprehensive review now. The main concerns I'll focus on are the decision rule being trained on only a single positive example out of seven data points, which makes it prone to overfitting, the limited baseline comparisons—only KIVI is included when other methods like KVTuner and GEAR should be evaluated—and the overall generalizability of the approach given these constraints.

Beyond those critical issues, I should also address the lack of confidence intervals on downstream tasks, the fact that KV cache compression becomes most impactful at larger model scales like 70B where this work maxes out at 14B, and that the evaluation relies on simulation rather than actual runtime measurements. There are also some framing choices worth noting, like the focus on symmetric quantization and the limited scope of long-context evaluation.

Now I'm ready to write out the full review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fefbd1de-e02a-4d7a-b44c-aa45c1209938",
  "isSidechain": false,
  "requestId": "req_011Cb4b833C3e5aXxkvJMPjQ",
  "type": "assistant",
  "uuid": "72defe83-ae4e-4c26-9033-81fd122a893a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoqqqsCgJsV4r7uBeYq8QL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 38102,
      "output_tokens": 8519,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8519,
          "cache_read_input_tokens": 38102,
          "cache_creation_input_tokens": 1398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1398
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

_source line 89 · 2026-05-15T15:27:54.057Z_

已阅读完论文全部 13 页（正文 8 页 + references + appendix A-L）。现在综合 ACL ARR 官方评分标准和 Director 指定的 7 个审查侧重点，撰写审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72defe83-ae4e-4c26-9033-81fd122a893a",
  "isSidechain": false,
  "requestId": "req_011Cb4b833C3e5aXxkvJMPjQ",
  "type": "assistant",
  "uuid": "7a667176-f164-41db-bfd4-316f72427417",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoqqqsCgJsV4r7uBeYq8QL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 38102,
      "output_tokens": 8519,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8519,
          "cache_read_input_tokens": 38102,
          "cache_creation_input_tokens": 1398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1398
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

_source line 90 · 2026-05-15T15:29:56.478Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01BnEZbWiokCe3m9Non29tFS`</summary>

```json
{
  "text": "## Round 2 Review — Reviewer 1（方法严谨性 + 实验验证）\n\n**论文**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\n**Target venue**: EMNLP 2026 Main Conference (ACL ARR)\n\n---\n\n## Summary (2-3 句)\n\n本文将 per-head KV cache 混合精度量化建模为基数约束的 MCKP 问题，核心发现是限制 2-bit head 数量可防止 distortion compounding 导致的灾难性退化。论文同时提出基于 concentration 和 t1/t5 的 heterogeneity diagnostic 来预判非均匀分配是否有益。技术思路清晰，但关键贡献（spread pattern 和 decision rule）的统计支撑极为薄弱——正样本仅 1 个模型，decision rule 在 7 个样本上有严重过拟合风险。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3/5 | 核心 claim（compounding 是 root cause）有合理机制解释但因果论证不够严谨；decision rule 统计基础极弱（N=1 正样本） |\n| **Excitement** | 2.5/5 | 问题有实际意义，但 7 个模型中仅 1 个获益，实用价值受限；缺少大规模模型验证 |\n| **Overall** | 2.5/5 | Borderline Findings——有有趣的观察和合理的形式化，但核心贡献的泛化性和统计可靠性不足以支撑 main conference |\n| **Confidence** | 4/5 | 仔细检查了方法、实验设计和数据，对量化和 KV cache 文献较熟悉 |\n| **Reproducibility** | 4/5 | 提供了详细的 profiling 流程、模型列表、超参数；未提供代码但描述足够复现 |\n\n---\n\n## Strengths\n\n- **S1**: 问题形式化干净优雅。将 per-head mixed-precision 量化建模为 MCKP，cardinality constraint 作为 minimal intervention 防止 compounding，理论动机清晰（Section 3.1-3.4）。Proposition 6 关于 polynomial structure 和 greedy optimality 的论证是扎实的。\n\n- **S2**: Compounding effect 的实验刻画有价值。Section 3.3 的 super-additivity 数据（1.56×–4.89×）和 Figure 1 的 U-shaped curve 为理解 2-bit 量化失败模式提供了有用的 empirical evidence，这一观察本身对社区有参考价值。\n\n- **S3**: 实验设计覆盖了 5 个架构族 7 个模型（MHA 到 GQA 8:1），且包含 cross-dataset validation（Appendix G）和 multi-seed stability（Section 4.2），展现了对实验严谨性的意识。\n\n- **S4**: 论文对 KIVI 对比的定位较为诚实——明确承认 \"complementary, not competitive\"（Section 4.2），没有过度宣称优于 asymmetric 方法。\n\n- **S5**: Appendix 内容丰富（A-L，13 个子节），高分辨率 heatmap（Figure 3）、budget sweep（Table 6）、KV 分离消融（Appendix J）等补充材料增强了可信度。\n\n---\n\n## Weaknesses (按严重程度排序)\n\n### W1 [critical]: Decision rule 的 N=1 正样本构成根本性的统计缺陷\n\n- **具体位置**: Section 5.2, Table 4, Section 8 (Limitations)\n- **问题**: Decision rule 用 2 个自由参数（concentration threshold ~0.50, t1/t5 threshold ~0.70）在 7 个模型上实现 7/7 分类正确率，但**正样本仅 Qwen2.5-7B 一个**。这在统计学上几乎没有意义：\n  - 任何能将 1 个点与其余 6 个分开的线性分界面都能 \"100% 准确\"——这不是 discriminative power 的证据，而是自由度过剩的必然结果\n  - 无法计算 precision/recall/F1，因为 TP=1, FP=0, FN=0 的置信区间无穷大\n  - 没有 leave-one-out cross-validation，没有 threshold sensitivity analysis（如果 concentration 阈值从 0.50 移到 0.45 或 0.55 会怎样？）\n  - 论文声称 \"correctly classifies all seven evaluated models (7/7)\" 时未提及正样本仅 1 个这一关键事实的统计含义\n- **为什么影响接收**: 这是论文三个 contribution 之一（Section 1 第三条贡献：\"we propose a joint empirical decision rule\"）。一个 N=1 正样本的 decision rule 无法被视为可靠的科学发现——它本质上是对单一模型的 post-hoc description，而非泛化性规律。\n- **建议修改方向**: (a) 大幅降低 decision rule 的 claim 强度，明确表述为 \"preliminary observation on 7 models with 1 positive case\"；(b) 补充 threshold sensitivity 分析（扫描参数空间）；(c) 增加更多模型以扩大正样本数量，或者 (d) 将 decision rule 从 contribution 列表中移除，降级为 discussion 中的观察。\n\n### W2 [critical]: Compounding claim 的因果推断不够严谨\n\n- **具体位置**: Section 3.3, Section 1 (contribution 1)\n- **问题**: 论文将 2-bit distortion compounding 定位为 unconstrained solver 失败的 **root cause**（Section 1: \"We identify 2-bit distortion compounding as the cause of catastrophic failure\"）。但实际提供的证据是：\n  - Super-additivity 数据（1.56×–4.89×）——这证明了 compounding 的**存在**，但不排除其他因素也参与导致失败\n  - Cardinality constraint 修复了问题——这证明限制 2-bit 数量有效，但 constraint 可能通过**其他机制**（如避免数值不稳定的极端量化配置）起作用，而非专门因为阻止了 \"compounding\"\n  - Super-additivity 的详细分析仅在 Qwen2.5-7B 上进行（Section 3.3 的 \"64 sequences\" profiling），其他模型未展示 compounding 的量化数据\n  - 替代解释未被排除：例如，2-bit 量化的绝对误差是否已经大到单独导致退化（而非必须通过 compounding）？在 Section 3.2 中提到 \"individual head distortions are typically below 0.1 PPL\" 但 2-bit 时 \"distortions are of magnitudes larger\"——如果单个 2-bit head 的 distortion 已经很大，是否即使不 compound 也会导致退化？\n- **为什么影响接收**: \"Cause\" 这个词在科学论文中有特定含义，需要排除替代假说的实验设计。当前证据支持 \"2-bit compounding is a contributing factor\" 但不足以支撑 \"the cause\"。\n- **建议修改方向**: (a) 将 \"cause\" 改为 \"a major contributing factor\"；(b) 在其他模型上也展示 super-additivity 数据；(c) 设计控制实验排除替代解释（如固定 2-bit head 数量但随机 vs. profiling-guided 选择，以分离 compounding 效应和选择效应）。\n\n### W3 [major]: 关键 baseline 缺失——混合精度 KV cache 文献对比不足\n\n- **具体位置**: Section 2 (Related Work), Section 4.2, Table 2\n- **问题**: 论文 Related Work 中提到了多种混合精度方法（KIVI, KVTuner, GEAR, RKVO, MiKV, Kitty），但实验对比仅包含 KIVI。特别是：\n  - **KVTuner**（Li et al., 2025）——论文 Section 2 自己提到 \"KVTuner: Sensitivity-aware layer-wise mixed-precision KV cache quantization\"，这是最直接的 competitor（也做 sensitivity-aware mixed-precision），却未对比\n  - **GEAR**（Kang et al., 2024）——\"efficient KV cache compression recipe for near-lossless generative inference\"，也是重要 baseline\n  - **Kitty**（Xu et al., 2025）——\"accurate and efficient 2-bit KV cache quantization with dynamic channel-wise precision boost\"，直接处理 2-bit 问题\n  - Table 5 中的 heuristic baselines（L0-random, Naive positional）是 strawman——没有真正的 SOTA mixed-precision 方法作为对比\n- **为什么影响接收**: 缺少直接 competitor 的对比使得无法判断论文方法相对于现有 SOTA 的真实贡献。读者无法确定 cardinality constraint 是否优于 KVTuner 等已有方法。\n- **建议修改方向**: 至少补充 KVTuner 的对比（同为 sensitivity-aware, mixed-precision, per-head allocation）。如果实验资源有限，可以在 1-2 个代表性模型上对比。\n\n### W4 [major]: 模型规模上限 14B，对结论泛化性构成重大限制\n\n- **具体位置**: Section 4.1, Table 2, Section 8 (Limitations)\n- **问题**: \n  - KV cache 压缩的实际需求主要在 70B+ 模型的长序列推理场景，14B 模型的 KV cache 压力相对较小\n  - 更大模型的 head sensitivity 分布可能存在质的差异——例如 Llama-70B/405B 的 GQA 结构、head 数量大幅增加后 concentration pattern 是否改变？\n  - 论文的 decision rule 是否适用于 head 数量从 112 扩展到 1000+ 的情况？\n  - Limitations section 提到 \"untested beyond 14B\" 但这不是一个可以轻描淡写的局限——它直接影响方法的实用价值\n- **为什么影响接收**: 一个声称解决 KV cache 量化问题的方法如果不能在实际需要 KV cache 压缩的模型规模上验证，其贡献的实际意义存疑。\n- **建议修改方向**: (a) 至少在一个 30B+ 模型上验证（如 Qwen2.5-32B 或 Llama-3-70B）；(b) 如果资源受限，应分析 head 数量 scaling 对 concentration pattern 的影响并提供理论预测。\n\n### W5 [major]: 统计可靠性问题——downstream evaluation 缺乏 confidence intervals\n\n- **具体位置**: Table 3, Section 4.2\n- **问题**:\n  - Table 3 的 0-shot accuracy 差异极小：ARC-C 变化 +1.2 到 -0.6，HellaSwag 变化 +0.6 到 -0.3，PIQA 变化 +1.1 到 -0.7，WinoGrande 变化 +2.0 到 -0.5。这些差异**完全在典型的评估噪声范围内**（0-shot evaluation 的标准差通常在 0.5-1.5%）\n  - 没有 confidence intervals 或 p-values，无法判断任何差异是否统计显著\n  - 仅报告 0-shot，未测试 few-shot 或其他设置\n  - Cross-dataset agreement \"96-97%\"（Section 4.2 / Appendix G）——未进行 bootstrap CI 或 McNemar test，97% 的 bit-assignment agreement 是否在统计上显著高于 random chance？\n  - 3-seed stability 仅在 Qwen2.5-7B 上测试（10.99±0.06），其他模型未报告\n- **为什么影响接收**: 在如此小的效应量下，不提供统计显著性检验会让读者怀疑报告的改善是否真实。\n- **建议修改方向**: (a) 对 Table 3 所有模型运行 3+ seeds 并报告均值±标准差；(b) 对 cross-dataset agreement 进行置换检验；(c) 补充 5-shot evaluation。\n\n### W6 [major]: Runtime benchmark 的 simulation 性质严重削弱实用性声明\n\n- **具体位置**: Table 7, Appendix K, Section 8\n- **问题**:\n  - Table 7 明确标注 \"PyTorch-level latency... simulated per-head quantize/dequantize calls\"——这不是真实的推理性能\n  - 论文承认 \"do not represent optimized CUDA kernel performance\"，且 \"fused attention kernels that batch dequantization with the matrix multiply, amortizing the per-head dispatch cost\"\n  - 8.5% overhead 被定位为 \"upper bound\"，但没有任何下界估计\n  - 实际部署中 mixed-precision dispatch 的开销取决于 kernel 实现，PyTorch-level simulation 可能**低估**（额外内存带宽）或**高估**（kernel fusion 可消除的开销）实际影响\n  - 论文结论 \"not a memory trade-off\" 基于 simulation 数据，但没有 real kernel 验证\n- **为什么影响接收**: 方法的实用价值取决于运行时开销是否可接受。没有真实 kernel benchmark，读者无法评估部署可行性。\n- **建议修改方向**: (a) 使用已有的 mixed-precision attention kernel（如 vLLM 或 TensorRT-LLM 中的实现）进行真实 benchmark；(b) 如果无法获取，应更保守地表述 runtime claim，并将 \"8.5% upper bound\" 改为 \"inconclusive\"。\n\n### W7 [minor]: Symmetric-only 定位的实用场景不够清晰\n\n- **具体位置**: Section 4.2 (Comparison with KIVI), Section 6\n- **问题**: 论文将自身定位为 \"symmetric-only\" 量化环境下的方案，与 KIVI 的 asymmetric per-channel 方法互补。但：\n  - 现代推理引擎（vLLM, TensorRT-LLM, SGLang）普遍支持 asymmetric quantization\n  - 什么实际场景**必须**使用 symmetric-only？论文未给出具体的部署约束场景\n  - 如果 KIVI 已经通过 asymmetric quantization 达到 9.90 PPL（vs. 论文的 10.91），且 KIVI+MCKP 没有额外收益，那么 symmetric-only 的贡献空间有多大？\n- **建议**: 补充 1-2 段说明 symmetric-only 量化的具体应用场景（如特定硬件约束、特定推理框架的限制）。\n\n### W8 [minor]: 长文本评估覆盖不足\n\n- **具体位置**: Table 8, Appendix L\n- **问题**: 长序列评估仅在 Qwen2.5-7B 和 Llama-3.1-8B 两个模型上测试（2K vs 8K），且 8K 仍然是相对短的上下文。对于 KV cache 压缩这一研究方向，32K+ 场景下的行为才是关键验证——compounding effect 在更长序列中可能加剧或缓解。\n\n---\n\n## Questions (需要作者回答)\n\n- **Q1**: Section 3.3 的 super-additivity 数据仅在 Qwen2.5-7B 上收集。其他 6 个模型是否也展示 super-additivity？如果是，为什么它们不从 cardinality constraint 中获益？如果不是，\"compounding is the cause\" 这个 claim 如何适用于全部模型？\n\n- **Q2**: Decision rule 的两个 threshold（concentration ~0.50, t1/t5 ~0.70）是如何选择的？是通过系统的 grid search 还是 visual inspection？如果将 concentration 阈值改为 0.40 或 0.60，t1/t5 阈值改为 0.60 或 0.80，分类结果是否改变？\n\n- **Q3**: Table 1 显示 unconstrained MCKP（36.92 PPL）远差于 unconstrained greedy（32.45 PPL）。这是否意味着 MCKP 的 polynomial structure 假设在 unconstrained 情况下**更加**不可靠？如果是，为什么在 constrained 情况下 MCKP 又是可靠的？\n\n- **Q4**: Appendix J 的 KV separation ablation 发现 \"K and V are not treated independently against the cardinality constraint\"——joint allocation 中 K 倾向获得更多 2-bit 分配。这一 asymmetry 的原因是什么？是否暗示 K 和 V 应该有独立的 cardinality constraint？\n\n- **Q5**: 论文是否考虑过在 calibration 阶段使用不同长度的序列？当前 calibration 使用 512 token（Section 4.1），但 profiling 在短序列上的 sensitivity 估计是否能外推到长序列？Table 8 的 8K 结果是否使用了 512 token 的 calibration profile？\n\n- **Q6**: 对于 \"flat\" pattern 的模型（Gemma-2, Qwen-14B, Pythia），constrained MCKP 产生与 uniform 4-bit **相同**的分配吗？还是产生不同但等效的分配？如果前者，为什么 MCKP solver 的开销是合理的？\n\n---\n\n## Missing References\n\n- **KIVI-V2 or per-channel variants**: 论文仅对比了 KIVI 原版，但 2025 年是否有 KIVI 的改进版本？\n- **SqueezeLLM** (Kim et al., 2024) 和其他 weight+KV joint quantization 方法可能值得在 Related Work 中讨论\n- 论文引用列表中包含多个 \"Preprint, arXiv\" 未标注年份或会议——应更新已接收论文的 venue 信息\n\n---\n\n## Overall Assessment\n\n**Score: 2.5 (Borderline Findings)**\n\n**Confidence: 4/5**\n\n**一句话总结**: 论文提出了一个优雅的形式化框架（cardinality-constrained MCKP）来理解和解决 per-head KV cache 量化中的 2-bit compounding 问题，但其最核心的贡献——heterogeneity diagnostic 和 decision rule——在 N=1 正样本上缺乏统计可信度，关键 baseline 缺失，且 14B 的模型规模上限限制了实际影响力。\n\n**主要接收障碍**:\n1. Decision rule 的 N=1 正样本使其从 \"empirical finding\" 降级为 \"anecdotal observation\"\n2. 缺少 KVTuner 等直接 competitor 的实验对比\n3. 方法仅在 ≤14B 模型上验证，而 KV cache 压缩的核心需求在大模型\n\n**如果作者能补充**：(a) 更多展示 spread pattern 的模型（哪怕只增加 1-2 个正样本），(b) 与 KVTuner 的对比，(c) 一个 30B+ 模型的验证——论文可以上升到 Findings 水平。当前状态下，形式化框架的贡献值得发表，但 claim 需要显著收缩。",
  "reviewer_id": "1",
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a667176-f164-41db-bfd4-316f72427417",
  "isSidechain": false,
  "requestId": "req_011Cb4b833C3e5aXxkvJMPjQ",
  "type": "assistant",
  "uuid": "aa57b54e-5018-46bf-9a68-651227a092f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoqqqsCgJsV4r7uBeYq8QL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 38102,
      "output_tokens": 8519,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8519,
          "cache_read_input_tokens": 38102,
          "cache_creation_input_tokens": 1398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1398
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

_source line 91_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验验证）  ### 论文信息 - **标题**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic - **路径**: `proje…",
  "leafUuid": "aa57b54e-5018-46bf-9a68-651227a092f9",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 92_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Tool result

_source line 93 · 2026-05-15T15:30:00.234Z_

<details><summary>↩ Tool result · `toolu_01BnEZbWiokCe3m9Non29tFS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa57b54e-5018-46bf-9a68-651227a092f9",
  "isSidechain": false,
  "promptId": "9b6d6a61-10a4-4705-bc4a-20685efd79c2",
  "type": "user",
  "uuid": "8f514393-aa6d-4b91-a7e2-5c71047b69f3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "aa57b54e-5018-46bf-9a68-651227a092f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 94_

```json
{
  "type": "ai-title",
  "aiTitle": "Round 2 peer review for KV cache quantization paper",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


### Runtime record

_source line 95 · 2026-05-15T15:33:44.389Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T15:33:44.389Z",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "content": "[Round 2 审稿请求]:\n## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的审稿意见\n\n**Score: 3.0 — Findings** | Soundness 3.5/5 | Excitement 2.5/5\n\n**Strengths:**\n- S1: 有价值的负面结论——6/7 模型无收益，\"when does it NOT help\" 视角稀缺\n- S2: 实验设计严谨——7 模型覆盖 MHA 到 GQA 8:1，multi-seed, cross-dataset, profiling resolution 消融\n- S3: Compounding effect 的因果分析有用\n- S4: Greedy-MCKP 等价性对工程部署有价值\n\n**Weaknesses:**\n- W1 [major]: Abstract \"29.4% reduction\" 突出呈现具有误导性——仅来自 1/7 模型，读者第一印象会认为方法普遍有效\n- W2 [major]: 经验判别规则的实用价值存疑——需要完整 profiling 数据，而有了 profiling 数据直接跑 solver 即可判断，O(H log B) 微秒级，判别规则无增量收益\n- W3 [major]: 与 RateQuant 的增量贡献界定模糊——技术上归结为 RateQuant + 一条 cardinality constraint\n- W4 [minor-to-major]: \"Catastrophic failure\" 叙事过度渲染——严格来说仅适用于 Qwen2.5-7B，其他模型为 moderate degradation\n- W5 [minor]: Spread/spike/flat 术语缺乏 formal definition\n- W6 [minor]: Related work 对 token-level mixed-precision 定位可更精确\n- W7 [minor]: Limitations section 过于简短\n- W8 [minor]: Table caption 自包含性可改进\n\n**Questions:**\n- Q1: Spread pattern 是模型固有属性还是校准数据的函数？\n- Q2: Profiling + k sweep + solver 的端到端开销是多少？\n- Q3: Yi-1.5 的 spike head 单独升级到 8-bit 是否能获益？\n- Q4: Table 2 的 unconstrained MCKP 是否就是 RateQuant 复现？\n\n**Missing References:** Cocktail (chunk-adaptive), MiKV/No Token Left Behind, \"More Tokens Lower Precision\"\n\n---\n\n请对以上每个 Weakness (W1-W8) 和 Question (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

---


### Runtime record

_source line 96 · 2026-05-15T15:33:44.389Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T15:33:44.389Z",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 97 · 2026-05-15T15:33:44.382Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f514393-aa6d-4b91-a7e2-5c71047b69f3",
  "isSidechain": false,
  "promptId": "4428806e-98ff-4cc4-8fd4-b11d870ca9cd",
  "type": "user",
  "isMeta": true,
  "uuid": "797be6b9-5f01-4d7b-b977-fb21c58277a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 98 · 2026-05-15T15:33:44.382Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "797be6b9-5f01-4d7b-b977-fb21c58277a2",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "dc8b392a-8ac2-4051-b739-6bd6914ae608",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "1afce127-e2c3-4d18-ab3d-7eb60b23e099",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 3

## Round 3

32 recorded events


### User

_source line 99 · 2026-05-15T15:33:44.505Z_

[Round 2 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 2 的审稿意见

**Score: 3.0 — Findings** | Soundness 3.5/5 | Excitement 2.5/5

**Strengths:**
- S1: 有价值的负面结论——6/7 模型无收益，"when does it NOT help" 视角稀缺
- S2: 实验设计严谨——7 模型覆盖 MHA 到 GQA 8:1，multi-seed, cross-dataset, profiling resolution 消融
- S3: Compounding effect 的因果分析有用
- S4: Greedy-MCKP 等价性对工程部署有价值

**Weaknesses:**
- W1 [major]: Abstract "29.4% reduction" 突出呈现具有误导性——仅来自 1/7 模型，读者第一印象会认为方法普遍有效
- W2 [major]: 经验判别规则的实用价值存疑——需要完整 profiling 数据，而有了 profiling 数据直接跑 solver 即可判断，O(H log B) 微秒级，判别规则无增量收益
- W3 [major]: 与 RateQuant 的增量贡献界定模糊——技术上归结为 RateQuant + 一条 cardinality constraint
- W4 [minor-to-major]: "Catastrophic failure" 叙事过度渲染——严格来说仅适用于 Qwen2.5-7B，其他模型为 moderate degradation
- W5 [minor]: Spread/spike/flat 术语缺乏 formal definition
- W6 [minor]: Related work 对 token-level mixed-precision 定位可更精确
- W7 [minor]: Limitations section 过于简短
- W8 [minor]: Table caption 自包含性可改进

**Questions:**
- Q1: Spread pattern 是模型固有属性还是校准数据的函数？
- Q2: Profiling + k sweep + solver 的端到端开销是多少？
- Q3: Yi-1.5 的 spike head 单独升级到 8-bit 是否能获益？
- Q4: Table 2 的 unconstrained MCKP 是否就是 RateQuant 复现？

**Missing References:** Cocktail (chunk-adaptive), MiKV/No Token Left Behind, "More Tokens Lower Precision"

---

请对以上每个 Weakness (W1-W8) 和 Question (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc8b392a-8ac2-4051-b739-6bd6914ae608",
  "isSidechain": false,
  "promptId": "4428806e-98ff-4cc4-8fd4-b11d870ca9cd",
  "type": "user",
  "uuid": "b98f68fa-d97d-4b4f-9a1a-933be21ebc4c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 100 · 2026-05-15T15:34:44.003Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me to cross-review Reviewer 2's opinions. I need to go through each weakness (W1-W8) and question (Q1-Q4) and respond with [AGREE] or [REBUT], citing specific evidence from the paper.

Let me think through each one carefully based on what I've read in the paper.

**W1 [major]: Abstract "29.4% reduction" misleading — only from 1/7 models**
I agree with this. The abstract prominently features the 29.4% number which comes only from Qwen2.5-7B. This creates a misleading first impression. 

**W2 [major]: Decision rule has no incremental value since profiling + solver is O(H log B)**
The decision rule's practical utility is limited since profiling and solving are already fast operations. However, I think there's conceptual value here — the rule helps explain *why* certain models benefit from the approach while others don't, even if the computational overhead is minimal.

Actually, R2 makes a sharper point: if you need complete profiling data to compute the concentration and t1/t5 metrics, and running the solver on that same data is essentially free, then the decision rule doesn't add practical value. You could just run the solver directly and observe whether it differs from uniform allocation. That's a strong argument.

The counterargument is that the diagnostic provides interpretability — it tells you *why* a model benefits (whether it's due to spread, spike, or flat distribution). But R2 is right that for actual deployment, this diagnostic doesn't add practical utility. I'll acknowledge the practical concern while noting the conceptual insight still has merit.

**W3 [major]: Incremental over RateQuant — just RateQuant + cardinality constraint**
I need to think through what RateQuant actually is and how this work builds on it.

The unconstrained MCKP formulation is essentially RateQuant applied to per-head KV cache, and the paper's main contribution is adding a cardinality constraint. Is one constraint enough to justify a paper? The paper argues the constraint is motivated by the compounding analysis, and the diagnostic is a separate contribution. But if the diagnostic has limited value as R2 suggests, and we're just adding one constraint, the technical novelty feels thin.

That said, the *analysis* of why the constraint is needed — the compounding effect — and the systematic evaluation across 7 models with the "mostly negative" finding are contributions in themselves. The constraint is simple, but understanding when and why it's needed is the real insight. I'll partially agree the technical delta is small, but the empirical analysis adds value.

**W4 [minor-to-major]: "Catastrophic failure" narrative is overblown**
Now I'm looking at Table 2 to see what the actual failure cases look like.

Qwen2.5-7B shows a dramatic gap: unconstrained greedy hits 32.45 versus uniform 4-bit at 15.45 — that's genuinely catastrophic. But for the other models in the table, the unconstrained greedy results don't show the same kind of collapse. Most of them degrade moderately or perform similarly to the constrained version. So R2's point holds: the "catastrophic failure" framing in the abstract and introduction really only applies to one or two models, not the general case.

I agree with that critique. The other weaknesses are more minor — the spread/spike/flat terminology lacks formal rigor since those thresholds are empirically chosen rather than theoretically grounded. The related work could be sharper on token-level mixed-precision methods, and the limitations section is genuinely brief given how many constraints the work operates under, like the single-model focus.

On the substantive questions, the cross-dataset validation in Appendix G is reassuring that spread patterns are model-inherent rather than calibration artifacts, though it's limited to English web text sources. That leaves open whether different domains would shift the picture. And I'm curious about the actual end-to-end cost of the profiling step itself.

The Yi-1.5 BOS spike is interesting—the paper mentions assigning it 8-bit or 16-bit precision but doesn't directly test whether upgrading helps. For the unconstrained MCKP in Table 2, if it's essentially a RateQuant reproduction, that should be stated explicitly rather than left ambiguous.

Comparing my review to R2's, I notice R2 is slightly more generous on soundness and overall assessment. R2 didn't flag the model scale limitation (14B max) or missing baselines like KVTuner that I marked as major weaknesses, and didn't emphasize the lack of confidence intervals as heavily. But R2 made some sharp points I missed—particularly about the practical utility of the decision rule and whether this is truly incremental over RateQuant—while I focused more on the statistical reliability gaps.

Now I'm reconsidering R2's claim that the core contribution reduces to RateQuant plus a cardinality constraint. Looking at the RateQuant paper they cite, it's a rate-distortion approach to KV cache quantization. If the unconstrained MCKP formulation in Table 1 is essentially equivalent to RateQuant, then the paper's main contribution would be showing that adding the cardinality constraint is what prevents the catastrophic failure on Qwen—which would make the incremental nature of the contribution more significant than I initially assessed.

R2 also raises a practical concern about W2: with per-head sensitivity profiling data already computed, you can directly run the MCKP solver in microseconds, so the decision rule itself doesn't add practical value beyond what the solver already provides. This is a fair point about the utility of the analytical framework.

Now I need to revisit W1 and check whether the abstract's 29.4% reduction claim is properly qualified or presented as a general result when it's actually specific to one model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b98f68fa-d97d-4b4f-9a1a-933be21ebc4c",
  "isSidechain": false,
  "requestId": "req_011Cb4befU2GzK2PzasFpMSV",
  "type": "assistant",
  "uuid": "d23204b3-62b5-4883-87bf-beae64271d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5p8d5w2L92VJoSE16DF1s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31159,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2759,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 31159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31159
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 18618
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 101 · 2026-05-15T15:34:44.435Z_

逐条回应 Reviewer 2 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d23204b3-62b5-4883-87bf-beae64271d3b",
  "isSidechain": false,
  "requestId": "req_011Cb4befU2GzK2PzasFpMSV",
  "type": "assistant",
  "uuid": "e6468453-3710-4881-bdb2-1092caff3499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5p8d5w2L92VJoSE16DF1s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31159,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2759,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 31159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31159
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 18618
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-15T15:34:45.853Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01NAZ6fRcqKPNXz4aGRfRhhN`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.pdf",
  "pages": "1",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6468453-3710-4881-bdb2-1092caff3499",
  "isSidechain": false,
  "requestId": "req_011Cb4befU2GzK2PzasFpMSV",
  "type": "assistant",
  "uuid": "870fdbb3-9864-4497-b968-eda0f3f0ee7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "659b7125-b174-4c9a-a25c-c85ac66eb0c5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5p8d5w2L92VJoSE16DF1s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31159,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2759,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 31159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31159
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 18618
      }
    }
  }
}
```

</details>

---


### Large event (continued)

````text
### Tool result

_source line 103 · 2026-05-15T15:34:46.650Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01NAZ6fRcqKPNXz4aGRfRhhN`&lt;/summary>

```text
Error: result (812,097 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778859286645.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778859286645.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "870fdbb3-9864-4497-b968-eda0f3f0ee7c",
  "isSidechain": false,
  "promptId": "4428806e-98ff-4cc4-8fd4-b11d870ca9cd",
  "type": "user",
  "uuid": "242ca04b-ffc4-4c5c-a72d-6cb915adb295",
  "toolUseResult": "Error: result (812,097 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778859286645.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv--claude-sessions-review-reviewer-1-36f1d6e8/659b7125-b174-4c9a-a25c-c85ac66eb0c5/tool-results/mcp-agent-ml-research-pdf_to_images-1778859286645.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/_pdf_images/main_p1.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABnYAAAkjCAIAAACzq+aSAAAACXBIWXMAAB7CAAAewgFu0HU+AAlJiElEQVR4nOzdedxNVf/4/xOizBVRUcjQYIqKUHFLGgx1h1IpbsmQBg000INQZipDERKpSJEGosGQJHMRyjyVIfN8cX7vz7W+7d9qrTPsc9a5rutcvJ5/9NDZa++99tprr73X+1p77UAQAAAAAAAAgINARmcAAAAAAAAAyNwIsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAAAE4IsQEAAAAAAABOCLEBAAAAAAAATgixAQAAAAAA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G03USlugQAG541x//fUNGjTo2bOn3FWPHDkSdctJfuCnGUobQHoixAYgZseOHXvttdfy5cunHlZy5szZu3fvXbt2eQl+++239u3bn3322bL0ggsuaNq0acmSJeXfyRn1kKfh1atXv/nmm1mzZg1ozj//fDtxsWLF9DTlypVL/wyHtH379jZt2gT+7Y477jCSxZR/eSrdtm1bWuY6utOsssXh77//PnjwYEbn4v+8++67RgX75JNP0nSPyVADM0pM7VI6O3ny5IoVK8aOHVu2bNlAKJUrV37//fd//fXX48ePB1Ov4uXLl48ZM0YanJDpy5cvL1uT9PaIVBfJc+0gnFhblXRuE9avXz958uSaNWuGrLc33HBDz549e/Xq1bZtW71u582b96mnnlq3bl2ELad/c3rai1A3KG0A6YkQG4DY7Ny5s3r16t5jSuHChX/55ZeQKaVPpYIdniSPetx55516bu2u7N69e42ntLPOOkv1IZOB5CRPnjx69owQW6z5f+aZZy688MK0z3hYp3Fl82nTpk3nnXfesGHDMjoj/+fJJ5806k/nzp3TdI8ZXgOTQdR2KQNt3749R44cRq0oWLDgvn37QqaXK9poo0Tu3Lnl94TnLamuHYQTa6uSIW3CsWPHLrvsMiOfF110UUpKip5s5syZRYoU0W+vHTt2DHeHTf/m9LQXoW5Q2gDSEyE2ADHYsGFD8eLF9SfIb7/9NkL6Xbt2lSpVKrNEPVq0aBG1K1ugQAE9TbFixdI/nxFceeWVevbsUWz+8//VV19JggwMcJzelc0P6b+pCGOShAkGDx5s9FLGjBmTdrvL8BqYJPy0SxnoqquuMmpFnTp1IqSvWrWqkf76669PeK6S7dpBODG1KhnYJtx9991GPsuXL28n27Jli34bEpUqVdq6daudMp2b09Ne5LpBaQNIT4TYAPh1+PDhihUr6s8o999/f9S11q5dKw89Kn2SRz3+97//Re3Kjhw50kuQJUuWCRMmpH8+IzC6u3aIzWf+N2zYoIJxGRXgOO0rmx/PPvusOpYkCRMcOnToiiuu0LuOavK7tJDhNTB5+GmXMtD1119v9F3/+9//Rkivz4ik/Oc//0l4rpLt2kE4/luVjG0T5AZk1NuQITYxf/78s846S09ZtmzZvXv3GsnSszk97UWtG5Q2gPREiA2AX82bNzceMZcsWeJn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l1+eM2dOJfMscsWr/c2dPHly5hq3ytWvXz+5a7Jmj2mlVT/hlpTtyVdeeWXyZQkThv9JP4JTTz21cJLSpe0bVdrNwgcX9pnM0wNKysLxc845p8jXhgCI2IBcZs2aFYZPf/zjH88444zDDz/8t7/97fHHH3/55Zc//fTTlV9QVlr2R+Ywkgnj2zBavv/++zMPLZ42bdrf/va3ML7t2bNn8puypoTlvvjiizfddFP4JRcGq+lfMocMGfLKK69UdItTramrzRKbO3du//79w8a57777ir9r7Mgjj8z/yJtK5NnZYj/88MOzzz4bxgNh2u7du/fp06fyEVEer7/+evqWwLBVBwwY0KtXr6uuuips24EDB1a+s40ZM+axxx7761//+u9//3vKlCk11aWw24SPNez8Yd1fe+21TJ4SxlrXXHNN2PfCpi7y/RLLQiV7YJ5NWpHlYZssu+PS8nBIySMM1B966KHrrrsufMr33HNPMUek4r871Zh5tY0aNSosoluZe++9t9xXdiTCMarwts3KZR6Hn1i8ePGgQYPCJxt2qltuueXxxx+PH1K57CyL5VbjrJS8EKaiNzIv/6r9zX355ZdbtGhR/M6Tec1LzSr+hBtO7mGlkv8Pa/TUU0+FqcK6P/nkk2PHjq1kEdX7xVKRefPm9evXL3Q1dPgvf/lLOIZkLp0DqJyIDYAasGjRorXXXrvIZ8wDUIkFCxb07t27yKuoSsreBlPXXV7u3H777ausskqVXhbxszFu3Lj4wXBLNXny5LruMsDPhIgNgKqZPXt2r169brzxxuSJVIn+/fuHn+mFb+ACoEqef/75li1blpQ9qH7EiBHfFPj6669HjRp10003NWrUKIlIDj300LrudV0aOnToDTfc8I9//CN+tOhee+1V7quHf97CCTq987dLly6FO08wYcKEl1566de//nUasSX3vwOQn4gNgCpYsGBB+hjmBg0apL/LjzrqqIMPPrhu+wawopswYUL6JoT4UfTluvTSS5OWf/jDH2qne8uhxx9/PI2KjjzyyKTwgw8+CP8cOnRo3fat9qVvqt1+++0rb/n999/Xr1+/pOxRbuU+5gyAahCxAVAFr776anx3SY8ePULh22+/HX6j9+/fv657B7Bie+KJJ9ID7DvvvFN54/TFCL/kq5Diq7FWWWWVpLBdu3Z77bVX3XasTqQv1ghb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1Lz+/fuX/NTo0aPrulPUsWrsFZmM6cknn6y8/bx58zbddNOlRmybb7553pWpFctPxBYsWLBgzJgxYQv/bBYEANQsERsA1Lyjjz46E6acf/75dd0p6lhV94qxY8fWr18/bVyvXr1i3kP69NNPi9gAAGqfHysAUMMmT57coEGDzOPnmzRpMmvWrIom+frrr58rkDyG6eOPP+7atetxxx133nnnPfzww5U8m+nHH3/s16/fRRdddOyxx5588sl//vOfR44cWVML6tu3b+GEwaRJk0rL3v8YF3766adjx47NtOzfv38yq2HDhl166aVh+3Ts2PH++++Pr9b54osvQrePP/74s846q1evXvPnz69kO3/22We33XZbmEn79u07d+782GOP/fDDD5k2hd2eNm1aKP/uu+8K1yX0OTP51KlT//73v4fOhE0aNs7rr78eehtKwvpW0rFyVWOvOP/88+PG2267bTELSl5u8N5778WFyzRie/nll//0pz+FTdSpU6fevXt//vnnX3755bXXXpvU5vkICiO28ImEfeacc87p0KHDNddcM2bMmExnChc3ceLE0rJbbu++++7TTz89fARdunT58MMP00kWL14cmoVPOez83bp1y2y6wj35P//5T1U3QjHNilxQ6TL+pgMA1SZiA4Aadt1112299dYzZsxYZZVV4oDg73//e0WTjBkz5pBDDslc4vTDDz9cf/31mcI99tjjm2++KXcOO++8c2iw66673n777VdddVWTJk3CP88666w5c+bkX1Dnzp0bNGgQNwhrd8YZZ4Theqh94YUX0vAorPvAgQMHDBiwzz77xO033njjBQsWZEKTZEEzZ84MM3nooYcyr1PcdtttJ0yYULiyixcvvvnmmxs2bNioUaMLL7zwnnvu2X///UP7DTfcMCw6bhlWf6WVVorn+eqrr4bySZMmnXnmmauvvnpcFeYZT/vwww83a9YsrHWYSc+ePU855ZR0C1SUfVSiGntFcstn6rDDDqvqQlPLKGKbNm1au3btwgy333777t27d+vWLXxk6ceatMnzEWT2lj59+mTahx2gV69e8STnn39+ps2DDz44ZMiQ9dZbLy6sX7/+Y489VlqW2e23336ZqhtuuCGd4RtvvPGrX/0qbrDuuutWdSMU02ypC0os6286AFBtIjYAqEmLFy/eaKONbr311tKCgGDrrbdesmRJJdMeccQRcfswzl9jjTU6duyYucHw9NNPz0z4xBNPJMHNWmutlV7Jdc899yTtt9lmm88++yz/grp27RrXdujQIdONbbfddpNNNpk7d25aEkcGG2+88dlnn73BBhucd955hx56aDyrc8455x//+Meqq67asUx8d+RBBx2UWcqsWbPSTCRNZObMmbPZZpuVlN1NeeONN8btw9rFy0ryncTzzz8fV8X5zltvvZV0Iy4cPnz4mmuuWVL1iK0ae8WECRNKfurcc8+t0kJjyyhiSzKjddZZJwlJS8ueI3bmmWeW/DRdqt5HUFqwrcIu9Mgjj4waNeqaa66Jy6+++up4qsw8w37btGnTQw455MILL4yDtsaNG7///vutW7feZZdd/vCHP2y//fbxVEOGDElnGD6+LbbYIq3KJF9FboRimlW+oNLa+qYDANUjYgOAmtS3b98GDRpMmTIl/P+IESNKfiq9WbJcF198cdx4zz33/Oqrr5Kq9u3bp+X16tXL3Fy52mqrJVW///3v0/IwgE8vmDr44IPzL2jatGnxFVjrrbfewoUL09pFixaFYf9tt90WL+iEE05I29evX//II49Mc4G2bdvGC9p+++3TC9a6dOkSdy9zIduFF16YVn355ZdpeZzjvP3222n5Y489Fs8tznc++eSTuCrOd379618nhS+//HK89BdffLGk6hFbNfaKgQMHZpqFzVKlhcaWRcQWtmS6/8TlYU/Ya6+94nSpeh9BaUHE9sorr6RVF110UVreqFGjOFrKzLNp06bph/jWW2/FVSuttFJYYhJxTp8+Pb7a7tRTT417kgRkiTj5KnIjFL+tKlpQaS1+0wGA6hGxAUBNOvTQQ4844oj0n2FMGw9xDz/88EqmvfTSS+PGcbR01113xVXvv/9+WhVfqJK563CXXXZJq5555pmcCwrOPffcuPb5559Pq15//fUGDRpMnTo1bn/SSSeljUPt7Nmz06rMhUhvvfVWWtWnT5+4ql+/fmnV8OHD69Wrl5Svueaa8bJeeOGFdJKddtopfcLU448/Hs8tznfGjRsXV6X5zsKFC1deeeX0I8s8rCps1apGbNXYK5588smSn+rWrVuVFhpbFhFbmmk2bNgw/vhKyz6LODaqxkeQqOR1B59++mlc1bFjx4rm2bVr17Rq8eLF6f4TtG3bNp5n2G3Sql133TWuiq+7jJOvIjdC8duqogWV1u43HQCoBhEbANSYiRMnhgF8nz590pKHH344HseG2vHjx1c0eWY8HD8gqaKQInNJ1HPPPRfP8Mgjj0yrdtxxxzwLSowdOzaujbOhTp06xSlSIo7YVlpppbiqZ8+e8azix88PGDAgrnrwwQfTqjhliNcoeP/998vdFNXId3744Ye4fO+99x4+fHg61eTJkwvfq1CJ6u0V//73v0t+6sorryx+oRnLImKLLzZceeWVb7nllvRZYIsWLYrXaFlEbEFYi7Qqzlsrn2f8pLb27dvHVW3atEmrNt5447iqouSryI1Q/LaqaEG1/E0HAKpBxAYANeaPf/xj5vbJ+fPnr7322vFQNgx6K5q8GuPhm2++OS4fMGBAPMPTTjstrk0vMcsz8D744IPT2vr160+ePDlZzdVXX/3ZZ5/NNK7ZiG3RokWrrrpqWt6mTZt4hp999lk8VefOnZe6RpVkMVtuuWXJT4UVf/fdd8v73JaienvFm2++menAhRdeWI2lp32IZ1UjEVvm9s+SsgeExeFRahlFbAceeGBcO2PGjGLmWbMRW5EbofhtVdGCav+bDgBUlYgNAGrGwoULW7Rocfnll2fKr7jiingo27x588JxdaIa4+HkcempoUOHxjM866yz4tphw4ZVe0GpzF2cN910U2nZJVdrrbXWjz/+mGlcsxHbpEmT4vLf/va38QwnT54c16YPpapevvP000+XlOe4446bNWtWuR9fuaq9V3z11VeZRRe+X6J4yyJiW7RoUXxnZWqdddZ54YUX4pbLKGI7/vjj49p33nmnmHnWbMRW5EYofltVtKDa/6YDAFUlYgOAmpGEMhtttNH2PxXG6plxde/evcudQzXGw/H7BILMZVadO3eOa9OnxecZeC9atKhly5Zpgy222GLJkiVHHXVUuddY1WzElnmM/SGHHBLPcNq0aXHt3nvvvdQ1qjyLueuuuxo0aFBSYIcddij+RtE8e8U222wTN9h9992LXGihakRsN9544/Tp0ytv89VXX+22226Fm6hevXoPPPBA2mwZRWxnn312XPv6668XM8+ajdiK3whFNqtoQbX/TQcAqkrEBgA1o23btq1atepRnp133jkezbZu3brcOVRjPHz++efH5emFPInMtS3//e9/q72g2LXXXhu3efbZZ1daaaVyH5desxHbt99+G5e3a9cunmHmKrb0OXHVzndKy96ukLkbMXHFFVcUrmy58uwVl19+edxglVVWWbBgQZHLzahqxBY+goYNGxZellho3rx5YbutscYamU3UtGnTr7/+OmmzjCK2U045Ja4dNWpUMfOs8YityI1QZLOKFlQn33QAoEpEbABQA5JRffxg/thzzz2XGVQPGjSosFk1xsO9evWKy9988814hvETmho2bJhee5Vz4D1p0qT48q4111wz8+aBVI2/7qBFixZp+QEHHBDPMPMstvTlANXIdxYvXjx37ty02eDBg8Oy4pbbbrttueubkXOvCNu5cePGcYPME7iKV9WI7Te/+U2rVq0qbzNv3rz0XaszZ8687rrrMuHRk08+mdQuo4jtsMMOS6vChkrzx9qM2IrcCMVvq4oWVCffdACgSkRsAFADwlC2SZMms2fPLrc2jK7XX3/9eEB79NFHlzuTqo6HJ06cGKddffv2jWcYv3/zwAMPzLOgjN/97ndxs549e5bbrMYjtviJVDvvvHM8w8wrF996662k/IknnqhojSrKYkJnmjdvnrlk7Nlnnw0fcdJy9dVXL3d9M/LvFVdeeWXc4MQTT1zqQufPn3/YYYfdcccdcWGVIrZ//etfoc3JJ59c+YLat2/fvXv3uGT69OnxLpfuFdX4CBKVR2x77bVXWhV2yCLnWbMRW5EbofhtVdGC6uqbDgAUT8QGAHnNnj27WbNmp5xySiVtunTpEg9o69WrN27cuEyb6o2HL7744rT8zjvvjGfYunXrpLx+/fojRozIuaBY//790zYNGzacNm1auc1qPGL76quvVltttaR8rbXWimf47LPPppMcddRRafngwYPjuT333HNp1ZgxY+Kq5NUNpWURW6Zl4u67705a7rHHHuWub6xG9ooff/wxzn0aNGjw9ttvVzLDmTNnHnTQQU2bNk1vFUwUH7ENHz48uXQuEwkVat++feHVi/Pnz99oo42SpfznP/9JCqvxESQqidjmzp278sorJ+VhDxw9enRaVcsRWzEbofhtVckdqXXyTQcAiidiA4C8brjhhjBGvf/++ytp89JLL5X81PHHH59pc8EFF8QNPv3007TqnnvuiavSAXkwa9as9PbJ+MqjUN6wYcOk/Pzzz8+/oNiSJUs233zzpM2RRx5Z0Vofc8wx6azC4D9MlVZ17949XlCcC7zyyitx1X333RfPs0ePHuX2PL3ga9VVV504cWJa/s0338RzO/vss5Py8ePHt2rVqtyqJGLbcsstM681ePnll5OWhW8ILVRTe0Xo/x577JE2CJ915jlcqX79+m299dZrrrlm+kLJVObNAGuvvXbh5IsWLbrrrrvC5EmbsLKVr2D79u1Ds169emXK99xzz+RTSAOdanwEiUzE9uWXX6ZVL774Ylp+0UUXxVP973//i6e67rrr4tpVVlklrTriiCPiqr333jut2mCDDeKq+JF8a6yxRlU3QvHbqqIFldbRNx0AKJ6IDQBy6dOnT3LVz7HHHhtfJBJbsmTJn/70p5ICjzzySNpmxowZmbihR48eSdXs2bMPOuiguKpr167x/N96663mzZuXlF0pNnLkyKQwvUKqbdu2cVSUZ0GxW2+9NWlTeLVXYuLEieuuu248t/79+ydVixcvjh+kVfLTy5euuuqquOq0006LZ7tw4cITTzwxqerQoUNS+OWXXzZr1iyUrLzyyoX9ySQ1O++88x577NGgQYPjjz8+Lm/UqFHnzp3Hjh2bRGzBfvvtN2HChGQmc+fOPfjgg0vKrm9a6htFa2qvSMyfPz9+nn3Dhg3DP4cMGTJz5sxFixaFdX/44YdDV5NV++yzz+JpQ4OXX345vnQrcd11133xxRdhRaZMmTJixIh77rlnu+22ixtMnjy58nVMYqOwmnfffXcanr7yyivJ/YyZO1Wr+hHEU9WvXz+5J/SSSy5JysM+vNlmmyWTHHjggfGtuKEnYaeN59mmTZv0nt933nknrmrRokX61tRp06Ylu1AiLDTtxrhx4zKPTgsbv0obochmlSwoUSffdACgSCI2AKi+Dh06ZJKL9ddfP35SfrDPPvtkHlofS245HDhwYBgzF9Z27Ngx1KbXixVOmJowYUIYxterV69Zs2bHHXfcvvvuW1J2FUwYVMfvhcy/oNQ333wTZrX22muX+97Je++9t379+plZhe7dfvvtCxYsWG+99QoXlDxo7Ne//nVhVcuWLeMnoy1ZsuS+++7bYIMNQtWuu+560kknJVle27Zt09dKxr777rsk40iFaZ9++ukvv/yypOxNnWEdTzjhhCuuuOLOO+/84osvkojtjDPOCJ0Jn92OO+548MEHr7POOiVl71gYP3587ewVGWHVjjnmmPTuyHSTJv+z2267PfPMM/F1gkEoybQvUrmXuWWETdqqVavTTjstbPzwgYaNv/vuu4dpmzRpEjZjpidV/QiSqX7/+99vuummyWP17r777ubNm4dmRx99dJKFhX927949s/uFXaVwddZcc81Q9Ze//CW92iu16qqrjhgxok+fPuF/MlVh0912222Zq70SYd8Oe3jxG6GYZpUvKFX733QAoEgiNgD4+Zg2bdq///3v22+/vVevXm+88cbChQuX6eL22WefzD16tWnx4sVDhw594IEHevbs+fjjj6e5TEVGjhz50EMP3XHHHf3790/CiNmzZ7/22muZ1xoE3377bZhh8v/Tp09/6aWX7rrrrkcffbTc/K6WzZ07N/SnR48eXbp0Oeecc2666aYnnnji/fffr/2e9OvXL7libsmSJSNGjHjsscf+/ve/v/rqqzNmzKhokuI/gsTAgQNnzpyZ/nPevHnDhg279957e/fuPWDAgGW9exejyI1QjW1VuVr+pgMAxRCxAQDV8f3336+00krxawoAAOAXS8QGACzdsGHDdtlll9atW6ePbA//s+eee9ZtrwAAYDkhYgMAli59bnr9+vXnzZu3YMGCrbfeOr2bEgAAfuFEbADA0iXvFkgMHTr05JNP3m677RYtWlTX/QIAgOWCiA0AWLqrr746fvlg06ZNhw4dWtedAgCA5YWIDQBYuiVLljz00EOHH354mzZtLrzwwqW+vhMAAH5RRGwAAAAAkIuIDQAAAAByEbEBAAAAQC4iNgAAAADIRcQGAAAAALmI2AAAAAAgFxEbAAAAAOQiYgMAAACAXERsAAAAAJCLiA0AAAAAchGxAQAAAEAuIjYAAAAAyEXEBgAAAAC5iNgAAAAAIBcRGwAAAADkImIDAAAAgFxEbAAAAACQi4gNAAAAAHIRsQEAAABALiI2AAAAAMhFxAYAAAAAuYjYAAAAACAXERsAAAAA5CJiAwAAAIBcRGwAAAAAkIuIDQAAAAByEbEBAAAAQC4iNgAAAADIRcQGAAAAALmI2AAAAAAgFxEbAAAAAOQiYgMAAACAXERsAAAAAJCLiA0AAAAAchGxAQAAAEAuIjYAAAAAyEXEBgAAAAC5iNgAAAAAIBcRGwAAAADkImIDAAAAgFxEbAAAAACQi4gNAAAAAHIRsQEAAABALiI2AAAAAMhFxAYAAAAAuYjYAAAAACAXERsAAAAA5CJiAwAAAIBcRGwAAAAAkIuIDQAAAAByEbEBAAAAQC4iNgAAAADIRcQGAAAAALmI2AAAAAAgFxEbAAAAAOQiYgMAAACAXERsAAAAAJCLiA0AAAAAchGxAQAAAEAuIjYAAAAAyEXEBgAAAAC5iNgAAAAAIBcRGwAAAADkImIDAAAAgFxEbAAAAACQi4gNAAAAAHIRsQEAAABALiI2AAAAAMhFxAYAAAAAuYjYAAAAACAXERsAAAAA5CJiAwAAAIBcRGwAAAAAkIuIDQAAAAByEbEBAAAAQC4iNgAAAADIRcQGAAAAALmI2AAAAAAgFxEbAAAAAOQiYgMAAACAXERsAAAAAJCLiA0AAAAAchGxAQAAAEAuIjYAAAAAyEXEBgAAAAC5iNgAAAAAIBcRGwAAAADkImIDAAAAgFxEbAAAAACQi4gNAAAAAHIRsQEAAABALiI2AAAAAMhFxAYAAAAAuYjYAAAAACAXERsAAAAA5CJiAwAAAIBcRGwAAAAAkIuIDQAAAAByEbEBAAAAQC4iNgAAAADIRcQGAAAAALmI2AAAAAAgFxEbAAAAAOQiYgMAAACAXERsAAAAAJCLiA0AAAAAchGxAQAAAEAuIjYAAAAAyEXEBgAAAAC5iNgAAAAAIBcRGwAAAADkImIDAAAAgFxEbAAAAACQi4gNAAAAAHIRsQEAAABALiI2AAAAAMhFxAYAAAAAuYjYAAAAACAXERsAAAAA5CJiAwAAAIBcRGwAAAAAkIuIDQAAAAByEbEBAAAAQC4iNgAAAADIRcQGAAAAALmI2AAAAAAgFxEbAAAAAOQiYgMAAACAXERsAAAAAJCLiA0AAAAAchGxAQAAAEAuIjYAAAAAyEXEBgAAAAC5iNgAAAAAIBcRGwAAAADkImIDAAAAgFxEbAAAAACQi4gNAAAAAHIRsQEAAABALiI2AAAAAMhFxAYAAAAAuYjYAAAAACAXERsAAAAA5CJiAwAAAIBcRGwAAAAAkIuIDQAAAAByEbEBAAAAQC4iNgAAAADIRcQGAAAAALmI2AAAAAAgFxEbAAAAAOQiYgMAAACAXERsAAAAAJCLiA0AAAAAchGxAQAAAEAuIjYAAAAAyEXEBgAAAAC5iNgAAAAAIBcRGwAAAADkImIDAAAAgFxEbAAAAACQi4gNAAAAAHIRsQEAAABALiI2AAAAAMhFxAYAAAAAuYjYAAAAACAXERsAAAAA5CJiAwAAAIBcRGwAAAAAkIuIDQAAAAByEbEBAAAAQC4iNgAAAADIRcQGAAAAALmI2AAAAAAgFxEbAAAAAOQiYgMAAACAXERsAAAAAJCLiA0AAAAAchGxAQAAAEAuIjYAAAAAyEXEBgAAAAC5iNgAAAAAIBcRGwAAAADkImIDAAAAgFxEbADVNHjw4A033HDGjBlLbTlixIieBWqhhwBFGjlyZKdOna655praX/S4ceMKj5AZn3/+ee13bJl64IEHClfziy++qOt+ZX3zzTcnnHBCy5Yt27Vr9+mnn9Z1dwBguSZiA6imMOooKSnp0aPHUlt+8MEHJ510UslP1UIPASq3ePHiZ599tk2bNslx6eyzz679PowfP/7Pf/5z27ZtSwo0bNjw2GOPvemmm5bD7CmnRx999JJLLmnWrFm8vq+++mpd9yvriCOOSLvXunXruu4OACzXjPEAqmPatGmNGjUKQ45NN900jFGLmeSggw6qnYitU6dOt95667Kbfw1agboKPzPffffdX/7yl0022SQ+LtVJxJa6+OKLMxHbXXfdVeNLWa4OO7fddttyErF9+OGHLVq0KCxv3Lhx3MOpU6fWft8AYEUhYgOojjBCS4ccffv2LWaS3//+97UQsT344INh5nVyt1dVrUBdhZ+TyZMnn3vuuWuuueZmm22WibTqNmJ76aWXMv35+OOPa3YRy9th5/HHH18eIrY5c+Zst9125Z6YWrdunXavefPmixYtqv3uAcCKQsQGUGVLlizZfPPN01HHgQceWMxUtRCx/fe//11llVWWqwFkRVagrsLPTPj2PfPMM3Pnzi0tu6Rr+YnYBgwYkInYPvvssxqc/3J42FlOIrYOHTpUdGIaMmTIOuusE6qaNm3ap0+f2u8bAKxARGwAVda/f//MOHD06NFLnWpZR2xffPFFy5Ytk5kvPwPIcq1AXYWft4ceeugXErEtn4ed5SFiu/rqqys/MS1YsGDMmDHz5s2r5Y4BwApHxAZQZUcffXRmHHj++ecvdaplGrGNHz9+4403Tme+/AwgC61AXYWfvaeffvqXELEtt4edOo/Y/vSnPy27ExMA/NLU9qn022+//e9//zuozHvvvTdp0qQlS5Zk2syZM+fDDz988803Bw4cOGzYsPCrqJLnPnz33XejRo365JNPlnHHAf5/kydPbtCgwTHHHBMPS5o0aTJr1qzKJyyM2KZOnXr//fefc845HTp0CEO+MWPGVDTtyy+/HAZCxx57bKdOnXr37v35559/+eWX1157bVI7evTo9ddfP5758ccf/1yZcMgNDT766KPnfmrIkCHJtK+99tpZZ5114oknPvzww5mFhmNvnz59QsdOP/30sOiLLrror3/961Kv1wvH+QceeCCsVPv27cN/e/bsOW3atLR2qV0FatMKFLF9/fXXzxVIfiJ+/PHHXbt2Pe64484777xwKMv8blxGR8ggdO+2227r2LFjONx17tz5scce++GHHypZwfDT97LLLgunj3BQDUsprThiGzt2bKZLgwcPTqqGDh2aqarkeaBvv/12OHecdNJJ4Sxz1VVX9e/fP6699NJLMxs8nWf4NV7Yh//85z/lLuXHH3/s169fOEeEM8XJJ5/85z//eeTIkZk21f74APgZWLhw4SeffBJOr+FcH/4bTs3JAyvKFao+/PDDUWUyrxRfvHhxOPmOGDHizTLhxBrGREW+eq521GrEFrbOgAL/+9//4pRtxowZYUtl2rzzzjvh5F04w3AODts0NAi/NmpxPYBftOuuu27rrbcOB6vkmT6pv//975VPmInY+vTps/rqq8cljRo16tWrV2aqadOmtWvXLtRuv/323bt379at27bbbpu032OPPZI2u+66a0kFTjvttNDgxRdf3HnnnePyAw44IJyNzj333LgwzD9d7lNPPbXRRhs1adIktLn33nvDIG3NNddMmoX+fP7554UrGM6d1157bbJZwkA9rEvYUOH/Gzdu3LNnzyK7CtSmFShiGzNmzCGHHJJp8MMPP1x//fWZwnBs/Oabb9IJl8URMtTefPPNDRs2DMftCy+88J577tl///1Dmw033HDgwIGFqzZ//vzTTz89s/QjjjjiH//4R1ySRmxvvPHGjjvuGFf9+te/TqrCJPvss09ctdJKKxUuMQw/9txzz1AbThl/+9vfQieTxrvsssukSZNCg379+lW0WUrKtnzow69+9au4cN111y1cUPhckq0XtvPtt99+1VVXhRNH+OdZZ501Z86c/B8fACu6efPmvfvuu5mQZ/DgwTNnziy3/ahRo+K8KC0PJ9Mk/8kIhctPylZ7EVs4WSbrH355hM00evToQYMGJSXJmb60bJOlheGXwdixY5OYM/joo4/iuYUtGGY4fPjwpFbEBtSOcPDZaKONbr311tKCyGzrrbcuvCw3lmm/8cYbP/LII+EUcs0118TlV199dTxVkq+ts8466UlowYIFZ555ZkkUsU2YMCEcWuOZnHfeeaPLTJ48OWmzcOHCFi1apA3CALJLly6Zgc0OO+yQNH7uuefq168fSsLgJ+3Jhx9+mBQGW221VXxtWmnZVQwHH3xwUtutW7ek8Mknn0xnHkbyRXYVqDUrUMSWOOKII+IGN9xwwxprrNGxY8fM/funn356OkmNHyFnzZq13377JYU333xzUjhnzpzkDa316tW78cYbM91u3759Op/WrVs/88wzb7755uGHH968efN4EfGNomFAkmRViTRiS8ThV2HE9vLLLyd/7Vh33XXTdUz/PNOqVatwtgprEbZA5ors0f8n+dt2OOVtscUWaW1hxPbEE08kC1prrbXSK/juueeepP0222yT+QSr8fEBsEILZ5w0txk2bNjYsWPTf7799tuF0di3336buSQrrQqnp6RwyJAhYT7hn+H8npTU7PuR8qi9iG3EiBHJyqdX+n399dfpRWpJSfgNlJR88MEHSUn4vZKGbvPnz08KCy9zE7EBtaNv374NGjSYMmVKadlhLTMAy9yDk5GJ2F555ZW06qKLLkrLGzVqlJ4kwnArKdxzzz3jWS1atGivvfZKI7bgyy+/jGde7pOG9t1337RBGNe1bNnypZdeuuCCC9LC3XffPWkZZp6UhBFjeuwtjUZoydAonnkYUqb9//7775PCF198MW1/5JFHFt9VoHascBHbxRdfHDcIx8avvvoqqYpjrHr16sWP56/ZI2R6RVgQ5pzOIRwV0/IwbEjL4zfkrLLKKulKhaNrq1at4o5lnsW25ZZbplWZiO2EE05IqzIR24wZM9Zdd92k6vLLL0/Ld9ttt3SS999/Pylc6kNCkz/zJDIRW/hJv9pqqyVVYT5p+YIFC9KrvA8++OB4kup9fACsuL777rs0F1u4cGFp2UAmvaht6tSpcePFixcPGzYslKcN0ohtyZIlSaA2aNCg9CbT9EbJMC6r5fWqSC1FbGEjpvli+oSFsI3SsCwZwv33v/9N/jl9+vR02vQqwa+//jopGVBAxAbUjkMPPfSII45I/5nchpM6/PDDK5m2kpHMp59+Gld17NgxKU8HbA0bNnzrrbfiSV544YWqRmxt2rSJ27z4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BNL0ovTp06vnAnmGz5adM2cOhfD0OlJY3nzzTcsltIVfokSJOETfRBg+tiNHKJcSJkzIW2KhgXTt2jVx4sQIr1SpUnQe564IQOrUqfET6rn9J5+apOeW8t133zkKPXworUU/5dO6LVMI7dA55i5T3VNPW16zZg1lnUVi089nOtMWHgQMLIXcuXOnWrVq9Dj1WKHz589ToEVi4wbO9ZDwUPMdS4qPLGjRooXl9dHe8+fPT01DP8FCbKHuoXb8+PGbN2+i0vL0NNrf2Y79uAPch7dd279/P0wxvF2eIven7MUmCEKMMnz48AIFClDvkiBBgkaNGlkmETxZ9OnTB4PazJkzO27sKghPDXv27ClXrhyGvOom04IQQK5cuULrK0mI6du3b+nSpd9///23337bZW7n37t3b/ZnRo0axUcVg+TJk9O5sf3791fvyTNu8B81fOHChRRu2UOHTioAlvNS2rRpw89CIgsVKkQH4yKd7lQGSrZlX3+dZ9GFgL0ywzzXHn0NPV2d0ESnJxNw79OmTZsjR47ChQsj65o1awY3Uue0DTixdAf1cDTD/LxfqlQphL/11lvsaaD558yZs3z58u6OKyHX3T55ihx++4wPAhaGViAScMLhpiY24WW/hum+0pQljB/UY3A8Q2oXaNKkCW9EvXPnzpdeeqls2bIWFUmzrH/44QeK06lTp+g/FO9IkS2arGa2bN++PWHChBbt4+7du0mTJqW2Y5lo6a7usSrXs2fPn376CYVIS30tDBw4kOI4vrgj4eHh/4+98w6L6njf/qoYNVZiw957ixF7j0nsilFir7Fiw9g1yWVB7A1r1ESNmliIXWOJfsGComLBCgqKCipYUaSo2fd+9/n5XOM5u8vZZVkgzucPLvbZOXNm5szMmefeKXRKNR7fli1b0E7pR1b4pbTaztHRUaHwouQVibSoi7CoHRmF53OhWY0bN27IkCHFixdftGgRNQr0P926dTty5Ih1tzP1CO7cuUM9W6FChRISEhRJ0t4kE20p7u7ulAAfHx/RvnjxYrJ7enqKdtY3TVV4BsmuWbMmBUZFbdeu3YABA2rVqlW3bl0SHBUSm/ZyxvOlkE5OThh+f//996VKleL11Bii4PLt27fr32uOOtXcxiVLlpDdw8NDtJup+eonhcZLMih6hufPn4tljseHdwrsZNGeYEkKghZkdPmn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sCNP/vz5q1WrFmfvapCQiC08f/78zJkze/fuxXKNf//++2/dC22wJMJagZ2ye/fuQ4cOXbhwwWQ2ocBjx47FtS/f3qbY7ty5g57areLgwYPXr183Wa2uXbuGLsO/2p+ePHly6tSpsLCwXbt27du378SJEzCPY7LhEu8UunXr5gWKbf369W/dqcN4BaxCEIPPP/88thviIrA/lStXjg6YWKfYbt68aZeV0yI6Otq6XQftGY2E4aT9idZt6K/mFBuypU2bFluGyw0mYLvx9/evVauW0fS3XlFwcHC9evXi/onRhAkTWqTYjFC2bFlJsUmsWLHCFsV27969woULK28ezyR4nxApWLCgpNi8DxMZMAKMqLx582LVwrPWS3sHKDbH62PCwIIFC7zetNjBnDlz6JXjMsUWFRVVtGhRNDJBggS6BqkuxowZg0eWLl0ao22TkHi7gG3rr7/++uNN7NmzR7js5fLly39ocOjQIZge2jL/++8/yvDvv/966z0swasU25UrV7RdduLECV0r5enTp+h0ZPj777+Fn27fvr1r1y5tUTdu3PDKe0i89fACxfbPP/+kSZPm999/j7kqJNzEiBEj3gq7Sxf379+H3Xj27FnSy71MsfXu3btixYpWckZGRkI9Necxr169ak6xff/99w0aNHCloW8iJCSkS5cuP/zwg9H0t14RdvosWbJ899137rcqRuE+xfbxxx9Liu1dBcR48uTJVatWLVCgQNasWcuVKzdy5Ejhg+WAAQOwSFaoUIEmaePGjVurQLpRsSdPnvT19aX8OXLkoPzsbgGeEIH6N3fuXBSeOXPmMmXKjBs3zoi2xlNYRgoXLpwvXz78x0pA8b1791LVKVKkQHW5cuVq/RrC1y8rhb948WL16tWNGjXy9/fHpKhTp863336LRG3OVatWNWnS5JNPPvn000+hbGDB2bZtG5/h0qVLsMDR7cKDPMWGNtStWzd79uyo68svv9QeOjOn2LBBIB2rXLZs2fz8/IYMGWL9Cz8MlV69emGgW7Ro0apVq9GjRwcHB9utwlwGjIAeRv7y5csL6R6XKCv9g9mxceNG9MCiRYv49JcvX2JAMbjr16/Hn2hGnjx5KleufOrUKfO3M6HYnjx5QucQASYtGAi0HwPhUOO1QeRy5syJGco/GB4e3qlTJ3QOxBvSi9bq8oznz5+HwtO0aVP6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
```

---
