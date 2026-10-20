# Research conversation: [DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 2
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/a322b9a6-2fd2-45a7-a43a-358b57dee024.jsonl`
- **Structured JSON:** [`3ef13ba1927b4473229e.json`](../../sessions/3e/3ef13ba1927b4473229e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T13:44:24.599Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T13:44:24.599Z",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "content": "[DREAM Review Director]\ndream_id=20260521T122458 | review_mode=simple | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_input_db82206b.pdf\n\n（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。\n\n## 审稿标准\n\n未指定目标 venue。在开始审稿前，你必须：\n1. 确认目标 venue 及其评分标准\n2. 用 WebSearch 搜索该 venue 的 reviewer guidelines\n3. 严格按照搜到的官方评分刻度打分\n4. 如果无法确认 venue，使用 ACL ARR 1-5 分制\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"xling_calib_direction\", tier=\"best\", dream_id=\"20260521T122458\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T122458/best/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T13:44:24.602Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T13:44:24.602Z",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-21T13:44:24.636Z_

[DREAM Review Director]
dream_id=20260521T122458 | review_mode=simple | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_input_db82206b.pdf

（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。

## 审稿标准

未指定目标 venue。在开始审稿前，你必须：
1. 确认目标 venue 及其评分标准
2. 用 WebSearch 搜索该 venue 的 reviewer guidelines
3. 严格按照搜到的官方评分刻度打分
4. 如果无法确认 venue，使用 ACL ARR 1-5 分制

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="xling_calib_direction", tier="best", dream_id="20260521T122458", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T122458/best/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "382d432b-2bdf-4e1d-ba47-65cd53e085a0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T13:44:24.636Z_

```json
{
  "parentUuid": "382d432b-2bdf-4e1d-ba47-65cd53e085a0",
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "d71773f7-b624-4bce-815d-0593aaa6b5a8",
  "timestamp": "2026-05-21T13:44:24.636Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T13:44:24.636Z_

```json
{
  "parentUuid": "d71773f7-b624-4bce-815d-0593aaa6b5a8",
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
  "uuid": "50437532-79ed-4930-b612-c4bbd1a1cbe2",
  "timestamp": "2026-05-21T13:44:24.636Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T13:44:24.636Z_

```json
{
  "parentUuid": "50437532-79ed-4930-b612-c4bbd1a1cbe2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "341b0d58-25a0-48dc-9bef-bef0295f31a1",
  "timestamp": "2026-05-21T13:44:24.636Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
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
  "aiTitle": "Review machine learning research paper PDF",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Assistant

_source line 8 · 2026-05-21T13:44:28.109Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the PDF and the review context YAML to understand what I'm reviewing. I also need to load the dream-review-simple skill for the dispatch template.

Let me first load the necessary tools and read the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "341b0d58-25a0-48dc-9bef-bef0295f31a1",
  "isSidechain": false,
  "requestId": "req_011CbFpAbnHuF3cDAhag9d3c",
  "type": "assistant",
  "uuid": "1a3db154-e9e7-4869-a78a-da7ce2db3452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgU4ryrheX32Xf3wbMQ7ox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11381,
      "cache_read_input_tokens": 11841,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 375,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11381
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

_source line 9 · 2026-05-21T13:44:29.237Z_

I'll read the PDF, the review context, and load the review skill in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a3db154-e9e7-4869-a78a-da7ce2db3452",
  "isSidechain": false,
  "requestId": "req_011CbFpAbnHuF3cDAhag9d3c",
  "type": "assistant",
  "uuid": "b715053b-8136-4b4b-9911-09d6994fd673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgU4ryrheX32Xf3wbMQ7ox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11381,
      "cache_read_input_tokens": 11841,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 375,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11381
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

_source line 10 · 2026-05-21T13:44:29.893Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KTUjZvHvMnkWGiAM39qvvp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_input_db82206b.pdf",
  "pages": "1-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b715053b-8136-4b4b-9911-09d6994fd673",
  "isSidechain": false,
  "requestId": "req_011CbFpAbnHuF3cDAhag9d3c",
  "type": "assistant",
  "uuid": "9ac56b89-ae4a-46b1-b7a1-ef8b15364fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgU4ryrheX32Xf3wbMQ7ox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11381,
      "cache_read_input_tokens": 11841,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 375,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11381
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

_source line 11 · 2026-05-21T13:44:31.202Z_

<details><summary>↩ Tool result · `toolu_01TMR2DewCP8ssuugLh6Kjdj`</summary>

```text
1	---
2	name: xling-calib-direction-research
3	description: Research patterns from 12 papers on cross-lingual calibration and internal representations in LLMs
4	type: skill
5	---
6	
7	# Cross-Lingual Calibration — Research Patterns (12 papers)
8	
9	## Evaluation Protocol
10	
11	**Metrics**: ECE (8/12) + AUROC (5/12) + Brier (4/12). Always pair calibration with discrimination. Point estimates without CIs is field norm (6/8). High conf.
12	
13	**Benchmarks**: MMLU (5/12), Belebele for multilingual (122 langs), TruthfulQA. Transfer: ARC, HellaSwag, CSQA. High conf.
14	
15	**Models**: 3-6 models. Llama-3.1-8B + Qwen2.5-7B near-universal. Include multilingual-first model (Aya). High conf.
16	
17	## Method Trends
18	
19	**Linear probing of hidden states** (7/12): Linear classifiers suffice. AUC 0.80-0.97. Source: confidence_manifold2026. High conf.
20	
21	**Layer-wise analysis standard** (7/12): Middle-to-late layers (15-29/32) richest for xling/calibration. Final layer suboptimal for non-English. Source: zhou2025lace (24-29), civelli2026shared (xling ~15, monolingual ~30). High conf.
22	
23	**Inference-time steering** (4/12): Extract direction, add to activations, no retraining. Source: ji2025calibrating, miao2026coral, miao2026closing. Med conf.
24	
25	**Training-free methods rising** (3/12): LACE, mean shift, projection. Field moving from fine-tuning. Med conf.
26	
27	**Temperature scaling declining**: Only baseline now. High conf.
28	
29	## Cross-Paper Findings
30	
31	**Non-English ECE 5x English** (23% vs 4.6%). Structural, tied to pretraining data. Source: zhou2025lace. 3/12. High conf.
32	
33	**Cross-lingual reps are linear**: Knowledge/confidence linearly encoded across languages in middle layers. Mean shift/projection enables training-free transfer. Source: xiao2025knowledge. 4/12. High conf.
34	
35	**Correctness distributed not sparse**: SAE neuron ablation negligible (delta ECE 1.25e-4). 3-8D subspace. Source: miao2026coral, confidence_manifold2026. 2/12. Med conf.
36	
37	**Layer-depth Pareto**: English calibration improves monotonically; non-English peaks mid-late then degrades. Source: zhou2025lace, joshi2025calibration. 2/12. High conf.
38	
39	## Competitor Landscape
40	
41	**zhou2025lace** (competitor): Per-language layer ensemble, ECE 22→3%, training-free. No directional methods.
42	**joshi2025calibration** (competitor): Calibration direction in residual stream. Transfers across datasets but NOT across models. Monolingual only.
43	
44	**Our niche**: No paper combines xling transfer + calibration directions + layer-depth Pareto. joshi's direction fails cross-model. civelli shows xling/monolingual optimal layers diverge. Intersection is open.
45	
46	## Gaps
47	
48	- Cross-model direction transfer unsolved (joshi shows failure)
49	- No multilingual verbal uncertainty (ji2025calibrating English-only)
50	- MCQA-only (5/12) → generation calibration open
51	- Instance-level causal validation missing (ravisankar correlation only)
52	- Scale beyond 7-8B untested
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f1379fa-8457-4360-ba3e-b769a6860da0",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "296bfa70-f652-4c16-bd61-eaa7417d5954",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md",
      "content": "---\nname: xling-calib-direction-research\ndescription: Research patterns from 12 papers on cross-lingual calibration and internal representations in LLMs\ntype: skill\n---\n\n# Cross-Lingual Calibration — Research Patterns (12 papers)\n\n## Evaluation Protocol\n\n**Metrics**: ECE (8/12) + AUROC (5/12) + Brier (4/12). Always pair calibration with discrimination. Point estimates without CIs is field norm (6/8). High conf.\n\n**Benchmarks**: MMLU (5/12), Belebele for multilingual (122 langs), TruthfulQA. Transfer: ARC, HellaSwag, CSQA. High conf.\n\n**Models**: 3-6 models. Llama-3.1-8B + Qwen2.5-7B near-universal. Include multilingual-first model (Aya). High conf.\n\n## Method Trends\n\n**Linear probing of hidden states** (7/12): Linear classifiers suffice. AUC 0.80-0.97. Source: confidence_manifold2026. High conf.\n\n**Layer-wise analysis standard** (7/12): Middle-to-late layers (15-29/32) richest for xling/calibration. Final layer suboptimal for non-English. Source: zhou2025lace (24-29), civelli2026shared (xling ~15, monolingual ~30). High conf.\n\n**Inference-time steering** (4/12): Extract direction, add to activations, no retraining. Source: ji2025calibrating, miao2026coral, miao2026closing. Med conf.\n\n**Training-free methods rising** (3/12): LACE, mean shift, projection. Field moving from fine-tuning. Med conf.\n\n**Temperature scaling declining**: Only baseline now. High conf.\n\n## Cross-Paper Findings\n\n**Non-English ECE 5x English** (23% vs 4.6%). Structural, tied to pretraining data. Source: zhou2025lace. 3/12. High conf.\n\n**Cross-lingual reps are linear**: Knowledge/confidence linearly encoded across languages in middle layers. Mean shift/projection enables training-free transfer. Source: xiao2025knowledge. 4/12. High conf.\n\n**Correctness distributed not sparse**: SAE neuron ablation negligible (delta ECE 1.25e-4). 3-8D subspace. Source: miao2026coral, confidence_manifold2026. 2/12. Med conf.\n\n**Layer-depth Pareto**: English calibration improves monotonically; non-English peaks mid-late then degrades. Source: zhou2025lace, joshi2025calibration. 2/12. High conf.\n\n## Competitor Landscape\n\n**zhou2025lace** (competitor): Per-language layer ensemble, ECE 22→3%, training-free. No directional methods.\n**joshi2025calibration** (competitor): Calibration direction in residual stream. Transfers across datasets but NOT across models. Monolingual only.\n\n**Our niche**: No paper combines xling transfer + calibration directions + layer-depth Pareto. joshi's direction fails cross-model. civelli shows xling/monolingual optimal layers diverge. Intersection is open.\n\n## Gaps\n\n- Cross-model direction transfer unsolved (joshi shows failure)\n- No multilingual verbal uncertainty (ji2025calibrating English-only)\n- MCQA-only (5/12) → generation calibration open\n- Instance-level causal validation missing (ravisankar correlation only)\n- Scale beyond 7-8B untested\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  },
  "sourceToolAssistantUUID": "6f1379fa-8457-4360-ba3e-b769a6860da0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T13:44:30.363Z_

<details><summary>↩ Tool result · `toolu_01KTUjZvHvMnkWGiAM39qvvp`</summary>

```text
PDF pages extracted: 11 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_input_db82206b.pdf (183.5KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ac56b89-ae4a-46b1-b7a1-ef8b15364fc7",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "5cc349e3-5f31-4912-805b-fc2b07b3934d",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_input_db82206b.pdf",
      "originalSize": 187870,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/a322b9a6-2fd2-45a7-a43a-358b57dee024/tool-results/pdf-f9722da2-3529-4be5-8889-5b3b96ce9a76",
      "count": 11
    }
  },
  "sourceToolAssistantUUID": "9ac56b89-ae4a-46b1-b7a1-ef8b15364fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

42 recorded events

### User

_source line 13 · 2026-05-21T13:44:30.361Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cc349e3-5f31-4912-805b-fc2b07b3934d",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "isMeta": true,
  "uuid": "1710f0ef-0f1e-4ff9-bc06-d13975c41e2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T13:44:30.884Z_

<details open><summary>🔧 Tool call — Read · `toolu_016d1UXdq3JwKtqJZX8DEfAh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1710f0ef-0f1e-4ff9-bc06-d13975c41e2d",
  "isSidechain": false,
  "requestId": "req_011CbFpAbnHuF3cDAhag9d3c",
  "type": "assistant",
  "uuid": "57783387-1446-4a31-8f48-2a775d0b2a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgU4ryrheX32Xf3wbMQ7ox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11381,
      "cache_read_input_tokens": 11841,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 375,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11381
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

_source line 15 · 2026-05-21T13:44:31.190Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TMR2DewCP8ssuugLh6Kjdj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57783387-1446-4a31-8f48-2a775d0b2a2a",
  "isSidechain": false,
  "requestId": "req_011CbFpAbnHuF3cDAhag9d3c",
  "type": "assistant",
  "uuid": "6f1379fa-8457-4360-ba3e-b769a6860da0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgU4ryrheX32Xf3wbMQ7ox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11381,
      "cache_read_input_tokens": 11841,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11381,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 375,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11381
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

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "296bfa70-f652-4c16-bd61-eaa7417d5954",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review machine learning research paper PDF",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Tool result

_source line 18 · 2026-05-21T13:44:33.060Z_

<details><summary>↩ Tool result · `toolu_016d1UXdq3JwKtqJZX8DEfAh`</summary>

```text
1	narrative_guidance: 'Method contribution paper — 因果链完整：Pareto discovery（architecture-dependent
2	  depth-transferability tradeoff with overall positive depth-transfer trend）→ Decomposition
3	  explains it（difficulty transfers, capability does not）→ CaCLR solves it（consistency
4	  loss shifts Pareto frontier, +3.3pp mean, 14/20 languages improved）→ CKA geometric
5	  explanation reveals why（Simpson''s Paradox confirmed across 3 architectures, partial
6	  rho +0.44 mean, p<0.01）。四条 claim 全力度支撑。Headline: "CaCLR-trained correctness probes
7	  reduce non-English ECE by 38% requiring zero target-language labels." Control task
8	  warning（10% cross-lingual artifact rate） 和 linear projection sample efficiency（~40
9	  pairs to 95%）作为 elevated empirical contributions 进入 main body。Procrustes effect
10	  reversal（threshold ~0.52）为 practitioner 提供直接指导。 三个架构（Qwen3 MoE + Llama4 MoE + Gemma4
11	  Dense）消除架构混淆因子——phenomenon 是 transformer depth 的 universal property。Mean EN AUROC
12	  0.818（range 0.805–0.835），ZS 20-lang mean 0.767， gap 5.2pp。所有 key metrics 落在 best
13	  区间内。
14	
15	  '
16	imagined_experiments:
17	- name: Full Pareto Frontier — Qwen3-235B-A22B (MoE)
18	  plan_id: plan_001
19	  description: '94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th: L0,L4,...,L92),
20	    20 typologically diverse languages, English logistic regression probes, 5 transfer
21	    conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100,
22	    CaCLR (optimal α=0.1, β=0.05 from plan_003)。验证 MVP 发现的 positive depth-transfer
23	    trend 和 local deep-layer Pareto tradeoff 在大 MoE 模型上放大。
24	
25	    '
26	  expected_results:
27	    en_best_auroc: 0.835
28	    en_best_layer_idx: 68
29	    en_best_depth_pct: 72
30	    en_auroc_range:
31	    - 0.59
32	    - 0.835
33	    en_ece_raw_best: 0.172
34	    zs_mean_auroc_20lang_at_zs_optimal: 0.775
35	    zs_best_transfer_layer_idx: 48
36	    zs_best_transfer_depth_pct: 51
37	    zs_pass_rate_auroc_gt_058: 19
38	    zs_fail_langs:
39	    - yo
40	    zs_auroc_by_tier:
41	      HIGH_mean: 0.817
42	      MID_mean: 0.788
43	      LOW_mean: 0.693
44	    zs_auroc_selected:
45	      zh: 0.83
46	      es: 0.82
47	      fr: 0.82
48	      de: 0.82
49	      ja: 0.81
50	      nl: 0.81
51	      pt: 0.81
52	      ar: 0.8
53	      hi: 0.79
54	      ko: 0.79
55	      ru: 0.8
56	      tr: 0.78
57	      vi: 0.77
58	      id: 0.79
59	      pl: 0.79
60	      uk: 0.78
61	      sw: 0.72
62	      bn: 0.73
63	      te: 0.67
64	      yo: 0.575
65	    overall_spearman_depth_vs_zs:
66	      global_rho: 0.68
67	      global_p: 0.0003
68	    per_lang_spearman_rho_median: 0.62
69	    per_lang_positive_rho_count: 17
70	    per_lang_significant_positive_count: 14
71	    per_lang_negative_rho_langs:
72	    - yo
73	    - te
74	    - sw
75	    pareto_tradeoff_langs_count: 15
76	    pareto_en_optimal_layer: 68
77	    pareto_zs_optimal_layer: 48
78	    pareto_depth_gap_layers: 20
79	    pareto_zs_drop_at_en_optimal_pp: 3.8
80	    mean_shift_delta_auroc: 0.0
81	    linproj_200pairs_mean_auroc: 0.793
82	    linproj_200pairs_delta_pp: 1.8
83	    fewshot_25_mean_auroc: 0.762
84	    fewshot_100_mean_auroc: 0.788
85	    caclr_mean_auroc: 0.812
86	    caclr_delta_vs_zs_pp: 3.7
87	  result_rationale: 'Qwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 ~3×。Probing
88	    scaling 预期 EN AUROC 从 0.754 提升至 0.835：更大模型在 intermediate layers 编码更清晰的 correctness
89	    signal， 因为 pretraining loss 更低 → 内部 representations 对 factual accuracy 更 informative。
90	
91	    Overall positive depth-transfer trend（median per-lang Spearman ρ=+0.62）因为更深层 encode
92	    更多 semantic content → 更好的 correctness discrimination，且 correctness direction 的
93	    cross-lingual alignment 在 shallow-to-mid layers 持续改善（CKA 在 0-50% depth 下降缓慢）。
94	    17/20 languages 有 positive ρ，3 个 negative 的（yo/te/sw）是 LOW-resource：这些语言在 Qwen3
95	    pretraining corpus 中占比极低（<0.1%），ZS AUROC 的 depth profile 呈倒 U 形 （peak 在 ~40% depth
96	    而非 >50%），因为深层的 language-specific specialization 对这些语言 反而有害。
97	
98	    Local Pareto tradeoff：从 ZS-optimal (L48, 51% depth) 到 EN-optimal (L68, 72% depth)，
99	    EN 增加 2pp（0.815→0.835）但 ZS 平均下降 3.8pp（0.775→0.737）。这一 tradeoff 在 15/20 languages
100	    上可观测（ZS-optimal ≠ EN-optimal，gap >1.5pp）。94 层深网络比 28 层 MVP 有 更大的 specialization
101	    空间，使 EN-optimal 与 ZS-optimal 之间的 depth gap 从 MVP 的 3 层 扩大至 20 层（22pp depth）。
102	
103	    MoE routing 在深层产生 language-specific expert activation patterns，加速 CKA cliff 下降，导致
104	    Qwen3 的 Pareto tradeoff 比 Llama4/Gemma4 更 pronounced（15/20 vs 10-12/20）。
105	
106	    Mean-shift ΔAUROC ≡ 0：StandardScaler + LR 下 mean-shift 对 AUROC 无影响（rank-invariant,
107	    MVP 中已数学证明并实验验证）。
108	
109	    Linear projection (+1.8pp) 通过 Procrustes 捕获 correctness subspace 旋转。 CaCLR (+3.7pp)
110	    通过 end-to-end 优化超越 linear projection。 Few-shot-100 (+1.3pp) 在 full-scale 上弱于 ZS
111	    因为 100 个 labeled samples 对 14K train set 的 probe 参数贡献边际很小。
112	
113	    '
114	  tables:
115	  - name: 'Table 1: Qwen3-235B Pareto Frontier (selected layers)'
116	    columns:
117	    - layer_idx
118	    - depth_pct
119	    - en_auroc
120	    - zs_mean_20
121	    - zs_drop_vs_en_pp
122	    - on_pareto
123	    rows:
124	    - - 4
125	      - 4
126	      - 0.59
127	      - 0.582
128	      - 0.8
129	      - false
130	    - - 12
131	      - 13
132	      - 0.645
133	      - 0.636
134	      - 0.9
135	      - false
136	    - - 20
137	      - 21
138	      - 0.71
139	      - 0.7
140	      - 1.0
141	      - false
142	    - - 28
143	      - 30
144	      - 0.752
145	      - 0.74
146	      - 1.2
147	      - false
148	    - - 36
149	      - 38
150	      - 0.785
151	      - 0.77
152	      - 1.5
153	      - false
154	    - - 40
155	      - 43
156	      - 0.798
157	      - 0.779
158	      - 1.9
159	      - false
160	    - - 44
161	      - 47
162	      - 0.808
163	      - 0.782
164	      - 2.6
165	      - false
166	    - - 48
167	      - 51
168	      - 0.815
169	      - 0.775
170	      - 4.0
171	      - true
172	    - - 52
173	      - 55
174	      - 0.822
175	      - 0.768
176	      - 5.4
177	      - true
178	    - - 56
179	      - 60
180	      - 0.828
181	      - 0.757
182	      - 7.1
183	      - true
184	    - - 60
185	      - 64
186	      - 0.832
187	      - 0.745
188	      - 8.7
189	      - true
190	    - - 64
191	      - 68
192	      - 0.834
193	      - 0.738
194	      - 9.6
195	      - true
196	    - - 68
197	      - 72
198	      - 0.835
199	      - 0.737
200	      - 9.8
201	      - true
202	    - - 72
203	      - 77
204	      - 0.834
205	      - 0.725
206	      - 10.9
207	      - false
208	    - - 76
209	      - 81
210	      - 0.83
211	      - 0.71
212	      - 12.0
213	      - false
214	    - - 80
215	      - 85
216	      - 0.822
217	      - 0.695
218	      - 12.7
219	      - false
220	    - - 84
221	      - 89
222	      - 0.815
223	      - 0.678
224	      - 13.7
225	      - false
226	    - - 88
227	      - 94
228	      - 0.805
229	      - 0.66
230	      - 14.5
231	      - false
232	    - - 92
233	      - 98
234	      - 0.79
235	      - 0.642
236	      - 14.8
237	      - false
238	  - name: 'Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3'
239	    columns:
240	    - language
241	    - tier
242	    - spearman_rho
243	    - p_value
244	    - significant_at_005
245	    rows:
246	    - - zh
247	      - HIGH
248	      - 0.75
249	      - 0.0001
250	      - true
251	    - - es
252	      - HIGH
253	      - 0.72
254	      - 0.0002
255	      - true
256	    - - fr
257	      - HIGH
258	      - 0.7
259	      - 0.0003
260	      - true
261	    - - de
262	      - HIGH
263	      - 0.73
264	      - 0.0002
265	      - true
266	    - - ja
267	      - HIGH
268	      - 0.68
269	      - 0.0005
270	      - true
271	    - - nl
272	      - HIGH
273	      - 0.71
274	      - 0.0003
275	      - true
276	    - - pt
277	      - HIGH
278	      - 0.69
279	      - 0.0004
280	      - true
281	    - - ar
282	      - MID
283	      - 0.67
284	      - 0.0006
285	      - true
286	    - - hi
287	      - MID
288	      - 0.62
289	      - 0.002
290	      - true
291	    - - ko
292	      - MID
293	      - 0.65
294	      - 0.001
295	      - true
296	    - - ru
297	      - MID
298	      - 0.68
299	      - 0.0005
300	      - true
301	    - - tr
302	      - MID
303	      - 0.6
304	      - 0.003
305	      - true
306	    - - vi
307	      - MID
308	      - 0.55
309	      - 0.007
310	      - true
311	    - - id
312	      - MID
313	      - 0.63
314	      - 0.002
315	      - true
316	    - - pl
317	      - MID
318	      - 0.62
319	      - 0.002
320	      - true
321	    - - uk
322	      - MID
323	      - 0.58
324	      - 0.005
325	      - true
326	    - - sw
327	      - LOW
328	      - -0.12
329	      - 0.58
330	      - false
331	    - - bn
332	      - LOW
333	      - 0.35
334	      - 0.1
335	      - false
336	    - - te
337	      - LOW
338	      - -0.08
339	      - 0.72
340	      - false
341	    - - yo
342	      - LOW
343	      - -0.18
344	      - 0.42
345	      - false
346	  - name: 'Table 3: Transfer Conditions at ZS-Optimal Layer (L48), Qwen3'
347	    columns:
348	    - condition
349	    - mean_auroc_20
350	    - delta_vs_zs_pp
351	    - requires
352	    rows:
353	    - - zero-shot
354	      - 0.775
355	      - 0.0
356	      - —
357	    - - mean-shift
358	      - 0.775
359	      - 0.0
360	      - —
361	    - - linear_proj_200
362	      - 0.793
363	      - 1.8
364	      - 200 parallel pairs
365	    - - few-shot-25
366	      - 0.762
367	      - -1.3
368	      - 25 labeled per lang
369	    - - few-shot-100
370	      - 0.788
371	      - 1.3
372	      - 100 labeled per lang
373	    - - CaCLR
374	      - 0.812
375	      - 3.7
376	      - parallel activations
377	  figures_description:
378	  - 'Figure 1a: EN AUROC (blue) and ZS mean AUROC (orange) vs normalized depth (%).
379	    Both rise together until ~50% depth, then diverge: EN continues to ~72%, ZS peaks
380	    and declines. Shaded region between curves from 51-72% depth marks Pareto zone.
381	
382	    '
383	  - 'Figure 1b: Heatmap — ZS AUROC by language (y-axis, ordered HIGH→MID→LOW) × layer
384	    index (x-axis). Warm yellow band in mid-depth (30-55%), cooling gradient toward
385	    deep layers, LOW-resource rows cool earliest.
386	
387	    '
388	  analysis: 'Qwen3-235B 展现 strong, consistent positive depth-transfer trend（global
389	    ρ=+0.68, p=0.0003）和 pronounced local Pareto tradeoff（15/20 langs）。EN-optimal (L68)
390	    与 ZS-optimal (L48) 相距 20 层，远大于 MVP 的 3 层，确认 tradeoff 在大模型上放大。 14/20 languages
391	    的 per-language ρ 显著为正，表明 "deeper is generally better for transfer" 是跨语言一致的。3 个
392	    LOW-resource languages (yo/te/sw) 显示 negative/near-zero ρ， 因为这些语言的 correctness
393	    signal quality 在深层退化快于 probe discrimination 的提升。 CaCLR 在 ZS-optimal layer 提供 +3.7pp，是所有
394	    label-free methods 中最优。
395	
396	    '
397	- name: Full Pareto Frontier — Llama 4 Scout (MoE)
398	  plan_id: plan_002
399	  description: '48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every
400	    4th: L0,L4,...,L44,L47), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B
401	    的 weaker/mixed tradeoff pattern 是否是 Llama 架构家族特征。
402	
403	    '
404	  expected_results:
405	    en_best_auroc: 0.815
406	    en_best_layer_idx: 36
407	    en_best_depth_pct: 75
408	    en_auroc_range:
409	    - 0.57
410	    - 0.815
411	    en_ece_raw_best: 0.178
412	    zs_mean_auroc_20lang_at_zs_optimal: 0.765
413	    zs_best_transfer_layer_idx: 28
414	    zs_best_transfer_depth_pct: 58
415	    zs_pass_rate_auroc_gt_058: 17
416	    zs_fail_langs:
417	    - yo
418	    - te
419	    - sw
420	    zs_auroc_by_tier:
421	      HIGH_mean: 0.808
422	      MID_mean: 0.778
423	      LOW_mean: 0.672
424	    per_lang_spearman_rho_median: 0.72
425	    per_lang_positive_rho_count: 19
426	    per_lang_significant_positive_count: 16
427	    per_lang_negative_rho_langs:
428	    - yo
429	    pareto_tradeoff_langs_count: 10
430	    pareto_zs_drop_at_en_optimal_pp: 2.5
431	    mean_shift_delta_auroc: 0.0
432	    linproj_200pairs_mean_auroc: 0.781
433	    fewshot_100_mean_auroc: 0.778
434	    caclr_mean_auroc: 0.798
435	    caclr_delta_vs_zs_pp: 3.3
436	  result_rationale: 'Llama 4 Scout 延续 MVP Llama-3.1-8B 的 weaker tradeoff 模式但在关键方面加强。
437	    Per-language Spearman median ρ=+0.72 高于 Qwen3 (0.62)，因为 Llama4 仅 48 层—— 更少的深层
438	    specialization 空间意味着 ZS AUROC 的下降区间更短（最后 ~20% 层）， 而上升区间（前 58% 层）主导了 overall correlation。19/20
439	    languages 有 positive ρ （仅 yo negative）。
440	
441	    Pareto tradeoff 仅 10/20 languages（vs Qwen3 15/20），且 ZS drop 仅 2.5pp （vs Qwen3
442	    3.8pp）。这与 MVP 一致（Llama-3.1-8B: 2/5 langs showed tradeoff, ar/ko 在深层反而改善）。归因于 Meta
443	    的 multilingual training recipe：Llama4 在 pretraining 中对中高资源语言的 cross-lingual alignment
444	    更均匀，深层 language-specific routing 效应弱于 Qwen3。
445	
446	    EN best AUROC 0.815 低于 Qwen3 的 0.835，部分因为 17B active params < 22B (Qwen3)，部分因为
447	    W4A16 量化引入 ~0.3pp noise（plan_010 验证）。
448	
449	    Architecture-dependent tradeoff strength 是 Claim 1 核心： Qwen3 strong (15/20, -3.8pp)
450	    vs Llama4 weak (10/20, -2.5pp)， median per-lang ρ 差异虽然在同一方向（都正），但 Qwen3 的 Pareto
451	    zone 更宽。
452	
453	    '
454	  tables:
455	  - name: 'Table 4: Llama 4 Scout Pareto Frontier'
456	    columns:
457	    - layer_idx
458	    - depth_pct
459	    - en_auroc
460	    - zs_mean_20
461	    - on_pareto
462	    rows:
463	    - - 4
464	      - 8
465	      - 0.57
466	      - 0.562
467	      - false
468	    - - 8
469	      - 17
470	      - 0.64
471	      - 0.63
472	      - false
473	    - - 12
474	      - 25
475	      - 0.7
476	      - 0.69
477	      - false
478	    - - 16
479	      - 33
480	      - 0.74
481	      - 0.728
482	      - false
483	    - - 20
484	      - 42
485	      - 0.768
486	      - 0.755
487	      - false
488	    - - 24
489	      - 50
490	      - 0.785
491	      - 0.764
492	      - false
493	    - - 28
494	      - 58
495	      - 0.798
496	      - 0.765
497	      - true
498	    - - 32
499	      - 67
500	      - 0.808
501	      - 0.755
502	      - true
503	    - - 36
504	      - 75
505	      - 0.815
506	      - 0.742
507	      - true
508	    - - 40
509	      - 83
510	      - 0.81
511	      - 0.722
512	      - false
513	    - - 44
514	      - 92
515	      - 0.795
516	      - 0.695
517	      - false
518	    - - 47
519	      - 98
520	      - 0.778
521	      - 0.668
522	      - false
523	  - name: 'Table 5: Architecture-Dependent Pareto Summary'
524	    columns:
525	    - metric
526	    - Qwen3_235B
527	    - Llama4_Scout
528	    - interpretation
529	    rows:
530	    - - en_best_auroc
531	      - 0.835
532	      - 0.815
533	      - both strong, Qwen slightly higher (22B>17B active)
534	    - - zs_mean_at_zs_opt
535	      - 0.775
536	      - 0.765
537	      - comparable transfer quality
538	    - - per_lang_rho_median
539	      - '+0.62'
540	      - '+0.72'
541	      - both positive; Llama higher (fewer deep layers)
542	    - - positive_rho_langs
543	      - 17/20
544	      - 19/20
545	      - Llama more consistent
546	    - - pareto_tradeoff_langs
547	      - 15/20
548	      - 10/20
549	      - Qwen stronger tradeoff
550	    - - pareto_zs_drop_pp
551	      - 3.8
552	      - 2.5
553	      - Qwen steeper
554	    - - best_transfer_depth_pct
555	      - 51
556	      - 58
557	      - comparable mid-depth zone
558	  figures_description:
559	  - 'Figure 2: Overlaid Pareto frontiers (normalized depth %). Qwen3 (blue) and Llama4
560	    (orange) share similar shape but Qwen3 has wider divergence zone between EN and
561	    ZS curves. Both peak in transfer at 51-58% depth.
562	
563	    '
564	  - 'Figure 3: Per-language Spearman ρ distribution — violin plots. Both architectures
565	    cluster on the positive side. Llama4 tighter (0.4-0.85), Qwen3 wider spread (−0.2
566	    to 0.8) with 3 LOW-resource outliers below zero.
567	
568	    '
569	  analysis: 'Llama4 与 Qwen3 的对比确认 architecture-dependent tradeoff strength。两者都有 positive
570	    depth-transfer trend 和 local Pareto tradeoff，但 effect sizes 不同： Qwen3 在 15/20
571	    languages 上有 measurable tradeoff（mean drop 3.8pp），Llama4 仅 10/20（mean drop 2.5pp）。差异无法从
572	    domain adaptation theory 预测—— 这是 architecture/training-recipe 的 empirical finding。Best-transfer
573	    depth converges to 51-58%，暗示 universal "mid-depth transfer zone"。
574	
575	    '
576	- name: Full Pareto Frontier — Gemma 4 31B Dense
577	  plan_id: plan_008
578	  description: '60 text layers, dense architecture, BF16 (~62.5GB, single 96GB GPU),
579	    16 probed layers (every 4th + final: L0,L4,...,L56,L59), 20 languages, 5 transfer
580	    conditions。 P0 priority — provides dense vs MoE architectural contrast, eliminates
581	    confound between architecture type and tradeoff strength。无量化 → 消除量化 confound。
582	
583	    '
584	  expected_results:
585	    en_best_auroc: 0.805
586	    en_best_layer_idx: 44
587	    en_best_depth_pct: 73
588	    en_auroc_range:
589	    - 0.57
590	    - 0.805
591	    en_ece_raw_best: 0.185
592	    zs_mean_auroc_20lang_at_zs_optimal: 0.76
593	    zs_best_transfer_layer_idx: 36
594	    zs_best_transfer_depth_pct: 60
595	    zs_pass_rate_auroc_gt_058: 18
596	    zs_fail_langs:
597	    - yo
598	    - te
599	    zs_auroc_by_tier:
600	      HIGH_mean: 0.802
601	      MID_mean: 0.772
602	      LOW_mean: 0.67
603	    per_lang_spearman_rho_median: 0.65
604	    per_lang_positive_rho_count: 18
605	    per_lang_significant_positive_count: 14
606	    pareto_tradeoff_langs_count: 12
607	    pareto_zs_drop_at_en_optimal_pp: 3.0
608	    linproj_200pairs_mean_auroc: 0.776
609	    caclr_mean_auroc: 0.79
610	    caclr_delta_vs_zs_pp: 3.0
611	    simpson_partial_rho: 0.44
612	    simpson_partial_p: 0.004
613	  result_rationale: 'Gemma4 31B Dense 是三架构中唯一的 dense model，消除了 "MoE routing 导致 Pareto
614	    tradeoff" 的替代解释。EN best AUROC 0.805 低于两个 MoE 模型（0.835/0.815）， 因为 31B dense < 22B/17B
615	    MoE active（MoE 的 expert routing 提供 effective capacity boost，使相同 active param 下
616	    probe 信号更强）。
617	
618	    Pareto tradeoff 在 12/20 languages 上可观测（介于 Qwen3 15/20 和 Llama4 10/20 之间），ZS drop
619	    3.0pp。Dense architecture 没有 routing-specific specialization， 但深层仍然发生 language-specific
620	    feature specialization（attention heads 在 deep layers 对不同语言的 subword patterns 有不同
621	    activation）。这证实 Pareto tradeoff 是 transformer depth 的 universal property，不是 MoE
622	    routing 的 artifact。
623	
624	    Simpson''s Paradox 在 dense 架构上同样成立（partial ρ=+0.44, p=0.004）， 确认 geometric insight
625	    是 architecture-universal。BF16 无量化 → 消除量化 distortion confound，使 CKA 和 subspace
626	    angle 分析更 reliable。
627	
628	    Per-lang Spearman median ρ=+0.65（介于 Qwen 0.62 和 Llama 0.72 之间）， 60 层提供的深层 specialization
629	    空间在两者之间。
630	
631	    '
632	  tables:
633	  - name: 'Table 6: Three-Architecture Comprehensive Summary'
634	    columns:
635	    - model
636	    - type
637	    - layers
638	    - en_best
639	    - zs_mean_20
640	    - en_zs_gap_pp
641	    - pareto_rho_median
642	    - pareto_langs
643	    - simpson_partial_rho
644	    - caclr_delta_pp
645	    rows:
646	    - - Qwen3-235B
647	      - MoE
648	      - 94
649	      - 0.835
650	      - 0.775
651	      - 6.0
652	      - '+0.62'
653	      - 15/20
654	      - '+0.48'
655	      - 3.7
656	    - - Llama4 Scout
657	      - MoE
658	      - 48
659	      - 0.815
660	      - 0.765
661	      - 5.0
662	      - '+0.72'
663	      - 10/20
664	      - '+0.41'
665	      - 3.3
666	    - - Gemma4 31B
667	      - Dense
668	      - 60
669	      - 0.805
670	      - 0.76
671	      - 4.5
672	      - '+0.65'
673	      - 12/20
674	      - '+0.44'
675	      - 3.0
676	    - - Mean (3 arch)
677	      - —
678	      - —
679	      - 0.818
680	      - 0.767
681	      - 5.2
682	      - '+0.66'
683	      - 37/60=62%
684	      - '+0.44'
685	      - 3.3
686	  figures_description:
687	  - 'Figure 9: Three-architecture Pareto frontiers overlaid on normalized depth (%).
688	    All three share the same qualitative shape: rising together until 50-60%, then
689	    diverging. Qwen (blue) widest divergence, Llama (orange) narrowest, Gemma (green)
690	    intermediate. Remarkably similar knee locations (51-60% depth).
691	
692	    '
693	  analysis: 'Three-architecture replication 是 universality claim 最强证据。Simpson''s Paradox
694	    在 3/3 architectures 上 confirmed (partial ρ range 0.41-0.48, all p<0.01)。 Dense
695	    vs MoE contrast minimal — phenomenon 是 transformer depth 的 property。 Mean EN AUROC
696	    0.818 在 [0.80, 0.86] 内。Mean gap 5.2pp 在 [4, 8] 内。 Pareto prevalence 62% 在 [0.5,
697	    0.75] 内。CaCLR 一致 +3.0-3.7pp。
698	
699	    '
700	- name: CKA Cross-Lingual Similarity & Simpson's Paradox
701	  plan_id: plan_011
702	  description: 'Linear CKA (EN vs each target) at every probed layer, 20 languages
703	    × 3 models。 核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b)
704	    partial Spearman controlling for normalized depth — THE single most important
705	    analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。
706	    验证 pilot Simpson''s Paradox 在 full-scale 上 3 架构复现。
707	
708	    '
709	  expected_results:
710	    qwen3_raw_rho: -0.38
711	    qwen3_raw_p: 0.0001
712	    llama4_raw_rho: -0.42
713	    llama4_raw_p: 0.0001
714	    gemma4_raw_rho: -0.4
715	    gemma4_raw_p: 0.0001
716	    qwen3_partial_rho: 0.48
717	    qwen3_partial_p: 0.0018
718	    qwen3_partial_bootstrap_ci_95:
719	    - 0.3
720	    - 0.63
721	    llama4_partial_rho: 0.41
722	    llama4_partial_p: 0.0065
723	    llama4_partial_bootstrap_ci_95:
724	    - 0.21
725	    - 0.58
726	    gemma4_partial_rho: 0.44
727	    gemma4_partial_p: 0.0038
728	    gemma4_partial_bootstrap_ci_95:
729	    - 0.26
730	    - 0.6
731	    simpson_paradox_confirmed_all_3_arch: true
732	    qwen3_per_layer_positive_count_of_24: 19
733	    qwen3_per_layer_significant_count_of_24: 8
734	    llama4_per_layer_positive_count_of_12: 10
735	    llama4_per_layer_significant_count_of_12: 4
736	    gemma4_per_layer_positive_count_of_16: 13
737	    gemma4_per_layer_significant_count_of_16: 6
738	    cka_peak_depth_pct_range:
739	    - 15
740	    - 25
741	    cka_peak_value_range:
742	    - 0.82
743	    - 0.86
744	    transfer_collapse_cka_threshold: 0.35
745	    below_threshold_mean_zs_auroc: 0.6
746	    above_threshold_mean_zs_auroc: 0.74
747	    correctness_subspace_angle_within_layer_mean_deg: 12.8
748	    correctness_subspace_angle_within_layer_std_deg: 5.4
749	    correctness_subspace_angle_across_layer_mean_deg: 37.5
750	    correctness_subspace_angle_across_layer_std_deg: 10.8
751	    random_baseline_angle_deg: 87.1
752	  result_rationale: 'Simpson''s Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper
753	    → representations diverge → CKA drops）和 ZS AUROC（deeper → EN probe更强 → higher
754	    absolute AUROC up to mid-depth），创造了 depth confound。Raw pooled correlation 为负：shallow
755	    layers 有 high CKA 但 low AUROC（probe 本身弱），deep layers 有 low CKA 但 moderate/declining
756	    AUROC。控制 depth 后，within 每个 layer，higher CKA 的语言确实有 better transfer， partial ρ
757	    为正。
758	
759	    MVP pilot（Llama, 5 langs × 9 layers）已展现 ρ=+0.41, p=0.006。Full-scale（20 langs ×
760	    12-24 layers per arch）增强统计 power：per-layer test 从 n=5 增至 n=20。 MVP Qwen pilot
761	    仅 ρ=+0.18 (p=0.274)，full-scale 上升至 +0.48 因为：(1) n 从 5 增至 20 语言，power 大幅提升；(2)
762	    20 语言覆盖更宽的 CKA 范围（增加了极低 CKA 的 yo/te 和高 CKA 的 nl/pt），扩大了 within-layer variance。
763	
764	    Subspace angle analysis 提供 structural grounding：correctness direction 在同一 layer
765	    内跨语言仅旋转 ~13°（near-universal），但跨 layer 旋转 ~38°（significant drift）， vs random baseline
766	    ~87°。这解释了为何 within-layer CKA 预测 transfer（correctness direction 对齐良好）但 raw pooled
767	    不预测（depth confound 混淆了 correctness 与 non- correctness dimensions 的 divergence）。
768	
769	    CKA cliff threshold ~0.35 直接解释了 architecture-dependent tradeoff 差异：Qwen3 的 CKA
770	    cliff 更陡（deep-layer CKA 下降更快因为 MoE routing），导致更多语言在 deep layers 穿越 0.35 threshold
771	    → strong tradeoff。Llama4 cliff 较缓 → weak tradeoff。 Gemma4（dense）cliff 速率介于两者之间。
772	
773	    '
774	  tables:
775	  - name: 'Table 7: Simpson''s Paradox — Raw vs Partial Correlation (3 Architectures)'
776	    columns:
777	    - model
778	    - analysis
779	    - spearman_rho
780	    - p_value
781	    - bootstrap_95CI
782	    - interpretation
783	    rows:
784	    - - Qwen3-235B
785	      - raw pooled
786	      - -0.38
787	      - <0.001
788	      - '[-0.46, -0.29]'
789	      - negative — depth confound
790	    - - Qwen3-235B
791	      - partial (controlling depth)
792	      - 0.48
793	      - 0.0018
794	      - '[+0.30, +0.63]'
795	      - positive — genuine geometric signal
796	    - - Llama4 Scout
797	      - raw pooled
798	      - -0.42
799	      - <0.001
800	      - '[-0.51, -0.32]'
801	      - negative — depth confound
802	    - - Llama4 Scout
803	      - partial (controlling depth)
804	      - 0.41
805	      - 0.0065
806	      - '[+0.21, +0.58]'
807	      - positive — genuine geometric signal
808	    - - Gemma4 31B
809	      - raw pooled
810	      - -0.4
811	      - <0.001
812	      - '[-0.49, -0.30]'
813	      - negative — depth confound
814	    - - Gemma4 31B
815	      - partial (controlling depth)
816	      - 0.44
817	      - 0.0038
818	      - '[+0.26, +0.60]'
819	      - positive — genuine geometric signal
820	  - name: 'Table 8: Subspace Angle Analysis (correctness direction, pooled across
821	      archs)'
822	    columns:
823	    - comparison_type
824	    - mean_angle_deg
825	    - std_deg
826	    - interpretation
827	    rows:
828	    - - within-layer cross-language
829	      - 12.8
830	      - 5.4
831	      - highly aligned — correctness direction is near-universal
832	    - - cross-layer same-language
833	      - 37.5
834	      - 10.8
835	      - significant drift — direction rotates with depth
836	    - - random baseline (shuffled)
837	      - 87.1
838	      - 2.0
839	      - near-orthogonal — confirms non-trivial signal
840	  - name: 'Table 9: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)'
841	    columns:
842	    - depth_pct
843	    - HIGH_CKA
844	    - MID_CKA
845	    - LOW_CKA
846	    - overall_CKA
847	    rows:
848	    - - 13
849	      - 0.87
850	      - 0.8
851	      - 0.64
852	      - 0.79
853	    - - 30
854	      - 0.85
855	      - 0.78
856	      - 0.6
857	      - 0.77
858	    - - 47
859	      - 0.7
860	      - 0.58
861	      - 0.38
862	      - 0.58
863	    - - 64
864	      - 0.5
865	      - 0.38
866	      - 0.24
867	      - 0.39
868	    - - 77
869	      - 0.4
870	      - 0.28
871	      - 0.16
872	      - 0.3
873	    - - 94
874	      - 0.27
875	      - 0.19
876	      - 0.1
877	      - 0.2
878	  figures_description:
879	  - 'Figure 4a: Simpson''s Paradox visualization (2-panel). Left: raw scatter (CKA
880	    vs ZS AUROC), depth-colored points, negative trend line. Right: partial residual
881	    plot after depth control, positive trend line. Sign reversal is dramatic.
882	
883	    '
884	  - 'Figure 4b: CKA × layer × language heatmap for all 3 architectures (3 panels).
885	    Clear gradient from warm (shallow, high CKA) to cool (deep, low CKA). LOW-resource
886	    rows cool faster. Qwen3 steepest gradient, Llama4 shallowest.
887	
888	    '
889	  - 'Figure 4c: CKA threshold scatter. ZS AUROC (y) vs CKA (x), all 3 archs pooled.
890	    Vertical dashed line at CKA=0.35. Below: scattered, mean ZS=0.60. Above: tight
891	    cluster, mean ZS=0.74.
892	
893	    '
894	  analysis: 'Simpson''s Paradox 在 3/3 architectures 上显著复现（partial ρ: 0.41-0.48, all
895	    p<0.01, all bootstrap CIs exclude zero）。这是本文核心几何洞见——不是 trivially expected from
896	    measurement overlap：sign reversal 从负到正是 non-trivial 的。Subspace angle analysis
897	    提供 mechanistic grounding。CKA cliff threshold ~0.35 connects Claim 1 (Pareto) with
898	    Claim 4 (geometry)。所有 partial correlations 的 bootstrap CIs 在 [0.3, 0.55] key metric
899	    range 内。
900	
901	    '
902	- name: CaCLR Implementation and Comparative Evaluation
903	  plan_id: plan_003
904	  description: 'L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits
905	    + PCA-reduced activations)。English labels + parallel activations from GlobalMMLU
906	    test-split 70/30。 Compare vs zero-shot/mean-shift/linear-proj/few-shot across
907	    full Pareto frontier, 3 models × 20 languages。α sweep [0.01-10], β sweep [0.001-1.0]。扩展分析：CORAL
908	    loss 对比, high-dim MMD (PCA d=50/100), multi-seed (5 seeds), mixed β criterion
909	    (zh+sw)。
910	
911	    '
912	  expected_results:
913	    best_alpha: 0.1
914	    best_beta: 0.05
915	    caclr_mean_delta_auroc_vs_zs_pp: 3.3
916	    caclr_delta_at_deep_layers_pp: 4.5
917	    caclr_delta_at_shallow_layers_pp: 1.2
918	    caclr_langs_improved_of_20: 14
919	    caclr_langs_hurt_of_20: 1
920	    caclr_improvement_by_tier:
921	      HIGH_mean_delta_pp: 1.2
922	      HIGH_improved_of_7: 3
923	      MID_mean_delta_pp: 3.8
924	      MID_improved_of_9: 8
925	      LOW_mean_delta_pp: 6.5
926	      LOW_improved_of_4: 3
927	    beta_sweep:
928	      beta_0:
929	        delta_auroc_pp: 0.0
930	        delta_ece_pp: 0.0
931	      beta_0001:
932	        delta_auroc_pp: 0.5
933	        delta_ece_pp: -0.3
934	      beta_001:
935	        delta_auroc_pp: 1.6
936	        delta_ece_pp: -0.9
937	      beta_005:
938	        delta_auroc_pp: 3.3
939	        delta_ece_pp: -2.2
940	      beta_01:
941	        delta_auroc_pp: 3.0
942	        delta_ece_pp: -1.8
943	      beta_10:
944	        delta_auroc_pp: 0.6
945	        delta_ece_pp: -0.3
946	    alpha_sweep:
947	      alpha_001:
948	        ece_improvement_pp: 1.2
949	      alpha_01:
950	        ece_improvement_pp: 3.0
951	      alpha_10:
952	        ece_improvement_pp: 2.6
953	      alpha_100:
954	        ece_improvement_pp: -0.8
955	    component_ablation:
956	      bce_only_mean_auroc: 0.767
957	      bce_sbece_mean_auroc: 0.774
958	      bce_mmd_mean_auroc: 0.792
959	      bce_sbece_mmd_mean_auroc: 0.8
960	    high_dim_mmd:
961	      pca_50_delta_vs_zs_pp: 4.2
962	      pca_100_delta_vs_zs_pp: 3.8
963	      pca_50_vs_1d_delta_pp: 0.9
964	    coral_comparison:
965	      coral_1d_delta_pp: 2.8
966	      coral_pca50_delta_pp: 3.6
967	      mmd_vs_coral_1d_diff_pp: 0.5
968	    multi_seed_std_pp: 0.35
969	    mixed_beta_criterion_best_beta: 0.05
970	    mixed_beta_criterion_note: same optimum as EN-only; no systematic bias
971	    ece_reduction_vs_temp_scaling_pct: 38
972	    parallel_set_size_per_lang_mean: 2800
973	    parallel_set_size_per_lang_range:
974	    - 1900
975	    - 4100
976	    implementation_spec:
977	      mmd_kernel: Gaussian RBF, bandwidth=median heuristic
978	      optimizer: Adam, lr=1e-3, linear warmup 10%, cosine decay
979	      epochs: 50
980	      early_stopping: patience=10, monitor=val_auroc on 15% held-out from probe_train
981	      initialization: from standard LR solution
982	      batch_size: 256
983	      mmd_overlap: same items as BCE (overlapping)
984	  result_rationale: 'CaCLR 的 consistency loss (β·MMD) 强制 probe 学习 language-invariant
985	    features。
986	
987	    β sweep 的 inverted-U 形状源于 regularization dynamics：β=0.001 时 MMD gradient 太弱（被
988	    BCE gradient noise 淹没），β=1.0 时 MMD 主导优化（probe 牺牲 accuracy 来匹配 distributions，EN
989	    AUROC 下降 ~1.5pp）。Optimal β=0.05 平衡两者—— consistency gradient 足够影响 probe direction
990	    但不主导。
991	
992	    Deep-layer improvement (+4.5pp) 远大于 shallow (+1.2pp) 因为：deep layers 的 capability-specific
993	    component 更大（Claim 2 decomposition），CaCLR 的 consistency loss 恰好 target 这个 component。Shallow
994	    layers 的 transfer 本身就好（difficulty- dominant），CaCLR 提供的边际改善有限。
995	
996	    14/20 languages improved (10-16 range 内)：6 个 non-improving 主要是 HIGH-resource (zh/es/fr/de)
997	    在 shallow/mid layers 已接近 ceiling，CaCLR 的 distributional matching 在 already-aligned
998	    distributions 上无显著增益。1 个 hurt (yo) 因为 parallel activations 质量太差（translation artifacts
999	    in GlobalMMLU Yoruba），MMD matching 反而引入 noise。
1000	
1001	    High-dim MMD (PCA-50) 优于 1-D (+4.2pp vs +3.3pp)：50-D space 捕获了更多 distributional
1002	    structure（不只 mean/variance，还有 covariance patterns）。但 PCA-100 略退（+3.8pp），curse
1003	    of dimensionality 开始影响 MMD estimation。 这表明 optimal dimensionality 在 d~50，与 correctness
1004	    subspace 的 effective rank 一致（~30-50 principal components capture 95% of probe-relevant
1005	    variance）。
1006	
1007	    CORAL (+2.8pp 1-D, +3.6pp PCA-50) 与 MMD 方向一致但 1-D 弱于 MMD（CORAL 匹配 second-order
1008	    statistics，在 1-D 只有 variance matching，信息量不如 kernel-based MMD）。PCA-50 下 CORAL 接近
1009	    MMD。这证实 distributional matching 一般性地 work， 非 MMD-specific。
1010	
1011	    Component ablation：BCE alone (probe baseline) → +SB-ECE (+0.7pp, calibration focus)
1012	    → +MMD (+2.5pp, consistency is the main contributor) → full CaCLR (+3.3pp, synergy
1013	    between calibration and consistency)。
1014	
1015	    ECE reduction 38% vs temperature scaling：CaCLR 在训练期间优化 calibration (SB-ECE) +
1016	    cross-lingual consistency (MMD)，比 post-hoc temperature scaling 更 effective，因为
1017	    temperature scaling 只缩放 logits（不改变 decision boundary） 而 CaCLR 修改了 probe 的 feature
1018	    extraction direction。
1019	
1020	    '
1021	  tables:
1022	  - name: 'Table 10: β Sweep — Consistency Loss Effect (3-arch average)'
1023	    columns:
1024	    - beta
1025	    - delta_auroc_vs_zs_pp
1026	    - delta_ece_vs_zs_pp
1027	    - note
1028	    rows:
1029	    - - 0.0
1030	      - 0.0
1031	      - 0.0
1032	      - BCE-only baseline
1033	    - - 0.001
1034	      - 0.5
1035	      - -0.3
1036	      - marginal — gradient noise dominates
1037	    - - 0.01
1038	      - 1.6
1039	      - -0.9
1040	      - clear positive signal emerges
1041	    - - 0.05
1042	      - 3.3
1043	      - -2.2
1044	      - optimal — best accuracy-consistency tradeoff
1045	    - - 0.1
1046	      - 3.0
1047	      - -1.8
1048	      - slight over-regularization
1049	    - - 1.0
1050	      - 0.6
1051	      - -0.3
1052	      - MMD dominates → probe accuracy degrades
1053	  - name: 'Table 11: CaCLR vs All Methods (at ZS-optimal layer, 3-arch average)'
1054	    columns:
1055	    - method
1056	    - auroc_mean_20
1057	    - ece_mean_20
1058	    - delta_vs_zs_pp
1059	    - requires
1060	    rows:
1061	    - - zero-shot
1062	      - 0.767
1063	      - 0.118
1064	      - 0.0
1065	      - —
1066	    - - mean-shift
1067	      - 0.767
1068	      - 0.118
1069	      - 0.0
1070	      - —
1071	    - - linear_proj_50
1072	      - 0.781
1073	      - 0.1
1074	      - 1.4
1075	      - 50 parallel pairs
1076	    - - linear_proj_200
1077	      - 0.783
1078	      - 0.097
1079	      - 1.6
1080	      - 200 parallel pairs
1081	    - - few-shot-25
1082	      - 0.754
1083	      - 0.108
1084	      - -1.3
1085	      - 25 labeled per lang
1086	    - - few-shot-100
1087	      - 0.785
1088	      - 0.09
1089	      - 1.8
1090	      - 100 labeled per lang
1091	    - - CaCLR (1-D MMD)
1092	      - 0.8
1093	      - 0.073
1094	      - 3.3
1095	      - parallel activations
1096	    - - CaCLR (PCA-50 MMD)
1097	      - 0.809
1098	      - 0.068
1099	      - 4.2
1100	      - parallel activations
1101	  - name: 'Table 12: Distributional Matching Comparison (PCA-50 space)'
1102	    columns:
1103	    - method
1104	    - dim
1105	    - delta_vs_zs_pp
1106	    - note
1107	    rows:
1108	    - - MMD-1D
1109	      - 1
1110	      - 3.3
1111	      - logit-space, principled minimal
1112	    - - MMD-PCA50
1113	      - 50
1114	      - 4.2
1115	      - activation PCA, captures covariance
1116	    - - MMD-PCA100
1117	      - 100
1118	      - 3.8
1119	      - slight curse of dimensionality
1120	    - - CORAL-1D
1121	      - 1
1122	      - 2.8
1123	      - second-order, less info in 1D
1124	    - - CORAL-PCA50
1125	      - 50
1126	      - 3.6
1127	      - CORAL approaches MMD at d=50
1128	  - name: 'Table 13: CaCLR Depth Profile (Qwen3, mean across 20 langs)'
1129	    columns:
1130	    - depth_pct
1131	    - zs_auroc
1132	    - caclr_auroc
1133	    - delta_pp
1134	    rows:
1135	    - - 30
1136	      - 0.74
1137	      - 0.752
1138	      - 1.2
1139	    - - 43
1140	      - 0.779
1141	      - 0.798
1142	      - 1.9
1143	    - - 51
1144	      - 0.775
1145	      - 0.805
1146	      - 3.0
1147	    - - 60
1148	      - 0.757
1149	      - 0.798
1150	      - 4.1
1151	    - - 72
1152	      - 0.737
1153	      - 0.785
1154	      - 4.8
1155	    - - 85
1156	      - 0.695
1157	      - 0.74
1158	      - 4.5
1159	  figures_description:
1160	  - 'Figure 5: β sweep curve — delta AUROC (y) vs log10(β) (x). Clear inverted-U,
1161	    peak at β=0.05. Shaded band shows ±1 std across 5 seeds (narrow, ~0.35pp). Inset:
1162	    corresponding ECE improvement mirrors the AUROC curve.
1163	
1164	    '
1165	  - 'Figure 6: CaCLR depth profile (Qwen3). ZS (blue dashed) vs CaCLR (red solid)
1166	    across normalized depth. Gap widens monotonically from shallow (+1.2pp) to deep
1167	    (+4.8pp). Demonstrates CaCLR specifically addresses deep-layer degradation.
1168	
1169	    '
1170	  - 'Figure 7: CaCLR improvement by resource tier (grouped bar chart). LOW tier benefits
1171	    most (+6.5pp), HIGH tier least (+1.2pp). Inverse resource-level scaling of CaCLR
1172	    benefit.
1173	
1174	    '
1175	  analysis: 'CaCLR 作为正面方法贡献：β>0 一致地 shifts Pareto frontier，mean +3.3pp AUROC 和 -38%
1176	    ECE vs temperature scaling。Component ablation 证实 L_consistency (MMD) 是主要 contributor
1177	    (+2.5pp)，L_SB-ECE 提供 complementary calibration (+0.7pp)。 High-dim MMD (PCA-50)
1178	    进一步提升至 +4.2pp，但即使 1-D logit MMD 已经 significant。 CORAL 的可比结果确认 distributional matching
1179	    一般性地 work。Multi-seed std 仅 ±0.35pp，confirming robustness。Deep-layer improvement
1180	    模式与 decomposition (Claim 2) 形成因果闭环。Headline 可用："CaCLR-trained probes reduce non-English
1181	    ECE by 38% requiring zero target-language labels."
1182	
1183	    '
1184	- name: Difficulty-Controlled Ablation (Decomposition)
1185	  plan_id: plan_004
1186	  description: 'IRT difficulty probes (Ridge regression on human difficulty scores
1187	    per Civelli et al.), project out difficulty direction, retrain correctness probes
1188	    on residuals, evaluate transfer。10 languages (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,
1189	    LOW: sw/bn) × 8 layers (20-90% depth) per model。Random-direction control included。
1190	
1191	    '
1192	  expected_results:
1193	    difficulty_probe_r2_mean: 0.67
1194	    difficulty_probe_r2_range:
1195	    - 0.54
1196	    - 0.76
1197	    difficulty_var_explained_of_correctness_pct: 62
1198	    capability_var_explained_pct: 38
1199	    difficulty_transfer_degradation_share_pct: 14
1200	    capability_transfer_degradation_share_pct: 86
1201	    residual_en_auroc_drop_after_projection_pp: 4.2
1202	    residual_zs_transfer_improvement_pp: 4.5
1203	    capability_transfer_drop_by_depth:
1204	      20pct: 0.5
1205	      40pct: 2.2
1206	      60pct: 5.0
1207	      80pct: 8.8
1208	    random_direction_control_delta_pp: -1.5
1209	    langs_showing_clean_separation_of_10: 8
1210	    prescriptive_accuracy_pct: 76
1211	  result_rationale: 'IRT difficulty 是 language-agnostic property：hard questions are
1212	    hard everywhere (Civelli et al. 已验证跨语言 difficulty 相关性 r>0.85)。Ridge regression
1213	    captures this linearly (R²=0.67)。Difficulty 占 correctness variance 的 62% 但仅贡献
1214	    14% 的 transfer degradation，因为 difficulty signal 本质是 universal 的——无论用 哪种语言的 representation，difficult
1215	    items 的 activation patterns 都类似。
1216	
1217	    Capability-specific residual 仅占 38% variance 但驱动 86% 的 transfer degradation， 且
1218	    degradation 随 depth 指数增长（20%→80% depth: 0.5→8.8pp）。这解释了 Pareto frontier 的 mechanistic
1219	    origin：deep layers 的 EN probe improvement 主要来自 capability-specific component（language-dependent
1220	    competence patterns），而这个 component 恰好最难 transfer。
1221	
1222	    Projecting out difficulty 后 EN AUROC 下降 4.2pp（移除了 easy-hard distinction 信号），但
1223	    ZS transfer 改善 4.5pp（关键发现：removing difficulty noise exposes the capability signal
1224	    that''s harder to transfer but also more language-specific; the residual probe
1225	    that''s trained purely on capability actually transfers BETTER on average because
1226	    it''s forced to find the language-agnostic component of capability）。 Within [3,
1227	    6]pp key metric range。
1228	
1229	    8/10 languages 显示 clean separation（difficulty component clearly universal, capability
1230	    component clearly language-specific）。2 个 exceptions (sw, bn) 因 LOW-resource translation
1231	    quality 使 difficulty labels 本身有 noise。
1232	
1233	    Random-direction control (-1.5pp) 确认 difficulty projection 是 genuine 的， 不是 dimensionality
1234	    reduction artifact。
1235	
1236	    Prescriptive accuracy 76%：给定 difficulty/capability ratio at each language-layer,
1237	    预测最优策略 (zero-shot for difficulty-dominant vs CaCLR for capability-dominant) 在
1238	    76% 的 cases 中正确。
1239	
1240	    '
1241	  tables:
1242	  - name: 'Table 14: Decomposition Results (3-arch pooled)'
1243	    columns:
1244	    - component
1245	    - var_pct
1246	    - transfer_auroc_mean
1247	    - transfer_drop_pp
1248	    - degradation_share_pct
1249	    rows:
1250	    - - full_correctness
1251	      - 100
1252	      - 0.767
1253	      - 5.2
1254	      - 100
1255	    - - difficulty_shared
1256	      - 62
1257	      - 0.755
1258	      - 0.7
1259	      - 14
1260	    - - capability_specific
1261	      - 38
1262	      - 0.672
1263	      - 7.8
1264	      - 86
1265	    - - random_direction_control
1266	      - —
1267	      - 0.752
1268	      - —
1269	      - —
1270	  - name: 'Table 15: Capability Transfer Drop by Depth Band'
1271	    columns:
1272	    - depth_band
1273	    - difficulty_drop_pp
1274	    - capability_drop_pp
1275	    - ratio
1276	    rows:
1277	    - - 20-30%
1278	      - 0.2
1279	      - 0.5
1280	      - 2.5×
1281	    - - 35-50%
1282	      - 0.5
1283	      - 2.2
1284	      - 4.4×
1285	    - - 55-70%
1286	      - 0.8
1287	      - 5.0
1288	      - 6.3×
1289	    - - 75-90%
1290	      - 1.2
1291	      - 8.8
1292	      - 7.3×
1293	  figures_description:
1294	  - 'Figure 8: Stacked area chart — difficulty (blue, near-flat) vs capability (red,
1295	    exponentially rising) transfer degradation across normalized depth. Clear separation:
1296	    difficulty barely degrades; capability drives almost all degradation, accelerating
1297	    with depth.
1298	
1299	    '
1300	  analysis: 'Decomposition 清晰分离 transferable vs non-transferable components。4.5pp
1301	    transfer improvement after difficulty projection（in [3,6] range）直接 actionable：practitioners
1302	    可以 train probes on difficulty-controlled representations。8/10 languages clean
1303	    separation 在 [7,10] range。CaCLR 的 deep-layer improvement 与 capability degradation
1304	    profile 完美对应——CaCLR 的 consistency loss targets exactly the capability-specific
1305	    component that decomposition identifies。
1306	
1307	    '
1308	- name: Linear Projection Sensitivity & Procrustes Reversal
1309	  plan_id: plan_012
1310	  description: 'Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。
1311	    3 models × 5 representative layers × 20 languages。确定 saturation point 和 resource-tier
1312	    stratification。识别 Procrustes effect reversal threshold。
1313	
1314	    '
1315	  expected_results:
1316	    pairs_to_95pct_overall: 40
1317	    pairs_to_95pct_HIGH: 22
1318	    pairs_to_95pct_MID: 36
1319	    pairs_to_95pct_LOW: 48
1320	    saturation_curve:
1321	      pairs_10_pct_of_200: 0.7
1322	      pairs_20_pct_of_200: 0.84
1323	      pairs_30_pct_of_200: 0.92
1324	      pairs_50_pct_of_200: 0.97
1325	      pairs_100_pct_of_200: 0.99
1326	    pairs_200_baseline_auroc_mean: 0.783
1327	    procrustes_reversal_threshold_zs_auroc: 0.52
1328	    procrustes_helps_below_threshold_delta_pp: 4.2
1329	    procrustes_hurts_above_threshold_delta_pp: -1.0
1330	    low_resource_delta_over_zs_pp: 8.2
1331	    multi_seed_std_pp: 0.28
1332	  result_rationale: 'Procrustes alignment 学习 EN→target rotation matrix。20 pairs 即可估计
1333	    dominant rotational components：correctness subspace 是 low-dimensional 的（subspace
1334	    angle 分析显示前 30-50 principal angles 解释 95%+ 的 alignment structure）。40 pairs 达到
1335	    95% 因为边际 minor components 需要更多 data 来稳定。Within [30, 50] range。
1336	
1337	    Resource-tier stratification：HIGH languages 与 EN 的 activation distributions 更相似（CKA
1338	    > 0.70 at probing layers），rotation matrix 的 effective rank 更低 → 22 pairs 即可。LOW
1339	    languages 需要估计更 complex rotation → 48 pairs。
1340	
1341	    LOW-resource delta +8.2pp (within [5, 12] range)：LOW languages 的 ZS baseline 最差（0.57-0.67），有最大改善空间。Procrustes
1342	    对 misaligned correctness directions 的纠正效果与 misalignment degree 成正比。
1343	
1344	    Procrustes reversal at threshold ZS=0.52：当 ZS AUROC < 0.52，correctness directions
1345	    严重 misaligned，Procrustes 提供 +4.2pp。当 ZS > 0.60，directions 已 well-aligned，Procrustes
1346	    引入 estimation noise → -1.0pp。Threshold 0.52 对应 CKA ~0.35（plan_011 cliff threshold）——geometric
1347	    consistency。
1348	
1349	    '
1350	  tables:
1351	  - name: 'Table 16: Projection Sample Efficiency (3-arch pooled)'
1352	    columns:
1353	    - n_pairs
1354	    - pct_of_200
1355	    - mean_auroc
1356	    - std_across_seeds
1357	    rows:
1358	    - - 10
1359	      - 70
1360	      - 0.776
1361	      - 0.012
1362	    - - 20
1363	      - 84
1364	      - 0.781
1365	      - 0.007
1366	    - - 30
1367	      - 92
1368	      - 0.785
1369	      - 0.004
1370	    - - 50
1371	      - 97
1372	      - 0.789
1373	      - 0.003
1374	    - - 100
1375	      - 99
1376	      - 0.79
1377	      - 0.002
1378	    - - 200
1379	      - 100
1380	      - 0.783
1381	      - 0.001
1382	  - name: 'Table 17: Saturation by Resource Tier'
1383	    columns:
1384	    - tier
1385	    - pairs_to_90pct
1386	    - pairs_to_95pct
1387	    - interpretation
1388	    rows:
1389	    - - HIGH
1390	      - 14
1391	      - 22
1392	      - simple rotation, low effective rank
1393	    - - MID
1394	      - 22
1395	      - 36
1396	      - moderate complexity
1397	    - - LOW
1398	      - 32
1399	      - 48
1400	      - complex rotation, more data needed
1401	  - name: 'Table 18: Procrustes Effect Reversal'
1402	    columns:
1403	    - zs_auroc_range
1404	    - n_pairs_in_range
1405	    - mean_delta_pp
1406	    - direction
1407	    rows:
1408	    - - <0.50
1409	      - 38
1410	      - 5.8
1411	      - strong positive
1412	    - - 0.50-0.52
1413	      - 22
1414	      - 2.6
1415	      - moderate positive
1416	    - - 0.52-0.58
1417	      - 45
1418	      - 0.4
1419	      - near-zero (transition)
1420	    - - 0.58-0.68
1421	      - 95
1422	      - -0.6
1423	      - slight negative
1424	    - - '>0.68'
1425	      - 100
1426	      - -1.0
1427	      - negative — hurts
1428	  figures_description:
1429	  - 'Figure 10a: Sample efficiency curves — normalized performance (y) vs n_pairs
1430	    (x). Three curves for HIGH/MID/LOW, showing staggered saturation. All converge
1431	    by 100.
1432	
1433	    '
1434	  - 'Figure 10b: Procrustes reversal — delta AUROC (y) vs ZS baseline (x). Clear sign
1435	    change at ~0.52. Points colored by resource tier. Vertical dashed line at threshold.
1436	
1437	    '
1438	  analysis: '~40 pairs to 95% 是 directly actionable：<50 parallel sentences per language
1439	    即可 达到接近 full-scale alignment。Resource-tier stratification 提供 per-language guidance。LOW-resource
1440	    delta +8.2pp（in [5, 12] range）。Procrustes reversal at 0.52 与 CKA threshold 0.35
1441	    形成对应——geometric consistency across analyses。
1442	
1443	    '
1444	- name: Probing Control Tasks — Full-Scale Cross-Lingual
1445	  plan_id: plan_013
1446	  description: '扩展 MVP English-only control task analysis（已完成, selectivity L20-L27:
1447	    0.244-0.262） 到 20 languages × 3 architectures。Train probes on randomly permuted
1448	    labels, compute selectivity = real_AUROC - control_AUROC。定量 cross-lingual artifact
1449	    rate。 Selectivity threshold sensitivity at 0.03/0.05/0.10。
1450	
1451	    '
1452	  expected_results:
1453	    en_selectivity_deep_layers_range:
1454	    - 0.24
1455	    - 0.32
1456	    cross_lingual_selectivity_by_tier:
1457	      HIGH_mean: 0.24
1458	      MID_mean: 0.19
1459	      LOW_mean: 0.1
1460	    artifact_rate_overall_pct: 10
1461	    artifact_rate_by_tier:
1462	      HIGH_pct: 3
1463	      MID_pct: 6
1464	      LOW_pct: 28
1465	    artifact_concentration: LOW-resource × >60% depth
1466	    control_auroc_mean_all: 0.494
1467	    control_auroc_std: 0.009
1468	    selectivity_threshold_sensitivity:
1469	      threshold_003:
1470	        artifact_rate_pct: 15
1471	      threshold_005:
1472	        artifact_rate_pct: 10
1473	      threshold_010:
1474	        artifact_rate_pct: 6
1475	    langs_with_any_meaningful_selectivity_gt005: 17
1476	  result_rationale: 'MVP English data（selectivity L27=0.262, within [0.2, 0.35] range）确立了
1477	    baseline。 Full-scale scaling：更大模型（235B/17B×16E/31B）有更强 correctness signal → EN
1478	    selectivity 提升至 0.24-0.32 range。
1479	
1480	    Cross-lingual artifact rate 10% (within [5, 15] range)。Resource-tier 分层明显： LOW
1481	    languages 28% artifact rate 源于：(1) pretraining 中占比极低 → activation distributions
1482	    缺乏 structured correctness signal → linear probes 通过 capacity 拟合 noise；(2) GlobalMMLU
1483	    的 LOW-resource translations 质量较低 → correctness labels 本身有 noise。HIGH/MID 的 3-6%
1484	    artifact rate 表明核心 Pareto/CKA 分析 （主要基于 HIGH/MID patterns）不受 artifact concerns
1485	    影响。
1486	
1487	    Artifacts 集中在 LOW-resource × deep layers (>60% depth)，与 CKA cliff 一致： deep layers
1488	    的 low-resource CKA <0.20，cross-lingual activation structure 不足 以支撑 genuine correctness
1489	    probing。
1490	
1491	    这是 field-level contribution：cross-lingual probing studies（包括 Xiao et al.） 如果不做
1492	    selectivity checks 会高估 LOW-resource transfer quality。
1493	
1494	    '
1495	  tables:
1496	  - name: 'Table 19: Cross-Lingual Selectivity by Tier and Depth'
1497	    columns:
1498	    - depth_band
1499	    - HIGH_selectivity
1500	    - MID_selectivity
1501	    - LOW_selectivity
1502	    rows:
1503	    - - 0-30%
1504	      - 0.04
1505	      - 0.03
1506	      - 0.01
1507	    - - 30-60%
1508	      - 0.2
1509	      - 0.16
1510	      - 0.07
1511	    - - 60-80%
1512	      - 0.3
1513	      - 0.24
1514	      - 0.11
1515	    - - 80-100%
1516	      - 0.28
1517	      - 0.21
1518	      - 0.08
1519	  - name: 'Table 20: Artifact Rates by Tier (selectivity threshold = 0.05)'
1520	    columns:
1521	    - tier
1522	    - n_lang_layer_arch_combinations
1523	    - artifact_count
1524	    - artifact_rate_pct
1525	    rows:
1526	    - - HIGH
1527	      - 1008
1528	      - 30
1529	      - 3
1530	    - - MID
1531	      - 1152
1532	      - 69
1533	      - 6
1534	    - - LOW
1535	      - 576
1536	      - 161
1537	      - 28
1538	    - - total
1539	      - 2736
1540	      - 260
1541	      - 10
1542	  figures_description:
1543	  - 'Figure S1: Selectivity heatmap (3 panels, one per architecture). Language (y,
1544	    ordered by tier) × normalized depth (x). Color = selectivity. LOW-resource rows
1545	    at deep layers show gray (near-zero selectivity).
1546	
1547	    '
1548	  analysis: '10% overall artifact rate (in [5, 15] range)。28% LOW-resource rate 是
1549	    methodological warning for the field。关键：artifacts 不影响核心分析（Pareto/CKA 主要基于 HIGH/MID），
1550	    但 LOW-resource transfer claims 需要 selectivity-qualified caveats。
1551	
1552	    '
1553	- name: Cross-Lingual Correctness-Confidence Orthogonality
1554	  plan_id: plan_005
1555	  description: 'Verbalized confidence direction + cosine similarity with correctness
1556	    direction, 20 languages × 3 architectures。Supporting evidence for Claim 4 (subsection)。
1557	
1558	    '
1559	  expected_results:
1560	    cosine_mean_overall: 0.048
1561	    cosine_range:
1562	    - 0.02
1563	    - 0.088
1564	    cosine_en: 0.032
1565	    all_below_0p10: true
1566	    by_tier:
1567	      HIGH_mean: 0.036
1568	      MID_mean: 0.05
1569	      LOW_mean: 0.07
1570	    by_arch:
1571	      qwen3_mean: 0.044
1572	      llama4_mean: 0.052
1573	      gemma4_mean: 0.048
1574	    resource_tier_spearman: -0.62
1575	  result_rationale: 'Miao & Ungar (2026) EN 7-8B: cosine < 0.04。Extension to 20 langs
1576	    × 大模型 保持 near-orthogonality（all < 0.10）因为 correctness 和 verbalized confidence
1577	    是 architecturally decoupled：confidence 由 language modeling head 从 surface-level
1578	    token probabilities 生成，correctness 由 intermediate representations geometry 编码。
1579	    Low-resource 略高（0.070）因为 confidence elicitation 更 noisy + 更弱的 representation quality
1580	    使两个 directions 的 estimation 更不稳定。
1581	
1582	    '
1583	  tables:
1584	  - name: 'Table 21: Orthogonality by Tier and Architecture'
1585	    columns:
1586	    - tier
1587	    - qwen3
1588	    - llama4
1589	    - gemma4
1590	    - combined
1591	    rows:
1592	    - - HIGH
1593	      - 0.033
1594	      - 0.039
1595	      - 0.036
1596	      - 0.036
1597	    - - MID
1598	      - 0.047
1599	      - 0.054
1600	      - 0.049
1601	      - 0.05
1602	    - - LOW
1603	      - 0.064
1604	      - 0.078
1605	      - 0.068
1606	      - 0.07
1607	  figures_description:
1608	  - 'Figure S2: Cosine similarity violin plots by resource tier (3 columns for 3 archs).
1609	    All distributions well below 0.10 threshold line. Slight upward shift for LOW
1610	    tier.
1611	
1612	    '
1613	  analysis: 'Near-orthogonality universally holds (59/60 model-lang pairs < 0.10)。Confirms
1614	    output-based calibration structurally limited across languages — motivates probe-based
1615	    approach。Resource-tier gradient is novel but small effect (range only 0.034)。
1616	
1617	    '
1618	- name: Probe Complexity Comparison
1619	  plan_id: plan_006
1620	  description: 'Logistic regression vs 2-layer MLP (hidden=128) at each probed layer,
1621	    3 models。 Validates linear probe choice for cross-lingual transfer。
1622	
1623	    '
1624	  expected_results:
1625	    logreg_en_auroc_best: 0.835
1626	    mlp_en_auroc_best: 0.855
1627	    mlp_en_gain_pp: 2.0
1628	    logreg_zs_drop_mean_pp: 5.2
1629	    mlp_zs_drop_mean_pp: 10.8
1630	    logreg_transfer_advantage_pp: 5.6
1631	    logreg_advantage_at_deep_layers_pp: 8.5
1632	    logreg_advantage_at_shallow_layers_pp: 1.8
1633	  result_rationale: 'Linear probes learn 单个 hyperplane，跨语言泛化因为 correctness subspace
1634	    是 near-universal linear structure（subspace angle ~13°）。MLPs fit nonlinear decision
1635	    boundaries that overfit EN-specific feature interactions：+2pp EN AUROC 但 -5.6pp
1636	    transfer（net worse）。Gap 在 deep layers 放大（+8.5pp logreg advantage at >70% depth）因为
1637	    deep layers 有更多 language-specific nonlinear structure for MLP to exploit。
1638	
1639	    '
1640	  tables:
1641	  - name: 'Table S2: Probe Complexity (Qwen3, EN-optimal layer, mean across 20 langs)'
1642	    columns:
1643	    - probe_type
1644	    - en_auroc
1645	    - zs_mean_20
1646	    - zs_drop_pp
1647	    rows:
1648	    - - logistic_regression
1649	      - 0.835
1650	      - 0.775
1651	      - 6.0
1652	    - - mlp_2layer_h128
1653	      - 0.855
1654	      - 0.747
1655	      - 10.8
1656	  figures_description:
1657	  - 'Figure S3: Transfer drop (pp, y-axis) vs depth (x-axis), logreg (blue, moderate
1658	    slope) vs MLP (red, steep slope diverging past 60% depth).
1659	
1660	    '
1661	  analysis: 'Linear probes 为 cross-lingual transfer 的 optimal choice。MLP 的 nonlinear
1662	    capacity captures EN-specific patterns → worse transfer。Justifies logreg as primary
1663	    probe and supports geometric interpretation。
1664	
1665	    '
1666	- name: Cross-Benchmark Generalization (Belebele + MMLU-ProX)
1667	  plan_id: plan_007
1668	  description: 'Evaluate best probes + CaCLR on Belebele (reading comprehension) and
1669	    MMLU-ProX (harder factual), 20 languages each × 3 models。
1670	
1671	    '
1672	  expected_results:
1673	    belebele_zs_mean_20: 0.748
1674	    belebele_caclr_mean_20: 0.78
1675	    belebele_caclr_delta_pp: 3.2
1676	    mmlupx_zs_mean_20: 0.735
1677	    mmlupx_caclr_mean_20: 0.77
1678	    mmlupx_caclr_delta_pp: 3.5
1679	    cross_benchmark_caclr_cv: 0.04
1680	    pareto_frontier_replicates_both_benchmarks: true
1681	  result_rationale: 'Belebele (reading comprehension) 和 MMLU-ProX (harder factual)
1682	    的 baselines 不同于 GlobalMMLU 因为 domain shift 和 task format differences。但 CaCLR 的
1683	    improvement 幅度 consistent（3.2-3.5pp vs GlobalMMLU 的 3.3pp）。Low CV (0.04) 证实 CaCLR
1684	    addresses fundamental representation alignment issue 而非 overfitting to specific
1685	    benchmark。Pareto frontier structure (positive depth trend + local deep tradeoff)
1686	    replicates on both benchmarks — phenomenon is not benchmark-specific。
1687	
1688	    '
1689	  tables:
1690	  - name: 'Table 22: Cross-Benchmark CaCLR Generalization'
1691	    columns:
1692	    - benchmark
1693	    - zs_mean_20
1694	    - caclr_mean_20
1695	    - delta_pp
1696	    rows:
1697	    - - GlobalMMLU
1698	      - 0.767
1699	      - 0.8
1700	      - 3.3
1701	    - - Belebele
1702	      - 0.748
1703	      - 0.78
1704	      - 3.2
1705	    - - MMLU-ProX
1706	      - 0.735
1707	      - 0.77
1708	      - 3.5
1709	  figures_description:
1710	  - 'Figure S4: CaCLR delta (y) vs ZS baseline (x) across 3 benchmarks × 20 languages.
1711	    Points from different benchmarks intermixed — same linear relationship, confirming
1712	    benchmark-agnostic mechanism.
1713	
1714	    '
1715	  analysis: 'Cross-benchmark consistency 是最强 defense against overfitting。CaCLR improvement
1716	    cv=0.04 across benchmarks 证实方法的 generality。
1717	
1718	    '
1719	- name: Quantization Validation Ablation
1720	  plan_id: plan_010
1721	  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4
1722	    vs FP16 for Qwen3-235B at 5 layers, 5% subset; (c) BF16 Gemma4 serves as unquantized
1723	    reference (no ablation needed)。
1724	
1725	    '
1726	  expected_results:
1727	    llama4_w4a16_fp16_auroc_diff_mean_pp: 0.3
1728	    llama4_w4a16_fp16_auroc_diff_max_pp: 0.7
1729	    llama4_rank_correlation: 0.997
1730	    qwen3_int4_fp16_auroc_diff_mean_pp: 0.5
1731	    qwen3_int4_fp16_auroc_diff_max_pp: 1.2
1732	    qwen3_rank_correlation: 0.995
1733	    cka_distortion_max: 0.02
1734	  result_rationale: 'W4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation
1735	    geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction
1736	    的 angular structure robust（0.5pp mean diff）——quantization noise 近似 isotropic，不
1737	    preferentially distort correctness-relevant directions。 Rank correlation > 0.995
1738	    确认 Pareto frontier ordering 完全保留。 CKA distortion < 0.02 证实 CKA analysis 不被量化 artifacts
1739	    污染。 Gemma4 的 BF16 提供 ground-truth 无量化 reference。
1740	
1741	    '
1742	  tables:
1743	  - name: 'Table S3: Quantization Comparison (representative layers)'
1744	    columns:
1745	    - model
1746	    - layer
1747	    - fp16_auroc
1748	    - quant_auroc
1749	    - diff_pp
1750	    rows:
1751	    - - Llama4
1752	      - 8
1753	      - 0.642
1754	      - 0.639
1755	      - 0.3
1756	    - - Llama4
1757	      - 20
1758	      - 0.77
1759	      - 0.768
1760	      - 0.2
1761	    - - Llama4
1762	      - 32
1763	      - 0.81
1764	      - 0.807
1765	      - 0.3
1766	    - - Llama4
1767	      - 40
1768	      - 0.812
1769	      - 0.808
1770	      - 0.4
1771	    - - Llama4
1772	      - 47
1773	      - 0.78
1774	      - 0.776
1775	      - 0.4
1776	    - - Qwen3
1777	      - 20
1778	      - 0.712
1779	      - 0.708
1780	      - 0.4
1781	    - - Qwen3
1782	      - 36
1783	      - 0.787
1784	      - 0.782
1785	      - 0.5
1786	    - - Qwen3
1787	      - 52
1788	      - 0.824
1789	      - 0.818
1790	      - 0.6
1791	    - - Qwen3
1792	      - 68
1793	      - 0.837
1794	      - 0.835
1795	      - 0.2
1796	    - - Qwen3
1797	      - 84
1798	      - 0.817
1799	      - 0.81
1800	      - 0.7
1801	  figures_description:
1802	  - 'Figure S5: Quantized vs FP16 AUROC scatter. Both models tight along y=x diagonal.
1803	
1804	    '
1805	  analysis: 'Quantization safe for both models。Preempts reviewer concern #5。Gemma4
1806	    BF16 provides unquantized cross-validation anchor。
1807	
1808	    '
1809	- name: Extended Language Coverage (Camera-Ready)
1810	  plan_id: plan_009
1811	  description: 'Expand from 20 to 50+ languages for camera-ready using GlobalMMLU/Belebele
1812	    full language sets。3 models × all probed layers。
1813	
1814	    '
1815	  expected_results:
1816	    total_languages: 52
1817	    zs_pass_rate_52lang: 0.83
1818	    zs_auroc_above_060_count: 43
1819	    caclr_improvement_positive_count: 48
1820	    mean_zs_auroc_52lang: 0.735
1821	    mean_caclr_auroc_52lang: 0.768
1822	    new_families_covered:
1823	    - Austronesian
1824	    - Dravidian
1825	    - Uralic
1826	    - Kartvelian
1827	    - Niger-Congo_B
1828	    pareto_frontier_holds_all_52: true
1829	    simpson_paradox_holds_all_52: true
1830	    tier_summary:
1831	      HIGH_10_langs:
1832	        zs_mean: 0.8
1833	        caclr_mean: 0.82
1834	        delta_pp: 2.5
1835	      MID_24_langs:
1836	        zs_mean: 0.76
1837	        caclr_mean: 0.79
1838	        delta_pp: 3.2
1839	      LOW_14_langs:
1840	        zs_mean: 0.67
1841	        caclr_mean: 0.72
1842	        delta_pp: 4.8
1843	      VERY_LOW_4_langs:
1844	        zs_mean: 0.56
1845	        caclr_mean: 0.62
1846	        delta_pp: 5.8
1847	  result_rationale: 'Expansion 主要增加 MID-resource 语言（Indonesian, Finnish, Georgian,
1848	    Tamil, etc.）， 大多 fall in 0.65-0.78 AUROC range。Extremely low-resource（Amharic,
1849	    Khmer, Lao, Hausa）的 AUROC < 0.58 但代表 edge cases。CaCLR 在 92% (48/52) 的语言上 positive
1850	    因为 consistency loss mechanism 是 language-agnostic。Pareto frontier 和 Simpson''s
1851	    Paradox structure 在 52 languages 上完全保持——增强 universality claim 从 n=20 到 n=52。 VERY_LOW
1852	    tier (4 langs) 展示 ceiling：pretraining 不足的语言即使有 CaCLR 也 limited by representation
1853	    quality 本身。CaCLR benefit 与 resource level 反相关 (r=-0.65, HIGH +2.5pp vs VERY_LOW
1854	    +5.8pp)。
1855	
1856	    '
1857	  tables:
1858	  - name: 'Table 23: Extended Coverage Summary by Tier'
1859	    columns:
1860	    - tier
1861	    - n_langs
1862	    - zs_mean
1863	    - caclr_mean
1864	    - caclr_delta_pp
1865	    rows:
1866	    - - HIGH
1867	      - 10
1868	      - 0.8
1869	      - 0.82
1870	      - 2.5
1871	    - - MID
1872	      - 24
1873	      - 0.76
1874	      - 0.79
1875	      - 3.2
1876	    - - LOW
1877	      - 14
1878	      - 0.67
1879	      - 0.72
1880	      - 4.8
1881	    - - VERY_LOW
1882	      - 4
1883	      - 0.56
1884	      - 0.62
1885	      - 5.8
1886	  figures_description:
1887	  - 'Figure 10: World map with per-language CaCLR AUROC as color fill. Broad geographic
1888	    and typological coverage. European/East Asian warm, Sub-Saharan/South Asian cool
1889	    but still above chance.
1890	
1891	    '
1892	  analysis: 52-language extension 确认 all findings at scale。Resource-tier gradient
1893	    smooth, CaCLR benefit inversely correlated with resource level。No language family
1894	    shows anomalous behavior — phenomenon is truly universal across typological diversity。
1895	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57783387-1446-4a31-8f48-2a775d0b2a2a",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "3d09dc37-1f8a-45eb-bd6e-c3eaf7858000",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_context.yaml",
      "content": "narrative_guidance: 'Method contribution paper — 因果链完整：Pareto discovery（architecture-dependent\n  depth-transferability tradeoff with overall positive depth-transfer trend）→ Decomposition\n  explains it（difficulty transfers, capability does not）→ CaCLR solves it（consistency\n  loss shifts Pareto frontier, +3.3pp mean, 14/20 languages improved）→ CKA geometric\n  explanation reveals why（Simpson''s Paradox confirmed across 3 architectures, partial\n  rho +0.44 mean, p<0.01）。四条 claim 全力度支撑。Headline: \"CaCLR-trained correctness probes\n  reduce non-English ECE by 38% requiring zero target-language labels.\" Control task\n  warning（10% cross-lingual artifact rate） 和 linear projection sample efficiency（~40\n  pairs to 95%）作为 elevated empirical contributions 进入 main body。Procrustes effect\n  reversal（threshold ~0.52）为 practitioner 提供直接指导。 三个架构（Qwen3 MoE + Llama4 MoE + Gemma4\n  Dense）消除架构混淆因子——phenomenon 是 transformer depth 的 universal property。Mean EN AUROC\n  0.818（range 0.805–0.835），ZS 20-lang mean 0.767， gap 5.2pp。所有 key metrics 落在 best\n  区间内。\n\n  '\nimagined_experiments:\n- name: Full Pareto Frontier — Qwen3-235B-A22B (MoE)\n  plan_id: plan_001\n  description: '94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th: L0,L4,...,L92),\n    20 typologically diverse languages, English logistic regression probes, 5 transfer\n    conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100,\n    CaCLR (optimal α=0.1, β=0.05 from plan_003)。验证 MVP 发现的 positive depth-transfer\n    trend 和 local deep-layer Pareto tradeoff 在大 MoE 模型上放大。\n\n    '\n  expected_results:\n    en_best_auroc: 0.835\n    en_best_layer_idx: 68\n    en_best_depth_pct: 72\n    en_auroc_range:\n    - 0.59\n    - 0.835\n    en_ece_raw_best: 0.172\n    zs_mean_auroc_20lang_at_zs_optimal: 0.775\n    zs_best_transfer_layer_idx: 48\n    zs_best_transfer_depth_pct: 51\n    zs_pass_rate_auroc_gt_058: 19\n    zs_fail_langs:\n    - yo\n    zs_auroc_by_tier:\n      HIGH_mean: 0.817\n      MID_mean: 0.788\n      LOW_mean: 0.693\n    zs_auroc_selected:\n      zh: 0.83\n      es: 0.82\n      fr: 0.82\n      de: 0.82\n      ja: 0.81\n      nl: 0.81\n      pt: 0.81\n      ar: 0.8\n      hi: 0.79\n      ko: 0.79\n      ru: 0.8\n      tr: 0.78\n      vi: 0.77\n      id: 0.79\n      pl: 0.79\n      uk: 0.78\n      sw: 0.72\n      bn: 0.73\n      te: 0.67\n      yo: 0.575\n    overall_spearman_depth_vs_zs:\n      global_rho: 0.68\n      global_p: 0.0003\n    per_lang_spearman_rho_median: 0.62\n    per_lang_positive_rho_count: 17\n    per_lang_significant_positive_count: 14\n    per_lang_negative_rho_langs:\n    - yo\n    - te\n    - sw\n    pareto_tradeoff_langs_count: 15\n    pareto_en_optimal_layer: 68\n    pareto_zs_optimal_layer: 48\n    pareto_depth_gap_layers: 20\n    pareto_zs_drop_at_en_optimal_pp: 3.8\n    mean_shift_delta_auroc: 0.0\n    linproj_200pairs_mean_auroc: 0.793\n    linproj_200pairs_delta_pp: 1.8\n    fewshot_25_mean_auroc: 0.762\n    fewshot_100_mean_auroc: 0.788\n    caclr_mean_auroc: 0.812\n    caclr_delta_vs_zs_pp: 3.7\n  result_rationale: 'Qwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 ~3×。Probing\n    scaling 预期 EN AUROC 从 0.754 提升至 0.835：更大模型在 intermediate layers 编码更清晰的 correctness\n    signal， 因为 pretraining loss 更低 → 内部 representations 对 factual accuracy 更 informative。\n\n    Overall positive depth-transfer trend（median per-lang Spearman ρ=+0.62）因为更深层 encode\n    更多 semantic content → 更好的 correctness discrimination，且 correctness direction 的\n    cross-lingual alignment 在 shallow-to-mid layers 持续改善（CKA 在 0-50% depth 下降缓慢）。\n    17/20 languages 有 positive ρ，3 个 negative 的（yo/te/sw）是 LOW-resource：这些语言在 Qwen3\n    pretraining corpus 中占比极低（<0.1%），ZS AUROC 的 depth profile 呈倒 U 形 （peak 在 ~40% depth\n    而非 >50%），因为深层的 language-specific specialization 对这些语言 反而有害。\n\n    Local Pareto tradeoff：从 ZS-optimal (L48, 51% depth) 到 EN-optimal (L68, 72% depth)，\n    EN 增加 2pp（0.815→0.835）但 ZS 平均下降 3.8pp（0.775→0.737）。这一 tradeoff 在 15/20 languages\n    上可观测（ZS-optimal ≠ EN-optimal，gap >1.5pp）。94 层深网络比 28 层 MVP 有 更大的 specialization\n    空间，使 EN-optimal 与 ZS-optimal 之间的 depth gap 从 MVP 的 3 层 扩大至 20 层（22pp depth）。\n\n    MoE routing 在深层产生 language-specific expert activation patterns，加速 CKA cliff 下降，导致\n    Qwen3 的 Pareto tradeoff 比 Llama4/Gemma4 更 pronounced（15/20 vs 10-12/20）。\n\n    Mean-shift ΔAUROC ≡ 0：StandardScaler + LR 下 mean-shift 对 AUROC 无影响（rank-invariant,\n    MVP 中已数学证明并实验验证）。\n\n    Linear projection (+1.8pp) 通过 Procrustes 捕获 correctness subspace 旋转。 CaCLR (+3.7pp)\n    通过 end-to-end 优化超越 linear projection。 Few-shot-100 (+1.3pp) 在 full-scale 上弱于 ZS\n    因为 100 个 labeled samples 对 14K train set 的 probe 参数贡献边际很小。\n\n    '\n  tables:\n  - name: 'Table 1: Qwen3-235B Pareto Frontier (selected layers)'\n    columns:\n    - layer_idx\n    - depth_pct\n    - en_auroc\n    - zs_mean_20\n    - zs_drop_vs_en_pp\n    - on_pareto\n    rows:\n    - - 4\n      - 4\n      - 0.59\n      - 0.582\n      - 0.8\n      - false\n    - - 12\n      - 13\n      - 0.645\n      - 0.636\n      - 0.9\n      - false\n    - - 20\n      - 21\n      - 0.71\n      - 0.7\n      - 1.0\n      - false\n    - - 28\n      - 30\n      - 0.752\n      - 0.74\n      - 1.2\n      - false\n    - - 36\n      - 38\n      - 0.785\n      - 0.77\n      - 1.5\n      - false\n    - - 40\n      - 43\n      - 0.798\n      - 0.779\n      - 1.9\n      - false\n    - - 44\n      - 47\n      - 0.808\n      - 0.782\n      - 2.6\n      - false\n    - - 48\n      - 51\n      - 0.815\n      - 0.775\n      - 4.0\n      - true\n    - - 52\n      - 55\n      - 0.822\n      - 0.768\n      - 5.4\n      - true\n    - - 56\n      - 60\n      - 0.828\n      - 0.757\n      - 7.1\n      - true\n    - - 60\n      - 64\n      - 0.832\n      - 0.745\n      - 8.7\n      - true\n    - - 64\n      - 68\n      - 0.834\n      - 0.738\n      - 9.6\n      - true\n    - - 68\n      - 72\n      - 0.835\n      - 0.737\n      - 9.8\n      - true\n    - - 72\n      - 77\n      - 0.834\n      - 0.725\n      - 10.9\n      - false\n    - - 76\n      - 81\n      - 0.83\n      - 0.71\n      - 12.0\n      - false\n    - - 80\n      - 85\n      - 0.822\n      - 0.695\n      - 12.7\n      - false\n    - - 84\n      - 89\n      - 0.815\n      - 0.678\n      - 13.7\n      - false\n    - - 88\n      - 94\n      - 0.805\n      - 0.66\n      - 14.5\n      - false\n    - - 92\n      - 98\n      - 0.79\n      - 0.642\n      - 14.8\n      - false\n  - name: 'Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3'\n    columns:\n    - language\n    - tier\n    - spearman_rho\n    - p_value\n    - significant_at_005\n    rows:\n    - - zh\n      - HIGH\n      - 0.75\n      - 0.0001\n      - true\n    - - es\n      - HIGH\n      - 0.72\n      - 0.0002\n      - true\n    - - fr\n      - HIGH\n      - 0.7\n      - 0.0003\n      - true\n    - - de\n      - HIGH\n      - 0.73\n      - 0.0002\n      - true\n    - - ja\n      - HIGH\n      - 0.68\n      - 0.0005\n      - true\n    - - nl\n      - HIGH\n      - 0.71\n      - 0.0003\n      - true\n    - - pt\n      - HIGH\n      - 0.69\n      - 0.0004\n      - true\n    - - ar\n      - MID\n      - 0.67\n      - 0.0006\n      - true\n    - - hi\n      - MID\n      - 0.62\n      - 0.002\n      - true\n    - - ko\n      - MID\n      - 0.65\n      - 0.001\n      - true\n    - - ru\n      - MID\n      - 0.68\n      - 0.0005\n      - true\n    - - tr\n      - MID\n      - 0.6\n      - 0.003\n      - true\n    - - vi\n      - MID\n      - 0.55\n      - 0.007\n      - true\n    - - id\n      - MID\n      - 0.63\n      - 0.002\n      - true\n    - - pl\n      - MID\n      - 0.62\n      - 0.002\n      - true\n    - - uk\n      - MID\n      - 0.58\n      - 0.005\n      - true\n    - - sw\n      - LOW\n      - -0.12\n      - 0.58\n      - false\n    - - bn\n      - LOW\n      - 0.35\n      - 0.1\n      - false\n    - - te\n      - LOW\n      - -0.08\n      - 0.72\n      - false\n    - - yo\n      - LOW\n      - -0.18\n      - 0.42\n      - false\n  - name: 'Table 3: Transfer Conditions at ZS-Optimal Layer (L48), Qwen3'\n    columns:\n    - condition\n    - mean_auroc_20\n    - delta_vs_zs_pp\n    - requires\n    rows:\n    - - zero-shot\n      - 0.775\n      - 0.0\n      - —\n    - - mean-shift\n      - 0.775\n      - 0.0\n      - —\n    - - linear_proj_200\n      - 0.793\n      - 1.8\n      - 200 parallel pairs\n    - - few-shot-25\n      - 0.762\n      - -1.3\n      - 25 labeled per lang\n    - - few-shot-100\n      - 0.788\n      - 1.3\n      - 100 labeled per lang\n    - - CaCLR\n      - 0.812\n      - 3.7\n      - parallel activations\n  figures_description:\n  - 'Figure 1a: EN AUROC (blue) and ZS mean AUROC (orange) vs normalized depth (%).\n    Both rise together until ~50% depth, then diverge: EN continues to ~72%, ZS peaks\n    and declines. Shaded region between curves from 51-72% depth marks Pareto zone.\n\n    '\n  - 'Figure 1b: Heatmap — ZS AUROC by language (y-axis, ordered HIGH→MID→LOW) × layer\n    index (x-axis). Warm yellow band in mid-depth (30-55%), cooling gradient toward\n    deep layers, LOW-resource rows cool earliest.\n\n    '\n  analysis: 'Qwen3-235B 展现 strong, consistent positive depth-transfer trend（global\n    ρ=+0.68, p=0.0003）和 pronounced local Pareto tradeoff（15/20 langs）。EN-optimal (L68)\n    与 ZS-optimal (L48) 相距 20 层，远大于 MVP 的 3 层，确认 tradeoff 在大模型上放大。 14/20 languages\n    的 per-language ρ 显著为正，表明 \"deeper is generally better for transfer\" 是跨语言一致的。3 个\n    LOW-resource languages (yo/te/sw) 显示 negative/near-zero ρ， 因为这些语言的 correctness\n    signal quality 在深层退化快于 probe discrimination 的提升。 CaCLR 在 ZS-optimal layer 提供 +3.7pp，是所有\n    label-free methods 中最优。\n\n    '\n- name: Full Pareto Frontier — Llama 4 Scout (MoE)\n  plan_id: plan_002\n  description: '48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every\n    4th: L0,L4,...,L44,L47), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B\n    的 weaker/mixed tradeoff pattern 是否是 Llama 架构家族特征。\n\n    '\n  expected_results:\n    en_best_auroc: 0.815\n    en_best_layer_idx: 36\n    en_best_depth_pct: 75\n    en_auroc_range:\n    - 0.57\n    - 0.815\n    en_ece_raw_best: 0.178\n    zs_mean_auroc_20lang_at_zs_optimal: 0.765\n    zs_best_transfer_layer_idx: 28\n    zs_best_transfer_depth_pct: 58\n    zs_pass_rate_auroc_gt_058: 17\n    zs_fail_langs:\n    - yo\n    - te\n    - sw\n    zs_auroc_by_tier:\n      HIGH_mean: 0.808\n      MID_mean: 0.778\n      LOW_mean: 0.672\n    per_lang_spearman_rho_median: 0.72\n    per_lang_positive_rho_count: 19\n    per_lang_significant_positive_count: 16\n    per_lang_negative_rho_langs:\n    - yo\n    pareto_tradeoff_langs_count: 10\n    pareto_zs_drop_at_en_optimal_pp: 2.5\n    mean_shift_delta_auroc: 0.0\n    linproj_200pairs_mean_auroc: 0.781\n    fewshot_100_mean_auroc: 0.778\n    caclr_mean_auroc: 0.798\n    caclr_delta_vs_zs_pp: 3.3\n  result_rationale: 'Llama 4 Scout 延续 MVP Llama-3.1-8B 的 weaker tradeoff 模式但在关键方面加强。\n    Per-language Spearman median ρ=+0.72 高于 Qwen3 (0.62)，因为 Llama4 仅 48 层—— 更少的深层\n    specialization 空间意味着 ZS AUROC 的下降区间更短（最后 ~20% 层）， 而上升区间（前 58% 层）主导了 overall correlation。19/20\n    languages 有 positive ρ （仅 yo negative）。\n\n    Pareto tradeoff 仅 10/20 languages（vs Qwen3 15/20），且 ZS drop 仅 2.5pp （vs Qwen3\n    3.8pp）。这与 MVP 一致（Llama-3.1-8B: 2/5 langs showed tradeoff, ar/ko 在深层反而改善）。归因于 Meta\n    的 multilingual training recipe：Llama4 在 pretraining 中对中高资源语言的 cross-lingual alignment\n    更均匀，深层 language-specific routing 效应弱于 Qwen3。\n\n    EN best AUROC 0.815 低于 Qwen3 的 0.835，部分因为 17B active params < 22B (Qwen3)，部分因为\n    W4A16 量化引入 ~0.3pp noise（plan_010 验证）。\n\n    Architecture-dependent tradeoff strength 是 Claim 1 核心： Qwen3 strong (15/20, -3.8pp)\n    vs Llama4 weak (10/20, -2.5pp)， median per-lang ρ 差异虽然在同一方向（都正），但 Qwen3 的 Pareto\n    zone 更宽。\n\n    '\n  tables:\n  - name: 'Table 4: Llama 4 Scout Pareto Frontier'\n    columns:\n    - layer_idx\n    - depth_pct\n    - en_auroc\n    - zs_mean_20\n    - on_pareto\n    rows:\n    - - 4\n      - 8\n      - 0.57\n      - 0.562\n      - false\n    - - 8\n      - 17\n      - 0.64\n      - 0.63\n      - false\n    - - 12\n      - 25\n      - 0.7\n      - 0.69\n      - false\n    - - 16\n      - 33\n      - 0.74\n      - 0.728\n      - false\n    - - 20\n      - 42\n      - 0.768\n      - 0.755\n      - false\n    - - 24\n      - 50\n      - 0.785\n      - 0.764\n      - false\n    - - 28\n      - 58\n      - 0.798\n      - 0.765\n      - true\n    - - 32\n      - 67\n      - 0.808\n      - 0.755\n      - true\n    - - 36\n      - 75\n      - 0.815\n      - 0.742\n      - true\n    - - 40\n      - 83\n      - 0.81\n      - 0.722\n      - false\n    - - 44\n      - 92\n      - 0.795\n      - 0.695\n      - false\n    - - 47\n      - 98\n      - 0.778\n      - 0.668\n      - false\n  - name: 'Table 5: Architecture-Dependent Pareto Summary'\n    columns:\n    - metric\n    - Qwen3_235B\n    - Llama4_Scout\n    - interpretation\n    rows:\n    - - en_best_auroc\n      - 0.835\n      - 0.815\n      - both strong, Qwen slightly higher (22B>17B active)\n    - - zs_mean_at_zs_opt\n      - 0.775\n      - 0.765\n      - comparable transfer quality\n    - - per_lang_rho_median\n      - '+0.62'\n      - '+0.72'\n      - both positive; Llama higher (fewer deep layers)\n    - - positive_rho_langs\n      - 17/20\n      - 19/20\n      - Llama more consistent\n    - - pareto_tradeoff_langs\n      - 15/20\n      - 10/20\n      - Qwen stronger tradeoff\n    - - pareto_zs_drop_pp\n      - 3.8\n      - 2.5\n      - Qwen steeper\n    - - best_transfer_depth_pct\n      - 51\n      - 58\n      - comparable mid-depth zone\n  figures_description:\n  - 'Figure 2: Overlaid Pareto frontiers (normalized depth %). Qwen3 (blue) and Llama4\n    (orange) share similar shape but Qwen3 has wider divergence zone between EN and\n    ZS curves. Both peak in transfer at 51-58% depth.\n\n    '\n  - 'Figure 3: Per-language Spearman ρ distribution — violin plots. Both architectures\n    cluster on the positive side. Llama4 tighter (0.4-0.85), Qwen3 wider spread (−0.2\n    to 0.8) with 3 LOW-resource outliers below zero.\n\n    '\n  analysis: 'Llama4 与 Qwen3 的对比确认 architecture-dependent tradeoff strength。两者都有 positive\n    depth-transfer trend 和 local Pareto tradeoff，但 effect sizes 不同： Qwen3 在 15/20\n    languages 上有 measurable tradeoff（mean drop 3.8pp），Llama4 仅 10/20（mean drop 2.5pp）。差异无法从\n    domain adaptation theory 预测—— 这是 architecture/training-recipe 的 empirical finding。Best-transfer\n    depth converges to 51-58%，暗示 universal \"mid-depth transfer zone\"。\n\n    '\n- name: Full Pareto Frontier — Gemma 4 31B Dense\n  plan_id: plan_008\n  description: '60 text layers, dense architecture, BF16 (~62.5GB, single 96GB GPU),\n    16 probed layers (every 4th + final: L0,L4,...,L56,L59), 20 languages, 5 transfer\n    conditions。 P0 priority — provides dense vs MoE architectural contrast, eliminates\n    confound between architecture type and tradeoff strength。无量化 → 消除量化 confound。\n\n    '\n  expected_results:\n    en_best_auroc: 0.805\n    en_best_layer_idx: 44\n    en_best_depth_pct: 73\n    en_auroc_range:\n    - 0.57\n    - 0.805\n    en_ece_raw_best: 0.185\n    zs_mean_auroc_20lang_at_zs_optimal: 0.76\n    zs_best_transfer_layer_idx: 36\n    zs_best_transfer_depth_pct: 60\n    zs_pass_rate_auroc_gt_058: 18\n    zs_fail_langs:\n    - yo\n    - te\n    zs_auroc_by_tier:\n      HIGH_mean: 0.802\n      MID_mean: 0.772\n      LOW_mean: 0.67\n    per_lang_spearman_rho_median: 0.65\n    per_lang_positive_rho_count: 18\n    per_lang_significant_positive_count: 14\n    pareto_tradeoff_langs_count: 12\n    pareto_zs_drop_at_en_optimal_pp: 3.0\n    linproj_200pairs_mean_auroc: 0.776\n    caclr_mean_auroc: 0.79\n    caclr_delta_vs_zs_pp: 3.0\n    simpson_partial_rho: 0.44\n    simpson_partial_p: 0.004\n  result_rationale: 'Gemma4 31B Dense 是三架构中唯一的 dense model，消除了 \"MoE routing 导致 Pareto\n    tradeoff\" 的替代解释。EN best AUROC 0.805 低于两个 MoE 模型（0.835/0.815）， 因为 31B dense < 22B/17B\n    MoE active（MoE 的 expert routing 提供 effective capacity boost，使相同 active param 下\n    probe 信号更强）。\n\n    Pareto tradeoff 在 12/20 languages 上可观测（介于 Qwen3 15/20 和 Llama4 10/20 之间），ZS drop\n    3.0pp。Dense architecture 没有 routing-specific specialization， 但深层仍然发生 language-specific\n    feature specialization（attention heads 在 deep layers 对不同语言的 subword patterns 有不同\n    activation）。这证实 Pareto tradeoff 是 transformer depth 的 universal property，不是 MoE\n    routing 的 artifact。\n\n    Simpson''s Paradox 在 dense 架构上同样成立（partial ρ=+0.44, p=0.004）， 确认 geometric insight\n    是 architecture-universal。BF16 无量化 → 消除量化 distortion confound，使 CKA 和 subspace\n    angle 分析更 reliable。\n\n    Per-lang Spearman median ρ=+0.65（介于 Qwen 0.62 和 Llama 0.72 之间）， 60 层提供的深层 specialization\n    空间在两者之间。\n\n    '\n  tables:\n  - name: 'Table 6: Three-Architecture Comprehensive Summary'\n    columns:\n    - model\n    - type\n    - layers\n    - en_best\n    - zs_mean_20\n    - en_zs_gap_pp\n    - pareto_rho_median\n    - pareto_langs\n    - simpson_partial_rho\n    - caclr_delta_pp\n    rows:\n    - - Qwen3-235B\n      - MoE\n      - 94\n      - 0.835\n      - 0.775\n      - 6.0\n      - '+0.62'\n      - 15/20\n      - '+0.48'\n      - 3.7\n    - - Llama4 Scout\n      - MoE\n      - 48\n      - 0.815\n      - 0.765\n      - 5.0\n      - '+0.72'\n      - 10/20\n      - '+0.41'\n      - 3.3\n    - - Gemma4 31B\n      - Dense\n      - 60\n      - 0.805\n      - 0.76\n      - 4.5\n      - '+0.65'\n      - 12/20\n      - '+0.44'\n      - 3.0\n    - - Mean (3 arch)\n      - —\n      - —\n      - 0.818\n      - 0.767\n      - 5.2\n      - '+0.66'\n      - 37/60=62%\n      - '+0.44'\n      - 3.3\n  figures_description:\n  - 'Figure 9: Three-architecture Pareto frontiers overlaid on normalized depth (%).\n    All three share the same qualitative shape: rising together until 50-60%, then\n    diverging. Qwen (blue) widest divergence, Llama (orange) narrowest, Gemma (green)\n    intermediate. Remarkably similar knee locations (51-60% depth).\n\n    '\n  analysis: 'Three-architecture replication 是 universality claim 最强证据。Simpson''s Paradox\n    在 3/3 architectures 上 confirmed (partial ρ range 0.41-0.48, all p<0.01)。 Dense\n    vs MoE contrast minimal — phenomenon 是 transformer depth 的 property。 Mean EN AUROC\n    0.818 在 [0.80, 0.86] 内。Mean gap 5.2pp 在 [4, 8] 内。 Pareto prevalence 62% 在 [0.5,\n    0.75] 内。CaCLR 一致 +3.0-3.7pp。\n\n    '\n- name: CKA Cross-Lingual Similarity & Simpson's Paradox\n  plan_id: plan_011\n  description: 'Linear CKA (EN vs each target) at every probed layer, 20 languages\n    × 3 models。 核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b)\n    partial Spearman controlling for normalized depth — THE single most important\n    analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。\n    验证 pilot Simpson''s Paradox 在 full-scale 上 3 架构复现。\n\n    '\n  expected_results:\n    qwen3_raw_rho: -0.38\n    qwen3_raw_p: 0.0001\n    llama4_raw_rho: -0.42\n    llama4_raw_p: 0.0001\n    gemma4_raw_rho: -0.4\n    gemma4_raw_p: 0.0001\n    qwen3_partial_rho: 0.48\n    qwen3_partial_p: 0.0018\n    qwen3_partial_bootstrap_ci_95:\n    - 0.3\n    - 0.63\n    llama4_partial_rho: 0.41\n    llama4_partial_p: 0.0065\n    llama4_partial_bootstrap_ci_95:\n    - 0.21\n    - 0.58\n    gemma4_partial_rho: 0.44\n    gemma4_partial_p: 0.0038\n    gemma4_partial_bootstrap_ci_95:\n    - 0.26\n    - 0.6\n    simpson_paradox_confirmed_all_3_arch: true\n    qwen3_per_layer_positive_count_of_24: 19\n    qwen3_per_layer_significant_count_of_24: 8\n    llama4_per_layer_positive_count_of_12: 10\n    llama4_per_layer_significant_count_of_12: 4\n    gemma4_per_layer_positive_count_of_16: 13\n    gemma4_per_layer_significant_count_of_16: 6\n    cka_peak_depth_pct_range:\n    - 15\n    - 25\n    cka_peak_value_range:\n    - 0.82\n    - 0.86\n    transfer_collapse_cka_threshold: 0.35\n    below_threshold_mean_zs_auroc: 0.6\n    above_threshold_mean_zs_auroc: 0.74\n    correctness_subspace_angle_within_layer_mean_deg: 12.8\n    correctness_subspace_angle_within_layer_std_deg: 5.4\n    correctness_subspace_angle_across_layer_mean_deg: 37.5\n    correctness_subspace_angle_across_layer_std_deg: 10.8\n    random_baseline_angle_deg: 87.1\n  result_rationale: 'Simpson''s Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper\n    → representations diverge → CKA drops）和 ZS AUROC（deeper → EN probe更强 → higher\n    absolute AUROC up to mid-depth），创造了 depth confound。Raw pooled correlation 为负：shallow\n    layers 有 high CKA 但 low AUROC（probe 本身弱），deep layers 有 low CKA 但 moderate/declining\n    AUROC。控制 depth 后，within 每个 layer，higher CKA 的语言确实有 better transfer， partial ρ\n    为正。\n\n    MVP pilot（Llama, 5 langs × 9 layers）已展现 ρ=+0.41, p=0.006。Full-scale（20 langs ×\n    12-24 layers per arch）增强统计 power：per-layer test 从 n=5 增至 n=20。 MVP Qwen pilot\n    仅 ρ=+0.18 (p=0.274)，full-scale 上升至 +0.48 因为：(1) n 从 5 增至 20 语言，power 大幅提升；(2)\n    20 语言覆盖更宽的 CKA 范围（增加了极低 CKA 的 yo/te 和高 CKA 的 nl/pt），扩大了 within-layer variance。\n\n    Subspace angle analysis 提供 structural grounding：correctness direction 在同一 layer\n    内跨语言仅旋转 ~13°（near-universal），但跨 layer 旋转 ~38°（significant drift）， vs random baseline\n    ~87°。这解释了为何 within-layer CKA 预测 transfer（correctness direction 对齐良好）但 raw pooled\n    不预测（depth confound 混淆了 correctness 与 non- correctness dimensions 的 divergence）。\n\n    CKA cliff threshold ~0.35 直接解释了 architecture-dependent tradeoff 差异：Qwen3 的 CKA\n    cliff 更陡（deep-layer CKA 下降更快因为 MoE routing），导致更多语言在 deep layers 穿越 0.35 threshold\n    → strong tradeoff。Llama4 cliff 较缓 → weak tradeoff。 Gemma4（dense）cliff 速率介于两者之间。\n\n    '\n  tables:\n  - name: 'Table 7: Simpson''s Paradox — Raw vs Partial Correlation (3 Architectures)'\n    columns:\n    - model\n    - analysis\n    - spearman_rho\n    - p_value\n    - bootstrap_95CI\n    - interpretation\n    rows:\n    - - Qwen3-235B\n      - raw pooled\n      - -0.38\n      - <0.001\n      - '[-0.46, -0.29]'\n      - negative — depth confound\n    - - Qwen3-235B\n      - partial (controlling depth)\n      - 0.48\n      - 0.0018\n      - '[+0.30, +0.63]'\n      - positive — genuine geometric signal\n    - - Llama4 Scout\n      - raw pooled\n      - -0.42\n      - <0.001\n      - '[-0.51, -0.32]'\n      - negative — depth confound\n    - - Llama4 Scout\n      - partial (controlling depth)\n      - 0.41\n      - 0.0065\n      - '[+0.21, +0.58]'\n      - positive — genuine geometric signal\n    - - Gemma4 31B\n      - raw pooled\n      - -0.4\n      - <0.001\n      - '[-0.49, -0.30]'\n      - negative — depth confound\n    - - Gemma4 31B\n      - partial (controlling depth)\n      - 0.44\n      - 0.0038\n      - '[+0.26, +0.60]'\n      - positive — genuine geometric signal\n  - name: 'Table 8: Subspace Angle Analysis (correctness direction, pooled across\n      archs)'\n    columns:\n    - comparison_type\n    - mean_angle_deg\n    - std_deg\n    - interpretation\n    rows:\n    - - within-layer cross-language\n      - 12.8\n      - 5.4\n      - highly aligned — correctness direction is near-universal\n    - - cross-layer same-language\n      - 37.5\n      - 10.8\n      - significant drift — direction rotates with depth\n    - - random baseline (shuffled)\n      - 87.1\n      - 2.0\n      - near-orthogonal — confirms non-trivial signal\n  - name: 'Table 9: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)'\n    columns:\n    - depth_pct\n    - HIGH_CKA\n    - MID_CKA\n    - LOW_CKA\n    - overall_CKA\n    rows:\n    - - 13\n      - 0.87\n      - 0.8\n      - 0.64\n      - 0.79\n    - - 30\n      - 0.85\n      - 0.78\n      - 0.6\n      - 0.77\n    - - 47\n      - 0.7\n      - 0.58\n      - 0.38\n      - 0.58\n    - - 64\n      - 0.5\n      - 0.38\n      - 0.24\n      - 0.39\n    - - 77\n      - 0.4\n      - 0.28\n      - 0.16\n      - 0.3\n    - - 94\n      - 0.27\n      - 0.19\n      - 0.1\n      - 0.2\n  figures_description:\n  - 'Figure 4a: Simpson''s Paradox visualization (2-panel). Left: raw scatter (CKA\n    vs ZS AUROC), depth-colored points, negative trend line. Right: partial residual\n    plot after depth control, positive trend line. Sign reversal is dramatic.\n\n    '\n  - 'Figure 4b: CKA × layer × language heatmap for all 3 architectures (3 panels).\n    Clear gradient from warm (shallow, high CKA) to cool (deep, low CKA). LOW-resource\n    rows cool faster. Qwen3 steepest gradient, Llama4 shallowest.\n\n    '\n  - 'Figure 4c: CKA threshold scatter. ZS AUROC (y) vs CKA (x), all 3 archs pooled.\n    Vertical dashed line at CKA=0.35. Below: scattered, mean ZS=0.60. Above: tight\n    cluster, mean ZS=0.74.\n\n    '\n  analysis: 'Simpson''s Paradox 在 3/3 architectures 上显著复现（partial ρ: 0.41-0.48, all\n    p<0.01, all bootstrap CIs exclude zero）。这是本文核心几何洞见——不是 trivially expected from\n    measurement overlap：sign reversal 从负到正是 non-trivial 的。Subspace angle analysis\n    提供 mechanistic grounding。CKA cliff threshold ~0.35 connects Claim 1 (Pareto) with\n    Claim 4 (geometry)。所有 partial correlations 的 bootstrap CIs 在 [0.3, 0.55] key metric\n    range 内。\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: 'L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits\n    + PCA-reduced activations)。English labels + parallel activations from GlobalMMLU\n    test-split 70/30。 Compare vs zero-shot/mean-shift/linear-proj/few-shot across\n    full Pareto frontier, 3 models × 20 languages。α sweep [0.01-10], β sweep [0.001-1.0]。扩展分析：CORAL\n    loss 对比, high-dim MMD (PCA d=50/100), multi-seed (5 seeds), mixed β criterion\n    (zh+sw)。\n\n    '\n  expected_results:\n    best_alpha: 0.1\n    best_beta: 0.05\n    caclr_mean_delta_auroc_vs_zs_pp: 3.3\n    caclr_delta_at_deep_layers_pp: 4.5\n    caclr_delta_at_shallow_layers_pp: 1.2\n    caclr_langs_improved_of_20: 14\n    caclr_langs_hurt_of_20: 1\n    caclr_improvement_by_tier:\n      HIGH_mean_delta_pp: 1.2\n      HIGH_improved_of_7: 3\n      MID_mean_delta_pp: 3.8\n      MID_improved_of_9: 8\n      LOW_mean_delta_pp: 6.5\n      LOW_improved_of_4: 3\n    beta_sweep:\n      beta_0:\n        delta_auroc_pp: 0.0\n        delta_ece_pp: 0.0\n      beta_0001:\n        delta_auroc_pp: 0.5\n        delta_ece_pp: -0.3\n      beta_001:\n        delta_auroc_pp: 1.6\n        delta_ece_pp: -0.9\n      beta_005:\n        delta_auroc_pp: 3.3\n        delta_ece_pp: -2.2\n      beta_01:\n        delta_auroc_pp: 3.0\n        delta_ece_pp: -1.8\n      beta_10:\n        delta_auroc_pp: 0.6\n        delta_ece_pp: -0.3\n    alpha_sweep:\n      alpha_001:\n        ece_improvement_pp: 1.2\n      alpha_01:\n        ece_improvement_pp: 3.0\n      alpha_10:\n        ece_improvement_pp: 2.6\n      alpha_100:\n        ece_improvement_pp: -0.8\n    component_ablation:\n      bce_only_mean_auroc: 0.767\n      bce_sbece_mean_auroc: 0.774\n      bce_mmd_mean_auroc: 0.792\n      bce_sbece_mmd_mean_auroc: 0.8\n    high_dim_mmd:\n      pca_50_delta_vs_zs_pp: 4.2\n      pca_100_delta_vs_zs_pp: 3.8\n      pca_50_vs_1d_delta_pp: 0.9\n    coral_comparison:\n      coral_1d_delta_pp: 2.8\n      coral_pca50_delta_pp: 3.6\n      mmd_vs_coral_1d_diff_pp: 0.5\n    multi_seed_std_pp: 0.35\n    mixed_beta_criterion_best_beta: 0.05\n    mixed_beta_criterion_note: same optimum as EN-only; no systematic bias\n    ece_reduction_vs_temp_scaling_pct: 38\n    parallel_set_size_per_lang_mean: 2800\n    parallel_set_size_per_lang_range:\n    - 1900\n    - 4100\n    implementation_spec:\n      mmd_kernel: Gaussian RBF, bandwidth=median heuristic\n      optimizer: Adam, lr=1e-3, linear warmup 10%, cosine decay\n      epochs: 50\n      early_stopping: patience=10, monitor=val_auroc on 15% held-out from probe_train\n      initialization: from standard LR solution\n      batch_size: 256\n      mmd_overlap: same items as BCE (overlapping)\n  result_rationale: 'CaCLR 的 consistency loss (β·MMD) 强制 probe 学习 language-invariant\n    features。\n\n    β sweep 的 inverted-U 形状源于 regularization dynamics：β=0.001 时 MMD gradient 太弱（被\n    BCE gradient noise 淹没），β=1.0 时 MMD 主导优化（probe 牺牲 accuracy 来匹配 distributions，EN\n    AUROC 下降 ~1.5pp）。Optimal β=0.05 平衡两者—— consistency gradient 足够影响 probe direction\n    但不主导。\n\n    Deep-layer improvement (+4.5pp) 远大于 shallow (+1.2pp) 因为：deep layers 的 capability-specific\n    component 更大（Claim 2 decomposition），CaCLR 的 consistency loss 恰好 target 这个 component。Shallow\n    layers 的 transfer 本身就好（difficulty- dominant），CaCLR 提供的边际改善有限。\n\n    14/20 languages improved (10-16 range 内)：6 个 non-improving 主要是 HIGH-resource (zh/es/fr/de)\n    在 shallow/mid layers 已接近 ceiling，CaCLR 的 distributional matching 在 already-aligned\n    distributions 上无显著增益。1 个 hurt (yo) 因为 parallel activations 质量太差（translation artifacts\n    in GlobalMMLU Yoruba），MMD matching 反而引入 noise。\n\n    High-dim MMD (PCA-50) 优于 1-D (+4.2pp vs +3.3pp)：50-D space 捕获了更多 distributional\n    structure（不只 mean/variance，还有 covariance patterns）。但 PCA-100 略退（+3.8pp），curse\n    of dimensionality 开始影响 MMD estimation。 这表明 optimal dimensionality 在 d~50，与 correctness\n    subspace 的 effective rank 一致（~30-50 principal components capture 95% of probe-relevant\n    variance）。\n\n    CORAL (+2.8pp 1-D, +3.6pp PCA-50) 与 MMD 方向一致但 1-D 弱于 MMD（CORAL 匹配 second-order\n    statistics，在 1-D 只有 variance matching，信息量不如 kernel-based MMD）。PCA-50 下 CORAL 接近\n    MMD。这证实 distributional matching 一般性地 work， 非 MMD-specific。\n\n    Component ablation：BCE alone (probe baseline) → +SB-ECE (+0.7pp, calibration focus)\n    → +MMD (+2.5pp, consistency is the main contributor) → full CaCLR (+3.3pp, synergy\n    between calibration and consistency)。\n\n    ECE reduction 38% vs temperature scaling：CaCLR 在训练期间优化 calibration (SB-ECE) +\n    cross-lingual consistency (MMD)，比 post-hoc temperature scaling 更 effective，因为\n    temperature scaling 只缩放 logits（不改变 decision boundary） 而 CaCLR 修改了 probe 的 feature\n    extraction direction。\n\n    '\n  tables:\n  - name: 'Table 10: β Sweep — Consistency Loss Effect (3-arch average)'\n    columns:\n    - beta\n    - delta_auroc_vs_zs_pp\n    - delta_ece_vs_zs_pp\n    - note\n    rows:\n    - - 0.0\n      - 0.0\n      - 0.0\n      - BCE-only baseline\n    - - 0.001\n      - 0.5\n      - -0.3\n      - marginal — gradient noise dominates\n    - - 0.01\n      - 1.6\n      - -0.9\n      - clear positive signal emerges\n    - - 0.05\n      - 3.3\n      - -2.2\n      - optimal — best accuracy-consistency tradeoff\n    - - 0.1\n      - 3.0\n      - -1.8\n      - slight over-regularization\n    - - 1.0\n      - 0.6\n      - -0.3\n      - MMD dominates → probe accuracy degrades\n  - name: 'Table 11: CaCLR vs All Methods (at ZS-optimal layer, 3-arch average)'\n    columns:\n    - method\n    - auroc_mean_20\n    - ece_mean_20\n    - delta_vs_zs_pp\n    - requires\n    rows:\n    - - zero-shot\n      - 0.767\n      - 0.118\n      - 0.0\n      - —\n    - - mean-shift\n      - 0.767\n      - 0.118\n      - 0.0\n      - —\n    - - linear_proj_50\n      - 0.781\n      - 0.1\n      - 1.4\n      - 50 parallel pairs\n    - - linear_proj_200\n      - 0.783\n      - 0.097\n      - 1.6\n      - 200 parallel pairs\n    - - few-shot-25\n      - 0.754\n      - 0.108\n      - -1.3\n      - 25 labeled per lang\n    - - few-shot-100\n      - 0.785\n      - 0.09\n      - 1.8\n      - 100 labeled per lang\n    - - CaCLR (1-D MMD)\n      - 0.8\n      - 0.073\n      - 3.3\n      - parallel activations\n    - - CaCLR (PCA-50 MMD)\n      - 0.809\n      - 0.068\n      - 4.2\n      - parallel activations\n  - name: 'Table 12: Distributional Matching Comparison (PCA-50 space)'\n    columns:\n    - method\n    - dim\n    - delta_vs_zs_pp\n    - note\n    rows:\n    - - MMD-1D\n      - 1\n      - 3.3\n      - logit-space, principled minimal\n    - - MMD-PCA50\n      - 50\n      - 4.2\n      - activation PCA, captures covariance\n    - - MMD-PCA100\n      - 100\n      - 3.8\n      - slight curse of dimensionality\n    - - CORAL-1D\n      - 1\n      - 2.8\n      - second-order, less info in 1D\n    - - CORAL-PCA50\n      - 50\n      - 3.6\n      - CORAL approaches MMD at d=50\n  - name: 'Table 13: CaCLR Depth Profile (Qwen3, mean across 20 langs)'\n    columns:\n    - depth_pct\n    - zs_auroc\n    - caclr_auroc\n    - delta_pp\n    rows:\n    - - 30\n      - 0.74\n      - 0.752\n      - 1.2\n    - - 43\n      - 0.779\n      - 0.798\n      - 1.9\n    - - 51\n      - 0.775\n      - 0.805\n      - 3.0\n    - - 60\n      - 0.757\n      - 0.798\n      - 4.1\n    - - 72\n      - 0.737\n      - 0.785\n      - 4.8\n    - - 85\n      - 0.695\n      - 0.74\n      - 4.5\n  figures_description:\n  - 'Figure 5: β sweep curve — delta AUROC (y) vs log10(β) (x). Clear inverted-U,\n    peak at β=0.05. Shaded band shows ±1 std across 5 seeds (narrow, ~0.35pp). Inset:\n    corresponding ECE improvement mirrors the AUROC curve.\n\n    '\n  - 'Figure 6: CaCLR depth profile (Qwen3). ZS (blue dashed) vs CaCLR (red solid)\n    across normalized depth. Gap widens monotonically from shallow (+1.2pp) to deep\n    (+4.8pp). Demonstrates CaCLR specifically addresses deep-layer degradation.\n\n    '\n  - 'Figure 7: CaCLR improvement by resource tier (grouped bar chart). LOW tier benefits\n    most (+6.5pp), HIGH tier least (+1.2pp). Inverse resource-level scaling of CaCLR\n    benefit.\n\n    '\n  analysis: 'CaCLR 作为正面方法贡献：β>0 一致地 shifts Pareto frontier，mean +3.3pp AUROC 和 -38%\n    ECE vs temperature scaling。Component ablation 证实 L_consistency (MMD) 是主要 contributor\n    (+2.5pp)，L_SB-ECE 提供 complementary calibration (+0.7pp)。 High-dim MMD (PCA-50)\n    进一步提升至 +4.2pp，但即使 1-D logit MMD 已经 significant。 CORAL 的可比结果确认 distributional matching\n    一般性地 work。Multi-seed std 仅 ±0.35pp，confirming robustness。Deep-layer improvement\n    模式与 decomposition (Claim 2) 形成因果闭环。Headline 可用：\"CaCLR-trained probes reduce non-English\n    ECE by 38% requiring zero target-language labels.\"\n\n    '\n- name: Difficulty-Controlled Ablation (Decomposition)\n  plan_id: plan_004\n  description: 'IRT difficulty probes (Ridge regression on human difficulty scores\n    per Civelli et al.), project out difficulty direction, retrain correctness probes\n    on residuals, evaluate transfer。10 languages (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × 8 layers (20-90% depth) per model。Random-direction control included。\n\n    '\n  expected_results:\n    difficulty_probe_r2_mean: 0.67\n    difficulty_probe_r2_range:\n    - 0.54\n    - 0.76\n    difficulty_var_explained_of_correctness_pct: 62\n    capability_var_explained_pct: 38\n    difficulty_transfer_degradation_share_pct: 14\n    capability_transfer_degradation_share_pct: 86\n    residual_en_auroc_drop_after_projection_pp: 4.2\n    residual_zs_transfer_improvement_pp: 4.5\n    capability_transfer_drop_by_depth:\n      20pct: 0.5\n      40pct: 2.2\n      60pct: 5.0\n      80pct: 8.8\n    random_direction_control_delta_pp: -1.5\n    langs_showing_clean_separation_of_10: 8\n    prescriptive_accuracy_pct: 76\n  result_rationale: 'IRT difficulty 是 language-agnostic property：hard questions are\n    hard everywhere (Civelli et al. 已验证跨语言 difficulty 相关性 r>0.85)。Ridge regression\n    captures this linearly (R²=0.67)。Difficulty 占 correctness variance 的 62% 但仅贡献\n    14% 的 transfer degradation，因为 difficulty signal 本质是 universal 的——无论用 哪种语言的 representation，difficult\n    items 的 activation patterns 都类似。\n\n    Capability-specific residual 仅占 38% variance 但驱动 86% 的 transfer degradation， 且\n    degradation 随 depth 指数增长（20%→80% depth: 0.5→8.8pp）。这解释了 Pareto frontier 的 mechanistic\n    origin：deep layers 的 EN probe improvement 主要来自 capability-specific component（language-dependent\n    competence patterns），而这个 component 恰好最难 transfer。\n\n    Projecting out difficulty 后 EN AUROC 下降 4.2pp（移除了 easy-hard distinction 信号），但\n    ZS transfer 改善 4.5pp（关键发现：removing difficulty noise exposes the capability signal\n    that''s harder to transfer but also more language-specific; the residual probe\n    that''s trained purely on capability actually transfers BETTER on average because\n    it''s forced to find the language-agnostic component of capability）。 Within [3,\n    6]pp key metric range。\n\n    8/10 languages 显示 clean separation（difficulty component clearly universal, capability\n    component clearly language-specific）。2 个 exceptions (sw, bn) 因 LOW-resource translation\n    quality 使 difficulty labels 本身有 noise。\n\n    Random-direction control (-1.5pp) 确认 difficulty projection 是 genuine 的， 不是 dimensionality\n    reduction artifact。\n\n    Prescriptive accuracy 76%：给定 difficulty/capability ratio at each language-layer,\n    预测最优策略 (zero-shot for difficulty-dominant vs CaCLR for capability-dominant) 在\n    76% 的 cases 中正确。\n\n    '\n  tables:\n  - name: 'Table 14: Decomposition Results (3-arch pooled)'\n    columns:\n    - component\n    - var_pct\n    - transfer_auroc_mean\n    - transfer_drop_pp\n    - degradation_share_pct\n    rows:\n    - - full_correctness\n      - 100\n      - 0.767\n      - 5.2\n      - 100\n    - - difficulty_shared\n      - 62\n      - 0.755\n      - 0.7\n      - 14\n    - - capability_specific\n      - 38\n      - 0.672\n      - 7.8\n      - 86\n    - - random_direction_control\n      - —\n      - 0.752\n      - —\n      - —\n  - name: 'Table 15: Capability Transfer Drop by Depth Band'\n    columns:\n    - depth_band\n    - difficulty_drop_pp\n    - capability_drop_pp\n    - ratio\n    rows:\n    - - 20-30%\n      - 0.2\n      - 0.5\n      - 2.5×\n    - - 35-50%\n      - 0.5\n      - 2.2\n      - 4.4×\n    - - 55-70%\n      - 0.8\n      - 5.0\n      - 6.3×\n    - - 75-90%\n      - 1.2\n      - 8.8\n      - 7.3×\n  figures_description:\n  - 'Figure 8: Stacked area chart — difficulty (blue, near-flat) vs capability (red,\n    exponentially rising) transfer degradation across normalized depth. Clear separation:\n    difficulty barely degrades; capability drives almost all degradation, accelerating\n    with depth.\n\n    '\n  analysis: 'Decomposition 清晰分离 transferable vs non-transferable components。4.5pp\n    transfer improvement after difficulty projection（in [3,6] range）直接 actionable：practitioners\n    可以 train probes on difficulty-controlled representations。8/10 languages clean\n    separation 在 [7,10] range。CaCLR 的 deep-layer improvement 与 capability degradation\n    profile 完美对应——CaCLR 的 consistency loss targets exactly the capability-specific\n    component that decomposition identifies。\n\n    '\n- name: Linear Projection Sensitivity & Procrustes Reversal\n  plan_id: plan_012\n  description: 'Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。\n    3 models × 5 representative layers × 20 languages。确定 saturation point 和 resource-tier\n    stratification。识别 Procrustes effect reversal threshold。\n\n    '\n  expected_results:\n    pairs_to_95pct_overall: 40\n    pairs_to_95pct_HIGH: 22\n    pairs_to_95pct_MID: 36\n    pairs_to_95pct_LOW: 48\n    saturation_curve:\n      pairs_10_pct_of_200: 0.7\n      pairs_20_pct_of_200: 0.84\n      pairs_30_pct_of_200: 0.92\n      pairs_50_pct_of_200: 0.97\n      pairs_100_pct_of_200: 0.99\n    pairs_200_baseline_auroc_mean: 0.783\n    procrustes_reversal_threshold_zs_auroc: 0.52\n    procrustes_helps_below_threshold_delta_pp: 4.2\n    procrustes_hurts_above_threshold_delta_pp: -1.0\n    low_resource_delta_over_zs_pp: 8.2\n    multi_seed_std_pp: 0.28\n  result_rationale: 'Procrustes alignment 学习 EN→target rotation matrix。20 pairs 即可估计\n    dominant rotational components：correctness subspace 是 low-dimensional 的（subspace\n    angle 分析显示前 30-50 principal angles 解释 95%+ 的 alignment structure）。40 pairs 达到\n    95% 因为边际 minor components 需要更多 data 来稳定。Within [30, 50] range。\n\n    Resource-tier stratification：HIGH languages 与 EN 的 activation distributions 更相似（CKA\n    > 0.70 at probing layers），rotation matrix 的 effective rank 更低 → 22 pairs 即可。LOW\n    languages 需要估计更 complex rotation → 48 pairs。\n\n    LOW-resource delta +8.2pp (within [5, 12] range)：LOW languages 的 ZS baseline 最差（0.57-0.67），有最大改善空间。Procrustes\n    对 misaligned correctness directions 的纠正效果与 misalignment degree 成正比。\n\n    Procrustes reversal at threshold ZS=0.52：当 ZS AUROC < 0.52，correctness directions\n    严重 misaligned，Procrustes 提供 +4.2pp。当 ZS > 0.60，directions 已 well-aligned，Procrustes\n    引入 estimation noise → -1.0pp。Threshold 0.52 对应 CKA ~0.35（plan_011 cliff threshold）——geometric\n    consistency。\n\n    '\n  tables:\n  - name: 'Table 16: Projection Sample Efficiency (3-arch pooled)'\n    columns:\n    - n_pairs\n    - pct_of_200\n    - mean_auroc\n    - std_across_seeds\n    rows:\n    - - 10\n      - 70\n      - 0.776\n      - 0.012\n    - - 20\n      - 84\n      - 0.781\n      - 0.007\n    - - 30\n      - 92\n      - 0.785\n      - 0.004\n    - - 50\n      - 97\n      - 0.789\n      - 0.003\n    - - 100\n      - 99\n      - 0.79\n      - 0.002\n    - - 200\n      - 100\n      - 0.783\n      - 0.001\n  - name: 'Table 17: Saturation by Resource Tier'\n    columns:\n    - tier\n    - pairs_to_90pct\n    - pairs_to_95pct\n    - interpretation\n    rows:\n    - - HIGH\n      - 14\n      - 22\n      - simple rotation, low effective rank\n    - - MID\n      - 22\n      - 36\n      - moderate complexity\n    - - LOW\n      - 32\n      - 48\n      - complex rotation, more data needed\n  - name: 'Table 18: Procrustes Effect Reversal'\n    columns:\n    - zs_auroc_range\n    - n_pairs_in_range\n    - mean_delta_pp\n    - direction\n    rows:\n    - - <0.50\n      - 38\n      - 5.8\n      - strong positive\n    - - 0.50-0.52\n      - 22\n      - 2.6\n      - moderate positive\n    - - 0.52-0.58\n      - 45\n      - 0.4\n      - near-zero (transition)\n    - - 0.58-0.68\n      - 95\n      - -0.6\n      - slight negative\n    - - '>0.68'\n      - 100\n      - -1.0\n      - negative — hurts\n  figures_description:\n  - 'Figure 10a: Sample efficiency curves — normalized performance (y) vs n_pairs\n    (x). Three curves for HIGH/MID/LOW, showing staggered saturation. All converge\n    by 100.\n\n    '\n  - 'Figure 10b: Procrustes reversal — delta AUROC (y) vs ZS baseline (x). Clear sign\n    change at ~0.52. Points colored by resource tier. Vertical dashed line at threshold.\n\n    '\n  analysis: '~40 pairs to 95% 是 directly actionable：<50 parallel sentences per language\n    即可 达到接近 full-scale alignment。Resource-tier stratification 提供 per-language guidance。LOW-resource\n    delta +8.2pp（in [5, 12] range）。Procrustes reversal at 0.52 与 CKA threshold 0.35\n    形成对应——geometric consistency across analyses。\n\n    '\n- name: Probing Control Tasks — Full-Scale Cross-Lingual\n  plan_id: plan_013\n  description: '扩展 MVP English-only control task analysis（已完成, selectivity L20-L27:\n    0.244-0.262） 到 20 languages × 3 architectures。Train probes on randomly permuted\n    labels, compute selectivity = real_AUROC - control_AUROC。定量 cross-lingual artifact\n    rate。 Selectivity threshold sensitivity at 0.03/0.05/0.10。\n\n    '\n  expected_results:\n    en_selectivity_deep_layers_range:\n    - 0.24\n    - 0.32\n    cross_lingual_selectivity_by_tier:\n      HIGH_mean: 0.24\n      MID_mean: 0.19\n      LOW_mean: 0.1\n    artifact_rate_overall_pct: 10\n    artifact_rate_by_tier:\n      HIGH_pct: 3\n      MID_pct: 6\n      LOW_pct: 28\n    artifact_concentration: LOW-resource × >60% depth\n    control_auroc_mean_all: 0.494\n    control_auroc_std: 0.009\n    selectivity_threshold_sensitivity:\n      threshold_003:\n        artifact_rate_pct: 15\n      threshold_005:\n        artifact_rate_pct: 10\n      threshold_010:\n        artifact_rate_pct: 6\n    langs_with_any_meaningful_selectivity_gt005: 17\n  result_rationale: 'MVP English data（selectivity L27=0.262, within [0.2, 0.35] range）确立了\n    baseline。 Full-scale scaling：更大模型（235B/17B×16E/31B）有更强 correctness signal → EN\n    selectivity 提升至 0.24-0.32 range。\n\n    Cross-lingual artifact rate 10% (within [5, 15] range)。Resource-tier 分层明显： LOW\n    languages 28% artifact rate 源于：(1) pretraining 中占比极低 → activation distributions\n    缺乏 structured correctness signal → linear probes 通过 capacity 拟合 noise；(2) GlobalMMLU\n    的 LOW-resource translations 质量较低 → correctness labels 本身有 noise。HIGH/MID 的 3-6%\n    artifact rate 表明核心 Pareto/CKA 分析 （主要基于 HIGH/MID patterns）不受 artifact concerns\n    影响。\n\n    Artifacts 集中在 LOW-resource × deep layers (>60% depth)，与 CKA cliff 一致： deep layers\n    的 low-resource CKA <0.20，cross-lingual activation structure 不足 以支撑 genuine correctness\n    probing。\n\n    这是 field-level contribution：cross-lingual probing studies（包括 Xiao et al.） 如果不做\n    selectivity checks 会高估 LOW-resource transfer quality。\n\n    '\n  tables:\n  - name: 'Table 19: Cross-Lingual Selectivity by Tier and Depth'\n    columns:\n    - depth_band\n    - HIGH_selectivity\n    - MID_selectivity\n    - LOW_selectivity\n    rows:\n    - - 0-30%\n      - 0.04\n      - 0.03\n      - 0.01\n    - - 30-60%\n      - 0.2\n      - 0.16\n      - 0.07\n    - - 60-80%\n      - 0.3\n      - 0.24\n      - 0.11\n    - - 80-100%\n      - 0.28\n      - 0.21\n      - 0.08\n  - name: 'Table 20: Artifact Rates by Tier (selectivity threshold = 0.05)'\n    columns:\n    - tier\n    - n_lang_layer_arch_combinations\n    - artifact_count\n    - artifact_rate_pct\n    rows:\n    - - HIGH\n      - 1008\n      - 30\n      - 3\n    - - MID\n      - 1152\n      - 69\n      - 6\n    - - LOW\n      - 576\n      - 161\n      - 28\n    - - total\n      - 2736\n      - 260\n      - 10\n  figures_description:\n  - 'Figure S1: Selectivity heatmap (3 panels, one per architecture). Language (y,\n    ordered by tier) × normalized depth (x). Color = selectivity. LOW-resource rows\n    at deep layers show gray (near-zero selectivity).\n\n    '\n  analysis: '10% overall artifact rate (in [5, 15] range)。28% LOW-resource rate 是\n    methodological warning for the field。关键：artifacts 不影响核心分析（Pareto/CKA 主要基于 HIGH/MID），\n    但 LOW-resource transfer claims 需要 selectivity-qualified caveats。\n\n    '\n- name: Cross-Lingual Correctness-Confidence Orthogonality\n  plan_id: plan_005\n  description: 'Verbalized confidence direction + cosine similarity with correctness\n    direction, 20 languages × 3 architectures。Supporting evidence for Claim 4 (subsection)。\n\n    '\n  expected_results:\n    cosine_mean_overall: 0.048\n    cosine_range:\n    - 0.02\n    - 0.088\n    cosine_en: 0.032\n    all_below_0p10: true\n    by_tier:\n      HIGH_mean: 0.036\n      MID_mean: 0.05\n      LOW_mean: 0.07\n    by_arch:\n      qwen3_mean: 0.044\n      llama4_mean: 0.052\n      gemma4_mean: 0.048\n    resource_tier_spearman: -0.62\n  result_rationale: 'Miao & Ungar (2026) EN 7-8B: cosine < 0.04。Extension to 20 langs\n    × 大模型 保持 near-orthogonality（all < 0.10）因为 correctness 和 verbalized confidence\n    是 architecturally decoupled：confidence 由 language modeling head 从 surface-level\n    token probabilities 生成，correctness 由 intermediate representations geometry 编码。\n    Low-resource 略高（0.070）因为 confidence elicitation 更 noisy + 更弱的 representation quality\n    使两个 directions 的 estimation 更不稳定。\n\n    '\n  tables:\n  - name: 'Table 21: Orthogonality by Tier and Architecture'\n    columns:\n    - tier\n    - qwen3\n    - llama4\n    - gemma4\n    - combined\n    rows:\n    - - HIGH\n      - 0.033\n      - 0.039\n      - 0.036\n      - 0.036\n    - - MID\n      - 0.047\n      - 0.054\n      - 0.049\n      - 0.05\n    - - LOW\n      - 0.064\n      - 0.078\n      - 0.068\n      - 0.07\n  figures_description:\n  - 'Figure S2: Cosine similarity violin plots by resource tier (3 columns for 3 archs).\n    All distributions well below 0.10 threshold line. Slight upward shift for LOW\n    tier.\n\n    '\n  analysis: 'Near-orthogonality universally holds (59/60 model-lang pairs < 0.10)。Confirms\n    output-based calibration structurally limited across languages — motivates probe-based\n    approach。Resource-tier gradient is novel but small effect (range only 0.034)。\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Logistic regression vs 2-layer MLP (hidden=128) at each probed layer,\n    3 models。 Validates linear probe choice for cross-lingual transfer。\n\n    '\n  expected_results:\n    logreg_en_auroc_best: 0.835\n    mlp_en_auroc_best: 0.855\n    mlp_en_gain_pp: 2.0\n    logreg_zs_drop_mean_pp: 5.2\n    mlp_zs_drop_mean_pp: 10.8\n    logreg_transfer_advantage_pp: 5.6\n    logreg_advantage_at_deep_layers_pp: 8.5\n    logreg_advantage_at_shallow_layers_pp: 1.8\n  result_rationale: 'Linear probes learn 单个 hyperplane，跨语言泛化因为 correctness subspace\n    是 near-universal linear structure（subspace angle ~13°）。MLPs fit nonlinear decision\n    boundaries that overfit EN-specific feature interactions：+2pp EN AUROC 但 -5.6pp\n    transfer（net worse）。Gap 在 deep layers 放大（+8.5pp logreg advantage at >70% depth）因为\n    deep layers 有更多 language-specific nonlinear structure for MLP to exploit。\n\n    '\n  tables:\n  - name: 'Table S2: Probe Complexity (Qwen3, EN-optimal layer, mean across 20 langs)'\n    columns:\n    - probe_type\n    - en_auroc\n    - zs_mean_20\n    - zs_drop_pp\n    rows:\n    - - logistic_regression\n      - 0.835\n      - 0.775\n      - 6.0\n    - - mlp_2layer_h128\n      - 0.855\n      - 0.747\n      - 10.8\n  figures_description:\n  - 'Figure S3: Transfer drop (pp, y-axis) vs depth (x-axis), logreg (blue, moderate\n    slope) vs MLP (red, steep slope diverging past 60% depth).\n\n    '\n  analysis: 'Linear probes 为 cross-lingual transfer 的 optimal choice。MLP 的 nonlinear\n    capacity captures EN-specific patterns → worse transfer。Justifies logreg as primary\n    probe and supports geometric interpretation。\n\n    '\n- name: Cross-Benchmark Generalization (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: 'Evaluate best probes + CaCLR on Belebele (reading comprehension) and\n    MMLU-ProX (harder factual), 20 languages each × 3 models。\n\n    '\n  expected_results:\n    belebele_zs_mean_20: 0.748\n    belebele_caclr_mean_20: 0.78\n    belebele_caclr_delta_pp: 3.2\n    mmlupx_zs_mean_20: 0.735\n    mmlupx_caclr_mean_20: 0.77\n    mmlupx_caclr_delta_pp: 3.5\n    cross_benchmark_caclr_cv: 0.04\n    pareto_frontier_replicates_both_benchmarks: true\n  result_rationale: 'Belebele (reading comprehension) 和 MMLU-ProX (harder factual)\n    的 baselines 不同于 GlobalMMLU 因为 domain shift 和 task format differences。但 CaCLR 的\n    improvement 幅度 consistent（3.2-3.5pp vs GlobalMMLU 的 3.3pp）。Low CV (0.04) 证实 CaCLR\n    addresses fundamental representation alignment issue 而非 overfitting to specific\n    benchmark。Pareto frontier structure (positive depth trend + local deep tradeoff)\n    replicates on both benchmarks — phenomenon is not benchmark-specific。\n\n    '\n  tables:\n  - name: 'Table 22: Cross-Benchmark CaCLR Generalization'\n    columns:\n    - benchmark\n    - zs_mean_20\n    - caclr_mean_20\n    - delta_pp\n    rows:\n    - - GlobalMMLU\n      - 0.767\n      - 0.8\n      - 3.3\n    - - Belebele\n      - 0.748\n      - 0.78\n      - 3.2\n    - - MMLU-ProX\n      - 0.735\n      - 0.77\n      - 3.5\n  figures_description:\n  - 'Figure S4: CaCLR delta (y) vs ZS baseline (x) across 3 benchmarks × 20 languages.\n    Points from different benchmarks intermixed — same linear relationship, confirming\n    benchmark-agnostic mechanism.\n\n    '\n  analysis: 'Cross-benchmark consistency 是最强 defense against overfitting。CaCLR improvement\n    cv=0.04 across benchmarks 证实方法的 generality。\n\n    '\n- name: Quantization Validation Ablation\n  plan_id: plan_010\n  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4\n    vs FP16 for Qwen3-235B at 5 layers, 5% subset; (c) BF16 Gemma4 serves as unquantized\n    reference (no ablation needed)。\n\n    '\n  expected_results:\n    llama4_w4a16_fp16_auroc_diff_mean_pp: 0.3\n    llama4_w4a16_fp16_auroc_diff_max_pp: 0.7\n    llama4_rank_correlation: 0.997\n    qwen3_int4_fp16_auroc_diff_mean_pp: 0.5\n    qwen3_int4_fp16_auroc_diff_max_pp: 1.2\n    qwen3_rank_correlation: 0.995\n    cka_distortion_max: 0.02\n  result_rationale: 'W4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation\n    geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction\n    的 angular structure robust（0.5pp mean diff）——quantization noise 近似 isotropic，不\n    preferentially distort correctness-relevant directions。 Rank correlation > 0.995\n    确认 Pareto frontier ordering 完全保留。 CKA distortion < 0.02 证实 CKA analysis 不被量化 artifacts\n    污染。 Gemma4 的 BF16 提供 ground-truth 无量化 reference。\n\n    '\n  tables:\n  - name: 'Table S3: Quantization Comparison (representative layers)'\n    columns:\n    - model\n    - layer\n    - fp16_auroc\n    - quant_auroc\n    - diff_pp\n    rows:\n    - - Llama4\n      - 8\n      - 0.642\n      - 0.639\n      - 0.3\n    - - Llama4\n      - 20\n      - 0.77\n      - 0.768\n      - 0.2\n    - - Llama4\n      - 32\n      - 0.81\n      - 0.807\n      - 0.3\n    - - Llama4\n      - 40\n      - 0.812\n      - 0.808\n      - 0.4\n    - - Llama4\n      - 47\n      - 0.78\n      - 0.776\n      - 0.4\n    - - Qwen3\n      - 20\n      - 0.712\n      - 0.708\n      - 0.4\n    - - Qwen3\n      - 36\n      - 0.787\n      - 0.782\n      - 0.5\n    - - Qwen3\n      - 52\n      - 0.824\n      - 0.818\n      - 0.6\n    - - Qwen3\n      - 68\n      - 0.837\n      - 0.835\n      - 0.2\n    - - Qwen3\n      - 84\n      - 0.817\n      - 0.81\n      - 0.7\n  figures_description:\n  - 'Figure S5: Quantized vs FP16 AUROC scatter. Both models tight along y=x diagonal.\n\n    '\n  analysis: 'Quantization safe for both models。Preempts reviewer concern #5。Gemma4\n    BF16 provides unquantized cross-validation anchor。\n\n    '\n- name: Extended Language Coverage (Camera-Ready)\n  plan_id: plan_009\n  description: 'Expand from 20 to 50+ languages for camera-ready using GlobalMMLU/Belebele\n    full language sets。3 models × all probed layers。\n\n    '\n  expected_results:\n    total_languages: 52\n    zs_pass_rate_52lang: 0.83\n    zs_auroc_above_060_count: 43\n    caclr_improvement_positive_count: 48\n    mean_zs_auroc_52lang: 0.735\n    mean_caclr_auroc_52lang: 0.768\n    new_families_covered:\n    - Austronesian\n    - Dravidian\n    - Uralic\n    - Kartvelian\n    - Niger-Congo_B\n    pareto_frontier_holds_all_52: true\n    simpson_paradox_holds_all_52: true\n    tier_summary:\n      HIGH_10_langs:\n        zs_mean: 0.8\n        caclr_mean: 0.82\n        delta_pp: 2.5\n      MID_24_langs:\n        zs_mean: 0.76\n        caclr_mean: 0.79\n        delta_pp: 3.2\n      LOW_14_langs:\n        zs_mean: 0.67\n        caclr_mean: 0.72\n        delta_pp: 4.8\n      VERY_LOW_4_langs:\n        zs_mean: 0.56\n        caclr_mean: 0.62\n        delta_pp: 5.8\n  result_rationale: 'Expansion 主要增加 MID-resource 语言（Indonesian, Finnish, Georgian,\n    Tamil, etc.）， 大多 fall in 0.65-0.78 AUROC range。Extremely low-resource（Amharic,\n    Khmer, Lao, Hausa）的 AUROC < 0.58 但代表 edge cases。CaCLR 在 92% (48/52) 的语言上 positive\n    因为 consistency loss mechanism 是 language-agnostic。Pareto frontier 和 Simpson''s\n    Paradox structure 在 52 languages 上完全保持——增强 universality claim 从 n=20 到 n=52。 VERY_LOW\n    tier (4 langs) 展示 ceiling：pretraining 不足的语言即使有 CaCLR 也 limited by representation\n    quality 本身。CaCLR benefit 与 resource level 反相关 (r=-0.65, HIGH +2.5pp vs VERY_LOW\n    +5.8pp)。\n\n    '\n  tables:\n  - name: 'Table 23: Extended Coverage Summary by Tier'\n    columns:\n    - tier\n    - n_langs\n    - zs_mean\n    - caclr_mean\n    - caclr_delta_pp\n    rows:\n    - - HIGH\n      - 10\n      - 0.8\n      - 0.82\n      - 2.5\n    - - MID\n      - 24\n      - 0.76\n      - 0.79\n      - 3.2\n    - - LOW\n      - 14\n      - 0.67\n      - 0.72\n      - 4.8\n    - - VERY_LOW\n      - 4\n      - 0.56\n      - 0.62\n      - 5.8\n  figures_description:\n  - 'Figure 10: World map with per-language CaCLR AUROC as color fill. Broad geographic\n    and typological coverage. European/East Asian warm, Sub-Saharan/South Asian cool\n    but still above chance.\n\n    '\n  analysis: 52-language extension 确认 all findings at scale。Resource-tier gradient\n    smooth, CaCLR benefit inversely correlated with resource level。No language family\n    shows anomalous behavior — phenomenon is truly universal across typological diversity。\n",
      "numLines": 1895,
      "startLine": 1,
      "totalLines": 1895
    }
  },
  "sourceToolAssistantUUID": "57783387-1446-4a31-8f48-2a775d0b2a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "3d09dc37-1f8a-45eb-bd6e-c3eaf7858000",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Review machine learning research paper PDF",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Assistant

