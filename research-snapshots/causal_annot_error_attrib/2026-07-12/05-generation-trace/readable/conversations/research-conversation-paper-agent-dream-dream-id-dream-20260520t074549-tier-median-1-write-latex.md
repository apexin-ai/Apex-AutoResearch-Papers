# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/25bf0861-1839-4453-8613-912d152b4cb0.jsonl`
- **Structured JSON:** [`dd17b4fd32e042818270.json`](../../sessions/dd/dd17b4fd32e042818270.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T08:29:37.083Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T08:29:37.083Z",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Version A 成立但 scope 收窄至 2 个反转拓扑：exposure（MVP 已确认，violation rate 85%）+ mediation（plan_001 新发现，violation rate 23%，条件性反转——仅在 off-diagonal dominance > 0.6 且 |indirect effect| > 0.2 时触发）。\n其余 4 个拓扑（confounding, collider, M-bias, instrument, front-door）保持单调性，但 magnitude 变异显著（如 collider bias range 0.04–0.21）。\nLead finding 聚焦于 exposure vs mediation 的对比：exposure 反转是\"广泛性的\"（85%，几乎所有非对角 C），mediation 反转是\"条件性的\"（23%，需要双重门控）。这一对比本身就是核心贡献——同样的 non-differential error 在不同拓扑下产生质变差异。\nClaim 1 调整：taxonomy 有效，但方向反转是 topology-specific 而非 universal；magnitude 不可预测性作为补充论据（所有 6 个拓扑均存在）。\nClaim 2 调整：ASV 紧性降级为 2 个拓扑有形式化证明（confounding + mediation）+ 4 个有 MC 数值证据；增加一段讨论 collider conditioning structure 导致优化非凸的技术障碍。\nClaim 3 不变。\n需补充实验：(1) 对 exposure 和 mediation 做 C structure 条件分析（反转边界的精确刻画——何时反转、何时不反转），(2) 增加 1 个经验任务（如 emotion detection K=6）以补偿理论覆盖面的缩窄，使经验证据更丰富。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T08:29:37.087Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T08:29:37.087Z",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-20T08:29:37.126Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Version A 成立但 scope 收窄至 2 个反转拓扑：exposure（MVP 已确认，violation rate 85%）+ mediation（plan_001 新发现，violation rate 23%，条件性反转——仅在 off-diagonal dominance > 0.6 且 |indirect effect| > 0.2 时触发）。
其余 4 个拓扑（confounding, collider, M-bias, instrument, front-door）保持单调性，但 magnitude 变异显著（如 collider bias range 0.04–0.21）。
Lead finding 聚焦于 exposure vs mediation 的对比：exposure 反转是"广泛性的"（85%，几乎所有非对角 C），mediation 反转是"条件性的"（23%，需要双重门控）。这一对比本身就是核心贡献——同样的 non-differential error 在不同拓扑下产生质变差异。
Claim 1 调整：taxonomy 有效，但方向反转是 topology-specific 而非 universal；magnitude 不可预测性作为补充论据（所有 6 个拓扑均存在）。
Claim 2 调整：ASV 紧性降级为 2 个拓扑有形式化证明（confounding + mediation）+ 4 个有 MC 数值证据；增加一段讨论 collider conditioning structure 导致优化非凸的技术障碍。
Claim 3 不变。
需补充实验：(1) 对 exposure 和 mediation 做 C structure 条件分析（反转边界的精确刻画——何时反转、何时不反转），(2) 增加 1 个经验任务（如 emotion detection K=6）以补偿理论覆盖面的缩窄，使经验证据更丰富。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "78d7cdb9-6088-442c-9af5-ed1b31614a82",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T08:29:37.125Z_

```json
{
  "parentUuid": "78d7cdb9-6088-442c-9af5-ed1b31614a82",
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
  "uuid": "00c45080-5c69-4282-b0a7-a5c1ee779d42",
  "timestamp": "2026-05-20T08:29:37.125Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T08:29:37.125Z_

```json
{
  "parentUuid": "00c45080-5c69-4282-b0a7-a5c1ee779d42",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2db1f187-c9e3-4673-bc38-72a526e60c80",
  "timestamp": "2026-05-20T08:29:37.125Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
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
  "aiTitle": "Generate simulated research paper with causal annotation analysis",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---

### Assistant

_source line 7 · 2026-05-20T08:29:40.354Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2db1f187-c9e3-4673-bc38-72a526e60c80",
  "isSidechain": false,
  "requestId": "req_011CbDWMQXpjvT78Fn7wiD6J",
  "type": "assistant",
  "uuid": "fadce6b1-516d-43e3-9533-21fb790a31e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVqKYbBC8QTrhmWzKBCDKS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12029,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12029,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12029
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

_source line 8 · 2026-05-20T08:29:41.420Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FbvQDfciawY8Gtaa6ukELt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fadce6b1-516d-43e3-9533-21fb790a31e5",
  "isSidechain": false,
  "requestId": "req_011CbDWMQXpjvT78Fn7wiD6J",
  "type": "assistant",
  "uuid": "70889562-b748-4584-8f67-19be7a5b1da5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVqKYbBC8QTrhmWzKBCDKS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12029,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12029,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12029
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

_source line 9 · 2026-05-20T08:29:41.691Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G63BGcBSV4o7q4UjTXE76r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70889562-b748-4584-8f67-19be7a5b1da5",
  "isSidechain": false,
  "requestId": "req_011CbDWMQXpjvT78Fn7wiD6J",
  "type": "assistant",
  "uuid": "a8f1ab6c-f62b-4719-8375-d016831c8961",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVqKYbBC8QTrhmWzKBCDKS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12029,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12029,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12029
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

_source line 10 · 2026-05-20T08:29:41.747Z_

<details><summary>↩ Tool result · `toolu_01FbvQDfciawY8Gtaa6ukELt`</summary>

```text
1	[
2	  {
3	    "name": "K=3 Bias Expressions and MC Validation Across 6 DAG Topologies",
4	    "description": "对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）推导 K=3 closed-form bias 表达式，\nMC 验证：1000 reps × N=10000 × 6 confusion matrix structures/topology = 36 scenarios。\n每个拓扑做 100k random C search 检测方向反转。Confounding 为 MVP 再验证；其余 5 个为新推导。\n结合 MVP exposure 结果，total reversal topologies = 2。\n",
5	    "results": {
6	      "total_scenarios": 36,
7	      "theory_mc_match": "33/36",
8	      "theory_mc_match_rate": 0.917,
9	      "reversal_in_plan_001": 1,
10	      "reversal_topology_new": "mediation",
11	      "combined_reversal_topologies": 2,
12	      "combined_reversal_list": [
13	        "exposure (MVP)",
14	        "mediation (new)"
15	      ],
16	      "confounding": {
17	        "violation_rate": 0.0,
18	        "bias_range": [
19	          0.132,
20	          0.298
21	        ],
22	        "theory_mc": "6/6",
23	        "mechanism": "residual confounding, monotonic toward OVB"
24	      },
25	      "mediation": {
26	        "violation_rate": 0.23,
27	        "sign_reversal_rate": 0.18,
28	        "amplification_rate": 0.05,
29	        "worst_severity": 1.62,
30	        "named_structures_with_violation": "2/6 (near-permutation, block-off-diagonal)",
31	        "theory_mc": "6/6",
32	        "reversal_condition": "off-diagonal dominance > 0.6 AND |indirect effect| > 0.2",
33	        "indirect_bias_range": [
34	          -0.18,
35	          0.14
36	        ]
37	      },
38	      "collider": {
39	        "violation_rate": 0.0,
40	        "bias_range": [
41	          0.04,
42	          0.21
43	        ],
44	        "attenuation_range": "15-60% reduction vs no misclassification",
45	        "theory_mc": "5/6",
46	        "mechanism": "misclassification smooths conditioning variable, reduces collider bias magnitude, preserves direction"
47	      },
48	      "mbias": {
49	        "violation_rate": 0.0,
50	        "bias_range": [
51	          0.02,
52	          0.16
53	        ],
54	        "theory_mc": "5/6",
55	        "mechanism": "spurious pathway weakened by misclassification of M-bias variable"
56	      },
57	      "instrument": {
58	        "violation_rate": 0.0,
59	        "bias_range": [
60	          0.03,
61	          0.19
62	        ],
63	        "theory_mc": "6/6",
64	        "mechanism": "instrument weakened, Wald estimator biased toward OLS, direction preserved"
65	      },
66	      "frontdoor": {
67	        "violation_rate": 0.0,
68	        "bias_range": [
69	          0.05,
70	          0.22
71	        ],
72	        "theory_mc": "5/6",
73	        "mechanism": "front-door estimate attenuated, identification weakened but direction stable"
74	      },
75	      "mc_mismatch_detail": "3 mismatches in collider(1), M-bias(1), front-door(1) — all near-permutation C where MC variance is highest due to complex bias formulas (conditioning, ratio estimators)"
76	    },
77	    "tables": [
78	      {
79	        "name": "Direction Reversal Summary by Topology (plan_001 + MVP exposure)",
80	        "columns": [
81	          "topology",
82	          "misclassified_var",
83	          "violation_rate",
84	          "sign_reversal",
85	          "worst_severity",
86	          "theory_mc",
87	          "direction"
88	        ],
89	        "rows": [
90	          [
91	            "exposure (MVP)",
92	            "treatment X",
93	            0.85,
94	            0.834,
95	            2.83,
96	            "5/5",
97	            "reversal-dominant"
98	          ],
99	          [
100	            "confounding",
101	            "confounder U",
102	            0.0,
103	            0.0,
104	            "1.00×OVB",
105	            "6/6",
106	            "monotonic toward OVB"
107	          ],
108	          [
109	            "mediation",
110	            "mediator M",
111	            0.23,
112	            0.18,
113	            1.62,
114	            "6/6",
115	            "conditional reversal"
116	          ],
117	          [
118	            "collider",
119	            "collider Z",
120	            0.0,
121	            0.0,
122	            "0.85×(attenuated)",
123	            "5/6",
124	            "monotonic attenuation"
125	          ],
126	          [
127	            "M-bias",
128	            "M-bias var",
129	            0.0,
130	            0.0,
131	            "0.92×(attenuated)",
132	            "5/6",
133	            "monotonic attenuation"
134	          ],
135	          [
136	            "instrument",
137	            "instrument Z",
138	            0.0,
139	            0.0,
140	            "0.78×(toward OLS)",
141	            "6/6",
142	            "monotonic toward OLS"
143	          ],
144	          [
145	            "front-door",
146	            "front-door M",
147	            0.0,
148	            0.0,
149	            "0.88×(attenuated)",
150	            "5/6",
151	            "monotonic attenuation"
152	          ]
153	        ]
154	      },
155	      {
156	        "name": "Mediation Reversal Conditions (100k Random C, K=3)",
157	        "columns": [
158	          "C_structure_category",
159	          "pct_of_random_C",
160	          "violation_rate",
161	          "sign_reversal_rate"
162	        ],
163	        "rows": [
164	          [
165	            "near-permutation (off-diag dom > 0.6)",
166	            "30%",
167	            0.57,
168	            0.44
169	          ],
170	          [
171	            "moderate (off-diag dom 0.3–0.6)",
172	            "40%",
173	            0.14,
174	            0.09
175	          ],
176	          [
177	            "diagonal-dominant (off-diag dom < 0.3)",
178	            "30%",
179	            0.0,
180	            0.0
181	          ],
182	          [
183	            "overall",
184	            "100%",
185	            0.23,
186	            0.18
187	          ]
188	        ]
189	      }
190	    ],
191	    "figures": [],
192	    "analysis": "plan_001 确认 median 档的核心结果：6 个拓扑中仅 mediation 出现新的反转（结合 MVP exposure = 2 个反转拓扑）。\n关键发现是反转机制的不对称性：exposure 是\"广泛性反转\"（label swap 直接作用于 treatment 对比），\nmediation 是\"条件性反转\"（需双重门控：C 足够非对角 + 间接效应足够大）。\n这一不对称性本身就是论文的核心贡献——它证明了 direction reversal 是 topology-specific 的，\n不能仅从 confusion matrix 结构预测，必须结合 DAG 拓扑分析。\n4 个单调拓扑的 magnitude 变异（如 collider 0.04–0.21）支持补充论据：即使方向保持，\nbias magnitude 仍不可从 binary 框架预测。\n需要补充实验：对 mediation 的 phase diagram 做更精细的 grid search（Fig 3 的分辨率不够用于实用指导）。\n\n\nMediation（23% violation）：misclassifying mediator M 影响间接路径 X→M→Y。反转需要双重门控：\n(a) C matrix off-diagonal dominance > 0.6（标签大幅置换），AND (b) |true indirect effect| > 0.2（间接效应足够大可以被反转）。\n因为间接效应 = X→M 系数 × M→Y 系数的乘积，两条路径都必须被实质性扰动才能反转——这种双重门控将 violation rate 限制在 23%。\n对比 exposure（MVP 85% violation）：exposure misclassification 直接作用于单一 X→Y 路径，无衰减机制，几乎所有非对角 C 都触发反转。\n这一机制差异（直接路径 vs 乘积路径）是 median 档的核心发现——direction reversal 是 topology-specific 的。\n\nCollider（0% violation）：misclassifying Z（collider）并 conditioning on Z* 时，误分类平滑了 Z 的分布，\n削弱了 selection effect 的强度但不改变其方向。方向由结构方程的符号决定（与测量质量无关）。\n100k random C 中无一例外。\n\nM-bias/Instrument/Front-door（0% violation）：这些拓扑涉及辅助变量，misclassification 削弱 identification 但不反转估计方向。\nInstrument 特殊之处在于 Wald estimator 的分母受影响（偏向 OLS），但符号不变。\nFront-door 的 double summation 使 MC 方差在极端 C 下偏高，导致 1/6 mismatch。\n\n3 个 MC mismatch 均出现在 near-permutation C structure 下——这些拓扑的 bias formula 含有 conditioning 或 ratio 结构，\nMC 在极端 C 下方差更大，理论值落在 95% CI 边缘外。\n"
193	  },
194	  {
195	    "name": "General-K Matrix Bias Expressions and Interpretability Tools",
196	    "description": "将 bias 表达式扩展到 K=5,7 的矩阵形式。开发 3 个可解释性工具：\n(a) eigendecomposition summaries，(b) worst-case scalar bounds，(c) diagnostic visualizations。\n在 confounding + mediation + collider + exposure DAGs 上验证 K=5,7。\n",
197	    "results": {
198	      "K5_theory_mc_match_rate": 0.89,
199	      "K7_theory_mc_match_rate": 0.85,
200	      "K5_scenarios_tested": 24,
201	      "K7_scenarios_tested": 24,
202	      "eigendecomp_variance_explained_top2_K5": {
203	        "confounding": 0.87,
204	        "exposure": 0.91,
205	        "mediation": 0.83,
206	        "collider": 0.88
207	      },
208	      "eigendecomp_variance_explained_top3_K7": {
209	        "confounding": 0.84,
210	        "exposure": 0.88,
211	        "mediation": 0.8,
212	        "collider": 0.85
213	      },
214	      "worst_case_bound_conservatism_median": "2.6×",
215	      "worst_case_bound_conservatism_range": "2.1–3.4×",
216	      "K5_exposure_violation_rate": 0.88,
217	      "K5_mediation_violation_rate": 0.28,
218	      "K7_exposure_violation_rate": 0.9,
219	      "K7_mediation_violation_rate": 0.31,
220	      "reversal_pattern_persistence": true,
221	      "dominant_eigenmode_interpretation": {
222	        "mode_1": "diagonal dominance deviation (how far C is from identity)",
223	        "mode_2": "permutation component (which off-diagonal entries dominate)"
224	      }
225	    },
226	    "tables": [
227	      {
228	        "name": "Eigendecomposition: Variance Explained by Top Modes",
229	        "columns": [
230	          "topology",
231	          "K",
232	          "mode_1",
233	          "mode_2",
234	          "mode_3",
235	          "cumulative_top2",
236	          "cumulative_top3"
237	        ],
238	        "rows": [
239	          [
240	            "confounding",
241	            5,
242	            0.68,
243	            0.19,
244	            0.08,
245	            0.87,
246	            0.95
247	          ],
248	          [
249	            "confounding",
250	            7,
251	            0.59,
252	            0.17,
253	            0.08,
254	            0.76,
255	            0.84
256	          ],
257	          [
258	            "exposure",
259	            5,
260	            0.74,
261	            0.17,
262	            0.05,
263	            0.91,
264	            0.96
265	          ],
266	          [
267	            "exposure",
268	            7,
269	            0.65,
270	            0.15,
271	            0.08,
272	            0.8,
273	            0.88
274	          ],
275	          [
276	            "mediation",
277	            5,
278	            0.61,
279	            0.22,
280	            0.09,
281	            0.83,
282	            0.92
283	          ],
284	          [
285	            "mediation",
286	            7,
287	            0.52,
288	            0.19,
289	            0.09,
290	            0.71,
291	            0.8
292	          ],
293	          [
294	            "collider",
295	            5,
296	            0.7,
297	            0.18,
298	            0.06,
299	            0.88,
300	            0.94
301	          ],
302	          [
303	            "collider",
304	            7,
305	            0.62,
306	            0.16,
307	            0.07,
308	            0.78,
309	            0.85
310	          ]
311	        ]
312	      },
313	      {
314	        "name": "Violation Rate Scaling with K",
315	        "columns": [
316	          "topology",
317	          "K=3",
318	          "K=5",
319	          "K=7",
320	          "trend"
321	        ],
322	        "rows": [
323	          [
324	            "exposure",
325	            0.85,
326	            0.88,
327	            0.9,
328	            "near saturation"
329	          ],
330	          [
331	            "mediation",
332	            0.23,
333	            0.28,
334	            0.31,
335	            "monotonic increase"
336	          ],
337	          [
338	            "confounding",
339	            0.0,
340	            0.0,
341	            0.0,
342	            "flat (monotonic)"
343	          ],
344	          [
345	            "collider",
346	            0.0,
347	            0.0,
348	            0.0,
349	            "flat (monotonic)"
350	          ]
351	        ]
352	      }
353	    ],
354	    "figures": [],
355	    "analysis": "Matrix-form 表达式成功泛化 K=3 结果。实用发现：top 2 eigenmodes 在 K≤5 下足够（>83% 方差解释），\nK=7 可能需要 3 个 modes。这指导 toolkit 设计——默认 2-mode summary 加可选扩展。\nReversal patterns 在 K=5,7 持续，确认 K=3 理论分析不是 special case。\nWorst-case bounds 的保守性（2.6×）是 tradeoff：tight bounds 需要 topology-specific 优化（随 K 扩展性差），\nconservative bounds 计算快且作为安全边界仍有实用价值。\n\n\nK=5,7 的 match rate 低于 K=3（0.89/0.85 vs 0.917）因为 MC 方差随 C 的自由参数数 K(K-1) 增长——K=5 有 20 个自由参数，K=7 有 42 个，\n相同 MC replications 下 confidence interval 更宽。\n\nEigendecomposition 的 top 2 modes 能解释 83–91% 方差，因为实际 confusion matrix 具有低有效秩结构：\n主导误差模式是\"相邻类别混淆\"（语义相似的类别被混淆），产生带对角扰动结构，被 2–3 个 eigenmodes 良好捕获。\nMediation 的方差解释率略低（0.83 K=5）因为间接效应涉及乘积，放大了二阶 eigenmode 的贡献。\n\nWorst-case bounds 保守（median 2.6×）因为它们对给定 diagonal dominance 下所有 C 做极值优化，\n包括实际罕见的对抗性配置。作为安全边界是可接受的——类似 E-values 的保守性。\n\nViolation rates 随 K 轻微上升（mediation 23% → 28% → 31%）因为更大的 K 增加了 off-diagonal confusion 路径，\n使 label permutation 更可能。Exposure 接近饱和（85% → 88% → 90%）。\n"
356	  },
357	  {
358	    "name": "Empirical Confusion Matrices: 3 LLMs × 3 CSS Tasks",
359	    "description": "从 Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4 收集经验 confusion matrices。\n3 个 CSS 任务：protest event coding (K=5, ACLED), stance detection (K=3, SemEval/VAST), toxicity (K=2, Civil Comments)。\n~30K annotations/model × 3 tasks × 3 prompt variants = ~270K total annotations。\n",
360	    "results": {
361	      "api_cost_actual": "$420",
362	      "total_annotations": 270000,
363	      "protest_K5": {
364	        "llama4_macro_f1": 0.71,
365	        "llama4_accuracy": 0.74,
366	        "qwen35_macro_f1": 0.68,
367	        "qwen35_accuracy": 0.71,
368	        "deepseek_macro_f1": 0.73,
369	        "deepseek_accuracy": 0.76,
370	        "inter_model_error_agreement": 0.58,
371	        "downstream_bias_range_abs": [
372	          0.05,
373	          0.12
374	        ],
375	        "dominant_error_pattern": "adjacent-category confusion (riot↔protest, strategic↔organized)"
376	      },
377	      "stance_K3": {
378	        "llama4_macro_f1": 0.76,
379	        "llama4_accuracy": 0.79,
380	        "qwen35_macro_f1": 0.74,
381	        "qwen35_accuracy": 0.77,
382	        "deepseek_macro_f1": 0.78,
383	        "deepseek_accuracy": 0.81,
384	        "inter_model_error_agreement": 0.62,
385	        "downstream_bias_range_abs": [
386	          0.03,
387	          0.08
388	        ],
389	        "dominant_error_pattern": "neutral-as-default bias (favor→neutral, against→neutral)"
390	      },
391	      "toxicity_K2": {
392	        "llama4_f1": 0.88,
393	        "llama4_accuracy": 0.9,
394	        "qwen35_f1": 0.86,
395	        "qwen35_accuracy": 0.88,
396	        "deepseek_f1": 0.89,
397	        "deepseek_accuracy": 0.91,
398	        "inter_model_error_agreement": 0.64,
399	        "downstream_bias_range_abs": [
400	          0.01,
401	          0.04
402	        ],
403	        "dominant_error_pattern": "slight FN bias (under-flagging toxicity)"
404	      },
405	      "prompt_variant_stability": "macro-F1 varies ±0.03; confusion matrix structure stable across prompts",
406	      "cross_model_error_correlation_mean": 0.61
407	    },
408	    "tables": [
409	      {
410	        "name": "Empirical Performance Summary",
411	        "columns": [
412	          "task",
413	          "K",
414	          "model",
415	          "macro_F1",
416	          "accuracy",
417	          "dominant_error"
418	        ],
419	        "rows": [
420	          [
421	            "protest",
422	            5,
423	            "Llama 4 Maverick",
424	            0.71,
425	            0.74,
426	            "riot↔protest (0.15)"
427	          ],
428	          [
429	            "protest",
430	            5,
431	            "Qwen 3.5 Plus",
432	            0.68,
433	            0.71,
434	            "riot↔protest (0.18), remote↔organized (0.12)"
435	          ],
436	          [
437	            "protest",
438	            5,
439	            "DeepSeek V4",
440	            0.73,
441	            0.76,
442	            "riot↔protest (0.13)"
443	          ],
444	          [
445	            "stance",
446	            3,
447	            "Llama 4 Maverick",
448	            0.76,
449	            0.79,
450	            "favor→neutral (0.18)"
451	          ],
452	          [
453	            "stance",
454	            3,
455	            "Qwen 3.5 Plus",
456	            0.74,
457	            0.77,
458	            "favor→neutral (0.21), against→neutral (0.14)"
459	          ],
460	          [
461	            "stance",
462	            3,
463	            "DeepSeek V4",
464	            0.78,
465	            0.81,
466	            "favor→neutral (0.15)"
467	          ],
468	          [
469	            "toxicity",
470	            2,
471	            "Llama 4 Maverick",
472	            0.88,
473	            0.9,
474	            "FN toxic→non-toxic (0.12)"
475	          ],
476	          [
477	            "toxicity",
478	            2,
479	            "Qwen 3.5 Plus",
480	            0.86,
481	            0.88,
482	            "FN toxic→non-toxic (0.14)"
483	          ],
484	          [
485	            "toxicity",
486	            2,
487	            "DeepSeek V4",
488	            0.89,
489	            0.91,
490	            "FN toxic→non-toxic (0.10)"
491	          ]
492	        ]
493	      },
494	      {
495	        "name": "Inter-Model Error Correlation",
496	        "columns": [
497	          "task",
498	          "model_pair",
499	          "error_agreement_when_both_err",
500	          "kappa_on_errors"
501	        ],
502	        "rows": [
503	          [
504	            "protest",
505	            "Llama4–Qwen35",
506	            0.56,
507	            0.31
508	          ],
509	          [
510	            "protest",
511	            "Llama4–DeepSeek",
512	            0.61,
513	            0.38
514	          ],
515	          [
516	            "protest",
517	            "Qwen35–DeepSeek",
518	            0.57,
519	            0.33
520	          ],
521	          [
522	            "stance",
523	            "Llama4–Qwen35",
524	            0.6,
525	            0.35
526	          ],
527	          [
528	            "stance",
529	            "Llama4–DeepSeek",
530	            0.64,
531	            0.41
532	          ],
533	          [
534	            "stance",
535	            "Qwen35–DeepSeek",
536	            0.62,
537	            0.37
538	          ],
539	          [
540	            "toxicity",
541	            "Llama4–Qwen35",
542	            0.63,
543	            0.39
544	          ],
545	          [
546	            "toxicity",
547	            "Llama4–DeepSeek",
548	            0.66,
549	            0.44
550	          ],
551	          [
552	            "toxicity",
553	            "Qwen35–DeepSeek",
554	            0.64,
555	            0.41
556	          ]
557	        ]
558	      }
559	    ],
560	    "figures": [],
561	    "analysis": "经验 confusion matrices 确认真实 LLMs 产生 moderately diagonal-dominant 的 C matrix——\n远离 near-permutation 极端但有足够 off-diagonal mass 产生可检测的 downstream bias。\n关键经验发现：C structure 是 task-dependent（adjacent-category for protest，neutral-absorbing for stance）\n且 model-stable（同一 task 下 3 个模型展示相似结构模式）。\n这意味着理论 taxonomy 的 per-topology 预测适用于真实 LLM 场景——C structure 可从 task 预测，不取决于模型选择。\nInter-model error correlation 直接支持论文 framing：ensembles 无法修复系统性误差。\n\n\n性能水平反映 2025–2026 LLMs 在 CSS 任务上的典型表现：K=5 protest coding 最难（事件类型间区分微妙），\nK=3 stance 中等（neutral 类别歧义性高），K=2 toxicity 最易（信号明确）。\n\nInter-model error agreement（0.58–0.64）与 Kim et al.（ICML 2025）报告的 ~60% 一致。\nToxicity 略高因为 binary task 出错方式更少。\n这验证了论文的动机前提：LLM errors are correlated，ensemble averaging 效果有限。\n\nDownstream bias 范围是中等的（非 dramatic）因为真实 LLM confusion matrices 是 moderately diagonal-dominant 的——\n不是 near-permutation 极端。这是 median 档的预期：理论极端（near-permutation C 导致 2.83× severity）\n在当前 LLMs 中不会实际出现，但 bias 是可检测的且非 trivial 的。\n\nPrompt variant 稳定性（±0.03 F1，C structure stable）支持论文聚焦于 confusion matrix structure 而非 prompt engineering——\nerror 的结构模式对 prompting 鲁棒，即使边际性能有移动。\n"
562	  },
563	  {
564	    "name": "Binarization Collapse Analysis Across 6 Topologies",
565	    "description": "对 6 个拓扑在 K=3,5,7 下：将 K-class 变量折叠为 binary，\n比较 full multi-class bias expression vs binarized expression。\n评估何时 binarization 安全、何时危险。\n",
566	    "results": {
567	      "max_delta_overall": 0.13,
568	      "max_delta_by_K": {
569	        "K3": 0.103,
570	        "K5": 0.13,
571	        "K7": 0.13
572	      },
573	      "worst_delta_topology": "mediation (K=5)",
574	      "binarization_direction_reversal_topologies": [
575	        "exposure",
576	        "mediation"
577	      ],
578	      "safe_binarization_topologies": [
579	        "collider",
580	        "M-bias",
581	        "instrument"
582	      ],
583	      "lossy_but_direction_safe": [
584	        "confounding",
585	        "front-door"
586	      ],
587	      "delta_by_topology_K3": {
588	        "confounding": 0.103,
589	        "mediation": 0.09,
590	        "collider": 0.07,
591	        "mbias": 0.06,
592	        "instrument": 0.05,
593	        "frontdoor": 0.08
594	      },
595	      "delta_by_topology_K5": {
596	        "confounding": 0.11,
597	        "mediation": 0.13,
598	        "collider": 0.09,
599	        "mbias": 0.08,
600	        "instrument": 0.06,
601	        "frontdoor": 0.09
602	      }
603	    },
604	    "tables": [
605	      {
606	        "name": "Binarization Delta Summary",
607	        "columns": [
608	          "topology",
609	          "K",
610	          "max_delta",
611	          "direction_reversal_from_binarization",
612	          "safety_class"
613	        ],
614	        "rows": [
615	          [
616	            "confounding",
617	            3,
618	            0.103,
619	            false,
620	            "direction-safe, magnitude-unsafe"
621	          ],
622	          [
623	            "confounding",
624	            5,
625	            0.11,
626	            false,
627	            "direction-safe, magnitude-unsafe"
628	          ],
629	          [
630	            "mediation",
631	            3,
632	            0.09,
633	            true,
634	            "unsafe"
635	          ],
636	          [
637	            "mediation",
638	            5,
639	            0.13,
640	            true,
641	            "unsafe"
642	          ],
643	          [
644	            "exposure (ref)",
645	            3,
646	            0.09,
647	            true,
648	            "unsafe"
649	          ],
650	          [
651	            "exposure (ref)",
652	            5,
653	            0.1,
654	            true,
655	            "unsafe"
656	          ],
657	          [
658	            "collider",
659	            3,
660	            0.07,
661	            false,
662	            "safe"
663	          ],
664	          [
665	            "collider",
666	            5,
667	            0.09,
668	            false,
669	            "safe"
670	          ],
671	          [
672	            "M-bias",
673	            3,
674	            0.06,
675	            false,
676	            "safe"
677	          ],
678	          [
679	            "instrument",
680	            3,
681	            0.05,
682	            false,
683	            "safe"
684	          ],
685	          [
686	            "front-door",
687	            3,
688	            0.08,
689	            false,
690	            "direction-safe, magnitude-marginal"
691	          ]
692	        ]
693	      }
694	    ],
695	    "figures": [],
696	    "analysis": "Binarization 不是逃离 K≥3 复杂性的安全手段。Max delta 0.13（mediation K=5）在典型 CSS 回归中\n（effect size 0.1–0.5）足以主导估计。\n拓扑分三组：(1) binarization-unsafe（exposure, mediation——可能反转方向），\n(2) binarization-lossy（confounding, front-door——保持方向但损失量级精度），\n(3) binarization-tolerable（collider, M-bias, instrument——delta 小，安全）。\n这支持论文的 multi-class treatment is necessary 论点。\n\n\nBinarization delta 在 K=5 达到峰值（0.13）并在 K=7 持平，因为 K→2 的信息损失在 K=5–7 饱和——\n超过 K=7 后额外类别的边际信息递减。\n\nMediation 的 delta 最大（K=5 时 0.13）因为 binarizing mediator M 将间接路径折叠为单一对比，\n丢失了 multi-class expression 捕获的 category-specific indirect effects。\n对 exposure 和 mediation，某些 binarization folding 产生方向反转：\n将 category 1+2 vs 3 折叠可能将相反方向的效应分配到同一 binary class。\n\nConfounding delta 高（K=3 0.103，来自 MVP）因为 binarizing confounder 丢失了残差混杂控制。\n但方向保持（direction-safe, magnitude-unsafe）。\n\nCollider/M-bias/instrument delta 较小因为这些拓扑涉及辅助变量，\nbinary 近似更接近 multi-class truth——关键量（induced bias direction）更依赖 conditioning operation 而非变量粒度。\n"
697	  },
698	  {
699	    "name": "ASV Framework: Formal Proofs for Confounding, Mediation, Collider",
700	    "description": "推导 3 个优先拓扑的 ASV 表达式。形式化证明 monotonicity 和 sharpness。\nMC 验证：coverage at 90%, 95%, 99% across 1000 scenarios/topology。\n",
701	    "results": {
702	      "monotonicity_proved": [
703	        "confounding",
704	        "mediation",
705	        "collider"
706	      ],
707	      "sharpness_proved": [
708	        "confounding",
709	        "mediation"
710	      ],
711	      "sharpness_incomplete": [
712	        "collider"
713	      ],
714	      "sharpness_formal_proofs_count": 2,
715	      "collider_sharpness_numerical": "achieving 93% of bound in 10k optimization runs",
716	      "coverage_at_95_nominal": {
717	        "confounding": 0.93,
718	        "mediation": 0.9,
719	        "collider": 0.91
720	      },
721	      "coverage_at_90_nominal": {
722	        "confounding": 0.95,
723	        "mediation": 0.92,
724	        "collider": 0.93
725	      },
726	      "coverage_at_99_nominal": {
727	        "confounding": 0.97,
728	        "mediation": 0.96,
729	        "collider": 0.95
730	      },
731	      "average_coverage_95": 0.913
732	    },
733	    "tables": [
734	      {
735	        "name": "ASV Proof Status and Coverage (Priority Topologies)",
736	        "columns": [
737	          "topology",
738	          "monotonicity",
739	          "sharpness",
740	          "coverage_90",
741	          "coverage_95",
742	          "coverage_99"
743	        ],
744	        "rows": [
745	          [
746	            "confounding",
747	            "formal proof",
748	            "formal proof",
749	            0.95,
750	            0.93,
751	            0.97
752	          ],
753	          [
754	            "mediation",
755	            "formal proof",
756	            "formal proof",
757	            0.92,
758	            0.9,
759	            0.96
760	          ],
761	          [
762	            "collider",
763	            "formal proof",
764	            "numerical only (93%)",
765	            0.93,
766	            0.91,
767	            0.95
768	          ]
769	        ]
770	      }
771	    ],
772	    "figures": [],
773	    "analysis": "ASV 框架在 3 个优先拓扑上验证：monotonicity universally proved，sharpness 2/3 proved。\nCollider sharpness gap（7%）是主要技术障碍——论文应增加一段讨论 conditioning-on-misclassified-variable 导致的非凸优化问题，\n并标记 convex relaxation approach 为 future work。\nMediation 的更陡 ASV 曲线意味着 mediation DAGs 的结论对 annotation error 更敏感——\n与 direction reversal 发现一致，自然连接 Claim 1 和 Claim 2。\n\n\nMonotonicity 对所有 3 个拓扑成立（proved）因为：更大的 δ 意味着 sensitivity set 中考虑更极端的 C →\noverturn conclusion 所需的 minimum perturbation 只能增加或不变。\n这与 underlying bias 是否单调无关——ASV 是 min-over-C 量，不是 pointwise bias。\n\nConfounding sharpness：bias 在 C 的 off-diagonal elements 上是线性的，supremum 有 clean convex structure，\nsharpness-achieving C 在 feasible set 的顶点。构造性证明。\n\nMediation sharpness：尽管存在方向反转，ASV sharpness 仍可证——通过分别分析 attenuation regime 和 reversal regime。\nReversal boundary 处的 worst-case C 恰好达到 bound——构造性证明利用 phase transition 结构。\n这是一个 nice 的结果：有反转的拓扑仍然有 tight bound，加强了 ASV 框架的可信度。\n\nCollider sharpness INCOMPLETE：bias 表达式涉及 conditioning on misclassified Z，\n产生 E[Y|X,Z*] = Σ_z P(Z=z|Z*) E[Y|X,Z=z]。\n对 C 做 supremum 要求联合优化 P(Z=z|Z*)，subject to C 为 valid confusion matrix，\n产生非凸 bilinear 约束。数值优化达到 analytical bound 的 93%，强烈暗示 sharpness，\n但形式化证明 supremum is attained 被 feasible set 的非凸拓扑阻断。\n\nCoverage 略低于 nominal（average 91.3% at 95% nominal）因为 ASV bounds 在已知 exact C 下推导，\n而 MC 用的是有限样本估计的 C。Gap（3.7%）反映估计不确定性而非 bound failure。\n"
774	  },
775	  {
776	    "name": "ASV MC Validation for M-bias, Instrument, Front-door",
777	    "description": "推导剩余 3 个拓扑的 ASV 表达式 + MC 验证。\nMonotonicity 和 coverage 验证。Sharpness 作为 conjectures + numerical evidence。\n",
778	    "results": {
779	      "monotonicity_holds": [
780	        "M-bias",
781	        "instrument",
782	        "front-door"
783	      ],
784	      "monotonicity_failures": 0,
785	      "sharpness_numerical": {
786	        "mbias": "achieving 92% of bound",
787	        "instrument": "achieving 89% of bound",
788	        "frontdoor": "achieving 94% of bound"
789	      },
790	      "coverage_at_95_nominal": {
791	        "mbias": 0.9,
792	        "instrument": 0.89,
793	        "frontdoor": 0.91
794	      },
795	      "instrument_conservatism": "ASV bounds 1.8× wider than necessary",
796	      "total_asv_coverage_6_topologies": 0.907
797	    },
798	    "tables": [
799	      {
800	        "name": "ASV Results for Secondary Topologies",
801	        "columns": [
802	          "topology",
803	          "monotonicity",
804	          "sharpness_numerical_pct",
805	          "coverage_95",
806	          "conservatism"
807	        ],
808	        "rows": [
809	          [
810	            "M-bias",
811	            "holds",
812	            "92%",
813	            0.9,
814	            "comparable to collider"
815	          ],
816	          [
817	            "instrument",
818	            "holds",
819	            "89%",
820	            0.89,
821	            "1.8× conservative (Wald ratio)"
822	          ],
823	          [
824	            "front-door",
825	            "holds",
826	            "94%",
827	            0.91,
828	            "near-tight"
829	          ]
830	        ]
831	      },
832	      {
833	        "name": "All 6 Topologies ASV Summary",
834	        "columns": [
835	          "topology",
836	          "monotonicity",
837	          "sharpness_status",
838	          "coverage_95"
839	        ],
840	        "rows": [
841	          [
842	            "confounding",
843	            "proved",
844	            "proved (formal)",
845	            0.93
846	          ],
847	          [
848	            "mediation",
849	            "proved",
850	            "proved (formal)",
851	            0.9
852	          ],
853	          [
854	            "collider",
855	            "proved",
856	            "93% numerical",
857	            0.91
858	          ],
859	          [
860	            "M-bias",
861	            "proved",
862	            "92% numerical",
863	            0.9
864	          ],
865	          [
866	            "instrument",
867	            "proved",
868	            "89% numerical",
869	            0.89
870	          ],
871	          [
872	            "front-door",
873	            "proved",
874	            "94% numerical",
875	            0.91
876	          ]
877	        ]
878	      }
879	    ],
880	    "figures": [],
881	    "analysis": "6 个拓扑全部有 ASV 表达式 + validated monotonicity。Sharpness landscape：\n2 proved (confounding, mediation) + 4 numerical (collider 93%, front-door 94%, M-bias 92%, instrument 89%)。\nInstrument 是最弱环节——ASV 保守性限制了实用性。论文应诚实讨论并标记 tighter instrument-specific bounds 为 future work。\nOverall average 95%-nominal coverage = 0.907，在 median 档 [0.88, 0.93] 范围内。\n\n\nMonotonicity 对所有 3 个拓扑成立——与 plan_004 相同的结构性论证：\nASV 是 minimum-over-perturbation 量，在 perturbation budget δ 中固有单调。\n\nSharpness numerical evidence 有差异：front-door 最接近 tight（94%，identification structure 较简单），\nM-bias 中等（92%），instrument 最远（89%）。\nInstrument gap 反映 Wald estimator 的 ratio structure——supremum 涉及优化 misclassified 量的 ratio，\nlandscape 有多个 local optima。\n\nInstrument ASV 显著保守（1.8× wider）因为 Wald estimator 放大小分母扰动，\nworst-case bound 比 typical case 差很多。这是 IV sensitivity analysis 的已知问题（非本框架特有）。\n"
882	  },
883	  {
884	    "name": "ASV Calibration on Empirical Data",
885	    "description": "将 ASVs 应用于 plan_003 的经验 confusion matrices，跨 3 CSS tasks × 3 LLMs。\n在 held-out gold-standard splits 上验证 coverage。\n比较 ASV 可解释性与 raw confusion matrix reporting。\n",
886	    "results": {
887	      "total_scenarios": 9,
888	      "empirical_asv_concordance": 7,
889	      "concordance_failures": 2,
890	      "failure_scenarios": [
891	        "toxicity-Llama4 vs toxicity-Qwen35",
892	        "toxicity-Qwen35 vs toxicity-DeepSeek"
893	      ],
894	      "failure_reason": "all 3 models produce high ASVs (>2.0) for toxicity K=2; differences within estimation noise",
895	      "asv_ranking": {
896	        "protest": "DeepSeek (0.91) > Llama4 (0.82) > Qwen35 (0.68) — correct",
897	        "stance": "DeepSeek (1.41) > Llama4 (1.24) > Qwen35 (1.08) — correct",
898	        "toxicity": "DeepSeek (2.44) ≈ Llama4 (2.31) ≈ Qwen35 (2.18) — indistinguishable"
899	      },
900	      "held_out_coverage_95": 0.89
901	    },
902	    "tables": [
903	      {
904	        "name": "ASV Values and Concordance by Task × Model",
905	        "columns": [
906	          "task",
907	          "model",
908	          "ASV_95",
909	          "observed_abs_bias",
910	          "robust_flag",
911	          "concordant"
912	        ],
913	        "rows": [
914	          [
915	            "protest",
916	            "Llama 4",
917	            0.82,
918	            0.09,
919	            "moderate",
920	            true
921	          ],
922	          [
923	            "protest",
924	            "Qwen 3.5",
925	            0.68,
926	            0.12,
927	            "fragile",
928	            true
929	          ],
930	          [
931	            "protest",
932	            "DeepSeek",
933	            0.91,
934	            0.05,
935	            "moderate-high",
936	            true
937	          ],
938	          [
939	            "stance",
940	            "Llama 4",
941	            1.24,
942	            0.06,
943	            "moderate-high",
944	            true
945	          ],
946	          [
947	            "stance",
948	            "Qwen 3.5",
949	            1.08,
950	            0.08,
951	            "moderate",
952	            true
953	          ],
954	          [
955	            "stance",
956	            "DeepSeek",
957	            1.41,
958	            0.03,
959	            "high",
960	            true
961	          ],
962	          [
963	            "toxicity",
964	            "Llama 4",
965	            2.31,
966	            0.02,
967	            "high",
968	            true
969	          ],
970	          [
971	            "toxicity",
972	            "Qwen 3.5",
973	            2.18,
974	            0.04,
975	            "high",
976	            false
977	          ],
978	          [
979	            "toxicity",
980	            "DeepSeek",
981	            2.44,
982	            0.01,
983	            "high",
984	            false
985	          ]
986	        ]
987	      }
988	    ],
989	    "figures": [],
990	    "analysis": "ASVs 在 moderate-to-high bias scenarios 中具有经验实用性（protest K=5, stance K=3），\n但在 low-bias regime 失去区分力（toxicity K=2）。这是诚实且预期的——\n类似 E-values 在 confounding 小时不 informative。\n论文应 frame 为：\"ASVs are most valuable when annotation error is non-trivial (K≥3, accuracy <0.85)——\nprecisely the scenarios where researchers lack existing diagnostic tools。\"\n7/9 concordance 支持 Claim 2 的实用价值。\n\n\nConcordance 7/9：ASV 在 protest (K=5) 和 stance (K=3) 任务上正确排序模型鲁棒性——\n这些任务的 confusion matrix 差异足够大，产生有区分力的 ASV 值。\nFailure 出现在 toxicity (K=2)：所有 3 个模型有 near-diagonal C（accuracy > 0.86），\n产生高 ASVs (>2.0)，差异在 MC estimation noise 内——无法区分模型。\n\n这是 low-bias regime 的结构性限制：annotation quality 高时（K=2 toxicity），\nASVs 正确指示\"robust\"但不能 rank-order models。\n这实际上是合适的——如果所有模型产生 negligible bias，ranking 本身就无信息量。\n\nHeld-out coverage (0.89 at 95% nominal) 略低于 MC coverage (0.91) 因为 empirical C 有额外的\ngold-standard sample size 估计噪声。Gap 小且在预期范围内。\n"
991	  },
992	  {
993	    "name": "Correction Guidance Framework: Decision Mapping and Validation",
994	    "description": "Decision framework: {topology × error structure × ASV} → correction method\n(DSL / PPI / MLA / naive plug-in / \"no existing method adequate\")。\nMC validation: 90 scenarios + empirical validation on plan_003 data。\n",
995	    "results": {
996	      "total_mc_scenarios": 90,
997	      "correction_framework_accuracy": 0.89,
998	      "correct_recommendations": 80,
999	      "boundary_indistinguishable_cases": 3,
1000	      "hard_failure_cases": 7,
1001	      "failure_breakdown": {
1002	        "near_diagonal_all_methods_equivalent": 3,
1003	        "differential_intermediate_mismatch": 2,
1004	        "false_recommendation_in_hopeless_regime": 2
1005	      },
1006	      "method_dominance": {
1007	        "DSL": "best in 28/90 (diagonal-dominant C, confounding/mediation)",
1008	        "PPI": "best in 22/90 (moderate C, exposure/front-door)",
1009	        "MLA": "best in 18/90 (high off-diagonal, confounding/collider)",
1010	        "naive_plugin": "best in 12/90 (near-diagonal, any topology)",
1011	        "no_method_adequate": "10/90 (near-permutation + reversal topologies)"
1012	      },
1013	      "empirical_validation_plan003": {
1014	        "protest_correct": true,
1015	        "stance_correct": true,
1016	        "toxicity_correct": true
1017	      },
1018	      "open_problems": [
1019	        "dependence-aware multi-LLM correction",
1020	        "differential K≥3 error correction",
1021	        "collider + near-permutation C (no method reduces bias below 50%)"
1022	      ]
1023	    },
1024	    "tables": [
1025	      {
1026	        "name": "Correction Method Dominance Map",
1027	        "columns": [
1028	          "method",
1029	          "best_in_n",
1030	          "primary_topology",
1031	          "primary_error_regime"
1032	        ],
1033	        "rows": [
1034	          [
1035	            "DSL",
1036	            28,
1037	            "confounding, mediation",
1038	            "diagonal-dominant C"
1039	          ],
1040	          [
1041	            "PPI",
1042	            22,
1043	            "exposure, front-door",
1044	            "moderate off-diagonal"
1045	          ],
1046	          [
1047	            "MLA",
1048	            18,
1049	            "confounding, collider",
1050	            "high off-diagonal"
1051	          ],
1052	          [
1053	            "naive plug-in",
1054	            12,
1055	            "any",
1056	            "near-diagonal"
1057	          ],
1058	          [
1059	            "no method",
1060	            10,
1061	            "exposure, mediation",
1062	            "near-permutation"
1063	          ]
1064	        ]
1065	      },
1066	      {
1067	        "name": "Framework Failure Analysis",
1068	        "columns": [
1069	          "failure_type",
1070	          "count",
1071	          "impact",
1072	          "mitigation"
1073	        ],
1074	        "rows": [
1075	          [
1076	            "boundary (methods ≤5% apart)",
1077	            3,
1078	            "low",
1079	            "any recommendation acceptable"
1080	          ],
1081	          [
1082	            "differential mismatch",
1083	            2,
1084	            "moderate",
1085	            "add continuous differentiality parameter"
1086	          ],
1087	          [
1088	            "false recommendation in hopeless regime",
1089	            2,
1090	            "high",
1091	            "add safety check: if reversal topology + extreme C → flag"
1092	          ]
1093	        ]
1094	      }
1095	    ],
1096	    "figures": [],
1097	    "analysis": "Correction framework 达到主要目标：89% 正确识别 best correction method。\n11% failure rate 集中在固有歧义的 boundary cases（3%）和真正困难的 regimes（8%）。\n2 个\"false recommendation in hopeless regime\"最令人担忧——框架提供了虚假信心。\n论文应明确讨论此风险并建议 practitioners 始终在 held-out data 上验证 corrections。\n10 个\"no method adequate\"scenarios 是论文对 open problems 的贡献——\n特别是 dependence-aware multi-LLM correction（结合 plan_003 的 correlation 发现）。\n\n\n89% accuracy 反映框架在 clear-cut scenarios（方法性能明显分离）的优势和 boundary cases 的弱点。\n\n3 个 boundary cases 是结构性不可区分的：near-diagonal C（low error）下所有方法结果相近（within 5%），\n\"best\" recommendation 是任意的。这不是框架的失败而是问题本身的 degeneracy。\n\n7 个 hard failures：\n(a) 3 cases: near-diagonal C 使所有方法等效但框架因 threshold effects 选了次优方法；\n(b) 2 cases: intermediate differential error 处框架的 non-differential/differential 二分类\n无法捕获 differentiality 的连续性质；\n(c) 2 cases: 框架推荐了方法但正确答案是\"no method adequate\"（near-permutation C + reversal topology）。\n\nMethod dominance 是 topology-driven 的：DSL 擅长 confounding（调整 misclassified confounder 是其 native use case），\nPPI 擅长 exposure（regression-calibration 处理 treatment misclassification），\nMLA 擅长 high off-diagonal error（maximum likelihood 直接建模 C）。\n\n10/90 \"no method adequate\" 集中在 reversal topologies（exposure, mediation）+ extreme C——\n这些是 current correction literature 的真实 gaps。\n"
1098	  },
1099	  {
1100	    "name": "Pathological Confusion Matrix Analysis",
1101	    "description": "极端 C 结构分析：near-permutation, rank-deficient, block-diagonal。\n刻画 catastrophic bias 条件并识别结构性预测因子。\n",
1102	    "results": {
1103	      "spectral_gap_predictive_R2": 0.78,
1104	      "diagonal_dominance_predictive_R2": 0.71,
1105	      "combined_predictor_R2": 0.84,
1106	      "catastrophic_threshold_spectral_gap": 0.3,
1107	      "catastrophic_threshold_diagonal_dominance": 0.5,
1108	      "near_permutation_universally_catastrophic": true,
1109	      "rank_deficient_topology_dependent": true,
1110	      "rank_deficient_worst": [
1111	        "front-door",
1112	        "instrument"
1113	      ],
1114	      "block_diagonal_worst": "mediation (blocks indirect path)"
1115	    },
1116	    "tables": [
1117	      {
1118	        "name": "Structural Predictors of Bias Severity",
1119	        "columns": [
1120	          "predictor",
1121	          "R2_overall",
1122	          "best_topology_R2",
1123	          "worst_topology_R2"
1124	        ],
1125	        "rows": [
1126	          [
1127	            "spectral gap",
1128	            0.78,
1129	            "exposure (0.85)",
1130	            "M-bias (0.67)"
1131	          ],
1132	          [
1133	            "diagonal dominance",
1134	            0.71,
1135	            "confounding (0.82)",
1136	            "front-door (0.58)"
1137	          ],
1138	          [
1139	            "spectral gap + diag dom",
1140	            0.84,
1141	            "exposure (0.91)",
1142	            "instrument (0.74)"
1143	          ]
1144	        ]
1145	      },
1146	      {
1147	        "name": "Catastrophic Bias Conditions by Topology and C Structure",
1148	        "columns": [
1149	          "topology",
1150	          "near_permutation",
1151	          "rank_deficient",
1152	          "block_diagonal"
1153	        ],
1154	        "rows": [
1155	          [
1156	            "confounding",
1157	            "severe (OVB > 2×)",
1158	            "moderate",
1159	            "moderate"
1160	          ],
1161	          [
1162	            "exposure",
1163	            "catastrophic (reversal)",
1164	            "severe",
1165	            "severe (block reversal)"
1166	          ],
1167	          [
1168	            "mediation",
1169	            "severe (reversal)",
1170	            "moderate",
1171	            "severe (block indirect effects)"
1172	          ],
1173	          [
1174	            "collider",
1175	            "severe (attenuation > 60%)",
1176	            "moderate",
1177	            "moderate"
1178	          ],
1179	          [
1180	            "M-bias",
1181	            "moderate",
1182	            "moderate",
1183	            "mild"
1184	          ],
1185	          [
1186	            "instrument",
1187	            "moderate",
1188	            "catastrophic (Wald denom → 0)",
1189	            "moderate"
1190	          ],
1191	          [
1192	            "front-door",
1193	            "moderate",
1194	            "catastrophic (identification loss)",
1195	            "moderate"
1196	          ]
1197	        ]
1198	      }
1199	    ],
1200	    "figures": [],
1201	    "analysis": "实用 takeaway：spectral gap < 0.3 OR diagonal dominance < 0.5 → 所有拓扑均高风险。\n这一双阈值规则足够简单可用且捕获 84% 的 bias variance。\nFront-door 和 instrument 对 rank-deficient C 特别脆弱（ratio estimator 分母问题）。\n这些 structural predictors 是 toolkit (plan_010) 的 automatic diagnostic features 候选。\n\n\nSpectral gap（C 的第一和第二 eigenvalue 之差）预测 bias severity（R²=0.78）\n因为它捕获了 C 距 permutation matrix 的距离——反转的结构性来源。\nR²=0.78 表示强但不完美的预测；剩余方差来自 topology-specific interactions。\n\nDiagonal dominance（minimum diagonal element）是更简单的 proxy，R² 略低（0.71）。\nCombined spectral gap + diagonal dominance 达到 R²=0.84——两个 features 捕获了大部分 bias-relevant C structure。\n\nNear-permutation 普遍 catastrophic 因为 label-swapping 搅乱所有拓扑。\nRank-deficient C 是 topology-dependent：front-door 和 instrument 的 identification formula\n含有 C-dependent 分母——C rank-deficient 时分母趋零，bias unbounded。\nConfounding/mediation/collider 对 rank deficiency 处理更 graceful（无 ratio estimator）。\n\nBlock-diagonal C 对 mediation 最 severe——block 结构可以创造 artifact category boundaries 上的 apparent indirect effects。\n"
1202	  },
1203	  {
1204	    "name": "annot-sensitivity Python Toolkit",
1205	    "description": "Open-source pip-installable package：user-specified DAG + confusion matrix + downstream estimate\n→ bias expressions + ASV + sensitivity curves + correction recommendation + diagnostic plots。\n",
1206	    "results": {
1207	      "package_name": "annot-sensitivity",
1208	      "supported_topologies": 6,
1209	      "supported_K_range": "2–10",
1210	      "core_api": [
1211	        "compute_bias(dag, C, estimate) → BiasResult",
1212	        "compute_asv(dag, C, estimate, delta_range) → ASVResult",
1213	        "recommend_correction(dag, C, asv) → CorrectionRecommendation",
1214	        "diagnostic_plot(result) → Figure",
1215	        "eigendecomp_summary(C, K) → EigenSummary",
1216	        "check_pathological(C) → PathologyReport (spectral gap + diag dom thresholds)"
1217	      ],
1218	      "worked_examples": 3,
1219	      "example_topologies": [
1220	        "confounding (baseline)",
1221	        "exposure (reversal)",
1222	        "mediation (conditional reversal)"
1223	      ],
1224	      "test_coverage": 0.87,
1225	      "documentation": "API reference + 3 tutorial notebooks + quick-start guide",
1226	      "known_limitations": [
1227	        "K>7 eigendecomposition slow (>10s/computation)",
1228	        "correction accuracy inherits plan_007 limitations (89%)",
1229	        "CLI + notebook only, no GUI",
1230	        "3/6 topologies lack detailed tutorials (M-bias, instrument, front-door)"
1231	      ]
1232	    },
1233	    "tables": [],
1234	    "figures": [],
1235	    "analysis": "Toolkit 是 functional deliverable，使论文的理论贡献对 practitioners 可及。\n3 个 worked examples 覆盖最重要的场景（reversal cases）。\n主要 gap：3 个拓扑缺少 tutorial，可能限制 M-bias/instrument/front-door 用户的采纳。\nPost-publication 低成本 follow-up。\n\n3 个 worked examples（而非 6）因为 median 档 scope 有限——优先覆盖 3 个 reversal-relevant 拓扑\n（confounding 作为 baseline，exposure + mediation 作为反转案例）。剩余 3 个拓扑在 API 中支持但缺少详细 tutorial。\n\nK>7 性能限制反映 eigendecomposition 的 O(K³) 成本——对典型 CSS 使用（K=3–7）可接受，\n对罕见 high-K 应用偏慢。\n\nTest coverage 0.87 反映核心计算（bias expressions, ASV）的 thorough unit testing\n和 visualization/correction recommendation 组件的 lighter testing。\n\ncheck_pathological() 集成 plan_009 的 spectral gap + diagonal dominance 阈值，\n为 practitioner 提供自动 C matrix 质量诊断。\n"
1236	  }
1237	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70889562-b748-4584-8f67-19be7a5b1da5",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "530dd707-2b01-4a98-a84c-a37268c49fe6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"K=3 Bias Expressions and MC Validation Across 6 DAG Topologies\",\n    \"description\": \"对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）推导 K=3 closed-form bias 表达式，\\nMC 验证：1000 reps × N=10000 × 6 confusion matrix structures/topology = 36 scenarios。\\n每个拓扑做 100k random C search 检测方向反转。Confounding 为 MVP 再验证；其余 5 个为新推导。\\n结合 MVP exposure 结果，total reversal topologies = 2。\\n\",\n    \"results\": {\n      \"total_scenarios\": 36,\n      \"theory_mc_match\": \"33/36\",\n      \"theory_mc_match_rate\": 0.917,\n      \"reversal_in_plan_001\": 1,\n      \"reversal_topology_new\": \"mediation\",\n      \"combined_reversal_topologies\": 2,\n      \"combined_reversal_list\": [\n        \"exposure (MVP)\",\n        \"mediation (new)\"\n      ],\n      \"confounding\": {\n        \"violation_rate\": 0.0,\n        \"bias_range\": [\n          0.132,\n          0.298\n        ],\n        \"theory_mc\": \"6/6\",\n        \"mechanism\": \"residual confounding, monotonic toward OVB\"\n      },\n      \"mediation\": {\n        \"violation_rate\": 0.23,\n        \"sign_reversal_rate\": 0.18,\n        \"amplification_rate\": 0.05,\n        \"worst_severity\": 1.62,\n        \"named_structures_with_violation\": \"2/6 (near-permutation, block-off-diagonal)\",\n        \"theory_mc\": \"6/6\",\n        \"reversal_condition\": \"off-diagonal dominance > 0.6 AND |indirect effect| > 0.2\",\n        \"indirect_bias_range\": [\n          -0.18,\n          0.14\n        ]\n      },\n      \"collider\": {\n        \"violation_rate\": 0.0,\n        \"bias_range\": [\n          0.04,\n          0.21\n        ],\n        \"attenuation_range\": \"15-60% reduction vs no misclassification\",\n        \"theory_mc\": \"5/6\",\n        \"mechanism\": \"misclassification smooths conditioning variable, reduces collider bias magnitude, preserves direction\"\n      },\n      \"mbias\": {\n        \"violation_rate\": 0.0,\n        \"bias_range\": [\n          0.02,\n          0.16\n        ],\n        \"theory_mc\": \"5/6\",\n        \"mechanism\": \"spurious pathway weakened by misclassification of M-bias variable\"\n      },\n      \"instrument\": {\n        \"violation_rate\": 0.0,\n        \"bias_range\": [\n          0.03,\n          0.19\n        ],\n        \"theory_mc\": \"6/6\",\n        \"mechanism\": \"instrument weakened, Wald estimator biased toward OLS, direction preserved\"\n      },\n      \"frontdoor\": {\n        \"violation_rate\": 0.0,\n        \"bias_range\": [\n          0.05,\n          0.22\n        ],\n        \"theory_mc\": \"5/6\",\n        \"mechanism\": \"front-door estimate attenuated, identification weakened but direction stable\"\n      },\n      \"mc_mismatch_detail\": \"3 mismatches in collider(1), M-bias(1), front-door(1) — all near-permutation C where MC variance is highest due to complex bias formulas (conditioning, ratio estimators)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Direction Reversal Summary by Topology (plan_001 + MVP exposure)\",\n        \"columns\": [\n          \"topology\",\n          \"misclassified_var\",\n          \"violation_rate\",\n          \"sign_reversal\",\n          \"worst_severity\",\n          \"theory_mc\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"exposure (MVP)\",\n            \"treatment X\",\n            0.85,\n            0.834,\n            2.83,\n            \"5/5\",\n            \"reversal-dominant\"\n          ],\n          [\n            \"confounding\",\n            \"confounder U\",\n            0.0,\n            0.0,\n            \"1.00×OVB\",\n            \"6/6\",\n            \"monotonic toward OVB\"\n          ],\n          [\n            \"mediation\",\n            \"mediator M\",\n            0.23,\n            0.18,\n            1.62,\n            \"6/6\",\n            \"conditional reversal\"\n          ],\n          [\n            \"collider\",\n            \"collider Z\",\n            0.0,\n            0.0,\n            \"0.85×(attenuated)\",\n            \"5/6\",\n            \"monotonic attenuation\"\n          ],\n          [\n            \"M-bias\",\n            \"M-bias var\",\n            0.0,\n            0.0,\n            \"0.92×(attenuated)\",\n            \"5/6\",\n            \"monotonic attenuation\"\n          ],\n          [\n            \"instrument\",\n            \"instrument Z\",\n            0.0,\n            0.0,\n            \"0.78×(toward OLS)\",\n            \"6/6\",\n            \"monotonic toward OLS\"\n          ],\n          [\n            \"front-door\",\n            \"front-door M\",\n            0.0,\n            0.0,\n            \"0.88×(attenuated)\",\n            \"5/6\",\n            \"monotonic attenuation\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Mediation Reversal Conditions (100k Random C, K=3)\",\n        \"columns\": [\n          \"C_structure_category\",\n          \"pct_of_random_C\",\n          \"violation_rate\",\n          \"sign_reversal_rate\"\n        ],\n        \"rows\": [\n          [\n            \"near-permutation (off-diag dom > 0.6)\",\n            \"30%\",\n            0.57,\n            0.44\n          ],\n          [\n            \"moderate (off-diag dom 0.3–0.6)\",\n            \"40%\",\n            0.14,\n            0.09\n          ],\n          [\n            \"diagonal-dominant (off-diag dom < 0.3)\",\n            \"30%\",\n            0.0,\n            0.0\n          ],\n          [\n            \"overall\",\n            \"100%\",\n            0.23,\n            0.18\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"plan_001 确认 median 档的核心结果：6 个拓扑中仅 mediation 出现新的反转（结合 MVP exposure = 2 个反转拓扑）。\\n关键发现是反转机制的不对称性：exposure 是\\\"广泛性反转\\\"（label swap 直接作用于 treatment 对比），\\nmediation 是\\\"条件性反转\\\"（需双重门控：C 足够非对角 + 间接效应足够大）。\\n这一不对称性本身就是论文的核心贡献——它证明了 direction reversal 是 topology-specific 的，\\n不能仅从 confusion matrix 结构预测，必须结合 DAG 拓扑分析。\\n4 个单调拓扑的 magnitude 变异（如 collider 0.04–0.21）支持补充论据：即使方向保持，\\nbias magnitude 仍不可从 binary 框架预测。\\n需要补充实验：对 mediation 的 phase diagram 做更精细的 grid search（Fig 3 的分辨率不够用于实用指导）。\\n\\n\\nMediation（23% violation）：misclassifying mediator M 影响间接路径 X→M→Y。反转需要双重门控：\\n(a) C matrix off-diagonal dominance > 0.6（标签大幅置换），AND (b) |true indirect effect| > 0.2（间接效应足够大可以被反转）。\\n因为间接效应 = X→M 系数 × M→Y 系数的乘积，两条路径都必须被实质性扰动才能反转——这种双重门控将 violation rate 限制在 23%。\\n对比 exposure（MVP 85% violation）：exposure misclassification 直接作用于单一 X→Y 路径，无衰减机制，几乎所有非对角 C 都触发反转。\\n这一机制差异（直接路径 vs 乘积路径）是 median 档的核心发现——direction reversal 是 topology-specific 的。\\n\\nCollider（0% violation）：misclassifying Z（collider）并 conditioning on Z* 时，误分类平滑了 Z 的分布，\\n削弱了 selection effect 的强度但不改变其方向。方向由结构方程的符号决定（与测量质量无关）。\\n100k random C 中无一例外。\\n\\nM-bias/Instrument/Front-door（0% violation）：这些拓扑涉及辅助变量，misclassification 削弱 identification 但不反转估计方向。\\nInstrument 特殊之处在于 Wald estimator 的分母受影响（偏向 OLS），但符号不变。\\nFront-door 的 double summation 使 MC 方差在极端 C 下偏高，导致 1/6 mismatch。\\n\\n3 个 MC mismatch 均出现在 near-permutation C structure 下——这些拓扑的 bias formula 含有 conditioning 或 ratio 结构，\\nMC 在极端 C 下方差更大，理论值落在 95% CI 边缘外。\\n\"\n  },\n  {\n    \"name\": \"General-K Matrix Bias Expressions and Interpretability Tools\",\n    \"description\": \"将 bias 表达式扩展到 K=5,7 的矩阵形式。开发 3 个可解释性工具：\\n(a) eigendecomposition summaries，(b) worst-case scalar bounds，(c) diagnostic visualizations。\\n在 confounding + mediation + collider + exposure DAGs 上验证 K=5,7。\\n\",\n    \"results\": {\n      \"K5_theory_mc_match_rate\": 0.89,\n      \"K7_theory_mc_match_rate\": 0.85,\n      \"K5_scenarios_tested\": 24,\n      \"K7_scenarios_tested\": 24,\n      \"eigendecomp_variance_explained_top2_K5\": {\n        \"confounding\": 0.87,\n        \"exposure\": 0.91,\n        \"mediation\": 0.83,\n        \"collider\": 0.88\n      },\n      \"eigendecomp_variance_explained_top3_K7\": {\n        \"confounding\": 0.84,\n        \"exposure\": 0.88,\n        \"mediation\": 0.8,\n        \"collider\": 0.85\n      },\n      \"worst_case_bound_conservatism_median\": \"2.6×\",\n      \"worst_case_bound_conservatism_range\": \"2.1–3.4×\",\n      \"K5_exposure_violation_rate\": 0.88,\n      \"K5_mediation_violation_rate\": 0.28,\n      \"K7_exposure_violation_rate\": 0.9,\n      \"K7_mediation_violation_rate\": 0.31,\n      \"reversal_pattern_persistence\": true,\n      \"dominant_eigenmode_interpretation\": {\n        \"mode_1\": \"diagonal dominance deviation (how far C is from identity)\",\n        \"mode_2\": \"permutation component (which off-diagonal entries dominate)\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Eigendecomposition: Variance Explained by Top Modes\",\n        \"columns\": [\n          \"topology\",\n          \"K\",\n          \"mode_1\",\n          \"mode_2\",\n          \"mode_3\",\n          \"cumulative_top2\",\n          \"cumulative_top3\"\n        ],\n        \"rows\": [\n          [\n            \"confounding\",\n            5,\n            0.68,\n            0.19,\n            0.08,\n            0.87,\n            0.95\n          ],\n          [\n            \"confounding\",\n            7,\n            0.59,\n            0.17,\n            0.08,\n            0.76,\n            0.84\n          ],\n          [\n            \"exposure\",\n            5,\n            0.74,\n            0.17,\n            0.05,\n            0.91,\n            0.96\n          ],\n          [\n            \"exposure\",\n            7,\n            0.65,\n            0.15,\n            0.08,\n            0.8,\n            0.88\n          ],\n          [\n            \"mediation\",\n            5,\n            0.61,\n            0.22,\n            0.09,\n            0.83,\n            0.92\n          ],\n          [\n            \"mediation\",\n            7,\n            0.52,\n            0.19,\n            0.09,\n            0.71,\n            0.8\n          ],\n          [\n            \"collider\",\n            5,\n            0.7,\n            0.18,\n            0.06,\n            0.88,\n            0.94\n          ],\n          [\n            \"collider\",\n            7,\n            0.62,\n            0.16,\n            0.07,\n            0.78,\n            0.85\n          ]\n        ]\n      },\n      {\n        \"name\": \"Violation Rate Scaling with K\",\n        \"columns\": [\n          \"topology\",\n          \"K=3\",\n          \"K=5\",\n          \"K=7\",\n          \"trend\"\n        ],\n        \"rows\": [\n          [\n            \"exposure\",\n            0.85,\n            0.88,\n            0.9,\n            \"near saturation\"\n          ],\n          [\n            \"mediation\",\n            0.23,\n            0.28,\n            0.31,\n            \"monotonic increase\"\n          ],\n          [\n            \"confounding\",\n            0.0,\n            0.0,\n            0.0,\n            \"flat (monotonic)\"\n          ],\n          [\n            \"collider\",\n            0.0,\n            0.0,\n            0.0,\n            \"flat (monotonic)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Matrix-form 表达式成功泛化 K=3 结果。实用发现：top 2 eigenmodes 在 K≤5 下足够（>83% 方差解释），\\nK=7 可能需要 3 个 modes。这指导 toolkit 设计——默认 2-mode summary 加可选扩展。\\nReversal patterns 在 K=5,7 持续，确认 K=3 理论分析不是 special case。\\nWorst-case bounds 的保守性（2.6×）是 tradeoff：tight bounds 需要 topology-specific 优化（随 K 扩展性差），\\nconservative bounds 计算快且作为安全边界仍有实用价值。\\n\\n\\nK=5,7 的 match rate 低于 K=3（0.89/0.85 vs 0.917）因为 MC 方差随 C 的自由参数数 K(K-1) 增长——K=5 有 20 个自由参数，K=7 有 42 个，\\n相同 MC replications 下 confidence interval 更宽。\\n\\nEigendecomposition 的 top 2 modes 能解释 83–91% 方差，因为实际 confusion matrix 具有低有效秩结构：\\n主导误差模式是\\\"相邻类别混淆\\\"（语义相似的类别被混淆），产生带对角扰动结构，被 2–3 个 eigenmodes 良好捕获。\\nMediation 的方差解释率略低（0.83 K=5）因为间接效应涉及乘积，放大了二阶 eigenmode 的贡献。\\n\\nWorst-case bounds 保守（median 2.6×）因为它们对给定 diagonal dominance 下所有 C 做极值优化，\\n包括实际罕见的对抗性配置。作为安全边界是可接受的——类似 E-values 的保守性。\\n\\nViolation rates 随 K 轻微上升（mediation 23% → 28% → 31%）因为更大的 K 增加了 off-diagonal confusion 路径，\\n使 label permutation 更可能。Exposure 接近饱和（85% → 88% → 90%）。\\n\"\n  },\n  {\n    \"name\": \"Empirical Confusion Matrices: 3 LLMs × 3 CSS Tasks\",\n    \"description\": \"从 Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4 收集经验 confusion matrices。\\n3 个 CSS 任务：protest event coding (K=5, ACLED), stance detection (K=3, SemEval/VAST), toxicity (K=2, Civil Comments)。\\n~30K annotations/model × 3 tasks × 3 prompt variants = ~270K total annotations。\\n\",\n    \"results\": {\n      \"api_cost_actual\": \"$420\",\n      \"total_annotations\": 270000,\n      \"protest_K5\": {\n        \"llama4_macro_f1\": 0.71,\n        \"llama4_accuracy\": 0.74,\n        \"qwen35_macro_f1\": 0.68,\n        \"qwen35_accuracy\": 0.71,\n        \"deepseek_macro_f1\": 0.73,\n        \"deepseek_accuracy\": 0.76,\n        \"inter_model_error_agreement\": 0.58,\n        \"downstream_bias_range_abs\": [\n          0.05,\n          0.12\n        ],\n        \"dominant_error_pattern\": \"adjacent-category confusion (riot↔protest, strategic↔organized)\"\n      },\n      \"stance_K3\": {\n        \"llama4_macro_f1\": 0.76,\n        \"llama4_accuracy\": 0.79,\n        \"qwen35_macro_f1\": 0.74,\n        \"qwen35_accuracy\": 0.77,\n        \"deepseek_macro_f1\": 0.78,\n        \"deepseek_accuracy\": 0.81,\n        \"inter_model_error_agreement\": 0.62,\n        \"downstream_bias_range_abs\": [\n          0.03,\n          0.08\n        ],\n        \"dominant_error_pattern\": \"neutral-as-default bias (favor→neutral, against→neutral)\"\n      },\n      \"toxicity_K2\": {\n        \"llama4_f1\": 0.88,\n        \"llama4_accuracy\": 0.9,\n        \"qwen35_f1\": 0.86,\n        \"qwen35_accuracy\": 0.88,\n        \"deepseek_f1\": 0.89,\n        \"deepseek_accuracy\": 0.91,\n        \"inter_model_error_agreement\": 0.64,\n        \"downstream_bias_range_abs\": [\n          0.01,\n          0.04\n        ],\n        \"dominant_error_pattern\": \"slight FN bias (under-flagging toxicity)\"\n      },\n      \"prompt_variant_stability\": \"macro-F1 varies ±0.03; confusion matrix structure stable across prompts\",\n      \"cross_model_error_correlation_mean\": 0.61\n    },\n    \"tables\": [\n      {\n        \"name\": \"Empirical Performance Summary\",\n        \"columns\": [\n          \"task\",\n          \"K\",\n          \"model\",\n          \"macro_F1\",\n          \"accuracy\",\n          \"dominant_error\"\n        ],\n        \"rows\": [\n          [\n            \"protest\",\n            5,\n            \"Llama 4 Maverick\",\n            0.71,\n            0.74,\n            \"riot↔protest (0.15)\"\n          ],\n          [\n            \"protest\",\n            5,\n            \"Qwen 3.5 Plus\",\n            0.68,\n            0.71,\n            \"riot↔protest (0.18), remote↔organized (0.12)\"\n          ],\n          [\n            \"protest\",\n            5,\n            \"DeepSeek V4\",\n            0.73,\n            0.76,\n            \"riot↔protest (0.13)\"\n          ],\n          [\n            \"stance\",\n            3,\n            \"Llama 4 Maverick\",\n            0.76,\n            0.79,\n            \"favor→neutral (0.18)\"\n          ],\n          [\n            \"stance\",\n            3,\n            \"Qwen 3.5 Plus\",\n            0.74,\n            0.77,\n            \"favor→neutral (0.21), against→neutral (0.14)\"\n          ],\n          [\n            \"stance\",\n            3,\n            \"DeepSeek V4\",\n            0.78,\n            0.81,\n            \"favor→neutral (0.15)\"\n          ],\n          [\n            \"toxicity\",\n            2,\n            \"Llama 4 Maverick\",\n            0.88,\n            0.9,\n            \"FN toxic→non-toxic (0.12)\"\n          ],\n          [\n            \"toxicity\",\n            2,\n            \"Qwen 3.5 Plus\",\n            0.86,\n            0.88,\n            \"FN toxic→non-toxic (0.14)\"\n          ],\n          [\n            \"toxicity\",\n            2,\n            \"DeepSeek V4\",\n            0.89,\n            0.91,\n            \"FN toxic→non-toxic (0.10)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Inter-Model Error Correlation\",\n        \"columns\": [\n          \"task\",\n          \"model_pair\",\n          \"error_agreement_when_both_err\",\n          \"kappa_on_errors\"\n        ],\n        \"rows\": [\n          [\n            \"protest\",\n            \"Llama4–Qwen35\",\n            0.56,\n            0.31\n          ],\n          [\n            \"protest\",\n            \"Llama4–DeepSeek\",\n            0.61,\n            0.38\n          ],\n          [\n            \"protest\",\n            \"Qwen35–DeepSeek\",\n            0.57,\n            0.33\n          ],\n          [\n            \"stance\",\n            \"Llama4–Qwen35\",\n            0.6,\n            0.35\n          ],\n          [\n            \"stance\",\n            \"Llama4–DeepSeek\",\n            0.64,\n            0.41\n          ],\n          [\n            \"stance\",\n            \"Qwen35–DeepSeek\",\n            0.62,\n            0.37\n          ],\n          [\n            \"toxicity\",\n            \"Llama4–Qwen35\",\n            0.63,\n            0.39\n          ],\n          [\n            \"toxicity\",\n            \"Llama4–DeepSeek\",\n            0.66,\n            0.44\n          ],\n          [\n            \"toxicity\",\n            \"Qwen35–DeepSeek\",\n            0.64,\n            0.41\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"经验 confusion matrices 确认真实 LLMs 产生 moderately diagonal-dominant 的 C matrix——\\n远离 near-permutation 极端但有足够 off-diagonal mass 产生可检测的 downstream bias。\\n关键经验发现：C structure 是 task-dependent（adjacent-category for protest，neutral-absorbing for stance）\\n且 model-stable（同一 task 下 3 个模型展示相似结构模式）。\\n这意味着理论 taxonomy 的 per-topology 预测适用于真实 LLM 场景——C structure 可从 task 预测，不取决于模型选择。\\nInter-model error correlation 直接支持论文 framing：ensembles 无法修复系统性误差。\\n\\n\\n性能水平反映 2025–2026 LLMs 在 CSS 任务上的典型表现：K=5 protest coding 最难（事件类型间区分微妙），\\nK=3 stance 中等（neutral 类别歧义性高），K=2 toxicity 最易（信号明确）。\\n\\nInter-model error agreement（0.58–0.64）与 Kim et al.（ICML 2025）报告的 ~60% 一致。\\nToxicity 略高因为 binary task 出错方式更少。\\n这验证了论文的动机前提：LLM errors are correlated，ensemble averaging 效果有限。\\n\\nDownstream bias 范围是中等的（非 dramatic）因为真实 LLM confusion matrices 是 moderately diagonal-dominant 的——\\n不是 near-permutation 极端。这是 median 档的预期：理论极端（near-permutation C 导致 2.83× severity）\\n在当前 LLMs 中不会实际出现，但 bias 是可检测的且非 trivial 的。\\n\\nPrompt variant 稳定性（±0.03 F1，C structure stable）支持论文聚焦于 confusion matrix structure 而非 prompt engineering——\\nerror 的结构模式对 prompting 鲁棒，即使边际性能有移动。\\n\"\n  },\n  {\n    \"name\": \"Binarization Collapse Analysis Across 6 Topologies\",\n    \"description\": \"对 6 个拓扑在 K=3,5,7 下：将 K-class 变量折叠为 binary，\\n比较 full multi-class bias expression vs binarized expression。\\n评估何时 binarization 安全、何时危险。\\n\",\n    \"results\": {\n      \"max_delta_overall\": 0.13,\n      \"max_delta_by_K\": {\n        \"K3\": 0.103,\n        \"K5\": 0.13,\n        \"K7\": 0.13\n      },\n      \"worst_delta_topology\": \"mediation (K=5)\",\n      \"binarization_direction_reversal_topologies\": [\n        \"exposure\",\n        \"mediation\"\n      ],\n      \"safe_binarization_topologies\": [\n        \"collider\",\n        \"M-bias\",\n        \"instrument\"\n      ],\n      \"lossy_but_direction_safe\": [\n        \"confounding\",\n        \"front-door\"\n      ],\n      \"delta_by_topology_K3\": {\n        \"confounding\": 0.103,\n        \"mediation\": 0.09,\n        \"collider\": 0.07,\n        \"mbias\": 0.06,\n        \"instrument\": 0.05,\n        \"frontdoor\": 0.08\n      },\n      \"delta_by_topology_K5\": {\n        \"confounding\": 0.11,\n        \"mediation\": 0.13,\n        \"collider\": 0.09,\n        \"mbias\": 0.08,\n        \"instrument\": 0.06,\n        \"frontdoor\": 0.09\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Binarization Delta Summary\",\n        \"columns\": [\n          \"topology\",\n          \"K\",\n          \"max_delta\",\n          \"direction_reversal_from_binarization\",\n          \"safety_class\"\n        ],\n        \"rows\": [\n          [\n            \"confounding\",\n            3,\n            0.103,\n            false,\n            \"direction-safe, magnitude-unsafe\"\n          ],\n          [\n            \"confounding\",\n            5,\n            0.11,\n            false,\n            \"direction-safe, magnitude-unsafe\"\n          ],\n          [\n            \"mediation\",\n            3,\n            0.09,\n            true,\n            \"unsafe\"\n          ],\n          [\n            \"mediation\",\n            5,\n            0.13,\n            true,\n            \"unsafe\"\n          ],\n          [\n            \"exposure (ref)\",\n            3,\n            0.09,\n            true,\n            \"unsafe\"\n          ],\n          [\n            \"exposure (ref)\",\n            5,\n            0.1,\n            true,\n            \"unsafe\"\n          ],\n          [\n            \"collider\",\n            3,\n            0.07,\n            false,\n            \"safe\"\n          ],\n          [\n            \"collider\",\n            5,\n            0.09,\n            false,\n            \"safe\"\n          ],\n          [\n            \"M-bias\",\n            3,\n            0.06,\n            false,\n            \"safe\"\n          ],\n          [\n            \"instrument\",\n            3,\n            0.05,\n            false,\n            \"safe\"\n          ],\n          [\n            \"front-door\",\n            3,\n            0.08,\n            false,\n            \"direction-safe, magnitude-marginal\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binarization 不是逃离 K≥3 复杂性的安全手段。Max delta 0.13（mediation K=5）在典型 CSS 回归中\\n（effect size 0.1–0.5）足以主导估计。\\n拓扑分三组：(1) binarization-unsafe（exposure, mediation——可能反转方向），\\n(2) binarization-lossy（confounding, front-door——保持方向但损失量级精度），\\n(3) binarization-tolerable（collider, M-bias, instrument——delta 小，安全）。\\n这支持论文的 multi-class treatment is necessary 论点。\\n\\n\\nBinarization delta 在 K=5 达到峰值（0.13）并在 K=7 持平，因为 K→2 的信息损失在 K=5–7 饱和——\\n超过 K=7 后额外类别的边际信息递减。\\n\\nMediation 的 delta 最大（K=5 时 0.13）因为 binarizing mediator M 将间接路径折叠为单一对比，\\n丢失了 multi-class expression 捕获的 category-specific indirect effects。\\n对 exposure 和 mediation，某些 binarization folding 产生方向反转：\\n将 category 1+2 vs 3 折叠可能将相反方向的效应分配到同一 binary class。\\n\\nConfounding delta 高（K=3 0.103，来自 MVP）因为 binarizing confounder 丢失了残差混杂控制。\\n但方向保持（direction-safe, magnitude-unsafe）。\\n\\nCollider/M-bias/instrument delta 较小因为这些拓扑涉及辅助变量，\\nbinary 近似更接近 multi-class truth——关键量（induced bias direction）更依赖 conditioning operation 而非变量粒度。\\n\"\n  },\n  {\n    \"name\": \"ASV Framework: Formal Proofs for Confounding, Mediation, Collider\",\n    \"description\": \"推导 3 个优先拓扑的 ASV 表达式。形式化证明 monotonicity 和 sharpness。\\nMC 验证：coverage at 90%, 95%, 99% across 1000 scenarios/topology。\\n\",\n    \"results\": {\n      \"monotonicity_proved\": [\n        \"confounding\",\n        \"mediation\",\n        \"collider\"\n      ],\n      \"sharpness_proved\": [\n        \"confounding\",\n        \"mediation\"\n      ],\n      \"sharpness_incomplete\": [\n        \"collider\"\n      ],\n      \"sharpness_formal_proofs_count\": 2,\n      \"collider_sharpness_numerical\": \"achieving 93% of bound in 10k optimization runs\",\n      \"coverage_at_95_nominal\": {\n        \"confounding\": 0.93,\n        \"mediation\": 0.9,\n        \"collider\": 0.91\n      },\n      \"coverage_at_90_nominal\": {\n        \"confounding\": 0.95,\n        \"mediation\": 0.92,\n        \"collider\": 0.93\n      },\n      \"coverage_at_99_nominal\": {\n        \"confounding\": 0.97,\n        \"mediation\": 0.96,\n        \"collider\": 0.95\n      },\n      \"average_coverage_95\": 0.913\n    },\n    \"tables\": [\n      {\n        \"name\": \"ASV Proof Status and Coverage (Priority Topologies)\",\n        \"columns\": [\n          \"topology\",\n          \"monotonicity\",\n          \"sharpness\",\n          \"coverage_90\",\n          \"coverage_95\",\n          \"coverage_99\"\n        ],\n        \"rows\": [\n          [\n            \"confounding\",\n            \"formal proof\",\n            \"formal proof\",\n            0.95,\n            0.93,\n            0.97\n          ],\n          [\n            \"mediation\",\n            \"formal proof\",\n            \"formal proof\",\n            0.92,\n            0.9,\n            0.96\n          ],\n          [\n            \"collider\",\n            \"formal proof\",\n            \"numerical only (93%)\",\n            0.93,\n            0.91,\n            0.95\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ASV 框架在 3 个优先拓扑上验证：monotonicity universally proved，sharpness 2/3 proved。\\nCollider sharpness gap（7%）是主要技术障碍——论文应增加一段讨论 conditioning-on-misclassified-variable 导致的非凸优化问题，\\n并标记 convex relaxation approach 为 future work。\\nMediation 的更陡 ASV 曲线意味着 mediation DAGs 的结论对 annotation error 更敏感——\\n与 direction reversal 发现一致，自然连接 Claim 1 和 Claim 2。\\n\\n\\nMonotonicity 对所有 3 个拓扑成立（proved）因为：更大的 δ 意味着 sensitivity set 中考虑更极端的 C →\\noverturn conclusion 所需的 minimum perturbation 只能增加或不变。\\n这与 underlying bias 是否单调无关——ASV 是 min-over-C 量，不是 pointwise bias。\\n\\nConfounding sharpness：bias 在 C 的 off-diagonal elements 上是线性的，supremum 有 clean convex structure，\\nsharpness-achieving C 在 feasible set 的顶点。构造性证明。\\n\\nMediation sharpness：尽管存在方向反转，ASV sharpness 仍可证——通过分别分析 attenuation regime 和 reversal regime。\\nReversal boundary 处的 worst-case C 恰好达到 bound——构造性证明利用 phase transition 结构。\\n这是一个 nice 的结果：有反转的拓扑仍然有 tight bound，加强了 ASV 框架的可信度。\\n\\nCollider sharpness INCOMPLETE：bias 表达式涉及 conditioning on misclassified Z，\\n产生 E[Y|X,Z*] = Σ_z P(Z=z|Z*) E[Y|X,Z=z]。\\n对 C 做 supremum 要求联合优化 P(Z=z|Z*)，subject to C 为 valid confusion matrix，\\n产生非凸 bilinear 约束。数值优化达到 analytical bound 的 93%，强烈暗示 sharpness，\\n但形式化证明 supremum is attained 被 feasible set 的非凸拓扑阻断。\\n\\nCoverage 略低于 nominal（average 91.3% at 95% nominal）因为 ASV bounds 在已知 exact C 下推导，\\n而 MC 用的是有限样本估计的 C。Gap（3.7%）反映估计不确定性而非 bound failure。\\n\"\n  },\n  {\n    \"name\": \"ASV MC Validation for M-bias, Instrument, Front-door\",\n    \"description\": \"推导剩余 3 个拓扑的 ASV 表达式 + MC 验证。\\nMonotonicity 和 coverage 验证。Sharpness 作为 conjectures + numerical evidence。\\n\",\n    \"results\": {\n      \"monotonicity_holds\": [\n        \"M-bias\",\n        \"instrument\",\n        \"front-door\"\n      ],\n      \"monotonicity_failures\": 0,\n      \"sharpness_numerical\": {\n        \"mbias\": \"achieving 92% of bound\",\n        \"instrument\": \"achieving 89% of bound\",\n        \"frontdoor\": \"achieving 94% of bound\"\n      },\n      \"coverage_at_95_nominal\": {\n        \"mbias\": 0.9,\n        \"instrument\": 0.89,\n        \"frontdoor\": 0.91\n      },\n      \"instrument_conservatism\": \"ASV bounds 1.8× wider than necessary\",\n      \"total_asv_coverage_6_topologies\": 0.907\n    },\n    \"tables\": [\n      {\n        \"name\": \"ASV Results for Secondary Topologies\",\n        \"columns\": [\n          \"topology\",\n          \"monotonicity\",\n          \"sharpness_numerical_pct\",\n          \"coverage_95\",\n          \"conservatism\"\n        ],\n        \"rows\": [\n          [\n            \"M-bias\",\n            \"holds\",\n            \"92%\",\n            0.9,\n            \"comparable to collider\"\n          ],\n          [\n            \"instrument\",\n            \"holds\",\n            \"89%\",\n            0.89,\n            \"1.8× conservative (Wald ratio)\"\n          ],\n          [\n            \"front-door\",\n            \"holds\",\n            \"94%\",\n            0.91,\n            \"near-tight\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"All 6 Topologies ASV Summary\",\n        \"columns\": [\n          \"topology\",\n          \"monotonicity\",\n          \"sharpness_status\",\n          \"coverage_95\"\n        ],\n        \"rows\": [\n          [\n            \"confounding\",\n            \"proved\",\n            \"proved (formal)\",\n            0.93\n          ],\n          [\n            \"mediation\",\n            \"proved\",\n            \"proved (formal)\",\n            0.9\n          ],\n          [\n            \"collider\",\n            \"proved\",\n            \"93% numerical\",\n            0.91\n          ],\n          [\n            \"M-bias\",\n            \"proved\",\n            \"92% numerical\",\n            0.9\n          ],\n          [\n            \"instrument\",\n            \"proved\",\n            \"89% numerical\",\n            0.89\n          ],\n          [\n            \"front-door\",\n            \"proved\",\n            \"94% numerical\",\n            0.91\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"6 个拓扑全部有 ASV 表达式 + validated monotonicity。Sharpness landscape：\\n2 proved (confounding, mediation) + 4 numerical (collider 93%, front-door 94%, M-bias 92%, instrument 89%)。\\nInstrument 是最弱环节——ASV 保守性限制了实用性。论文应诚实讨论并标记 tighter instrument-specific bounds 为 future work。\\nOverall average 95%-nominal coverage = 0.907，在 median 档 [0.88, 0.93] 范围内。\\n\\n\\nMonotonicity 对所有 3 个拓扑成立——与 plan_004 相同的结构性论证：\\nASV 是 minimum-over-perturbation 量，在 perturbation budget δ 中固有单调。\\n\\nSharpness numerical evidence 有差异：front-door 最接近 tight（94%，identification structure 较简单），\\nM-bias 中等（92%），instrument 最远（89%）。\\nInstrument gap 反映 Wald estimator 的 ratio structure——supremum 涉及优化 misclassified 量的 ratio，\\nlandscape 有多个 local optima。\\n\\nInstrument ASV 显著保守（1.8× wider）因为 Wald estimator 放大小分母扰动，\\nworst-case bound 比 typical case 差很多。这是 IV sensitivity analysis 的已知问题（非本框架特有）。\\n\"\n  },\n  {\n    \"name\": \"ASV Calibration on Empirical Data\",\n    \"description\": \"将 ASVs 应用于 plan_003 的经验 confusion matrices，跨 3 CSS tasks × 3 LLMs。\\n在 held-out gold-standard splits 上验证 coverage。\\n比较 ASV 可解释性与 raw confusion matrix reporting。\\n\",\n    \"results\": {\n      \"total_scenarios\": 9,\n      \"empirical_asv_concordance\": 7,\n      \"concordance_failures\": 2,\n      \"failure_scenarios\": [\n        \"toxicity-Llama4 vs toxicity-Qwen35\",\n        \"toxicity-Qwen35 vs toxicity-DeepSeek\"\n      ],\n      \"failure_reason\": \"all 3 models produce high ASVs (>2.0) for toxicity K=2; differences within estimation noise\",\n      \"asv_ranking\": {\n        \"protest\": \"DeepSeek (0.91) > Llama4 (0.82) > Qwen35 (0.68) — correct\",\n        \"stance\": \"DeepSeek (1.41) > Llama4 (1.24) > Qwen35 (1.08) — correct\",\n        \"toxicity\": \"DeepSeek (2.44) ≈ Llama4 (2.31) ≈ Qwen35 (2.18) — indistinguishable\"\n      },\n      \"held_out_coverage_95\": 0.89\n    },\n    \"tables\": [\n      {\n        \"name\": \"ASV Values and Concordance by Task × Model\",\n        \"columns\": [\n          \"task\",\n          \"model\",\n          \"ASV_95\",\n          \"observed_abs_bias\",\n          \"robust_flag\",\n          \"concordant\"\n        ],\n        \"rows\": [\n          [\n            \"protest\",\n            \"Llama 4\",\n            0.82,\n            0.09,\n            \"moderate\",\n            true\n          ],\n          [\n            \"protest\",\n            \"Qwen 3.5\",\n            0.68,\n            0.12,\n            \"fragile\",\n            true\n          ],\n          [\n            \"protest\",\n            \"DeepSeek\",\n            0.91,\n            0.05,\n            \"moderate-high\",\n            true\n          ],\n          [\n            \"stance\",\n            \"Llama 4\",\n            1.24,\n            0.06,\n            \"moderate-high\",\n            true\n          ],\n          [\n            \"stance\",\n            \"Qwen 3.5\",\n            1.08,\n            0.08,\n            \"moderate\",\n            true\n          ],\n          [\n            \"stance\",\n            \"DeepSeek\",\n            1.41,\n            0.03,\n            \"high\",\n            true\n          ],\n          [\n            \"toxicity\",\n            \"Llama 4\",\n            2.31,\n            0.02,\n            \"high\",\n            true\n          ],\n          [\n            \"toxicity\",\n            \"Qwen 3.5\",\n            2.18,\n            0.04,\n            \"high\",\n            false\n          ],\n          [\n            \"toxicity\",\n            \"DeepSeek\",\n            2.44,\n            0.01,\n            \"high\",\n            false\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ASVs 在 moderate-to-high bias scenarios 中具有经验实用性（protest K=5, stance K=3），\\n但在 low-bias regime 失去区分力（toxicity K=2）。这是诚实且预期的——\\n类似 E-values 在 confounding 小时不 informative。\\n论文应 frame 为：\\\"ASVs are most valuable when annotation error is non-trivial (K≥3, accuracy <0.85)——\\nprecisely the scenarios where researchers lack existing diagnostic tools。\\\"\\n7/9 concordance 支持 Claim 2 的实用价值。\\n\\n\\nConcordance 7/9：ASV 在 protest (K=5) 和 stance (K=3) 任务上正确排序模型鲁棒性——\\n这些任务的 confusion matrix 差异足够大，产生有区分力的 ASV 值。\\nFailure 出现在 toxicity (K=2)：所有 3 个模型有 near-diagonal C（accuracy > 0.86），\\n产生高 ASVs (>2.0)，差异在 MC estimation noise 内——无法区分模型。\\n\\n这是 low-bias regime 的结构性限制：annotation quality 高时（K=2 toxicity），\\nASVs 正确指示\\\"robust\\\"但不能 rank-order models。\\n这实际上是合适的——如果所有模型产生 negligible bias，ranking 本身就无信息量。\\n\\nHeld-out coverage (0.89 at 95% nominal) 略低于 MC coverage (0.91) 因为 empirical C 有额外的\\ngold-standard sample size 估计噪声。Gap 小且在预期范围内。\\n\"\n  },\n  {\n    \"name\": \"Correction Guidance Framework: Decision Mapping and Validation\",\n    \"description\": \"Decision framework: {topology × error structure × ASV} → correction method\\n(DSL / PPI / MLA / naive plug-in / \\\"no existing method adequate\\\")。\\nMC validation: 90 scenarios + empirical validation on plan_003 data。\\n\",\n    \"results\": {\n      \"total_mc_scenarios\": 90,\n      \"correction_framework_accuracy\": 0.89,\n      \"correct_recommendations\": 80,\n      \"boundary_indistinguishable_cases\": 3,\n      \"hard_failure_cases\": 7,\n      \"failure_breakdown\": {\n        \"near_diagonal_all_methods_equivalent\": 3,\n        \"differential_intermediate_mismatch\": 2,\n        \"false_recommendation_in_hopeless_regime\": 2\n      },\n      \"method_dominance\": {\n        \"DSL\": \"best in 28/90 (diagonal-dominant C, confounding/mediation)\",\n        \"PPI\": \"best in 22/90 (moderate C, exposure/front-door)\",\n        \"MLA\": \"best in 18/90 (high off-diagonal, confounding/collider)\",\n        \"naive_plugin\": \"best in 12/90 (near-diagonal, any topology)\",\n        \"no_method_adequate\": \"10/90 (near-permutation + reversal topologies)\"\n      },\n      \"empirical_validation_plan003\": {\n        \"protest_correct\": true,\n        \"stance_correct\": true,\n        \"toxicity_correct\": true\n      },\n      \"open_problems\": [\n        \"dependence-aware multi-LLM correction\",\n        \"differential K≥3 error correction\",\n        \"collider + near-permutation C (no method reduces bias below 50%)\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Correction Method Dominance Map\",\n        \"columns\": [\n          \"method\",\n          \"best_in_n\",\n          \"primary_topology\",\n          \"primary_error_regime\"\n        ],\n        \"rows\": [\n          [\n            \"DSL\",\n            28,\n            \"confounding, mediation\",\n            \"diagonal-dominant C\"\n          ],\n          [\n            \"PPI\",\n            22,\n            \"exposure, front-door\",\n            \"moderate off-diagonal\"\n          ],\n          [\n            \"MLA\",\n            18,\n            \"confounding, collider\",\n            \"high off-diagonal\"\n          ],\n          [\n            \"naive plug-in\",\n            12,\n            \"any\",\n            \"near-diagonal\"\n          ],\n          [\n            \"no method\",\n            10,\n            \"exposure, mediation\",\n            \"near-permutation\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Framework Failure Analysis\",\n        \"columns\": [\n          \"failure_type\",\n          \"count\",\n          \"impact\",\n          \"mitigation\"\n        ],\n        \"rows\": [\n          [\n            \"boundary (methods ≤5% apart)\",\n            3,\n            \"low\",\n            \"any recommendation acceptable\"\n          ],\n          [\n            \"differential mismatch\",\n            2,\n            \"moderate\",\n            \"add continuous differentiality parameter\"\n          ],\n          [\n            \"false recommendation in hopeless regime\",\n            2,\n            \"high\",\n            \"add safety check: if reversal topology + extreme C → flag\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Correction framework 达到主要目标：89% 正确识别 best correction method。\\n11% failure rate 集中在固有歧义的 boundary cases（3%）和真正困难的 regimes（8%）。\\n2 个\\\"false recommendation in hopeless regime\\\"最令人担忧——框架提供了虚假信心。\\n论文应明确讨论此风险并建议 practitioners 始终在 held-out data 上验证 corrections。\\n10 个\\\"no method adequate\\\"scenarios 是论文对 open problems 的贡献——\\n特别是 dependence-aware multi-LLM correction（结合 plan_003 的 correlation 发现）。\\n\\n\\n89% accuracy 反映框架在 clear-cut scenarios（方法性能明显分离）的优势和 boundary cases 的弱点。\\n\\n3 个 boundary cases 是结构性不可区分的：near-diagonal C（low error）下所有方法结果相近（within 5%），\\n\\\"best\\\" recommendation 是任意的。这不是框架的失败而是问题本身的 degeneracy。\\n\\n7 个 hard failures：\\n(a) 3 cases: near-diagonal C 使所有方法等效但框架因 threshold effects 选了次优方法；\\n(b) 2 cases: intermediate differential error 处框架的 non-differential/differential 二分类\\n无法捕获 differentiality 的连续性质；\\n(c) 2 cases: 框架推荐了方法但正确答案是\\\"no method adequate\\\"（near-permutation C + reversal topology）。\\n\\nMethod dominance 是 topology-driven 的：DSL 擅长 confounding（调整 misclassified confounder 是其 native use case），\\nPPI 擅长 exposure（regression-calibration 处理 treatment misclassification），\\nMLA 擅长 high off-diagonal error（maximum likelihood 直接建模 C）。\\n\\n10/90 \\\"no method adequate\\\" 集中在 reversal topologies（exposure, mediation）+ extreme C——\\n这些是 current correction literature 的真实 gaps。\\n\"\n  },\n  {\n    \"name\": \"Pathological Confusion Matrix Analysis\",\n    \"description\": \"极端 C 结构分析：near-permutation, rank-deficient, block-diagonal。\\n刻画 catastrophic bias 条件并识别结构性预测因子。\\n\",\n    \"results\": {\n      \"spectral_gap_predictive_R2\": 0.78,\n      \"diagonal_dominance_predictive_R2\": 0.71,\n      \"combined_predictor_R2\": 0.84,\n      \"catastrophic_threshold_spectral_gap\": 0.3,\n      \"catastrophic_threshold_diagonal_dominance\": 0.5,\n      \"near_permutation_universally_catastrophic\": true,\n      \"rank_deficient_topology_dependent\": true,\n      \"rank_deficient_worst\": [\n        \"front-door\",\n        \"instrument\"\n      ],\n      \"block_diagonal_worst\": \"mediation (blocks indirect path)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Structural Predictors of Bias Severity\",\n        \"columns\": [\n          \"predictor\",\n          \"R2_overall\",\n          \"best_topology_R2\",\n          \"worst_topology_R2\"\n        ],\n        \"rows\": [\n          [\n            \"spectral gap\",\n            0.78,\n            \"exposure (0.85)\",\n            \"M-bias (0.67)\"\n          ],\n          [\n            \"diagonal dominance\",\n            0.71,\n            \"confounding (0.82)\",\n            \"front-door (0.58)\"\n          ],\n          [\n            \"spectral gap + diag dom\",\n            0.84,\n            \"exposure (0.91)\",\n            \"instrument (0.74)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Catastrophic Bias Conditions by Topology and C Structure\",\n        \"columns\": [\n          \"topology\",\n          \"near_permutation\",\n          \"rank_deficient\",\n          \"block_diagonal\"\n        ],\n        \"rows\": [\n          [\n            \"confounding\",\n            \"severe (OVB > 2×)\",\n            \"moderate\",\n            \"moderate\"\n          ],\n          [\n            \"exposure\",\n            \"catastrophic (reversal)\",\n            \"severe\",\n            \"severe (block reversal)\"\n          ],\n          [\n            \"mediation\",\n            \"severe (reversal)\",\n            \"moderate\",\n            \"severe (block indirect effects)\"\n          ],\n          [\n            \"collider\",\n            \"severe (attenuation > 60%)\",\n            \"moderate\",\n            \"moderate\"\n          ],\n          [\n            \"M-bias\",\n            \"moderate\",\n            \"moderate\",\n            \"mild\"\n          ],\n          [\n            \"instrument\",\n            \"moderate\",\n            \"catastrophic (Wald denom → 0)\",\n            \"moderate\"\n          ],\n          [\n            \"front-door\",\n            \"moderate\",\n            \"catastrophic (identification loss)\",\n            \"moderate\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"实用 takeaway：spectral gap < 0.3 OR diagonal dominance < 0.5 → 所有拓扑均高风险。\\n这一双阈值规则足够简单可用且捕获 84% 的 bias variance。\\nFront-door 和 instrument 对 rank-deficient C 特别脆弱（ratio estimator 分母问题）。\\n这些 structural predictors 是 toolkit (plan_010) 的 automatic diagnostic features 候选。\\n\\n\\nSpectral gap（C 的第一和第二 eigenvalue 之差）预测 bias severity（R²=0.78）\\n因为它捕获了 C 距 permutation matrix 的距离——反转的结构性来源。\\nR²=0.78 表示强但不完美的预测；剩余方差来自 topology-specific interactions。\\n\\nDiagonal dominance（minimum diagonal element）是更简单的 proxy，R² 略低（0.71）。\\nCombined spectral gap + diagonal dominance 达到 R²=0.84——两个 features 捕获了大部分 bias-relevant C structure。\\n\\nNear-permutation 普遍 catastrophic 因为 label-swapping 搅乱所有拓扑。\\nRank-deficient C 是 topology-dependent：front-door 和 instrument 的 identification formula\\n含有 C-dependent 分母——C rank-deficient 时分母趋零，bias unbounded。\\nConfounding/mediation/collider 对 rank deficiency 处理更 graceful（无 ratio estimator）。\\n\\nBlock-diagonal C 对 mediation 最 severe——block 结构可以创造 artifact category boundaries 上的 apparent indirect effects。\\n\"\n  },\n  {\n    \"name\": \"annot-sensitivity Python Toolkit\",\n    \"description\": \"Open-source pip-installable package：user-specified DAG + confusion matrix + downstream estimate\\n→ bias expressions + ASV + sensitivity curves + correction recommendation + diagnostic plots。\\n\",\n    \"results\": {\n      \"package_name\": \"annot-sensitivity\",\n      \"supported_topologies\": 6,\n      \"supported_K_range\": \"2–10\",\n      \"core_api\": [\n        \"compute_bias(dag, C, estimate) → BiasResult\",\n        \"compute_asv(dag, C, estimate, delta_range) → ASVResult\",\n        \"recommend_correction(dag, C, asv) → CorrectionRecommendation\",\n        \"diagnostic_plot(result) → Figure\",\n        \"eigendecomp_summary(C, K) → EigenSummary\",\n        \"check_pathological(C) → PathologyReport (spectral gap + diag dom thresholds)\"\n      ],\n      \"worked_examples\": 3,\n      \"example_topologies\": [\n        \"confounding (baseline)\",\n        \"exposure (reversal)\",\n        \"mediation (conditional reversal)\"\n      ],\n      \"test_coverage\": 0.87,\n      \"documentation\": \"API reference + 3 tutorial notebooks + quick-start guide\",\n      \"known_limitations\": [\n        \"K>7 eigendecomposition slow (>10s/computation)\",\n        \"correction accuracy inherits plan_007 limitations (89%)\",\n        \"CLI + notebook only, no GUI\",\n        \"3/6 topologies lack detailed tutorials (M-bias, instrument, front-door)\"\n      ]\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Toolkit 是 functional deliverable，使论文的理论贡献对 practitioners 可及。\\n3 个 worked examples 覆盖最重要的场景（reversal cases）。\\n主要 gap：3 个拓扑缺少 tutorial，可能限制 M-bias/instrument/front-door 用户的采纳。\\nPost-publication 低成本 follow-up。\\n\\n3 个 worked examples（而非 6）因为 median 档 scope 有限——优先覆盖 3 个 reversal-relevant 拓扑\\n（confounding 作为 baseline，exposure + mediation 作为反转案例）。剩余 3 个拓扑在 API 中支持但缺少详细 tutorial。\\n\\nK>7 性能限制反映 eigendecomposition 的 O(K³) 成本——对典型 CSS 使用（K=3–7）可接受，\\n对罕见 high-K 应用偏慢。\\n\\nTest coverage 0.87 反映核心计算（bias expressions, ASV）的 thorough unit testing\\n和 visualization/correction recommendation 组件的 lighter testing。\\n\\ncheck_pathological() 集成 plan_009 的 spectral gap + diagonal dominance 阈值，\\n为 practitioner 提供自动 C matrix 质量诊断。\\n\"\n  }\n]",
      "numLines": 1237,
      "startLine": 1,
      "totalLines": 1237
    }
  },
  "sourceToolAssistantUUID": "70889562-b748-4584-8f67-19be7a5b1da5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T08:29:41.698Z_

<details><summary>↩ Tool result · `toolu_01G63BGcBSV4o7q4UjTXE76r`</summary>

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
  "parentUuid": "a8f1ab6c-f62b-4719-8375-d016831c8961",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "054fae7b-db34-47c5-acb4-bf6f454264ec",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper_framing.md",
      "content": "# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias.\"\n\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\n\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\nThe binary guarantee that \"non-differential exposure misclassification biases toward the null\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\"bias can go in either direction\"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \"escape\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\n\n### Version B (no direction reversal found across topologies)\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\n\n**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.\n\n## MVP Evidence\n\n**Confounding DAG + K=3** (confounder misclassification):\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \"well-behaved\" (predictable direction)\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\n\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\n- K=2 control: 6/6 toward null (binary guarantee holds)\n- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 6 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]\n",
      "numLines": 75,
      "startLine": 1,
      "totalLines": 75
    }
  },
  "sourceToolAssistantUUID": "a8f1ab6c-f62b-4719-8375-d016831c8961",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_att…",
  "leafUuid": "530dd707-2b01-4a98-a84c-a37268c49fe6",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with causal annotation analysis",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---

### Assistant

_source line 14 · 2026-05-20T08:29:48.021Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment data and paper framing. Let me also read the paper-writing-norms skill to guide the writing.

Actually, the task says "够审" level, not submission quality. Let me now construct the full LaTeX paper.

Let me first check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "054fae7b-db34-47c5-acb4-bf6f454264ec",
  "isSidechain": false,
  "requestId": "req_011CbDWMkDkRQBeWPLbA54ks",
  "type": "assistant",
  "uuid": "763f5eaf-b3d6-4b2d-b02b-01d26aabd859",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YdN65R6krXkUCvnrdc9GN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21251,
      "cache_read_input_tokens": 23870,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 23870,
          "cache_creation_input_tokens": 21251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21251
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

_source line 15 · 2026-05-20T08:29:48.405Z_

Now let me check the output directory and read the paper writing norms skill for style guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "763f5eaf-b3d6-4b2d-b02b-01d26aabd859",
  "isSidechain": false,
  "requestId": "req_011CbDWMkDkRQBeWPLbA54ks",
  "type": "assistant",
  "uuid": "b4dc3f67-21e7-4266-8ccd-b0c2177c1a34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YdN65R6krXkUCvnrdc9GN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21251,
      "cache_read_input_tokens": 23870,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 23870,
          "cache_creation_input_tokens": 21251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21251
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

_source line 16 · 2026-05-20T08:29:50.933Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wje2u9g6oYSSGPGSzMwUgn`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4dc3f67-21e7-4266-8ccd-b0c2177c1a34",
  "isSidechain": false,
  "requestId": "req_011CbDWMkDkRQBeWPLbA54ks",
  "type": "assistant",
  "uuid": "d8fd42cb-8efa-4192-accc-431242193fbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YdN65R6krXkUCvnrdc9GN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21251,
      "cache_read_input_tokens": 23870,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 23870,
          "cache_creation_input_tokens": 21251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21251
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

_source line 17 · 2026-05-20T08:29:51.612Z_

<details><summary>↩ Tool result · `toolu_01HBRUoCCc8XSb4gGHhg7j9f`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a60794b-b133-4ae4-a161-eba480029530",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "608fdd9d-62e5-4b02-90e3-6094a451a1ee",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "8a60794b-b133-4ae4-a161-eba480029530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T08:29:51.144Z_

<details><summary>↩ Tool result · `toolu_01Wje2u9g6oYSSGPGSzMwUgn`</summary>

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
  "parentUuid": "d8fd42cb-8efa-4192-accc-431242193fbc",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "3a929308-fbc1-4ee3-8ef3-f4c2eaea4756",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d8fd42cb-8efa-4192-accc-431242193fbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T08:29:51.603Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HBRUoCCc8XSb4gGHhg7j9f`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a929308-fbc1-4ee3-8ef3-f4c2eaea4756",
  "isSidechain": false,
  "requestId": "req_011CbDWMkDkRQBeWPLbA54ks",
  "type": "assistant",
  "uuid": "8a60794b-b133-4ae4-a161-eba480029530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YdN65R6krXkUCvnrdc9GN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21251,
      "cache_read_input_tokens": 23870,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 23870,
          "cache_creation_input_tokens": 21251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21251
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

_source line 20 · 2026-05-20T08:30:20.065Z_

<details><summary>Logged reasoning block</summary>

```text
I have all the information I need. Now let me write the full LaTeX paper. Let me synthesize the experiment data and narrative guidance into a coherent paper.

Key points from the narrative guidance:
- Version A: direction reversal is topology-specific (exposure 85% + mediation 23%)
- Exposure reversal is "pervasive" (85%), mediation is "conditional" (23%, dual-gated)
- Remaining 4 topologies maintain monotonicity but with significant magnitude variation
- Claim 1: taxonomy works, but direction reversal is topology-specific not universal


- Claim 2: ASV tightness holds across 2 topologies with formal proofs and 4 with Monte Carlo evidence
- Claim 3: correction guidance framework remains unchanged

Now I'm structuring the paper with five main experiments: the K=3 bias expressions across all six topologies, general-K matrix expressions, empirical confusion matrices from LLMs, binarization collapse analysis, and one more experiment to complete the evaluation.

Then I need to add the ASV framework validation, ASV calibration on real data, the correction guidance framework demonstration, pathological confusion matrix analysis, and the annotation-sensitivity toolkit. But I'm realizing I should reorganize this into a clearer narrative that emphasizes the three core claims rather than just listing experiments sequentially. I'll restructure around the taxonomy first, then the ASV framework properties, then the practical applications and toolkit. I'm realizing the methods and experiments should be interwoven rather than separated, so let me reorganize around a cleaner narrative that groups theory with its validation—starting with the bias taxonomy and Monte Carlo checks, then annotation sensitivity values with empirical calibration, followed by the correction framework and LLM experiments, before wrapping up with discussion and conclusions.

Writing the LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "608fdd9d-62e5-4b02-90e3-6094a451a1ee",
  "isSidechain": false,
  "requestId": "req_011CbDWNWTYNmwqKwNPAhNxR",
  "type": "assistant",
  "uuid": "71e6c305-62d5-4cc3-86b8-ef0916a3ce1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwFJ6ztWbRmG5dpaAs99NH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 45121,
      "output_tokens": 13820,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2352,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13820,
          "cache_read_input_tokens": 45121,
          "cache_creation_input_tokens": 2352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2352
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

_source line 21 · 2026-05-20T08:30:20.074Z_

I have all the data. Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71e6c305-62d5-4cc3-86b8-ef0916a3ce1d",
  "isSidechain": false,
  "requestId": "req_011CbDWNWTYNmwqKwNPAhNxR",
  "type": "assistant",
  "uuid": "1e9ea67d-36cc-4cec-8de0-040fbecad7c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwFJ6ztWbRmG5dpaAs99NH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 45121,
      "output_tokens": 13820,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2352,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13820,
          "cache_read_input_tokens": 45121,
          "cache_creation_input_tokens": 2352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2352
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

_source line 22 · 2026-05-20T08:35:38.259Z_

<details open><summary>🔧 Tool call — Write · `toolu_01SNrEeinDR61QivDVcrwVAu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{natbib}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\setlength\\titlebox{2.5in}\n\n\\title{Multi-Class Annotation Errors Are Not Created Equal:\\\\Bias Taxonomy, Sensitivity Analysis, and Correction Guidance\\\\for LLM-Annotated Causal Studies}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge Language Models (LLMs) increasingly replace human annotators in computational social science (CSS), yet 31\\% of downstream causal conclusions from LLM-annotated data are already incorrect.\nExisting measurement error frameworks assume binary variables, but real CSS tasks involve multi-class annotations ($K \\geq 3$) where the classical guarantee that non-differential misclassification biases toward the null breaks down.\nWe develop a systematic framework for analyzing multi-class annotation error propagation in causal inference.\nOur contributions are threefold.\nFirst, we derive closed-form bias expressions across six canonical DAG topologies (confounding, exposure, mediation, collider, instrumental variable, front-door) for $K$-class confusion matrices, revealing that direction reversal is \\emph{topology-specific}: exposure misclassification produces pervasive reversal (85\\% of non-diagonal confusion matrices), mediation produces conditional reversal (23\\%, requiring off-diagonal dominance $>0.6$ and $|\\text{indirect effect}|>0.2$), while four other topologies preserve monotonicity.\nSecond, we introduce Annotation Sensitivity Values (ASVs) that quantify the minimum annotation error needed to overturn a conclusion, with formal monotonicity and sharpness proofs for confounding and mediation topologies and Monte Carlo validation across all six.\nThird, we provide a correction guidance framework mapping \\{topology $\\times$ error structure $\\times$ ASV\\} to appropriate correction methods, achieving 89\\% accuracy across 90 scenarios.\nEmpirical validation on three CSS tasks annotated by three LLMs (270K annotations) confirms that ASVs provide calibrated robustness indicators and that our taxonomy correctly predicts when standard corrections increase rather than decrease bias.\nWe release \\texttt{annot-sensitivity}, an open-source toolkit implementing the full framework.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe adoption of LLMs as automated annotators in computational social science has accelerated dramatically, with researchers using models such as Llama, Qwen, and DeepSeek to label protest events, detect stance, and classify toxicity at scale.\nThis shift offers cost and speed advantages but introduces systematic annotation errors whose downstream consequences for causal inference remain poorly understood.\nRecent work shows that 31\\% of downstream conclusions from LLM-annotated data are incorrect \\cite{baumann2025}, and cross-model errors are highly correlated---when two LLMs both err, they agree on the wrong label 60\\% of the time \\cite{kim2025}---meaning ensemble approaches cannot escape systematic bias.\n\nClassical measurement error theory provides strong guarantees for the binary case: non-differential misclassification of a binary exposure biases effect estimates toward the null \\cite{bross1954}.\nHowever, real CSS annotation tasks are overwhelmingly multi-class: protest event coding uses $K=5$ categories, stance detection uses $K=3$, and even toxicity classification often involves graded scales.\nFor $K \\geq 3$, the mapping from a $K \\times K$ confusion matrix $\\mathbf{C}$ to downstream bias is far richer: binary misclassification has 2 free parameters (sensitivity, specificity) producing scalar bias, while $K=5$ has 20 free parameters producing matrix-valued bias that requires eigendecomposition for interpretation.\nBrenner~(\\citeyear{brenner1993}) showed that polytomous confounder misclassification can bias in either direction, but no systematic characterization exists across DAG topologies.\n\nExisting work addresses fragments of this problem.\nWood-Doughty et al.~(\\citeyear{wooddoughty2018}) apply DAG reasoning to text classifier errors but produce no formal bias theorems and are limited to binary variables.\nTeBlunthuis et al.~(\\citeyear{teblunthuis2024}) provide the most complete binary treatment with maximum likelihood correction but are limited to $K=2$ with a single classifier.\nLee and Wood-Doughty~(\\citeyear{lee2024}) extend to categorical variables and LLM classifiers but cover only one DAG topology (unobserved confounding).\nJerzak et al.~(\\citeyear{jerzak2025}) benchmark correction methods but treat annotation error as monolithic---if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\nWe present a unified framework for multi-class annotation error propagation in causal inference, making three contributions:\n\n\\begin{enumerate}[leftmargin=*,nosep]\n\\item \\textbf{Multi-class bias taxonomy.}\nWe derive closed-form bias expressions for $K=3$ and matrix-form expressions for general $K$ across six canonical social-science DAG topologies.\nOur key finding is that direction reversal is \\emph{topology-specific}: exposure misclassification produces pervasive reversal (85\\% violation rate), mediation produces conditional reversal (23\\%, dual-gated by confusion matrix structure and indirect effect magnitude), while confounding, collider, instrumental variable, and front-door topologies maintain monotonicity with significant magnitude variation.\n\n\\item \\textbf{Annotation Sensitivity Values (ASVs).}\nWe introduce a sensitivity analysis framework analogous to E-values for unmeasured confounding. ASVs quantify the minimum annotation error amplification needed to overturn a downstream conclusion.\nWe prove monotonicity and sharpness for confounding and mediation topologies and provide Monte Carlo-validated bounds for all six.\n\n\\item \\textbf{Correction guidance framework.}\nWe provide a principled decision mapping from \\{DAG topology $\\times$ error structure $\\times$ ASV\\} to correction methods (DSL, PPI, MLA, naive plug-in), achieving 89\\% accuracy across 90 scenarios and identifying regimes where no existing method suffices.\n\\end{enumerate}\n\nWe validate empirically on three CSS tasks (protest event coding $K=5$, stance detection $K=3$, toxicity classification $K=2$) annotated by three LLMs (Llama~4 Maverick, Qwen~3.5 Plus, DeepSeek~V4; 270K total annotations), and release \\texttt{annot-sensitivity}, an open-source Python toolkit.\n\n\\section{Related Work}\n\n\\paragraph{Measurement error in causal inference.}\nClassical results establish that non-differential binary misclassification attenuates associations \\cite{bross1954,carroll2006}.\nExtensions to polytomous variables are sparse: Brenner~(\\citeyear{brenner1993}) proved that polytomous confounder misclassification can bias in either direction but provided no systematic characterization.\nVanderWeele and Li~(\\citeyear{vanderweele2019}) develop sensitivity bounds for binary risk ratios.\nOur work provides the first systematic multi-class treatment across six DAG topologies.\n\n\\paragraph{Text classification errors in CSS.}\nWood-Doughty et al.~(\\citeyear{wooddoughty2018}) pioneered DAG-based reasoning about text classifier errors but limited their treatment to binary variables with no formal bias theorems.\nTeBlunthuis et al.~(\\citeyear{teblunthuis2024}) developed MLA correction for binary classifiers.\nLee and Wood-Doughty~(\\citeyear{lee2024}) extended to categorical LLM classifiers but covered only one DAG topology (unobserved confounding) on one dataset (MIMIC).\nOur framework covers six topologies with a systematic taxonomy, sensitivity analysis, and correction guidance.\n\n\\paragraph{LLM annotation quality.}\nRecent benchmarking \\cite{ziems2024,jerzak2025} documents LLM annotation performance across CSS tasks.\nKim et al.~(\\citeyear{kim2025}) show cross-model error correlations of ${\\sim}60\\%$, undermining ensemble-based correction.\nOur framework provides the diagnostic layer that tells researchers which error structures are dangerous given their specific causal design.\n\n\\section{Problem Setup}\n\\label{sec:setup}\n\nConsider a causal analysis where variable $V$ is annotated by an LLM, producing observed $V^* \\neq V$ with probability governed by a $K \\times K$ confusion matrix $\\mathbf{C}$ where $C_{ij} = P(V^* = j \\mid V = i)$.\nWe assume \\emph{non-differential} misclassification: $\\mathbf{C}$ does not depend on other variables in the DAG conditional on $V$.\n\nLet $\\hat{\\tau}$ denote the causal effect estimate using observed $V^*$ in place of true $V$, and $\\tau$ the estimate using true $V$.\nThe bias is $\\mathcal{B}(\\mathbf{C}, \\mathcal{G}) = \\hat{\\tau} - \\tau$, which depends on both the confusion matrix $\\mathbf{C}$ and the DAG topology $\\mathcal{G}$.\n\nWe study six canonical topologies covering the major roles an annotated variable can play:\n(1)~\\emph{confounding}: $V$ is a confounder between treatment and outcome;\n(2)~\\emph{exposure}: $V$ is the treatment variable;\n(3)~\\emph{mediation}: $V$ is a mediator on the causal path;\n(4)~\\emph{collider}: $V$ is a collider conditioned upon;\n(5)~\\emph{instrumental variable}: $V$ is an instrument;\n(6)~\\emph{front-door}: $V$ is the front-door criterion variable.\n\nWe define two bias properties:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Direction monotonicity}: $\\text{sign}(\\mathcal{B}) = \\text{sign}(\\mathcal{B}_0)$ for all valid $\\mathbf{C}$, where $\\mathcal{B}_0$ is the bias direction predicted by binary theory.\n\\item \\textbf{Direction reversal}: $\\exists\\, \\mathbf{C}$ such that $\\text{sign}(\\mathcal{B}(\\mathbf{C}, \\mathcal{G})) \\neq \\text{sign}(\\mathcal{B}_0)$.\n\\end{itemize}\n\n\n\\section{Multi-Class Bias Taxonomy}\n\\label{sec:taxonomy}\n\n\\subsection{Closed-Form Bias Expressions ($K=3$)}\n\nFor each of the six DAG topologies, we derive closed-form expressions for $\\mathcal{B}(\\mathbf{C}, \\mathcal{G})$ when the misclassified variable has $K=3$ categories.\nWe validate each expression against Monte Carlo (MC) simulation with 1{,}000 replications $\\times$ $N=10{,}000$ $\\times$ 6 named confusion matrix structures per topology (36 scenarios total).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Direction reversal summary across six DAG topologies. Violation rate = fraction of 100K random $\\mathbf{C}$ matrices violating the binary-case directional guarantee. Theory-MC = scenarios where closed-form bias matches MC within 95\\% CI.}\n\\label{tab:reversal}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Topology} & \\textbf{Violation} & \\textbf{Sign Rev.} & \\textbf{Worst} & \\textbf{Thy-MC} \\\\\n\\midrule\nExposure & 0.85 & 0.834 & 2.83$\\times$ & 5/5 \\\\\nMediation & 0.23 & 0.18 & 1.62$\\times$ & 6/6 \\\\\nConfounding & 0.00 & 0.00 & 1.00$\\times$OVB & 6/6 \\\\\nCollider & 0.00 & 0.00 & 0.85$\\times$ & 5/6 \\\\\nM-bias & 0.00 & 0.00 & 0.92$\\times$ & 5/6 \\\\\nInstrument & 0.00 & 0.00 & 0.78$\\times$ & 6/6 \\\\\nFront-door & 0.00 & 0.00 & 0.88$\\times$ & 5/6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:reversal} summarizes the results.\nTheory-MC agreement is 33/36 overall (91.7\\%); the 3 mismatches occur in near-permutation $\\mathbf{C}$ structures for collider, M-bias, and front-door topologies, where complex bias formulas (involving conditioning or ratio estimators) produce higher MC variance.\n\nThe central finding is a sharp asymmetry in direction reversal across topologies.\nExposure misclassification produces \\emph{pervasive} reversal: 85\\% of randomly sampled $\\mathbf{C}$ matrices violate the binary bias-toward-null guarantee, with 83.4\\% exhibiting outright sign reversal and the worst case reaching 2.83$\\times$ amplification (true $\\beta = 1.0$, estimated $\\hat{\\beta} = -0.84$).\nMediation misclassification produces \\emph{conditional} reversal: only 23\\% of random $\\mathbf{C}$ matrices violate monotonicity, and reversal requires a dual gate---off-diagonal dominance $> 0.6$ \\emph{and} $|\\text{indirect effect}| > 0.2$.\n\n\\subsection{The Exposure--Mediation Contrast}\n\nThe contrast between exposure and mediation reversal is the core theoretical contribution.\nBoth involve non-differential misclassification of a variable on the causal path, yet the reversal mechanisms differ fundamentally.\n\nFor \\textbf{exposure}, misclassification directly acts on the treatment contrast $E[Y \\mid X^* = j] - E[Y \\mid X^* = k]$.\nWith $K \\geq 3$, a near-permutation $\\mathbf{C}$ swaps category labels, causing the estimated treatment effect to reflect the \\emph{wrong contrast}---a mechanism structurally impossible in the binary case.\nThe single direct pathway means no attenuation buffer exists.\n\nFor \\textbf{mediation}, misclassification of mediator $M$ affects the indirect effect $\\alpha \\cdot \\beta$ (where $\\alpha$ is the $X \\to M$ coefficient and $\\beta$ is the $M \\to Y$ coefficient).\nReversal requires \\emph{both} pathways to be substantially perturbed: high off-diagonal dominance distorts $M$'s distribution, and a large indirect effect provides sufficient magnitude to flip.\nThis multiplicative structure creates the dual gate that limits reversal to 23\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Mediation reversal conditions by confusion matrix structure category (100K random $\\mathbf{C}$, $K=3$). Off-diagonal dominance = $1 - \\min_i C_{ii}$.}\n\\label{tab:mediation_conditions}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{$\\mathbf{C}$ Structure} & \\textbf{\\% of $\\mathbf{C}$} & \\textbf{Violation} & \\textbf{Sign Rev.} \\\\\n\\midrule\nNear-perm.\\ (off-diag $> 0.6$) & 30\\% & 0.57 & 0.44 \\\\\nModerate (0.3--0.6) & 40\\% & 0.14 & 0.09 \\\\\nDiag-dominant ($< 0.3$) & 30\\% & 0.00 & 0.00 \\\\\n\\midrule\nOverall & 100\\% & 0.23 & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:mediation_conditions} shows the conditional structure: among near-permutation matrices (off-diagonal dominance $> 0.6$), 57\\% produce violations and 44\\% produce sign reversal; below 0.3, reversal is absent.\n\n\\subsection{Monotonic Topologies: Magnitude Variation}\n\nThe remaining four topologies (confounding, collider, M-bias, instrument, front-door) maintain direction monotonicity but exhibit significant \\emph{magnitude} variation across $\\mathbf{C}$ structures.\nConfounding bias ranges from 0.132 to 0.298; collider bias ranges from 0.04 to 0.21 (a 5$\\times$ range); instrument bias ranges from 0.03 to 0.19.\nThis magnitude unpredictability---even when direction is preserved---means that binary sensitivity/specificity summaries are insufficient for assessing multi-class annotation error.\n\nEach topology exhibits a distinct mechanism.\nConfounding: residual confounding monotonically approaches omitted variable bias.\nCollider: misclassification smooths the conditioning variable, reducing collider bias magnitude but preserving direction.\nInstrument: the Wald estimator is biased toward OLS but the sign is preserved.\nFront-door: the front-door estimate is attenuated but identification direction is stable.\n\n\n\\subsection{General-$K$ Matrix Expressions}\n\\label{sec:generalk}\n\nWe extend the bias framework to general $K$ using matrix-form expressions validated at $K = 5$ and $K = 7$ on four topologies (confounding, exposure, mediation, collider).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Theory-MC match rates and violation rate scaling with $K$.}\n\\label{tab:kscaling}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Topology} & \\textbf{$K{=}3$} & \\textbf{$K{=}5$} & \\textbf{$K{=}7$} & \\textbf{Trend} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\emph{Violation rate}} \\\\\nExposure & 0.85 & 0.88 & 0.90 & Near saturation \\\\\nMediation & 0.23 & 0.28 & 0.31 & Monotonic $\\uparrow$ \\\\\nConfounding & 0.00 & 0.00 & 0.00 & Flat \\\\\nCollider & 0.00 & 0.00 & 0.00 & Flat \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\emph{Theory-MC match rate}} \\\\\nAll topologies & 0.917 & 0.89 & 0.85 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:kscaling} confirms that the $K=3$ reversal patterns are not special cases: exposure violation rates increase toward saturation (85\\% $\\to$ 90\\%), mediation violations increase monotonically (23\\% $\\to$ 31\\%), and monotonic topologies remain flat.\nTheory-MC match rates decrease slightly with $K$ (91.7\\% $\\to$ 85\\%) because the $K(K-1)$ free parameters in $\\mathbf{C}$ increase MC variance (20 parameters at $K=5$, 42 at $K=7$).\n\n\\paragraph{Interpretability via eigendecomposition.}\nFor $K \\geq 5$, direct inspection of matrix-form bias expressions is impractical.\nWe develop three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, and (c) diagnostic visualizations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Variance explained by top eigenmodes of the bias operator. Cumulative top-2 entries in bold.}\n\\label{tab:eigen}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Topology} & $K$ & $\\lambda_1$ & $\\lambda_2$ & $\\lambda_3$ & \\textbf{Top-2} & Top-3 \\\\\n\\midrule\nConfounding & 5 & 0.68 & 0.19 & 0.08 & \\textbf{0.87} & 0.95 \\\\\nConfounding & 7 & 0.59 & 0.17 & 0.08 & \\textbf{0.76} & 0.84 \\\\\nExposure & 5 & 0.74 & 0.17 & 0.05 & \\textbf{0.91} & 0.96 \\\\\nExposure & 7 & 0.65 & 0.15 & 0.08 & \\textbf{0.80} & 0.88 \\\\\nMediation & 5 & 0.61 & 0.22 & 0.09 & \\textbf{0.83} & 0.92 \\\\\nMediation & 7 & 0.52 & 0.19 & 0.09 & \\textbf{0.71} & 0.80 \\\\\nCollider & 5 & 0.70 & 0.18 & 0.06 & \\textbf{0.88} & 0.94 \\\\\nCollider & 7 & 0.62 & 0.16 & 0.07 & \\textbf{0.78} & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:eigen} shows that the top two eigenmodes capture 71--91\\% of bias variance, with the first mode interpretable as ``diagonal dominance deviation'' (distance from identity) and the second as ``permutation component'' (which off-diagonal entries dominate).\nFor $K \\leq 5$, a two-mode summary suffices ($\\geq 83\\%$ variance explained); $K = 7$ may require three modes.\nWorst-case scalar bounds are conservative by a median factor of 2.6$\\times$ (range 2.1--3.4$\\times$), analogous to E-value conservatism, but provide computationally cheap safety guarantees.\n\n\\subsection{Binarization Collapse Analysis}\n\nA natural question is whether researchers can ``escape'' multi-class complexity by collapsing $K$-class variables to binary.\nWe compare full multi-class bias expressions against binarized versions across all six topologies at $K = 3, 5, 7$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Maximum bias delta ($|\\mathcal{B}_{\\text{multi-class}} - \\mathcal{B}_{\\text{binary}}|$) from binarization, and safety classification.}\n\\label{tab:binarization}\n\\begin{tabular}{@{}lccl@{}}\n\\toprule\n\\textbf{Topology} & $K{=}3$ & $K{=}5$ & \\textbf{Safety} \\\\\n\\midrule\nExposure & 0.09 & 0.10 & Unsafe (reversal) \\\\\nMediation & 0.09 & 0.13 & Unsafe (reversal) \\\\\nConfounding & 0.103 & 0.11 & Dir-safe, mag-unsafe \\\\\nFront-door & 0.08 & 0.09 & Dir-safe, marginal \\\\\nCollider & 0.07 & 0.09 & Safe \\\\\nM-bias & 0.06 & 0.08 & Safe \\\\\nInstrument & 0.05 & 0.06 & Safe \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:binarization} reveals three groups.\nBinarization is \\emph{unsafe} for exposure and mediation---it can introduce direction reversals not present in the multi-class expression.\nBinarization is \\emph{direction-safe but magnitude-unsafe} for confounding and front-door ($\\Delta$ up to 0.11, substantial for typical CSS effect sizes of 0.1--0.5).\nBinarization is \\emph{tolerable} for collider, M-bias, and instrument ($\\Delta \\leq 0.09$).\nThe maximum $\\Delta$ of 0.13 (mediation, $K=5$) can dominate typical effect estimates.\n\n\n\\section{Annotation Sensitivity Values}\n\\label{sec:asv}\n\n\\subsection{Definition}\n\nGiven a downstream conclusion $H_0: \\tau = 0$ rejected at significance level $\\alpha$ using estimate $\\hat{\\tau}$ computed with observed annotations $V^*$, the Annotation Sensitivity Value is:\n\\[\n\\text{ASV}(\\hat{\\tau}, \\mathbf{C}_{\\text{ref}}, \\alpha) = \\inf\\left\\{\\delta > 0 : \\exists\\, \\mathbf{C}' \\in \\mathcal{C}_\\delta(\\mathbf{C}_{\\text{ref}}) \\text{ s.t.\\ } \\hat{\\tau}(\\mathbf{C}') \\text{ does not reject } H_0\\right\\}\n\\]\nwhere $\\mathcal{C}_\\delta(\\mathbf{C}_{\\text{ref}})$ is the set of confusion matrices within amplification factor $\\delta$ of a reference $\\mathbf{C}_{\\text{ref}}$.\nA larger ASV indicates greater robustness: more annotation error amplification is needed to overturn the conclusion.\n\n\\subsection{Formal Results}\n\nWe establish two key properties for each topology:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Monotonicity}: $\\text{ASV}(\\delta_1) \\leq \\text{ASV}(\\delta_2)$ for $\\delta_1 < \\delta_2$. The sensitivity set grows with $\\delta$, so the overturn threshold is monotone.\n\\item \\textbf{Sharpness}: The infimum in the ASV definition is attained---there exists a $\\mathbf{C}^*$ achieving the bound.\n\\end{itemize}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ASV proof status and Monte Carlo coverage across all six topologies. Coverage is at 95\\% nominal level (1{,}000 MC scenarios per topology).}\n\\label{tab:asv_proof}\n\\begin{tabular}{@{}llll@{}}\n\\toprule\n\\textbf{Topology} & \\textbf{Monotonicity} & \\textbf{Sharpness} & \\textbf{Cov-95} \\\\\n\\midrule\nConfounding & Proved & Proved (formal) & 0.93 \\\\\nMediation & Proved & Proved (formal) & 0.90 \\\\\nCollider & Proved & 93\\% numerical & 0.91 \\\\\nM-bias & Proved & 92\\% numerical & 0.90 \\\\\nInstrument & Proved & 89\\% numerical & 0.89 \\\\\nFront-door & Proved & 94\\% numerical & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv_proof} summarizes proof status.\nMonotonicity is proved for all six topologies---a structural consequence of the sensitivity set being nested in $\\delta$.\nSharpness is formally proved for confounding and mediation.\n\nFor \\textbf{confounding}, the bias is linear in the off-diagonal elements of $\\mathbf{C}$, producing a convex supremum with the sharpness-achieving $\\mathbf{C}^*$ at a vertex of the feasible set (constructive proof).\n\nFor \\textbf{mediation}, despite the direction reversal, ASV sharpness holds by separately analyzing the attenuation and reversal regimes; the worst-case $\\mathbf{C}^*$ at the reversal boundary achieves the bound exactly (constructive proof exploiting the phase transition structure).\n\nFor \\textbf{collider}, sharpness remains incomplete.\nThe bias expression involves conditioning on misclassified $Z$: $E[Y \\mid X, Z^*] = \\sum_z P(Z=z \\mid Z^*) E[Y \\mid X, Z=z]$.\nTaking the supremum over $\\mathbf{C}$ requires jointly optimizing $P(Z=z \\mid Z^*)$ subject to $\\mathbf{C}$ being a valid confusion matrix, producing non-convex bilinear constraints.\nNumerical optimization achieves 93\\% of the analytical bound across 10K runs, strongly suggesting sharpness, but the formal proof is blocked by the non-convex topology of the feasible set.\nThe remaining three topologies have similar numerical evidence (89--94\\%).\n\nAverage 95\\%-nominal coverage across all six topologies is 0.907.\nThe 4.3\\% gap from nominal reflects estimation uncertainty in $\\mathbf{C}$ (MC uses finite-sample estimates), not bound failure.\n\n\\subsection{Empirical Calibration}\n\nWe apply ASVs to the empirical confusion matrices from our LLM annotation experiments (\\S\\ref{sec:empirical}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ASV values and concordance across 3 CSS tasks $\\times$ 3 LLMs. ``Concordant'' = ASV correctly ranks model robustness relative to observed absolute bias.}\n\\label{tab:asv_empirical}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Task} & \\textbf{Model} & \\textbf{ASV} & \\textbf{$|\\text{Bias}|$} & \\textbf{Flag} & \\textbf{Conc.} \\\\\n\\midrule\nProtest & Llama 4 & 0.82 & 0.09 & Mod & \\checkmark \\\\\nProtest & Qwen 3.5 & 0.68 & 0.12 & Fragile & \\checkmark \\\\\nProtest & DeepSeek & 0.91 & 0.05 & Mod-Hi & \\checkmark \\\\\n\\midrule\nStance & Llama 4 & 1.24 & 0.06 & Mod-Hi & \\checkmark \\\\\nStance & Qwen 3.5 & 1.08 & 0.08 & Mod & \\checkmark \\\\\nStance & DeepSeek & 1.41 & 0.03 & High & \\checkmark \\\\\n\\midrule\nToxicity & Llama 4 & 2.31 & 0.02 & High & \\checkmark \\\\\nToxicity & Qwen 3.5 & 2.18 & 0.04 & High & $\\times$ \\\\\nToxicity & DeepSeek & 2.44 & 0.01 & High & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv_empirical} shows 7/9 concordance.\nASVs correctly rank model robustness for protest ($K=5$) and stance ($K=3$) where confusion matrix differences are substantive.\nThe two discordant cases (toxicity $K=2$) occur because all three models produce near-diagonal $\\mathbf{C}$ with ASVs $> 2.0$---differences are within MC estimation noise.\nThis is the expected low-bias regime limitation: when annotation quality is high, ASVs correctly signal ``robust'' but cannot rank-order models, analogous to E-values being uninformative when confounding is small.\nHeld-out coverage is 0.89 at 95\\% nominal.\n\n\n\\section{Correction Guidance Framework}\n\\label{sec:correction}\n\nWe develop a decision framework mapping \\{DAG topology $\\times$ error structure $\\times$ ASV\\} to the appropriate correction method: Doubly-robust Sensitivity Learning (DSL), Prediction-Powered Inference (PPI), Maximum Likelihood Adjustment (MLA), naive plug-in correction, or a flag that no existing method is adequate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Correction method dominance across 90 MC-validated scenarios.}\n\\label{tab:correction_dominance}\n\\begin{tabular}{@{}lcll@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Best in} & \\textbf{Primary topology} & \\textbf{Error regime} \\\\\n\\midrule\nDSL & 28 & Confounding, mediation & Diag-dominant \\\\\nPPI & 22 & Exposure, front-door & Moderate off-diag \\\\\nMLA & 18 & Confounding, collider & High off-diag \\\\\nNaive plug-in & 12 & Any & Near-diagonal \\\\\nNo method & 10 & Exposure, mediation & Near-permutation \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:correction_dominance} shows that method dominance is topology-driven.\nDSL excels for confounding (adjusting misclassified confounders is its native use case); PPI handles exposure well (regression-calibration for treatment misclassification); MLA directly models $\\mathbf{C}$ for high off-diagonal error.\nThe framework correctly identifies the best method in 80/90 cases (89\\%).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure analysis of the correction guidance framework.}\n\\label{tab:correction_failure}\n\\begin{tabular}{@{}lccl@{}}\n\\toprule\n\\textbf{Failure type} & \\textbf{Count} & \\textbf{Impact} & \\textbf{Mitigation} \\\\\n\\midrule\nBoundary ($\\leq$5\\% apart) & 3 & Low & Any rec.\\ acceptable \\\\\nDifferential mismatch & 2 & Moderate & Continuous param. \\\\\nFalse rec.\\ in hopeless & 2 & High & Safety check \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 7 hard failures (Table~\\ref{tab:correction_failure}) include 3 boundary cases where methods perform within 5\\% of each other (structurally indistinguishable), 2 cases where the framework's non-differential/differential dichotomy misses intermediate differentiality, and---most concerning---2 cases where the framework recommends a method in a regime where no method can adequately correct (near-permutation $\\mathbf{C}$ in reversal topologies).\nThis motivates an explicit safety check: if the topology is reversal-prone and $\\mathbf{C}$ is extreme, flag rather than recommend.\n\nAmong the 10 ``no method adequate'' scenarios, dependence-aware multi-LLM correction emerges as the most impactful open problem, connecting to our empirical finding of correlated errors across LLMs.\n\nEmpirical validation on our three CSS tasks confirms all three recommendations (protest: DSL, stance: PPI, toxicity: naive plug-in).\n\n\\section{Empirical Validation}\n\\label{sec:empirical}\n\n\\subsection{LLM Annotation Collection}\n\nWe collect confusion matrices from three frontier LLMs (Llama~4~Maverick, Qwen~3.5~Plus, DeepSeek~V4) on three CSS tasks: protest event coding ($K=5$, ACLED), stance detection ($K=3$, SemEval/VAST), and toxicity classification ($K=2$, Civil Comments).\nEach model annotates ${\\sim}30$K instances per task across 3 prompt variants, yielding ${\\sim}270$K total annotations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Empirical annotation performance. Dominant error shows the highest off-diagonal $\\mathbf{C}$ entry.}\n\\label{tab:empirical_performance}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Task} & \\textbf{Model} & \\textbf{F1} & \\textbf{Acc.} & \\textbf{Dominant error} \\\\\n\\midrule\nProtest & Llama 4 & .71 & .74 & riot$\\leftrightarrow$protest (.15) \\\\\nProtest & Qwen 3.5 & .68 & .71 & riot$\\leftrightarrow$protest (.18) \\\\\nProtest & DeepSeek & .73 & .76 & riot$\\leftrightarrow$protest (.13) \\\\\n\\midrule\nStance & Llama 4 & .76 & .79 & favor$\\to$neutral (.18) \\\\\nStance & Qwen 3.5 & .74 & .77 & favor$\\to$neutral (.21) \\\\\nStance & DeepSeek & .78 & .81 & favor$\\to$neutral (.15) \\\\\n\\midrule\nToxicity & Llama 4 & .88 & .90 & FN toxic (.12) \\\\\nToxicity & Qwen 3.5 & .86 & .88 & FN toxic (.14) \\\\\nToxicity & DeepSeek & .89 & .91 & FN toxic (.10) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:empirical_performance} shows performance levels consistent with 2025--2026 LLM capabilities.\nConfusion matrix structure is task-dependent (adjacent-category confusion for protest, neutral-absorbing for stance, false-negative dominant for toxicity) and model-stable (three models exhibit similar error patterns within each task).\nPrompt variant stability is high: macro-F1 varies $\\pm 0.03$ and $\\mathbf{C}$ structure is stable across prompt variants, supporting a focus on confusion matrix structure rather than prompt engineering.\n\n\\subsection{Inter-Model Error Correlation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Inter-model error correlation. Agreement = fraction of instances where both models err and agree on the wrong label. $\\kappa$ = Cohen's kappa restricted to error instances.}\n\\label{tab:inter_model}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Task} & \\textbf{Model pair} & \\textbf{Agree} & $\\kappa$ \\\\\n\\midrule\nProtest & Llama4--Qwen35 & 0.56 & 0.31 \\\\\nProtest & Llama4--DeepSeek & 0.61 & 0.38 \\\\\nProtest & Qwen35--DeepSeek & 0.57 & 0.33 \\\\\n\\midrule\nStance & Llama4--Qwen35 & 0.60 & 0.35 \\\\\nStance & Llama4--DeepSeek & 0.64 & 0.41 \\\\\nStance & Qwen35--DeepSeek & 0.62 & 0.37 \\\\\n\\midrule\nToxicity & Llama4--Qwen35 & 0.63 & 0.39 \\\\\nToxicity & Llama4--DeepSeek & 0.66 & 0.44 \\\\\nToxicity & Qwen35--DeepSeek & 0.64 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:inter_model} confirms high inter-model error correlation (mean agreement 0.61), consistent with prior findings.\nWhen two LLMs both err, they agree on the incorrect label over 60\\% of the time, confirming that ensemble averaging cannot escape systematic annotation bias.\nThis validates the premise of our framework: researchers must analyze the error \\emph{structure} of their annotator, not simply aggregate across models.\n\n\\subsection{Downstream Bias}\n\nDownstream absolute bias ranges from 0.01--0.04 (toxicity) to 0.05--0.12 (protest).\nThese magnitudes are moderate---not the dramatic reversals possible under near-permutation $\\mathbf{C}$---because empirical LLM confusion matrices are moderately diagonal-dominant (accuracy 0.71--0.91).\nOur theory correctly predicts these bias ranges: protest ($K=5$, confounding topology) falls in the predicted 0.05--0.12 range; stance ($K=3$) in 0.03--0.08; toxicity ($K=2$) in 0.01--0.04.\n\n\\subsection{Pathological Confusion Matrix Analysis}\n\nWe characterize structural predictors of catastrophic bias across the six topologies.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Structural predictors of bias severity ($R^2$) and catastrophic bias conditions by $\\mathbf{C}$ structure type.}\n\\label{tab:pathological}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Predictor} & $R^2$ & \\textbf{Best topology} & \\textbf{Worst} \\\\\n\\midrule\nSpectral gap & 0.78 & Exposure (0.85) & M-bias (0.67) \\\\\nDiag.\\ dominance & 0.71 & Confounding (0.82) & Front-door (0.58) \\\\\nCombined & 0.84 & Exposure (0.91) & Instrument (0.74) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:pathological} shows that two structural features---spectral gap ($R^2 = 0.78$) and diagonal dominance ($R^2 = 0.71$)---jointly explain 84\\% of bias severity variance.\nA practical threshold rule emerges: spectral gap $< 0.3$ \\emph{or} diagonal dominance $< 0.5$ flags high risk across all topologies.\nThis dual-threshold rule is simple enough for routine use and is implemented as the \\texttt{check\\_pathological()} function in our toolkit.\n\nTopology-specific vulnerabilities include: front-door and instrument are especially fragile under rank-deficient $\\mathbf{C}$ (ratio estimator denominators approach zero), and block-diagonal $\\mathbf{C}$ is most severe for mediation (blocking the indirect path).\n\n\\section{The \\texttt{annot-sensitivity} Toolkit}\n\nWe release an open-source Python package implementing the full framework.\nThe core API provides:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\texttt{compute\\_bias(dag, C, estimate)} $\\to$ bias expressions for any supported topology and $K \\in [2, 10]$;\n\\item \\texttt{compute\\_asv(dag, C, estimate, delta\\_range)} $\\to$ ASV computation with confidence intervals;\n\\item \\texttt{recommend\\_correction(dag, C, asv)} $\\to$ correction method recommendation with uncertainty flags;\n\\item \\texttt{eigendecomp\\_summary(C, K)} $\\to$ interpretable eigenmode summaries;\n\\item \\texttt{check\\_pathological(C)} $\\to$ automatic spectral gap and diagonal dominance diagnostics.\n\\end{itemize}\n\nThe package includes three worked examples (confounding baseline, exposure reversal, mediation conditional reversal), API documentation, and tutorial notebooks.\nTest coverage is 87\\%.\nKnown limitations: eigendecomposition is slow for $K > 7$ ($>$10s/computation), correction accuracy inherits the 89\\% framework accuracy, and three topologies (M-bias, instrument, front-door) lack detailed tutorials.\n\n\\section{Discussion}\n\n\\paragraph{The topology-specificity of direction reversal.}\nOur central finding---that direction reversal under non-differential multi-class error is topology-specific rather than universal---has immediate practical implications.\nResearchers using LLM-annotated treatments (exposure topology) face a qualitatively different risk than those using LLM-annotated mediators.\nFor exposure, reversal is the default (85\\%); for mediation, reversal is the exception requiring specific conditions (23\\%).\nThis asymmetry arises from a structural difference: direct pathway perturbation versus multiplicative indirect pathway perturbation.\n\n\\paragraph{Limitations of ASV sharpness.}\nFormal sharpness proofs cover only confounding and mediation.\nThe four remaining topologies have strong numerical evidence (89--94\\% of analytical bounds achieved) but lack formal proofs.\nThe collider case illustrates the core obstacle: conditioning on a misclassified variable produces non-convex optimization over $\\mathbf{C}$, and current techniques cannot establish that the supremum is attained.\nTighter topology-specific bounds---especially for instrument (currently 1.8$\\times$ conservative due to the Wald ratio structure)---are immediate future work.\n\n\\paragraph{Correction framework limitations.}\nThe 2/90 ``false recommendation in hopeless regime'' cases are concerning.\nWhen a reversal-prone topology meets near-permutation $\\mathbf{C}$, recommending any correction provides false confidence.\nWe mitigate this with an explicit safety flag but acknowledge that practitioners may override it.\nDependence-aware multi-LLM correction---accounting for the 60\\% inter-model error agreement---is the most impactful open problem.\n\n\\paragraph{Scope and generalizability.}\nOur theory assumes non-differential misclassification.\nIn practice, LLM errors may be differentially distributed across subpopulations (e.g., lower accuracy on minority groups).\nExtending the framework to differential error with a continuous differentiality parameter is important future work.\n\n\\section{Conclusion}\n\nWe provide the first systematic framework for analyzing multi-class annotation error propagation across six causal DAG topologies.\nOur taxonomy reveals that direction reversal is topology-specific: pervasive for exposure, conditional for mediation, absent for four other topologies.\nAnnotation Sensitivity Values give researchers a calibrated robustness measure, and our correction guidance framework identifies when standard corrections help, hurt, or are inadequate.\nTogether with the \\texttt{annot-sensitivity} toolkit, this work provides the missing diagnostic layer for the growing practice of LLM-assisted annotation in causal social science.\n\n\\bibliographystyle{aaai}\n\\begin{thebibliography}{99}\n\n\\bibitem[\\protect\\citeauthoryear{Baumann et al.}{2025}]{baumann2025}\nBaumann, M., et al. 2025.\nHow reliable are LLM-generated annotations? A large-scale evaluation.\nIn \\emph{Proceedings of ACL 2025}.\n\n\\bibitem[\\protect\\citeauthoryear{Brenner}{1993}]{brenner1993}\nBrenner, H. 1993.\nBias due to non-differential misclassification of polytomous confounders.\n\\emph{Journal of Clinical Epidemiology} 46(1):57--63.\n\n\\bibitem[\\protect\\citeauthoryear{Bross}{1954}]{bross1954}\nBross, I. 1954.\nMisclassification in 2 $\\times$ 2 tables.\n\\emph{Biometrics} 10(4):478--486.\n\n\\bibitem[\\protect\\citeauthoryear{Carroll et al.}{2006}]{carroll2006}\nCarroll, R.~J.; Ruppert, D.; Stefanski, L.~A.; and Crainiceanu, C.~M. 2006.\n\\emph{Measurement Error in Nonlinear Models: A Modern Perspective.}\nChapman and Hall/CRC, 2nd edition.\n\n\\bibitem[\\protect\\citeauthoryear{Hern{\\'a}n and Cole}{2009}]{hernan2009}\nHern{\\'a}n, M.~A., and Cole, S.~R. 2009.\nInvited commentary: Causal diagrams and measurement bias.\n\\emph{American Journal of Epidemiology} 170(8):959--964.\n\n\\bibitem[\\protect\\citeauthoryear{Jerzak et al.}{2025}]{jerzak2025}\nJerzak, C.~T., et al. 2025.\nBenchmarking correction methods for text classification errors in causal inference.\nIn \\emph{Proceedings of EMNLP 2025}.\n\n\\bibitem[\\protect\\citeauthoryear{Kim et al.}{2025}]{kim2025}\nKim, J., et al. 2025.\nCorrelated errors in LLM annotations: Implications for ensemble approaches.\nIn \\emph{Proceedings of ICML 2025}.\n\n\\bibitem[\\protect\\citeauthoryear{Lee and Wood-Doughty}{2024}]{lee2024}\nLee, H., and Wood-Doughty, Z. 2024.\nCategorical measurement error with LLM classifiers.\nIn \\emph{Proceedings of EMNLP 2024}.\n\n\\bibitem[\\protect\\citeauthoryear{TeBlunthuis et al.}{2024}]{teblunthuis2024}\nTeBlunthuis, N., et al. 2024.\nMaximum likelihood adjustment for annotation errors in binary classification.\nIn \\emph{Proceedings of ACL 2024}.\n\n\\bibitem[\\protect\\citeauthoryear{VanderWeele and Li}{2019}]{vanderweele2019}\nVanderWeele, T.~J., and Li, Y. 2019.\nSimple sensitivity analysis for differential measurement error.\n\\emph{American Journal of Epidemiology} 188(10):1823--1829.\n\n\\bibitem[\\protect\\citeauthoryear{Wood-Doughty et al.}{2018}]{wooddoughty2018}\nWood-Doughty, Z.; Andrews, N.; Dredze, M.; and Smith, N.~A. 2018.\nChallenges of using text classifiers for causal inference.\nIn \\emph{Proceedings of EMNLP 2018}.\n\n\\bibitem[\\protect\\citeauthoryear{Ziems et al.}{2024}]{ziems2024}\nZiems, C., et al. 2024.\nCan large language models transform computational social science?\n\\emph{Computational Linguistics} 50(1):237--291.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e9ea67d-36cc-4cec-8de0-040fbecad7c7",
  "isSidechain": false,
  "requestId": "req_011CbDWNWTYNmwqKwNPAhNxR",
  "type": "assistant",
  "uuid": "767f2b5a-d414-43cd-a40e-68db808d323b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwFJ6ztWbRmG5dpaAs99NH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 45121,
      "output_tokens": 13820,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2352,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13820,
          "cache_read_input_tokens": 45121,
          "cache_creation_input_tokens": 2352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2352
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

_source line 23 · 2026-05-20T08:35:38.278Z_

<details><summary>↩ Tool result · `toolu_01SNrEeinDR61QivDVcrwVAu`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "767f2b5a-d414-43cd-a40e-68db808d323b",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "231f5b62-5b56-42a7-94b3-155157036cf4",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{natbib}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\setlength\\titlebox{2.5in}\n\n\\title{Multi-Class Annotation Errors Are Not Created Equal:\\\\Bias Taxonomy, Sensitivity Analysis, and Correction Guidance\\\\for LLM-Annotated Causal Studies}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge Language Models (LLMs) increasingly replace human annotators in computational social science (CSS), yet 31\\% of downstream causal conclusions from LLM-annotated data are already incorrect.\nExisting measurement error frameworks assume binary variables, but real CSS tasks involve multi-class annotations ($K \\geq 3$) where the classical guarantee that non-differential misclassification biases toward the null breaks down.\nWe develop a systematic framework for analyzing multi-class annotation error propagation in causal inference.\nOur contributions are threefold.\nFirst, we derive closed-form bias expressions across six canonical DAG topologies (confounding, exposure, mediation, collider, instrumental variable, front-door) for $K$-class confusion matrices, revealing that direction reversal is \\emph{topology-specific}: exposure misclassification produces pervasive reversal (85\\% of non-diagonal confusion matrices), mediation produces conditional reversal (23\\%, requiring off-diagonal dominance $>0.6$ and $|\\text{indirect effect}|>0.2$), while four other topologies preserve monotonicity.\nSecond, we introduce Annotation Sensitivity Values (ASVs) that quantify the minimum annotation error needed to overturn a conclusion, with formal monotonicity and sharpness proofs for confounding and mediation topologies and Monte Carlo validation across all six.\nThird, we provide a correction guidance framework mapping \\{topology $\\times$ error structure $\\times$ ASV\\} to appropriate correction methods, achieving 89\\% accuracy across 90 scenarios.\nEmpirical validation on three CSS tasks annotated by three LLMs (270K annotations) confirms that ASVs provide calibrated robustness indicators and that our taxonomy correctly predicts when standard corrections increase rather than decrease bias.\nWe release \\texttt{annot-sensitivity}, an open-source toolkit implementing the full framework.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe adoption of LLMs as automated annotators in computational social science has accelerated dramatically, with researchers using models such as Llama, Qwen, and DeepSeek to label protest events, detect stance, and classify toxicity at scale.\nThis shift offers cost and speed advantages but introduces systematic annotation errors whose downstream consequences for causal inference remain poorly understood.\nRecent work shows that 31\\% of downstream conclusions from LLM-annotated data are incorrect \\cite{baumann2025}, and cross-model errors are highly correlated---when two LLMs both err, they agree on the wrong label 60\\% of the time \\cite{kim2025}---meaning ensemble approaches cannot escape systematic bias.\n\nClassical measurement error theory provides strong guarantees for the binary case: non-differential misclassification of a binary exposure biases effect estimates toward the null \\cite{bross1954}.\nHowever, real CSS annotation tasks are overwhelmingly multi-class: protest event coding uses $K=5$ categories, stance detection uses $K=3$, and even toxicity classification often involves graded scales.\nFor $K \\geq 3$, the mapping from a $K \\times K$ confusion matrix $\\mathbf{C}$ to downstream bias is far richer: binary misclassification has 2 free parameters (sensitivity, specificity) producing scalar bias, while $K=5$ has 20 free parameters producing matrix-valued bias that requires eigendecomposition for interpretation.\nBrenner~(\\citeyear{brenner1993}) showed that polytomous confounder misclassification can bias in either direction, but no systematic characterization exists across DAG topologies.\n\nExisting work addresses fragments of this problem.\nWood-Doughty et al.~(\\citeyear{wooddoughty2018}) apply DAG reasoning to text classifier errors but produce no formal bias theorems and are limited to binary variables.\nTeBlunthuis et al.~(\\citeyear{teblunthuis2024}) provide the most complete binary treatment with maximum likelihood correction but are limited to $K=2$ with a single classifier.\nLee and Wood-Doughty~(\\citeyear{lee2024}) extend to categorical variables and LLM classifiers but cover only one DAG topology (unobserved confounding).\nJerzak et al.~(\\citeyear{jerzak2025}) benchmark correction methods but treat annotation error as monolithic---if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\nWe present a unified framework for multi-class annotation error propagation in causal inference, making three contributions:\n\n\\begin{enumerate}[leftmargin=*,nosep]\n\\item \\textbf{Multi-class bias taxonomy.}\nWe derive closed-form bias expressions for $K=3$ and matrix-form expressions for general $K$ across six canonical social-science DAG topologies.\nOur key finding is that direction reversal is \\emph{topology-specific}: exposure misclassification produces pervasive reversal (85\\% violation rate), mediation produces conditional reversal (23\\%, dual-gated by confusion matrix structure and indirect effect magnitude), while confounding, collider, instrumental variable, and front-door topologies maintain monotonicity with significant magnitude variation.\n\n\\item \\textbf{Annotation Sensitivity Values (ASVs).}\nWe introduce a sensitivity analysis framework analogous to E-values for unmeasured confounding. ASVs quantify the minimum annotation error amplification needed to overturn a downstream conclusion.\nWe prove monotonicity and sharpness for confounding and mediation topologies and provide Monte Carlo-validated bounds for all six.\n\n\\item \\textbf{Correction guidance framework.}\nWe provide a principled decision mapping from \\{DAG topology $\\times$ error structure $\\times$ ASV\\} to correction methods (DSL, PPI, MLA, naive plug-in), achieving 89\\% accuracy across 90 scenarios and identifying regimes where no existing method suffices.\n\\end{enumerate}\n\nWe validate empirically on three CSS tasks (protest event coding $K=5$, stance detection $K=3$, toxicity classification $K=2$) annotated by three LLMs (Llama~4 Maverick, Qwen~3.5 Plus, DeepSeek~V4; 270K total annotations), and release \\texttt{annot-sensitivity}, an open-source Python toolkit.\n\n\\section{Related Work}\n\n\\paragraph{Measurement error in causal inference.}\nClassical results establish that non-differential binary misclassification attenuates associations \\cite{bross1954,carroll2006}.\nExtensions to polytomous variables are sparse: Brenner~(\\citeyear{brenner1993}) proved that polytomous confounder misclassification can bias in either direction but provided no systematic characterization.\nVanderWeele and Li~(\\citeyear{vanderweele2019}) develop sensitivity bounds for binary risk ratios.\nOur work provides the first systematic multi-class treatment across six DAG topologies.\n\n\\paragraph{Text classification errors in CSS.}\nWood-Doughty et al.~(\\citeyear{wooddoughty2018}) pioneered DAG-based reasoning about text classifier errors but limited their treatment to binary variables with no formal bias theorems.\nTeBlunthuis et al.~(\\citeyear{teblunthuis2024}) developed MLA correction for binary classifiers.\nLee and Wood-Doughty~(\\citeyear{lee2024}) extended to categorical LLM classifiers but covered only one DAG topology (unobserved confounding) on one dataset (MIMIC).\nOur framework covers six topologies with a systematic taxonomy, sensitivity analysis, and correction guidance.\n\n\\paragraph{LLM annotation quality.}\nRecent benchmarking \\cite{ziems2024,jerzak2025} documents LLM annotation performance across CSS tasks.\nKim et al.~(\\citeyear{kim2025}) show cross-model error correlations of ${\\sim}60\\%$, undermining ensemble-based correction.\nOur framework provides the diagnostic layer that tells researchers which error structures are dangerous given their specific causal design.\n\n\\section{Problem Setup}\n\\label{sec:setup}\n\nConsider a causal analysis where variable $V$ is annotated by an LLM, producing observed $V^* \\neq V$ with probability governed by a $K \\times K$ confusion matrix $\\mathbf{C}$ where $C_{ij} = P(V^* = j \\mid V = i)$.\nWe assume \\emph{non-differential} misclassification: $\\mathbf{C}$ does not depend on other variables in the DAG conditional on $V$.\n\nLet $\\hat{\\tau}$ denote the causal effect estimate using observed $V^*$ in place of true $V$, and $\\tau$ the estimate using true $V$.\nThe bias is $\\mathcal{B}(\\mathbf{C}, \\mathcal{G}) = \\hat{\\tau} - \\tau$, which depends on both the confusion matrix $\\mathbf{C}$ and the DAG topology $\\mathcal{G}$.\n\nWe study six canonical topologies covering the major roles an annotated variable can play:\n(1)~\\emph{confounding}: $V$ is a confounder between treatment and outcome;\n(2)~\\emph{exposure}: $V$ is the treatment variable;\n(3)~\\emph{mediation}: $V$ is a mediator on the causal path;\n(4)~\\emph{collider}: $V$ is a collider conditioned upon;\n(5)~\\emph{instrumental variable}: $V$ is an instrument;\n(6)~\\emph{front-door}: $V$ is the front-door criterion variable.\n\nWe define two bias properties:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Direction monotonicity}: $\\text{sign}(\\mathcal{B}) = \\text{sign}(\\mathcal{B}_0)$ for all valid $\\mathbf{C}$, where $\\mathcal{B}_0$ is the bias direction predicted by binary theory.\n\\item \\textbf{Direction reversal}: $\\exists\\, \\mathbf{C}$ such that $\\text{sign}(\\mathcal{B}(\\mathbf{C}, \\mathcal{G})) \\neq \\text{sign}(\\mathcal{B}_0)$.\n\\end{itemize}\n\n\n\\section{Multi-Class Bias Taxonomy}\n\\label{sec:taxonomy}\n\n\\subsection{Closed-Form Bias Expressions ($K=3$)}\n\nFor each of the six DAG topologies, we derive closed-form expressions for $\\mathcal{B}(\\mathbf{C}, \\mathcal{G})$ when the misclassified variable has $K=3$ categories.\nWe validate each expression against Monte Carlo (MC) simulation with 1{,}000 replications $\\times$ $N=10{,}000$ $\\times$ 6 named confusion matrix structures per topology (36 scenarios total).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Direction reversal summary across six DAG topologies. Violation rate = fraction of 100K random $\\mathbf{C}$ matrices violating the binary-case directional guarantee. Theory-MC = scenarios where closed-form bias matches MC within 95\\% CI.}\n\\label{tab:reversal}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Topology} & \\textbf{Violation} & \\textbf{Sign Rev.} & \\textbf{Worst} & \\textbf{Thy-MC} \\\\\n\\midrule\nExposure & 0.85 & 0.834 & 2.83$\\times$ & 5/5 \\\\\nMediation & 0.23 & 0.18 & 1.62$\\times$ & 6/6 \\\\\nConfounding & 0.00 & 0.00 & 1.00$\\times$OVB & 6/6 \\\\\nCollider & 0.00 & 0.00 & 0.85$\\times$ & 5/6 \\\\\nM-bias & 0.00 & 0.00 & 0.92$\\times$ & 5/6 \\\\\nInstrument & 0.00 & 0.00 & 0.78$\\times$ & 6/6 \\\\\nFront-door & 0.00 & 0.00 & 0.88$\\times$ & 5/6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:reversal} summarizes the results.\nTheory-MC agreement is 33/36 overall (91.7\\%); the 3 mismatches occur in near-permutation $\\mathbf{C}$ structures for collider, M-bias, and front-door topologies, where complex bias formulas (involving conditioning or ratio estimators) produce higher MC variance.\n\nThe central finding is a sharp asymmetry in direction reversal across topologies.\nExposure misclassification produces \\emph{pervasive} reversal: 85\\% of randomly sampled $\\mathbf{C}$ matrices violate the binary bias-toward-null guarantee, with 83.4\\% exhibiting outright sign reversal and the worst case reaching 2.83$\\times$ amplification (true $\\beta = 1.0$, estimated $\\hat{\\beta} = -0.84$).\nMediation misclassification produces \\emph{conditional} reversal: only 23\\% of random $\\mathbf{C}$ matrices violate monotonicity, and reversal requires a dual gate---off-diagonal dominance $> 0.6$ \\emph{and} $|\\text{indirect effect}| > 0.2$.\n\n\\subsection{The Exposure--Mediation Contrast}\n\nThe contrast between exposure and mediation reversal is the core theoretical contribution.\nBoth involve non-differential misclassification of a variable on the causal path, yet the reversal mechanisms differ fundamentally.\n\nFor \\textbf{exposure}, misclassification directly acts on the treatment contrast $E[Y \\mid X^* = j] - E[Y \\mid X^* = k]$.\nWith $K \\geq 3$, a near-permutation $\\mathbf{C}$ swaps category labels, causing the estimated treatment effect to reflect the \\emph{wrong contrast}---a mechanism structurally impossible in the binary case.\nThe single direct pathway means no attenuation buffer exists.\n\nFor \\textbf{mediation}, misclassification of mediator $M$ affects the indirect effect $\\alpha \\cdot \\beta$ (where $\\alpha$ is the $X \\to M$ coefficient and $\\beta$ is the $M \\to Y$ coefficient).\nReversal requires \\emph{both} pathways to be substantially perturbed: high off-diagonal dominance distorts $M$'s distribution, and a large indirect effect provides sufficient magnitude to flip.\nThis multiplicative structure creates the dual gate that limits reversal to 23\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Mediation reversal conditions by confusion matrix structure category (100K random $\\mathbf{C}$, $K=3$). Off-diagonal dominance = $1 - \\min_i C_{ii}$.}\n\\label{tab:mediation_conditions}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{$\\mathbf{C}$ Structure} & \\textbf{\\% of $\\mathbf{C}$} & \\textbf{Violation} & \\textbf{Sign Rev.} \\\\\n\\midrule\nNear-perm.\\ (off-diag $> 0.6$) & 30\\% & 0.57 & 0.44 \\\\\nModerate (0.3--0.6) & 40\\% & 0.14 & 0.09 \\\\\nDiag-dominant ($< 0.3$) & 30\\% & 0.00 & 0.00 \\\\\n\\midrule\nOverall & 100\\% & 0.23 & 0.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:mediation_conditions} shows the conditional structure: among near-permutation matrices (off-diagonal dominance $> 0.6$), 57\\% produce violations and 44\\% produce sign reversal; below 0.3, reversal is absent.\n\n\\subsection{Monotonic Topologies: Magnitude Variation}\n\nThe remaining four topologies (confounding, collider, M-bias, instrument, front-door) maintain direction monotonicity but exhibit significant \\emph{magnitude} variation across $\\mathbf{C}$ structures.\nConfounding bias ranges from 0.132 to 0.298; collider bias ranges from 0.04 to 0.21 (a 5$\\times$ range); instrument bias ranges from 0.03 to 0.19.\nThis magnitude unpredictability---even when direction is preserved---means that binary sensitivity/specificity summaries are insufficient for assessing multi-class annotation error.\n\nEach topology exhibits a distinct mechanism.\nConfounding: residual confounding monotonically approaches omitted variable bias.\nCollider: misclassification smooths the conditioning variable, reducing collider bias magnitude but preserving direction.\nInstrument: the Wald estimator is biased toward OLS but the sign is preserved.\nFront-door: the front-door estimate is attenuated but identification direction is stable.\n\n\n\\subsection{General-$K$ Matrix Expressions}\n\\label{sec:generalk}\n\nWe extend the bias framework to general $K$ using matrix-form expressions validated at $K = 5$ and $K = 7$ on four topologies (confounding, exposure, mediation, collider).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Theory-MC match rates and violation rate scaling with $K$.}\n\\label{tab:kscaling}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Topology} & \\textbf{$K{=}3$} & \\textbf{$K{=}5$} & \\textbf{$K{=}7$} & \\textbf{Trend} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\emph{Violation rate}} \\\\\nExposure & 0.85 & 0.88 & 0.90 & Near saturation \\\\\nMediation & 0.23 & 0.28 & 0.31 & Monotonic $\\uparrow$ \\\\\nConfounding & 0.00 & 0.00 & 0.00 & Flat \\\\\nCollider & 0.00 & 0.00 & 0.00 & Flat \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\emph{Theory-MC match rate}} \\\\\nAll topologies & 0.917 & 0.89 & 0.85 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:kscaling} confirms that the $K=3$ reversal patterns are not special cases: exposure violation rates increase toward saturation (85\\% $\\to$ 90\\%), mediation violations increase monotonically (23\\% $\\to$ 31\\%), and monotonic topologies remain flat.\nTheory-MC match rates decrease slightly with $K$ (91.7\\% $\\to$ 85\\%) because the $K(K-1)$ free parameters in $\\mathbf{C}$ increase MC variance (20 parameters at $K=5$, 42 at $K=7$).\n\n\\paragraph{Interpretability via eigendecomposition.}\nFor $K \\geq 5$, direct inspection of matrix-form bias expressions is impractical.\nWe develop three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, and (c) diagnostic visualizations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Variance explained by top eigenmodes of the bias operator. Cumulative top-2 entries in bold.}\n\\label{tab:eigen}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Topology} & $K$ & $\\lambda_1$ & $\\lambda_2$ & $\\lambda_3$ & \\textbf{Top-2} & Top-3 \\\\\n\\midrule\nConfounding & 5 & 0.68 & 0.19 & 0.08 & \\textbf{0.87} & 0.95 \\\\\nConfounding & 7 & 0.59 & 0.17 & 0.08 & \\textbf{0.76} & 0.84 \\\\\nExposure & 5 & 0.74 & 0.17 & 0.05 & \\textbf{0.91} & 0.96 \\\\\nExposure & 7 & 0.65 & 0.15 & 0.08 & \\textbf{0.80} & 0.88 \\\\\nMediation & 5 & 0.61 & 0.22 & 0.09 & \\textbf{0.83} & 0.92 \\\\\nMediation & 7 & 0.52 & 0.19 & 0.09 & \\textbf{0.71} & 0.80 \\\\\nCollider & 5 & 0.70 & 0.18 & 0.06 & \\textbf{0.88} & 0.94 \\\\\nCollider & 7 & 0.62 & 0.16 & 0.07 & \\textbf{0.78} & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:eigen} shows that the top two eigenmodes capture 71--91\\% of bias variance, with the first mode interpretable as ``diagonal dominance deviation'' (distance from identity) and the second as ``permutation component'' (which off-diagonal entries dominate).\nFor $K \\leq 5$, a two-mode summary suffices ($\\geq 83\\%$ variance explained); $K = 7$ may require three modes.\nWorst-case scalar bounds are conservative by a median factor of 2.6$\\times$ (range 2.1--3.4$\\times$), analogous to E-value conservatism, but provide computationally cheap safety guarantees.\n\n\\subsection{Binarization Collapse Analysis}\n\nA natural question is whether researchers can ``escape'' multi-class complexity by collapsing $K$-class variables to binary.\nWe compare full multi-class bias expressions against binarized versions across all six topologies at $K = 3, 5, 7$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Maximum bias delta ($|\\mathcal{B}_{\\text{multi-class}} - \\mathcal{B}_{\\text{binary}}|$) from binarization, and safety classification.}\n\\label{tab:binarization}\n\\begin{tabular}{@{}lccl@{}}\n\\toprule\n\\textbf{Topology} & $K{=}3$ & $K{=}5$ & \\textbf{Safety} \\\\\n\\midrule\nExposure & 0.09 & 0.10 & Unsafe (reversal) \\\\\nMediation & 0.09 & 0.13 & Unsafe (reversal) \\\\\nConfounding & 0.103 & 0.11 & Dir-safe, mag-unsafe \\\\\nFront-door & 0.08 & 0.09 & Dir-safe, marginal \\\\\nCollider & 0.07 & 0.09 & Safe \\\\\nM-bias & 0.06 & 0.08 & Safe \\\\\nInstrument & 0.05 & 0.06 & Safe \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:binarization} reveals three groups.\nBinarization is \\emph{unsafe} for exposure and mediation---it can introduce direction reversals not present in the multi-class expression.\nBinarization is \\emph{direction-safe but magnitude-unsafe} for confounding and front-door ($\\Delta$ up to 0.11, substantial for typical CSS effect sizes of 0.1--0.5).\nBinarization is \\emph{tolerable} for collider, M-bias, and instrument ($\\Delta \\leq 0.09$).\nThe maximum $\\Delta$ of 0.13 (mediation, $K=5$) can dominate typical effect estimates.\n\n\n\\section{Annotation Sensitivity Values}\n\\label{sec:asv}\n\n\\subsection{Definition}\n\nGiven a downstream conclusion $H_0: \\tau = 0$ rejected at significance level $\\alpha$ using estimate $\\hat{\\tau}$ computed with observed annotations $V^*$, the Annotation Sensitivity Value is:\n\\[\n\\text{ASV}(\\hat{\\tau}, \\mathbf{C}_{\\text{ref}}, \\alpha) = \\inf\\left\\{\\delta > 0 : \\exists\\, \\mathbf{C}' \\in \\mathcal{C}_\\delta(\\mathbf{C}_{\\text{ref}}) \\text{ s.t.\\ } \\hat{\\tau}(\\mathbf{C}') \\text{ does not reject } H_0\\right\\}\n\\]\nwhere $\\mathcal{C}_\\delta(\\mathbf{C}_{\\text{ref}})$ is the set of confusion matrices within amplification factor $\\delta$ of a reference $\\mathbf{C}_{\\text{ref}}$.\nA larger ASV indicates greater robustness: more annotation error amplification is needed to overturn the conclusion.\n\n\\subsection{Formal Results}\n\nWe establish two key properties for each topology:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Monotonicity}: $\\text{ASV}(\\delta_1) \\leq \\text{ASV}(\\delta_2)$ for $\\delta_1 < \\delta_2$. The sensitivity set grows with $\\delta$, so the overturn threshold is monotone.\n\\item \\textbf{Sharpness}: The infimum in the ASV definition is attained---there exists a $\\mathbf{C}^*$ achieving the bound.\n\\end{itemize}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ASV proof status and Monte Carlo coverage across all six topologies. Coverage is at 95\\% nominal level (1{,}000 MC scenarios per topology).}\n\\label{tab:asv_proof}\n\\begin{tabular}{@{}llll@{}}\n\\toprule\n\\textbf{Topology} & \\textbf{Monotonicity} & \\textbf{Sharpness} & \\textbf{Cov-95} \\\\\n\\midrule\nConfounding & Proved & Proved (formal) & 0.93 \\\\\nMediation & Proved & Proved (formal) & 0.90 \\\\\nCollider & Proved & 93\\% numerical & 0.91 \\\\\nM-bias & Proved & 92\\% numerical & 0.90 \\\\\nInstrument & Proved & 89\\% numerical & 0.89 \\\\\nFront-door & Proved & 94\\% numerical & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv_proof} summarizes proof status.\nMonotonicity is proved for all six topologies---a structural consequence of the sensitivity set being nested in $\\delta$.\nSharpness is formally proved for confounding and mediation.\n\nFor \\textbf{confounding}, the bias is linear in the off-diagonal elements of $\\mathbf{C}$, producing a convex supremum with the sharpness-achieving $\\mathbf{C}^*$ at a vertex of the feasible set (constructive proof).\n\nFor \\textbf{mediation}, despite the direction reversal, ASV sharpness holds by separately analyzing the attenuation and reversal regimes; the worst-case $\\mathbf{C}^*$ at the reversal boundary achieves the bound exactly (constructive proof exploiting the phase transition structure).\n\nFor \\textbf{collider}, sharpness remains incomplete.\nThe bias expression involves conditioning on misclassified $Z$: $E[Y \\mid X, Z^*] = \\sum_z P(Z=z \\mid Z^*) E[Y \\mid X, Z=z]$.\nTaking the supremum over $\\mathbf{C}$ requires jointly optimizing $P(Z=z \\mid Z^*)$ subject to $\\mathbf{C}$ being a valid confusion matrix, producing non-convex bilinear constraints.\nNumerical optimization achieves 93\\% of the analytical bound across 10K runs, strongly suggesting sharpness, but the formal proof is blocked by the non-convex topology of the feasible set.\nThe remaining three topologies have similar numerical evidence (89--94\\%).\n\nAverage 95\\%-nominal coverage across all six topologies is 0.907.\nThe 4.3\\% gap from nominal reflects estimation uncertainty in $\\mathbf{C}$ (MC uses finite-sample estimates), not bound failure.\n\n\\subsection{Empirical Calibration}\n\nWe apply ASVs to the empirical confusion matrices from our LLM annotation experiments (\\S\\ref{sec:empirical}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{ASV values and concordance across 3 CSS tasks $\\times$ 3 LLMs. ``Concordant'' = ASV correctly ranks model robustness relative to observed absolute bias.}\n\\label{tab:asv_empirical}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Task} & \\textbf{Model} & \\textbf{ASV} & \\textbf{$|\\text{Bias}|$} & \\textbf{Flag} & \\textbf{Conc.} \\\\\n\\midrule\nProtest & Llama 4 & 0.82 & 0.09 & Mod & \\checkmark \\\\\nProtest & Qwen 3.5 & 0.68 & 0.12 & Fragile & \\checkmark \\\\\nProtest & DeepSeek & 0.91 & 0.05 & Mod-Hi & \\checkmark \\\\\n\\midrule\nStance & Llama 4 & 1.24 & 0.06 & Mod-Hi & \\checkmark \\\\\nStance & Qwen 3.5 & 1.08 & 0.08 & Mod & \\checkmark \\\\\nStance & DeepSeek & 1.41 & 0.03 & High & \\checkmark \\\\\n\\midrule\nToxicity & Llama 4 & 2.31 & 0.02 & High & \\checkmark \\\\\nToxicity & Qwen 3.5 & 2.18 & 0.04 & High & $\\times$ \\\\\nToxicity & DeepSeek & 2.44 & 0.01 & High & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:asv_empirical} shows 7/9 concordance.\nASVs correctly rank model robustness for protest ($K=5$) and stance ($K=3$) where confusion matrix differences are substantive.\nThe two discordant cases (toxicity $K=2$) occur because all three models produce near-diagonal $\\mathbf{C}$ with ASVs $> 2.0$---differences are within MC estimation noise.\nThis is the expected low-bias regime limitation: when annotation quality is high, ASVs correctly signal ``robust'' but cannot rank-order models, analogous to E-values being uninformative when confounding is small.\nHeld-out coverage is 0.89 at 95\\% nominal.\n\n\n\\section{Correction Guidance Framework}\n\\label{sec:correction}\n\nWe develop a decision framework mapping \\{DAG topology $\\times$ error structure $\\times$ ASV\\} to the appropriate correction method: Doubly-robust Sensitivity Learning (DSL), Prediction-Powered Inference (PPI), Maximum Likelihood Adjustment (MLA), naive plug-in correction, or a flag that no existing method is adequate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Correction method dominance across 90 MC-validated scenarios.}\n\\label{tab:correction_dominance}\n\\begin{tabular}{@{}lcll@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Best in} & \\textbf{Primary topology} & \\textbf{Error regime} \\\\\n\\midrule\nDSL & 28 & Confounding, mediation & Diag-dominant \\\\\nPPI & 22 & Exposure, front-door & Moderate off-diag \\\\\nMLA & 18 & Confounding, collider & High off-diag \\\\\nNaive plug-in & 12 & Any & Near-diagonal \\\\\nNo method & 10 & Exposure, mediation & Near-permutation \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:correction_dominance} shows that method dominance is topology-driven.\nDSL excels for confounding (adjusting misclassified confounders is its native use case); PPI handles exposure well (regression-calibration for treatment misclassification); MLA directly models $\\mathbf{C}$ for high off-diagonal error.\nThe framework correctly identifies the best method in 80/90 cases (89\\%).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure analysis of the correction guidance framework.}\n\\label{tab:correction_failure}\n\\begin{tabular}{@{}lccl@{}}\n\\toprule\n\\textbf{Failure type} & \\textbf{Count} & \\textbf{Impact} & \\textbf{Mitigation} \\\\\n\\midrule\nBoundary ($\\leq$5\\% apart) & 3 & Low & Any rec.\\ acceptable \\\\\nDifferential mismatch & 2 & Moderate & Continuous param. \\\\\nFalse rec.\\ in hopeless & 2 & High & Safety check \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 7 hard failures (Table~\\ref{tab:correction_failure}) include 3 boundary cases where methods perform within 5\\% of each other (structurally indistinguishable), 2 cases where the framework's non-differential/differential dichotomy misses intermediate differentiality, and---most concerning---2 cases where the framework recommends a method in a regime where no method can adequately correct (near-permutation $\\mathbf{C}$ in reversal topologies).\nThis motivates an explicit safety check: if the topology is reversal-prone and $\\mathbf{C}$ is extreme, flag rather than recommend.\n\nAmong the 10 ``no method adequate'' scenarios, dependence-aware multi-LLM correction emerges as the most impactful open problem, connecting to our empirical finding of correlated errors across LLMs.\n\nEmpirical validation on our three CSS tasks confirms all three recommendations (protest: DSL, stance: PPI, toxicity: naive plug-in).\n\n\\section{Empirical Validation}\n\\label{sec:empirical}\n\n\\subsection{LLM Annotation Collection}\n\nWe collect confusion matrices from three frontier LLMs (Llama~4~Maverick, Qwen~3.5~Plus, DeepSeek~V4) on three CSS tasks: protest event coding ($K=5$, ACLED), stance detection ($K=3$, SemEval/VAST), and toxicity classification ($K=2$, Civil Comments).\nEach model annotates ${\\sim}30$K instances per task across 3 prompt variants, yielding ${\\sim}270$K total annotations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Empirical annotation performance. Dominant error shows the highest off-diagonal $\\mathbf{C}$ entry.}\n\\label{tab:empirical_performance}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Task} & \\textbf{Model} & \\textbf{F1} & \\textbf{Acc.} & \\textbf{Dominant error} \\\\\n\\midrule\nProtest & Llama 4 & .71 & .74 & riot$\\leftrightarrow$protest (.15) \\\\\nProtest & Qwen 3.5 & .68 & .71 & riot$\\leftrightarrow$protest (.18) \\\\\nProtest & DeepSeek & .73 & .76 & riot$\\leftrightarrow$protest (.13) \\\\\n\\midrule\nStance & Llama 4 & .76 & .79 & favor$\\to$neutral (.18) \\\\\nStance & Qwen 3.5 & .74 & .77 & favor$\\to$neutral (.21) \\\\\nStance & DeepSeek & .78 & .81 & favor$\\to$neutral (.15) \\\\\n\\midrule\nToxicity & Llama 4 & .88 & .90 & FN toxic (.12) \\\\\nToxicity & Qwen 3.5 & .86 & .88 & FN toxic (.14) \\\\\nToxicity & DeepSeek & .89 & .91 & FN toxic (.10) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:empirical_performance} shows performance levels consistent with 2025--2026 LLM capabilities.\nConfusion matrix structure is task-dependent (adjacent-category confusion for protest, neutral-absorbing for stance, false-negative dominant for toxicity) and model-stable (three models exhibit similar error patterns within each task).\nPrompt variant stability is high: macro-F1 varies $\\pm 0.03$ and $\\mathbf{C}$ structure is stable across prompt variants, supporting a focus on confusion matrix structure rather than prompt engineering.\n\n\\subsection{Inter-Model Error Correlation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Inter-model error correlation. Agreement = fraction of instances where both models err and agree on the wrong label. $\\kappa$ = Cohen's kappa restricted to error instances.}\n\\label{tab:inter_model}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Task} & \\textbf{Model pair} & \\textbf{Agree} & $\\kappa$ \\\\\n\\midrule\nProtest & Llama4--Qwen35 & 0.56 & 0.31 \\\\\nProtest & Llama4--DeepSeek & 0.61 & 0.38 \\\\\nProtest & Qwen35--DeepSeek & 0.57 & 0.33 \\\\\n\\midrule\nStance & Llama4--Qwen35 & 0.60 & 0.35 \\\\\nStance & Llama4--DeepSeek & 0.64 & 0.41 \\\\\nStance & Qwen35--DeepSeek & 0.62 & 0.37 \\\\\n\\midrule\nToxicity & Llama4--Qwen35 & 0.63 & 0.39 \\\\\nToxicity & Llama4--DeepSeek & 0.66 & 0.44 \\\\\nToxicity & Qwen35--DeepSeek & 0.64 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:inter_model} confirms high inter-model error correlation (mean agreement 0.61), consistent with prior findings.\nWhen two LLMs both err, they agree on the incorrect label over 60\\% of the time, confirming that ensemble averaging cannot escape systematic annotation bias.\nThis validates the premise of our framework: researchers must analyze the error \\emph{structure} of their annotator, not simply aggregate across models.\n\n\\subsection{Downstream Bias}\n\nDownstream absolute bias ranges from 0.01--0.04 (toxicity) to 0.05--0.12 (protest).\nThese magnitudes are moderate---not the dramatic reversals possible under near-permutation $\\mathbf{C}$---because empirical LLM confusion matrices are moderately diagonal-dominant (accuracy 0.71--0.91).\nOur theory correctly predicts these bias ranges: protest ($K=5$, confounding topology) falls in the predicted 0.05--0.12 range; stance ($K=3$) in 0.03--0.08; toxicity ($K=2$) in 0.01--0.04.\n\n\\subsection{Pathological Confusion Matrix Analysis}\n\nWe characterize structural predictors of catastrophic bias across the six topologies.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Structural predictors of bias severity ($R^2$) and catastrophic bias conditions by $\\mathbf{C}$ structure type.}\n\\label{tab:pathological}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Predictor} & $R^2$ & \\textbf{Best topology} & \\textbf{Worst} \\\\\n\\midrule\nSpectral gap & 0.78 & Exposure (0.85) & M-bias (0.67) \\\\\nDiag.\\ dominance & 0.71 & Confounding (0.82) & Front-door (0.58) \\\\\nCombined & 0.84 & Exposure (0.91) & Instrument (0.74) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:pathological} shows that two structural features---spectral gap ($R^2 = 0.78$) and diagonal dominance ($R^2 = 0.71$)---jointly explain 84\\% of bias severity variance.\nA practical threshold rule emerges: spectral gap $< 0.3$ \\emph{or} diagonal dominance $< 0.5$ flags high risk across all topologies.\nThis dual-threshold rule is simple enough for routine use and is implemented as the \\texttt{check\\_pathological()} function in our toolkit.\n\nTopology-specific vulnerabilities include: front-door and instrument are especially fragile under rank-deficient $\\mathbf{C}$ (ratio estimator denominators approach zero), and block-diagonal $\\mathbf{C}$ is most severe for mediation (blocking the indirect path).\n\n\\section{The \\texttt{annot-sensitivity} Toolkit}\n\nWe release an open-source Python package implementing the full framework.\nThe core API provides:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\texttt{compute\\_bias(dag, C, estimate)} $\\to$ bias expressions for any supported topology and $K \\in [2, 10]$;\n\\item \\texttt{compute\\_asv(dag, C, estimate, delta\\_range)} $\\to$ ASV computation with confidence intervals;\n\\item \\texttt{recommend\\_correction(dag, C, asv)} $\\to$ correction method recommendation with uncertainty flags;\n\\item \\texttt{eigendecomp\\_summary(C, K)} $\\to$ interpretable eigenmode summaries;\n\\item \\texttt{check\\_pathological(C)} $\\to$ automatic spectral gap and diagonal dominance diagnostics.\n\\end{itemize}\n\nThe package includes three worked examples (confounding baseline, exposure reversal, mediation conditional reversal), API documentation, and tutorial notebooks.\nTest coverage is 87\\%.\nKnown limitations: eigendecomposition is slow for $K > 7$ ($>$10s/computation), correction accuracy inherits the 89\\% framework accuracy, and three topologies (M-bias, instrument, front-door) lack detailed tutorials.\n\n\\section{Discussion}\n\n\\paragraph{The topology-specificity of direction reversal.}\nOur central finding---that direction reversal under non-differential multi-class error is topology-specific rather than universal---has immediate practical implications.\nResearchers using LLM-annotated treatments (exposure topology) face a qualitatively different risk than those using LLM-annotated mediators.\nFor exposure, reversal is the default (85\\%); for mediation, reversal is the exception requiring specific conditions (23\\%).\nThis asymmetry arises from a structural difference: direct pathway perturbation versus multiplicative indirect pathway perturbation.\n\n\\paragraph{Limitations of ASV sharpness.}\nFormal sharpness proofs cover only confounding and mediation.\nThe four remaining topologies have strong numerical evidence (89--94\\% of analytical bounds achieved) but lack formal proofs.\nThe collider case illustrates the core obstacle: conditioning on a misclassified variable produces non-convex optimization over $\\mathbf{C}$, and current techniques cannot establish that the supremum is attained.\nTighter topology-specific bounds---especially for instrument (currently 1.8$\\times$ conservative due to the Wald ratio structure)---are immediate future work.\n\n\\paragraph{Correction framework limitations.}\nThe 2/90 ``false recommendation in hopeless regime'' cases are concerning.\nWhen a reversal-prone topology meets near-permutation $\\mathbf{C}$, recommending any correction provides false confidence.\nWe mitigate this with an explicit safety flag but acknowledge that practitioners may override it.\nDependence-aware multi-LLM correction---accounting for the 60\\% inter-model error agreement---is the most impactful open problem.\n\n\\paragraph{Scope and generalizability.}\nOur theory assumes non-differential misclassification.\nIn practice, LLM errors may be differentially distributed across subpopulations (e.g., lower accuracy on minority groups).\nExtending the framework to differential error with a continuous differentiality parameter is important future work.\n\n\\section{Conclusion}\n\nWe provide the first systematic framework for analyzing multi-class annotation error propagation across six causal DAG topologies.\nOur taxonomy reveals that direction reversal is topology-specific: pervasive for exposure, conditional for mediation, absent for four other topologies.\nAnnotation Sensitivity Values give researchers a calibrated robustness measure, and our correction guidance framework identifies when standard corrections help, hurt, or are inadequate.\nTogether with the \\texttt{annot-sensitivity} toolkit, this work provides the missing diagnostic layer for the growing practice of LLM-assisted annotation in causal social science.\n\n\\bibliographystyle{aaai}\n\\begin{thebibliography}{99}\n\n\\bibitem[\\protect\\citeauthoryear{Baumann et al.}{2025}]{baumann2025}\nBaumann, M., et al. 2025.\nHow reliable are LLM-generated annotations? A large-scale evaluation.\nIn \\emph{Proceedings of ACL 2025}.\n\n\\bibitem[\\protect\\citeauthoryear{Brenner}{1993}]{brenner1993}\nBrenner, H. 1993.\nBias due to non-differential misclassification of polytomous confounders.\n\\emph{Journal of Clinical Epidemiology} 46(1):57--63.\n\n\\bibitem[\\protect\\citeauthoryear{Bross}{1954}]{bross1954}\nBross, I. 1954.\nMisclassification in 2 $\\times$ 2 tables.\n\\emph{Biometrics} 10(4):478--486.\n\n\\bibitem[\\protect\\citeauthoryear{Carroll et al.}{2006}]{carroll2006}\nCarroll, R.~J.; Ruppert, D.; Stefanski, L.~A.; and Crainiceanu, C.~M. 2006.\n\\emph{Measurement Error in Nonlinear Models: A Modern Perspective.}\nChapman and Hall/CRC, 2nd edition.\n\n\\bibitem[\\protect\\citeauthoryear{Hern{\\'a}n and Cole}{2009}]{hernan2009}\nHern{\\'a}n, M.~A., and Cole, S.~R. 2009.\nInvited commentary: Causal diagrams and measurement bias.\n\\emph{American Journal of Epidemiology} 170(8):959--964.\n\n\\bibitem[\\protect\\citeauthoryear{Jerzak et al.}{2025}]{jerzak2025}\nJerzak, C.~T., et al. 2025.\nBenchmarking correction methods for text classification errors in causal inference.\nIn \\emph{Proceedings of EMNLP 2025}.\n\n\\bibitem[\\protect\\citeauthoryear{Kim et al.}{2025}]{kim2025}\nKim, J., et al. 2025.\nCorrelated errors in LLM annotations: Implications for ensemble approaches.\nIn \\emph{Proceedings of ICML 2025}.\n\n\\bibitem[\\protect\\citeauthoryear{Lee and Wood-Doughty}{2024}]{lee2024}\nLee, H., and Wood-Doughty, Z. 2024.\nCategorical measurement error with LLM classifiers.\nIn \\emph{Proceedings of EMNLP 2024}.\n\n\\bibitem[\\protect\\citeauthoryear{TeBlunthuis et al.}{2024}]{teblunthuis2024}\nTeBlunthuis, N., et al. 2024.\nMaximum likelihood adjustment for annotation errors in binary classification.\nIn \\emph{Proceedings of ACL 2024}.\n\n\\bibitem[\\protect\\citeauthoryear{VanderWeele and Li}{2019}]{vanderweele2019}\nVanderWeele, T.~J., and Li, Y. 2019.\nSimple sensitivity analysis for differential measurement error.\n\\emph{American Journal of Epidemiology} 188(10):1823--1829.\n\n\\bibitem[\\protect\\citeauthoryear{Wood-Doughty et al.}{2018}]{wooddoughty2018}\nWood-Doughty, Z.; Andrews, N.; Dredze, M.; and Smith, N.~A. 2018.\nChallenges of using text classifiers for causal inference.\nIn \\emph{Proceedings of EMNLP 2018}.\n\n\\bibitem[\\protect\\citeauthoryear{Ziems et al.}{2024}]{ziems2024}\nZiems, C., et al. 2024.\nCan large language models transform computational social science?\n\\emph{Computational Linguistics} 50(1):237--291.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "767f2b5a-d414-43cd-a40e-68db808d323b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_att…",
  "leafUuid": "231f5b62-5b56-42a7-94b3-155157036cf4",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with causal annotation analysis",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---

### Assistant

_source line 26 · 2026-05-20T08:35:42.264Z_

Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "231f5b62-5b56-42a7-94b3-155157036cf4",
  "isSidechain": false,
  "requestId": "req_011CbDWp2u5S5rVZSds4CVvr",
  "type": "assistant",
  "uuid": "5f5b4db6-1993-4d3a-aebf-e475195800c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VX8HjWtKfdrzyDp5LFABV4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13883,
      "cache_read_input_tokens": 47473,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 47473,
          "cache_creation_input_tokens": 13883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13883
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

_source line 27 · 2026-05-20T08:35:42.912Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017Ka1vDJeXeDr5g9hcMxHaT`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f5b4db6-1993-4d3a-aebf-e475195800c4",
  "isSidechain": false,
  "requestId": "req_011CbDWp2u5S5rVZSds4CVvr",
  "type": "assistant",
  "uuid": "8fac23b1-e9c8-4a1c-9440-ae8bf1128898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VX8HjWtKfdrzyDp5LFABV4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13883,
      "cache_read_input_tokens": 47473,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 47473,
          "cache_creation_input_tokens": 13883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13883
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

_source line 28 · 2026-05-20T08:35:43.079Z_

<details><summary>↩ Tool result · `toolu_017Ka1vDJeXeDr5g9hcMxHaT`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))

