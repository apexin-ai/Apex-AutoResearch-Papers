# Research conversation: [Round 1 审稿请求]: 你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。 ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety — Part 1 of 3

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-round-1-reviewer-1-layer-selection-sensitivity-in-hidden-state-safety-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/66/66ca6118dce31f25f598.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-18T13:02:03.232Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T13:02:03.232Z",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "content": "[Round 1 审稿请求]:\n你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models\n- **路径**: projects/contrastive_trace_safety/docs/paper/main.tex（sections/ 下各章节）\n- **目标 venue**: EMNLP 2026 (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **类别**: LLM Security / Empirical Study\n\n## Venue 要求\n- Long paper: 8 页正文 + unlimited references + unlimited Limitations\n- ACL 官方模板 + `\\usepackage[review]{acl}` + double-blind\n- Limitations section 必须（不计入页数）\n- ARR Responsible NLP Checklist 必须\n- Overall Assessment 评分标准：5=Consider for Award（前2.5%）, 4=Conference（主会议可接收）, 3.5=Borderline Conference, 3=Findings（可被Findings接收）, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n请重点审查以下方面：\n\n1. **统计方法学**\n   - Holm-Bonferroni 多重比较校正是否恰当？12 tests vs effective DoF=4 的论证是否合理？\n   - Bootstrap 10,000 resamples 在 n=19-20 的 32B 模型上是否提供足够精度？\n   - Exact sign-flip permutation test 作为 bootstrap 验证是否充分？\n   - 论文声称 \"all four models pass HB\" 但 QwQ-32B position baseline BA(0.832) > HS BA(0.796)，这个 claim 是否 misleading？\n\n2. **实验设计与超参数选择**\n   - 累积超参数搜索空间：64 layers × 7 W × 5 K = 2,240 configs 在 n=4-9 per-class validation traces (32B) 上选择，过拟合风险如何？\n   - R1-32B 仅 W=1 通过 HB (coverage 25%, 5/20 traces) — 这个 \"显著性\" 实际意义多大？\n   - Joint (layer, W) grid search 仅对 QwQ-32B 做了，R1-32B 缺失，是否构成方法学不完整？\n   - K=5 作为 \"design pre-selection\" 但 K×W 交互未充分探索 — 这是否影响结论可靠性？\n   - 60/20/20 单次分割 vs 5-seed stability：R1-32B precision std=0.128 是否太高？\n\n3. **对照实验与控制**\n   - PCA-384d capacity control：PCA 最大方差方向 ≠ text encoder 语义空间，\"rules out capacity explanation\" 论证强度如何？\n   - Position residualization：12-18pp drop 后 residualized BA 0.61-0.67，\"substantial non-positional signal\" 的解释是否过强？\n   - Control task selectivity 12.5-19.7pp — 对于此类任务是否足够？\n   - GRU 评估使用 70/30 split vs 主实验 60/20/20 — validation 策略是否清楚？\n\n4. **负面结果与边界**\n   - 7 种替代方法的配置空间是否充分？\n   - RepE comparison: analytic vs iterative parameterization 差异是否被公平讨论？\n   - Cross-model transfer 17 configurations \"all fail\" — 是否测试了足够的 alignment 方法？\n   - FPR 39-52% 与论文各处 framing 的一致性\n\n5. **数据与可复现性**\n   - 单数据集 (HarmThoughts) 的 generalizability concern\n   - CP annotation IAA 未报告 — 如果标注误差 ≥2 steps，lead time 结果 (+4.5 to +13 steps) 可靠性如何？\n   - \"Code and data will be released upon publication\" — 当前是否有足够信息复现？\n\n请按照 Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Overall Assessment (使用EMNLP评分标准) 的结构输出审稿报告。"
}
```

---


### Runtime record

_source line 2 · 2026-05-18T13:02:03.236Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T13:02:03.236Z",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


## Round 1

## Round 1

83 recorded events


### User

_source line 3 · 2026-05-18T13:02:03.271Z_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。

## 论文信息
- **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
- **路径**: projects/contrastive_trace_safety/docs/paper/main.tex（sections/ 下各章节）
- **目标 venue**: EMNLP 2026 (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **类别**: LLM Security / Empirical Study

## Venue 要求
- Long paper: 8 页正文 + unlimited references + unlimited Limitations
- ACL 官方模板 + `\usepackage[review]{acl}` + double-blind
- Limitations section 必须（不计入页数）
- ARR Responsible NLP Checklist 必须
- Overall Assessment 评分标准：5=Consider for Award（前2.5%）, 4=Conference（主会议可接收）, 3.5=Borderline Conference, 3=Findings（可被Findings接收）, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

## 你的审查侧重
请重点审查以下方面：

1. **统计方法学**
   - Holm-Bonferroni 多重比较校正是否恰当？12 tests vs effective DoF=4 的论证是否合理？
   - Bootstrap 10,000 resamples 在 n=19-20 的 32B 模型上是否提供足够精度？
   - Exact sign-flip permutation test 作为 bootstrap 验证是否充分？
   - 论文声称 "all four models pass HB" 但 QwQ-32B position baseline BA(0.832) > HS BA(0.796)，这个 claim 是否 misleading？

2. **实验设计与超参数选择**
   - 累积超参数搜索空间：64 layers × 7 W × 5 K = 2,240 configs 在 n=4-9 per-class validation traces (32B) 上选择，过拟合风险如何？
   - R1-32B 仅 W=1 通过 HB (coverage 25%, 5/20 traces) — 这个 "显著性" 实际意义多大？
   - Joint (layer, W) grid search 仅对 QwQ-32B 做了，R1-32B 缺失，是否构成方法学不完整？
   - K=5 作为 "design pre-selection" 但 K×W 交互未充分探索 — 这是否影响结论可靠性？
   - 60/20/20 单次分割 vs 5-seed stability：R1-32B precision std=0.128 是否太高？

3. **对照实验与控制**
   - PCA-384d capacity control：PCA 最大方差方向 ≠ text encoder 语义空间，"rules out capacity explanation" 论证强度如何？
   - Position residualization：12-18pp drop 后 residualized BA 0.61-0.67，"substantial non-positional signal" 的解释是否过强？
   - Control task selectivity 12.5-19.7pp — 对于此类任务是否足够？
   - GRU 评估使用 70/30 split vs 主实验 60/20/20 — validation 策略是否清楚？

4. **负面结果与边界**
   - 7 种替代方法的配置空间是否充分？
   - RepE comparison: analytic vs iterative parameterization 差异是否被公平讨论？
   - Cross-model transfer 17 configurations "all fail" — 是否测试了足够的 alignment 方法？
   - FPR 39-52% 与论文各处 framing 的一致性

5. **数据与可复现性**
   - 单数据集 (HarmThoughts) 的 generalizability concern
   - CP annotation IAA 未报告 — 如果标注误差 ≥2 steps，lead time 结果 (+4.5 to +13 steps) 可靠性如何？
   - "Code and data will be released upon publication" — 当前是否有足够信息复现？

请按照 Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Overall Assessment (使用EMNLP评分标准) 的结构输出审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "024e6898-ec83-4179-b99a-21f93d09c66c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-18T13:02:03.270Z_

```json
{
  "parentUuid": "024e6898-ec83-4179-b99a-21f93d09c66c",
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
  "uuid": "ee3f8a75-d267-4893-9bd3-bacbeca54e2d",
  "timestamp": "2026-05-18T13:02:03.270Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-18T13:02:03.270Z_

```json
{
  "parentUuid": "ee3f8a75-d267-4893-9bd3-bacbeca54e2d",
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
  "uuid": "013dd9e6-73cc-49c7-956a-120b0a5281c3",
  "timestamp": "2026-05-18T13:02:03.270Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-18T13:02:03.270Z_

```json
{
  "parentUuid": "013dd9e6-73cc-49c7-956a-120b0a5281c3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7656ef7f-a3bd-471a-b8c4-b0af291b5c7d",
  "timestamp": "2026-05-18T13:02:03.270Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
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
  "aiTitle": "Review paper on layer selection sensitivity in safety probes",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


### Assistant

_source line 8 · 2026-05-18T13:02:07.400Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as Reviewer 1 for an EMNLP 2026 submission. I need to:

1. First, run the session start skill
2. Search for ACL ARR reviewer guidelines
3. Read the paper thoroughly
4. Produce a detailed review focusing on the specified areas

Let me start by reading the paper and searching for reviewer guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7656ef7f-a3bd-471a-b8c4-b0af291b5c7d",
  "isSidechain": false,
  "requestId": "req_011CbA5WXRPdme4319V29NyQ",
  "type": "assistant",
  "uuid": "a6f883a7-37f7-4d83-be07-08c29615d5a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VprSNNpiabgKV7FPMtqnfT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16147,
      "cache_read_input_tokens": 11841,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16147
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

_source line 9 · 2026-05-18T13:02:08.418Z_

我将开始审稿流程。首先加载论文并搜索 ACL ARR 官方审稿标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6f883a7-37f7-4d83-be07-08c29615d5a2",
  "isSidechain": false,
  "requestId": "req_011CbA5WXRPdme4319V29NyQ",
  "type": "assistant",
  "uuid": "3891c4e8-ff93-4b69-88e6-32e61b9a1753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VprSNNpiabgKV7FPMtqnfT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16147,
      "cache_read_input_tokens": 11841,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16147
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

_source line 10 · 2026-05-18T13:02:09.474Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01McYrGfpp56EyPMJCgaFPyy`</summary>

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
  "parentUuid": "3891c4e8-ff93-4b69-88e6-32e61b9a1753",
  "isSidechain": false,
  "requestId": "req_011CbA5WXRPdme4319V29NyQ",
  "type": "assistant",
  "uuid": "f7a59ef0-fea4-4e59-a88b-b5c0d96b8432",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VprSNNpiabgKV7FPMtqnfT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16147,
      "cache_read_input_tokens": 11841,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16147
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

_source line 11 · 2026-05-18T13:02:09.481Z_

<details><summary>↩ Tool result · `toolu_01McYrGfpp56EyPMJCgaFPyy`</summary>

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
  "parentUuid": "f7a59ef0-fea4-4e59-a88b-b5c0d96b8432",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "e668e796-252b-49e6-8880-cb764001303d",
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
  "sourceToolAssistantUUID": "f7a59ef0-fea4-4e59-a88b-b5c0d96b8432",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 12 · 2026-05-18T13:02:13.359Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me start by:
1. Searching for ACL ARR reviewer guidelines
2. Reading the paper (main.tex and sections)
3. Let me first find the paper structure
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e668e796-252b-49e6-8880-cb764001303d",
  "isSidechain": false,
  "requestId": "req_011CbA5WzFBdLkEnDmTXsaHH",
  "type": "assistant",
  "uuid": "2a8d2625-7dcb-47d0-ba75-463f69839854",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014KEn6Be5q9Vim7r8PVt2do",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2257,
      "cache_read_input_tokens": 27988,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 27988,
          "cache_creation_input_tokens": 2257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2257
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

_source line 13 · 2026-05-18T13:02:13.897Z_

先并行搜索审稿标准和定位论文文件结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a8d2625-7dcb-47d0-ba75-463f69839854",
  "isSidechain": false,
  "requestId": "req_011CbA5WzFBdLkEnDmTXsaHH",
  "type": "assistant",
  "uuid": "867a34f4-d7da-452a-80a5-8c39ad299952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014KEn6Be5q9Vim7r8PVt2do",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2257,
      "cache_read_input_tokens": 27988,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 27988,
          "cache_creation_input_tokens": 2257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2257
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

_source line 14 · 2026-05-18T13:02:14.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R9UUrKLQNCgDEaSvMDvhdx`</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "867a34f4-d7da-452a-80a5-8c39ad299952",
  "isSidechain": false,
  "requestId": "req_011CbA5WzFBdLkEnDmTXsaHH",
  "type": "assistant",
  "uuid": "a684fcd4-367d-48a1-8313-a442f4c7f7e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014KEn6Be5q9Vim7r8PVt2do",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2257,
      "cache_read_input_tokens": 27988,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 27988,
          "cache_creation_input_tokens": 2257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2257
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

_source line 15 · 2026-05-18T13:02:15.183Z_

<details><summary>↩ Tool result · `toolu_01BNA5v6XYBT5TXgnKrwAeFK`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d142496-c964-4279-87c8-0d4ac8dc7df6",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "06139463-80f6-439c-8d14-bdcdbe018a2b",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 11,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "4d142496-c964-4279-87c8-0d4ac8dc7df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-18T13:02:14.934Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CjGdgPBjD4QSUo38avGNcU`</summary>

```json
{
  "pattern": "projects/contrastive_trace_safety/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a684fcd4-367d-48a1-8313-a442f4c7f7e4",
  "isSidechain": false,
  "requestId": "req_011CbA5WzFBdLkEnDmTXsaHH",
  "type": "assistant",
  "uuid": "73cfbf37-faf8-4a41-a1da-9d64be085033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014KEn6Be5q9Vim7r8PVt2do",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2257,
      "cache_read_input_tokens": 27988,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 27988,
          "cache_creation_input_tokens": 2257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2257
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

_source line 17 · 2026-05-18T13:02:14.949Z_

<details><summary>↩ Tool result · `toolu_01CjGdgPBjD4QSUo38avGNcU`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73cfbf37-faf8-4a41-a1da-9d64be085033",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "b9d26f85-a73c-4082-9381-5b995ea0ac66",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 10,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "73cfbf37-faf8-4a41-a1da-9d64be085033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-18T13:02:15.169Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BNA5v6XYBT5TXgnKrwAeFK`</summary>

```json
{
  "pattern": "projects/contrastive_trace_safety/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9d26f85-a73c-4082-9381-5b995ea0ac66",
  "isSidechain": false,
  "requestId": "req_011CbA5WzFBdLkEnDmTXsaHH",
  "type": "assistant",
  "uuid": "4d142496-c964-4279-87c8-0d4ac8dc7df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014KEn6Be5q9Vim7r8PVt2do",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2257,
      "cache_read_input_tokens": 27988,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 27988,
          "cache_creation_input_tokens": 2257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2257
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

_source line 19 · 2026-05-18T13:02:22.723Z_

<details><summary>↩ Tool result · `toolu_01R9UUrKLQNCgDEaSvMDvhdx`</summary>

```text
Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the web search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and evaluation dimensions:

## Reviewer Guidelines and Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Key Scoring Dimensions:

1. **Soundness**: The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

2. **Excitement**: Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

3. **Overall Recommendation**: The review form includes an overall recommendation assessment.

## Review Form Criteria

The review form covers several evaluation areas including:
- Discussion of limitations and potential positive and negative societal impacts of work, with constructive suggestions for improvement if lacking.
- Ethical issues assessment based on the ACL code of ethics and the ARR checklist submitted by authors.
- Reproducibility: whether there is enough information in the paper for a reader to reproduce the main results, use results in future work, or build upon the work.

## General Reviewer Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a684fcd4-367d-48a1-8313-a442f4c7f7e4",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "1086c715-b25d-439c-acc9-9a699e3a7fe0",
  "toolUseResult": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions",
    "results": [
      {
        "tool_use_id": "srvtoolu_017vcRkkAw22tj5dKnjspDjb",
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
            "title": "Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/dates"
          }
        ]
      },
      "Based on the web search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and evaluation dimensions:\n\n## Reviewer Guidelines and Scoring\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n### Key Scoring Dimensions:\n\n1. **Soundness**: The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.\n\n2. **Excitement**: Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.\n\n3. **Overall Recommendation**: The review form includes an overall recommendation assessment.\n\n## Review Form Criteria\n\nThe review form covers several evaluation areas including:\n- Discussion of limitations and potential positive and negative societal impacts of work, with constructive suggestions for improvement if lacking.\n- Ethical issues assessment based on the ACL code of ethics and the ARR checklist submitted by authors.\n- Reproducibility: whether there is enough information in the paper for a reader to reproduce the main results, use results in future work, or build upon the work.\n\n## General Reviewer Requirements\n\nAll reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements."
    ],
    "durationSeconds": 8.266146414999998
  },
  "sourceToolAssistantUUID": "a684fcd4-367d-48a1-8313-a442f4c7f7e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。  ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models - **路径**: projects/contrastive_trace_safety/docs/p…",
  "leafUuid": "1086c715-b25d-439c-acc9-9a699e3a7fe0",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on layer selection sensitivity in safety probes",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


### Assistant

_source line 22 · 2026-05-18T13:02:25.457Z_

<details><summary>Logged reasoning block</summary>

```text
The paper files weren't found at the expected path. Let me search more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1086c715-b25d-439c-acc9-9a699e3a7fe0",
  "isSidechain": false,
  "requestId": "req_011CbA5XxCviiKew15RkgfBe",
  "type": "assistant",
  "uuid": "8522b2af-671a-4fd8-945b-35ece9e48d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjACvthKiKVbubLEEse8yK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 30245,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 61,
          "output_tokens": 246,
          "cache_read_input_tokens": 30245,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 23 · 2026-05-18T13:02:25.890Z_

论文文件未在预期路径找到，让我扩大搜索范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8522b2af-671a-4fd8-945b-35ece9e48d7f",
  "isSidechain": false,
  "requestId": "req_011CbA5XxCviiKew15RkgfBe",
  "type": "assistant",
  "uuid": "f9fbdc0d-9764-4f93-8267-c1c51cbcd70b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjACvthKiKVbubLEEse8yK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 30245,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 61,
          "output_tokens": 246,
          "cache_read_input_tokens": 30245,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 24 · 2026-05-18T13:02:25.915Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Jeb6VNeU68S4mL4uqPnGV8`</summary>

```json
{
  "pattern": "**/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9fbdc0d-9764-4f93-8267-c1c51cbcd70b",
  "isSidechain": false,
  "requestId": "req_011CbA5XxCviiKew15RkgfBe",
  "type": "assistant",
  "uuid": "c4233ef2-b725-435c-b85f-3fc1375047f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjACvthKiKVbubLEEse8yK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 30245,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 61,
          "output_tokens": 246,
          "cache_read_input_tokens": 30245,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 25 · 2026-05-18T13:02:25.950Z_

<details><summary>↩ Tool result · `toolu_01Jeb6VNeU68S4mL4uqPnGV8`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4233ef2-b725-435c-b85f-3fc1375047f8",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "d61ef239-63fb-41d1-972c-14bdf76df997",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 23,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c4233ef2-b725-435c-b85f-3fc1375047f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-18T13:02:27.349Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012ZqQGkeDjZRZ7mBqfAWkHv`</summary>

```json
{
  "pattern": "**/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d61ef239-63fb-41d1-972c-14bdf76df997",
  "isSidechain": false,
  "requestId": "req_011CbA5XxCviiKew15RkgfBe",
  "type": "assistant",
  "uuid": "3f1a2377-6bf1-45e3-bbdf-57009dc23b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjACvthKiKVbubLEEse8yK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 30245,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 61,
          "output_tokens": 246,
          "cache_read_input_tokens": 30245,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 27 · 2026-05-18T13:02:27.361Z_

<details><summary>↩ Tool result · `toolu_012ZqQGkeDjZRZ7mBqfAWkHv`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f1a2377-6bf1-45e3-bbdf-57009dc23b45",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "1822bb09-89b2-4c55-b6b4-6307a230c4e8",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 9,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "3f1a2377-6bf1-45e3-bbdf-57009dc23b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-18T13:02:27.838Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Kcw27hR2i3q5wMYrZ2fjV2`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales and any other criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1822bb09-89b2-4c55-b6b4-6307a230c4e8",
  "isSidechain": false,
  "requestId": "req_011CbA5XxCviiKew15RkgfBe",
  "type": "assistant",
  "uuid": "95f38c8e-c723-4147-bdd8-a9362736396b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjACvthKiKVbubLEEse8yK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 30245,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 61,
          "output_tokens": 246,
          "cache_read_input_tokens": 30245,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 29 · 2026-05-18T13:02:33.662Z_

<details><summary>↩ Tool result · `toolu_01Kcw27hR2i3q5wMYrZ2fjV2`</summary>

```text
# ACL Rolling Review Form - Complete Scoring Dimensions

## Primary Evaluation Criteria

**Soundness** (1-5 scale):
- 5 = "Excellent: This study is one of the most thorough I have seen, given its type"
- 4 = Strong study with sufficient support; additional experiments optional
- 3 = Acceptable with adequate main claim support; minor details may need work
- 2 = Poor; major claims lack sufficient support
- 1 = "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale):
- 5 = "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- 4 = Would mention to colleagues and attempt to attend presentation
- 3 = Might discuss certain points; attendance if time permits
- 2 = Doesn't resonate personally but may appeal to broader community
- 1 = Not relevant to computational linguistics or community

**Overall Assessment** (1-5 scale):
- 5 = Consider for Award (top 2.5% papers)
- 4 = Conference acceptance recommendation
- 3.5 = Borderline Conference
- 3 = Findings acceptance (prioritizes soundness/reproducibility)
- 2 = Needs substantial revisions for next cycle
- 1 = Do not resubmit or lacks relevance

## Additional Metrics

**Reviewer Confidence** (1-5): Assesses evaluation reliability based on familiarity with topic

**Reproducibility** (1-5): Evaluates information sufficiency for replicating results

**Datasets/Software** (1-5): Rates value of released resources to research community

**Author Identity Knowledge** (1-5): Tracks potential anonymity breaches
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95f38c8e-c723-4147-bdd8-a9362736396b",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "f759b57a-df5f-4343-ab7a-9d01cc53abf8",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Complete Scoring Dimensions\n\n## Primary Evaluation Criteria\n\n**Soundness** (1-5 scale):\n- 5 = \"Excellent: This study is one of the most thorough I have seen, given its type\"\n- 4 = Strong study with sufficient support; additional experiments optional\n- 3 = Acceptable with adequate main claim support; minor details may need work\n- 2 = Poor; major claims lack sufficient support\n- 1 = \"Major Issues: This study is not yet sufficiently thorough to warrant publication\"\n\n**Excitement** (1-5 scale):\n- 5 = \"Highly Exciting: I would recommend this paper to others and/or attend its presentation\"\n- 4 = Would mention to colleagues and attempt to attend presentation\n- 3 = Might discuss certain points; attendance if time permits\n- 2 = Doesn't resonate personally but may appeal to broader community\n- 1 = Not relevant to computational linguistics or community\n\n**Overall Assessment** (1-5 scale):\n- 5 = Consider for Award (top 2.5% papers)\n- 4 = Conference acceptance recommendation\n- 3.5 = Borderline Conference\n- 3 = Findings acceptance (prioritizes soundness/reproducibility)\n- 2 = Needs substantial revisions for next cycle\n- 1 = Do not resubmit or lacks relevance\n\n## Additional Metrics\n\n**Reviewer Confidence** (1-5): Assesses evaluation reliability based on familiarity with topic\n\n**Reproducibility** (1-5): Evaluates information sufficiency for replicating results\n\n**Datasets/Software** (1-5): Rates value of released resources to research community\n\n**Author Identity Knowledge** (1-5): Tracks potential anonymity breaches",
    "durationMs": 5819,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "95f38c8e-c723-4147-bdd8-a9362736396b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 30 · 2026-05-18T13:02:33.666Z_

```json
{
  "parentUuid": "f759b57a-df5f-4343-ab7a-9d01cc53abf8",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bef5c122-bbc8-46d8-9f24-a1ce0220f52c",
  "timestamp": "2026-05-18T13:02:33.666Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 31 · 2026-05-18T13:02:36.897Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the ARR review form. Now I need to find the paper. Let me check the project directory structure more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bef5c122-bbc8-46d8-9f24-a1ce0220f52c",
  "isSidechain": false,
  "requestId": "req_011CbA5YkvJGwf3wXbDYRM8E",
  "type": "assistant",
  "uuid": "fc7e6721-5d44-4446-ae26-718ae70164b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJc1fxEScFzxGeQcuypTGH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 31364,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 31364,
          "cache_creation_input_tokens": 918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 918
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

_source line 32 · 2026-05-18T13:02:36.983Z_

找到 ARR review form 了。现在需要定位论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc7e6721-5d44-4446-ae26-718ae70164b9",
  "isSidechain": false,
  "requestId": "req_011CbA5YkvJGwf3wXbDYRM8E",
  "type": "assistant",
  "uuid": "1f3e72f6-1fd6-4db9-ad92-193f265fcfe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJc1fxEScFzxGeQcuypTGH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 31364,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 31364,
          "cache_creation_input_tokens": 918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 918
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

_source line 33 · 2026-05-18T13:02:39.106Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SS8p9tp2WXEt5e5WWtVMRQ`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs -type f -name \"*.tex\" 2>/dev/null | head -30",
  "description": "Find tex files in project docs directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f3e72f6-1fd6-4db9-ad92-193f265fcfe3",
  "isSidechain": false,
  "requestId": "req_011CbA5YkvJGwf3wXbDYRM8E",
  "type": "assistant",
  "uuid": "eb791fdc-086b-41f8-87e7-e516663b3f96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJc1fxEScFzxGeQcuypTGH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 31364,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 31364,
          "cache_creation_input_tokens": 918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 918
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

_source line 34 · 2026-05-18T13:02:40.051Z_

<details><summary>↩ Tool result · `toolu_017N17mR6HfBJ5xUosT7wmwh`</summary>

```text
total 760
drwxr-xr-x 5 ubuntu ubuntu   4096 May 18 12:51 .
drwxr-xr-x 4 ubuntu ubuntu   4096 May 16 21:08 ..
drwxr-xr-x 2 ubuntu ubuntu   4096 May 18 12:51 _pdf_images
-rw-r--r-- 1 ubuntu ubuntu  11615 May 17 03:08 acl.sty
-rw-r--r-- 1 ubuntu ubuntu  11615 May 16 23:17 acl2023.sty
-rw-r--r-- 1 ubuntu ubuntu  45186 May 16 23:17 acl_natbib.bst
drwxr-xr-x 2 ubuntu ubuntu   4096 May 18 07:56 figures
-rw-r--r-- 1 ubuntu ubuntu  71167 May 18 12:51 main.aux
-rw-r--r-- 1 ubuntu ubuntu  21781 May 18 12:50 main.bbl
-rw-r--r-- 1 ubuntu ubuntu   1302 May 18 12:50 main.blg
-rw-r--r-- 1 ubuntu ubuntu  19575 May 18 12:51 main.fdb_latexmk
-rw-r--r-- 1 ubuntu ubuntu  21922 May 18 12:51 main.fls
-rw-r--r-- 1 ubuntu ubuntu  43368 May 18 12:51 main.log
-rw-r--r-- 1 ubuntu ubuntu   6555 May 18 12:51 main.out
-rw-r--r-- 1 ubuntu ubuntu 456918 May 18 12:51 main.pdf
-rw-r--r-- 1 ubuntu ubuntu    800 May 17 17:57 main.tex
-rw-r--r-- 1 ubuntu ubuntu  20236 May 18 12:15 references.bib
drwxr-xr-x 2 ubuntu ubuntu   4096 May 18 12:51 sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e49c151-15e9-401a-8de3-d553dc6d31be",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "d334622d-42a0-430f-9fd5-3fd8b2a8b0e5",
  "toolUseResult": {
    "stdout": "total 760\ndrwxr-xr-x 5 ubuntu ubuntu   4096 May 18 12:51 .\ndrwxr-xr-x 4 ubuntu ubuntu   4096 May 16 21:08 ..\ndrwxr-xr-x 2 ubuntu ubuntu   4096 May 18 12:51 _pdf_images\n-rw-r--r-- 1 ubuntu ubuntu  11615 May 17 03:08 acl.sty\n-rw-r--r-- 1 ubuntu ubuntu  11615 May 16 23:17 acl2023.sty\n-rw-r--r-- 1 ubuntu ubuntu  45186 May 16 23:17 acl_natbib.bst\ndrwxr-xr-x 2 ubuntu ubuntu   4096 May 18 07:56 figures\n-rw-r--r-- 1 ubuntu ubuntu  71167 May 18 12:51 main.aux\n-rw-r--r-- 1 ubuntu ubuntu  21781 May 18 12:50 main.bbl\n-rw-r--r-- 1 ubuntu ubuntu   1302 May 18 12:50 main.blg\n-rw-r--r-- 1 ubuntu ubuntu  19575 May 18 12:51 main.fdb_latexmk\n-rw-r--r-- 1 ubuntu ubuntu  21922 May 18 12:51 main.fls\n-rw-r--r-- 1 ubuntu ubuntu  43368 May 18 12:51 main.log\n-rw-r--r-- 1 ubuntu ubuntu   6555 May 18 12:51 main.out\n-rw-r--r-- 1 ubuntu ubuntu 456918 May 18 12:51 main.pdf\n-rw-r--r-- 1 ubuntu ubuntu    800 May 17 17:57 main.tex\n-rw-r--r-- 1 ubuntu ubuntu  20236 May 18 12:15 references.bib\ndrwxr-xr-x 2 ubuntu ubuntu   4096 May 18 12:51 sections",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9e49c151-15e9-401a-8de3-d553dc6d31be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-18T13:02:39.276Z_

<details><summary>↩ Tool result · `toolu_01SS8p9tp2WXEt5e5WWtVMRQ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb791fdc-086b-41f8-87e7-e516663b3f96",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "301a3aa3-818a-4b29-a141-dc8c609eb122",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "eb791fdc-086b-41f8-87e7-e516663b3f96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-18T13:02:39.988Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017N17mR6HfBJ5xUosT7wmwh`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/ 2>/dev/null || echo \"Directory not found\"",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "301a3aa3-818a-4b29-a141-dc8c609eb122",
  "isSidechain": false,
  "requestId": "req_011CbA5YkvJGwf3wXbDYRM8E",
  "type": "assistant",
  "uuid": "9e49c151-15e9-401a-8de3-d553dc6d31be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJc1fxEScFzxGeQcuypTGH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 31364,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 31364,
          "cache_creation_input_tokens": 918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 918
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

_source line 37 · 2026-05-18T13:02:43.352Z_

论文已编译为 PDF。我将并行读取所有 tex 文件和渲染 PDF 页面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d334622d-42a0-430f-9fd5-3fd8b2a8b0e5",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "72336929-aa10-4bac-95b0-715355174644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 38 · 2026-05-18T13:02:43.862Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KDSqL3ULReKFv4zF1ntvzr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72336929-aa10-4bac-95b0-715355174644",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "8de9de05-952a-4a5a-8343-06d6e34183e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 39 · 2026-05-18T13:02:43.871Z_

<details><summary>↩ Tool result · `toolu_01KDSqL3ULReKFv4zF1ntvzr`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{colortbl}
13	\usepackage{hyperref}
14	\usepackage{cleveref}
15	
16	\title{Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models}
17	
18	\author{Anonymous ARR Submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{sections/abstract}
25	\end{abstract}
26	
27	\input{sections/introduction}
28	
29	\input{sections/related_work}
30	
31	\input{sections/method}
32	
33	\input{sections/experiments}
34	
35	\input{sections/discussion}
36	
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	
43	\input{sections/appendix}
44	
45	\end{document}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8de9de05-952a-4a5a-8343-06d6e34183e1",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "4b51743c-e5dc-4d37-acab-981666e81bc4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\n\\title{Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models}\n\n\\author{Anonymous ARR Submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{sections/abstract}\n\\end{abstract}\n\n\\input{sections/introduction}\n\n\\input{sections/related_work}\n\n\\input{sections/method}\n\n\\input{sections/experiments}\n\n\\input{sections/discussion}\n\n\\input{sections/conclusion}\n\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  },
  "sourceToolAssistantUUID": "8de9de05-952a-4a5a-8343-06d6e34183e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-18T13:02:44.411Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QNP1YGNfbiQ9gVU6uDAmhB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b51743c-e5dc-4d37-acab-981666e81bc4",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "80288768-9565-4f26-b4c6-023d31b24e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 41 · 2026-05-18T13:02:44.416Z_

<details><summary>↩ Tool result · `toolu_01QNP1YGNfbiQ9gVU6uDAmhB`</summary>

```text
1	Reasoning models with chain-of-thought can self-jailbreak: their reasoning traces transition from safe deliberation to committed harmful generation without adversarial input. We present the first systematic comparison of hidden-state (HS) probes and text-based monitors for detecting this safety commitment, evaluated across four reasoning models spanning two architectures and two scales (7--8B, 32B).
2	
3	Our central finding is methodological: the choice of layer selection metric can reverse a study's conclusions. A composite metric that incorporates crossing rate (the frequency of threshold crossings) systematically selects shallow layers at 32B scale and masks the HS advantage entirely. With principled layer selection, HS probes achieve precision gains of +15.4 to +32.5 percentage points over 384d sentence embeddings across all four models (Holm-Bonferroni corrected). PCA dimensionality matching to 384d preserves the advantage (all four models pass Holm-Bonferroni), ruling out a pure capacity explanation. Against a competitive 1024d encoder, all four models retain directional HS advantage but only 1/4 survives Holm-Bonferroni correction. The advantage has two separable components: a robust modality effect that survives dimensionality matching, and an encoder-dependent magnitude that narrows with stronger text baselines. At 32B ($n{=}19$--$20$, sample-limited), model-specific caveats further qualify the results.
4	
5	Our results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39--52\%, and no alternative method consistently matches supervised probing. Layer selection methodology is a critical, underexamined researcher degree of freedom in the probing literature.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80288768-9565-4f26-b4c6-023d31b24e81",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "2412acb7-6d98-4e64-b993-4aa96d503d85",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex",
      "content": "Reasoning models with chain-of-thought can self-jailbreak: their reasoning traces transition from safe deliberation to committed harmful generation without adversarial input. We present the first systematic comparison of hidden-state (HS) probes and text-based monitors for detecting this safety commitment, evaluated across four reasoning models spanning two architectures and two scales (7--8B, 32B).\n\nOur central finding is methodological: the choice of layer selection metric can reverse a study's conclusions. A composite metric that incorporates crossing rate (the frequency of threshold crossings) systematically selects shallow layers at 32B scale and masks the HS advantage entirely. With principled layer selection, HS probes achieve precision gains of +15.4 to +32.5 percentage points over 384d sentence embeddings across all four models (Holm-Bonferroni corrected). PCA dimensionality matching to 384d preserves the advantage (all four models pass Holm-Bonferroni), ruling out a pure capacity explanation. Against a competitive 1024d encoder, all four models retain directional HS advantage but only 1/4 survives Holm-Bonferroni correction. The advantage has two separable components: a robust modality effect that survives dimensionality matching, and an encoder-dependent magnitude that narrows with stronger text baselines. At 32B ($n{=}19$--$20$, sample-limited), model-specific caveats further qualify the results.\n\nOur results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39--52\\%, and no alternative method consistently matches supervised probing. Layer selection methodology is a critical, underexamined researcher degree of freedom in the probing literature.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  },
  "sourceToolAssistantUUID": "80288768-9565-4f26-b4c6-023d31b24e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-18T13:02:45.161Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C3LY74fudLzva26RHjBXxV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2412acb7-6d98-4e64-b993-4aa96d503d85",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "8273f40f-f9b6-4036-a23f-228b97da3cb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 43 · 2026-05-18T13:02:45.167Z_

<details><summary>↩ Tool result · `toolu_01C3LY74fudLzva26RHjBXxV`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT). Recent work documents that these models can ``self-jailbreak'': without adversarial input modification, the CoT transitions from safety-aware deliberation to committed harmful generation~\cite{harmthoughts,selfjailbreak}. We define the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). This failure mode differs qualitatively from adversarial jailbreaks on standard LLMs because the harmful transition originates within the model's own reasoning. Before building production detectors, a prior question must be answered: can current probing methods reliably distinguish pre-CP from post-CP reasoning steps, and under what conditions? This paper provides a systematic characterization of what hidden-state and text-based probes can and cannot detect.
4	
5	Existing safety detectors target fundamentally different problems. Hidden-state (HS) methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} classify adversarial inputs at the token level, while text monitors like SafeRemind~\cite{saferemind} scan generated reasoning for explicit violations. Neither tracks the gradual, multi-step commitment process. A fundamental question remains: should a monitoring system read the model's hidden states or its generated text? This comparison has never been conducted under controlled conditions. Na\"ive reasoning suggests HS features (up to 5120 dimensions) should dominate text embeddings (384d sentence encoder), but no prior work tests this systematically. A further complication is that HS probes require selecting which transformer layer to monitor, a choice rarely scrutinized but potentially decisive.
6	
7	We present the first systematic evaluation across four reasoning models spanning two architectures (Llama, Qwen) and two scales (7--8B, 32B). Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is observed. A composite metric (balanced accuracy $\times$ crossing rate) selects shallow layers for 32B models because shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings reflect noise rather than semantic transitions. At these layers, only the two 7--8B models show significant HS advantage. Threshold-dependent metrics excluding crossing rate consistently select deep layers (\cref{tab:layer_selection}), where all four models show significant HS advantage (Holm-Bonferroni corrected, \cref{sec:evaluation}; precision +15.4 to +32.5pp over 384d sentence embeddings; \cref{tab:hs_vs_text}).
8	
9	Our contributions are:
10	\begin{itemize}
11	    \item \textbf{Layer selection sensitivity.} We identify a systematic bias in composite metrics that reverses HS probe conclusions at 32B scale. A five-metric ablation establishes principled selection criteria (\cref{sec:layer-results}).
12	
13	    \item \textbf{Encoder-conditional directional advantage.} Against MiniLM-384d, all four models show significant HS precision gains (+15.4 to +32.5pp, Holm-Bonferroni corrected). PCA reduction to matched 384d dimensionality (79--92\% variance retained) preserves significance on all four models (+16.8 to +23.1pp), ruling out capacity gap as the sole explanation. Against BGE-large-1024d, all four models retain directional advantage but only 1/4 survives Holm-Bonferroni (\cref{fig:forest_precision}). The advantage has two separable components: a robust modality effect (survives dimensionality matching) and an encoder-dependent magnitude (narrows with stronger baselines). At 7--8B scale (moderate samples, robust across 5 seeds), evidence is strong; at 32B ($n{=}19$--$20$ test traces, sample-limited), model-specific caveats apply (\cref{sec:32b-analysis}).
14	
15	    \item \textbf{Negative results define method boundaries.} No alternative method consistently matches supervised probing across all four models (\cref{tab:negative}): BOCPD/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation; RepE achieves competitive balanced accuracy on QwQ-32B (0.756 vs.\ supervised 0.778) but at substantially lower precision (0.512 vs.\ 0.700), a metric-dependent discrepancy; cross-model transfer fails under PCA alignment. Control task selectivity (12.5--19.7pp above chance; \cref{app:control}) confirms genuine safety structure.
16	\end{itemize}
17	
18	\noindent Our results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39--52\%, and the 85.5\% oracle gap (\cref{sec:discussion}) underscores how much room remains for improvement.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8273f40f-f9b6-4036-a23f-228b97da3cb7",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "8f43236c-445d-4f72-a8c4-aee0e785e15d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nReasoning models such as DeepSeek-R1~\\cite{deepseekr1} and QwQ~\\cite{qwq} scale inference-time computation through extended chains of thought (CoT). Recent work documents that these models can ``self-jailbreak'': without adversarial input modification, the CoT transitions from safety-aware deliberation to committed harmful generation~\\cite{harmthoughts,selfjailbreak}. We define the first reasoning step after which safety deliberation permanently ceases as the \\textbf{Safety Commitment Point} (CP). This failure mode differs qualitatively from adversarial jailbreaks on standard LLMs because the harmful transition originates within the model's own reasoning. Before building production detectors, a prior question must be answered: can current probing methods reliably distinguish pre-CP from post-CP reasoning steps, and under what conditions? This paper provides a systematic characterization of what hidden-state and text-based probes can and cannot detect.\n\nExisting safety detectors target fundamentally different problems. Hidden-state (HS) methods such as TrajGuard~\\cite{trajguard} and SafeSwitch~\\cite{safeswitch} classify adversarial inputs at the token level, while text monitors like SafeRemind~\\cite{saferemind} scan generated reasoning for explicit violations. Neither tracks the gradual, multi-step commitment process. A fundamental question remains: should a monitoring system read the model's hidden states or its generated text? This comparison has never been conducted under controlled conditions. Na\\\"ive reasoning suggests HS features (up to 5120 dimensions) should dominate text embeddings (384d sentence encoder), but no prior work tests this systematically. A further complication is that HS probes require selecting which transformer layer to monitor, a choice rarely scrutinized but potentially decisive.\n\nWe present the first systematic evaluation across four reasoning models spanning two architectures (Llama, Qwen) and two scales (7--8B, 32B). Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is observed. A composite metric (balanced accuracy $\\times$ crossing rate) selects shallow layers for 32B models because shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings reflect noise rather than semantic transitions. At these layers, only the two 7--8B models show significant HS advantage. Threshold-dependent metrics excluding crossing rate consistently select deep layers (\\cref{tab:layer_selection}), where all four models show significant HS advantage (Holm-Bonferroni corrected, \\cref{sec:evaluation}; precision +15.4 to +32.5pp over 384d sentence embeddings; \\cref{tab:hs_vs_text}).\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{Layer selection sensitivity.} We identify a systematic bias in composite metrics that reverses HS probe conclusions at 32B scale. A five-metric ablation establishes principled selection criteria (\\cref{sec:layer-results}).\n\n    \\item \\textbf{Encoder-conditional directional advantage.} Against MiniLM-384d, all four models show significant HS precision gains (+15.4 to +32.5pp, Holm-Bonferroni corrected). PCA reduction to matched 384d dimensionality (79--92\\% variance retained) preserves significance on all four models (+16.8 to +23.1pp), ruling out capacity gap as the sole explanation. Against BGE-large-1024d, all four models retain directional advantage but only 1/4 survives Holm-Bonferroni (\\cref{fig:forest_precision}). The advantage has two separable components: a robust modality effect (survives dimensionality matching) and an encoder-dependent magnitude (narrows with stronger baselines). At 7--8B scale (moderate samples, robust across 5 seeds), evidence is strong; at 32B ($n{=}19$--$20$ test traces, sample-limited), model-specific caveats apply (\\cref{sec:32b-analysis}).\n\n    \\item \\textbf{Negative results define method boundaries.} No alternative method consistently matches supervised probing across all four models (\\cref{tab:negative}): BOCPD/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation; RepE achieves competitive balanced accuracy on QwQ-32B (0.756 vs.\\ supervised 0.778) but at substantially lower precision (0.512 vs.\\ 0.700), a metric-dependent discrepancy; cross-model transfer fails under PCA alignment. Control task selectivity (12.5--19.7pp above chance; \\cref{app:control}) confirms genuine safety structure.\n\\end{itemize}\n\n\\noindent Our results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39--52\\%, and the 85.5\\% oracle gap (\\cref{sec:discussion}) underscores how much room remains for improvement.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "8273f40f-f9b6-4036-a23f-228b97da3cb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-18T13:02:45.327Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KxSgEVqK8Pr78PUruPhdoE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f43236c-445d-4f72-a8c4-aee0e785e15d",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "c864586b-d031-4068-9f2c-176e7130128c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 45 · 2026-05-18T13:02:45.337Z_

<details><summary>↩ Tool result · `toolu_01KxSgEVqK8Pr78PUruPhdoE`</summary>

```text
1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Steps before CP are \emph{pre-commitment} ($y_t = 0$); steps at or after CP are \emph{post-commitment} ($y_t = 1$). The detection task produces a score $s_t \in [0, 1]$ estimating whether the model has passed its CP by step $t$.
8	
9	We study four reasoning models spanning two architectures and two scales (\cref{tab:models}).
10	
11	\begin{table}[t]
12	\centering
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{lccccc}
15	\toprule
16	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{$n$ (total\,/\,test)} \\
17	\midrule
18	R1-8B & Llama & 8B & 32 & 4096 & 209\,/\,43 \\
19	OT-7B & Qwen & 7B & 28 & 3584 & 228\,/\,47 \\
20	R1-32B & Qwen & 32B & 64 & 5120 & 100\,/\,20 \\
21	QwQ-32B & Qwen & 32B & 64 & 5120 & 95\,/\,19 \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20.}
25	\label{tab:models}
26	\end{table}
27	
28	\subsection{Probe Architecture}
29	\label{sec:probe-architecture}
30	
31	\paragraph{Hidden-state (HS) probes.} At each step $t$, we extract the last-token hidden state $\mathbf{h}_t^{(\ell)} \in \mathbb{R}^d$ from layer $\ell$ and train an L2-regularized logistic regression classifier (balanced class weights, $C{=}1.0$, LBFGS, max\_iter${}=2000$) on binary CP labels. Layer selection is analyzed in \cref{sec:layer-sensitivity}.
32	
33	\paragraph{Text probes.} Each step's text is encoded with all-MiniLM-L6-v2~\citep{wang2020minilm} ($\mathbb{R}^{384}$), a distilled sentence encoder from the Sentence-BERT family~\citep{reimers2019sentence}. The same logistic regression is applied as a surface-level modality baseline.
34	
35	\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \ldots, t]$. We evaluate $W \in \{1, 3, 5, 10, 15, 20, 25\}$ and select per-model on validation. GRU sequence models are also evaluated; for fair comparison, \cref{tab:gru_multi_seeds} reports GRU results under the same 60/20/20 split used for all LR experiments (\cref{app:gru_details}).
36	
37	\subsection{Layer Selection Sensitivity}
38	\label{sec:layer-sensitivity}
39	
40	Layer selection is a researcher degree of freedom that can reverse modality comparison conclusions. A composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\% depth) for QwQ-32B, L10 (16\%) for R1-32B. Shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings are noise-driven (\cref{app:cosine_volatility}).
41	
42	A five-metric ablation reveals that threshold-dependent metrics (precision, inverse FPR, additive composite) consistently select deep layers: L60 (94\%) for QwQ-32B, L63 (98\%) for R1-32B. Pure balanced accuracy selects middle layers (L30, L47), paralleling the AUROC pattern (\cref{sec:layer-results}). At these layers, all four models show significant HS advantage (Holm-Bonferroni corrected, \cref{sec:evaluation}); at biased layers, only the two 7--8B models survive. Because the three metrics (balanced accuracy, precision, FPR) share the same confusion matrix, the effective number of independent comparisons is four (one per model); Holm-Bonferroni step-down on four model-level tests yields the same result (all four pass, with R1-8B FPR $p{=}0.044$ at rank-4 threshold $\alpha/1{=}0.050$). A joint (layer, $W$) grid search over 192 configurations confirms that L60 is near-optimal for QwQ-32B at recommended windows ($W{=}3$--$5$; \cref{app:layer_sweep}). Full per-layer results appear in the same appendix.
43	
44	\subsection{Baseline Methods}
45	\label{sec:baselines}
46	
47	We evaluate seven alternatives to contextualize probe performance (\cref{tab:negative}): BOCPD~\citep{adams2007bayesian} and CUSUM~\citep{page1954cusum} for change-point detection; Mahalanobis distance following TrajGuard~\citep{trajguard}; RepE mean-difference directions~\citep{zou2023representation}; two-layer MLP probes; CCS-adapted~\citep{burns2023discovering}; and cross-model transfer via PCA. A position-only baseline ($t/T$) controls for temporal artifacts. Detailed configurations in \cref{app:bocpd_config,app:transfer_details}.
48	
49	\subsection{Evaluation Protocol}
50	\label{sec:evaluation}
51	
52	We report balanced accuracy, precision, pre-CP FPR (step-level and trace-level), coverage, and lead time (steps between first detection and true CP). Detection requires $K{=}5$ consecutive threshold crossings; $K$ was set as a design pre-selection before examining performance, and sensitivity analysis (\cref{app:k_ablation}) confirms that $K \in \{3, 5, 7\}$ produces smooth coverage-FPR tradeoffs without qualitative changes in the modality comparison. Modality comparisons use two-sided null-centered bootstrap (10{,}000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence. Control task selectivity~\citep{hewitt2019control} validates genuine representational structure (\cref{app:control}).
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c864586b-d031-4068-9f2c-176e7130128c",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "13b44375-52c2-456b-929a-c63efc6fa831",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex",
      "content": "\\section{Problem Setup and Methods}\n\\label{sec:method}\n\n\\subsection{Safety Commitment Point}\n\\label{sec:commitment-point}\n\nWhen a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \\textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Steps before CP are \\emph{pre-commitment} ($y_t = 0$); steps at or after CP are \\emph{post-commitment} ($y_t = 1$). The detection task produces a score $s_t \\in [0, 1]$ estimating whether the model has passed its CP by step $t$.\n\nWe study four reasoning models spanning two architectures and two scales (\\cref{tab:models}).\n\n\\begin{table}[t]\n\\centering\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Arch.} & \\textbf{Params} & \\textbf{Layers} & \\textbf{Hidden} & \\textbf{$n$ (total\\,/\\,test)} \\\\\n\\midrule\nR1-8B & Llama & 8B & 32 & 4096 & 209\\,/\\,43 \\\\\nOT-7B & Qwen & 7B & 28 & 3584 & 228\\,/\\,47 \\\\\nR1-32B & Qwen & 32B & 64 & 5120 & 100\\,/\\,20 \\\\\nQwQ-32B & Qwen & 32B & 64 & 5120 & 95\\,/\\,19 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\\citep{deepseekr1}; QwQ-32B~\\citep{qwq} is a native reasoning model; OT-7B~\\citep{openthinker} is trained with STILL~\\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20.}\n\\label{tab:models}\n\\end{table}\n\n\\subsection{Probe Architecture}\n\\label{sec:probe-architecture}\n\n\\paragraph{Hidden-state (HS) probes.} At each step $t$, we extract the last-token hidden state $\\mathbf{h}_t^{(\\ell)} \\in \\mathbb{R}^d$ from layer $\\ell$ and train an L2-regularized logistic regression classifier (balanced class weights, $C{=}1.0$, LBFGS, max\\_iter${}=2000$) on binary CP labels. Layer selection is analyzed in \\cref{sec:layer-sensitivity}.\n\n\\paragraph{Text probes.} Each step's text is encoded with all-MiniLM-L6-v2~\\citep{wang2020minilm} ($\\mathbb{R}^{384}$), a distilled sentence encoder from the Sentence-BERT family~\\citep{reimers2019sentence}. The same logistic regression is applied as a surface-level modality baseline.\n\n\\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \\ldots, t]$. We evaluate $W \\in \\{1, 3, 5, 10, 15, 20, 25\\}$ and select per-model on validation. GRU sequence models are also evaluated; for fair comparison, \\cref{tab:gru_multi_seeds} reports GRU results under the same 60/20/20 split used for all LR experiments (\\cref{app:gru_details}).\n\n\\subsection{Layer Selection Sensitivity}\n\\label{sec:layer-sensitivity}\n\nLayer selection is a researcher degree of freedom that can reverse modality comparison conclusions. A composite metric (balanced accuracy $\\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\\% depth) for QwQ-32B, L10 (16\\%) for R1-32B. Shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings are noise-driven (\\cref{app:cosine_volatility}).\n\nA five-metric ablation reveals that threshold-dependent metrics (precision, inverse FPR, additive composite) consistently select deep layers: L60 (94\\%) for QwQ-32B, L63 (98\\%) for R1-32B. Pure balanced accuracy selects middle layers (L30, L47), paralleling the AUROC pattern (\\cref{sec:layer-results}). At these layers, all four models show significant HS advantage (Holm-Bonferroni corrected, \\cref{sec:evaluation}); at biased layers, only the two 7--8B models survive. Because the three metrics (balanced accuracy, precision, FPR) share the same confusion matrix, the effective number of independent comparisons is four (one per model); Holm-Bonferroni step-down on four model-level tests yields the same result (all four pass, with R1-8B FPR $p{=}0.044$ at rank-4 threshold $\\alpha/1{=}0.050$). A joint (layer, $W$) grid search over 192 configurations confirms that L60 is near-optimal for QwQ-32B at recommended windows ($W{=}3$--$5$; \\cref{app:layer_sweep}). Full per-layer results appear in the same appendix.\n\n\\subsection{Baseline Methods}\n\\label{sec:baselines}\n\nWe evaluate seven alternatives to contextualize probe performance (\\cref{tab:negative}): BOCPD~\\citep{adams2007bayesian} and CUSUM~\\citep{page1954cusum} for change-point detection; Mahalanobis distance following TrajGuard~\\citep{trajguard}; RepE mean-difference directions~\\citep{zou2023representation}; two-layer MLP probes; CCS-adapted~\\citep{burns2023discovering}; and cross-model transfer via PCA. A position-only baseline ($t/T$) controls for temporal artifacts. Detailed configurations in \\cref{app:bocpd_config,app:transfer_details}.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\nWe report balanced accuracy, precision, pre-CP FPR (step-level and trace-level), coverage, and lead time (steps between first detection and true CP). Detection requires $K{=}5$ consecutive threshold crossings; $K$ was set as a design pre-selection before examining performance, and sensitivity analysis (\\cref{app:k_ablation}) confirms that $K \\in \\{3, 5, 7\\}$ produces smooth coverage-FPR tradeoffs without qualitative changes in the modality comparison. Modality comparisons use two-sided null-centered bootstrap (10{,}000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\\times$ 4 models $= 12$ tests, $\\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence. Control task selectivity~\\citep{hewitt2019control} validates genuine representational structure (\\cref{app:control}).\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  },
  "sourceToolAssistantUUID": "c864586b-d031-4068-9f2c-176e7130128c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-18T13:02:46.187Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JwbYAyjy4jFg6eM8FnbSPQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13b44375-52c2-456b-929a-c63efc6fa831",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "a7fdd35f-578b-4023-baf7-729436724364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 47 · 2026-05-18T13:02:46.200Z_

<details><summary>↩ Tool result · `toolu_01JwbYAyjy4jFg6eM8FnbSPQ`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria.
4	
5	\subsection{Setup}\label{sec:setup}
6	
7	We study R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (OpenThinker-7B, trained on the OpenThoughts dataset~\citep{openthinker}; Qwen-7B backbone, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level CP annotations (60/20/20 split). HS probes extract last-token hidden states from a selected layer; text probes encode each step with all-MiniLM-L6-v2 (384d). Both use L2-regularized logistic regression with temporal windowing $W \in \{1, 3, 5, 10, 15, 20, 25\}$ selected on validation. Detection requires $K{=}5$ consecutive threshold crossings. Statistical testing follows \cref{sec:evaluation}.
8	
9	\subsection{Layer Selection Results}\label{sec:layer-results}
10	
11	\cref{tab:layer_selection} shows that the biased composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\% depth) for QwQ-32B and L10 (16\%) for R1-32B. Three of four metrics excluding crossing rate (precision, inverse FPR, and additive composite) consistently select deep layers: L60 (94\%) and L63 (98\%). Pure balanced accuracy, a threshold-free metric, selects middle layers (L30 and L47), consistent with the AUROC pattern discussed in \cref{sec:discussion}. The mechanism is that shallow layers produce highly compressed representations with small inter-step margins: step-to-step cosine distances are 1.4--2.7$\times$ smaller than at deep layers across all four models (\cref{app:cosine_volatility}). A linear probe in this compressed space operates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (\cref{sec:layer-sensitivity}).
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\begin{tabular}{lccc}
17	\toprule
18	\textbf{Model} & \textbf{Biased}$^a$ & \textbf{Corrected}$^b$ & $p$ \textbf{(corr.)} \\
19	\midrule
20	R1-8B & L14 (44\%) & L14 (44\%) & ${<}0.001$ \\
21	OT-7B & L0 (0\%) & L16 (57\%) & ${<}0.001$ \\
22	QwQ-32B & L2 (3\%) & L60 (94\%) & ${<}0.005$ \\
23	R1-32B & L10 (16\%) & L63 (98\%) & ${<}0.001$ \\
24	\bottomrule
25	\end{tabular}
26	\caption{Layer selection sensitivity. $^a$\,bal\_acc $\times$ crossing\_rate. $^b$\,Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Rightmost: HS vs.\ text precision $p$-value at corrected layer (e.g., QwQ-32B biased-layer: bal\_acc $p{=}0.35$, precision $p{=}0.83$, both non-significant).}
27	\label{tab:layer_selection}
28	\end{table}
29	
30	\begin{figure}[t]
31	\centering
32	\includegraphics[width=\columnwidth]{figures/fig_layer_heatmap.pdf}
33	\caption{Per-layer metric heatmap (2$\times$2). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal\_acc $\times$ crossing\_rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers.}
34	\label{fig:layer_heatmap}
35	\end{figure}
36	
37	The downstream impact is severe: at biased layers, only the two 7--8B models show significant HS advantage; both 32B models fail. At corrected layers, all four models pass Holm-Bonferroni correction (\cref{sec:evaluation}). Had we reported only biased-layer results, we would have concluded a scale-dependent HS advantage that is entirely a methodological artifact.
38	
39	\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
40	
41	\begin{table}[t]
42	\centering
43	\small
44	\resizebox{\columnwidth}{!}{%
45	\begin{tabular}{llclrrlrc}
46	\toprule
47	\textbf{Model} & \textbf{Layer} & \textbf{Enc.} & $W$ & $\Delta$\textbf{BA} & $\Delta$\textbf{Prec} & \textbf{95\% CI} & $\Delta$\textbf{FPR} & \textbf{HB} \\
48	\midrule
49	R1-8B & L14 & 384d & 15 & +8.2 & \textbf{+32.5} & [+20.2, +45.2] & $-$7.4 & \checkmark \\
50	 & & 1024d & & \multicolumn{1}{c}{--} & +5.8 & [$-$7.4, +19.5] & \multicolumn{1}{c}{--} & \\[2pt]
51	OT-7B & L16 & 384d & 3 & +10.7 & +21.9 & [+14.4, +29.6] & $-$17.1 & \checkmark \\
52	 & & 1024d & & \multicolumn{1}{c}{--} & +18.1 & [+8.4, +29.0] & \multicolumn{1}{c}{--} & \checkmark \\[2pt]
53	QwQ & L60 & 384d & 3 & +15.4 & +23.6 & [+12.9, +35.1] & $-$9.8 & \checkmark \\
54	 & & 1024d & & \multicolumn{1}{c}{--} & +9.4 & [$-$7.1, +27.7] & \multicolumn{1}{c}{--} & \\[2pt]
55	R1-32B & L63 & 384d & 1 & \textbf{+18.7} & +15.4 & [+8.7, +22.6] & \textbf{$-$14.6} & \checkmark \\
56	 & & 1024d & & \multicolumn{1}{c}{--} & +11.7 & [$-$0.2, +24.3] & \multicolumn{1}{c}{--} & \\
57	\bottomrule
58	\end{tabular}}
59	\caption{HS vs.\ text at corrected layers (LR probes, 60/20/20 split). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\Delta$: HS$-$text difference (pp). 95\% CI: bootstrap interval for $\Delta$Prec (10{,}000 resamples). HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$); all four 384d model-level tests pass. 1024d: HB over 4 model-level precision tests. Values from canonical split; 5-seed mean$\pm$std in \cref{app:multi_seed}.$^*$\,R1-32B: precision std${=}0.128$, FPR std${=}0.145$ across 5 seeds (\cref{app:multi_seed}). BGE $\Delta$BA/$\Delta$FPR in \cref{app:encoder_robustness}.}
60	\label{tab:hs_vs_text}
61	\end{table}
62	
63	Against the 384d baseline, HS probes significantly outperform text probes on all four models across all three metrics (\cref{tab:hs_vs_text}), though R1-8B FPR significance is fragile across seeds (2/5 uncorrected, 1/5 Bonferroni-corrected; \cref{tab:r18b_fpr_seeds}). At 7--8B, the evidence is strong: precision gains of +32.5pp (R1-8B) and +21.9pp (OT-7B), stable across seeds (std ${<}4$pp). R1-8B FPR advantage is directionally consistent across seeds (5/5) but not robust to data split (2/5 reach $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds, 1/5 remains significant; \cref{app:multi_seed}). At 32B, both models are significant (HB corrected) but with model-specific caveats: R1-32B achieves significance only at $W{=}1$ with 25\% coverage (5/20 traces; significance at this coverage means the probe fires reliably on a narrow subset rather than detecting commitment broadly), and QwQ-32B's position baseline is competitive (\cref{sec:32b-analysis}). Control task selectivity confirms genuine safety signal: 12.5--19.7pp above chance (\cref{app:control}).
64	
65	\paragraph{Capacity control.} PCA reduction of HS features to 384d (matching text encoder dimensionality, 79--92\% variance retained) preserves the precision advantage on all four models (+16.8 to +23.1pp, all $p{<}0.012$), with all four model-level precision tests passing Holm-Bonferroni. Two individual metric comparisons are non-significant: R1-8B balanced accuracy (+1.3pp, $p{=}0.731$, effect too small at $n{=}43$) and QwQ-32B FPR ($-$11.4pp, $p{=}0.038$, below HB threshold). PCA retains directions of maximum variance in hidden-state space, which need not align with the semantic dimensions captured by a trained text encoder; the control rules out a pure capacity explanation but not all encoder-quality effects. This confirms a modality effect rather than a capacity artifact.
66	
67	\paragraph{Encoder robustness.} The 1024d rows in \cref{tab:hs_vs_text} replace MiniLM (384d) with BGE-large~\citep{xiao2023cpack} (1024d, a 2.7$\times$ stronger encoder). The HS precision advantage persists directionally on all four models but narrows substantially: only OT-7B survives Holm-Bonferroni (1/4 precision tests). HS balanced accuracy advantage is also directionally positive on all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni; FPR advantage is significant only for OT-7B (1/4). R1-8B shows an adverse FPR direction (HS FPR 1.2pp higher than BGE, $p{=}0.564$). The advantage is encoder-conditional rather than absolute (\cref{fig:forest_precision}). Layer selection (Contribution 1) is encoder-independent, as it concerns hidden-state properties across layers rather than the text baseline.
68	
69	\paragraph{Position mediation.} Position ($t/T$) is a significant component of probe performance across all models: residualization reduces HS balanced accuracy by 12--18pp at optimal $W$ (R1-8B 16.5pp, OT-7B 12.3pp, QwQ-32B 17.7pp), but all models retain substantial non-positional signal (residualized BA 0.61--0.67, all $p{<}0.001$; \cref{app:position_residual}). Temporal windowing reduces position dependence (R1-8B: 24.3pp drop at $W{=}3$ vs.\ 16.5pp at $W{=}15$), and HS residualized probes retain more non-positional signal than text probes (+3.7 to +6.9pp BA gap).
70	
71	\paragraph{Caveats.} R1-32B achieves significance only at $W{=}1$ with 25\% coverage (5/20 traces); at $W{\geq}3$, dimensionality ($51200 \times W$ for $n{=}20$) prevents significance. Sweeping regularization $C$ over $[0.01, 100]$ yields ${<}2$pp variation in balanced accuracy; the HS advantage is also stable across decision thresholds (BA variation ${<}1.5$pp across $\tau \in [0.3, 0.7]$; \cref{app:threshold_sensitivity}). QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps vs.\ text 3.7--12.3 steps): higher precision at later detection. On benign traces, probes produce 39--52\% false alarm rates, so current methods characterize the commitment phenomenon rather than constitute production-ready detectors. Per-model details in \cref{sec:32b-analysis}.
72	
73	\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
74	
75	R1-32B and QwQ-32B share the Qwen-32B architecture (64 layers, 5120 hidden) but present opposite detection profiles (\cref{tab:32b_divergence}); training method is the likely differentiator.
76	
77	\begin{table}[t]
78	\centering
79	\small
80	\begin{tabular}{lcccc}
81	\toprule
82	\textbf{Model} & \textbf{Cov.} & \textbf{Lead (steps)} & \textbf{HB} & \textbf{Pos.\ margin} \\
83	\midrule
84	R1-32B & 25\% & +11.7 to +13.3 & \checkmark{} ($W{=}1$) & +14.2pp \\
85	QwQ-32B & 74\% & $-$1.2 to +1.9 & \checkmark{} (all $W$) & $-$3.6pp \\
86	\bottomrule
87	\end{tabular}
88	\caption{32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$). Pos.\ margin: HS balanced accuracy minus position-only baseline.}
89	\label{tab:32b_divergence}
90	\end{table}
91	
92	R1-32B detects commitment 11--13 steps early with a +14.2pp margin over the position baseline, which confirms genuine representational signal, but covers only 25\% of traces at the single significant window ($W{=}1$). QwQ-32B achieves statistical significance at all window sizes with 74\% coverage, but HS probes fire later than text probes (negative lead time). Consistent with the universal position analysis (\cref{sec:hs-text}), QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\ 0.796). HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are directionally positive but not statistically significant at $n{=}19$. The divergence implies that per-model validation is essential: no single detection configuration generalizes even within the same architecture at the same scale, and a system validated on one 32B model would fail on the other.
93	
94	\subsection{Temporal Context}\label{sec:temporal}
95	
96	Temporal windowing ($W{>}1$) improves both modalities on all four models (\cref{fig:window_ablation}). Text precision improves +8 to +23pp from $W{=}1$ to $W{=}25$; HS precision improves +1.7 to +12.9pp. At 7--8B, the modality advantage (+22 to +33pp precision) exceeds the temporal improvement (+13pp). Both effects are complementary: temporal windowing ($W{=}3$--$15$) combined with principled layer selection yields the most consistent gains. Full per-model temporal ablations appear in \cref{app:temporal_details}.
97	
98	\begin{figure}[t]
99	\centering
100	\includegraphics[width=\columnwidth]{figures/fig_forest_precision.pdf}
101	\caption{Forest plot of HS precision advantage over text probes. Blue: vs.\ MiniLM-384d; orange: vs.\ BGE-1024d. Solid markers: survives Holm-Bonferroni; hollow: does not. All four 384d comparisons are significant; against BGE-1024d, only OT-7B survives correction.}
102	\label{fig:forest_precision}
103	\end{figure}
104	
105	\subsection{Negative Results}\label{sec:negative}
106	
107	\begin{table}[t]
108	\centering
109	\small
110	\begin{tabular}{p{1.5cm}p{2.9cm}p{2.3cm}}
111	\toprule
112	\textbf{Method} & \textbf{Result} & \textbf{Limitation} \\
113	\midrule
114	BOCPD & 0\% det.\ on 3/4 models & Commitment gradual \\
115	CUSUM & $<$ threshold, all models & Same as BOCPD \\
116	Mahalanobis & $\Delta d \approx 0$ & Signal in minor PCs \\
117	RepE & QwQ 0.756; R1-32B 0.559$^a$ & Model-dependent \\
118	MLP & 3/4 worse than LR & Overfitting \\
119	CCS & No gain over supervised$^b$ & Alignment mismatch \\
120	Transfer & Best 59.5\% (PCA)$^c$ & Model-specific repr. \\
121	\bottomrule
122	\end{tabular}
123	\caption{Seven alternative approaches. $^a$\,RepE QwQ approaches supervised bal\_acc but precision is 0.512 vs.\ LR 0.700. $^b$\,Semi-supervised (requires CP labels). $^c$\,Best direct transfer 67.3\% but 1\% crossing rate.}
124	\label{tab:negative}
125	\end{table}
126	
127	No alternative method consistently matches supervised probing across all four models (\cref{tab:negative}). We prioritize precision over balanced accuracy as the primary evaluation criterion because in a hypothetical deployment scenario, false positives on pre-CP steps would waste intervention resources (triggering unnecessary safety responses), while missed post-CP steps merely reduce coverage without causing immediate harm. This framing is critical for interpreting RepE results below.
128	
129	\paragraph{Change-point methods.} BOCPD~\citep{adams2007bayesian} achieves 0\% detection on 3/4 models because safety commitment is gradual rather than abrupt: the probe score sequence transitions smoothly over 5--15 steps without the discontinuity that BOCPD's hazard function requires. On R1-8B (the sole model with non-zero detection), the best BOCPD configuration ($\lambda{=}10$) achieves 93\% detection rate but with lower lead time (+3.5 steps) than simple thresholding (+4.9 steps). CUSUM similarly fails because cumulative evidence never exceeds the decision boundary on smooth transitions. The gradual nature of commitment is itself an empirical finding: it rules out the entire class of abrupt-change detectors and motivates the supervised probe approach that explicitly learns the transition boundary.
130	
131	\paragraph{RepE inconsistency.} RepE computes the class-conditioned mean difference as a fixed direction (analytic), while LR optimizes cross-entropy to learn the classification boundary (iterative). Both require the same labeled data; the key distinction is parameterization, not supervision level. This difference is consequential: RepE mean-difference directions~\citep{zou2023representation} illustrate the metric-dependent nature of method comparison. On QwQ-32B, RepE achieves 0.756 balanced accuracy (comparable to supervised LR at 0.778), but its precision is 0.512 vs.\ LR 0.700 and its FPR is 0.309 vs.\ 0.120. The mean-difference direction captures enough signal to classify steps above chance, but fires indiscriminately on pre-CP steps, producing 2.6$\times$ more false alarms than supervised probes. On R1-32B, RepE nearly fails entirely (0.559 balanced accuracy). The inconsistency across two models sharing the same architecture confirms that a single linear direction computed from class means does not reliably capture safety commitment structure.
132	
133	Cross-model transfer produces no practical utility across 17 configurations; stronger alignment methods (CCA, model stitching~\cite{kornblith2019cka,bansal2021stitching}) remain unexplored. Detailed per-method analysis in \cref{app:negative_details}.
134	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7fdd35f-578b-4023-baf7-729436724364",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "78df9cde-8ccf-4e72-be73-ba2850305a3a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\\label{sec:experiments}\n\nWe evaluate temporal probes across four reasoning models (\\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria.\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe study R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (OpenThinker-7B, trained on the OpenThoughts dataset~\\citep{openthinker}; Qwen-7B backbone, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level CP annotations (60/20/20 split). HS probes extract last-token hidden states from a selected layer; text probes encode each step with all-MiniLM-L6-v2 (384d). Both use L2-regularized logistic regression with temporal windowing $W \\in \\{1, 3, 5, 10, 15, 20, 25\\}$ selected on validation. Detection requires $K{=}5$ consecutive threshold crossings. Statistical testing follows \\cref{sec:evaluation}.\n\n\\subsection{Layer Selection Results}\\label{sec:layer-results}\n\n\\cref{tab:layer_selection} shows that the biased composite metric (balanced accuracy $\\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\\% depth) for QwQ-32B and L10 (16\\%) for R1-32B. Three of four metrics excluding crossing rate (precision, inverse FPR, and additive composite) consistently select deep layers: L60 (94\\%) and L63 (98\\%). Pure balanced accuracy, a threshold-free metric, selects middle layers (L30 and L47), consistent with the AUROC pattern discussed in \\cref{sec:discussion}. The mechanism is that shallow layers produce highly compressed representations with small inter-step margins: step-to-step cosine distances are 1.4--2.7$\\times$ smaller than at deep layers across all four models (\\cref{app:cosine_volatility}). A linear probe in this compressed space operates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (\\cref{sec:layer-sensitivity}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Biased}$^a$ & \\textbf{Corrected}$^b$ & $p$ \\textbf{(corr.)} \\\\\n\\midrule\nR1-8B & L14 (44\\%) & L14 (44\\%) & ${<}0.001$ \\\\\nOT-7B & L0 (0\\%) & L16 (57\\%) & ${<}0.001$ \\\\\nQwQ-32B & L2 (3\\%) & L60 (94\\%) & ${<}0.005$ \\\\\nR1-32B & L10 (16\\%) & L63 (98\\%) & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Layer selection sensitivity. $^a$\\,bal\\_acc $\\times$ crossing\\_rate. $^b$\\,Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Rightmost: HS vs.\\ text precision $p$-value at corrected layer (e.g., QwQ-32B biased-layer: bal\\_acc $p{=}0.35$, precision $p{=}0.83$, both non-significant).}\n\\label{tab:layer_selection}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_layer_heatmap.pdf}\n\\caption{Per-layer metric heatmap (2$\\times$2). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal\\_acc $\\times$ crossing\\_rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers.}\n\\label{fig:layer_heatmap}\n\\end{figure}\n\nThe downstream impact is severe: at biased layers, only the two 7--8B models show significant HS advantage; both 32B models fail. At corrected layers, all four models pass Holm-Bonferroni correction (\\cref{sec:evaluation}). Had we reported only biased-layer results, we would have concluded a scale-dependent HS advantage that is entirely a methodological artifact.\n\n\\subsection{HS vs.\\ Text Comparison}\\label{sec:hs-text}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llclrrlrc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{Enc.} & $W$ & $\\Delta$\\textbf{BA} & $\\Delta$\\textbf{Prec} & \\textbf{95\\% CI} & $\\Delta$\\textbf{FPR} & \\textbf{HB} \\\\\n\\midrule\nR1-8B & L14 & 384d & 15 & +8.2 & \\textbf{+32.5} & [+20.2, +45.2] & $-$7.4 & \\checkmark \\\\\n & & 1024d & & \\multicolumn{1}{c}{--} & +5.8 & [$-$7.4, +19.5] & \\multicolumn{1}{c}{--} & \\\\[2pt]\nOT-7B & L16 & 384d & 3 & +10.7 & +21.9 & [+14.4, +29.6] & $-$17.1 & \\checkmark \\\\\n & & 1024d & & \\multicolumn{1}{c}{--} & +18.1 & [+8.4, +29.0] & \\multicolumn{1}{c}{--} & \\checkmark \\\\[2pt]\nQwQ & L60 & 384d & 3 & +15.4 & +23.6 & [+12.9, +35.1] & $-$9.8 & \\checkmark \\\\\n & & 1024d & & \\multicolumn{1}{c}{--} & +9.4 & [$-$7.1, +27.7] & \\multicolumn{1}{c}{--} & \\\\[2pt]\nR1-32B & L63 & 384d & 1 & \\textbf{+18.7} & +15.4 & [+8.7, +22.6] & \\textbf{$-$14.6} & \\checkmark \\\\\n & & 1024d & & \\multicolumn{1}{c}{--} & +11.7 & [$-$0.2, +24.3] & \\multicolumn{1}{c}{--} & \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{HS vs.\\ text at corrected layers (LR probes, 60/20/20 split). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\\Delta$: HS$-$text difference (pp). 95\\% CI: bootstrap interval for $\\Delta$Prec (10{,}000 resamples). HB: \\checkmark{} = model-level test passes Holm-Bonferroni ($\\alpha{=}0.05$); all four 384d model-level tests pass. 1024d: HB over 4 model-level precision tests. Values from canonical split; 5-seed mean$\\pm$std in \\cref{app:multi_seed}.$^*$\\,R1-32B: precision std${=}0.128$, FPR std${=}0.145$ across 5 seeds (\\cref{app:multi_seed}). BGE $\\Delta$BA/$\\Delta$FPR in \\cref{app:encoder_robustness}.}\n\\label{tab:hs_vs_text}\n\\end{table}\n\nAgainst the 384d baseline, HS probes significantly outperform text probes on all four models across all three metrics (\\cref{tab:hs_vs_text}), though R1-8B FPR significance is fragile across seeds (2/5 uncorrected, 1/5 Bonferroni-corrected; \\cref{tab:r18b_fpr_seeds}). At 7--8B, the evidence is strong: precision gains of +32.5pp (R1-8B) and +21.9pp (OT-7B), stable across seeds (std ${<}4$pp). R1-8B FPR advantage is directionally consistent across seeds (5/5) but not robust to data split (2/5 reach $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds, 1/5 remains significant; \\cref{app:multi_seed}). At 32B, both models are significant (HB corrected) but with model-specific caveats: R1-32B achieves significance only at $W{=}1$ with 25\\% coverage (5/20 traces; significance at this coverage means the probe fires reliably on a narrow subset rather than detecting commitment broadly), and QwQ-32B's position baseline is competitive (\\cref{sec:32b-analysis}). Control task selectivity confirms genuine safety signal: 12.5--19.7pp above chance (\\cref{app:control}).\n\n\\paragraph{Capacity control.} PCA reduction of HS features to 384d (matching text encoder dimensionality, 79--92\\% variance retained) preserves the precision advantage on all four models (+16.8 to +23.1pp, all $p{<}0.012$), with all four model-level precision tests passing Holm-Bonferroni. Two individual metric comparisons are non-significant: R1-8B balanced accuracy (+1.3pp, $p{=}0.731$, effect too small at $n{=}43$) and QwQ-32B FPR ($-$11.4pp, $p{=}0.038$, below HB threshold). PCA retains directions of maximum variance in hidden-state space, which need not align with the semantic dimensions captured by a trained text encoder; the control rules out a pure capacity explanation but not all encoder-quality effects. This confirms a modality effect rather than a capacity artifact.\n\n\\paragraph{Encoder robustness.} The 1024d rows in \\cref{tab:hs_vs_text} replace MiniLM (384d) with BGE-large~\\citep{xiao2023cpack} (1024d, a 2.7$\\times$ stronger encoder). The HS precision advantage persists directionally on all four models but narrows substantially: only OT-7B survives Holm-Bonferroni (1/4 precision tests). HS balanced accuracy advantage is also directionally positive on all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni; FPR advantage is significant only for OT-7B (1/4). R1-8B shows an adverse FPR direction (HS FPR 1.2pp higher than BGE, $p{=}0.564$). The advantage is encoder-conditional rather than absolute (\\cref{fig:forest_precision}). Layer selection (Contribution 1) is encoder-independent, as it concerns hidden-state properties across layers rather than the text baseline.\n\n\\paragraph{Position mediation.} Position ($t/T$) is a significant component of probe performance across all models: residualization reduces HS balanced accuracy by 12--18pp at optimal $W$ (R1-8B 16.5pp, OT-7B 12.3pp, QwQ-32B 17.7pp), but all models retain substantial non-positional signal (residualized BA 0.61--0.67, all $p{<}0.001$; \\cref{app:position_residual}). Temporal windowing reduces position dependence (R1-8B: 24.3pp drop at $W{=}3$ vs.\\ 16.5pp at $W{=}15$), and HS residualized probes retain more non-positional signal than text probes (+3.7 to +6.9pp BA gap).\n\n\\paragraph{Caveats.} R1-32B achieves significance only at $W{=}1$ with 25\\% coverage (5/20 traces); at $W{\\geq}3$, dimensionality ($51200 \\times W$ for $n{=}20$) prevents significance. Sweeping regularization $C$ over $[0.01, 100]$ yields ${<}2$pp variation in balanced accuracy; the HS advantage is also stable across decision thresholds (BA variation ${<}1.5$pp across $\\tau \\in [0.3, 0.7]$; \\cref{app:threshold_sensitivity}). QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps vs.\\ text 3.7--12.3 steps): higher precision at later detection. On benign traces, probes produce 39--52\\% false alarm rates, so current methods characterize the commitment phenomenon rather than constitute production-ready detectors. Per-model details in \\cref{sec:32b-analysis}.\n\n\\subsection{32B Model-Specific Analysis}\\label{sec:32b-analysis}\n\nR1-32B and QwQ-32B share the Qwen-32B architecture (64 layers, 5120 hidden) but present opposite detection profiles (\\cref{tab:32b_divergence}); training method is the likely differentiator.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Cov.} & \\textbf{Lead (steps)} & \\textbf{HB} & \\textbf{Pos.\\ margin} \\\\\n\\midrule\nR1-32B & 25\\% & +11.7 to +13.3 & \\checkmark{} ($W{=}1$) & +14.2pp \\\\\nQwQ-32B & 74\\% & $-$1.2 to +1.9 & \\checkmark{} (all $W$) & $-$3.6pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: \\checkmark{} = model-level test passes Holm-Bonferroni ($\\alpha{=}0.05$). Pos.\\ margin: HS balanced accuracy minus position-only baseline.}\n\\label{tab:32b_divergence}\n\\end{table}\n\nR1-32B detects commitment 11--13 steps early with a +14.2pp margin over the position baseline, which confirms genuine representational signal, but covers only 25\\% of traces at the single significant window ($W{=}1$). QwQ-32B achieves statistical significance at all window sizes with 74\\% coverage, but HS probes fire later than text probes (negative lead time). Consistent with the universal position analysis (\\cref{sec:hs-text}), QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\\ 0.796). HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are directionally positive but not statistically significant at $n{=}19$. The divergence implies that per-model validation is essential: no single detection configuration generalizes even within the same architecture at the same scale, and a system validated on one 32B model would fail on the other.\n\n\\subsection{Temporal Context}\\label{sec:temporal}\n\nTemporal windowing ($W{>}1$) improves both modalities on all four models (\\cref{fig:window_ablation}). Text precision improves +8 to +23pp from $W{=}1$ to $W{=}25$; HS precision improves +1.7 to +12.9pp. At 7--8B, the modality advantage (+22 to +33pp precision) exceeds the temporal improvement (+13pp). Both effects are complementary: temporal windowing ($W{=}3$--$15$) combined with principled layer selection yields the most consistent gains. Full per-model temporal ablations appear in \\cref{app:temporal_details}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_forest_precision.pdf}\n\\caption{Forest plot of HS precision advantage over text probes. Blue: vs.\\ MiniLM-384d; orange: vs.\\ BGE-1024d. Solid markers: survives Holm-Bonferroni; hollow: does not. All four 384d comparisons are significant; against BGE-1024d, only OT-7B survives correction.}\n\\label{fig:forest_precision}\n\\end{figure}\n\n\\subsection{Negative Results}\\label{sec:negative}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{p{1.5cm}p{2.9cm}p{2.3cm}}\n\\toprule\n\\textbf{Method} & \\textbf{Result} & \\textbf{Limitation} \\\\\n\\midrule\nBOCPD & 0\\% det.\\ on 3/4 models & Commitment gradual \\\\\nCUSUM & $<$ threshold, all models & Same as BOCPD \\\\\nMahalanobis & $\\Delta d \\approx 0$ & Signal in minor PCs \\\\\nRepE & QwQ 0.756; R1-32B 0.559$^a$ & Model-dependent \\\\\nMLP & 3/4 worse than LR & Overfitting \\\\\nCCS & No gain over supervised$^b$ & Alignment mismatch \\\\\nTransfer & Best 59.5\\% (PCA)$^c$ & Model-specific repr. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Seven alternative approaches. $^a$\\,RepE QwQ approaches supervised bal\\_acc but precision is 0.512 vs.\\ LR 0.700. $^b$\\,Semi-supervised (requires CP labels). $^c$\\,Best direct transfer 67.3\\% but 1\\% crossing rate.}\n\\label{tab:negative}\n\\end{table}\n\nNo alternative method consistently matches supervised probing across all four models (\\cref{tab:negative}). We prioritize precision over balanced accuracy as the primary evaluation criterion because in a hypothetical deployment scenario, false positives on pre-CP steps would waste intervention resources (triggering unnecessary safety responses), while missed post-CP steps merely reduce coverage without causing immediate harm. This framing is critical for interpreting RepE results below.\n\n\\paragraph{Change-point methods.} BOCPD~\\citep{adams2007bayesian} achieves 0\\% detection on 3/4 models because safety commitment is gradual rather than abrupt: the probe score sequence transitions smoothly over 5--15 steps without the discontinuity that BOCPD's hazard function requires. On R1-8B (the sole model with non-zero detection), the best BOCPD configuration ($\\lambda{=}10$) achieves 93\\% detection rate but with lower lead time (+3.5 steps) than simple thresholding (+4.9 steps). CUSUM similarly fails because cumulative evidence never exceeds the decision boundary on smooth transitions. The gradual nature of commitment is itself an empirical finding: it rules out the entire class of abrupt-change detectors and motivates the supervised probe approach that explicitly learns the transition boundary.\n\n\\paragraph{RepE inconsistency.} RepE computes the class-conditioned mean difference as a fixed direction (analytic), while LR optimizes cross-entropy to learn the classification boundary (iterative). Both require the same labeled data; the key distinction is parameterization, not supervision level. This difference is consequential: RepE mean-difference directions~\\citep{zou2023representation} illustrate the metric-dependent nature of method comparison. On QwQ-32B, RepE achieves 0.756 balanced accuracy (comparable to supervised LR at 0.778), but its precision is 0.512 vs.\\ LR 0.700 and its FPR is 0.309 vs.\\ 0.120. The mean-difference direction captures enough signal to classify steps above chance, but fires indiscriminately on pre-CP steps, producing 2.6$\\times$ more false alarms than supervised probes. On R1-32B, RepE nearly fails entirely (0.559 balanced accuracy). The inconsistency across two models sharing the same architecture confirms that a single linear direction computed from class means does not reliably capture safety commitment structure.\n\nCross-model transfer produces no practical utility across 17 configurations; stronger alignment methods (CCA, model stitching~\\cite{kornblith2019cka,bansal2021stitching}) remain unexplored. Detailed per-method analysis in \\cref{app:negative_details}.\n",
      "numLines": 134,
      "startLine": 1,
      "totalLines": 134
    }
  },
  "sourceToolAssistantUUID": "a7fdd35f-578b-4023-baf7-729436724364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-18T13:02:46.692Z_