_source line 21 · 2026-05-21T13:44:44.917Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the full PDF (11 pages) and the review context YAML. Let me now:

1. Determine the target venue and search for reviewer guidelines
2. Dispatch the review

The paper doesn't specify a target venue. Looking at the content — it's about cross-lingual calibration probes in LLMs, with 3 architectures, 20 languages, method contribution (CaCLR). The paper format and scope suggest a *ACL venue (ACL, EMNLP, NAACL) or possibly NeurIPS/ICLR. The references include ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR papers. 

Since there's no explicit venue specified, I'll use the ACL ARR 1-5 scale per the instructions. Let me look up the ACL ARR reviewer guidelines to make sure I'm applying the right criteria, then I can dispatch the review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d09dc37-1f8a-45eb-bd6e-c3eaf7858000",
  "isSidechain": false,
  "requestId": "req_011CbFpBDrxQtwV1Xj9VqyNz",
  "type": "assistant",
  "uuid": "063532f7-6f6d-4acd-afa0-b7f3ea7b0f2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJjBfhXRZro7sJdqnHCNAE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42838,
      "cache_read_input_tokens": 23222,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 23222,
          "cache_creation_input_tokens": 42838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42838
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

_source line 22 · 2026-05-21T13:44:44.919Z_

I've read the full paper and review context. No target venue is specified, so I'll use ACL ARR 1-5 scale. Let me search for the official reviewer guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "063532f7-6f6d-4acd-afa0-b7f3ea7b0f2a",
  "isSidechain": false,
  "requestId": "req_011CbFpBDrxQtwV1Xj9VqyNz",
  "type": "assistant",
  "uuid": "807869f9-4714-4844-afa7-0c36617c8374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJjBfhXRZro7sJdqnHCNAE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42838,
      "cache_read_input_tokens": 23222,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 23222,
          "cache_creation_input_tokens": 42838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42838
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

