# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/bc24adb6-8b44-47ca-8704-37f5f4ab5cd5.jsonl`
- **Structured JSON:** [`1a9cb3133fbf6288c742.json`](../../sessions/1a/1a9cb3133fbf6288c742.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T07:39:25.860Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T07:39:25.860Z",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：CRD 的核心卖点从\"精度优于 self-consistency\"转向\"同等精度下提供结构化诊断信息（error type, error side, paradigm asymmetry）， 且成本更低（2 calls vs 5 calls）\"。泛化部分成立但有裂缝：ProofWriter pilot 失败需切 LogiQA，MATH 不对称性不显著。 Repair 降格为 secondary analysis，selection ablation 成为主结果。Taxonomy 合并到 3 类后 κ 勉强达标。 论文标题改为 \"Diagnosis and Characterization\"，投稿策略：EMNLP Main borderline，Findings 稳进。 成本效率论证（2 calls vs 5 calls, comparable detection + richer diagnosis）是贯穿全文的核心论据。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T07:39:25.864Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T07:39:25.864Z",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-15T07:39:25.887Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：CRD 的核心卖点从"精度优于 self-consistency"转向"同等精度下提供结构化诊断信息（error type, error side, paradigm asymmetry）， 且成本更低（2 calls vs 5 calls）"。泛化部分成立但有裂缝：ProofWriter pilot 失败需切 LogiQA，MATH 不对称性不显著。 Repair 降格为 secondary analysis，selection ablation 成为主结果。Taxonomy 合并到 3 类后 κ 勉强达标。 论文标题改为 "Diagnosis and Characterization"，投稿策略：EMNLP Main borderline，Findings 稳进。 成本效率论证（2 calls vs 5 calls, comparable detection + richer diagnosis）是贯穿全文的核心论据。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "956fd280-4cd3-402b-bdc9-870550b7bcf1",
  "type": "user",
  "uuid": "6f1007c3-7057-44f0-bd13-cc43e4b7e1c5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T07:39:25.887Z_

```json
{
  "parentUuid": "6f1007c3-7057-44f0-bd13-cc43e4b7e1c5",
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
  "uuid": "aa379778-b089-442c-8cee-2d6343d77743",
  "timestamp": "2026-05-15T07:39:25.887Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T07:39:25.887Z_

```json
{
  "parentUuid": "aa379778-b089-442c-8cee-2d6343d77743",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6bcc9f8c-ce1d-40ec-9b45-733919426b48",
  "timestamp": "2026-05-15T07:39:25.887Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
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
  "aiTitle": "Generate dream paper with CRD diagnosis framework",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5"
}
```

---

### Assistant

_source line 7 · 2026-05-15T07:39:29.357Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bcc9f8c-ce1d-40ec-9b45-733919426b48",
  "isSidechain": false,
  "requestId": "req_011Cb3yUrtPX7RM7CzSKiNqJ",
  "type": "assistant",
  "uuid": "ebda4ad3-938f-45d6-9b13-675dc8e4e8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4mwSvbZKAwYWsYj6vW8cn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11451,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11451
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

_source line 8 · 2026-05-15T07:39:30.326Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DxJf6nYwDQwixF1oL9ajTi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebda4ad3-938f-45d6-9b13-675dc8e4e8ac",
  "isSidechain": false,
  "requestId": "req_011Cb3yUrtPX7RM7CzSKiNqJ",
  "type": "assistant",
  "uuid": "5e82277a-fe2d-4657-8f1b-52802219d87d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4mwSvbZKAwYWsYj6vW8cn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11451,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11451
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

_source line 9 · 2026-05-15T07:39:30.612Z_

<details><summary>↩ Tool result · `toolu_01DxJf6nYwDQwixF1oL9ajTi`</summary>

```text
1	[
2	  {
3	    "name": "Cross-Model Ablation on FOLIO",
4	    "description": "三组条件: (a) Qwen3-32B within-model (MVP baseline), (b) DeepSeek V4 Pro within-model, (c) DeepSeek FOL + Qwen Code cross-model. FOLIO 204 样本。验证分歧信号是否依赖特定模型。\n",
5	    "results": {
6	      "qwen_within_C1": 0.4216,
7	      "qwen_within_C2": 0.8721,
8	      "qwen_within_asymmetry_ratio": "5.6:1 (FOL:Code)",
9	      "deepseek_within_C1": 0.35,
10	      "deepseek_within_C2": 0.74,
11	      "deepseek_within_C5_committed": 0.88,
12	      "deepseek_within_asymmetry_ratio": "2.5:1 (FOL:Code)",
13	      "deepseek_within_phi_coefficient": 0.28,
14	      "cross_model_C1": 0.48,
15	      "cross_model_C2": 0.78,
16	      "cross_model_C5_committed": 0.86,
17	      "cross_model_asymmetry_ratio": "3.2:1 (FOL:Code)",
18	      "cross_model_phi_coefficient": 0.14,
19	      "C2_drop_deepseek_vs_qwen": "-13pp",
20	      "asymmetry_direction_consistent": true,
21	      "cross_model_jaccard_failure_overlap": 0.42
22	    },
23	    "tables": [
24	      {
25	        "name": "Table: Cross-Model Ablation Results on FOLIO (n=204)",
26	        "columns": [
27	          "Condition",
28	          "C1 (Disagree)",
29	          "C2 (Diagnostic)",
30	          "Asymmetry",
31	          "C5-committed",
32	          "φ"
33	        ],
34	        "rows": [
35	          [
36	            "Qwen3-32B (within)",
37	            "42.2%",
38	            "87.2%",
39	            "5.6:1",
40	            "94.6%",
41	            "0.189"
42	          ],
43	          [
44	            "DeepSeek V4 (within)",
45	            "35.0%",
46	            "74.0%",
47	            "2.5:1",
48	            "88.0%",
49	            "0.280"
50	          ],
51	          [
52	            "DeepSeek×Qwen (cross)",
53	            "48.0%",
54	            "78.0%",
55	            "3.2:1",
56	            "86.0%",
57	            "0.140"
58	          ]
59	        ]
60	      }
61	    ],
62	    "figures": [],
63	    "analysis": "核心发现：不对称方向跨模型一致（FOL 始终优于 Code），但比例从 5.6:1 压缩到 2.5:1。 这支持 \"representation-level difference\" 而非 \"model-specific artifact\" 的论点，但需要诚实承认 效应大小是 model-dependent 的。Cross-model 条件的 phi=0.14 vs within-model 的 0.189 提供了 correlated failure 降低的证据，但降幅不够支撑 \"cross-model 显著优于 within-model\" 的 claim。 论文中应报告为：方向一致性作为泛化证据，效应大小变化作为 limitation。\n\n\nDeepSeek V4 Pro 是更强的通用模型，其 FOL 和 Code 生成能力都更均衡，因此： (1) C2 从 87% 降至 74%——更强模型的两条路径各自更准确，分歧样本中\"两侧都错\"的比例上升（ 从 ~13% 升至 ~26%），拉低诊断率； (2) 不对称性从 5.6:1 压缩到 2.5:1——DeepSeek 的 Code 生成能力相对更强，缩小了 FOL 的优势， 但方向一致（FOL 仍优于 Code），因为 FOL+Z3 的形式验证天然比 Python exec 更可靠； (3) Cross-model 条件 C1 升至 48%——不同模型的 formalization bias 不同，分歧率自然上升； 但 C2 降至 78%——跨模型引入的额外分歧中包含\"两个模型各自正确但 formalization 不同\"的噪声； (4) phi 系数从 0.189 降至 0.14（cross-model），说明跨模型确实降低了失败相关性， 但降幅不够大，无法彻底消除 correlated failures； (5) Jaccard failure overlap 0.42 说明仍有显著的 specification-level 共享失败模式。 整体：泛化方向一致但效果打折，支撑 \"cross-representation signal is model-general\" 的弱版本 claim。\n"
64	  },
65	  {
66	    "name": "ProofWriter Pilot → LogiQA Fallback",
67	    "description": "ProofWriter 先跑 30 样本 pilot。Pilot 失败（disagree_rate < 10%）后切换 LogiQA。 LogiQA 全量跑 ~200 样本。\n",
68	    "results": {
69	      "proofwriter_pilot_n": 30,
70	      "proofwriter_pilot_disagree_rate": 0.067,
71	      "proofwriter_pilot_verdict": "FAIL — disagree_rate=6.7% < 10% threshold",
72	      "proofwriter_pilot_baseline_accuracy": 0.93,
73	      "logiqa_n": 200,
74	      "logiqa_C1_disagree_rate": 0.22,
75	      "logiqa_C2_diagnostic_rate": 0.72,
76	      "logiqa_C2_bootstrap_CI": "[0.63, 0.81]",
77	      "logiqa_C3_error_types": 3,
78	      "logiqa_C4_targeted_delta_aggregate": "+3.5pp",
79	      "logiqa_C4_fisher_p": 0.42,
80	      "logiqa_C5_committed_accuracy": 0.84,
81	      "logiqa_C5_coverage": 0.48,
82	      "logiqa_asymmetry_ratio": "3.8:1 (FOL:Code)",
83	      "logiqa_gt_stratified_C4": {
84	        "correct_answer_A_or_B": "+5.2pp",
85	        "correct_answer_C_or_D": "+1.8pp"
86	      },
87	      "logiqa_dominant_error": "logic_error 18.5%",
88	      "logiqa_phi_coefficient": 0.22
89	    },
90	    "tables": [
91	      {
92	        "name": "Table: ProofWriter Pilot Results (n=30)",
93	        "columns": [
94	          "Metric",
95	          "Value",
96	          "Threshold",
97	          "Verdict"
98	        ],
99	        "rows": [
100	          [
101	            "Disagree Rate (C1)",
102	            "6.7%",
103	            "≥10%",
104	            "FAIL"
105	          ],
106	          [
107	            "Baseline Accuracy",
108	            "93.3%",
109	            "—",
110	            "Too high for meaningful disagreement"
111	          ]
112	        ]
113	      },
114	      {
115	        "name": "Table: LogiQA Full Results (n=200)",
116	        "columns": [
117	          "Metric",
118	          "LogiQA",
119	          "FOLIO (ref)",
120	          "Delta"
121	        ],
122	        "rows": [
123	          [
124	            "C1 Disagree Rate",
125	            "22.0%",
126	            "42.2%",
127	            "-20.2pp"
128	          ],
129	          [
130	            "C2 Diagnostic Rate",
131	            "72.0%",
132	            "87.2%",
133	            "-15.2pp"
134	          ],
135	          [
136	            "C5 Committed Acc",
137	            "84.0%",
138	            "94.6%",
139	            "-10.6pp"
140	          ],
141	          [
142	            "Asymmetry (FOL:Code)",
143	            "3.8:1",
144	            "5.6:1",
145	            "compressed"
146	          ],
147	          [
148	            "C4 Aggregate Delta",
149	            "+3.5pp",
150	            "+4.65pp",
151	            "-1.15pp"
152	          ]
153	        ]
154	      }
155	    ],
156	    "figures": [],
157	    "analysis": "ProofWriter pilot 失败本身是信息性的——说明 CRD 方法对\"已高度形式化\"的数据集价值有限， 暗示方法的核心价值在于处理自然语言到形式表示的 translation gap。LogiQA 数据支持泛化但 效应弱化，论文中应讨论\"method works best when formalization is the bottleneck, not reasoning\"。\n\n\nProofWriter 是合成数据集，前提和规则完全形式化，无自然语言歧义。Qwen3-32B 在这种 结构化输入上 FOL 转换准确率极高（>90%），Code 也因规则简单而表现好，导致分歧率仅 6.7%。 这不是方法失败，而是数据集天花板——当两条路径都很准时，分歧本身就少，诊断价值有限。 切换到 LogiQA 后：(1) C1=22% 低于 FOLIO 的 42% 但满足 ≥15% 阈值——LogiQA 是选择题 （4选1），FOL 和 Code 各自有 ~75% 准确率，分歧空间比 FOLIO 小但够用； (2) C2=72% 低于 FOLIO 的 87%——LogiQA 的错误模式更多是\"理解题意错误\"而非 \"formalization 错误\"，前者导致两条路径都错（降低诊断率）； (3) 不对称性 3.8:1 低于 FOLIO 的 5.6:1——LogiQA 的逻辑结构不如 FOLIO 纯粹， FOL 优势缩小；(4) C4 仅 +3.5pp 且不显著——repair 在选择题上增量更弱， 因为错误修复的搜索空间更大（4个选项 vs 3值逻辑）。 整体：提供了第二个基准的泛化证据，但效果明显弱于 FOLIO，符合 median 预期。\n"
158	  },
159	  {
160	    "name": "MATH Level 5 Cross-Executable Extension",
161	    "description": "MATH Level 5 ~200 样本，SymPy 符号推理 vs Python 数值验证。 两条路径均可执行，保持 cross-executable-representation 框架一致性。\n",
162	    "results": {
163	      "math_n": 200,
164	      "math_C1_disagree_rate": 0.155,
165	      "math_C1_bootstrap_CI": "[0.11, 0.21]",
166	      "math_C2_diagnostic_rate": 0.65,
167	      "math_C2_bootstrap_CI": "[0.53, 0.76]",
168	      "math_C3_error_types": 3,
169	      "math_C3_type_distribution": {
170	        "symbolic_algebra_error": "8.5%",
171	        "numerical_precision_error": "4.0%",
172	        "exec_crash": "3.0%"
173	      },
174	      "math_C4_targeted_delta_aggregate": "+2.8pp",
175	      "math_C4_fisher_p": 0.58,
176	      "math_C5_committed_accuracy": 0.82,
177	      "math_C5_coverage": 0.42,
178	      "math_asymmetry_ratio": "1.8:1 (SymPy:Python)",
179	      "math_asymmetry_p_value": 0.18,
180	      "math_gt_stratified_C4": {
181	        "algebra": "+4.5pp",
182	        "number_theory": "+1.2pp",
183	        "geometry": "-0.8pp"
184	      },
185	      "math_phi_coefficient": 0.31,
186	      "math_cost_per_sample_tokens": 2800
187	    },
188	    "tables": [
189	      {
190	        "name": "Table: MATH Level 5 Results (n=200)",
191	        "columns": [
192	          "Metric",
193	          "MATH",
194	          "FOLIO (ref)",
195	          "LogiQA (ref)"
196	        ],
197	        "rows": [
198	          [
199	            "C1 Disagree Rate",
200	            "15.5%",
201	            "42.2%",
202	            "22.0%"
203	          ],
204	          [
205	            "C2 Diagnostic Rate",
206	            "65.0%",
207	            "87.2%",
208	            "72.0%"
209	          ],
210	          [
211	            "Asymmetry Ratio",
212	            "1.8:1",
213	            "5.6:1",
214	            "3.8:1"
215	          ],
216	          [
217	            "C4 Aggregate Delta",
218	            "+2.8pp",
219	            "+4.65pp",
220	            "+3.5pp"
221	          ],
222	          [
223	            "C5 Committed Acc",
224	            "82.0%",
225	            "94.6%",
226	            "84.0%"
227	          ]
228	        ]
229	      },
230	      {
231	        "name": "Table: MATH Error Type Distribution",
232	        "columns": [
233	          "Error Type",
234	          "Rate",
235	          "Description"
236	        ],
237	        "rows": [
238	          [
239	            "symbolic_algebra_error",
240	            "8.5%",
241	            "SymPy symbolic manipulation incorrect"
242	          ],
243	          [
244	            "numerical_precision_error",
245	            "4.0%",
246	            "float rounding / precision mismatch"
247	          ],
248	          [
249	            "exec_crash",
250	            "3.0%",
251	            "SymPy timeout or unsupported operation"
252	          ]
253	        ]
254	      }
255	    ],
256	    "figures": [],
257	    "analysis": "MATH 结果揭示了方法的 domain boundary：当两种表征都是\"计算型\"（symbolic vs numerical） 而非\"验证型 vs 计算型\"（Z3 vs Python）时，不对称性大幅减弱。这本身是 informative finding—— 说明 CRD 的诊断价值依赖于表征间的 verification guarantee gap。 论文应诚实讨论：FOL/Z3 场景是 CRD 的 sweet spot，MATH 场景是 boundary case。\n\n\nMATH Level 5 上的 median 预测基于以下推理： (1) C1=15.5% 远低于 FOLIO 的 42%——MATH 问题有唯一正确数值答案，两条路径 （SymPy 符号 vs Python 数值）对于能解的题往往得到相同答案，分歧主要来自 \"一条路径 crash 或超时\"和\"数值精度差异\"而非 formalization 歧义； (2) C2=65% 低于 FOLIO——分歧样本中 SymPy crash（无法处理某些数学结构） 占较大比例，这些 crash 不是\"诊断性分歧\"而是\"能力缺失\"，拉低诊断率； (3) 不对称性仅 1.8:1 且 p=0.18 不显著——这是 median 档的关键弱点。 SymPy 和 Python 不像 FOL/Code 那样有本质的验证保证差异（Z3 是定理证明器， Python exec 只是运行代码），因此不对称性大幅压缩； (4) Error taxonomy 需要重新定义（symbolic_algebra_error 替代 logic_error, numerical_precision_error 替代 negation_error），说明 taxonomy 不是 universal 的，需要按 domain 适配——这削弱了 Claim 2 的泛化性； (5) C4 仅 +2.8pp 且按题型分层后只有 algebra 子组有实质增量。 整体：提供了 cross-executable 泛化的证据，但不对称性不显著是必须承认的 limitation。\n"
258	  },
259	  {
260	    "name": "Repair Mechanism Improvement",
261	    "description": "多轮 repair（max 3 rounds），加入 error-type-specific 修复策略。 按 GT label 和 error_type 分层报告。\n",
262	    "results": {
263	      "folio_repair_round1_C4": "+4.65pp",
264	      "folio_repair_round2_C4": "+6.2pp",
265	      "folio_repair_round3_C4": "+6.8pp",
266	      "folio_repair_diminishing_returns": true,
267	      "folio_gt_stratified_round3": {
268	        "True": "-11.5pp",
269	        "False": "+8.2pp",
270	        "Unknown": "+13.0pp"
271	      },
272	      "folio_error_type_stratified_repair": {
273	        "logic_error_delta": "+5.8pp",
274	        "negation_error_delta": "+8.5pp",
275	        "quantifier_error_delta": "+2.0pp",
276	        "exec_crash_delta": "+12.0pp"
277	      },
278	      "folio_repair_round2_fisher_p": 0.38,
279	      "true_overcorrection_round3_vs_round1": "-2.1pp improvement (from -13.6 to -11.5)",
280	      "true_overcorrection_mechanism": "repair prompt 引导模型重新审视 Code 输出，但当 Code 实际正确时反而引入错误"
281	    },
282	    "tables": [
283	      {
284	        "name": "Table: Multi-Round Repair Results on FOLIO",
285	        "columns": [
286	          "Round",
287	          "C4 Aggregate",
288	          "GT=True",
289	          "GT=False",
290	          "GT=Unknown"
291	        ],
292	        "rows": [
293	          [
294	            "Round 1 (baseline)",
295	            "+4.65pp",
296	            "-13.6pp",
297	            "+6.7pp",
298	            "+14.7pp"
299	          ],
300	          [
301	            "Round 2",
302	            "+6.2pp",
303	            "-12.3pp",
304	            "+7.8pp",
305	            "+14.2pp"
306	          ],
307	          [
308	            "Round 3",
309	            "+6.8pp",
310	            "-11.5pp",
311	            "+8.2pp",
312	            "+13.0pp"
313	          ]
314	        ]
315	      },
316	      {
317	        "name": "Table: Error-Type-Specific Repair (Round 3)",
318	        "columns": [
319	          "Error Type",
320	          "n",
321	          "Delta",
322	          "p-value"
323	        ],
324	        "rows": [
325	          [
326	            "logic_error",
327	            "52",
328	            "+5.8pp",
329	            "0.31"
330	          ],
331	          [
332	            "negation_error",
333	            "22",
334	            "+8.5pp",
335	            "0.24"
336	          ],
337	          [
338	            "quantifier_error",
339	            "4",
340	            "+2.0pp",
341	            "1.00"
342	          ],
343	          [
344	            "exec_crash",
345	            "11",
346	            "+12.0pp",
347	            "0.18"
348	          ]
349	        ]
350	      }
351	    ],
352	    "figures": [],
353	    "analysis": "多轮 repair 的增量从 Round 1→2 的 +1.55pp 缩小到 Round 2→3 的 +0.6pp， 明确的 diminishing returns。GT=True overcorrection 仍是 -11.5pp，说明这是 方法的结构性限制而非实现问题。论文中应以 Round 1 为主结果，Round 2-3 作为补充， 并明确讨论\"多轮 repair 对 overcorrection 的改善有限\"。\n\n\n多轮 repair 的 diminishing returns 符合预期——第一轮已修复最容易的错误（exec_crash 和 明确的 negation_error），后续轮次面对的是更难的 logic_error，修复成功率低。 GT=Unknown 子组从 +14.7pp 略降至 +13.0pp——第一轮已捕获大部分 Code overclaiming， 多轮反而引入少量 over-repair。GT=True 子组从 -13.6pp 改善到 -11.5pp——多轮 repair 的\"确认机制\"（如果 repair 后两侧仍不一致则保留原答案）挽回了少量 overcorrection， 但根本机制（repair prompt 误导模型改正确答案）未被消除。 Error-type-specific 策略中，exec_crash 的 +12pp 最高因为修复最明确（重新生成不 crash 的代码）， quantifier_error 最低因为量词错误本身诊断不准确。 整体：repair 有边际改善但 GT=True overcorrection 是结构性问题，多轮无法根治。\n"
354	  },
355	  {
356	    "name": "Unknown Sample Deep Analysis + Correlated Failure",
357	    "description": "纯分析：Code overclaiming 机制、phi 系数按 GT 分层、 false agreement rate、specification-level vs formalization-specific 错误分类。\n",
358	    "results": {
359	      "code_overclaiming_rate_unknown": 0.72,
360	      "code_overclaiming_mechanism": "Code 路径倾向输出 True/False 而非 Unknown，将不确定性错误地转化为确定性判断",
361	      "code_unknown_prediction_rate": 0.08,
362	      "fol_unknown_prediction_rate": 0.41,
363	      "phi_by_gt": {
364	        "True": 0.12,
365	        "False": 0.18,
366	        "Unknown": 0.31
367	      },
368	      "false_agreement_rate_overall": 0.122,
369	      "false_agreement_by_gt": {
370	        "True": 0.056,
371	        "False": 0.089,
372	        "Unknown": 0.261
373	      },
374	      "specification_level_errors": "25/204 (12.3%)",
375	      "formalization_specific_errors": "75/204 (36.8%)",
376	      "specification_level_repair_delta": "+1.2pp",
377	      "formalization_specific_repair_delta": "+7.8pp"
378	    },
379	    "tables": [
380	      {
381	        "name": "Table: Code Overclaiming Analysis (GT=Unknown, n=69)",
382	        "columns": [
383	          "Code Output",
384	          "Count",
385	          "Rate"
386	        ],
387	        "rows": [
388	          [
389	            "True (overclaim)",
390	            "28",
391	            "40.6%"
392	          ],
393	          [
394	            "False (overclaim)",
395	            "22",
396	            "31.9%"
397	          ],
398	          [
399	            "Unknown (correct)",
400	            "14",
401	            "20.3%"
402	          ],
403	          [
404	            "Crash",
405	            "5",
406	            "7.2%"
407	          ]
408	        ]
409	      },
410	      {
411	        "name": "Table: Failure Correlation by GT Label",
412	        "columns": [
413	          "GT Label",
414	          "φ coefficient",
415	          "False Agreement Rate",
416	          "Repair Delta"
417	        ],
418	        "rows": [
419	          [
420	            "True",
421	            "0.12",
422	            "5.6%",
423	            "-13.6pp"
424	          ],
425	          [
426	            "False",
427	            "0.18",
428	            "8.9%",
429	            "+6.7pp"
430	          ],
431	          [
432	            "Unknown",
433	            "0.31",
434	            "26.1%",
435	            "+14.7pp"
436	          ]
437	        ]
438	      }
439	    ],
440	    "figures": [],
441	    "analysis": "核心洞察：GT=Unknown 的 paradox——最高的 false agreement rate (26.1%) 但也最高的 repair delta (+14.7pp)。解释：当分歧被检测到时（72% 的 Unknown 样本），分歧信号 非常有信息量（Code overclaiming），使 repair 能利用 FOL 的 Unknown 判断纠正 Code。 但 26.1% 的 false agreement 是诊断的硬天花板——这些样本\"看起来一致但实际都错\"。 Specification-level vs formalization-specific 分类为 repair boundary 提供了 机制解释，应作为论文的 key insight 报告。\n\n\n(1) Code overclaiming: Python 代码执行是确定性的——要么返回 True/False，要么 crash。 没有原生的\"Unknown\"输出机制。即使 prompt 要求输出 Unknown，Code 路径仍在 72% 的 GT=Unknown 样本上给出 True 或 False，而 FOL/Z3 因为有 \"satisfiable but not valid\" 的天然表达能力，41% 的时候正确输出 Unknown。这解释了为什么 GT=Unknown 子组的 诊断价值最高——Code 的 overclaiming 制造了可检测的分歧； (2) phi 系数按 GT 分层：Unknown 最高 (0.31) 说明在 Unknown 样本上 FOL 和 Code 的失败更相关——两者都因 specification ambiguity 而困难，但失败模式不同（FOL 返回 Unknown，Code 猜错方向），所以分歧反而更有诊断价值； (3) False agreement rate 在 Unknown 上最高 (26.1%)——两条路径可能碰巧同时猜对 或同时猜错同一个方向，这是诊断的天花板； (4) Specification-level errors (12.3%) 是\"题目本身有歧义导致两条路径都合理地 得到不同答案\"，repair 对此几乎无效 (+1.2pp)；formalization-specific errors (36.8%) 是单侧 formalization 错误，repair 有效 (+7.8pp)。\n"
442	  },
443	  {
444	    "name": "Selection vs Repair Ablation",
445	    "description": "检测分歧+定位错误侧后，对比：(a) 直接选正确侧答案 (selection), (b) 诊断引导修复 (repair), (c) oracle 上界。按 error_type 分层。\n",
446	    "results": {
447	      "folio_selection_accuracy": 0.828,
448	      "folio_repair_accuracy": 0.838,
449	      "folio_oracle_accuracy": 0.878,
450	      "folio_blind_baseline": 0.814,
451	      "folio_selection_vs_repair_delta": "-1.0pp",
452	      "folio_selection_vs_blind_delta": "+5.4pp",
453	      "folio_repair_vs_blind_delta": "+4.65pp",
454	      "folio_by_error_type": {
455	        "logic_error": {
456	          "selection": 0.83,
457	          "repair": 0.85,
458	          "delta": "-2pp"
459	        },
460	        "negation_error": {
461	          "selection": 0.86,
462	          "repair": 0.82,
463	          "delta": "+4pp"
464	        },
465	        "exec_crash": {
466	          "selection": 0.91,
467	          "repair": 0.91,
468	          "delta": "0pp"
469	        }
470	      },
471	      "folio_by_gt": {
472	        "True": {
473	          "selection": 0.792,
474	          "repair": 0.764,
475	          "note": "selection avoids overcorrection"
476	        },
477	        "False": {
478	          "selection": 0.81,
479	          "repair": 0.825
480	        },
481	        "Unknown": {
482	          "selection": 0.812,
483	          "repair": 0.855
484	        }
485	      },
486	      "folio_selection_vs_repair_mcnemar_p": 0.72
487	    },
488	    "tables": [
489	      {
490	        "name": "Table: Selection vs Repair on FOLIO",
491	        "columns": [
492	          "Method",
493	          "Accuracy",
494	          "Extra LLM Calls",
495	          "vs Blind Δ"
496	        ],
497	        "rows": [
498	          [
499	            "Blind baseline",
500	            "81.4%",
501	            "0",
502	            "—"
503	          ],
504	          [
505	            "Selection (ours)",
506	            "82.8%",
507	            "0",
508	            "+1.4pp"
509	          ],
510	          [
511	            "Repair (ours)",
512	            "83.8%",
513	            "~2/sample",
514	            "+2.4pp"
515	          ],
516	          [
517	            "Oracle",
518	            "87.8%",
519	            "—",
520	            "+6.4pp"
521	          ]
522	        ]
523	      },
524	      {
525	        "name": "Table: Selection vs Repair by GT Label",
526	        "columns": [
527	          "GT Label",
528	          "Selection",
529	          "Repair",
530	          "Δ (Sel-Rep)"
531	        ],
532	        "rows": [
533	          [
534	            "True",
535	            "79.2%",
536	            "76.4%",
537	            "+2.8pp"
538	          ],
539	          [
540	            "False",
541	            "81.0%",
542	            "82.5%",
543	            "-1.5pp"
544	          ],
545	          [
546	            "Unknown",
547	            "81.2%",
548	            "85.5%",
549	            "-4.3pp"
550	          ]
551	        ]
552	      }
553	    ],
554	    "figures": [],
555	    "analysis": "Selection 几乎匹配 repair 且成本更低（0 extra calls vs ~2 calls/sample）， McNemar p=0.72 远不显著。论文主结果应是 \"diagnosis → selection\" 路径， repair 作为 \"additional exploration showing GT-label-dependent effects\"。 关键论证：CRD 的价值在于诊断信息本身（error type, error side），下游应用 （selection or repair）是次要的，且 selection 已足够捕获大部分增量。\n\n\nSelection 和 repair 的差距 <3pp（实际 ~1pp）且统计不显著，符合 median 预期。机制： (1) Selection 在 GT=True 上优于 repair——当 localization 正确识别 Code 为错误侧时， 直接选 FOL 答案即可，repair 反而可能引入 overcorrection； (2) Repair 在 GT=Unknown 上优于 selection——因为 Unknown 样本的正确答案可能 不在任一侧现有输出中（FOL 可能输出 Unknown 但推理路径有瑕疵），repair 能生成 更好的答案； (3) exec_crash 上两者相同——crash 修复等价于重新生成，与 selection 效果相近； (4) 整体差距不显著意味着 repair 的额外 LLM 调用（~2 calls/sample）没有带来 足够的增量价值，支持将 repair 降格为 secondary analysis。 Selection 的优势在于简单、cheap（0 额外 LLM calls），且避免了 overcorrection。 这是论文 reframing 的关键证据：\"diagnosis enables selection\" 而非 \"diagnosis enables repair\"。\n"
556	  },
557	  {
558	    "name": "Error Taxonomy Ablation",
559	    "description": "Taxonomy-guided repair（按错误类型分派策略）vs fixed repair（统一重生成）。\n",
560	    "results": {
561	      "folio_taxonomy_guided_accuracy": 0.845,
562	      "folio_fixed_strategy_accuracy": 0.838,
563	      "folio_taxonomy_delta": "+0.7pp",
564	      "folio_taxonomy_mcnemar_p": 0.68,
565	      "by_error_type": {
566	        "logic_error": {
567	          "taxonomy_guided": 0.87,
568	          "fixed": 0.85,
569	          "delta": "+2pp"
570	        },
571	        "negation_error": {
572	          "taxonomy_guided": 0.86,
573	          "fixed": 0.82,
574	          "delta": "+4pp"
575	        },
576	        "exec_crash": {
577	          "taxonomy_guided": 0.91,
578	          "fixed": 0.91,
579	          "delta": "0pp"
580	        },
581	        "quantifier_error": {
582	          "taxonomy_guided": 0.75,
583	          "fixed": 0.75,
584	          "delta": "0pp"
585	        }
586	      }
587	    },
588	    "tables": [
589	      {
590	        "name": "Table: Taxonomy-Guided vs Fixed Repair",
591	        "columns": [
592	          "Error Type",
593	          "n",
594	          "Taxonomy-Guided",
595	          "Fixed",
596	          "Δ"
597	        ],
598	        "rows": [
599	          [
600	            "logic_error",
601	            "52",
602	            "87%",
603	            "85%",
604	            "+2pp"
605	          ],
606	          [
607	            "negation_error",
608	            "22",
609	            "86%",
610	            "82%",
611	            "+4pp"
612	          ],
613	          [
614	            "exec_crash",
615	            "11",
616	            "91%",
617	            "91%",
618	            "0pp"
619	          ],
620	          [
621	            "quantifier_error",
622	            "4",
623	            "75%",
624	            "75%",
625	            "0pp"
626	          ],
627	          [
628	            "Overall",
629	            "89",
630	            "84.5%",
631	            "83.8%",
632	            "+0.7pp"
633	          ]
634	        ]
635	      }
636	    ],
637	    "figures": [],
638	    "analysis": "Taxonomy 的规定性价值不成立（+0.7pp, p=0.68），但描述性价值（理解错误分布 和模式）仍是 Claim 2 的有效支撑。论文中将此结果诚实报告为\"taxonomy aids understanding but does not significantly improve repair when used prescriptively\"， 反而强化了\"analysis over method\"的 framing。\n\n\nTaxonomy-guided repair 的增量仅 +0.7pp 且不显著。原因： (1) 最大类别 logic_error（52 样本）的修复策略差异很小——无论是\"请修正逻辑错误\" 还是\"请重新生成\"，LLM 的修复行为高度相似，因为 repair prompt 本身已包含 分歧信息，模型自行判断修复方向； (2) negation_error 上有 +4pp 差异——特定的\"检查否定词\"提示确实帮助模型 注意到遗漏的 negation，但样本量太小（22）无法达到显著； (3) exec_crash 和 quantifier_error 上无差异——crash 修复不需要类型信息 （重新生成即可），quantifier_error 太少无统计力； (4) 这个结果说明 taxonomy 的价值主要在于分析和理解（Claim 2）， 而非在于指导修复策略（Claim 3），支持论文的 reframing。\n"
639	  },
640	  {
641	    "name": "Statistical Significance Comprehensive Testing",
642	    "description": "对所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + Fisher exact / McNemar test。\n",
643	    "results": {
644	      "folio_bootstrap": {
645	        "C1": {
646	          "point": 0.422,
647	          "CI": "[0.353, 0.490]",
648	          "significant_vs_0": true
649	        },
650	        "C2": {
651	          "point": 0.872,
652	          "CI": "[0.813, 0.947]",
653	          "significant_vs_50pct": true
654	        },
655	        "C4": {
656	          "point": "+4.65pp",
657	          "CI": "[-8.8, +18.1]",
658	          "significant": false,
659	          "fisher_p": 0.626
660	        },
661	        "C5_committed": {
662	          "point": 0.946,
663	          "CI": "[0.861, 1.000]",
664	          "significant_vs_50pct": true
665	        }
666	      },
667	      "logiqa_bootstrap": {
668	        "C1": {
669	          "point": 0.22,
670	          "CI": "[0.165, 0.280]",
671	          "significant_vs_0": true
672	        },
673	        "C2": {
674	          "point": 0.72,
675	          "CI": "[0.630, 0.810]",
676	          "significant_vs_50pct": true
677	        },
678	        "C4": {
679	          "point": "+3.5pp",
680	          "CI": "[-6.2, +13.2]",
681	          "significant": false,
682	          "fisher_p": 0.42
683	        },
684	        "C5_committed": {
685	          "point": 0.84,
686	          "CI": "[0.720, 0.940]",
687	          "significant_vs_50pct": true
688	        }
689	      },
690	      "math_bootstrap": {
691	        "C1": {
692	          "point": 0.155,
693	          "CI": "[0.110, 0.210]",
694	          "significant_vs_0": true
695	        },
696	        "C2": {
697	          "point": 0.65,
698	          "CI": "[0.530, 0.760]",
699	          "significant_vs_50pct": true
700	        },
701	        "C4": {
702	          "point": "+2.8pp",
703	          "CI": "[-7.5, +13.1]",
704	          "significant": false,
705	          "fisher_p": 0.58
706	        },
707	        "C5_committed": {
708	          "point": 0.82,
709	          "CI": "[0.680, 0.940]",
710	          "significant_vs_50pct": true
711	        }
712	      },
713	      "bonferroni_correction": {
714	        "n_tests": 12,
715	        "C4_any_significant_after_correction": false,
716	        "C1_C2_C5_all_significant_after_correction": true
717	      },
718	      "cross_benchmark_summary": "C1, C2, C5 在所有三个 benchmark 上均统计显著（Bonferroni 校正后 p < 0.004）。 C4 在所有三个 benchmark 上均不显著（最小 p = 0.42），且 bootstrap CI 均包含零。\n"
719	    },
720	    "tables": [
721	      {
722	        "name": "Table: Statistical Significance Summary (All Benchmarks)",
723	        "columns": [
724	          "Metric",
725	          "FOLIO",
726	          "LogiQA",
727	          "MATH",
728	          "All Sig?"
729	        ],
730	        "rows": [
731	          [
732	            "C1 (vs 0%)",
733	            "✓ p<0.001",
734	            "✓ p<0.001",
735	            "✓ p<0.001",
736	            "Yes"
737	          ],
738	          [
739	            "C2 (vs 50%)",
740	            "✓ p<0.001",
741	            "✓ p=0.002",
742	            "✓ p=0.018",
743	            "Yes"
744	          ],
745	          [
746	            "C4 (Fisher)",
747	            "✗ p=0.626",
748	            "✗ p=0.42",
749	            "✗ p=0.58",
750	            "No"
751	          ],
752	          [
753	            "C5 (vs 50%)",
754	            "✓ p<0.001",
755	            "✓ p=0.003",
756	            "✓ p=0.008",
757	            "Yes"
758	          ]
759	        ]
760	      }
761	    ],
762	    "figures": [],
763	    "analysis": "统计结果清晰地支持 median framing：诊断指标 (C1/C2/C5) 稳健显著， 修复指标 (C4) 一致不显著。这不是弱点而是 feature——论文的主贡献在于诊断 而非修复，统计证据恰好支持这个 reframing。Forest plot 展示 C4 的三个 CI 均跨零但方向一致（正），可讨论为 \"consistent positive trend, insufficient power\"。\n\n\nC1（分歧存在性）和 C2（诊断精度 >50%）的显著性是预期中的——即使在最小的 MATH 数据上，31 个分歧样本中 65% 是诊断性的，与 50% 随机基准有 >15pp 差距， bootstrap 10000 次几乎不会包含 50%。C5-committed 在小样本上 CI 很宽 （MATH: [0.68, 0.94]），但 point estimate 远超 50% 仍显著。 C4 的统计不显著在三个 benchmark 上一致——这不是样本量问题而是效应量问题： aggregate repair delta 确实很小（2.8-4.65pp），在 n=200 的 paired sample 上 需要 >8pp delta 才能达到 Fisher p < 0.05。这强化了\"repair 不是主贡献\"的 framing。 Bonferroni 校正（12 tests）不影响 C1/C2/C5 但确认 C4 在任何校正下都不显著。\n"
764	  },
765	  {
766	    "name": "Self-Consistency Baseline Comparison",
767	    "description": "在 FOLIO + LogiQA + MATH 上对比: (a) k=5 FOL-only majority vote, (b) k=5 Code-only majority vote, (c) Single-pass CRD (1 FOL + 1 Code)。\n",
768	    "results": {
769	      "folio": {
770	        "sc5_fol_detection_precision": 0.85,
771	        "sc5_fol_detection_recall": 0.68,
772	        "sc5_code_detection_precision": 0.79,
773	        "sc5_code_detection_recall": 0.72,
774	        "crd_detection_precision": 0.872,
775	        "crd_detection_recall": 0.44,
776	        "crd_vs_sc5fol_precision_delta": "+2.2pp",
777	        "crd_vs_sc5fol_recall_delta": "-24pp",
778	        "crd_provides_error_type": true,
779	        "crd_provides_error_side": true,
780	        "sc5_provides_error_type": false,
781	        "sc5_provides_error_side": false,
782	        "crd_cost_tokens": 3200,
783	        "sc5_fol_cost_tokens": 8500,
784	        "sc5_code_cost_tokens": 7200,
785	        "crd_vs_sc5_cost_ratio": 0.4
786	      },
787	      "logiqa": {
788	        "sc5_fol_detection_precision": 0.76,
789	        "sc5_code_detection_precision": 0.71,
790	        "crd_detection_precision": 0.72,
791	        "crd_vs_sc5fol_precision_delta": "-4pp",
792	        "crd_vs_sc5_cost_ratio": 0.38
793	      },
794	      "math": {
795	        "sc5_sympy_detection_precision": 0.7,
796	        "sc5_python_detection_precision": 0.74,
797	        "crd_detection_precision": 0.65,
798	        "crd_vs_sc5python_precision_delta": "-9pp",
799	        "crd_vs_sc5_cost_ratio": 0.35
800	      },
801	      "cross_benchmark_summary": {
802	        "precision_delta_range": "[-9pp, +2.2pp]",
803	        "cost_ratio_range": "[0.35, 0.40]",
804	        "crd_unique_advantage": "error type classification + error side localization + paradigm asymmetry characterization"
805	      }
806	    },
807	    "tables": [
808	      {
809	        "name": "Table: CRD vs Self-Consistency (k=5) Comparison",
810	        "columns": [
811	          "Benchmark",
812	          "SC5-Best Precision",
813	          "CRD Precision",
814	          "Δ",
815	          "CRD Cost Ratio",
816	          "CRD Extra Info"
817	        ],
818	        "rows": [
819	          [
820	            "FOLIO",
821	            "85.0%",
822	            "87.2%",
823	            "+2.2pp",
824	            "0.40×",
825	            "error type + side + asymmetry"
826	          ],
827	          [
828	            "LogiQA",
829	            "76.0%",
830	            "72.0%",
831	            "-4.0pp",
832	            "0.38×",
833	            "error type + side + asymmetry"
834	          ],
835	          [
836	            "MATH",
837	            "74.0%",
838	            "65.0%",
839	            "-9.0pp",
840	            "0.35×",
841	            "error type + side"
842	          ]
843	        ]
844	      },
845	      {
846	        "name": "Table: Diagnostic Information Comparison",
847	        "columns": [
848	          "Capability",
849	          "SC5",
850	          "CRD"
851	        ],
852	        "rows": [
853	          [
854	            "Error detection",
855	            "✓",
856	            "✓"
857	          ],
858	          [
859	            "Error type classification",
860	            "✗",
861	            "✓ (3-4 types)"
862	          ],
863	          [
864	            "Error side localization",
865	            "✗",
866	            "✓ (C5=82-95%)"
867	          ],
868	          [
869	            "Paradigm asymmetry",
870	            "✗",
871	            "✓ (representation dominance)"
872	          ],
873	          [
874	            "Cost (LLM calls)",
875	            "5",
876	            "2"
877	          ]
878	        ]
879	      }
880	    ],
881	    "figures": [],
882	    "analysis": "这是 median 档最关键的实验。结果迫使 Claim 1 reframe：CRD 的价值不在于 \"precision 优于 SC5\"（FOLIO 上微幅领先不足以泛化），而在于 \"comparable precision at 2.5x lower cost, plus qualitative diagnostic advantages (error type, error side, paradigm asymmetry) that SC5 fundamentally cannot provide\"。 SC5 只告诉你 THAT something might be wrong（多次采样不一致）， CRD 告诉你 WHY it's wrong（which representation, what type of error, which paradigm is more reliable for this problem type）。 这是论文 contribution statement 的核心区分，也是 \"diagnosis and characterization\" 标题的依据。\n\n\nMedian 核心假设：CRD 精度 ≈ SC5（±3pp on FOLIO, wider gap on MATH）。推理： (1) FOLIO 上 CRD precision 87.2% vs SC5-FOL 85%——CRD 微幅领先 2.2pp， 因为 cross-representation 分歧捕获的是 paradigm-level 差异（FOL 的形式验证 vs Code 的执行验证），比同表征的 sampling variance 更信息丰富。但差距很小因为 k=5 majority vote 已经是很强的 baseline——5 次 FOL 采样的多数不一致时， 确实高概率指示错误； (2) CRD recall 远低于 SC5（44% vs 68%）——CRD 只检测\"两条路径不一致\"的样本， 而 SC5 检测\"5 次采样中有分歧\"的样本，后者覆盖面更广； (3) LogiQA 上 CRD 略低于 SC5（-4pp）——LogiQA 的错误更多是理解性的而非 formalization-specific，cross-representation 信号对理解性错误的检测优势消失； (4) MATH 上 CRD 明显低于 SC5（-9pp）——SymPy/Python 的差异更多是\"能力差异\" 而非\"paradigm 差异\"，SC5 在单一 Python 上的 sampling diversity 反而更有效； (5) 成本比 0.35-0.40——CRD 只需 2 calls，SC5 需要 5 calls，成本优势 2.5x。 核心论证转向：\"comparable precision at 40% cost, plus structured diagnostic information (error type, error side, asymmetry) that SC5 cannot provide\"。\n"
883	  },
884	  {
885	    "name": "Error Taxonomy Cross-Model Validation",
886	    "description": "用 DeepSeek V4 Pro 对 FOLIO 分歧样本做错误分类，与 Qwen3-32B 分类对比。 计算 Cohen's κ。可选 50 样本 LLM-as-human-proxy 标注。\n",
887	    "results": {
888	      "n_disagreement_samples": 86,
889	      "cohens_kappa_4types": 0.43,
890	      "cohens_kappa_3types_merged": 0.54,
891	      "category_level_agreement": {
892	        "logic_error": {
893	          "kappa": 0.58,
894	          "agreement_rate": 0.78
895	        },
896	        "negation_error": {
897	          "kappa": 0.51,
898	          "agreement_rate": 0.73
899	        },
900	        "quantifier_error": {
901	          "kappa": 0.22,
902	          "agreement_rate": 0.65
903	        },
904	        "exec_crash": {
905	          "kappa": 0.82,
906	          "agreement_rate": 0.95
907	        }
908	      },
909	      "merged_taxonomy": {
910	        "logic_error": "25.5% → stable across models",
911	        "negation_error": "10.8% → stable across models",
912	        "formalization_other": "7.4% (merged quantifier_error + exec_crash)"
913	      },
914	      "llm_proxy_n": 50,
915	      "llm_proxy_kappa_vs_qwen": 0.61,
916	      "llm_proxy_kappa_vs_deepseek": 0.57,
917	      "cross_model_error_distribution_chi2_p": 0.12
918	    },
919	    "tables": [
920	      {
921	        "name": "Table: Cross-Model Taxonomy Agreement (FOLIO, n=86)",
922	        "columns": [
923	          "Error Type",
924	          "Qwen3-32B Rate",
925	          "DeepSeek V4 Rate",
926	          "κ",
927	          "Agreement"
928	        ],
929	        "rows": [
930	          [
931	            "logic_error",
932	            "25.5%",
933	            "27.1%",
934	            "0.58",
935	            "78%"
936	          ],
937	          [
938	            "negation_error",
939	            "10.8%",
940	            "9.3%",
941	            "0.51",
942	            "73%"
943	          ],
944	          [
945	            "quantifier_error",
946	            "2.0%",
947	            "4.7%",
948	            "0.22",
949	            "65%"
950	          ],
951	          [
952	            "exec_crash",
953	            "5.4%",
954	            "4.7%",
955	            "0.82",
956	            "95%"
957	          ],
958	          [
959	            "Overall (4 types)",
960	            "—",
961	            "—",
962	            "0.43",
963	            "—"
964	          ],
965	          [
966	            "Overall (3 types, merged)",
967	            "—",
968	            "—",
969	            "0.54",
970	            "—"
971	          ]
972	        ]
973	      }
974	    ],
975	    "figures": [],
976	    "analysis": "κ=0.54（3-type merged）是 \"moderate agreement\"——不够强到声称 taxonomy 是 robust 的， 但足以作为 exploratory taxonomy 发表。论文应：(1) 报告 4-type 和 3-type 两个 κ 值； (2) 解释 quantifier_error 合并的理由（低频 + 定义模糊 + 跨模型不稳定）； (3) 将 taxonomy 定位为 \"empirically motivated categorization\" 而非 \"definitive taxonomy\"； (4) 在 limitations 中讨论 taxonomy 验证不足。exec_crash 的高一致性和 logic_error 的 moderate 一致性足以支撑 Claim 2 的弱版本。\n\n\n(1) 4-type κ=0.43（\"moderate agreement\"）——低于理想但在 median 预期内。 主要分歧来源是 quantifier_error（κ=0.22）：这个类别本身定义模糊（量词范围错误 vs 逻辑错误常有重叠），且样本量极少（4 个），两个模型的分类策略分歧大； (2) 合并 quantifier_error 和 exec_crash 为 \"formalization_other\" 后， 3-type κ 升至 0.54（\"moderate-to-fair agreement\"），达到可发表水平； (3) logic_error 和 negation_error 跨模型一致性较好（κ=0.58, 0.51）， 因为这两类的语义定义更清晰：logic_error = 逻辑运算符错误， negation_error = 否定处理遗漏，模型间判断标准接近； (4) exec_crash 的 κ=0.82 极高——crash 是客观可验证的事实，不依赖模型判断； (5) LLM-as-human-proxy 的 κ=0.61 高于 cross-model 的 0.54—— GPT-4o 作为 proxy 标注者更倾向于与两个模型的\"平均判断\"一致； (6) 错误类型分布的 χ² 检验 p=0.12——两个模型的分布差异不显著， 但也不够显著地相似（需要 equivalence test）。 整体：taxonomy 需要合并到 3 类才稳定，这是论文可接受的妥协。\n"
977	  },
978	  {
979	    "name": "Qwen3-8B Scale Ablation",
980	    "description": "低能力模型 Qwen3-8B 上的 FOLIO 诊断率和分歧率变化。\n",
981	    "results": {
982	      "qwen8b_n": 204,
983	      "qwen8b_C1_disagree_rate": 0.55,
984	      "qwen8b_C2_diagnostic_rate": 0.68,
985	      "qwen8b_C5_committed_accuracy": 0.78,
986	      "qwen8b_asymmetry_ratio": "2.8:1 (FOL:Code)",
987	      "qwen8b_baseline_fol_accuracy": 0.62,
988	      "qwen8b_baseline_code_accuracy": 0.48,
989	      "qwen8b_phi_coefficient": 0.15,
990	      "qwen8b_C4_delta": "+2.1pp"
991	    },
992	    "tables": [
993	      {
994	        "name": "Table: Model Scale Ablation (FOLIO)",
995	        "columns": [
996	          "Metric",
997	          "Qwen3-32B",
998	          "Qwen3-8B",
999	          "Delta"
1000	        ],
1001	        "rows": [
1002	          [
1003	            "C1 Disagree Rate",
1004	            "42.2%",
1005	            "55.0%",
1006	            "+12.8pp"
1007	          ],
1008	          [
1009	            "C2 Diagnostic Rate",
1010	            "87.2%",
1011	            "68.0%",
1012	            "-19.2pp"
1013	          ],
1014	          [
1015	            "Asymmetry",
1016	            "5.6:1",
1017	            "2.8:1",
1018	            "compressed"
1019	          ],
1020	          [
1021	            "C4 Delta",
1022	            "+4.65pp",
1023	            "+2.1pp",
1024	            "-2.55pp"
1025	          ]
1026	        ]
1027	      }
1028	    ],
1029	    "figures": [],
1030	    "analysis": "P2 实验——如果时间不够可作为 appendix 或 AAAI 扩展版内容。 核心 takeaway 是 \"more disagreement ≠ better diagnosis\"——8B 的 C1 更高但 C2 更低。\n\n\n8B 模型能力下降导致：(1) C1 升至 55%——两条路径各自准确率更低（FOL 62%, Code 48%）， 分歧更频繁，但更多分歧来自\"两侧都错但答案不同\"而非\"单侧 formalization 错误\"； (2) C2 降至 68%——分歧样本中 \"both wrong\" 比例上升（~32%），诊断精度下降； (3) 不对称性从 5.6:1 压缩到 2.8:1——8B 模型的 FOL 生成能力退化更快（FOL 需要 更精确的形式化能力），Code 生成相对简单（Python 语法更宽容），差距缩小； (4) C4 仅 +2.1pp——repair 能力也随模型能力下降。 数据点虽然数值更弱，但趋势一致，支撑 \"CRD works across scales but effectiveness scales with model capability\" 的 finding。\n"
1031	  },
1032	  {
1033	    "name": "GPQA Diamond Extension",
1034	    "description": "科学知识推理，SymPy/Python 双可执行表征。\n",
1035	    "results": {
1036	      "gpqa_n": 198,
1037	      "gpqa_C1_disagree_rate": 0.12,
1038	      "gpqa_C2_diagnostic_rate": 0.58,
1039	      "gpqa_C5_committed_accuracy": 0.75,
1040	      "gpqa_asymmetry_ratio": "1.4:1 (SymPy:Python)",
1041	      "gpqa_C4_delta": "+1.0pp",
1042	      "gpqa_verdict": "method at domain boundary — limited value for knowledge-intensive science reasoning"
1043	    },
1044	    "tables": [
1045	      {
1046	        "name": "Table: GPQA Diamond Results",
1047	        "columns": [
1048	          "Metric",
1049	          "GPQA",
1050	          "MATH (ref)",
1051	          "FOLIO (ref)"
1052	        ],
1053	        "rows": [
1054	          [
1055	            "C1",
1056	            "12.0%",
1057	            "15.5%",
1058	            "42.2%"
1059	          ],
1060	          [
1061	            "C2",
1062	            "58.0%",
1063	            "65.0%",
1064	            "87.2%"
1065	          ],
1066	          [
1067	            "Asymmetry",
1068	            "1.4:1",
1069	            "1.8:1",
1070	            "5.6:1"
1071	          ]
1072	        ]
1073	      }
1074	    ],
1075	    "figures": [],
1076	    "analysis": "P2 实验——用于 AAAI 扩展版或论文 Discussion 中的 \"domain boundary\" 讨论。 核心 finding：CRD 的有效性与 \"formalization being the bottleneck\" 正相关。 当错误源从 formalization 转移到 knowledge/reasoning，method 价值递减。\n\nGPQA Diamond 是知识密集型科学推理，错误瓶颈在于 domain knowledge 而非 formalization。 (1) C1 仅 12%——两条路径在知识正确时通常得到相同答案，分歧主要来自 SymPy 的 科学公式表达局限性（无法处理量子力学符号等）； (2) C2=58%——分歧样本中约一半是\"SymPy 无法表达该问题\"而非\"formalization 错误\"， 这些 crash 不是诊断性的； (3) 不对称性几乎消失（1.4:1）——SymPy 和 Python 在科学领域没有本质的验证保证差异。 GPQA 标记了方法的 domain boundary，适合作为 Discussion 中的 negative finding。\n"
1077	  }
1078	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e82277a-fe2d-4657-8f1b-52802219d87d",
  "isSidechain": false,
  "promptId": "956fd280-4cd3-402b-bdc9-870550b7bcf1",
  "type": "user",
  "uuid": "e64ebb61-e15d-4cbf-a3d2-4ca32fef92de",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Cross-Model Ablation on FOLIO\",\n    \"description\": \"三组条件: (a) Qwen3-32B within-model (MVP baseline), (b) DeepSeek V4 Pro within-model, (c) DeepSeek FOL + Qwen Code cross-model. FOLIO 204 样本。验证分歧信号是否依赖特定模型。\\n\",\n    \"results\": {\n      \"qwen_within_C1\": 0.4216,\n      \"qwen_within_C2\": 0.8721,\n      \"qwen_within_asymmetry_ratio\": \"5.6:1 (FOL:Code)\",\n      \"deepseek_within_C1\": 0.35,\n      \"deepseek_within_C2\": 0.74,\n      \"deepseek_within_C5_committed\": 0.88,\n      \"deepseek_within_asymmetry_ratio\": \"2.5:1 (FOL:Code)\",\n      \"deepseek_within_phi_coefficient\": 0.28,\n      \"cross_model_C1\": 0.48,\n      \"cross_model_C2\": 0.78,\n      \"cross_model_C5_committed\": 0.86,\n      \"cross_model_asymmetry_ratio\": \"3.2:1 (FOL:Code)\",\n      \"cross_model_phi_coefficient\": 0.14,\n      \"C2_drop_deepseek_vs_qwen\": \"-13pp\",\n      \"asymmetry_direction_consistent\": true,\n      \"cross_model_jaccard_failure_overlap\": 0.42\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Model Ablation Results on FOLIO (n=204)\",\n        \"columns\": [\n          \"Condition\",\n          \"C1 (Disagree)\",\n          \"C2 (Diagnostic)\",\n          \"Asymmetry\",\n          \"C5-committed\",\n          \"φ\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-32B (within)\",\n            \"42.2%\",\n            \"87.2%\",\n            \"5.6:1\",\n            \"94.6%\",\n            \"0.189\"\n          ],\n          [\n            \"DeepSeek V4 (within)\",\n            \"35.0%\",\n            \"74.0%\",\n            \"2.5:1\",\n            \"88.0%\",\n            \"0.280\"\n          ],\n          [\n            \"DeepSeek×Qwen (cross)\",\n            \"48.0%\",\n            \"78.0%\",\n            \"3.2:1\",\n            \"86.0%\",\n            \"0.140\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：不对称方向跨模型一致（FOL 始终优于 Code），但比例从 5.6:1 压缩到 2.5:1。 这支持 \\\"representation-level difference\\\" 而非 \\\"model-specific artifact\\\" 的论点，但需要诚实承认 效应大小是 model-dependent 的。Cross-model 条件的 phi=0.14 vs within-model 的 0.189 提供了 correlated failure 降低的证据，但降幅不够支撑 \\\"cross-model 显著优于 within-model\\\" 的 claim。 论文中应报告为：方向一致性作为泛化证据，效应大小变化作为 limitation。\\n\\n\\nDeepSeek V4 Pro 是更强的通用模型，其 FOL 和 Code 生成能力都更均衡，因此： (1) C2 从 87% 降至 74%——更强模型的两条路径各自更准确，分歧样本中\\\"两侧都错\\\"的比例上升（ 从 ~13% 升至 ~26%），拉低诊断率； (2) 不对称性从 5.6:1 压缩到 2.5:1——DeepSeek 的 Code 生成能力相对更强，缩小了 FOL 的优势， 但方向一致（FOL 仍优于 Code），因为 FOL+Z3 的形式验证天然比 Python exec 更可靠； (3) Cross-model 条件 C1 升至 48%——不同模型的 formalization bias 不同，分歧率自然上升； 但 C2 降至 78%——跨模型引入的额外分歧中包含\\\"两个模型各自正确但 formalization 不同\\\"的噪声； (4) phi 系数从 0.189 降至 0.14（cross-model），说明跨模型确实降低了失败相关性， 但降幅不够大，无法彻底消除 correlated failures； (5) Jaccard failure overlap 0.42 说明仍有显著的 specification-level 共享失败模式。 整体：泛化方向一致但效果打折，支撑 \\\"cross-representation signal is model-general\\\" 的弱版本 claim。\\n\"\n  },\n  {\n    \"name\": \"ProofWriter Pilot → LogiQA Fallback\",\n    \"description\": \"ProofWriter 先跑 30 样本 pilot。Pilot 失败（disagree_rate < 10%）后切换 LogiQA。 LogiQA 全量跑 ~200 样本。\\n\",\n    \"results\": {\n      \"proofwriter_pilot_n\": 30,\n      \"proofwriter_pilot_disagree_rate\": 0.067,\n      \"proofwriter_pilot_verdict\": \"FAIL — disagree_rate=6.7% < 10% threshold\",\n      \"proofwriter_pilot_baseline_accuracy\": 0.93,\n      \"logiqa_n\": 200,\n      \"logiqa_C1_disagree_rate\": 0.22,\n      \"logiqa_C2_diagnostic_rate\": 0.72,\n      \"logiqa_C2_bootstrap_CI\": \"[0.63, 0.81]\",\n      \"logiqa_C3_error_types\": 3,\n      \"logiqa_C4_targeted_delta_aggregate\": \"+3.5pp\",\n      \"logiqa_C4_fisher_p\": 0.42,\n      \"logiqa_C5_committed_accuracy\": 0.84,\n      \"logiqa_C5_coverage\": 0.48,\n      \"logiqa_asymmetry_ratio\": \"3.8:1 (FOL:Code)\",\n      \"logiqa_gt_stratified_C4\": {\n        \"correct_answer_A_or_B\": \"+5.2pp\",\n        \"correct_answer_C_or_D\": \"+1.8pp\"\n      },\n      \"logiqa_dominant_error\": \"logic_error 18.5%\",\n      \"logiqa_phi_coefficient\": 0.22\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: ProofWriter Pilot Results (n=30)\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Threshold\",\n          \"Verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Disagree Rate (C1)\",\n            \"6.7%\",\n            \"≥10%\",\n            \"FAIL\"\n          ],\n          [\n            \"Baseline Accuracy\",\n            \"93.3%\",\n            \"—\",\n            \"Too high for meaningful disagreement\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: LogiQA Full Results (n=200)\",\n        \"columns\": [\n          \"Metric\",\n          \"LogiQA\",\n          \"FOLIO (ref)\",\n          \"Delta\"\n        ],\n        \"rows\": [\n          [\n            \"C1 Disagree Rate\",\n            \"22.0%\",\n            \"42.2%\",\n            \"-20.2pp\"\n          ],\n          [\n            \"C2 Diagnostic Rate\",\n            \"72.0%\",\n            \"87.2%\",\n            \"-15.2pp\"\n          ],\n          [\n            \"C5 Committed Acc\",\n            \"84.0%\",\n            \"94.6%\",\n            \"-10.6pp\"\n          ],\n          [\n            \"Asymmetry (FOL:Code)\",\n            \"3.8:1\",\n            \"5.6:1\",\n            \"compressed\"\n          ],\n          [\n            \"C4 Aggregate Delta\",\n            \"+3.5pp\",\n            \"+4.65pp\",\n            \"-1.15pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ProofWriter pilot 失败本身是信息性的——说明 CRD 方法对\\\"已高度形式化\\\"的数据集价值有限， 暗示方法的核心价值在于处理自然语言到形式表示的 translation gap。LogiQA 数据支持泛化但 效应弱化，论文中应讨论\\\"method works best when formalization is the bottleneck, not reasoning\\\"。\\n\\n\\nProofWriter 是合成数据集，前提和规则完全形式化，无自然语言歧义。Qwen3-32B 在这种 结构化输入上 FOL 转换准确率极高（>90%），Code 也因规则简单而表现好，导致分歧率仅 6.7%。 这不是方法失败，而是数据集天花板——当两条路径都很准时，分歧本身就少，诊断价值有限。 切换到 LogiQA 后：(1) C1=22% 低于 FOLIO 的 42% 但满足 ≥15% 阈值——LogiQA 是选择题 （4选1），FOL 和 Code 各自有 ~75% 准确率，分歧空间比 FOLIO 小但够用； (2) C2=72% 低于 FOLIO 的 87%——LogiQA 的错误模式更多是\\\"理解题意错误\\\"而非 \\\"formalization 错误\\\"，前者导致两条路径都错（降低诊断率）； (3) 不对称性 3.8:1 低于 FOLIO 的 5.6:1——LogiQA 的逻辑结构不如 FOLIO 纯粹， FOL 优势缩小；(4) C4 仅 +3.5pp 且不显著——repair 在选择题上增量更弱， 因为错误修复的搜索空间更大（4个选项 vs 3值逻辑）。 整体：提供了第二个基准的泛化证据，但效果明显弱于 FOLIO，符合 median 预期。\\n\"\n  },\n  {\n    \"name\": \"MATH Level 5 Cross-Executable Extension\",\n    \"description\": \"MATH Level 5 ~200 样本，SymPy 符号推理 vs Python 数值验证。 两条路径均可执行，保持 cross-executable-representation 框架一致性。\\n\",\n    \"results\": {\n      \"math_n\": 200,\n      \"math_C1_disagree_rate\": 0.155,\n      \"math_C1_bootstrap_CI\": \"[0.11, 0.21]\",\n      \"math_C2_diagnostic_rate\": 0.65,\n      \"math_C2_bootstrap_CI\": \"[0.53, 0.76]\",\n      \"math_C3_error_types\": 3,\n      \"math_C3_type_distribution\": {\n        \"symbolic_algebra_error\": \"8.5%\",\n        \"numerical_precision_error\": \"4.0%\",\n        \"exec_crash\": \"3.0%\"\n      },\n      \"math_C4_targeted_delta_aggregate\": \"+2.8pp\",\n      \"math_C4_fisher_p\": 0.58,\n      \"math_C5_committed_accuracy\": 0.82,\n      \"math_C5_coverage\": 0.42,\n      \"math_asymmetry_ratio\": \"1.8:1 (SymPy:Python)\",\n      \"math_asymmetry_p_value\": 0.18,\n      \"math_gt_stratified_C4\": {\n        \"algebra\": \"+4.5pp\",\n        \"number_theory\": \"+1.2pp\",\n        \"geometry\": \"-0.8pp\"\n      },\n      \"math_phi_coefficient\": 0.31,\n      \"math_cost_per_sample_tokens\": 2800\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: MATH Level 5 Results (n=200)\",\n        \"columns\": [\n          \"Metric\",\n          \"MATH\",\n          \"FOLIO (ref)\",\n          \"LogiQA (ref)\"\n        ],\n        \"rows\": [\n          [\n            \"C1 Disagree Rate\",\n            \"15.5%\",\n            \"42.2%\",\n            \"22.0%\"\n          ],\n          [\n            \"C2 Diagnostic Rate\",\n            \"65.0%\",\n            \"87.2%\",\n            \"72.0%\"\n          ],\n          [\n            \"Asymmetry Ratio\",\n            \"1.8:1\",\n            \"5.6:1\",\n            \"3.8:1\"\n          ],\n          [\n            \"C4 Aggregate Delta\",\n            \"+2.8pp\",\n            \"+4.65pp\",\n            \"+3.5pp\"\n          ],\n          [\n            \"C5 Committed Acc\",\n            \"82.0%\",\n            \"94.6%\",\n            \"84.0%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: MATH Error Type Distribution\",\n        \"columns\": [\n          \"Error Type\",\n          \"Rate\",\n          \"Description\"\n        ],\n        \"rows\": [\n          [\n            \"symbolic_algebra_error\",\n            \"8.5%\",\n            \"SymPy symbolic manipulation incorrect\"\n          ],\n          [\n            \"numerical_precision_error\",\n            \"4.0%\",\n            \"float rounding / precision mismatch\"\n          ],\n          [\n            \"exec_crash\",\n            \"3.0%\",\n            \"SymPy timeout or unsupported operation\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MATH 结果揭示了方法的 domain boundary：当两种表征都是\\\"计算型\\\"（symbolic vs numerical） 而非\\\"验证型 vs 计算型\\\"（Z3 vs Python）时，不对称性大幅减弱。这本身是 informative finding—— 说明 CRD 的诊断价值依赖于表征间的 verification guarantee gap。 论文应诚实讨论：FOL/Z3 场景是 CRD 的 sweet spot，MATH 场景是 boundary case。\\n\\n\\nMATH Level 5 上的 median 预测基于以下推理： (1) C1=15.5% 远低于 FOLIO 的 42%——MATH 问题有唯一正确数值答案，两条路径 （SymPy 符号 vs Python 数值）对于能解的题往往得到相同答案，分歧主要来自 \\\"一条路径 crash 或超时\\\"和\\\"数值精度差异\\\"而非 formalization 歧义； (2) C2=65% 低于 FOLIO——分歧样本中 SymPy crash（无法处理某些数学结构） 占较大比例，这些 crash 不是\\\"诊断性分歧\\\"而是\\\"能力缺失\\\"，拉低诊断率； (3) 不对称性仅 1.8:1 且 p=0.18 不显著——这是 median 档的关键弱点。 SymPy 和 Python 不像 FOL/Code 那样有本质的验证保证差异（Z3 是定理证明器， Python exec 只是运行代码），因此不对称性大幅压缩； (4) Error taxonomy 需要重新定义（symbolic_algebra_error 替代 logic_error, numerical_precision_error 替代 negation_error），说明 taxonomy 不是 universal 的，需要按 domain 适配——这削弱了 Claim 2 的泛化性； (5) C4 仅 +2.8pp 且按题型分层后只有 algebra 子组有实质增量。 整体：提供了 cross-executable 泛化的证据，但不对称性不显著是必须承认的 limitation。\\n\"\n  },\n  {\n    \"name\": \"Repair Mechanism Improvement\",\n    \"description\": \"多轮 repair（max 3 rounds），加入 error-type-specific 修复策略。 按 GT label 和 error_type 分层报告。\\n\",\n    \"results\": {\n      \"folio_repair_round1_C4\": \"+4.65pp\",\n      \"folio_repair_round2_C4\": \"+6.2pp\",\n      \"folio_repair_round3_C4\": \"+6.8pp\",\n      \"folio_repair_diminishing_returns\": true,\n      \"folio_gt_stratified_round3\": {\n        \"True\": \"-11.5pp\",\n        \"False\": \"+8.2pp\",\n        \"Unknown\": \"+13.0pp\"\n      },\n      \"folio_error_type_stratified_repair\": {\n        \"logic_error_delta\": \"+5.8pp\",\n        \"negation_error_delta\": \"+8.5pp\",\n        \"quantifier_error_delta\": \"+2.0pp\",\n        \"exec_crash_delta\": \"+12.0pp\"\n      },\n      \"folio_repair_round2_fisher_p\": 0.38,\n      \"true_overcorrection_round3_vs_round1\": \"-2.1pp improvement (from -13.6 to -11.5)\",\n      \"true_overcorrection_mechanism\": \"repair prompt 引导模型重新审视 Code 输出，但当 Code 实际正确时反而引入错误\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Multi-Round Repair Results on FOLIO\",\n        \"columns\": [\n          \"Round\",\n          \"C4 Aggregate\",\n          \"GT=True\",\n          \"GT=False\",\n          \"GT=Unknown\"\n        ],\n        \"rows\": [\n          [\n            \"Round 1 (baseline)\",\n            \"+4.65pp\",\n            \"-13.6pp\",\n            \"+6.7pp\",\n            \"+14.7pp\"\n          ],\n          [\n            \"Round 2\",\n            \"+6.2pp\",\n            \"-12.3pp\",\n            \"+7.8pp\",\n            \"+14.2pp\"\n          ],\n          [\n            \"Round 3\",\n            \"+6.8pp\",\n            \"-11.5pp\",\n            \"+8.2pp\",\n            \"+13.0pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Error-Type-Specific Repair (Round 3)\",\n        \"columns\": [\n          \"Error Type\",\n          \"n\",\n          \"Delta\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"logic_error\",\n            \"52\",\n            \"+5.8pp\",\n            \"0.31\"\n          ],\n          [\n            \"negation_error\",\n            \"22\",\n            \"+8.5pp\",\n            \"0.24\"\n          ],\n          [\n            \"quantifier_error\",\n            \"4\",\n            \"+2.0pp\",\n            \"1.00\"\n          ],\n          [\n            \"exec_crash\",\n            \"11\",\n            \"+12.0pp\",\n            \"0.18\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"多轮 repair 的增量从 Round 1→2 的 +1.55pp 缩小到 Round 2→3 的 +0.6pp， 明确的 diminishing returns。GT=True overcorrection 仍是 -11.5pp，说明这是 方法的结构性限制而非实现问题。论文中应以 Round 1 为主结果，Round 2-3 作为补充， 并明确讨论\\\"多轮 repair 对 overcorrection 的改善有限\\\"。\\n\\n\\n多轮 repair 的 diminishing returns 符合预期——第一轮已修复最容易的错误（exec_crash 和 明确的 negation_error），后续轮次面对的是更难的 logic_error，修复成功率低。 GT=Unknown 子组从 +14.7pp 略降至 +13.0pp——第一轮已捕获大部分 Code overclaiming， 多轮反而引入少量 over-repair。GT=True 子组从 -13.6pp 改善到 -11.5pp——多轮 repair 的\\\"确认机制\\\"（如果 repair 后两侧仍不一致则保留原答案）挽回了少量 overcorrection， 但根本机制（repair prompt 误导模型改正确答案）未被消除。 Error-type-specific 策略中，exec_crash 的 +12pp 最高因为修复最明确（重新生成不 crash 的代码）， quantifier_error 最低因为量词错误本身诊断不准确。 整体：repair 有边际改善但 GT=True overcorrection 是结构性问题，多轮无法根治。\\n\"\n  },\n  {\n    \"name\": \"Unknown Sample Deep Analysis + Correlated Failure\",\n    \"description\": \"纯分析：Code overclaiming 机制、phi 系数按 GT 分层、 false agreement rate、specification-level vs formalization-specific 错误分类。\\n\",\n    \"results\": {\n      \"code_overclaiming_rate_unknown\": 0.72,\n      \"code_overclaiming_mechanism\": \"Code 路径倾向输出 True/False 而非 Unknown，将不确定性错误地转化为确定性判断\",\n      \"code_unknown_prediction_rate\": 0.08,\n      \"fol_unknown_prediction_rate\": 0.41,\n      \"phi_by_gt\": {\n        \"True\": 0.12,\n        \"False\": 0.18,\n        \"Unknown\": 0.31\n      },\n      \"false_agreement_rate_overall\": 0.122,\n      \"false_agreement_by_gt\": {\n        \"True\": 0.056,\n        \"False\": 0.089,\n        \"Unknown\": 0.261\n      },\n      \"specification_level_errors\": \"25/204 (12.3%)\",\n      \"formalization_specific_errors\": \"75/204 (36.8%)\",\n      \"specification_level_repair_delta\": \"+1.2pp\",\n      \"formalization_specific_repair_delta\": \"+7.8pp\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Code Overclaiming Analysis (GT=Unknown, n=69)\",\n        \"columns\": [\n          \"Code Output\",\n          \"Count\",\n          \"Rate\"\n        ],\n        \"rows\": [\n          [\n            \"True (overclaim)\",\n            \"28\",\n            \"40.6%\"\n          ],\n          [\n            \"False (overclaim)\",\n            \"22\",\n            \"31.9%\"\n          ],\n          [\n            \"Unknown (correct)\",\n            \"14\",\n            \"20.3%\"\n          ],\n          [\n            \"Crash\",\n            \"5\",\n            \"7.2%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Failure Correlation by GT Label\",\n        \"columns\": [\n          \"GT Label\",\n          \"φ coefficient\",\n          \"False Agreement Rate\",\n          \"Repair Delta\"\n        ],\n        \"rows\": [\n          [\n            \"True\",\n            \"0.12\",\n            \"5.6%\",\n            \"-13.6pp\"\n          ],\n          [\n            \"False\",\n            \"0.18\",\n            \"8.9%\",\n            \"+6.7pp\"\n          ],\n          [\n            \"Unknown\",\n            \"0.31\",\n            \"26.1%\",\n            \"+14.7pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心洞察：GT=Unknown 的 paradox——最高的 false agreement rate (26.1%) 但也最高的 repair delta (+14.7pp)。解释：当分歧被检测到时（72% 的 Unknown 样本），分歧信号 非常有信息量（Code overclaiming），使 repair 能利用 FOL 的 Unknown 判断纠正 Code。 但 26.1% 的 false agreement 是诊断的硬天花板——这些样本\\\"看起来一致但实际都错\\\"。 Specification-level vs formalization-specific 分类为 repair boundary 提供了 机制解释，应作为论文的 key insight 报告。\\n\\n\\n(1) Code overclaiming: Python 代码执行是确定性的——要么返回 True/False，要么 crash。 没有原生的\\\"Unknown\\\"输出机制。即使 prompt 要求输出 Unknown，Code 路径仍在 72% 的 GT=Unknown 样本上给出 True 或 False，而 FOL/Z3 因为有 \\\"satisfiable but not valid\\\" 的天然表达能力，41% 的时候正确输出 Unknown。这解释了为什么 GT=Unknown 子组的 诊断价值最高——Code 的 overclaiming 制造了可检测的分歧； (2) phi 系数按 GT 分层：Unknown 最高 (0.31) 说明在 Unknown 样本上 FOL 和 Code 的失败更相关——两者都因 specification ambiguity 而困难，但失败模式不同（FOL 返回 Unknown，Code 猜错方向），所以分歧反而更有诊断价值； (3) False agreement rate 在 Unknown 上最高 (26.1%)——两条路径可能碰巧同时猜对 或同时猜错同一个方向，这是诊断的天花板； (4) Specification-level errors (12.3%) 是\\\"题目本身有歧义导致两条路径都合理地 得到不同答案\\\"，repair 对此几乎无效 (+1.2pp)；formalization-specific errors (36.8%) 是单侧 formalization 错误，repair 有效 (+7.8pp)。\\n\"\n  },\n  {\n    \"name\": \"Selection vs Repair Ablation\",\n    \"description\": \"检测分歧+定位错误侧后，对比：(a) 直接选正确侧答案 (selection), (b) 诊断引导修复 (repair), (c) oracle 上界。按 error_type 分层。\\n\",\n    \"results\": {\n      \"folio_selection_accuracy\": 0.828,\n      \"folio_repair_accuracy\": 0.838,\n      \"folio_oracle_accuracy\": 0.878,\n      \"folio_blind_baseline\": 0.814,\n      \"folio_selection_vs_repair_delta\": \"-1.0pp\",\n      \"folio_selection_vs_blind_delta\": \"+5.4pp\",\n      \"folio_repair_vs_blind_delta\": \"+4.65pp\",\n      \"folio_by_error_type\": {\n        \"logic_error\": {\n          \"selection\": 0.83,\n          \"repair\": 0.85,\n          \"delta\": \"-2pp\"\n        },\n        \"negation_error\": {\n          \"selection\": 0.86,\n          \"repair\": 0.82,\n          \"delta\": \"+4pp\"\n        },\n        \"exec_crash\": {\n          \"selection\": 0.91,\n          \"repair\": 0.91,\n          \"delta\": \"0pp\"\n        }\n      },\n      \"folio_by_gt\": {\n        \"True\": {\n          \"selection\": 0.792,\n          \"repair\": 0.764,\n          \"note\": \"selection avoids overcorrection\"\n        },\n        \"False\": {\n          \"selection\": 0.81,\n          \"repair\": 0.825\n        },\n        \"Unknown\": {\n          \"selection\": 0.812,\n          \"repair\": 0.855\n        }\n      },\n      \"folio_selection_vs_repair_mcnemar_p\": 0.72\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Selection vs Repair on FOLIO\",\n        \"columns\": [\n          \"Method\",\n          \"Accuracy\",\n          \"Extra LLM Calls\",\n          \"vs Blind Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Blind baseline\",\n            \"81.4%\",\n            \"0\",\n            \"—\"\n          ],\n          [\n            \"Selection (ours)\",\n            \"82.8%\",\n            \"0\",\n            \"+1.4pp\"\n          ],\n          [\n            \"Repair (ours)\",\n            \"83.8%\",\n            \"~2/sample\",\n            \"+2.4pp\"\n          ],\n          [\n            \"Oracle\",\n            \"87.8%\",\n            \"—\",\n            \"+6.4pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Selection vs Repair by GT Label\",\n        \"columns\": [\n          \"GT Label\",\n          \"Selection\",\n          \"Repair\",\n          \"Δ (Sel-Rep)\"\n        ],\n        \"rows\": [\n          [\n            \"True\",\n            \"79.2%\",\n            \"76.4%\",\n            \"+2.8pp\"\n          ],\n          [\n            \"False\",\n            \"81.0%\",\n            \"82.5%\",\n            \"-1.5pp\"\n          ],\n          [\n            \"Unknown\",\n            \"81.2%\",\n            \"85.5%\",\n            \"-4.3pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Selection 几乎匹配 repair 且成本更低（0 extra calls vs ~2 calls/sample）， McNemar p=0.72 远不显著。论文主结果应是 \\\"diagnosis → selection\\\" 路径， repair 作为 \\\"additional exploration showing GT-label-dependent effects\\\"。 关键论证：CRD 的价值在于诊断信息本身（error type, error side），下游应用 （selection or repair）是次要的，且 selection 已足够捕获大部分增量。\\n\\n\\nSelection 和 repair 的差距 <3pp（实际 ~1pp）且统计不显著，符合 median 预期。机制： (1) Selection 在 GT=True 上优于 repair——当 localization 正确识别 Code 为错误侧时， 直接选 FOL 答案即可，repair 反而可能引入 overcorrection； (2) Repair 在 GT=Unknown 上优于 selection——因为 Unknown 样本的正确答案可能 不在任一侧现有输出中（FOL 可能输出 Unknown 但推理路径有瑕疵），repair 能生成 更好的答案； (3) exec_crash 上两者相同——crash 修复等价于重新生成，与 selection 效果相近； (4) 整体差距不显著意味着 repair 的额外 LLM 调用（~2 calls/sample）没有带来 足够的增量价值，支持将 repair 降格为 secondary analysis。 Selection 的优势在于简单、cheap（0 额外 LLM calls），且避免了 overcorrection。 这是论文 reframing 的关键证据：\\\"diagnosis enables selection\\\" 而非 \\\"diagnosis enables repair\\\"。\\n\"\n  },\n  {\n    \"name\": \"Error Taxonomy Ablation\",\n    \"description\": \"Taxonomy-guided repair（按错误类型分派策略）vs fixed repair（统一重生成）。\\n\",\n    \"results\": {\n      \"folio_taxonomy_guided_accuracy\": 0.845,\n      \"folio_fixed_strategy_accuracy\": 0.838,\n      \"folio_taxonomy_delta\": \"+0.7pp\",\n      \"folio_taxonomy_mcnemar_p\": 0.68,\n      \"by_error_type\": {\n        \"logic_error\": {\n          \"taxonomy_guided\": 0.87,\n          \"fixed\": 0.85,\n          \"delta\": \"+2pp\"\n        },\n        \"negation_error\": {\n          \"taxonomy_guided\": 0.86,\n          \"fixed\": 0.82,\n          \"delta\": \"+4pp\"\n        },\n        \"exec_crash\": {\n          \"taxonomy_guided\": 0.91,\n          \"fixed\": 0.91,\n          \"delta\": \"0pp\"\n        },\n        \"quantifier_error\": {\n          \"taxonomy_guided\": 0.75,\n          \"fixed\": 0.75,\n          \"delta\": \"0pp\"\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Taxonomy-Guided vs Fixed Repair\",\n        \"columns\": [\n          \"Error Type\",\n          \"n\",\n          \"Taxonomy-Guided\",\n          \"Fixed\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"logic_error\",\n            \"52\",\n            \"87%\",\n            \"85%\",\n            \"+2pp\"\n          ],\n          [\n            \"negation_error\",\n            \"22\",\n            \"86%\",\n            \"82%\",\n            \"+4pp\"\n          ],\n          [\n            \"exec_crash\",\n            \"11\",\n            \"91%\",\n            \"91%\",\n            \"0pp\"\n          ],\n          [\n            \"quantifier_error\",\n            \"4\",\n            \"75%\",\n            \"75%\",\n            \"0pp\"\n          ],\n          [\n            \"Overall\",\n            \"89\",\n            \"84.5%\",\n            \"83.8%\",\n            \"+0.7pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Taxonomy 的规定性价值不成立（+0.7pp, p=0.68），但描述性价值（理解错误分布 和模式）仍是 Claim 2 的有效支撑。论文中将此结果诚实报告为\\\"taxonomy aids understanding but does not significantly improve repair when used prescriptively\\\"， 反而强化了\\\"analysis over method\\\"的 framing。\\n\\n\\nTaxonomy-guided repair 的增量仅 +0.7pp 且不显著。原因： (1) 最大类别 logic_error（52 样本）的修复策略差异很小——无论是\\\"请修正逻辑错误\\\" 还是\\\"请重新生成\\\"，LLM 的修复行为高度相似，因为 repair prompt 本身已包含 分歧信息，模型自行判断修复方向； (2) negation_error 上有 +4pp 差异——特定的\\\"检查否定词\\\"提示确实帮助模型 注意到遗漏的 negation，但样本量太小（22）无法达到显著； (3) exec_crash 和 quantifier_error 上无差异——crash 修复不需要类型信息 （重新生成即可），quantifier_error 太少无统计力； (4) 这个结果说明 taxonomy 的价值主要在于分析和理解（Claim 2）， 而非在于指导修复策略（Claim 3），支持论文的 reframing。\\n\"\n  },\n  {\n    \"name\": \"Statistical Significance Comprehensive Testing\",\n    \"description\": \"对所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + Fisher exact / McNemar test。\\n\",\n    \"results\": {\n      \"folio_bootstrap\": {\n        \"C1\": {\n          \"point\": 0.422,\n          \"CI\": \"[0.353, 0.490]\",\n          \"significant_vs_0\": true\n        },\n        \"C2\": {\n          \"point\": 0.872,\n          \"CI\": \"[0.813, 0.947]\",\n          \"significant_vs_50pct\": true\n        },\n        \"C4\": {\n          \"point\": \"+4.65pp\",\n          \"CI\": \"[-8.8, +18.1]\",\n          \"significant\": false,\n          \"fisher_p\": 0.626\n        },\n        \"C5_committed\": {\n          \"point\": 0.946,\n          \"CI\": \"[0.861, 1.000]\",\n          \"significant_vs_50pct\": true\n        }\n      },\n      \"logiqa_bootstrap\": {\n        \"C1\": {\n          \"point\": 0.22,\n          \"CI\": \"[0.165, 0.280]\",\n          \"significant_vs_0\": true\n        },\n        \"C2\": {\n          \"point\": 0.72,\n          \"CI\": \"[0.630, 0.810]\",\n          \"significant_vs_50pct\": true\n        },\n        \"C4\": {\n          \"point\": \"+3.5pp\",\n          \"CI\": \"[-6.2, +13.2]\",\n          \"significant\": false,\n          \"fisher_p\": 0.42\n        },\n        \"C5_committed\": {\n          \"point\": 0.84,\n          \"CI\": \"[0.720, 0.940]\",\n          \"significant_vs_50pct\": true\n        }\n      },\n      \"math_bootstrap\": {\n        \"C1\": {\n          \"point\": 0.155,\n          \"CI\": \"[0.110, 0.210]\",\n          \"significant_vs_0\": true\n        },\n        \"C2\": {\n          \"point\": 0.65,\n          \"CI\": \"[0.530, 0.760]\",\n          \"significant_vs_50pct\": true\n        },\n        \"C4\": {\n          \"point\": \"+2.8pp\",\n          \"CI\": \"[-7.5, +13.1]\",\n          \"significant\": false,\n          \"fisher_p\": 0.58\n        },\n        \"C5_committed\": {\n          \"point\": 0.82,\n          \"CI\": \"[0.680, 0.940]\",\n          \"significant_vs_50pct\": true\n        }\n      },\n      \"bonferroni_correction\": {\n        \"n_tests\": 12,\n        \"C4_any_significant_after_correction\": false,\n        \"C1_C2_C5_all_significant_after_correction\": true\n      },\n      \"cross_benchmark_summary\": \"C1, C2, C5 在所有三个 benchmark 上均统计显著（Bonferroni 校正后 p < 0.004）。 C4 在所有三个 benchmark 上均不显著（最小 p = 0.42），且 bootstrap CI 均包含零。\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Statistical Significance Summary (All Benchmarks)\",\n        \"columns\": [\n          \"Metric\",\n          \"FOLIO\",\n          \"LogiQA\",\n          \"MATH\",\n          \"All Sig?\"\n        ],\n        \"rows\": [\n          [\n            \"C1 (vs 0%)\",\n            \"✓ p<0.001\",\n            \"✓ p<0.001\",\n            \"✓ p<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"C2 (vs 50%)\",\n            \"✓ p<0.001\",\n            \"✓ p=0.002\",\n            \"✓ p=0.018\",\n            \"Yes\"\n          ],\n          [\n            \"C4 (Fisher)\",\n            \"✗ p=0.626\",\n            \"✗ p=0.42\",\n            \"✗ p=0.58\",\n            \"No\"\n          ],\n          [\n            \"C5 (vs 50%)\",\n            \"✓ p<0.001\",\n            \"✓ p=0.003\",\n            \"✓ p=0.008\",\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"统计结果清晰地支持 median framing：诊断指标 (C1/C2/C5) 稳健显著， 修复指标 (C4) 一致不显著。这不是弱点而是 feature——论文的主贡献在于诊断 而非修复，统计证据恰好支持这个 reframing。Forest plot 展示 C4 的三个 CI 均跨零但方向一致（正），可讨论为 \\\"consistent positive trend, insufficient power\\\"。\\n\\n\\nC1（分歧存在性）和 C2（诊断精度 >50%）的显著性是预期中的——即使在最小的 MATH 数据上，31 个分歧样本中 65% 是诊断性的，与 50% 随机基准有 >15pp 差距， bootstrap 10000 次几乎不会包含 50%。C5-committed 在小样本上 CI 很宽 （MATH: [0.68, 0.94]），但 point estimate 远超 50% 仍显著。 C4 的统计不显著在三个 benchmark 上一致——这不是样本量问题而是效应量问题： aggregate repair delta 确实很小（2.8-4.65pp），在 n=200 的 paired sample 上 需要 >8pp delta 才能达到 Fisher p < 0.05。这强化了\\\"repair 不是主贡献\\\"的 framing。 Bonferroni 校正（12 tests）不影响 C1/C2/C5 但确认 C4 在任何校正下都不显著。\\n\"\n  },\n  {\n    \"name\": \"Self-Consistency Baseline Comparison\",\n    \"description\": \"在 FOLIO + LogiQA + MATH 上对比: (a) k=5 FOL-only majority vote, (b) k=5 Code-only majority vote, (c) Single-pass CRD (1 FOL + 1 Code)。\\n\",\n    \"results\": {\n      \"folio\": {\n        \"sc5_fol_detection_precision\": 0.85,\n        \"sc5_fol_detection_recall\": 0.68,\n        \"sc5_code_detection_precision\": 0.79,\n        \"sc5_code_detection_recall\": 0.72,\n        \"crd_detection_precision\": 0.872,\n        \"crd_detection_recall\": 0.44,\n        \"crd_vs_sc5fol_precision_delta\": \"+2.2pp\",\n        \"crd_vs_sc5fol_recall_delta\": \"-24pp\",\n        \"crd_provides_error_type\": true,\n        \"crd_provides_error_side\": true,\n        \"sc5_provides_error_type\": false,\n        \"sc5_provides_error_side\": false,\n        \"crd_cost_tokens\": 3200,\n        \"sc5_fol_cost_tokens\": 8500,\n        \"sc5_code_cost_tokens\": 7200,\n        \"crd_vs_sc5_cost_ratio\": 0.4\n      },\n      \"logiqa\": {\n        \"sc5_fol_detection_precision\": 0.76,\n        \"sc5_code_detection_precision\": 0.71,\n        \"crd_detection_precision\": 0.72,\n        \"crd_vs_sc5fol_precision_delta\": \"-4pp\",\n        \"crd_vs_sc5_cost_ratio\": 0.38\n      },\n      \"math\": {\n        \"sc5_sympy_detection_precision\": 0.7,\n        \"sc5_python_detection_precision\": 0.74,\n        \"crd_detection_precision\": 0.65,\n        \"crd_vs_sc5python_precision_delta\": \"-9pp\",\n        \"crd_vs_sc5_cost_ratio\": 0.35\n      },\n      \"cross_benchmark_summary\": {\n        \"precision_delta_range\": \"[-9pp, +2.2pp]\",\n        \"cost_ratio_range\": \"[0.35, 0.40]\",\n        \"crd_unique_advantage\": \"error type classification + error side localization + paradigm asymmetry characterization\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: CRD vs Self-Consistency (k=5) Comparison\",\n        \"columns\": [\n          \"Benchmark\",\n          \"SC5-Best Precision\",\n          \"CRD Precision\",\n          \"Δ\",\n          \"CRD Cost Ratio\",\n          \"CRD Extra Info\"\n        ],\n        \"rows\": [\n          [\n            \"FOLIO\",\n            \"85.0%\",\n            \"87.2%\",\n            \"+2.2pp\",\n            \"0.40×\",\n            \"error type + side + asymmetry\"\n          ],\n          [\n            \"LogiQA\",\n            \"76.0%\",\n            \"72.0%\",\n            \"-4.0pp\",\n            \"0.38×\",\n            \"error type + side + asymmetry\"\n          ],\n          [\n            \"MATH\",\n            \"74.0%\",\n            \"65.0%\",\n            \"-9.0pp\",\n            \"0.35×\",\n            \"error type + side\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Diagnostic Information Comparison\",\n        \"columns\": [\n          \"Capability\",\n          \"SC5\",\n          \"CRD\"\n        ],\n        \"rows\": [\n          [\n            \"Error detection\",\n            \"✓\",\n            \"✓\"\n          ],\n          [\n            \"Error type classification\",\n            \"✗\",\n            \"✓ (3-4 types)\"\n          ],\n          [\n            \"Error side localization\",\n            \"✗\",\n            \"✓ (C5=82-95%)\"\n          ],\n          [\n            \"Paradigm asymmetry\",\n            \"✗\",\n            \"✓ (representation dominance)\"\n          ],\n          [\n            \"Cost (LLM calls)\",\n            \"5\",\n            \"2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 median 档最关键的实验。结果迫使 Claim 1 reframe：CRD 的价值不在于 \\\"precision 优于 SC5\\\"（FOLIO 上微幅领先不足以泛化），而在于 \\\"comparable precision at 2.5x lower cost, plus qualitative diagnostic advantages (error type, error side, paradigm asymmetry) that SC5 fundamentally cannot provide\\\"。 SC5 只告诉你 THAT something might be wrong（多次采样不一致）， CRD 告诉你 WHY it's wrong（which representation, what type of error, which paradigm is more reliable for this problem type）。 这是论文 contribution statement 的核心区分，也是 \\\"diagnosis and characterization\\\" 标题的依据。\\n\\n\\nMedian 核心假设：CRD 精度 ≈ SC5（±3pp on FOLIO, wider gap on MATH）。推理： (1) FOLIO 上 CRD precision 87.2% vs SC5-FOL 85%——CRD 微幅领先 2.2pp， 因为 cross-representation 分歧捕获的是 paradigm-level 差异（FOL 的形式验证 vs Code 的执行验证），比同表征的 sampling variance 更信息丰富。但差距很小因为 k=5 majority vote 已经是很强的 baseline——5 次 FOL 采样的多数不一致时， 确实高概率指示错误； (2) CRD recall 远低于 SC5（44% vs 68%）——CRD 只检测\\\"两条路径不一致\\\"的样本， 而 SC5 检测\\\"5 次采样中有分歧\\\"的样本，后者覆盖面更广； (3) LogiQA 上 CRD 略低于 SC5（-4pp）——LogiQA 的错误更多是理解性的而非 formalization-specific，cross-representation 信号对理解性错误的检测优势消失； (4) MATH 上 CRD 明显低于 SC5（-9pp）——SymPy/Python 的差异更多是\\\"能力差异\\\" 而非\\\"paradigm 差异\\\"，SC5 在单一 Python 上的 sampling diversity 反而更有效； (5) 成本比 0.35-0.40——CRD 只需 2 calls，SC5 需要 5 calls，成本优势 2.5x。 核心论证转向：\\\"comparable precision at 40% cost, plus structured diagnostic information (error type, error side, asymmetry) that SC5 cannot provide\\\"。\\n\"\n  },\n  {\n    \"name\": \"Error Taxonomy Cross-Model Validation\",\n    \"description\": \"用 DeepSeek V4 Pro 对 FOLIO 分歧样本做错误分类，与 Qwen3-32B 分类对比。 计算 Cohen's κ。可选 50 样本 LLM-as-human-proxy 标注。\\n\",\n    \"results\": {\n      \"n_disagreement_samples\": 86,\n      \"cohens_kappa_4types\": 0.43,\n      \"cohens_kappa_3types_merged\": 0.54,\n      \"category_level_agreement\": {\n        \"logic_error\": {\n          \"kappa\": 0.58,\n          \"agreement_rate\": 0.78\n        },\n        \"negation_error\": {\n          \"kappa\": 0.51,\n          \"agreement_rate\": 0.73\n        },\n        \"quantifier_error\": {\n          \"kappa\": 0.22,\n          \"agreement_rate\": 0.65\n        },\n        \"exec_crash\": {\n          \"kappa\": 0.82,\n          \"agreement_rate\": 0.95\n        }\n      },\n      \"merged_taxonomy\": {\n        \"logic_error\": \"25.5% → stable across models\",\n        \"negation_error\": \"10.8% → stable across models\",\n        \"formalization_other\": \"7.4% (merged quantifier_error + exec_crash)\"\n      },\n      \"llm_proxy_n\": 50,\n      \"llm_proxy_kappa_vs_qwen\": 0.61,\n      \"llm_proxy_kappa_vs_deepseek\": 0.57,\n      \"cross_model_error_distribution_chi2_p\": 0.12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Model Taxonomy Agreement (FOLIO, n=86)\",\n        \"columns\": [\n          \"Error Type\",\n          \"Qwen3-32B Rate\",\n          \"DeepSeek V4 Rate\",\n          \"κ\",\n          \"Agreement\"\n        ],\n        \"rows\": [\n          [\n            \"logic_error\",\n            \"25.5%\",\n            \"27.1%\",\n            \"0.58\",\n            \"78%\"\n          ],\n          [\n            \"negation_error\",\n            \"10.8%\",\n            \"9.3%\",\n            \"0.51\",\n            \"73%\"\n          ],\n          [\n            \"quantifier_error\",\n            \"2.0%\",\n            \"4.7%\",\n            \"0.22\",\n            \"65%\"\n          ],\n          [\n            \"exec_crash\",\n            \"5.4%\",\n            \"4.7%\",\n            \"0.82\",\n            \"95%\"\n          ],\n          [\n            \"Overall (4 types)\",\n            \"—\",\n            \"—\",\n            \"0.43\",\n            \"—\"\n          ],\n          [\n            \"Overall (3 types, merged)\",\n            \"—\",\n            \"—\",\n            \"0.54\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"κ=0.54（3-type merged）是 \\\"moderate agreement\\\"——不够强到声称 taxonomy 是 robust 的， 但足以作为 exploratory taxonomy 发表。论文应：(1) 报告 4-type 和 3-type 两个 κ 值； (2) 解释 quantifier_error 合并的理由（低频 + 定义模糊 + 跨模型不稳定）； (3) 将 taxonomy 定位为 \\\"empirically motivated categorization\\\" 而非 \\\"definitive taxonomy\\\"； (4) 在 limitations 中讨论 taxonomy 验证不足。exec_crash 的高一致性和 logic_error 的 moderate 一致性足以支撑 Claim 2 的弱版本。\\n\\n\\n(1) 4-type κ=0.43（\\\"moderate agreement\\\"）——低于理想但在 median 预期内。 主要分歧来源是 quantifier_error（κ=0.22）：这个类别本身定义模糊（量词范围错误 vs 逻辑错误常有重叠），且样本量极少（4 个），两个模型的分类策略分歧大； (2) 合并 quantifier_error 和 exec_crash 为 \\\"formalization_other\\\" 后， 3-type κ 升至 0.54（\\\"moderate-to-fair agreement\\\"），达到可发表水平； (3) logic_error 和 negation_error 跨模型一致性较好（κ=0.58, 0.51）， 因为这两类的语义定义更清晰：logic_error = 逻辑运算符错误， negation_error = 否定处理遗漏，模型间判断标准接近； (4) exec_crash 的 κ=0.82 极高——crash 是客观可验证的事实，不依赖模型判断； (5) LLM-as-human-proxy 的 κ=0.61 高于 cross-model 的 0.54—— GPT-4o 作为 proxy 标注者更倾向于与两个模型的\\\"平均判断\\\"一致； (6) 错误类型分布的 χ² 检验 p=0.12——两个模型的分布差异不显著， 但也不够显著地相似（需要 equivalence test）。 整体：taxonomy 需要合并到 3 类才稳定，这是论文可接受的妥协。\\n\"\n  },\n  {\n    \"name\": \"Qwen3-8B Scale Ablation\",\n    \"description\": \"低能力模型 Qwen3-8B 上的 FOLIO 诊断率和分歧率变化。\\n\",\n    \"results\": {\n      \"qwen8b_n\": 204,\n      \"qwen8b_C1_disagree_rate\": 0.55,\n      \"qwen8b_C2_diagnostic_rate\": 0.68,\n      \"qwen8b_C5_committed_accuracy\": 0.78,\n      \"qwen8b_asymmetry_ratio\": \"2.8:1 (FOL:Code)\",\n      \"qwen8b_baseline_fol_accuracy\": 0.62,\n      \"qwen8b_baseline_code_accuracy\": 0.48,\n      \"qwen8b_phi_coefficient\": 0.15,\n      \"qwen8b_C4_delta\": \"+2.1pp\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Model Scale Ablation (FOLIO)\",\n        \"columns\": [\n          \"Metric\",\n          \"Qwen3-32B\",\n          \"Qwen3-8B\",\n          \"Delta\"\n        ],\n        \"rows\": [\n          [\n            \"C1 Disagree Rate\",\n            \"42.2%\",\n            \"55.0%\",\n            \"+12.8pp\"\n          ],\n          [\n            \"C2 Diagnostic Rate\",\n            \"87.2%\",\n            \"68.0%\",\n            \"-19.2pp\"\n          ],\n          [\n            \"Asymmetry\",\n            \"5.6:1\",\n            \"2.8:1\",\n            \"compressed\"\n          ],\n          [\n            \"C4 Delta\",\n            \"+4.65pp\",\n            \"+2.1pp\",\n            \"-2.55pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2 实验——如果时间不够可作为 appendix 或 AAAI 扩展版内容。 核心 takeaway 是 \\\"more disagreement ≠ better diagnosis\\\"——8B 的 C1 更高但 C2 更低。\\n\\n\\n8B 模型能力下降导致：(1) C1 升至 55%——两条路径各自准确率更低（FOL 62%, Code 48%）， 分歧更频繁，但更多分歧来自\\\"两侧都错但答案不同\\\"而非\\\"单侧 formalization 错误\\\"； (2) C2 降至 68%——分歧样本中 \\\"both wrong\\\" 比例上升（~32%），诊断精度下降； (3) 不对称性从 5.6:1 压缩到 2.8:1——8B 模型的 FOL 生成能力退化更快（FOL 需要 更精确的形式化能力），Code 生成相对简单（Python 语法更宽容），差距缩小； (4) C4 仅 +2.1pp——repair 能力也随模型能力下降。 数据点虽然数值更弱，但趋势一致，支撑 \\\"CRD works across scales but effectiveness scales with model capability\\\" 的 finding。\\n\"\n  },\n  {\n    \"name\": \"GPQA Diamond Extension\",\n    \"description\": \"科学知识推理，SymPy/Python 双可执行表征。\\n\",\n    \"results\": {\n      \"gpqa_n\": 198,\n      \"gpqa_C1_disagree_rate\": 0.12,\n      \"gpqa_C2_diagnostic_rate\": 0.58,\n      \"gpqa_C5_committed_accuracy\": 0.75,\n      \"gpqa_asymmetry_ratio\": \"1.4:1 (SymPy:Python)\",\n      \"gpqa_C4_delta\": \"+1.0pp\",\n      \"gpqa_verdict\": \"method at domain boundary — limited value for knowledge-intensive science reasoning\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: GPQA Diamond Results\",\n        \"columns\": [\n          \"Metric\",\n          \"GPQA\",\n          \"MATH (ref)\",\n          \"FOLIO (ref)\"\n        ],\n        \"rows\": [\n          [\n            \"C1\",\n            \"12.0%\",\n            \"15.5%\",\n            \"42.2%\"\n          ],\n          [\n            \"C2\",\n            \"58.0%\",\n            \"65.0%\",\n            \"87.2%\"\n          ],\n          [\n            \"Asymmetry\",\n            \"1.4:1\",\n            \"1.8:1\",\n            \"5.6:1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2 实验——用于 AAAI 扩展版或论文 Discussion 中的 \\\"domain boundary\\\" 讨论。 核心 finding：CRD 的有效性与 \\\"formalization being the bottleneck\\\" 正相关。 当错误源从 formalization 转移到 knowledge/reasoning，method 价值递减。\\n\\nGPQA Diamond 是知识密集型科学推理，错误瓶颈在于 domain knowledge 而非 formalization。 (1) C1 仅 12%——两条路径在知识正确时通常得到相同答案，分歧主要来自 SymPy 的 科学公式表达局限性（无法处理量子力学符号等）； (2) C2=58%——分歧样本中约一半是\\\"SymPy 无法表达该问题\\\"而非\\\"formalization 错误\\\"， 这些 crash 不是诊断性的； (3) 不对称性几乎消失（1.4:1）——SymPy 和 Python 在科学领域没有本质的验证保证差异。 GPQA 标记了方法的 domain boundary，适合作为 Discussion 中的 negative finding。\\n\"\n  }\n]",
      "numLines": 1078,
      "startLine": 1,
      "totalLines": 1078
    }
  },
  "sourceToolAssistantUUID": "5e82277a-fe2d-4657-8f1b-52802219d87d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T07:39:30.658Z_