<details open><summary>🔧 Tool call — Read · `toolu_015WExtHwx7kRRFjPNY2Yin7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78df9cde-8ccf-4e72-be73-ba2850305a3a",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "542552d0-a8b1-45d2-ae78-238f5139b02e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 49 · 2026-05-18T13:02:46.697Z_

<details><summary>↩ Tool result · `toolu_015WExtHwx7kRRFjPNY2Yin7`</summary>

```text
1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models introduce a qualitatively new failure mode: the model's own chain of thought can transition from safety-aware deliberation to harmful generation without adversarial input modification~\cite{wang2025lrmsafety}.
5	
6	\textit{Attack characterization.} Self-jailbreak has been documented with step-level annotations~\cite{harmthoughts}, with longer chains increasing circumvention probability~\cite{selfjailbreak}. Reasoning models can autonomously jailbreak other LLMs with 97\% success~\cite{hagendorff2026lrm_jailbreak}. H-CoT~\cite{hcot2025} shows reasoning chains can be externally hijacked. Unfaithful reasoning~\cite{chen2025unfaithful} further motivates hidden-state monitoring that bypasses text. Safety-aligned models maintain refusal intentions during thinking but experience a sharp drop at output generation~\cite{yin2025refusal_cliff}, a phenomenon our temporal probes target. Refusal dynamics in standard LLMs~\cite{hu2026refusal_dynamics} and information leakage in traces~\cite{ahrend2026safer_traces} provide additional context.
7	
8	\textit{Detection.} CoT monitoring can detect reward hacking but optimization pressure promotes obfuscation~\cite{baker2025monitoring}. CoT monitorability is valuable but fragile~\cite{korbak2025cot_monitorability}. GuardReasoner~\cite{xiang2025guardreasoner} trains a dedicated reasoning-based guard model.
9	
10	\textit{Mitigation.} SafeThink~\cite{safethink} steers early reasoning toward safety, SafeRemind~\cite{saferemind} inserts entropy-triggered reminders, and Chain-of-Guardrails~\cite{mao2025selfjailbreak_reasoning} proposes guardrail insertion during reasoning. None of these conducts a systematic modality comparison for commitment detection.
11	
12	\paragraph{Hidden-State Safety Detection.}
13	Internal activations can detect safety violations in standard LLMs. \citet{zhou2024alignment} show safety-relevant information distributes across layers, while \citet{qi2025shallow_alignment} find that alignment operates primarily over early output tokens. \citet{arditi2024refusal} identify a single refusal direction, but \citet{zhao2025harmfulness} show harmfulness and refusal are encoded separately. \citet{joad2026refusal_multi} reveal eleven category-specific refusal directions, and \citet{wollschlager2025geometry} formalize multi-dimensionality through concept cones, consistent with our finding that single-direction methods are insufficient. TrajGuard~\cite{trajguard} uses Mahalanobis distance from safe trajectories; SafeSwitch~\cite{safeswitch} trains hidden-state classifiers; SIREN~\cite{siren} monitors internal representations during generation; SafeDream~\cite{safedream2026} proposes proactive world models for detection. These methods assume threats from external input manipulation and operate at the token level on instruction-tuned models. The self-jailbreak setting differs because transitions are internal and span multiple reasoning steps. \citet{kadali2025internal} decompose internal layer representations to separate jailbreak from benign prompts; their results confirm that layer-wise structure carries safety-relevant signal. We reproduce TrajGuard (\cref{sec:negative}) and find its geometric approach fails because discriminative signal resides in minor PCA components.
14	
15	\paragraph{Probing Methodology and Layer Selection.}
16	Linear probing has a long history from layer-wise classifiers~\cite{alain2017understanding} through sentence probing~\cite{conneau2018probing} to comprehensive surveys~\cite{belinkov2019analysis,belinkov2022probing}. Layer-wise analyses reveal hierarchical linguistic structure across depth~\cite{jawahar2019bert,liu2019linguistic}, and information-theoretic formulations address probe complexity~\cite{voita2020information,pimentel2020information}. \citet{hewitt2019control} introduce control tasks to distinguish structure from memorization, which we adopt (\cref{app:control}). \citet{belrose2023leace} establish theoretical limits on linear probe extraction; \citet{elazar2021amnesic} test whether probed information is causally used. \citet{tenney2019bert} show syntactic information in middle layers and semantics in deeper layers. \citet{zhang2025probing_selfverify} apply hidden-state probing to self-verification in reasoning models, a complementary perspective on what reasoning-model representations encode. Concurrent work by \citet{alvarez2026transport_geometry} uses hidden-state geometry for step-level hallucination detection; the approach shares our temporal probing framework but targets a different phenomenon. \citet{boxo2025linear_probes} show that linear probes can rely on textual evidence rather than deeper representations, which motivates our comparison of hidden-state probes against text-based monitors. Despite this foundation, layer selection remains underexamined: most studies select by a single metric without sensitivity analysis. We demonstrate that this practice can reverse a study's central conclusion (\cref{sec:layer-results}).
17	
18	\paragraph{Change-Point Detection.}
19	BOCPD~\cite{adams2007bayesian} detects abrupt distributional shifts; CCS~\cite{burns2023discovering} discovers latent truth directions via consistency constraints; RepE~\cite{zou2023representation} identifies concept directions through mean differences. We adapt all three to temporal commitment detection (\cref{sec:negative}). BOCPD and CUSUM fail because commitment is gradual. CCS provides no gain because its consistency objective misaligns with temporal structure. RepE shows inconsistent performance across models (0.756 on QwQ, 0.559 on R1-32B). These failures motivate supervised probes with principled layer selection as the minimal effective methodology.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "542552d0-a8b1-45d2-ae78-238f5139b02e",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "d726caa4-9ac6-4f3e-bf10-f1533bbc921b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related-work}\n\n\\paragraph{Safety in Reasoning Models.}\nReasoning models introduce a qualitatively new failure mode: the model's own chain of thought can transition from safety-aware deliberation to harmful generation without adversarial input modification~\\cite{wang2025lrmsafety}.\n\n\\textit{Attack characterization.} Self-jailbreak has been documented with step-level annotations~\\cite{harmthoughts}, with longer chains increasing circumvention probability~\\cite{selfjailbreak}. Reasoning models can autonomously jailbreak other LLMs with 97\\% success~\\cite{hagendorff2026lrm_jailbreak}. H-CoT~\\cite{hcot2025} shows reasoning chains can be externally hijacked. Unfaithful reasoning~\\cite{chen2025unfaithful} further motivates hidden-state monitoring that bypasses text. Safety-aligned models maintain refusal intentions during thinking but experience a sharp drop at output generation~\\cite{yin2025refusal_cliff}, a phenomenon our temporal probes target. Refusal dynamics in standard LLMs~\\cite{hu2026refusal_dynamics} and information leakage in traces~\\cite{ahrend2026safer_traces} provide additional context.\n\n\\textit{Detection.} CoT monitoring can detect reward hacking but optimization pressure promotes obfuscation~\\cite{baker2025monitoring}. CoT monitorability is valuable but fragile~\\cite{korbak2025cot_monitorability}. GuardReasoner~\\cite{xiang2025guardreasoner} trains a dedicated reasoning-based guard model.\n\n\\textit{Mitigation.} SafeThink~\\cite{safethink} steers early reasoning toward safety, SafeRemind~\\cite{saferemind} inserts entropy-triggered reminders, and Chain-of-Guardrails~\\cite{mao2025selfjailbreak_reasoning} proposes guardrail insertion during reasoning. None of these conducts a systematic modality comparison for commitment detection.\n\n\\paragraph{Hidden-State Safety Detection.}\nInternal activations can detect safety violations in standard LLMs. \\citet{zhou2024alignment} show safety-relevant information distributes across layers, while \\citet{qi2025shallow_alignment} find that alignment operates primarily over early output tokens. \\citet{arditi2024refusal} identify a single refusal direction, but \\citet{zhao2025harmfulness} show harmfulness and refusal are encoded separately. \\citet{joad2026refusal_multi} reveal eleven category-specific refusal directions, and \\citet{wollschlager2025geometry} formalize multi-dimensionality through concept cones, consistent with our finding that single-direction methods are insufficient. TrajGuard~\\cite{trajguard} uses Mahalanobis distance from safe trajectories; SafeSwitch~\\cite{safeswitch} trains hidden-state classifiers; SIREN~\\cite{siren} monitors internal representations during generation; SafeDream~\\cite{safedream2026} proposes proactive world models for detection. These methods assume threats from external input manipulation and operate at the token level on instruction-tuned models. The self-jailbreak setting differs because transitions are internal and span multiple reasoning steps. \\citet{kadali2025internal} decompose internal layer representations to separate jailbreak from benign prompts; their results confirm that layer-wise structure carries safety-relevant signal. We reproduce TrajGuard (\\cref{sec:negative}) and find its geometric approach fails because discriminative signal resides in minor PCA components.\n\n\\paragraph{Probing Methodology and Layer Selection.}\nLinear probing has a long history from layer-wise classifiers~\\cite{alain2017understanding} through sentence probing~\\cite{conneau2018probing} to comprehensive surveys~\\cite{belinkov2019analysis,belinkov2022probing}. Layer-wise analyses reveal hierarchical linguistic structure across depth~\\cite{jawahar2019bert,liu2019linguistic}, and information-theoretic formulations address probe complexity~\\cite{voita2020information,pimentel2020information}. \\citet{hewitt2019control} introduce control tasks to distinguish structure from memorization, which we adopt (\\cref{app:control}). \\citet{belrose2023leace} establish theoretical limits on linear probe extraction; \\citet{elazar2021amnesic} test whether probed information is causally used. \\citet{tenney2019bert} show syntactic information in middle layers and semantics in deeper layers. \\citet{zhang2025probing_selfverify} apply hidden-state probing to self-verification in reasoning models, a complementary perspective on what reasoning-model representations encode. Concurrent work by \\citet{alvarez2026transport_geometry} uses hidden-state geometry for step-level hallucination detection; the approach shares our temporal probing framework but targets a different phenomenon. \\citet{boxo2025linear_probes} show that linear probes can rely on textual evidence rather than deeper representations, which motivates our comparison of hidden-state probes against text-based monitors. Despite this foundation, layer selection remains underexamined: most studies select by a single metric without sensitivity analysis. We demonstrate that this practice can reverse a study's central conclusion (\\cref{sec:layer-results}).\n\n\\paragraph{Change-Point Detection.}\nBOCPD~\\cite{adams2007bayesian} detects abrupt distributional shifts; CCS~\\cite{burns2023discovering} discovers latent truth directions via consistency constraints; RepE~\\cite{zou2023representation} identifies concept directions through mean differences. We adapt all three to temporal commitment detection (\\cref{sec:negative}). BOCPD and CUSUM fail because commitment is gradual. CCS provides no gain because its consistency objective misaligns with temporal structure. RepE shows inconsistent performance across models (0.756 on QwQ, 0.559 on R1-32B). These failures motivate supervised probes with principled layer selection as the minimal effective methodology.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "542552d0-a8b1-45d2-ae78-238f5139b02e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-18T13:02:47.180Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FESgZ3SB5WkGjJSKKHRC3j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d726caa4-9ac6-4f3e-bf10-f1533bbc921b",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "52aaf49a-190c-4939-b614-213f5fedb7e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 51 · 2026-05-18T13:02:47.184Z_