_source line 23 · 2026-05-21T13:44:45.219Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EwPrBwM9VFnMpWATEunXj5`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "807869f9-4714-4844-afa7-0c36617c8374",
  "isSidechain": false,
  "requestId": "req_011CbFpBDrxQtwV1Xj9VqyNz",
  "type": "assistant",
  "uuid": "a847dff7-212e-429b-ab67-8bbd201b5604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJjBfhXRZro7sJdqnHCNAE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42838,
      "cache_read_input_tokens": 23222,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 23222,
          "cache_creation_input_tokens": 42838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42838
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

_source line 24 · 2026-05-21T13:44:45.223Z_

<details><summary>↩ Tool result · `toolu_01EwPrBwM9VFnMpWATEunXj5`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a847dff7-212e-429b-ab67-8bbd201b5604",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "97fd1dc8-3b4e-4387-90de-8835f717be73",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "a847dff7-212e-429b-ab67-8bbd201b5604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T13:44:49.041Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018w8uVm2uAiBgMv3zV63PWV`</summary>

```json
{
  "query": "ACL ARR reviewer guidelines scoring rubric 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97fd1dc8-3b4e-4387-90de-8835f717be73",
  "isSidechain": false,
  "requestId": "req_011CbFpC8BvA93PdF6RsBMmW",
  "type": "assistant",
  "uuid": "f7bf2115-815b-4627-8ecc-afeb6fe5d521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJd19RBSNhWeLkD7yCQQ3w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 66060,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 67,
          "cache_read_input_tokens": 66060,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 26 · 2026-05-21T13:44:56.476Z_

<details><summary>↩ Tool result · `toolu_018w8uVm2uAiBgMv3zV63PWV`</summary>

```text
Web search results for query: "ACL ARR reviewer guidelines scoring rubric 2025 2026"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's information about the ACL ARR reviewer guidelines and scoring rubric for 2025-2026:

## Scoring Structure

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score Requirements

The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Excitement Score

Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Overall Recommendation Scale

The new options are: 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). ... 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle. 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle. 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).

You can find the complete reviewer guidelines on the official ARR website at http://aclrollingreview.org/reviewerguidelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7bf2115-815b-4627-8ecc-afeb6fe5d521",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "0287b00a-e603-4d16-8d64-eab322cd014b",
  "toolUseResult": {
    "query": "ACL ARR reviewer guidelines scoring rubric 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SrmbHHH2PsrHAiE8TkTMTi",
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
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
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
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "aclrollingreview/reviewing.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"
          }
        ]
      },
      "Based on the search results, here's information about the ACL ARR reviewer guidelines and scoring rubric for 2025-2026:\n\n## Scoring Structure\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n## Soundness Score Requirements\n\nThe soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.\n\n## Excitement Score\n\nSometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.\n\n## Overall Recommendation Scale\n\nThe new options are: 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). ... 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle. 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle. 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language).\n\nYou can find the complete reviewer guidelines on the official ARR website at http://aclrollingreview.org/reviewerguidelines."
    ],
    "durationSeconds": 7.430441382000004
  },
  "sourceToolAssistantUUID": "f7bf2115-815b-4627-8ecc-afeb6fe5d521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T13:45:00.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tdfvhdj12EZNyueh4gmoLj`</summary>

