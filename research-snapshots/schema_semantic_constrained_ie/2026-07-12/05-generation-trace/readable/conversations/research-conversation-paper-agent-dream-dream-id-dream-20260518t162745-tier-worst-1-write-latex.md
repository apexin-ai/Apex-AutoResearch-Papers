# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/59dbf90d-a03d-487e-aec5-135e784bb958.jsonl`
- **Structured JSON:** [`1278584654f45cf585ec.json`](../../sessions/12/1278584654f45cf585ec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T17:06:57.226Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T17:06:57.226Z",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：核心叙事需要从 \"method paper with empirical validation\" 重构为 \"empirical study with method validation\"。 三个 reframe 策略组合使用：(A) Violation Landscape 升级为论文主体贡献——70B 低违规反而是 positive finding （\"scale partially mitigates but task complexity determines violation severity — EE RoV 64-89% regardless of model size\"）；(B) prefix-decidability taxonomy formalize 为 theorem；(C) FT composability 作为 practical selling point（\"decoding-time type checking for neural generation\"）。 worst 档下审稿人平均分 2.75-3.25（Borderline Findings），核心攻击面：70B 近乎消除违规使方法动机被 削弱；novelty 仍被视为 incremental；CF 15-21% 在 EE 上被标记为 \"method introduces more problems than it solves\"。需要 rebuttal 期全面回应 + AC meta-review 争取 Findings 录用。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T17:06:57.229Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T17:06:57.229Z",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-18T17:06:57.249Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：核心叙事需要从 "method paper with empirical validation" 重构为 "empirical study with method validation"。 三个 reframe 策略组合使用：(A) Violation Landscape 升级为论文主体贡献——70B 低违规反而是 positive finding （"scale partially mitigates but task complexity determines violation severity — EE RoV 64-89% regardless of model size"）；(B) prefix-decidability taxonomy formalize 为 theorem；(C) FT composability 作为 practical selling point（"decoding-time type checking for neural generation"）。 worst 档下审稿人平均分 2.75-3.25（Borderline Findings），核心攻击面：70B 近乎消除违规使方法动机被 削弱；novelty 仍被视为 incremental；CF 15-21% 在 EE 上被标记为 "method introduces more problems than it solves"。需要 rebuttal 期全面回应 + AC meta-review 争取 Findings 录用。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b88248f5-45f7-484a-873c-8d439b996f3d",
  "type": "user",
  "uuid": "c6876ca1-b641-4a77-a5fd-aeadc08d21e3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T17:06:57.248Z_

```json
{
  "parentUuid": "c6876ca1-b641-4a77-a5fd-aeadc08d21e3",
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
  "uuid": "fceffcd8-fc82-49c6-9a03-1add2b46d1f0",
  "timestamp": "2026-05-18T17:06:57.248Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T17:06:57.248Z_

```json
{
  "parentUuid": "fceffcd8-fc82-49c6-9a03-1add2b46d1f0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3fadd1f4-04a4-48fb-89ed-3500bd864dc6",
  "timestamp": "2026-05-18T17:06:57.248Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
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
  "aiTitle": "Generate worst-tier empirical research paper on schema-constrained IE",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Assistant

_source line 7 · 2026-05-18T17:07:01.950Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fadd1f4-04a4-48fb-89ed-3500bd864dc6",
  "isSidechain": false,
  "requestId": "req_011CbAQBgLM8aiVZP29Vcm4T",
  "type": "assistant",
  "uuid": "5b5d5cc3-a398-4ed9-a08b-59e23a1097f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YG5TSvwezrRdDvPmJdgthm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12892,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12892
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

_source line 8 · 2026-05-18T17:07:02.421Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AnXVg28DmpevMDv3bAvWoP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b5d5cc3-a398-4ed9-a08b-59e23a1097f7",
  "isSidechain": false,
  "requestId": "req_011CbAQBgLM8aiVZP29Vcm4T",
  "type": "assistant",
  "uuid": "57177777-f8ca-4cbc-b661-7b448a99e09b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YG5TSvwezrRdDvPmJdgthm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12892,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12892
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

_source line 9 · 2026-05-18T17:07:02.830Z_

<details><summary>↩ Tool result · `toolu_01AnXVg28DmpevMDv3bAvWoP`</summary>

```text
1	[
2	  {
3	    "name": "70B SciERC unconstrained + constrained",
4	    "description": "Llama-3.1-70B-Instruct AWQ-INT4 on SciERC 551 docs。已完成，实际结果需在 worst tier 下解读。 实际结果：unconstrained DR=6.5%, constrained DR=0%, CF=3.66%。\n",
5	    "results": {
6	      "70b_scierc_uncon_DR_pct": 6.5,
7	      "70b_scierc_uncon_RV_pct": 0.6,
8	      "70b_scierc_uncon_ET_pct": 0,
9	      "70b_scierc_uncon_R_F1": 11.22,
10	      "70b_scierc_uncon_E_F1": 35.17,
11	      "70b_scierc_con_DR_pct": 0.0,
12	      "70b_scierc_con_RV_pct": 0.0,
13	      "70b_scierc_con_CF_pct": 3.66,
14	      "70b_scierc_con_R_F1": 11.24,
15	      "70b_scierc_con_E_F1": 35.14,
16	      "DR_reduction_pct": 100.0,
17	      "R_F1_delta_pp": 0.02,
18	      "E_F1_delta_pp": -0.03
19	    },
20	    "tables": [
21	      {
22	        "name": "Table: 70B SciERC Cross-Scale Comparison",
23	        "columns": [
24	          "Model",
25	          "Scale",
26	          "DR%↓",
27	          "RV%",
28	          "ET%",
29	          "CF%",
30	          "R-F1",
31	          "ΔR-F1"
32	        ],
33	        "rows": [
34	          [
35	            "Qwen3-8B",
36	            "8B",
37	            "15.37→0.93 (↓94%)",
38	            "1.39→0",
39	            "0.40→0",
40	            "0.08→9.90",
41	            "8.23→8.36",
42	            "+0.13"
43	          ],
44	          [
45	            "Llama-3.1-8B",
46	            "8B",
47	            "13.34→0.08 (↓99%)",
48	            "0.55→0",
49	            "0→0",
50	            "0.49→6.56",
51	            "2.68→2.54",
52	            "-0.14"
53	          ],
54	          [
55	            "Llama-3.1-70B",
56	            "70B",
57	            "6.50→0.00 (↓100%)",
58	            "0.60→0",
59	            "0→0",
60	            "0→3.66",
61	            "11.22→11.24",
62	            "+0.02"
63	          ]
64	        ]
65	      }
66	    ],
67	    "figures": [],
68	    "analysis": "worst tier 审稿人解读：SciERC unconstrained DR 从 8B 的 13-15% 降至 70B 的 6.5%， 自然 scaling 已削减 50-57%。OntoCoDec 将剩余 6.5%→0%（绝对 Δ=6.5pp）， 但审稿人可能认为 \"this remaining 6.5% would likely disappear at 405B or with better prompting\"。防线：指出 DR=6.5% 仍然意味着 97 个 triples 含有结构性违规， 下游 KG 不可用。但此防线在 DocRED 上会崩溃（见 P030）。\n\n\n70B SciERC 结果对 worst tier 叙事是双刃剑。一方面，unconstrained DR=6.5% 远低于 8B 的 15.4% （Qwen）和 13.3%（Llama-8B），证明 scale 确实大幅缓解违规。另一方面，6.5% 仍非零——7 个 relation type 中 constraint tightness 高的（Feature-of τ=0.143, Compare τ=0.194）在 70B 下 仍有残留违规。审稿人会抓住 \"6.5%→0% 在 SciERC 是有意义的\"，但随即质问 \"DocRED 呢？\"。 worst tier 下 SciERC 被视为 cherry-pick（小 ontology，tight constraints 人为放大违规率）， DocRED 才是 litmus test。CF=3.66% 比 8B（Qwen 9.9%）低但仍非零，审稿人认为 \"even at 70B scale, the method still introduces new violation types (CF)\"。 R_F1 delta +0.02pp 在 noise 范围内——无法声明 F1 improvement，只能声明 neutral。\n"
69	  },
70	  {
71	    "name": "70B DocRED unconstrained + constrained",
72	    "description": "Llama-3.1-70B-Instruct AWQ-INT4 on DocRED 998 docs。 8B baseline: Qwen DR=18.46%, Llama-8B DR=26.07%。 worst tier 预测 70B unconstrained DR 在 0.5-3.0% 之间，constrained 0-0.5%。\n",
73	    "results": {
74	      "70b_docred_uncon_DR_pct": 1.8,
75	      "70b_docred_uncon_RV_pct": 2.3,
76	      "70b_docred_uncon_ET_pct": 0.0,
77	      "70b_docred_uncon_CF_pct": 0.04,
78	      "70b_docred_uncon_parse_fail_rate": 2.1,
79	      "70b_docred_uncon_E_F1": 64.2,
80	      "70b_docred_uncon_E_P": 63.8,
81	      "70b_docred_uncon_E_R": 64.6,
82	      "70b_docred_uncon_R_F1": 10.1,
83	      "70b_docred_uncon_R_P": 8.6,
84	      "70b_docred_uncon_R_R": 12.3,
85	      "70b_docred_uncon_total_triples": 17200,
86	      "70b_docred_con_DR_pct": 0.3,
87	      "70b_docred_con_RV_pct": 0.0,
88	      "70b_docred_con_ET_pct": 0.0,
89	      "70b_docred_con_CF_pct": 3.8,
90	      "70b_docred_con_parse_fail_rate": 2.8,
91	      "70b_docred_con_E_F1": 64.0,
92	      "70b_docred_con_E_P": 63.5,
93	      "70b_docred_con_E_R": 64.5,
94	      "70b_docred_con_R_F1": 9.9,
95	      "70b_docred_con_R_P": 8.4,
96	      "70b_docred_con_R_R": 12.1,
97	      "70b_docred_DR_reduction_pct": 83.3,
98	      "70b_docred_R_F1_delta_pp": -0.2,
99	      "70b_docred_E_F1_delta_pp": -0.2,
100	      "70b_docred_absolute_DR_delta_pp": 1.5,
101	      "70b_docred_DR_eligible_triples_with_violations_uncon": "~265",
102	      "70b_docred_DR_eligible_triples_with_violations_con": "~44"
103	    },
104	    "tables": [
105	      {
106	        "name": "Table: 70B DocRED Cross-Scale DR Trajectory",
107	        "columns": [
108	          "Model",
109	          "Uncon DR%",
110	          "Con DR%",
111	          "Absolute Δ",
112	          "Relative ↓%",
113	          "ΔR-F1"
114	        ],
115	        "rows": [
116	          [
117	            "Qwen3-8B",
118	            "18.46",
119	            "10.21",
120	            "8.25pp",
121	            "44.7%",
122	            "+0.50"
123	          ],
124	          [
125	            "Llama-3.1-8B",
126	            "26.07",
127	            "2.55",
128	            "23.52pp",
129	            "90.2%",
130	            "+0.29"
131	          ],
132	          [
133	            "Llama-3.1-70B",
134	            "1.8",
135	            "0.3",
136	            "1.5pp",
137	            "83.3%",
138	            "-0.2"
139	          ]
140	        ]
141	      },
142	      {
143	        "name": "Table: 70B DocRED Full Violation Profile",
144	        "columns": [
145	          "Condition",
146	          "ET%",
147	          "RV%",
148	          "DR%",
149	          "CF%",
150	          "E-F1",
151	          "R-F1",
152	          "Parse%"
153	        ],
154	        "rows": [
155	          [
156	            "70B unconstrained",
157	            "0.0",
158	            "2.3",
159	            "1.8",
160	            "0.04",
161	            "64.2",
162	            "10.1",
163	            "97.9"
164	          ],
165	          [
166	            "70B constrained",
167	            "0.0",
168	            "0.0",
169	            "0.3",
170	            "3.8",
171	            "64.0",
172	            "9.9",
173	            "97.2"
174	          ]
175	        ]
176	      }
177	    ],
178	    "figures": [],
179	    "analysis": "这是 worst tier 的致命攻击面。审稿人会构建如下论证链： (1) \"Violations are a scaling phenomenon: 8B→70B reduces DR by 86-93% on DocRED without any method intervention\"; (2) \"The residual 1.8% at 70B is within the range achievable by prompt engineering (schema-informed prompt on 8B already achieves DR↓32%, better prompting on 70B should do more)\"; (3) \"OntoCoDec's absolute contribution at 70B is 1.5pp — smaller than the confidence interval of most IE metrics\"; (4) \"Meanwhile, the method introduces CF violations (0.04%→3.8%), creating a new problem to solve a vanishing one\"。\n防御策略（reframe A 为主）： - 不争论 70B 数字本身，承认 \"scale partially mitigates violations on loose-constraint\n  ontologies\" 作为 positive finding\n- 将论点转向 task complexity：SciERC 70B DR=6.5%（tight constraints 下 scale 不够），\n  EE RoV=64-89%（role constraints 下 scale 完全无效）\n- 70B DocRED 低 DR 恰好证明 \"tightness determines violation severity\" 的理论 claim——\n  DocRED τ̄=0.842 是 loose ontology 的代表，结论是 \"loose ontology + large model = low\n  violation, but tight ontology or complex task structure requires enforcement regardless\n  of scale\"\n- 但审稿人可能不买账：worst tier 下 2/3 审稿人仍标记 novelty incremental\n\n\n70B DocRED 是 worst tier 的核心打击点。预测 unconstrained DR=1.8%，基于以下推理： (1) 8B→70B SciERC DR 从 13.3%→6.5%（↓51%），但 SciERC 只有 7 types 且 constraint tightness 更高（τ̄=0.571），70B 的 distributional prior 仍频繁违反 tight constraints； (2) DocRED 96 types，τ̄=0.842（loose），大多数 relation 的 domain/range 覆盖多种 entity type——70B 的更好 type assignment 能力在 loose constraints 下几乎不违规； (3) 对标 FT 场景：Qwen FT DocRED DR=0.76%，Llama FT DocRED DR=0.49%——FT 让 8B 模型 \"学会\" schema，70B 的 in-context learning 能力接近但略弱于 FT，预期 DR 在 1-3% 区间； (4) RV=2.3% 远低于 8B 的 16-30%，因为 70B 对 96 个 relation name 的 recall 更强—— 但仍有少量 paraphrase/abbreviation（如 P710_participant → \"participant_in\"）； (5) Constrained DR=0.3% 因为 70B 本身违规少，semantic mask 的 fallback 频率极低 （估计 <5 次/doc vs Llama-8B 的 57 次/doc），几乎所有 token 位置 semantic mask 生效； (6) R_F1 delta=-0.2pp 因为 70B 的 RV baseline 已很低（2.3%），grammar 层消除 OOV 带来的 FP reduction 微乎其微（对比 Qwen-8B RV=29.66% → grammar 消除产生显著 F1 提升）； (7) CF=3.8% 比 8B 低但仍存在——semantic layer 的 per-relation independent type enforcement 在 70B 上仍产生 cross-relation inconsistency，只是频率更低； (8) Parse fail rate 2.1-2.8% 比 Llama-8B (6.8-9.1%) 低，70B 指令遵循能力更强。\n审稿人攻击线：\"70B unconstrained DR=1.8%，your method brings it to 0.3% — a 1.5pp absolute improvement on a 17000-triple dataset means ~265→44 violating triples。 This is a marginal cleanup, not a methodological contribution。At this scale, better prompting or a 405B model would likely eliminate the remaining 1.8% entirely。\"\n更致命的是百分比 reduction 虽为 83.3%，但审稿人会指出 \"83% reduction of 1.8% is 1.5 percentage points — statistically indistinguishable from noise on individual documents\"。 这与 Qwen-8B DocRED 的 18.46%→10.21% (Δ=8.25pp) 形成鲜明对比。\n"
180	  },
181	  {
182	    "name": "Error analysis / case study (EE + RE)",
183	    "description": "10-20 representative cases from WikiEvents v3 EE results + DocRED RE residuals。 分析 AC residual root causes, CF systematic patterns, qualitative evidence for paper。\n",
184	    "results": {
185	      "ee_ac_residual_cases_analyzed": 15,
186	      "ee_ac_root_cause_semantic_confusion_pct": 72,
187	      "ee_ac_root_cause_annotation_ambiguity_pct": 18,
188	      "ee_ac_root_cause_tokenizer_residual_pct": 10,
189	      "ee_cf_pattern_top1": "same entity assigned PER in one event and SID in another",
190	      "ee_cf_pattern_top2": "GPE vs FAC for location-type arguments across co-located events",
191	      "ee_cf_pattern_top3": "ORG vs SID for group entities in Movement vs Conflict events",
192	      "ee_cf_systematic_type_pair_count": 5,
193	      "re_docred_residual_dr_per_relation_top3": [
194	        "P31_instance_of: DR still ~3-5% even at constrained",
195	        "P17_country: loose constraint but edge-case entity types",
196	        "P131_located_in: GPE vs LOC boundary confusion"
197	      ],
198	      "qualitative_insight_novelty": "low"
199	    },
200	    "tables": [],
201	    "figures": [],
202	    "analysis": "error analysis 在 worst tier 下是 necessary but not sufficient。审稿人 comment： \"The error analysis confirms that residual violations are due to model confusion between semantically similar types, which is expected. The CF analysis shows the method systematically introduces a new violation category. Neither finding is surprising or provides actionable insight for improving the method.\" 防御：将 error analysis 定位为 \"empirical validation of the decidability taxonomy\" ——AC residuals 是 category (b) constraints 的 boundary cases，CF 是 category (c) non-local constraints 的 concrete manifestation。但这在 worst tier 下仅获得 \"adequate but not compelling\" 评价。\n\n\nworst tier 下 error analysis 不会产生 surprising findings。AC 残留（Qwen 2.1%, Llama 3.8%, Mistral 1.3%）的根因已在 BPE collision diagnostic 中部分解释： Mistral 有 2 个 collision group 贡献了大部分 AC，Qwen/Llama 0 collision 但仍有 AC， 说明是模型本身的 semantic confusion（如 SID vs SEN 语义相近，模型难以在 constrained 空间中区分）。分析 15 个 case 后，预期 72% 属于 \"similar entity types that the model confuses under constraint pressure\"（如 PER/SID/SEN 在 WikiEvents 中语义重叠）， 18% 属于 annotation 本身的 ambiguity（gold label 也可争议），10% 是 tokenizer residual（collision fix 后仍有边缘 case）。 CF 分析会揭示与 RE CF 相同的模式：type system 语义边界模糊导致同一 entity 在 不同 event context 中被合理归类为不同 type。但 worst tier 审稿人不接受 \"type ambiguity 解释\"——认为这是 method limitation 而非 type system 问题。 qualitative insight 缺乏 novelty：所有发现都是 \"method works as designed, residuals are expected boundary cases\"，不会产生 \"我没想到\" 的 insight。\n"
203	  },
204	  {
205	    "name": "EE FT composability",
206	    "description": "Fine-tuned model + OntoCoDec on WikiEvents Event Extraction。 验证 FT regime 下 constrained decoding 的 composability。 估算 ~30 GPU-hours，仅时间允许时执行。\n",
207	    "results": {
208	      "ee_ft_uncon_EV_pct": 0.5,
209	      "ee_ft_uncon_RoV_pct": 8.2,
210	      "ee_ft_uncon_AC_pct": 0.4,
211	      "ee_ft_uncon_CF_pct": 0.1,
212	      "ee_ft_uncon_trigger_f1": 62.5,
213	      "ee_ft_uncon_argument_f1": 38.0,
214	      "ee_ft_uncon_entity_f1": 71.3,
215	      "ee_ft_con_EV_pct": 0.0,
216	      "ee_ft_con_RoV_pct": 0.0,
217	      "ee_ft_con_AC_pct": 0.1,
218	      "ee_ft_con_CF_pct": 1.8,
219	      "ee_ft_con_trigger_f1": 62.3,
220	      "ee_ft_con_argument_f1": 37.8,
221	      "ee_ft_con_entity_f1": 71.0,
222	      "RoV_reduction_pct": 100.0,
223	      "AC_reduction_pct": 75.0,
224	      "argument_f1_delta_pp": -0.2,
225	      "ee_ft_total_violations_uncon_pct": 9.2,
226	      "ee_ft_total_violations_con_pct": 1.9
227	    },
228	    "tables": [
229	      {
230	        "name": "Table: EE FT Composability (WikiEvents, Qwen3-8B)",
231	        "columns": [
232	          "Condition",
233	          "EV%",
234	          "RoV%",
235	          "AC%",
236	          "CF%",
237	          "Trig-F1",
238	          "Arg-F1",
239	          "Ent-F1"
240	        ],
241	        "rows": [
242	          [
243	            "FT unconstrained",
244	            "0.5",
245	            "8.2",
246	            "0.4",
247	            "0.1",
248	            "62.5",
249	            "38.0",
250	            "71.3"
251	          ],
252	          [
253	            "FT constrained",
254	            "0.0",
255	            "0.0",
256	            "0.1",
257	            "1.8",
258	            "62.3",
259	            "37.8",
260	            "71.0"
261	          ],
262	          [
263	            "ZS unconstrained (ref)",
264	            "24.0",
265	            "74.9",
266	            "0.3",
267	            "0.0",
268	            "11.8",
269	            "0.1",
270	            "0.0"
271	          ],
272	          [
273	            "ZS constrained (ref)",
274	            "0.0",
275	            "0.0",
276	            "2.1",
277	            "21.1",
278	            "13.4",
279	            "1.7",
280	            "14.1"
281	          ]
282	        ]
283	      }
284	    ],
285	    "figures": [],
286	    "analysis": "worst tier 下 EE FT composability 是 reframe C 的关键支撑。即使审稿人质疑 ZS 场景的 practical relevance，FT 结果展示 \"even well-trained models benefit from decoding-time type checking\"。但攻击面是 F1 delta 为负——虽然微小（-0.2pp），在 worst tier 下会被 放大为 \"method degrades the model it's supposed to help\"。 如果时间不够（May 25 前），此实验可能无法完成。没有此数据，论文缺少 EE+FT 交叉 验证，reframe C 在 EE 维度的支撑变弱。建议如果必须砍实验，保留 RE FT 数据即可， EE FT 降级为 future work，但这会被审稿人标记为 \"incomplete evaluation\"。\n\n\nFT composability 在 RE 上已验证（Qwen DocRED: DR 0.76%→0.01%, R_F1 -0.30pp； Llama DocRED: DR 0.49%→0.20%, R_F1 +0.51pp）。EE FT 预期模式类似但更复杂：\n(1) FT 大幅降低 EV 和 RoV（模型学会了 event type 和 role vocabulary），预期 EV 0.5%、RoV 8.2%（比 ZS 的 24-37% 和 64-89% 大幅下降但不为零——EE 的 56 event types × 80 roles 比 RE 的 96 relation types 更复杂，长尾 event types 训练样本不足）； (2) AC 从 ZS 的 0-3.8% 降至 0.4%（FT 改善 entity type assignment）； (3) Constrained 消除所有 EV/RoV（grammar+semantic 层直接生效），AC 降至 0.1%； (4) CF 从 0.1%→1.8%（semantic layer 引入的系统性副作用，但比 ZS 的 14-21% 低很多—— FT 模型本身更一致，cross-event type drift 减少）； (5) F1 基本 neutral（delta <0.5pp），因为 FT 模型 RoV baseline 已低，grammar/semantic 消除 OOV 带来的 FP reduction 有限。\nworst tier 审稿人反应： - \"FT regime is the realistic deployment scenario. FT already reduces violations\n  to <10%. The additional 7pp reduction from OntoCoDec (9.2%→1.9%) is useful but\n  incremental — the heavy lifting is done by fine-tuning, not your method.\"\n- \"F1 delta is negative (-0.2pp), so the method doesn't even preserve quality.\" - 但 \"decoding-time type checking\" angle 对 industry reviewers 仍有吸引力\n  （类比 static typing for neural generation），这是 reframe C 的核心卖点。\n"
287	  },
288	  {
289	    "name": "Grammar-only cross-model validation (Qwen/Llama EE)",
290	    "description": "WikiEvents grammar_only ablation on Qwen3-8B 和 Llama-3.1-8B， 补全 Mistral grammar_only v3 已有的消融证据。\n",
291	    "results": {
292	      "qwen_ee_grammar_only_EV_pct": 0.0,
293	      "qwen_ee_grammar_only_RoV_pct": 71.5,
294	      "qwen_ee_grammar_only_AC_pct": 8.4,
295	      "qwen_ee_grammar_only_CF_pct": 0.2,
296	      "qwen_ee_grammar_only_trigger_f1": 12.8,
297	      "qwen_ee_grammar_only_entity_f1": 0.5,
298	      "llama_ee_grammar_only_EV_pct": 0.0,
299	      "llama_ee_grammar_only_RoV_pct": 77.2,
300	      "llama_ee_grammar_only_AC_pct": 11.6,
301	      "llama_ee_grammar_only_CF_pct": 0.1,
302	      "llama_ee_grammar_only_trigger_f1": 6.9,
303	      "llama_ee_grammar_only_entity_f1": 1.2,
304	      "grammar_only_RoV_range": "64-77%",
305	      "grammar_only_AC_surfacing_range": "8-14%",
306	      "semantic_layer_necessity_confirmed": true
307	    },
308	    "tables": [
309	      {
310	        "name": "Table: Grammar-only Ablation Cross-Model (WikiEvents EE)",
311	        "columns": [
312	          "Model",
313	          "EV%",
314	          "RoV%",
315	          "AC%",
316	          "CF%",
317	          "Ent-F1"
318	        ],
319	        "rows": [
320	          [
321	            "Qwen3-8B grammar_only",
322	            "0",
323	            "71.5",
324	            "8.4",
325	            "0.2",
326	            "0.5"
327	          ],
328	          [
329	            "Llama-3.1-8B grammar_only",
330	            "0",
331	            "77.2",
332	            "11.6",
333	            "0.1",
334	            "1.2"
335	          ],
336	          [
337	            "Mistral-7B grammar_only (actual)",
338	            "0",
339	            "64.0",
340	            "13.8",
341	            "1.1",
342	            "11.9"
343	          ],
344	          [
345	            "Qwen3-8B full_s1 (ref)",
346	            "0",
347	            "0",
348	            "2.1",
349	            "21.1",
350	            "14.1"
351	          ],
352	          [
353	            "Llama-3.1-8B full_s1 (ref)",
354	            "0",
355	            "0",
356	            "3.8",
357	            "17.2",
358	            "17.6"
359	          ],
360	          [
361	            "Mistral-7B full_s1 (ref)",
362	            "0",
363	            "0",
364	            "1.3",
365	            "14.9",
366	            "11.7"
367	          ]
368	        ]
369	      }
370	    ],
371	    "figures": [],
372	    "analysis": "消融结果 mechanically confirms semantic layer necessity，但 worst tier 审稿人 认为 \"this is a predictable result from the method design, not an empirical finding\"。 此实验的价值在于 completeness（审稿人不能攻击 \"only tested grammar_only on one model\"）， 但对 novelty 评分无贡献。优先级 Tier 3 合理——如果时间紧可以只报 Mistral（已有）， Qwen/Llama 放 appendix 或省略。\n\n\nMistral grammar_only v3 已显示：EV→0%, RoV=64%, AC=13.8%, CF=1.1%。 Qwen 和 Llama grammar_only 预期模式一致但具体数值因模型特性不同：\n(1) EV→0%（所有模型）：grammar CFG 限制 event type vocabulary 是确定性消除； (2) RoV 71.5%（Qwen）和 77.2%（Llama）：grammar CFG 无法 enforce context-dependent role constraints（需要知道当前 event type 才能确定 allowed roles），这是 structural limitation 不是 implementation bug。Llama RoV 更高是因为 Llama unconstrained baseline RoV=88.8% > Qwen 74.9%——grammar 消除 EV 后暴露更多 latent RoV violations （与 RE 中 grammar 暴露 latent DR 的模式完全对应）； (3) AC 8.4-11.6%：grammar-only 下 RoV 仍高 → 很多 role assignment 是 OOV → valid role 的 AC check 基于 grammar 强制匹配的 role（可能不是模型意图的 role） → AC 升高。与 Mistral 的 13.8% 一致； (4) CF 极低（0.1-0.2%）：grammar 不引入 cross-event type drift，CF 主要来自 semantic layer 的 per-event independent enforcement。\nworst tier 审稿人反应：\"Grammar CFG cannot handle context-dependent constraints — this is obvious from the CFG formalism itself. Demonstrating it empirically on 3 models adds confirmation but not insight. The real question is whether the semantic layer is novel, and it's just a lookup table with logit masking.\"\n"
373	  },
374	  {
375	    "name": "Bootstrap CI for EE metrics",
376	    "description": "10000-iteration bootstrap CI for WikiEvents EE F1 changes (constrained vs unconstrained, 3 models)。\n",
377	    "results": {
378	      "qwen_ee_trigger_f1_delta_pp": 1.55,
379	      "qwen_ee_trigger_f1_p_value": 0.08,
380	      "qwen_ee_trigger_f1_ci_95": [
381	        -0.2,
382	        3.3
383	      ],
384	      "qwen_ee_entity_f1_delta_pp": 14.09,
385	      "qwen_ee_entity_f1_p_value": 0.001,
386	      "qwen_ee_entity_f1_ci_95": [
387	        10.5,
388	        17.8
389	      ],
390	      "llama_ee_trigger_f1_delta_pp": 1.76,
391	      "llama_ee_trigger_f1_p_value": 0.12,
392	      "llama_ee_trigger_f1_ci_95": [
393	        -0.5,
394	        4.0
395	      ],
396	      "llama_ee_entity_f1_delta_pp": 17.63,
397	      "llama_ee_entity_f1_p_value": 0.001,
398	      "llama_ee_entity_f1_ci_95": [
399	        13.8,
400	        21.5
401	      ],
402	      "mistral_ee_trigger_f1_delta_pp": 1.5,
403	      "mistral_ee_trigger_f1_p_value": 0.15,
404	      "mistral_ee_trigger_f1_ci_95": [
405	        -0.6,
406	        3.6
407	      ],
408	      "mistral_ee_entity_f1_delta_pp": 11.71,
409	      "mistral_ee_entity_f1_p_value": 0.001,
410	      "mistral_ee_entity_f1_ci_95": [
411	        8.2,
412	        15.2
413	      ],
414	      "trigger_f1_significant_count": "0/3",
415	      "entity_f1_significant_count": "3/3",
416	      "argument_f1_too_low_for_ci": true
417	    },
418	    "tables": [
419	      {
420	        "name": "Table: Bootstrap CI for EE F1 (10000 iterations)",
421	        "columns": [
422	          "Model",
423	          "Metric",
424	          "Δ (pp)",
425	          "95% CI",
426	          "p-value",
427	          "Significant?"
428	        ],
429	        "rows": [
430	          [
431	            "Qwen3-8B",
432	            "Trigger F1",
433	            "+1.55",
434	            "[-0.2, +3.3]",
435	            "0.08",
436	            "No"
437	          ],
438	          [
439	            "Qwen3-8B",
440	            "Entity F1",
441	            "+14.09",
442	            "[+10.5, +17.8]",
443	            "<0.001",
444	            "Yes*"
445	          ],
446	          [
447	            "Llama-3.1-8B",
448	            "Trigger F1",
449	            "+1.76",
450	            "[-0.5, +4.0]",
451	            "0.12",
452	            "No"
453	          ],
454	          [
455	            "Llama-3.1-8B",
456	            "Entity F1",
457	            "+17.63",
458	            "[+13.8, +21.5]",
459	            "<0.001",
460	            "Yes*"
461	          ],
462	          [
463	            "Mistral-7B",
464	            "Trigger F1",
465	            "+1.50",
466	            "[-0.6, +3.6]",
467	            "0.15",
468	            "No"
469	          ],
470	          [
471	            "Mistral-7B",
472	            "Entity F1",
473	            "+11.71",
474	            "[+8.2, +15.2]",
475	            "<0.001",
476	            "Yes*"
477	          ]
478	        ]
479	      }
480	    ],
481	    "figures": [],
482	    "analysis": "worst tier 下 bootstrap CI 反而帮了倒忙：它精确量化了 \"trigger F1 improvement is not significant\"，给审稿人提供了弹药。Entity F1 的显著性被 \"format compliance\" 解释完全化解——不是方法带来了 semantic improvement，而是 grammar enforcement 让 parser 能工作了。 建议论文中如实报告 CI，但 framing 为 \"F1 is a control variable (C8), not an optimization target。Significance testing confirms constraints do not degrade trigger detection while restoring entity parsability。\" 避免把 entity F1 improvement 作为 selling point。\n\n\nBootstrap CI 预测基于以下分析：\n(1) Entity F1 从 0%→11-18% 的改变在所有模型上都 highly significant（p<0.001）。 但审稿人会 dismiss 这个结果：\"Entity F1 going from 0% to 14% is not a semantic improvement — it's format compliance. Without grammar enforcement, the JSON output is so malformed that the parser can't extract entities at all. This is measuring parser compatibility, not extraction quality.\" 这是准确的——unconstrained 的 entity_f1=0% 是因为 parser 无法识别 non-schema entity types，不是因为 entity spans 不正确。\n(2) Trigger F1 delta 1.5-1.8pp 在所有模型上都 NOT significant（p=0.08-0.15）。 246 docs 样本量下，trigger 级别的 bootstrap variance 较大（每个 doc 平均 只有 ~2-3 trigger mentions），CI 跨越零。worst tier 审稿人：\"Trigger F1 improvement is within noise — the method doesn't improve event detection.\"\n(3) Argument F1 太低（0.3-1.7%）无法做有意义的 CI——bootstrap 在此量级下 方差占比过高，CI 宽度 > point estimate。\n(4) worst tier 关键：所有 \"显著\" 的 F1 improvement 都来自 format compliance 而非 semantic improvement。审稿人 framing：\"If your contribution is making JSON parseable, that's an engineering contribution, not a research contribution.\"\n"
483	  },
484	  {
485	    "name": "Latency overhead measurement (DocRED)",
486	    "description": "Wall-clock comparison for DocRED constrained vs unconstrained decoding。 SciERC 已完成（p8: overhead 13.1%）。DocRED (p8b) 正在运行。\n",
487	    "results": {
488	      "docred_unconstrained_mean_s": 8.9,
489	      "docred_unconstrained_median_s": 8.5,
490	      "docred_constrained_mean_s": 11.2,
491	      "docred_constrained_median_s": 10.7,
492	      "docred_overhead_ratio_mean": 1.258,
493	      "docred_overhead_pct": 25.8,
494	      "docred_overhead_p95_perdoc": 1.42,
495	      "docred_constrained_total_hours": 3.1,
496	      "ee_estimated_overhead_pct": 32.0,
497	      "scierc_overhead_pct": 13.1,
498	      "docred_overhead_pct_final": 25.8,
499	      "overhead_scales_with_schema_size": true
500	    },
501	    "tables": [
502	      {
503	        "name": "Table: Latency Overhead Across Datasets",
504	        "columns": [
505	          "Dataset",
506	          "Schema Size",
507	          "Uncon (s/doc)",
508	          "Con (s/doc)",
509	          "Overhead %",
510	          "P95 Overhead"
511	        ],
512	        "rows": [
513	          [
514	            "SciERC (actual)",
515	            "7 rels",
516	            "4.16",
517	            "4.71",
518	            "13.1%",
519	            "26.2%"
520	          ],
521	          [
522	            "DocRED (predicted)",
523	            "96 rels",
524	            "8.9",
525	            "11.2",
526	            "25.8%",
527	            "42.0%"
528	          ],
529	          [
530	            "WikiEvents (est.)",
531	            "56 evt × 80 roles",
532	            "~12",
533	            "~15.8",
534	            "~32%",
535	            "~48%"
536	          ]
537	        ]
538	      }
539	    ],
540	    "figures": [],
541	    "analysis": "latency overhead 在 worst tier 下是辅助攻击面（不致命但 additive）。主要问题： overhead 随 schema complexity 增长，论文只测了 7-type 和 96-type，审稿人质疑 scalability。防御：overhead 主要来自 mask computation 而非 grammar compilation （compilation 是 one-time），mask 计算是 O(|allowed_types|) per type-token position， 在 GPU 上可并行。但 worst tier 下审稿人不接受 theoretical argument，要求 empirical scaling curve（需要 synthetic ontologies of varying sizes，deadline 前 不可能做）。\n\nSciERC overhead 13.1%（7 relation types, ~350 constraint rules）。DocRED 预期更高：\n(1) DocRED 96 relation types → grammar CFG 更大（~5x token count in grammar definition），XGrammar compilation overhead per-token 增加； (2) Semantic mask lookup table 96×N entries vs 7×N → per-token mask computation 更重； (3) 更关键：DocRED 文档更长（平均 ~200 tokens input, output ~800 tokens）， semantic layer 的 entity registry 累积更多 entries → lookup 时间随 generation length 线性增长； (4) 预期 overhead 25.8%——比 SciERC 翻倍但仍在 single-digit seconds per doc 内； (5) P95 per-doc overhead 1.42x（部分文档 entity registry 很大，mask computation spike）；\nworst tier 审稿人反应： - \"25.8% overhead on DocRED, estimated 32% on EE with 56 event types × 80 roles。\n  At 70B scale, generation is already slow (~30s per doc), adding 25% means\n  ~37.5s per doc. For a method that only removes 1.5pp of violations at 70B scale,\n  this overhead-to-benefit ratio is poor.\"\n- \"Overhead scales with schema complexity — for production KGs with hundreds of\n  types, overhead could exceed 50%. The paper doesn't analyze scaling behavior.\"\n\n防御：overhead 只影响 decoding-time（不影响 training），且只在 type token positions 有 mask computation（free text tokens 无额外开销）。25.8% 是 wall-clock 包含 all tokens 的 amortized overhead，type-token-only overhead 可能 >100% 但 amortized 后 acceptable。论文中应报告 per-type-token overhead 和 amortized overhead 两个维度。\n"
542	  }
543	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57177777-f8ca-4cbc-b661-7b448a99e09b",
  "isSidechain": false,
  "promptId": "b88248f5-45f7-484a-873c-8d439b996f3d",
  "type": "user",
  "uuid": "9830f352-1474-43ba-9531-294b44e68cc0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"70B SciERC unconstrained + constrained\",\n    \"description\": \"Llama-3.1-70B-Instruct AWQ-INT4 on SciERC 551 docs。已完成，实际结果需在 worst tier 下解读。 实际结果：unconstrained DR=6.5%, constrained DR=0%, CF=3.66%。\\n\",\n    \"results\": {\n      \"70b_scierc_uncon_DR_pct\": 6.5,\n      \"70b_scierc_uncon_RV_pct\": 0.6,\n      \"70b_scierc_uncon_ET_pct\": 0,\n      \"70b_scierc_uncon_R_F1\": 11.22,\n      \"70b_scierc_uncon_E_F1\": 35.17,\n      \"70b_scierc_con_DR_pct\": 0.0,\n      \"70b_scierc_con_RV_pct\": 0.0,\n      \"70b_scierc_con_CF_pct\": 3.66,\n      \"70b_scierc_con_R_F1\": 11.24,\n      \"70b_scierc_con_E_F1\": 35.14,\n      \"DR_reduction_pct\": 100.0,\n      \"R_F1_delta_pp\": 0.02,\n      \"E_F1_delta_pp\": -0.03\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 70B SciERC Cross-Scale Comparison\",\n        \"columns\": [\n          \"Model\",\n          \"Scale\",\n          \"DR%↓\",\n          \"RV%\",\n          \"ET%\",\n          \"CF%\",\n          \"R-F1\",\n          \"ΔR-F1\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"8B\",\n            \"15.37→0.93 (↓94%)\",\n            \"1.39→0\",\n            \"0.40→0\",\n            \"0.08→9.90\",\n            \"8.23→8.36\",\n            \"+0.13\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"8B\",\n            \"13.34→0.08 (↓99%)\",\n            \"0.55→0\",\n            \"0→0\",\n            \"0.49→6.56\",\n            \"2.68→2.54\",\n            \"-0.14\"\n          ],\n          [\n            \"Llama-3.1-70B\",\n            \"70B\",\n            \"6.50→0.00 (↓100%)\",\n            \"0.60→0\",\n            \"0→0\",\n            \"0→3.66\",\n            \"11.22→11.24\",\n            \"+0.02\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"worst tier 审稿人解读：SciERC unconstrained DR 从 8B 的 13-15% 降至 70B 的 6.5%， 自然 scaling 已削减 50-57%。OntoCoDec 将剩余 6.5%→0%（绝对 Δ=6.5pp）， 但审稿人可能认为 \\\"this remaining 6.5% would likely disappear at 405B or with better prompting\\\"。防线：指出 DR=6.5% 仍然意味着 97 个 triples 含有结构性违规， 下游 KG 不可用。但此防线在 DocRED 上会崩溃（见 P030）。\\n\\n\\n70B SciERC 结果对 worst tier 叙事是双刃剑。一方面，unconstrained DR=6.5% 远低于 8B 的 15.4% （Qwen）和 13.3%（Llama-8B），证明 scale 确实大幅缓解违规。另一方面，6.5% 仍非零——7 个 relation type 中 constraint tightness 高的（Feature-of τ=0.143, Compare τ=0.194）在 70B 下 仍有残留违规。审稿人会抓住 \\\"6.5%→0% 在 SciERC 是有意义的\\\"，但随即质问 \\\"DocRED 呢？\\\"。 worst tier 下 SciERC 被视为 cherry-pick（小 ontology，tight constraints 人为放大违规率）， DocRED 才是 litmus test。CF=3.66% 比 8B（Qwen 9.9%）低但仍非零，审稿人认为 \\\"even at 70B scale, the method still introduces new violation types (CF)\\\"。 R_F1 delta +0.02pp 在 noise 范围内——无法声明 F1 improvement，只能声明 neutral。\\n\"\n  },\n  {\n    \"name\": \"70B DocRED unconstrained + constrained\",\n    \"description\": \"Llama-3.1-70B-Instruct AWQ-INT4 on DocRED 998 docs。 8B baseline: Qwen DR=18.46%, Llama-8B DR=26.07%。 worst tier 预测 70B unconstrained DR 在 0.5-3.0% 之间，constrained 0-0.5%。\\n\",\n    \"results\": {\n      \"70b_docred_uncon_DR_pct\": 1.8,\n      \"70b_docred_uncon_RV_pct\": 2.3,\n      \"70b_docred_uncon_ET_pct\": 0.0,\n      \"70b_docred_uncon_CF_pct\": 0.04,\n      \"70b_docred_uncon_parse_fail_rate\": 2.1,\n      \"70b_docred_uncon_E_F1\": 64.2,\n      \"70b_docred_uncon_E_P\": 63.8,\n      \"70b_docred_uncon_E_R\": 64.6,\n      \"70b_docred_uncon_R_F1\": 10.1,\n      \"70b_docred_uncon_R_P\": 8.6,\n      \"70b_docred_uncon_R_R\": 12.3,\n      \"70b_docred_uncon_total_triples\": 17200,\n      \"70b_docred_con_DR_pct\": 0.3,\n      \"70b_docred_con_RV_pct\": 0.0,\n      \"70b_docred_con_ET_pct\": 0.0,\n      \"70b_docred_con_CF_pct\": 3.8,\n      \"70b_docred_con_parse_fail_rate\": 2.8,\n      \"70b_docred_con_E_F1\": 64.0,\n      \"70b_docred_con_E_P\": 63.5,\n      \"70b_docred_con_E_R\": 64.5,\n      \"70b_docred_con_R_F1\": 9.9,\n      \"70b_docred_con_R_P\": 8.4,\n      \"70b_docred_con_R_R\": 12.1,\n      \"70b_docred_DR_reduction_pct\": 83.3,\n      \"70b_docred_R_F1_delta_pp\": -0.2,\n      \"70b_docred_E_F1_delta_pp\": -0.2,\n      \"70b_docred_absolute_DR_delta_pp\": 1.5,\n      \"70b_docred_DR_eligible_triples_with_violations_uncon\": \"~265\",\n      \"70b_docred_DR_eligible_triples_with_violations_con\": \"~44\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 70B DocRED Cross-Scale DR Trajectory\",\n        \"columns\": [\n          \"Model\",\n          \"Uncon DR%\",\n          \"Con DR%\",\n          \"Absolute Δ\",\n          \"Relative ↓%\",\n          \"ΔR-F1\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"18.46\",\n            \"10.21\",\n            \"8.25pp\",\n            \"44.7%\",\n            \"+0.50\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"26.07\",\n            \"2.55\",\n            \"23.52pp\",\n            \"90.2%\",\n            \"+0.29\"\n          ],\n          [\n            \"Llama-3.1-70B\",\n            \"1.8\",\n            \"0.3\",\n            \"1.5pp\",\n            \"83.3%\",\n            \"-0.2\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: 70B DocRED Full Violation Profile\",\n        \"columns\": [\n          \"Condition\",\n          \"ET%\",\n          \"RV%\",\n          \"DR%\",\n          \"CF%\",\n          \"E-F1\",\n          \"R-F1\",\n          \"Parse%\"\n        ],\n        \"rows\": [\n          [\n            \"70B unconstrained\",\n            \"0.0\",\n            \"2.3\",\n            \"1.8\",\n            \"0.04\",\n            \"64.2\",\n            \"10.1\",\n            \"97.9\"\n          ],\n          [\n            \"70B constrained\",\n            \"0.0\",\n            \"0.0\",\n            \"0.3\",\n            \"3.8\",\n            \"64.0\",\n            \"9.9\",\n            \"97.2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 worst tier 的致命攻击面。审稿人会构建如下论证链： (1) \\\"Violations are a scaling phenomenon: 8B→70B reduces DR by 86-93% on DocRED without any method intervention\\\"; (2) \\\"The residual 1.8% at 70B is within the range achievable by prompt engineering (schema-informed prompt on 8B already achieves DR↓32%, better prompting on 70B should do more)\\\"; (3) \\\"OntoCoDec's absolute contribution at 70B is 1.5pp — smaller than the confidence interval of most IE metrics\\\"; (4) \\\"Meanwhile, the method introduces CF violations (0.04%→3.8%), creating a new problem to solve a vanishing one\\\"。\\n防御策略（reframe A 为主）： - 不争论 70B 数字本身，承认 \\\"scale partially mitigates violations on loose-constraint\\n  ontologies\\\" 作为 positive finding\\n- 将论点转向 task complexity：SciERC 70B DR=6.5%（tight constraints 下 scale 不够），\\n  EE RoV=64-89%（role constraints 下 scale 完全无效）\\n- 70B DocRED 低 DR 恰好证明 \\\"tightness determines violation severity\\\" 的理论 claim——\\n  DocRED τ̄=0.842 是 loose ontology 的代表，结论是 \\\"loose ontology + large model = low\\n  violation, but tight ontology or complex task structure requires enforcement regardless\\n  of scale\\\"\\n- 但审稿人可能不买账：worst tier 下 2/3 审稿人仍标记 novelty incremental\\n\\n\\n70B DocRED 是 worst tier 的核心打击点。预测 unconstrained DR=1.8%，基于以下推理： (1) 8B→70B SciERC DR 从 13.3%→6.5%（↓51%），但 SciERC 只有 7 types 且 constraint tightness 更高（τ̄=0.571），70B 的 distributional prior 仍频繁违反 tight constraints； (2) DocRED 96 types，τ̄=0.842（loose），大多数 relation 的 domain/range 覆盖多种 entity type——70B 的更好 type assignment 能力在 loose constraints 下几乎不违规； (3) 对标 FT 场景：Qwen FT DocRED DR=0.76%，Llama FT DocRED DR=0.49%——FT 让 8B 模型 \\\"学会\\\" schema，70B 的 in-context learning 能力接近但略弱于 FT，预期 DR 在 1-3% 区间； (4) RV=2.3% 远低于 8B 的 16-30%，因为 70B 对 96 个 relation name 的 recall 更强—— 但仍有少量 paraphrase/abbreviation（如 P710_participant → \\\"participant_in\\\"）； (5) Constrained DR=0.3% 因为 70B 本身违规少，semantic mask 的 fallback 频率极低 （估计 <5 次/doc vs Llama-8B 的 57 次/doc），几乎所有 token 位置 semantic mask 生效； (6) R_F1 delta=-0.2pp 因为 70B 的 RV baseline 已很低（2.3%），grammar 层消除 OOV 带来的 FP reduction 微乎其微（对比 Qwen-8B RV=29.66% → grammar 消除产生显著 F1 提升）； (7) CF=3.8% 比 8B 低但仍存在——semantic layer 的 per-relation independent type enforcement 在 70B 上仍产生 cross-relation inconsistency，只是频率更低； (8) Parse fail rate 2.1-2.8% 比 Llama-8B (6.8-9.1%) 低，70B 指令遵循能力更强。\\n审稿人攻击线：\\\"70B unconstrained DR=1.8%，your method brings it to 0.3% — a 1.5pp absolute improvement on a 17000-triple dataset means ~265→44 violating triples。 This is a marginal cleanup, not a methodological contribution。At this scale, better prompting or a 405B model would likely eliminate the remaining 1.8% entirely。\\\"\\n更致命的是百分比 reduction 虽为 83.3%，但审稿人会指出 \\\"83% reduction of 1.8% is 1.5 percentage points — statistically indistinguishable from noise on individual documents\\\"。 这与 Qwen-8B DocRED 的 18.46%→10.21% (Δ=8.25pp) 形成鲜明对比。\\n\"\n  },\n  {\n    \"name\": \"Error analysis / case study (EE + RE)\",\n    \"description\": \"10-20 representative cases from WikiEvents v3 EE results + DocRED RE residuals。 分析 AC residual root causes, CF systematic patterns, qualitative evidence for paper。\\n\",\n    \"results\": {\n      \"ee_ac_residual_cases_analyzed\": 15,\n      \"ee_ac_root_cause_semantic_confusion_pct\": 72,\n      \"ee_ac_root_cause_annotation_ambiguity_pct\": 18,\n      \"ee_ac_root_cause_tokenizer_residual_pct\": 10,\n      \"ee_cf_pattern_top1\": \"same entity assigned PER in one event and SID in another\",\n      \"ee_cf_pattern_top2\": \"GPE vs FAC for location-type arguments across co-located events\",\n      \"ee_cf_pattern_top3\": \"ORG vs SID for group entities in Movement vs Conflict events\",\n      \"ee_cf_systematic_type_pair_count\": 5,\n      \"re_docred_residual_dr_per_relation_top3\": [\n        \"P31_instance_of: DR still ~3-5% even at constrained\",\n        \"P17_country: loose constraint but edge-case entity types\",\n        \"P131_located_in: GPE vs LOC boundary confusion\"\n      ],\n      \"qualitative_insight_novelty\": \"low\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"error analysis 在 worst tier 下是 necessary but not sufficient。审稿人 comment： \\\"The error analysis confirms that residual violations are due to model confusion between semantically similar types, which is expected. The CF analysis shows the method systematically introduces a new violation category. Neither finding is surprising or provides actionable insight for improving the method.\\\" 防御：将 error analysis 定位为 \\\"empirical validation of the decidability taxonomy\\\" ——AC residuals 是 category (b) constraints 的 boundary cases，CF 是 category (c) non-local constraints 的 concrete manifestation。但这在 worst tier 下仅获得 \\\"adequate but not compelling\\\" 评价。\\n\\n\\nworst tier 下 error analysis 不会产生 surprising findings。AC 残留（Qwen 2.1%, Llama 3.8%, Mistral 1.3%）的根因已在 BPE collision diagnostic 中部分解释： Mistral 有 2 个 collision group 贡献了大部分 AC，Qwen/Llama 0 collision 但仍有 AC， 说明是模型本身的 semantic confusion（如 SID vs SEN 语义相近，模型难以在 constrained 空间中区分）。分析 15 个 case 后，预期 72% 属于 \\\"similar entity types that the model confuses under constraint pressure\\\"（如 PER/SID/SEN 在 WikiEvents 中语义重叠）， 18% 属于 annotation 本身的 ambiguity（gold label 也可争议），10% 是 tokenizer residual（collision fix 后仍有边缘 case）。 CF 分析会揭示与 RE CF 相同的模式：type system 语义边界模糊导致同一 entity 在 不同 event context 中被合理归类为不同 type。但 worst tier 审稿人不接受 \\\"type ambiguity 解释\\\"——认为这是 method limitation 而非 type system 问题。 qualitative insight 缺乏 novelty：所有发现都是 \\\"method works as designed, residuals are expected boundary cases\\\"，不会产生 \\\"我没想到\\\" 的 insight。\\n\"\n  },\n  {\n    \"name\": \"EE FT composability\",\n    \"description\": \"Fine-tuned model + OntoCoDec on WikiEvents Event Extraction。 验证 FT regime 下 constrained decoding 的 composability。 估算 ~30 GPU-hours，仅时间允许时执行。\\n\",\n    \"results\": {\n      \"ee_ft_uncon_EV_pct\": 0.5,\n      \"ee_ft_uncon_RoV_pct\": 8.2,\n      \"ee_ft_uncon_AC_pct\": 0.4,\n      \"ee_ft_uncon_CF_pct\": 0.1,\n      \"ee_ft_uncon_trigger_f1\": 62.5,\n      \"ee_ft_uncon_argument_f1\": 38.0,\n      \"ee_ft_uncon_entity_f1\": 71.3,\n      \"ee_ft_con_EV_pct\": 0.0,\n      \"ee_ft_con_RoV_pct\": 0.0,\n      \"ee_ft_con_AC_pct\": 0.1,\n      \"ee_ft_con_CF_pct\": 1.8,\n      \"ee_ft_con_trigger_f1\": 62.3,\n      \"ee_ft_con_argument_f1\": 37.8,\n      \"ee_ft_con_entity_f1\": 71.0,\n      \"RoV_reduction_pct\": 100.0,\n      \"AC_reduction_pct\": 75.0,\n      \"argument_f1_delta_pp\": -0.2,\n      \"ee_ft_total_violations_uncon_pct\": 9.2,\n      \"ee_ft_total_violations_con_pct\": 1.9\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: EE FT Composability (WikiEvents, Qwen3-8B)\",\n        \"columns\": [\n          \"Condition\",\n          \"EV%\",\n          \"RoV%\",\n          \"AC%\",\n          \"CF%\",\n          \"Trig-F1\",\n          \"Arg-F1\",\n          \"Ent-F1\"\n        ],\n        \"rows\": [\n          [\n            \"FT unconstrained\",\n            \"0.5\",\n            \"8.2\",\n            \"0.4\",\n            \"0.1\",\n            \"62.5\",\n            \"38.0\",\n            \"71.3\"\n          ],\n          [\n            \"FT constrained\",\n            \"0.0\",\n            \"0.0\",\n            \"0.1\",\n            \"1.8\",\n            \"62.3\",\n            \"37.8\",\n            \"71.0\"\n          ],\n          [\n            \"ZS unconstrained (ref)\",\n            \"24.0\",\n            \"74.9\",\n            \"0.3\",\n            \"0.0\",\n            \"11.8\",\n            \"0.1\",\n            \"0.0\"\n          ],\n          [\n            \"ZS constrained (ref)\",\n            \"0.0\",\n            \"0.0\",\n            \"2.1\",\n            \"21.1\",\n            \"13.4\",\n            \"1.7\",\n            \"14.1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"worst tier 下 EE FT composability 是 reframe C 的关键支撑。即使审稿人质疑 ZS 场景的 practical relevance，FT 结果展示 \\\"even well-trained models benefit from decoding-time type checking\\\"。但攻击面是 F1 delta 为负——虽然微小（-0.2pp），在 worst tier 下会被 放大为 \\\"method degrades the model it's supposed to help\\\"。 如果时间不够（May 25 前），此实验可能无法完成。没有此数据，论文缺少 EE+FT 交叉 验证，reframe C 在 EE 维度的支撑变弱。建议如果必须砍实验，保留 RE FT 数据即可， EE FT 降级为 future work，但这会被审稿人标记为 \\\"incomplete evaluation\\\"。\\n\\n\\nFT composability 在 RE 上已验证（Qwen DocRED: DR 0.76%→0.01%, R_F1 -0.30pp； Llama DocRED: DR 0.49%→0.20%, R_F1 +0.51pp）。EE FT 预期模式类似但更复杂：\\n(1) FT 大幅降低 EV 和 RoV（模型学会了 event type 和 role vocabulary），预期 EV 0.5%、RoV 8.2%（比 ZS 的 24-37% 和 64-89% 大幅下降但不为零——EE 的 56 event types × 80 roles 比 RE 的 96 relation types 更复杂，长尾 event types 训练样本不足）； (2) AC 从 ZS 的 0-3.8% 降至 0.4%（FT 改善 entity type assignment）； (3) Constrained 消除所有 EV/RoV（grammar+semantic 层直接生效），AC 降至 0.1%； (4) CF 从 0.1%→1.8%（semantic layer 引入的系统性副作用，但比 ZS 的 14-21% 低很多—— FT 模型本身更一致，cross-event type drift 减少）； (5) F1 基本 neutral（delta <0.5pp），因为 FT 模型 RoV baseline 已低，grammar/semantic 消除 OOV 带来的 FP reduction 有限。\\nworst tier 审稿人反应： - \\\"FT regime is the realistic deployment scenario. FT already reduces violations\\n  to <10%. The additional 7pp reduction from OntoCoDec (9.2%→1.9%) is useful but\\n  incremental — the heavy lifting is done by fine-tuning, not your method.\\\"\\n- \\\"F1 delta is negative (-0.2pp), so the method doesn't even preserve quality.\\\" - 但 \\\"decoding-time type checking\\\" angle 对 industry reviewers 仍有吸引力\\n  （类比 static typing for neural generation），这是 reframe C 的核心卖点。\\n\"\n  },\n  {\n    \"name\": \"Grammar-only cross-model validation (Qwen/Llama EE)\",\n    \"description\": \"WikiEvents grammar_only ablation on Qwen3-8B 和 Llama-3.1-8B， 补全 Mistral grammar_only v3 已有的消融证据。\\n\",\n    \"results\": {\n      \"qwen_ee_grammar_only_EV_pct\": 0.0,\n      \"qwen_ee_grammar_only_RoV_pct\": 71.5,\n      \"qwen_ee_grammar_only_AC_pct\": 8.4,\n      \"qwen_ee_grammar_only_CF_pct\": 0.2,\n      \"qwen_ee_grammar_only_trigger_f1\": 12.8,\n      \"qwen_ee_grammar_only_entity_f1\": 0.5,\n      \"llama_ee_grammar_only_EV_pct\": 0.0,\n      \"llama_ee_grammar_only_RoV_pct\": 77.2,\n      \"llama_ee_grammar_only_AC_pct\": 11.6,\n      \"llama_ee_grammar_only_CF_pct\": 0.1,\n      \"llama_ee_grammar_only_trigger_f1\": 6.9,\n      \"llama_ee_grammar_only_entity_f1\": 1.2,\n      \"grammar_only_RoV_range\": \"64-77%\",\n      \"grammar_only_AC_surfacing_range\": \"8-14%\",\n      \"semantic_layer_necessity_confirmed\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Grammar-only Ablation Cross-Model (WikiEvents EE)\",\n        \"columns\": [\n          \"Model\",\n          \"EV%\",\n          \"RoV%\",\n          \"AC%\",\n          \"CF%\",\n          \"Ent-F1\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B grammar_only\",\n            \"0\",\n            \"71.5\",\n            \"8.4\",\n            \"0.2\",\n            \"0.5\"\n          ],\n          [\n            \"Llama-3.1-8B grammar_only\",\n            \"0\",\n            \"77.2\",\n            \"11.6\",\n            \"0.1\",\n            \"1.2\"\n          ],\n          [\n            \"Mistral-7B grammar_only (actual)\",\n            \"0\",\n            \"64.0\",\n            \"13.8\",\n            \"1.1\",\n            \"11.9\"\n          ],\n          [\n            \"Qwen3-8B full_s1 (ref)\",\n            \"0\",\n            \"0\",\n            \"2.1\",\n            \"21.1\",\n            \"14.1\"\n          ],\n          [\n            \"Llama-3.1-8B full_s1 (ref)\",\n            \"0\",\n            \"0\",\n            \"3.8\",\n            \"17.2\",\n            \"17.6\"\n          ],\n          [\n            \"Mistral-7B full_s1 (ref)\",\n            \"0\",\n            \"0\",\n            \"1.3\",\n            \"14.9\",\n            \"11.7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"消融结果 mechanically confirms semantic layer necessity，但 worst tier 审稿人 认为 \\\"this is a predictable result from the method design, not an empirical finding\\\"。 此实验的价值在于 completeness（审稿人不能攻击 \\\"only tested grammar_only on one model\\\"）， 但对 novelty 评分无贡献。优先级 Tier 3 合理——如果时间紧可以只报 Mistral（已有）， Qwen/Llama 放 appendix 或省略。\\n\\n\\nMistral grammar_only v3 已显示：EV→0%, RoV=64%, AC=13.8%, CF=1.1%。 Qwen 和 Llama grammar_only 预期模式一致但具体数值因模型特性不同：\\n(1) EV→0%（所有模型）：grammar CFG 限制 event type vocabulary 是确定性消除； (2) RoV 71.5%（Qwen）和 77.2%（Llama）：grammar CFG 无法 enforce context-dependent role constraints（需要知道当前 event type 才能确定 allowed roles），这是 structural limitation 不是 implementation bug。Llama RoV 更高是因为 Llama unconstrained baseline RoV=88.8% > Qwen 74.9%——grammar 消除 EV 后暴露更多 latent RoV violations （与 RE 中 grammar 暴露 latent DR 的模式完全对应）； (3) AC 8.4-11.6%：grammar-only 下 RoV 仍高 → 很多 role assignment 是 OOV → valid role 的 AC check 基于 grammar 强制匹配的 role（可能不是模型意图的 role） → AC 升高。与 Mistral 的 13.8% 一致； (4) CF 极低（0.1-0.2%）：grammar 不引入 cross-event type drift，CF 主要来自 semantic layer 的 per-event independent enforcement。\\nworst tier 审稿人反应：\\\"Grammar CFG cannot handle context-dependent constraints — this is obvious from the CFG formalism itself. Demonstrating it empirically on 3 models adds confirmation but not insight. The real question is whether the semantic layer is novel, and it's just a lookup table with logit masking.\\\"\\n\"\n  },\n  {\n    \"name\": \"Bootstrap CI for EE metrics\",\n    \"description\": \"10000-iteration bootstrap CI for WikiEvents EE F1 changes (constrained vs unconstrained, 3 models)。\\n\",\n    \"results\": {\n      \"qwen_ee_trigger_f1_delta_pp\": 1.55,\n      \"qwen_ee_trigger_f1_p_value\": 0.08,\n      \"qwen_ee_trigger_f1_ci_95\": [\n        -0.2,\n        3.3\n      ],\n      \"qwen_ee_entity_f1_delta_pp\": 14.09,\n      \"qwen_ee_entity_f1_p_value\": 0.001,\n      \"qwen_ee_entity_f1_ci_95\": [\n        10.5,\n        17.8\n      ],\n      \"llama_ee_trigger_f1_delta_pp\": 1.76,\n      \"llama_ee_trigger_f1_p_value\": 0.12,\n      \"llama_ee_trigger_f1_ci_95\": [\n        -0.5,\n        4.0\n      ],\n      \"llama_ee_entity_f1_delta_pp\": 17.63,\n      \"llama_ee_entity_f1_p_value\": 0.001,\n      \"llama_ee_entity_f1_ci_95\": [\n        13.8,\n        21.5\n      ],\n      \"mistral_ee_trigger_f1_delta_pp\": 1.5,\n      \"mistral_ee_trigger_f1_p_value\": 0.15,\n      \"mistral_ee_trigger_f1_ci_95\": [\n        -0.6,\n        3.6\n      ],\n      \"mistral_ee_entity_f1_delta_pp\": 11.71,\n      \"mistral_ee_entity_f1_p_value\": 0.001,\n      \"mistral_ee_entity_f1_ci_95\": [\n        8.2,\n        15.2\n      ],\n      \"trigger_f1_significant_count\": \"0/3\",\n      \"entity_f1_significant_count\": \"3/3\",\n      \"argument_f1_too_low_for_ci\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Bootstrap CI for EE F1 (10000 iterations)\",\n        \"columns\": [\n          \"Model\",\n          \"Metric\",\n          \"Δ (pp)\",\n          \"95% CI\",\n          \"p-value\",\n          \"Significant?\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"Trigger F1\",\n            \"+1.55\",\n            \"[-0.2, +3.3]\",\n            \"0.08\",\n            \"No\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"Entity F1\",\n            \"+14.09\",\n            \"[+10.5, +17.8]\",\n            \"<0.001\",\n            \"Yes*\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"Trigger F1\",\n            \"+1.76\",\n            \"[-0.5, +4.0]\",\n            \"0.12\",\n            \"No\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"Entity F1\",\n            \"+17.63\",\n            \"[+13.8, +21.5]\",\n            \"<0.001\",\n            \"Yes*\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"Trigger F1\",\n            \"+1.50\",\n            \"[-0.6, +3.6]\",\n            \"0.15\",\n            \"No\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"Entity F1\",\n            \"+11.71\",\n            \"[+8.2, +15.2]\",\n            \"<0.001\",\n            \"Yes*\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"worst tier 下 bootstrap CI 反而帮了倒忙：它精确量化了 \\\"trigger F1 improvement is not significant\\\"，给审稿人提供了弹药。Entity F1 的显著性被 \\\"format compliance\\\" 解释完全化解——不是方法带来了 semantic improvement，而是 grammar enforcement 让 parser 能工作了。 建议论文中如实报告 CI，但 framing 为 \\\"F1 is a control variable (C8), not an optimization target。Significance testing confirms constraints do not degrade trigger detection while restoring entity parsability。\\\" 避免把 entity F1 improvement 作为 selling point。\\n\\n\\nBootstrap CI 预测基于以下分析：\\n(1) Entity F1 从 0%→11-18% 的改变在所有模型上都 highly significant（p<0.001）。 但审稿人会 dismiss 这个结果：\\\"Entity F1 going from 0% to 14% is not a semantic improvement — it's format compliance. Without grammar enforcement, the JSON output is so malformed that the parser can't extract entities at all. This is measuring parser compatibility, not extraction quality.\\\" 这是准确的——unconstrained 的 entity_f1=0% 是因为 parser 无法识别 non-schema entity types，不是因为 entity spans 不正确。\\n(2) Trigger F1 delta 1.5-1.8pp 在所有模型上都 NOT significant（p=0.08-0.15）。 246 docs 样本量下，trigger 级别的 bootstrap variance 较大（每个 doc 平均 只有 ~2-3 trigger mentions），CI 跨越零。worst tier 审稿人：\\\"Trigger F1 improvement is within noise — the method doesn't improve event detection.\\\"\\n(3) Argument F1 太低（0.3-1.7%）无法做有意义的 CI——bootstrap 在此量级下 方差占比过高，CI 宽度 > point estimate。\\n(4) worst tier 关键：所有 \\\"显著\\\" 的 F1 improvement 都来自 format compliance 而非 semantic improvement。审稿人 framing：\\\"If your contribution is making JSON parseable, that's an engineering contribution, not a research contribution.\\\"\\n\"\n  },\n  {\n    \"name\": \"Latency overhead measurement (DocRED)\",\n    \"description\": \"Wall-clock comparison for DocRED constrained vs unconstrained decoding。 SciERC 已完成（p8: overhead 13.1%）。DocRED (p8b) 正在运行。\\n\",\n    \"results\": {\n      \"docred_unconstrained_mean_s\": 8.9,\n      \"docred_unconstrained_median_s\": 8.5,\n      \"docred_constrained_mean_s\": 11.2,\n      \"docred_constrained_median_s\": 10.7,\n      \"docred_overhead_ratio_mean\": 1.258,\n      \"docred_overhead_pct\": 25.8,\n      \"docred_overhead_p95_perdoc\": 1.42,\n      \"docred_constrained_total_hours\": 3.1,\n      \"ee_estimated_overhead_pct\": 32.0,\n      \"scierc_overhead_pct\": 13.1,\n      \"docred_overhead_pct_final\": 25.8,\n      \"overhead_scales_with_schema_size\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Latency Overhead Across Datasets\",\n        \"columns\": [\n          \"Dataset\",\n          \"Schema Size\",\n          \"Uncon (s/doc)\",\n          \"Con (s/doc)\",\n          \"Overhead %\",\n          \"P95 Overhead\"\n        ],\n        \"rows\": [\n          [\n            \"SciERC (actual)\",\n            \"7 rels\",\n            \"4.16\",\n            \"4.71\",\n            \"13.1%\",\n            \"26.2%\"\n          ],\n          [\n            \"DocRED (predicted)\",\n            \"96 rels\",\n            \"8.9\",\n            \"11.2\",\n            \"25.8%\",\n            \"42.0%\"\n          ],\n          [\n            \"WikiEvents (est.)\",\n            \"56 evt × 80 roles\",\n            \"~12\",\n            \"~15.8\",\n            \"~32%\",\n            \"~48%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"latency overhead 在 worst tier 下是辅助攻击面（不致命但 additive）。主要问题： overhead 随 schema complexity 增长，论文只测了 7-type 和 96-type，审稿人质疑 scalability。防御：overhead 主要来自 mask computation 而非 grammar compilation （compilation 是 one-time），mask 计算是 O(|allowed_types|) per type-token position， 在 GPU 上可并行。但 worst tier 下审稿人不接受 theoretical argument，要求 empirical scaling curve（需要 synthetic ontologies of varying sizes，deadline 前 不可能做）。\\n\\nSciERC overhead 13.1%（7 relation types, ~350 constraint rules）。DocRED 预期更高：\\n(1) DocRED 96 relation types → grammar CFG 更大（~5x token count in grammar definition），XGrammar compilation overhead per-token 增加； (2) Semantic mask lookup table 96×N entries vs 7×N → per-token mask computation 更重； (3) 更关键：DocRED 文档更长（平均 ~200 tokens input, output ~800 tokens）， semantic layer 的 entity registry 累积更多 entries → lookup 时间随 generation length 线性增长； (4) 预期 overhead 25.8%——比 SciERC 翻倍但仍在 single-digit seconds per doc 内； (5) P95 per-doc overhead 1.42x（部分文档 entity registry 很大，mask computation spike）；\\nworst tier 审稿人反应： - \\\"25.8% overhead on DocRED, estimated 32% on EE with 56 event types × 80 roles。\\n  At 70B scale, generation is already slow (~30s per doc), adding 25% means\\n  ~37.5s per doc. For a method that only removes 1.5pp of violations at 70B scale,\\n  this overhead-to-benefit ratio is poor.\\\"\\n- \\\"Overhead scales with schema complexity — for production KGs with hundreds of\\n  types, overhead could exceed 50%. The paper doesn't analyze scaling behavior.\\\"\\n\\n防御：overhead 只影响 decoding-time（不影响 training），且只在 type token positions 有 mask computation（free text tokens 无额外开销）。25.8% 是 wall-clock 包含 all tokens 的 amortized overhead，type-token-only overhead 可能 >100% 但 amortized 后 acceptable。论文中应报告 per-type-token overhead 和 amortized overhead 两个维度。\\n\"\n  }\n]",
      "numLines": 543,
      "startLine": 1,
      "totalLines": 543
    }
  },
  "sourceToolAssistantUUID": "57177777-f8ca-4cbc-b661-7b448a99e09b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T17:07:02.975Z_

<details open><summary>🔧 Tool call — Read · `toolu_017pqsEZiqAym6cxseFzVr5c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9830f352-1474-43ba-9531-294b44e68cc0",
  "isSidechain": false,
  "requestId": "req_011CbAQBgLM8aiVZP29Vcm4T",
  "type": "assistant",
  "uuid": "e17f4c67-41c3-44a9-94ca-d733c7f8450a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YG5TSvwezrRdDvPmJdgthm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12892,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12892
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "e17f4c67-41c3-44a9-94ca-d733c7f8450a",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier empirical research paper on schema-constrained IE",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Tool result

_source line 13 · 2026-05-18T17:07:03.281Z_

<details><summary>↩ Tool result · `toolu_017pqsEZiqAym6cxseFzVr5c`</summary>

```text
1	# OntoCoDec — Paper Framing
2	
3	## Target Venue
4	EMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）
5	
6	## Title
7	OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints
8	(D015: "Near-Complete" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)
9	
10	**D040 Story 升级方向**: 从 "IE-specific constrained decoding" → "universal ontology-constrained structured generation framework"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。
11	
12	## Core Insight
13	LLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.
14	
15	**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:
16	- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)
17	- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])
18	- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。
19	- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。
20	
21	## Core Claims
22	
23	### Claim 1 (Empirical): Violation Landscape
24	LLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).
25	
26	**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.
27	
28	**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。
29	
30	**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.
31	
32	### Claim 2 (Empirical): Prompt Insufficiency
33	Schema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:
34	- Overall: 15.4% → 5.78% (-62.4%), still above 5%
35	- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)
36	- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses
37	
38	**Narrative**: This is NOT about "5.78% barely above 5%". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.
39	
40	### Claim 3 (Methodological): Composable Constraint Framework
41	OntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:
42	1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)
43	2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking
44	
45	The two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT "synergistic" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.
46	
47	The two layers compose via bitwise AND of token masks. Recommended framing: "Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor."
48	
49	**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):
50	When $M_{semantic} \cap M_{grammar} = \emptyset$, the system falls back to grammar-only control.
51	
52	**关键量化数据（Reviewer 从日志挖掘）**:
53	- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**
54	- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**
55	- DocRED fallback 频率是 SciERC 的 **5.3×**
56	- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）
57	
58	**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。
59	
60	**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 "Constraint Coverage" 指标（semantic masking 实际生效的 token 比例）。这把 "10.19% DR 残余" 从弱点变成可量化分析的 finding。Frame as "engineering robustness" in §4; fallback 频率 + tightness 作为 §5 定量分析。
61	
62	**Decidability taxonomy**: Constraints classified by prefix-decidability:
63	- (a) Purely local: entity type ∈ vocabulary (grammar layer)
64	- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)
65	- (c) Truly non-local: forward coreference — out of scope for forward-only decoding
66	
67	### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation
68	- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.
69	- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.
70	
71	**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.
72	
73	⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).
74	
75	### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)
76	**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)
77	
78	OntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.
79	
80	**Cross-task framing (Reviewer 评估 confirmed)**:
81	- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 "more complex ontology → more critical constraint enforcement" claim
82	- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。
83	- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints
84	- **"Practical value" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效
85	
86	**WikiEvents specifics** (DARPA KAIROS ontology):
87	- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）
88	- 245 组显式 (event_type, role) → allowed_entity_types 约束
89	- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints
90	- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值
91	- 99.98% 数据满足约束 → 约束定义是真实有效的
92	- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）
93	
94	**数据集选择理由**（MAVEN/RAMS 排除）：
95	- MAVEN (168 types): 无 argument extraction，不适用
96	- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束
97	- RAMS (139 types): 仅 cardinality 约束，无 entity type binding
98	- ACE05 (33 types): LDC 付费，采购周期来不及
99	- **WikiEvents 是唯一同时满足 "免费 + 有显式 role→entity_type 约束" 的数据集**
100	
101	**Violation 分类** (5 类，从 RE 的 4 类扩展):
102	- ET (Entity Type): entity type 不在 ontology 合法类型列表中
103	- EV (Event Vocabulary): event type 不在 ontology 定义中
104	- RoV (Role Vocabulary): argument role 不在该 event type 定义中
105	- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）
106	- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type
107	
108	**Full results (246 docs, v3 final — collision fix + exact-match fix)**:
109	
110	| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |
111	|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|
112	| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |
113	| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |
114	| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |
115	| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |
116	| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |
117	| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |
118	| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |
119	
120	**Grammar-only ablation (Mistral v3, all 3 models)**:
121	- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context
122	- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)
123	- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient
124	
125	**Post-hoc filtering comparison (devastating)**:
126	- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation
127	- Llama: 5,053→3 arguments (99.9% discarded)
128	- Mistral: 6,034→0 arguments (100% discarded)
129	- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)
130	
131	**BPE collision diagnostic (confirmed 2026-05-18)**:
132	- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens
133	- Llama (BPE, ~128K vocab): **0 collision groups** — same
134	- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')
135	- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision
136	
137	**关键 findings**:
138	- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求
139	- EV 显著（10-37%）→ grammar 层直接消除
140	- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions
141	- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP
142	- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing
143	
144	**Story upgrade**: WikiEvents results confirm paper narrative: "universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.
145	
146	**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.
147	
148	**Remaining risk**:
149	- CF 15-21% higher than RE → continues CF tradeoff framing
150	- 70B experiment timeline tight (need results by May 20 for paper integration)
151	
152	## Anticipated Reviewer Concerns
153	
154	### C1: "5.78% is barely above 5% — threshold is arbitrary"
155	**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.
156	
157	### C2: "Why not just post-hoc filter?"
158	**Response (D013, 实验结果已出)**:
159	
160	Post-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。
161	
162	**论文 framing（不以 F1 论高低，多维对比）**:
163	1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。
164	2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。
165	3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。
166	4. **Precision trade-off（诚实承认）**: "Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters."
167	
168	数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。
169	
170	**Reviewer 补充发现（D013 后）**:
171	5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。
172	6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——"prevent vs detect" 核心论据的具体数据。
173	7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。
174	
175	### C3: "Bitwise AND of two masks is not novel"
176	**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.
177	
178	### C4: "Evaluate-for violation rate increases with schema-informed prompt"
179	**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior ("Method X evaluates for Task Y" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just "harder instances" — it's an active interference between prompt-level constraint signals and the model's learned type associations.
180	
181	**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.
182	
183	### C5: "Only tested on one model (Qwen3-8B)"
184	**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：
185	- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS
186	- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)
187	- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)
188	
189	**Cross-model claim 指导（Reviewer 专项评估）**:
190	- ✅ 可声明："OntoCoDec generalizes across model families without code modification"（程序性事实，铁证）
191	- ❌ 不可声明："consistently achieves the same reduction rate"（仅 2 模型，不足以量化声明）
192	- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。
193	- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。
194	- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。
195	- 等 llama_docred_full_s1 出来后定最终 claim 措辞。
196	
197	### C6: "Constrained decoding degrades generation quality (CRANE, Structure Snowballing)"
198	**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:
199	
200	**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).
201	**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).
202	
203	**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。
204	- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。
205	- Frame as: "On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent."
206	- 不升级为 core claim，但如实报告。
207	
208	### C7: "Your method trades DR violations for CF violations (cross-field consistency)"
209	**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:
210	
211	**CF 子类型分析（根因已确认）**：
212	- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)
213	- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)
214	- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差
215	
216	**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。
217	
218	**论证层次**：
219	1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint
220	2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference
221	3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug
222	4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)
223	
224	**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 "CF 是 semantic type enforcement 的系统性副作用" 提供干净的消融证据。
225	
226	**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。
227	
228	**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。
229	
230	### C8: "Absolute F1 is too low (~8%) — results are not meaningful"
231	**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: "We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance."
232	
233	## Paper Structure (Draft — D040 updated)
234	1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)
235	2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure
236	3. Violation Landscape Study (Phase 0 empirics — independent contribution)
237	4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies
238	5. Experiments:
239	   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)
240	   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)
241	   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)
242	6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods
243	7. Conclusion: Framework generality across IE tasks
244	
245	## Claim Calibration (per Reviewer assessment)
246	
247	**Safe to claim (sufficient evidence from Phase 2)**:
248	- "First systematic study of ontology constraint violations in LLM-based IE"
249	- "Violation rate correlates with constraint tightness, not ontology size" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)
250	- "Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost" ✅ Phase 2 confirmed
251	- "Two-layer architecture provides complementary coverage — grammar enables semantic" ✅ Ablation confirmed
252	- "Prompt-level intervention scales poorly with ontology complexity" ✅ SciERC ↓62% vs DocRED ↓32%
253	
254	**Claim with caution**:
255	- "Near-complete type-valid IE" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to "Near-Complete"
256	- "Principled framework applicable to arbitrary IE ontologies" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending
257	- "F1 improvement" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升
258	- "CF reveals type system ambiguity" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示"因为是 type ambiguity 所以 CF 可接受"
259	
260	**Do NOT claim**:
261	- "General infrastructure for IE" — only zero-shot extraction validated
262	- "State-of-the-art" — F1 is control variable, not optimization target (see C8)
263	- "Synergistic effect" — mechanism is enabling dependency, not mutual amplification (see Claim 3)
264	- "S2 solves CF" or "S2 mitigates Structure Snowballing" — data shows S2 ≈ S1 on all metrics; position as architectural variant only
265	- "Pilot50 DR=0%" — small-sample artifact, full S2 has DR=0.97%
266	- "Grammar-first invariant" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim
267	- "Robust dual-layer composition across schema complexities" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim
268	
269	## Risk Ranking (ordered by reject probability)
270	
271	1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).
272	2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。
273	3. **Novelty perception** (MEDIUM): "PLDI'25 for code → OntoCoDec for IE" attack line. Must argue IE constraint structure differs fundamentally.
274	4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.
275	5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.
276	
277	## Critical Path to EMNLP Submission (May 25)
278	
279	- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅
280	- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)
281	- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅
282	- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破
283	- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量
284	- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写
285	- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review
286	- **May 20-24**: Review 修改 + 最终提交
287	
288	**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。
289	
290	## Status
291	- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)
292	- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)
293	- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)
294	- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)
295	- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)
296	- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)
297	- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)
298	- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)
299	- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)
300	- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)
301	- Related work: ✅ 42 bib entries, 4 additions merged
302	- Dream 6/6 actions: ✅ All complete
303	- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)
304	- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)
305	- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)
306	- Paper compilation: ✅ 8 pages正文 + appendix
307	- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified
308	- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)
309	- Doc length breakdown: ✅ Complete (appendix written)
310	- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动
311	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e17f4c67-41c3-44a9-94ca-d733c7f8450a",
  "isSidechain": false,
  "promptId": "b88248f5-45f7-484a-873c-8d439b996f3d",
  "type": "user",
  "uuid": "0d53656c-1246-4641-94be-ed7014e9d191",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/paper_framing.md",
      "content": "# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）\n\n## Title\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\n(D015: \"Near-Complete\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\n\n**D040 Story 升级方向**: 从 \"IE-specific constrained decoding\" → \"universal ontology-constrained structured generation framework\"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\nWhen $M_{semantic} \\cap M_{grammar} = \\emptyset$, the system falls back to grammar-only control.\n\n**关键量化数据（Reviewer 从日志挖掘）**:\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\n- DocRED fallback 频率是 SciERC 的 **5.3×**\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\n\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\n\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \"Constraint Coverage\" 指标（semantic masking 实际生效的 token 比例）。这把 \"10.19% DR 残余\" 从弱点变成可量化分析的 finding。Frame as \"engineering robustness\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)\n**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)\n\nOntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.\n\n**Cross-task framing (Reviewer 评估 confirmed)**:\n- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 \"more complex ontology → more critical constraint enforcement\" claim\n- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。\n- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints\n- **\"Practical value\" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效\n\n**WikiEvents specifics** (DARPA KAIROS ontology):\n- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）\n- 245 组显式 (event_type, role) → allowed_entity_types 约束\n- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints\n- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值\n- 99.98% 数据满足约束 → 约束定义是真实有效的\n- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）\n\n**数据集选择理由**（MAVEN/RAMS 排除）：\n- MAVEN (168 types): 无 argument extraction，不适用\n- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束\n- RAMS (139 types): 仅 cardinality 约束，无 entity type binding\n- ACE05 (33 types): LDC 付费，采购周期来不及\n- **WikiEvents 是唯一同时满足 \"免费 + 有显式 role→entity_type 约束\" 的数据集**\n\n**Violation 分类** (5 类，从 RE 的 4 类扩展):\n- ET (Entity Type): entity type 不在 ontology 合法类型列表中\n- EV (Event Vocabulary): event type 不在 ontology 定义中\n- RoV (Role Vocabulary): argument role 不在该 event type 定义中\n- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）\n- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type\n\n**Full results (246 docs, v3 final — collision fix + exact-match fix)**:\n\n| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |\n|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|\n| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |\n| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |\n| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |\n| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |\n| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |\n| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |\n| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |\n\n**Grammar-only ablation (Mistral v3, all 3 models)**:\n- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context\n- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)\n- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient\n\n**Post-hoc filtering comparison (devastating)**:\n- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation\n- Llama: 5,053→3 arguments (99.9% discarded)\n- Mistral: 6,034→0 arguments (100% discarded)\n- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)\n\n**BPE collision diagnostic (confirmed 2026-05-18)**:\n- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens\n- Llama (BPE, ~128K vocab): **0 collision groups** — same\n- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')\n- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision\n\n**关键 findings**:\n- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求\n- EV 显著（10-37%）→ grammar 层直接消除\n- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions\n- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP\n- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing\n\n**Story upgrade**: WikiEvents results confirm paper narrative: \"universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints\". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.\n\n**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.\n\n**Remaining risk**:\n- CF 15-21% higher than RE → continues CF tradeoff framing\n- 70B experiment timeline tight (need results by May 20 for paper integration)\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response (D013, 实验结果已出)**:\n\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\n\n**论文 framing（不以 F1 论高低，多维对比）**:\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\n4. **Precision trade-off（诚实承认）**: \"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\"\n\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\n\n**Reviewer 补充发现（D013 后）**:\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\"prevent vs detect\" 核心论据的具体数据。\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：\n- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS\n- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)\n- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)\n\n**Cross-model claim 指导（Reviewer 专项评估）**:\n- ✅ 可声明：\"OntoCoDec generalizes across model families without code modification\"（程序性事实，铁证）\n- ❌ 不可声明：\"consistently achieves the same reduction rate\"（仅 2 模型，不足以量化声明）\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:\n\n**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).\n**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).\n\n**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\n- Frame as: \"On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent.\"\n- 不升级为 core claim，但如实报告。\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft — D040 updated)\n1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments:\n   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)\n   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)\n   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods\n7. Conclusion: Framework generality across IE tasks\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending\n- \"F1 improvement\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\n- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅\n- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破\n- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量\n- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写\n- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review\n- **May 20-24**: Review 修改 + 最终提交\n\n**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\n- Related work: ✅ 42 bib entries, 4 additions merged\n- Dream 6/6 actions: ✅ All complete\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\n- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)\n- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)\n- Paper compilation: ✅ 8 pages正文 + appendix\n- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified\n- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)\n- Doc length breakdown: ✅ Complete (appendix written)\n- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动\n",
      "numLines": 311,
      "startLine": 1,
      "totalLines": 311
    }
  },
  "sourceToolAssistantUUID": "e17f4c67-41c3-44a9-94ca-d733c7f8450a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "0d53656c-1246-4641-94be-ed7014e9d191",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier empirical research paper on schema-constrained IE",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Assistant

_source line 16 · 2026-05-18T17:07:24.299Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me write the full LaTeX paper for the "worst" tier dream. This is a simulated paper for review purposes, targeting a score of 2.75-3.25 (Borderline Findings).

Key points from the narrative guidance:
1. Reframe from "method paper with empirical validation" to "empirical study with method validation"
2. Violation Landscape as main contribution (70B low violation is a positive finding about scale vs task complexity)
3. Prefix-decidability taxonomy formalized as theorem


4. FT composability as practical selling point ("decoding-time type checking for neural generation")
5. Worst tier: reviewers average 2.75-3.25, attacks on 70B making method motivation weak, novelty incremental, CF 15-21% on EE

Now I'm structuring the paper around the four core experiments: the 70B results on both SciERC and DocRED with constrained and unconstrained variants, the error analysis comparing entity extraction and relation extraction, and the fine-tuning F-score metrics. I'll weave these into sections that emphasize the empirical findings while positioning the method as a supporting contribution.

I'm also planning to include validation across different model families like Qwen and Llama for grammar-only approaches, bootstrap confidence intervals for the extraction metrics, and latency measurements on DocRED to show the practical overhead. Let me start writing the paper now using a standard article structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d53656c-1246-4641-94be-ed7014e9d191",
  "isSidechain": false,
  "requestId": "req_011CbAQC7wyHvNGKM3TrgX9C",
  "type": "assistant",
  "uuid": "a32680a3-44ba-4668-a7aa-7cf86adff30d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Lnw6yGe8ZUKfXBRc1HAcC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23236,
      "cache_read_input_tokens": 24733,
      "output_tokens": 482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 482,
          "cache_read_input_tokens": 24733,
          "cache_creation_input_tokens": 23236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23236
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

_source line 17 · 2026-05-18T17:07:24.301Z_

Now let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a32680a3-44ba-4668-a7aa-7cf86adff30d",
  "isSidechain": false,
  "requestId": "req_011CbAQC7wyHvNGKM3TrgX9C",
  "type": "assistant",
  "uuid": "59e135d8-f375-437d-a51a-2c6edaba557d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Lnw6yGe8ZUKfXBRc1HAcC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23236,
      "cache_read_input_tokens": 24733,
      "output_tokens": 482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 482,
          "cache_read_input_tokens": 24733,
          "cache_creation_input_tokens": 23236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23236
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

_source line 18 · 2026-05-18T17:07:25.671Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MdrJgHXfPrYp9tMRwgrnWE`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e135d8-f375-437d-a51a-2c6edaba557d",
  "isSidechain": false,
  "requestId": "req_011CbAQC7wyHvNGKM3TrgX9C",
  "type": "assistant",
  "uuid": "9a26e893-775c-4f4a-b238-51e59c60bb76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Lnw6yGe8ZUKfXBRc1HAcC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23236,
      "cache_read_input_tokens": 24733,
      "output_tokens": 482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 482,
          "cache_read_input_tokens": 24733,
          "cache_creation_input_tokens": 23236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23236
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

_source line 19 · 2026-05-18T17:07:25.842Z_

<details><summary>↩ Tool result · `toolu_01MdrJgHXfPrYp9tMRwgrnWE`</summary>

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
  "parentUuid": "9a26e893-775c-4f4a-b238-51e59c60bb76",
  "isSidechain": false,
  "promptId": "b88248f5-45f7-484a-873c-8d439b996f3d",
  "type": "user",
  "uuid": "27f55d86-e68e-40a7-940c-d7196891e279",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9a26e893-775c-4f4a-b238-51e59c60bb76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-18T17:07:52.538Z_

<details><summary>Logged reasoning block</summary>

```text
Good. The directory exists. Now let me write the paper. Let me carefully construct the LaTeX source.

Key data points I need to include:

**Experiment 1: 70B SciERC**
- 70B uncon: DR=6.5%, RV=0.6%, ET=0%, R_F1=11.22, E_F1=35.17
- 70B con: DR=0%, RV=0%, CF=3.66%, R_F1=11.24, E_F1=35.14
- Cross-scale table: Qwen-8B, Llama-8B, Llama-70B


- **Experiment 2: 70B DocRED**
- 70B uncon: DR=1.8%, RV=2.3%, ET=0%, CF=0.04%, E_F1=64.2, R_F1=10.1
- 70B con: DR=0.3%, RV=0%, ET=0%, CF=3.8%, E_F1=64.0, R_F1=9.9
- Cross-scale trajectory table and full violation profile table

Now I need to work through the error analysis section with the 15 cases examined, where semantic confusion accounts for the majority of issues.

**Experiment 4: EE FT composability**
- FT uncon: EV=0.5%, RoV=8.2%, AC=0.4%, CF=0.1%, Trig-F1=62.5, Arg-F1=38.0, Ent-F1=71.3
- FT con: EV=0%, RoV=0%, AC=0.1%, CF=1.8%, Trig-F1=62.3, Arg-F1=37.8, Ent-F1=71.0
- ZS reference rows

Looking at the grammar experiment next...

**Experiment 5: Grammar-only ablation**
Across the three models, grammar-only constraints show high role value errors (Qwen 71.5%, Llama 77.2%, Mistral 64%) with minimal entity recognition, suggesting the models struggle when restricted to structural patterns alone.

**Experiment 6: Bootstrap CI**
Now examining confidence intervals for the trigger and entity metrics, where Qwen's trigger F1 improvement of 1.55 percentage points isn't statistically significant at p=0.08, though entity F1 shows a larger gain.

**Experiment 7: Latency overhead**
Measuring inference time increases across datasets, with SciERC showing a 13.1% slowdown and DocRED experiencing similar overhead...

Now I'm planning out the paper structure with a focus on empirical validation—starting with the theoretical foundation, then the framework itself, followed by comprehensive experiments that test violation patterns at scale, cross-task generalization, ablations, and practical considerations like latency and statistical rigor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27f55d86-e68e-40a7-940c-d7196891e279",
  "isSidechain": false,
  "requestId": "req_011CbAQDnN47qyyY3ALLk64Y",
  "type": "assistant",
  "uuid": "67c3035b-007e-4e60-9244-7052714800b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvNeA4prfqWuGZsCgrXiLt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 47969,
      "output_tokens": 9860,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9860,
          "cache_read_input_tokens": 47969,
          "cache_creation_input_tokens": 512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 512
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

_source line 21 · 2026-05-18T17:07:52.539Z_

Writing the paper now. This covers all 7 experiments from the JSON.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67c3035b-007e-4e60-9244-7052714800b8",
  "isSidechain": false,
  "requestId": "req_011CbAQDnN47qyyY3ALLk64Y",
  "type": "assistant",
  "uuid": "9b42e43e-42d0-43d2-93f7-6ed5e375f351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvNeA4prfqWuGZsCgrXiLt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 47969,
      "output_tokens": 9860,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9860,
          "cache_read_input_tokens": 47969,
          "cache_creation_input_tokens": 512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 512
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

_source line 22 · 2026-05-18T17:10:49.264Z_

<details open><summary>🔧 Tool call — Write · `toolu_01B5C1ij5UpWtmip2NFcUVue`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{definition}{Definition}\n\n\\title{How and When Do LLMs Violate Ontology Constraints? \\\\ An Empirical Study with Decoding-Time Enforcement}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge Language Models (LLMs) generate ontology constraint violations at non-trivial rates when performing information extraction (IE), yet the factors governing violation severity remain poorly understood.\nWe present a large-scale empirical study of ontology constraint violations across three IE tasks (relation extraction on SciERC and DocRED, event extraction on WikiEvents), four LLM families (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-70B), and two training regimes (zero-shot and fine-tuned).\nOur analysis reveals that violation severity is determined by the interaction of constraint tightness and task structural complexity, not model scale alone: scaling from 8B to 70B parameters reduces domain/range violations on loose-constraint ontologies (DocRED DR: 26.1\\%$\\to$1.8\\%) but leaves violations on tight-constraint ontologies largely intact (SciERC DR: 13.3\\%$\\to$6.5\\%), while role-of-vocabulary violations in event extraction persist at 64--89\\% regardless of model size.\nWe formalize these observations through a prefix-decidability taxonomy that classifies constraints by their amenability to autoregressive enforcement.\nTo validate the taxonomy, we implement OntoCoDec, a system that compiles ontology schemas into composable grammar and semantic decoding constraints.\nOntoCoDec eliminates vocabulary and structural violations across all configurations, reduces domain/range violations by 83--100\\%, and composes with fine-tuned models to provide decoding-time type checking (total violations: 9.2\\%$\\to$1.9\\% on fine-tuned EE).\nThe method introduces cross-field consistency violations (CF: 1.8--21.1\\%) as a systematic trade-off of per-relation independent enforcement.\n\\end{abstract}\n\n\\section{Introduction}\n\nLLM-based information extraction systems produce structured outputs that must conform to ontology-defined type constraints: relation arguments must have entity types within the relation's domain and range, event arguments must satisfy role-specific entity type restrictions, and all generated types must belong to the target vocabulary. Violations of these constraints render extracted triples unusable for downstream knowledge graph construction and reasoning.\n\nThe prevalence and distribution of such violations, however, have not been systematically characterized. Prior work on constrained decoding for structured generation has focused on syntactic validity (JSON format, grammar compliance) rather than semantic constraint satisfaction. This leaves open a fundamental empirical question: how severe are ontology constraint violations in practice, what determines their severity, and when is decoding-time enforcement necessary versus when does model scaling suffice?\n\nWe address this question through a comprehensive empirical study spanning three IE tasks (relation extraction and event extraction), four model families at two scales (8B and 70B parameters), and two training regimes (zero-shot and fine-tuned). Our study yields three principal findings.\n\nFirst, constraint tightness and task structural complexity jointly determine violation severity, and model scale provides only partial mitigation. On DocRED, a loose-constraint ontology ($\\bar{\\tau}$=0.842) with 96 relation types, scaling from 8B to 70B reduces domain/range violations from 18.5--26.1\\% to 1.8\\%. On SciERC, a tight-constraint ontology ($\\bar{\\tau}$=0.571) with 7 relations, the same scaling reduces violations only from 13.3--15.4\\% to 6.5\\%. On WikiEvents event extraction, role-of-vocabulary violations remain at 64--89\\% across all 8B models, reflecting fundamental structural complexity that scaling alone cannot resolve.\n\nSecond, we formalize the space of enforceable constraints through a prefix-decidability taxonomy that partitions constraints into three categories: (a) purely local constraints decidable from the current token, (b) prefix-decidable constraints requiring generation history, and (c) truly non-local constraints requiring future context. This taxonomy provides theoretical guidance for what decoding-time enforcement can and cannot achieve.\n\nThird, we validate the taxonomy by implementing OntoCoDec, a system that compiles ontology definitions into composable grammar (category a) and semantic (category b) constraint layers. OntoCoDec eliminates vocabulary violations across all configurations and reduces domain/range violations by 83--100\\%, confirming the taxonomy's predictions. The method composes with fine-tuned models, reducing total violations from 9.2\\% to 1.9\\% on event extraction while preserving task performance ($\\Delta$Arg-F1 = $-$0.2pp).\n\nOur contributions are:\n\\begin{itemize}[nosep]\n    \\item A systematic empirical study of ontology constraint violations across tasks, model scales, and training regimes, establishing that constraint tightness and task complexity, not model scale, determine violation severity.\n    \\item A prefix-decidability taxonomy that formally characterizes the space of constraints amenable to autoregressive enforcement.\n    \\item OntoCoDec, a constraint enforcement system that validates the taxonomy and provides decoding-time type checking for neural IE, composable with both zero-shot and fine-tuned models.\n    \\item Quantitative analysis of the cross-field consistency trade-off introduced by per-relation independent enforcement, identifying systematic patterns tied to type system ambiguity.\n\\end{itemize}\n\n\\section{Prefix-Decidability of Ontology Constraints}\n\nWe formalize the conditions under which ontology constraints can be enforced during autoregressive generation.\n\n\\begin{definition}[Ontology Constraint]\nAn ontology constraint $c$ is a predicate over structured outputs $y$ such that $c(y) \\in \\{0, 1\\}$. An output $y$ is \\emph{type-valid} if $c(y) = 1$ for all constraints $c$ in the ontology $\\mathcal{O}$.\n\\end{definition}\n\n\\begin{definition}[Prefix-Decidability]\nA constraint $c$ is \\emph{prefix-decidable at position $t$} if there exists a function $f_c$ such that for any prefix $y_{1:t}$, $f_c(y_{1:t}) = 1$ implies $c(y) = 1$ for all valid completions $y_{t+1:T}$, and $f_c(y_{1:t}) = 0$ implies $c(y) = 0$ for all completions.\n\\end{definition}\n\n\\begin{theorem}[Decidability Trichotomy]\nOntology constraints in IE structured generation partition into three categories:\n\\begin{enumerate}[nosep,label=(\\alph*)]\n    \\item \\textbf{Purely local}: The constraint is decidable from the current token position alone (e.g., ``entity type $\\in$ vocabulary''). These are expressible as context-free grammars.\n    \\item \\textbf{Prefix-decidable with state}: The constraint requires a finite state register tracking previously generated content (e.g., ``argument entity type $\\in$ domain(relation\\_type)'' requires knowing the current relation type from earlier in the generation). These require stateful logit masking.\n    \\item \\textbf{Truly non-local}: The constraint depends on tokens not yet generated (e.g., forward coreference: ``entity $e$ at position $i$ must have the same type as entity $e$ at position $j > i$''). These cannot be enforced during left-to-right decoding without lookahead.\n\\end{enumerate}\n\\end{theorem}\n\n\\begin{proof}[Proof sketch]\nCategory (a) follows from the definition of CFGs: a token-level membership check requires no context. Category (b): the state register is finite (bounded by the ontology size), and the constraint function is computable given the register. Category (c): by construction, the constraint predicate requires $y_j$ with $j > t$, which is unavailable at decoding step $t$. No finite-state augmentation of the decoder can decide such constraints without generating $y_j$ first.\n\\end{proof}\n\nThis taxonomy directly maps to our system architecture: category (a) constraints are handled by a grammar layer (compiled CFG), category (b) by a semantic layer (stateful logit masking with an entity registry), and category (c) constraints (cross-field consistency) remain unenforced, explaining the CF violations observed empirically.\n\n\\section{OntoCoDec: Compiled Ontology Constraints}\n\nOntoCoDec compiles an IE ontology schema $\\mathcal{O}$ into two composable constraint layers applied during autoregressive decoding.\n\n\\subsection{Grammar Layer}\n\nThe grammar layer compiles the ontology's type vocabulary into a context-free grammar (CFG) that constrains the decoder's output to produce syntactically valid JSON with only schema-defined type names. Given an ontology $\\mathcal{O}$ with entity types $\\mathcal{E}$, relation types $\\mathcal{R}$ (for RE) or event types $\\mathcal{V}$ and argument roles $\\mathcal{A}$ (for EE), the compiler generates a CFG where type-name terminals are restricted to $\\mathcal{E} \\cup \\mathcal{R}$ (or $\\mathcal{E} \\cup \\mathcal{V} \\cup \\mathcal{A}$). At each decoding step, the grammar mask $M_{\\text{grammar}}$ zeroes out logits for tokens that would violate the CFG.\n\nThis layer eliminates category (a) violations: entity type vocabulary errors (ET$\\to$0\\%), relation vocabulary errors (RV$\\to$0\\%), and event vocabulary errors (EV$\\to$0\\%).\n\n\\subsection{Semantic Layer}\n\nThe semantic layer maintains a stateful entity registry $\\mathcal{S}$ that tracks (entity mention, entity type) pairs as they are generated. When the decoder reaches a type-constrained position (e.g., the entity type field of a relation argument), the semantic layer computes an allowed-type mask based on the current context:\n\nFor relation extraction, given a relation type $r$ at the current position, the semantic mask is:\n\\[\nM_{\\text{semantic}}(t) = \\{e \\in \\mathcal{E} \\mid e \\in \\text{domain}(r) \\cup \\text{range}(r)\\}\n\\]\n\nFor event extraction, given event type $v$ and argument role $a$:\n\\[\nM_{\\text{semantic}}(t) = \\{e \\in \\mathcal{E} \\mid e \\in \\text{allowed\\_types}(v, a)\\}\n\\]\n\nThis layer enforces category (b) constraints: domain/range violations (DR) and argument constraint violations (AC).\n\n\\subsection{Constraint Composition}\n\nThe two layers compose via bitwise AND of token masks:\n\\[\nM_{\\text{final}}(t) = M_{\\text{grammar}}(t) \\wedge M_{\\text{semantic}}(t)\n\\]\n\nWhen $M_{\\text{final}}(t) = \\emptyset$ (empty intersection), the system falls back to grammar-only constraints ($M_{\\text{grammar}}(t)$), maintaining structural validity as a guaranteed floor. This graceful degradation is critical: on DocRED (96 relation types), fallback occurs approximately 57 times per document for 8B models due to frequent constraint conflicts, explaining residual DR violations under constrained decoding.\n\nThe grammar layer is a prerequisite for the semantic layer, not a symmetric complement. Without grammar enforcement, the semantic layer encounters out-of-vocabulary relation types for which no domain/range rules exist, rendering it ineffective (semantic-only achieves only 24\\% DR reduction vs. the full system's 94\\%).\n\n\\section{Experiments}\n\nWe evaluate across three IE tasks, four model families, and two training regimes. All experiments use greedy decoding. F1 scores are computed using the all\\_set matching criterion. We report five violation types: entity type (ET), relation/event vocabulary (RV/EV), domain/range (DR), role-of-vocabulary (RoV), argument constraint (AC), and cross-field consistency (CF).\n\n\\subsection{Violation Landscape Across Model Scales}\n\nWe compare ontology constraint violations between 8B-parameter models (Qwen3-8B, Llama-3.1-8B) and a 70B-parameter model (Llama-3.1-70B-Instruct, AWQ-INT4 quantized) on relation extraction.\n\n\\paragraph{SciERC (7 relation types, $\\bar{\\tau}$=0.571).}\nTable~\\ref{tab:70b-scierc} shows violation rates across scales. Scaling from 8B to 70B reduces unconstrained DR from 13.3--15.4\\% to 6.5\\%, a 50--58\\% relative reduction. OntoCoDec eliminates the remaining violations completely (DR: 6.5\\%$\\to$0.0\\%, $\\Delta$=100\\%), with R-F1 change of +0.02pp (within noise). At 8B scale, OntoCoDec achieves 94--99\\% DR reduction with comparable F1 neutrality.\n\nThe 70B unconstrained DR of 6.5\\% corresponds to 97 triples with structural violations in the 551-document corpus. While model scaling substantially reduces violation rates, the residual violations concentrate on tight-constraint relations (Feature-of: $\\tau$=0.143, Compare: $\\tau$=0.194), confirming that constraint tightness, not model capability, is the binding factor.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-scale violation comparison on SciERC. DR\\%$\\downarrow$ shows unconstrained$\\to$constrained (relative reduction). CF\\% is constrained-only.}\n\\label{tab:70b-scierc}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Scale & DR\\%$\\downarrow$ & RV\\% & ET\\% & CF\\% & $\\Delta$R-F1 \\\\\n\\midrule\nQwen3-8B & 8B & 15.4$\\to$0.93 (94\\%) & 1.39$\\to$0 & 0.40$\\to$0 & 9.90 & +0.13 \\\\\nLlama-3.1-8B & 8B & 13.3$\\to$0.08 (99\\%) & 0.55$\\to$0 & 0$\\to$0 & 6.56 & $-$0.14 \\\\\nLlama-3.1-70B & 70B & 6.50$\\to$0.00 (100\\%) & 0.60$\\to$0 & 0$\\to$0 & 3.66 & +0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DocRED (96 relation types, $\\bar{\\tau}$=0.842).}\nTable~\\ref{tab:70b-docred-trajectory} presents the cross-scale DR trajectory. The loose-constraint DocRED ontology shows a dramatically different scaling pattern: 70B unconstrained DR is only 1.8\\%, compared to 18.5\\% (Qwen-8B) and 26.1\\% (Llama-8B). Model scaling reduces DocRED violations by 86--93\\% without any method intervention.\n\nOntoCoDec further reduces 70B DocRED DR from 1.8\\% to 0.3\\% (83.3\\% relative reduction, 1.5pp absolute). Table~\\ref{tab:70b-docred-profile} shows the full violation profile. The absolute improvement of 1.5pp is modest: on 17,200 total triples, this corresponds to approximately 265$\\to$44 violating triples. The method simultaneously introduces CF violations (0.04\\%$\\to$3.8\\%), creating a new violation category while resolving a diminishing one.\n\nThis result is a positive finding for the violation landscape study: it confirms that loose-constraint ontologies combined with large models produce minimal violations, while tight-constraint ontologies and structurally complex tasks (Section~\\ref{sec:ee}) require enforcement regardless of scale.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-scale DR trajectory on DocRED.}\n\\label{tab:70b-docred-trajectory}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Uncon DR\\% & Con DR\\% & Abs. $\\Delta$ & Rel. $\\downarrow$\\% & $\\Delta$R-F1 \\\\\n\\midrule\nQwen3-8B & 18.46 & 10.21 & 8.25pp & 44.7 & +0.50 \\\\\nLlama-3.1-8B & 26.07 & 2.55 & 23.5pp & 90.2 & +0.29 \\\\\nLlama-3.1-70B & 1.80 & 0.30 & 1.50pp & 83.3 & $-$0.20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Full violation profile for Llama-3.1-70B on DocRED.}\n\\label{tab:70b-docred-profile}\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nCondition & ET\\% & RV\\% & DR\\% & CF\\% & E-F1 & R-F1 & Parse\\% \\\\\n\\midrule\n70B unconstrained & 0.0 & 2.3 & 1.8 & 0.04 & 64.2 & 10.1 & 97.9 \\\\\n70B constrained & 0.0 & 0.0 & 0.3 & 3.8 & 64.0 & 9.9 & 97.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Task Generalization: Event Extraction}\n\\label{sec:ee}\n\nWe evaluate OntoCoDec on WikiEvents event extraction (56 event types, 80 argument roles, 27 entity types, 245 role$\\to$entity type constraints). Event extraction presents a structurally more complex constraint space than relation extraction: each event type defines which argument roles are permitted and which entity types each role accepts.\n\n\\paragraph{Grammar-Only Ablation.}\nTable~\\ref{tab:grammar-ablation} presents the grammar-only ablation across three 8B models. Grammar enforcement eliminates event vocabulary violations (EV$\\to$0\\%) across all models but leaves role-of-vocabulary violations at 64--77\\%. This confirms that grammar CFGs cannot express context-dependent constraints (which roles are valid depends on the current event type), validating the necessity of the semantic layer for category (b) constraints.\n\nUnder grammar-only decoding, argument constraint violations rise to 8.4--13.8\\%. This is a latent violation surfacing effect: grammar forces the model to produce valid event type names, which enables the violation checker to evaluate role constraints that were previously masked by invalid event types. The same pattern appears in relation extraction, where grammar enforcement exposes latent DR violations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Grammar-only ablation on WikiEvents event extraction (3 models, 8B scale). Full S1 rows are constrained with both grammar and semantic layers.}\n\\label{tab:grammar-ablation}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nModel / Condition & EV\\% & RoV\\% & AC\\% & CF\\% & Ent-F1 \\\\\n\\midrule\nQwen3-8B grammar-only & 0 & 71.5 & 8.4 & 0.2 & 0.5 \\\\\nLlama-3.1-8B grammar-only & 0 & 77.2 & 11.6 & 0.1 & 1.2 \\\\\nMistral-7B grammar-only & 0 & 64.0 & 13.8 & 1.1 & 11.9 \\\\\n\\midrule\nQwen3-8B full S1 & 0 & 0 & 2.1 & 21.1 & 14.1 \\\\\nLlama-3.1-8B full S1 & 0 & 0 & 3.8 & 17.2 & 17.6 \\\\\nMistral-7B full S1 & 0 & 0 & 1.3 & 14.9 & 11.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RoV as the Critical EE Violation.}\nRole-of-vocabulary violations in EE (64--89\\% unconstrained) are 3--5$\\times$ higher than relation vocabulary violations in RE (1--30\\%). This disparity reflects the structural complexity difference: EE requires context-dependent role assignment conditioned on event type, while RE relation names are drawn from a flat vocabulary. The persistence of high RoV rates across all 8B models, combined with the grammar layer's inability to address them, provides the strongest evidence that semantic-layer enforcement is necessary for structurally complex IE tasks.\n\n\\subsection{Fine-Tuning Composability}\n\\label{sec:ft}\n\nA practical question is whether decoding-time constraint enforcement remains useful when the model has been fine-tuned on task-specific data. Table~\\ref{tab:ft-composability} compares fine-tuned Qwen3-8B with and without OntoCoDec on WikiEvents event extraction.\n\nFine-tuning dramatically reduces violations compared to zero-shot (total violations: 9.2\\% vs. $>$99\\% unconstrained zero-shot). OntoCoDec further reduces total violations from 9.2\\% to 1.9\\%, eliminating all remaining EV and RoV violations and reducing AC from 0.4\\% to 0.1\\%. Task performance is preserved: trigger F1 changes by $-$0.2pp and argument F1 by $-$0.2pp, both within noise.\n\nThe CF trade-off is substantially mitigated in the fine-tuned regime: CF rises from 0.1\\% to 1.8\\% (vs. 0\\%$\\to$14--21\\% in zero-shot). Fine-tuned models produce more internally consistent type assignments, reducing the cross-event type drift that drives CF violations.\n\nThis result supports the framing of OntoCoDec as decoding-time type checking for neural generation: analogous to static type systems in programming languages, it provides compile-time guarantees regardless of the underlying model's training, catching residual violations that fine-tuning reduces but does not eliminate.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning composability on WikiEvents EE (Qwen3-8B). ZS = zero-shot reference.}\n\\label{tab:ft-composability}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & EV\\% & RoV\\% & AC\\% & CF\\% & Trig-F1 & Arg-F1 & Ent-F1 \\\\\n\\midrule\nFT unconstrained & 0.5 & 8.2 & 0.4 & 0.1 & 62.5 & 38.0 & 71.3 \\\\\nFT constrained & 0.0 & 0.0 & 0.1 & 1.8 & 62.3 & 37.8 & 71.0 \\\\\n\\midrule\nZS unconstrained & 24.0 & 74.9 & 0.3 & 0.0 & 11.8 & 0.1 & 0.0 \\\\\nZS constrained & 0.0 & 0.0 & 2.1 & 21.1 & 13.4 & 1.7 & 14.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Statistical Significance}\n\nTable~\\ref{tab:bootstrap-ci} reports bootstrap confidence intervals (10,000 iterations) for EE F1 changes under constrained decoding.\n\nTrigger F1 improvements (+1.50 to +1.76pp) are not statistically significant for any model (all $p > 0.05$, CIs spanning zero). Entity F1 improvements (+11.7 to +17.6pp) are significant ($p < 0.001$) for all models, but this reflects format compliance rather than semantic improvement: unconstrained entity F1 is 0\\% because the parser cannot extract entities from outputs containing non-schema type names. Grammar enforcement restores parseable output, and the entity F1 gain measures parser compatibility, not extraction quality.\n\nArgument F1 is too low in the zero-shot setting (0.1--1.7\\%) for meaningful confidence interval estimation; bootstrap variance at this scale exceeds the point estimates.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap CI (10,000 iterations) for WikiEvents EE F1 changes (constrained $-$ unconstrained). $^*$Significance reflects format compliance, not semantic improvement.}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Metric & $\\Delta$ (pp) & 95\\% CI & $p$ & Sig.? \\\\\n\\midrule\nQwen3-8B & Trigger F1 & +1.55 & [$-$0.2, +3.3] & 0.08 & No \\\\\nQwen3-8B & Entity F1 & +14.09 & [+10.5, +17.8] & $<$0.001 & Yes$^*$ \\\\\nLlama-3.1-8B & Trigger F1 & +1.76 & [$-$0.5, +4.0] & 0.12 & No \\\\\nLlama-3.1-8B & Entity F1 & +17.63 & [+13.8, +21.5] & $<$0.001 & Yes$^*$ \\\\\nMistral-7B & Trigger F1 & +1.50 & [$-$0.6, +3.6] & 0.15 & No \\\\\nMistral-7B & Entity F1 & +11.71 & [+8.2, +15.2] & $<$0.001 & Yes$^*$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Latency Overhead}\n\nTable~\\ref{tab:latency} reports wall-clock latency overhead of constrained decoding. Overhead scales with schema complexity: 13.1\\% on SciERC (7 relations), 25.8\\% on DocRED (96 relations), and an estimated 32\\% on WikiEvents (56 event types $\\times$ 80 roles). The overhead arises primarily from semantic mask computation at type-token positions; free-text tokens incur no additional cost. P95 per-document overhead reaches 42\\% on DocRED due to documents with large entity registries.\n\n\\begin{table}[t]\n\\centering\n\\caption{Latency overhead across datasets. WikiEvents values are estimated.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nDataset & Schema Size & Uncon (s/doc) & Con (s/doc) & Overhead \\% & P95 \\\\\n\\midrule\nSciERC & 7 rels & 4.16 & 4.71 & 13.1\\% & 26.2\\% \\\\\nDocRED & 96 rels & 8.9 & 11.2 & 25.8\\% & 42.0\\% \\\\\nWikiEvents & 56 evt $\\times$ 80 roles & $\\sim$12 & $\\sim$15.8 & $\\sim$32\\% & $\\sim$48\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Error Analysis}\n\\label{sec:error-analysis}\n\nWe analyze 15 representative cases of residual argument constraint (AC) violations and cross-field consistency (CF) patterns from WikiEvents EE and DocRED RE.\n\n\\paragraph{AC Residual Root Causes.}\nOf 15 analyzed AC residual cases, 72\\% stem from semantic confusion between similar entity types (e.g., PER vs. SID vs. SEN in WikiEvents, where these types have overlapping semantic boundaries), 18\\% from genuine annotation ambiguity in the gold labels, and 10\\% from tokenizer-level residuals after BPE collision mitigation. The dominance of semantic confusion confirms that AC residuals are category (b) boundary cases where the model's type distribution concentrates probability mass on semantically adjacent types within the constrained set.\n\n\\paragraph{CF Systematic Patterns.}\nCross-field violations follow five systematic type-pair patterns. The three most frequent are: (1) the same entity assigned PER in one event and SID in another, (2) GPE vs. FAC for location arguments across co-located events, and (3) ORG vs. SID for group entities in Movement vs. Conflict events. These patterns reflect genuine semantic ambiguity in the type system: a person can function as an individual (PER) in one event context and as a member of a side (SID) in another.\n\n\\paragraph{RE Residual Patterns.}\nOn DocRED, three relations account for most residual DR under constrained 70B decoding: P31 (instance\\_of, DR 3--5\\% due to broad domain coverage), P17 (country, edge-case entity types at GPE/LOC boundaries), and P131 (located\\_in, GPE vs. LOC boundary confusion). These are intrinsically ambiguous constraint boundaries rather than method failures.\n\n\\paragraph{Implications.}\nThe error analysis validates the decidability taxonomy: AC residuals correspond to category (b) boundary cases where the constraint is formally decidable but the model's probability distribution straddles the decision boundary. CF violations correspond to category (c) non-local constraints that cannot be enforced during forward-only decoding. Neither finding is unexpected given the theoretical framework, but both provide concrete quantification of the taxonomy's practical boundaries.\n\n\\section{Related Work}\n\n\\paragraph{Constrained Decoding for Structured Generation.}\nGrammar-constrained decoding enforces syntactic validity of generated outputs through CFG-based token masking \\cite{willard2023efficient,geng2024grammarconstrained}. XGrammar extends this to efficient BNF-compiled constraints for JSON schema validation. These approaches handle category (a) constraints in our taxonomy but cannot express cross-field semantic constraints. DOMINO applies type-level constraints for code generation; OntoCoDec extends this paradigm to IE-specific ontology constraints with a stateful semantic layer.\n\n\\paragraph{Information Extraction with LLMs.}\nRecent work applies LLMs to IE tasks including relation extraction and event extraction in zero-shot and few-shot settings. GoLLIE and CodeIE use code-generation frameworks. These approaches rely on prompt-level schema specification and do not enforce output validity at decoding time. InstructUIE and UniEX provide unified IE frameworks but similarly lack constraint enforcement.\n\n\\paragraph{Ontology-Guided IE.}\nClassical IE systems incorporate ontology constraints through pipeline architectures with hard-coded validation. Neural approaches have largely abandoned explicit constraint enforcement in favor of end-to-end learning. OntoCoDec bridges this gap by compiling ontology constraints into decoding-time enforcement compatible with any autoregressive LLM.\n\n\\paragraph{Type Systems for Neural Generation.}\nThe analogy between constrained decoding and type systems has been noted in the code generation literature. Our prefix-decidability taxonomy formalizes this connection for IE, distinguishing enforceable constraints from those requiring fundamentally different approaches (e.g., global consistency passes).\n\n\\section{Conclusion}\n\nWe presented an empirical study of ontology constraint violations in LLM-based information extraction, revealing that violation severity is governed by constraint tightness and task complexity rather than model scale. Our prefix-decidability taxonomy formalizes which constraints are amenable to autoregressive enforcement, and OntoCoDec validates this taxonomy through a composable grammar and semantic constraint system.\n\nKey findings: (1) model scaling from 8B to 70B substantially reduces violations on loose-constraint ontologies but leaves tight-constraint and structurally complex tasks largely unaffected; (2) grammar-only enforcement cannot address context-dependent constraints, necessitating a semantic layer; (3) constrained decoding composes with fine-tuning, providing decoding-time type checking that reduces residual violations from 9.2\\% to 1.9\\%.\n\n\\paragraph{Limitations.}\nOntoCoDec introduces cross-field consistency violations (CF: 1.8--21.1\\%) as a systematic trade-off of per-relation independent type enforcement. This is an inherent limitation of forward-only decoding for category (c) constraints. Future work should explore global entity-type consensus mechanisms (e.g., a post-generation consistency pass) to address CF without sacrificing the composability of the current approach. Additionally, latency overhead scales with schema complexity (13--32\\%), and the current evaluation is limited to English-language IE tasks. The latency scaling behavior for ontologies with hundreds of types has not been empirically characterized.\n\n\\begin{thebibliography}{10}\n\\bibitem{willard2023efficient}\nB.~Willard and R.~Louf.\n\\newblock Efficient guided generation for large language models.\n\\newblock {\\em arXiv preprint arXiv:2307.09702}, 2023.\n\n\\bibitem{geng2024grammarconstrained}\nY.~Geng et~al.\n\\newblock Grammar-constrained decoding for structured {NLP} tasks without finetuning.\n\\newblock In {\\em Proceedings of EMNLP}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b42e43e-42d0-43d2-93f7-6ed5e375f351",
  "isSidechain": false,
  "requestId": "req_011CbAQDnN47qyyY3ALLk64Y",
  "type": "assistant",
  "uuid": "a2fd6477-5f76-4687-a8e2-243856e366cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvNeA4prfqWuGZsCgrXiLt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 47969,
      "output_tokens": 9860,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9860,
          "cache_read_input_tokens": 47969,
          "cache_creation_input_tokens": 512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 512
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

_source line 23 · 2026-05-18T17:10:49.288Z_

<details><summary>↩ Tool result · `toolu_01B5C1ij5UpWtmip2NFcUVue`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2fd6477-5f76-4687-a8e2-243856e366cd",
  "isSidechain": false,
  "promptId": "b88248f5-45f7-484a-873c-8d439b996f3d",
  "type": "user",
  "uuid": "f9719da9-29d6-49e6-b40d-5d01f12dd972",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{definition}{Definition}\n\n\\title{How and When Do LLMs Violate Ontology Constraints? \\\\ An Empirical Study with Decoding-Time Enforcement}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLarge Language Models (LLMs) generate ontology constraint violations at non-trivial rates when performing information extraction (IE), yet the factors governing violation severity remain poorly understood.\nWe present a large-scale empirical study of ontology constraint violations across three IE tasks (relation extraction on SciERC and DocRED, event extraction on WikiEvents), four LLM families (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-70B), and two training regimes (zero-shot and fine-tuned).\nOur analysis reveals that violation severity is determined by the interaction of constraint tightness and task structural complexity, not model scale alone: scaling from 8B to 70B parameters reduces domain/range violations on loose-constraint ontologies (DocRED DR: 26.1\\%$\\to$1.8\\%) but leaves violations on tight-constraint ontologies largely intact (SciERC DR: 13.3\\%$\\to$6.5\\%), while role-of-vocabulary violations in event extraction persist at 64--89\\% regardless of model size.\nWe formalize these observations through a prefix-decidability taxonomy that classifies constraints by their amenability to autoregressive enforcement.\nTo validate the taxonomy, we implement OntoCoDec, a system that compiles ontology schemas into composable grammar and semantic decoding constraints.\nOntoCoDec eliminates vocabulary and structural violations across all configurations, reduces domain/range violations by 83--100\\%, and composes with fine-tuned models to provide decoding-time type checking (total violations: 9.2\\%$\\to$1.9\\% on fine-tuned EE).\nThe method introduces cross-field consistency violations (CF: 1.8--21.1\\%) as a systematic trade-off of per-relation independent enforcement.\n\\end{abstract}\n\n\\section{Introduction}\n\nLLM-based information extraction systems produce structured outputs that must conform to ontology-defined type constraints: relation arguments must have entity types within the relation's domain and range, event arguments must satisfy role-specific entity type restrictions, and all generated types must belong to the target vocabulary. Violations of these constraints render extracted triples unusable for downstream knowledge graph construction and reasoning.\n\nThe prevalence and distribution of such violations, however, have not been systematically characterized. Prior work on constrained decoding for structured generation has focused on syntactic validity (JSON format, grammar compliance) rather than semantic constraint satisfaction. This leaves open a fundamental empirical question: how severe are ontology constraint violations in practice, what determines their severity, and when is decoding-time enforcement necessary versus when does model scaling suffice?\n\nWe address this question through a comprehensive empirical study spanning three IE tasks (relation extraction and event extraction), four model families at two scales (8B and 70B parameters), and two training regimes (zero-shot and fine-tuned). Our study yields three principal findings.\n\nFirst, constraint tightness and task structural complexity jointly determine violation severity, and model scale provides only partial mitigation. On DocRED, a loose-constraint ontology ($\\bar{\\tau}$=0.842) with 96 relation types, scaling from 8B to 70B reduces domain/range violations from 18.5--26.1\\% to 1.8\\%. On SciERC, a tight-constraint ontology ($\\bar{\\tau}$=0.571) with 7 relations, the same scaling reduces violations only from 13.3--15.4\\% to 6.5\\%. On WikiEvents event extraction, role-of-vocabulary violations remain at 64--89\\% across all 8B models, reflecting fundamental structural complexity that scaling alone cannot resolve.\n\nSecond, we formalize the space of enforceable constraints through a prefix-decidability taxonomy that partitions constraints into three categories: (a) purely local constraints decidable from the current token, (b) prefix-decidable constraints requiring generation history, and (c) truly non-local constraints requiring future context. This taxonomy provides theoretical guidance for what decoding-time enforcement can and cannot achieve.\n\nThird, we validate the taxonomy by implementing OntoCoDec, a system that compiles ontology definitions into composable grammar (category a) and semantic (category b) constraint layers. OntoCoDec eliminates vocabulary violations across all configurations and reduces domain/range violations by 83--100\\%, confirming the taxonomy's predictions. The method composes with fine-tuned models, reducing total violations from 9.2\\% to 1.9\\% on event extraction while preserving task performance ($\\Delta$Arg-F1 = $-$0.2pp).\n\nOur contributions are:\n\\begin{itemize}[nosep]\n    \\item A systematic empirical study of ontology constraint violations across tasks, model scales, and training regimes, establishing that constraint tightness and task complexity, not model scale, determine violation severity.\n    \\item A prefix-decidability taxonomy that formally characterizes the space of constraints amenable to autoregressive enforcement.\n    \\item OntoCoDec, a constraint enforcement system that validates the taxonomy and provides decoding-time type checking for neural IE, composable with both zero-shot and fine-tuned models.\n    \\item Quantitative analysis of the cross-field consistency trade-off introduced by per-relation independent enforcement, identifying systematic patterns tied to type system ambiguity.\n\\end{itemize}\n\n\\section{Prefix-Decidability of Ontology Constraints}\n\nWe formalize the conditions under which ontology constraints can be enforced during autoregressive generation.\n\n\\begin{definition}[Ontology Constraint]\nAn ontology constraint $c$ is a predicate over structured outputs $y$ such that $c(y) \\in \\{0, 1\\}$. An output $y$ is \\emph{type-valid} if $c(y) = 1$ for all constraints $c$ in the ontology $\\mathcal{O}$.\n\\end{definition}\n\n\\begin{definition}[Prefix-Decidability]\nA constraint $c$ is \\emph{prefix-decidable at position $t$} if there exists a function $f_c$ such that for any prefix $y_{1:t}$, $f_c(y_{1:t}) = 1$ implies $c(y) = 1$ for all valid completions $y_{t+1:T}$, and $f_c(y_{1:t}) = 0$ implies $c(y) = 0$ for all completions.\n\\end{definition}\n\n\\begin{theorem}[Decidability Trichotomy]\nOntology constraints in IE structured generation partition into three categories:\n\\begin{enumerate}[nosep,label=(\\alph*)]\n    \\item \\textbf{Purely local}: The constraint is decidable from the current token position alone (e.g., ``entity type $\\in$ vocabulary''). These are expressible as context-free grammars.\n    \\item \\textbf{Prefix-decidable with state}: The constraint requires a finite state register tracking previously generated content (e.g., ``argument entity type $\\in$ domain(relation\\_type)'' requires knowing the current relation type from earlier in the generation). These require stateful logit masking.\n    \\item \\textbf{Truly non-local}: The constraint depends on tokens not yet generated (e.g., forward coreference: ``entity $e$ at position $i$ must have the same type as entity $e$ at position $j > i$''). These cannot be enforced during left-to-right decoding without lookahead.\n\\end{enumerate}\n\\end{theorem}\n\n\\begin{proof}[Proof sketch]\nCategory (a) follows from the definition of CFGs: a token-level membership check requires no context. Category (b): the state register is finite (bounded by the ontology size), and the constraint function is computable given the register. Category (c): by construction, the constraint predicate requires $y_j$ with $j > t$, which is unavailable at decoding step $t$. No finite-state augmentation of the decoder can decide such constraints without generating $y_j$ first.\n\\end{proof}\n\nThis taxonomy directly maps to our system architecture: category (a) constraints are handled by a grammar layer (compiled CFG), category (b) by a semantic layer (stateful logit masking with an entity registry), and category (c) constraints (cross-field consistency) remain unenforced, explaining the CF violations observed empirically.\n\n\\section{OntoCoDec: Compiled Ontology Constraints}\n\nOntoCoDec compiles an IE ontology schema $\\mathcal{O}$ into two composable constraint layers applied during autoregressive decoding.\n\n\\subsection{Grammar Layer}\n\nThe grammar layer compiles the ontology's type vocabulary into a context-free grammar (CFG) that constrains the decoder's output to produce syntactically valid JSON with only schema-defined type names. Given an ontology $\\mathcal{O}$ with entity types $\\mathcal{E}$, relation types $\\mathcal{R}$ (for RE) or event types $\\mathcal{V}$ and argument roles $\\mathcal{A}$ (for EE), the compiler generates a CFG where type-name terminals are restricted to $\\mathcal{E} \\cup \\mathcal{R}$ (or $\\mathcal{E} \\cup \\mathcal{V} \\cup \\mathcal{A}$). At each decoding step, the grammar mask $M_{\\text{grammar}}$ zeroes out logits for tokens that would violate the CFG.\n\nThis layer eliminates category (a) violations: entity type vocabulary errors (ET$\\to$0\\%), relation vocabulary errors (RV$\\to$0\\%), and event vocabulary errors (EV$\\to$0\\%).\n\n\\subsection{Semantic Layer}\n\nThe semantic layer maintains a stateful entity registry $\\mathcal{S}$ that tracks (entity mention, entity type) pairs as they are generated. When the decoder reaches a type-constrained position (e.g., the entity type field of a relation argument), the semantic layer computes an allowed-type mask based on the current context:\n\nFor relation extraction, given a relation type $r$ at the current position, the semantic mask is:\n\\[\nM_{\\text{semantic}}(t) = \\{e \\in \\mathcal{E} \\mid e \\in \\text{domain}(r) \\cup \\text{range}(r)\\}\n\\]\n\nFor event extraction, given event type $v$ and argument role $a$:\n\\[\nM_{\\text{semantic}}(t) = \\{e \\in \\mathcal{E} \\mid e \\in \\text{allowed\\_types}(v, a)\\}\n\\]\n\nThis layer enforces category (b) constraints: domain/range violations (DR) and argument constraint violations (AC).\n\n\\subsection{Constraint Composition}\n\nThe two layers compose via bitwise AND of token masks:\n\\[\nM_{\\text{final}}(t) = M_{\\text{grammar}}(t) \\wedge M_{\\text{semantic}}(t)\n\\]\n\nWhen $M_{\\text{final}}(t) = \\emptyset$ (empty intersection), the system falls back to grammar-only constraints ($M_{\\text{grammar}}(t)$), maintaining structural validity as a guaranteed floor. This graceful degradation is critical: on DocRED (96 relation types), fallback occurs approximately 57 times per document for 8B models due to frequent constraint conflicts, explaining residual DR violations under constrained decoding.\n\nThe grammar layer is a prerequisite for the semantic layer, not a symmetric complement. Without grammar enforcement, the semantic layer encounters out-of-vocabulary relation types for which no domain/range rules exist, rendering it ineffective (semantic-only achieves only 24\\% DR reduction vs. the full system's 94\\%).\n\n\\section{Experiments}\n\nWe evaluate across three IE tasks, four model families, and two training regimes. All experiments use greedy decoding. F1 scores are computed using the all\\_set matching criterion. We report five violation types: entity type (ET), relation/event vocabulary (RV/EV), domain/range (DR), role-of-vocabulary (RoV), argument constraint (AC), and cross-field consistency (CF).\n\n\\subsection{Violation Landscape Across Model Scales}\n\nWe compare ontology constraint violations between 8B-parameter models (Qwen3-8B, Llama-3.1-8B) and a 70B-parameter model (Llama-3.1-70B-Instruct, AWQ-INT4 quantized) on relation extraction.\n\n\\paragraph{SciERC (7 relation types, $\\bar{\\tau}$=0.571).}\nTable~\\ref{tab:70b-scierc} shows violation rates across scales. Scaling from 8B to 70B reduces unconstrained DR from 13.3--15.4\\% to 6.5\\%, a 50--58\\% relative reduction. OntoCoDec eliminates the remaining violations completely (DR: 6.5\\%$\\to$0.0\\%, $\\Delta$=100\\%), with R-F1 change of +0.02pp (within noise). At 8B scale, OntoCoDec achieves 94--99\\% DR reduction with comparable F1 neutrality.\n\nThe 70B unconstrained DR of 6.5\\% corresponds to 97 triples with structural violations in the 551-document corpus. While model scaling substantially reduces violation rates, the residual violations concentrate on tight-constraint relations (Feature-of: $\\tau$=0.143, Compare: $\\tau$=0.194), confirming that constraint tightness, not model capability, is the binding factor.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-scale violation comparison on SciERC. DR\\%$\\downarrow$ shows unconstrained$\\to$constrained (relative reduction). CF\\% is constrained-only.}\n\\label{tab:70b-scierc}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Scale & DR\\%$\\downarrow$ & RV\\% & ET\\% & CF\\% & $\\Delta$R-F1 \\\\\n\\midrule\nQwen3-8B & 8B & 15.4$\\to$0.93 (94\\%) & 1.39$\\to$0 & 0.40$\\to$0 & 9.90 & +0.13 \\\\\nLlama-3.1-8B & 8B & 13.3$\\to$0.08 (99\\%) & 0.55$\\to$0 & 0$\\to$0 & 6.56 & $-$0.14 \\\\\nLlama-3.1-70B & 70B & 6.50$\\to$0.00 (100\\%) & 0.60$\\to$0 & 0$\\to$0 & 3.66 & +0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{DocRED (96 relation types, $\\bar{\\tau}$=0.842).}\nTable~\\ref{tab:70b-docred-trajectory} presents the cross-scale DR trajectory. The loose-constraint DocRED ontology shows a dramatically different scaling pattern: 70B unconstrained DR is only 1.8\\%, compared to 18.5\\% (Qwen-8B) and 26.1\\% (Llama-8B). Model scaling reduces DocRED violations by 86--93\\% without any method intervention.\n\nOntoCoDec further reduces 70B DocRED DR from 1.8\\% to 0.3\\% (83.3\\% relative reduction, 1.5pp absolute). Table~\\ref{tab:70b-docred-profile} shows the full violation profile. The absolute improvement of 1.5pp is modest: on 17,200 total triples, this corresponds to approximately 265$\\to$44 violating triples. The method simultaneously introduces CF violations (0.04\\%$\\to$3.8\\%), creating a new violation category while resolving a diminishing one.\n\nThis result is a positive finding for the violation landscape study: it confirms that loose-constraint ontologies combined with large models produce minimal violations, while tight-constraint ontologies and structurally complex tasks (Section~\\ref{sec:ee}) require enforcement regardless of scale.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-scale DR trajectory on DocRED.}\n\\label{tab:70b-docred-trajectory}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Uncon DR\\% & Con DR\\% & Abs. $\\Delta$ & Rel. $\\downarrow$\\% & $\\Delta$R-F1 \\\\\n\\midrule\nQwen3-8B & 18.46 & 10.21 & 8.25pp & 44.7 & +0.50 \\\\\nLlama-3.1-8B & 26.07 & 2.55 & 23.5pp & 90.2 & +0.29 \\\\\nLlama-3.1-70B & 1.80 & 0.30 & 1.50pp & 83.3 & $-$0.20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Full violation profile for Llama-3.1-70B on DocRED.}\n\\label{tab:70b-docred-profile}\n\\small\n\\begin{tabular}{lcccccccc}\n\\toprule\nCondition & ET\\% & RV\\% & DR\\% & CF\\% & E-F1 & R-F1 & Parse\\% \\\\\n\\midrule\n70B unconstrained & 0.0 & 2.3 & 1.8 & 0.04 & 64.2 & 10.1 & 97.9 \\\\\n70B constrained & 0.0 & 0.0 & 0.3 & 3.8 & 64.0 & 9.9 & 97.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Task Generalization: Event Extraction}\n\\label{sec:ee}\n\nWe evaluate OntoCoDec on WikiEvents event extraction (56 event types, 80 argument roles, 27 entity types, 245 role$\\to$entity type constraints). Event extraction presents a structurally more complex constraint space than relation extraction: each event type defines which argument roles are permitted and which entity types each role accepts.\n\n\\paragraph{Grammar-Only Ablation.}\nTable~\\ref{tab:grammar-ablation} presents the grammar-only ablation across three 8B models. Grammar enforcement eliminates event vocabulary violations (EV$\\to$0\\%) across all models but leaves role-of-vocabulary violations at 64--77\\%. This confirms that grammar CFGs cannot express context-dependent constraints (which roles are valid depends on the current event type), validating the necessity of the semantic layer for category (b) constraints.\n\nUnder grammar-only decoding, argument constraint violations rise to 8.4--13.8\\%. This is a latent violation surfacing effect: grammar forces the model to produce valid event type names, which enables the violation checker to evaluate role constraints that were previously masked by invalid event types. The same pattern appears in relation extraction, where grammar enforcement exposes latent DR violations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Grammar-only ablation on WikiEvents event extraction (3 models, 8B scale). Full S1 rows are constrained with both grammar and semantic layers.}\n\\label{tab:grammar-ablation}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nModel / Condition & EV\\% & RoV\\% & AC\\% & CF\\% & Ent-F1 \\\\\n\\midrule\nQwen3-8B grammar-only & 0 & 71.5 & 8.4 & 0.2 & 0.5 \\\\\nLlama-3.1-8B grammar-only & 0 & 77.2 & 11.6 & 0.1 & 1.2 \\\\\nMistral-7B grammar-only & 0 & 64.0 & 13.8 & 1.1 & 11.9 \\\\\n\\midrule\nQwen3-8B full S1 & 0 & 0 & 2.1 & 21.1 & 14.1 \\\\\nLlama-3.1-8B full S1 & 0 & 0 & 3.8 & 17.2 & 17.6 \\\\\nMistral-7B full S1 & 0 & 0 & 1.3 & 14.9 & 11.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RoV as the Critical EE Violation.}\nRole-of-vocabulary violations in EE (64--89\\% unconstrained) are 3--5$\\times$ higher than relation vocabulary violations in RE (1--30\\%). This disparity reflects the structural complexity difference: EE requires context-dependent role assignment conditioned on event type, while RE relation names are drawn from a flat vocabulary. The persistence of high RoV rates across all 8B models, combined with the grammar layer's inability to address them, provides the strongest evidence that semantic-layer enforcement is necessary for structurally complex IE tasks.\n\n\\subsection{Fine-Tuning Composability}\n\\label{sec:ft}\n\nA practical question is whether decoding-time constraint enforcement remains useful when the model has been fine-tuned on task-specific data. Table~\\ref{tab:ft-composability} compares fine-tuned Qwen3-8B with and without OntoCoDec on WikiEvents event extraction.\n\nFine-tuning dramatically reduces violations compared to zero-shot (total violations: 9.2\\% vs. $>$99\\% unconstrained zero-shot). OntoCoDec further reduces total violations from 9.2\\% to 1.9\\%, eliminating all remaining EV and RoV violations and reducing AC from 0.4\\% to 0.1\\%. Task performance is preserved: trigger F1 changes by $-$0.2pp and argument F1 by $-$0.2pp, both within noise.\n\nThe CF trade-off is substantially mitigated in the fine-tuned regime: CF rises from 0.1\\% to 1.8\\% (vs. 0\\%$\\to$14--21\\% in zero-shot). Fine-tuned models produce more internally consistent type assignments, reducing the cross-event type drift that drives CF violations.\n\nThis result supports the framing of OntoCoDec as decoding-time type checking for neural generation: analogous to static type systems in programming languages, it provides compile-time guarantees regardless of the underlying model's training, catching residual violations that fine-tuning reduces but does not eliminate.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning composability on WikiEvents EE (Qwen3-8B). ZS = zero-shot reference.}\n\\label{tab:ft-composability}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & EV\\% & RoV\\% & AC\\% & CF\\% & Trig-F1 & Arg-F1 & Ent-F1 \\\\\n\\midrule\nFT unconstrained & 0.5 & 8.2 & 0.4 & 0.1 & 62.5 & 38.0 & 71.3 \\\\\nFT constrained & 0.0 & 0.0 & 0.1 & 1.8 & 62.3 & 37.8 & 71.0 \\\\\n\\midrule\nZS unconstrained & 24.0 & 74.9 & 0.3 & 0.0 & 11.8 & 0.1 & 0.0 \\\\\nZS constrained & 0.0 & 0.0 & 2.1 & 21.1 & 13.4 & 1.7 & 14.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Statistical Significance}\n\nTable~\\ref{tab:bootstrap-ci} reports bootstrap confidence intervals (10,000 iterations) for EE F1 changes under constrained decoding.\n\nTrigger F1 improvements (+1.50 to +1.76pp) are not statistically significant for any model (all $p > 0.05$, CIs spanning zero). Entity F1 improvements (+11.7 to +17.6pp) are significant ($p < 0.001$) for all models, but this reflects format compliance rather than semantic improvement: unconstrained entity F1 is 0\\% because the parser cannot extract entities from outputs containing non-schema type names. Grammar enforcement restores parseable output, and the entity F1 gain measures parser compatibility, not extraction quality.\n\nArgument F1 is too low in the zero-shot setting (0.1--1.7\\%) for meaningful confidence interval estimation; bootstrap variance at this scale exceeds the point estimates.\n\n\\begin{table}[t]\n\\centering\n\\caption{Bootstrap CI (10,000 iterations) for WikiEvents EE F1 changes (constrained $-$ unconstrained). $^*$Significance reflects format compliance, not semantic improvement.}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Metric & $\\Delta$ (pp) & 95\\% CI & $p$ & Sig.? \\\\\n\\midrule\nQwen3-8B & Trigger F1 & +1.55 & [$-$0.2, +3.3] & 0.08 & No \\\\\nQwen3-8B & Entity F1 & +14.09 & [+10.5, +17.8] & $<$0.001 & Yes$^*$ \\\\\nLlama-3.1-8B & Trigger F1 & +1.76 & [$-$0.5, +4.0] & 0.12 & No \\\\\nLlama-3.1-8B & Entity F1 & +17.63 & [+13.8, +21.5] & $<$0.001 & Yes$^*$ \\\\\nMistral-7B & Trigger F1 & +1.50 & [$-$0.6, +3.6] & 0.15 & No \\\\\nMistral-7B & Entity F1 & +11.71 & [+8.2, +15.2] & $<$0.001 & Yes$^*$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Latency Overhead}\n\nTable~\\ref{tab:latency} reports wall-clock latency overhead of constrained decoding. Overhead scales with schema complexity: 13.1\\% on SciERC (7 relations), 25.8\\% on DocRED (96 relations), and an estimated 32\\% on WikiEvents (56 event types $\\times$ 80 roles). The overhead arises primarily from semantic mask computation at type-token positions; free-text tokens incur no additional cost. P95 per-document overhead reaches 42\\% on DocRED due to documents with large entity registries.\n\n\\begin{table}[t]\n\\centering\n\\caption{Latency overhead across datasets. WikiEvents values are estimated.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nDataset & Schema Size & Uncon (s/doc) & Con (s/doc) & Overhead \\% & P95 \\\\\n\\midrule\nSciERC & 7 rels & 4.16 & 4.71 & 13.1\\% & 26.2\\% \\\\\nDocRED & 96 rels & 8.9 & 11.2 & 25.8\\% & 42.0\\% \\\\\nWikiEvents & 56 evt $\\times$ 80 roles & $\\sim$12 & $\\sim$15.8 & $\\sim$32\\% & $\\sim$48\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Error Analysis}\n\\label{sec:error-analysis}\n\nWe analyze 15 representative cases of residual argument constraint (AC) violations and cross-field consistency (CF) patterns from WikiEvents EE and DocRED RE.\n\n\\paragraph{AC Residual Root Causes.}\nOf 15 analyzed AC residual cases, 72\\% stem from semantic confusion between similar entity types (e.g., PER vs. SID vs. SEN in WikiEvents, where these types have overlapping semantic boundaries), 18\\% from genuine annotation ambiguity in the gold labels, and 10\\% from tokenizer-level residuals after BPE collision mitigation. The dominance of semantic confusion confirms that AC residuals are category (b) boundary cases where the model's type distribution concentrates probability mass on semantically adjacent types within the constrained set.\n\n\\paragraph{CF Systematic Patterns.}\nCross-field violations follow five systematic type-pair patterns. The three most frequent are: (1) the same entity assigned PER in one event and SID in another, (2) GPE vs. FAC for location arguments across co-located events, and (3) ORG vs. SID for group entities in Movement vs. Conflict events. These patterns reflect genuine semantic ambiguity in the type system: a person can function as an individual (PER) in one event context and as a member of a side (SID) in another.\n\n\\paragraph{RE Residual Patterns.}\nOn DocRED, three relations account for most residual DR under constrained 70B decoding: P31 (instance\\_of, DR 3--5\\% due to broad domain coverage), P17 (country, edge-case entity types at GPE/LOC boundaries), and P131 (located\\_in, GPE vs. LOC boundary confusion). These are intrinsically ambiguous constraint boundaries rather than method failures.\n\n\\paragraph{Implications.}\nThe error analysis validates the decidability taxonomy: AC residuals correspond to category (b) boundary cases where the constraint is formally decidable but the model's probability distribution straddles the decision boundary. CF violations correspond to category (c) non-local constraints that cannot be enforced during forward-only decoding. Neither finding is unexpected given the theoretical framework, but both provide concrete quantification of the taxonomy's practical boundaries.\n\n\\section{Related Work}\n\n\\paragraph{Constrained Decoding for Structured Generation.}\nGrammar-constrained decoding enforces syntactic validity of generated outputs through CFG-based token masking \\cite{willard2023efficient,geng2024grammarconstrained}. XGrammar extends this to efficient BNF-compiled constraints for JSON schema validation. These approaches handle category (a) constraints in our taxonomy but cannot express cross-field semantic constraints. DOMINO applies type-level constraints for code generation; OntoCoDec extends this paradigm to IE-specific ontology constraints with a stateful semantic layer.\n\n\\paragraph{Information Extraction with LLMs.}\nRecent work applies LLMs to IE tasks including relation extraction and event extraction in zero-shot and few-shot settings. GoLLIE and CodeIE use code-generation frameworks. These approaches rely on prompt-level schema specification and do not enforce output validity at decoding time. InstructUIE and UniEX provide unified IE frameworks but similarly lack constraint enforcement.\n\n\\paragraph{Ontology-Guided IE.}\nClassical IE systems incorporate ontology constraints through pipeline architectures with hard-coded validation. Neural approaches have largely abandoned explicit constraint enforcement in favor of end-to-end learning. OntoCoDec bridges this gap by compiling ontology constraints into decoding-time enforcement compatible with any autoregressive LLM.\n\n\\paragraph{Type Systems for Neural Generation.}\nThe analogy between constrained decoding and type systems has been noted in the code generation literature. Our prefix-decidability taxonomy formalizes this connection for IE, distinguishing enforceable constraints from those requiring fundamentally different approaches (e.g., global consistency passes).\n\n\\section{Conclusion}\n\nWe presented an empirical study of ontology constraint violations in LLM-based information extraction, revealing that violation severity is governed by constraint tightness and task complexity rather than model scale. Our prefix-decidability taxonomy formalizes which constraints are amenable to autoregressive enforcement, and OntoCoDec validates this taxonomy through a composable grammar and semantic constraint system.\n\nKey findings: (1) model scaling from 8B to 70B substantially reduces violations on loose-constraint ontologies but leaves tight-constraint and structurally complex tasks largely unaffected; (2) grammar-only enforcement cannot address context-dependent constraints, necessitating a semantic layer; (3) constrained decoding composes with fine-tuning, providing decoding-time type checking that reduces residual violations from 9.2\\% to 1.9\\%.\n\n\\paragraph{Limitations.}\nOntoCoDec introduces cross-field consistency violations (CF: 1.8--21.1\\%) as a systematic trade-off of per-relation independent type enforcement. This is an inherent limitation of forward-only decoding for category (c) constraints. Future work should explore global entity-type consensus mechanisms (e.g., a post-generation consistency pass) to address CF without sacrificing the composability of the current approach. Additionally, latency overhead scales with schema complexity (13--32\\%), and the current evaluation is limited to English-language IE tasks. The latency scaling behavior for ontologies with hundreds of types has not been empirically characterized.\n\n\\begin{thebibliography}{10}\n\\bibitem{willard2023efficient}\nB.~Willard and R.~Louf.\n\\newblock Efficient guided generation for large language models.\n\\newblock {\\em arXiv preprint arXiv:2307.09702}, 2023.\n\n\\bibitem{geng2024grammarconstrained}\nY.~Geng et~al.\n\\newblock Grammar-constrained decoding for structured {NLP} tasks without finetuning.\n\\newblock In {\\em Proceedings of EMNLP}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "a2fd6477-5f76-4687-a8e2-243856e366cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "f9719da9-29d6-49e6-b40d-5d01f12dd972",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier empirical research paper on schema-constrained IE",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Tool call

_source line 26 · 2026-05-18T17:10:52.764Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011nMu5qRgDNuxubTDJzMEEr`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9719da9-29d6-49e6-b40d-5d01f12dd972",
  "isSidechain": false,
  "requestId": "req_011CbAQUn8q7ufs9RPVngcb6",
  "type": "assistant",
  "uuid": "b39cd726-e46f-4811-b11e-a3dcea179df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DtbkbovAH9XMkks4XdgDo6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9924,
      "cache_read_input_tokens": 48481,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 48481,
          "cache_creation_input_tokens": 9924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9924
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

_source line 27 · 2026-05-18T17:10:54.317Z_

<details><summary>↩ Tool result · `toolu_011nMu5qRgDNuxubTDJzMEEr`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty)
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (3.09291pt too wide) in paragraph at lines 51--52
[]\T1/cmr/m/n/10.95 A prefix-decidability tax-on-omy that for-mally char-ac-ter
-izes the space of con-straints amenable
[2] [3]

LaTeX Warning: Reference `tab:70b-scierc' on page 4 undefined on input line 129
.


LaTeX Warning: Reference `tab:70b-docred-trajectory' on page 4 undefined on inp
ut line 150.


LaTeX Warning: Reference `tab:70b-docred-profile' on page 4 undefined on input 
line 152.


LaTeX Warning: Reference `sec:ee' on page 4 undefined on input line 154.


Overfull \hbox (9.90059pt too wide) in paragraph at lines 154--155
\T1/cmr/m/n/10.95 constraint on-tolo-gies com-bined with large mod-els pro-duce
 min-i-mal vi-o-la-tions, while tight-constraint
[4]

LaTeX Warning: Reference `tab:grammar-ablation' on page 5 undefined on input li
ne 193.


LaTeX Warning: Reference `tab:ft-composability' on page 5 undefined on input li
ne 223.

[5]

LaTeX Warning: Reference `tab:bootstrap-ci' on page 6 undefined on input line 2
51.


LaTeX Warning: Reference `tab:latency' on page 6 undefined on input line 278.

[6]

LaTeX Warning: Citation `willard2023efficient' on page 7 undefined on input lin
e 316.


LaTeX Warning: Citation `geng2024grammarconstrained' on page 7 undefined on inp
ut line 316.

[7] [8] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbi1095
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbi1095
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbi1095.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbi.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf
 Ok [25] [26] [27] [28] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf
 Ok) ) ) )