<details><summary>↩ Tool result · `toolu_01FESgZ3SB5WkGjJSKKHRC3j`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Layer selection as researcher degree of freedom.}
4	Layer selection is an underexamined methodological choice in the probing literature that can silently determine a study's conclusions. Our five-metric ablation (\cref{sec:layer-results}) demonstrates that a single metric component, the crossing rate, reverses the central finding: at biased layers, the HS advantage appears scale-dependent; at corrected layers, all four models are significant (\cref{sec:evaluation}). The mechanism is representation compression at shallow layers (\cref{app:cosine_volatility}), which pushes a linear probe to the noise floor and inflates crossing rate independently of discriminative power. Any composite metric that incorporates crossing rate is susceptible to this bias, and we hypothesize the effect generalizes beyond safety probing to any threshold-based detection study. We recommend that probing studies report results under at least two complementary layer selection criteria and that multi-metric ablations become standard practice.
5	
6	\paragraph{Temporal context and modality choice.}
7	Both temporal context and modality choice improve detection, but their relative magnitudes differ by scale: at 7--8B, the modality advantage exceeds temporal improvement (\cref{sec:temporal}); at 32B, relative magnitudes are model-dependent. Temporal windowing ($W{=}3$ to $15$) provides consistent improvement regardless of modality, while modality choice requires principled layer selection.
8	
9	\paragraph{Encoder-conditional advantage.}
10	Part of the observed advantage may reflect text encoder quality rather than hidden-state informational superiority. At matched 384d dimensionality via PCA (79--92\% variance retained), the precision advantage persists on all four models (+16.8 to +23.1pp, all four model-level precision tests pass Holm-Bonferroni), eliminating capacity gap as the sole explanation. A stronger 1024d encoder closes most of the significance gap (1/4 HB-significant), suggesting a continuum rather than a binary modality distinction. The HS advantage has two separable components: a robust modality effect that survives dimensionality matching, and an encoder-dependent magnitude component that narrows with stronger baselines.
11	
12	\paragraph{Cross-model divergence and design implications.}
13	R1-32B and QwQ-32B share architecture but present opposite detection profiles (\cref{tab:32b_divergence}), with training method (distillation vs.\ native reasoning) as the likely differentiator; per-model validation is essential. If future work achieves acceptable false positive rates, our results suggest temporal windowing ($W{=}3$--$15$) with principled layer selection as a starting configuration. At 7--8B, HS probes Pareto-dominate text probes, robust across 5 seeds (precision std ${<}8$pp); at 32B ($n{=}19$--$20$), higher variance (R1-32B std $= 12.8$pp) warrants sample-limited interpretation (\cref{sec:32b-analysis}). Safe-trace FPR of 39--52\% and the 85.5\% oracle gap (\cref{sec:oracle}) confirm that current probes characterize the commitment phenomenon rather than provide operational detection. PCA capacity control, control task selectivity, and position residualization (HS retains +3.7 to +6.9pp more non-positional signal than text; \cref{app:position_residual}) provide converging evidence that the HS advantage reflects genuine safety representations; direct erasure methods (LEACE; \citealp{belrose2023leace}) remain untested.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52aaf49a-190c-4939-b614-213f5fedb7e6",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "c3ccb668-c298-45f3-9e5e-921f410c2ec1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Layer selection as researcher degree of freedom.}\nLayer selection is an underexamined methodological choice in the probing literature that can silently determine a study's conclusions. Our five-metric ablation (\\cref{sec:layer-results}) demonstrates that a single metric component, the crossing rate, reverses the central finding: at biased layers, the HS advantage appears scale-dependent; at corrected layers, all four models are significant (\\cref{sec:evaluation}). The mechanism is representation compression at shallow layers (\\cref{app:cosine_volatility}), which pushes a linear probe to the noise floor and inflates crossing rate independently of discriminative power. Any composite metric that incorporates crossing rate is susceptible to this bias, and we hypothesize the effect generalizes beyond safety probing to any threshold-based detection study. We recommend that probing studies report results under at least two complementary layer selection criteria and that multi-metric ablations become standard practice.\n\n\\paragraph{Temporal context and modality choice.}\nBoth temporal context and modality choice improve detection, but their relative magnitudes differ by scale: at 7--8B, the modality advantage exceeds temporal improvement (\\cref{sec:temporal}); at 32B, relative magnitudes are model-dependent. Temporal windowing ($W{=}3$ to $15$) provides consistent improvement regardless of modality, while modality choice requires principled layer selection.\n\n\\paragraph{Encoder-conditional advantage.}\nPart of the observed advantage may reflect text encoder quality rather than hidden-state informational superiority. At matched 384d dimensionality via PCA (79--92\\% variance retained), the precision advantage persists on all four models (+16.8 to +23.1pp, all four model-level precision tests pass Holm-Bonferroni), eliminating capacity gap as the sole explanation. A stronger 1024d encoder closes most of the significance gap (1/4 HB-significant), suggesting a continuum rather than a binary modality distinction. The HS advantage has two separable components: a robust modality effect that survives dimensionality matching, and an encoder-dependent magnitude component that narrows with stronger baselines.\n\n\\paragraph{Cross-model divergence and design implications.}\nR1-32B and QwQ-32B share architecture but present opposite detection profiles (\\cref{tab:32b_divergence}), with training method (distillation vs.\\ native reasoning) as the likely differentiator; per-model validation is essential. If future work achieves acceptable false positive rates, our results suggest temporal windowing ($W{=}3$--$15$) with principled layer selection as a starting configuration. At 7--8B, HS probes Pareto-dominate text probes, robust across 5 seeds (precision std ${<}8$pp); at 32B ($n{=}19$--$20$), higher variance (R1-32B std $= 12.8$pp) warrants sample-limited interpretation (\\cref{sec:32b-analysis}). Safe-trace FPR of 39--52\\% and the 85.5\\% oracle gap (\\cref{sec:oracle}) confirm that current probes characterize the commitment phenomenon rather than provide operational detection. PCA capacity control, control task selectivity, and position residualization (HS retains +3.7 to +6.9pp more non-positional signal than text; \\cref{app:position_residual}) provide converging evidence that the HS advantage reflects genuine safety representations; direct erasure methods (LEACE; \\citealp{belrose2023leace}) remain untested.\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  },
  "sourceToolAssistantUUID": "52aaf49a-190c-4939-b614-213f5fedb7e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-18T13:02:47.658Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T72iuk9ASHnT3GsitfzK55`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3ccb668-c298-45f3-9e5e-921f410c2ec1",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "13303a16-0d9d-4bb2-8ec0-c1eb7ff82441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 53 · 2026-05-18T13:02:47.664Z_