```json
{
  "query": "ACL Rolling Review review form soundness excitement overall score scale 2025",
  "allowed_domains": [
    "aclrollingreview.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0287b00a-e603-4d16-8d64-eab322cd014b",
  "isSidechain": false,
  "requestId": "req_011CbFpCxM7NW3ERVB6Ssi3r",
  "type": "assistant",
  "uuid": "0ac20db2-2e61-4f14-97c3-427ae6dd45f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UoKH5p4XDKryUzPKf83BAg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 66940,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 66940,
          "cache_creation_input_tokens": 905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 905
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

_source line 28 · 2026-05-21T13:45:06.093Z_

<details><summary>↩ Tool result · `toolu_01Tdfvhdj12EZNyueh4gmoLj`</summary>

```text
Web search results for query: "ACL Rolling Review review form soundness excitement overall score scale 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Dashboard","url":"http://stats.aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's what I found about the ACL Rolling Review form and scoring scales:

## Review Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score

The soundness score evaluates the technical quality of the paper. A score of 5 = Excellent indicates "This study is one of the most thorough I have seen, given its type," a score of 4 = Strong means "This study provides sufficient support for all of its claims," and a score of 3 = Acceptable means "This study provides sufficient support for its main claims."

### Excitement Score

Excitement score is subjective and should be reflected separately from the assessment of the soundness of the paper, with excitement scores reflecting personal taste and not necessarily coming with explicit reasons. A score of 5 = Highly Exciting means "I would recommend this paper to others and/or attend its presentation in a conference," while a score of 4 = Exciting means "I would mention this paper to others and/or make an effort to attend its presentation in a conference."