<details><summary>↩ Tool result · `toolu_015JwX7ddaqCyciRYNEVGwak`</summary>

```text
1	# Paper Framing — cross_representation_disagreement_diagno
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026 (10 days)
7	- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage
8	
9	## Core Insight
10	When the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This "disagreement as diagnostic" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.
11	
12	## Core Claims (3 条)
13	
14	### Claim 1: Disagreement as High-Precision Diagnostic Signal
15	When the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.
16	
17	**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).
18	
19	### Claim 2: Error Classification and Conditional Localization
20	Disagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is high (85.4%). The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.
21	
22	**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return "ambiguous" (especially Unknown: 61%). C3=4 error types.
23	
24	**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.
25	
26	**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled "the error."
27	
28	### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral
29	Diagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:
30	
31	| GT Label | n | Targeted | Blind | Delta | Interpretation |
32	|----------|---|----------|-------|-------|----------------|
33	| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |
34	| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |
35	| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |
36	
37	This is NOT simply "conditional advantage" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal ("Code disagrees with FOL") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.
38	
39	**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.
40	
41	**Presentation strategy**: 
42	1. Report C4 stratified by GT label as the PRIMARY result (table above)
43	2. Aggregate C4 only as context, with explicit caveat about non-significance
44	3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness
45	4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)
46	
47	## Story Spine
48	
49	- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.
50	
51	- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.
52	
53	- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).
54	
55	- **Headline result template**: "On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation."
56	
57	## Venue Fit
58	
59	- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.
60	- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.
61	- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.
62	
63	## Anticipated Reviewer Concerns & Responses
64	
65	| # | Concern | Response Strategy | Required Experiment |
66	|---|---------|-------------------|---------------------|
67	| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |
68	| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |
69	| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |
70	| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |
71	| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |
72	| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |
73	| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |
74	| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |
75	| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |
76	| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as "cross-representation" is imprecise | Frame MATH domain as "cross-executable-paradigm" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |
77	| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f972ab1f-a457-48dd-8ce0-a9f79742d51d",
  "isSidechain": false,
  "promptId": "956fd280-4cd3-402b-bdc9-870550b7bcf1",
  "type": "user",
  "uuid": "976d347b-c3e0-4da8-a287-491e814c36ca",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper_framing.md",
      "content": "# Paper Framing — cross_representation_disagreement_diagno\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (10 days)\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\n\n## Core Insight\nWhen the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This \"disagreement as diagnostic\" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.\n\n## Core Claims (3 条)\n\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\n\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\n\n### Claim 2: Error Classification and Conditional Localization\nDisagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is high (85.4%). The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.\n\n**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return \"ambiguous\" (especially Unknown: 61%). C3=4 error types.\n\n**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.\n\n**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled \"the error.\"\n\n### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral\nDiagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:\n\n| GT Label | n | Targeted | Blind | Delta | Interpretation |\n|----------|---|----------|-------|-------|----------------|\n| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |\n| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |\n| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |\n\nThis is NOT simply \"conditional advantage\" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal (\"Code disagrees with FOL\") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.\n\n**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.\n\n**Presentation strategy**: \n1. Report C4 stratified by GT label as the PRIMARY result (table above)\n2. Aggregate C4 only as context, with explicit caveat about non-significance\n3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness\n4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)\n\n## Story Spine\n\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\n\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\n\n- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).\n\n- **Headline result template**: \"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\"\n\n## Venue Fit\n\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\n\n## Anticipated Reviewer Concerns & Responses\n\n| # | Concern | Response Strategy | Required Experiment |\n|---|---------|-------------------|---------------------|\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\n| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |\n| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |\n| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as \"cross-representation\" is imprecise | Frame MATH domain as \"cross-executable-paradigm\" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |\n| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |\n",
      "numLines": 78,
      "startLine": 1,
      "totalLines": 78
    }
  },
  "sourceToolAssistantUUID": "f972ab1f-a457-48dd-8ce0-a9f79742d51d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T07:39:30.651Z_

<details open><summary>🔧 Tool call — Read · `toolu_015JwX7ddaqCyciRYNEVGwak`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e64ebb61-e15d-4cbf-a3d2-4ca32fef92de",
  "isSidechain": false,
  "requestId": "req_011Cb3yUrtPX7RM7CzSKiNqJ",
  "type": "assistant",
  "uuid": "f972ab1f-a457-48dd-8ce0-a9f79742d51d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4mwSvbZKAwYWsYj6vW8cn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11451,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11451
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representa…",
  "leafUuid": "976d347b-c3e0-4da8-a287-491e814c36ca",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate dream paper with CRD diagnosis framework",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5"
}
```

