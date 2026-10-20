# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/3c2c87c3-1a27-412c-9894-e2a083a5bf6f.jsonl`
- **Structured JSON:** [`78f975def3e9565bb15f.json`](../../sessions/78/78f975def3e9565bb15f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T08:36:30.254Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T08:36:30.254Z",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Version B framing. Lead finding: \"multi-class annotation error 的危险性是 topology-dependent 的：\nexposure misclassification 在方向和幅度上均不可预测，其余拓扑方向可预测但幅度需全 K×K 矩阵\n才能量化——binary 框架在两种情况下均不足。\" Claim 1 从 \"breaks guarantees across topologies\"\n调整为 \"reveals a sharp topology-dependent dichotomy\"——exposure 是唯一方向不可预测的拓扑，\n这本身是重要发现（exposure 是 CSS 中最常被 LLM 标注的变量）。Claim 2 的 ASV 从\n\"robustness to direction reversal\" 调整为 \"robustness to magnitude uncertainty\"，\n因 collider ASV 单调性部分失效（7% violations），需修改定义或加条件，降低紧性要求。\nClaim 3 权重增加——correction guidance 的实用价值成为主要卖点，弥补 taxonomy 发现不够 dramatic。\n需额外投入：(a) spectral 分析深挖 exposure 反转机制（λ₂/λ₁ 阈值），\n(b) 经验实验扩充至 4-5 个 task 以补偿理论贡献缩窄，\n(c) 考虑 user study 展示 ASV 对研究者决策的影响。\ntheory-MC match 在复杂拓扑（front-door, collider）偏低，需坦诚承认闭合形式表达式的近似局限性，\n将 MC 验证本身作为补充贡献。经验混淆矩阵 diagonal-dominant，极端 C 结构罕见——\nASV 在多数实证场景输出 \"robust\"，实用区分力有限，需通过 semi-synthetic 注入实验补救。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T08:36:30.258Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T08:36:30.258Z",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-20T08:36:30.299Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Version B framing. Lead finding: "multi-class annotation error 的危险性是 topology-dependent 的：
exposure misclassification 在方向和幅度上均不可预测，其余拓扑方向可预测但幅度需全 K×K 矩阵
才能量化——binary 框架在两种情况下均不足。" Claim 1 从 "breaks guarantees across topologies"
调整为 "reveals a sharp topology-dependent dichotomy"——exposure 是唯一方向不可预测的拓扑，
这本身是重要发现（exposure 是 CSS 中最常被 LLM 标注的变量）。Claim 2 的 ASV 从
"robustness to direction reversal" 调整为 "robustness to magnitude uncertainty"，
因 collider ASV 单调性部分失效（7% violations），需修改定义或加条件，降低紧性要求。
Claim 3 权重增加——correction guidance 的实用价值成为主要卖点，弥补 taxonomy 发现不够 dramatic。
需额外投入：(a) spectral 分析深挖 exposure 反转机制（λ₂/λ₁ 阈值），
(b) 经验实验扩充至 4-5 个 task 以补偿理论贡献缩窄，
(c) 考虑 user study 展示 ASV 对研究者决策的影响。
theory-MC match 在复杂拓扑（front-door, collider）偏低，需坦诚承认闭合形式表达式的近似局限性，
将 MC 验证本身作为补充贡献。经验混淆矩阵 diagonal-dominant，极端 C 结构罕见——
ASV 在多数实证场景输出 "robust"，实用区分力有限，需通过 semi-synthetic 注入实验补救。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "74990caf-6c19-4294-8631-731e236d5131",
  "type": "user",
  "uuid": "5cde06d8-be77-4191-9404-f2af5986e12f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T08:36:30.298Z_

```json
{
  "parentUuid": "5cde06d8-be77-4191-9404-f2af5986e12f",
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7e512e2e-562c-4987-83bc-f033152968d0",
  "timestamp": "2026-05-20T08:36:30.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T08:36:30.298Z_

```json
{
  "parentUuid": "7e512e2e-562c-4987-83bc-f033152968d0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ab79cbde-626f-4e4d-b0a3-497baeaf97cb",
  "timestamp": "2026-05-20T08:36:30.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for annotation error study",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Assistant

_source line 7 · 2026-05-20T08:36:33.865Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab79cbde-626f-4e4d-b0a3-497baeaf97cb",
  "isSidechain": false,
  "requestId": "req_011CbDWsrzsbhqeoJPwthPiz",
  "type": "assistant",
  "uuid": "2c3f271e-40b4-4b9e-93be-df594843b5ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014asM1MvqxezQXzEEVAXKzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12044,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12044,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12044
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

_source line 8 · 2026-05-20T08:36:34.914Z_

<details open><summary>🔧 Tool call — Read · `toolu_012YVbEs7eLD7LRc6rNWtZh3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c3f271e-40b4-4b9e-93be-df594843b5ba",
  "isSidechain": false,
  "requestId": "req_011CbDWsrzsbhqeoJPwthPiz",
  "type": "assistant",
  "uuid": "1ed08bb2-5e03-4fe3-ace2-e6046627f830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014asM1MvqxezQXzEEVAXKzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12044,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12044,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12044
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

_source line 9 · 2026-05-20T08:36:35.201Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KUvKcL5hw8ydUZAVoLg59a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ed08bb2-5e03-4fe3-ace2-e6046627f830",
  "isSidechain": false,
  "requestId": "req_011CbDWsrzsbhqeoJPwthPiz",
  "type": "assistant",
  "uuid": "50a6ac15-26de-424b-bb4a-73edf79e5cf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014asM1MvqxezQXzEEVAXKzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12044,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12044,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12044
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

_source line 10 · 2026-05-20T08:36:35.220Z_

<details><summary>↩ Tool result · `toolu_012YVbEs7eLD7LRc6rNWtZh3`</summary>

```text
1	[
2	  {
3	    "name": "Six-topology bias taxonomy (K=3)",
4	    "description": "对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）\n推导 K=3 闭合形式 bias 表达式，用 MC 验证（1000 reps × N=10000 × 6 种 C 结构）。\n核心问题：哪些拓扑在 non-differential K≥3 误分类下出现方向反转？\n",
5	    "results": {
6	      "reversal_topologies_count": 1,
7	      "confounding_reversal_rate": 0.0,
8	      "confounding_theory_mc_match": "6/6",
9	      "confounding_bias_range": "0.063–0.298",
10	      "exposure_reversal_rate": 0.85,
11	      "exposure_sign_reversal_rate": 0.834,
12	      "exposure_amplification_rate": 0.141,
13	      "exposure_theory_mc_match": "5/6",
14	      "exposure_bias_range": "-0.84–0.42",
15	      "mediation_reversal_rate": 0.0,
16	      "mediation_theory_mc_match": "5/6",
17	      "mediation_bias_range": "0.00–0.15",
18	      "collider_reversal_rate": 0.0,
19	      "collider_theory_mc_match": "4/6",
20	      "collider_bias_range": "0.02–0.18",
21	      "mbias_reversal_rate": 0.0,
22	      "mbias_theory_mc_match": "4/6",
23	      "mbias_bias_range": "0.04–0.22",
24	      "instrument_reversal_rate": 0.0,
25	      "instrument_theory_mc_match": "5/6",
26	      "instrument_bias_range": "0.03–0.25",
27	      "frontdoor_reversal_rate": 0.0,
28	      "frontdoor_theory_mc_match": "3/6",
29	      "frontdoor_bias_range": "0.01–0.19",
30	      "overall_theory_mc_match": "32/42 (0.76)",
31	      "random_100k_reversal_topologies": "exposure only"
32	    },
33	    "tables": [
34	      {
35	        "name": "Table 1: Six-Topology Bias Taxonomy Summary (K=3)",
36	        "description": "6 rows (topologies) × columns: reversal_rate_100k, named_structure_match (x/6),\nbias_range [min, max], bias_direction_class (monotonic-toward-null / monotonic-toward-OVB /\nunpredictable), mechanism_summary.\nKey pattern: exposure 行显著异于其余——reversal 85%，direction unpredictable；\n其余 5 行 reversal 0%，方向可预测，但 magnitude range 差异大\n（confounding 0.06-0.30 vs mediation 0.00-0.15 vs collider 0.02-0.18）。\n"
37	      },
38	      {
39	        "name": "Table 2: Theory vs MC Bias — Per-Structure Detail",
40	        "description": "42 rows (6 topologies × ~7 structures including identity-adjacent, uniform-leaning,\nnear-permutation, block-diagonal, asymmetric, random-moderate, plus MVP-inherited).\nColumns: topology, C_structure, theoretical_bias, mc_mean, mc_95ci, match (✓/✗).\n10 个 ✗ 集中在 collider-near-permutation, mbias-block-diagonal,\nfrontdoor-near-permutation/asymmetric/block-diagonal。\n"
41	      }
42	    ],
43	    "figures": [],
44	    "analysis": "核心结论：topology-dependent dichotomy 成立但 dramatic 程度有限。Exposure 是唯一 \"dangerous\"\n拓扑，其余 5 个是 \"well-behaved\"。这支持 Version B framing，但问题是 5 个 well-behaved\n拓扑的故事不够 exciting——\"magnitude varies but direction is predictable\" 比\n\"guarantees break\" 弱得多。Theory-MC mismatch 在复杂拓扑的存在是双刃剑：一方面暴露\n闭合表达式的局限性（reviewer concern），另一方面 MC 验证本身成为必要贡献\n（\"我们提供的不仅是理论，还有数值验证\"）。Front-door 3/6 match 可能需要在论文中\n降格为 \"MC-validated conjecture\" 而非 \"theorem\"。\nVersion B lead: 虽然 5 个拓扑方向可预测，但 magnitude range 的跨拓扑差异\n（confounding 0.06-0.30 vs mediation 0.00-0.15）本身有信息量——研究者需要知道\n自己的 DAG topology 处于哪个 magnitude regime，binary 框架无法提供这个信息。\n\n\nWorst 档的核心预测：仅 exposure DAG 出现方向反转。机制上，exposure misclassification\n直接扰乱 treatment assignment labels——当 K≥3 时，near-permutation C 导致 label swap，\n将 treatment A 的 outcome 映射到 treatment B 的估计上，产生符号翻转。这在 K=2 时\n结构性不可能（binary 只有\"正确/错误\"两种状态，non-differential 保证 bias toward null）。\n其余 5 个拓扑中，misclassified 变量（confounder/mediator/collider/instrument/front-door variable）\n不直接定义 treatment contrast，其误分类调制 bias magnitude 但不翻转 numerator/denominator，\n因此方向可预测。Theory-MC match 率 0.76 偏低的原因：collider（conditioning 引入非线性）、\nM-bias（双 confounder 路径交互）、front-door（复合 mediation 步骤）的闭合形式表达式\n在 extreme C structures 下需要高阶 Taylor 项，一阶近似不够精确。Front-door 最差（3/6），\n因为 front-door criterion 涉及两步 mediation，每步的近似误差在复合后被放大。\n"
45	  },
46	  {
47	    "name": "General-K matrix expressions and interpretability (K=5,7)",
48	    "description": "将 bias 表达式推广到 K=5,7 的矩阵形式，开发三个可解释性工具：\n(a) eigendecomposition 摘要，(b) worst-case scalar bounds，(c) diagnostic visualizations。\n在 confounding + mediation + collider 上验证。\n",
49	    "results": {
50	      "confounding_K5_dominant_eigenvalue_fraction": 0.82,
51	      "confounding_K7_dominant_eigenvalue_fraction": 0.76,
52	      "mediation_K5_dominant_eigenvalue_fraction": 0.75,
53	      "mediation_K7_dominant_eigenvalue_fraction": 0.68,
54	      "collider_K5_dominant_eigenvalue_fraction": 0.58,
55	      "collider_K7_dominant_eigenvalue_fraction": 0.49,
56	      "K5_theory_mc_match_rate": 0.7,
57	      "K7_theory_mc_match_rate": 0.63,
58	      "worst_case_bound_tightness_K5": "1.8–2.5x conservative",
59	      "worst_case_bound_tightness_K7": "2.5–3.2x conservative",
60	      "modes_needed_for_90pct_variance_collider_K7": 4
61	    },
62	    "tables": [
63	      {
64	        "name": "Table 3: Eigendecomposition Summary — K=3,5,7 × 3 Topologies",
65	        "description": "9 rows (3 K × 3 topologies) × columns: K, topology, λ₁/tr(Λ), modes_for_90pct,\ndominant_mode_interpretation, bound_tightness_ratio.\nKey pattern: confounding 始终 clean（1-2 modes），collider 随 K 增长迅速恶化。\n"
66	      },
67	      {
68	        "name": "Table 4: Worst-Case Scalar Bound vs Actual MC Maximum Bias",
69	        "description": "展示 bound 的 conservativeness。Columns: topology, K, worst_case_bound,\nmc_observed_max, ratio. Ratio 从 K=3 的 1.3x 增长到 K=7 的 3.2x。\n"
70	      }
71	    ],
72	    "figures": [],
73	    "analysis": "Worst 档下，K=5,7 的 interpretability tools 对 confounding/mediation 有效但对 collider 不足。\n这意味着论文中 \"eigendecomposition as interpretability tool\" 的 claim 需要加 caveat：\n仅对 bias 有清晰方向结构的拓扑有效。Worst-case bounds 的 3x conservativeness\n使其实用价值有限——bound 告诉你 \"bias 最多这么大\" 但实际远小于此。\n建议：对 collider/M-bias 拓扑放弃 eigendecomposition 摘要，改用 worst-case bound +\ndiagnostic visualization 的组合。论文中坦诚分拓扑讨论可解释性工具的适用范围。\n\n\nK 增大时，C 的自由度从 K=3 的 6 个增长到 K=5 的 20 个、K=7 的 42 个。\nConfounding DAG 的 bias 有简单的方向结构（residual confounding 沿单一方向累积），\n因此 dominant eigenvalue 即使在 K=7 仍捕获 76% variance——eigendecomposition 是有效的摘要工具。\nCollider DAG 的 bias 来自 conditioning 引入的伪相关，其方向依赖于 collider 各类别间的\n相对误分类强度——K=7 时 7 个类别的两两误分类形成多维度干扰，dominant eigenvalue 仅捕获\n49%，需要 4 个 mode 才能解释 90% variance，eigendecomposition 失去摘要价值。\nWorst-case bounds 松的原因：bounds 必须覆盖 adversarial C 结构，但实际 C 的 feasible region\n在高 K 时是高维空间中的低维 manifold——bounds 优化的 supremum 在实践中不可达。\nTheory-MC match 在 K=7 降至 0.63，因为矩阵形式表达式中的 Kronecker product 项\n在数值求解时积累舍入误差，且 MC 的 N=10000 在 K=7 时 per-cell 样本量不足\n（7×7=49 cells，某些 cell 可能 <50 observations）。\n"
74	  },
75	  {
76	    "name": "Empirical confusion matrices (3 LLMs × 3 CSS tasks)",
77	    "description": "收集 Llama 4 Maverick / Qwen 3.5 Plus / DeepSeek V4 在 protest event coding (K=5),\nstance detection (K=3), toxicity (K=2) 上的经验混淆矩阵，分析 inter-model 相关性\n和 downstream regression bias。\n",
78	    "results": {
79	      "protest_accuracy_range": "0.68–0.73",
80	      "protest_diagonal_dominance_range": "0.74–0.80",
81	      "stance_accuracy_range": "0.76–0.81",
82	      "stance_diagonal_dominance_range": "0.82–0.87",
83	      "toxicity_accuracy_range": "0.83–0.88",
84	      "inter_model_error_kappa": "0.58–0.67",
85	      "near_permutation_structures_observed": 0,
86	      "downstream_bias_gt_005_count": "2–3 out of 9",
87	      "downstream_direction_reversal_observed": false,
88	      "max_downstream_bias": 0.12,
89	      "total_annotations": "~270K (30K × 3 models × 3 tasks)",
90	      "api_cost_actual": "$350–480"
91	    },
92	    "tables": [
93	      {
94	        "name": "Table 5: Empirical Confusion Matrices — 9 Combinations",
95	        "description": "9 个混淆矩阵（3 LLMs × 3 tasks），每个附 accuracy, diagonal_dominance_ratio,\nFrobenius_distance_to_identity. Protest K=5 的矩阵最 \"丰富\"（off-diagonal 分散），\ntoxicity K=2 的矩阵最 diagonal-dominant。\n"
96	      },
97	      {
98	        "name": "Table 6: Inter-Model Error Correlation",
99	        "description": "3×3 模型对的 error agreement matrix（pairwise kappa on error cells）。\n值 0.58-0.67，证实跨模型错误高度相关。附 per-category breakdown。\n"
100	      },
101	      {
102	        "name": "Table 7: Downstream Regression Bias vs Gold Standard",
103	        "description": "9 rows × columns: task, model, DAG_topology_assumed, effect_gold, effect_annotated,\nbias, bias_direction, theoretical_prediction, match (✓/✗).\n2-3 行 bias >0.05，其余 <0.05。\n"
104	      }
105	    ],
106	    "figures": [],
107	    "analysis": "Worst 档的关键困境：经验混淆矩阵全部 diagonal-dominant，无 near-permutation 结构。\n这意味着：(1) bias taxonomy 的 \"dramatic\" 案例（direction reversal）在实证中不出现，\n(2) ASV 多数输出 \"robust\"（大 ASV 值），区分力有限，(3) correction guidance 在多数场景\n退化为 \"MLA suffices\"。应对策略：(a) semi-synthetic 实验——在经验 C 基础上注入\ncontrolled perturbation，展示 \"如果 LLM 准确率再低 10% 会怎样\"，\n(b) 将 diagonal-dominant 本身作为 positive finding（\"当前 LLM 的错误模式在多数 CSS\ntasks 上落在 safe zone——但 ASV 量化了 safe zone 的边界\"），\n(c) 增加 4th/5th task（低资源语言 stance detection 或 fine-grained emotion K=7）\n以提高观察到 non-diagonal-dominant C 的概率。\n\n\n当前 SOTA LLMs 在 well-studied CSS tasks 上准确率 0.68-0.88，产出的混淆矩阵\n必然 diagonal-dominant。Off-diagonal mass 集中在语义相邻类别（如 stance detection 中\n\"support\" 与 \"somewhat support\" 互混），而非随机分散——这意味着 C 结构远离\nnear-permutation 极端。Inter-model error kappa 0.58-0.67 与 Kim et al. (ICML 2025)\n的 60% error agreement 一致，因为 LLM 的错误模式受 pre-training data distribution\n驱动，不同模型在相同 \"难\" 样本上犯相似错误。Downstream bias 多数 <0.05 因为\ndiagonal-dominant C 的 bias 表达式给出小值；2-3 个 >0.05 的案例出现在 protest event\ncoding（K=5，准确率最低）与较弱模型（Qwen 3.5 Plus）的组合。无方向反转因为：\n(a) 经验 C 是 diagonal-dominant，远未到 near-permutation threshold，\n(b) 如果实验设计中 annotated variable 是 confounder/mediator（非 exposure），\n则即使 C 极端也不会反转（worst 档核心假设）。\n这是 worst 档最关键的弱点：经验数据 \"太好了\"，极端 C 结构罕见，\nASV 和 bias taxonomy 的实用展示受限。\n"
108	  },
109	  {
110	    "name": "Binarization collapse analysis (K→2 across 6 topologies)",
111	    "description": "对 6 个拓扑的 K=3,5,7 变量做 binary collapse，比较 full multi-class bias expression\n与 binarized bias expression 的差异，证明 binarization 不是安全捷径。\n",
112	    "results": {
113	      "confounding_K3_max_delta": 0.078,
114	      "confounding_K5_max_delta": 0.085,
115	      "confounding_K7_max_delta": 0.091,
116	      "exposure_K3_max_delta": 0.072,
117	      "mediation_K3_max_delta": 0.041,
118	      "collider_K3_max_delta": 0.068,
119	      "mbias_K3_max_delta": 0.055,
120	      "instrument_K3_max_delta": 0.038,
121	      "frontdoor_K3_max_delta": 0.045,
122	      "overall_max_delta": 0.091,
123	      "topologies_with_delta_gt_005": 4,
124	      "topologies_with_delta_gt_008": 2,
125	      "binarization_can_reverse_direction": false
126	    },
127	    "tables": [
128	      {
129	        "name": "Table 8: Binarization Delta — 6 Topologies × K=3,5,7",
130	        "description": "~18 rows (6 topologies × 3 K values) × columns: topology, K, folding_scheme,\nbias_multiclass, bias_binary, delta, delta/bias_multiclass (relative),\ndirection_change (all \"No\"). Max delta bolded. Confounding rows consistently\nhighest delta.\n"
131	      }
132	    ],
133	    "figures": [],
134	    "analysis": "Worst 档下 binarization 分析的结论是 \"real but modest\"。Max Δ=0.091 支持\n\"binary 框架不足\" 的 claim，但不够 dramatic 作为 standalone finding。在 Version B\nframing 中，binarization 分析应作为 supporting evidence 而非 lead result——\n它回答的问题从 \"binarization is dangerous\" 降级为 \"binarization loses information\nthat matters for magnitude estimation\"。建议：在论文中将 binarization 分析压缩为\n1 段 + 1 figure，将篇幅让给 exposure 反转机制的 spectral 分析和 correction framework。\n\n\nBinarization 将 K-class variable collapse 为 binary，丢弃类别间的 fine-grained\n误分类信息。在 worst 档下，max delta 0.091 低于 MVP 的 0.103（MVP 的 0.103\n来自特定 near-permutation C 结构 + confounding DAG 的最优案例）。系统搜索发现\nconfounding DAG 仍是 binarization effect 最大的拓扑（residual confounding 对\nclass-collapse 最敏感），而 mediation/instrument 的 delta 较小（<0.05）因为这些拓扑中\nannotated variable 的 misclassification 本身效应就小，binarization 损失的信息量有限。\n关键限制：binarization 在 worst 档下未导致方向反转（仅改变 magnitude），\n削弱了 \"binarization is hazardous\" 的 claim 力度。Delta 0.091 在统计上显著\n但实质意义存疑——reviewer 可能质疑 \"0.09 的额外 bias 在社会科学效应量通常 0.1-0.3\n的语境下是否 material\"。\n"
135	  },
136	  {
137	    "name": "ASV formal proofs (confounding, mediation, collider)",
138	    "description": "为 3 个优先拓扑推导 ASV 表达式，证明 monotonicity 和 sharpness，\nMC 验证 coverage（90%, 95%, 99%）。\n",
139	    "results": {
140	      "confounding_monotonicity": "PROVED (formal)",
141	      "confounding_sharpness": "PROVED (formal)",
142	      "confounding_coverage_90": 0.88,
143	      "confounding_coverage_95": 0.93,
144	      "confounding_coverage_99": 0.97,
145	      "mediation_monotonicity": "PROVED (formal)",
146	      "mediation_sharpness": "FAILED — bound conservative by factor 1.4–1.8x",
147	      "mediation_coverage_90": 0.86,
148	      "mediation_coverage_95": 0.91,
149	      "mediation_coverage_99": 0.96,
150	      "collider_monotonicity": "FAILED — 7% of C structures show non-monotone ASV in δ",
151	      "collider_sharpness": "N/A (requires monotonicity)",
152	      "collider_coverage_90": 0.74,
153	      "collider_coverage_95": 0.78,
154	      "collider_coverage_99": 0.85,
155	      "asv_sharpness_formal_proofs": 1,
156	      "collider_monotonicity_violation_delta_range": "0.3–0.5",
157	      "collider_violation_C_characterization": "off-diagonal mass concentrated in 2 adjacent cells"
158	    },
159	    "tables": [
160	      {
161	        "name": "Table 9: ASV Proof Status Summary",
162	        "description": "3 rows (topologies) × columns: monotonicity (✓/✗ + proof type),\nsharpness (✓/✗ + proof type), coverage_90/95/99, notes.\nConfounding 行全绿，mediation 行部分黄（sharpness ✗），collider 行红（monotonicity ✗）。\n"
163	      },
164	      {
165	        "name": "Table 10: ASV Coverage — 1000 Scenario MC Validation",
166	        "description": "详细 coverage 分析。Per topology 的 coverage 分布（不是单个数字）——\nhistogram of \"actual coverage across 1000 scenarios\"。Confounding 集中在 0.92-0.95，\ncollider 分散在 0.65-0.90 with a tail of under-coverage。\n"
167	      }
168	    ],
169	    "figures": [],
170	    "analysis": "ASV 框架在 worst 档下遭遇了预期中的 collider 难题。Sharpness 仅 1 个拓扑完成证明，\n低于理想但在 [1,2] 范围内。Collider 的 non-monotonicity 是论文的潜在 weakness——\nreviewer 会问 \"如果 ASV 在 collider 拓扑不 monotone，你的框架怎么用？\"\n应对：(1) 论文中诚实报告 collider 的限制，提出 restricted ASV 定义，\n(2) 强调 collider 在 CSS 实证中相对少见（mediation/confounding 更常见），\n(3) 将 collider ASV 修复标记为 \"important future work\" 而非尝试勉强证明。\nCoverage 0.85 (aggregated) 在 [0.80, 0.88] 范围内——不是灾难性的 under-coverage，\n但需要在论文中解释为什么 coverage 低于 nominal 并建议 practitioners 使用 99% level\n而非 95% level 作为 conservative 选择。\n\n\nConfounding ASV monotonicity 成立因为 residual confounding 是 δ 的单调函数——\n更大的 annotation error amplification 只能增加残差混淆，不能减少。Sharpness 成立因为\nnear-permutation C 结构确实实现了 bound（近似完全 label swap 达到最大 residual confounding）。\n\nMediation ASV monotonicity 成立因为 indirect effect 的 attenuation 随 mediator\nmisclassification 单调增加。但 sharpness 失败因为 mediation bias 的 maximum 受限于\ndirect effect magnitude——即使 C 完全 permutation，bias 也不能超过 direct effect，\n而 ASV bound 的推导假设 bias 可以达到 \"worst-case over all C in δ-ball\"，\n其中包含了结构上不可达的 C 配置。Bound conservative 1.4-1.8x。\n\nCollider ASV 是 worst 档的关键难点。Collider bias 来自 conditioning on a common effect——\n当 collider variable 被 misclassify 时，conditioning 的 \"打开\" 程度取决于 C 结构。\n在某些 C 结构下（off-diagonal mass 集中在 2 个相邻 cell），δ 从 0.3 增到 0.5 时\nbias 先增后减——因为中等 misclassification 部分打开 collider path 但保留 conditioning\n结构，而更大的 misclassification 反而 \"破坏\" 了 conditioning 的精确性，使 collider path\n的打开效果被噪声稀释。这产生 non-monotone ASV，7% violation rate。\n修补方案：restricted ASV（限制 δ-path 在 monotone region）或 conditional ASV\n（对 C 结构分区域定义）。两种方案都增加框架复杂度，降低实用性。\n"
171	  },
172	  {
173	    "name": "ASV MC validation (M-bias, instrument, front-door)",
174	    "description": "对剩余 3 个拓扑推导 ASV 表达式并做 MC 验证。\nMonotonicity 和 sharpness 作为 conjecture + numerical evidence，不要求 formal proof。\n",
175	    "results": {
176	      "mbias_monotonicity_mc": "holds (0/1000 violations)",
177	      "mbias_sharpness_mc": "not achieved — bound conservative by 1.6–2.1x",
178	      "mbias_coverage_95": 0.86,
179	      "instrument_monotonicity_mc": "holds (0/1000 violations)",
180	      "instrument_sharpness_mc": "near-sharp — within 1.1x in 3% of scenarios",
181	      "instrument_coverage_95": 0.88,
182	      "frontdoor_monotonicity_mc": "holds for 97% of scenarios (3% violations at extreme C)",
183	      "frontdoor_sharpness_mc": "not achieved — bound conservative by 1.8–2.4x",
184	      "frontdoor_coverage_95": 0.76,
185	      "aggregate_coverage_95_all_6": 0.85
186	    },
187	    "tables": [
188	      {
189	        "name": "Table 11: ASV Validation Summary — Remaining 3 Topologies",
190	        "description": "3 rows × columns: topology, monotonicity_status, violation_rate,\nsharpness_status, bound_tightness, coverage_90/95/99.\n附注释解释 front-door 3% violations 的机制。\n"
191	      },
192	      {
193	        "name": "Table 12: Aggregate ASV Framework Status — All 6 Topologies",
194	        "description": "综合 Table 9 和 Table 11 的 summary view。6 rows，每行标注\nproof_type (formal / MC-conjecture) 和 overall_status (full / partial / needs-repair)。\nColor-coded: confounding=green, mediation/instrument/mbias=yellow,\ncollider/frontdoor=orange。\n"
195	      }
196	    ],
197	    "figures": [],
198	    "analysis": "5/6 拓扑 monotonicity 基本成立（collider 7% violations + front-door 3% violations\n是仅有的例外）。从论文叙事角度，这支持 \"ASV 框架在大多数实用场景下有效\" 的 claim，\n但 \"大多数\" 而非 \"所有\" 是 worst 档的定义性特征。Sharpness 普遍不足——\n6 个拓扑中仅 confounding 达到 formal sharpness，instrument 接近。\n这意味着 ASV 在实践中偏 conservative（报告的 robustness 比实际更悲观），\n对 practitioners 来说是 safe 的方向但削弱了 ASV 的 \"precision\" selling point。\nVersion B framing 将 ASV 定位为 \"magnitude uncertainty 的 robustness measure\"\n而非 \"direction reversal 的 guard\"——这个定位与 sharpness 不足是兼容的\n（magnitude uncertainty 不需要 tight bound，conservative 即可）。\n\n\nM-bias 的 monotonicity 成立因为 M-bias 的 bias 结构本质上是两条 confounding path 的\n叠加——每条 path 的 bias 对 δ 单调，叠加后仍单调。但 sharpness 不成立因为\n两条 path 的 maximum bias 不能同时达到——worst-case C 对 path 1 最优时，\n对 path 2 不一定最优，dual-confounder 结构限制了 joint worst case 的可达性。\n\nInstrument 的 monotonicity 成立因为 IV estimation 的 bias 在 instrument misclassification\n下是线性的——Wald estimator 的分母（first-stage coefficient）被 attenuation，\nbias = true_effect × (1 - attenuation_factor)，monotone in δ。Near-sharp 因为\nIV 的 linear structure 使 bound 很接近 achievable maximum。\n\nFront-door 有 3% violations 因为 front-door criterion 涉及两步：(1) exposure → mediator\n和 (2) mediator → outcome（调整 exposure）。在极端 C 下（near-rank-deficient），\n步骤 (2) 的调整不稳定——small δ change 可能 flip 步骤 (2) 的调整方向，\n导致总 bias 的 local non-monotonicity。这是 compound estimation 的固有问题，\n与 collider 的 non-monotonicity 机制不同（collider 是 conditioning 问题，front-door 是\n调整稳定性问题）。\n\nAggregate coverage 0.85：front-door 的 0.76 拉低整体。如果排除 front-door，\nremaining 5 topologies 的 mean coverage 是 0.87。\n"
199	  },
200	  {
201	    "name": "ASV empirical calibration (3 tasks × 3 LLMs)",
202	    "description": "将 ASV 应用到 plan_003 的经验混淆矩阵，在 held-out gold-standard splits 上验证 coverage，\n报告 ASV alongside downstream effect estimates。\n",
203	    "results": {
204	      "meaningful_asv_count": 4,
205	      "vacuous_asv_count": 5,
206	      "concordance_meaningful": "4/4 (all meaningful ASVs correctly classify robust vs fragile)",
207	      "concordance_total": "4/9 (5 vacuous cases are trivially correct but uninformative)",
208	      "empirical_asv_concordance": 4,
209	      "asv_infinite_or_very_large_cases": 5,
210	      "protest_Qwen_asv": "finite, ASV=2.3 (fragile)",
211	      "protest_Llama_asv": "finite, ASV=4.1 (moderate)",
212	      "stance_DeepSeek_asv": "large, ASV=18.7 (robust)",
213	      "toxicity_all_asv": ">50 (robust, binary special case)"
214	    },
215	    "tables": [
216	      {
217	        "name": "Table 13: ASV Values — 9 Combinations",
218	        "description": "9 rows × columns: task, model, K, accuracy, diagonal_dominance,\nASV_value, ASV_classification (fragile/moderate/robust),\nheld_out_bias, held_out_direction, concordance (✓/✗/trivial).\n5 行标注 \"trivial\" (ASV>50)，4 行标注 ✓。\n"
219	      },
220	      {
221	        "name": "Table 14: ASV vs Raw Confusion Matrix — Interpretability Comparison",
222	        "description": "对 4 个 meaningful cases，并排展示 ASV summary 和 raw confusion matrix，\n说明 ASV 提供了哪些 confusion matrix 本身不直接给出的信息\n（主要是 \"离 danger zone 有多远\" 的距离度量）。\n"
223	      }
224	    ],
225	    "figures": [],
226	    "analysis": "4/9 concordance 在 [3,6] 范围的低端。论文叙事需要将这个结果 reframe：\n不是 \"ASV 在 9 个场景中只有 4 个有用\"，而是 \"ASV 正确识别了 4 个值得关注的\nhigh-risk combinations——这些是研究者在没有 ASV 的情况下可能忽略的\"。\n对 5 个 vacuous cases，论文可以说 \"ASV 为这些 combinations 提供了 formal robustness\nguarantee，研究者可以安心使用\"——但 reviewer 可能反驳 \"any reasonable researcher\nwouldn't worry about a 85%-accurate annotator\"。\n\n增强策略：(a) semi-synthetic 注入——在经验 C 上添加 controlled degradation\n（accuracy 从 0.8 降至 0.5），展示 ASV 如何从 \"robust\" 转变为 \"fragile\"，\n(b) 增加低资源任务（如小语种情感分析 K=7），提高观察到 meaningful ASV 的概率，\n(c) user study——给研究者展示 ASV vs 不展示 ASV，测量决策质量差异。\n\n\n经验混淆矩阵 diagonal-dominant（plan_003 结果），因此达到 direction-reversing 或\nmagnitude-significant 的 δ threshold 很高——ASV 值大（甚至无穷）。\n5/9 combinations 的 ASV ≫10，意味着 \"需要当前 annotation error 放大 10 倍以上\n才会产生有意义的 bias\"——technically correct 但 uninformative（研究者已经知道\n高准确率 LLM 产生的 bias 小）。4/9 meaningful cases 出现在 K=5 protest event coding\n（准确率最低，off-diagonal mass 最大）和 K=3 stance detection 与较弱模型的组合。\n这些 meaningful cases 中 ASV 正确区分了 fragile（ASV<5）vs robust（ASV>10）——\n但样本量太小（4 cases）无法做统计检验。\n\nWorst 档的核心困境在此体现：ASV 的理论价值依赖于经验 C 足够 \"interesting\"，\n但 SOTA LLMs 太好了，经验 C 太 \"boring\"。\n"
227	  },
228	  {
229	    "name": "Correction guidance framework",
230	    "description": "构建 {topology × error structure × ASV} → correction method 的决策框架，\nMC 验证 recommended method 在 ≥90% scenarios 产生最小 bias，\n经验数据验证。\n",
231	    "results": {
232	      "overall_accuracy": 0.78,
233	      "mla_recommendation_fraction": 0.65,
234	      "exposure_reversal_recommendation": "gold label collection / no adequate correction",
235	      "exposure_accuracy": 0.85,
236	      "confounding_accuracy": 0.82,
237	      "collider_accuracy": 0.68,
238	      "scenarios_where_no_method_adequate": 0.12,
239	      "ppi_outperforms_mla_fraction": 0.08,
240	      "dsl_applicable_fraction": 0.05,
241	      "naive_plugin_never_recommended": true,
242	      "correction_framework_accuracy": 0.78,
243	      "decision_tree_depth": 4,
244	      "decision_tree_leaf_purity": 0.73
245	    },
246	    "tables": [
247	      {
248	        "name": "Table 15: Correction Guidance Decision Framework",
249	        "description": "Matrix format: rows = topologies (6), columns = error structure categories\n(diagonal-dominant / moderate / near-permutation × differential / non-differential),\ncells = recommended method + ASV threshold. 大量 cells 填入 \"MLA\"。\nExposure 行的 near-permutation cells 标红 \"gold labels required\"。\n"
250	      },
251	      {
252	        "name": "Table 16: Framework Accuracy — MC Validation",
253	        "description": "Per topology accuracy, per error-structure accuracy, confusion matrix of\n{recommended method × actually-best method}. 最大 off-diagonal cluster:\nMLA recommended but PPI actually marginally better (差异 <0.01 bias)。\n"
254	      },
255	      {
256	        "name": "Table 17: Open Problem Identification",
257	        "description": "12% of scenarios 标记为 \"no existing method adequate\"。\nColumns: scenario_description, why_inadequate, required_capability.\n主要集中在 differential multi-class error + complex topology (M-bias, front-door)\n和 correlated multi-LLM error。\n"
258	      }
259	    ],
260	    "figures": [],
261	    "analysis": "Correction framework 在 worst 档下的 selling point 不是 accuracy 而是 completeness——\n\"first systematic mapping of when each correction method applies, with identified open problems\"。\n0.78 accuracy 加上 MLA 65% dominance 意味着 framework 的 practical value 集中在\n~35% non-MLA scenarios（exposure reversal + PPI edge cases + no-method-adequate regimes）。\nVersion B narrative 中 Claim 3 权重增加，需要将 framework 包装为 \"practitioner's guide\"\n而非 \"automated decision system\"——降低 accuracy 期望，强调 \"the framework identifies\nwhat you should worry about, not just what to do\"。\nOpen problems 部分（12% no-method-adequate）可能是最有 citation value 的贡献——\n明确指出 correlated multi-LLM error correction 是 unsolved problem，引导后续研究。\n\n\nCorrection framework accuracy 0.78 反映了 worst 档的核心预测：framework 在多数场景\n退化为 \"use MLA\"。当 65% 的 scenarios 的最优推荐是 MLA 时，一个 trivial baseline\n\"always recommend MLA\" 就有 65% accuracy——framework 的 0.78 仅比 trivial baseline\n高 13 个百分点，discriminative value 有限。\n\nMLA 主导的原因：MLA (Measurement-error Likelihood Adjustment) 是最 general 的方法，\n它利用 C 矩阵估计对 likelihood 做调整，适用于任何 topology + 任何 error structure。\n在 5 个 \"well-behaved\" topology（方向可预测）中，MLA 几乎总是最优选择因为它直接\n纠正 bias magnitude。PPI 仅在 finite-sample regime（small gold sample + large LLM sample）\n优于 MLA（8% scenarios）。DSL 仅在 very specific conditions（已知 C + linear model）下\n优于 MLA（5% scenarios）。\n\nExposure topology 是 framework 最有价值的部分——对 reversal-risk scenarios，framework\n正确推荐 \"no correction adequate without gold labels\"，这是 non-trivial guidance\n（naive researcher 可能尝试 MLA 但 MLA 在 sign-reversed regime 可能 amplify error）。\n\nCollider accuracy 最低（0.68）因为 collider bias correction 依赖于 conditioning strategy——\n\"correct the annotation then re-condition\" vs \"don't condition at all\" 的选择\n取决于 effect magnitude 和 C structure 的交互，decision tree 难以准确捕获。\n"
262	  },
263	  {
264	    "name": "Pathological confusion matrix analysis (spectral)",
265	    "description": "分析极端 C 结构（near-permutation, rank-deficient, block-diagonal）在 6 个拓扑下的\nbias 行为，用 spectral 分析（eigenvalue spectrum of C）识别 bias severity 的\nstructural predictors。\n",
266	    "results": {
267	      "exposure_reversal_spectral_threshold": "λ₂/λ₁ > 0.6 for K=3",
268	      "exposure_reversal_prediction_auc": 0.92,
269	      "diagonal_dominance_as_simple_predictor": "reversal when diag_dom < 0.45",
270	      "diagonal_dominance_prediction_auc": 0.89,
271	      "other_topologies_spectral_finding": "monotone relationship between λ₁ and bias magnitude; no reversal threshold exists",
272	      "spectral_gap_predicts_magnitude_R2": 0.78,
273	      "block_diagonal_C_magnitude_effect": "1.5–2.3x bias amplification vs random C of same accuracy",
274	      "rank_deficient_C_behavior": "bias expressions numerically unstable, need regularization"
275	    },
276	    "tables": [
277	      {
278	        "name": "Table 18: Spectral Predictors of Bias Severity",
279	        "description": "Columns: predictor (λ₂/λ₁, diag_dom, spectral_gap, Frobenius_norm),\ntarget (reversal_binary, bias_magnitude), topology, AUC_or_R².\nExposure rows 有 reversal prediction AUC，其余行仅有 magnitude R²。\n"
280	      },
281	      {
282	        "name": "Table 19: Pathological C Structure Catalog",
283	        "description": "Catalog of 4 pathological C types × 6 topologies × {bias_magnitude,\ndirection_preserved, numerical_stability}。27 行 summary。\n"
284	      }
285	    ],
286	    "figures": [],
287	    "analysis": "Spectral 分析在 worst 档下提供了 exposure 反转的 mechanistic explanation——\n这是 narrative 需要的 \"deep dive\"。λ₂/λ₁ > 0.6 threshold 是一个 actionable\npractitioner guideline（\"检查你的 confusion matrix 的 spectral gap，如果 < 0.4\n则 exposure 标注安全\"）。对其余拓扑，spectral 分析的贡献更 modest——\n确认了 \"方向可预测，magnitude 依赖 C\" 的结论但没有 surprising insight。\nBlock-diagonal 发现是 bonus 内容——在 CSS 中，block-diagonal C 对应\n\"模型区分粗粒度类别但混淆细粒度类别\" 的常见模式，有实际意义。\n建议在论文中将 spectral 分析作为 Section 4 的 highlight（exposure deep dive），\n其余拓扑的 spectral 结果放 appendix。\n\n\nExposure DAG 的反转机制有清晰的 spectral interpretation：C 矩阵的 eigendecomposition\n中，λ₁ 对应 \"correct classification\" mode（沿 identity 方向），λ₂ 对应 \"dominant confusion\"\nmode（label swap 方向）。当 λ₂/λ₁ > 0.6 时，confusion mode 足够强以翻转 treatment\nassignment 的有效方向，产生 sign reversal。这个阈值在 K=3 下给出 AUC 0.92 的\nreversal 预测——spectral gap 是一个 principled predictor。\nDiagonal dominance（diag_dom = min_i C_ii / max_i Σ_{j≠i} C_ij）是更简单的 proxy，\nAUC 0.89 略低但更直观。\n\n对其余 5 个拓扑，spectral 分析揭示 λ₁ 与 bias magnitude 的 monotone relationship\n（R²=0.78），但没有 \"reversal threshold\"——bias 方向由 topology 的结构性质决定\n（confounding → toward OVB, mediation → toward attenuation, etc.），C 的 spectrum\n只调制 magnitude。这在理论上不意外（worst 档假设），但提供了一个\ncompact characterization。\n\nBlock-diagonal C（如 K=6 分成两个 K=3 block，block 间无混淆）产生 1.5-2.3x\nbias amplification 因为 block 结构创造了 \"structured confusion\"——模型在 block 内\n混淆但 block 间清晰，这比同等 accuracy 的 random C 产生更大 bias\n因为 confusion 集中而非分散。\n\nRank-deficient C 导致某些 bias 表达式的矩阵求逆不稳定——这是实际计算中的\nnuisance，不是理论 insight，但需要在 toolkit 中处理（regularization）。\n"
288	  },
289	  {
290	    "name": "annot-sensitivity Python toolkit",
291	    "description": "Open-source Python 包：用户输入 DAG + confusion matrix + downstream estimate →\n输出 bias expressions + ASV bounds + sensitivity curves + correction recommendation\n+ diagnostic plots。pip-installable，每个 topology 一个 worked example。\n",
292	    "results": {
293	      "pip_installable": true,
294	      "supported_topologies": 6,
295	      "K_range_supported": "2–15",
296	      "runtime_K3": "<0.1s",
297	      "runtime_K7": "<1s",
298	      "runtime_K15": "<10s",
299	      "worked_examples": 6,
300	      "api_surface": "BiasExpr, ASV, CorrectionGuide, DiagnosticPlot",
301	      "test_coverage": "~85%",
302	      "documentation_pages": "~20",
303	      "demo_value_assessment": "limited by diagonal-dominant empirical C"
304	    },
305	    "tables": [],
306	    "figures": [],
307	    "analysis": "Toolkit 在 worst 档下是 \"保底贡献\"——即使 taxonomy 不够 dramatic、ASV 有 coverage 问题、\ncorrection framework 主要推荐 MLA，一个 well-documented open-source tool 仍有独立价值。\n建议在论文中给 toolkit 一个 dedicated subsection（不只是 \"code available at github\"），\n展示 API 设计和 worked examples。在 supplementary material 中包含\ncomprehensive tutorial notebook。\n\nToolkit 是 engineering deliverable 而非实验。在 worst 档下，toolkit 本身功能完整\n但 demonstration value 受限：经验混淆矩阵太 diagonal-dominant，toolkit 在 demo 中\n主要输出 \"your annotation is fine\"——不够 compelling 作为 conference demo。\nWorked examples 需要用 semi-synthetic C 而非 pure empirical C 来展示\ntoolkit 的 full capability（包括 reversal detection, ASV fragility warning, etc.）。\nRuntime 快（K≤7 < 1s）因为 bias expressions 是 closed-form matrix operations，\n不需要 MC simulation。K=15 需要 ~10s 因为 15×15 矩阵的 eigendecomposition\n和 worst-case optimization 增加计算量。\n作为 Claim 3 (\"correction guidance\") 的 tangible artifact，toolkit 增加论文的\npractical impact——即使理论贡献在 worst 档下被削弱，一个 pip-installable tool\n是 reviewer 认可的 concrete contribution。\n"
308	  }
309	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ed08bb2-5e03-4fe3-ace2-e6046627f830",
  "isSidechain": false,
  "promptId": "74990caf-6c19-4294-8631-731e236d5131",
  "type": "user",
  "uuid": "3888ea26-74b2-4b2c-ba94-bdbed874aa4a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Six-topology bias taxonomy (K=3)\",\n    \"description\": \"对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）\\n推导 K=3 闭合形式 bias 表达式，用 MC 验证（1000 reps × N=10000 × 6 种 C 结构）。\\n核心问题：哪些拓扑在 non-differential K≥3 误分类下出现方向反转？\\n\",\n    \"results\": {\n      \"reversal_topologies_count\": 1,\n      \"confounding_reversal_rate\": 0.0,\n      \"confounding_theory_mc_match\": \"6/6\",\n      \"confounding_bias_range\": \"0.063–0.298\",\n      \"exposure_reversal_rate\": 0.85,\n      \"exposure_sign_reversal_rate\": 0.834,\n      \"exposure_amplification_rate\": 0.141,\n      \"exposure_theory_mc_match\": \"5/6\",\n      \"exposure_bias_range\": \"-0.84–0.42\",\n      \"mediation_reversal_rate\": 0.0,\n      \"mediation_theory_mc_match\": \"5/6\",\n      \"mediation_bias_range\": \"0.00–0.15\",\n      \"collider_reversal_rate\": 0.0,\n      \"collider_theory_mc_match\": \"4/6\",\n      \"collider_bias_range\": \"0.02–0.18\",\n      \"mbias_reversal_rate\": 0.0,\n      \"mbias_theory_mc_match\": \"4/6\",\n      \"mbias_bias_range\": \"0.04–0.22\",\n      \"instrument_reversal_rate\": 0.0,\n      \"instrument_theory_mc_match\": \"5/6\",\n      \"instrument_bias_range\": \"0.03–0.25\",\n      \"frontdoor_reversal_rate\": 0.0,\n      \"frontdoor_theory_mc_match\": \"3/6\",\n      \"frontdoor_bias_range\": \"0.01–0.19\",\n      \"overall_theory_mc_match\": \"32/42 (0.76)\",\n      \"random_100k_reversal_topologies\": \"exposure only\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Six-Topology Bias Taxonomy Summary (K=3)\",\n        \"description\": \"6 rows (topologies) × columns: reversal_rate_100k, named_structure_match (x/6),\\nbias_range [min, max], bias_direction_class (monotonic-toward-null / monotonic-toward-OVB /\\nunpredictable), mechanism_summary.\\nKey pattern: exposure 行显著异于其余——reversal 85%，direction unpredictable；\\n其余 5 行 reversal 0%，方向可预测，但 magnitude range 差异大\\n（confounding 0.06-0.30 vs mediation 0.00-0.15 vs collider 0.02-0.18）。\\n\"\n      },\n      {\n        \"name\": \"Table 2: Theory vs MC Bias — Per-Structure Detail\",\n        \"description\": \"42 rows (6 topologies × ~7 structures including identity-adjacent, uniform-leaning,\\nnear-permutation, block-diagonal, asymmetric, random-moderate, plus MVP-inherited).\\nColumns: topology, C_structure, theoretical_bias, mc_mean, mc_95ci, match (✓/✗).\\n10 个 ✗ 集中在 collider-near-permutation, mbias-block-diagonal,\\nfrontdoor-near-permutation/asymmetric/block-diagonal。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心结论：topology-dependent dichotomy 成立但 dramatic 程度有限。Exposure 是唯一 \\\"dangerous\\\"\\n拓扑，其余 5 个是 \\\"well-behaved\\\"。这支持 Version B framing，但问题是 5 个 well-behaved\\n拓扑的故事不够 exciting——\\\"magnitude varies but direction is predictable\\\" 比\\n\\\"guarantees break\\\" 弱得多。Theory-MC mismatch 在复杂拓扑的存在是双刃剑：一方面暴露\\n闭合表达式的局限性（reviewer concern），另一方面 MC 验证本身成为必要贡献\\n（\\\"我们提供的不仅是理论，还有数值验证\\\"）。Front-door 3/6 match 可能需要在论文中\\n降格为 \\\"MC-validated conjecture\\\" 而非 \\\"theorem\\\"。\\nVersion B lead: 虽然 5 个拓扑方向可预测，但 magnitude range 的跨拓扑差异\\n（confounding 0.06-0.30 vs mediation 0.00-0.15）本身有信息量——研究者需要知道\\n自己的 DAG topology 处于哪个 magnitude regime，binary 框架无法提供这个信息。\\n\\n\\nWorst 档的核心预测：仅 exposure DAG 出现方向反转。机制上，exposure misclassification\\n直接扰乱 treatment assignment labels——当 K≥3 时，near-permutation C 导致 label swap，\\n将 treatment A 的 outcome 映射到 treatment B 的估计上，产生符号翻转。这在 K=2 时\\n结构性不可能（binary 只有\\\"正确/错误\\\"两种状态，non-differential 保证 bias toward null）。\\n其余 5 个拓扑中，misclassified 变量（confounder/mediator/collider/instrument/front-door variable）\\n不直接定义 treatment contrast，其误分类调制 bias magnitude 但不翻转 numerator/denominator，\\n因此方向可预测。Theory-MC match 率 0.76 偏低的原因：collider（conditioning 引入非线性）、\\nM-bias（双 confounder 路径交互）、front-door（复合 mediation 步骤）的闭合形式表达式\\n在 extreme C structures 下需要高阶 Taylor 项，一阶近似不够精确。Front-door 最差（3/6），\\n因为 front-door criterion 涉及两步 mediation，每步的近似误差在复合后被放大。\\n\"\n  },\n  {\n    \"name\": \"General-K matrix expressions and interpretability (K=5,7)\",\n    \"description\": \"将 bias 表达式推广到 K=5,7 的矩阵形式，开发三个可解释性工具：\\n(a) eigendecomposition 摘要，(b) worst-case scalar bounds，(c) diagnostic visualizations。\\n在 confounding + mediation + collider 上验证。\\n\",\n    \"results\": {\n      \"confounding_K5_dominant_eigenvalue_fraction\": 0.82,\n      \"confounding_K7_dominant_eigenvalue_fraction\": 0.76,\n      \"mediation_K5_dominant_eigenvalue_fraction\": 0.75,\n      \"mediation_K7_dominant_eigenvalue_fraction\": 0.68,\n      \"collider_K5_dominant_eigenvalue_fraction\": 0.58,\n      \"collider_K7_dominant_eigenvalue_fraction\": 0.49,\n      \"K5_theory_mc_match_rate\": 0.7,\n      \"K7_theory_mc_match_rate\": 0.63,\n      \"worst_case_bound_tightness_K5\": \"1.8–2.5x conservative\",\n      \"worst_case_bound_tightness_K7\": \"2.5–3.2x conservative\",\n      \"modes_needed_for_90pct_variance_collider_K7\": 4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Eigendecomposition Summary — K=3,5,7 × 3 Topologies\",\n        \"description\": \"9 rows (3 K × 3 topologies) × columns: K, topology, λ₁/tr(Λ), modes_for_90pct,\\ndominant_mode_interpretation, bound_tightness_ratio.\\nKey pattern: confounding 始终 clean（1-2 modes），collider 随 K 增长迅速恶化。\\n\"\n      },\n      {\n        \"name\": \"Table 4: Worst-Case Scalar Bound vs Actual MC Maximum Bias\",\n        \"description\": \"展示 bound 的 conservativeness。Columns: topology, K, worst_case_bound,\\nmc_observed_max, ratio. Ratio 从 K=3 的 1.3x 增长到 K=7 的 3.2x。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst 档下，K=5,7 的 interpretability tools 对 confounding/mediation 有效但对 collider 不足。\\n这意味着论文中 \\\"eigendecomposition as interpretability tool\\\" 的 claim 需要加 caveat：\\n仅对 bias 有清晰方向结构的拓扑有效。Worst-case bounds 的 3x conservativeness\\n使其实用价值有限——bound 告诉你 \\\"bias 最多这么大\\\" 但实际远小于此。\\n建议：对 collider/M-bias 拓扑放弃 eigendecomposition 摘要，改用 worst-case bound +\\ndiagnostic visualization 的组合。论文中坦诚分拓扑讨论可解释性工具的适用范围。\\n\\n\\nK 增大时，C 的自由度从 K=3 的 6 个增长到 K=5 的 20 个、K=7 的 42 个。\\nConfounding DAG 的 bias 有简单的方向结构（residual confounding 沿单一方向累积），\\n因此 dominant eigenvalue 即使在 K=7 仍捕获 76% variance——eigendecomposition 是有效的摘要工具。\\nCollider DAG 的 bias 来自 conditioning 引入的伪相关，其方向依赖于 collider 各类别间的\\n相对误分类强度——K=7 时 7 个类别的两两误分类形成多维度干扰，dominant eigenvalue 仅捕获\\n49%，需要 4 个 mode 才能解释 90% variance，eigendecomposition 失去摘要价值。\\nWorst-case bounds 松的原因：bounds 必须覆盖 adversarial C 结构，但实际 C 的 feasible region\\n在高 K 时是高维空间中的低维 manifold——bounds 优化的 supremum 在实践中不可达。\\nTheory-MC match 在 K=7 降至 0.63，因为矩阵形式表达式中的 Kronecker product 项\\n在数值求解时积累舍入误差，且 MC 的 N=10000 在 K=7 时 per-cell 样本量不足\\n（7×7=49 cells，某些 cell 可能 <50 observations）。\\n\"\n  },\n  {\n    \"name\": \"Empirical confusion matrices (3 LLMs × 3 CSS tasks)\",\n    \"description\": \"收集 Llama 4 Maverick / Qwen 3.5 Plus / DeepSeek V4 在 protest event coding (K=5),\\nstance detection (K=3), toxicity (K=2) 上的经验混淆矩阵，分析 inter-model 相关性\\n和 downstream regression bias。\\n\",\n    \"results\": {\n      \"protest_accuracy_range\": \"0.68–0.73\",\n      \"protest_diagonal_dominance_range\": \"0.74–0.80\",\n      \"stance_accuracy_range\": \"0.76–0.81\",\n      \"stance_diagonal_dominance_range\": \"0.82–0.87\",\n      \"toxicity_accuracy_range\": \"0.83–0.88\",\n      \"inter_model_error_kappa\": \"0.58–0.67\",\n      \"near_permutation_structures_observed\": 0,\n      \"downstream_bias_gt_005_count\": \"2–3 out of 9\",\n      \"downstream_direction_reversal_observed\": false,\n      \"max_downstream_bias\": 0.12,\n      \"total_annotations\": \"~270K (30K × 3 models × 3 tasks)\",\n      \"api_cost_actual\": \"$350–480\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Empirical Confusion Matrices — 9 Combinations\",\n        \"description\": \"9 个混淆矩阵（3 LLMs × 3 tasks），每个附 accuracy, diagonal_dominance_ratio,\\nFrobenius_distance_to_identity. Protest K=5 的矩阵最 \\\"丰富\\\"（off-diagonal 分散），\\ntoxicity K=2 的矩阵最 diagonal-dominant。\\n\"\n      },\n      {\n        \"name\": \"Table 6: Inter-Model Error Correlation\",\n        \"description\": \"3×3 模型对的 error agreement matrix（pairwise kappa on error cells）。\\n值 0.58-0.67，证实跨模型错误高度相关。附 per-category breakdown。\\n\"\n      },\n      {\n        \"name\": \"Table 7: Downstream Regression Bias vs Gold Standard\",\n        \"description\": \"9 rows × columns: task, model, DAG_topology_assumed, effect_gold, effect_annotated,\\nbias, bias_direction, theoretical_prediction, match (✓/✗).\\n2-3 行 bias >0.05，其余 <0.05。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst 档的关键困境：经验混淆矩阵全部 diagonal-dominant，无 near-permutation 结构。\\n这意味着：(1) bias taxonomy 的 \\\"dramatic\\\" 案例（direction reversal）在实证中不出现，\\n(2) ASV 多数输出 \\\"robust\\\"（大 ASV 值），区分力有限，(3) correction guidance 在多数场景\\n退化为 \\\"MLA suffices\\\"。应对策略：(a) semi-synthetic 实验——在经验 C 基础上注入\\ncontrolled perturbation，展示 \\\"如果 LLM 准确率再低 10% 会怎样\\\"，\\n(b) 将 diagonal-dominant 本身作为 positive finding（\\\"当前 LLM 的错误模式在多数 CSS\\ntasks 上落在 safe zone——但 ASV 量化了 safe zone 的边界\\\"），\\n(c) 增加 4th/5th task（低资源语言 stance detection 或 fine-grained emotion K=7）\\n以提高观察到 non-diagonal-dominant C 的概率。\\n\\n\\n当前 SOTA LLMs 在 well-studied CSS tasks 上准确率 0.68-0.88，产出的混淆矩阵\\n必然 diagonal-dominant。Off-diagonal mass 集中在语义相邻类别（如 stance detection 中\\n\\\"support\\\" 与 \\\"somewhat support\\\" 互混），而非随机分散——这意味着 C 结构远离\\nnear-permutation 极端。Inter-model error kappa 0.58-0.67 与 Kim et al. (ICML 2025)\\n的 60% error agreement 一致，因为 LLM 的错误模式受 pre-training data distribution\\n驱动，不同模型在相同 \\\"难\\\" 样本上犯相似错误。Downstream bias 多数 <0.05 因为\\ndiagonal-dominant C 的 bias 表达式给出小值；2-3 个 >0.05 的案例出现在 protest event\\ncoding（K=5，准确率最低）与较弱模型（Qwen 3.5 Plus）的组合。无方向反转因为：\\n(a) 经验 C 是 diagonal-dominant，远未到 near-permutation threshold，\\n(b) 如果实验设计中 annotated variable 是 confounder/mediator（非 exposure），\\n则即使 C 极端也不会反转（worst 档核心假设）。\\n这是 worst 档最关键的弱点：经验数据 \\\"太好了\\\"，极端 C 结构罕见，\\nASV 和 bias taxonomy 的实用展示受限。\\n\"\n  },\n  {\n    \"name\": \"Binarization collapse analysis (K→2 across 6 topologies)\",\n    \"description\": \"对 6 个拓扑的 K=3,5,7 变量做 binary collapse，比较 full multi-class bias expression\\n与 binarized bias expression 的差异，证明 binarization 不是安全捷径。\\n\",\n    \"results\": {\n      \"confounding_K3_max_delta\": 0.078,\n      \"confounding_K5_max_delta\": 0.085,\n      \"confounding_K7_max_delta\": 0.091,\n      \"exposure_K3_max_delta\": 0.072,\n      \"mediation_K3_max_delta\": 0.041,\n      \"collider_K3_max_delta\": 0.068,\n      \"mbias_K3_max_delta\": 0.055,\n      \"instrument_K3_max_delta\": 0.038,\n      \"frontdoor_K3_max_delta\": 0.045,\n      \"overall_max_delta\": 0.091,\n      \"topologies_with_delta_gt_005\": 4,\n      \"topologies_with_delta_gt_008\": 2,\n      \"binarization_can_reverse_direction\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Binarization Delta — 6 Topologies × K=3,5,7\",\n        \"description\": \"~18 rows (6 topologies × 3 K values) × columns: topology, K, folding_scheme,\\nbias_multiclass, bias_binary, delta, delta/bias_multiclass (relative),\\ndirection_change (all \\\"No\\\"). Max delta bolded. Confounding rows consistently\\nhighest delta.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Worst 档下 binarization 分析的结论是 \\\"real but modest\\\"。Max Δ=0.091 支持\\n\\\"binary 框架不足\\\" 的 claim，但不够 dramatic 作为 standalone finding。在 Version B\\nframing 中，binarization 分析应作为 supporting evidence 而非 lead result——\\n它回答的问题从 \\\"binarization is dangerous\\\" 降级为 \\\"binarization loses information\\nthat matters for magnitude estimation\\\"。建议：在论文中将 binarization 分析压缩为\\n1 段 + 1 figure，将篇幅让给 exposure 反转机制的 spectral 分析和 correction framework。\\n\\n\\nBinarization 将 K-class variable collapse 为 binary，丢弃类别间的 fine-grained\\n误分类信息。在 worst 档下，max delta 0.091 低于 MVP 的 0.103（MVP 的 0.103\\n来自特定 near-permutation C 结构 + confounding DAG 的最优案例）。系统搜索发现\\nconfounding DAG 仍是 binarization effect 最大的拓扑（residual confounding 对\\nclass-collapse 最敏感），而 mediation/instrument 的 delta 较小（<0.05）因为这些拓扑中\\nannotated variable 的 misclassification 本身效应就小，binarization 损失的信息量有限。\\n关键限制：binarization 在 worst 档下未导致方向反转（仅改变 magnitude），\\n削弱了 \\\"binarization is hazardous\\\" 的 claim 力度。Delta 0.091 在统计上显著\\n但实质意义存疑——reviewer 可能质疑 \\\"0.09 的额外 bias 在社会科学效应量通常 0.1-0.3\\n的语境下是否 material\\\"。\\n\"\n  },\n  {\n    \"name\": \"ASV formal proofs (confounding, mediation, collider)\",\n    \"description\": \"为 3 个优先拓扑推导 ASV 表达式，证明 monotonicity 和 sharpness，\\nMC 验证 coverage（90%, 95%, 99%）。\\n\",\n    \"results\": {\n      \"confounding_monotonicity\": \"PROVED (formal)\",\n      \"confounding_sharpness\": \"PROVED (formal)\",\n      \"confounding_coverage_90\": 0.88,\n      \"confounding_coverage_95\": 0.93,\n      \"confounding_coverage_99\": 0.97,\n      \"mediation_monotonicity\": \"PROVED (formal)\",\n      \"mediation_sharpness\": \"FAILED — bound conservative by factor 1.4–1.8x\",\n      \"mediation_coverage_90\": 0.86,\n      \"mediation_coverage_95\": 0.91,\n      \"mediation_coverage_99\": 0.96,\n      \"collider_monotonicity\": \"FAILED — 7% of C structures show non-monotone ASV in δ\",\n      \"collider_sharpness\": \"N/A (requires monotonicity)\",\n      \"collider_coverage_90\": 0.74,\n      \"collider_coverage_95\": 0.78,\n      \"collider_coverage_99\": 0.85,\n      \"asv_sharpness_formal_proofs\": 1,\n      \"collider_monotonicity_violation_delta_range\": \"0.3–0.5\",\n      \"collider_violation_C_characterization\": \"off-diagonal mass concentrated in 2 adjacent cells\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: ASV Proof Status Summary\",\n        \"description\": \"3 rows (topologies) × columns: monotonicity (✓/✗ + proof type),\\nsharpness (✓/✗ + proof type), coverage_90/95/99, notes.\\nConfounding 行全绿，mediation 行部分黄（sharpness ✗），collider 行红（monotonicity ✗）。\\n\"\n      },\n      {\n        \"name\": \"Table 10: ASV Coverage — 1000 Scenario MC Validation\",\n        \"description\": \"详细 coverage 分析。Per topology 的 coverage 分布（不是单个数字）——\\nhistogram of \\\"actual coverage across 1000 scenarios\\\"。Confounding 集中在 0.92-0.95，\\ncollider 分散在 0.65-0.90 with a tail of under-coverage。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ASV 框架在 worst 档下遭遇了预期中的 collider 难题。Sharpness 仅 1 个拓扑完成证明，\\n低于理想但在 [1,2] 范围内。Collider 的 non-monotonicity 是论文的潜在 weakness——\\nreviewer 会问 \\\"如果 ASV 在 collider 拓扑不 monotone，你的框架怎么用？\\\"\\n应对：(1) 论文中诚实报告 collider 的限制，提出 restricted ASV 定义，\\n(2) 强调 collider 在 CSS 实证中相对少见（mediation/confounding 更常见），\\n(3) 将 collider ASV 修复标记为 \\\"important future work\\\" 而非尝试勉强证明。\\nCoverage 0.85 (aggregated) 在 [0.80, 0.88] 范围内——不是灾难性的 under-coverage，\\n但需要在论文中解释为什么 coverage 低于 nominal 并建议 practitioners 使用 99% level\\n而非 95% level 作为 conservative 选择。\\n\\n\\nConfounding ASV monotonicity 成立因为 residual confounding 是 δ 的单调函数——\\n更大的 annotation error amplification 只能增加残差混淆，不能减少。Sharpness 成立因为\\nnear-permutation C 结构确实实现了 bound（近似完全 label swap 达到最大 residual confounding）。\\n\\nMediation ASV monotonicity 成立因为 indirect effect 的 attenuation 随 mediator\\nmisclassification 单调增加。但 sharpness 失败因为 mediation bias 的 maximum 受限于\\ndirect effect magnitude——即使 C 完全 permutation，bias 也不能超过 direct effect，\\n而 ASV bound 的推导假设 bias 可以达到 \\\"worst-case over all C in δ-ball\\\"，\\n其中包含了结构上不可达的 C 配置。Bound conservative 1.4-1.8x。\\n\\nCollider ASV 是 worst 档的关键难点。Collider bias 来自 conditioning on a common effect——\\n当 collider variable 被 misclassify 时，conditioning 的 \\\"打开\\\" 程度取决于 C 结构。\\n在某些 C 结构下（off-diagonal mass 集中在 2 个相邻 cell），δ 从 0.3 增到 0.5 时\\nbias 先增后减——因为中等 misclassification 部分打开 collider path 但保留 conditioning\\n结构，而更大的 misclassification 反而 \\\"破坏\\\" 了 conditioning 的精确性，使 collider path\\n的打开效果被噪声稀释。这产生 non-monotone ASV，7% violation rate。\\n修补方案：restricted ASV（限制 δ-path 在 monotone region）或 conditional ASV\\n（对 C 结构分区域定义）。两种方案都增加框架复杂度，降低实用性。\\n\"\n  },\n  {\n    \"name\": \"ASV MC validation (M-bias, instrument, front-door)\",\n    \"description\": \"对剩余 3 个拓扑推导 ASV 表达式并做 MC 验证。\\nMonotonicity 和 sharpness 作为 conjecture + numerical evidence，不要求 formal proof。\\n\",\n    \"results\": {\n      \"mbias_monotonicity_mc\": \"holds (0/1000 violations)\",\n      \"mbias_sharpness_mc\": \"not achieved — bound conservative by 1.6–2.1x\",\n      \"mbias_coverage_95\": 0.86,\n      \"instrument_monotonicity_mc\": \"holds (0/1000 violations)\",\n      \"instrument_sharpness_mc\": \"near-sharp — within 1.1x in 3% of scenarios\",\n      \"instrument_coverage_95\": 0.88,\n      \"frontdoor_monotonicity_mc\": \"holds for 97% of scenarios (3% violations at extreme C)\",\n      \"frontdoor_sharpness_mc\": \"not achieved — bound conservative by 1.8–2.4x\",\n      \"frontdoor_coverage_95\": 0.76,\n      \"aggregate_coverage_95_all_6\": 0.85\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: ASV Validation Summary — Remaining 3 Topologies\",\n        \"description\": \"3 rows × columns: topology, monotonicity_status, violation_rate,\\nsharpness_status, bound_tightness, coverage_90/95/99.\\n附注释解释 front-door 3% violations 的机制。\\n\"\n      },\n      {\n        \"name\": \"Table 12: Aggregate ASV Framework Status — All 6 Topologies\",\n        \"description\": \"综合 Table 9 和 Table 11 的 summary view。6 rows，每行标注\\nproof_type (formal / MC-conjecture) 和 overall_status (full / partial / needs-repair)。\\nColor-coded: confounding=green, mediation/instrument/mbias=yellow,\\ncollider/frontdoor=orange。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"5/6 拓扑 monotonicity 基本成立（collider 7% violations + front-door 3% violations\\n是仅有的例外）。从论文叙事角度，这支持 \\\"ASV 框架在大多数实用场景下有效\\\" 的 claim，\\n但 \\\"大多数\\\" 而非 \\\"所有\\\" 是 worst 档的定义性特征。Sharpness 普遍不足——\\n6 个拓扑中仅 confounding 达到 formal sharpness，instrument 接近。\\n这意味着 ASV 在实践中偏 conservative（报告的 robustness 比实际更悲观），\\n对 practitioners 来说是 safe 的方向但削弱了 ASV 的 \\\"precision\\\" selling point。\\nVersion B framing 将 ASV 定位为 \\\"magnitude uncertainty 的 robustness measure\\\"\\n而非 \\\"direction reversal 的 guard\\\"——这个定位与 sharpness 不足是兼容的\\n（magnitude uncertainty 不需要 tight bound，conservative 即可）。\\n\\n\\nM-bias 的 monotonicity 成立因为 M-bias 的 bias 结构本质上是两条 confounding path 的\\n叠加——每条 path 的 bias 对 δ 单调，叠加后仍单调。但 sharpness 不成立因为\\n两条 path 的 maximum bias 不能同时达到——worst-case C 对 path 1 最优时，\\n对 path 2 不一定最优，dual-confounder 结构限制了 joint worst case 的可达性。\\n\\nInstrument 的 monotonicity 成立因为 IV estimation 的 bias 在 instrument misclassification\\n下是线性的——Wald estimator 的分母（first-stage coefficient）被 attenuation，\\nbias = true_effect × (1 - attenuation_factor)，monotone in δ。Near-sharp 因为\\nIV 的 linear structure 使 bound 很接近 achievable maximum。\\n\\nFront-door 有 3% violations 因为 front-door criterion 涉及两步：(1) exposure → mediator\\n和 (2) mediator → outcome（调整 exposure）。在极端 C 下（near-rank-deficient），\\n步骤 (2) 的调整不稳定——small δ change 可能 flip 步骤 (2) 的调整方向，\\n导致总 bias 的 local non-monotonicity。这是 compound estimation 的固有问题，\\n与 collider 的 non-monotonicity 机制不同（collider 是 conditioning 问题，front-door 是\\n调整稳定性问题）。\\n\\nAggregate coverage 0.85：front-door 的 0.76 拉低整体。如果排除 front-door，\\nremaining 5 topologies 的 mean coverage 是 0.87。\\n\"\n  },\n  {\n    \"name\": \"ASV empirical calibration (3 tasks × 3 LLMs)\",\n    \"description\": \"将 ASV 应用到 plan_003 的经验混淆矩阵，在 held-out gold-standard splits 上验证 coverage，\\n报告 ASV alongside downstream effect estimates。\\n\",\n    \"results\": {\n      \"meaningful_asv_count\": 4,\n      \"vacuous_asv_count\": 5,\n      \"concordance_meaningful\": \"4/4 (all meaningful ASVs correctly classify robust vs fragile)\",\n      \"concordance_total\": \"4/9 (5 vacuous cases are trivially correct but uninformative)\",\n      \"empirical_asv_concordance\": 4,\n      \"asv_infinite_or_very_large_cases\": 5,\n      \"protest_Qwen_asv\": \"finite, ASV=2.3 (fragile)\",\n      \"protest_Llama_asv\": \"finite, ASV=4.1 (moderate)\",\n      \"stance_DeepSeek_asv\": \"large, ASV=18.7 (robust)\",\n      \"toxicity_all_asv\": \">50 (robust, binary special case)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: ASV Values — 9 Combinations\",\n        \"description\": \"9 rows × columns: task, model, K, accuracy, diagonal_dominance,\\nASV_value, ASV_classification (fragile/moderate/robust),\\nheld_out_bias, held_out_direction, concordance (✓/✗/trivial).\\n5 行标注 \\\"trivial\\\" (ASV>50)，4 行标注 ✓。\\n\"\n      },\n      {\n        \"name\": \"Table 14: ASV vs Raw Confusion Matrix — Interpretability Comparison\",\n        \"description\": \"对 4 个 meaningful cases，并排展示 ASV summary 和 raw confusion matrix，\\n说明 ASV 提供了哪些 confusion matrix 本身不直接给出的信息\\n（主要是 \\\"离 danger zone 有多远\\\" 的距离度量）。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4/9 concordance 在 [3,6] 范围的低端。论文叙事需要将这个结果 reframe：\\n不是 \\\"ASV 在 9 个场景中只有 4 个有用\\\"，而是 \\\"ASV 正确识别了 4 个值得关注的\\nhigh-risk combinations——这些是研究者在没有 ASV 的情况下可能忽略的\\\"。\\n对 5 个 vacuous cases，论文可以说 \\\"ASV 为这些 combinations 提供了 formal robustness\\nguarantee，研究者可以安心使用\\\"——但 reviewer 可能反驳 \\\"any reasonable researcher\\nwouldn't worry about a 85%-accurate annotator\\\"。\\n\\n增强策略：(a) semi-synthetic 注入——在经验 C 上添加 controlled degradation\\n（accuracy 从 0.8 降至 0.5），展示 ASV 如何从 \\\"robust\\\" 转变为 \\\"fragile\\\"，\\n(b) 增加低资源任务（如小语种情感分析 K=7），提高观察到 meaningful ASV 的概率，\\n(c) user study——给研究者展示 ASV vs 不展示 ASV，测量决策质量差异。\\n\\n\\n经验混淆矩阵 diagonal-dominant（plan_003 结果），因此达到 direction-reversing 或\\nmagnitude-significant 的 δ threshold 很高——ASV 值大（甚至无穷）。\\n5/9 combinations 的 ASV ≫10，意味着 \\\"需要当前 annotation error 放大 10 倍以上\\n才会产生有意义的 bias\\\"——technically correct 但 uninformative（研究者已经知道\\n高准确率 LLM 产生的 bias 小）。4/9 meaningful cases 出现在 K=5 protest event coding\\n（准确率最低，off-diagonal mass 最大）和 K=3 stance detection 与较弱模型的组合。\\n这些 meaningful cases 中 ASV 正确区分了 fragile（ASV<5）vs robust（ASV>10）——\\n但样本量太小（4 cases）无法做统计检验。\\n\\nWorst 档的核心困境在此体现：ASV 的理论价值依赖于经验 C 足够 \\\"interesting\\\"，\\n但 SOTA LLMs 太好了，经验 C 太 \\\"boring\\\"。\\n\"\n  },\n  {\n    \"name\": \"Correction guidance framework\",\n    \"description\": \"构建 {topology × error structure × ASV} → correction method 的决策框架，\\nMC 验证 recommended method 在 ≥90% scenarios 产生最小 bias，\\n经验数据验证。\\n\",\n    \"results\": {\n      \"overall_accuracy\": 0.78,\n      \"mla_recommendation_fraction\": 0.65,\n      \"exposure_reversal_recommendation\": \"gold label collection / no adequate correction\",\n      \"exposure_accuracy\": 0.85,\n      \"confounding_accuracy\": 0.82,\n      \"collider_accuracy\": 0.68,\n      \"scenarios_where_no_method_adequate\": 0.12,\n      \"ppi_outperforms_mla_fraction\": 0.08,\n      \"dsl_applicable_fraction\": 0.05,\n      \"naive_plugin_never_recommended\": true,\n      \"correction_framework_accuracy\": 0.78,\n      \"decision_tree_depth\": 4,\n      \"decision_tree_leaf_purity\": 0.73\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Correction Guidance Decision Framework\",\n        \"description\": \"Matrix format: rows = topologies (6), columns = error structure categories\\n(diagonal-dominant / moderate / near-permutation × differential / non-differential),\\ncells = recommended method + ASV threshold. 大量 cells 填入 \\\"MLA\\\"。\\nExposure 行的 near-permutation cells 标红 \\\"gold labels required\\\"。\\n\"\n      },\n      {\n        \"name\": \"Table 16: Framework Accuracy — MC Validation\",\n        \"description\": \"Per topology accuracy, per error-structure accuracy, confusion matrix of\\n{recommended method × actually-best method}. 最大 off-diagonal cluster:\\nMLA recommended but PPI actually marginally better (差异 <0.01 bias)。\\n\"\n      },\n      {\n        \"name\": \"Table 17: Open Problem Identification\",\n        \"description\": \"12% of scenarios 标记为 \\\"no existing method adequate\\\"。\\nColumns: scenario_description, why_inadequate, required_capability.\\n主要集中在 differential multi-class error + complex topology (M-bias, front-door)\\n和 correlated multi-LLM error。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Correction framework 在 worst 档下的 selling point 不是 accuracy 而是 completeness——\\n\\\"first systematic mapping of when each correction method applies, with identified open problems\\\"。\\n0.78 accuracy 加上 MLA 65% dominance 意味着 framework 的 practical value 集中在\\n~35% non-MLA scenarios（exposure reversal + PPI edge cases + no-method-adequate regimes）。\\nVersion B narrative 中 Claim 3 权重增加，需要将 framework 包装为 \\\"practitioner's guide\\\"\\n而非 \\\"automated decision system\\\"——降低 accuracy 期望，强调 \\\"the framework identifies\\nwhat you should worry about, not just what to do\\\"。\\nOpen problems 部分（12% no-method-adequate）可能是最有 citation value 的贡献——\\n明确指出 correlated multi-LLM error correction 是 unsolved problem，引导后续研究。\\n\\n\\nCorrection framework accuracy 0.78 反映了 worst 档的核心预测：framework 在多数场景\\n退化为 \\\"use MLA\\\"。当 65% 的 scenarios 的最优推荐是 MLA 时，一个 trivial baseline\\n\\\"always recommend MLA\\\" 就有 65% accuracy——framework 的 0.78 仅比 trivial baseline\\n高 13 个百分点，discriminative value 有限。\\n\\nMLA 主导的原因：MLA (Measurement-error Likelihood Adjustment) 是最 general 的方法，\\n它利用 C 矩阵估计对 likelihood 做调整，适用于任何 topology + 任何 error structure。\\n在 5 个 \\\"well-behaved\\\" topology（方向可预测）中，MLA 几乎总是最优选择因为它直接\\n纠正 bias magnitude。PPI 仅在 finite-sample regime（small gold sample + large LLM sample）\\n优于 MLA（8% scenarios）。DSL 仅在 very specific conditions（已知 C + linear model）下\\n优于 MLA（5% scenarios）。\\n\\nExposure topology 是 framework 最有价值的部分——对 reversal-risk scenarios，framework\\n正确推荐 \\\"no correction adequate without gold labels\\\"，这是 non-trivial guidance\\n（naive researcher 可能尝试 MLA 但 MLA 在 sign-reversed regime 可能 amplify error）。\\n\\nCollider accuracy 最低（0.68）因为 collider bias correction 依赖于 conditioning strategy——\\n\\\"correct the annotation then re-condition\\\" vs \\\"don't condition at all\\\" 的选择\\n取决于 effect magnitude 和 C structure 的交互，decision tree 难以准确捕获。\\n\"\n  },\n  {\n    \"name\": \"Pathological confusion matrix analysis (spectral)\",\n    \"description\": \"分析极端 C 结构（near-permutation, rank-deficient, block-diagonal）在 6 个拓扑下的\\nbias 行为，用 spectral 分析（eigenvalue spectrum of C）识别 bias severity 的\\nstructural predictors。\\n\",\n    \"results\": {\n      \"exposure_reversal_spectral_threshold\": \"λ₂/λ₁ > 0.6 for K=3\",\n      \"exposure_reversal_prediction_auc\": 0.92,\n      \"diagonal_dominance_as_simple_predictor\": \"reversal when diag_dom < 0.45\",\n      \"diagonal_dominance_prediction_auc\": 0.89,\n      \"other_topologies_spectral_finding\": \"monotone relationship between λ₁ and bias magnitude; no reversal threshold exists\",\n      \"spectral_gap_predicts_magnitude_R2\": 0.78,\n      \"block_diagonal_C_magnitude_effect\": \"1.5–2.3x bias amplification vs random C of same accuracy\",\n      \"rank_deficient_C_behavior\": \"bias expressions numerically unstable, need regularization\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: Spectral Predictors of Bias Severity\",\n        \"description\": \"Columns: predictor (λ₂/λ₁, diag_dom, spectral_gap, Frobenius_norm),\\ntarget (reversal_binary, bias_magnitude), topology, AUC_or_R².\\nExposure rows 有 reversal prediction AUC，其余行仅有 magnitude R²。\\n\"\n      },\n      {\n        \"name\": \"Table 19: Pathological C Structure Catalog\",\n        \"description\": \"Catalog of 4 pathological C types × 6 topologies × {bias_magnitude,\\ndirection_preserved, numerical_stability}。27 行 summary。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Spectral 分析在 worst 档下提供了 exposure 反转的 mechanistic explanation——\\n这是 narrative 需要的 \\\"deep dive\\\"。λ₂/λ₁ > 0.6 threshold 是一个 actionable\\npractitioner guideline（\\\"检查你的 confusion matrix 的 spectral gap，如果 < 0.4\\n则 exposure 标注安全\\\"）。对其余拓扑，spectral 分析的贡献更 modest——\\n确认了 \\\"方向可预测，magnitude 依赖 C\\\" 的结论但没有 surprising insight。\\nBlock-diagonal 发现是 bonus 内容——在 CSS 中，block-diagonal C 对应\\n\\\"模型区分粗粒度类别但混淆细粒度类别\\\" 的常见模式，有实际意义。\\n建议在论文中将 spectral 分析作为 Section 4 的 highlight（exposure deep dive），\\n其余拓扑的 spectral 结果放 appendix。\\n\\n\\nExposure DAG 的反转机制有清晰的 spectral interpretation：C 矩阵的 eigendecomposition\\n中，λ₁ 对应 \\\"correct classification\\\" mode（沿 identity 方向），λ₂ 对应 \\\"dominant confusion\\\"\\nmode（label swap 方向）。当 λ₂/λ₁ > 0.6 时，confusion mode 足够强以翻转 treatment\\nassignment 的有效方向，产生 sign reversal。这个阈值在 K=3 下给出 AUC 0.92 的\\nreversal 预测——spectral gap 是一个 principled predictor。\\nDiagonal dominance（diag_dom = min_i C_ii / max_i Σ_{j≠i} C_ij）是更简单的 proxy，\\nAUC 0.89 略低但更直观。\\n\\n对其余 5 个拓扑，spectral 分析揭示 λ₁ 与 bias magnitude 的 monotone relationship\\n（R²=0.78），但没有 \\\"reversal threshold\\\"——bias 方向由 topology 的结构性质决定\\n（confounding → toward OVB, mediation → toward attenuation, etc.），C 的 spectrum\\n只调制 magnitude。这在理论上不意外（worst 档假设），但提供了一个\\ncompact characterization。\\n\\nBlock-diagonal C（如 K=6 分成两个 K=3 block，block 间无混淆）产生 1.5-2.3x\\nbias amplification 因为 block 结构创造了 \\\"structured confusion\\\"——模型在 block 内\\n混淆但 block 间清晰，这比同等 accuracy 的 random C 产生更大 bias\\n因为 confusion 集中而非分散。\\n\\nRank-deficient C 导致某些 bias 表达式的矩阵求逆不稳定——这是实际计算中的\\nnuisance，不是理论 insight，但需要在 toolkit 中处理（regularization）。\\n\"\n  },\n  {\n    \"name\": \"annot-sensitivity Python toolkit\",\n    \"description\": \"Open-source Python 包：用户输入 DAG + confusion matrix + downstream estimate →\\n输出 bias expressions + ASV bounds + sensitivity curves + correction recommendation\\n+ diagnostic plots。pip-installable，每个 topology 一个 worked example。\\n\",\n    \"results\": {\n      \"pip_installable\": true,\n      \"supported_topologies\": 6,\n      \"K_range_supported\": \"2–15\",\n      \"runtime_K3\": \"<0.1s\",\n      \"runtime_K7\": \"<1s\",\n      \"runtime_K15\": \"<10s\",\n      \"worked_examples\": 6,\n      \"api_surface\": \"BiasExpr, ASV, CorrectionGuide, DiagnosticPlot\",\n      \"test_coverage\": \"~85%\",\n      \"documentation_pages\": \"~20\",\n      \"demo_value_assessment\": \"limited by diagonal-dominant empirical C\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Toolkit 在 worst 档下是 \\\"保底贡献\\\"——即使 taxonomy 不够 dramatic、ASV 有 coverage 问题、\\ncorrection framework 主要推荐 MLA，一个 well-documented open-source tool 仍有独立价值。\\n建议在论文中给 toolkit 一个 dedicated subsection（不只是 \\\"code available at github\\\"），\\n展示 API 设计和 worked examples。在 supplementary material 中包含\\ncomprehensive tutorial notebook。\\n\\nToolkit 是 engineering deliverable 而非实验。在 worst 档下，toolkit 本身功能完整\\n但 demonstration value 受限：经验混淆矩阵太 diagonal-dominant，toolkit 在 demo 中\\n主要输出 \\\"your annotation is fine\\\"——不够 compelling 作为 conference demo。\\nWorked examples 需要用 semi-synthetic C 而非 pure empirical C 来展示\\ntoolkit 的 full capability（包括 reversal detection, ASV fragility warning, etc.）。\\nRuntime 快（K≤7 < 1s）因为 bias expressions 是 closed-form matrix operations，\\n不需要 MC simulation。K=15 需要 ~10s 因为 15×15 矩阵的 eigendecomposition\\n和 worst-case optimization 增加计算量。\\n作为 Claim 3 (\\\"correction guidance\\\") 的 tangible artifact，toolkit 增加论文的\\npractical impact——即使理论贡献在 worst 档下被削弱，一个 pip-installable tool\\n是 reviewer 认可的 concrete contribution。\\n\"\n  }\n]",
      "numLines": 309,
      "startLine": 1,
      "totalLines": 309
    }
  },
  "sourceToolAssistantUUID": "1ed08bb2-5e03-4fe3-ace2-e6046627f830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T08:36:35.209Z_

<details><summary>↩ Tool result · `toolu_01KUvKcL5hw8ydUZAVoLg59a`</summary>

```text
1	# Paper Framing — causal_annot_error_attrib
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)
5	- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)
6	- Tertiary: ICWSM 2027 Round 2 (2026-09-15)
7	
8	## Title
9	Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies
10	
11	## Core Claims (3 条)
12	
13	1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).
14	
15	2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.
16	
17	3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.
18	
19	## Story Spine
20	
21	- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.
22	
23	- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.
24	
25	- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.
26	
27	- **Headline result template**: "Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias."
28	
29	## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001
30	
31	### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)
32	The binary guarantee that "non-differential exposure misclassification biases toward the null" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification ("bias can go in either direction"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to "escape" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).
33	
34	### Version B (no direction reversal found across topologies)
35	Multi-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.
36	
37	**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.
38	
39	## MVP Evidence
40	
41	**Confounding DAG + K=3** (confounder misclassification):
42	- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated
43	- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization
44	- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is "well-behaved" (predictable direction)
45	- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.
46	
47	**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):
48	- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification
49	- K=2 control: 6/6 toward null (binary guarantee holds)
50	- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)
51	- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)
52	- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim
53	
54	## Venue Fit Risks
55	
56	- **AAAI**: Broad AI audience — emphasize general methodology for "automated annotation measurement error," not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.
57	- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.
58	- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.
59	
60	## Anticipated Reviewer Concerns & Planned Responses
61	
62	1. **"Trivial extension of binary to multi-class"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]
63	
64	2. **"Lee & Wood-Doughty (2024) already did categorical"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]
65	
66	3. **"Why these 6 DAG topologies?"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]
67	
68	4. **"K≥5 expressions aren't actionable"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]
69	
70	5. **"ASV sharpness only proved for 3 topologies"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]
71	
72	6. **"Correlated multi-LLM errors?"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]
73	
74	7. **"Empirical validation scope"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50a6ac15-26de-424b-bb4a-73edf79e5cf6",
  "isSidechain": false,
  "promptId": "74990caf-6c19-4294-8631-731e236d5131",
  "type": "user",
  "uuid": "922c53da-0c71-427a-8af5-698eac6526c4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper_framing.md",
      "content": "# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias.\"\n\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\n\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\nThe binary guarantee that \"non-differential exposure misclassification biases toward the null\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\"bias can go in either direction\"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \"escape\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\n\n### Version B (no direction reversal found across topologies)\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\n\n**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.\n\n## MVP Evidence\n\n**Confounding DAG + K=3** (confounder misclassification):\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \"well-behaved\" (predictable direction)\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\n\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\n- K=2 control: 6/6 toward null (binary guarantee holds)\n- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 6 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]\n",
      "numLines": 75,
      "startLine": 1,
      "totalLines": 75
    }
  },
  "sourceToolAssistantUUID": "50a6ac15-26de-424b-bb4a-73edf79e5cf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attr…",
  "leafUuid": "3888ea26-74b2-4b2c-ba94-bdbed874aa4a",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for annotation error study",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Assistant

_source line 14 · 2026-05-20T08:36:40.150Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "922c53da-0c71-427a-8af5-698eac6526c4",
  "isSidechain": false,
  "requestId": "req_011CbDWtEPFBmpwLWJowV94R",
  "type": "assistant",
  "uuid": "50eb7249-95f0-49de-889e-32d74e39e89d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsnFH7BAVETzDtZ26t6Qhb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16734,
      "cache_read_input_tokens": 23885,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 23885,
          "cache_creation_input_tokens": 16734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16734
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

_source line 15 · 2026-05-20T08:36:41.110Z_

Now let me check the output directory and load the paper-writing skill for reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50eb7249-95f0-49de-889e-32d74e39e89d",
  "isSidechain": false,
  "requestId": "req_011CbDWtEPFBmpwLWJowV94R",
  "type": "assistant",
  "uuid": "a34415df-9d10-4256-8dc1-e08525f62922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsnFH7BAVETzDtZ26t6Qhb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16734,
      "cache_read_input_tokens": 23885,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 23885,
          "cache_creation_input_tokens": 16734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16734
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

_source line 16 · 2026-05-20T08:36:42.970Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CViKWiWC7Jq2UCdowWTL3J`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a34415df-9d10-4256-8dc1-e08525f62922",
  "isSidechain": false,
  "requestId": "req_011CbDWtEPFBmpwLWJowV94R",
  "type": "assistant",
  "uuid": "d2902fcb-db7a-46cd-96d1-6c359f151f1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsnFH7BAVETzDtZ26t6Qhb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16734,
      "cache_read_input_tokens": 23885,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 23885,
          "cache_creation_input_tokens": 16734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16734
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

_source line 17 · 2026-05-20T08:36:43.460Z_

<details><summary>↩ Tool result · `toolu_017t1oWvuDRkPsv3qLGGhSk7`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "4e19b08a-8691-46af-9895-dff9d5543ebc",
  "isSidechain": false,
  "promptId": "74990caf-6c19-4294-8631-731e236d5131",
  "type": "user",
  "uuid": "df0cc5a0-5965-44c9-90bd-cb8f1dbb2cb1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "4e19b08a-8691-46af-9895-dff9d5543ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 18 · 2026-05-20T08:36:43.142Z_

<details><summary>↩ Tool result · `toolu_01CViKWiWC7Jq2UCdowWTL3J`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2902fcb-db7a-46cd-96d1-6c359f151f1d",
  "isSidechain": false,
  "promptId": "74990caf-6c19-4294-8631-731e236d5131",
  "type": "user",
  "uuid": "18f9d955-5ae1-48e7-8495-da64df497481",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d2902fcb-db7a-46cd-96d1-6c359f151f1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T08:36:43.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_017t1oWvuDRkPsv3qLGGhSk7`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18f9d955-5ae1-48e7-8495-da64df497481",
  "isSidechain": false,
  "requestId": "req_011CbDWtEPFBmpwLWJowV94R",
  "type": "assistant",
  "uuid": "4e19b08a-8691-46af-9895-dff9d5543ebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsnFH7BAVETzDtZ26t6Qhb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16734,
      "cache_read_input_tokens": 23885,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 23885,
          "cache_creation_input_tokens": 16734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16734
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attr…",
  "leafUuid": "df0cc5a0-5965-44c9-90bd-cb8f1dbb2cb1",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for annotation error study",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Assistant

_source line 22 · 2026-05-20T08:37:13.178Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write a complete LaTeX paper based on:

1. The experiment data from `experiment_data.json` (8 experiments)
2. The paper framing from `paper_framing.md`
3. The narrative guidance (Version B framing, topology-dependent dichotomy)
4. The paper writing norms

The paper needs to cover all 8 experiments:
1. Six-topology bias taxonomy (K=3) - Tables 1, 2
2. General-K matrix expressions (K=5,7) - Tables 3, 4


3. Empirical confusion matrices across three LLMs and CSS tasks - Tables 5, 6, 7
4. Binarization collapse analysis - Table 8
5. ASV formal proofs examining confounding, mediation, and collider structures - Tables 9, 10
6. ASV Monte Carlo validation across M-bias, instrument, and front-door scenarios - Tables 11, 12
7. ASV empirical calibration results - Tables 13, 14
8. Correction guidance framework with implementation guidance - Tables 15, 16, 17
9. Pathological confusion matrix analysis using spectral methods - Tables 18, 19
10. The annot-sensitivity toolkit documentation

Now I'm organizing these eight experiments into a coherent paper structure with sections for the bias taxonomy, general-K extensions, binarization collapse, annotation sensitivity values, spectral analysis, and the correction guidance framework, followed by the empirical results section. I'm working through the paper structure and realizing I need to be selective about which tables to include given the 8-page EMNLP constraint—I'll feature the most critical ones and reference the rest rather than trying to fit all 19 tables into the draft. Writing the LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df0cc5a0-5965-44c9-90bd-cb8f1dbb2cb1",
  "isSidechain": false,
  "requestId": "req_011CbDWtqNvXKKx2nNKdrmse",
  "type": "assistant",
  "uuid": "263159b5-93a9-4c5b-84da-fc0f1f9c9378",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyqbFqbFXE8Duj11nj5Ydp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5794,
      "cache_read_input_tokens": 40619,
      "output_tokens": 13302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13302,
          "cache_read_input_tokens": 40619,
          "cache_creation_input_tokens": 5794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5794
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

_source line 23 · 2026-05-20T08:37:13.180Z_

Now I'll write the full paper. This is a substantial document covering all 8 experiments with the Version B framing (topology-dependent dichotomy).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "263159b5-93a9-4c5b-84da-fc0f1f9c9378",
  "isSidechain": false,
  "requestId": "req_011CbDWtqNvXKKx2nNKdrmse",
  "type": "assistant",
  "uuid": "d7c1fab6-b4dc-4738-a0ab-9136d808c554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyqbFqbFXE8Duj11nj5Ydp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5794,
      "cache_read_input_tokens": 40619,
      "output_tokens": 13302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13302,
          "cache_read_input_tokens": 40619,
          "cache_creation_input_tokens": 5794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5794
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

_source line 24 · 2026-05-20T08:41:08.476Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Y4smPM3ojPh9hYCpWvFzBA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{geometry}\n\\usepackage{natbib}\n\\usepackage{bm}\n\\usepackage{enumitem}\n\n\\geometry{margin=1in}\n\n\\newcommand{\\Cmat}{\\mathbf{C}}\n\\newcommand{\\bvec}{\\mathbf{b}}\n\\newcommand{\\R}{\\mathbb{R}}\n\n\\title{Multi-Class Annotation Errors Are Not Created Equal:\\\\\nBias Taxonomy, Sensitivity Analysis, and Correction Guidance\\\\for LLM-Annotated Causal Studies}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nLarge Language Models (LLMs) are rapidly replacing human annotators in computational social science (CSS), yet recent evidence shows that 31\\% of downstream causal conclusions may already be incorrect due to annotation errors.\nExisting measurement error frameworks assume binary variables, leaving researchers without diagnostic tools for multi-class ($K \\geq 3$) annotation.\nWe present the first systematic characterization of how $K \\times K$ confusion matrix structures interact with causal DAG topologies to produce downstream bias.\nOur bias taxonomy covers six canonical DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door) with closed-form expressions for $K=3$ and matrix-form expressions with eigendecomposition-based interpretability tools for general $K$.\nA key finding is a sharp topology-dependent dichotomy: exposure misclassification is the only topology where non-differential multi-class error produces direction-unpredictable bias (85\\% reversal rate in 100K random confusion matrices), while the remaining five topologies preserve bias direction but exhibit magnitude variation that requires the full $K \\times K$ matrix to quantify.\nWe introduce Annotation Sensitivity Values (ASVs), analogous to E-values for unmeasured confounding, that quantify the minimum annotation error amplification needed to overturn a conclusion.\nWe validate our framework on three CSS tasks annotated by three LLMs ($\\sim$270K annotations), and provide an open-source Python toolkit and a correction guidance decision framework.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nAnnotation by Large Language Models has become the de facto approach for large-scale coding in computational social science.\nProtest event classification, stance detection, and toxicity labeling are routinely performed by LLMs at a fraction of the cost of human annotation.\nYet a growing body of evidence reveals that LLM annotation errors propagate into downstream causal analyses in ways that researchers cannot currently anticipate or diagnose \\citep{baumann2025}.\n\nThe core problem is structural.\nClassical measurement error theory provides reassuring guarantees for binary variables: non-differential misclassification of a binary exposure biases effect estimates toward the null \\citep{bross1954}.\nResearchers routinely invoke this guarantee to argue that their LLM-annotated results are ``conservative.''\nHowever, CSS variables are frequently multi-class: protest event types ($K=5$), stance categories ($K=3$), and emotion labels ($K=7$) are standard.\n\\citet{brenner1993} showed decades ago that polytomous misclassification can bias in either direction, but no systematic framework exists that characterizes when, why, and by how much this occurs across different causal designs.\n\nThe gap matters because different causal designs interact differently with annotation error.\nA confounder mislabeled as category B instead of category A produces residual confounding; an exposure mislabeled the same way produces a fundamentally different distortion by swapping treatment assignments.\nWithout a framework that accounts for both the confusion matrix structure and the DAG topology, researchers cannot determine whether their specific combination is safe or hazardous.\nRecent work by \\citet{kim2025} compounds the urgency: cross-model annotation errors are highly correlated (60\\% agreement when both LLMs err), meaning multi-annotator ensembles cannot escape systematic bias.\n\nWe address this gap with three contributions:\n\n\\begin{enumerate}[leftmargin=*, itemsep=2pt]\n\\item \\textbf{Multi-class bias taxonomy.}\nClosed-form bias expressions for $K=3$ and matrix-form expressions with eigendecomposition-based interpretability tools for general $K$, across six canonical DAG topologies.\nOur taxonomy reveals a topology-dependent dichotomy: exposure misclassification is uniquely dangerous (85\\% direction reversal rate), while the remaining five topologies are directionally predictable but magnitude-variable.\nTheory matches Monte Carlo (MC) simulation in 32/42 topology-structure combinations (76\\%), with mismatches concentrated in complex topologies (collider, M-bias, front-door) where closed-form approximations require higher-order terms (Section~\\ref{sec:taxonomy}, Tables~\\ref{tab:taxonomy-summary} and~\\ref{tab:theory-mc}).\n\n\\item \\textbf{Annotation Sensitivity Values (ASVs).}\nA sensitivity analysis framework, analogous to E-values for unmeasured confounding, that quantifies the minimum annotation error amplification $\\delta$ needed to overturn a downstream conclusion.\nWe prove monotonicity and sharpness for the confounding topology, monotonicity for mediation and instrument topologies, and identify specific failure conditions for collider (7\\% non-monotone scenarios) and front-door (3\\%) topologies.\nAggregate MC coverage at 95\\% nominal level is 85\\% across all six topologies (Section~\\ref{sec:asv}, Tables~\\ref{tab:asv-proof} and~\\ref{tab:asv-remaining}).\n\n\\item \\textbf{Correction guidance framework and toolkit.}\nA decision framework mapping \\{topology $\\times$ error structure $\\times$ ASV\\} to appropriate correction methods, with 78\\% accuracy validated by MC simulation.\nThe framework identifies 12\\% of scenarios where no existing correction method is adequate, including correlated multi-LLM error as an open problem.\nWe release \\texttt{annot-sensitivity}, a pip-installable Python toolkit supporting $K=2$--$15$ across all six topologies (Section~\\ref{sec:correction}, Table~\\ref{tab:correction-framework}).\n\\end{enumerate}\n\nWe validate the full framework on three CSS tasks (protest event coding $K=5$, stance detection $K=3$, toxicity $K=2$) annotated by Llama 4 Maverick, Qwen 3.5 Plus, and DeepSeek V4, totaling $\\sim$270K annotations.\nASVs correctly classify all four non-trivial robustness cases (Section~\\ref{sec:empirical}).\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Measurement error in causal inference.}\nThe study of misclassification bias dates to \\citet{bross1954}, who established that non-differential binary exposure error biases toward the null.\n\\citet{brenner1993} extended this to polytomous variables, proving that multi-class misclassification can bias in either direction.\n\\citet{vanderweele2019} developed sensitivity bounds (E-values) for unmeasured confounding with binary risk ratios, providing a conceptual template for our ASV framework.\nHowever, none of these works provide a systematic taxonomy across DAG topologies or tools for general $K$.\n\n\\paragraph{Annotation error in NLP and CSS.}\n\\citet{wood-doughty2018} applied DAG reasoning to text classifier errors but restricted analysis to binary variables without formal bias theorems.\n\\citet{teblunthuis2024} provided the most complete binary treatment with Measurement-error Likelihood Adjustment (MLA) correction, but their framework is limited to $K=2$ and single classifiers.\n\\citet{lee2024} extended to categorical variables and LLM classifiers, covering unobserved confounding on a single dataset (MIMIC).\nOur work covers six topologies with a systematic taxonomy, sensitivity analysis, and correction guidance.\n\n\\paragraph{LLM annotation quality.}\n\\citet{jerzak2025} benchmarked correction methods for LLM annotation but treated error as monolithic, without conditioning on confusion matrix structure or DAG topology.\n\\citet{kim2025} documented that cross-model LLM errors are highly correlated, a finding that strengthens the case for error-structure-aware analysis rather than ensemble approaches.\n\\citet{baumann2025} quantified that 31\\% of downstream CSS conclusions are incorrect when using LLM annotations, motivating diagnostic tools rather than better annotators.\n\n%% ============================================================\n%% 3. BIAS TAXONOMY\n%% ============================================================\n\\section{Multi-Class Bias Taxonomy}\\label{sec:taxonomy}\n\n\\subsection{Setup and Notation}\n\nConsider a variable $V$ with $K$ categories, annotated by an LLM with confusion matrix $\\Cmat \\in \\R^{K \\times K}$ where $C_{jk} = P(\\hat{V}=k \\mid V=j)$.\nThe variable $V$ occupies a specific role in a causal DAG $\\mathcal{G}$: confounder, exposure, mediator, collider, instrument, or front-door criterion variable.\nLet $\\beta$ denote the true causal effect and $\\hat{\\beta}(\\Cmat)$ the estimate obtained when $V$ is replaced by its LLM annotation $\\hat{V}$.\nThe bias is $B(\\Cmat, \\mathcal{G}) = \\hat{\\beta}(\\Cmat) - \\beta$.\n\nFor $K=3$, we derive closed-form expressions $B(\\Cmat, \\mathcal{G})$ for each of the six topologies.\nFor general $K$, the bias takes a matrix form $\\bvec(\\Cmat, \\mathcal{G}) = \\mathbf{M}(\\Cmat, \\mathcal{G})\\bm{\\theta}$ where $\\mathbf{M}$ depends on the Kronecker product of $\\Cmat$ with structural parameters from $\\mathcal{G}$, and $\\bm{\\theta}$ collects the true causal parameters.\n\n\\subsection{Closed-Form Results ($K=3$, Six Topologies)}\\label{sec:closed-form}\n\nWe evaluate each bias expression against MC simulation with 1000 replications ($N=10{,}000$) across six named confusion matrix structures: identity-adjacent, uniform-leaning, near-permutation, block-diagonal, asymmetric, and random-moderate.\nWe also run a random search over 100K confusion matrices per topology.\n\n\\begin{table}[t]\n\\centering\n\\caption{Six-topology bias taxonomy summary ($K=3$). Reversal rate from 100K random confusion matrices. Theory-MC match counts structures (of 6) where theoretical bias falls within 95\\% MC confidence interval.}\n\\label{tab:taxonomy-summary}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nTopology & Reversal & Theory-MC & Bias Range & Direction Class \\\\\n\\midrule\nConfounding & 0.0\\% & 6/6 & 0.063--0.298 & Monotone toward OVB \\\\\nExposure & 85.0\\% & 5/6 & $-$0.84--0.42 & \\textbf{Unpredictable} \\\\\nMediation & 0.0\\% & 5/6 & 0.00--0.15 & Monotone attenuation \\\\\nCollider & 0.0\\% & 4/6 & 0.02--0.18 & Monotone (conditioning) \\\\\nM-bias & 0.0\\% & 4/6 & 0.04--0.22 & Monotone (dual path) \\\\\nInstrument & 0.0\\% & 5/6 & 0.03--0.25 & Monotone attenuation \\\\\nFront-door & 0.0\\% & 3/6 & 0.01--0.19 & Monotone (compound) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:taxonomy-summary} reveals a sharp dichotomy.\nExposure misclassification is the only topology where non-differential $K=3$ error produces direction reversal, with 85\\% of random confusion matrices violating the binary bias-toward-null guarantee.\nAmong these violations, 83.4\\% are sign reversals and 14.1\\% are amplifications beyond the true effect magnitude.\nThe worst case reaches $\\hat{\\beta} = -0.84$ for a true $\\beta = 1.0$ (sign reversal with 2.83$\\times$ amplification).\n\nThe mechanism is specific to exposure: when the exposure variable is misclassified, near-permutation $\\Cmat$ structures swap treatment labels across categories.\nA subject truly in treatment group A is coded as group B, and the outcome attributed to the wrong treatment.\nThis label-swap mechanism is structurally impossible in binary ($K=2$) non-differential misclassification, where the only effect is attenuation.\n\nFor the remaining five topologies, the annotated variable (confounder, mediator, etc.) does not define the treatment contrast.\nIts misclassification modulates bias magnitude but cannot flip the numerator/denominator of the estimand.\nConfounding produces the largest magnitude range (0.063--0.298) among the well-behaved topologies, while mediation produces the smallest (0.00--0.15).\n\n\\begin{table}[t]\n\\centering\n\\caption{Theory vs MC match detail. Each row is one topology-structure combination. Match = theoretical bias within 95\\% MC CI. 10 mismatches concentrate in complex topologies with extreme $\\Cmat$ structures.}\n\\label{tab:theory-mc}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTopology group & Matches / Total & Mismatch locations \\\\\n\\midrule\nConfounding & 6/6 & (none) \\\\\nExposure & 5/6 & Near-permutation \\\\\nMediation & 5/6 & Block-diagonal \\\\\nCollider & 4/6 & Near-perm., asymmetric \\\\\nM-bias & 4/6 & Block-diag., asymmetric \\\\\nInstrument & 5/6 & Near-permutation \\\\\nFront-door & 3/6 & Near-perm., asym., block-diag. \\\\\n\\midrule\n\\textbf{Total} & \\textbf{32/42 (76\\%)} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overall theory-MC match rate is 76\\% (Table~\\ref{tab:theory-mc}).\nAll 10 mismatches occur with extreme confusion matrix structures (near-permutation, block-diagonal, asymmetric) in topologies with complex conditioning or compound estimation steps.\nFront-door has the lowest match rate (3/6) because the front-door criterion involves two mediation steps whose approximation errors compound.\nWe treat front-door expressions as MC-validated conjectures rather than exact theorems.\n\n\\subsection{General-$K$ Extensions ($K=5,7$)}\\label{sec:general-k}\n\nFor $K > 3$, we express bias in matrix form and develop three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, and (c) diagnostic visualizations.\nWe validate on confounding, mediation, and collider topologies.\n\n\\begin{table}[t]\n\\centering\n\\caption{Eigendecomposition summary across $K$ and topologies. $\\lambda_1/\\text{tr}(\\Lambda)$ = fraction of bias variance captured by the dominant eigenvalue. Modes for 90\\% = number of eigenvalues needed for 90\\% cumulative variance. Bound ratio = worst-case bound / MC observed maximum.}\n\\label{tab:eigen}\n\\small\n\\begin{tabular}{clcccc}\n\\toprule\n$K$ & Topology & $\\lambda_1/\\text{tr}(\\Lambda)$ & Modes (90\\%) & Bound ratio \\\\\n\\midrule\n3 & Confounding & --- & 1 & 1.3$\\times$ \\\\\n3 & Mediation & --- & 1 & 1.3$\\times$ \\\\\n3 & Collider & --- & 2 & 1.4$\\times$ \\\\\n\\midrule\n5 & Confounding & 0.82 & 1 & 1.8$\\times$ \\\\\n5 & Mediation & 0.75 & 2 & 2.0$\\times$ \\\\\n5 & Collider & 0.58 & 3 & 2.5$\\times$ \\\\\n\\midrule\n7 & Confounding & 0.76 & 2 & 2.5$\\times$ \\\\\n7 & Mediation & 0.68 & 2 & 2.8$\\times$ \\\\\n7 & Collider & 0.49 & 4 & 3.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:eigen} shows that eigendecomposition is an effective summary for confounding (dominant eigenvalue captures $\\geq$76\\% variance through $K=7$) but degrades for collider ($\\lambda_1/\\text{tr}(\\Lambda) = 0.49$ at $K=7$, requiring 4 modes for 90\\% variance).\nThe theory-MC match rate decreases from 70\\% at $K=5$ to 63\\% at $K=7$, partly because per-cell sample sizes become insufficient at higher $K$ ($7 \\times 7 = 49$ cells with $N=10{,}000$).\n\nWorst-case scalar bounds grow increasingly conservative with $K$ (1.8--2.5$\\times$ at $K=5$; 2.5--3.2$\\times$ at $K=7$).\nThe bound optimizes over an adversarial $\\Cmat$ whose supremum is not achievable in practice because the feasible region of confusion matrices is a low-dimensional manifold in high-dimensional space.\nFor collider and M-bias topologies at $K \\geq 5$, we recommend pairing worst-case bounds with diagnostic visualizations rather than relying on eigendecomposition alone.\n\n\\subsection{Binarization Collapse ($K \\to 2$)}\\label{sec:binarization}\n\nIf multi-class bias analysis is complex, can researchers collapse $K$-class variables to binary and apply established binary theory?\nWe compare full multi-class bias expressions with their binarized counterparts across all six topologies and $K = 3, 5, 7$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Binarization delta: the maximum absolute difference between multi-class and binarized bias expressions. Confounding consistently shows the largest delta.}\n\\label{tab:binarization}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTopology & $K=3$ & $K=5$ & $K=7$ \\\\\n\\midrule\nConfounding & 0.078 & 0.085 & \\textbf{0.091} \\\\\nExposure & 0.072 & --- & --- \\\\\nMediation & 0.041 & --- & --- \\\\\nCollider & 0.068 & --- & --- \\\\\nM-bias & 0.055 & --- & --- \\\\\nInstrument & 0.038 & --- & --- \\\\\nFront-door & 0.045 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:binarization} shows that binarization introduces a maximum absolute bias discrepancy of 0.091 (confounding, $K=7$).\nFour of six topologies exceed $\\Delta = 0.05$, and two exceed 0.08.\nBinarization does not reverse bias direction in any tested case; its effect is purely on magnitude estimation.\nIn context, a $\\Delta$ of 0.09 represents 30--70\\% of the full multi-class bias across confounding scenarios, indicating that binarization is not a safe shortcut for magnitude estimation.\nThe discrepancy is largest for confounding because residual confounding is most sensitive to collapsing fine-grained categories into coarse binary groups.\n\n%% ============================================================\n%% 4. ANNOTATION SENSITIVITY VALUES\n%% ============================================================\n\\section{Annotation Sensitivity Values}\\label{sec:asv}\n\n\\subsection{Definition}\n\nGiven a reference confusion matrix $\\Cmat_0$ (e.g., from a validation set), we define a family of perturbed matrices $\\Cmat(\\delta) = (1 - \\delta)\\Cmat_0 + \\delta \\Cmat_{\\text{worst}}$ for $\\delta \\in [0,1]$, where $\\Cmat_{\\text{worst}}$ is the worst-case matrix within a topology-specific constraint set.\nThe Annotation Sensitivity Value (ASV) for a conclusion $H$ is:\n\\begin{equation}\n\\text{ASV}(H, \\Cmat_0, \\mathcal{G}) = \\inf\\{\\delta > 0 : H \\text{ is overturned under } \\Cmat(\\delta) \\text{ in topology } \\mathcal{G}\\}.\n\\end{equation}\nLarger ASV values indicate greater robustness: a conclusion with $\\text{ASV} = 5$ requires annotation error five times worse than the reference to be overturned.\nASVs are reported alongside effect estimates, analogous to how E-values are reported for unmeasured confounding.\n\nWe study two formal properties:\n\\textit{Monotonicity}: $|B(\\Cmat(\\delta), \\mathcal{G})|$ is non-decreasing in $\\delta$ (bias grows with error amplification).\n\\textit{Sharpness}: the ASV bound is achievable (there exists a $\\Cmat$ that attains the bound).\n\n\\subsection{Formal Results: Confounding, Mediation, Collider}\\label{sec:asv-formal}\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV proof status and MC validation for three priority topologies. Coverage = fraction of scenarios where ASV-implied confidence set contains the true bias, at nominal 90/95/99\\% levels.}\n\\label{tab:asv-proof}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTopology & Monotone & Sharp & Cov.\\ 90 & Cov.\\ 95 & Cov.\\ 99 \\\\\n\\midrule\nConfounding & \\checkmark (formal) & \\checkmark (formal) & 0.88 & 0.93 & 0.97 \\\\\nMediation & \\checkmark (formal) & $\\times$ (1.4--1.8$\\times$) & 0.86 & 0.91 & 0.96 \\\\\nCollider & $\\times$ (7\\% viol.) & N/A & 0.74 & 0.78 & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv-proof} summarizes the proof status.\nConfounding achieves both formal monotonicity and sharpness: residual confounding is a monotone function of annotation error amplification, and near-permutation confusion matrices achieve the worst-case bound.\n\nMediation achieves formal monotonicity (indirect effect attenuation is monotone in mediator misclassification) but not sharpness.\nThe ASV bound is conservative by a factor of 1.4--1.8$\\times$ because the mediation bias maximum is structurally bounded by the direct effect magnitude; the worst-case $\\Cmat$ optimization includes structurally unreachable configurations.\n\nCollider ASV fails monotonicity in 7\\% of tested confusion matrix structures, specifically when off-diagonal mass is concentrated in two adjacent cells and $\\delta \\in [0.3, 0.5]$.\nThe mechanism is that moderate misclassification partially opens the collider path while preserving conditioning structure, but larger misclassification destroys the conditioning precision, diluting the collider association.\nThis produces non-monotone bias as a function of $\\delta$.\nWe recommend reporting collider ASVs with a caveat and using the 99\\% coverage level ($0.85$) as a conservative choice.\n\n\\subsection{MC Validation: M-Bias, Instrument, Front-Door}\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV validation for the remaining three topologies (MC-validated conjectures). Front-door shows 3\\% monotonicity violations at extreme $\\Cmat$.}\n\\label{tab:asv-remaining}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & Monotone & Sharp & Tightness & Cov.\\ 95 \\\\\n\\midrule\nM-bias & \\checkmark (0/1000) & $\\times$ (1.6--2.1$\\times$) & Conserv. & 0.86 \\\\\nInstrument & \\checkmark (0/1000) & Near (1.1$\\times$) & Tight & 0.88 \\\\\nFront-door & Partial (3\\% viol.) & $\\times$ (1.8--2.4$\\times$) & Conserv. & 0.76 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv-remaining} reports MC-validated results for the remaining topologies.\nFive of six topologies show monotonicity (collider 7\\% violations, front-door 3\\%).\nOnly confounding achieves formal sharpness; instrument is near-sharp (within 1.1$\\times$).\nAggregate 95\\% coverage across all six topologies is 0.85; excluding front-door (0.76), the remaining five average 0.87.\n\nThe front-door violations arise from a different mechanism than collider: the front-door criterion involves two estimation steps (exposure $\\to$ mediator and mediator $\\to$ outcome adjusting for exposure), and near-rank-deficient confusion matrices can destabilize the second step, producing local non-monotonicity.\n\n\\subsection{Spectral Analysis of Pathological Confusion Matrices}\\label{sec:spectral}\n\nTo characterize when bias becomes severe, we analyze pathological confusion matrix structures (near-permutation, rank-deficient, block-diagonal) using spectral properties.\n\n\\begin{table}[t]\n\\centering\n\\caption{Spectral predictors of bias severity. For exposure, the target is reversal (binary); for other topologies, the target is bias magnitude.}\n\\label{tab:spectral}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nTopology & Predictor & Target & AUC / $R^2$ \\\\\n\\midrule\nExposure & $\\lambda_2/\\lambda_1 > 0.6$ & Reversal & AUC = 0.92 \\\\\nExposure & Diag.\\ dom.\\ $< 0.45$ & Reversal & AUC = 0.89 \\\\\nOthers (5) & $\\lambda_1$ & Magnitude & $R^2$ = 0.78 \\\\\nOthers (5) & Spectral gap & Magnitude & $R^2$ = 0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe spectral ratio $\\lambda_2/\\lambda_1$ of the confusion matrix provides a principled predictor of exposure bias reversal (Table~\\ref{tab:spectral}).\nWhen $\\lambda_2/\\lambda_1 > 0.6$ (i.e., the ``dominant confusion'' eigenmode is at least 60\\% as strong as the ``correct classification'' eigenmode), treatment label swaps become sufficient to reverse effect direction, yielding AUC = 0.92 for reversal prediction.\nDiagonal dominance (the simpler proxy $\\min_i C_{ii} / \\max_i \\sum_{j \\neq i} C_{ij}$) achieves AUC = 0.89 with a threshold of 0.45.\n\nFor the five well-behaved topologies, $\\lambda_1$ and spectral gap predict bias magnitude with $R^2 = 0.78$, but no reversal threshold exists because bias direction is determined by topology rather than by the confusion matrix spectrum.\n\nBlock-diagonal confusion matrices (corresponding to models that distinguish coarse categories but confuse fine-grained subcategories) produce 1.5--2.3$\\times$ bias amplification relative to random confusion matrices of the same accuracy, because structured confusion concentrates error rather than dispersing it.\nRank-deficient confusion matrices cause numerical instability in bias expressions that require matrix inversion; our toolkit applies Tikhonov regularization in these cases.\n\n%% ============================================================\n%% 5. EMPIRICAL VALIDATION\n%% ============================================================\n\\section{Empirical Validation}\\label{sec:empirical}\n\n\\subsection{LLM Annotation Experiments}\n\nWe collect annotations from Llama 4 Maverick, Qwen 3.5 Plus, and DeepSeek V4 on three CSS tasks: protest event coding ($K=5$), stance detection ($K=3$), and toxicity classification ($K=2$), totaling $\\sim$270K annotations (30K items $\\times$ 3 models $\\times$ 3 tasks).\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrix statistics. Diagonal dominance = sum of diagonal / sum of all entries.}\n\\label{tab:empirical-cm}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nTask ($K$) & Metric & Range (3 LLMs) \\\\\n\\midrule\nProtest ($K\\!=\\!5$) & Accuracy & 0.68--0.73 \\\\\n& Diag.\\ dominance & 0.74--0.80 \\\\\n\\midrule\nStance ($K\\!=\\!3$) & Accuracy & 0.76--0.81 \\\\\n& Diag.\\ dominance & 0.82--0.87 \\\\\n\\midrule\nToxicity ($K\\!=\\!2$) & Accuracy & 0.83--0.88 \\\\\n& Diag.\\ dominance & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Inter-model error correlation (pairwise Cohen's $\\kappa$ on error cells). High agreement confirms correlated errors across LLMs.}\n\\label{tab:inter-model}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nModel pair & $\\kappa$ (error agreement) \\\\\n\\midrule\nLlama--Qwen & 0.58--0.67 \\\\\nLlama--DeepSeek & 0.58--0.67 \\\\\nQwen--DeepSeek & 0.58--0.67 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:empirical-cm} shows that all empirical confusion matrices are diagonal-dominant (diagonal dominance 0.74--0.87), with no near-permutation structures observed.\nProtest event coding ($K=5$) has the lowest accuracy and most dispersed off-diagonal mass; toxicity ($K=2$) is most diagonal-dominant.\nInter-model error correlation (Table~\\ref{tab:inter-model}) shows pairwise $\\kappa$ of 0.58--0.67, consistent with the 60\\% cross-model error agreement reported by \\citet{kim2025} and driven by shared pre-training data distributions that cause similar errors on the same ``hard'' instances.\n\n\\subsection{Downstream Regression Bias}\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream bias vs gold standard for representative task-model-topology combinations. Bias $> 0.05$ is bolded.}\n\\label{tab:downstream-bias}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nTask & Model & $|\\text{Bias}|$ & Reversal? & Theory match \\\\\n\\midrule\nProtest & Qwen 3.5 Plus & \\textbf{0.12} & No & \\checkmark \\\\\nProtest & Llama 4 & \\textbf{0.08} & No & \\checkmark \\\\\nProtest & DeepSeek V4 & \\textbf{0.06} & No & \\checkmark \\\\\nStance & Qwen 3.5 Plus & 0.04 & No & \\checkmark \\\\\nStance & Llama 4 & 0.03 & No & \\checkmark \\\\\nStance & DeepSeek V4 & 0.02 & No & \\checkmark \\\\\nToxicity & All & $<$0.02 & No & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:downstream-bias} reports downstream regression bias against gold-standard labels.\nTwo to three of nine combinations exceed $|\\text{Bias}| > 0.05$, concentrated in protest event coding with weaker models.\nNo direction reversal is observed, consistent with our taxonomy: empirical confusion matrices are far from the near-permutation threshold ($\\lambda_2/\\lambda_1 > 0.6$) required for exposure reversal.\nThe maximum observed bias is 0.12 (Qwen 3.5 Plus on protest events), which is practically meaningful given that CSS effect sizes typically range from 0.1 to 0.3.\n\n\\subsection{ASV Calibration}\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV values for nine task-model combinations. ASV $> 50$ indicates trivially robust (annotation error would need $> 50\\times$ amplification to overturn the conclusion).}\n\\label{tab:asv-empirical}\n\\small\n\\begin{tabular}{llccl}\n\\toprule\nTask & Model & ASV & Classification & Note \\\\\n\\midrule\nProtest & Qwen 3.5 Plus & 2.3 & Fragile & Meaningful \\\\\nProtest & Llama 4 & 4.1 & Moderate & Meaningful \\\\\nProtest & DeepSeek V4 & 8.5 & Moderate & Meaningful \\\\\nStance & DeepSeek V4 & 18.7 & Robust & Meaningful \\\\\nStance & Llama 4 & $>$50 & Robust & Trivial \\\\\nStance & Qwen 3.5 Plus & $>$50 & Robust & Trivial \\\\\nToxicity & Llama 4 & $>$50 & Robust & Trivial \\\\\nToxicity & Qwen 3.5 Plus & $>$50 & Robust & Trivial \\\\\nToxicity & DeepSeek V4 & $>$50 & Robust & Trivial \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv-empirical} shows ASV values across all nine task-model combinations.\nFive of nine produce trivially large ASVs ($>$50), reflecting the diagonal-dominant confusion matrices.\nThe four meaningful cases correctly classify robustness: protest/Qwen ($\\text{ASV} = 2.3$, fragile) exhibits the largest downstream bias (0.12), while protest/DeepSeek ($\\text{ASV} = 8.5$, moderate) has smaller bias (0.06).\nAll four meaningful ASVs correctly distinguish fragile from robust combinations, achieving perfect concordance on non-trivial cases.\n\nThe prevalence of trivially robust cases is a feature, not a bug: for five of nine combinations, ASV provides a formal guarantee that annotation error cannot meaningfully distort conclusions at current LLM quality levels.\nFor the four flagged combinations, ASV identifies where researchers should invest in validation or correction.\n\n%% ============================================================\n%% 6. CORRECTION GUIDANCE\n%% ============================================================\n\\section{Correction Guidance Framework}\\label{sec:correction}\n\nWe construct a decision framework mapping \\{topology $\\times$ error structure $\\times$ ASV\\} to correction methods: Measurement-error Likelihood Adjustment (MLA), Prediction-Powered Inference (PPI), Design-based Sensitivity Limits (DSL), or ``gold label collection required.''\n\n\\begin{table}[t]\n\\centering\n\\caption{Correction framework accuracy by topology (MC validation). MLA = Measurement-error Likelihood Adjustment, PPI = Prediction-Powered Inference, DSL = Design-based Sensitivity Limits.}\n\\label{tab:correction-framework}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTopology & Accuracy & MLA fraction & No method \\\\\n\\midrule\nConfounding & 0.82 & 0.60 & 0.08 \\\\\nExposure & 0.85 & 0.15 & 0.35 \\\\\nMediation & 0.80 & 0.72 & 0.05 \\\\\nCollider & 0.68 & 0.55 & 0.15 \\\\\nM-bias & 0.76 & 0.68 & 0.10 \\\\\nInstrument & 0.81 & 0.70 & 0.08 \\\\\nFront-door & 0.74 & 0.65 & 0.12 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{0.78} & \\textbf{0.65} & \\textbf{0.12} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe framework achieves 78\\% accuracy overall (Table~\\ref{tab:correction-framework}), compared to a trivial baseline of 65\\% (``always recommend MLA'').\nMLA dominates recommendations in five well-behaved topologies because it is the most general method, adjusting the likelihood using the estimated confusion matrix.\nThe 13-percentage-point improvement over the trivial baseline concentrates in three areas:\n\n\\textit{Exposure reversal regime.}\nFor exposure topology with near-permutation confusion matrices, the framework correctly recommends gold label collection (35\\% of exposure scenarios have no adequate correction).\nMLA can amplify error in the sign-reversed regime; the framework identifies these cases.\n\n\\textit{PPI edge cases.}\nPPI outperforms MLA in 8\\% of scenarios, specifically in finite-sample regimes where a small gold-standard sample combined with a large LLM-annotated sample favors PPI's semi-supervised approach.\n\n\\textit{Open problems.}\nThe framework identifies 12\\% of scenarios where no existing method is adequate, concentrated in differential multi-class error with complex topologies and correlated multi-LLM error.\nDependence-aware multi-annotator correction is flagged as an open problem.\n\nCollider accuracy is lowest (0.68) because the choice between ``correct annotation then re-condition'' and ``avoid conditioning'' depends on the interaction between effect magnitude and confusion matrix structure, which a depth-4 decision tree captures imperfectly.\n\n%% ============================================================\n%% 7. THE ANNOT-SENSITIVITY TOOLKIT\n%% ============================================================\n\\section{The \\texttt{annot-sensitivity} Toolkit}\\label{sec:toolkit}\n\nWe release an open-source Python package (pip-installable) with four core modules:\n\\texttt{BiasExpr} (bias expressions for six topologies, $K=2$--15),\n\\texttt{ASV} (annotation sensitivity values with coverage calibration),\n\\texttt{CorrectionGuide} (decision framework lookup), and\n\\texttt{DiagnosticPlot} (spectral analysis and sensitivity curve visualization).\n\nRuntime is $<$0.1s for $K=3$, $<$1s for $K=7$, and $<$10s for $K=15$, because all bias expressions are closed-form matrix operations (no MC simulation required at inference time).\nThe package includes six worked examples (one per topology) and $\\sim$20 pages of documentation.\nTest coverage is approximately 85\\%.\n\nA typical workflow: the user provides a DAG specification, an estimated confusion matrix (from a validation set), and a downstream effect estimate.\nThe toolkit returns the predicted bias, an ASV value with interpretation, a sensitivity curve, and a correction recommendation.\n\n%% ============================================================\n%% 8. DISCUSSION & LIMITATIONS\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{The topology-dependent dichotomy.}\nOur central finding is that multi-class annotation error produces a sharp split between exposure misclassification (direction-unpredictable, requiring gold labels or spectral monitoring) and the remaining five topologies (direction-predictable, correctable with MLA).\nThis dichotomy has immediate practical implications for CSS researchers: the role of the annotated variable in the causal DAG, not just its accuracy, determines the risk profile.\nExposure is the most commonly LLM-annotated variable in CSS causal studies, making this finding especially relevant.\n\n\\paragraph{Theory-MC gap.}\nOur closed-form expressions match MC in 76\\% of topology-structure combinations.\nThe 24\\% mismatch concentrates in complex topologies with extreme confusion matrices, where first-order approximations are insufficient.\nWe view the MC validation itself as a necessary complement to the theoretical contribution: in the presence of approximation, validated numerical results are more trustworthy than unvalidated closed forms.\n\n\\paragraph{Diagonal-dominant empirical confusion matrices.}\nCurrent SOTA LLMs produce diagonal-dominant confusion matrices on well-studied CSS tasks, limiting the empirical demonstration of extreme-bias scenarios.\nThis is a limitation of the empirical validation, not the framework: as LLMs are applied to harder tasks (low-resource languages, fine-grained categories with $K \\geq 7$), the confusion matrices will be less diagonal-dominant and the framework's diagnostic value will increase.\nSemi-synthetic experiments (injecting controlled degradation into empirical confusion matrices) could demonstrate behavior in these regimes but are outside the scope of the current study.\n\n\\paragraph{Collider ASV non-monotonicity.}\nThe 7\\% monotonicity violation rate for collider ASV and 3\\% for front-door are honest limitations.\nA restricted ASV definition (constraining the $\\delta$-path to monotone regions) or a conditional ASV (defining separate bounds by confusion matrix structure region) are viable repairs that increase framework complexity.\nCollider topologies are less common than confounding and mediation in CSS practice, partially mitigating this limitation.\n\n\\paragraph{ASV discriminative power.}\nFive of nine empirical combinations produce trivially large ASVs ($>$50), providing formal robustness guarantees but limited discriminative value.\nThe four meaningful cases (ASV $<$ 20) correctly classify fragile vs.\\ robust, suggesting that ASV is most informative precisely when researchers most need guidance.\n\n%% ============================================================\n%% 9. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented a systematic framework for analyzing multi-class annotation error in LLM-annotated causal studies.\nOur bias taxonomy reveals that exposure misclassification is the only topology producing direction-unpredictable bias under non-differential $K \\geq 3$ error (85\\% reversal rate), while five other topologies preserve direction but vary in magnitude.\nAnnotation Sensitivity Values provide calibrated robustness indicators, with formal proofs for confounding and MC-validated conjectures for the remaining topologies.\nThe correction guidance framework and open-source toolkit translate these theoretical results into actionable diagnostics.\n\nThe binary measurement error framework is insufficient for multi-class annotation: researchers need the full $K \\times K$ confusion matrix, knowledge of their DAG topology, and tools that account for their interaction.\nWe provide all three.\n\n%% ============================================================\n%% REFERENCES (placeholder entries)\n%% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Baumann et~al.(2025)]{baumann2025}\nBaumann, M., et~al. (2025).\n\\newblock Automated annotation and downstream validity in computational social science.\n\\newblock \\textit{Proceedings of ACL 2025}.\n\n\\bibitem[Brenner(1993)]{brenner1993}\nBrenner, H. (1993).\n\\newblock Bias due to non-differential misclassification of polytomous confounders.\n\\newblock \\textit{Journal of Clinical Epidemiology}, 46(1):57--63.\n\n\\bibitem[Bross(1954)]{bross1954}\nBross, I.~D.~J. (1954).\n\\newblock Misclassification in 2 $\\times$ 2 tables.\n\\newblock \\textit{Biometrics}, 10(4):478--486.\n\n\\bibitem[Hern\\'{a}n and Cole(2009)]{hernan2009}\nHern\\'{a}n, M.~A. and Cole, S.~R. (2009).\n\\newblock Invited commentary: Causal diagrams and measurement bias.\n\\newblock \\textit{American Journal of Epidemiology}, 170(8):959--964.\n\n\\bibitem[Jerzak et~al.(2025)]{jerzak2025}\nJerzak, C.~T., et~al. (2025).\n\\newblock Benchmarking correction methods for LLM annotation error.\n\\newblock \\textit{Proceedings of EMNLP 2025}.\n\n\\bibitem[Kim et~al.(2025)]{kim2025}\nKim, S., et~al. (2025).\n\\newblock Correlated errors in LLM annotation: Implications for multi-annotator aggregation.\n\\newblock \\textit{Proceedings of ICML 2025}.\n\n\\bibitem[Lee and Wood-Doughty(2024)]{lee2024}\nLee, J. and Wood-Doughty, Z. (2024).\n\\newblock Categorical measurement error in LLM-annotated data.\n\\newblock \\textit{Proceedings of EMNLP 2024}.\n\n\\bibitem[TeBlunthuis et~al.(2024)]{teblunthuis2024}\nTeBlunthuis, N., et~al. (2024).\n\\newblock Measurement error correction for binary annotations.\n\\newblock \\textit{Proceedings of ACL 2024}.\n\n\\bibitem[VanderWeele and Li(2019)]{vanderweele2019}\nVanderWeele, T.~J. and Li, Y. (2019).\n\\newblock Simple sensitivity analysis for differential measurement error.\n\\newblock \\textit{American Journal of Epidemiology}, 188(10):1823--1829.\n\n\\bibitem[Wood-Doughty et~al.(2018)]{wood-doughty2018}\nWood-Doughty, Z., et~al. (2018).\n\\newblock Challenges of using text classifiers for causal inference.\n\\newblock \\textit{Proceedings of EMNLP 2018}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7c1fab6-b4dc-4738-a0ab-9136d808c554",
  "isSidechain": false,
  "requestId": "req_011CbDWtqNvXKKx2nNKdrmse",
  "type": "assistant",
  "uuid": "2491a6f8-0f1f-4e66-a123-16682362af44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyqbFqbFXE8Duj11nj5Ydp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5794,
      "cache_read_input_tokens": 40619,
      "output_tokens": 13302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13302,
          "cache_read_input_tokens": 40619,
          "cache_creation_input_tokens": 5794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5794
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

_source line 25 · 2026-05-20T08:41:08.496Z_

<details><summary>↩ Tool result · `toolu_01Y4smPM3ojPh9hYCpWvFzBA`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2491a6f8-0f1f-4e66-a123-16682362af44",
  "isSidechain": false,
  "promptId": "74990caf-6c19-4294-8631-731e236d5131",
  "type": "user",
  "uuid": "c6ef18ac-55b8-4e8d-a6b8-36411342d3ba",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{geometry}\n\\usepackage{natbib}\n\\usepackage{bm}\n\\usepackage{enumitem}\n\n\\geometry{margin=1in}\n\n\\newcommand{\\Cmat}{\\mathbf{C}}\n\\newcommand{\\bvec}{\\mathbf{b}}\n\\newcommand{\\R}{\\mathbb{R}}\n\n\\title{Multi-Class Annotation Errors Are Not Created Equal:\\\\\nBias Taxonomy, Sensitivity Analysis, and Correction Guidance\\\\for LLM-Annotated Causal Studies}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nLarge Language Models (LLMs) are rapidly replacing human annotators in computational social science (CSS), yet recent evidence shows that 31\\% of downstream causal conclusions may already be incorrect due to annotation errors.\nExisting measurement error frameworks assume binary variables, leaving researchers without diagnostic tools for multi-class ($K \\geq 3$) annotation.\nWe present the first systematic characterization of how $K \\times K$ confusion matrix structures interact with causal DAG topologies to produce downstream bias.\nOur bias taxonomy covers six canonical DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door) with closed-form expressions for $K=3$ and matrix-form expressions with eigendecomposition-based interpretability tools for general $K$.\nA key finding is a sharp topology-dependent dichotomy: exposure misclassification is the only topology where non-differential multi-class error produces direction-unpredictable bias (85\\% reversal rate in 100K random confusion matrices), while the remaining five topologies preserve bias direction but exhibit magnitude variation that requires the full $K \\times K$ matrix to quantify.\nWe introduce Annotation Sensitivity Values (ASVs), analogous to E-values for unmeasured confounding, that quantify the minimum annotation error amplification needed to overturn a conclusion.\nWe validate our framework on three CSS tasks annotated by three LLMs ($\\sim$270K annotations), and provide an open-source Python toolkit and a correction guidance decision framework.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nAnnotation by Large Language Models has become the de facto approach for large-scale coding in computational social science.\nProtest event classification, stance detection, and toxicity labeling are routinely performed by LLMs at a fraction of the cost of human annotation.\nYet a growing body of evidence reveals that LLM annotation errors propagate into downstream causal analyses in ways that researchers cannot currently anticipate or diagnose \\citep{baumann2025}.\n\nThe core problem is structural.\nClassical measurement error theory provides reassuring guarantees for binary variables: non-differential misclassification of a binary exposure biases effect estimates toward the null \\citep{bross1954}.\nResearchers routinely invoke this guarantee to argue that their LLM-annotated results are ``conservative.''\nHowever, CSS variables are frequently multi-class: protest event types ($K=5$), stance categories ($K=3$), and emotion labels ($K=7$) are standard.\n\\citet{brenner1993} showed decades ago that polytomous misclassification can bias in either direction, but no systematic framework exists that characterizes when, why, and by how much this occurs across different causal designs.\n\nThe gap matters because different causal designs interact differently with annotation error.\nA confounder mislabeled as category B instead of category A produces residual confounding; an exposure mislabeled the same way produces a fundamentally different distortion by swapping treatment assignments.\nWithout a framework that accounts for both the confusion matrix structure and the DAG topology, researchers cannot determine whether their specific combination is safe or hazardous.\nRecent work by \\citet{kim2025} compounds the urgency: cross-model annotation errors are highly correlated (60\\% agreement when both LLMs err), meaning multi-annotator ensembles cannot escape systematic bias.\n\nWe address this gap with three contributions:\n\n\\begin{enumerate}[leftmargin=*, itemsep=2pt]\n\\item \\textbf{Multi-class bias taxonomy.}\nClosed-form bias expressions for $K=3$ and matrix-form expressions with eigendecomposition-based interpretability tools for general $K$, across six canonical DAG topologies.\nOur taxonomy reveals a topology-dependent dichotomy: exposure misclassification is uniquely dangerous (85\\% direction reversal rate), while the remaining five topologies are directionally predictable but magnitude-variable.\nTheory matches Monte Carlo (MC) simulation in 32/42 topology-structure combinations (76\\%), with mismatches concentrated in complex topologies (collider, M-bias, front-door) where closed-form approximations require higher-order terms (Section~\\ref{sec:taxonomy}, Tables~\\ref{tab:taxonomy-summary} and~\\ref{tab:theory-mc}).\n\n\\item \\textbf{Annotation Sensitivity Values (ASVs).}\nA sensitivity analysis framework, analogous to E-values for unmeasured confounding, that quantifies the minimum annotation error amplification $\\delta$ needed to overturn a downstream conclusion.\nWe prove monotonicity and sharpness for the confounding topology, monotonicity for mediation and instrument topologies, and identify specific failure conditions for collider (7\\% non-monotone scenarios) and front-door (3\\%) topologies.\nAggregate MC coverage at 95\\% nominal level is 85\\% across all six topologies (Section~\\ref{sec:asv}, Tables~\\ref{tab:asv-proof} and~\\ref{tab:asv-remaining}).\n\n\\item \\textbf{Correction guidance framework and toolkit.}\nA decision framework mapping \\{topology $\\times$ error structure $\\times$ ASV\\} to appropriate correction methods, with 78\\% accuracy validated by MC simulation.\nThe framework identifies 12\\% of scenarios where no existing correction method is adequate, including correlated multi-LLM error as an open problem.\nWe release \\texttt{annot-sensitivity}, a pip-installable Python toolkit supporting $K=2$--$15$ across all six topologies (Section~\\ref{sec:correction}, Table~\\ref{tab:correction-framework}).\n\\end{enumerate}\n\nWe validate the full framework on three CSS tasks (protest event coding $K=5$, stance detection $K=3$, toxicity $K=2$) annotated by Llama 4 Maverick, Qwen 3.5 Plus, and DeepSeek V4, totaling $\\sim$270K annotations.\nASVs correctly classify all four non-trivial robustness cases (Section~\\ref{sec:empirical}).\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Measurement error in causal inference.}\nThe study of misclassification bias dates to \\citet{bross1954}, who established that non-differential binary exposure error biases toward the null.\n\\citet{brenner1993} extended this to polytomous variables, proving that multi-class misclassification can bias in either direction.\n\\citet{vanderweele2019} developed sensitivity bounds (E-values) for unmeasured confounding with binary risk ratios, providing a conceptual template for our ASV framework.\nHowever, none of these works provide a systematic taxonomy across DAG topologies or tools for general $K$.\n\n\\paragraph{Annotation error in NLP and CSS.}\n\\citet{wood-doughty2018} applied DAG reasoning to text classifier errors but restricted analysis to binary variables without formal bias theorems.\n\\citet{teblunthuis2024} provided the most complete binary treatment with Measurement-error Likelihood Adjustment (MLA) correction, but their framework is limited to $K=2$ and single classifiers.\n\\citet{lee2024} extended to categorical variables and LLM classifiers, covering unobserved confounding on a single dataset (MIMIC).\nOur work covers six topologies with a systematic taxonomy, sensitivity analysis, and correction guidance.\n\n\\paragraph{LLM annotation quality.}\n\\citet{jerzak2025} benchmarked correction methods for LLM annotation but treated error as monolithic, without conditioning on confusion matrix structure or DAG topology.\n\\citet{kim2025} documented that cross-model LLM errors are highly correlated, a finding that strengthens the case for error-structure-aware analysis rather than ensemble approaches.\n\\citet{baumann2025} quantified that 31\\% of downstream CSS conclusions are incorrect when using LLM annotations, motivating diagnostic tools rather than better annotators.\n\n%% ============================================================\n%% 3. BIAS TAXONOMY\n%% ============================================================\n\\section{Multi-Class Bias Taxonomy}\\label{sec:taxonomy}\n\n\\subsection{Setup and Notation}\n\nConsider a variable $V$ with $K$ categories, annotated by an LLM with confusion matrix $\\Cmat \\in \\R^{K \\times K}$ where $C_{jk} = P(\\hat{V}=k \\mid V=j)$.\nThe variable $V$ occupies a specific role in a causal DAG $\\mathcal{G}$: confounder, exposure, mediator, collider, instrument, or front-door criterion variable.\nLet $\\beta$ denote the true causal effect and $\\hat{\\beta}(\\Cmat)$ the estimate obtained when $V$ is replaced by its LLM annotation $\\hat{V}$.\nThe bias is $B(\\Cmat, \\mathcal{G}) = \\hat{\\beta}(\\Cmat) - \\beta$.\n\nFor $K=3$, we derive closed-form expressions $B(\\Cmat, \\mathcal{G})$ for each of the six topologies.\nFor general $K$, the bias takes a matrix form $\\bvec(\\Cmat, \\mathcal{G}) = \\mathbf{M}(\\Cmat, \\mathcal{G})\\bm{\\theta}$ where $\\mathbf{M}$ depends on the Kronecker product of $\\Cmat$ with structural parameters from $\\mathcal{G}$, and $\\bm{\\theta}$ collects the true causal parameters.\n\n\\subsection{Closed-Form Results ($K=3$, Six Topologies)}\\label{sec:closed-form}\n\nWe evaluate each bias expression against MC simulation with 1000 replications ($N=10{,}000$) across six named confusion matrix structures: identity-adjacent, uniform-leaning, near-permutation, block-diagonal, asymmetric, and random-moderate.\nWe also run a random search over 100K confusion matrices per topology.\n\n\\begin{table}[t]\n\\centering\n\\caption{Six-topology bias taxonomy summary ($K=3$). Reversal rate from 100K random confusion matrices. Theory-MC match counts structures (of 6) where theoretical bias falls within 95\\% MC confidence interval.}\n\\label{tab:taxonomy-summary}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nTopology & Reversal & Theory-MC & Bias Range & Direction Class \\\\\n\\midrule\nConfounding & 0.0\\% & 6/6 & 0.063--0.298 & Monotone toward OVB \\\\\nExposure & 85.0\\% & 5/6 & $-$0.84--0.42 & \\textbf{Unpredictable} \\\\\nMediation & 0.0\\% & 5/6 & 0.00--0.15 & Monotone attenuation \\\\\nCollider & 0.0\\% & 4/6 & 0.02--0.18 & Monotone (conditioning) \\\\\nM-bias & 0.0\\% & 4/6 & 0.04--0.22 & Monotone (dual path) \\\\\nInstrument & 0.0\\% & 5/6 & 0.03--0.25 & Monotone attenuation \\\\\nFront-door & 0.0\\% & 3/6 & 0.01--0.19 & Monotone (compound) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:taxonomy-summary} reveals a sharp dichotomy.\nExposure misclassification is the only topology where non-differential $K=3$ error produces direction reversal, with 85\\% of random confusion matrices violating the binary bias-toward-null guarantee.\nAmong these violations, 83.4\\% are sign reversals and 14.1\\% are amplifications beyond the true effect magnitude.\nThe worst case reaches $\\hat{\\beta} = -0.84$ for a true $\\beta = 1.0$ (sign reversal with 2.83$\\times$ amplification).\n\nThe mechanism is specific to exposure: when the exposure variable is misclassified, near-permutation $\\Cmat$ structures swap treatment labels across categories.\nA subject truly in treatment group A is coded as group B, and the outcome attributed to the wrong treatment.\nThis label-swap mechanism is structurally impossible in binary ($K=2$) non-differential misclassification, where the only effect is attenuation.\n\nFor the remaining five topologies, the annotated variable (confounder, mediator, etc.) does not define the treatment contrast.\nIts misclassification modulates bias magnitude but cannot flip the numerator/denominator of the estimand.\nConfounding produces the largest magnitude range (0.063--0.298) among the well-behaved topologies, while mediation produces the smallest (0.00--0.15).\n\n\\begin{table}[t]\n\\centering\n\\caption{Theory vs MC match detail. Each row is one topology-structure combination. Match = theoretical bias within 95\\% MC CI. 10 mismatches concentrate in complex topologies with extreme $\\Cmat$ structures.}\n\\label{tab:theory-mc}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTopology group & Matches / Total & Mismatch locations \\\\\n\\midrule\nConfounding & 6/6 & (none) \\\\\nExposure & 5/6 & Near-permutation \\\\\nMediation & 5/6 & Block-diagonal \\\\\nCollider & 4/6 & Near-perm., asymmetric \\\\\nM-bias & 4/6 & Block-diag., asymmetric \\\\\nInstrument & 5/6 & Near-permutation \\\\\nFront-door & 3/6 & Near-perm., asym., block-diag. \\\\\n\\midrule\n\\textbf{Total} & \\textbf{32/42 (76\\%)} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overall theory-MC match rate is 76\\% (Table~\\ref{tab:theory-mc}).\nAll 10 mismatches occur with extreme confusion matrix structures (near-permutation, block-diagonal, asymmetric) in topologies with complex conditioning or compound estimation steps.\nFront-door has the lowest match rate (3/6) because the front-door criterion involves two mediation steps whose approximation errors compound.\nWe treat front-door expressions as MC-validated conjectures rather than exact theorems.\n\n\\subsection{General-$K$ Extensions ($K=5,7$)}\\label{sec:general-k}\n\nFor $K > 3$, we express bias in matrix form and develop three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, and (c) diagnostic visualizations.\nWe validate on confounding, mediation, and collider topologies.\n\n\\begin{table}[t]\n\\centering\n\\caption{Eigendecomposition summary across $K$ and topologies. $\\lambda_1/\\text{tr}(\\Lambda)$ = fraction of bias variance captured by the dominant eigenvalue. Modes for 90\\% = number of eigenvalues needed for 90\\% cumulative variance. Bound ratio = worst-case bound / MC observed maximum.}\n\\label{tab:eigen}\n\\small\n\\begin{tabular}{clcccc}\n\\toprule\n$K$ & Topology & $\\lambda_1/\\text{tr}(\\Lambda)$ & Modes (90\\%) & Bound ratio \\\\\n\\midrule\n3 & Confounding & --- & 1 & 1.3$\\times$ \\\\\n3 & Mediation & --- & 1 & 1.3$\\times$ \\\\\n3 & Collider & --- & 2 & 1.4$\\times$ \\\\\n\\midrule\n5 & Confounding & 0.82 & 1 & 1.8$\\times$ \\\\\n5 & Mediation & 0.75 & 2 & 2.0$\\times$ \\\\\n5 & Collider & 0.58 & 3 & 2.5$\\times$ \\\\\n\\midrule\n7 & Confounding & 0.76 & 2 & 2.5$\\times$ \\\\\n7 & Mediation & 0.68 & 2 & 2.8$\\times$ \\\\\n7 & Collider & 0.49 & 4 & 3.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:eigen} shows that eigendecomposition is an effective summary for confounding (dominant eigenvalue captures $\\geq$76\\% variance through $K=7$) but degrades for collider ($\\lambda_1/\\text{tr}(\\Lambda) = 0.49$ at $K=7$, requiring 4 modes for 90\\% variance).\nThe theory-MC match rate decreases from 70\\% at $K=5$ to 63\\% at $K=7$, partly because per-cell sample sizes become insufficient at higher $K$ ($7 \\times 7 = 49$ cells with $N=10{,}000$).\n\nWorst-case scalar bounds grow increasingly conservative with $K$ (1.8--2.5$\\times$ at $K=5$; 2.5--3.2$\\times$ at $K=7$).\nThe bound optimizes over an adversarial $\\Cmat$ whose supremum is not achievable in practice because the feasible region of confusion matrices is a low-dimensional manifold in high-dimensional space.\nFor collider and M-bias topologies at $K \\geq 5$, we recommend pairing worst-case bounds with diagnostic visualizations rather than relying on eigendecomposition alone.\n\n\\subsection{Binarization Collapse ($K \\to 2$)}\\label{sec:binarization}\n\nIf multi-class bias analysis is complex, can researchers collapse $K$-class variables to binary and apply established binary theory?\nWe compare full multi-class bias expressions with their binarized counterparts across all six topologies and $K = 3, 5, 7$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Binarization delta: the maximum absolute difference between multi-class and binarized bias expressions. Confounding consistently shows the largest delta.}\n\\label{tab:binarization}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTopology & $K=3$ & $K=5$ & $K=7$ \\\\\n\\midrule\nConfounding & 0.078 & 0.085 & \\textbf{0.091} \\\\\nExposure & 0.072 & --- & --- \\\\\nMediation & 0.041 & --- & --- \\\\\nCollider & 0.068 & --- & --- \\\\\nM-bias & 0.055 & --- & --- \\\\\nInstrument & 0.038 & --- & --- \\\\\nFront-door & 0.045 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:binarization} shows that binarization introduces a maximum absolute bias discrepancy of 0.091 (confounding, $K=7$).\nFour of six topologies exceed $\\Delta = 0.05$, and two exceed 0.08.\nBinarization does not reverse bias direction in any tested case; its effect is purely on magnitude estimation.\nIn context, a $\\Delta$ of 0.09 represents 30--70\\% of the full multi-class bias across confounding scenarios, indicating that binarization is not a safe shortcut for magnitude estimation.\nThe discrepancy is largest for confounding because residual confounding is most sensitive to collapsing fine-grained categories into coarse binary groups.\n\n%% ============================================================\n%% 4. ANNOTATION SENSITIVITY VALUES\n%% ============================================================\n\\section{Annotation Sensitivity Values}\\label{sec:asv}\n\n\\subsection{Definition}\n\nGiven a reference confusion matrix $\\Cmat_0$ (e.g., from a validation set), we define a family of perturbed matrices $\\Cmat(\\delta) = (1 - \\delta)\\Cmat_0 + \\delta \\Cmat_{\\text{worst}}$ for $\\delta \\in [0,1]$, where $\\Cmat_{\\text{worst}}$ is the worst-case matrix within a topology-specific constraint set.\nThe Annotation Sensitivity Value (ASV) for a conclusion $H$ is:\n\\begin{equation}\n\\text{ASV}(H, \\Cmat_0, \\mathcal{G}) = \\inf\\{\\delta > 0 : H \\text{ is overturned under } \\Cmat(\\delta) \\text{ in topology } \\mathcal{G}\\}.\n\\end{equation}\nLarger ASV values indicate greater robustness: a conclusion with $\\text{ASV} = 5$ requires annotation error five times worse than the reference to be overturned.\nASVs are reported alongside effect estimates, analogous to how E-values are reported for unmeasured confounding.\n\nWe study two formal properties:\n\\textit{Monotonicity}: $|B(\\Cmat(\\delta), \\mathcal{G})|$ is non-decreasing in $\\delta$ (bias grows with error amplification).\n\\textit{Sharpness}: the ASV bound is achievable (there exists a $\\Cmat$ that attains the bound).\n\n\\subsection{Formal Results: Confounding, Mediation, Collider}\\label{sec:asv-formal}\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV proof status and MC validation for three priority topologies. Coverage = fraction of scenarios where ASV-implied confidence set contains the true bias, at nominal 90/95/99\\% levels.}\n\\label{tab:asv-proof}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTopology & Monotone & Sharp & Cov.\\ 90 & Cov.\\ 95 & Cov.\\ 99 \\\\\n\\midrule\nConfounding & \\checkmark (formal) & \\checkmark (formal) & 0.88 & 0.93 & 0.97 \\\\\nMediation & \\checkmark (formal) & $\\times$ (1.4--1.8$\\times$) & 0.86 & 0.91 & 0.96 \\\\\nCollider & $\\times$ (7\\% viol.) & N/A & 0.74 & 0.78 & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv-proof} summarizes the proof status.\nConfounding achieves both formal monotonicity and sharpness: residual confounding is a monotone function of annotation error amplification, and near-permutation confusion matrices achieve the worst-case bound.\n\nMediation achieves formal monotonicity (indirect effect attenuation is monotone in mediator misclassification) but not sharpness.\nThe ASV bound is conservative by a factor of 1.4--1.8$\\times$ because the mediation bias maximum is structurally bounded by the direct effect magnitude; the worst-case $\\Cmat$ optimization includes structurally unreachable configurations.\n\nCollider ASV fails monotonicity in 7\\% of tested confusion matrix structures, specifically when off-diagonal mass is concentrated in two adjacent cells and $\\delta \\in [0.3, 0.5]$.\nThe mechanism is that moderate misclassification partially opens the collider path while preserving conditioning structure, but larger misclassification destroys the conditioning precision, diluting the collider association.\nThis produces non-monotone bias as a function of $\\delta$.\nWe recommend reporting collider ASVs with a caveat and using the 99\\% coverage level ($0.85$) as a conservative choice.\n\n\\subsection{MC Validation: M-Bias, Instrument, Front-Door}\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV validation for the remaining three topologies (MC-validated conjectures). Front-door shows 3\\% monotonicity violations at extreme $\\Cmat$.}\n\\label{tab:asv-remaining}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTopology & Monotone & Sharp & Tightness & Cov.\\ 95 \\\\\n\\midrule\nM-bias & \\checkmark (0/1000) & $\\times$ (1.6--2.1$\\times$) & Conserv. & 0.86 \\\\\nInstrument & \\checkmark (0/1000) & Near (1.1$\\times$) & Tight & 0.88 \\\\\nFront-door & Partial (3\\% viol.) & $\\times$ (1.8--2.4$\\times$) & Conserv. & 0.76 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv-remaining} reports MC-validated results for the remaining topologies.\nFive of six topologies show monotonicity (collider 7\\% violations, front-door 3\\%).\nOnly confounding achieves formal sharpness; instrument is near-sharp (within 1.1$\\times$).\nAggregate 95\\% coverage across all six topologies is 0.85; excluding front-door (0.76), the remaining five average 0.87.\n\nThe front-door violations arise from a different mechanism than collider: the front-door criterion involves two estimation steps (exposure $\\to$ mediator and mediator $\\to$ outcome adjusting for exposure), and near-rank-deficient confusion matrices can destabilize the second step, producing local non-monotonicity.\n\n\\subsection{Spectral Analysis of Pathological Confusion Matrices}\\label{sec:spectral}\n\nTo characterize when bias becomes severe, we analyze pathological confusion matrix structures (near-permutation, rank-deficient, block-diagonal) using spectral properties.\n\n\\begin{table}[t]\n\\centering\n\\caption{Spectral predictors of bias severity. For exposure, the target is reversal (binary); for other topologies, the target is bias magnitude.}\n\\label{tab:spectral}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nTopology & Predictor & Target & AUC / $R^2$ \\\\\n\\midrule\nExposure & $\\lambda_2/\\lambda_1 > 0.6$ & Reversal & AUC = 0.92 \\\\\nExposure & Diag.\\ dom.\\ $< 0.45$ & Reversal & AUC = 0.89 \\\\\nOthers (5) & $\\lambda_1$ & Magnitude & $R^2$ = 0.78 \\\\\nOthers (5) & Spectral gap & Magnitude & $R^2$ = 0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe spectral ratio $\\lambda_2/\\lambda_1$ of the confusion matrix provides a principled predictor of exposure bias reversal (Table~\\ref{tab:spectral}).\nWhen $\\lambda_2/\\lambda_1 > 0.6$ (i.e., the ``dominant confusion'' eigenmode is at least 60\\% as strong as the ``correct classification'' eigenmode), treatment label swaps become sufficient to reverse effect direction, yielding AUC = 0.92 for reversal prediction.\nDiagonal dominance (the simpler proxy $\\min_i C_{ii} / \\max_i \\sum_{j \\neq i} C_{ij}$) achieves AUC = 0.89 with a threshold of 0.45.\n\nFor the five well-behaved topologies, $\\lambda_1$ and spectral gap predict bias magnitude with $R^2 = 0.78$, but no reversal threshold exists because bias direction is determined by topology rather than by the confusion matrix spectrum.\n\nBlock-diagonal confusion matrices (corresponding to models that distinguish coarse categories but confuse fine-grained subcategories) produce 1.5--2.3$\\times$ bias amplification relative to random confusion matrices of the same accuracy, because structured confusion concentrates error rather than dispersing it.\nRank-deficient confusion matrices cause numerical instability in bias expressions that require matrix inversion; our toolkit applies Tikhonov regularization in these cases.\n\n%% ============================================================\n%% 5. EMPIRICAL VALIDATION\n%% ============================================================\n\\section{Empirical Validation}\\label{sec:empirical}\n\n\\subsection{LLM Annotation Experiments}\n\nWe collect annotations from Llama 4 Maverick, Qwen 3.5 Plus, and DeepSeek V4 on three CSS tasks: protest event coding ($K=5$), stance detection ($K=3$), and toxicity classification ($K=2$), totaling $\\sim$270K annotations (30K items $\\times$ 3 models $\\times$ 3 tasks).\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrix statistics. Diagonal dominance = sum of diagonal / sum of all entries.}\n\\label{tab:empirical-cm}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nTask ($K$) & Metric & Range (3 LLMs) \\\\\n\\midrule\nProtest ($K\\!=\\!5$) & Accuracy & 0.68--0.73 \\\\\n& Diag.\\ dominance & 0.74--0.80 \\\\\n\\midrule\nStance ($K\\!=\\!3$) & Accuracy & 0.76--0.81 \\\\\n& Diag.\\ dominance & 0.82--0.87 \\\\\n\\midrule\nToxicity ($K\\!=\\!2$) & Accuracy & 0.83--0.88 \\\\\n& Diag.\\ dominance & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Inter-model error correlation (pairwise Cohen's $\\kappa$ on error cells). High agreement confirms correlated errors across LLMs.}\n\\label{tab:inter-model}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nModel pair & $\\kappa$ (error agreement) \\\\\n\\midrule\nLlama--Qwen & 0.58--0.67 \\\\\nLlama--DeepSeek & 0.58--0.67 \\\\\nQwen--DeepSeek & 0.58--0.67 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:empirical-cm} shows that all empirical confusion matrices are diagonal-dominant (diagonal dominance 0.74--0.87), with no near-permutation structures observed.\nProtest event coding ($K=5$) has the lowest accuracy and most dispersed off-diagonal mass; toxicity ($K=2$) is most diagonal-dominant.\nInter-model error correlation (Table~\\ref{tab:inter-model}) shows pairwise $\\kappa$ of 0.58--0.67, consistent with the 60\\% cross-model error agreement reported by \\citet{kim2025} and driven by shared pre-training data distributions that cause similar errors on the same ``hard'' instances.\n\n\\subsection{Downstream Regression Bias}\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream bias vs gold standard for representative task-model-topology combinations. Bias $> 0.05$ is bolded.}\n\\label{tab:downstream-bias}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nTask & Model & $|\\text{Bias}|$ & Reversal? & Theory match \\\\\n\\midrule\nProtest & Qwen 3.5 Plus & \\textbf{0.12} & No & \\checkmark \\\\\nProtest & Llama 4 & \\textbf{0.08} & No & \\checkmark \\\\\nProtest & DeepSeek V4 & \\textbf{0.06} & No & \\checkmark \\\\\nStance & Qwen 3.5 Plus & 0.04 & No & \\checkmark \\\\\nStance & Llama 4 & 0.03 & No & \\checkmark \\\\\nStance & DeepSeek V4 & 0.02 & No & \\checkmark \\\\\nToxicity & All & $<$0.02 & No & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:downstream-bias} reports downstream regression bias against gold-standard labels.\nTwo to three of nine combinations exceed $|\\text{Bias}| > 0.05$, concentrated in protest event coding with weaker models.\nNo direction reversal is observed, consistent with our taxonomy: empirical confusion matrices are far from the near-permutation threshold ($\\lambda_2/\\lambda_1 > 0.6$) required for exposure reversal.\nThe maximum observed bias is 0.12 (Qwen 3.5 Plus on protest events), which is practically meaningful given that CSS effect sizes typically range from 0.1 to 0.3.\n\n\\subsection{ASV Calibration}\n\n\\begin{table}[t]\n\\centering\n\\caption{ASV values for nine task-model combinations. ASV $> 50$ indicates trivially robust (annotation error would need $> 50\\times$ amplification to overturn the conclusion).}\n\\label{tab:asv-empirical}\n\\small\n\\begin{tabular}{llccl}\n\\toprule\nTask & Model & ASV & Classification & Note \\\\\n\\midrule\nProtest & Qwen 3.5 Plus & 2.3 & Fragile & Meaningful \\\\\nProtest & Llama 4 & 4.1 & Moderate & Meaningful \\\\\nProtest & DeepSeek V4 & 8.5 & Moderate & Meaningful \\\\\nStance & DeepSeek V4 & 18.7 & Robust & Meaningful \\\\\nStance & Llama 4 & $>$50 & Robust & Trivial \\\\\nStance & Qwen 3.5 Plus & $>$50 & Robust & Trivial \\\\\nToxicity & Llama 4 & $>$50 & Robust & Trivial \\\\\nToxicity & Qwen 3.5 Plus & $>$50 & Robust & Trivial \\\\\nToxicity & DeepSeek V4 & $>$50 & Robust & Trivial \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv-empirical} shows ASV values across all nine task-model combinations.\nFive of nine produce trivially large ASVs ($>$50), reflecting the diagonal-dominant confusion matrices.\nThe four meaningful cases correctly classify robustness: protest/Qwen ($\\text{ASV} = 2.3$, fragile) exhibits the largest downstream bias (0.12), while protest/DeepSeek ($\\text{ASV} = 8.5$, moderate) has smaller bias (0.06).\nAll four meaningful ASVs correctly distinguish fragile from robust combinations, achieving perfect concordance on non-trivial cases.\n\nThe prevalence of trivially robust cases is a feature, not a bug: for five of nine combinations, ASV provides a formal guarantee that annotation error cannot meaningfully distort conclusions at current LLM quality levels.\nFor the four flagged combinations, ASV identifies where researchers should invest in validation or correction.\n\n%% ============================================================\n%% 6. CORRECTION GUIDANCE\n%% ============================================================\n\\section{Correction Guidance Framework}\\label{sec:correction}\n\nWe construct a decision framework mapping \\{topology $\\times$ error structure $\\times$ ASV\\} to correction methods: Measurement-error Likelihood Adjustment (MLA), Prediction-Powered Inference (PPI), Design-based Sensitivity Limits (DSL), or ``gold label collection required.''\n\n\\begin{table}[t]\n\\centering\n\\caption{Correction framework accuracy by topology (MC validation). MLA = Measurement-error Likelihood Adjustment, PPI = Prediction-Powered Inference, DSL = Design-based Sensitivity Limits.}\n\\label{tab:correction-framework}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTopology & Accuracy & MLA fraction & No method \\\\\n\\midrule\nConfounding & 0.82 & 0.60 & 0.08 \\\\\nExposure & 0.85 & 0.15 & 0.35 \\\\\nMediation & 0.80 & 0.72 & 0.05 \\\\\nCollider & 0.68 & 0.55 & 0.15 \\\\\nM-bias & 0.76 & 0.68 & 0.10 \\\\\nInstrument & 0.81 & 0.70 & 0.08 \\\\\nFront-door & 0.74 & 0.65 & 0.12 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{0.78} & \\textbf{0.65} & \\textbf{0.12} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe framework achieves 78\\% accuracy overall (Table~\\ref{tab:correction-framework}), compared to a trivial baseline of 65\\% (``always recommend MLA'').\nMLA dominates recommendations in five well-behaved topologies because it is the most general method, adjusting the likelihood using the estimated confusion matrix.\nThe 13-percentage-point improvement over the trivial baseline concentrates in three areas:\n\n\\textit{Exposure reversal regime.}\nFor exposure topology with near-permutation confusion matrices, the framework correctly recommends gold label collection (35\\% of exposure scenarios have no adequate correction).\nMLA can amplify error in the sign-reversed regime; the framework identifies these cases.\n\n\\textit{PPI edge cases.}\nPPI outperforms MLA in 8\\% of scenarios, specifically in finite-sample regimes where a small gold-standard sample combined with a large LLM-annotated sample favors PPI's semi-supervised approach.\n\n\\textit{Open problems.}\nThe framework identifies 12\\% of scenarios where no existing method is adequate, concentrated in differential multi-class error with complex topologies and correlated multi-LLM error.\nDependence-aware multi-annotator correction is flagged as an open problem.\n\nCollider accuracy is lowest (0.68) because the choice between ``correct annotation then re-condition'' and ``avoid conditioning'' depends on the interaction between effect magnitude and confusion matrix structure, which a depth-4 decision tree captures imperfectly.\n\n%% ============================================================\n%% 7. THE ANNOT-SENSITIVITY TOOLKIT\n%% ============================================================\n\\section{The \\texttt{annot-sensitivity} Toolkit}\\label{sec:toolkit}\n\nWe release an open-source Python package (pip-installable) with four core modules:\n\\texttt{BiasExpr} (bias expressions for six topologies, $K=2$--15),\n\\texttt{ASV} (annotation sensitivity values with coverage calibration),\n\\texttt{CorrectionGuide} (decision framework lookup), and\n\\texttt{DiagnosticPlot} (spectral analysis and sensitivity curve visualization).\n\nRuntime is $<$0.1s for $K=3$, $<$1s for $K=7$, and $<$10s for $K=15$, because all bias expressions are closed-form matrix operations (no MC simulation required at inference time).\nThe package includes six worked examples (one per topology) and $\\sim$20 pages of documentation.\nTest coverage is approximately 85\\%.\n\nA typical workflow: the user provides a DAG specification, an estimated confusion matrix (from a validation set), and a downstream effect estimate.\nThe toolkit returns the predicted bias, an ASV value with interpretation, a sensitivity curve, and a correction recommendation.\n\n%% ============================================================\n%% 8. DISCUSSION & LIMITATIONS\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{The topology-dependent dichotomy.}\nOur central finding is that multi-class annotation error produces a sharp split between exposure misclassification (direction-unpredictable, requiring gold labels or spectral monitoring) and the remaining five topologies (direction-predictable, correctable with MLA).\nThis dichotomy has immediate practical implications for CSS researchers: the role of the annotated variable in the causal DAG, not just its accuracy, determines the risk profile.\nExposure is the most commonly LLM-annotated variable in CSS causal studies, making this finding especially relevant.\n\n\\paragraph{Theory-MC gap.}\nOur closed-form expressions match MC in 76\\% of topology-structure combinations.\nThe 24\\% mismatch concentrates in complex topologies with extreme confusion matrices, where first-order approximations are insufficient.\nWe view the MC validation itself as a necessary complement to the theoretical contribution: in the presence of approximation, validated numerical results are more trustworthy than unvalidated closed forms.\n\n\\paragraph{Diagonal-dominant empirical confusion matrices.}\nCurrent SOTA LLMs produce diagonal-dominant confusion matrices on well-studied CSS tasks, limiting the empirical demonstration of extreme-bias scenarios.\nThis is a limitation of the empirical validation, not the framework: as LLMs are applied to harder tasks (low-resource languages, fine-grained categories with $K \\geq 7$), the confusion matrices will be less diagonal-dominant and the framework's diagnostic value will increase.\nSemi-synthetic experiments (injecting controlled degradation into empirical confusion matrices) could demonstrate behavior in these regimes but are outside the scope of the current study.\n\n\\paragraph{Collider ASV non-monotonicity.}\nThe 7\\% monotonicity violation rate for collider ASV and 3\\% for front-door are honest limitations.\nA restricted ASV definition (constraining the $\\delta$-path to monotone regions) or a conditional ASV (defining separate bounds by confusion matrix structure region) are viable repairs that increase framework complexity.\nCollider topologies are less common than confounding and mediation in CSS practice, partially mitigating this limitation.\n\n\\paragraph{ASV discriminative power.}\nFive of nine empirical combinations produce trivially large ASVs ($>$50), providing formal robustness guarantees but limited discriminative value.\nThe four meaningful cases (ASV $<$ 20) correctly classify fragile vs.\\ robust, suggesting that ASV is most informative precisely when researchers most need guidance.\n\n%% ============================================================\n%% 9. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented a systematic framework for analyzing multi-class annotation error in LLM-annotated causal studies.\nOur bias taxonomy reveals that exposure misclassification is the only topology producing direction-unpredictable bias under non-differential $K \\geq 3$ error (85\\% reversal rate), while five other topologies preserve direction but vary in magnitude.\nAnnotation Sensitivity Values provide calibrated robustness indicators, with formal proofs for confounding and MC-validated conjectures for the remaining topologies.\nThe correction guidance framework and open-source toolkit translate these theoretical results into actionable diagnostics.\n\nThe binary measurement error framework is insufficient for multi-class annotation: researchers need the full $K \\times K$ confusion matrix, knowledge of their DAG topology, and tools that account for their interaction.\nWe provide all three.\n\n%% ============================================================\n%% REFERENCES (placeholder entries)\n%% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Baumann et~al.(2025)]{baumann2025}\nBaumann, M., et~al. (2025).\n\\newblock Automated annotation and downstream validity in computational social science.\n\\newblock \\textit{Proceedings of ACL 2025}.\n\n\\bibitem[Brenner(1993)]{brenner1993}\nBrenner, H. (1993).\n\\newblock Bias due to non-differential misclassification of polytomous confounders.\n\\newblock \\textit{Journal of Clinical Epidemiology}, 46(1):57--63.\n\n\\bibitem[Bross(1954)]{bross1954}\nBross, I.~D.~J. (1954).\n\\newblock Misclassification in 2 $\\times$ 2 tables.\n\\newblock \\textit{Biometrics}, 10(4):478--486.\n\n\\bibitem[Hern\\'{a}n and Cole(2009)]{hernan2009}\nHern\\'{a}n, M.~A. and Cole, S.~R. (2009).\n\\newblock Invited commentary: Causal diagrams and measurement bias.\n\\newblock \\textit{American Journal of Epidemiology}, 170(8):959--964.\n\n\\bibitem[Jerzak et~al.(2025)]{jerzak2025}\nJerzak, C.~T., et~al. (2025).\n\\newblock Benchmarking correction methods for LLM annotation error.\n\\newblock \\textit{Proceedings of EMNLP 2025}.\n\n\\bibitem[Kim et~al.(2025)]{kim2025}\nKim, S., et~al. (2025).\n\\newblock Correlated errors in LLM annotation: Implications for multi-annotator aggregation.\n\\newblock \\textit{Proceedings of ICML 2025}.\n\n\\bibitem[Lee and Wood-Doughty(2024)]{lee2024}\nLee, J. and Wood-Doughty, Z. (2024).\n\\newblock Categorical measurement error in LLM-annotated data.\n\\newblock \\textit{Proceedings of EMNLP 2024}.\n\n\\bibitem[TeBlunthuis et~al.(2024)]{teblunthuis2024}\nTeBlunthuis, N., et~al. (2024).\n\\newblock Measurement error correction for binary annotations.\n\\newblock \\textit{Proceedings of ACL 2024}.\n\n\\bibitem[VanderWeele and Li(2019)]{vanderweele2019}\nVanderWeele, T.~J. and Li, Y. (2019).\n\\newblock Simple sensitivity analysis for differential measurement error.\n\\newblock \\textit{American Journal of Epidemiology}, 188(10):1823--1829.\n\n\\bibitem[Wood-Doughty et~al.(2018)]{wood-doughty2018}\nWood-Doughty, Z., et~al. (2018).\n\\newblock Challenges of using text classifiers for causal inference.\n\\newblock \\textit{Proceedings of EMNLP 2018}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "2491a6f8-0f1f-4e66-a123-16682362af44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attr…",
  "leafUuid": "c6ef18ac-55b8-4e8d-a6b8-36411342d3ba",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for annotation error study",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Tool call

_source line 28 · 2026-05-20T08:41:15.218Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016fnmZPTAzBvXQcQAJpxYfc`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6ef18ac-55b8-4e8d-a6b8-36411342d3ba",
  "isSidechain": false,
  "requestId": "req_011CbDXEQ8vzd24kcKXwbWbV",
  "type": "assistant",
  "uuid": "48d89ff0-e3c0-40f1-9388-00ca38b5585a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHBYBbq3TeR2TUYKpeNvva",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13368,
      "cache_read_input_tokens": 46413,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 46413,
          "cache_creation_input_tokens": 13368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13368
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

_source line 29 · 2026-05-20T08:41:16.226Z_

<details><summary>↩ Tool result · `toolu_016fnmZPTAzBvXQcQAJpxYfc`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/bm.sty)
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `baumann2025' on page 1 undefined on input lin
e 51.


Package natbib Warning: Citation `bross1954' on page 1 undefined on input line 
54.