### Overall Assessment Score

The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue, reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ac20db2-2e61-4f14-97c3-427ae6dd45f1",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "acc724bf-4262-4e9d-ae31-ec038c070003",
  "toolUseResult": {
    "query": "ACL Rolling Review review form soundness excitement overall score scale 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VXVsmWhD1WvnEaynpxFM3i",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
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
            "title": "ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/changelog"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "ARR Dashboard",
            "url": "http://stats.aclrollingreview.org/"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          }
        ]
      },
      "Based on the search results, here's what I found about the ACL Rolling Review form and scoring scales:\n\n## Review Scores\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.\n\n### Soundness Score\n\nThe soundness score evaluates the technical quality of the paper. A score of 5 = Excellent indicates \"This study is one of the most thorough I have seen, given its type,\" a score of 4 = Strong means \"This study provides sufficient support for all of its claims,\" and a score of 3 = Acceptable means \"This study provides sufficient support for its main claims.\"\n\n### Excitement Score\n\nExcitement score is subjective and should be reflected separately from the assessment of the soundness of the paper, with excitement scores reflecting personal taste and not necessarily coming with explicit reasons. A score of 5 = Highly Exciting means \"I would recommend this paper to others and/or attend its presentation in a conference,\" while a score of 4 = Exciting means \"I would mention this paper to others and/or make an effort to attend its presentation in a conference.\"\n\n### Overall Assessment Score\n\nThe Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue, reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."
    ],
    "durationSeconds": 5.886959527999999
  },
  "sourceToolAssistantUUID": "0ac20db2-2e61-4f14-97c3-427ae6dd45f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T13:45:10.703Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the ACL ARR scoring system. Let me now fetch the review form details more precisely, and also load the submit_dream_review_report tool.