<details><summary>↩ Tool result · `toolu_01T72iuk9ASHnT3GsitfzK55`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We present the first controlled comparison of hidden-state and text-based probes for safety commitment detection in reasoning models, evaluated across four models spanning two architectures and two scales.
4	The central finding is methodological: a composite layer selection metric incorporating crossing rate reverses the study's main conclusion at 32B scale, while threshold-dependent metrics excluding crossing rate consistently select deep layers where all four models pass Holm-Bonferroni correction (precision +15.4 to +32.5pp over MiniLM-384d). At 7--8B the advantage is robust; at 32B, model-specific caveats apply (\cref{sec:32b-analysis}). The advantage is encoder-conditional: it narrows substantially against BGE-large-1024d (1/4 models significant).
5	Future work should close the 85.5\% oracle gap through causal intervention techniques~\citep{meng2022rome}, extend to multilingual and multi-turn settings, and explore stronger cross-model alignment methods beyond PCA-based transfer.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13303a16-0d9d-4bb2-8ec0-c1eb7ff82441",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "b66e291a-10e4-44d9-b0fb-81b633de74c2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe present the first controlled comparison of hidden-state and text-based probes for safety commitment detection in reasoning models, evaluated across four models spanning two architectures and two scales.\nThe central finding is methodological: a composite layer selection metric incorporating crossing rate reverses the study's main conclusion at 32B scale, while threshold-dependent metrics excluding crossing rate consistently select deep layers where all four models pass Holm-Bonferroni correction (precision +15.4 to +32.5pp over MiniLM-384d). At 7--8B the advantage is robust; at 32B, model-specific caveats apply (\\cref{sec:32b-analysis}). The advantage is encoder-conditional: it narrows substantially against BGE-large-1024d (1/4 models significant).\nFuture work should close the 85.5\\% oracle gap through causal intervention techniques~\\citep{meng2022rome}, extend to multilingual and multi-turn settings, and explore stronger cross-model alignment methods beyond PCA-based transfer.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  },
  "sourceToolAssistantUUID": "13303a16-0d9d-4bb2-8ec0-c1eb7ff82441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-18T13:02:48.105Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UavbdxaAqc6kgTNbeq8qkk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b66e291a-10e4-44d9-b0fb-81b633de74c2",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "caa3c67c-3220-4f12-acde-fc97a6a4bdf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 55 · 2026-05-18T13:02:48.112Z_

<details><summary>↩ Tool result · `toolu_01UavbdxaAqc6kgTNbeq8qkk`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	\paragraph{32B model-specific caveats.}
4	R1-32B achieves significance only at $W{=}1$ (25\% coverage, 5/20 traces); dimensionality ($51200 \times W$ for $n{=}20$) prevents larger windows. QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\ HS 0.796) and HS lead time is negative. Position residualization reduces balanced accuracy by 12--18pp across all models, though all retain substantial non-positional signal (\cref{app:position_residual}). Multi-seed analysis (\cref{app:multi_seed}) confirms scale-dependent robustness: 7--8B precision std ${<}8$pp across 5 seeds, while R1-32B std $= 12.8$pp. This motivates a two-tier framing: 7--8B results are robust; 32B results are sample-limited with caveats.
5	
6	\paragraph{High false positive rate and oracle gap.}
7	Safe-trace FPR is 39--52\% at standard thresholds, so current probes characterize the phenomenon rather than constitute production detectors. The 85.5\% oracle gap confirms that passive probing captures only a fraction of available signal.
8	
9	\paragraph{Cumulative hyperparameter selection.}
10	Layer (up to 64), $W$ (7 values), $K$ (5 values), and threshold are selected on the same validation set ($n{=}4$--$9$ per-class validation traces at 32B scale), yielding up to $64 \times 7 \times 5 = 2{,}240$ configurations. $C$-insensitivity (${<}2$pp) covers one hyperparameter; the cumulative researcher degrees of freedom are substantial, particularly at 32B where per-fold sample sizes are small. $K$ was set as a design pre-selection (\cref{app:k_ablation}), and the $K \times W$ joint surface is not fully explored. Joint (layer, $W$) stability was verified via grid search for QwQ-32B ($W \in \{1,3,5\}$; \cref{app:layer_sweep}), but full leave-one-fold-out validation of the (layer, $W$) pair and extension to R1-32B remain for future work. Bootstrap CIs at $n{=}19$--$20$ may exhibit below-nominal coverage~\citep{efron1993bootstrap}; $p$-value resolution with 10{,}000 resamples is $10^{-4}$.
11	
12	\paragraph{CP annotation uncertainty.}
13	CP annotations follow the HarmThoughts methodology~\citep{harmthoughts}, which defines commitment points through content analysis of reasoning steps. We do not independently evaluate inter-annotator agreement (IAA). If CP annotation error is ${\geq}2$ steps, the reported lead times (+4.5 to +13 steps) may partially fall within annotation noise, particularly at the lower end of this range. Future work should quantify annotation reliability and assess its impact on probe evaluation.
14	
15	\paragraph{Scope.}
16	We cover 2 architectures and 2 scales (7--8B, 32B); intermediate scales (13B, 70B) and proprietary reasoning models (o1, o3) are missing. The text baseline uses MiniLM-384d; BGE-large-1024d narrows the gap (1/4 HB-significant). All results use HarmThoughts; generalization to multi-turn, multilingual, or encoded-prompt settings is untested. Probing results are correlational; causal intervention is needed to confirm mechanistic involvement.
17	
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caa3c67c-3220-4f12-acde-fc97a6a4bdf5",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "2c80301d-ca18-4796-8dc5-613d17bf418c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex",
      "content": "\\section{Limitations}\\label{sec:limitations}\n\n\\paragraph{32B model-specific caveats.}\nR1-32B achieves significance only at $W{=}1$ (25\\% coverage, 5/20 traces); dimensionality ($51200 \\times W$ for $n{=}20$) prevents larger windows. QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\\ HS 0.796) and HS lead time is negative. Position residualization reduces balanced accuracy by 12--18pp across all models, though all retain substantial non-positional signal (\\cref{app:position_residual}). Multi-seed analysis (\\cref{app:multi_seed}) confirms scale-dependent robustness: 7--8B precision std ${<}8$pp across 5 seeds, while R1-32B std $= 12.8$pp. This motivates a two-tier framing: 7--8B results are robust; 32B results are sample-limited with caveats.\n\n\\paragraph{High false positive rate and oracle gap.}\nSafe-trace FPR is 39--52\\% at standard thresholds, so current probes characterize the phenomenon rather than constitute production detectors. The 85.5\\% oracle gap confirms that passive probing captures only a fraction of available signal.\n\n\\paragraph{Cumulative hyperparameter selection.}\nLayer (up to 64), $W$ (7 values), $K$ (5 values), and threshold are selected on the same validation set ($n{=}4$--$9$ per-class validation traces at 32B scale), yielding up to $64 \\times 7 \\times 5 = 2{,}240$ configurations. $C$-insensitivity (${<}2$pp) covers one hyperparameter; the cumulative researcher degrees of freedom are substantial, particularly at 32B where per-fold sample sizes are small. $K$ was set as a design pre-selection (\\cref{app:k_ablation}), and the $K \\times W$ joint surface is not fully explored. Joint (layer, $W$) stability was verified via grid search for QwQ-32B ($W \\in \\{1,3,5\\}$; \\cref{app:layer_sweep}), but full leave-one-fold-out validation of the (layer, $W$) pair and extension to R1-32B remain for future work. Bootstrap CIs at $n{=}19$--$20$ may exhibit below-nominal coverage~\\citep{efron1993bootstrap}; $p$-value resolution with 10{,}000 resamples is $10^{-4}$.\n\n\\paragraph{CP annotation uncertainty.}\nCP annotations follow the HarmThoughts methodology~\\citep{harmthoughts}, which defines commitment points through content analysis of reasoning steps. We do not independently evaluate inter-annotator agreement (IAA). If CP annotation error is ${\\geq}2$ steps, the reported lead times (+4.5 to +13 steps) may partially fall within annotation noise, particularly at the lower end of this range. Future work should quantify annotation reliability and assess its impact on probe evaluation.\n\n\\paragraph{Scope.}\nWe cover 2 architectures and 2 scales (7--8B, 32B); intermediate scales (13B, 70B) and proprietary reasoning models (o1, o3) are missing. The text baseline uses MiniLM-384d; BGE-large-1024d narrows the gap (1/4 HB-significant). All results use HarmThoughts; generalization to multi-turn, multilingual, or encoded-prompt settings is untested. Probing results are correlational; causal intervention is needed to confirm mechanistic involvement.\n\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "caa3c67c-3220-4f12-acde-fc97a6a4bdf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-18T13:02:48.613Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YRzNYdi7GLzmN3hYmD5mq2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c80301d-ca18-4796-8dc5-613d17bf418c",
  "isSidechain": false,
  "requestId": "req_011CbA5ZEUzkWb9HMxneE5hD",
  "type": "assistant",
  "uuid": "bebb4622-93c4-4aa7-b757-73cebcd6cced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118dmRimhyWpefu9dUjK76b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1298,
      "cache_read_input_tokens": 32282,
      "output_tokens": 791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 791,
          "cache_read_input_tokens": 32282,
          "cache_creation_input_tokens": 1298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1298
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

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。  ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models - **路径**: projects/contrastive_trace_safety/docs/p…",
  "leafUuid": "bebb4622-93c4-4aa7-b757-73cebcd6cced",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on layer selection sensitivity in safety probes",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


### Tool result

_source line 59 · 2026-05-18T13:02:48.882Z_

<details><summary>↩ Tool result · `toolu_01YRzNYdi7GLzmN3hYmD5mq2`</summary>