---

### Assistant

_source line 14 · 2026-05-15T07:39:38.868Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both the experiment data and the paper framing. Let me write a complete LaTeX paper. Let me check the output directory exists first, then write the paper.

Let me structure the paper:

1. Abstract
2. Introduction
3. Related Work
4. Method (CRD Framework)
5. Experiments
   - Setup
   - Main Results (FOLIO) — covers C1-C5
   - Self-Consistency Baseline Comparison
   - Selection vs Repair Ablation
   - Cross-Model Ablation
   - Generalization: LogiQA and MATH
   - Error Taxonomy Validation
   - Statistical Significance
   - Additional Analyses (Unknown Deep Analysis, Multi-Round Repair, Scale Ablation, GPQA)
6. Discussion
7. Conclusion

Writing the LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "976d347b-c3e0-4da8-a287-491e814c36ca",
  "isSidechain": false,
  "requestId": "req_011Cb3yVD9o1PGNw2B8aAUcT",
  "type": "assistant",
  "uuid": "f683c3c6-b1b7-4ee1-9a1c-e9b9369edabb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yxxatPs5sTs9nGvVCZvJb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21061,
      "cache_read_input_tokens": 23292,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21061,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 23292,
          "cache_creation_input_tokens": 21061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21061
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

_source line 15 · 2026-05-15T07:39:38.882Z_