(some charht values had to be adjusted by as much as 0.079pt)
Font metrics written on ecbi1095.tfm.
Output written on ecbi1095.600gf (256 characters, 57548 bytes).
Transcript written on ecbi1095.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbi1095.600pk: successfully generated.
 &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbi1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (8 pages, 219720 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty)
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
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
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (3.09291pt too wide) in paragraph at lines 51--52
[]\T1/cmr/m/n/10.95 A prefix-decidability tax-on-omy that for-mally char-ac-ter
-izes the space of con-straints amenable
[2] [3]
Overfull \hbox (9.90059pt too wide) in paragraph at lines 154--155
\T1/cmr/m/n/10.95 constraint on-tolo-gies com-bined with large mod-els pro-duce
 min-i-mal vi-o-la-tions, while tight-constraint
[4] [5] [6] [7] [8] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbi1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (8 pages, 220746 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b39cd726-e46f-4811-b11e-a3dcea179df6",
  "isSidechain": false,
  "promptId": "b88248f5-45f7-484a-873c-8d439b996f3d",
  "type": "user",
  "uuid": "975dab26-92d6-4b97-9a0c-993ac0dab243",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (3.09291pt too wide) in paragraph at lines 51--52\n[]\\T1/cmr/m/n/10.95 A prefix-decidability tax-on-omy that for-mally char-ac-ter\n-izes the space of con-straints amenable\n[2] [3]\n\nLaTeX Warning: Reference `tab:70b-scierc' on page 4 undefined on input line 129\n.\n\n\nLaTeX Warning: Reference `tab:70b-docred-trajectory' on page 4 undefined on inp\nut line 150.\n\n\nLaTeX Warning: Reference `tab:70b-docred-profile' on page 4 undefined on input \nline 152.\n\n\nLaTeX Warning: Reference `sec:ee' on page 4 undefined on input line 154.\n\n\nOverfull \\hbox (9.90059pt too wide) in paragraph at lines 154--155\n\\T1/cmr/m/n/10.95 constraint on-tolo-gies com-bined with large mod-els pro-duce\n min-i-mal vi-o-la-tions, while tight-constraint\n[4]\n\nLaTeX Warning: Reference `tab:grammar-ablation' on page 5 undefined on input li\nne 193.\n\n\nLaTeX Warning: Reference `tab:ft-composability' on page 5 undefined on input li\nne 223.\n\n[5]\n\nLaTeX Warning: Reference `tab:bootstrap-ci' on page 6 undefined on input line 2\n51.\n\n\nLaTeX Warning: Reference `tab:latency' on page 6 undefined on input line 278.\n\n[6]\n\nLaTeX Warning: Citation `willard2023efficient' on page 7 undefined on input lin\ne 316.\n\n\nLaTeX Warning: Citation `geng2024grammarconstrained' on page 7 undefined on inp\nut line 316.\n\n[7] [8] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbi1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbi1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbi1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbi.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.079pt)\nFont metrics written on ecbi1095.tfm.\nOutput written on ecbi1095.600gf (256 characters, 57548 bytes).\nTranscript written on ecbi1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbi1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbi1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (8 pages, 219720 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (3.09291pt too wide) in paragraph at lines 51--52\n[]\\T1/cmr/m/n/10.95 A prefix-decidability tax-on-omy that for-mally char-ac-ter\n-izes the space of con-straints amenable\n[2] [3]\nOverfull \\hbox (9.90059pt too wide) in paragraph at lines 154--155\n\\T1/cmr/m/n/10.95 constraint on-tolo-gies com-bined with large mod-els pro-duce\n min-i-mal vi-o-la-tions, while tight-constraint\n[4] [5] [6] [7] [8] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbi1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (8 pages, 220746 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b39cd726-e46f-4811-b11e-a3dcea179df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "975dab26-92d6-4b97-9a0c-993ac0dab243",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier empirical research paper on schema-constrained IE",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Assistant

_source line 30 · 2026-05-18T17:11:03.048Z_

PDF compiled successfully (8 pages, no errors). All cross-references resolved on the second pass.

The paper covers all 7 experiments from `experiment_data.json`:
- **Table 1**: 70B SciERC cross-scale comparison
- **Tables 2-3**: 70B DocRED trajectory + full violation profile
- **Table 4**: Grammar-only ablation (3 models, EE)
- **Table 5**: FT composability (WikiEvents EE)
- **Table 6**: Bootstrap CI for EE metrics
- **Table 7**: Latency overhead
- **Section 5.7**: Error analysis (AC root causes, CF patterns, RE residuals)

Framed as "empirical study with method validation" per the narrative guidance, with the violation landscape as the primary contribution, prefix-decidability formalized as a theorem, and FT composability positioned as the practical selling point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "975dab26-92d6-4b97-9a0c-993ac0dab243",
  "isSidechain": false,
  "requestId": "req_011CbAQV9cQSQJR4Ntn1Bu7i",
  "type": "assistant",
  "uuid": "7c8b79d6-e94c-498e-965e-9cb076527345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260518T162745/worst",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMBkE9xarFyx4WKd4a5bxq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8018,
      "cache_read_input_tokens": 58405,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 58405,
          "cache_creation_input_tokens": 8018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8018
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162745 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_c…",
  "leafUuid": "7c8b79d6-e94c-498e-965e-9cb076527345",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier empirical research paper on schema-constrained IE",
  "sessionId": "59dbf90d-a03d-487e-aec5-135e784bb958"
}
```

---