Package natbib Warning: Citation `brenner1993' on page 1 undefined on input lin
e 57.


Package natbib Warning: Citation `kim2025' on page 1 undefined on input line 62
.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `sec:taxonomy' on page 2 undefined on input line 70.


LaTeX Warning: Reference `tab:taxonomy-summary' on page 2 undefined on input li
ne 70.


LaTeX Warning: Reference `tab:theory-mc' on page 2 undefined on input line 70.


LaTeX Warning: Reference `sec:asv' on page 2 undefined on input line 75.


LaTeX Warning: Reference `tab:asv-proof' on page 2 undefined on input line 75.


LaTeX Warning: Reference `tab:asv-remaining' on page 2 undefined on input line 
75.


LaTeX Warning: Reference `sec:correction' on page 2 undefined on input line 80.



LaTeX Warning: Reference `tab:correction-framework' on page 2 undefined on inpu
t line 80.


LaTeX Warning: Reference `sec:empirical' on page 2 undefined on input line 84.


Package natbib Warning: Citation `bross1954' on page 2 undefined on input line 
92.


Package natbib Warning: Citation `brenner1993' on page 2 undefined on input lin
e 93.


Package natbib Warning: Citation `vanderweele2019' on page 2 undefined on input
 line 94.


Package natbib Warning: Citation `wood-doughty2018' on page 2 undefined on inpu
t line 98.


Package natbib Warning: Citation `teblunthuis2024' on page 2 undefined on input
 line 99.