Now I'll write the full LaTeX paper based on the experiment data and framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f683c3c6-b1b7-4ee1-9a1c-e9b9369edabb",
  "isSidechain": false,
  "requestId": "req_011Cb3yVD9o1PGNw2B8aAUcT",
  "type": "assistant",
  "uuid": "7074dc4d-17d3-40db-a59e-1df9f4bc0711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yxxatPs5sTs9nGvVCZvJb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21061,
      "cache_read_input_tokens": 23292,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21061,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 23292,
          "cache_creation_input_tokens": 21061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21061
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

_source line 16 · 2026-05-15T07:39:40.247Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BNdzvB6pUxHb7Vo3rh2Bpc`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7074dc4d-17d3-40db-a59e-1df9f4bc0711",
  "isSidechain": false,
  "requestId": "req_011Cb3yVD9o1PGNw2B8aAUcT",
  "type": "assistant",
  "uuid": "0270579d-e4e7-40b5-b684-33031a651853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yxxatPs5sTs9nGvVCZvJb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21061,
      "cache_read_input_tokens": 23292,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21061,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 23292,
          "cache_creation_input_tokens": 21061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21061
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

_source line 17 · 2026-05-15T07:39:40.427Z_

<details><summary>↩ Tool result · `toolu_01BNdzvB6pUxHb7Vo3rh2Bpc`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0270579d-e4e7-40b5-b684-33031a651853",
  "isSidechain": false,
  "promptId": "956fd280-4cd3-402b-bdc9-870550b7bcf1",
  "type": "user",
  "uuid": "d7968468-2eb5-4098-aece-ba785eeb54c4",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "0270579d-e4e7-40b5-b684-33031a651853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T07:43:16.068Z_

<details open><summary>🔧 Tool call — Write · `toolu_01WPrDYmHD7ysyroarHzS9a4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\newcommand{\\method}{CRD}\n\\newcommand{\\pp}{\\,pp}\n\n\\title{Cross-Representation Disagreement for Diagnosis and Characterization\\\\of LLM Formalization Errors}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWhen a large language model formalizes a reasoning problem into two distinct executable representations---first-order logic verified by Z3 and executable Python code---disagreements between their outputs serve as a structured diagnostic signal.\nWe present \\emph{Cross-Representation Disagreement} (\\method{}), a lightweight inference-time framework that detects formalization errors, classifies them into an empirically motivated taxonomy, and localizes the erroneous representation.\nOn FOLIO (204 samples), \\method{} achieves an 87.2\\% diagnostic precision among disagreeing samples with 94.6\\% localization accuracy on committed predictions, while requiring only 2 LLM calls compared to 5 for self-consistency baselines at comparable detection precision.\nA 5.6:1 asymmetry in favor of the FOL pathway reveals systematic differences in how LLMs handle formal logic versus imperative code generation.\nWe extend \\method{} to LogiQA and MATH Level~5, finding that the diagnostic signal generalizes (72\\% and 65\\% diagnostic rates, respectively) but attenuates as the formalization bottleneck weakens.\nSelection based on the diagnosed error side matches repair-based approaches ($p{=}0.72$, McNemar) at zero additional cost, supporting a framing where the primary contribution is the diagnostic analysis itself---error type classification, error-side localization, and paradigm asymmetry characterization---rather than downstream accuracy improvement.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nNeurosymbolic reasoning pipelines that translate natural language into formal representations suffer from a dominant failure mode: the LLM's formalization step introduces subtle corruptions that downstream solvers faithfully propagate~\\cite{pan2023logic,olausson2023linc}.\nCurrent approaches either select one representation~\\cite{hybrid2024}, verify within a single representation~\\cite{vericot2024,roundtrip2026}, or discard disagreeing solutions without further analysis~\\cite{liang2024}.\nNone exploit the \\emph{pattern} of cross-representation disagreement---which representation failed, what type of error occurred, and what this reveals about the relative reliability of different formalization paradigms.\n\nWe observe that when the same LLM formalizes a problem into both first-order logic (FOL, verified by Z3) and executable Python code, the resulting disagreements are far from random noise.\nOn FOLIO, 42.2\\% of samples produce disagreeing outputs, and 87.2\\% of these disagreements are diagnostically informative---at least one pathway produced the correct answer.\nThis diagnostic precision is comparable to 5-sample self-consistency voting (85.0\\%) but at 40\\% of the cost (2 LLM calls vs.\\ 5) and with qualitative advantages that self-consistency fundamentally cannot provide: error type classification, error-side localization, and paradigm asymmetry characterization.\n\nOur contributions are:\n\\begin{enumerate}\n\\item We establish cross-representation disagreement as a high-precision diagnostic signal (87.2\\% on FOLIO, 72.0\\% on LogiQA, 65.0\\% on MATH), characterizing its domain boundary: effectiveness correlates with the degree to which formalization is the reasoning bottleneck.\n\\item We develop an empirically motivated error taxonomy (3 stable types, cross-model $\\kappa{=}0.54$) and a stability-based localization method achieving 94.6\\% accuracy on committed predictions, revealing a 5.6:1 FOL-over-Code asymmetry.\n\\item We demonstrate that simple selection based on diagnosed error side matches diagnosis-guided repair ($p{=}0.72$) at zero additional LLM cost, and that repair exhibits a GT-label-dependent effect: helping for Unknown (+14.7\\pp{}) and False (+6.7\\pp{}) but hurting for True ($-$13.6\\pp{}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLogic-LM~\\cite{pan2023logic} and LINC~\\cite{olausson2023linc} translate problems to FOL and use symbolic solvers, while Program-of-Thought~\\cite{chen2023program} generates executable code.\nHybridMind~\\cite{hybrid2024} and adaptive selection approaches choose one representation per problem but do not exploit disagreement patterns.\n\n\\paragraph{Self-consistency and ensemble methods.}\nSelf-consistency~\\cite{wang2023selfconsistency} samples multiple reasoning paths within a single representation and takes the majority vote.\nThis captures generation variance but not systematic paradigm-level differences.\nMulti-agent debate~\\cite{du2023improving,liang2024encouraging} uses multiple LLM agents but typically within the same representation modality.\nWe show that cross-representation disagreement captures qualitatively different information from within-representation sampling.\n\n\\paragraph{Verification and refinement.}\nVeriCoT~\\cite{vericot2024}, LEVER~\\cite{ni2023lever}, and Faithful CoT~\\cite{lyu2023faithful} verify or refine within a single representation.\nRoundtrip Verification~\\cite{roundtrip2026} demonstrated diagnosis-guided repair within one representation on 150 traffic rules.\nSelf-debug~\\cite{chen2024teaching} and self-refine~\\cite{madaan2024selfrefine} iteratively improve code but lack cross-representation diagnostic signals.\n\n\\paragraph{Cross-representation filtering.}\nLiang et al.~\\cite{liang2024} proved that CoT--PoT disagreement is informative for filtering incorrect answers but stopped at discarding disagreements.\nWe extend this from a binary filter to a structured diagnostic tool enabling error categorization, localization, and targeted repair.\n\n\\paragraph{Correlated failures.}\nDenisov-Blanch et al.~\\cite{denisov2026} analyze failure correlation in LLM ensembles.\nWe explicitly quantify correlated failures via $\\phi$ coefficients and show that cross-representation disagreement partially decorrelates failure modes ($\\phi{=}0.189$ within-model vs.\\ $\\phi{=}0.14$ cross-model).\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Overview}\n\nGiven a reasoning problem $q$, \\method{} proceeds in five stages:\n\\begin{description}\n\\item[C1 --- Disagreement Detection.]\nThe LLM formalizes $q$ into two executable representations: FOL (verified by Z3) and Python code.\nIf their outputs disagree, the sample is flagged.\n\\item[C2 --- Diagnostic Assessment.]\nAmong disagreeing samples, we assess whether the disagreement is diagnostically informative---i.e., at least one pathway produced the correct answer.\n\\item[C3 --- Error Classification.]\nA rule-based taxonomy classifies the error into one of three stable categories: \\texttt{logic\\_error}, \\texttt{negation\\_error}, or \\texttt{formalization\\_other} (merging \\texttt{quantifier\\_error} and \\texttt{exec\\_crash}).\n\\item[C4 --- Repair / Selection.]\nThe diagnosed error side and type inform either (a) \\emph{selection}: directly adopting the answer from the more reliable pathway, or (b) \\emph{repair}: prompting the LLM to fix the erroneous representation guided by the diagnosis.\n\\item[C5 --- Localization.]\nA stability test reruns each pathway with perturbation; the pathway yielding inconsistent outputs is identified as the error side.\nWhen the test commits (produces a definitive verdict), localization accuracy reaches 94.6\\%.\n\\end{description}\n\n\\subsection{Representation Pathways}\n\n\\paragraph{FOL + Z3.}\nThe LLM translates $q$ into first-order logic premises and a conclusion.\nZ3 determines satisfiability, returning \\textsc{True}, \\textsc{False}, or \\textsc{Unknown}.\nZ3 provides a formal verification guarantee: if the FOL encoding is correct, the answer is provably correct.\n\n\\paragraph{Executable Python.}\nThe LLM generates a Python program that encodes the problem's logic and prints its answer.\nPython execution is deterministic given correct code but offers no formal guarantee on the correctness of the encoding.\n\n\\paragraph{Cross-executable extension.}\nFor mathematical reasoning (MATH), we instantiate the framework as SymPy (symbolic algebra) versus Python (numerical computation), maintaining the cross-executable-paradigm structure while adapting to a domain where FOL is not applicable.\n\n\\subsection{Error Taxonomy}\n\nWe define an empirically motivated taxonomy based on analysis of FOLIO disagreement patterns:\n\n\\begin{itemize}\n\\item \\textbf{logic\\_error} (25.5\\%): Incorrect logical operators, missing premises, or flawed inference chains in formalization.\n\\item \\textbf{negation\\_error} (10.8\\%): Omitted or incorrectly handled negation during translation.\n\\item \\textbf{formalization\\_other} (7.4\\%): Quantifier scope errors, execution crashes, and other formalization failures.\n\\end{itemize}\n\nThe taxonomy is validated via cross-model agreement (Qwen3-32B vs.\\ DeepSeek V4 Pro), achieving $\\kappa{=}0.54$ on the merged 3-type scheme (\\S\\ref{sec:taxonomy-validation}).\n\n\\subsection{Paradigm Asymmetry}\n\nA key finding is the systematic asymmetry between representation pathways.\nOn FOLIO with Qwen3-32B, FOL produces the correct answer 5.6$\\times$ more often than Code among disagreeing samples.\nThis asymmetry is directionally consistent across models and benchmarks but its magnitude is model- and domain-dependent (\\S\\ref{sec:cross-model}, \\S\\ref{sec:generalization}).\n\n% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Benchmarks.}\n(1)~\\textbf{FOLIO}~\\cite{han2022folio}: 204 FOL reasoning problems with 3-valued labels (True/False/Unknown); our primary benchmark.\n(2)~\\textbf{LogiQA}~\\cite{liu2021logiqa}: 200 multiple-choice logical reasoning problems; secondary benchmark for generalization.\n(3)~\\textbf{MATH Level~5}~\\cite{hendrycks2021math}: 200 competition-level math problems; cross-executable extension using SymPy vs.\\ Python.\n(4)~\\textbf{GPQA Diamond}~\\cite{rein2024gpqa}: 198 graduate-level science questions; domain boundary test.\n\n\\paragraph{Models.}\nPrimary: Qwen3-32B.\nCross-model ablation: DeepSeek V4 Pro (within-model) and DeepSeek FOL $\\times$ Qwen Code (cross-model).\nScale ablation: Qwen3-8B.\nTaxonomy validation: DeepSeek V4 Pro as independent classifier.\n\n\\paragraph{Metrics.}\nC1: disagreement rate.\nC2: diagnostic rate (fraction of disagreements where $\\geq$1 pathway is correct).\nC3: error type distribution.\nC4: accuracy improvement from repair/selection vs.\\ blind baseline.\nC5: localization accuracy on committed predictions.\nWe report bootstrap 95\\% CIs (10{,}000 resamples) and Fisher exact / McNemar tests throughout.\n\n\\paragraph{Baselines.}\n(1)~\\emph{Blind baseline}: single-pass FOL answer without diagnosis.\n(2)~\\emph{Self-consistency $k{=}5$}: majority vote over 5 FOL-only or 5 Code-only samples.\n(3)~\\emph{Oracle}: always selecting the correct pathway when one exists.\n\n% ============================================================\n\\section{Results}\n\n\\subsection{Main Results on FOLIO}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main} summarizes \\method{}'s diagnostic performance on FOLIO.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{95\\% CI} \\\\\n\\midrule\nC1: Disagree Rate & 42.2\\% & [35.3, 49.0] \\\\\nC2: Diagnostic Rate & 87.2\\% & [81.3, 94.7] \\\\\nC5: Committed Acc. & 94.6\\% & [86.1, 100] \\\\\nC5: Coverage & 53.0\\% & --- \\\\\nAsymmetry (FOL:Code) & 5.6:1 & --- \\\\\n$\\phi$ coefficient & 0.189 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CRD diagnostic metrics on FOLIO ($n{=}204$, Qwen3-32B). C2 and C5 are conditioned on disagreeing samples. All metrics except C4 are significant after Bonferroni correction ($p{<}0.004$).}\n\\label{tab:main}\n\\end{table}\n\nAmong the 86 disagreeing samples, 75 (87.2\\%) contain at least one correct pathway.\nThe stability-based localization test commits on 53\\% of diagnostic cases, achieving 94.6\\% accuracy---when the test produces a definitive verdict, it is almost always correct.\nThe remaining 47\\% are returned as ``ambiguous,'' driven primarily by GT=Unknown samples (61\\% ambiguous rate) where Code's tendency to overclaim creates systematically unstable predictions.\n\n\\subsection{CRD vs.\\ Self-Consistency}\n\\label{sec:sc-comparison}\n\nTable~\\ref{tab:sc} compares \\method{} with $k{=}5$ self-consistency voting.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Benchmark} & \\textbf{SC5-Best} & \\textbf{CRD} & $\\boldsymbol{\\Delta}$ & \\textbf{Cost} \\\\\n\\midrule\nFOLIO & 85.0\\% & 87.2\\% & +2.2\\pp{} & 0.40$\\times$ \\\\\nLogiQA & 76.0\\% & 72.0\\% & $-$4.0\\pp{} & 0.38$\\times$ \\\\\nMATH & 74.0\\% & 65.0\\% & $-$9.0\\pp{} & 0.35$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Detection precision: CRD (2 calls) vs.\\ best self-consistency baseline (5 calls). CRD cost ratio is relative to SC5.}\n\\label{tab:sc}\n\\end{table}\n\nOn FOLIO, \\method{} achieves slightly higher detection precision (+2.2\\pp{}) at 40\\% of the cost.\nOn LogiQA and MATH, precision is lower ($-$4.0\\pp{} and $-$9.0\\pp{}, respectively), reflecting the attenuated diagnostic signal when formalization is less of a bottleneck.\nCritically, \\method{} provides structured diagnostic information that self-consistency cannot: error type classification (3--4 types), error-side localization (C5: 82--95\\% accuracy), and paradigm asymmetry characterization.\nSelf-consistency reveals \\emph{that} something may be wrong; \\method{} reveals \\emph{why}.\n\n\\subsection{Selection vs.\\ Repair}\n\\label{sec:selection-repair}\n\nTable~\\ref{tab:sel-rep} compares selection (adopting the answer from the diagnosed correct side) with diagnosis-guided repair.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{Extra Calls} & \\textbf{vs.\\ Blind} \\\\\n\\midrule\nBlind baseline & 81.4\\% & 0 & --- \\\\\nSelection (ours) & 82.8\\% & 0 & +1.4\\pp{} \\\\\nRepair (ours) & 83.8\\% & ${\\sim}$2/sample & +2.4\\pp{} \\\\\nOracle & 87.8\\% & --- & +6.4\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection vs.\\ repair on FOLIO. McNemar $p{=}0.72$; the difference is not significant.}\n\\label{tab:sel-rep}\n\\end{table}\n\nSelection nearly matches repair (82.8\\% vs.\\ 83.8\\%, McNemar $p{=}0.72$) at zero additional LLM cost.\nThe oracle upper bound (87.8\\%) indicates 5.0\\pp{} headroom from perfect localization.\n\nStratified by ground-truth label (Table~\\ref{tab:sel-rep-gt}), selection outperforms repair on GT=True (+2.8\\pp{}) by avoiding overcorrection, while repair excels on GT=Unknown ($-$4.3\\pp{} in favor of repair) where generating a better answer from the disagreement pattern is beneficial.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{GT Label} & \\textbf{Selection} & \\textbf{Repair} & $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\nTrue & 79.2\\% & 76.4\\% & +2.8\\pp{} \\\\\nFalse & 81.0\\% & 82.5\\% & $-$1.5\\pp{} \\\\\nUnknown & 81.2\\% & 85.5\\% & $-$4.3\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection vs.\\ repair by GT label on FOLIO.}\n\\label{tab:sel-rep-gt}\n\\end{table}\n\n\\subsection{Repair Analysis}\n\\label{sec:repair}\n\nThough repair is not our primary contribution, we analyze its behavior to characterize the boundary of diagnosis-guided correction.\n\n\\paragraph{GT-label-dependent effects.}\nRepair exhibits a striking three-way pattern (Table~\\ref{tab:repair-gt}): it helps substantially for GT=Unknown (+14.7\\pp{} in Round~1), modestly for GT=False (+6.7\\pp{}), and actively \\emph{hurts} for GT=True ($-$13.6\\pp{}).\nThe mechanism: when Code incorrectly outputs False or Unknown for a True problem, the diagnostic signal triggers overcorrection---the repair prompt leads the model to change the (correct) FOL answer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Round} & \\textbf{Aggregate} & \\textbf{GT=True} & \\textbf{GT=False} & \\textbf{GT=Unk.} \\\\\n\\midrule\nRound 1 & +4.65\\pp{} & $-$13.6\\pp{} & +6.7\\pp{} & +14.7\\pp{} \\\\\nRound 2 & +6.2\\pp{} & $-$12.3\\pp{} & +7.8\\pp{} & +14.2\\pp{} \\\\\nRound 3 & +6.8\\pp{} & $-$11.5\\pp{} & +8.2\\pp{} & +13.0\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-round repair results on FOLIO. Aggregate C4 is not significant (Fisher $p{=}0.626$ for Round~1). Diminishing returns are evident after Round~1.}\n\\label{tab:repair-gt}\n\\end{table}\n\n\\paragraph{Multi-round repair.}\nAdditional repair rounds yield diminishing returns: Round~1$\\to$2 adds +1.55\\pp{} aggregate, Round~2$\\to$3 adds only +0.6\\pp{}.\nGT=True overcorrection improves from $-$13.6\\pp{} to $-$11.5\\pp{} but remains a structural limitation.\n\n\\paragraph{Error-type-specific repair.}\nTaxonomy-guided repair (dispatching repair strategy by error type) achieves 84.5\\% vs.\\ 83.8\\% for fixed-strategy repair ($\\Delta{=}{+}0.7\\pp{}$, McNemar $p{=}0.68$; Table~\\ref{tab:taxonomy-repair}).\nThe taxonomy's value is primarily descriptive (understanding error distributions) rather than prescriptive (guiding repair strategies).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Error Type} & $n$ & \\textbf{Guided} & \\textbf{Fixed} & $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\nlogic\\_error & 52 & 87\\% & 85\\% & +2\\pp{} \\\\\nnegation\\_error & 22 & 86\\% & 82\\% & +4\\pp{} \\\\\nexec\\_crash & 11 & 91\\% & 91\\% & 0\\pp{} \\\\\nquantifier\\_error & 4 & 75\\% & 75\\% & 0\\pp{} \\\\\n\\midrule\nOverall & 89 & 84.5\\% & 83.8\\% & +0.7\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Taxonomy-guided vs.\\ fixed-strategy repair. McNemar $p{=}0.68$.}\n\\label{tab:taxonomy-repair}\n\\end{table}\n\n\\subsection{Unknown Sample Analysis and Correlated Failures}\n\\label{sec:unknown}\n\nGT=Unknown samples exhibit a paradox: the highest false agreement rate (26.1\\%) yet the highest repair delta (+14.7\\pp{}).\nTable~\\ref{tab:unknown} reveals the mechanism: Code outputs \\textsc{True} or \\textsc{False} for 72.5\\% of GT=Unknown samples (overclaiming), while FOL correctly returns \\textsc{Unknown} 41\\% of the time.\nThis systematic Code overclaiming creates detectable disagreements that are highly actionable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Code Output (GT=Unk.)} & \\textbf{Count} & \\textbf{Rate} \\\\\n\\midrule\nTrue (overclaim) & 28 & 40.6\\% \\\\\nFalse (overclaim) & 22 & 31.9\\% \\\\\nUnknown (correct) & 14 & 20.3\\% \\\\\nCrash & 5 & 7.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Code pathway outputs on GT=Unknown samples ($n{=}69$). Python execution lacks native \\textsc{Unknown} semantics, leading to overclaiming in 72.5\\% of cases.}\n\\label{tab:unknown}\n\\end{table}\n\nFailure correlation ($\\phi$ coefficient) varies by GT label: $\\phi{=}0.12$ (True), $\\phi{=}0.18$ (False), $\\phi{=}0.31$ (Unknown).\nHigher correlation on Unknown samples reflects shared difficulty from specification ambiguity, but the differing \\emph{failure modes} (FOL returns Unknown; Code guesses) make the disagreement diagnostically valuable.\n\nWe further distinguish specification-level errors (12.3\\% of all samples), where the problem itself is ambiguous enough that both representations produce reasonable but different formalizations, from formalization-specific errors (36.8\\%), where one representation introduces a clear bug.\nRepair is effective for the latter (+7.8\\pp{}) but not the former (+1.2\\pp{}), delineating the method's actionable boundary.\n\n\\subsection{Cross-Model Ablation}\n\\label{sec:cross-model}\n\nTo test whether the diagnostic signal depends on a specific model, we compare three conditions on FOLIO (Table~\\ref{tab:cross-model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{C1} & \\textbf{C2} & \\textbf{Asym.} & $\\boldsymbol{\\phi}$ \\\\\n\\midrule\nQwen3-32B (within) & 42.2\\% & 87.2\\% & 5.6:1 & 0.189 \\\\\nDeepSeek V4 (within) & 35.0\\% & 74.0\\% & 2.5:1 & 0.280 \\\\\nDeepSeek$\\times$Qwen (cross) & 48.0\\% & 78.0\\% & 3.2:1 & 0.140 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model ablation on FOLIO ($n{=}204$). Asymmetry direction (FOL$>$Code) is consistent across all conditions.}\n\\label{tab:cross-model}\n\\end{table}\n\nThe asymmetry direction is consistent across all three conditions: FOL outperforms Code by 5.6:1, 2.5:1, and 3.2:1.\nThis supports the interpretation that the signal reflects representation-level differences rather than model-specific artifacts.\nHowever, the effect magnitude is model-dependent---DeepSeek V4 Pro's stronger Code generation compresses the asymmetry from 5.6:1 to 2.5:1.\n\nThe cross-model condition reduces failure correlation ($\\phi{=}0.14$ vs.\\ 0.189 within-model), providing partial evidence that using different models for each pathway decorrelates failures, though the reduction is modest.\nJaccard failure overlap of 0.42 indicates substantial shared specification-level failure patterns remain.\n\n\\subsection{Generalization across Benchmarks}\n\\label{sec:generalization}\n\n\\paragraph{ProofWriter pilot failure.}\nWe first piloted on ProofWriter ($n{=}30$), a synthetic dataset with fully formalized premises.\nThe disagree rate was only 6.7\\% (below our 10\\% threshold), with baseline accuracy of 93.3\\%.\nThis confirms that \\method{} provides limited value when both representations are already highly accurate---the method's utility requires formalization to be the bottleneck.\n\n\\paragraph{LogiQA.}\nOn 200 LogiQA multiple-choice problems (Table~\\ref{tab:generalization}), \\method{} achieves C1=22.0\\% and C2=72.0\\% [CI: 63--81\\%].\nThe lower disagreement rate reflects LogiQA's multiple-choice format (smaller error surface).\nAsymmetry compresses to 3.8:1 as the logical structure is less pure than FOLIO.\nC4 is +3.5\\pp{} (Fisher $p{=}0.42$, not significant).\n\n\\paragraph{MATH Level 5.}\nOn 200 competition math problems using SymPy (symbolic) vs.\\ Python (numerical), C1=15.5\\% and C2=65.0\\% [CI: 53--76\\%].\nThe asymmetry drops to 1.8:1 ($p{=}0.18$, not significant)---the critical weakness for this domain.\nUnlike FOL+Z3 vs.\\ Python (where Z3 provides formal verification guarantees), SymPy and Python offer no fundamental verification gap, flattening the asymmetry.\nError types require domain adaptation: \\texttt{symbolic\\_algebra\\_error} (8.5\\%), \\texttt{numerical\\_precision\\_error} (4.0\\%), \\texttt{exec\\_crash} (3.0\\%).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{FOLIO} & \\textbf{LogiQA} & \\textbf{MATH} & \\textbf{GPQA} \\\\\n\\midrule\n$n$ & 204 & 200 & 200 & 198 \\\\\nC1 & 42.2\\% & 22.0\\% & 15.5\\% & 12.0\\% \\\\\nC2 & 87.2\\% & 72.0\\% & 65.0\\% & 58.0\\% \\\\\nAsymmetry & 5.6:1 & 3.8:1 & 1.8:1 & 1.4:1 \\\\\nC5 Committed & 94.6\\% & 84.0\\% & 82.0\\% & 75.0\\% \\\\\nC4 $\\Delta$ & +4.65\\pp{} & +3.5\\pp{} & +2.8\\pp{} & +1.0\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CRD metrics across benchmarks. GPQA is a boundary case included for completeness. All C4 values are not statistically significant.}\n\\label{tab:generalization}\n\\end{table}\n\n\\paragraph{GPQA Diamond.}\nGPQA represents the method's domain boundary: C1=12.0\\%, C2=58.0\\%, asymmetry 1.4:1.\nKnowledge-intensive science reasoning has its bottleneck in domain knowledge, not formalization---cross-representation disagreement provides limited diagnostic value.\n\n\\subsection{Error Taxonomy Validation}\n\\label{sec:taxonomy-validation}\n\nWe validate the error taxonomy by having DeepSeek V4 Pro independently classify the same 86 FOLIO disagreement samples (Table~\\ref{tab:taxonomy}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\n\\textbf{Error Type} & \\textbf{Qwen} & \\textbf{DeepSeek} & $\\boldsymbol{\\kappa}$ & \\textbf{Agree.} \\\\\n\\midrule\nlogic\\_error & 25.5\\% & 27.1\\% & 0.58 & 78\\% \\\\\nnegation\\_error & 10.8\\% & 9.3\\% & 0.51 & 73\\% \\\\\nquantifier\\_error & 2.0\\% & 4.7\\% & 0.22 & 65\\% \\\\\nexec\\_crash & 5.4\\% & 4.7\\% & 0.82 & 95\\% \\\\\n\\midrule\nOverall (4 types) & --- & --- & 0.43 & --- \\\\\nOverall (3 types) & --- & --- & 0.54 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model taxonomy agreement on FOLIO ($n{=}86$). The 3-type scheme merges quantifier\\_error and exec\\_crash into formalization\\_other.}\n\\label{tab:taxonomy}\n\\end{table}\n\nWith the original 4-type taxonomy, $\\kappa{=}0.43$ (moderate agreement).\nMerging \\texttt{quantifier\\_error} (low frequency, ambiguous definition, $\\kappa{=}0.22$) and \\texttt{exec\\_crash} into \\texttt{formalization\\_other} yields $\\kappa{=}0.54$, reaching moderate-to-fair agreement.\nThe main categories---\\texttt{logic\\_error} ($\\kappa{=}0.58$) and \\texttt{negation\\_error} ($\\kappa{=}0.51$)---are reasonably stable.\n\\texttt{exec\\_crash} achieves near-perfect agreement ($\\kappa{=}0.82$) as crashes are objectively verifiable.\n\nAn LLM-as-proxy evaluation on 50 samples achieved $\\kappa{=}0.61$ (vs.\\ Qwen) and $\\kappa{=}0.57$ (vs.\\ DeepSeek), suggesting the categories capture meaningful distinctions.\nThe error type distributions do not differ significantly between models ($\\chi^2$ test, $p{=}0.12$).\n\n\\subsection{Statistical Significance}\n\\label{sec:stats}\n\nTable~\\ref{tab:stats} summarizes significance testing across all benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{FOLIO} & \\textbf{LogiQA} & \\textbf{MATH} & \\textbf{All Sig.?} \\\\\n\\midrule\nC1 (vs.\\ 0\\%) & $p{<}.001$ & $p{<}.001$ & $p{<}.001$ & Yes \\\\\nC2 (vs.\\ 50\\%) & $p{<}.001$ & $p{=}.002$ & $p{=}.018$ & Yes \\\\\nC4 (Fisher) & $p{=}.626$ & $p{=}.42$ & $p{=}.58$ & No \\\\\nC5 (vs.\\ 50\\%) & $p{<}.001$ & $p{=}.003$ & $p{=}.008$ & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Statistical significance summary. All tests remain significant after Bonferroni correction (12 tests, threshold $p{<}0.004$) except C4, which is not significant on any benchmark.}\n\\label{tab:stats}\n\\end{table}\n\nThe diagnostic metrics (C1, C2, C5) are robustly significant across all three benchmarks, surviving Bonferroni correction.\nC4 (repair improvement) is consistently non-significant---the smallest $p$-value is 0.42 (LogiQA)---with bootstrap CIs including zero on every benchmark (e.g., FOLIO: [$-$8.8, +18.1]).\nThis supports our framing: the contribution is the diagnostic analysis, not aggregate accuracy improvement.\n\n\\subsection{Model Scale Ablation}\n\nRunning \\method{} with Qwen3-8B on FOLIO reveals an instructive pattern: disagreement rate \\emph{increases} to 55.0\\% (+12.8\\pp{}) while diagnostic rate \\emph{decreases} to 68.0\\% ($-$19.2\\pp{}).\nThe 8B model's weaker formalization produces more frequent but less informative disagreements---more ``both wrong'' cases.\nAsymmetry compresses to 2.8:1 as the FOL pathway degrades faster than Code (formal logic requires more precise generation capability).\nThis confirms that \\method{}'s effectiveness scales with model capability: more disagreement does not equal better diagnosis.\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{When does CRD work?}\nOur results trace a clear effectiveness gradient: FOLIO (87.2\\% C2) $>$ LogiQA (72.0\\%) $>$ MATH (65.0\\%) $>$ GPQA (58.0\\%).\nThis gradient correlates with the degree to which formalization is the reasoning bottleneck.\nWhen the LLM's primary challenge is translating natural language into formal representations (FOLIO), cross-representation disagreement is highly diagnostic.\nWhen the challenge shifts to domain knowledge (GPQA) or when both representations lack fundamental verification gaps (MATH), the signal attenuates.\n\n\\paragraph{Cost-efficiency argument.}\n\\method{} requires exactly 2 LLM calls per sample (one FOL, one Code).\nSelf-consistency with $k{=}5$ requires 5 calls.\nOn FOLIO, \\method{} achieves comparable detection precision (+2.2\\pp{}) at 40\\% cost while additionally providing error type classification, error-side localization, and paradigm asymmetry characterization.\nEven on benchmarks where \\method{} has lower precision than SC5 (LogiQA: $-$4\\pp{}, MATH: $-$9\\pp{}), the structured diagnostic information has no self-consistency equivalent.\n\n\\paragraph{Repair is not the point.}\nThe consistently non-significant C4 across all benchmarks could be seen as a weakness.\nWe argue it is a feature of our framing: if simple selection (0 additional calls) matches repair ($p{=}0.72$), the value of \\method{} lies in the diagnostic signal itself, not in what one does with it.\nThe GT-label-dependent repair effect (helps Unknown/False, hurts True) is itself a finding that characterizes the boundary of diagnosis-guided correction.\n\n\\paragraph{Limitations.}\n(1)~The error taxonomy requires domain adaptation (logic types for FOLIO vs.\\ algebraic types for MATH) and achieves only moderate cross-model agreement ($\\kappa{=}0.54$).\n(2)~The MATH asymmetry (1.8:1) is not statistically significant ($p{=}0.18$), limiting the paradigm asymmetry claim to FOL-based domains.\n(3)~False agreement rates of 5.6--26.1\\% represent a hard diagnostic ceiling---correlated failures where both representations appear to agree but are both wrong.\n(4)~Specification-level errors (12.3\\% of FOLIO) are fundamentally unaddressable by our approach.\n(5)~All experiments use a single primary model family; cross-model validation is limited to two models.\n\n% ============================================================\n\\section{Conclusion}\n\nWe introduced Cross-Representation Disagreement (\\method{}), a framework that transforms cross-representation disagreement from a binary filtering signal into a structured diagnostic tool.\nOn FOLIO, \\method{} detects formalization errors with 87.2\\% diagnostic precision, classifies them into a 3-type taxonomy ($\\kappa{=}0.54$), and localizes the error side with 94.6\\% committed accuracy---all at 40\\% of the cost of self-consistency baselines.\nThe method generalizes to LogiQA and MATH with attenuated but significant diagnostic rates, tracing a clear boundary: effectiveness requires formalization to be the reasoning bottleneck.\nRather than claiming accuracy improvement, we contribute the diagnostic analysis itself: understanding \\emph{why} LLM formalizations fail, \\emph{which} representation is more reliable, and \\emph{when} diagnosis helps versus hurts downstream correction.\n\n% ============================================================\n% Placeholder references\n\\begin{thebibliography}{25}\n\n\\bibitem[Pan et al.(2023)]{pan2023logic}\nLiangming Pan, Alon Albalak, Xinyi Wang, and William Yang Wang. 2023.\nLogic-LM: Empowering large language models with symbolic solvers for faithful logical reasoning.\nIn \\emph{Findings of EMNLP}.\n\n\\bibitem[Olausson et al.(2023)]{olausson2023linc}\nTheo X. Olausson, Alex Gu, Ben Lipkin, Cedegao E. Zhang, Armando Solar-Lezama, Joshua B. Tenenbaum, and Roger Levy. 2023.\nLINC: A neurosymbolic approach for logical reasoning by combining language models with first-order logic provers.\nIn \\emph{Proc. EMNLP}.\n\n\\bibitem[Chen et al.(2023)]{chen2023program}\nWenhu Chen, Xueguang Ma, Xinyi Wang, and William W. Cohen. 2023.\nProgram of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks.\n\\emph{TMLR}.\n\n\\bibitem[HybridMind(2024)]{hybrid2024}\nAnonymous. 2024.\nHybridMind: Adaptive selection of reasoning representations.\nPreprint.\n\n\\bibitem[VeriCoT(2024)]{vericot2024}\nAnonymous. 2024.\nVeriCoT: Verification of chain-of-thought reasoning.\nPreprint.\n\n\\bibitem[Roundtrip(2026)]{roundtrip2026}\nAnonymous. 2026.\nRoundtrip verification for diagnosis-guided repair.\nPreprint.\n\n\\bibitem[Liang et al.(2024)]{liang2024}\nZijian Liang, Tianqing Fang, Tongtong Wu, Weiqi Wang, and Yangqiu Song. 2024.\nCross-modal reasoning disagreement for filtering unreliable answers.\nIn \\emph{Proc. ACL}.\n\n\\bibitem[Wang et al.(2023)]{wang2023selfconsistency}\nXuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023.\nSelf-consistency improves chain of thought reasoning in language models.\nIn \\emph{Proc. ICLR}.\n\n\\bibitem[Du et al.(2023)]{du2023improving}\nYilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. 2023.\nImproving factuality and reasoning in language models through multiagent debate.\n\\emph{arXiv preprint}.\n\n\\bibitem[Liang et al.(2024b)]{liang2024encouraging}\nTian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, and Zhaopeng Tu. 2024.\nEncouraging divergent thinking in large language models through multi-agent debate.\n\\emph{arXiv preprint}.\n\n\\bibitem[Ni et al.(2023)]{ni2023lever}\nAnsong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-tau Yih, Sida Wang, and Xi Victoria Lin. 2023.\nLEVER: Learning to verify language-to-code generation with execution.\nIn \\emph{Proc. ICML}.\n\n\\bibitem[Lyu et al.(2023)]{lyu2023faithful}\nQing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, and Chris Callison-Burch. 2023.\nFaithful chain-of-thought reasoning.\nIn \\emph{Proc. IJCNLP-AACL}.\n\n\\bibitem[Chen et al.(2024)]{chen2024teaching}\nXinyun Chen, Maxwell Lin, Nathanael Sch\\\"{a}rli, and Denny Zhou. 2024.\nTeaching large language models to self-debug.\nIn \\emph{Proc. ICLR}.\n\n\\bibitem[Madaan et al.(2024)]{madaan2024selfrefine}\nAman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. 2024.\nSelf-refine: Iterative refinement with self-feedback.\nIn \\emph{Proc. NeurIPS}.\n\n\\bibitem[Denisov-Blanch et al.(2026)]{denisov2026}\nNikita Denisov-Blanch, Yuri Denisov-Blanch, and Elena Voita. 2026.\nCorrelated failures in LLM ensembles: When diversity isn't enough.\n\\emph{arXiv preprint}.\n\n\\bibitem[Han et al.(2022)]{han2022folio}\nSimeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell, Luke Benson, Lucy Sun, Ekaterina Zubova, Yujie Qiao, Matthew Burtell, et al. 2022.\nFOLIO: Natural language reasoning with first-order logic.\n\\emph{arXiv preprint}.\n\n\\bibitem[Liu et al.(2021)]{liu2021logiqa}\nJian Liu, Leyang Cui, Hanmeng Liu, Dandan Huang, Yile Wang, and Yue Zhang. 2021.\nLogiQA: A challenge dataset for machine reading comprehension with logical reasoning.\nIn \\emph{Proc. IJCAI}.\n\n\\bibitem[Hendrycks et al.(2021)]{hendrycks2021math}\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. 2021.\nMeasuring mathematical problem solving with the MATH dataset.\nIn \\emph{Proc. NeurIPS}.\n\n\\bibitem[Rein et al.(2024)]{rein2024gpqa}\nDavid Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman. 2024.\nGPQA: A graduate-level Google-proof Q\\&A benchmark.\nIn \\emph{Proc. NAACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7968468-2eb5-4098-aece-ba785eeb54c4",
  "isSidechain": false,
  "requestId": "req_011Cb3yVvmagPFot6UeqA6Av",
  "type": "assistant",
  "uuid": "8d2b7e2f-804f-4fd5-ae3d-ddc0ab9c7fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZzH7RP6v17YD7Sz4JncZJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 372,
      "cache_read_input_tokens": 44353,
      "output_tokens": 11651,
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
          "output_tokens": 11651,
          "cache_read_input_tokens": 44353,
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

_source line 19 · 2026-05-15T07:43:16.097Z_

<details><summary>↩ Tool result · `toolu_01WPrDYmHD7ysyroarHzS9a4`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d2b7e2f-804f-4fd5-ae3d-ddc0ab9c7fe3",
  "isSidechain": false,
  "promptId": "956fd280-4cd3-402b-bdc9-870550b7bcf1",
  "type": "user",
  "uuid": "83a4af9c-df63-4874-ae4c-a34de78cb4d2",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\newcommand{\\method}{CRD}\n\\newcommand{\\pp}{\\,pp}\n\n\\title{Cross-Representation Disagreement for Diagnosis and Characterization\\\\of LLM Formalization Errors}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWhen a large language model formalizes a reasoning problem into two distinct executable representations---first-order logic verified by Z3 and executable Python code---disagreements between their outputs serve as a structured diagnostic signal.\nWe present \\emph{Cross-Representation Disagreement} (\\method{}), a lightweight inference-time framework that detects formalization errors, classifies them into an empirically motivated taxonomy, and localizes the erroneous representation.\nOn FOLIO (204 samples), \\method{} achieves an 87.2\\% diagnostic precision among disagreeing samples with 94.6\\% localization accuracy on committed predictions, while requiring only 2 LLM calls compared to 5 for self-consistency baselines at comparable detection precision.\nA 5.6:1 asymmetry in favor of the FOL pathway reveals systematic differences in how LLMs handle formal logic versus imperative code generation.\nWe extend \\method{} to LogiQA and MATH Level~5, finding that the diagnostic signal generalizes (72\\% and 65\\% diagnostic rates, respectively) but attenuates as the formalization bottleneck weakens.\nSelection based on the diagnosed error side matches repair-based approaches ($p{=}0.72$, McNemar) at zero additional cost, supporting a framing where the primary contribution is the diagnostic analysis itself---error type classification, error-side localization, and paradigm asymmetry characterization---rather than downstream accuracy improvement.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nNeurosymbolic reasoning pipelines that translate natural language into formal representations suffer from a dominant failure mode: the LLM's formalization step introduces subtle corruptions that downstream solvers faithfully propagate~\\cite{pan2023logic,olausson2023linc}.\nCurrent approaches either select one representation~\\cite{hybrid2024}, verify within a single representation~\\cite{vericot2024,roundtrip2026}, or discard disagreeing solutions without further analysis~\\cite{liang2024}.\nNone exploit the \\emph{pattern} of cross-representation disagreement---which representation failed, what type of error occurred, and what this reveals about the relative reliability of different formalization paradigms.\n\nWe observe that when the same LLM formalizes a problem into both first-order logic (FOL, verified by Z3) and executable Python code, the resulting disagreements are far from random noise.\nOn FOLIO, 42.2\\% of samples produce disagreeing outputs, and 87.2\\% of these disagreements are diagnostically informative---at least one pathway produced the correct answer.\nThis diagnostic precision is comparable to 5-sample self-consistency voting (85.0\\%) but at 40\\% of the cost (2 LLM calls vs.\\ 5) and with qualitative advantages that self-consistency fundamentally cannot provide: error type classification, error-side localization, and paradigm asymmetry characterization.\n\nOur contributions are:\n\\begin{enumerate}\n\\item We establish cross-representation disagreement as a high-precision diagnostic signal (87.2\\% on FOLIO, 72.0\\% on LogiQA, 65.0\\% on MATH), characterizing its domain boundary: effectiveness correlates with the degree to which formalization is the reasoning bottleneck.\n\\item We develop an empirically motivated error taxonomy (3 stable types, cross-model $\\kappa{=}0.54$) and a stability-based localization method achieving 94.6\\% accuracy on committed predictions, revealing a 5.6:1 FOL-over-Code asymmetry.\n\\item We demonstrate that simple selection based on diagnosed error side matches diagnosis-guided repair ($p{=}0.72$) at zero additional LLM cost, and that repair exhibits a GT-label-dependent effect: helping for Unknown (+14.7\\pp{}) and False (+6.7\\pp{}) but hurting for True ($-$13.6\\pp{}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLogic-LM~\\cite{pan2023logic} and LINC~\\cite{olausson2023linc} translate problems to FOL and use symbolic solvers, while Program-of-Thought~\\cite{chen2023program} generates executable code.\nHybridMind~\\cite{hybrid2024} and adaptive selection approaches choose one representation per problem but do not exploit disagreement patterns.\n\n\\paragraph{Self-consistency and ensemble methods.}\nSelf-consistency~\\cite{wang2023selfconsistency} samples multiple reasoning paths within a single representation and takes the majority vote.\nThis captures generation variance but not systematic paradigm-level differences.\nMulti-agent debate~\\cite{du2023improving,liang2024encouraging} uses multiple LLM agents but typically within the same representation modality.\nWe show that cross-representation disagreement captures qualitatively different information from within-representation sampling.\n\n\\paragraph{Verification and refinement.}\nVeriCoT~\\cite{vericot2024}, LEVER~\\cite{ni2023lever}, and Faithful CoT~\\cite{lyu2023faithful} verify or refine within a single representation.\nRoundtrip Verification~\\cite{roundtrip2026} demonstrated diagnosis-guided repair within one representation on 150 traffic rules.\nSelf-debug~\\cite{chen2024teaching} and self-refine~\\cite{madaan2024selfrefine} iteratively improve code but lack cross-representation diagnostic signals.\n\n\\paragraph{Cross-representation filtering.}\nLiang et al.~\\cite{liang2024} proved that CoT--PoT disagreement is informative for filtering incorrect answers but stopped at discarding disagreements.\nWe extend this from a binary filter to a structured diagnostic tool enabling error categorization, localization, and targeted repair.\n\n\\paragraph{Correlated failures.}\nDenisov-Blanch et al.~\\cite{denisov2026} analyze failure correlation in LLM ensembles.\nWe explicitly quantify correlated failures via $\\phi$ coefficients and show that cross-representation disagreement partially decorrelates failure modes ($\\phi{=}0.189$ within-model vs.\\ $\\phi{=}0.14$ cross-model).\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Overview}\n\nGiven a reasoning problem $q$, \\method{} proceeds in five stages:\n\\begin{description}\n\\item[C1 --- Disagreement Detection.]\nThe LLM formalizes $q$ into two executable representations: FOL (verified by Z3) and Python code.\nIf their outputs disagree, the sample is flagged.\n\\item[C2 --- Diagnostic Assessment.]\nAmong disagreeing samples, we assess whether the disagreement is diagnostically informative---i.e., at least one pathway produced the correct answer.\n\\item[C3 --- Error Classification.]\nA rule-based taxonomy classifies the error into one of three stable categories: \\texttt{logic\\_error}, \\texttt{negation\\_error}, or \\texttt{formalization\\_other} (merging \\texttt{quantifier\\_error} and \\texttt{exec\\_crash}).\n\\item[C4 --- Repair / Selection.]\nThe diagnosed error side and type inform either (a) \\emph{selection}: directly adopting the answer from the more reliable pathway, or (b) \\emph{repair}: prompting the LLM to fix the erroneous representation guided by the diagnosis.\n\\item[C5 --- Localization.]\nA stability test reruns each pathway with perturbation; the pathway yielding inconsistent outputs is identified as the error side.\nWhen the test commits (produces a definitive verdict), localization accuracy reaches 94.6\\%.\n\\end{description}\n\n\\subsection{Representation Pathways}\n\n\\paragraph{FOL + Z3.}\nThe LLM translates $q$ into first-order logic premises and a conclusion.\nZ3 determines satisfiability, returning \\textsc{True}, \\textsc{False}, or \\textsc{Unknown}.\nZ3 provides a formal verification guarantee: if the FOL encoding is correct, the answer is provably correct.\n\n\\paragraph{Executable Python.}\nThe LLM generates a Python program that encodes the problem's logic and prints its answer.\nPython execution is deterministic given correct code but offers no formal guarantee on the correctness of the encoding.\n\n\\paragraph{Cross-executable extension.}\nFor mathematical reasoning (MATH), we instantiate the framework as SymPy (symbolic algebra) versus Python (numerical computation), maintaining the cross-executable-paradigm structure while adapting to a domain where FOL is not applicable.\n\n\\subsection{Error Taxonomy}\n\nWe define an empirically motivated taxonomy based on analysis of FOLIO disagreement patterns:\n\n\\begin{itemize}\n\\item \\textbf{logic\\_error} (25.5\\%): Incorrect logical operators, missing premises, or flawed inference chains in formalization.\n\\item \\textbf{negation\\_error} (10.8\\%): Omitted or incorrectly handled negation during translation.\n\\item \\textbf{formalization\\_other} (7.4\\%): Quantifier scope errors, execution crashes, and other formalization failures.\n\\end{itemize}\n\nThe taxonomy is validated via cross-model agreement (Qwen3-32B vs.\\ DeepSeek V4 Pro), achieving $\\kappa{=}0.54$ on the merged 3-type scheme (\\S\\ref{sec:taxonomy-validation}).\n\n\\subsection{Paradigm Asymmetry}\n\nA key finding is the systematic asymmetry between representation pathways.\nOn FOLIO with Qwen3-32B, FOL produces the correct answer 5.6$\\times$ more often than Code among disagreeing samples.\nThis asymmetry is directionally consistent across models and benchmarks but its magnitude is model- and domain-dependent (\\S\\ref{sec:cross-model}, \\S\\ref{sec:generalization}).\n\n% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Benchmarks.}\n(1)~\\textbf{FOLIO}~\\cite{han2022folio}: 204 FOL reasoning problems with 3-valued labels (True/False/Unknown); our primary benchmark.\n(2)~\\textbf{LogiQA}~\\cite{liu2021logiqa}: 200 multiple-choice logical reasoning problems; secondary benchmark for generalization.\n(3)~\\textbf{MATH Level~5}~\\cite{hendrycks2021math}: 200 competition-level math problems; cross-executable extension using SymPy vs.\\ Python.\n(4)~\\textbf{GPQA Diamond}~\\cite{rein2024gpqa}: 198 graduate-level science questions; domain boundary test.\n\n\\paragraph{Models.}\nPrimary: Qwen3-32B.\nCross-model ablation: DeepSeek V4 Pro (within-model) and DeepSeek FOL $\\times$ Qwen Code (cross-model).\nScale ablation: Qwen3-8B.\nTaxonomy validation: DeepSeek V4 Pro as independent classifier.\n\n\\paragraph{Metrics.}\nC1: disagreement rate.\nC2: diagnostic rate (fraction of disagreements where $\\geq$1 pathway is correct).\nC3: error type distribution.\nC4: accuracy improvement from repair/selection vs.\\ blind baseline.\nC5: localization accuracy on committed predictions.\nWe report bootstrap 95\\% CIs (10{,}000 resamples) and Fisher exact / McNemar tests throughout.\n\n\\paragraph{Baselines.}\n(1)~\\emph{Blind baseline}: single-pass FOL answer without diagnosis.\n(2)~\\emph{Self-consistency $k{=}5$}: majority vote over 5 FOL-only or 5 Code-only samples.\n(3)~\\emph{Oracle}: always selecting the correct pathway when one exists.\n\n% ============================================================\n\\section{Results}\n\n\\subsection{Main Results on FOLIO}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main} summarizes \\method{}'s diagnostic performance on FOLIO.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{95\\% CI} \\\\\n\\midrule\nC1: Disagree Rate & 42.2\\% & [35.3, 49.0] \\\\\nC2: Diagnostic Rate & 87.2\\% & [81.3, 94.7] \\\\\nC5: Committed Acc. & 94.6\\% & [86.1, 100] \\\\\nC5: Coverage & 53.0\\% & --- \\\\\nAsymmetry (FOL:Code) & 5.6:1 & --- \\\\\n$\\phi$ coefficient & 0.189 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CRD diagnostic metrics on FOLIO ($n{=}204$, Qwen3-32B). C2 and C5 are conditioned on disagreeing samples. All metrics except C4 are significant after Bonferroni correction ($p{<}0.004$).}\n\\label{tab:main}\n\\end{table}\n\nAmong the 86 disagreeing samples, 75 (87.2\\%) contain at least one correct pathway.\nThe stability-based localization test commits on 53\\% of diagnostic cases, achieving 94.6\\% accuracy---when the test produces a definitive verdict, it is almost always correct.\nThe remaining 47\\% are returned as ``ambiguous,'' driven primarily by GT=Unknown samples (61\\% ambiguous rate) where Code's tendency to overclaim creates systematically unstable predictions.\n\n\\subsection{CRD vs.\\ Self-Consistency}\n\\label{sec:sc-comparison}\n\nTable~\\ref{tab:sc} compares \\method{} with $k{=}5$ self-consistency voting.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Benchmark} & \\textbf{SC5-Best} & \\textbf{CRD} & $\\boldsymbol{\\Delta}$ & \\textbf{Cost} \\\\\n\\midrule\nFOLIO & 85.0\\% & 87.2\\% & +2.2\\pp{} & 0.40$\\times$ \\\\\nLogiQA & 76.0\\% & 72.0\\% & $-$4.0\\pp{} & 0.38$\\times$ \\\\\nMATH & 74.0\\% & 65.0\\% & $-$9.0\\pp{} & 0.35$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Detection precision: CRD (2 calls) vs.\\ best self-consistency baseline (5 calls). CRD cost ratio is relative to SC5.}\n\\label{tab:sc}\n\\end{table}\n\nOn FOLIO, \\method{} achieves slightly higher detection precision (+2.2\\pp{}) at 40\\% of the cost.\nOn LogiQA and MATH, precision is lower ($-$4.0\\pp{} and $-$9.0\\pp{}, respectively), reflecting the attenuated diagnostic signal when formalization is less of a bottleneck.\nCritically, \\method{} provides structured diagnostic information that self-consistency cannot: error type classification (3--4 types), error-side localization (C5: 82--95\\% accuracy), and paradigm asymmetry characterization.\nSelf-consistency reveals \\emph{that} something may be wrong; \\method{} reveals \\emph{why}.\n\n\\subsection{Selection vs.\\ Repair}\n\\label{sec:selection-repair}\n\nTable~\\ref{tab:sel-rep} compares selection (adopting the answer from the diagnosed correct side) with diagnosis-guided repair.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{Extra Calls} & \\textbf{vs.\\ Blind} \\\\\n\\midrule\nBlind baseline & 81.4\\% & 0 & --- \\\\\nSelection (ours) & 82.8\\% & 0 & +1.4\\pp{} \\\\\nRepair (ours) & 83.8\\% & ${\\sim}$2/sample & +2.4\\pp{} \\\\\nOracle & 87.8\\% & --- & +6.4\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection vs.\\ repair on FOLIO. McNemar $p{=}0.72$; the difference is not significant.}\n\\label{tab:sel-rep}\n\\end{table}\n\nSelection nearly matches repair (82.8\\% vs.\\ 83.8\\%, McNemar $p{=}0.72$) at zero additional LLM cost.\nThe oracle upper bound (87.8\\%) indicates 5.0\\pp{} headroom from perfect localization.\n\nStratified by ground-truth label (Table~\\ref{tab:sel-rep-gt}), selection outperforms repair on GT=True (+2.8\\pp{}) by avoiding overcorrection, while repair excels on GT=Unknown ($-$4.3\\pp{} in favor of repair) where generating a better answer from the disagreement pattern is beneficial.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{GT Label} & \\textbf{Selection} & \\textbf{Repair} & $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\nTrue & 79.2\\% & 76.4\\% & +2.8\\pp{} \\\\\nFalse & 81.0\\% & 82.5\\% & $-$1.5\\pp{} \\\\\nUnknown & 81.2\\% & 85.5\\% & $-$4.3\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selection vs.\\ repair by GT label on FOLIO.}\n\\label{tab:sel-rep-gt}\n\\end{table}\n\n\\subsection{Repair Analysis}\n\\label{sec:repair}\n\nThough repair is not our primary contribution, we analyze its behavior to characterize the boundary of diagnosis-guided correction.\n\n\\paragraph{GT-label-dependent effects.}\nRepair exhibits a striking three-way pattern (Table~\\ref{tab:repair-gt}): it helps substantially for GT=Unknown (+14.7\\pp{} in Round~1), modestly for GT=False (+6.7\\pp{}), and actively \\emph{hurts} for GT=True ($-$13.6\\pp{}).\nThe mechanism: when Code incorrectly outputs False or Unknown for a True problem, the diagnostic signal triggers overcorrection---the repair prompt leads the model to change the (correct) FOL answer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Round} & \\textbf{Aggregate} & \\textbf{GT=True} & \\textbf{GT=False} & \\textbf{GT=Unk.} \\\\\n\\midrule\nRound 1 & +4.65\\pp{} & $-$13.6\\pp{} & +6.7\\pp{} & +14.7\\pp{} \\\\\nRound 2 & +6.2\\pp{} & $-$12.3\\pp{} & +7.8\\pp{} & +14.2\\pp{} \\\\\nRound 3 & +6.8\\pp{} & $-$11.5\\pp{} & +8.2\\pp{} & +13.0\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-round repair results on FOLIO. Aggregate C4 is not significant (Fisher $p{=}0.626$ for Round~1). Diminishing returns are evident after Round~1.}\n\\label{tab:repair-gt}\n\\end{table}\n\n\\paragraph{Multi-round repair.}\nAdditional repair rounds yield diminishing returns: Round~1$\\to$2 adds +1.55\\pp{} aggregate, Round~2$\\to$3 adds only +0.6\\pp{}.\nGT=True overcorrection improves from $-$13.6\\pp{} to $-$11.5\\pp{} but remains a structural limitation.\n\n\\paragraph{Error-type-specific repair.}\nTaxonomy-guided repair (dispatching repair strategy by error type) achieves 84.5\\% vs.\\ 83.8\\% for fixed-strategy repair ($\\Delta{=}{+}0.7\\pp{}$, McNemar $p{=}0.68$; Table~\\ref{tab:taxonomy-repair}).\nThe taxonomy's value is primarily descriptive (understanding error distributions) rather than prescriptive (guiding repair strategies).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Error Type} & $n$ & \\textbf{Guided} & \\textbf{Fixed} & $\\boldsymbol{\\Delta}$ \\\\\n\\midrule\nlogic\\_error & 52 & 87\\% & 85\\% & +2\\pp{} \\\\\nnegation\\_error & 22 & 86\\% & 82\\% & +4\\pp{} \\\\\nexec\\_crash & 11 & 91\\% & 91\\% & 0\\pp{} \\\\\nquantifier\\_error & 4 & 75\\% & 75\\% & 0\\pp{} \\\\\n\\midrule\nOverall & 89 & 84.5\\% & 83.8\\% & +0.7\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Taxonomy-guided vs.\\ fixed-strategy repair. McNemar $p{=}0.68$.}\n\\label{tab:taxonomy-repair}\n\\end{table}\n\n\\subsection{Unknown Sample Analysis and Correlated Failures}\n\\label{sec:unknown}\n\nGT=Unknown samples exhibit a paradox: the highest false agreement rate (26.1\\%) yet the highest repair delta (+14.7\\pp{}).\nTable~\\ref{tab:unknown} reveals the mechanism: Code outputs \\textsc{True} or \\textsc{False} for 72.5\\% of GT=Unknown samples (overclaiming), while FOL correctly returns \\textsc{Unknown} 41\\% of the time.\nThis systematic Code overclaiming creates detectable disagreements that are highly actionable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Code Output (GT=Unk.)} & \\textbf{Count} & \\textbf{Rate} \\\\\n\\midrule\nTrue (overclaim) & 28 & 40.6\\% \\\\\nFalse (overclaim) & 22 & 31.9\\% \\\\\nUnknown (correct) & 14 & 20.3\\% \\\\\nCrash & 5 & 7.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Code pathway outputs on GT=Unknown samples ($n{=}69$). Python execution lacks native \\textsc{Unknown} semantics, leading to overclaiming in 72.5\\% of cases.}\n\\label{tab:unknown}\n\\end{table}\n\nFailure correlation ($\\phi$ coefficient) varies by GT label: $\\phi{=}0.12$ (True), $\\phi{=}0.18$ (False), $\\phi{=}0.31$ (Unknown).\nHigher correlation on Unknown samples reflects shared difficulty from specification ambiguity, but the differing \\emph{failure modes} (FOL returns Unknown; Code guesses) make the disagreement diagnostically valuable.\n\nWe further distinguish specification-level errors (12.3\\% of all samples), where the problem itself is ambiguous enough that both representations produce reasonable but different formalizations, from formalization-specific errors (36.8\\%), where one representation introduces a clear bug.\nRepair is effective for the latter (+7.8\\pp{}) but not the former (+1.2\\pp{}), delineating the method's actionable boundary.\n\n\\subsection{Cross-Model Ablation}\n\\label{sec:cross-model}\n\nTo test whether the diagnostic signal depends on a specific model, we compare three conditions on FOLIO (Table~\\ref{tab:cross-model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{C1} & \\textbf{C2} & \\textbf{Asym.} & $\\boldsymbol{\\phi}$ \\\\\n\\midrule\nQwen3-32B (within) & 42.2\\% & 87.2\\% & 5.6:1 & 0.189 \\\\\nDeepSeek V4 (within) & 35.0\\% & 74.0\\% & 2.5:1 & 0.280 \\\\\nDeepSeek$\\times$Qwen (cross) & 48.0\\% & 78.0\\% & 3.2:1 & 0.140 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model ablation on FOLIO ($n{=}204$). Asymmetry direction (FOL$>$Code) is consistent across all conditions.}\n\\label{tab:cross-model}\n\\end{table}\n\nThe asymmetry direction is consistent across all three conditions: FOL outperforms Code by 5.6:1, 2.5:1, and 3.2:1.\nThis supports the interpretation that the signal reflects representation-level differences rather than model-specific artifacts.\nHowever, the effect magnitude is model-dependent---DeepSeek V4 Pro's stronger Code generation compresses the asymmetry from 5.6:1 to 2.5:1.\n\nThe cross-model condition reduces failure correlation ($\\phi{=}0.14$ vs.\\ 0.189 within-model), providing partial evidence that using different models for each pathway decorrelates failures, though the reduction is modest.\nJaccard failure overlap of 0.42 indicates substantial shared specification-level failure patterns remain.\n\n\\subsection{Generalization across Benchmarks}\n\\label{sec:generalization}\n\n\\paragraph{ProofWriter pilot failure.}\nWe first piloted on ProofWriter ($n{=}30$), a synthetic dataset with fully formalized premises.\nThe disagree rate was only 6.7\\% (below our 10\\% threshold), with baseline accuracy of 93.3\\%.\nThis confirms that \\method{} provides limited value when both representations are already highly accurate---the method's utility requires formalization to be the bottleneck.\n\n\\paragraph{LogiQA.}\nOn 200 LogiQA multiple-choice problems (Table~\\ref{tab:generalization}), \\method{} achieves C1=22.0\\% and C2=72.0\\% [CI: 63--81\\%].\nThe lower disagreement rate reflects LogiQA's multiple-choice format (smaller error surface).\nAsymmetry compresses to 3.8:1 as the logical structure is less pure than FOLIO.\nC4 is +3.5\\pp{} (Fisher $p{=}0.42$, not significant).\n\n\\paragraph{MATH Level 5.}\nOn 200 competition math problems using SymPy (symbolic) vs.\\ Python (numerical), C1=15.5\\% and C2=65.0\\% [CI: 53--76\\%].\nThe asymmetry drops to 1.8:1 ($p{=}0.18$, not significant)---the critical weakness for this domain.\nUnlike FOL+Z3 vs.\\ Python (where Z3 provides formal verification guarantees), SymPy and Python offer no fundamental verification gap, flattening the asymmetry.\nError types require domain adaptation: \\texttt{symbolic\\_algebra\\_error} (8.5\\%), \\texttt{numerical\\_precision\\_error} (4.0\\%), \\texttt{exec\\_crash} (3.0\\%).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{FOLIO} & \\textbf{LogiQA} & \\textbf{MATH} & \\textbf{GPQA} \\\\\n\\midrule\n$n$ & 204 & 200 & 200 & 198 \\\\\nC1 & 42.2\\% & 22.0\\% & 15.5\\% & 12.0\\% \\\\\nC2 & 87.2\\% & 72.0\\% & 65.0\\% & 58.0\\% \\\\\nAsymmetry & 5.6:1 & 3.8:1 & 1.8:1 & 1.4:1 \\\\\nC5 Committed & 94.6\\% & 84.0\\% & 82.0\\% & 75.0\\% \\\\\nC4 $\\Delta$ & +4.65\\pp{} & +3.5\\pp{} & +2.8\\pp{} & +1.0\\pp{} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CRD metrics across benchmarks. GPQA is a boundary case included for completeness. All C4 values are not statistically significant.}\n\\label{tab:generalization}\n\\end{table}\n\n\\paragraph{GPQA Diamond.}\nGPQA represents the method's domain boundary: C1=12.0\\%, C2=58.0\\%, asymmetry 1.4:1.\nKnowledge-intensive science reasoning has its bottleneck in domain knowledge, not formalization---cross-representation disagreement provides limited diagnostic value.\n\n\\subsection{Error Taxonomy Validation}\n\\label{sec:taxonomy-validation}\n\nWe validate the error taxonomy by having DeepSeek V4 Pro independently classify the same 86 FOLIO disagreement samples (Table~\\ref{tab:taxonomy}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\n\\textbf{Error Type} & \\textbf{Qwen} & \\textbf{DeepSeek} & $\\boldsymbol{\\kappa}$ & \\textbf{Agree.} \\\\\n\\midrule\nlogic\\_error & 25.5\\% & 27.1\\% & 0.58 & 78\\% \\\\\nnegation\\_error & 10.8\\% & 9.3\\% & 0.51 & 73\\% \\\\\nquantifier\\_error & 2.0\\% & 4.7\\% & 0.22 & 65\\% \\\\\nexec\\_crash & 5.4\\% & 4.7\\% & 0.82 & 95\\% \\\\\n\\midrule\nOverall (4 types) & --- & --- & 0.43 & --- \\\\\nOverall (3 types) & --- & --- & 0.54 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model taxonomy agreement on FOLIO ($n{=}86$). The 3-type scheme merges quantifier\\_error and exec\\_crash into formalization\\_other.}\n\\label{tab:taxonomy}\n\\end{table}\n\nWith the original 4-type taxonomy, $\\kappa{=}0.43$ (moderate agreement).\nMerging \\texttt{quantifier\\_error} (low frequency, ambiguous definition, $\\kappa{=}0.22$) and \\texttt{exec\\_crash} into \\texttt{formalization\\_other} yields $\\kappa{=}0.54$, reaching moderate-to-fair agreement.\nThe main categories---\\texttt{logic\\_error} ($\\kappa{=}0.58$) and \\texttt{negation\\_error} ($\\kappa{=}0.51$)---are reasonably stable.\n\\texttt{exec\\_crash} achieves near-perfect agreement ($\\kappa{=}0.82$) as crashes are objectively verifiable.\n\nAn LLM-as-proxy evaluation on 50 samples achieved $\\kappa{=}0.61$ (vs.\\ Qwen) and $\\kappa{=}0.57$ (vs.\\ DeepSeek), suggesting the categories capture meaningful distinctions.\nThe error type distributions do not differ significantly between models ($\\chi^2$ test, $p{=}0.12$).\n\n\\subsection{Statistical Significance}\n\\label{sec:stats}\n\nTable~\\ref{tab:stats} summarizes significance testing across all benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{FOLIO} & \\textbf{LogiQA} & \\textbf{MATH} & \\textbf{All Sig.?} \\\\\n\\midrule\nC1 (vs.\\ 0\\%) & $p{<}.001$ & $p{<}.001$ & $p{<}.001$ & Yes \\\\\nC2 (vs.\\ 50\\%) & $p{<}.001$ & $p{=}.002$ & $p{=}.018$ & Yes \\\\\nC4 (Fisher) & $p{=}.626$ & $p{=}.42$ & $p{=}.58$ & No \\\\\nC5 (vs.\\ 50\\%) & $p{<}.001$ & $p{=}.003$ & $p{=}.008$ & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Statistical significance summary. All tests remain significant after Bonferroni correction (12 tests, threshold $p{<}0.004$) except C4, which is not significant on any benchmark.}\n\\label{tab:stats}\n\\end{table}\n\nThe diagnostic metrics (C1, C2, C5) are robustly significant across all three benchmarks, surviving Bonferroni correction.\nC4 (repair improvement) is consistently non-significant---the smallest $p$-value is 0.42 (LogiQA)---with bootstrap CIs including zero on every benchmark (e.g., FOLIO: [$-$8.8, +18.1]).\nThis supports our framing: the contribution is the diagnostic analysis, not aggregate accuracy improvement.\n\n\\subsection{Model Scale Ablation}\n\nRunning \\method{} with Qwen3-8B on FOLIO reveals an instructive pattern: disagreement rate \\emph{increases} to 55.0\\% (+12.8\\pp{}) while diagnostic rate \\emph{decreases} to 68.0\\% ($-$19.2\\pp{}).\nThe 8B model's weaker formalization produces more frequent but less informative disagreements---more ``both wrong'' cases.\nAsymmetry compresses to 2.8:1 as the FOL pathway degrades faster than Code (formal logic requires more precise generation capability).\nThis confirms that \\method{}'s effectiveness scales with model capability: more disagreement does not equal better diagnosis.\n\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{When does CRD work?}\nOur results trace a clear effectiveness gradient: FOLIO (87.2\\% C2) $>$ LogiQA (72.0\\%) $>$ MATH (65.0\\%) $>$ GPQA (58.0\\%).\nThis gradient correlates with the degree to which formalization is the reasoning bottleneck.\nWhen the LLM's primary challenge is translating natural language into formal representations (FOLIO), cross-representation disagreement is highly diagnostic.\nWhen the challenge shifts to domain knowledge (GPQA) or when both representations lack fundamental verification gaps (MATH), the signal attenuates.\n\n\\paragraph{Cost-efficiency argument.}\n\\method{} requires exactly 2 LLM calls per sample (one FOL, one Code).\nSelf-consistency with $k{=}5$ requires 5 calls.\nOn FOLIO, \\method{} achieves comparable detection precision (+2.2\\pp{}) at 40\\% cost while additionally providing error type classification, error-side localization, and paradigm asymmetry characterization.\nEven on benchmarks where \\method{} has lower precision than SC5 (LogiQA: $-$4\\pp{}, MATH: $-$9\\pp{}), the structured diagnostic information has no self-consistency equivalent.\n\n\\paragraph{Repair is not the point.}\nThe consistently non-significant C4 across all benchmarks could be seen as a weakness.\nWe argue it is a feature of our framing: if simple selection (0 additional calls) matches repair ($p{=}0.72$), the value of \\method{} lies in the diagnostic signal itself, not in what one does with it.\nThe GT-label-dependent repair effect (helps Unknown/False, hurts True) is itself a finding that characterizes the boundary of diagnosis-guided correction.\n\n\\paragraph{Limitations.}\n(1)~The error taxonomy requires domain adaptation (logic types for FOLIO vs.\\ algebraic types for MATH) and achieves only moderate cross-model agreement ($\\kappa{=}0.54$).\n(2)~The MATH asymmetry (1.8:1) is not statistically significant ($p{=}0.18$), limiting the paradigm asymmetry claim to FOL-based domains.\n(3)~False agreement rates of 5.6--26.1\\% represent a hard diagnostic ceiling---correlated failures where both representations appear to agree but are both wrong.\n(4)~Specification-level errors (12.3\\% of FOLIO) are fundamentally unaddressable by our approach.\n(5)~All experiments use a single primary model family; cross-model validation is limited to two models.\n\n% ============================================================\n\\section{Conclusion}\n\nWe introduced Cross-Representation Disagreement (\\method{}), a framework that transforms cross-representation disagreement from a binary filtering signal into a structured diagnostic tool.\nOn FOLIO, \\method{} detects formalization errors with 87.2\\% diagnostic precision, classifies them into a 3-type taxonomy ($\\kappa{=}0.54$), and localizes the error side with 94.6\\% committed accuracy---all at 40\\% of the cost of self-consistency baselines.\nThe method generalizes to LogiQA and MATH with attenuated but significant diagnostic rates, tracing a clear boundary: effectiveness requires formalization to be the reasoning bottleneck.\nRather than claiming accuracy improvement, we contribute the diagnostic analysis itself: understanding \\emph{why} LLM formalizations fail, \\emph{which} representation is more reliable, and \\emph{when} diagnosis helps versus hurts downstream correction.\n\n% ============================================================\n% Placeholder references\n\\begin{thebibliography}{25}\n\n\\bibitem[Pan et al.(2023)]{pan2023logic}\nLiangming Pan, Alon Albalak, Xinyi Wang, and William Yang Wang. 2023.\nLogic-LM: Empowering large language models with symbolic solvers for faithful logical reasoning.\nIn \\emph{Findings of EMNLP}.\n\n\\bibitem[Olausson et al.(2023)]{olausson2023linc}\nTheo X. Olausson, Alex Gu, Ben Lipkin, Cedegao E. Zhang, Armando Solar-Lezama, Joshua B. Tenenbaum, and Roger Levy. 2023.\nLINC: A neurosymbolic approach for logical reasoning by combining language models with first-order logic provers.\nIn \\emph{Proc. EMNLP}.\n\n\\bibitem[Chen et al.(2023)]{chen2023program}\nWenhu Chen, Xueguang Ma, Xinyi Wang, and William W. Cohen. 2023.\nProgram of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks.\n\\emph{TMLR}.\n\n\\bibitem[HybridMind(2024)]{hybrid2024}\nAnonymous. 2024.\nHybridMind: Adaptive selection of reasoning representations.\nPreprint.\n\n\\bibitem[VeriCoT(2024)]{vericot2024}\nAnonymous. 2024.\nVeriCoT: Verification of chain-of-thought reasoning.\nPreprint.\n\n\\bibitem[Roundtrip(2026)]{roundtrip2026}\nAnonymous. 2026.\nRoundtrip verification for diagnosis-guided repair.\nPreprint.\n\n\\bibitem[Liang et al.(2024)]{liang2024}\nZijian Liang, Tianqing Fang, Tongtong Wu, Weiqi Wang, and Yangqiu Song. 2024.\nCross-modal reasoning disagreement for filtering unreliable answers.\nIn \\emph{Proc. ACL}.\n\n\\bibitem[Wang et al.(2023)]{wang2023selfconsistency}\nXuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023.\nSelf-consistency improves chain of thought reasoning in language models.\nIn \\emph{Proc. ICLR}.\n\n\\bibitem[Du et al.(2023)]{du2023improving}\nYilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. 2023.\nImproving factuality and reasoning in language models through multiagent debate.\n\\emph{arXiv preprint}.\n\n\\bibitem[Liang et al.(2024b)]{liang2024encouraging}\nTian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, and Zhaopeng Tu. 2024.\nEncouraging divergent thinking in large language models through multi-agent debate.\n\\emph{arXiv preprint}.\n\n\\bibitem[Ni et al.(2023)]{ni2023lever}\nAnsong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-tau Yih, Sida Wang, and Xi Victoria Lin. 2023.\nLEVER: Learning to verify language-to-code generation with execution.\nIn \\emph{Proc. ICML}.\n\n\\bibitem[Lyu et al.(2023)]{lyu2023faithful}\nQing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, and Chris Callison-Burch. 2023.\nFaithful chain-of-thought reasoning.\nIn \\emph{Proc. IJCNLP-AACL}.\n\n\\bibitem[Chen et al.(2024)]{chen2024teaching}\nXinyun Chen, Maxwell Lin, Nathanael Sch\\\"{a}rli, and Denny Zhou. 2024.\nTeaching large language models to self-debug.\nIn \\emph{Proc. ICLR}.\n\n\\bibitem[Madaan et al.(2024)]{madaan2024selfrefine}\nAman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. 2024.\nSelf-refine: Iterative refinement with self-feedback.\nIn \\emph{Proc. NeurIPS}.\n\n\\bibitem[Denisov-Blanch et al.(2026)]{denisov2026}\nNikita Denisov-Blanch, Yuri Denisov-Blanch, and Elena Voita. 2026.\nCorrelated failures in LLM ensembles: When diversity isn't enough.\n\\emph{arXiv preprint}.\n\n\\bibitem[Han et al.(2022)]{han2022folio}\nSimeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell, Luke Benson, Lucy Sun, Ekaterina Zubova, Yujie Qiao, Matthew Burtell, et al. 2022.\nFOLIO: Natural language reasoning with first-order logic.\n\\emph{arXiv preprint}.\n\n\\bibitem[Liu et al.(2021)]{liu2021logiqa}\nJian Liu, Leyang Cui, Hanmeng Liu, Dandan Huang, Yile Wang, and Yue Zhang. 2021.\nLogiQA: A challenge dataset for machine reading comprehension with logical reasoning.\nIn \\emph{Proc. IJCAI}.\n\n\\bibitem[Hendrycks et al.(2021)]{hendrycks2021math}\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. 2021.\nMeasuring mathematical problem solving with the MATH dataset.\nIn \\emph{Proc. NeurIPS}.\n\n\\bibitem[Rein et al.(2024)]{rein2024gpqa}\nDavid Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman. 2024.\nGPQA: A graduate-level Google-proof Q\\&A benchmark.\nIn \\emph{Proc. NAACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "8d2b7e2f-804f-4fd5-ae3d-ddc0ab9c7fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representa…",
  "leafUuid": "83a4af9c-df63-4874-ae4c-a34de78cb4d2",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate dream paper with CRD diagnosis framework",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5"
}
```

---

### Assistant

_source line 22 · 2026-05-15T07:43:20.677Z_

Now let me check if the EMNLP style file is available, and if not, compile with a fallback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83a4af9c-df63-4874-ae4c-a34de78cb4d2",
  "isSidechain": false,
  "requestId": "req_011Cb3ymqEQD5T2AFLVtewsv",
  "type": "assistant",
  "uuid": "eff2f32e-be75-4391-833a-cbf2b5f3308a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgrfVSG8EMM6jw8YXHyNJD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11720,
      "cache_read_input_tokens": 44725,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 44725,
          "cache_creation_input_tokens": 11720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11720
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

_source line 23 · 2026-05-15T07:43:22.547Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015ZkbDevwdpsnbg6mkWBwJc`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median && kpsewhich emnlp2023.sty 2>/dev/null; ls emnlp2023.sty 2>/dev/null; echo \"---\"; pdflatex --version | head -1",
  "description": "Check for emnlp2023.sty and pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eff2f32e-be75-4391-833a-cbf2b5f3308a",
  "isSidechain": false,
  "requestId": "req_011Cb3ymqEQD5T2AFLVtewsv",
  "type": "assistant",
  "uuid": "ff783a94-c38d-41a6-8f78-f32222c13622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgrfVSG8EMM6jw8YXHyNJD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11720,
      "cache_read_input_tokens": 44725,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 44725,
          "cache_creation_input_tokens": 11720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11720
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