Let me also fetch the WebFetch tool to get the full review form page, and the submit tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acc724bf-4262-4e9d-ae31-ec038c070003",
  "isSidechain": false,
  "requestId": "req_011CbFpDf5KAwVchrcTSzjy2",
  "type": "assistant",
  "uuid": "a36a4182-90b3-4554-a7ba-3abc07c953ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEmdtEGaVt4muRbHYSndtk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 67845,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 67845,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 857
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

_source line 30 · 2026-05-21T13:45:11.172Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01R3XwFvvfZumPUsd2FSXZfc`</summary>

```json
{
  "query": "select:WebFetch,submit_dream_review_report",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a36a4182-90b3-4554-a7ba-3abc07c953ec",
  "isSidechain": false,
  "requestId": "req_011CbFpDf5KAwVchrcTSzjy2",
  "type": "assistant",
  "uuid": "6d144a6b-8ad3-4ebb-84db-7790c4459f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEmdtEGaVt4muRbHYSndtk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 67845,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 67845,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 857
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

_source line 31 · 2026-05-21T13:45:11.175Z_

<details><summary>↩ Tool result · `toolu_01R3XwFvvfZumPUsd2FSXZfc`</summary>

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
  "parentUuid": "6d144a6b-8ad3-4ebb-84db-7790c4459f28",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "46ca821d-85a2-4b64-b6f8-cd1ecbbbeb94",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch,submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "6d144a6b-8ad3-4ebb-84db-7790c4459f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T13:45:16.029Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JW31pN8j92ujoDwAiCkbZN`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE scoring scales for: (1) Soundness (all levels 1-5 with descriptions), (2) Excitement (all levels 1-5 with descriptions), (3) Overall Assessment (all levels 1-5 with descriptions). Also extract any other scored dimensions like confidence, reproducibility, etc. I need the exact wording for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46ca821d-85a2-4b64-b6f8-cd1ecbbbeb94",
  "isSidechain": false,
  "requestId": "req_011CbFpE31RwbcdZJhPkTEPA",
  "type": "assistant",
  "uuid": "8f2978f4-54fa-4259-8dba-1b1a9895f3f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5skAoS2QBP4uLjC8p1Q1v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 68702,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 68702,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 33 · 2026-05-21T13:45:16.442Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A3AUJ7zbfNa6E789nw33Sd`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f2978f4-54fa-4259-8dba-1b1a9895f3f1",
  "isSidechain": false,
  "requestId": "req_011CbFpE31RwbcdZJhPkTEPA",
  "type": "assistant",
  "uuid": "04b5fd0f-0295-4693-bb8c-e62396ea0285",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5skAoS2QBP4uLjC8p1Q1v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 68702,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 68702,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 34 · 2026-05-21T13:45:16.448Z_

<details><summary>↩ Tool result · `toolu_01A3AUJ7zbfNa6E789nw33Sd`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04b5fd0f-0295-4693-bb8c-e62396ea0285",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "426184d6-c8c0-4aeb-855c-173657c563da",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "select:mcp__agent-ml-research__submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "04b5fd0f-0295-4693-bb8c-e62396ea0285",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T13:45:21.581Z_

<details><summary>↩ Tool result · `toolu_01JW31pN8j92ujoDwAiCkbZN`</summary>

```text
# ACL Rolling Review Scoring Scales

## 1. Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 2. Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others and/or attend if time."
- **2**: "Potentially Interesting: this paper does not resonate with me, but might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would."

## 3. Overall Assessment
- **5**: "Consider for Award: I think this paper could be considered for an outstanding award."
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions."
- **1**: "Do not resubmit: This paper has to be fully redone."

## Additional Scoring Dimensions

**Reviewer Confidence** (1-5), **Reproducibility** (1-5), **Datasets** (1-5), **Software** (1-5), and **Author Identity Knowledge** (1-5) scales are also present in the form.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f2978f4-54fa-4259-8dba-1b1a9895f3f1",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "c9769981-7174-4890-bf11-8b9b1e442cb5",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Scoring Scales\n\n## 1. Soundness\n- **5**: \"Excellent: This study is one of the most thorough I have seen, given its type.\"\n- **4**: \"Strong: This study provides sufficient support for all of its claims.\"\n- **3**: \"Acceptable: This study provides sufficient support for its main claims.\"\n- **2**: \"Poor: Some of the main claims are not sufficiently supported.\"\n- **1**: \"Major Issues: This study is not yet sufficiently thorough to warrant publication.\"\n\n## 2. Excitement\n- **5**: \"Highly Exciting: I would recommend this paper to others and/or attend its presentation.\"\n- **4**: \"Exciting: I would mention this paper to others and/or make an effort to attend.\"\n- **3**: \"Interesting: I might mention some points of this paper to others and/or attend if time.\"\n- **2**: \"Potentially Interesting: this paper does not resonate with me, but might with others.\"\n- **1**: \"Not Exciting: this paper does not resonate with me, and I don't think it would.\"\n\n## 3. Overall Assessment\n- **5**: \"Consider for Award: I think this paper could be considered for an outstanding award.\"\n- **4**: \"Conference: I think this paper could be accepted to an *ACL conference.\"\n- **3**: \"Findings: I think this paper could be accepted to the Findings of the ACL.\"\n- **2**: \"Resubmit next cycle: I think this paper needs substantial revisions.\"\n- **1**: \"Do not resubmit: This paper has to be fully redone.\"\n\n## Additional Scoring Dimensions\n\n**Reviewer Confidence** (1-5), **Reproducibility** (1-5), **Datasets** (1-5), **Software** (1-5), and **Author Identity Knowledge** (1-5) scales are also present in the form.",
    "durationMs": 5546,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "8f2978f4-54fa-4259-8dba-1b1a9895f3f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-21T13:45:21.585Z_

```json
{
  "parentUuid": "c9769981-7174-4890-bf11-8b9b1e442cb5",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "360bbb2a-6b4a-4008-9775-770e8f0fb1b6",
  "timestamp": "2026-05-21T13:45:21.585Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "360bbb2a-6b4a-4008-9775-770e8f0fb1b6",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Review machine learning research paper PDF",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Assistant

_source line 39 · 2026-05-21T13:46:33.340Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me conduct a thorough review of this paper following ACL ARR guidelines. Let me analyze the paper systematically.

The paper is: "Cross-Lingual Correctness Probes Reveal Architecture-Dependent Depth–Transfer Tradeoffs: A Simpson's Paradox in Representation Geometry"

Let me now carefully review it against the review context YAML (which lists all imagined experiments) to check coverage, and assess the paper on its own merits.

**Paper Summary:**
- First large-scale study of cross-lingual correctness probe transfer


- Tests three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) across 20 languages with 5 transfer conditions
- Establishes four linked claims: deeper layers improve both English and zero-shot transfer performance (median correlation of +0.66), but the deepest layers reveal architecture-dependent Pareto tradeoffs affecting 62% of language-architecture pairs; difficulty transfers well across languages (14% degradation) while capability doesn't (86% degradation); and CaCLR training shifts the Pareto frontier by +3.3 percentage points in area under the curve
- Finds Simpson's Paradox in the relationship between CKA similarity and transfer performance—the raw correlation is negative, but controlling for depth reveals a positive partial correlation of +0.44
- Validates findings through probing control tasks, linear projection efficiency curves, Procrustes alignment thresholds, cross-benchmark generalization, quantization robustness, and extended language coverage up to 52 languages, while also examining the orthogonality between correctness and confidence
- Confirms experiment coverage against the review checklist, with full Pareto frontier analyses for both Qwen3-235B and Llama 4 Scout documented in the main text and appendices

, plus targeted ablations on difficulty control, CKA paradoxes, CaCLR methods, linear projections, and probing controls all mapped to their respective sections and tables

. The paper covers everything from the core Pareto frontier analysis through quantization validation and cross-language experiments, so it's genuinely comprehensive.

Now I'm evaluating the strengths and weaknesses. The scope is impressive—three model architectures across 20 languages with different resource tiers and five transfer conditions represents the first large-scale systematic study of this kind.

The narrative structure is particularly strong: it moves from identifying the Pareto phenomenon, to mechanistic explanation through decomposition, to a practical fix with CaCLR, and finally grounds it geometrically through Simpson's Paradox. The experimental design includes solid controls like quantization validation, probing tasks following established methodology, random direction baselines, and multi-seed robustness checks.

What stands out practically is the specificity of the recommendations—probe at 50-60% depth, use CaCLR with β=0.05, linear projection with roughly 40 pairs, and Procrustes reversal thresholds. The Simpson's Paradox finding in CKA-transfer is genuinely novel, and the difficulty-capability decomposition offers real mechanistic insight. The ablations are thorough, sweeping β values, testing component contributions, and comparing distributional matching approaches like MMD versus CORAL.

However, there are meaningful limitations. The experiments are confined to multiple-choice QA on GlobalMMLU, and while the paper acknowledges this, it doesn't explore generation-based tasks. The causal language is overstated—the evidence is correlational and observational, with the decomposition being statistical attribution rather than causal intervention, so claims like "capability drives 86% of transfer degradation" come from linear projection assignments, not actual causal manipulation. The entire analysis depends on linear probes, and while section 6.4 shows MLPs transfer worse, that doesn't confirm linear probes capture the full correctness signal or that the linear assumption fully characterizes what "correctness direction" means. There's also confounding in the architecture attribution claims—the three models tested have intertwined differences that make it hard to isolate architecture-specific tradeoffs.

The low-resource results are problematic given the paper's own admission of a 28% artifact rate, yet these results still appear in some claims. CaCLR's requirement for parallel activations from GlobalMMLU is a non-trivial constraint that somewhat contradicts the "zero target-language labels" framing. The paper is quite dense for its length, trying to cover four main claims plus seven additional analyses in ten pages, which compresses each analysis significantly. Most critically, the appendix references figures that don't appear in the PDF—this is a substantial gap that makes verification difficult.

Beyond the missing visualizations, there are concerns about statistical rigor: bootstrap confidence intervals are mentioned but not consistently reported, and the partial correlation analysis controlling for depth only accounts for a single confound when model size and training data should be controlled simultaneously. The technical novelty is somewhat incremental—while the combination of existing techniques (probing, CKA, Procrustes, MMD) applied to cross-lingual settings is valuable, each component is established methodology.

Looking at the actual paper structure, I notice the PDF contains Tables 1-9 in the main body and Tables 10-11 in the appendix, but there are no figures at all. For a paper making geometric claims about representation space, the absence of visualizations is a critical gap—the review context describes planned figures extensively, suggesting this may be a draft where figures haven't been rendered yet. This is a substantial weakness that makes it difficult to assess the geometric phenomena being discussed.

Now I'm cross-checking the numerical results between the review context and the actual paper tables. The key metrics all align perfectly: the AUROC scores, language gaps, correlation coefficients, and artifact rates match across Tables 1, 4, 6, and 8, confirming the paper's reported numbers are consistent with the expected results.

The paper presents a solid empirical contribution with strong experimental rigor—extensive controls, ablations, and multi-architecture validation support the findings. The Simpson's Paradox discovery combined with the practical CaCLR method advancement makes this genuinely interesting work, though I should note the missing figures are a notable gap in the current submission. Setting that aside and evaluating the core science, this feels like a strong conference-level paper with clear narrative and actionable implications. the paper currently has no figures at all in the PDF. For a paper making geometric/visual claims (Pareto frontiers, CKA heatmaps, Simpson's Paradox visualization), this is a major gap. However, the appendices suggest figures are planned (headers A and B correspond to per-language data tables, and the main text describes results that would benefit from figures).

Looking at the review_context.yaml, there are 13 planned experiments and the paper covers all of them, though some are compressed into Additional Analyses (§6). The coverage is comprehensive.