```text
1	\appendix
2	
3	\section{Responsible NLP Research Checklist}
4	\label{app:checklist}
5	
6	We address the ARR Responsible NLP Research requirements below.
7	
8	\begin{itemize}
9	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
10	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this risk, as evasion requires white-box access to the probe, which a deployed monitoring system would not expose.
11	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
12	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.
13	    \item \textbf{Human subjects:} No human subjects research was conducted.
14	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
15	\end{itemize}
16	
17	
18	\section{Layer Sweep Results}
19	\label{app:layer_sweep}
20	
21	For each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\times$ crossing rate (the biased composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The biased composite systematically selects shallow layers for 32B models because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. Three threshold-dependent metrics (precision, inverse FPR, additive composite) converge on deep layers for all models; pure balanced accuracy selects middle layers for 32B models (L30 for QwQ-32B, L47 for R1-32B).
22	
23	\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\% depth). OT-7B: biased metric selects L0 (0\%), unbiased consensus selects L16 (57\%). QwQ-32B: biased metric selects L2 (3\%), unbiased consensus selects L60 (94\%). R1-32B: biased metric selects L10 (16\%), unbiased consensus selects L63 (98\%). The bias is most extreme for 64-layer models, where the composite metric selects layers in the bottom 16\% of the network while threshold-dependent metrics select layers above 94\%. Pure balanced accuracy selects middle layers (L30 at 47\% for QwQ-32B, L47 at 73\% for R1-32B), consistent with the AUROC pattern.
24	
25	\paragraph{Impact on modality comparison.} At the biased layers, HS vs.\ text precision $p$-values are 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant. At the corrected deep layers, all $p$-values fall below 0.005. The initially reported ``scale-dependent'' pattern (HS advantage at 7--8B but not 32B) was entirely an artifact of layer selection methodology, not a genuine property of model scale (\cref{sec:layer-results}).
26	
27	\paragraph{Layer selection stability (LOO-CV).} Leave-one-out cross-validation on the validation set confirms that layer selection is robust to data composition regardless of metric. Under pure balanced accuracy, the dominant layer is selected in 68\% (QwQ-32B: L30, 13/19 folds) and 65\% (R1-32B: L47, 13/20 folds) of folds. Alternative selections cluster in neighboring layers (L29, L55--56 for QwQ; L32, L38, L43 for R1-32B). The consensus corrected layers (L60, L63) are similarly dominant under threshold-dependent selection.
28	
29	\paragraph{Joint (layer, $W$) sensitivity.} To verify that the corrected layer is not an artifact of a single window size, we evaluate QwQ-32B across 64 layers $\times$ 3 windows ($W \in \{1, 3, 5\}$), yielding 192 configurations (\cref{tab:joint_layer_w}). L60 is near-optimal: within 2.1pp of the global best at $W{=}3$ and the top-ranked layer at $W{=}5$. The optimal layer shifts from middle-deep (L46--47 at $W{=}1$) to deep (L60 at $W{=}5$), confirming a layer-window interaction. L30, selected by per-fold LOO-CV at $W{=}1$ under balanced accuracy, is suboptimal across all windows (max BA $= 0.769$ vs.\ global best 0.817). Joint (layer, $W$) stability was evaluated via grid search on $W \in \{1, 3, 5\}$ for QwQ-32B only; full leave-one-fold-out validation of the (layer, $W$) pair and extension to R1-32B remain for future work.
30	
31	\begin{table}[h]
32	\centering
33	\small
34	\caption{QwQ-32B joint (layer, $W$) grid search. L60 is near-optimal at recommended windows ($W{=}3$--$5$). L30 (LOO-CV selection at $W{=}1$) is suboptimal across all windows.}
35	\label{tab:joint_layer_w}
36	\begin{tabular}{clccc}
37	\toprule
38	$W$ & \textbf{Best layer} & \textbf{Best BA} & \textbf{L60 BA} & \textbf{L60 rank} \\
39	\midrule
40	1 & L47 & 0.798 & 0.783 & $\sim$15th \\
41	3 & L46 & 0.817 & 0.796 & $\sim$6th \\
42	5 & L60 & 0.808 & 0.808 & 1st \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	
48	\section{Representation Compression Analysis}
49	\label{app:cosine_volatility}
50	
51	We measure step-to-step cosine distance at biased (shallow) vs.\ corrected (deep) layers across all four models to characterize the compression mechanism underlying the crossing rate bias (\cref{tab:cosine_volatility}).
52	
53	\begin{table}[h]
54	\centering
55	\small
56	\caption{Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4--2.7$\times$ smaller inter-step distances).}
57	\label{tab:cosine_volatility}
58	\begin{tabular}{llcc}
59	\toprule
60	\textbf{Model} & \textbf{Layer (type)} & \textbf{Mean} & \textbf{Std} \\
61	\midrule
62	R1-8B & L2 (biased) & 0.186 & 0.097 \\
63	 & L14 (corrected) & 0.411 & 0.143 \\[2pt]
64	OT-7B & L2 (biased) & 0.077 & 0.080 \\
65	 & L16 (corrected) & 0.206 & 0.091 \\[2pt]
66	QwQ-32B & L2 (biased) & 0.037 & 0.064 \\
67	 & L60 (corrected) & 0.102 & 0.075 \\[2pt]
68	R1-32B & L10 (biased) & 0.067 & 0.050 \\
69	 & L63 (corrected) & 0.092 & 0.076 \\
70	\bottomrule
71	\end{tabular}
72	\end{table}
73	
74	Shallow layers produce highly compressed representations: consecutive steps cluster within small cosine distances (0.04--0.19), while deep-layer representations spread more widely (0.09--0.41). Inter-step distances at shallow layers are 1.4--2.7$\times$ smaller than at deep layers across all four models. A linear probe operating in this compressed space sits near the noise floor, where minor numerical fluctuations produce spurious threshold crossings that inflate crossing rate independently of discriminative power. Deep layers produce well-separated representations where crossings correspond to genuine semantic transitions.
75	
76	
77	\section{Holm-Bonferroni Step-Down Correction}
78	\label{app:holm_bonferroni}
79	
80	\cref{tab:holm_bonferroni} reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the conservative 12-test correction and the 4-test model-level correction: both yield the same outcome (all tests pass at $\alpha{=}0.05$). Under 4-test HB, the tightest threshold falls on R1-8B FPR ($p{=}0.044$, rank-4 threshold $\alpha/1{=}0.050$), which still passes. Tests are ranked by $p$-value; each test $i$ (rank $i$ of $m$) must satisfy $p_i < \alpha / (m - i + 1)$ under the step-down procedure.
81	
82	\begin{table}[h]
83	\centering
84	\small
85	\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}
86	\label{tab:holm_bonferroni}
87	\setlength{\tabcolsep}{4pt}
88	\begin{tabular}{clllcc}
89	\toprule
90	\textbf{Rank} & \textbf{Model} & \textbf{Metric} & \textbf{$p$-val} & \textbf{Thresh.} & \textbf{Pass} \\
91	\midrule
92	1  & R1-8B  & Precision & $<$0.001 & 0.0042 & \checkmark \\
93	2  & OT-7B  & Bal.\ Acc. & $<$0.001 & 0.0045 & \checkmark \\
94	3  & OT-7B  & Precision & $<$0.001 & 0.0050 & \checkmark \\
95	4  & OT-7B  & FPR & $<$0.001 & 0.0056 & \checkmark \\
96	5  & QwQ-32B & Bal.\ Acc. & $<$0.001 & 0.0063 & \checkmark \\
97	6  & QwQ-32B & Precision & $<$0.001 & 0.0071 & \checkmark \\
98	7  & R1-32B & Bal.\ Acc. & $<$0.001 & 0.0083 & \checkmark \\
99	8  & R1-32B & Precision & $<$0.001 & 0.0100 & \checkmark \\
100	9  & QwQ-32B & FPR & 0.004 & 0.0125 & \checkmark \\
101	10 & R1-8B  & Bal.\ Acc. & 0.005 & 0.0167 & \checkmark \\
102	11 & R1-32B & FPR & 0.007 & 0.0250 & \checkmark \\
103	12 & R1-8B  & FPR & 0.044 & 0.0500 & \checkmark \\
104	\bottomrule
105	\end{tabular}
106	\end{table}
107	
108	The weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B showing the largest precision gap (+32.5pp). This reflects R1-8B's already-low text FPR (11.8\%), which leaves less room for HS improvement on this metric.
109	
110	\paragraph{Exact sign-flip permutation test validation.} As an independent check on bootstrap significance for the small-sample 32B models, we run exact sign-flip permutation tests on all six 32B comparisons, enumerating all $2^n$ sign permutations ($2^{19}{=}524{,}288$ for QwQ-32B, $2^{20}{=}1{,}048{,}576$ for R1-32B). All six tests reject the null at $\alpha{=}0.05$: QwQ-32B (bal\_acc $p{<}0.001$, precision $p{=}0.003$, FPR $p{<}0.001$); R1-32B (bal\_acc $p{=}0.008$, precision $p{<}0.001$, FPR $p{=}0.004$). The permutation $p$-values are consistent with the bootstrap values in \cref{tab:holm_bonferroni}, confirming that the bootstrap-based conclusions are not artifacts of distributional assumptions at small $n$.
111	
112	
113	\section{Window Size Ablation Details}
114	\label{app:window_ablation}
115	
116	\cref{tab:window_full} reports the complete window size ablation across all four models and seven window sizes. The main text (\cref{sec:temporal}) presents R1-8B results; here we provide the full data. \cref{fig:window_ablation} visualizes the monotonic improvement on R1-8B: precision rises from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) while FPR drops from 9.65\% to 4.8\%.
117	
118	\begin{figure}[h]
119	\centering
120	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
121	\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}
122	\label{fig:window_ablation}
123	\end{figure}
124	
125	\begin{table}[h]
126	\centering
127	\small
128	\caption{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models.}
129	\label{tab:window_full}
130	\resizebox{\columnwidth}{!}{%
131	\begin{tabular}{llccccc}
132	\toprule
133	Model & $W$ & Bal.\ Acc. & Precision & FPR$_{\text{step}}$ & Coverage & Lead \\
134	\midrule
135	\multirow{7}{*}{R1-8B}
136	 & 1  & 77.8 & 69.3 & 9.65 & 72.1 & 13.8 \\
137	 & 3  & 79.0 & 72.3 & 8.50 & 69.8 & 12.1 \\
138	 & 5  & 78.1 & 72.6 & 8.09 & 65.1 & 8.3 \\
139	 & 10 & 79.3 & 74.3 & 7.61 & 55.8 & 10.0 \\
140	 & 15 & 80.2 & 77.7 & 6.39 & 51.2 & 7.2 \\
141	 & 20 & 80.7 & 78.6 & 6.12 & 53.5 & 7.4 \\
142	 & 25 & 81.0 & 82.2 & 4.83 & 48.8 & 8.1 \\
143	\midrule
144	\multirow{7}{*}{OT-7B}
145	 & 1  & 68.2 & 42.8 & 12.0 & 53.2 & 16.1 \\
146	 & 3  & \textbf{68.8} & 46.6 & 10.0 & 53.2 & 21.6 \\
147	 & 5  & 68.1 & 46.4 & 9.9 & 53.2 & 21.7 \\
148	 & 10 & 66.5 & 46.9 & 8.6 & 48.9 & 25.0 \\
149	 & 15 & 66.4 & 48.8 & 7.7 & 44.7 & 39.6 \\
150	 & 20 & 66.0 & \textbf{49.4} & \textbf{7.5} & 48.9 & 17.9 \\
151	 & 25 & 65.9 & 48.9 & 8.0 & 51.1 & 28.3 \\
152	\midrule
153	\multirow{7}{*}{R1-32B}
154	 & 1  & 71.8 & 54.9 & 32.03 & 80.0 & 12.9 \\
155	 & 3  & 72.5 & 56.0 & 30.64 & 80.0 & 11.4 \\
156	 & 5  & 73.1 & 57.5 & 28.41 & 75.0 & 11.1 \\
157	 & 10 & 73.7 & 60.9 & 23.40 & 70.0 & 10.8 \\
158	 & 15 & 72.1 & 59.1 & 24.51 & 70.0 & 10.9 \\
159	 & 20 & 69.6 & 56.3 & 26.18 & 65.0 & 9.6 \\
160	 & 25 & 70.3 & 56.6 & 26.46 & 70.0 & 10.7 \\
161	\midrule
162	\multirow{7}{*}{QwQ-32B}
163	 & 1  & 73.0 & 54.4 & 22.76 & 79.0 & 19.7 \\
164	 & 3  & 74.5 & 56.5 & 21.41 & 73.7 & 20.6 \\
165	 & 5  & 76.1 & 57.3 & 21.68 & 73.7 & 20.1 \\
166	 & 10 & 74.7 & 57.1 & 20.73 & 73.7 & 18.4 \\
167	 & 15 & 74.1 & 58.2 & 19.11 & 68.4 & 15.8 \\
168	 & 20 & 75.4 & 60.2 & 17.89 & 63.2 & 15.8 \\
169	 & 25 & 76.2 & 61.8 & 16.94 & 57.9 & 14.9 \\
170	\bottomrule
171	\end{tabular}}%
172	\end{table}
173	
174	Key cross-model patterns emerge from the window ablation:
175	
176	\paragraph{R1-8B} shows a general upward trend in balanced accuracy from 77.8\% ($W{=}1$) to 81.0\% ($W{=}25$), gaining +3.2pp overall with a slight dip at $W{=}5$ (78.1\%). Precision improves sharply (+12.9pp) and step-level FPR halves (9.65\% to 4.83\%). Coverage trades off against quality, dropping from 72.1\% to 48.8\%.
177	
178	\paragraph{OT-7B} exhibits a split temporal pattern at layer 16: balanced accuracy peaks at $W{=}3$ (68.8\%) and declines at larger windows ($-$2.9pp by $W{=}25$), while precision and FPR continue improving. Precision rises from 42.8\% ($W{=}1$) to 49.4\% ($W{=}20$), and FPR drops from 12.0\% to 7.5\% over the same range. The split indicates that larger windows reduce false alarms and sharpen positive predictions even as overall classification accuracy degrades. Lead times are shorter than old layer-0 estimates (16.1--39.6 steps) due to the corrected layer selection (\cref{app:ot7b_details}). OT-7B text probes improve monotonically across all metrics (\cref{app:ot7b_details}), so the accuracy saturation is specific to HS probes on this model.
179	
180	\paragraph{R1-32B} exhibits a non-monotonic pattern: balanced accuracy peaks at $W{=}10$ (73.7\%) and then declines, falling below the $W{=}1$ baseline by $W{=}20$ (69.6\%). The optimal window for R1-32B is $W{=}10$, which achieves the lowest FPR (23.40\%) and highest precision (60.9\%). The accuracy degradation at large windows likely reflects overfitting on the smaller dataset ($n{=}100$).
181	
182	\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
183	
184	\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.
185	
186	\subsection{Text Probe Window Ablation}
187	\label{app:text_window}
188	
189	\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
190	
191	\begin{table}[h]
192	\centering
193	\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}
194	\label{tab:text_window}
195	\begin{tabular}{lcccc}
196	\toprule
197	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
198	\midrule
199	 1  & 64.7 & 41.6 & 25.8 & 95.4 \\
200	 3  & 66.9 & 44.8 & 23.1 & 90.7 \\
201	 5  & 69.2 & 48.5 & 20.4 & 84.9 \\
202	 10 & 72.1 & 54.3 & 16.7 & 74.4 \\
203	 15 & 74.3 & 58.9 & 14.2 & 67.4 \\
204	 20 & 75.8 & 62.1 & 12.5 & 62.8 \\
205	 25 & 76.7 & 64.8 & 11.8 & 58.1 \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	Text probes show monotonic improvement across all window sizes without the plateau observed in HS probes (which saturate around $W{=}15$). The absolute FPR reduction ($-$14.0pp) is nearly three times the HS reduction ($-$4.8pp), and accuracy gains (+12.0pp vs.\ +3.2pp) are four times larger. This asymmetry supports the interpretation that temporal context is the primary factor in commitment detection: text features, which encode less information per step, benefit proportionally more from observing the multi-step progression.
211	
212	
213	\section{OpenThinker-7B Detailed Results}
214	\label{app:ot7b_details}
215	
216	OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
217	
218	\paragraph{Layer sweep.}
219	
220	\begin{table}[h]
221	\centering
222	\small
223	\caption{OT-7B layer sweep. Score = balanced accuracy $\times$ crossing rate. Layer 16 (57\% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.}
224	\label{tab:ot7b_layer_sweep}
225	\setlength{\tabcolsep}{4pt}
226	\begin{tabular}{lcccc}
227	\toprule
228	Layer & Depth & Bal.\ Acc. & Cross.\ Rate & Score \\
229	\midrule
230	0 (embed.) & 0 & 66.7 & 53.2 & 35.5 \\
231	4 & 14 & 66.3 & 40.4 & 26.8 \\
232	8 & 29 & 66.4 & 25.5 & 17.0 \\
233	12 & 43 & 67.5 & 31.9 & 21.6 \\
234	16 & 57 & 68.2 & 31.9 & 21.8 \\
235	20 & 71 & 65.5 & 31.9 & 20.9 \\
236	24 & 86 & 66.9 & 29.8 & 19.9 \\
237	27 & 96 & 63.0 & 31.9 & 20.1 \\
238	\bottomrule
239	\end{tabular}
240	\end{table}
241	
242	After correction of a layer selection bug, layer 16 (57\% depth) is selected. It achieves the highest balanced accuracy (68.2\%) among transformer layers and is consistent with the mid-depth pattern of R1-8B (44\%). Layer 0 (embedding) has a higher crossing rate (53.2\% vs.\ 31.9\%) but lower accuracy.
243	
244	\paragraph{Text probe window ablation.}
245	
246	\begin{table}[h]
247	\centering
248	\small
249	\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}
250	\label{tab:ot7b_text_window}
251	\begin{tabular}{lcccc}
252	\toprule
253	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
254	\midrule
255	 1  & 58.1 & 24.5 & 34.5 & 63.8 \\
256	 3  & 57.9 & 25.4 & 27.1 & 74.5 \\
257	 5  & 56.9 & 24.7 & 25.5 & 70.2 \\
258	 10 & 58.3 & 27.0 & 22.2 & 70.2 \\
259	 15 & 58.9 & 28.3 & 20.0 & 66.0 \\
260	 20 & 60.9 & 31.6 & 17.6 & 66.0 \\
261	 25 & 61.4 & 32.9 & 16.1 & 66.0 \\
262	\bottomrule
263	\end{tabular}
264	\end{table}
265	
266	OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
267	
268	\paragraph{Bootstrap comparison (matched $W{=}3$).} To ensure a fair modality comparison, bootstrap tests use matched $W{=}3$ for both HS and text probes. At $W{=}3$, HS probes achieve 75.3\% trace-level balanced accuracy vs.\ 65.6\% for text (bootstrap $\Delta{=}$+10.7pp, 95\% CI [4.9, 16.3], $p{<}0.001$, survives Holm-Bonferroni). Precision: 55.8\% vs.\ 34.6\% (bootstrap $\Delta{=}$+21.9pp, 95\% CI [14.0, 29.6], $p{<}0.001$, survives Holm-Bonferroni). Pre-CP FPR: 10.0\% vs.\ 27.1\% (bootstrap $\Delta{=}{-}17.1$pp, 95\% CI [$-$22.2, $-$12.2], $p{<}0.001$, survives Holm-Bonferroni). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (+21.9pp); the small discrepancy reflects resampling variance. Using each modality's optimal $W$ (HS at $W{=}3$, text at $W{=}25$) would introduce a confound because text would benefit from 8$\times$ more temporal context.
269	
270	
271	\section{GRU Training Details}
272	\label{app:gru_details}
273	
274	\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
275	
276	\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.
277	
278	\paragraph{Training procedure.} We train with Adam (learning rate $1 \times 10^{-3}$, default $\beta_1{=}0.9$, $\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.
279	
280	\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\pm$ standard deviation.
281	
282	\paragraph{Per-seed results for R1-8B (single-layer GRU).}
283	
284	\begin{table}[h]
285	\centering
286	\small
287	\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}
288	\label{tab:gru_seeds}
289	\setlength{\tabcolsep}{4pt}
290	\begin{tabular}{lccc}
291	\toprule
292	Seed & Peak Acc. & Crossing Acc. & Lead (steps) \\
293	\midrule
294	1 & 85.2 & 74.3 & +4.8 \\
295	2 & 83.1 & 71.6 & +4.8 \\
296	3 & 83.4 & 70.4 & +0.9 \\
297	\midrule
298	Mean $\pm$ std & 83.9 $\pm$ 1.1 & 72.1 $\pm$ 2.0 & +3.5 $\pm$ 2.3 \\
299	\bottomrule
300	\end{tabular}
301	\end{table}
302	
303	The high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.
304	
305	\paragraph{Multi-layer GRU and baseline comparison (60/20/20 protocol).}
306	
307	\begin{table}[h]
308	\centering
309	\scriptsize
310	\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}
311	\label{tab:gru_multi_seeds}
312	\resizebox{\columnwidth}{!}{%
313	\begin{tabular}{llccccc}
314	\toprule
315	Model & Seed & Acc & Prec & FPR & Cross.\% & Lead \\
316	\midrule
317	GRU-single & 42  & 0.845 & 0.657 & 0.139 & 72.1\% & 3.55 \\
318	GRU-single & 123 & 0.760 & 0.454 & 0.191 & 65.1\% & 7.39 \\
319	GRU-single & 456 & 0.792 & 0.474 & 0.203 & 67.4\% & 8.45 \\
320	\rowcolor{gray!10}
321	GRU-single & \textit{mean} & 0.799$\pm$0.035 & 0.528$\pm$0.091 & 0.178$\pm$0.028 & 68.2$\pm$2.9\% & 6.46$\pm$2.10 \\
322	\midrule
323	GRU-multi  & 42  & 0.824 & 0.616 & 0.164 & 74.4\% & 5.66 \\
324	GRU-multi  & 123 & 0.759 & 0.454 & 0.195 & 65.1\% & 6.43 \\
325	GRU-multi  & 456 & 0.784 & 0.460 & 0.207 & 65.1\% & 8.93 \\
326	\rowcolor{gray!10}
327	GRU-multi  & \textit{mean} & 0.789$\pm$0.027 & 0.510$\pm$0.075 & 0.189$\pm$0.018 & 68.2$\pm$4.4\% & 7.01$\pm$1.40 \\
328	\midrule
329	LR-single  & 42  & 0.841 & 0.693 & 0.097 & 46.5\% & $-$2.00 \\
330	LR-single  & 123 & 0.753 & 0.436 & 0.181 & 53.5\% & 5.26 \\
331	LR-single  & 456 & 0.814 & 0.512 & 0.146 & 41.9\% & 3.94 \\
332	\rowcolor{gray!10}
333	LR-single  & \textit{mean} & 0.803$\pm$0.037 & 0.547$\pm$0.108 & 0.141$\pm$0.035 & 47.3$\pm$4.8\% & 2.40$\pm$3.16 \\
334	\midrule
335	LR-multi   & 42  & 0.827 & 0.679 & 0.092 & 39.5\% & 1.06 \\
336	LR-multi   & 123 & 0.756 & 0.442 & 0.180 & 46.5\% & 7.30 \\
337	LR-multi   & 456 & 0.817 & 0.521 & 0.130 & 34.9\% & 4.00 \\
338	\rowcolor{gray!10}
339	LR-multi   & \textit{mean} & 0.800$\pm$0.032 & 0.547$\pm$0.099 & 0.134$\pm$0.036 & 40.3$\pm$4.8\% & 4.12$\pm$2.55 \\
340	\bottomrule
341	\end{tabular}}%
342	\end{table}
343	
344	Under this protocol, multi-layer GRU achieves the highest mean lead (7.01$\pm$1.40 steps) but at higher FPR than logistic regression baselines (0.189 vs.\ 0.134). The GRU advantage is concentrated in detection timing rather than classification accuracy, consistent with the main text finding that GRUs capture sequential dependencies that improve early detection. Lead time shows high variance across seeds (range 5.66--8.93 for GRU-multi), reinforcing that reported means should be interpreted cautiously.
345	
346	\paragraph{OT-7B multi-layer GRU (layers 13--19, 3 seeds, 60/20/20 split).}
347	OT-7B GRU achieves 74.6$\pm$1.3\% balanced accuracy, 64.5$\pm$7.0\% coverage, +33.6$\pm$4.8 steps lead, and 27.4$\pm$6.1\% pre-CP FPR. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average ${\sim}$80 reasoning steps (vs.\ ${\sim}$30 for R1-8B and 32B models), so absolute lead times are not directly comparable. The FPR-lead tradeoff mirrors R1-8B: GRU FPR (27.4\%) is far above the LR probe at layer 16 (10.0\%), confirming that GRUs gain lead time at the cost of more false alarms across both 7-8B models.
348	
349	
350	\section{Control Task Methodology}
351	\label{app:control}
352	
353	We follow the selectivity framework of \cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.
354	
355	\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) across all steps while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:
356	\begin{equation}
357	    \text{Selectivity} = \text{Acc}_{\text{linguistic}} - \text{Acc}_{\text{control}}
358	\end{equation}
359	where $\text{Acc}_{\text{linguistic}}$ is the probe accuracy on true labels and $\text{Acc}_{\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information.
360	
361	\paragraph{Results.} We repeat the control experiment 5 times (10 for OT-7B) with different random permutations and report the mean control accuracy. Selectivity scores at corrected layers are: R1-32B 19.7pp (layer 63), OT-7B 18.3pp (layer 16), QwQ-32B 14.4pp (layer 60), R1-8B 12.5pp (layer 14). All values exceed the 5pp threshold recommended by \cite{hewitt2019control}. R1-32B achieves the strongest selectivity (19.7pp) at the corrected layer, a 2.6$\times$ increase from 7.5pp at the biased layer L10. OT-7B achieves the second-highest selectivity at a mid-depth transformer layer (57\%), consistent with R1-8B's pattern at 44\% depth. On QwQ-32B, the position baseline accuracy (0.705) slightly exceeds the HS probe (0.667) at L60, consistent with the main-text finding that QwQ's HS advantage is concentrated in precision and FPR rather than balanced accuracy.
362	
363	\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 14.4pp at L60 (comparable to 15.3pp at L2), confirming that safety-specific signal persists at deep layers.
364	
365	\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\% FPR compared to 8.1\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.
366	
367	
368	\section{Oracle Upper Bound Analysis}
369	\label{sec:oracle}
370	
371	We compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. This provides a theoretical ceiling on early detection performance.
372	
373	On R1-8B, the oracle achieves +31 steps mean lead time compared to +4.5 steps for the best learned probe (GRU), yielding an oracle gap of 85.5\%. This gap indicates that hidden states at step $t$ encode the model's current safety state but carry limited predictive power about future trajectory evolution. The learned probe captures the contemporaneous safety signal effectively (balanced accuracy 81--84\%) but cannot anticipate the commitment transition far in advance. Closing this gap will likely require causal intervention techniques (e.g., activation patching) rather than improvements to passive monitoring.
374	
375	
376	\section{BOCPD/CUSUM Configuration Sweep}
377	\label{app:bocpd_config}
378	
379	We sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.
380	
381	\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\lambda$ controls the prior probability of a change-point at each step ($P(\text{change}) = 1/\lambda$).
382	
383	\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.
384	
385	\begin{table}[h]
386	\centering
387	\small
388	\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}
389	\label{tab:cpd_sweep}
390	\setlength{\tabcolsep}{4pt}
391	\begin{tabular}{llcc}
392	\toprule
393	Method & Configuration & Det.\ Rate & Lead \\
394	\midrule
395	\multirow{5}{*}{BOCPD}
396	 & $\lambda = 5$   & 97 & +2.1 \\
397	 & $\lambda = 10$  & 93 & +3.5 \\
398	 & $\lambda = 20$  & 87 & +4.2 \\
399	 & $\lambda = 50$  & 72 & +5.8 \\
400	 & $\lambda = 100$ & 67.4 & +1.03 \\
401	\midrule
402	\multirow{10}{*}{CUSUM}
403	 & $\delta{=}0.3$, $h{=}3$ & 65.1 & +0.89 \\
404	 & $\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\
405	 & $\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\
406	 & $\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\
407	 & $\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\
408	 & $\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\
409	 & $\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\
410	 & $\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\
411	 & $\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\
412	 & $\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\
413	\midrule
414	Simple threshold & FCP baseline & 65.1 & +4.89 \\
415	\bottomrule
416	\end{tabular}
417	\end{table}
418	
419	The best BOCPD configuration ($\lambda{=}10$) achieves 93.0\% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1\% detection with superior lead (+4.89 steps). All CUSUM configurations underperform the simple threshold on lead time.
420	
421	These results reveal a coverage-timing tradeoff. BOCPD ($\lambda{=}10$) achieves 28pp higher detection rate than simple thresholding (93.0\% vs.\ 65.1\%), but with lower lead (+3.45 vs.\ +4.89 steps). The transition toward unsafe reasoning is gradual rather than abrupt, so change-point methods cannot exploit discontinuities for early warning. When missed detections are costly, BOCPD's coverage advantage justifies its use despite the timing penalty. When early intervention is the priority, simple thresholding provides better lead time.
422	
423	\paragraph{Other models.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). The probe score sequences for these models show smoother transitions that never trigger the hazard function, consistent with the gradual commitment pattern. R1-8B's higher detection rate likely reflects its sharper probe score transitions at commitment boundaries.
424	
425	
426	\section{Detection Threshold ($K$) Ablation}
427	\label{app:k_ablation}
428	
429	The consecutive-crossings threshold $K$ controls the trade-off between detection coverage and false positive rate. We evaluate $K \in \{1, 3, 5, 7, 10\}$ at $W{=}1$ on all four models using HS probes at corrected layers (\cref{tab:k_ablation}).
430	
431	\begin{table}[h]
432	\centering
433	\small
434	\caption{Detection threshold ablation ($W{=}1$, HS probes at corrected layers). Coverage: fraction of jailbreak traces with $\geq K$ consecutive crossings. Safe FPR: fraction of safe traces with $\geq K$ consecutive false alarms.}
435	\label{tab:k_ablation}
436	\setlength{\tabcolsep}{3pt}
437	\begin{tabular}{lccccccccc}
438	\toprule
439	& \multicolumn{4}{c}{\textbf{Coverage}} & & \multicolumn{4}{c}{\textbf{Safe FPR}} \\
440	\cmidrule{2-5} \cmidrule{7-10}
441	$K$ & R1-8B & OT-7B & QwQ & R1-32B & & R1-8B & OT-7B & QwQ & R1-32B \\
442	\midrule
443	1  & 1.00 & 1.00 & 1.00 & 1.00 & & 1.00 & 0.92 & 1.00 & 0.99 \\
444	3  & 0.74 & 0.79 & 0.95 & 0.90 & & 0.81 & 0.41 & 0.78 & 0.78 \\
445	5  & 0.47 & 0.51 & 0.79 & 0.65 & & 0.63 & 0.19 & 0.65 & 0.47 \\
446	7  & 0.35 & 0.30 & 0.58 & 0.45 & & 0.39 & 0.16 & 0.35 & 0.31 \\
447	10 & 0.14 & 0.21 & 0.32 & 0.35 & & 0.22 & 0.08 & 0.25 & 0.17 \\
448	\bottomrule
449	\end{tabular}
450	\end{table}
451	
452	$K{=}1$ yields perfect coverage but near-perfect safe FPR (0.92--1.00), offering no discrimination. $K{=}5$ is empirically selected as a middle-ground tradeoff: average coverage 0.60 with average safe FPR 0.48 across models. OT-7B benefits most from increasing $K$, reaching 0.19 safe FPR at $K{=}5$ (vs.\ 0.92 at $K{=}1$) while retaining 51\% coverage. Higher $K$ values ($\geq$7) reduce safe FPR further but at steep coverage cost. $K{=}5$ vs.\ $K{=}7$ is the key decision: $K{=}7$ reduces mean safe FPR from 0.48 to 0.30 but drops mean coverage from 0.60 to 0.42.
453	
454	$K$ was set as a design pre-selection before evaluation, not tuned on the validation set; all main-text results use $K{=}5$ without per-model optimization. The $K \times W$ interaction is not fully explored: this ablation uses $W{=}1$ to isolate $K$'s effect, and the joint $K \times W$ surface remains a limitation. At optimal $W$, coverage at $K{=}5$ improves (e.g., R1-8B: 0.47 at $W{=}1$ vs.\ 0.60 at $W{=}15$).
455	
456	
457	\section{Decision Threshold Sensitivity}
458	\label{app:threshold_sensitivity}
459	
460	We evaluate whether the HS advantage depends on the logistic regression decision threshold by sweeping $\tau \in \{0.3, 0.4, 0.5, 0.6, 0.7\}$ for both 32B models at their corrected layers. QwQ-32B (L60, $W{=}3$) HS balanced accuracy varies by only 0.53pp across all thresholds, with $\Delta$(HS$-$Text) stable at +8.5 to +9.3pp. \cref{tab:threshold_r132b} reports R1-32B results.
461	
462	\begin{table}[h]
463	\centering
464	\small
465	\caption{R1-32B threshold sensitivity (L63, $W{=}1$). HS BA varies by 1.1pp (0.741--0.752); the HS advantage is consistent across all thresholds.}
466	\label{tab:threshold_r132b}
467	\begin{tabular}{ccccccc}
468	\toprule
469	$\tau$ & HS BA & $\Delta$BA & HS Prec & $\Delta$Prec & HS FPR & $\Delta$FPR \\
470	\midrule
471	0.3 & 0.752 & +0.126 & 0.583 & +0.126 & 0.295 & $-$0.106 \\
472	0.4 & 0.746 & +0.116 & 0.586 & +0.120 & 0.281 & $-$0.092 \\
473	\textbf{0.5} & \textbf{0.742} & \textbf{+0.109} & \textbf{0.588} & \textbf{+0.113} & \textbf{0.273} & $\mathbf{-}$\textbf{0.078} \\
474	0.6 & 0.741 & +0.112 & 0.599 & +0.119 & 0.254 & $-$0.072 \\
475	0.7 & 0.743 & +0.126 & 0.617 & +0.143 & 0.228 & $-$0.084 \\
476	\bottomrule
477	\end{tabular}
478	\end{table}
479	
480	R1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\Delta$BA $= +0.109$ to $+0.126$, $\Delta$Prec $= +0.113$ to $+0.143$, $\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\tau{=}0.5$.
481	
482	
483	\section{M002 Bug Disclosure}
484	\label{app:bug}
485	
486	We disclose a bug discovered during development that affected intermediate results for QwQ-32B.
487	
488	\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).
489	
490	\paragraph{Discovery and correction.} The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QwQ-32B and R1-32B modality comparisons at the originally selected layers (L2 and L10, chosen by the biased composite metric) showed no significant HS advantage: QwQ-32B accuracy $p{=}0.828$, precision $p{=}0.346$; R1-32B precision $p{=}0.050$ but no tests surviving Holm-Bonferroni. The subsequent discovery that these layer selections were themselves artifacts of metric bias (\cref{sec:layer-results}) led to the corrected-layer analysis reported in the main text, where all four models show significant HS advantage at corrected deep layers (\cref{tab:hs_vs_text}).
491	
492	\paragraph{Impact on reported results.} All numbers reported in this paper use the corrected text embedding pipeline. The bug affected only QwQ-32B text probe features. The correction, combined with the separate layer selection correction (\cref{sec:layer-results}), means that early-stage intermediate results (non-significant 32B modality comparisons) reflected two compounding errors: incorrect text features and biased layer selection. Both are fully resolved in the final analysis.
493	
494	\paragraph{Commitment to transparency.} We report this bug to maintain scientific integrity. Code and data will be released upon publication.
495	
496	\section{Adaptive Two-Stage Detection}
497	\label{app:two_stage}
498	
499	We explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window ($W_{\text{screen}}$) to flag candidate unsafe segments, followed by a longer confirmation window ($W_{\text{confirm}}$) applied only to flagged segments. A trace is classified as unsafe if at least $k$ steps exceed the threshold during the confirmation stage.
500	
501	We merge the validation and test partitions ($n{=}55$ total: 39 jailbreak, 16 benign) for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of $W_{\text{screen}} \in \{1, 3, 5\}$, $W_{\text{confirm}} \in \{10, 15, 20, 25\}$, and $k \in \{1, 3, 5\}$ on these R1-8B traces. \cref{fig:pareto_two_stage} shows the precision-coverage Pareto front for both methods. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) achieves 72.2\% precision at 76.9\% coverage, compared to 70.9\% precision at 76.9\% coverage for single-stage $W{=}15$. This +1.3pp precision gain at matched coverage represents a Pareto improvement, but the magnitude is marginal. At higher confirmation thresholds ($k{=}3$, $k{=}5$), two-stage detection trades coverage for small precision gains (up to 73.5\% precision at 38.5\% coverage with $k{=}5$), but these operating points are impractical due to excessive missed detections.
502	
503	\begin{figure}[h]
504	\centering
505	\includegraphics[width=0.85\columnwidth]{figures/pareto_two_stage.pdf}
506	\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}
507	\label{fig:pareto_two_stage}
508	\end{figure}
509	
510	The marginal improvement suggests that fixed-window smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach adds configuration complexity (three hyperparameters vs. one) without proportional performance gain.
511	
512	
513	\section{Temporal Ablation Details}
514	\label{app:temporal_details}
515	
516	Full per-model temporal ablations are reported in \cref{tab:window_full} (\cref{app:window_ablation}). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) with FPR halving (9.65\% to 4.83\%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at $W{=}3$ while precision and FPR continue improving at larger windows; (3) R1-32B peaks at $W{=}10$ then degrades, likely reflecting overfitting on the small dataset ($n{=}100$); (4) QwQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (\cref{app:text_window}) show monotonic improvement across all window sizes for both models tested, with larger marginal gains than HS probes (+12.0pp accuracy vs.\ +3.2pp for R1-8B). The asymmetry supports the interpretation that text features benefit proportionally more from temporal context because they encode less information per step.
517	
518	\section{Negative Results Details}
519	\label{app:negative_details}
520	
521	\paragraph{BOCPD/CUSUM.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). Only R1-8B produces non-zero detection (best: $\lambda{=}10$, 93\% rate, +3.45 steps lead). CUSUM configurations universally underperform simple thresholding on lead time. The probe score sequences for 3/4 models show smooth transitions that never trigger the hazard function (\cref{app:bocpd_config}).
522	
523	\paragraph{Mahalanobis distance.} Following TrajGuard~\cite{trajguard}, Mahalanobis distance from the pre-CP centroid produces $\Delta d \approx 0$ between pre-CP and post-CP steps. The discriminative signal resides in minor PCA components (explaining $<$5\% of total variance) rather than the principal directions that dominate the distance computation.
524	
525	\paragraph{RepE.} Mean-difference directions~\cite{zou2023representation} show inconsistent performance: QwQ-32B achieves 0.756 balanced accuracy (approaching supervised 0.778) but with substantially worse precision (0.512 vs.\ LR 0.700) and FPR (0.309 vs.\ 0.120). R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment structure in some models but not others, making it unreliable as a general-purpose method.
526	
527	\paragraph{MLP probes.} Two-layer MLPs ($d \rightarrow 128 \rightarrow 1$, ReLU) underperform logistic regression on 3/4 models. The commitment boundary is linearly separable at correctly selected layers; additional capacity causes overfitting given the small training sets.
528	
529	\paragraph{CCS.} Contrast-Consistent Search~\cite{burns2023discovering} adapted with contrastive pairs from pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction, making it semi-supervised.
530	
531	\paragraph{Cross-model transfer.} 17 configurations (5 directional pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers) all fail. Best PCA: R1-8B $\rightarrow$ QwQ-32B at 59.5\% (PCA-2048). Best direct: QwQ-32B $\rightarrow$ R1-32B at 67.3\% but 1\% crossing rate. Implementation details in \cref{app:transfer_details}.
532	
533	\section{Cross-Model Transfer Implementation Details}
534	\label{app:transfer_details}
535	
536	We test whether safety probes transfer across models by projecting hidden states into a shared dimensionality space and applying cross-model classification.
537	
538	\paragraph{Method.} For each source-target model pair, we apply PCA independently to each model's hidden states, reducing to a shared dimensionality $d \in \{512, 1024, 2048\}$. PCA is fitted on the full dataset (including test traces) for each model separately, a setting favorable to transfer since it maximizes the quality of the projection. A logistic regression classifier (C=1.0, class\_weight=`balanced', max\_iter=2000, random\_state=42) trained on the source model's PCA-projected training data is then applied directly to the target model's PCA-projected test data. No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied; PCA serves as a standard linear dimensionality reduction baseline.
539	
540	\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.
541	
542	\paragraph{Results.} All 17 transfer configurations (5 directional pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers for same-dimension pairs) fail to produce practically useful transfer. The best PCA result is R1-8B $\rightarrow$ QwQ-32B at 59.5\% balanced accuracy (PCA-2048). The best direct transfer (QwQ-32B $\rightarrow$ R1-32B) reaches 67.3\% balanced accuracy, which exceeds the within-model baseline of 65.2\%. However, this transfer direction achieves only 1\% crossing rate, meaning the transferred probe almost never triggers detection in practice, rendering it useless for deployment despite above-baseline accuracy. The complete failure under maximally favorable conditions (PCA fitted on full data, no train/test separation for projection) strengthens the conclusion that safety commitment is encoded in model-specific geometric configurations. PCA is a standard linear alignment baseline; its failure indicates that the problem lies in the representations themselves rather than in the choice of alignment method.
543	
544	
545	\section{Encoder Robustness Analysis}
546	\label{app:encoder_robustness}
547	
548	To test whether the HS advantage over text probes depends on the specific text encoder, we replace all-MiniLM-L6-v2 (384d) with BGE-large-en-v1.5 (1024d), a 2.7$\times$ higher-dimensional encoder with stronger semantic representations. \cref{tab:encoder_robustness} reports precision comparisons at each model's corrected layer; \cref{fig:forest_precision} provides a visual summary.
549	
550	\begin{table}[h]
551	\centering
552	\small
553	\caption{HS vs.\ BGE-large (1024d) text probe precision. $\Delta$: HS minus BGE-large. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\alpha{=}0.05$).}
554	\label{tab:encoder_robustness}
555	\begin{tabular}{lcccccc}
556	\toprule
557	\textbf{Model} & \textbf{HS Prec} & \textbf{BGE Prec} & $\Delta$ & \textbf{95\% CI} & $p$ & \textbf{HB} \\
558	\midrule
559	R1-8B & 0.497 & 0.436 & +0.058 & [$-$0.07, +0.20] & 0.185 & No \\
560	OT-7B & 0.446 & 0.263 & +0.181 & [+0.08, +0.29] & ${<}0.001$ & Yes \\
561	R1-32B & 0.588 & 0.475 & +0.117 & [$-$0.00, +0.24] & 0.042 & No \\
562	QwQ-32B & 0.545 & 0.454 & +0.094 & [$-$0.07, +0.28] & 0.132 & No \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	The HS precision advantage is directionally consistent across all four models (positive $\Delta$ in every case). OT-7B shows a strong, significant advantage (+18.1pp, $p{<}0.001$, survives Holm-Bonferroni). The remaining three models do not survive Holm-Bonferroni correction; R1-32B's CI includes zero with 10{,}000 resamples, so even the individual precision test is non-significant. This is consistent with the prediction in \cref{sec:limitations} that stronger text encoders would reduce the observed gap. The pattern confirms that the HS modality advantage is genuine but partially attributable to the weakness of the 384d MiniLM baseline.
568	
569	\paragraph{Balanced accuracy and FPR.} \cref{tab:bge_ba_fpr} reports BGE-large comparisons on balanced accuracy and FPR. HS balanced accuracy advantage is directionally positive on all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni. FPR advantage is significant only for OT-7B. R1-8B shows an adverse FPR direction: HS FPR is 1.2pp higher (worse) than BGE ($p{=}0.564$), the only model where HS does not improve over the stronger encoder on this metric.
570	
571	\begin{table}[h]
572	\centering
573	\small
574	\caption{HS vs.\ BGE-large (1024d): balanced accuracy and FPR differences. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: Holm-Bonferroni correction (4 tests per metric, $\alpha{=}0.05$).}
575	\label{tab:bge_ba_fpr}
576	\begin{tabular}{lcccccc}
577	\toprule
578	\textbf{Model} & $\Delta$\textbf{BA} & $p$ (BA) & \textbf{HB} & $\Delta$\textbf{FPR} & $p$ (FPR) & \textbf{HB} \\
579	\midrule
580	R1-8B & +8.4 & 0.029 & No & $-$1.2$^\dagger$ & 0.564 & No \\
581	OT-7B & +10.8 & 0.002 & Yes & +10.5 & ${<}0.001$ & Yes \\
582	QwQ-32B & +9.3 & 0.067 & No & +2.7 & 0.368 & No \\
583	R1-32B & +10.9 & 0.008 & Yes & +7.8 & 0.165 & No \\
584	\bottomrule
585	\end{tabular}
586	\begin{flushleft}
587	\scriptsize $^\dagger$Adverse direction: HS FPR higher (worse) than BGE.
588	\end{flushleft}
589	\end{table}
590	
591	
592	\section{Position-Residualized Probing}
593	\label{app:position_residual}
594	
595	To quantify non-positional safety signal, we regress out the normalized position $t/T$ from each hidden-state (or text-embedding) vector before training the logistic regression probe. \cref{tab:position_residual} summarizes results across all models at their optimal $W$.
596	
597	\begin{table}[h]
598	\centering
599	\small
600	\begin{tabular}{lcrrrr}
601	\toprule
602	\textbf{Model} & $W$ & \textbf{HS BA} & \textbf{Resid.\ HS BA} & \textbf{Drop} & \textbf{Resid.\ Text BA} \\
603	\midrule
604	R1-8B & 15 & 0.834 & 0.669 & 16.5pp & 0.605 \\
605	R1-8B & 3 & 0.813 & 0.571 & 24.3pp & 0.534 \\
606	OT-7B & 3 & 0.732 & 0.609 & 12.3pp & 0.540 \\
607	QwQ-32B & 3 & 0.796 & 0.619 & 17.7pp & --- \\
608	\bottomrule
609	\end{tabular}
610	\caption{Position-residualized probe balanced accuracy. All residualized HS probes significantly above chance ($p{<}0.001$). HS residualized probes retain more non-positional signal than text residualized probes (+3.7 to +6.9pp).}
611	\label{tab:position_residual}
612	\end{table}
613	
614	Position is a significant component across all models (12--18pp BA reduction at optimal $W$), but all models retain substantial non-positional signal (residualized BA 0.61--0.67, all $p{<}0.001$). Larger temporal windows reduce position dependence: R1-8B drops 24.3pp at $W{=}3$ but only 16.5pp at $W{=}15$, indicating that broader context captures more non-positional structure.
615	
616	For QwQ-32B specifically, three complementary significance tests confirm the residualized probe performs above chance: Wilcoxon signed-rank $p{=}0.0024$, paired $t$-test $p{=}0.0008$, permutation test $p{<}0.001$ (bootstrap 95\% CI for per-trace BA: $[0.575, 0.744]$). The position baseline achieves higher balanced accuracy (0.832 vs.\ HS 0.796), and HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are not statistically significant at $n{=}19$.
617	
618	
619	\section{Multi-Seed Stability}
620	\label{app:multi_seed}
621	
622	\cref{tab:multi_seed} reports LR probe performance across 5 random seeds at each model's corrected layer and optimal $W$.
623	
624	\begin{table}[h]
625	\centering
626	\small
627	\caption{LR probe stability across 5 random seeds (corrected layers, optimal $W$). 7--8B models are stable; R1-32B shows high variance due to small sample ($n{=}20$).}
628	\label{tab:multi_seed}
629	\begin{tabular}{lccc}
630	\toprule
631	\textbf{Model} & \textbf{Precision} & \textbf{Bal.\ Acc} & \textbf{FPR} \\
632	\midrule
633	R1-8B & $0.590 \pm 0.072$ & $0.756 \pm 0.028$ & $0.154 \pm 0.026$ \\
634	OT-7B & $0.421 \pm 0.034$ & $0.633 \pm 0.023$ & $0.157 \pm 0.021$ \\
635	QwQ-32B & $0.651 \pm 0.099$ & $0.731 \pm 0.028$ & $0.133 \pm 0.032$ \\
636	R1-32B & $0.594 \pm 0.128$ & $0.692 \pm 0.056$ & $0.207 \pm 0.145$ \\
637	\bottomrule
638	\end{tabular}
639	\end{table}
640	
641	R1-32B's high FPR variance (std $= 0.145$) reflects a single outlier seed (FPR $= 0.48$), amplified by the small test set ($n{=}20$). At 7--8B scale, all metrics are stable (precision std ${<}8$pp, FPR std ${<}3$pp), supporting robust conclusions.
642	
643	\paragraph{R1-8B FPR per-seed breakdown.} \cref{tab:r18b_fpr_seeds} reports per-seed HS vs.\ text FPR comparisons for R1-8B. The HS advantage is directionally consistent (5/5 seeds), with 2/5 reaching $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds ($\alpha{=}0.01$), 1/5 remains significant. Text FPR is highly stable (std $= 0.007$) while HS FPR is split-sensitive (std $= 0.040$), which explains why the canonical-split FPR advantage ($-7.4$pp) does not generalize robustly across seeds.
644	
645	\begin{table}[h]
646	\centering
647	\small
648	\caption{R1-8B FPR per-seed comparison (L14, $W{=}15$). Direction is consistent (5/5 HS $\leq$ Text); 2/5 reach $p{<}0.05$ uncorrected, 1/5 after Bonferroni correction (5 seeds, $\alpha{=}0.01$).}
649	\label{tab:r18b_fpr_seeds}
650	\begin{tabular}{ccccc}
651	\toprule
652	\textbf{Seed} & \textbf{HS FPR} & \textbf{Text FPR} & $\Delta$\textbf{FPR} & $p$ \\
653	\midrule
654	0 & 0.161 & 0.165 & $-$0.004 & 0.440 \\
655	1 & 0.061 & 0.166 & $-$0.105 & ${<}0.001$ \\
656	2 & 0.123 & 0.176 & $-$0.053 & 0.093 \\
657	3 & 0.148 & 0.167 & $-$0.018 & 0.293 \\
658	4 & 0.100 & 0.176 & $-$0.076 & 0.021 \\
659	\midrule
660	mean$\pm$std & $0.119 \pm 0.040$ & $0.170 \pm 0.007$ & $-$0.051 & -- \\
661	\bottomrule
662	\end{tabular}
663	\end{table}
664	
665	\paragraph{R1-32B per-seed breakdown.} \cref{tab:r132b_seeds} reports the full per-seed breakdown for R1-32B. Seed 0 is an outlier (FPR $= 0.483$), driven by test-set trace allocation at $n{=}20$. Excluding seed 0, FPR std drops from 0.145 to 0.046.
666	
667	\begin{table}[h]
668	\centering
669	\small
670	\caption{R1-32B per-seed performance (L63, $W{=}1$). Seed 0 is an outlier driven by test-set trace allocation.}
671	\label{tab:r132b_seeds}
672	\begin{tabular}{cccc}
673	\toprule
674	\textbf{Seed} & \textbf{Precision} & \textbf{Bal.\ Acc} & \textbf{FPR} \\
675	\midrule
676	0 & 0.441 & 0.594 & 0.483 \\
677	1 & 0.750 & 0.748 & 0.109 \\
678	2 & 0.685 & 0.670 & 0.111 \\
679	3 & 0.652 & 0.733 & 0.111 \\
680	4 & 0.444 & 0.715 & 0.221 \\
681	\midrule
682	mean$\pm$std & $0.594 \pm 0.128$ & $0.692 \pm 0.056$ & $0.207 \pm 0.145$ \\
683	\bottomrule
684	\end{tabular}
685	\end{table}
686	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bebb4622-93c4-4aa7-b757-73cebcd6cced",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "8b444efc-7739-413d-b17b-9396c3757c35",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
      "content": "\\appendix\n\n\\section{Responsible NLP Research Checklist}\n\\label{app:checklist}\n\nWe address the ARR Responsible NLP Research requirements below.\n\n\\begin{itemize}\n    \\item \\textbf{Limitations discussed:} Yes (\\cref{sec:limitations}).\n    \\item \\textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this risk, as evasion requires white-box access to the probe, which a deployed monitoring system would not expose.\n    \\item \\textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.\n    \\item \\textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.\n    \\item \\textbf{Human subjects:} No human subjects research was conducted.\n    \\item \\textbf{Reproducibility:} All hyperparameters are reported in \\cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.\n\\end{itemize}\n\n\n\\section{Layer Sweep Results}\n\\label{app:layer_sweep}\n\nFor each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\\times$ crossing rate (the biased composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The biased composite systematically selects shallow layers for 32B models because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. Three threshold-dependent metrics (precision, inverse FPR, additive composite) converge on deep layers for all models; pure balanced accuracy selects middle layers for 32B models (L30 for QwQ-32B, L47 for R1-32B).\n\n\\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\\% depth). OT-7B: biased metric selects L0 (0\\%), unbiased consensus selects L16 (57\\%). QwQ-32B: biased metric selects L2 (3\\%), unbiased consensus selects L60 (94\\%). R1-32B: biased metric selects L10 (16\\%), unbiased consensus selects L63 (98\\%). The bias is most extreme for 64-layer models, where the composite metric selects layers in the bottom 16\\% of the network while threshold-dependent metrics select layers above 94\\%. Pure balanced accuracy selects middle layers (L30 at 47\\% for QwQ-32B, L47 at 73\\% for R1-32B), consistent with the AUROC pattern.\n\n\\paragraph{Impact on modality comparison.} At the biased layers, HS vs.\\ text precision $p$-values are 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant. At the corrected deep layers, all $p$-values fall below 0.005. The initially reported ``scale-dependent'' pattern (HS advantage at 7--8B but not 32B) was entirely an artifact of layer selection methodology, not a genuine property of model scale (\\cref{sec:layer-results}).\n\n\\paragraph{Layer selection stability (LOO-CV).} Leave-one-out cross-validation on the validation set confirms that layer selection is robust to data composition regardless of metric. Under pure balanced accuracy, the dominant layer is selected in 68\\% (QwQ-32B: L30, 13/19 folds) and 65\\% (R1-32B: L47, 13/20 folds) of folds. Alternative selections cluster in neighboring layers (L29, L55--56 for QwQ; L32, L38, L43 for R1-32B). The consensus corrected layers (L60, L63) are similarly dominant under threshold-dependent selection.\n\n\\paragraph{Joint (layer, $W$) sensitivity.} To verify that the corrected layer is not an artifact of a single window size, we evaluate QwQ-32B across 64 layers $\\times$ 3 windows ($W \\in \\{1, 3, 5\\}$), yielding 192 configurations (\\cref{tab:joint_layer_w}). L60 is near-optimal: within 2.1pp of the global best at $W{=}3$ and the top-ranked layer at $W{=}5$. The optimal layer shifts from middle-deep (L46--47 at $W{=}1$) to deep (L60 at $W{=}5$), confirming a layer-window interaction. L30, selected by per-fold LOO-CV at $W{=}1$ under balanced accuracy, is suboptimal across all windows (max BA $= 0.769$ vs.\\ global best 0.817). Joint (layer, $W$) stability was evaluated via grid search on $W \\in \\{1, 3, 5\\}$ for QwQ-32B only; full leave-one-fold-out validation of the (layer, $W$) pair and extension to R1-32B remain for future work.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{QwQ-32B joint (layer, $W$) grid search. L60 is near-optimal at recommended windows ($W{=}3$--$5$). L30 (LOO-CV selection at $W{=}1$) is suboptimal across all windows.}\n\\label{tab:joint_layer_w}\n\\begin{tabular}{clccc}\n\\toprule\n$W$ & \\textbf{Best layer} & \\textbf{Best BA} & \\textbf{L60 BA} & \\textbf{L60 rank} \\\\\n\\midrule\n1 & L47 & 0.798 & 0.783 & $\\sim$15th \\\\\n3 & L46 & 0.817 & 0.796 & $\\sim$6th \\\\\n5 & L60 & 0.808 & 0.808 & 1st \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Representation Compression Analysis}\n\\label{app:cosine_volatility}\n\nWe measure step-to-step cosine distance at biased (shallow) vs.\\ corrected (deep) layers across all four models to characterize the compression mechanism underlying the crossing rate bias (\\cref{tab:cosine_volatility}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4--2.7$\\times$ smaller inter-step distances).}\n\\label{tab:cosine_volatility}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & \\textbf{Layer (type)} & \\textbf{Mean} & \\textbf{Std} \\\\\n\\midrule\nR1-8B & L2 (biased) & 0.186 & 0.097 \\\\\n & L14 (corrected) & 0.411 & 0.143 \\\\[2pt]\nOT-7B & L2 (biased) & 0.077 & 0.080 \\\\\n & L16 (corrected) & 0.206 & 0.091 \\\\[2pt]\nQwQ-32B & L2 (biased) & 0.037 & 0.064 \\\\\n & L60 (corrected) & 0.102 & 0.075 \\\\[2pt]\nR1-32B & L10 (biased) & 0.067 & 0.050 \\\\\n & L63 (corrected) & 0.092 & 0.076 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nShallow layers produce highly compressed representations: consecutive steps cluster within small cosine distances (0.04--0.19), while deep-layer representations spread more widely (0.09--0.41). Inter-step distances at shallow layers are 1.4--2.7$\\times$ smaller than at deep layers across all four models. A linear probe operating in this compressed space sits near the noise floor, where minor numerical fluctuations produce spurious threshold crossings that inflate crossing rate independently of discriminative power. Deep layers produce well-separated representations where crossings correspond to genuine semantic transitions.\n\n\n\\section{Holm-Bonferroni Step-Down Correction}\n\\label{app:holm_bonferroni}\n\n\\cref{tab:holm_bonferroni} reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the conservative 12-test correction and the 4-test model-level correction: both yield the same outcome (all tests pass at $\\alpha{=}0.05$). Under 4-test HB, the tightest threshold falls on R1-8B FPR ($p{=}0.044$, rank-4 threshold $\\alpha/1{=}0.050$), which still passes. Tests are ranked by $p$-value; each test $i$ (rank $i$ of $m$) must satisfy $p_i < \\alpha / (m - i + 1)$ under the step-down procedure.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}\n\\label{tab:holm_bonferroni}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{clllcc}\n\\toprule\n\\textbf{Rank} & \\textbf{Model} & \\textbf{Metric} & \\textbf{$p$-val} & \\textbf{Thresh.} & \\textbf{Pass} \\\\\n\\midrule\n1  & R1-8B  & Precision & $<$0.001 & 0.0042 & \\checkmark \\\\\n2  & OT-7B  & Bal.\\ Acc. & $<$0.001 & 0.0045 & \\checkmark \\\\\n3  & OT-7B  & Precision & $<$0.001 & 0.0050 & \\checkmark \\\\\n4  & OT-7B  & FPR & $<$0.001 & 0.0056 & \\checkmark \\\\\n5  & QwQ-32B & Bal.\\ Acc. & $<$0.001 & 0.0063 & \\checkmark \\\\\n6  & QwQ-32B & Precision & $<$0.001 & 0.0071 & \\checkmark \\\\\n7  & R1-32B & Bal.\\ Acc. & $<$0.001 & 0.0083 & \\checkmark \\\\\n8  & R1-32B & Precision & $<$0.001 & 0.0100 & \\checkmark \\\\\n9  & QwQ-32B & FPR & 0.004 & 0.0125 & \\checkmark \\\\\n10 & R1-8B  & Bal.\\ Acc. & 0.005 & 0.0167 & \\checkmark \\\\\n11 & R1-32B & FPR & 0.007 & 0.0250 & \\checkmark \\\\\n12 & R1-8B  & FPR & 0.044 & 0.0500 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B showing the largest precision gap (+32.5pp). This reflects R1-8B's already-low text FPR (11.8\\%), which leaves less room for HS improvement on this metric.\n\n\\paragraph{Exact sign-flip permutation test validation.} As an independent check on bootstrap significance for the small-sample 32B models, we run exact sign-flip permutation tests on all six 32B comparisons, enumerating all $2^n$ sign permutations ($2^{19}{=}524{,}288$ for QwQ-32B, $2^{20}{=}1{,}048{,}576$ for R1-32B). All six tests reject the null at $\\alpha{=}0.05$: QwQ-32B (bal\\_acc $p{<}0.001$, precision $p{=}0.003$, FPR $p{<}0.001$); R1-32B (bal\\_acc $p{=}0.008$, precision $p{<}0.001$, FPR $p{=}0.004$). The permutation $p$-values are consistent with the bootstrap values in \\cref{tab:holm_bonferroni}, confirming that the bootstrap-based conclusions are not artifacts of distributional assumptions at small $n$.\n\n\n\\section{Window Size Ablation Details}\n\\label{app:window_ablation}\n\n\\cref{tab:window_full} reports the complete window size ablation across all four models and seven window sizes. The main text (\\cref{sec:temporal}) presents R1-8B results; here we provide the full data. \\cref{fig:window_ablation} visualizes the monotonic improvement on R1-8B: precision rises from 69.3\\% ($W{=}1$) to 82.2\\% ($W{=}25$) while FPR drops from 9.65\\% to 4.8\\%.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_temporal_improvement.pdf}\n\\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\\% ($W{=}1$) to 82.2\\% ($W{=}25$); FPR: 9.65\\% to 4.8\\%.}\n\\label{fig:window_ablation}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models.}\n\\label{tab:window_full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\nModel & $W$ & Bal.\\ Acc. & Precision & FPR$_{\\text{step}}$ & Coverage & Lead \\\\\n\\midrule\n\\multirow{7}{*}{R1-8B}\n & 1  & 77.8 & 69.3 & 9.65 & 72.1 & 13.8 \\\\\n & 3  & 79.0 & 72.3 & 8.50 & 69.8 & 12.1 \\\\\n & 5  & 78.1 & 72.6 & 8.09 & 65.1 & 8.3 \\\\\n & 10 & 79.3 & 74.3 & 7.61 & 55.8 & 10.0 \\\\\n & 15 & 80.2 & 77.7 & 6.39 & 51.2 & 7.2 \\\\\n & 20 & 80.7 & 78.6 & 6.12 & 53.5 & 7.4 \\\\\n & 25 & 81.0 & 82.2 & 4.83 & 48.8 & 8.1 \\\\\n\\midrule\n\\multirow{7}{*}{OT-7B}\n & 1  & 68.2 & 42.8 & 12.0 & 53.2 & 16.1 \\\\\n & 3  & \\textbf{68.8} & 46.6 & 10.0 & 53.2 & 21.6 \\\\\n & 5  & 68.1 & 46.4 & 9.9 & 53.2 & 21.7 \\\\\n & 10 & 66.5 & 46.9 & 8.6 & 48.9 & 25.0 \\\\\n & 15 & 66.4 & 48.8 & 7.7 & 44.7 & 39.6 \\\\\n & 20 & 66.0 & \\textbf{49.4} & \\textbf{7.5} & 48.9 & 17.9 \\\\\n & 25 & 65.9 & 48.9 & 8.0 & 51.1 & 28.3 \\\\\n\\midrule\n\\multirow{7}{*}{R1-32B}\n & 1  & 71.8 & 54.9 & 32.03 & 80.0 & 12.9 \\\\\n & 3  & 72.5 & 56.0 & 30.64 & 80.0 & 11.4 \\\\\n & 5  & 73.1 & 57.5 & 28.41 & 75.0 & 11.1 \\\\\n & 10 & 73.7 & 60.9 & 23.40 & 70.0 & 10.8 \\\\\n & 15 & 72.1 & 59.1 & 24.51 & 70.0 & 10.9 \\\\\n & 20 & 69.6 & 56.3 & 26.18 & 65.0 & 9.6 \\\\\n & 25 & 70.3 & 56.6 & 26.46 & 70.0 & 10.7 \\\\\n\\midrule\n\\multirow{7}{*}{QwQ-32B}\n & 1  & 73.0 & 54.4 & 22.76 & 79.0 & 19.7 \\\\\n & 3  & 74.5 & 56.5 & 21.41 & 73.7 & 20.6 \\\\\n & 5  & 76.1 & 57.3 & 21.68 & 73.7 & 20.1 \\\\\n & 10 & 74.7 & 57.1 & 20.73 & 73.7 & 18.4 \\\\\n & 15 & 74.1 & 58.2 & 19.11 & 68.4 & 15.8 \\\\\n & 20 & 75.4 & 60.2 & 17.89 & 63.2 & 15.8 \\\\\n & 25 & 76.2 & 61.8 & 16.94 & 57.9 & 14.9 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\end{table}\n\nKey cross-model patterns emerge from the window ablation:\n\n\\paragraph{R1-8B} shows a general upward trend in balanced accuracy from 77.8\\% ($W{=}1$) to 81.0\\% ($W{=}25$), gaining +3.2pp overall with a slight dip at $W{=}5$ (78.1\\%). Precision improves sharply (+12.9pp) and step-level FPR halves (9.65\\% to 4.83\\%). Coverage trades off against quality, dropping from 72.1\\% to 48.8\\%.\n\n\\paragraph{OT-7B} exhibits a split temporal pattern at layer 16: balanced accuracy peaks at $W{=}3$ (68.8\\%) and declines at larger windows ($-$2.9pp by $W{=}25$), while precision and FPR continue improving. Precision rises from 42.8\\% ($W{=}1$) to 49.4\\% ($W{=}20$), and FPR drops from 12.0\\% to 7.5\\% over the same range. The split indicates that larger windows reduce false alarms and sharpen positive predictions even as overall classification accuracy degrades. Lead times are shorter than old layer-0 estimates (16.1--39.6 steps) due to the corrected layer selection (\\cref{app:ot7b_details}). OT-7B text probes improve monotonically across all metrics (\\cref{app:ot7b_details}), so the accuracy saturation is specific to HS probes on this model.\n\n\\paragraph{R1-32B} exhibits a non-monotonic pattern: balanced accuracy peaks at $W{=}10$ (73.7\\%) and then declines, falling below the $W{=}1$ baseline by $W{=}20$ (69.6\\%). The optimal window for R1-32B is $W{=}10$, which achieves the lowest FPR (23.40\\%) and highest precision (60.9\\%). The accuracy degradation at large windows likely reflects overfitting on the smaller dataset ($n{=}100$).\n\n\\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\\%), dips at $W{=}10$--$15$, then recovers to 76.2\\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\\% to 61.8\\% precision; 22.76\\% to 16.94\\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.\n\n\\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.\n\n\\subsection{Text Probe Window Ablation}\n\\label{app:text_window}\n\n\\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.\n\n\\begin{table}[h]\n\\centering\n\\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}\n\\label{tab:text_window}\n\\begin{tabular}{lcccc}\n\\toprule\n$W$ & Bal. Acc. & Precision & FPR & Coverage \\\\\n\\midrule\n 1  & 64.7 & 41.6 & 25.8 & 95.4 \\\\\n 3  & 66.9 & 44.8 & 23.1 & 90.7 \\\\\n 5  & 69.2 & 48.5 & 20.4 & 84.9 \\\\\n 10 & 72.1 & 54.3 & 16.7 & 74.4 \\\\\n 15 & 74.3 & 58.9 & 14.2 & 67.4 \\\\\n 20 & 75.8 & 62.1 & 12.5 & 62.8 \\\\\n 25 & 76.7 & 64.8 & 11.8 & 58.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nText probes show monotonic improvement across all window sizes without the plateau observed in HS probes (which saturate around $W{=}15$). The absolute FPR reduction ($-$14.0pp) is nearly three times the HS reduction ($-$4.8pp), and accuracy gains (+12.0pp vs.\\ +3.2pp) are four times larger. This asymmetry supports the interpretation that temporal context is the primary factor in commitment detection: text features, which encode less information per step, benefit proportionally more from observing the multi-step progression.\n\n\n\\section{OpenThinker-7B Detailed Results}\n\\label{app:ot7b_details}\n\nOpenThinker-7B (OT-7B) is trained with STILL~\\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.\n\n\\paragraph{Layer sweep.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{OT-7B layer sweep. Score = balanced accuracy $\\times$ crossing rate. Layer 16 (57\\% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.}\n\\label{tab:ot7b_layer_sweep}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Depth & Bal.\\ Acc. & Cross.\\ Rate & Score \\\\\n\\midrule\n0 (embed.) & 0 & 66.7 & 53.2 & 35.5 \\\\\n4 & 14 & 66.3 & 40.4 & 26.8 \\\\\n8 & 29 & 66.4 & 25.5 & 17.0 \\\\\n12 & 43 & 67.5 & 31.9 & 21.6 \\\\\n16 & 57 & 68.2 & 31.9 & 21.8 \\\\\n20 & 71 & 65.5 & 31.9 & 20.9 \\\\\n24 & 86 & 66.9 & 29.8 & 19.9 \\\\\n27 & 96 & 63.0 & 31.9 & 20.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAfter correction of a layer selection bug, layer 16 (57\\% depth) is selected. It achieves the highest balanced accuracy (68.2\\%) among transformer layers and is consistent with the mid-depth pattern of R1-8B (44\\%). Layer 0 (embedding) has a higher crossing rate (53.2\\% vs.\\ 31.9\\%) but lower accuracy.\n\n\\paragraph{Text probe window ablation.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}\n\\label{tab:ot7b_text_window}\n\\begin{tabular}{lcccc}\n\\toprule\n$W$ & Bal. Acc. & Precision & FPR & Coverage \\\\\n\\midrule\n 1  & 58.1 & 24.5 & 34.5 & 63.8 \\\\\n 3  & 57.9 & 25.4 & 27.1 & 74.5 \\\\\n 5  & 56.9 & 24.7 & 25.5 & 70.2 \\\\\n 10 & 58.3 & 27.0 & 22.2 & 70.2 \\\\\n 15 & 58.9 & 28.3 & 20.0 & 66.0 \\\\\n 20 & 60.9 & 31.6 & 17.6 & 66.0 \\\\\n 25 & 61.4 & 32.9 & 16.1 & 66.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.\n\n\\paragraph{Bootstrap comparison (matched $W{=}3$).} To ensure a fair modality comparison, bootstrap tests use matched $W{=}3$ for both HS and text probes. At $W{=}3$, HS probes achieve 75.3\\% trace-level balanced accuracy vs.\\ 65.6\\% for text (bootstrap $\\Delta{=}$+10.7pp, 95\\% CI [4.9, 16.3], $p{<}0.001$, survives Holm-Bonferroni). Precision: 55.8\\% vs.\\ 34.6\\% (bootstrap $\\Delta{=}$+21.9pp, 95\\% CI [14.0, 29.6], $p{<}0.001$, survives Holm-Bonferroni). Pre-CP FPR: 10.0\\% vs.\\ 27.1\\% (bootstrap $\\Delta{=}{-}17.1$pp, 95\\% CI [$-$22.2, $-$12.2], $p{<}0.001$, survives Holm-Bonferroni). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (+21.9pp); the small discrepancy reflects resampling variance. Using each modality's optimal $W$ (HS at $W{=}3$, text at $W{=}25$) would introduce a confound because text would benefit from 8$\\times$ more temporal context.\n\n\n\\section{GRU Training Details}\n\\label{app:gru_details}\n\n\\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\\% training portion, we hold out 10\\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.\n\n\\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.\n\n\\paragraph{Training procedure.} We train with Adam (learning rate $1 \\times 10^{-3}$, default $\\beta_1{=}0.9$, $\\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.\n\n\\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\\pm$ standard deviation.\n\n\\paragraph{Per-seed results for R1-8B (single-layer GRU).}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}\n\\label{tab:gru_seeds}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & Peak Acc. & Crossing Acc. & Lead (steps) \\\\\n\\midrule\n1 & 85.2 & 74.3 & +4.8 \\\\\n2 & 83.1 & 71.6 & +4.8 \\\\\n3 & 83.4 & 70.4 & +0.9 \\\\\n\\midrule\nMean $\\pm$ std & 83.9 $\\pm$ 1.1 & 72.1 $\\pm$ 2.0 & +3.5 $\\pm$ 2.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.\n\n\\paragraph{Multi-layer GRU and baseline comparison (60/20/20 protocol).}\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}\n\\label{tab:gru_multi_seeds}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Seed & Acc & Prec & FPR & Cross.\\% & Lead \\\\\n\\midrule\nGRU-single & 42  & 0.845 & 0.657 & 0.139 & 72.1\\% & 3.55 \\\\\nGRU-single & 123 & 0.760 & 0.454 & 0.191 & 65.1\\% & 7.39 \\\\\nGRU-single & 456 & 0.792 & 0.474 & 0.203 & 67.4\\% & 8.45 \\\\\n\\rowcolor{gray!10}\nGRU-single & \\textit{mean} & 0.799$\\pm$0.035 & 0.528$\\pm$0.091 & 0.178$\\pm$0.028 & 68.2$\\pm$2.9\\% & 6.46$\\pm$2.10 \\\\\n\\midrule\nGRU-multi  & 42  & 0.824 & 0.616 & 0.164 & 74.4\\% & 5.66 \\\\\nGRU-multi  & 123 & 0.759 & 0.454 & 0.195 & 65.1\\% & 6.43 \\\\\nGRU-multi  & 456 & 0.784 & 0.460 & 0.207 & 65.1\\% & 8.93 \\\\\n\\rowcolor{gray!10}\nGRU-multi  & \\textit{mean} & 0.789$\\pm$0.027 & 0.510$\\pm$0.075 & 0.189$\\pm$0.018 & 68.2$\\pm$4.4\\% & 7.01$\\pm$1.40 \\\\\n\\midrule\nLR-single  & 42  & 0.841 & 0.693 & 0.097 & 46.5\\% & $-$2.00 \\\\\nLR-single  & 123 & 0.753 & 0.436 & 0.181 & 53.5\\% & 5.26 \\\\\nLR-single  & 456 & 0.814 & 0.512 & 0.146 & 41.9\\% & 3.94 \\\\\n\\rowcolor{gray!10}\nLR-single  & \\textit{mean} & 0.803$\\pm$0.037 & 0.547$\\pm$0.108 & 0.141$\\pm$0.035 & 47.3$\\pm$4.8\\% & 2.40$\\pm$3.16 \\\\\n\\midrule\nLR-multi   & 42  & 0.827 & 0.679 & 0.092 & 39.5\\% & 1.06 \\\\\nLR-multi   & 123 & 0.756 & 0.442 & 0.180 & 46.5\\% & 7.30 \\\\\nLR-multi   & 456 & 0.817 & 0.521 & 0.130 & 34.9\\% & 4.00 \\\\\n\\rowcolor{gray!10}\nLR-multi   & \\textit{mean} & 0.800$\\pm$0.032 & 0.547$\\pm$0.099 & 0.134$\\pm$0.036 & 40.3$\\pm$4.8\\% & 4.12$\\pm$2.55 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\end{table}\n\nUnder this protocol, multi-layer GRU achieves the highest mean lead (7.01$\\pm$1.40 steps) but at higher FPR than logistic regression baselines (0.189 vs.\\ 0.134). The GRU advantage is concentrated in detection timing rather than classification accuracy, consistent with the main text finding that GRUs capture sequential dependencies that improve early detection. Lead time shows high variance across seeds (range 5.66--8.93 for GRU-multi), reinforcing that reported means should be interpreted cautiously.\n\n\\paragraph{OT-7B multi-layer GRU (layers 13--19, 3 seeds, 60/20/20 split).}\nOT-7B GRU achieves 74.6$\\pm$1.3\\% balanced accuracy, 64.5$\\pm$7.0\\% coverage, +33.6$\\pm$4.8 steps lead, and 27.4$\\pm$6.1\\% pre-CP FPR. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average ${\\sim}$80 reasoning steps (vs.\\ ${\\sim}$30 for R1-8B and 32B models), so absolute lead times are not directly comparable. The FPR-lead tradeoff mirrors R1-8B: GRU FPR (27.4\\%) is far above the LR probe at layer 16 (10.0\\%), confirming that GRUs gain lead time at the cost of more false alarms across both 7-8B models.\n\n\n\\section{Control Task Methodology}\n\\label{app:control}\n\nWe follow the selectivity framework of \\cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.\n\n\\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) across all steps while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:\n\\begin{equation}\n    \\text{Selectivity} = \\text{Acc}_{\\text{linguistic}} - \\text{Acc}_{\\text{control}}\n\\end{equation}\nwhere $\\text{Acc}_{\\text{linguistic}}$ is the probe accuracy on true labels and $\\text{Acc}_{\\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information.\n\n\\paragraph{Results.} We repeat the control experiment 5 times (10 for OT-7B) with different random permutations and report the mean control accuracy. Selectivity scores at corrected layers are: R1-32B 19.7pp (layer 63), OT-7B 18.3pp (layer 16), QwQ-32B 14.4pp (layer 60), R1-8B 12.5pp (layer 14). All values exceed the 5pp threshold recommended by \\cite{hewitt2019control}. R1-32B achieves the strongest selectivity (19.7pp) at the corrected layer, a 2.6$\\times$ increase from 7.5pp at the biased layer L10. OT-7B achieves the second-highest selectivity at a mid-depth transformer layer (57\\%), consistent with R1-8B's pattern at 44\\% depth. On QwQ-32B, the position baseline accuracy (0.705) slightly exceeds the HS probe (0.667) at L60, consistent with the main-text finding that QwQ's HS advantage is concentrated in precision and FPR rather than balanced accuracy.\n\n\\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 14.4pp at L60 (comparable to 15.3pp at L2), confirming that safety-specific signal persists at deep layers.\n\n\\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\\% FPR compared to 8.1\\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.\n\n\n\\section{Oracle Upper Bound Analysis}\n\\label{sec:oracle}\n\nWe compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. This provides a theoretical ceiling on early detection performance.\n\nOn R1-8B, the oracle achieves +31 steps mean lead time compared to +4.5 steps for the best learned probe (GRU), yielding an oracle gap of 85.5\\%. This gap indicates that hidden states at step $t$ encode the model's current safety state but carry limited predictive power about future trajectory evolution. The learned probe captures the contemporaneous safety signal effectively (balanced accuracy 81--84\\%) but cannot anticipate the commitment transition far in advance. Closing this gap will likely require causal intervention techniques (e.g., activation patching) rather than improvements to passive monitoring.\n\n\n\\section{BOCPD/CUSUM Configuration Sweep}\n\\label{app:bocpd_config}\n\nWe sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.\n\n\\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\\lambda$ controls the prior probability of a change-point at each step ($P(\\text{change}) = 1/\\lambda$).\n\n\\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}\n\\label{tab:cpd_sweep}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\nMethod & Configuration & Det.\\ Rate & Lead \\\\\n\\midrule\n\\multirow{5}{*}{BOCPD}\n & $\\lambda = 5$   & 97 & +2.1 \\\\\n & $\\lambda = 10$  & 93 & +3.5 \\\\\n & $\\lambda = 20$  & 87 & +4.2 \\\\\n & $\\lambda = 50$  & 72 & +5.8 \\\\\n & $\\lambda = 100$ & 67.4 & +1.03 \\\\\n\\midrule\n\\multirow{10}{*}{CUSUM}\n & $\\delta{=}0.3$, $h{=}3$ & 65.1 & +0.89 \\\\\n & $\\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\\\\n & $\\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\\\\n & $\\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\\\\n & $\\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\\\\n & $\\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\\\\n & $\\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\\\\n & $\\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\\\\n & $\\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\\\\n & $\\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\\\\n\\midrule\nSimple threshold & FCP baseline & 65.1 & +4.89 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe best BOCPD configuration ($\\lambda{=}10$) achieves 93.0\\% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1\\% detection with superior lead (+4.89 steps). All CUSUM configurations underperform the simple threshold on lead time.\n\nThese results reveal a coverage-timing tradeoff. BOCPD ($\\lambda{=}10$) achieves 28pp higher detection rate than simple thresholding (93.0\\% vs.\\ 65.1\\%), but with lower lead (+3.45 vs.\\ +4.89 steps). The transition toward unsafe reasoning is gradual rather than abrupt, so change-point methods cannot exploit discontinuities for early warning. When missed detections are costly, BOCPD's coverage advantage justifies its use despite the timing penalty. When early intervention is the priority, simple thresholding provides better lead time.\n\n\\paragraph{Other models.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\\% detection rate across all tested configurations ($\\lambda \\in \\{5, 10, 50, 100, 200\\}$). The probe score sequences for these models show smoother transitions that never trigger the hazard function, consistent with the gradual commitment pattern. R1-8B's higher detection rate likely reflects its sharper probe score transitions at commitment boundaries.\n\n\n\\section{Detection Threshold ($K$) Ablation}\n\\label{app:k_ablation}\n\nThe consecutive-crossings threshold $K$ controls the trade-off between detection coverage and false positive rate. We evaluate $K \\in \\{1, 3, 5, 7, 10\\}$ at $W{=}1$ on all four models using HS probes at corrected layers (\\cref{tab:k_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Detection threshold ablation ($W{=}1$, HS probes at corrected layers). Coverage: fraction of jailbreak traces with $\\geq K$ consecutive crossings. Safe FPR: fraction of safe traces with $\\geq K$ consecutive false alarms.}\n\\label{tab:k_ablation}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccccccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Coverage}} & & \\multicolumn{4}{c}{\\textbf{Safe FPR}} \\\\\n\\cmidrule{2-5} \\cmidrule{7-10}\n$K$ & R1-8B & OT-7B & QwQ & R1-32B & & R1-8B & OT-7B & QwQ & R1-32B \\\\\n\\midrule\n1  & 1.00 & 1.00 & 1.00 & 1.00 & & 1.00 & 0.92 & 1.00 & 0.99 \\\\\n3  & 0.74 & 0.79 & 0.95 & 0.90 & & 0.81 & 0.41 & 0.78 & 0.78 \\\\\n5  & 0.47 & 0.51 & 0.79 & 0.65 & & 0.63 & 0.19 & 0.65 & 0.47 \\\\\n7  & 0.35 & 0.30 & 0.58 & 0.45 & & 0.39 & 0.16 & 0.35 & 0.31 \\\\\n10 & 0.14 & 0.21 & 0.32 & 0.35 & & 0.22 & 0.08 & 0.25 & 0.17 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$K{=}1$ yields perfect coverage but near-perfect safe FPR (0.92--1.00), offering no discrimination. $K{=}5$ is empirically selected as a middle-ground tradeoff: average coverage 0.60 with average safe FPR 0.48 across models. OT-7B benefits most from increasing $K$, reaching 0.19 safe FPR at $K{=}5$ (vs.\\ 0.92 at $K{=}1$) while retaining 51\\% coverage. Higher $K$ values ($\\geq$7) reduce safe FPR further but at steep coverage cost. $K{=}5$ vs.\\ $K{=}7$ is the key decision: $K{=}7$ reduces mean safe FPR from 0.48 to 0.30 but drops mean coverage from 0.60 to 0.42.\n\n$K$ was set as a design pre-selection before evaluation, not tuned on the validation set; all main-text results use $K{=}5$ without per-model optimization. The $K \\times W$ interaction is not fully explored: this ablation uses $W{=}1$ to isolate $K$'s effect, and the joint $K \\times W$ surface remains a limitation. At optimal $W$, coverage at $K{=}5$ improves (e.g., R1-8B: 0.47 at $W{=}1$ vs.\\ 0.60 at $W{=}15$).\n\n\n\\section{Decision Threshold Sensitivity}\n\\label{app:threshold_sensitivity}\n\nWe evaluate whether the HS advantage depends on the logistic regression decision threshold by sweeping $\\tau \\in \\{0.3, 0.4, 0.5, 0.6, 0.7\\}$ for both 32B models at their corrected layers. QwQ-32B (L60, $W{=}3$) HS balanced accuracy varies by only 0.53pp across all thresholds, with $\\Delta$(HS$-$Text) stable at +8.5 to +9.3pp. \\cref{tab:threshold_r132b} reports R1-32B results.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-32B threshold sensitivity (L63, $W{=}1$). HS BA varies by 1.1pp (0.741--0.752); the HS advantage is consistent across all thresholds.}\n\\label{tab:threshold_r132b}\n\\begin{tabular}{ccccccc}\n\\toprule\n$\\tau$ & HS BA & $\\Delta$BA & HS Prec & $\\Delta$Prec & HS FPR & $\\Delta$FPR \\\\\n\\midrule\n0.3 & 0.752 & +0.126 & 0.583 & +0.126 & 0.295 & $-$0.106 \\\\\n0.4 & 0.746 & +0.116 & 0.586 & +0.120 & 0.281 & $-$0.092 \\\\\n\\textbf{0.5} & \\textbf{0.742} & \\textbf{+0.109} & \\textbf{0.588} & \\textbf{+0.113} & \\textbf{0.273} & $\\mathbf{-}$\\textbf{0.078} \\\\\n0.6 & 0.741 & +0.112 & 0.599 & +0.119 & 0.254 & $-$0.072 \\\\\n0.7 & 0.743 & +0.126 & 0.617 & +0.143 & 0.228 & $-$0.084 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nR1-32B HS balanced accuracy varies by only 1.1pp across the full threshold range. The modality advantage ($\\Delta$BA $= +0.109$ to $+0.126$, $\\Delta$Prec $= +0.113$ to $+0.143$, $\\Delta$FPR $= -0.072$ to $-0.106$) is consistent in both magnitude and direction at every threshold, confirming that the HS advantage is not an artifact of the default $\\tau{=}0.5$.\n\n\n\\section{M002 Bug Disclosure}\n\\label{app:bug}\n\nWe disclose a bug discovered during development that affected intermediate results for QwQ-32B.\n\n\\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).\n\n\\paragraph{Discovery and correction.} The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QwQ-32B and R1-32B modality comparisons at the originally selected layers (L2 and L10, chosen by the biased composite metric) showed no significant HS advantage: QwQ-32B accuracy $p{=}0.828$, precision $p{=}0.346$; R1-32B precision $p{=}0.050$ but no tests surviving Holm-Bonferroni. The subsequent discovery that these layer selections were themselves artifacts of metric bias (\\cref{sec:layer-results}) led to the corrected-layer analysis reported in the main text, where all four models show significant HS advantage at corrected deep layers (\\cref{tab:hs_vs_text}).\n\n\\paragraph{Impact on reported results.} All numbers reported in this paper use the corrected text embedding pipeline. The bug affected only QwQ-32B text probe features. The correction, combined with the separate layer selection correction (\\cref{sec:layer-results}), means that early-stage intermediate results (non-significant 32B modality comparisons) reflected two compounding errors: incorrect text features and biased layer selection. Both are fully resolved in the final analysis.\n\n\\paragraph{Commitment to transparency.} We report this bug to maintain scientific integrity. Code and data will be released upon publication.\n\n\\section{Adaptive Two-Stage Detection}\n\\label{app:two_stage}\n\nWe explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window ($W_{\\text{screen}}$) to flag candidate unsafe segments, followed by a longer confirmation window ($W_{\\text{confirm}}$) applied only to flagged segments. A trace is classified as unsafe if at least $k$ steps exceed the threshold during the confirmation stage.\n\nWe merge the validation and test partitions ($n{=}55$ total: 39 jailbreak, 16 benign) for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of $W_{\\text{screen}} \\in \\{1, 3, 5\\}$, $W_{\\text{confirm}} \\in \\{10, 15, 20, 25\\}$, and $k \\in \\{1, 3, 5\\}$ on these R1-8B traces. \\cref{fig:pareto_two_stage} shows the precision-coverage Pareto front for both methods. The best two-stage configuration ($W_{\\text{screen}}{=}3$, $W_{\\text{confirm}}{=}15$, $k{=}1$) achieves 72.2\\% precision at 76.9\\% coverage, compared to 70.9\\% precision at 76.9\\% coverage for single-stage $W{=}15$. This +1.3pp precision gain at matched coverage represents a Pareto improvement, but the magnitude is marginal. At higher confirmation thresholds ($k{=}3$, $k{=}5$), two-stage detection trades coverage for small precision gains (up to 73.5\\% precision at 38.5\\% coverage with $k{=}5$), but these operating points are impractical due to excessive missed detections.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/pareto_two_stage.pdf}\n\\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\\text{screen}}{=}3$, $W_{\\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}\n\\label{fig:pareto_two_stage}\n\\end{figure}\n\nThe marginal improvement suggests that fixed-window smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach adds configuration complexity (three hyperparameters vs. one) without proportional performance gain.\n\n\n\\section{Temporal Ablation Details}\n\\label{app:temporal_details}\n\nFull per-model temporal ablations are reported in \\cref{tab:window_full} (\\cref{app:window_ablation}). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 69.3\\% ($W{=}1$) to 82.2\\% ($W{=}25$) with FPR halving (9.65\\% to 4.83\\%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at $W{=}3$ while precision and FPR continue improving at larger windows; (3) R1-32B peaks at $W{=}10$ then degrades, likely reflecting overfitting on the small dataset ($n{=}100$); (4) QwQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (\\cref{app:text_window}) show monotonic improvement across all window sizes for both models tested, with larger marginal gains than HS probes (+12.0pp accuracy vs.\\ +3.2pp for R1-8B). The asymmetry supports the interpretation that text features benefit proportionally more from temporal context because they encode less information per step.\n\n\\section{Negative Results Details}\n\\label{app:negative_details}\n\n\\paragraph{BOCPD/CUSUM.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\\% detection rate across all tested configurations ($\\lambda \\in \\{5, 10, 50, 100, 200\\}$). Only R1-8B produces non-zero detection (best: $\\lambda{=}10$, 93\\% rate, +3.45 steps lead). CUSUM configurations universally underperform simple thresholding on lead time. The probe score sequences for 3/4 models show smooth transitions that never trigger the hazard function (\\cref{app:bocpd_config}).\n\n\\paragraph{Mahalanobis distance.} Following TrajGuard~\\cite{trajguard}, Mahalanobis distance from the pre-CP centroid produces $\\Delta d \\approx 0$ between pre-CP and post-CP steps. The discriminative signal resides in minor PCA components (explaining $<$5\\% of total variance) rather than the principal directions that dominate the distance computation.\n\n\\paragraph{RepE.} Mean-difference directions~\\cite{zou2023representation} show inconsistent performance: QwQ-32B achieves 0.756 balanced accuracy (approaching supervised 0.778) but with substantially worse precision (0.512 vs.\\ LR 0.700) and FPR (0.309 vs.\\ 0.120). R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment structure in some models but not others, making it unreliable as a general-purpose method.\n\n\\paragraph{MLP probes.} Two-layer MLPs ($d \\rightarrow 128 \\rightarrow 1$, ReLU) underperform logistic regression on 3/4 models. The commitment boundary is linearly separable at correctly selected layers; additional capacity causes overfitting given the small training sets.\n\n\\paragraph{CCS.} Contrast-Consistent Search~\\cite{burns2023discovering} adapted with contrastive pairs from pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction, making it semi-supervised.\n\n\\paragraph{Cross-model transfer.} 17 configurations (5 directional pairs $\\times$ 3 PCA dimensionalities, plus 2 direct transfers) all fail. Best PCA: R1-8B $\\rightarrow$ QwQ-32B at 59.5\\% (PCA-2048). Best direct: QwQ-32B $\\rightarrow$ R1-32B at 67.3\\% but 1\\% crossing rate. Implementation details in \\cref{app:transfer_details}.\n\n\\section{Cross-Model Transfer Implementation Details}\n\\label{app:transfer_details}\n\nWe test whether safety probes transfer across models by projecting hidden states into a shared dimensionality space and applying cross-model classification.\n\n\\paragraph{Method.} For each source-target model pair, we apply PCA independently to each model's hidden states, reducing to a shared dimensionality $d \\in \\{512, 1024, 2048\\}$. PCA is fitted on the full dataset (including test traces) for each model separately, a setting favorable to transfer since it maximizes the quality of the projection. A logistic regression classifier (C=1.0, class\\_weight=`balanced', max\\_iter=2000, random\\_state=42) trained on the source model's PCA-projected training data is then applied directly to the target model's PCA-projected test data. No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied; PCA serves as a standard linear dimensionality reduction baseline.\n\n\\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.\n\n\\paragraph{Results.} All 17 transfer configurations (5 directional pairs $\\times$ 3 PCA dimensionalities, plus 2 direct transfers for same-dimension pairs) fail to produce practically useful transfer. The best PCA result is R1-8B $\\rightarrow$ QwQ-32B at 59.5\\% balanced accuracy (PCA-2048). The best direct transfer (QwQ-32B $\\rightarrow$ R1-32B) reaches 67.3\\% balanced accuracy, which exceeds the within-model baseline of 65.2\\%. However, this transfer direction achieves only 1\\% crossing rate, meaning the transferred probe almost never triggers detection in practice, rendering it useless for deployment despite above-baseline accuracy. The complete failure under maximally favorable conditions (PCA fitted on full data, no train/test separation for projection) strengthens the conclusion that safety commitment is encoded in model-specific geometric configurations. PCA is a standard linear alignment baseline; its failure indicates that the problem lies in the representations themselves rather than in the choice of alignment method.\n\n\n\\section{Encoder Robustness Analysis}\n\\label{app:encoder_robustness}\n\nTo test whether the HS advantage over text probes depends on the specific text encoder, we replace all-MiniLM-L6-v2 (384d) with BGE-large-en-v1.5 (1024d), a 2.7$\\times$ higher-dimensional encoder with stronger semantic representations. \\cref{tab:encoder_robustness} reports precision comparisons at each model's corrected layer; \\cref{fig:forest_precision} provides a visual summary.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{HS vs.\\ BGE-large (1024d) text probe precision. $\\Delta$: HS minus BGE-large. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\\alpha{=}0.05$).}\n\\label{tab:encoder_robustness}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{HS Prec} & \\textbf{BGE Prec} & $\\Delta$ & \\textbf{95\\% CI} & $p$ & \\textbf{HB} \\\\\n\\midrule\nR1-8B & 0.497 & 0.436 & +0.058 & [$-$0.07, +0.20] & 0.185 & No \\\\\nOT-7B & 0.446 & 0.263 & +0.181 & [+0.08, +0.29] & ${<}0.001$ & Yes \\\\\nR1-32B & 0.588 & 0.475 & +0.117 & [$-$0.00, +0.24] & 0.042 & No \\\\\nQwQ-32B & 0.545 & 0.454 & +0.094 & [$-$0.07, +0.28] & 0.132 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe HS precision advantage is directionally consistent across all four models (positive $\\Delta$ in every case). OT-7B shows a strong, significant advantage (+18.1pp, $p{<}0.001$, survives Holm-Bonferroni). The remaining three models do not survive Holm-Bonferroni correction; R1-32B's CI includes zero with 10{,}000 resamples, so even the individual precision test is non-significant. This is consistent with the prediction in \\cref{sec:limitations} that stronger text encoders would reduce the observed gap. The pattern confirms that the HS modality advantage is genuine but partially attributable to the weakness of the 384d MiniLM baseline.\n\n\\paragraph{Balanced accuracy and FPR.} \\cref{tab:bge_ba_fpr} reports BGE-large comparisons on balanced accuracy and FPR. HS balanced accuracy advantage is directionally positive on all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni. FPR advantage is significant only for OT-7B. R1-8B shows an adverse FPR direction: HS FPR is 1.2pp higher (worse) than BGE ($p{=}0.564$), the only model where HS does not improve over the stronger encoder on this metric.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{HS vs.\\ BGE-large (1024d): balanced accuracy and FPR differences. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: Holm-Bonferroni correction (4 tests per metric, $\\alpha{=}0.05$).}\n\\label{tab:bge_ba_fpr}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & $\\Delta$\\textbf{BA} & $p$ (BA) & \\textbf{HB} & $\\Delta$\\textbf{FPR} & $p$ (FPR) & \\textbf{HB} \\\\\n\\midrule\nR1-8B & +8.4 & 0.029 & No & $-$1.2$^\\dagger$ & 0.564 & No \\\\\nOT-7B & +10.8 & 0.002 & Yes & +10.5 & ${<}0.001$ & Yes \\\\\nQwQ-32B & +9.3 & 0.067 & No & +2.7 & 0.368 & No \\\\\nR1-32B & +10.9 & 0.008 & Yes & +7.8 & 0.165 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\scriptsize $^\\dagger$Adverse direction: HS FPR higher (worse) than BGE.\n\\end{flushleft}\n\\end{table}\n\n\n\\section{Position-Residualized Probing}\n\\label{app:position_residual}\n\nTo quantify non-positional safety signal, we regress out the normalized position $t/T$ from each hidden-state (or text-embedding) vector before training the logistic regression probe. \\cref{tab:position_residual} summarizes results across all models at their optimal $W$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Model} & $W$ & \\textbf{HS BA} & \\textbf{Resid.\\ HS BA} & \\textbf{Drop} & \\textbf{Resid.\\ Text BA} \\\\\n\\midrule\nR1-8B & 15 & 0.834 & 0.669 & 16.5pp & 0.605 \\\\\nR1-8B & 3 & 0.813 & 0.571 & 24.3pp & 0.534 \\\\\nOT-7B & 3 & 0.732 & 0.609 & 12.3pp & 0.540 \\\\\nQwQ-32B & 3 & 0.796 & 0.619 & 17.7pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Position-residualized probe balanced accuracy. All residualized HS probes significantly above chance ($p{<}0.001$). HS residualized probes retain more non-positional signal than text residualized probes (+3.7 to +6.9pp).}\n\\label{tab:position_residual}\n\\end{table}\n\nPosition is a significant component across all models (12--18pp BA reduction at optimal $W$), but all models retain substantial non-positional signal (residualized BA 0.61--0.67, all $p{<}0.001$). Larger temporal windows reduce position dependence: R1-8B drops 24.3pp at $W{=}3$ but only 16.5pp at $W{=}15$, indicating that broader context captures more non-positional structure.\n\nFor QwQ-32B specifically, three complementary significance tests confirm the residualized probe performs above chance: Wilcoxon signed-rank $p{=}0.0024$, paired $t$-test $p{=}0.0008$, permutation test $p{<}0.001$ (bootstrap 95\\% CI for per-trace BA: $[0.575, 0.744]$). The position baseline achieves higher balanced accuracy (0.832 vs.\\ HS 0.796), and HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are not statistically significant at $n{=}19$.\n\n\n\\section{Multi-Seed Stability}\n\\label{app:multi_seed}\n\n\\cref{tab:multi_seed} reports LR probe performance across 5 random seeds at each model's corrected layer and optimal $W$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LR probe stability across 5 random seeds (corrected layers, optimal $W$). 7--8B models are stable; R1-32B shows high variance due to small sample ($n{=}20$).}\n\\label{tab:multi_seed}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Precision} & \\textbf{Bal.\\ Acc} & \\textbf{FPR} \\\\\n\\midrule\nR1-8B & $0.590 \\pm 0.072$ & $0.756 \\pm 0.028$ & $0.154 \\pm 0.026$ \\\\\nOT-7B & $0.421 \\pm 0.034$ & $0.633 \\pm 0.023$ & $0.157 \\pm 0.021$ \\\\\nQwQ-32B & $0.651 \\pm 0.099$ & $0.731 \\pm 0.028$ & $0.133 \\pm 0.032$ \\\\\nR1-32B & $0.594 \\pm 0.128$ & $0.692 \\pm 0.056$ & $0.207 \\pm 0.145$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nR1-32B's high FPR variance (std $= 0.145$) reflects a single outlier seed (FPR $= 0.48$), amplified by the small test set ($n{=}20$). At 7--8B scale, all metrics are stable (precision std ${<}8$pp, FPR std ${<}3$pp), supporting robust conclusions.\n\n\\paragraph{R1-8B FPR per-seed breakdown.} \\cref{tab:r18b_fpr_seeds} reports per-seed HS vs.\\ text FPR comparisons for R1-8B. The HS advantage is directionally consistent (5/5 seeds), with 2/5 reaching $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds ($\\alpha{=}0.01$), 1/5 remains significant. Text FPR is highly stable (std $= 0.007$) while HS FPR is split-sensitive (std $= 0.040$), which explains why the canonical-split FPR advantage ($-7.4$pp) does not generalize robustly across seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-8B FPR per-seed comparison (L14, $W{=}15$). Direction is consistent (5/5 HS $\\leq$ Text); 2/5 reach $p{<}0.05$ uncorrected, 1/5 after Bonferroni correction (5 seeds, $\\alpha{=}0.01$).}\n\\label{tab:r18b_fpr_seeds}\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{HS FPR} & \\textbf{Text FPR} & $\\Delta$\\textbf{FPR} & $p$ \\\\\n\\midrule\n0 & 0.161 & 0.165 & $-$0.004 & 0.440 \\\\\n1 & 0.061 & 0.166 & $-$0.105 & ${<}0.001$ \\\\\n2 & 0.123 & 0.176 & $-$0.053 & 0.093 \\\\\n3 & 0.148 & 0.167 & $-$0.018 & 0.293 \\\\\n4 & 0.100 & 0.176 & $-$0.076 & 0.021 \\\\\n\\midrule\nmean$\\pm$std & $0.119 \\pm 0.040$ & $0.170 \\pm 0.007$ & $-$0.051 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{R1-32B per-seed breakdown.} \\cref{tab:r132b_seeds} reports the full per-seed breakdown for R1-32B. Seed 0 is an outlier (FPR $= 0.483$), driven by test-set trace allocation at $n{=}20$. Excluding seed 0, FPR std drops from 0.145 to 0.046.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{R1-32B per-seed performance (L63, $W{=}1$). Seed 0 is an outlier driven by test-set trace allocation.}\n\\label{tab:r132b_seeds}\n\\begin{tabular}{cccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Precision} & \\textbf{Bal.\\ Acc} & \\textbf{FPR} \\\\\n\\midrule\n0 & 0.441 & 0.594 & 0.483 \\\\\n1 & 0.750 & 0.748 & 0.109 \\\\\n2 & 0.685 & 0.670 & 0.111 \\\\\n3 & 0.652 & 0.733 & 0.111 \\\\\n4 & 0.444 & 0.715 & 0.221 \\\\\n\\midrule\nmean$\\pm$std & $0.594 \\pm 0.128$ & $0.692 \\pm 0.056$ & $0.207 \\pm 0.145$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 686,
      "startLine": 1,
      "totalLines": 686
    }
  },
  "sourceToolAssistantUUID": "bebb4622-93c4-4aa7-b757-73cebcd6cced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 60 · 2026-05-18T13:02:48.888Z_