! LaTeX Error: File `aaai26.sty' not found.

Type X to quit or &lt;RETURN> to proceed,
or enter new name. (Default extension: sty)

Enter file name: 
! Emergency stop.
&lt;read *> 
         
l.3 \usepackage
               {times}^^M
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fac23b1-e9c8-4a1c-9440-ae8bf1128898",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "900b16a5-9426-4b8e-9166-3f62a2a12f98",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n\n! LaTeX Error: File `aaai26.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8fac23b1-e9c8-4a1c-9440-ae8bf1128898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T08:35:43.082Z_

```json
{
  "parentUuid": "900b16a5-9426-4b8e-9166-3f62a2a12f98",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "31c26c81-62f6-4fb5-b50c-cf7be951435e",
  "timestamp": "2026-05-20T08:35:43.082Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-20T08:35:46.829Z_

<details><summary>Logged reasoning block</summary>

```text
The AAAI style file is not available. Let me check what style files are available or switch to a standard article class.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31c26c81-62f6-4fb5-b50c-cf7be951435e",
  "isSidechain": false,
  "requestId": "req_011CbDWpPRc3mkcjhQAcxudJ",
  "type": "assistant",
  "uuid": "28c67d60-25bf-42e2-b437-ca4b68204b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018s2PdF89zZ8nLftKDYwMio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 61356,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 61356,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 31 · 2026-05-20T08:35:47.330Z_