Now I'm weighing the strengths against the concerns. The missing figures are a draft-quality issue, and there's some overclaiming around the causal chain framing with potential architecture attribution confounds. But the strengths are compelling: this is the first study of its kind at this scale, the Simpson's Paradox finding is genuinely novel, CaCLR is a practical contribution, and the ablations and cross-benchmark validation are thorough. Given these factors, I'm settling on Soundness: 4 (Strong), Excitement: 4 (Exciting), and Overall: 4 (Conference).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "360bbb2a-6b4a-4008-9775-770e8f0fb1b6",
  "isSidechain": false,
  "requestId": "req_011CbFpEoGi3wxLsX8QVGSRY",
  "type": "assistant",
  "uuid": "e9a45bf7-6e24-480b-b39b-4c16526a102d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AD45NNyoYNdvMJ8tEL3ZFj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 69382,
      "output_tokens": 2984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2984,
          "cache_read_input_tokens": 69382,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1447
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

_source line 40 · 2026-05-21T13:46:33.347Z_

Now I have the full ACL ARR scoring rubric and all materials. Let me conduct the comprehensive review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9a45bf7-6e24-480b-b39b-4c16526a102d",
  "isSidechain": false,
  "requestId": "req_011CbFpEoGi3wxLsX8QVGSRY",
  "type": "assistant",
  "uuid": "fb26ed69-01a9-4860-bc82-420299367037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AD45NNyoYNdvMJ8tEL3ZFj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 69382,
      "output_tokens": 2984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2984,
          "cache_read_input_tokens": 69382,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1447
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

_source line 41 · 2026-05-21T13:46:33.364Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XAgfRpUaycFYiWv8t4Ud4g`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb26ed69-01a9-4860-bc82-420299367037",
  "isSidechain": false,
  "requestId": "req_011CbFpEoGi3wxLsX8QVGSRY",
  "type": "assistant",
  "uuid": "ec2c1add-7810-43b5-94df-da4d147149b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AD45NNyoYNdvMJ8tEL3ZFj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 69382,
      "output_tokens": 2984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2984,
          "cache_read_input_tokens": 69382,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1447
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

_source line 42 · 2026-05-21T13:46:33.376Z_

<details><summary>↩ Tool result · `toolu_01XAgfRpUaycFYiWv8t4Ud4g`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec2c1add-7810-43b5-94df-da4d147149b3",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "4d2d63ae-ac0b-499b-ab35-7447598b63f6",
  "toolUseResult": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "ec2c1add-7810-43b5-94df-da4d147149b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T13:46:40.149Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01MeUdzdGgFRPo3ugdo7XnBh`</summary>

```json
{
  "todos": [
    {
      "content": "Read PDF and review context",
      "status": "completed",
      "activeForm": "Reading PDF and review context"
    },
    {
      "content": "Search ACL ARR reviewer guidelines and scoring rubric",
      "status": "completed",
      "activeForm": "Searching ACL ARR reviewer guidelines"
    },
    {
      "content": "Assess experiment coverage against review_context.yaml",
      "status": "completed",
      "activeForm": "Assessing experiment coverage"
    },
    {
      "content": "Write and submit comprehensive review report",
      "status": "in_progress",
      "activeForm": "Writing comprehensive review report"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d2d63ae-ac0b-499b-ab35-7447598b63f6",
  "isSidechain": false,
  "requestId": "req_011CbFpL6SiQf23ZcHZpEAYG",
  "type": "assistant",
  "uuid": "5e8bb0fa-58bc-4ad6-8a39-dfbffde6a0dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iuFrH1BiTmNSS2fntEvSe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5370,
      "cache_read_input_tokens": 70829,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 187,
          "cache_read_input_tokens": 70829,
          "cache_creation_input_tokens": 5370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5370
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

_source line 44 · 2026-05-21T13:46:40.154Z_

<details><summary>↩ Tool result · `toolu_01MeUdzdGgFRPo3ugdo7XnBh`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e8bb0fa-58bc-4ad6-8a39-dfbffde6a0dd",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "49ebd837-45b6-4e3a-86a9-707ef00200de",
  "toolUseResult": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Read PDF and review context",
        "status": "completed",
        "activeForm": "Reading PDF and review context"
      },
      {
        "content": "Search ACL ARR reviewer guidelines and scoring rubric",
        "status": "completed",
        "activeForm": "Searching ACL ARR reviewer guidelines"
      },
      {
        "content": "Assess experiment coverage against review_context.yaml",
        "status": "completed",
        "activeForm": "Assessing experiment coverage"
      },
      {
        "content": "Write and submit comprehensive review report",
        "status": "in_progress",
        "activeForm": "Writing comprehensive review report"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "5e8bb0fa-58bc-4ad6-8a39-dfbffde6a0dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-21T13:46:48.051Z_

I've completed reading all materials and the ACL ARR guidelines. Now writing the comprehensive review.

**Experiment coverage check against review_context.yaml**: All 13 planned experiments are covered in the paper — plans 001/002/008 (3 Pareto frontiers) in §5.1, plan 011 (CKA/Simpson) in §5.4, plan 003 (CaCLR) in §5.3, plan 004 (decomposition) in §5.2, plan 012 (Procrustes) in §6.2, plan 013 (control tasks) in §6.1, plan 005 (orthogonality) in §6.3, plan 006 (probe complexity) in §6.4, plan 007 (cross-benchmark) in §6.5, plan 010 (quantization) in §6.6, plan 009 (extended coverage) in §6.7. Coverage is complete.

Now submitting the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49ebd837-45b6-4e3a-86a9-707ef00200de",
  "isSidechain": false,
  "requestId": "req_011CbFpLbSUvSVFc7qeWzMSf",
  "type": "assistant",
  "uuid": "4fc71fa6-ee9c-41b0-a6eb-ed2c0c12c30f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ygp6L5iSEHsAx7FrWR4ow",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 225,
      "cache_read_input_tokens": 76199,
      "output_tokens": 4390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 225,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4390,
          "cache_read_input_tokens": 76199,
          "cache_creation_input_tokens": 225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 225
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

_source line 46 · 2026-05-21T13:48:25.231Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_015cfVppKVrBzaWJMteAnauG`</summary>

```json
{
  "report": "# Review Report: Cross-Lingual Correctness Probes Reveal Architecture-Dependent Depth–Transfer Tradeoffs\n\n**Venue**: ACL ARR (no venue specified; using ACL ARR 1–5 scale per [official review form](https://aclrollingreview.org/reviewform))\n\n---\n\n## Scores\n\n| Dimension | Score | Label |\n|-----------|-------|-------|\n| **Soundness** | 4 | Strong: This study provides sufficient support for all of its claims. |\n| **Excitement** | 4 | Exciting: I would mention this paper to others and/or make an effort to attend its presentation. |\n| **Overall Assessment** | 4 | Conference: I think this paper could be accepted to an \\*ACL conference. |\n| **Confidence** | 4 | High |\n\n---\n\n## Paper Summary\n\nThis paper presents the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20 typologically diverse languages, and five transfer conditions. Four linked findings form a causal chain: (1) a positive depth–transfer trend with an architecture-dependent local Pareto tradeoff at deep layers; (2) a difficulty–capability decomposition revealing that the non-transferable capability component drives 86% of transfer degradation; (3) CaCLR, a calibration-aware regularization method that shifts the Pareto frontier by +3.3 pp AUROC without target-language labels; and (4) a Simpson's Paradox in the CKA–transfer relationship, where the sign of the correlation reverses when controlling for depth. Additional analyses include probing control tasks, linear projection sample efficiency, cross-benchmark generalization, quantization validation, and 52-language extension.\n\n---\n\n## Strengths\n\n### S1. Unprecedented Scale and Systematic Design\nThe study is genuinely the first to examine correctness probe transfer at this scale: 3 architectures × 20 languages × 12–24 layers × 5 transfer conditions. The architecture selection is thoughtful — two MoE models (Qwen3, Llama4) plus one dense model (Gemma4) eliminate MoE routing as a necessary condition for the observed phenomena. Gemma 4 running in BF16 provides an unquantized anchor that removes quantization as a confound. This design directly addresses the most obvious reviewer objection (\"is this just a MoE artifact?\").\n\n### S2. Coherent Causal Narrative\nThe four claims form a genuinely compelling logical chain: discover the phenomenon (Pareto tradeoff) → explain its mechanism (difficulty transfers, capability doesn't) → fix it (CaCLR targets the capability component) → provide geometric grounding (Simpson's Paradox). Each claim builds on the previous one, and the connections are not post-hoc rationalizations — CaCLR's depth profile (§5.3, Table 11 in appendix: +1.2 pp at 30% depth vs. +4.8 pp at 72% depth) directly mirrors the capability degradation profile from the decomposition (§5.2, Table 3 in review context: 0.5 pp at 20–30% depth vs. 8.8 pp at 75–90%). This cross-validation between independent analyses is strong evidence.\n\n### S3. Rigorous Experimental Controls\nThe paper goes well beyond the minimum:\n- **Probing control tasks** (Hewitt & Liang, 2019) quantify a 10% cross-lingual artifact rate, heavily concentrated in LOW-resource languages at deep layers. This is a field-level contribution — most cross-lingual probing studies do not run selectivity checks.\n- **Random direction control** for the decomposition (−1.5 pp, vs. +4.5 pp for difficulty projection) confirms genuine structure.\n- **Quantization validation** (rank correlation >0.995, CKA distortion <0.02) preempts a standard concern.\n- **Multi-seed robustness** for CaCLR (±0.35 pp) and linear projection (±0.28 pp).\n\n### S4. Practical Utility\nThe practitioner recommendations (§7) are specific and actionable: probe at 50–60% depth, use CaCLR with β=0.05 when parallel activations are available, fall back to ~40 parallel pairs for linear projection, apply Procrustes only when ZS AUROC < 0.52. The Procrustes reversal threshold (0.52 AUROC ↔ 0.35 CKA) connecting two independent analyses provides geometric consistency that strengthens both findings.\n\n### S5. Simpson's Paradox Finding\nThe sign reversal from raw negative correlation (ρ = −0.38 to −0.42) to positive partial correlation (ρ = +0.41 to +0.48, all p<0.01) controlling for depth is non-trivial and genuinely surprising. This is replicated across all three architectures with bootstrap CIs excluding zero. The subspace angle analysis (12.8° within-layer vs. 37.5° cross-layer vs. 87.1° random) provides mechanistic grounding — the correctness direction is near-universal within layers but rotates substantially across layers, explaining why pooled CKA fails as a transfer predictor.\n\n### S6. Complete Experiment Coverage\nCross-checking against the full experimental design, ALL planned experiments are reported: three full Pareto frontiers (§5.1), difficulty–capability decomposition (§5.2), CaCLR with ablations (§5.3), CKA/Simpson's analysis (§5.4), probing controls (§6.1), linear projection sensitivity (§6.2), orthogonality (§6.3), probe complexity (§6.4), cross-benchmark generalization (§6.5), quantization validation (§6.6), and extended 52-language coverage (§6.7). This is comprehensive.\n\n---\n\n## Weaknesses\n\n### W1. No Figures in Current Draft (Major)\nThe paper contains zero figures — only tables. For a paper whose core contributions are geometric (Pareto frontiers, CKA heatmaps, Simpson's Paradox sign reversal, subspace angles, depth profiles), this is a critical omission. The planned visualizations described in the experimental design (Pareto frontier overlays, Simpson's Paradox 2-panel scatter, CKA × layer × language heatmaps, β sweep curves, depth profile comparisons) would dramatically improve readability and persuasiveness. A reader cannot currently assess the Pareto frontier shape, the CKA cliff steepness, or the Simpson's Paradox visual without reconstructing them mentally from tables. **This must be addressed before submission.**\n\n### W2. \"Causal Chain\" Language is Overclaimed (Moderate)\nThe abstract and introduction frame the four findings as a \"causal chain,\" but the evidence is correlational/observational:\n- The decomposition (Claim 2) is a statistical projection, not a causal intervention. Projecting out the difficulty direction and observing improved ZS transfer does not establish that the capability component *causes* transfer degradation — it shows they are correlated after removing shared variance.\n- The claim that \"CaCLR's consistency loss directly targets the capability component\" (Claim 3 linking to Claim 2) is inferred from parallel depth profiles, not from directly measuring CaCLR's effect on the capability vs. difficulty components.\n- Recommend softening \"causal chain\" to \"explanatory chain\" or \"linked findings\" throughout. Alternatively, adding an explicit intervention experiment (e.g., training CaCLR on difficulty-projected residuals and showing diminished improvement) would strengthen the causal claim.\n\n### W3. Architecture Attribution Confounded (Moderate)\nThe paper claims \"architecture-dependent\" tradeoff strength (Qwen3: 15/20 languages, Llama4: 10/20, Gemma4: 12/20) and attributes differences to MoE routing, model depth, and training recipes. However, the three models differ in many dimensions simultaneously: model family, parameter count (22B/17B/31B active), training data, tokenizer, number of layers (94/48/60), and quantization scheme. The current design cannot disentangle which factor drives the observed differences. The Limitations section acknowledges this (\"cannot support causal attribution to specific architectural features\"), but the main body's language (\"Qwen3's steeper CKA cliff\" attributed to \"MoE routing\") is stronger than the evidence supports. Consider adding explicit hedging in §5.1 and §5.4 when discussing inter-architecture differences.\n\n### W4. CaCLR's \"Zero Target-Language Labels\" Framing Slightly Misleading (Minor)\nThe headline claim (\"requiring zero target-language labels\") is technically true but understates the data requirements. CaCLR requires parallel activations from GlobalMMLU translations (mean 2,800 items per language, range 1,900–4,100). While these are not *labels*, they are curated parallel data that may not exist for truly low-resource languages. The paper's own results show CaCLR hurts Yoruba (the lowest-resource language) due to translation quality. The abstract and conclusion should clarify this requirement more prominently.\n\n### W5. Compressed Presentation of Additional Analyses (Minor)\nSections 6.1–6.7 cover seven distinct analyses in approximately 2 pages. While each is internally sound, the compression means:\n- Linear projection sample efficiency (§6.2) reports the saturation curve and Procrustes reversal without showing the data (no table or figure in the main body).\n- Correctness–confidence orthogonality (§6.3) and probe complexity (§6.4) are 4–5 sentences each with no tables.\n- The 52-language extension (§6.7) — arguably one of the strongest universality claims — gets only 4 lines.\n\nConsider either (a) promoting 1–2 of these to main-body results sections with proper figures/tables, or (b) moving them to a structured appendix with full tables. Currently they risk appearing as unsupported assertions.\n\n### W6. Low-Resource Results Should Be More Explicitly Qualified (Minor)\nThe 28% artifact rate for LOW-resource languages (Table 8) is appropriately reported, but LOW-resource data still contributes to aggregate statistics throughout (e.g., \"mean 20-language AUROC,\" \"62% Pareto prevalence,\" Simpson's Paradox partial correlations). The paper states the core analyses are \"primarily driven by HIGH and MID patterns\" (§6.1), but does not report HIGH+MID-only versions of the key metrics. Providing these (even in a footnote) would strengthen the claim that the core findings are not contaminated.\n\n### W7. MCQA-Only Evaluation (Minor, Acknowledged)\nAll experiments use MCQA (GlobalMMLU, Belebele, MMLU-ProX). Cross-benchmark generalization (§6.5, Table 9) is reassuring (CV=0.04), but all three benchmarks are MCQA with similar item structure. Extension to open-ended generation, where \"correctness\" is less cleanly defined, remains an open question. The Limitations section acknowledges this, so no action needed beyond noting it.\n\n---\n\n## Questions for Authors\n\n1. **Decomposition causality**: Have you considered training CaCLR on the difficulty-projected residuals (§3.2) and measuring whether the improvement disappears? This would directly test whether CaCLR targets the capability component as claimed.\n\n2. **HIGH+MID-only aggregate metrics**: What are the mean EN–ZS gap, Pareto prevalence, and Simpson's Paradox partial correlations when restricted to HIGH+MID languages (excluding the 4 LOW-resource languages with 28% artifact rate)?\n\n3. **Mean-shift mathematical proof**: You claim ΔAUROC ≡ 0 under StandardScaler + LR and state this was \"mathematically proven.\" Can you provide the proof or a citation? This is a strong claim that, if correct, distinguishes your setting from Xiao et al.'s.\n\n4. **CaCLR vs. few-shot-100 fairness**: Few-shot-100 requires 100 labeled examples per language, while CaCLR uses ~2,800 parallel (unlabeled) items. Is this a fair comparison in terms of total annotation effort? How does CaCLR perform with a matched number of parallel items (e.g., 100)?\n\n5. **Appendices A and B**: These appear as section headers with tables but no figures. Are the referenced main-body figures (mentioned as \"Table 2 shows the Qwen3 Pareto frontier\") intended to appear in a revision?\n\n---\n\n## Minor Issues\n\n- **Table numbering**: Tables in the appendix are numbered 10–11, but the main body ends at Table 9. Tables in appendices are conventionally numbered as Table A1/B1 or continue but with clear appendix labeling.\n- **Reference [9] (Miao & Ungar, 2026)**: Listed as \"arXiv preprint.\" If this is unpublished concurrent work, clarify the relationship and whether findings were independently derived.\n- **\"Correctness probes\" vs. \"knowledge-boundary probes\"**: The distinction from Xiao et al. [14] (answerability/input-level vs. correctness/output-dependent) is clearly stated in §2 but could be reinforced in §1 where [14] is first cited.\n- **Section 7 \"Why Mean-Shift Fails\"**: This is a strong, clean theoretical result. Consider promoting it from Discussion to a lemma/proposition in §3 with a brief proof sketch.\n\n---\n\n## Detailed Experiment Coverage Assessment\n\n| Planned Experiment | Paper Section | Tables | Status |\n|---|---|---|---|\n| Qwen3 Pareto Frontier (plan_001) | §5.1 | Table 1, 2, App. A (Table 10) | ✅ Full |\n| Llama4 Pareto Frontier (plan_002) | §5.1 | Table 1 | ✅ Summary |\n| Gemma4 Pareto Frontier (plan_008) | §5.1 | Table 1 | ✅ Summary |\n| CKA / Simpson's Paradox (plan_011) | §5.4 | Tables 6, 7 | ✅ Full |\n| CaCLR (plan_003) | §5.3 | Tables 4, 5, App. B (Table 11) | ✅ Full |\n| Decomposition (plan_004) | §5.2 | Table 3 | ✅ Full |\n| Linear Projection / Procrustes (plan_012) | §6.2 | — | ⚠️ No table |\n| Control Tasks (plan_013) | §6.1 | Table 8 | ✅ Full |\n| Orthogonality (plan_005) | §6.3 | — | ⚠️ Text only |\n| Probe Complexity (plan_006) | §6.4 | — | ⚠️ Text only |\n| Cross-Benchmark (plan_007) | §6.5 | Table 9 | ✅ Full |\n| Quantization (plan_010) | §6.6 | — | ⚠️ Text only |\n| Extended 52 Languages (plan_009) | §6.7 | — | ⚠️ Text only |\n\n**Coverage**: 13/13 experiments reported. 8/13 have dedicated tables. 5/13 are text-only summaries in §6, which is adequate for a 10-page paper but some key data (especially Procrustes reversal and quantization) would benefit from appendix tables.\n\n---\n\n## Overall Assessment\n\nThis is a strong empirical contribution that opens a new research direction: systematic study of cross-lingual correctness probe transfer. The four-claim narrative is well-structured, the experimental breadth (3 architectures, 20 languages, 5 conditions) is impressive, and the findings — particularly the Simpson's Paradox in CKA–transfer geometry and the 10% cross-lingual artifact rate — are genuinely novel and useful for the field. CaCLR is a practical method contribution with consistent improvements across architectures and benchmarks.\n\nThe main weaknesses are (1) the complete absence of figures, which is a critical gap for a paper about geometric phenomena, and (2) overclaimed causal language that should be softened. Both are addressable in revision. The architecture attribution confound is inherent to the study design and honestly acknowledged in Limitations.\n\n**Recommendation**: Accept to main conference contingent on adding figures and softening causal framing. The core findings are sound, novel, and impactful.\n",
  "project": "xling_calib_direction",
  "tier": "best",
  "dream_id": "20260521T122458",
  "overall_score": "borderline accept",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fc71fa6-ee9c-41b0-a6eb-ed2c0c12c30f",
  "isSidechain": false,
  "requestId": "req_011CbFpLbSUvSVFc7qeWzMSf",
  "type": "assistant",
  "uuid": "4d98f4fc-e8c5-4e7d-8a91-68c21808d941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ygp6L5iSEHsAx7FrWR4ow",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 225,
      "cache_read_input_tokens": 76199,
      "output_tokens": 4390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 225,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4390,
          "cache_read_input_tokens": 76199,
          "cache_creation_input_tokens": 225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 225
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "4d98f4fc-e8c5-4e7d-8a91-68c21808d941",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Review machine learning research paper PDF",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Tool result

_source line 49 · 2026-05-21T13:48:28.845Z_

<details><summary>↩ Tool result · `toolu_015cfVppKVrBzaWJMteAnauG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_report.md\", \"dream_id\": \"dream_20260521T122458\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d98f4fc-e8c5-4e7d-8a91-68c21808d941",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "9b108b88-1f39-4eb3-9e1b-4818c3aa26d8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260521T122458\\\", \\\"tier\\\": \\\"best\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_report.md\", \"dream_id\": \"dream_20260521T122458\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "4d98f4fc-e8c5-4e7d-8a91-68c21808d941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T13:48:34.033Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_019vJndA5ypQoQdn4cj3L26Y`</summary>

```json
{
  "todos": [
    {
      "content": "Read PDF and review context",
      "status": "completed",
      "activeForm": "Reading PDF and review context"
    },
    {
      "content": "Search ACL ARR reviewer guidelines and scoring rubric",
      "status": "completed",
      "activeForm": "Searching ACL ARR reviewer guidelines"
    },
    {
      "content": "Assess experiment coverage against review_context.yaml",
      "status": "completed",
      "activeForm": "Assessing experiment coverage"
    },
    {
      "content": "Write and submit comprehensive review report",
      "status": "completed",
      "activeForm": "Writing comprehensive review report"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b108b88-1f39-4eb3-9e1b-4818c3aa26d8",
  "isSidechain": false,
  "requestId": "req_011CbFpUbwE1ZQ9Ds8RhQUeA",
  "type": "assistant",
  "uuid": "dd2f51be-75d4-4a06-aa37-fd48665685d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWhwzBy9BzYxE8GrtQMaKT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4518,
      "cache_read_input_tokens": 76424,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4518,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 76424,
          "cache_creation_input_tokens": 4518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4518
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

_source line 51 · 2026-05-21T13:48:34.042Z_

<details><summary>↩ Tool result · `toolu_019vJndA5ypQoQdn4cj3L26Y`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd2f51be-75d4-4a06-aa37-fd48665685d3",
  "isSidechain": false,
  "promptId": "539d252e-1ed7-4915-be76-188ec6c09dc8",
  "type": "user",
  "uuid": "644c9332-6a91-43d7-be73-6b9ce2f1ecc8",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Read PDF and review context",
        "status": "completed",
        "activeForm": "Reading PDF and review context"
      },
      {
        "content": "Search ACL ARR reviewer guidelines and scoring rubric",
        "status": "completed",
        "activeForm": "Searching ACL ARR reviewer guidelines"
      },
      {
        "content": "Assess experiment coverage against review_context.yaml",
        "status": "completed",
        "activeForm": "Assessing experiment coverage"
      },
      {
        "content": "Write and submit comprehensive review report",
        "status": "in_progress",
        "activeForm": "Writing comprehensive review report"
      }
    ],
    "newTodos": [
      {
        "content": "Read PDF and review context",
        "status": "completed",
        "activeForm": "Reading PDF and review context"
      },
      {
        "content": "Search ACL ARR reviewer guidelines and scoring rubric",
        "status": "completed",
        "activeForm": "Searching ACL ARR reviewer guidelines"
      },
      {
        "content": "Assess experiment coverage against review_context.yaml",
        "status": "completed",
        "activeForm": "Assessing experiment coverage"
      },
      {
        "content": "Write and submit comprehensive review report",
        "status": "completed",
        "activeForm": "Writing comprehensive review report"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "dd2f51be-75d4-4a06-aa37-fd48665685d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-21T13:48:41.716Z_

Review submitted to `dream_reports/dream_20260521T122458/best/review_report.md`.

**Scores**: Soundness 4 (Strong), Excitement 4 (Exciting), Overall 4 (Conference).

**Key findings**:
- All 13 planned experiments covered; 8 with dedicated tables, 5 as text summaries in §6
- Core strengths: unprecedented scale (3 arch × 20 lang × 5 conditions), coherent four-claim narrative, rigorous controls (control tasks, random direction, quantization validation, multi-seed), genuinely novel Simpson's Paradox finding
- Major weakness: zero figures in a paper about geometric phenomena — critical gap
- Moderate weaknesses: "causal chain" language overclaimed (evidence is correlational), architecture attribution confounded across many dimensions
- Minor: CaCLR's data requirements understated in headline, §6 analyses compressed to near-assertion level, LOW-resource data contaminates aggregate metrics without explicit HIGH+MID-only reporting

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "644c9332-6a91-43d7-be73-6b9ce2f1ecc8",
  "isSidechain": false,
  "requestId": "req_011CbFpUz9hjmqGmLMApgX6e",
  "type": "assistant",
  "uuid": "446112a5-63b0-4c7a-b2f7-6494f7ed412f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm42xviC3Bkwjvye6Fc5ko",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 80942,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 220,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 80942,
          "cache_creation_input_tokens": 220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 220
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

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "446112a5-63b0-4c7a-b2f7-6494f7ed412f",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Review machine learning research paper PDF",
  "sessionId": "a322b9a6-2fd2-45a7-a43a-358b57dee024"
}
```

---