```json
{
  "parentUuid": "8b444efc-7739-413d-b17b-9396c3757c35",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f1fa1087-e38c-4343-aa98-78eb6766a34a",
  "timestamp": "2026-05-18T13:02:48.888Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。  ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models - **路径**: projects/contrastive_trace_safety/docs/p…",
  "leafUuid": "f1fa1087-e38c-4343-aa98-78eb6766a34a",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on layer selection sensitivity in safety probes",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


### Assistant

_source line 63 · 2026-05-18T13:02:51.986Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also check if there's more to the appendix and read the references file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1fa1087-e38c-4343-aa98-78eb6766a34a",
  "isSidechain": false,
  "requestId": "req_011CbA5Zt6SBZxTFirHXx32S",
  "type": "assistant",
  "uuid": "c9e4c451-a734-42ca-beae-4f16ba59ced0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaokNsSBRq2nUdWvxZGFeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36394,
      "cache_read_input_tokens": 33580,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 33580,
          "cache_creation_input_tokens": 36394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36394
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

_source line 64 · 2026-05-18T13:02:53.445Z_

论文全文已读完。现在渲染 PDF 关键页面并获取 ARR reviewer guidelines 详细内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9e4c451-a734-42ca-beae-4f16ba59ced0",
  "isSidechain": false,
  "requestId": "req_011CbA5Zt6SBZxTFirHXx32S",
  "type": "assistant",
  "uuid": "e5278184-a089-419e-ad01-194f209032ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaokNsSBRq2nUdWvxZGFeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36394,
      "cache_read_input_tokens": 33580,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 33580,
          "cache_creation_input_tokens": 36394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36394
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

_source line 65 · 2026-05-18T13:02:55.735Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01BvvD7Tu6tFL6NuMaJkW59P`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf",
  "pages": "1-8",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5278184-a089-419e-ad01-194f209032ad",
  "isSidechain": false,
  "requestId": "req_011CbA5Zt6SBZxTFirHXx32S",
  "type": "assistant",
  "uuid": "b58f0129-f167-4734-a879-4960f946a93e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaokNsSBRq2nUdWvxZGFeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36394,
      "cache_read_input_tokens": 33580,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 33580,
          "cache_creation_input_tokens": 36394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36394
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