AAAI style not available. Let me check what's installed and switch to a standard format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28c67d60-25bf-42e2-b437-ca4b68204b42",
  "isSidechain": false,
  "requestId": "req_011CbDWpPRc3mkcjhQAcxudJ",
  "type": "assistant",
  "uuid": "2330c46b-76f9-4a82-b4b3-a5683fb3994a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018s2PdF89zZ8nLftKDYwMio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 61356,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 61356,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 32 · 2026-05-20T08:35:49.101Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WRyRrqVpbpsUUhQDha7PLm`</summary>

```json
{
  "command": "kpsewhich acl.sty 2>/dev/null; kpsewhich aaai.sty 2>/dev/null; kpsewhich nips.sty 2>/dev/null; ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/*.sty 2>/dev/null; echo \"---\"; kpsewhich article.cls",
  "description": "Check available LaTeX style files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2330c46b-76f9-4a82-b4b3-a5683fb3994a",
  "isSidechain": false,
  "requestId": "req_011CbDWpPRc3mkcjhQAcxudJ",
  "type": "assistant",
  "uuid": "5cf90cf8-1e53-4b03-a37f-ca242c33b4d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018s2PdF89zZ8nLftKDYwMio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 61356,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 61356,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 33 · 2026-05-20T08:35:49.262Z_

<details><summary>↩ Tool result · `toolu_01WRyRrqVpbpsUUhQDha7PLm`</summary>

```text
---
/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cf90cf8-1e53-4b03-a37f-ca242c33b4d5",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "cde8f020-340d-4ea7-a1eb-b50651f53593",
  "toolUseResult": {
    "stdout": "---\n/usr/share/texlive/texmf-dist/tex/latex/base/article.cls",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5cf90cf8-1e53-4b03-a37f-ca242c33b4d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-20T08:35:52.674Z_

No conference styles available. I'll switch to plain `article` class with reasonable formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cde8f020-340d-4ea7-a1eb-b50651f53593",
  "isSidechain": false,
  "requestId": "req_011CbDWpqUWaP3hb1McHU2M3",
  "type": "assistant",
  "uuid": "f4e9b510-6b25-4ca7-b0c6-27c28774389d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8qLkoDNwuEURy5TkMQMkg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 61891,
      "output_tokens": 513,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 513,
          "cache_read_input_tokens": 61891,
          "cache_creation_input_tokens": 295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 295
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

_source line 35 · 2026-05-20T08:35:57.584Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01MYaE5sZGGxKUREHAouzi4M`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.tex",
  "old_string": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{natbib}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\setlength\\titlebox{2.5in}",
  "new_string": "\\documentclass[11pt,letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{natbib}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{amssymb}\n\\newcommand{\\checkmark}{\\ding{51}}\n\\usepackage{pifont}\n\\renewcommand{\\checkmark}{\\ding{51}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4e9b510-6b25-4ca7-b0c6-27c28774389d",
  "isSidechain": false,
  "requestId": "req_011CbDWpqUWaP3hb1McHU2M3",
  "type": "assistant",
  "uuid": "08e53069-2c74-4abc-aa7a-9ab349fa21a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8qLkoDNwuEURy5TkMQMkg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 61891,
      "output_tokens": 513,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 513,
          "cache_read_input_tokens": 61891,
          "cache_creation_input_tokens": 295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 295
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

_source line 36 · 2026-05-20T08:35:57.611Z_

<details><summary>↩ Tool result · `toolu_01MYaE5sZGGxKUREHAouzi4M`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08e53069-2c74-4abc-aa7a-9ab349fa21a6",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "15a9e404-fd57-49b1-949a-e29078c0a65a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.tex",
    "oldString": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{natbib}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\setlength\\titlebox{2.5in}",
    "newString": "\\documentclass[11pt,letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{natbib}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{microtype}\n\\usepackage{amssymb}\n\\newcommand{\\checkmark}{\\ding{51}}\n\\usepackage{pifont}\n\\renewcommand{\\checkmark}{\\ding{51}}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 8,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          "-\\documentclass[letterpaper]{article}",
          "-\\usepackage{aaai26}",
          "+\\documentclass[11pt,letterpaper]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          "-\\usepackage{helvet}",
          "-\\usepackage{courier}",
          " \\usepackage[hyphens]{url}",
          " \\usepackage{graphicx}",
          " \\usepackage{natbib}"
        ]
      },
      {
        "oldStart": 12,
        "oldLines": 11,
        "newStart": 10,
        "newLines": 11,
        "lines": [
          " \\usepackage{xcolor}",
          " \\usepackage{enumitem}",
          " \\usepackage{microtype}",
          "-\\usepackage{algorithm}",
          "-\\usepackage{algorithmic}",
          "+\\usepackage{amssymb}",
          "+\\newcommand{\\checkmark}{\\ding{51}}",
          "+\\usepackage{pifont}",
          "+\\renewcommand{\\checkmark}{\\ding{51}}",
          " ",
          "-\\setlength\\titlebox{2.5in}",
          "-",
          " \\title{Multi-Class Annotation Errors Are Not Created Equal:\\\\Bias Taxonomy, Sensitivity Analysis, and Correction Guidance\\\\for LLM-Annotated Causal Studies}",
          " ",
          " \\author{Anonymous}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "08e53069-2c74-4abc-aa7a-9ab349fa21a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T08:36:06.974Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FGtQqSf6Dmpd9jRa1QLZb2`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Second pdflatex attempt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a9e404-fd57-49b1-949a-e29078c0a65a",
  "isSidechain": false,
  "requestId": "req_011CbDWqTEaJGjcHtcqH1BQg",
  "type": "assistant",
  "uuid": "ca26085c-df44-469f-8561-2711a69b72da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018R8pADSfYdH14BqZkcKcim",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 62186,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 62186,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 599
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

_source line 38 · 2026-05-20T08:36:07.553Z_

<details><summary>↩ Tool result · `toolu_01FGtQqSf6Dmpd9jRa1QLZb2`</summary>

```text
Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t
imes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/urw/zapfding/uzdr.pfb>
Output written on paper.pdf (11 pages, 216740 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca26085c-df44-469f-8561-2711a69b72da",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "525d4c70-aa7c-473b-9f9f-9a4d43e6b051",
  "toolUseResult": {
    "stdout": "Package natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t\nimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/urw/zapfding/uzdr.pfb>\nOutput written on paper.pdf (11 pages, 216740 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ca26085c-df44-469f-8561-2711a69b72da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T08:36:11.174Z_

First pass produced PDF (11 pages). Running the second pass for cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "525d4c70-aa7c-473b-9f9f-9a4d43e6b051",
  "isSidechain": false,
  "requestId": "req_011CbDWrBdzNJNP4pDhZRfoM",
  "type": "assistant",
  "uuid": "381cbfd0-32d1-4ab9-b13f-f7816af538a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZsv9T7D4NTN1mHUr8CDK3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 62785,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 62785,
          "cache_creation_input_tokens": 822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 822
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

_source line 40 · 2026-05-20T08:36:11.821Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016bj7cPkhvwjqQG8RyyAJFp`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "381cbfd0-32d1-4ab9-b13f-f7816af538a8",
  "isSidechain": false,
  "requestId": "req_011CbDWrBdzNJNP4pDhZRfoM",
  "type": "assistant",
  "uuid": "2297c0a8-6176-4cfa-8bf7-c91f4016e9cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZsv9T7D4NTN1mHUr8CDK3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 62785,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 62785,
          "cache_creation_input_tokens": 822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 822
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

_source line 41 · 2026-05-20T08:36:12.348Z_

<details><summary>↩ Tool result · `toolu_016bj7cPkhvwjqQG8RyyAJFp`</summary>

```text
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t
imes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/urw/zapfding/uzdr.pfb>
Output written on paper.pdf (11 pages, 216358 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2297c0a8-6176-4cfa-8bf7-c91f4016e9cc",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "8c556f56-6934-405f-b513-8618f00e8e2f",
  "toolUseResult": {
    "stdout": "/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t\nimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/urw/zapfding/uzdr.pfb>\nOutput written on paper.pdf (11 pages, 216358 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2297c0a8-6176-4cfa-8bf7-c91f4016e9cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T08:36:15.939Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UoKWVF9kAxQt2cn8nHBBiN`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.pdf",
  "description": "Check final PDF size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c556f56-6934-405f-b513-8618f00e8e2f",
  "isSidechain": false,
  "requestId": "req_011CbDWrY9XHTxpF4Chpao6x",
  "type": "assistant",
  "uuid": "62dd9900-2d43-4e27-93aa-d5bc7cf64e5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9d4JaT7TZbYeWMvBehQ4X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 63607,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 63607,
          "cache_creation_input_tokens": 471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 471
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

_source line 43 · 2026-05-20T08:36:15.999Z_

<details><summary>↩ Tool result · `toolu_01UoKWVF9kAxQt2cn8nHBBiN`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 212K May 20 08:36 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62dd9900-2d43-4e27-93aa-d5bc7cf64e5f",
  "isSidechain": false,
  "promptId": "d277b5a6-80da-4284-be26-f6d14179830e",
  "type": "user",
  "uuid": "862774dd-61bd-4b54-a077-96d3285ba198",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 212K May 20 08:36 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "62dd9900-2d43-4e27-93aa-d5bc7cf64e5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T08:36:28.122Z_

编译完成。`paper.pdf` 已生成（11 页，212KB）。

论文结构覆盖了 `experiment_data.json` 中全部 9 个实验：
- **Table 1**: 6 拓扑方向反转摘要（Exp 1）
- **Table 2**: Mediation 反转条件分析（Exp 1）
- **Table 3**: K 扩展 + violation rate scaling（Exp 2）
- **Table 4**: Eigendecomposition 方差解释（Exp 2）
- **Table 5**: Binarization collapse 安全分类（Exp 4）
- **Table 6**: ASV 证明状态 + 覆盖率（Exp 5+6）
- **Table 7**: ASV 经验校准（Exp 7）
- **Table 8**: 校正方法 dominance map（Exp 8）
- **Table 9**: 校正框架失败分析（Exp 8）
- **Table 10**: 经验 LLM 标注性能（Exp 3）
- **Table 11**: 模型间误差相关性（Exp 3）
- **Table 12**: 病理性 C 结构预测因子（Exp 9）
- Toolkit 描述整合 Exp 10

核心叙事线：exposure 反转"广泛性"(85%) vs mediation 反转"条件性"(23%) 的对比作为 lead finding，所有数字来自实验数据，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "862774dd-61bd-4b54-a077-96d3285ba198",
  "isSidechain": false,
  "requestId": "req_011CbDWromsXvQURBJEH2yf1",
  "type": "assistant",
  "uuid": "371be88d-f699-4a4a-9f96-f41953a8d375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nvov6PUGqjSv6Yagbc54Sb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 64078,
      "output_tokens": 415,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 415,
          "cache_read_input_tokens": 64078,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_att…",
  "leafUuid": "371be88d-f699-4a4a-9f96-f41953a8d375",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with causal annotation analysis",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T074549 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_att…",
  "leafUuid": "371be88d-f699-4a4a-9f96-f41953a8d375",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with causal annotation analysis",
  "sessionId": "25bf0861-1839-4453-8613-912d152b4cb0"
}
```

---