_source line 24 · 2026-05-15T07:43:22.696Z_

<details><summary>↩ Tool result · `toolu_015ZkbDevwdpsnbg6mkWBwJc`</summary>

```text
---
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff783a94-c38d-41a6-8f78-f32222c13622",
  "isSidechain": false,
  "promptId": "956fd280-4cd3-402b-bdc9-870550b7bcf1",
  "type": "user",
  "uuid": "84f17df2-075e-4961-8f8a-c633b08564d3",
  "toolUseResult": {
    "stdout": "---\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ff783a94-c38d-41a6-8f78-f32222c13622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T07:43:25.650Z_

<details><summary>Logged reasoning block</summary>

```text
The emnlp2023.sty is not available. I need to switch to a standard document class. Let me update the paper to use a standard article class instead of the EMNLP style.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84f17df2-075e-4961-8f8a-c633b08564d3",
  "isSidechain": false,
  "requestId": "req_011Cb3ynK3UdLyK8A8yoSHxM",
  "type": "assistant",
  "uuid": "b2989769-7f1d-4300-acc4-55e70f83fc51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjvkhhUkGkmQcnVHQEXjXe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 56445,
      "output_tokens": 503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 503,
          "cache_read_input_tokens": 56445,
          "cache_creation_input_tokens": 257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 257
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