_source line 66 · 2026-05-18T13:02:57.261Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xa3PPewkADWAkAhfunxyEu`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what dimensions should reviewers evaluate, what makes a good review, how should soundness and excitement be scored, what are common mistakes to avoid. Full details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b58f0129-f167-4734-a879-4960f946a93e",
  "isSidechain": false,
  "requestId": "req_011CbA5Zt6SBZxTFirHXx32S",
  "type": "assistant",
  "uuid": "497a4757-3001-4112-8c2f-81ea8c78baa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaokNsSBRq2nUdWvxZGFeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36394,
      "cache_read_input_tokens": 33580,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 33580,
          "cache_creation_input_tokens": 36394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36394
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

_source line 67 · 2026-05-18T13:02:58.305Z_

<details><summary>↩ Tool result · `toolu_01BvvD7Tu6tFL6NuMaJkW59P`</summary>

```text
Error: result (5,323,809 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/59a48043-f2ca-4de6-bd44-a46da822d6ca/tool-results/mcp-agent-ml-research-pdf_to_images-1779109378293.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/59a48043-f2ca-4de6-bd44-a46da822d6ca/tool-results/mcp-agent-ml-research-pdf_to_images-1779109378293.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b58f0129-f167-4734-a879-4960f946a93e",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "cc28517e-4d53-4810-afbd-33e57bebb7f8",
  "toolUseResult": "Error: result (5,323,809 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/59a48043-f2ca-4de6-bd44-a46da822d6ca/tool-results/mcp-agent-ml-research-pdf_to_images-1779109378293.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/59a48043-f2ca-4de6-bd44-a46da822d6ca/tool-results/mcp-agent-ml-research-pdf_to_images-1779109378293.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 67,
    "serialized_bytes": 5323846,
    "serialized_sha256": "74e10cae79e2f277cfe2ce44f2a8455f95b6123b43784b4b7c2046b7ba66cf46",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "b58f0129-f167-4734-a879-4960f946a93e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。  ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models - **路径**: projects/contrastive_trace_safety/docs/p…",
  "leafUuid": "cc28517e-4d53-4810-afbd-33e57bebb7f8",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on layer selection sensitivity in safety probes",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca"
}
```

---


### Tool result

_source line 70 · 2026-05-18T13:03:10.642Z_

<details><summary>↩ Tool result · `toolu_01Xa3PPewkADWAkAhfunxyEu`</summary>

```text
# ARR Reviewer Guidelines Summary

## Key Evaluation Dimensions

Reviewers assess papers across three primary scores:

1. **Soundness**: Technical correctness and validity. Must be justified by review text—low scores require identifying specific faults.

2. **Excitement**: Personal interest level, orthogonal to soundness. Subjective preferences need not require explicit justification.

3. **Overall Assessment**: Composite recommendation balancing soundness, excitement, novelty, and potential impact.

## Characteristics of Strong Reviews

Effective reviews are:
- **Specific**: "The paper omits references X, Y, Z" rather than "missing relevant references"
- **Justified**: Each score reflects actual evidence from the review content
- **Professional**: "Write the review you would like to get yourself"
- **Fair**: Avoid cognitive biases (see heuristics H1-H17 below)

## Critical Reading Approach

Reviewers should read papers twice:

1. **Skim first**: Identify research questions, methodology scope, and expected contributions without examining results
2. **Deep read**: Evaluate technical soundness, evidence quality, and novelty

This prevents confirmation bias and hindsight bias from tainting initial assessments.

## Common Review Mistakes to Avoid

**Cognitive Biases (Heuristics H1-H17):**
- H1: Dismissing findings as "unsurprising" despite lacking prior empirical validation
- H3: Demanding novelty citations when none may exist for truly original work
- H5: Requiring SOTA results when papers contribute via other dimensions (efficiency, interpretability)
- H6: Penalizing negative results—these provide valuable community knowledge
- H7: Criticizing simplicity; simpler solutions are preferable
- H13: Listing optional experiments as weaknesses rather than suggestions
- H16: Treating acknowledged limitations as rejection grounds without justification

## Common Paper Problems to Flag (M, T, R, G codes)

**Methodology Issues (M):**
- M1: LLM evaluators used without validation in that context
- M2: Insufficient reproducibility details or unclear code availability
- M3: Data quality issues not disclosed in resource papers

**Results Issues (R):**
- R1: Statistical practices (p-hacking, cherry-picked results, undertrained baselines)
- R2: Claims overgeneralizing from limited samples
- R4: Overclaiming (e.g., "LLMs understand language" from benchmark performance)

**General Issues (G):**
- G1: Unclear research questions or contributions
- G3: Misrepresented related work or unfair comparisons

## Scoring Integrity

The guideline emphasizes: "If you give a low Soundness score without finding major faults, your review is not faithful to your recommendation." Scores must align with documented concerns.

## Author Engagement

After author responses, reviewers should:
- **Acknowledge** rebuttal attempts, even if unconvinced
- **Update** scores when weaknesses are genuinely addressed
- **Explain** why responses proved insufficient if issues persist

## Prohibited and Limited Practices

- **Confidentiality**: Never upload manuscripts or reviews to non-privacy-preserving AI tools
- **Generative AI**: Cannot use LLMs to create initial review drafts; limited use for grammar assistance acceptable
- **Anonymity**: Postpone related-work searches until after forming initial impressions; disclose known author identities

## Secondary Reviewers

The main reviewer remains responsible for timely submission and sustained engagement through author discussion.

---

**Key Philosophy**: Reviews should balance rigor with fairness, recognizing that NLP encompasses diverse contribution types (models, resources, analyses, surveys) beyond engineering-focused benchmarking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "497a4757-3001-4112-8c2f-81ea8c78baa5",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "84162a57-c8b0-4c51-9d96-08d6d69da83a",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines Summary\n\n## Key Evaluation Dimensions\n\nReviewers assess papers across three primary scores:\n\n1. **Soundness**: Technical correctness and validity. Must be justified by review text—low scores require identifying specific faults.\n\n2. **Excitement**: Personal interest level, orthogonal to soundness. Subjective preferences need not require explicit justification.\n\n3. **Overall Assessment**: Composite recommendation balancing soundness, excitement, novelty, and potential impact.\n\n## Characteristics of Strong Reviews\n\nEffective reviews are:\n- **Specific**: \"The paper omits references X, Y, Z\" rather than \"missing relevant references\"\n- **Justified**: Each score reflects actual evidence from the review content\n- **Professional**: \"Write the review you would like to get yourself\"\n- **Fair**: Avoid cognitive biases (see heuristics H1-H17 below)\n\n## Critical Reading Approach\n\nReviewers should read papers twice:\n\n1. **Skim first**: Identify research questions, methodology scope, and expected contributions without examining results\n2. **Deep read**: Evaluate technical soundness, evidence quality, and novelty\n\nThis prevents confirmation bias and hindsight bias from tainting initial assessments.\n\n## Common Review Mistakes to Avoid\n\n**Cognitive Biases (Heuristics H1-H17):**\n- H1: Dismissing findings as \"unsurprising\" despite lacking prior empirical validation\n- H3: Demanding novelty citations when none may exist for truly original work\n- H5: Requiring SOTA results when papers contribute via other dimensions (efficiency, interpretability)\n- H6: Penalizing negative results—these provide valuable community knowledge\n- H7: Criticizing simplicity; simpler solutions are preferable\n- H13: Listing optional experiments as weaknesses rather than suggestions\n- H16: Treating acknowledged limitations as rejection grounds without justification\n\n## Common Paper Problems to Flag (M, T, R, G codes)\n\n**Methodology Issues (M):**\n- M1: LLM evaluators used without validation in that context\n- M2: Insufficient reproducibility details or unclear code availability\n- M3: Data quality issues not disclosed in resource papers\n\n**Results Issues (R):**\n- R1: Statistical practices (p-hacking, cherry-picked results, undertrained baselines)\n- R2: Claims overgeneralizing from limited samples\n- R4: Overclaiming (e.g., \"LLMs understand language\" from benchmark performance)\n\n**General Issues (G):**\n- G1: Unclear research questions or contributions\n- G3: Misrepresented related work or unfair comparisons\n\n## Scoring Integrity\n\nThe guideline emphasizes: \"If you give a low Soundness score without finding major faults, your review is not faithful to your recommendation.\" Scores must align with documented concerns.\n\n## Author Engagement\n\nAfter author responses, reviewers should:\n- **Acknowledge** rebuttal attempts, even if unconvinced\n- **Update** scores when weaknesses are genuinely addressed\n- **Explain** why responses proved insufficient if issues persist\n\n## Prohibited and Limited Practices\n\n- **Confidentiality**: Never upload manuscripts or reviews to non-privacy-preserving AI tools\n- **Generative AI**: Cannot use LLMs to create initial review drafts; limited use for grammar assistance acceptable\n- **Anonymity**: Postpone related-work searches until after forming initial impressions; disclose known author identities\n\n## Secondary Reviewers\n\nThe main reviewer remains responsible for timely submission and sustained engagement through author discussion.\n\n---\n\n**Key Philosophy**: Reviews should balance rigor with fairness, recognizing that NLP encompasses diverse contribution types (models, resources, analyses, surveys) beyond engineering-focused benchmarking.",
    "durationMs": 12332,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "497a4757-3001-4112-8c2f-81ea8c78baa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 71 · 2026-05-18T13:03:17.251Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I have the complete paper content and the ARR reviewer guidelines. Now let me render PDF pages in smaller batches to see the actual visual layout, figures, and tables.

Actually, the PDF images were too large. Let me render just a few key pages to check the visual quality of figures and tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84162a57-c8b0-4c51-9d96-08d6d69da83a",
  "isSidechain": false,
  "requestId": "req_011CbA5bV5tLfQ9hsioUurBz",
  "type": "assistant",
  "uuid": "aea72abb-4f52-4bf6-a80f-e088bcfcf2fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5ekvuMkhjxKwdsqUanb6f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1630,
      "cache_read_input_tokens": 69974,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 69974,
          "cache_creation_input_tokens": 1630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1630
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

_source line 72 · 2026-05-18T13:03:17.381Z_

PDF 太大无法一次渲染。让我分页查看关键图表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aea72abb-4f52-4bf6-a80f-e088bcfcf2fb",
  "isSidechain": false,
  "requestId": "req_011CbA5bV5tLfQ9hsioUurBz",
  "type": "assistant",
  "uuid": "78d53a75-0d2f-47f3-8aac-5d181937d769",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5ekvuMkhjxKwdsqUanb6f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1630,
      "cache_read_input_tokens": 69974,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 69974,
          "cache_creation_input_tokens": 1630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1630
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

_source line 73 · 2026-05-18T13:03:17.475Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_011B3cdgcKSkpAj3o9KioKMH`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf",
  "pages": "1-2",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78d53a75-0d2f-47f3-8aac-5d181937d769",
  "isSidechain": false,
  "requestId": "req_011CbA5bV5tLfQ9hsioUurBz",
  "type": "assistant",
  "uuid": "053c7611-d78d-427d-9d6a-4b8358a7b5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "59a48043-f2ca-4de6-bd44-a46da822d6ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5ekvuMkhjxKwdsqUanb6f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1630,
      "cache_read_input_tokens": 69974,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 69974,
          "cache_creation_input_tokens": 1630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1630
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

_source line 74 · 2026-05-18T13:03:18.098Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_011B3cdgcKSkpAj3o9KioKMH`&lt;/summary>