Package natbib Warning: Citation `lee2024' on page 2 undefined on input line 10
0.


Package natbib Warning: Citation `jerzak2025' on page 2 undefined on input line
 104.


Package natbib Warning: Citation `kim2025' on page 2 undefined on input line 10
5.


Package natbib Warning: Citation `baumann2025' on page 2 undefined on input lin
e 106.

[2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 123.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 123.


LaTeX Warning: Reference `tab:taxonomy-summary' on page 3 undefined on input li
ne 148.

[3]

LaTeX Warning: Reference `tab:theory-mc' on page 4 undefined on input line 183.



Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


LaTeX Warning: Reference `tab:eigen' on page 4 undefined on input line 217.

[4]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 224.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 224.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 224.


LaTeX Warning: Reference `tab:binarization' on page 5 undefined on input line 2
49.

[5]

LaTeX Warning: Reference `tab:asv-proof' on page 6 undefined on input line 292.



LaTeX Warning: Reference `tab:asv-remaining' on page 6 undefined on input line 
321.

[6]

LaTeX Warning: Reference `tab:spectral' on page 7 undefined on input line 349.


LaTeX Warning: Reference `tab:empirical-cm' on page 7 undefined on input line 4
04.


LaTeX Warning: Reference `tab:inter-model' on page 7 undefined on input line 40
6.


Package natbib Warning: Citation `kim2025' on page 7 undefined on input line 40
6.

[7]

LaTeX Warning: Reference `tab:downstream-bias' on page 8 undefined on input lin
e 430.


LaTeX Warning: Reference `tab:asv-empirical' on page 8 undefined on input line 
459.

[8]

LaTeX Warning: Reference `tab:correction-framework' on page 9 undefined on inpu
t line 496.

[9] [10]

Package natbib Warning: There were undefined citations.

[11] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1440.60
0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.
600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm080
0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1
200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ect
t1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e
cbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec
/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/
ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe
n/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn
appen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j
knappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/symbols/msbm10.pfb>
Output written on paper.pdf (11 pages, 294061 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/bm.sty)
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 123.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 123.

[3]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 188.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 224.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 224.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 224.

[4] [5] [6] [7] [8] [9] [10] [11] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1440.60
0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.
600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm080
0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1
200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ect
t1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e
cbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec
/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/
ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe
n/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn
appen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j
knappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/symbols/msbm10.pfb>
Output written on paper.pdf (11 pages, 297993 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48d89ff0-e3c0-40f1-9388-00ca38b5585a",
  "isSidechain": false,
  "promptId": "74990caf-6c19-4294-8631-731e236d5131",
  "type": "user",
  "uuid": "27f3c793-3494-4896-b9bc-57e3f90caae8",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/bm.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `baumann2025' on page 1 undefined on input lin\ne 51.\n\n\nPackage natbib Warning: Citation `bross1954' on page 1 undefined on input line \n54.\n\n\nPackage natbib Warning: Citation `brenner1993' on page 1 undefined on input lin\ne 57.\n\n\nPackage natbib Warning: Citation `kim2025' on page 1 undefined on input line 62\n.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:taxonomy' on page 2 undefined on input line 70.\n\n\nLaTeX Warning: Reference `tab:taxonomy-summary' on page 2 undefined on input li\nne 70.\n\n\nLaTeX Warning: Reference `tab:theory-mc' on page 2 undefined on input line 70.\n\n\nLaTeX Warning: Reference `sec:asv' on page 2 undefined on input line 75.\n\n\nLaTeX Warning: Reference `tab:asv-proof' on page 2 undefined on input line 75.\n\n\nLaTeX Warning: Reference `tab:asv-remaining' on page 2 undefined on input line \n75.\n\n\nLaTeX Warning: Reference `sec:correction' on page 2 undefined on input line 80.\n\n\n\nLaTeX Warning: Reference `tab:correction-framework' on page 2 undefined on inpu\nt line 80.\n\n\nLaTeX Warning: Reference `sec:empirical' on page 2 undefined on input line 84.\n\n\nPackage natbib Warning: Citation `bross1954' on page 2 undefined on input line \n92.\n\n\nPackage natbib Warning: Citation `brenner1993' on page 2 undefined on input lin\ne 93.\n\n\nPackage natbib Warning: Citation `vanderweele2019' on page 2 undefined on input\n line 94.\n\n\nPackage natbib Warning: Citation `wood-doughty2018' on page 2 undefined on inpu\nt line 98.\n\n\nPackage natbib Warning: Citation `teblunthuis2024' on page 2 undefined on input\n line 99.\n\n\nPackage natbib Warning: Citation `lee2024' on page 2 undefined on input line 10\n0.\n\n\nPackage natbib Warning: Citation `jerzak2025' on page 2 undefined on input line\n 104.\n\n\nPackage natbib Warning: Citation `kim2025' on page 2 undefined on input line 10\n5.\n\n\nPackage natbib Warning: Citation `baumann2025' on page 2 undefined on input lin\ne 106.\n\n[2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 123.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 123.\n\n\nLaTeX Warning: Reference `tab:taxonomy-summary' on page 3 undefined on input li\nne 148.\n\n[3]\n\nLaTeX Warning: Reference `tab:theory-mc' on page 4 undefined on input line 183.\n\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nLaTeX Warning: Reference `tab:eigen' on page 4 undefined on input line 217.\n\n[4]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 224.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 224.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 224.\n\n\nLaTeX Warning: Reference `tab:binarization' on page 5 undefined on input line 2\n49.\n\n[5]\n\nLaTeX Warning: Reference `tab:asv-proof' on page 6 undefined on input line 292.\n\n\n\nLaTeX Warning: Reference `tab:asv-remaining' on page 6 undefined on input line \n321.\n\n[6]\n\nLaTeX Warning: Reference `tab:spectral' on page 7 undefined on input line 349.\n\n\nLaTeX Warning: Reference `tab:empirical-cm' on page 7 undefined on input line 4\n04.\n\n\nLaTeX Warning: Reference `tab:inter-model' on page 7 undefined on input line 40\n6.\n\n\nPackage natbib Warning: Citation `kim2025' on page 7 undefined on input line 40\n6.\n\n[7]\n\nLaTeX Warning: Reference `tab:downstream-bias' on page 8 undefined on input lin\ne 430.\n\n\nLaTeX Warning: Reference `tab:asv-empirical' on page 8 undefined on input line \n459.\n\n[8]\n\nLaTeX Warning: Reference `tab:correction-framework' on page 9 undefined on inpu\nt line 496.\n\n[9] [10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1440.60\n0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.\n600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm080\n0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1\n200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ect\nt1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e\ncbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec\n/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/\nec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe\nn/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn\nappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j\nknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/symbols/msbm10.pfb>\nOutput written on paper.pdf (11 pages, 294061 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/bm.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 123.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 123.\n\n[3]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 188.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 224.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 224.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 224.\n\n[4] [5] [6] [7] [8] [9] [10] [11] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1440.60\n0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.\n600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm080\n0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1\n200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ect\nt1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e\ncbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec\n/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/\nec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe\nn/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn\nappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j\nknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/symbols/msbm10.pfb>\nOutput written on paper.pdf (11 pages, 297993 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "48d89ff0-e3c0-40f1-9388-00ca38b5585a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attr…",
  "leafUuid": "27f3c793-3494-4896-b9bc-57e3f90caae8",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for annotation error study",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Assistant

_source line 32 · 2026-05-20T08:41:19.708Z_

<details><summary>Logged reasoning block</summary>

```text
There's a warning about labels changing, so I need to run pdflatex a third time to resolve cross-references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27f3c793-3494-4896-b9bc-57e3f90caae8",
  "isSidechain": false,
  "requestId": "req_011CbDXEwN9BHdV3ZVoqVA68",
  "type": "assistant",
  "uuid": "e222d037-ee32-4b6e-a34e-ed2de0523f9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hrt2aqTzZcJRnVtpxrBYEC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7891,
      "cache_read_input_tokens": 59781,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7891,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 59781,
          "cache_creation_input_tokens": 7891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7891
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

_source line 33 · 2026-05-20T08:41:20.186Z_

Cross-references need one more pass.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e222d037-ee32-4b6e-a34e-ed2de0523f9b",
  "isSidechain": false,
  "requestId": "req_011CbDXEwN9BHdV3ZVoqVA68",
  "type": "assistant",
  "uuid": "34c56793-755f-4b6c-b934-31b906a43c4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hrt2aqTzZcJRnVtpxrBYEC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7891,
      "cache_read_input_tokens": 59781,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7891,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 59781,
          "cache_creation_input_tokens": 7891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7891
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

_source line 34 · 2026-05-20T08:41:22.394Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WhUX27UnB8U89BVQchC3Pe`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third pdflatex pass for stable cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34c56793-755f-4b6c-b934-31b906a43c4c",
  "isSidechain": false,
  "requestId": "req_011CbDXEwN9BHdV3ZVoqVA68",
  "type": "assistant",
  "uuid": "94886873-b56d-4be2-a7ae-66c0f67b472a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hrt2aqTzZcJRnVtpxrBYEC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7891,
      "cache_read_input_tokens": 59781,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7891,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 59781,
          "cache_creation_input_tokens": 7891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7891
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

_source line 35 · 2026-05-20T08:41:22.960Z_

<details><summary>↩ Tool result · `toolu_01WhUX27UnB8U89BVQchC3Pe`</summary>

```text
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>
Output written on paper.pdf (11 pages, 297993 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94886873-b56d-4be2-a7ae-66c0f67b472a",
  "isSidechain": false,
  "promptId": "74990caf-6c19-4294-8631-731e236d5131",
  "type": "user",
  "uuid": "d046fa02-285f-45f1-b2b3-f4b0abb423ac",
  "toolUseResult": {
    "stdout": ">&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>\nOutput written on paper.pdf (11 pages, 297993 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "94886873-b56d-4be2-a7ae-66c0f67b472a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-20T08:41:22.965Z_

```json
{
  "parentUuid": "d046fa02-285f-45f1-b2b3-f4b0abb423ac",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6c73798d-8707-4083-ad4d-59e57c4cdf42",
  "timestamp": "2026-05-20T08:41:22.965Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 37 · 2026-05-20T08:41:28.838Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011e2LVPp2Rhx9rn43vhkVBF`</summary>

```json
{
  "command": "grep -c \"Warning\" paper.log | head -1 && ls -la paper.pdf",
  "description": "Check warnings count and PDF existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c73798d-8707-4083-ad4d-59e57c4cdf42",
  "isSidechain": false,
  "requestId": "req_011CbDXFSCypAhryEsUP7wBZ",
  "type": "assistant",
  "uuid": "1338bc00-01fe-40d3-978a-a8c46a487bd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DQyWjicuGvottm8RxaQGb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 67672,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 404,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 67672,
          "cache_creation_input_tokens": 404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 404
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

_source line 38 · 2026-05-20T08:41:28.910Z_

<details><summary>↩ Tool result · `toolu_011e2LVPp2Rhx9rn43vhkVBF`</summary>

```text
9
-rw-r--r-- 1 ubuntu ubuntu 297993 May 20 08:41 paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1338bc00-01fe-40d3-978a-a8c46a487bd0",
  "isSidechain": false,
  "promptId": "74990caf-6c19-4294-8631-731e236d5131",
  "type": "user",
  "uuid": "fb76965e-bc54-4b0a-a8ad-7493f3254b66",
  "toolUseResult": {
    "stdout": "9\n-rw-r--r-- 1 ubuntu ubuntu 297993 May 20 08:41 paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1338bc00-01fe-40d3-978a-a8c46a487bd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T08:41:41.815Z_

PDF 编译成功（11 页，298KB）。剩余 9 个 warnings 均为 hyperref 的 PDF bookmark 中 math mode token 警告，不影响内容。

论文覆盖了 `experiment_data.json` 中全部 8 个实验：

| 实验 | 对应章节/表格 |
|---|---|
| Six-topology bias taxonomy (K=3) | §3.2, Table 1 & 2 |
| General-K expressions (K=5,7) | §3.3, Table 3 |
| Binarization collapse | §3.4, Table 4 |
| ASV formal proofs (3 topologies) | §4.2, Table 5 |
| ASV MC validation (3 topologies) | §4.3, Table 6 |
| Empirical confusion matrices (3 LLMs × 3 tasks) | §5.1, Table 7 & 8 |
| ASV empirical calibration | §5.3, Table 10 |
| Correction guidance framework | §6, Table 11 |
| Spectral analysis | §4.4, Table 9 |
| annot-sensitivity toolkit | §7 |

所有定量数据来自 `experiment_data.json`，Version B framing（topology-dependent dichotomy）贯穿全文，Discussion 坦诚承认 collider ASV non-monotonicity、theory-MC gap、diagonal-dominant 经验矩阵等 worst 档限制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb76965e-bc54-4b0a-a8ad-7493f3254b66",
  "isSidechain": false,
  "requestId": "req_011CbDXFsaU1b9XFeaqyfKAU",
  "type": "assistant",
  "uuid": "fd09f36f-cd7b-4f83-b319-7a2977339dd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9EaCK69FW5ob3RgvBz2yj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 68076,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 136,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 394,
          "cache_read_input_tokens": 68076,
          "cache_creation_input_tokens": 136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 136
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attr…",
  "leafUuid": "fd09f36f-cd7b-4f83-b319-7a2977339dd9",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for annotation error study",
  "sessionId": "3c2c87c3-1a27-412c-9894-e2a083a5bf6f"
}
```

---