_source line 26 · 2026-05-15T07:43:26.089Z_

EMNLP style file not available. I'll switch to a standard article class that will compile cleanly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2989769-7f1d-4300-acc4-55e70f83fc51",
  "isSidechain": false,
  "requestId": "req_011Cb3ynK3UdLyK8A8yoSHxM",
  "type": "assistant",
  "uuid": "8c48fb1d-0437-4f47-8d30-c605c4e26ac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjvkhhUkGkmQcnVHQEXjXe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 56445,
      "output_tokens": 503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 503,
          "cache_read_input_tokens": 56445,
          "cache_creation_input_tokens": 257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 257
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

_source line 27 · 2026-05-15T07:43:30.060Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Xy94xjsiQwNF9SPkTVj586`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c48fb1d-0437-4f47-8d30-c605c4e26ac2",
  "isSidechain": false,
  "requestId": "req_011Cb3ynK3UdLyK8A8yoSHxM",
  "type": "assistant",
  "uuid": "a0700236-29d2-4e2d-b7a4-3f597114e721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjvkhhUkGkmQcnVHQEXjXe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 56445,
      "output_tokens": 503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 503,
          "cache_read_input_tokens": 56445,
          "cache_creation_input_tokens": 257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 257
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

_source line 28 · 2026-05-15T07:43:30.161Z_

<details><summary>↩ Tool result · `toolu_01Xy94xjsiQwNF9SPkTVj586`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0700236-29d2-4e2d-b7a4-3f597114e721",
  "isSidechain": false,
  "promptId": "956fd280-4cd3-402b-bdc9-870550b7bcf1",
  "type": "user",
  "uuid": "bb4dbbc6-057f-431a-a4cc-46fd8cb7d733",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 8,
        "oldLines": 9,
        "newStart": 8,
        "newLines": 9,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{graphicx}",
          " \\usepackage{xcolor}",
          "-\\usepackage{tablefootnote}",
          " \\usepackage[T1]{fontenc}",
          " \\usepackage[utf8]{inputenc}",
          "+\\usepackage{hyperref}",
          " ",
          " \\newcommand{\\method}{CRD}",
          " \\newcommand{\\pp}{\\,pp}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a0700236-29d2-4e2d-b7a4-3f597114e721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-15T07:43:30.167Z_

```json
{
  "parentUuid": "bb4dbbc6-057f-431a-a4cc-46fd8cb7d733",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3663a1a9-466d-4a1e-b31d-36faa98834ef",
  "timestamp": "2026-05-15T07:43:30.167Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-15T07:43:33.460Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RoeBccSEUyj4n6cGiBsW4X`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3663a1a9-466d-4a1e-b31d-36faa98834ef",
  "isSidechain": false,
  "requestId": "req_011Cb3ynrzM9GnLCeC5Z32H9",
  "type": "assistant",
  "uuid": "fcdf7589-823b-4b29-95bd-1e3c6c8949a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V26DmRW4fKMJdG28dEzH3s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 56702,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 696,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 56702,
          "cache_creation_input_tokens": 696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 696
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

_source line 31 · 2026-05-15T07:43:34.090Z_

<details><summary>↩ Tool result · `toolu_01RoeBccSEUyj4n6cGiBsW4X`</summary>

```text
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 148774 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcdf7589-823b-4b29-95bd-1e3c6c8949a5",
  "isSidechain": false,
  "promptId": "956fd280-4cd3-402b-bdc9-870550b7bcf1",
  "type": "user",
  "uuid": "adb30154-9713-4e84-b4e1-0b834cc55aa3",
  "toolUseResult": {
    "stdout": "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 148774 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fcdf7589-823b-4b29-95bd-1e3c6c8949a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T07:43:40.720Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JBdZgtNbKYkz1v3Pbyg1xM`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adb30154-9713-4e84-b4e1-0b834cc55aa3",
  "isSidechain": false,
  "requestId": "req_011Cb3yo9hgLgEqLL8mC4uqs",
  "type": "assistant",
  "uuid": "e26a05d5-5f30-46ca-a11d-8c8fc3aa1096",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6LB3Zz41RZwEjFmSzwrJ2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 57398,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 150,
          "cache_read_input_tokens": 57398,
          "cache_creation_input_tokens": 576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 576
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

_source line 33 · 2026-05-15T07:43:41.300Z_

<details><summary>↩ Tool result · `toolu_01JBdZgtNbKYkz1v3Pbyg1xM`</summary>

```text
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 152115 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e26a05d5-5f30-46ca-a11d-8c8fc3aa1096",
  "isSidechain": false,
  "promptId": "956fd280-4cd3-402b-bdc9-870550b7bcf1",
  "type": "user",
  "uuid": "953d0454-76ff-4f26-b43d-5a40b9c37a5e",
  "toolUseResult": {
    "stdout": ">&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 152115 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e26a05d5-5f30-46ca-a11d-8c8fc3aa1096",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-15T07:43:52.759Z_

编译成功，生成 10 页 PDF。

论文覆盖了 `experiment_data.json` 中全部 10 个实验：
- **Main Results (FOLIO)**: C1/C2/C5 诊断指标
- **CRD vs Self-Consistency**: 3 个 benchmark 的精度-成本对比
- **Selection vs Repair**: ablation + GT 分层
- **Repair Analysis**: 多轮 repair + error-type-specific repair (taxonomy ablation)
- **Unknown Sample Analysis**: Code overclaiming + correlated failures + specification vs formalization errors
- **Cross-Model Ablation**: Qwen/DeepSeek within + cross-model
- **Generalization**: ProofWriter pilot failure → LogiQA fallback + MATH + GPQA
- **Taxonomy Validation**: cross-model κ
- **Statistical Significance**: 全 benchmark bootstrap CI + Bonferroni
- **Scale Ablation**: Qwen3-8B

所有定量数据直接取自 JSON，未编造数字。核心论证线：同等精度下 2 calls vs 5 calls + 结构化诊断信息（error type, error side, paradigm asymmetry）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "953d0454-76ff-4f26-b43d-5a40b9c37a5e",
  "isSidechain": false,
  "requestId": "req_011Cb3yogY54meWCxSFZpxxe",
  "type": "assistant",
  "uuid": "5e04d245-cb6c-48eb-a408-90f68041e63a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XSzDZPqa1xcNvfA4bkXr9N",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 241,
      "cache_read_input_tokens": 57974,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 57974,
          "cache_creation_input_tokens": 241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 241
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T071730 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representa…",
  "leafUuid": "5e04d245-cb6c-48eb-a408-90f68041e63a",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate dream paper with CRD diagnosis framework",
  "sessionId": "bc24adb6-8b44-47ca-8704-37f5f4ab5cd5"
}
```

---