```text
Error: result (1,293,549 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/59a48043-f2ca-4de6-bd44-a46da822d6ca/tool-results/mcp-agent-ml-research-pdf_to_images-1779109398091.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/59a48043-f2ca-4de6-bd44-a46da822d6ca/tool-results/mcp-agent-ml-research-pdf_to_images-1779109398091.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "053c7611-d78d-427d-9d6a-4b8358a7b5c1",
  "isSidechain": false,
  "promptId": "33be94a3-2a9f-4a7b-b60f-e801f93532a5",
  "type": "user",
  "uuid": "93bd4b28-a618-4ac8-a2ea-d0a359831855",
  "toolUseResult": "Error: result (1,293,549 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/59a48043-f2ca-4de6-bd44-a46da822d6ca/tool-results/mcp-agent-ml-research-pdf_to_images-1779109398091.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/59a48043-f2ca-4de6-bd44-a46da822d6ca/tool-results/mcp-agent-ml-research-pdf_to_images-1779109398091.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p1.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABNkAAAbaCAIAAAB3QTY3AAAACXBIWXMAABcSAAAXEgFnn9JSAAbK6UlEQVR4nOzdd5wV1f0//qUoKhoVxYINFYk1Sqyxl0RRMJZoQmyJ2NFEE4klig81MdFozMfoRwVbiBV7QWOs0di7YheMiiCKYJcisL/3Z+eX8x3v3b1777I7C/J8/sGDPXPuzJm5U87rTqurBwAAgGLVtXcDAAAAmOfIogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiw6r3j//fefrKi9G1iQN9544/LLLz/hhBP233//o48+Ov4fSybKP/roo3322aemUY0bN65kGU6ZMqVtWt28SZMmDRky5Mgjj3z55Zfbqw3lWnFpt6mRI0ceeuihF1xwwYwZM9r6U20xkjlt0i+88EKFXc2XX34ZdZ566qkKddKmVP2K/dprr5WMZPTo0RXqf/bZZ021bQ4xt2w+tWrT+frkk0+GDx/+y1/+cuDAgSeddNJDDz3UGk1uHRVW+Geeeebdd9+dOXNmMS0p2frmqKNGfUPzTjnllAMOOCC+xwsvvPDjjz8ubNKvv/56U99RtCqGfvrpp4U1Zk7Tjkcrvtlk0XnF/fffv/vuuy+00EJ1X9ehQ4dtt932oIMOau8GtrnJkycffvjhHTt23HTTTWNneu211x533HHf/va3YyFsuOGGa6+9diycmkZ4ww03LLHEEvmF+corr7RR4yuLHsy6666btWGRRRaJkNwuzchr9aXdduJ7TN9g9Izb9FNtMZI5cNKDBw9ec80168ost9xye+21V7Z+RkdzrbXWKq/To0ePqPPee+/V17hin3/++f369evUqVMa1Q9/+MMK9d96660DDzxw5ZVXzk/92Wefbd1F0TJz0eZTk7aer/vuu2+ppZaKsa2yyipXX331HnvsEf/fbbfdvvrqq9aahRaLlXnfffddfvnly9f5bt26de3aNf4Ta29UOPjgg1966aU2bUxsYp07d04N+O53v9umk6ve9OnTo21Zq371q19deeWVXbp0iW0/OjDFNOCvf/3rlltuWf4dLbrooquttlo0Jv4fa2msq3/4wx/Gjx9fTKvmBO14tOIbTxadt7z66qsRPvN72Ouuu669G1WEGTNmbLTRRjG/0TvJl0+dOvUXv/hFtiha0A169NFH8wuzmCy6//77P/DAA/mS1157Ld+Mv//97wU0o4I2WtptZMCAAWnRRTJptE75Mq/mU2006VbRKu2vbL/99suvlhtssEF0NEvqDBw4MF8n0mmsJGloC1bsww47LNWvnEUzH3zwQX4Sc0IWnZ3NpxXXllZf8dp6tzBx4sRvfetb2XguvPDCKNl7772zP4cOHVrr2J588skf//jHLW5MU6ZMmdK7d+/8Kveb3/wmGxRHk549e6bytv6B+I9//GOa1pyTRY8//visScsss8ysWbPeeOON7M9ll122yGb8+c9/zn9HMfXsiolo0k033dS9e/esvGPHjhGY55GThAUcMphnyaLznOWWWy6/k/3iiy/au0VF+MMf/pDN72OPPVY+9KijjmpZN2jmzJn5hVlAFj3vvPNiQrfddlu+8NNPP82f8X7kkUfauhmVtdHSbiNDhgxJi2777bcvr9DoMm/2U2036VbRKu2v7IorrshvHccee2x5neuuuy5f5/DDD88PbcGKne9hV5NFw/zzz58+Midk0RZvPq24trTFitfWu4Vzzz03fY8jR46MkkUWWST7M7JuTaP65JNPorfdRglt0KBB+XU+/3PwXXfdlR/029/+ti0akLn66qvThOaQLBqhLjutHdZff/0oOfvss1MjJ0+eXFhL4lCe/yK23HLL/NDLL788PzTyc2ENa0cFHDKYZ8mi85xVVlkl7VA6duzY3s0pyGqrrZbN8ltvvVU+dPr06euuu27LukH5Y1JbZ9F///vf8803X6N9xJtvvjm+2aWXXvqMM85o0zZUo+2Wdlv47LPP9txzz8UWWyw6HOV3GDa1zCt/qk0n3Spapf2VleTMk046qbxOzFq+zq9//euSCrWu2N+ALNqyzacV15Y2WvHaerfQt2/f9D3+4x//iJKDDz64Q4cOMc6HH364+vHMnDlzp512aruEFgkzv86XXJqUzrnVNdxBM3bs2LZoQ/0cmUUff/zx1KSNNtooSp5//vllllkm/txll12KbMl7772X/45Ksmhk5uxi3Uz8/6OPPiqyee2igEMG8yxZdJ4zD2bRL7/8Ml2ZfPHFFzdaJw7Mc3gWHTVq1JJLLplNqC3CSWtp06VdsHZc5nPL111Bq2TRWs3tWbRlm08rri1ttOIVsFtYe+210/eYZdEwfvz4mnLCrFmz0mXe7ZJF11tvvfzQa665pi3aUD9HZtH8HYlZFq1vCH5vvPFGfC9FtqRyFg0l95nfd999RTYPvmFk0XnO7GfR6dOnx566LZ4GMXXq1OyBitX7rEHlOq+//nqa5a5du8YBr7zOlClTyo83mTgKTpw4sakHbOYPSE1l0ernK467EyZMKH8e79NPP92tW7c0oRb3ET9sUNNHZs6cGY2v/gGPbbq0W9zCGG1+wX7xxRfN3uTTWsu8Bdpx0k359NNPP/nkk5o+UlgWnTx5cvpmq8mise+KdSz9WU0WbcGuqdYNJ9OCzaemtWXSpEkVsln1o6p1O53N3UKzLa//+qEtZdGaWh5fVv4G5nbJottuu21+6N/+9rcKo8rWsaZyWuW9fVNZNEZYfl93uWq2iM8//zy/oTX7BNr8ta8pizZq2rRp48ePz99bXo3Kiyuv2Szap0+ffIWmHq1U/WZSfbeqyqU6O4uoVZ7nXP2ootq8/HRi6mXReVCLs2h0JgYNGtSjweKLLx6fXW655Q499NBXX3011Yn9zhZbbLHp12222WbXX399DD3llFNS4V577ZUf+T//+c8NN9ywU6dOPXv2jM5Q375980+Z//3vf18yzggSb7755nbbbZfNyH777VfhABO742ht/sixww47PPfcc83OcqTcmOWY2SWXXDL+XWONNU477bSSfWt+tOVZtPJ85T344IMxO/PNN9/KK68crY36p59+etbDjqamZ3JkoiXZcvjggw8uvvjikoVT/gzGOHQdeOCBMQuLLbZY/Lvooovuv//+8dlU4c477ywZSRxco+d3wAEHLLDAAjHFBRdccM8994w41+xCa6Ol3eIWxnrbv3//hRdeeJFFFomam2yyydFHHx1bQXxZMfLNN988P86UhSos85hEU5+KBmxa5i9/+UsMij5lbAhZyVZbbdWyScdXdskll5RPYqeddqpveDBsfuu79957G13OFSZd0v7sBRs333xzOuMUq+VVV13V7FeZmc0sWs2KPXz48OwERefOneObfeCBBypn0ej0/OhHP8qeILrsssseeeSR0U2snEUrb8KtuOFk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d9999+WWW+7XX3f44YenRzfln5zHN54sSis7+eST6xru4Mqev/fEE0+svvrq7d0o+IZ45513sgc/7LnnnlnJjjvuOGLEiPZtFXzjObTB7EtP2Wjqwv7sQcQ77bRTwQ2jHcmitLJ06+kvfvGLGTNmbL311lU+JxBoVv7B/ZMnT7733nt79uzZ6J1dQCtyaIPZl95jF8evRitkj7Cq6ZFgzO1kUVpZ9miKuoYHe26yySZrr722jjK0lvxLO/v169e1a9f03Feg7Ti0wex79NFHs591+vfv/9prr+UHjR079tRTT+3UqVOjL6PmG0wWpZU988wzcZCua3g24E477RQ7l/ZuEXyjDB48OHsZ49JLL+3HYyiGQxu0ildeeeWQQw7Jns3bvXv3NdZYY/XVV48/V1tttTi6vfDCC+3dQIomi9ImJk+enN61DbSuGTNmfPjhh+3dCpjnOLRBa5k+ffqECRPefPPNKl+MxDeVLAoAAEDRZFEAAACKJosCAABQNFkUAACAosmiAAAAFE0WBWAu82Rj3nnnnWY/GHUa/WyrtOq1114rGe3o0aNrHUnJGMaMGdMqbQOAOZAsCsDcZObMmT//+c/XWGONuq9ba621mv3suuuuW/Kp3r17x9hinLPfsPPPP79fv36dOnVKI//hD39Y0xiiGdtuu22+eT/+8Y9nv2EAMGeSRQGYK+29994lwfL++++vUP/BBx8sqR/Br1VSaN5hhx3W4iya2X777WVRAOYFsigAc6WLL754scUWW3jhhVNy22233SrU33PPPXfYYYd8Fj3rrLNavVV//OMfZzOLnnjiibIoAPMCWRSAudLll1/eo0ePQYMGpeTWsWPHpu4aHTduXNeuXa+77rp8Fr3oootavVWzn0VPOukkWRSAeYEsCsBcKcuir7zySj5eHnfccY1WPvHEE/fee+/7779fFgWAOYQsCsBcKcui8Z/tttsuhbclllhi6tSpJTWnT5++9NJLP/LIIzVl0WnTpo0fP758bOUmT548ZcqU7P9VZtEY7fvvv9/ooGaz6KxZsyZMmJCm+MUXX8yYMaPZRgLAnEYWBWCulLLozTffnE+Yf/vb30pqXnnlleuuu278p8oset11122wwQYdOnTo2bNn/Pvd7353xIgRjdYcPnz4yiuvHKPq3LnzJpts8sADDzSbRf/5z39uuOGGnTp1ipF369atb9++L7/8cr5ChSz6+uuv9+/ff+GFF15kkUUWWGCBmOLRRx+9yiqrvPLKK1UvNgCYU8iiAMyVUhadOXPmSiutlPJbRMeSmhtvvPHQoUPrq8iin3322X777ReDunTp8uKLL0bJs88+O99880XJPvvs8+mnn6aas2bNOu6449KoNt988z322ONb3/rWFlts0VQWjY+ccMIJEW4jiD766KNRcvvtt0e1BRdc8MYbb0zVmsqio0aNivwZH48Znz59+pQpU0477bSOHTtGNVkUgLmRLArAXCll0fCnP/0pHzKzpJd5+umnIyJ+/vnn9VVk0QEDBmSDDj/88FS4//77Z4V77bVXfuppPAcddFBW+Prrry+00EJNZdHhw4dn5ZtttlkqXGuttaJkySWXjBiclTSVRTfaaKMoWW211fLjPPPMM2VRAOZSsigAc6V8Fp00adICCyyQItxPf/rTVO1nP/vZEUcckf2/cha9884706ArrrgilUe1VH7fffdFyYwZM3r16pUK//Of/6TKxx9/fKNZdMqUKcsvv3xWftRRR6XynXfeOSs87bTTspJGs+inn37aoUOHKJlvvvnyyfOrr75adtllZVEA5kayKABzpXwWDQMHDkwRLgLbe++9F4UffvhhZNR0Q2blLNqnT5806MEHH0zl+Yy66aabRsktt9ySSlZaaaX8SJq6X/Saa65J5Sl2hn333Tcr/N73vpeVNJpFx4wZkwqXWGKJiMozZ87MBo0aNeqLL76YzYUJAMWTRQGYK5Vk0eeeey6fM0855ZT6hmS41VZbpToVsujEiRPzg55//vk06LHHHkvlHTt2/OyzzyJMlqTTpKksmk+Ye+yxx7n/FR/PCr/1rW+V10xZNJLn4osvnm9h796984kUAOY6sigAc6WSLBo222yzFNWWWWaZKVOmrLjiitdee22qUCGLPvXUU/lBr776ahr07LPP5ge9/PLLP/vZz9KfO+64Y74NTWXRdCdqWGWVVX5YZpdddpk2bVp90/eLXnLJJXVl1l133TfffLP1FioAFEcWBWCuVJ5FR4wYkc9pEf8ikX711VepQoUs+sILL+QHvfHGG00Neu655/r27Zv+3HnnnfNtaCqL9uvXL5Xvv//+FearwjtdLrvssi5dupTE0e7du3/44Yc1LjwAaH+yKABzpfIsGrEzSvI5bciQIfkKFbLotGnTOnXqlAblz4s+/fTT+U+9//77Bx98cPozfw1wfdNZ9Mgjj0zl22yzTYX5qpBFw7hx4wYNGpS9ZiY5/vjjq11qADDHkEUBmCuVZ9Fw6qmnpoTWsWPHd999Nz+08rOLvv3tb6dBkT9T+QMPPJDKV1111Sg566yzUsk666yTH0lTWfT8889P5V27dq3wtKFGs+jo0aOHDx+e6owdO/bnP/95qrbDDjtUudAAYM4hiwIwV4os2r1795LCCRMmpHOGu+66a8nQkiw6dOjQ/ND8S0pHjhyZyq+88spUfs4550TJM888k0o6deqUvbw0c8oppzSaRSNMdu7cOQ0aNmxYftIzZsw4/vjjP/300/omsmi0vFu3btOnT89/Kj1CaY899qhx4QFA+5NFAZgrnXfeeR06dPjyyy9Lyvfaa68sod19990lg2677bZ8Fj3jjDPyQyPprb766tmg/MW9Rx11VFa43nrrRWjMCvv375/GE6k4K3z//ffTS0TDlltumR//oEGD0qAFFljgzjvvzMrHjRu38847H3roodmfgwcPTtXSzahZiv7rX/+aH2F60cvpp59e48IDgPYniwIw94nUt/HGG0cMO+KII6ZMmZIflL2CZbXVVps1a1a+/PPPP99jjz3yWXTttdceO3Zsvs5TTz2VhclevXplZzs//vjjrGTllVceNWpUqvnSSy8tueSS2XgWX3zxCMaXXnppz5498xf6RlSOTJsegzRx4sS11lor34AePXpk9fv27Zud84xovc4666QKSyyxRHY1b5ZFu3TpcsMNN6Q2nHnmmVG4wgorZCdUAWDuIosCMDeJcNi7d+/8c4YWXHDBkqcBbbDBBn/5y1/yJVFhgQUWqCsTcTFSazrbGT766KOf/OQnMWjNNdc89NBDIytGnX322eeTTz4pacmYMWPWWGONNKoIimedddZll10W/1900UU32WSTAQMGHHfccflbTyNqDhw4MN+AaPzgwYOzBsycOTPCZ0kLY1QTJkyILNq1a9e999474ut3vvOdvfbaa4sttoihG264YaTi1l/KAND2ZFEAKDV+/Pgbb7xx2LBhN910U0TBpqpFevzXv/516aWXPvDAA9l51DfffHPUqFElp2RLvPvuu9ddd91FF110++23T5o0qcr2PPjgg9n/X3jhhfj4FVdc8dxzz0UDapktAJiDyKIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFAACgaLIoAAAARZNFAQAAKJosCgAAQNFkUQAAAIomiwIAAFA0WRQAAICiyaIAAAAUTRYFmCO8/vrr7d0E/p+PPvpo4sSJNX1k0qRJL7300pgxY6ZNm5YKZ82aNWHChNZu3dxk6tSpr7766ldffTUHjg2A9iWLArS/d999t1OnTs8//3x7N4T/3yGHHLLrrrtWU/PDDz88/vjjV1ttta5du/bv33/33XdfddVVt9pqq3PPPXfs2LH/+7//++Mf/ziqXXXVVRtvvHHvr1trrbXiI/Htt/HcfM1nn322xRZbpDbss88+bTetcePGrbDCCnV1dX369Pnyyy/nqLEB0O5kUYD2d/LJJ0cP+8ADD2zvhvB/Iq0tvPDCHTt2fPvttyvXHDFixLe+9a0sHU2aNClfvtRSS9U1yLJomD59euTbuv9aYoklIqy24Ww0bdq0acstt1zWjC233LLtJnT22Wen+b3tttvmqLEB0O5kUYB2NmPGjCwYLLjggpMnT27v5lA/dOjQLPAce+yxFaqdf/75WbUVV1yx/ILet956a5lllsln0XDBBRekNNW/f/82aX11dtxxxwKy6MiRI7OpRLB/5ZVX5qixAdDuZFGAdnbrrbemfHLmmWe2d3Oo79OnT/Z1dOvWbcqUKY3Weeihhzp16pRV+/3vf99onaeeeqpz5875LHrRRRel7zpfXryddtqpgCwaLrvssgMPPPCOO+6YA8cGQPuSRQHaWTpDFXr27Dlz5sz2btE87YknnqjLifDTaLWNNtoo1XnzzTebGtuvfvWreTyLAkBTZFGA9vT222+vssoqG2+8cYoot956a3m100477Xf/laWj22+/fY899th2222PPPLI9957r/wjDzzwwHHHHbfDDjvsu+++5557bv7q33//+9+/yxkzZszEiROPP/74GFuM85prrkk177jjjt99Xda8yFTZn2ecccbnn3+er3DjjTfWNzyqZ9ddd42cc9hhh73zzjvZ2IYPH96vX7/tt9/+5JNP/uKLL0oa/PHHH5933nn77bdftPnYY4+977770qCSSdx5551RGBXyhTFTqf7UqVP//Oc/RwO22WabSIM33XTTIYccUuU3MnDgwAEDBqSvo0+fPuV1Hn300VRhhRVWqDC2999/P1qS/pz9LNrUrNW6iPJZdNKkSSeeeGLfvn1j4cd3NGvWrKxOybf/4Ycfxup61FFHbb311vE9Xn755Vm1//znP4cffvhWW2219957P/jgg2kSJR/PP0/4ySefPPjgg2M8P/rRj+JLv/TSS6+++urKM1hhbPUVV576Fm0+ABRAFgVoT7/97W9PPfXU6NaniPL973+/vFp08RdffPGswkYbbRRZbv755+/cuXNWsvTSS+cfnPPll18eeuihUR4d/cgPd999d6dOnZZffvl//etfWYVInlmFzLBhwyJQde3aNZX84Q9/yGqOGzduiy22SOW/+MUvIlzVN8SPnXfeedFFF/3HP/4xc+bMSD7RnhSx9t9//4UWWihdwhojj2b85Cc/iUl06NAhK9xwww3zZ4BjBqPafPPNd++990blXXbZJeocdNBB2eNSo+aIESNSMwYNGpTNRbQzFUbMyEYVqWyttdaKqUeoHjt27Pnnnx+NieZV83V88sknsTA/++yzXr16pTE//PDDJdUiuaWh66+/fnVf9f+ZzSxaYdZqWkT1uSy60korbbzxxnvttVd6mlF8szGh+oZvPxqZPh5xsVu3bossskgqOfvss2PhxJq58MILp8Jbbrklm8Q777wTo0rlzz77bFYeyTNWg2jASy+99PTTT2+33XYx9I9//GPlGWxqbPXNrTz1NW4+ABRGFgVoN1999VWPHj2ikz116tQll1wy9bMbfS5L//79s6HR749MGP3sCITR/84K87csHnzwwVlhemfp7rvvHn8usMAC6WrSyABpcmuuueZjjz0WhQceeGBWEjWnT5+e1Xz88cdTzeOPPz5NZfDgwRGk05+bbLJJVicCauSfmLXXXnutY8eOWWHPnj3PO++8WbNmRR4uDy1jxoyJKUbJT3/606xk1KhRWZ2YlzSJ7t2754NWfUPqLg9a0ar4c5tttkkfvOGGG6rMotHI7GnG+Ue2DhgwoKRatjwzO+64YzVjzsxmFm121qpcRPW5LLrgggtma8X48ePTx4cMGZJV++c//5k+vummm2Zr5t57752VRFDs27dvrIeRhLfddtuscL311ss3L308S48ff/xxTDH+TGdQp02bFnk+y6KVZ7B8bPVVrzzVbz4AFEYWBWg30bfeYYcdsv8fe+yxqZ99+OGHl1dOZ6hWW221VBj9/pJg88gjj6Q+d7rYMrraWWG/fv2ykggVaXJXXnllVhjhMBXm8/CWW26ZFS633HLpZGavXr1Gjx6d6qQoEoklFa688srluSudQU3RKBZCVpIe3TRjxowuXbpESYcOHZ544omscMUVVywJWiHF3TS27ERuxKRI0alalYlx7bXXzmL5Rx99lEWm0Llz55LLOPPnilMEqsZsZtFmZ63KRVTfxP2iRxxxRFp5IjTWN1zOnRp89913Z9X+/ve/l68n6QRsBLy0kvzjH/9INbP0eN9996Xlln7vuPXWW88///xmZ7B8bPVVrzxVbj4AFEkWBWg33//+96+77rrs/2+99Va6fjWSwKefflpSOXWmv/Od76TCCH5ZYUSLrOSXv/xlVrL66qunahdffHHqxH/22Wf1X8+iN910U1YtwkYqfPLJJ9PHb7755lR+++23R0kEtogN+ealLBr/SYVrrrlmVrjffvulwuyFnOGYY46pb0h9aeQjRoxI1dIlo4MHD85Kqgxa22+/fVYSGfLggw+OBVvFV/F/Hn744Whw+nP//fdPDTv55JPzNfv27ZsGpSVfjdnMos3O2mxm0WuvvTY174EHHqj/ehZNt5vGSpsK//Of/2SFf/nLX1JhevhweXrM32obq+hVV12Vv1S78gyWj636lafKzQeAIsmiAO1jzJgx3bt3nzZtWirp169f6life+65JfWr7ExvvfXWWUn+PsYrr7wyjTk771dTFo20sMIKK2Tlu+22W33DCbRLL70037wWZ9HIPGmiI0eOTNXSHZvp1HGVQSt/JWddw2m6aO3UqVOb+0Lq991337PPPjv9mb+Meemll04n8epzFzOHDTbYoNkxJ7OZRZudtdnMoumkZbj44ovr2yCLzpgxI52NzKyxxhrpet3KM1g+tupXHlkUYA4kiwK0j9/85jddunRZMWexxRZLHevevXunK2wzVXam11lnnaxkww03TNXyXfzsLs2asmg49dRTs/LOnTuPGzeuZ8+e2fnVpMVZ9MYbb0wTzb83cu21184K0/2H1Qet888/P90KmNlmm21KlmeJyZMnx9cRmTP/jeTHcNVVV6XKV199dSqv/BzdEtVk0a+++uqEE05oagyVZ202s2h86Wm00dT6Nsii9Q2PRMq/EaeuYaVKFwBXmMHysVW/8siiAHMgWRSgHUybNq179+4PPfTQeznjx49Ppx/DXXfdlf9IlZ3pRqtdccUVabTZA41qzaKRH9JzcSNt7rvvviVz1OIs2mhLwqqrrpoVphsyqw9a9Q3XPA8cODC1uSSrlIsotcsuu7z3deecc076+Pe+971U+ZNPPsn/cPDaa69VGHNeNVn073//+6677lphJBVmrRXPi8bKWd82WbS+4Ux7rJP5hxXnfzppagbLx1b9yiOLAsyBZFGAdnD11Vc3em1neshQXdkDWqvsTJ9++ulZSXTHU7WhQ4dmhZEDs9vzas2iIQJSGnr//feXDG1xFv3qq6/S62Qin6RqyyyzTFaY3s+50korZSWVg9Y+++wzY8aM7P9jxozZfPPNswoRlsoXeGbWrFnf/va3s1th87744ov8K0zSg3DyyzmccsopTY15woQJRx99dLolstksGik3ZvOkk05qdGzNzlqVi6i+iSx6/fXXZ4Xzzz//Rx99VN8GWXTkyJHpWVkxLxdccEH2LKtYK5qdwfKxVb/yyKIAcyBZFKAdbLjhhvlbE5M33nijLuell15Kg6rsTGdvyMziRLoZNeJQSde8BVk0vd6jZ8+e5de7tjiL1udyXQp1n376afYkpx49eqTHOG288cZZtUgsWcmHH36YHviUHi+04oor5m8djI9naefmm28uX+CZO+64o1u3bhFsygfttddeaZnk02PEy/QE16WWWmr8+PHlnx09enTv3r2zt5Vk0o8CdY1l0enTp2fjvOGGGxptZ7OzVuUiqs9l0fhIKkzrybHHHpuVtHoWveyyyzbYYIP8+nPcccfF0HXXXbfZGWz0LGuVK48sCjAHkkUBinb55ZdH9/f6668vHzR16tTOnTunDnckk3RKLT2UaNFFF02F6fzPOuusk0YSSSYbSfTd6xtSU/S/48/NNtssxa38Q19SQL3wwgtT4Y033ljStsgPq6yySgxq9KxdenJpr169spIZM2akk4rpobuTJ09Ok0ivf4wMloWo+DdLKdkNrvPNN9+tt96aJpGFlrqGc2jR5mHDhkXWTSf9Yu6y92RGnllhhRXGjh2bfSpSYiSTKCl/NHHm888/j6W39tprN3pD6YknnliXk125mvniiy/23HPPrHzllVdOdzxmE/3tb38bs3/OOefkx3booYemUcVE0znA+N5vuummdM3qG2+80WhTm521KhdR/X+zaHw8VpX4Uuob3vyZXeK7xhprpJuB809gTuczzzzzzFR43333ZYVHHnlkKkyvwDnvvPNSYfaTR2TR+P+pp55askyyBVV5BsvHVl/1ylP95gNAYWRRgEINGjQoO2mzwAILfP/733/++efToAMOOCC9kDPZYIMNokeezjpmIjhFqtxmm23yhendoeGpp55aa621oqsdUap///5dunSJaJSCaHTWl1xyyfTBaEkkhNtvvz1d7hi6d++eRdm8M844IwalPJP55JNPSh5Fs/POO8e0vvvd7+YLBw4cGBElck4qibTwy1/+MhtJJIpjjjlm/vnn33XXXU844YSYeuTn/B2G9Q3nu1KiCDH+UaNGLbTQQosvvvimm246YMCA0047rb7hOtXI8D179tx3330PPPDAGFXv3r3LT/NmYhLpHt2oFlkuDbrnnntictmbKpOIlyUntCO0pznt0aPH5ptvvuyyy8ZXHDH1ueeeS9WuuOKKdJY4WWqppeL7XX755dOpy7qGt2s29ZilZmetykVU35BFd9ttt3fffTcy5CabbBKrR+SxyKUHHXRQZOysztChQ9NJ7LqGfBvJc/jw4QsvvHAqjBXp6aefPv3002MtSoWrrLJKrNgXXHBBfo1abLHFIsnHmhaRO+Y6JhqT3mKLLTp16vSrX/0qy4cVZrDRsVW58tS6+QBQDFkU4BtrwoQJd955Z3TKG736tAUeeeSRrbbaqlVG1agIFc8880y0+f3332+0QoS0CDkjR45MeTj+LElu2aWkM2bMiBm/5ZZbYoT517G0kbFjx15//fXnnXfehRdeeNddd0XGa4upVDNr1Syi8OKLL6b/f/DBB9HmJ554opo338ymt95665133on/xFd87733xnedTqLWz9531+zKA8CcRhYFoEmRYe6+++7bb789CzODBw/OPyEGAKDFZFEAmnTVVVdlVzDedtttkyZN6tWrVwGnzgCAeYEsCkCThgwZkmXRPffcc/vtty95Eg8AQIvJogA06YMPPvje974XWbRLly7592QCAMwmWRSAZnzyySfp7SMAAK1CFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosigAAABFk0UBAAAomiwKAABA0WRRAAAAiiaLAgAAUDRZFAAAgKLJogAAABRNFgUAAKBosijMQz766KOJEye2dyuARnz55Zeff/55e7eC/2fq1KmvvvrqV1991d4NAfjGkkVhHnLIIYfsuuuuTQ397LPPtthii97/tc8++xTZNphnvf3224MHD15sscVuuummthj/ddddt+mmm/b+utVXX32nnXYaPXp0W0yxVYwYMSK/R+rfv3+RUx83btwKK6xQV1fXp0+fL7/8sshJA8w7ZFGYV0TUXHjhhTt27Bgd36bqTJs2bbnllqtrsOWWW87+RM8555xRo0bN/njm3gZABf/+979/9KMfxVaZbXRtlEXDzJkzjznmmLr/6tSp01NPPdXisY0fP37IkCGt2LymRLM322yzrM1rrrlmm06rZF9x9tlnp8V12223temkAeZZsijMK4YOHZr1q4499tgK1XbcccfWyqL33HNPhw4d7r///tkcz9zbAGjKs88+269fv912223BBRdMmaftsmh44okn0oRWWWWVFo9nxowZW2+9dav8VlWN/fbbr4AsWr6vGDlyZDbdjh07vvLKK203aYB5mSwK84o+ffpkXatu3bpNmTKlqWo77bRTq2TRN998MyYU42mvKNjuDYAKPv7445kzZ8Z/TjzxxGKyaKTfNKHevXu3eDxHHXVUa103UY0CsmhT+4rLLrvswAMPvOOOO9pougDIojBPyJ8SCdHHaqpmq2TRMWPGrLTSStl42iUKtnsDoEqXXHLJXJRFU3L+xmRR+wqAdtT6WXTatGkvvfTSww1efPHF/OmXWbNmxU7/8ccff/DBB5977rmPPvqo/OPvv//+008//emnn7Z6w2BeNnDgwAEDBqSeaJ8+fZqqmc+ikyZNiq5n3759ozs4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yimnJBIJdfO9e/cOHDiwfPnypKCfSdm0aRMq5eijjyblo48+ysGsH4gJEyZUr16dj5533nlJb8DNrVixIjcgaUq58cYbuURpkOcczdt3333Hh4oWLUp1Jb1h/fr1KISCBQtymzTwoYI1a9a0adOGnkvOKWZeZycTSNsoNr7//vtu3bpxM48888wz2fLOwxLjxo2rXLkylXDDDTeYRFtj2Fi2bBlW++WXX169evXVV1/NPV26dMm5vE2cOJFP4NXk3CccDmk4LuqQHr/++utVV12FKongovCic845Z8eOHeGfcESgXnJWkvq7mzdvbt++Pb/mE3qQc6Ck1OS6det0uWfPnhNOOIGC41MG7rzvvvtIr1Sp0r59+5QCbYCCNm7cWA7TL7/8okr7v//7P/PUvffe+9Zbb+VKUf4/kD2MWYkSJY477rjc/G6Wkd+EjR7Ru3dv8pMnXDRt33TIUfTs2bNXr17x7x85cmS7du3sKf2nnnrKcFHh7LPPzmUuCt5///0ILgrOP//8hA9l/sEHHzzqqKO4nD17do5mDAmHn/fr1y+QbvSq588tw4pzjYvanz5IkPMKFSocclw0VaNEoG3bttFcNAvvzEZkY5seDKifABcNawzPH38pVqzYwoULdYkfglty6623ZmNOAhWydu1aPhERN+FwhCP7uShi/dVXX33gY/ny5bt27TI/oTdxWxcvXrxgwYKlS5cavU/H+DQZVq1ale3Zc8gaHnrooWgumhZ///vfI/xdCFWe0APEddCgQTlxcxh79+7FV3v33XftxHr16lHwKVOmBG4eP3486RdeeKFJmTZtWth1w8zcc8895hJ73KBBgxUrVmQ5k1kDJPlQ4aJeDGE7yIbO7KtefvnlvOKiQnTfdMjPePvttwNcVK2Zy1z022+/jeainj8PfNppp5lL/ONWrVp9/vnnOZ+7IPh0165d7RQyljtcdMKECSbOJVtwzjnnHHJcNAv43//932gumocIi1Ne4Y033ghw0aS444474KI5mpO0eXBwsJHNXPSPP/7ABMJYcLhRuPzDpVmD8eWXX873ARflLzds3ryZdAjq/GSAjmZv9hyyjMOVi956662XXXZZTtwcRp8+fVq3bh1IlCfxz3/+M5CumJaLL77YpKgJhg0bZt+2du3aDh062Clz5sypVauWWZeVOzjMuOhBNnRmX+W4qEOW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cHDIbTgu6uDg4ODg4ODg4ODg4JDbcFzUwcHBwcHBwcHBwcHBIbfhuKhDXJhzCPIbtm7dumnTplz+aPYe8p4F7Nu3L8vHQ2cjIvKQT3Lo+cdh79q1K69zke+Q+73GwcHBwcHBwcGG46IOsfDJJ58UKFDg7rvvzuuMHIA1a9bcdNNN/fr1K1KkSMOGDXNhg+9169bxufr169erVy+nvxWNli1bHnPMMRs3bsyTry9durRnz56VK1emNlLdk7c5FN54442uXbt26tSpcOHCXbp0ycOc5Dc8/vjjiURizpw5eZ0RBwcHBwcHhyMXjos6xAKs78wzzxw/fnxeZ+T/x+7du08++eS3337b84/NrFatWi7M3O7du/ezzz7Dif/b3/6W09+KRp8+fc4555y8Ol+L7z7yyCPUQwQXzdscgs8//7xo0aI7d+7k/1tuueWKK67Iq5zkQ8yePbtmzZqffvppXmfEwcHBwcHB4chF9nPRPXv2fPXVVx/4WL58uR0a9+eff65evXrx4sULFixYunTpb7/9Zn7av3//999/v2jRonffffejjz7itn379mV73hyyF3379s3Dr//zn/+EC61bty73P33sscfG5KJ0h0GDBmXLR/O2tr1QWd5///1oLprnuPXWW6tUqRL//jVr1kycODHHspPfkY2ymgXMnDkTo5BXX88/WLJkyfz583PizZs2bXr77benTZs2d+5cRF2JGOvff/89zuOY8t9jACufE5k/ePzwww9jxoyxvY6kwD+ZNGlSnpfim2++GT9+/JNPPvnll1/mbU4OHodTWXIZqMQ333wz5s0I7SeffPLGG2+YlJ07d44dO5b6Nyl42gsXLsTTzuaMZh4x+6PDEYJs5qJ//PEHTBJTCqV87733+IfL3bt361c00XwfcFH+coOZyFqxYoX9E1i2bFme2wOHCEAFixUrlocZuOuuu+BCaLTc/3R8Lgoduuyyyw7+i3le216oLPmfi9JGp556asybMdt16tR57LHHcjRL+RnZJatZwMqVK0uUKIEjlSdfzyd4/vnnq1SpQp/q2bNn9r559erVLVu2LFCgQPXq1a+77rq2bdvSLypUqHDVVVeVKVPm66+/jvOSCy64IOHjL3/5y3HHHVe0aFH+5538j2pKZCBPFHIc3HDDDWRv8ODB0bedcsop3PbBBx/kTq6S4v/+7/8eeOAB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qzxVqlSp/fv3P/DAA2nTpl27dq2fB/fu3XvkyJE4ZT8krl69OnDgwIwZM6ZOnXrAgAG//vrr7t27J0+enCdPnrvuuqtWrVq33HJLdN8YRVARZE9q4aeffnLcUnT62sGqVauSOgsGUYDhogYGBgYGBgZJjCtXruiX27ZtM1w0keGogg8//DDhuGjr1q1JfMKECXrgZ599FikXXbFihXCnLl26/PXXXylSpOD/22+/HfbB8+fP33333V9//XXEWQ8NCvDpp58mA2Rj1qxZ+q3Tp08/8cQT3LqWueg///xz2223SXl+8803+q0mTZq88cYbSZWxoJg4cWLJkiWTOhcGUYDhogZxxNWrV5M6C9cQ/v7777g9ePHixd9///3cuXPxz8OpU6fU/7Nnz/7777/xT9M/Tpw4kZivizMwCKKY2uXLlyOqO+ro//7v/6L19iiWeZwFOFJEt/wNkhNeeukl/ZLGZbhoIsNRBcIME4KLXrp0KXXq1CT+448/Om61aNEiIi7arVs34U7du3dHu9apU+fOO+/csGFD2Afr1avHU9Hlou+//75kBtrpvnvmzJl77733Wuailj0fXq5cuYEDB+pd1ejRo/moa4qLrlu3Lm3atIaLJg8YLmoQGb766qsqVaoULly4bNmyRYsWrVat2owZM5I6U0mGNWvWoJ0feOCBRx55JNJn165d27x585EjR9IjpkmT5p133olbHlavXt2uXbuCBQuqfgJ+mz179lKlSsUtwThg6NChdFTz5s1LtDdGiitXrowaNapGjRoUdVQSnDVrVqNGjTJnzuzHlDlw4EDfvn0rVqyI+fXPP/9EJQNRKfP4CHBEiImJwaItUKBAz549E/RFBtcpxowZgzzrIYaLJjLcVZBwXHTTpk3C2Ro0aOAY196yZUuFChX8J9WsWTPFRX0+Astq27atPBVFLrpnz5506dJJso75XoUVK1akT58+Wm9MHHz66aepUqW6prgo8nP77beTJcNFg+LPP/+Eqy9btozfgwcPqnAk/9dff13/X6hB7d9//91xa9++fYmTYcNFDfzi9OnTjRs3zpgx4+eff64Cp02blilTpqpVq96Y0x0XLlxYvnw5CvHhhx+O6MGff/65SJEiMhmFdqBg77rrrjjnYcSIEXo/QddeuXLlli1bxi3BOGDOnDn33HMPmivR3hgHoFXz5MnjMLbi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5rFjxypWrAjz1APR/xBp9OGaNWv08I8++ihDhgxkaf369RIyc+ZMyaSkAP+EofFqQlBBV65cIfDy5csNGjSIlFGXLl2axqgy1rdvX+HzcolWHzp0KCG///47lzIE4MFFadrNmjWLc48GlixZwisOHjzI/02bNsGFfvvtN+9Hhg8fzofr08UffvhhMuaili0A0o1GhYsGTXDfvn3PPPPM7NmzHTEff/zxFi1ayP9OnTq99dZboQKvd7ilKJR4SwOMCPoj8W81Dmzbts1w0RsH0eeiWOpbt25dYWPLli1BjfVdu3bRP+nLUZBjAlevXr106dJffvmFTiUODcMgSfDzzz/Hh4teI3jllVcKFizoPz7mRTLgooL+/ftHhYvS9vv16xeVLCU5evTokdRZMEj+SJkypdCzJ598UgU+++yziqP+9ddfftL55JNPypUrN3DgwDjsGqhXrx4vCstFad2lSpX6/PPP9cDBgwfLPGfQtQ8//PBDihQp6CDkEoYpHwXfVnHo96GyBI4aNUpC+OS8efPu37/f/ycUL1788OHD6tLBRQWwfVkri6r35qLxB6zypptuimcilF7y5qLg4YcfjiIX9Zngjh07iPPuu++GDUwG8ClF586da9u2bUQpT5w4cdmyZfHIWhhcvnzZcNEbB1HmokgPTHLJkiVQSsSUP1xevHhRRaCnpM9YYkPvNX/99VcJpN+SPxDa6ObNIIGQPLhoyZIlCxUq5D9+tWrVkg0XlZnt+HNRjDzdpL5+8dlnn6VPnz6pc2GQ/BGUi7Zr105x0Xnz5iXc2+mCMUDlRWG5aNeuXcuWLauH7NmzR5ZEKhrpBkbwd999J/+lp3BwUcue1SSwRo0aKqRHjx5lypTxz6s7d+6sXwblolOnTt2yZYuVKFz07rvvNlzUD5KEi86YMcNNO4MGJgP4lKIXXnjh8ccf95/shg0bbr755oTYdKpguGh8gI5dt24dLIxfWaAhQKnCttb/FydOnFB30epr166VBxNzd1WUueiBAweQzpUrV/77779I0po1a7iUlTOXLl2KiYnh1pJYqJ7mzJkzQl/5I2UhEUghutkziCeowQ8++ICe/vvvv1eBiotSxQsWLOjTpw9q3fHglStXeGTQoEFDhw51r7/asWPHF198oYcgBsTv16/fe++953b8wK3+/fuPHj3asVrMG6dOneItvXv3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rVql0k+ePDlt2rR+/frNnj37559/jlWeDhw9ejRDhgz6NzJpUzRWDt9///3MmTOfPXtWv4su06pVK/745aK///474u3fv/+KFSviwEWRKsKMjo6mFVB+Oqb6uifYv3//6tWruYDq63PygTpaZGTkmDFjUCR6wb59+xynpkyZQlGXLFnyzz//qHR64owZM/76669Dhw6hVzxxzpw5okXz5s2TaxCapMi7QO7iMtoFjdUjfgH0/9133506dSp96vz586FLw8CyX8GzZs1K7FL4B30/6TiGMHLqA0VCgrGRwTlRHn0rIhFbKnGRlPuygUF4EWYuiuGFEY9NKYdCTbdu3cp/GAL/d+zYIaewRYRwYo3xisI+VqeEmoKgYScNEgxQuE6dOjVq1AhjF8sSwzplypTCRcU3EiscSxrz0bL5CVdyiLEOSXj22WdbtGiRPHly/kAm+W3Xrl2FChW4ALtWPaJr167wEDSB3BSvw07t2LEjh4ULF8bUrlmzZp06dTisXr26uhFz9rHHHvvpp5/QpSeffJJMSNy8eTMXcyUp6kr40iOPPEI+EAas/5w5cz711FO//vqrZXM5ruT6l19+uXXr1k8//TS14xDOJvdCz5555pl69ephH8Mes2XL1q1bN5WzzkXdAkH5e/TowWGzZs0w0Pfu3RsVFUVJSEE+yrKnChBCBwcIhDgI2aMKXJMvX740adLMsyEe8hs2bKhcuTLsCEZHhhEREfRKuV64KCTkoYceatq0abp06aivkD235GGY6dOnJwU2Uq1atRdeeIGseLoea/fzzz8vXrz4kSNHtm3bds8991CRIkWKlC5dOhRRIExKIguYKbyi39Atyr9z505k1b59e0oIJQslQzeQGCXftGmTnog6Zc+enefSNT766KNSpUrRsvoFMGpEIV8H3FyUEa9EiRILFy6E5EMpqXXoXPTvv//u3LlzqlSpuAX9z5s3L3VPliwZgpVvGevWrXv00Uc5S/dp0qQJLJr/DMhWgI5m2R960AHIJHrSu3fvJ554Qj0OubVp02bNmjXIOUuWLHQ3qsYYzmWZMmUiE2pRqFAh/rRs2RKdT5EiBf8VMaa0DRs2pGfxx7KZ8HPPPbds2TL6IELLkycPvU+ufOWVV7p06ULmMNt7770XXYpFI93eWLt2LZ0Rsd93332JXRYnaPEaNWqgn6lTp07sslj0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dCm6i/Avbt++feXKleguRVTjwal/Fw87rl27Nnr06AMHDkR3QR4sHD16dPbs2dFdinv4+++/v/nmm8OHD0fxcy9cuDB9+nT+P2KPu3nz5tKlS/fv3++QZsuWLZMnT/7nn39UDL+3bt3KjZFdvEcP9sqMXhw5cmTq1Kl6DD197dq1eszJkycnTJjw4JTZRdTA5aIuHkEMHjzY4/EsWrQougsSENq0aVPGEVWqVDl16lT37t0LFy5cqlSp6C6vMWfOnAYNGiRJkuTbb7+N7rJEEXbs2NG2bduMGTN27do1usvi4hHBV199hZoqV65cdBfkQcGPP/5YsmRJ6uS5556L3pIcOnSocePGTz31FIVZuXJllD33hx9+qF69+hNPPMFzDx48+Mg8DmrxySefJEyYkAdB7x1Spk+fnjQbN27k961bt0JCQlKlSkVM/fr1I694jyr0yoxeQEELFixIYVKnTq0ioabExI0bl4YmCCktW7asfIz99u3b0VdYF9EAl4u6eASxYMGC3Llzb9u2LboLEhDy589funTpFStW7NmzB4NALIPVq1f/9ttv2AoNGzbEJEI1r1+/nviXX345ust7bx69Xr16FObx4aJXr17t06cPr+xyURfBwrFjx2rUqDF37txoefqdO3cekPz1lCi9yOOiYX1lsYyjkouCu3fvpkyZMmq4aBQ/7s033/TLRYcOHVq3bl19x82XX34ZLC4adJmP7E4UQdgr04i+MkvX1rkostekSRN9SL1x40a8ePFcLvoYIvhc9ObNm5jUG03s3r37+vXr6hJytnfvXuLXrVv3008/nThxQi3E8+PIkSObN2/m0i+//HLmzJmgF8zFIwzsuR07dkR3KcKJwoULX7x4UQUts9Toa3i1jB9cehC4KPjiiy+ihouiT3r27BnZTwkEP/zwQ3Rx0YdavF08gMA8bdWqVaQ+olGjRoEkw0gYMGCACv7vf/+LJC46ceJErIsw3QL/iXouCooXLx5lXDQqH/fuu+/65aJ2UP9B4aIWSQsKAhTyBwrRVWbopYWLegUJXC76GCLIXBQB+vHHH9euXfv999+j9/lBEApqmCY1VHOtCaw6+aHUH/TVcunUqVPBLZuLRxX79u1LmDDh1q1bo7sg4UTfvn31oH3HFMTv2rVrxmPJRTFfKlWqFNlPCQTRxUUfdvF28QDizTffjFRNMmrU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
```

---
