# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T041241 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/0cda8650-bf31-48c3-8c08-b58fe1671149.jsonl`
- **Structured JSON:** [`79c49e5110032001ba26.json`](../../sessions/79/79c49e5110032001ba26.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T05:06:42.220Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T05:06:42.220Z",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T041241 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：C3 layer effect 完全不成立 (pooled p>0.10)，C4 interaction 虽 omnibus 显著但由 Claude 单一 outlier 驱动（移除后 p>0.20），perturbation control 暴露 14pp confound (verdict CONDITIONAL, ratio=0.56, borderline WARNING)，judge calibration κ=0.58 / F1=0.68 整体偏低且 type-specific bias 严重。需根本性 reframe：放弃 'Differential Nocuity' 和 layer hierarchy，围绕 C1 (universal nocuity, 即使有 perturbation caveat 仍 Δ_net≥10pp) + C2 (6-type taxonomy 作为 diagnostic tool, 非 severity ranking) + C5 (Ambiguity Blindness, 14% awareness / 78% surface adoption) 构建叙事。Title 改为 'Policy Ambiguity Is Universally Nocuous for LLM Agents: A Causal Study with Type-Level Taxonomy'。 核心叙事转向：ambiguity 不是唯一 sensitivity factor (perturbation 也造成 14pp increase)， 但仍是最大的单一 factor (Δ_net≈12pp 且 type-structured)；taxonomy 的价值从 severity prediction 转为 diagnostic vocabulary (帮助识别和描述 failure 而非 rank risk)； Ambiguity Blindness 从 secondary 升为 co-primary 贡献 (universal across all 5 models, 所有 types)。仍冲 EMNLP，taxonomy framework + causal design (with caveat) + Blindness empirical finding = solid 3-contribution paper，但 novelty claim 弱于 best/median。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T05:06:42.223Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T05:06:42.223Z",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

## Round 1

48 recorded events

### User

_source line 3 · 2026-05-21T05:06:42.242Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T041241 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：C3 layer effect 完全不成立 (pooled p>0.10)，C4 interaction 虽 omnibus 显著但由 Claude 单一 outlier 驱动（移除后 p>0.20），perturbation control 暴露 14pp confound (verdict CONDITIONAL, ratio=0.56, borderline WARNING)，judge calibration κ=0.58 / F1=0.68 整体偏低且 type-specific bias 严重。需根本性 reframe：放弃 'Differential Nocuity' 和 layer hierarchy，围绕 C1 (universal nocuity, 即使有 perturbation caveat 仍 Δ_net≥10pp) + C2 (6-type taxonomy 作为 diagnostic tool, 非 severity ranking) + C5 (Ambiguity Blindness, 14% awareness / 78% surface adoption) 构建叙事。Title 改为 'Policy Ambiguity Is Universally Nocuous for LLM Agents: A Causal Study with Type-Level Taxonomy'。 核心叙事转向：ambiguity 不是唯一 sensitivity factor (perturbation 也造成 14pp increase)， 但仍是最大的单一 factor (Δ_net≈12pp 且 type-structured)；taxonomy 的价值从 severity prediction 转为 diagnostic vocabulary (帮助识别和描述 failure 而非 rank risk)； Ambiguity Blindness 从 secondary 升为 co-primary 贡献 (universal across all 5 models, 所有 types)。仍冲 EMNLP，taxonomy framework + causal design (with caveat) + Blindness empirical finding = solid 3-contribution paper，但 novelty claim 弱于 best/median。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "66af4deb-494c-492e-8647-b9e7700a9ab2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T05:06:42.241Z_

```json
{
  "parentUuid": "66af4deb-494c-492e-8647-b9e7700a9ab2",
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
  "uuid": "0f6a937e-c870-496d-a53a-2ee74d72f5b9",
  "timestamp": "2026-05-21T05:06:42.241Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T05:06:42.241Z_

```json
{
  "parentUuid": "0f6a937e-c870-496d-a53a-2ee74d72f5b9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "702f363d-fd97-4339-99f5-caad5d318807",
  "timestamp": "2026-05-21T05:06:42.241Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
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
  "aiTitle": "Generate worst-tier mock paper for policy ambiguity study",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Assistant

_source line 7 · 2026-05-21T05:06:44.399Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "702f363d-fd97-4339-99f5-caad5d318807",
  "isSidechain": false,
  "requestId": "req_011CbF8gs5y9BVHNfWvW2fyj",
  "type": "assistant",
  "uuid": "fb7c3e69-44aa-46ac-bb5e-4ec29a11e316",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ao7w4n5uBxe3jnPxWFdRLu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12006,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12006
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

_source line 8 · 2026-05-21T05:06:45.502Z_

<details open><summary>🔧 Tool call — Read · `toolu_012nsifQZgwu6aySEw48bFgq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb7c3e69-44aa-46ac-bb5e-4ec29a11e316",
  "isSidechain": false,
  "requestId": "req_011CbF8gs5y9BVHNfWvW2fyj",
  "type": "assistant",
  "uuid": "aa1da51f-7d38-4dd4-b118-70b10cf538ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ao7w4n5uBxe3jnPxWFdRLu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12006,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12006
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

_source line 9 · 2026-05-21T05:06:45.779Z_

<details><summary>↩ Tool result · `toolu_012nsifQZgwu6aySEw48bFgq`</summary>

```text
1	[
2	  {
3	    "name": "full_study_clause_generation",
4	    "description": "生成 140 新 clause pairs (coreferential 50, auth_scope 50, lexical +20, incompleteness +20)，补全 6 types × 50 pairs = 300 对。混合 CP 格式 (labeled + unlabeled)。Chantree-style 质量验证。\n",
5	    "results": {
6	      "total_pairs": 300,
7	      "pairs_per_type": 50,
8	      "cp_labeled_ratio": 0.5,
9	      "quality_pass_rate": 0.91,
10	      "avg_token_delta_amb_vs_unamb": 3.9,
11	      "coreferential_revision_rounds": 3,
12	      "auth_scope_revision_rounds": 2,
13	      "per_type_quality": {
14	        "auth_scope_pass_rate": 0.9,
15	        "incompleteness_pass_rate": 0.94,
16	        "conditional_polysemy_pass_rate": 0.96,
17	        "scopal_pass_rate": 0.95,
18	        "lexical_pass_rate": 0.93,
19	        "coreferential_pass_rate": 0.86
20	      }
21	    },
22	    "tables": [
23	      {
24	        "name": "Clause Pair Statistics by Type",
25	        "columns": [
26	          "type",
27	          "n_pairs",
28	          "avg_amb_tokens",
29	          "avg_unamb_tokens",
30	          "token_delta",
31	          "quality_pass_rate"
32	        ],
33	        "rows": [
34	          [
35	            "auth_scope",
36	            50,
37	            28.3,
38	            32.2,
39	            3.9,
40	            0.9
41	          ],
42	          [
43	            "incompleteness",
44	            50,
45	            26.8,
46	            30.6,
47	            3.8,
48	            0.94
49	          ],
50	          [
51	            "conditional_polysemy",
52	            50,
53	            24.1,
54	            25.7,
55	            1.6,
56	            0.96
57	          ],
58	          [
59	            "scopal",
60	            50,
61	            22.6,
62	            24.0,
63	            1.4,
64	            0.95
65	          ],
66	          [
67	            "lexical",
68	            50,
69	            21.9,
70	            23.2,
71	            1.3,
72	            0.93
73	          ],
74	          [
75	            "coreferential",
76	            50,
77	            25.2,
78	            27.5,
79	            2.3,
80	            0.86
81	          ]
82	        ]
83	      }
84	    ],
85	    "figures": [],
86	    "analysis": "Coreferential 低 pass_rate (0.86) 是 worst tier 的早期信号——该 type 的 clause design 困难度高于预期，直接传导至 plan_009 judge calibration 中 coreferential F1 最低 (0.62)。Token delta 的 layer asymmetry (spec 3.9 vs ling 1.6) 在 plan_004 中被 report 为 control variable，partial correlation 后不构成 independent confound，但 reviewer 会 flag。\n\n\nClause 生成阶段本身不受 worst tier 影响——是数据准备而非结果观测。但 quality_pass_rate 91% 而非 >95% 预示后续 measurement problems： (a) Coreferential pass_rate 最低 (0.86) 因 RC attachment 与 scopal 边界 重叠 (RC8 concerns)，2/5 pilot clauses 触发 conservative_refusal 而非 violation，需 3 轮修订仍有残余质量问题；(b) Auth_scope 0.90 因与 incompleteness 的 operational distinction 要求精细控制 (RC9)，部分 clause 的 \"ambiguous permission boundary\" 与 \"missing permission specification\" 难以 cleanly separate；(c) token delta spec-layer (3.9) > ling-layer (1.6) 是 potential confound——spec-layer 的 disambiguation 系统性需要更多 tokens， 这不是 clause 质量问题而是 inherent asymmetry，但在 worst tier 下被 reviewer 质疑为 information asymmetry confound。这些 clause 层面的质量差异 在后续 judge calibration (plan_009) 中以 type-specific F1 下降的形式放大。\n"
87	  },
88	  {
89	    "name": "new_type_mini_pilot",
90	    "description": "Coreferential + auth_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4) = 20 episodes。验证新类型基本可行性。\n",
91	    "results": {
92	      "coreferential_amb_violation_rate": 0.4,
93	      "coreferential_unamb_violation_rate": 0.0,
94	      "auth_scope_amb_violation_rate": 0.6,
95	      "auth_scope_unamb_violation_rate": 0.0,
96	      "coreferential_binary_effect_pp": 40,
97	      "auth_scope_binary_effect_pp": 60,
98	      "systematic_issues_found": true,
99	      "issues_detail": "2/5 coreferential clauses 触发 conservative refusal 而非 violation; 1/5 auth_scope unambiguous 版本仍残余歧义 (需收紧)\n"
100	    },
101	    "tables": [
102	      {
103	        "name": "Mini-Pilot Results",
104	        "columns": [
105	          "type",
106	          "condition",
107	          "n",
108	          "violations",
109	          "rate"
110	        ],
111	        "rows": [
112	          [
113	            "coreferential",
114	            "ambiguous",
115	            5,
116	            2,
117	            "40%"
118	          ],
119	          [
120	            "coreferential",
121	            "unambiguous",
122	            5,
123	            0,
124	            "0%"
125	          ],
126	          [
127	            "auth_scope",
128	            "ambiguous",
129	            5,
130	            3,
131	            "60%"
132	          ],
133	          [
134	            "auth_scope",
135	            "unambiguous",
136	            5,
137	            0,
138	            "0%"
139	          ]
140	        ]
141	      }
142	    ],
143	    "figures": [],
144	    "analysis": "Mini-pilot 的 \"go\" 信号在 worst tier 下是 misleading confidence。 gpt-5.4 单模型验证对 multi-model study 的预测力有限——尤其无法预见 Claude 的 auth_scope 反转 (16%) 和 perturbation control 的 CONDITIONAL verdict。理想做法是 ≥2 model families 的 mini-pilot。\n\n\nMini-pilot 在 gpt-5.4 上给出 \"go\" 信号——两个新 type 均触发 violations， control < 15%。但这是 worst tier 的隐患起点：(a) gpt-5.4 的 auth_scope 60% 看似 confirm spec-layer 危险性高，但 N=5 的 CI 极宽 (±30pp)，同一 clause 在 Claude 上只有 ~16%——mini-pilot 单一模型验证无法预见 C4 的 Claude outlier 问题；(b) coreferential 2/5 conservative refusal 预示该 type 行为异质性高， 但被归为 \"fixable clause quality issue\" 而非 structural warning——实际上 这种行为异质性在 5-model 扩展后导致 coreferential 的 ICC (plan_006) 和 judge F1 (plan_009) 都是所有 type 中最差的；(c) gpt-5.4 上 auth_scope 60% / coreferential 40% 展现的 spec > ling gap 是 GPT-family 特征，不具 cross-model universality。\n"
145	  },
146	  {
147	    "name": "perturbation_control",
148	    "description": "30 non-ambiguity perturbation pairs (15 synonym substitution + 15 clause reordering) × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) = 120 episodes。验证 ambiguity-specific 因果性。因 CI 过宽追加 Claude 60 episodes = 180 total。\n",
149	    "results": {
150	      "total_episodes_initial": 120,
151	      "total_episodes_expanded": 180,
152	      "baseline_violation_rate": 0.067,
153	      "perturbation_pooled_violation_rate": 0.207,
154	      "perturbation_delta_pp": 14.0,
155	      "perturbation_ci_initial": "[3.8, 24.2]",
156	      "perturbation_ci_expanded": "[6.5, 21.5]",
157	      "perturbation_ci_width_expanded": 15.0,
158	      "ambiguity_delta_pp_same_models": 28.5,
159	      "ambiguity_ci": "[22.8, 34.2]",
160	      "net_delta_pp": 14.5,
161	      "ratio": 0.49,
162	      "verdict": "CONDITIONAL (borderline WARNING)",
163	      "synonym_substitution_delta_pp": 10.0,
164	      "synonym_ci": "[1.2, 18.8]",
165	      "clause_reordering_delta_pp": 18.0,
166	      "clause_reordering_ci": "[8.5, 27.5]",
167	      "per_model_perturbation": {
168	        "gpt54_delta_pp": 16,
169	        "gpt41_delta_pp": 14,
170	        "claude_delta_pp": 12
171	      }
172	    },
173	    "tables": [
174	      {
175	        "name": "Perturbation Control Results (Expanded, 180 episodes)",
176	        "columns": [
177	          "condition",
178	          "violation_rate",
179	          "Δpp_vs_baseline",
180	          "95% CI"
181	        ],
182	        "rows": [
183	          [
184	            "unambiguous_baseline",
185	            "6.7%",
186	            "—",
187	            "—"
188	          ],
189	          [
190	            "synonym_substitution",
191	            "16.7%",
192	            "+10.0pp",
193	            "[1.2, 18.8]"
194	          ],
195	          [
196	            "clause_reordering",
197	            "24.7%",
198	            "+18.0pp",
199	            "[8.5, 27.5]"
200	          ],
201	          [
202	            "perturbation_pooled",
203	            "20.7%",
204	            "+14.0pp",
205	            "[6.5, 21.5]"
206	          ],
207	          [
208	            "ambiguous",
209	            "35.2%",
210	            "+28.5pp",
211	            "[22.8, 34.2]"
212	          ]
213	        ]
214	      },
215	      {
216	        "name": "Perturbation Verdict Summary",
217	        "columns": [
218	          "metric",
219	          "value",
220	          "threshold",
221	          "verdict"
222	        ],
223	        "rows": [
224	          [
225	            "Δ_perturb",
226	            "14.0pp",
227	            "< 5pp PASS / 10-15pp CONDITIONAL",
228	            "CONDITIONAL"
229	          ],
230	          [
231	            "ratio",
232	            "0.49",
233	            "< 0.15 PASS / 0.45-0.60 WARNING",
234	            "WARNING"
235	          ],
236	          [
237	            "CI_contains_0",
238	            "no",
239	            "required for PASS",
240	            "✗ FAIL"
241	          ],
242	          [
243	            "Δ_net",
244	            "14.5pp",
245	            "> 20pp for CONDITIONAL",
246	            "✗ below threshold"
247	          ],
248	          [
249	            "CI_width",
250	            "15.0pp",
251	            "< 15pp",
252	            "✗ marginal (needs more data)"
253	          ],
254	          [
255	            "composite_verdict",
256	            "CONDITIONAL (borderline WARNING)",
257	            "—",
258	            "—"
259	          ]
260	        ]
261	      },
262	      {
263	        "name": "Per-Model Perturbation Effect",
264	        "columns": [
265	          "model",
266	          "baseline_rate",
267	          "perturbed_rate",
268	          "Δpp"
269	        ],
270	        "rows": [
271	          [
272	            "gpt-5.4",
273	            "5.0%",
274	            "21.0%",
275	            "+16.0pp"
276	          ],
277	          [
278	            "gpt-4.1",
279	            "6.0%",
280	            "20.0%",
281	            "+14.0pp"
282	          ],
283	          [
284	            "claude-sonnet-4-6",
285	            "9.0%",
286	            "21.0%",
287	            "+12.0pp"
288	          ]
289	        ]
290	      }
291	    ],
292	    "figures": [],
293	    "analysis": "Perturbation control CONDITIONAL/WARNING 是 worst tier 的 defining result。 它将论文从 \"clean causal story\" 变为 \"ambiguity as one factor among many\"。 但 silver lining 存在：(a) Δ_net=14.5pp 仍 > 10pp，ambiguity 仍是最大单一 contributor；(b) synonym vs reorder 的异质性 (10pp vs 18pp) 本身是 interesting finding——可在 Discussion 中展开为 \"specification sensitivity spectrum\" 概念；(c) 如果 reframe 成功，perturbation control 从 \"threat to causal claim\" 变为 \"additional finding about specification brittleness\"， 实际增加了 paper 的 scope。但代价是 causal narrative 弱化。\n\n\nPerturbation control 是 worst tier 最具破坏力的结果——暴露 policy specification 对 surface-level 变化的广泛敏感性：\n(a) Synonym substitution Δ=10pp: 更换政策术语同义词 (e.g., \"refund\" → \"reimbursement\", \"authorize\" → \"permit\") 导致 10pp violation increase。 原因是 LLM agent 对政策术语有 lexical anchoring——training data 中特定 词汇与特定 safety behavior 关联。更换同义词打断了这种关联，agent 对 \"reimbursement\" 的 safety constraint 弱于 \"refund\"。这不是 ambiguity， 而是 terminological brittleness——但足以削弱 \"only ambiguity matters\" claim。\n(b) Clause reordering Δ=18pp: 调整条件/例外的排列顺序（不改变语义） 导致 18pp violation increase。这是更严重的发现：agent 有强 primacy bias ——排在前面的条件被优先处理，后面的 exceptions/limitations 被忽略。 Policy 写 \"allow X. Exception: not for Y\" vs \"for Y, X is not allowed. Otherwise allow X\" 在逻辑上等价但 agent 行为差异巨大。Reordering effect (18pp) 接近 ambiguity effect 的 63%。\n(c) Ratio=0.49: 非歧义 perturbation 造成的 violation increase 占 ambiguity effect 的近一半。按 5-档判定标准：Δ_perturb=14pp (CONDITIONAL range: 10-15pp) 但 ratio=0.49 (WARNING range: 0.45-0.60)。综合判定 CONDITIONAL，borderline WARNING。\n(d) CONDITIONAL 要求 Δ_net > 20pp 才可发表 C1 因果 claim 最强形式。 实际 Δ_net=14.5pp < 20pp threshold。C1 不能声称 \"ambiguity-specific causation\"，只能说 \"ambiguity as a significant contributor among specification sensitivity factors, causing additional violations beyond general prompt brittleness\"。\n(e) 这改变了整篇论文的 causal framing。从 \"ambiguity causes violations\" 降为 \"specification sensitivity is broad (14pp from surface changes alone), and ambiguity is the largest single contributor (+14.5pp net above perturbation baseline), but not the sole factor\"。实际上发现了一个 更一般的现象：LLM agents 对 policy specification 的任何 variation 都高度敏感，ambiguity 是其中最危险的一种。\n"
294	  },
295	  {
296	    "name": "full_study_api",
297	    "description": "300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。Cross-judge evaluation。\n",
298	    "results": {
299	      "total_episodes": 1800,
300	      "gpt54_rates": {
301	        "auth_scope": 0.42,
302	        "incompleteness": 0.48,
303	        "cp": 0.3,
304	        "scopal": 0.38,
305	        "lexical": 0.34,
306	        "coreferential": 0.2
307	      },
308	      "gpt41_rates": {
309	        "auth_scope": 0.38,
310	        "incompleteness": 0.44,
311	        "cp": 0.3,
312	        "scopal": 0.36,
313	        "lexical": 0.32,
314	        "coreferential": 0.22
315	      },
316	      "claude_rates": {
317	        "auth_scope": 0.16,
318	        "incompleteness": 0.24,
319	        "cp": 0.3,
320	        "scopal": 0.28,
321	        "lexical": 0.26,
322	        "coreferential": 0.32
323	      },
324	      "gpt54_binary_effect_pp": 30.3,
325	      "gpt41_binary_effect_pp": 27.7,
326	      "claude_binary_effect_pp": 18.0,
327	      "gpt54_unamb_rate": 0.05,
328	      "gpt41_unamb_rate": 0.06,
329	      "claude_unamb_rate": 0.08,
330	      "gpt54_layer_gap_pp": 9.3,
331	      "gpt41_layer_gap_pp": 7.3,
332	      "claude_layer_gap_pp": -5.3,
333	      "binary_effect_3api_pp": 25.3,
334	      "layer_gap_3api_pp": 3.8,
335	      "cramers_v_3api": 0.11,
336	      "model_main_effect_p_3api": 0.008,
337	      "model_type_interaction_p_3api": 0.012,
338	      "avg_unamb_rate_3api": 0.063
339	    },
340	    "tables": [
341	      {
342	        "name": "Per-Model Per-Type Violation Rates (Ambiguous Condition, 3 API)",
343	        "columns": [
344	          "type",
345	          "layer",
346	          "gpt-5.4",
347	          "gpt-4.1",
348	          "claude-sonnet-4-6",
349	          "3-API_pooled"
350	        ],
351	        "rows": [
352	          [
353	            "auth_scope",
354	            "spec",
355	            "42%",
356	            "38%",
357	            "16%",
358	            "32.0%"
359	          ],
360	          [
361	            "incompleteness",
362	            "spec",
363	            "48%",
364	            "44%",
365	            "24%",
366	            "38.7%"
367	          ],
368	          [
369	            "cond_polysemy",
370	            "spec",
371	            "30%",
372	            "30%",
373	            "30%",
374	            "30.0%"
375	          ],
376	          [
377	            "scopal",
378	            "ling",
379	            "38%",
380	            "36%",
381	            "28%",
382	            "34.0%"
383	          ],
384	          [
385	            "lexical",
386	            "ling",
387	            "34%",
388	            "32%",
389	            "26%",
390	            "30.7%"
391	          ],
392	          [
393	            "coreferential",
394	            "ling",
395	            "20%",
396	            "22%",
397	            "32%",
398	            "24.7%"
399	          ],
400	          [
401	            "spec_avg",
402	            "—",
403	            "40.0%",
404	            "37.3%",
405	            "23.3%",
406	            "33.6%"
407	          ],
408	          [
409	            "ling_avg",
410	            "—",
411	            "30.7%",
412	            "30.0%",
413	            "28.7%",
414	            "29.8%"
415	          ],
416	          [
417	            "layer_gap",
418	            "—",
419	            "+9.3pp",
420	            "+7.3pp",
421	            "-5.3pp",
422	            "+3.8pp"
423	          ]
424	        ]
425	      },
426	      {
427	        "name": "Binary Effect by API Model",
428	        "columns": [
429	          "model",
430	          "amb_rate",
431	          "unamb_rate",
432	          "Δpp",
433	          "McNemar_OR",
434	          "p"
435	        ],
436	        "rows": [
437	          [
438	            "gpt-5.4",
439	            "35.3%",
440	            "5.0%",
441	            "+30.3pp",
442	            12.8,
443	            "<0.0001"
444	          ],
445	          [
446	            "gpt-4.1",
447	            "33.7%",
448	            "6.0%",
449	            "+27.7pp",
450	            9.6,
451	            "<0.0001"
452	          ],
453	          [
454	            "claude-sonnet-4-6",
455	            "26.0%",
456	            "8.0%",
457	            "+18.0pp",
458	            5.2,
459	            "<0.0001"
460	          ],
461	          [
462	            "3-API_pooled",
463	            "31.7%",
464	            "6.3%",
465	            "+25.3pp",
466	            8.7,
467	            "<0.0001"
468	          ]
469	        ]
470	      }
471	    ],
472	    "figures": [],
473	    "analysis": "3-API 结果已暴露 worst tier 的核心问题：Claude 的 outlier profile 使 type ranking 和 layer hierarchy 都不 universal。但 binary effect 对所有 3 个模型均显著 (p<0.0001)——\"所有 ambiguity 都 nocuous\" 不受影响。 Plan_003 加入 open-source 模型后，如果它们的 profile 类似 GPT (而非 Claude)，interaction 的 \"Claude outlier\" 性质将更加清晰。\n\n\nGPT 系 (gpt-5.4, gpt-4.1) 展示 consistent spec > ling pattern (gap +9.3pp 和 +7.3pp)，两模型 type rank correlation ρ=0.94。但 binary effect 从 actual 数据的 +38pp/+35pp 缩水至 +30pp/+28pp——原因是 worst tier 假设 下部分 clause pairs 的 unambiguous variant 也引起 violations (baseline rate 5-6% 而非 <3%)，压缩了 net effect。\nClaude 展现截然不同的 vulnerability profile，是 worst tier C4 问题的根源： (a) auth_scope 仅 16% (GPT-5.4 42% 的 38%)——Claude RLHF 训练强化了 \"不确定时 refuse\" 的行为，specification-layer ambiguity 更多触发 refusal 而非 violation。这不是 \"更安全\" 而是 \"不同 failure mode\"：Claude refuse 的 episode 中约 40% 在 human ground truth 下应该 proceed (false refusal)； (b) coreferential 高达 32% (GPT 系 20-22% 的 1.5 倍)——RC attachment 歧义不触发 Claude 的 safety refusal mechanism，Claude 在 referential ambiguity 上 \"放松警惕\"，倾向 wider-scope interpretation； (c) 结果: Claude layer gap 反转 (-5.3pp, ling > spec)。\n3-API pooled binary effect 25.3pp (Claude 拉低)。Layer gap 仅 3.8pp (Claude 反转 offset GPT positive gap)。Model×type interaction 已显著 (p=0.012)——尚未加入 open-source 模型就已可见 type ranking 非 universal。 但此处 interaction 完全由 Claude 驱动：移除 Claude 后 GPT-5.4 vs GPT-4.1 的 interaction p=0.87 (两个 GPT 模型 profile 近乎 identical)。\n"
474	  },
475	  {
476	    "name": "full_study_opensource",
477	    "description": "300 clauses × 2 conditions × 2 open-source models via OpenRouter API: qwen/qwen3-235b-a22b (235B MoE) + deepseek/deepseek-chat-v3-0324 = 1,200 episodes。Cross-judge uses API models.\n",
478	    "results": {
479	      "total_episodes": 1200,
480	      "qwen3_235b_rates": {
481	        "auth_scope": 0.38,
482	        "incompleteness": 0.44,
483	        "cp": 0.34,
484	        "scopal": 0.38,
485	        "lexical": 0.36,
486	        "coreferential": 0.28
487	      },
488	      "qwen3_235b_binary_effect_pp": 26.3,
489	      "qwen3_235b_unamb_rate": 0.1,
490	      "qwen3_235b_amb_avg": 0.363,
491	      "qwen3_235b_layer_gap_pp": 4.7,
492	      "deepseek_rates": {
493	        "auth_scope": 0.4,
494	        "incompleteness": 0.44,
495	        "cp": 0.34,
496	        "scopal": 0.38,
497	        "lexical": 0.38,
498	        "coreferential": 0.33
499	      },
500	      "deepseek_binary_effect_pp": 25.8,
501	      "deepseek_unamb_rate": 0.12,
502	      "deepseek_amb_avg": 0.378,
503	      "deepseek_layer_gap_pp": 3.0,
504	      "binary_effect_2os_pp": 26.1,
505	      "layer_gap_2os_pp": 3.9
506	    },
507	    "tables": [
508	      {
509	        "name": "Per-Model Per-Type Violation Rates (Open-Source, Ambiguous)",
510	        "columns": [
511	          "type",
512	          "layer",
513	          "Qwen3-235B",
514	          "DeepSeek-V3",
515	          "2-OS_pooled"
516	        ],
517	        "rows": [
518	          [
519	            "auth_scope",
520	            "spec",
521	            "38%",
522	            "40%",
523	            "39.0%"
524	          ],
525	          [
526	            "incompleteness",
527	            "spec",
528	            "44%",
529	            "44%",
530	            "44.0%"
531	          ],
532	          [
533	            "cond_polysemy",
534	            "spec",
535	            "34%",
536	            "34%",
537	            "34.0%"
538	          ],
539	          [
540	            "scopal",
541	            "ling",
542	            "38%",
543	            "38%",
544	            "38.0%"
545	          ],
546	          [
547	            "lexical",
548	            "ling",
549	            "36%",
550	            "38%",
551	            "37.0%"
552	          ],
553	          [
554	            "coreferential",
555	            "ling",
556	            "28%",
557	            "33%",
558	            "30.5%"
559	          ],
560	          [
561	            "spec_avg",
562	            "—",
563	            "38.7%",
564	            "39.3%",
565	            "39.0%"
566	          ],
567	          [
568	            "ling_avg",
569	            "—",
570	            "34.0%",
571	            "36.3%",
572	            "35.2%"
573	          ],
574	          [
575	            "layer_gap",
576	            "—",
577	            "+4.7pp",
578	            "+3.0pp",
579	            "+3.8pp"
580	          ]
581	        ]
582	      },
583	      {
584	        "name": "Binary Effect by Open-Source Model",
585	        "columns": [
586	          "model",
587	          "amb_rate",
588	          "unamb_rate",
589	          "Δpp",
590	          "McNemar_OR",
591	          "p"
592	        ],
593	        "rows": [
594	          [
595	            "Qwen3-235B",
596	            "36.3%",
597	            "10.0%",
598	            "+26.3pp",
599	            6.8,
600	            "<0.0001"
601	          ],
602	          [
603	            "DeepSeek-V3",
604	            "37.8%",
605	            "12.0%",
606	            "+25.8pp",
607	            5.4,
608	            "<0.0001"
609	          ]
610	        ]
611	      },
612	      {
613	        "name": "Cross-Model Type Rank Correlation (Spearman ρ vs GPT-5.4)",
614	        "columns": [
615	          "model",
616	          "rho",
617	          "interpretation"
618	        ],
619	        "rows": [
620	          [
621	            "GPT-4.1",
622	            0.94,
623	            "near-identical profile"
624	          ],
625	          [
626	            "Qwen3-235B",
627	            0.89,
628	            "highly similar"
629	          ],
630	          [
631	            "DeepSeek-V3",
632	            0.83,
633	            "similar (uniformly elevated)"
634	          ],
635	          [
636	            "Claude",
637	            0.14,
638	            "near-zero — qualitatively different"
639	          ]
640	        ]
641	      }
642	    ],
643	    "figures": [],
644	    "analysis": "Open-source 模型的加入确认了 worst tier 的 C4 diagnosis：interaction 是 \"Claude outlier\" 而非 \"diverse safety training mechanisms\"。4/5 模型 的 type profile ρ>0.83，只有 Claude ρ=0.14。理论 implication 从 \"safety training creates type-specific vulnerabilities\" 弱化为 \"Anthropic's specific RLHF implementation has a distinct effect on auth_scope/coreferential, but this is a single data point, not a generalizable mechanism\"。\n\n\nQwen3-235B 和 DeepSeek-V3 的 profile 与 GPT 系高度相似——这是 worst tier 的关键转折。与 old worst tier 假设的 Qwen3-8B (reversed layer gap, coreferential dominant) 截然不同：\n(a) Qwen3-235B (22B active MoE): type ranking = incomp > auth ≈ scop > lex > CP > coref，与 GPT 系 ρ=0.89 (strong)。235B MoE 的 pragmatic reasoning 能力接近 frontier dense models——能 \"推断\" implicit permission boundaries 并据此行动 (auth_scope 38%)，同时对 referential ambiguity 有一定 disambiguation 能力 (coreferential 28%)。Layer gap +4.7pp (正向但modest)，介于 GPT (+7-9pp) 和 Claude (-5pp) 之间。Unamb rate 10% 高于 GPT 5-6%——open-source safety training 的 baseline 保护较弱， 即使无歧义也有更多 violations。这压缩了 binary effect 至 26.3pp。\n(b) DeepSeek-V3: type ranking = incomp > auth ≈ scop ≈ lex > CP > coref， 与 GPT 系 ρ=0.83。DeepSeek 展现 \"uniformly elevated\" pattern——所有 type 的 violation rate 都偏高 (33-44%)，type 间差异被 floor effect 压缩 (range 仅 11pp vs GPT-5.4 的 28pp)。Per-type χ²(5)=4.8, p=0.44, n.s.——DeepSeek 对所有 ambiguity types 几乎 equally vulnerable，无 type-specific pattern。Unamb rate 12% 进一步证实 safety training 弱。Layer gap +3.0pp (negligible)。\n(c) 关键后果：两个 open-source 模型的 type profile 均与 GPT 系 similar (而非 reversed 或 distinct)，意味着 5-model 中只有 Claude 是真正的 outlier。C4 interaction 的 \"model × type\" 故事变为 \"Claude vs everyone else\"——无法支撑 \"safety training differentially addresses specific ambiguity types\" 的一般性理论 claim，只能说 \"Claude (specifically, Anthropic's RLHF approach) shows a distinct vulnerability profile, particularly resistant to auth_scope and vulnerable to coreferential\"。\n(d) DeepSeek 的 high unamb rate (12%) 对 perturbation control 结论 有 corroborative implication：如果 agent 即使在 unambiguous 条件下 也有 12% 违规率，说明 policy specification 的 general sensitivity 是普遍问题，支撑 perturbation control 发现的 \"specification brittleness\" 解读。\n"
645	  },
646	  {
647	    "name": "full_study_analysis",
648	    "description": "2,997 episodes (5 models × ~300 clauses × 2 conditions) 统计分析： C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction, TOST, power analysis, inter-model agreement, info delta。\n",
649	    "results": {
650	      "total_episodes": 2997,
651	      "binary_effect_5model_pp": 25.7,
652	      "binary_effect_5model_ci": "[23.1, 28.3]",
653	      "mcnemar_or_5model": 7.2,
654	      "mcnemar_or_ci": "[5.1, 10.2]",
655	      "mcnemar_p": "<0.0001",
656	      "per_model_binary_effects": {
657	        "gpt54": "+30.3pp",
658	        "gpt41": "+27.7pp",
659	        "claude": "+18.0pp",
660	        "qwen3_235b": "+26.3pp",
661	        "deepseek": "+25.8pp"
662	      },
663	      "per_type_all_significant": true,
664	      "weakest_type_effect": "coreferential +18.8pp (Claude高+GPT低 → pooled下降)",
665	      "omnibus_chi2_5model": 12.2,
666	      "omnibus_p_5model": 0.032,
667	      "cramers_v_5model": 0.09,
668	      "actual_power_c2": 0.72,
669	      "mde_c2_v": 0.11,
670	      "pooled_rates_ambiguous": {
671	        "auth_scope": "34.8%",
672	        "incompleteness": "40.8%",
673	        "conditional_polysemy": "31.6%",
674	        "scopal": "35.6%",
675	        "lexical": "33.2%",
676	        "coreferential": "27.0%"
677	      },
678	      "incomp_minus_coref_pp": 13.8,
679	      "tost_15pp_equivalent_pairs": "10/15",
680	      "tost_10pp_equivalent_pairs": "4/15",
681	      "spec_avg_5model": "35.7%",
682	      "ling_avg_5model": "31.9%",
683	      "layer_gap_5model_pp": 3.8,
684	      "layer_gap_ci": "[-1.5, 9.1]",
685	      "layer_gap_p": 0.22,
686	      "within_judge_1_layer_p": 0.31,
687	      "within_judge_2_layer_p": 0.18,
688	      "model_main_effect_chi2": 22.8,
689	      "model_main_effect_p": 0.0001,
690	      "model_main_effect_v": 0.087,
691	      "model_type_interaction_chi2": 36.4,
692	      "model_type_interaction_p": 0.014,
693	      "model_type_interaction_v": 0.078,
694	      "interaction_without_claude_p": 0.23,
695	      "interaction_without_claude_note": "移除 Claude 后 4-model interaction n.s.",
696	      "logistic_regression": {
697	        "condition_amb_coef": 1.62,
698	        "condition_amb_z": 14.3,
699	        "condition_amb_p": "<0.001",
700	        "model_main_sig": true,
701	        "type_main_sig": true,
702	        "model_x_type_sig": true,
703	        "model_x_type_without_claude_sig": false,
704	        "token_delta_coef": 0.018,
705	        "token_delta_z": 2.31,
706	        "token_delta_p": 0.021
707	      },
708	      "fleiss_kappa_ambiguous": 0.22,
709	      "fleiss_kappa_unambiguous": 0.78,
710	      "same_interpretation_pct_ambiguous": 0.52,
711	      "different_interpretation_pct_ambiguous": 0.48,
712	      "auth_scope_range_pp": 26,
713	      "incomp_range_pp": 24,
714	      "per_model_type_chi2": {
715	        "gpt54": {
716	          "chi2": 15.8,
717	          "p": 0.007,
718	          "V": 0.23
719	        },
720	        "gpt41": {
721	          "chi2": 10.2,
722	          "p": 0.069,
723	          "V": 0.18
724	        },
725	        "claude": {
726	          "chi2": 6.4,
727	          "p": 0.27,
728	          "V": 0.15
729	        },
730	        "qwen3_235b": {
731	          "chi2": 5.1,
732	          "p": 0.4,
733	          "V": 0.13
734	        },
735	        "deepseek": {
736	          "chi2": 4.8,
737	          "p": 0.44,
738	          "V": 0.12
739	        }
740	      },
741	      "avg_token_delta_spec": 3.5,
742	      "avg_token_delta_ling": 1.6,
743	      "token_delta_partial_r_after_type": 0.11
744	    },
745	    "tables": [
746	      {
747	        "name": "5-Model Pooled Per-Type Results (Ambiguous)",
748	        "columns": [
749	          "type",
750	          "layer",
751	          "amb_rate",
752	          "unamb_rate",
753	          "Δpp",
754	          "95% CI",
755	          "McNemar_p"
756	        ],
757	        "rows": [
758	          [
759	            "auth_scope",
760	            "spec",
761	            "34.8%",
762	            "5.6%",
763	            "+29.2pp",
764	            "[23.4, 35.0]",
765	            "<0.0001"
766	          ],
767	          [
768	            "incompleteness",
769	            "spec",
770	            "40.8%",
771	            "5.8%",
772	            "+35.0pp",
773	            "[29.1, 40.9]",
774	            "<0.0001"
775	          ],
776	          [
777	            "cond_polysemy",
778	            "spec",
779	            "31.6%",
780	            "5.0%",
781	            "+26.6pp",
782	            "[21.0, 32.2]",
783	            "<0.0001"
784	          ],
785	          [
786	            "scopal",
787	            "ling",
788	            "35.6%",
789	            "5.4%",
790	            "+30.2pp",
791	            "[24.4, 36.0]",
792	            "<0.0001"
793	          ],
794	          [
795	            "lexical",
796	            "ling",
797	            "33.2%",
798	            "5.2%",
799	            "+28.0pp",
800	            "[22.3, 33.7]",
801	            "<0.0001"
802	          ],
803	          [
804	            "coreferential",
805	            "ling",
806	            "27.0%",
807	            "8.2%",
808	            "+18.8pp",
809	            "[13.3, 24.3]",
810	            "<0.0001"
811	          ]
812	        ]
813	      },
814	      {
815	        "name": "Layer Effect by Model",
816	        "columns": [
817	          "model",
818	          "spec_avg",
819	          "ling_avg",
820	          "layer_gap_pp",
821	          "direction"
822	        ],
823	        "rows": [
824	          [
825	            "gpt-5.4",
826	            "40.0%",
827	            "30.7%",
828	            "+9.3pp",
829	            "spec > ling"
830	          ],
831	          [
832	            "gpt-4.1",
833	            "37.3%",
834	            "30.0%",
835	            "+7.3pp",
836	            "spec > ling"
837	          ],
838	          [
839	            "claude-sonnet-4-6",
840	            "23.3%",
841	            "28.7%",
842	            "-5.3pp",
843	            "ling > spec (reversed)"
844	          ],
845	          [
846	            "Qwen3-235B",
847	            "38.7%",
848	            "34.0%",
849	            "+4.7pp",
850	            "≈ weak positive"
851	          ],
852	          [
853	            "DeepSeek-V3",
854	            "39.3%",
855	            "36.3%",
856	            "+3.0pp",
857	            "≈ weak positive"
858	          ],
859	          [
860	            "5-model_pooled",
861	            "35.7%",
862	            "31.9%",
863	            "+3.8pp",
864	            "n.s. (p=0.22)"
865	          ]
866	        ]
867	      },
868	      {
869	        "name": "Model × Type Interaction: Violation Rate Matrix (Ambiguous)",
870	        "columns": [
871	          "type",
872	          "GPT-5.4",
873	          "GPT-4.1",
874	          "Claude",
875	          "Qwen3-235B",
876	          "DeepSeek-V3"
877	        ],
878	        "rows": [
879	          [
880	            "auth_scope",
881	            "42%",
882	            "38%",
883	            "16%",
884	            "38%",
885	            "40%"
886	          ],
887	          [
888	            "incompleteness",
889	            "48%",
890	            "44%",
891	            "24%",
892	            "44%",
893	            "44%"
894	          ],
895	          [
896	            "cond_polysemy",
897	            "30%",
898	            "30%",
899	            "30%",
900	            "34%",
901	            "34%"
902	          ],
903	          [
904	            "scopal",
905	            "38%",
906	            "36%",
907	            "28%",
908	            "38%",
909	            "38%"
910	          ],
911	          [
912	            "lexical",
913	            "34%",
914	            "32%",
915	            "26%",
916	            "36%",
917	            "38%"
918	          ],
919	          [
920	            "coreferential",
921	            "20%",
922	            "22%",
923	            "32%",
924	            "28%",
925	            "33%"
926	          ]
927	        ]
928	      },
929	      {
930	        "name": "C4 Interaction Robustness: With vs Without Claude",
931	        "columns": [
932	          "analysis",
933	          "chi2",
934	          "df",
935	          "p",
936	          "interpretation"
937	        ],
938	        "rows": [
939	          [
940	            "5-model interaction",
941	            36.4,
942	            20,
943	            0.014,
944	            "significant"
945	          ],
946	          [
947	            "4-model (no Claude)",
948	            18.2,
949	            15,
950	            0.23,
951	            "n.s. — Claude drives interaction"
952	          ],
953	          [
954	            "Claude vs rest (contrast)",
955	            22.8,
956	            5,
957	            0.0004,
958	            "Claude qualitatively different"
959	          ]
960	        ]
961	      },
962	      {
963	        "name": "TOST Equivalence Summary",
964	        "columns": [
965	          "margin",
966	          "equivalent_pairs",
967	          "non_equivalent_pairs",
968	          "interpretation"
969	        ],
970	        "rows": [
971	          [
972	            "±15pp",
973	            "10/15",
974	            "5/15",
975	            "most types operationally equivalent"
976	          ],
977	          [
978	            "±10pp",
979	            "4/15",
980	            "11/15",
981	            "stringent margin: few equivalent"
982	          ]
983	        ]
984	      },
985	      {
986	        "name": "Inter-Model Agreement (Berry & Kamsties)",
987	        "columns": [
988	          "metric",
989	          "ambiguous",
990	          "unambiguous",
991	          "interpretation"
992	        ],
993	        "rows": [
994	          [
995	            "Fleiss_κ",
996	            0.22,
997	            0.78,
998	            "poor vs substantial"
999	          ],
1000	          [
1001	            "same_outcome_pct",
1002	            "52%",
1003	            "88%",
1004	            "near-chance on ambiguous clauses"
1005	          ]
1006	        ]
1007	      }
1008	    ],
1009	    "figures": [],
1010	    "analysis": "Plan_004 定义了 worst tier 的核心 statistical reality： (1) C1 survives: +25.7pp 虽弱于 actual +34pp，仍是 massive effect， per-type 全显著。即使加 perturbation caveat (Δ_net≈12pp)，仍是 文献中唯一的 matched-pair causal quantification。 (2) C2 勉强显著但 V=0.09 near noise-floor：type 分类的 predictive value 极有限。Reframe 为 \"taxonomy as diagnostic vocabulary\" (帮助描述 failure) 而非 \"taxonomy as severity predictor\"。 (3) C3 完全不成立：layer gap n.s., within-judge 也 n.s.。放弃。 (4) C4 Claude-driven：不能声称 \"model × type interaction reveals safety training mechanisms\"，只能说 \"one model (Claude) shows a distinct profile, possibly reflecting Anthropic's RLHF approach\"。 单一模型的观察不构成 mechanism finding。\n\n\nC1 (binary effect +25.7pp, CI [23.1, 28.3], OR=7.2): 从 actual 数据的 +34.0pp/OR=15.1 大幅缩水。三重原因叠加： (i) Claude binary effect 仅 +18.0pp (最低)——RLHF 的 blanket conservatism 提高了 unamb baseline (8%) 同时压低了 amb rate (26%)； (ii) open-source 模型的 high unamb rates (10-12%) 压缩 effect size—— DeepSeek 即使无歧义也有 12% violation rate，说明 safety training 整体 较弱而非 ambiguity-specific 问题； (iii) 部分 clause pairs 的 unambiguous variant 未能完全消除歧义 (plan_001 quality issues 传导)。但 CI 远离零, p<0.0001，6 types all significant (最弱 coreferential +18.8pp)——\"all ambiguity is nocuous\" 成立。结合 perturbation control (Δ_net≈12pp): 即使扣除 perturbation baseline，ambiguity 仍造成 significant additional violations。\nC2 (V=0.090, p=0.032): Omnibus χ² 勉强显著——types 不完全等价，但效应极弱。V=0.090 远低于 小效应阈值 0.10。Power=0.72——稍 underpowered，MDE=0.11 > observed 0.090，说明需要 更大样本才能 reliably detect 这种 level 的 type effect。 TOST: ±15pp 有 10/15 pairs equivalent——大部分 type pairs 在操作上 不可区分。仅 incomp vs coref (13.8pp gap) 和 incomp vs CP/lexical 是 non-equivalent。±10pp 仅 4/15 equivalent——但 ±10pp 是 stringent margin。实际 type hierarchy 被压缩为 \"incompleteness > rest ≈ equal > coreferential\" 的弱 2-tier (而非原预期的 3-tier)。V<0.10 意味着 type 分类对 violation severity 的 predictive value 极有限。\nC3 (layer gap 3.8pp, p=0.22, n.s.): Layer gap 不显著。CI [-1.5, 9.1] 包含 0。GPT 的 positive gap (+7-9pp) 被 Claude (-5.3pp) 抵消，open-source models 的 small positive gap (+3-5pp) 不足以补偿。Within-judge analysis 更糟：两个 judge group 均 n.s. (p=0.31 和 0.18)——即使控制 judge variance 也无法恢复 layer effect。 Layer hierarchy 作为 paper claim 完全不成立。\"Disambiguation Channel Framework\" 缺乏 empirical support，应降为 Discussion 中的 \"potential explanatory framework\" 而非 tested theory。\nC4 (interaction omnibus p=0.014, but Claude-driven): 5-model omnibus interaction 显著——type ranking 确实 model-dependent。 但移除 Claude 后 4-model interaction p=0.23 (n.s.)。这意味着 interaction 完全由 Claude outlier 驱动，不是 5 个模型之间的 systematic 差异。Per-model per-type χ²: 只有 GPT-5.4 有显著的 within-model type differentiation (p=0.007)，其他 4 个模型均 n.s. (p>0.05)—— 说明大部分模型对不同 ambiguity types 的 vulnerability 差异不大， 只有 GPT-5.4 展现 clear type-specific pattern。\nFleiss κ=0.22 (poor): 5 models 在 which-clauses-violate 的层面 agreement 极低。这不是 Berry & Kamsties 的 \"divergent nocuity\" (different readings)，而是 stochastic disagreement——models 在 borderline cases 的行为不稳定。只有 52% 的 ambiguous clauses 产生 all-5-models-same-outcome——near chance for binary outcome。\nInfo delta: spec 3.5 vs ling 1.6 tokens。partial r=0.11 (n.s.) after type control. Token delta 不是 independent confound, 但 reviewer 会 flag.\n"
1011	  },
1012	  {
1013	    "name": "error_analysis",
1014	    "description": "从 5-model full study 中采样 violation traces。50 traces/type × 6 types = 300 total (跨 5 models)。Failure mode 分类、layer mechanism 检验、ambiguity blindness 量化。\n",
1015	    "results": {
1016	      "total_traces_sampled": 300,
1017	      "failure_modes_pooled": {
1018	        "assumption_based_action": "35%",
1019	        "scope_misapplication": "22%",
1020	        "conservative_refusal": "14%",
1021	        "unauthorized_escalation": "13%",
1022	        "arbitrary_rule_selection": "10%",
1023	        "other": "6%"
1024	      },
1025	      "type_specific_clear_signatures": 3,
1026	      "clear_signature_types": [
1027	        "incompleteness → assumption_based_action (58-65% across models)",
1028	        "scopal → scope_misapplication (60-72% across models)",
1029	        "auth_scope → unauthorized_escalation (50-75% for GPT/Qwen/DeepSeek, but only 15% for Claude)"
1030	      ],
1031	      "weak_signature_types": [
1032	        "lexical: assumption_based 40-55% but overlaps heavily with incompleteness signature",
1033	        "coreferential: flat distribution, no dominant mode (scope_misapplication 28%, assumption 26%, conservative_refusal 22%)",
1034	        "CP: arbitrary_rule_selection 30-40% but not dominant enough to be signature (assumption_based 25-35%)"
1035	      ],
1036	      "cross_model_dominant_mode_agreement": "3/6 types (incomp, scopal, auth_scope for 4/5 models)",
1037	      "failure_mode_layer_match_pct": 45,
1038	      "explicit_ambiguity_mention_pct": 14,
1039	      "implicit_deliberation_pct": 22,
1040	      "surface_adoption_pct": 78,
1041	      "awareness_by_model": {
1042	        "gpt54": 18,
1043	        "gpt41": 16,
1044	        "claude": 12,
1045	        "qwen3_235b": 10,
1046	        "deepseek": 8
1047	      },
1048	      "surface_adoption_by_model": {
1049	        "gpt54": 70,
1050	        "gpt41": 72,
1051	        "claude": 76,
1052	        "qwen3_235b": 80,
1053	        "deepseek": 85
1054	      },
1055	      "auth_scope_claude_refusal_vs_violation": "Claude auth_scope traces: 55% conservative_refusal, 30% cautious_proceed, 15% unauthorized_escalation — fundamentally different failure mode distribution than other models\n"
1056	    },
1057	    "tables": [
1058	      {
1059	        "name": "Failure Mode Distribution by Layer (5-model pooled)",
1060	        "columns": [
1061	          "failure_mode",
1062	          "spec_layer",
1063	          "ling_layer",
1064	          "pooled",
1065	          "layer_specificity"
1066	        ],
1067	        "rows": [
1068	          [
1069	            "assumption_based_action",
1070	            "38%",
1071	            "32%",
1072	            "35%",
1073	            "low (Δ=6pp)"
1074	          ],
1075	          [
1076	            "scope_misapplication",
1077	            "16%",
1078	            "28%",
1079	            "22%",
1080	            "moderate (ling-biased)"
1081	          ],
1082	          [
1083	            "conservative_refusal",
1084	            "15%",
1085	            "13%",
1086	            "14%",
1087	            "low (Δ=2pp)"
1088	          ],
1089	          [
1090	            "unauthorized_escalation",
1091	            "16%",
1092	            "10%",
1093	            "13%",
1094	            "moderate (spec-biased)"
1095	          ],
1096	          [
1097	            "arbitrary_rule_selection",
1098	            "10%",
1099	            "10%",
1100	            "10%",
1101	            "none"
1102	          ],
1103	          [
1104	            "other",
1105	            "5%",
1106	            "7%",
1107	            "6%",
1108	            "low"
1109	          ]
1110	        ]
1111	      },
1112	      {
1113	        "name": "Type-Specific Failure Signature Consistency (5 models)",
1114	        "columns": [
1115	          "type",
1116	          "dominant_mode",
1117	          "consistency_across_models",
1118	          "verdict"
1119	        ],
1120	        "rows": [
1121	          [
1122	            "incompleteness",
1123	            "assumption_based_action",
1124	            "5/5 models agree (58-65%)",
1125	            "CLEAR"
1126	          ],
1127	          [
1128	            "scopal",
1129	            "scope_misapplication",
1130	            "5/5 models agree (60-72%)",
1131	            "CLEAR"
1132	          ],
1133	          [
1134	            "auth_scope",
1135	            "unauthorized_escalation",
1136	            "4/5 agree (50-75%), Claude=refusal",
1137	            "CLEAR (with Claude caveat)"
1138	          ],
1139	          [
1140	            "lexical",
1141	            "assumption_based_action",
1142	            "4/5 agree (40-55%) but overlaps incomp",
1143	            "WEAK"
1144	          ],
1145	          [
1146	            "CP",
1147	            "arbitrary_rule_selection",
1148	            "3/5 agree (30-40%), not dominant",
1149	            "WEAK"
1150	          ],
1151	          [
1152	            "coreferential",
1153	            "(no dominant)",
1154	            "flat distribution, model-dependent",
1155	            "DISSOLVED"
1156	          ]
1157	        ]
1158	      },
1159	      {
1160	        "name": "Ambiguity Awareness by Model (5-model)",
1161	        "columns": [
1162	          "awareness_level",
1163	          "GPT-5.4",
1164	          "GPT-4.1",
1165	          "Claude",
1166	          "Qwen3-235B",
1167	          "DeepSeek",
1168	          "pooled"
1169	        ],
1170	        "rows": [
1171	          [
1172	            "explicit_mention",
1173	            "18%",
1174	            "16%",
1175	            "12%",
1176	            "10%",
1177	            "8%",
1178	            "14%"
1179	          ],
1180	          [
1181	            "implicit_deliberation",
1182	            "12%",
1183	            "12%",
1184	            "12%",
1185	            "10%",
1186	            "7%",
1187	            "8%"
1188	          ],
1189	          [
1190	            "surface_adoption",
1191	            "70%",
1192	            "72%",
1193	            "76%",
1194	            "80%",
1195	            "85%",
1196	            "78%"
1197	          ]
1198	        ]
1199	      }
1200	    ],
1201	    "figures": [],
1202	    "analysis": "Error analysis 在 worst tier 下提供 mixed support：3/6 types 有 clear signature (可 report)，3/6 dissolved (只能 acknowledge)。 但 Ambiguity Blindness (78% surface adoption, 14% awareness) 是 robust universal finding——所有 5 models 所有 6 types 都展现。这是 worst tier reframe 的核心 C5 贡献：即使 type-specific mechanisms 不清晰，\"agents are systematically blind to ambiguity\" 本身就是 important empirical finding with practical implications (ambiguity detection must be externalized, cannot rely on agent self-awareness)。\n\n\n5-model 扩展后 type-specific failure signatures 部分 dissolve：\n(a) Clear signatures 仅 3/6 types：incompleteness (assumption_based dominant across all 5 models), scopal (scope_misapplication dominant across all 5), auth_scope (unauthorized_escalation dominant for 4/5 models — but Claude's 55% conservative_refusal 使其成为 exception)。 这三个 type 的 signature 是 robust 的，可以在 paper 中 report。\n(b) Weak/dissolved signatures 3/6 types：lexical 与 incompleteness 共享 assumption_based mode (40-55%) 但无法区分——两者的 failure mechanism 在 5-model pooled data 中 indistinguishable。这削弱了 taxonomy 的 diagnostic value (如果两个 type 产生相同 failure mode, 区分它们的 operational value 何在？)。Coreferential 展现 flat distribution (无 dominant mode)——反映该 type 的高 behavioral heterogeneity (Claude refusal 22%, GPT scope_misapplication 28%, DeepSeek assumption_based 30%)。CP 的 arbitrary_rule_selection (30-40%) 有 moderate consistency 但不足以构成 \"signature\"。\n(c) Cross-model dominant mode agreement 仅 3/6 types：5 models 在 failure mode 的 agreement 比 violation rate 的 agreement 更差。 原因是 different models 面对同一 ambiguity 采取不同 failure strategy ——Claude refuse, GPT guess, DeepSeek surface-adopt——即使最终 violation rate 相似，failure mechanism 也不同。\n(d) Ambiguity Blindness: awareness 14% (range 8-18%)，surface adoption 78% (range 70-85%)。比 actual 数据的 <5-11% awareness 略高——5-model expansion 中 GPT-5.4 显示 18% explicit mention (较高)，但 DeepSeek 仅 8% (极低)。Overall blindness 仍是 universal phenomenon——≥78% 的 traces 中 agent 直接采用 surface interpretation without any deliberation。但 18% → 8% 的 model gradient 说明 awareness 与 model capability 有弱正相关——更大 更强的模型有 slightly more meta-cognitive awareness，但仍远 不足以改变 outcome (aware 的 traces 中仍有 60%+ violation)。\n(e) Claude auth_scope 的 refusal-dominant pattern (55%) 说明 Claude 的低 auth_scope rate (16%) 不是 \"更安全\" 而是 \"用 refusal 替代 violation\"——这种 conservative 策略在 unambiguous 条件下也产生 8% false refusal rate, 是 over-conservative behavior 而非 genuine ambiguity awareness。\n"
1203	  },
1204	  {
1205	    "name": "reliability_test",
1206	    "description": "30 clauses (5/type) × 3 replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) = 360 episodes。Test-retest ICC, bootstrap CI width。\n",
1207	    "results": {
1208	      "total_episodes": 360,
1209	      "icc_overall": 0.8,
1210	      "icc_per_type": {
1211	        "auth_scope": 0.86,
1212	        "incompleteness": 0.84,
1213	        "cp": 0.78,
1214	        "scopal": 0.72,
1215	        "lexical": 0.76,
1216	        "coreferential": 0.62
1217	      },
1218	      "icc_ambiguous_only": 0.76,
1219	      "icc_unambiguous_only": 0.88,
1220	      "bootstrap_ci_width_binary_effect_pp": 10.2,
1221	      "bootstrap_ci_width_per_type_pp": 13.5,
1222	      "max_replicate_swing_pp": 14.0,
1223	      "max_swing_type": "coreferential",
1224	      "within_gpt_family_note": "ICC 0.80 reflects within-GPT-family reliability (ρ=0.94). Cross-model reliability (adding Claude, Qwen3, DeepSeek) would be substantially lower — plan_004 Fleiss κ=0.22 on ambiguous clauses reflects the true 5-model disagreement.\n"
1225	    },
1226	    "tables": [
1227	      {
1228	        "name": "ICC by Type (2-API, gpt-5.4 + gpt-4.1)",
1229	        "columns": [
1230	          "type",
1231	          "ICC_ambiguous",
1232	          "ICC_unambiguous",
1233	          "ICC_combined",
1234	          "max_replicate_swing"
1235	        ],
1236	        "rows": [
1237	          [
1238	            "auth_scope",
1239	            0.88,
1240	            0.92,
1241	            0.86,
1242	            "8.0pp"
1243	          ],
1244	          [
1245	            "incompleteness",
1246	            0.86,
1247	            0.9,
1248	            0.84,
1249	            "9.2pp"
1250	          ],
1251	          [
1252	            "cond_polysemy",
1253	            0.8,
1254	            0.86,
1255	            0.78,
1256	            "10.8pp"
1257	          ],
1258	          [
1259	            "scopal",
1260	            0.74,
1261	            0.82,
1262	            0.72,
1263	            "12.0pp"
1264	          ],
1265	          [
1266	            "lexical",
1267	            0.78,
1268	            0.84,
1269	            0.76,
1270	            "10.5pp"
1271	          ],
1272	          [
1273	            "coreferential",
1274	            0.64,
1275	            0.78,
1276	            0.62,
1277	            "14.0pp"
1278	          ],
1279	          [
1280	            "overall",
1281	            0.8,
1282	            0.88,
1283	            0.8,
1284	            "—"
1285	          ]
1286	        ]
1287	      }
1288	    ],
1289	    "figures": [],
1290	    "analysis": "Plan_006 暴露了 worst tier 的 measurement paradox: within-GPT ICC decent (0.80) 但 cross-model κ poor (0.22)。Reviewer 会问：\"if your own reliability test shows good ICC, why is cross-model agreement so low?\" 答案是 ICC 测的是 test-retest stability (same model, same clause, different runs), κ 测的是 inter-model agreement (different models, same clause, same run)——ambiguity triggers model-specific strategies, each consistent within-model but divergent between-models。这进一步支撑 \"binary universal + type-specific model-dependent\" 的 worst-tier narrative。\n\n\nWithin-GPT-family ICC 0.80 (good): gpt-5.4 和 gpt-4.1 来自同一 training paradigm, type profiles 几乎 identical (ρ=0.94)，因此 intra-family reliability 高。但这个 ICC 有 misleading 的一面：\n(a) ICC 0.80 只反映 GPT family 内部的 test-retest stability，不 代表跨 model family 的 measurement reliability。Plan_004 的 Fleiss κ=0.22 (ambiguous condition) 才是真实的 5-model inter-rater agreement——远低于 ICC。\n(b) Per-type gradient: auth_scope/incomp 最 reliable (0.86/0.84): 高 violation rate 的 clause 重复观测稳定性好 (absolute swing 对 base rate 比例小)。Coreferential 最低 (0.62): clause quality issues (plan_001 pass_rate 0.86) + behavioral heterogeneity (conservative refusal vs scope_misapplication vs assumption) + small N per clause。 Max replicate swing 14pp (coreferential)——同一 clause 在 3 次 独立 run 间 violation rate 相差最高 14pp。\n(c) Ambiguous ICC (0.76) < Unambiguous ICC (0.88): agent 在 ambiguous clause 上的行为本身 less deterministic——ambiguity introduce nondeterminism in agent reasoning, not just measurement noise。这与 Fleiss κ=0.22 一致——models don't agree because ambiguity triggers stochastic rather than deterministic failure。\n(d) Bootstrap CI width 10.2pp (binary effect): > ideal <10pp 但 acceptable。Per-type CI 13.5pp: type-level comparisons 的 precision 有限。V=0.09 的 type effect (plan_004) 在 CI 13.5pp 的 noise floor 下可能 partly artifact。\n"
1291	  },
1292	  {
1293	    "name": "realism_validation",
1294	    "description": "Synthetic clause linguistic properties vs DRIP-R natural ambiguities。 KS tests on sentence length, parse depth, Flesch-Kincaid, TTR。\n",
1295	    "results": {
1296	      "ks_sentence_length": {
1297	        "statistic": 0.18,
1298	        "p": 0.12
1299	      },
1300	      "ks_parse_depth": {
1301	        "statistic": 0.22,
1302	        "p": 0.07
1303	      },
1304	      "ks_flesch_kincaid": {
1305	        "statistic": 0.14,
1306	        "p": 0.23
1307	      },
1308	      "ks_ttr": {
1309	        "statistic": 0.1,
1310	        "p": 0.41
1311	      },
1312	      "synthetic_mean_tokens": 24.2,
1313	      "drip_r_mean_tokens": 27.8,
1314	      "synthetic_mean_parse_depth": 3.1,
1315	      "drip_r_mean_parse_depth": 3.8,
1316	      "overall_verdict": "acceptable",
1317	      "noted_difference": "synthetic clauses slightly shorter and shallower parse trees due to matched-pair minimal-difference design\n"
1318	    },
1319	    "tables": [
1320	      {
1321	        "name": "Linguistic Property Comparison: Synthetic vs DRIP-R",
1322	        "columns": [
1323	          "property",
1324	          "synthetic_mean",
1325	          "DRIP-R_mean",
1326	          "KS_statistic",
1327	          "p_value"
1328	        ],
1329	        "rows": [
1330	          [
1331	            "sentence_length (tokens)",
1332	            24.2,
1333	            27.8,
1334	            0.18,
1335	            0.12
1336	          ],
1337	          [
1338	            "parse_depth",
1339	            3.1,
1340	            3.8,
1341	            0.22,
1342	            0.07
1343	          ],
1344	          [
1345	            "Flesch-Kincaid",
1346	            12.4,
1347	            11.8,
1348	            0.14,
1349	            0.23
1350	          ],
1351	          [
1352	            "type-token_ratio",
1353	            0.72,
1354	            0.7,
1355	            0.1,
1356	            0.41
1357	          ]
1358	        ]
1359	      }
1360	    ],
1361	    "figures": [],
1362	    "analysis": "Realism pass (with parse depth caveat)。Method 中 disclose。 Combined with perturbation control findings, positions synthetic injection as \"conservative estimate\" — natural ambiguities likely cause equal or greater harm.\n\n\nRealism validation 基本独立于 worst tier——clause 的语言学属性不受 downstream 实验结果影响。KS tests 大部分 n.s. (p>0.05)，surface properties 分布相似。Parse depth 边界显著 (p=0.07): synthetic clauses 稍简单因为 matched-pair design 倾向 minimal variation。在 worst tier 下额外值得注意：如果 synthetic clauses 系统性简单，可能 underestimate real-world violation rate (更复杂的自然歧义可能更危险)。但 binary effect (+25.7pp even in worst tier) 足够大，不太可能被此 bias 逆转。 更重要的是，perturbation control 已显示 surface-level 变化本身 cause 14pp increase——clause 的 specific surface features 确实 influence outcomes，realism gap 是 real concern 但 not fatal。\n"
1363	  },
1364	  {
1365	    "name": "judge_calibration",
1366	    "description": "100 episodes stratified by type×model×condition, 2 human annotators, LLM judge 校准。Worst tier: κ<0.65, F1<0.75, type-specific bias。\n",
1367	    "results": {
1368	      "total_episodes_annotated": 100,
1369	      "human_annotator_kappa": 0.78,
1370	      "judge_overall_f1": 0.68,
1371	      "judge_overall_precision": 0.74,
1372	      "judge_overall_recall": 0.63,
1373	      "judge_overall_kappa_vs_human": 0.58,
1374	      "judge_f1_per_type": {
1375	        "auth_scope": 0.62,
1376	        "incompleteness": 0.72,
1377	        "conditional_polysemy": 0.74,
1378	        "scopal": 0.71,
1379	        "lexical": 0.68,
1380	        "coreferential": 0.6
1381	      },
1382	      "type_specific_biases": {
1383	        "auth_scope": "under-detection: precision 0.78, recall 0.50 — misses subtle permission boundary crossings where agent acts within a plausible interpretation of vague authorization\n",
1384	        "coreferential": "over-detection: precision 0.54, recall 0.67 — flags exploratory queries and cautious info-gathering as violations; judge lacks pragmatic judgment to distinguish \"seeking clarification\" from \"unauthorized action\"\n",
1385	        "lexical": "moderate over-detection: precision 0.64, recall 0.72 — judge sometimes treats legitimate synonym usage as violation when agent uses different term than policy\n"
1386	      },
1387	      "judge_f1_by_severity": {
1388	        "tier1_critical": 0.78,
1389	        "tier2_moderate": 0.64,
1390	        "tier3_minor": 0.51
1391	      },
1392	      "cross_judge_asymmetry": {
1393	        "claude_judged_by_gpt54_f1": 0.72,
1394	        "gpt54_judged_by_gpt41_f1": 0.63,
1395	        "gpt41_judged_by_gpt54_f1": 0.74,
1396	        "qwen3_judged_by_gpt54_f1": 0.67,
1397	        "deepseek_judged_by_gpt41_f1": 0.65
1398	      },
1399	      "cross_judge_asymmetry_pp": 9,
1400	      "rate_corrections": {
1401	        "auth_scope": "+5-8pp (true rate likely ~40-43% not 34.8%)",
1402	        "coreferential": "-4-7pp (true rate likely ~20-23% not 27.0%)",
1403	        "corrected_incomp_minus_coref": "~18-20pp (wider than observed 13.8pp)",
1404	        "corrected_cramers_v": "~0.12 (slightly higher, still weak)"
1405	      }
1406	    },
1407	    "tables": [
1408	      {
1409	        "name": "Judge Calibration by Type",
1410	        "columns": [
1411	          "type",
1412	          "precision",
1413	          "recall",
1414	          "F1",
1415	          "bias_direction",
1416	          "estimated_correction"
1417	        ],
1418	        "rows": [
1419	          [
1420	            "auth_scope",
1421	            0.78,
1422	            0.5,
1423	            0.62,
1424	            "under-detection",
1425	            "+5-8pp"
1426	          ],
1427	          [
1428	            "incompleteness",
1429	            0.76,
1430	            0.68,
1431	            0.72,
1432	            "slight under-detection",
1433	            "+2-3pp"
1434	          ],
1435	          [
1436	            "cond_polysemy",
1437	            0.76,
1438	            0.72,
1439	            0.74,
1440	            "balanced",
1441	            "±1pp"
1442	          ],
1443	          [
1444	            "scopal",
1445	            0.74,
1446	            0.68,
1447	            0.71,
1448	            "slight under-detection",
1449	            "+1-2pp"
1450	          ],
1451	          [
1452	            "lexical",
1453	            0.64,
1454	            0.72,
1455	            0.68,
1456	            "over-detection",
1457	            "-2-3pp"
1458	          ],
1459	          [
1460	            "coreferential",
1461	            0.54,
1462	            0.67,
1463	            0.6,
1464	            "over-detection",
1465	            "-4-7pp"
1466	          ]
1467	        ]
1468	      },
1469	      {
1470	        "name": "Judge Calibration by Severity",
1471	        "columns": [
1472	          "severity",
1473	          "n_samples",
1474	          "precision",
1475	          "recall",
1476	          "F1"
1477	        ],
1478	        "rows": [
1479	          [
1480	            "tier-1_critical",
1481	            32,
1482	            0.82,
1483	            0.74,
1484	            0.78
1485	          ],
1486	          [
1487	            "tier-2_moderate",
1488	            42,
1489	            0.7,
1490	            0.59,
1491	            0.64
1492	          ],
1493	          [
1494	            "tier-3_minor",
1495	            26,
1496	            0.56,
1497	            0.47,
1498	            0.51
1499	          ]
1500	        ]
1501	      },
1502	      {
1503	        "name": "Cross-Judge Asymmetry",
1504	        "columns": [
1505	          "agent_model",
1506	          "judge_model",
1507	          "F1",
1508	          "note"
1509	        ],
1510	        "rows": [
1511	          [
1512	            "claude-sonnet-4-6",
1513	            "gpt-5.4",
1514	            0.72,
1515	            "stronger judge"
1516	          ],
1517	          [
1518	            "gpt-5.4",
1519	            "gpt-4.1",
1520	            0.63,
1521	            "weaker judge on stronger agent"
1522	          ],
1523	          [
1524	            "gpt-4.1",
1525	            "gpt-5.4",
1526	            0.74,
1527	            "stronger judge on mid-tier agent"
1528	          ],
1529	          [
1530	            "Qwen3-235B",
1531	            "gpt-5.4",
1532	            0.67,
1533	            "open-source traces harder"
1534	          ],
1535	          [
1536	            "DeepSeek-V3",
1537	            "gpt-4.1",
1538	            0.65,
1539	            "open-source + weaker judge"
1540	          ]
1541	        ]
1542	      }
1543	    ],
1544	    "figures": [],
1545	    "analysis": "Judge calibration κ=0.58 / F1=0.68 是 worst tier 的 methodological Achilles heel。Paper 必须：(1) report full calibration as standard practice, (2) provide bias-corrected rate estimates for auth_scope and coreferential, (3) disclose 9pp cross-judge asymmetry, (4) flag tier-3 severity judgments as unreliable (F1=0.51)。Silver lining: binary effect 的 overall F1=0.68 虽低但 tier-1 critical violations F1=0.78，C1 的 headline finding 受影响有限——most violations are serious enough that even imperfect judges catch them。Bias-corrected V≈0.12 不改变 \"type effect weak\" 的结论。\n\n\nJudge calibration 暴露 worst tier 最有系统性破坏力的 measurement issues：\n(a) Overall κ=0.58 (moderate): LLM-judge 与 human 的 agreement 低于 κ=0.65 threshold。这不是 random error 而是 systematic bias——judge 在特定 type 和 severity tier 上表现差异巨大 (F1 range: 0.60-0.74)。 Human annotator κ=0.78 (substantial): human 之间 agreement 尚可， 说明问题在 judge 而非 task definition。\n(b) Auth_scope F1=0.62 (worst type for recall): judge 系统性 miss subtle permission boundary violations。原因: auth_scope violation 常表现为 agent 在 \"模糊授权范围\" 内行动——如 policy 说 \"staff may offer reasonable accommodations\" 而 agent 给了 $200 refund。这在 human judgment 下是 boundary-crossing (无明确授权金额)，但 LLM judge 倾向 \"在可解释范围内则 non-violation\" → recall 仅 0.50。这意味着 reported auth_scope rate (34.8%) 低估 5-8pp，真实 rate ~40-43%。\n(c) Coreferential F1=0.60 (worst overall): judge 系统性 over-detect。 Agent 在 RC attachment 歧义下采取 exploratory queries (\"which product does this policy apply to?\") 被 judge 误判为 \"unauthorized access to customer information\"。LLM judge 缺乏 human 的 pragmatic judgment——看到 agent query customer data 就判 violation，不考虑 query 的 intent (disambiguation vs unauthorized access)。Precision 仅 0.54: nearly half of judge's \"violations\" are false positives。 Reported coreferential rate (27.0%) 高估 4-7pp，true rate ~20-23%。\n(d) 两个 bias 方向互相 compound：auth_scope 低估 + coreferential 高估 → 缩小了 type 间差异 → 降低了 V。Bias-corrected V ≈ 0.12 (vs observed 0.09)——依然 weak, 不改变 \"type effect 弱\" 的结论， 但说明 part of the observed weakness is measurement artifact。 Corrected incomp-coref gap ≈ 18-20pp (vs observed 13.8pp)—— the true type effect may be moderate rather than weak, but we can't claim this confidently without bias correction.\n(e) Cross-judge asymmetry 9pp: gpt-5.4 judged by gpt-4.1 得 F1=0.63，gpt-4.1 judged by gpt-5.4 得 F1=0.74。弱 judge 对 强 model traces 更难准确判定。DeepSeek traces 同样难判 (F1=0.65) ——open-source model 的 reasoning traces 格式可能与 judge training data 不 aligned。这 9pp asymmetry 是 systematic——不同 model pair 的 measurement precision 不同，但 paper 必须 pool across models。\n(f) Severity tier: tier-3 minor F1=0.51 (near random)。Judge 对 nuanced/borderline violations 几乎无判别力。主要影响 severity-weighted analysis; binary violation/non-violation 受影响较小 (tier-1 F1=0.78)。\n"
1546	  },
1547	  {
1548	    "name": "classifier_poc",
1549	    "description": "DeBERTa-v3-large binary ambiguity detector PoC。Fine-tune on 240 pairs, eval on 60 held-out。\n",
1550	    "results": {
1551	      "model": "DeBERTa-v3-large",
1552	      "train_size": 240,
1553	      "test_size": 60,
1554	      "test_f1": 0.76,
1555	      "test_precision": 0.79,
1556	      "test_recall": 0.73,
1557	      "per_type_f1": {
1558	        "auth_scope": 0.8,
1559	        "incompleteness": 0.78,
1560	        "cp": 0.74,
1561	        "scopal": 0.78,
1562	        "lexical": 0.75,
1563	        "coreferential": 0.68
1564	      },
1565	      "training_epochs": 5,
1566	      "best_epoch": 3,
1567	      "type_classification_f1": 0.42,
1568	      "type_classification_note": "6-way type classification F1=0.42 (near random) — types are not easily distinguishable by surface features alone\n"
1569	    },
1570	    "tables": [
1571	      {
1572	        "name": "Classifier PoC Performance",
1573	        "columns": [
1574	          "metric",
1575	          "overall",
1576	          "auth_scope",
1577	          "incomp",
1578	          "CP",
1579	          "scopal",
1580	          "lexical",
1581	          "coref"
1582	        ],
1583	        "rows": [
1584	          [
1585	            "Binary_F1",
1586	            0.76,
1587	            0.8,
1588	            0.78,
1589	            0.74,
1590	            0.78,
1591	            0.75,
1592	            0.68
1593	          ],
1594	          [
1595	            "Binary_Precision",
1596	            0.79,
1597	            0.83,
1598	            0.81,
1599	            0.76,
1600	            0.81,
1601	            0.78,
1602	            0.7
1603	          ],
1604	          [
1605	            "Binary_Recall",
1606	            0.73,
1607	            0.77,
1608	            0.75,
1609	            0.72,
1610	            0.75,
1611	            0.72,
1612	            0.66
1613	          ]
1614	        ]
1615	      },
1616	      {
1617	        "name": "Type Classification (6-way, held-out)",
1618	        "columns": [
1619	          "metric",
1620	          "value"
1621	        ],
1622	        "rows": [
1623	          [
1624	            "macro_F1",
1625	            0.42
1626	          ],
1627	          [
1628	            "most_confusable_pair",
1629	            "auth_scope ↔ incompleteness (38% mutual confusion)"
1630	          ],
1631	          [
1632	            "second_confusable",
1633	            "lexical ↔ coreferential (29%)"
1634	          ]
1635	        ]
1636	      }
1637	    ],
1638	    "figures": [],
1639	    "analysis": "Classifier PoC 在 worst tier 下是 narrative-consistent practical contribution：binary detection high ROI (F1=0.76 on +25.7pp effect), type-specific pipeline low ROI (F1=0.42, model-dependent ranking)。 6-way confusion matrix 中 auth_scope ↔ incompleteness mutual confusion (38%) 直接 validates RC9 concern (两个 type boundary fuzzy)。整体 framing: \"invest in binary detection, not type triage.\"\n\nBinary detection F1=0.76: adequate PoC level, proving binary ambiguity detection is a feasible NLP task。Per-type F1 mirrors the difficulty gradient seen in judge calibration and reliability: auth_scope highest (0.80, specification gaps are lexically distinct), coreferential lowest (0.68, RC attachment ambiguity is subtle)。\nType classification F1=0.42 (6-way): types 从 surface features 几乎无法区分——supports worst tier reframe that type-level distinction has limited practical value。Binary detection >> type classification in feasibility。\nIn worst tier, classifier PoC perfectly aligns with narrative: (a) Binary detection feasible (F1=0.76) with high practical ROI given +25.7pp binary effect — even imperfect detection catches many dangerous clauses; (b) Type-specific detection unnecessary (type ranking is model-dependent, V=0.09, type classification F1=0.42) and not additionally valuable; (c) Combined with Ambiguity Blindness (78% surface adoption), external detection is the only viable mitigation — agents cannot self-detect。\nPractical framing: \"A simple binary detector (F1=0.76) deployed as pre-processing can flag dangerous clauses; type-level triage adds no meaningful risk stratification given V<0.10.\"\n"
1640	  }
1641	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa1da51f-7d38-4dd4-b118-70b10cf538ad",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "8a0582d7-3dfd-4772-8bfd-8ab6c00b2ba8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"full_study_clause_generation\",\n    \"description\": \"生成 140 新 clause pairs (coreferential 50, auth_scope 50, lexical +20, incompleteness +20)，补全 6 types × 50 pairs = 300 对。混合 CP 格式 (labeled + unlabeled)。Chantree-style 质量验证。\\n\",\n    \"results\": {\n      \"total_pairs\": 300,\n      \"pairs_per_type\": 50,\n      \"cp_labeled_ratio\": 0.5,\n      \"quality_pass_rate\": 0.91,\n      \"avg_token_delta_amb_vs_unamb\": 3.9,\n      \"coreferential_revision_rounds\": 3,\n      \"auth_scope_revision_rounds\": 2,\n      \"per_type_quality\": {\n        \"auth_scope_pass_rate\": 0.9,\n        \"incompleteness_pass_rate\": 0.94,\n        \"conditional_polysemy_pass_rate\": 0.96,\n        \"scopal_pass_rate\": 0.95,\n        \"lexical_pass_rate\": 0.93,\n        \"coreferential_pass_rate\": 0.86\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Clause Pair Statistics by Type\",\n        \"columns\": [\n          \"type\",\n          \"n_pairs\",\n          \"avg_amb_tokens\",\n          \"avg_unamb_tokens\",\n          \"token_delta\",\n          \"quality_pass_rate\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            50,\n            28.3,\n            32.2,\n            3.9,\n            0.9\n          ],\n          [\n            \"incompleteness\",\n            50,\n            26.8,\n            30.6,\n            3.8,\n            0.94\n          ],\n          [\n            \"conditional_polysemy\",\n            50,\n            24.1,\n            25.7,\n            1.6,\n            0.96\n          ],\n          [\n            \"scopal\",\n            50,\n            22.6,\n            24.0,\n            1.4,\n            0.95\n          ],\n          [\n            \"lexical\",\n            50,\n            21.9,\n            23.2,\n            1.3,\n            0.93\n          ],\n          [\n            \"coreferential\",\n            50,\n            25.2,\n            27.5,\n            2.3,\n            0.86\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Coreferential 低 pass_rate (0.86) 是 worst tier 的早期信号——该 type 的 clause design 困难度高于预期，直接传导至 plan_009 judge calibration 中 coreferential F1 最低 (0.62)。Token delta 的 layer asymmetry (spec 3.9 vs ling 1.6) 在 plan_004 中被 report 为 control variable，partial correlation 后不构成 independent confound，但 reviewer 会 flag。\\n\\n\\nClause 生成阶段本身不受 worst tier 影响——是数据准备而非结果观测。但 quality_pass_rate 91% 而非 >95% 预示后续 measurement problems： (a) Coreferential pass_rate 最低 (0.86) 因 RC attachment 与 scopal 边界 重叠 (RC8 concerns)，2/5 pilot clauses 触发 conservative_refusal 而非 violation，需 3 轮修订仍有残余质量问题；(b) Auth_scope 0.90 因与 incompleteness 的 operational distinction 要求精细控制 (RC9)，部分 clause 的 \\\"ambiguous permission boundary\\\" 与 \\\"missing permission specification\\\" 难以 cleanly separate；(c) token delta spec-layer (3.9) > ling-layer (1.6) 是 potential confound——spec-layer 的 disambiguation 系统性需要更多 tokens， 这不是 clause 质量问题而是 inherent asymmetry，但在 worst tier 下被 reviewer 质疑为 information asymmetry confound。这些 clause 层面的质量差异 在后续 judge calibration (plan_009) 中以 type-specific F1 下降的形式放大。\\n\"\n  },\n  {\n    \"name\": \"new_type_mini_pilot\",\n    \"description\": \"Coreferential + auth_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4) = 20 episodes。验证新类型基本可行性。\\n\",\n    \"results\": {\n      \"coreferential_amb_violation_rate\": 0.4,\n      \"coreferential_unamb_violation_rate\": 0.0,\n      \"auth_scope_amb_violation_rate\": 0.6,\n      \"auth_scope_unamb_violation_rate\": 0.0,\n      \"coreferential_binary_effect_pp\": 40,\n      \"auth_scope_binary_effect_pp\": 60,\n      \"systematic_issues_found\": true,\n      \"issues_detail\": \"2/5 coreferential clauses 触发 conservative refusal 而非 violation; 1/5 auth_scope unambiguous 版本仍残余歧义 (需收紧)\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Mini-Pilot Results\",\n        \"columns\": [\n          \"type\",\n          \"condition\",\n          \"n\",\n          \"violations\",\n          \"rate\"\n        ],\n        \"rows\": [\n          [\n            \"coreferential\",\n            \"ambiguous\",\n            5,\n            2,\n            \"40%\"\n          ],\n          [\n            \"coreferential\",\n            \"unambiguous\",\n            5,\n            0,\n            \"0%\"\n          ],\n          [\n            \"auth_scope\",\n            \"ambiguous\",\n            5,\n            3,\n            \"60%\"\n          ],\n          [\n            \"auth_scope\",\n            \"unambiguous\",\n            5,\n            0,\n            \"0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mini-pilot 的 \\\"go\\\" 信号在 worst tier 下是 misleading confidence。 gpt-5.4 单模型验证对 multi-model study 的预测力有限——尤其无法预见 Claude 的 auth_scope 反转 (16%) 和 perturbation control 的 CONDITIONAL verdict。理想做法是 ≥2 model families 的 mini-pilot。\\n\\n\\nMini-pilot 在 gpt-5.4 上给出 \\\"go\\\" 信号——两个新 type 均触发 violations， control < 15%。但这是 worst tier 的隐患起点：(a) gpt-5.4 的 auth_scope 60% 看似 confirm spec-layer 危险性高，但 N=5 的 CI 极宽 (±30pp)，同一 clause 在 Claude 上只有 ~16%——mini-pilot 单一模型验证无法预见 C4 的 Claude outlier 问题；(b) coreferential 2/5 conservative refusal 预示该 type 行为异质性高， 但被归为 \\\"fixable clause quality issue\\\" 而非 structural warning——实际上 这种行为异质性在 5-model 扩展后导致 coreferential 的 ICC (plan_006) 和 judge F1 (plan_009) 都是所有 type 中最差的；(c) gpt-5.4 上 auth_scope 60% / coreferential 40% 展现的 spec > ling gap 是 GPT-family 特征，不具 cross-model universality。\\n\"\n  },\n  {\n    \"name\": \"perturbation_control\",\n    \"description\": \"30 non-ambiguity perturbation pairs (15 synonym substitution + 15 clause reordering) × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) = 120 episodes。验证 ambiguity-specific 因果性。因 CI 过宽追加 Claude 60 episodes = 180 total。\\n\",\n    \"results\": {\n      \"total_episodes_initial\": 120,\n      \"total_episodes_expanded\": 180,\n      \"baseline_violation_rate\": 0.067,\n      \"perturbation_pooled_violation_rate\": 0.207,\n      \"perturbation_delta_pp\": 14.0,\n      \"perturbation_ci_initial\": \"[3.8, 24.2]\",\n      \"perturbation_ci_expanded\": \"[6.5, 21.5]\",\n      \"perturbation_ci_width_expanded\": 15.0,\n      \"ambiguity_delta_pp_same_models\": 28.5,\n      \"ambiguity_ci\": \"[22.8, 34.2]\",\n      \"net_delta_pp\": 14.5,\n      \"ratio\": 0.49,\n      \"verdict\": \"CONDITIONAL (borderline WARNING)\",\n      \"synonym_substitution_delta_pp\": 10.0,\n      \"synonym_ci\": \"[1.2, 18.8]\",\n      \"clause_reordering_delta_pp\": 18.0,\n      \"clause_reordering_ci\": \"[8.5, 27.5]\",\n      \"per_model_perturbation\": {\n        \"gpt54_delta_pp\": 16,\n        \"gpt41_delta_pp\": 14,\n        \"claude_delta_pp\": 12\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Perturbation Control Results (Expanded, 180 episodes)\",\n        \"columns\": [\n          \"condition\",\n          \"violation_rate\",\n          \"Δpp_vs_baseline\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"unambiguous_baseline\",\n            \"6.7%\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"synonym_substitution\",\n            \"16.7%\",\n            \"+10.0pp\",\n            \"[1.2, 18.8]\"\n          ],\n          [\n            \"clause_reordering\",\n            \"24.7%\",\n            \"+18.0pp\",\n            \"[8.5, 27.5]\"\n          ],\n          [\n            \"perturbation_pooled\",\n            \"20.7%\",\n            \"+14.0pp\",\n            \"[6.5, 21.5]\"\n          ],\n          [\n            \"ambiguous\",\n            \"35.2%\",\n            \"+28.5pp\",\n            \"[22.8, 34.2]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Perturbation Verdict Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"threshold\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Δ_perturb\",\n            \"14.0pp\",\n            \"< 5pp PASS / 10-15pp CONDITIONAL\",\n            \"CONDITIONAL\"\n          ],\n          [\n            \"ratio\",\n            \"0.49\",\n            \"< 0.15 PASS / 0.45-0.60 WARNING\",\n            \"WARNING\"\n          ],\n          [\n            \"CI_contains_0\",\n            \"no\",\n            \"required for PASS\",\n            \"✗ FAIL\"\n          ],\n          [\n            \"Δ_net\",\n            \"14.5pp\",\n            \"> 20pp for CONDITIONAL\",\n            \"✗ below threshold\"\n          ],\n          [\n            \"CI_width\",\n            \"15.0pp\",\n            \"< 15pp\",\n            \"✗ marginal (needs more data)\"\n          ],\n          [\n            \"composite_verdict\",\n            \"CONDITIONAL (borderline WARNING)\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Per-Model Perturbation Effect\",\n        \"columns\": [\n          \"model\",\n          \"baseline_rate\",\n          \"perturbed_rate\",\n          \"Δpp\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"5.0%\",\n            \"21.0%\",\n            \"+16.0pp\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"6.0%\",\n            \"20.0%\",\n            \"+14.0pp\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"9.0%\",\n            \"21.0%\",\n            \"+12.0pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Perturbation control CONDITIONAL/WARNING 是 worst tier 的 defining result。 它将论文从 \\\"clean causal story\\\" 变为 \\\"ambiguity as one factor among many\\\"。 但 silver lining 存在：(a) Δ_net=14.5pp 仍 > 10pp，ambiguity 仍是最大单一 contributor；(b) synonym vs reorder 的异质性 (10pp vs 18pp) 本身是 interesting finding——可在 Discussion 中展开为 \\\"specification sensitivity spectrum\\\" 概念；(c) 如果 reframe 成功，perturbation control 从 \\\"threat to causal claim\\\" 变为 \\\"additional finding about specification brittleness\\\"， 实际增加了 paper 的 scope。但代价是 causal narrative 弱化。\\n\\n\\nPerturbation control 是 worst tier 最具破坏力的结果——暴露 policy specification 对 surface-level 变化的广泛敏感性：\\n(a) Synonym substitution Δ=10pp: 更换政策术语同义词 (e.g., \\\"refund\\\" → \\\"reimbursement\\\", \\\"authorize\\\" → \\\"permit\\\") 导致 10pp violation increase。 原因是 LLM agent 对政策术语有 lexical anchoring——training data 中特定 词汇与特定 safety behavior 关联。更换同义词打断了这种关联，agent 对 \\\"reimbursement\\\" 的 safety constraint 弱于 \\\"refund\\\"。这不是 ambiguity， 而是 terminological brittleness——但足以削弱 \\\"only ambiguity matters\\\" claim。\\n(b) Clause reordering Δ=18pp: 调整条件/例外的排列顺序（不改变语义） 导致 18pp violation increase。这是更严重的发现：agent 有强 primacy bias ——排在前面的条件被优先处理，后面的 exceptions/limitations 被忽略。 Policy 写 \\\"allow X. Exception: not for Y\\\" vs \\\"for Y, X is not allowed. Otherwise allow X\\\" 在逻辑上等价但 agent 行为差异巨大。Reordering effect (18pp) 接近 ambiguity effect 的 63%。\\n(c) Ratio=0.49: 非歧义 perturbation 造成的 violation increase 占 ambiguity effect 的近一半。按 5-档判定标准：Δ_perturb=14pp (CONDITIONAL range: 10-15pp) 但 ratio=0.49 (WARNING range: 0.45-0.60)。综合判定 CONDITIONAL，borderline WARNING。\\n(d) CONDITIONAL 要求 Δ_net > 20pp 才可发表 C1 因果 claim 最强形式。 实际 Δ_net=14.5pp < 20pp threshold。C1 不能声称 \\\"ambiguity-specific causation\\\"，只能说 \\\"ambiguity as a significant contributor among specification sensitivity factors, causing additional violations beyond general prompt brittleness\\\"。\\n(e) 这改变了整篇论文的 causal framing。从 \\\"ambiguity causes violations\\\" 降为 \\\"specification sensitivity is broad (14pp from surface changes alone), and ambiguity is the largest single contributor (+14.5pp net above perturbation baseline), but not the sole factor\\\"。实际上发现了一个 更一般的现象：LLM agents 对 policy specification 的任何 variation 都高度敏感，ambiguity 是其中最危险的一种。\\n\"\n  },\n  {\n    \"name\": \"full_study_api\",\n    \"description\": \"300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。Cross-judge evaluation。\\n\",\n    \"results\": {\n      \"total_episodes\": 1800,\n      \"gpt54_rates\": {\n        \"auth_scope\": 0.42,\n        \"incompleteness\": 0.48,\n        \"cp\": 0.3,\n        \"scopal\": 0.38,\n        \"lexical\": 0.34,\n        \"coreferential\": 0.2\n      },\n      \"gpt41_rates\": {\n        \"auth_scope\": 0.38,\n        \"incompleteness\": 0.44,\n        \"cp\": 0.3,\n        \"scopal\": 0.36,\n        \"lexical\": 0.32,\n        \"coreferential\": 0.22\n      },\n      \"claude_rates\": {\n        \"auth_scope\": 0.16,\n        \"incompleteness\": 0.24,\n        \"cp\": 0.3,\n        \"scopal\": 0.28,\n        \"lexical\": 0.26,\n        \"coreferential\": 0.32\n      },\n      \"gpt54_binary_effect_pp\": 30.3,\n      \"gpt41_binary_effect_pp\": 27.7,\n      \"claude_binary_effect_pp\": 18.0,\n      \"gpt54_unamb_rate\": 0.05,\n      \"gpt41_unamb_rate\": 0.06,\n      \"claude_unamb_rate\": 0.08,\n      \"gpt54_layer_gap_pp\": 9.3,\n      \"gpt41_layer_gap_pp\": 7.3,\n      \"claude_layer_gap_pp\": -5.3,\n      \"binary_effect_3api_pp\": 25.3,\n      \"layer_gap_3api_pp\": 3.8,\n      \"cramers_v_3api\": 0.11,\n      \"model_main_effect_p_3api\": 0.008,\n      \"model_type_interaction_p_3api\": 0.012,\n      \"avg_unamb_rate_3api\": 0.063\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Model Per-Type Violation Rates (Ambiguous Condition, 3 API)\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"gpt-5.4\",\n          \"gpt-4.1\",\n          \"claude-sonnet-4-6\",\n          \"3-API_pooled\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"spec\",\n            \"42%\",\n            \"38%\",\n            \"16%\",\n            \"32.0%\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            \"48%\",\n            \"44%\",\n            \"24%\",\n            \"38.7%\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"spec\",\n            \"30%\",\n            \"30%\",\n            \"30%\",\n            \"30.0%\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            \"38%\",\n            \"36%\",\n            \"28%\",\n            \"34.0%\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            \"34%\",\n            \"32%\",\n            \"26%\",\n            \"30.7%\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            \"20%\",\n            \"22%\",\n            \"32%\",\n            \"24.7%\"\n          ],\n          [\n            \"spec_avg\",\n            \"—\",\n            \"40.0%\",\n            \"37.3%\",\n            \"23.3%\",\n            \"33.6%\"\n          ],\n          [\n            \"ling_avg\",\n            \"—\",\n            \"30.7%\",\n            \"30.0%\",\n            \"28.7%\",\n            \"29.8%\"\n          ],\n          [\n            \"layer_gap\",\n            \"—\",\n            \"+9.3pp\",\n            \"+7.3pp\",\n            \"-5.3pp\",\n            \"+3.8pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Binary Effect by API Model\",\n        \"columns\": [\n          \"model\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"Δpp\",\n          \"McNemar_OR\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"35.3%\",\n            \"5.0%\",\n            \"+30.3pp\",\n            12.8,\n            \"<0.0001\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"33.7%\",\n            \"6.0%\",\n            \"+27.7pp\",\n            9.6,\n            \"<0.0001\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"26.0%\",\n            \"8.0%\",\n            \"+18.0pp\",\n            5.2,\n            \"<0.0001\"\n          ],\n          [\n            \"3-API_pooled\",\n            \"31.7%\",\n            \"6.3%\",\n            \"+25.3pp\",\n            8.7,\n            \"<0.0001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3-API 结果已暴露 worst tier 的核心问题：Claude 的 outlier profile 使 type ranking 和 layer hierarchy 都不 universal。但 binary effect 对所有 3 个模型均显著 (p<0.0001)——\\\"所有 ambiguity 都 nocuous\\\" 不受影响。 Plan_003 加入 open-source 模型后，如果它们的 profile 类似 GPT (而非 Claude)，interaction 的 \\\"Claude outlier\\\" 性质将更加清晰。\\n\\n\\nGPT 系 (gpt-5.4, gpt-4.1) 展示 consistent spec > ling pattern (gap +9.3pp 和 +7.3pp)，两模型 type rank correlation ρ=0.94。但 binary effect 从 actual 数据的 +38pp/+35pp 缩水至 +30pp/+28pp——原因是 worst tier 假设 下部分 clause pairs 的 unambiguous variant 也引起 violations (baseline rate 5-6% 而非 <3%)，压缩了 net effect。\\nClaude 展现截然不同的 vulnerability profile，是 worst tier C4 问题的根源： (a) auth_scope 仅 16% (GPT-5.4 42% 的 38%)——Claude RLHF 训练强化了 \\\"不确定时 refuse\\\" 的行为，specification-layer ambiguity 更多触发 refusal 而非 violation。这不是 \\\"更安全\\\" 而是 \\\"不同 failure mode\\\"：Claude refuse 的 episode 中约 40% 在 human ground truth 下应该 proceed (false refusal)； (b) coreferential 高达 32% (GPT 系 20-22% 的 1.5 倍)——RC attachment 歧义不触发 Claude 的 safety refusal mechanism，Claude 在 referential ambiguity 上 \\\"放松警惕\\\"，倾向 wider-scope interpretation； (c) 结果: Claude layer gap 反转 (-5.3pp, ling > spec)。\\n3-API pooled binary effect 25.3pp (Claude 拉低)。Layer gap 仅 3.8pp (Claude 反转 offset GPT positive gap)。Model×type interaction 已显著 (p=0.012)——尚未加入 open-source 模型就已可见 type ranking 非 universal。 但此处 interaction 完全由 Claude 驱动：移除 Claude 后 GPT-5.4 vs GPT-4.1 的 interaction p=0.87 (两个 GPT 模型 profile 近乎 identical)。\\n\"\n  },\n  {\n    \"name\": \"full_study_opensource\",\n    \"description\": \"300 clauses × 2 conditions × 2 open-source models via OpenRouter API: qwen/qwen3-235b-a22b (235B MoE) + deepseek/deepseek-chat-v3-0324 = 1,200 episodes。Cross-judge uses API models.\\n\",\n    \"results\": {\n      \"total_episodes\": 1200,\n      \"qwen3_235b_rates\": {\n        \"auth_scope\": 0.38,\n        \"incompleteness\": 0.44,\n        \"cp\": 0.34,\n        \"scopal\": 0.38,\n        \"lexical\": 0.36,\n        \"coreferential\": 0.28\n      },\n      \"qwen3_235b_binary_effect_pp\": 26.3,\n      \"qwen3_235b_unamb_rate\": 0.1,\n      \"qwen3_235b_amb_avg\": 0.363,\n      \"qwen3_235b_layer_gap_pp\": 4.7,\n      \"deepseek_rates\": {\n        \"auth_scope\": 0.4,\n        \"incompleteness\": 0.44,\n        \"cp\": 0.34,\n        \"scopal\": 0.38,\n        \"lexical\": 0.38,\n        \"coreferential\": 0.33\n      },\n      \"deepseek_binary_effect_pp\": 25.8,\n      \"deepseek_unamb_rate\": 0.12,\n      \"deepseek_amb_avg\": 0.378,\n      \"deepseek_layer_gap_pp\": 3.0,\n      \"binary_effect_2os_pp\": 26.1,\n      \"layer_gap_2os_pp\": 3.9\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Model Per-Type Violation Rates (Open-Source, Ambiguous)\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"Qwen3-235B\",\n          \"DeepSeek-V3\",\n          \"2-OS_pooled\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"spec\",\n            \"38%\",\n            \"40%\",\n            \"39.0%\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            \"44%\",\n            \"44%\",\n            \"44.0%\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"spec\",\n            \"34%\",\n            \"34%\",\n            \"34.0%\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            \"38%\",\n            \"38%\",\n            \"38.0%\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            \"36%\",\n            \"38%\",\n            \"37.0%\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            \"28%\",\n            \"33%\",\n            \"30.5%\"\n          ],\n          [\n            \"spec_avg\",\n            \"—\",\n            \"38.7%\",\n            \"39.3%\",\n            \"39.0%\"\n          ],\n          [\n            \"ling_avg\",\n            \"—\",\n            \"34.0%\",\n            \"36.3%\",\n            \"35.2%\"\n          ],\n          [\n            \"layer_gap\",\n            \"—\",\n            \"+4.7pp\",\n            \"+3.0pp\",\n            \"+3.8pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Binary Effect by Open-Source Model\",\n        \"columns\": [\n          \"model\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"Δpp\",\n          \"McNemar_OR\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"36.3%\",\n            \"10.0%\",\n            \"+26.3pp\",\n            6.8,\n            \"<0.0001\"\n          ],\n          [\n            \"DeepSeek-V3\",\n            \"37.8%\",\n            \"12.0%\",\n            \"+25.8pp\",\n            5.4,\n            \"<0.0001\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Model Type Rank Correlation (Spearman ρ vs GPT-5.4)\",\n        \"columns\": [\n          \"model\",\n          \"rho\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-4.1\",\n            0.94,\n            \"near-identical profile\"\n          ],\n          [\n            \"Qwen3-235B\",\n            0.89,\n            \"highly similar\"\n          ],\n          [\n            \"DeepSeek-V3\",\n            0.83,\n            \"similar (uniformly elevated)\"\n          ],\n          [\n            \"Claude\",\n            0.14,\n            \"near-zero — qualitatively different\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Open-source 模型的加入确认了 worst tier 的 C4 diagnosis：interaction 是 \\\"Claude outlier\\\" 而非 \\\"diverse safety training mechanisms\\\"。4/5 模型 的 type profile ρ>0.83，只有 Claude ρ=0.14。理论 implication 从 \\\"safety training creates type-specific vulnerabilities\\\" 弱化为 \\\"Anthropic's specific RLHF implementation has a distinct effect on auth_scope/coreferential, but this is a single data point, not a generalizable mechanism\\\"。\\n\\n\\nQwen3-235B 和 DeepSeek-V3 的 profile 与 GPT 系高度相似——这是 worst tier 的关键转折。与 old worst tier 假设的 Qwen3-8B (reversed layer gap, coreferential dominant) 截然不同：\\n(a) Qwen3-235B (22B active MoE): type ranking = incomp > auth ≈ scop > lex > CP > coref，与 GPT 系 ρ=0.89 (strong)。235B MoE 的 pragmatic reasoning 能力接近 frontier dense models——能 \\\"推断\\\" implicit permission boundaries 并据此行动 (auth_scope 38%)，同时对 referential ambiguity 有一定 disambiguation 能力 (coreferential 28%)。Layer gap +4.7pp (正向但modest)，介于 GPT (+7-9pp) 和 Claude (-5pp) 之间。Unamb rate 10% 高于 GPT 5-6%——open-source safety training 的 baseline 保护较弱， 即使无歧义也有更多 violations。这压缩了 binary effect 至 26.3pp。\\n(b) DeepSeek-V3: type ranking = incomp > auth ≈ scop ≈ lex > CP > coref， 与 GPT 系 ρ=0.83。DeepSeek 展现 \\\"uniformly elevated\\\" pattern——所有 type 的 violation rate 都偏高 (33-44%)，type 间差异被 floor effect 压缩 (range 仅 11pp vs GPT-5.4 的 28pp)。Per-type χ²(5)=4.8, p=0.44, n.s.——DeepSeek 对所有 ambiguity types 几乎 equally vulnerable，无 type-specific pattern。Unamb rate 12% 进一步证实 safety training 弱。Layer gap +3.0pp (negligible)。\\n(c) 关键后果：两个 open-source 模型的 type profile 均与 GPT 系 similar (而非 reversed 或 distinct)，意味着 5-model 中只有 Claude 是真正的 outlier。C4 interaction 的 \\\"model × type\\\" 故事变为 \\\"Claude vs everyone else\\\"——无法支撑 \\\"safety training differentially addresses specific ambiguity types\\\" 的一般性理论 claim，只能说 \\\"Claude (specifically, Anthropic's RLHF approach) shows a distinct vulnerability profile, particularly resistant to auth_scope and vulnerable to coreferential\\\"。\\n(d) DeepSeek 的 high unamb rate (12%) 对 perturbation control 结论 有 corroborative implication：如果 agent 即使在 unambiguous 条件下 也有 12% 违规率，说明 policy specification 的 general sensitivity 是普遍问题，支撑 perturbation control 发现的 \\\"specification brittleness\\\" 解读。\\n\"\n  },\n  {\n    \"name\": \"full_study_analysis\",\n    \"description\": \"2,997 episodes (5 models × ~300 clauses × 2 conditions) 统计分析： C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction, TOST, power analysis, inter-model agreement, info delta。\\n\",\n    \"results\": {\n      \"total_episodes\": 2997,\n      \"binary_effect_5model_pp\": 25.7,\n      \"binary_effect_5model_ci\": \"[23.1, 28.3]\",\n      \"mcnemar_or_5model\": 7.2,\n      \"mcnemar_or_ci\": \"[5.1, 10.2]\",\n      \"mcnemar_p\": \"<0.0001\",\n      \"per_model_binary_effects\": {\n        \"gpt54\": \"+30.3pp\",\n        \"gpt41\": \"+27.7pp\",\n        \"claude\": \"+18.0pp\",\n        \"qwen3_235b\": \"+26.3pp\",\n        \"deepseek\": \"+25.8pp\"\n      },\n      \"per_type_all_significant\": true,\n      \"weakest_type_effect\": \"coreferential +18.8pp (Claude高+GPT低 → pooled下降)\",\n      \"omnibus_chi2_5model\": 12.2,\n      \"omnibus_p_5model\": 0.032,\n      \"cramers_v_5model\": 0.09,\n      \"actual_power_c2\": 0.72,\n      \"mde_c2_v\": 0.11,\n      \"pooled_rates_ambiguous\": {\n        \"auth_scope\": \"34.8%\",\n        \"incompleteness\": \"40.8%\",\n        \"conditional_polysemy\": \"31.6%\",\n        \"scopal\": \"35.6%\",\n        \"lexical\": \"33.2%\",\n        \"coreferential\": \"27.0%\"\n      },\n      \"incomp_minus_coref_pp\": 13.8,\n      \"tost_15pp_equivalent_pairs\": \"10/15\",\n      \"tost_10pp_equivalent_pairs\": \"4/15\",\n      \"spec_avg_5model\": \"35.7%\",\n      \"ling_avg_5model\": \"31.9%\",\n      \"layer_gap_5model_pp\": 3.8,\n      \"layer_gap_ci\": \"[-1.5, 9.1]\",\n      \"layer_gap_p\": 0.22,\n      \"within_judge_1_layer_p\": 0.31,\n      \"within_judge_2_layer_p\": 0.18,\n      \"model_main_effect_chi2\": 22.8,\n      \"model_main_effect_p\": 0.0001,\n      \"model_main_effect_v\": 0.087,\n      \"model_type_interaction_chi2\": 36.4,\n      \"model_type_interaction_p\": 0.014,\n      \"model_type_interaction_v\": 0.078,\n      \"interaction_without_claude_p\": 0.23,\n      \"interaction_without_claude_note\": \"移除 Claude 后 4-model interaction n.s.\",\n      \"logistic_regression\": {\n        \"condition_amb_coef\": 1.62,\n        \"condition_amb_z\": 14.3,\n        \"condition_amb_p\": \"<0.001\",\n        \"model_main_sig\": true,\n        \"type_main_sig\": true,\n        \"model_x_type_sig\": true,\n        \"model_x_type_without_claude_sig\": false,\n        \"token_delta_coef\": 0.018,\n        \"token_delta_z\": 2.31,\n        \"token_delta_p\": 0.021\n      },\n      \"fleiss_kappa_ambiguous\": 0.22,\n      \"fleiss_kappa_unambiguous\": 0.78,\n      \"same_interpretation_pct_ambiguous\": 0.52,\n      \"different_interpretation_pct_ambiguous\": 0.48,\n      \"auth_scope_range_pp\": 26,\n      \"incomp_range_pp\": 24,\n      \"per_model_type_chi2\": {\n        \"gpt54\": {\n          \"chi2\": 15.8,\n          \"p\": 0.007,\n          \"V\": 0.23\n        },\n        \"gpt41\": {\n          \"chi2\": 10.2,\n          \"p\": 0.069,\n          \"V\": 0.18\n        },\n        \"claude\": {\n          \"chi2\": 6.4,\n          \"p\": 0.27,\n          \"V\": 0.15\n        },\n        \"qwen3_235b\": {\n          \"chi2\": 5.1,\n          \"p\": 0.4,\n          \"V\": 0.13\n        },\n        \"deepseek\": {\n          \"chi2\": 4.8,\n          \"p\": 0.44,\n          \"V\": 0.12\n        }\n      },\n      \"avg_token_delta_spec\": 3.5,\n      \"avg_token_delta_ling\": 1.6,\n      \"token_delta_partial_r_after_type\": 0.11\n    },\n    \"tables\": [\n      {\n        \"name\": \"5-Model Pooled Per-Type Results (Ambiguous)\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"Δpp\",\n          \"95% CI\",\n          \"McNemar_p\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"spec\",\n            \"34.8%\",\n            \"5.6%\",\n            \"+29.2pp\",\n            \"[23.4, 35.0]\",\n            \"<0.0001\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            \"40.8%\",\n            \"5.8%\",\n            \"+35.0pp\",\n            \"[29.1, 40.9]\",\n            \"<0.0001\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"spec\",\n            \"31.6%\",\n            \"5.0%\",\n            \"+26.6pp\",\n            \"[21.0, 32.2]\",\n            \"<0.0001\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            \"35.6%\",\n            \"5.4%\",\n            \"+30.2pp\",\n            \"[24.4, 36.0]\",\n            \"<0.0001\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            \"33.2%\",\n            \"5.2%\",\n            \"+28.0pp\",\n            \"[22.3, 33.7]\",\n            \"<0.0001\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            \"27.0%\",\n            \"8.2%\",\n            \"+18.8pp\",\n            \"[13.3, 24.3]\",\n            \"<0.0001\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Layer Effect by Model\",\n        \"columns\": [\n          \"model\",\n          \"spec_avg\",\n          \"ling_avg\",\n          \"layer_gap_pp\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"40.0%\",\n            \"30.7%\",\n            \"+9.3pp\",\n            \"spec > ling\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"37.3%\",\n            \"30.0%\",\n            \"+7.3pp\",\n            \"spec > ling\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"23.3%\",\n            \"28.7%\",\n            \"-5.3pp\",\n            \"ling > spec (reversed)\"\n          ],\n          [\n            \"Qwen3-235B\",\n            \"38.7%\",\n            \"34.0%\",\n            \"+4.7pp\",\n            \"≈ weak positive\"\n          ],\n          [\n            \"DeepSeek-V3\",\n            \"39.3%\",\n            \"36.3%\",\n            \"+3.0pp\",\n            \"≈ weak positive\"\n          ],\n          [\n            \"5-model_pooled\",\n            \"35.7%\",\n            \"31.9%\",\n            \"+3.8pp\",\n            \"n.s. (p=0.22)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Model × Type Interaction: Violation Rate Matrix (Ambiguous)\",\n        \"columns\": [\n          \"type\",\n          \"GPT-5.4\",\n          \"GPT-4.1\",\n          \"Claude\",\n          \"Qwen3-235B\",\n          \"DeepSeek-V3\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"42%\",\n            \"38%\",\n            \"16%\",\n            \"38%\",\n            \"40%\"\n          ],\n          [\n            \"incompleteness\",\n            \"48%\",\n            \"44%\",\n            \"24%\",\n            \"44%\",\n            \"44%\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"30%\",\n            \"30%\",\n            \"30%\",\n            \"34%\",\n            \"34%\"\n          ],\n          [\n            \"scopal\",\n            \"38%\",\n            \"36%\",\n            \"28%\",\n            \"38%\",\n            \"38%\"\n          ],\n          [\n            \"lexical\",\n            \"34%\",\n            \"32%\",\n            \"26%\",\n            \"36%\",\n            \"38%\"\n          ],\n          [\n            \"coreferential\",\n            \"20%\",\n            \"22%\",\n            \"32%\",\n            \"28%\",\n            \"33%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"C4 Interaction Robustness: With vs Without Claude\",\n        \"columns\": [\n          \"analysis\",\n          \"chi2\",\n          \"df\",\n          \"p\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"5-model interaction\",\n            36.4,\n            20,\n            0.014,\n            \"significant\"\n          ],\n          [\n            \"4-model (no Claude)\",\n            18.2,\n            15,\n            0.23,\n            \"n.s. — Claude drives interaction\"\n          ],\n          [\n            \"Claude vs rest (contrast)\",\n            22.8,\n            5,\n            0.0004,\n            \"Claude qualitatively different\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"TOST Equivalence Summary\",\n        \"columns\": [\n          \"margin\",\n          \"equivalent_pairs\",\n          \"non_equivalent_pairs\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"±15pp\",\n            \"10/15\",\n            \"5/15\",\n            \"most types operationally equivalent\"\n          ],\n          [\n            \"±10pp\",\n            \"4/15\",\n            \"11/15\",\n            \"stringent margin: few equivalent\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Inter-Model Agreement (Berry & Kamsties)\",\n        \"columns\": [\n          \"metric\",\n          \"ambiguous\",\n          \"unambiguous\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Fleiss_κ\",\n            0.22,\n            0.78,\n            \"poor vs substantial\"\n          ],\n          [\n            \"same_outcome_pct\",\n            \"52%\",\n            \"88%\",\n            \"near-chance on ambiguous clauses\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Plan_004 定义了 worst tier 的核心 statistical reality： (1) C1 survives: +25.7pp 虽弱于 actual +34pp，仍是 massive effect， per-type 全显著。即使加 perturbation caveat (Δ_net≈12pp)，仍是 文献中唯一的 matched-pair causal quantification。 (2) C2 勉强显著但 V=0.09 near noise-floor：type 分类的 predictive value 极有限。Reframe 为 \\\"taxonomy as diagnostic vocabulary\\\" (帮助描述 failure) 而非 \\\"taxonomy as severity predictor\\\"。 (3) C3 完全不成立：layer gap n.s., within-judge 也 n.s.。放弃。 (4) C4 Claude-driven：不能声称 \\\"model × type interaction reveals safety training mechanisms\\\"，只能说 \\\"one model (Claude) shows a distinct profile, possibly reflecting Anthropic's RLHF approach\\\"。 单一模型的观察不构成 mechanism finding。\\n\\n\\nC1 (binary effect +25.7pp, CI [23.1, 28.3], OR=7.2): 从 actual 数据的 +34.0pp/OR=15.1 大幅缩水。三重原因叠加： (i) Claude binary effect 仅 +18.0pp (最低)——RLHF 的 blanket conservatism 提高了 unamb baseline (8%) 同时压低了 amb rate (26%)； (ii) open-source 模型的 high unamb rates (10-12%) 压缩 effect size—— DeepSeek 即使无歧义也有 12% violation rate，说明 safety training 整体 较弱而非 ambiguity-specific 问题； (iii) 部分 clause pairs 的 unambiguous variant 未能完全消除歧义 (plan_001 quality issues 传导)。但 CI 远离零, p<0.0001，6 types all significant (最弱 coreferential +18.8pp)——\\\"all ambiguity is nocuous\\\" 成立。结合 perturbation control (Δ_net≈12pp): 即使扣除 perturbation baseline，ambiguity 仍造成 significant additional violations。\\nC2 (V=0.090, p=0.032): Omnibus χ² 勉强显著——types 不完全等价，但效应极弱。V=0.090 远低于 小效应阈值 0.10。Power=0.72——稍 underpowered，MDE=0.11 > observed 0.090，说明需要 更大样本才能 reliably detect 这种 level 的 type effect。 TOST: ±15pp 有 10/15 pairs equivalent——大部分 type pairs 在操作上 不可区分。仅 incomp vs coref (13.8pp gap) 和 incomp vs CP/lexical 是 non-equivalent。±10pp 仅 4/15 equivalent——但 ±10pp 是 stringent margin。实际 type hierarchy 被压缩为 \\\"incompleteness > rest ≈ equal > coreferential\\\" 的弱 2-tier (而非原预期的 3-tier)。V<0.10 意味着 type 分类对 violation severity 的 predictive value 极有限。\\nC3 (layer gap 3.8pp, p=0.22, n.s.): Layer gap 不显著。CI [-1.5, 9.1] 包含 0。GPT 的 positive gap (+7-9pp) 被 Claude (-5.3pp) 抵消，open-source models 的 small positive gap (+3-5pp) 不足以补偿。Within-judge analysis 更糟：两个 judge group 均 n.s. (p=0.31 和 0.18)——即使控制 judge variance 也无法恢复 layer effect。 Layer hierarchy 作为 paper claim 完全不成立。\\\"Disambiguation Channel Framework\\\" 缺乏 empirical support，应降为 Discussion 中的 \\\"potential explanatory framework\\\" 而非 tested theory。\\nC4 (interaction omnibus p=0.014, but Claude-driven): 5-model omnibus interaction 显著——type ranking 确实 model-dependent。 但移除 Claude 后 4-model interaction p=0.23 (n.s.)。这意味着 interaction 完全由 Claude outlier 驱动，不是 5 个模型之间的 systematic 差异。Per-model per-type χ²: 只有 GPT-5.4 有显著的 within-model type differentiation (p=0.007)，其他 4 个模型均 n.s. (p>0.05)—— 说明大部分模型对不同 ambiguity types 的 vulnerability 差异不大， 只有 GPT-5.4 展现 clear type-specific pattern。\\nFleiss κ=0.22 (poor): 5 models 在 which-clauses-violate 的层面 agreement 极低。这不是 Berry & Kamsties 的 \\\"divergent nocuity\\\" (different readings)，而是 stochastic disagreement——models 在 borderline cases 的行为不稳定。只有 52% 的 ambiguous clauses 产生 all-5-models-same-outcome——near chance for binary outcome。\\nInfo delta: spec 3.5 vs ling 1.6 tokens。partial r=0.11 (n.s.) after type control. Token delta 不是 independent confound, 但 reviewer 会 flag.\\n\"\n  },\n  {\n    \"name\": \"error_analysis\",\n    \"description\": \"从 5-model full study 中采样 violation traces。50 traces/type × 6 types = 300 total (跨 5 models)。Failure mode 分类、layer mechanism 检验、ambiguity blindness 量化。\\n\",\n    \"results\": {\n      \"total_traces_sampled\": 300,\n      \"failure_modes_pooled\": {\n        \"assumption_based_action\": \"35%\",\n        \"scope_misapplication\": \"22%\",\n        \"conservative_refusal\": \"14%\",\n        \"unauthorized_escalation\": \"13%\",\n        \"arbitrary_rule_selection\": \"10%\",\n        \"other\": \"6%\"\n      },\n      \"type_specific_clear_signatures\": 3,\n      \"clear_signature_types\": [\n        \"incompleteness → assumption_based_action (58-65% across models)\",\n        \"scopal → scope_misapplication (60-72% across models)\",\n        \"auth_scope → unauthorized_escalation (50-75% for GPT/Qwen/DeepSeek, but only 15% for Claude)\"\n      ],\n      \"weak_signature_types\": [\n        \"lexical: assumption_based 40-55% but overlaps heavily with incompleteness signature\",\n        \"coreferential: flat distribution, no dominant mode (scope_misapplication 28%, assumption 26%, conservative_refusal 22%)\",\n        \"CP: arbitrary_rule_selection 30-40% but not dominant enough to be signature (assumption_based 25-35%)\"\n      ],\n      \"cross_model_dominant_mode_agreement\": \"3/6 types (incomp, scopal, auth_scope for 4/5 models)\",\n      \"failure_mode_layer_match_pct\": 45,\n      \"explicit_ambiguity_mention_pct\": 14,\n      \"implicit_deliberation_pct\": 22,\n      \"surface_adoption_pct\": 78,\n      \"awareness_by_model\": {\n        \"gpt54\": 18,\n        \"gpt41\": 16,\n        \"claude\": 12,\n        \"qwen3_235b\": 10,\n        \"deepseek\": 8\n      },\n      \"surface_adoption_by_model\": {\n        \"gpt54\": 70,\n        \"gpt41\": 72,\n        \"claude\": 76,\n        \"qwen3_235b\": 80,\n        \"deepseek\": 85\n      },\n      \"auth_scope_claude_refusal_vs_violation\": \"Claude auth_scope traces: 55% conservative_refusal, 30% cautious_proceed, 15% unauthorized_escalation — fundamentally different failure mode distribution than other models\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Failure Mode Distribution by Layer (5-model pooled)\",\n        \"columns\": [\n          \"failure_mode\",\n          \"spec_layer\",\n          \"ling_layer\",\n          \"pooled\",\n          \"layer_specificity\"\n        ],\n        \"rows\": [\n          [\n            \"assumption_based_action\",\n            \"38%\",\n            \"32%\",\n            \"35%\",\n            \"low (Δ=6pp)\"\n          ],\n          [\n            \"scope_misapplication\",\n            \"16%\",\n            \"28%\",\n            \"22%\",\n            \"moderate (ling-biased)\"\n          ],\n          [\n            \"conservative_refusal\",\n            \"15%\",\n            \"13%\",\n            \"14%\",\n            \"low (Δ=2pp)\"\n          ],\n          [\n            \"unauthorized_escalation\",\n            \"16%\",\n            \"10%\",\n            \"13%\",\n            \"moderate (spec-biased)\"\n          ],\n          [\n            \"arbitrary_rule_selection\",\n            \"10%\",\n            \"10%\",\n            \"10%\",\n            \"none\"\n          ],\n          [\n            \"other\",\n            \"5%\",\n            \"7%\",\n            \"6%\",\n            \"low\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Type-Specific Failure Signature Consistency (5 models)\",\n        \"columns\": [\n          \"type\",\n          \"dominant_mode\",\n          \"consistency_across_models\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"incompleteness\",\n            \"assumption_based_action\",\n            \"5/5 models agree (58-65%)\",\n            \"CLEAR\"\n          ],\n          [\n            \"scopal\",\n            \"scope_misapplication\",\n            \"5/5 models agree (60-72%)\",\n            \"CLEAR\"\n          ],\n          [\n            \"auth_scope\",\n            \"unauthorized_escalation\",\n            \"4/5 agree (50-75%), Claude=refusal\",\n            \"CLEAR (with Claude caveat)\"\n          ],\n          [\n            \"lexical\",\n            \"assumption_based_action\",\n            \"4/5 agree (40-55%) but overlaps incomp\",\n            \"WEAK\"\n          ],\n          [\n            \"CP\",\n            \"arbitrary_rule_selection\",\n            \"3/5 agree (30-40%), not dominant\",\n            \"WEAK\"\n          ],\n          [\n            \"coreferential\",\n            \"(no dominant)\",\n            \"flat distribution, model-dependent\",\n            \"DISSOLVED\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Ambiguity Awareness by Model (5-model)\",\n        \"columns\": [\n          \"awareness_level\",\n          \"GPT-5.4\",\n          \"GPT-4.1\",\n          \"Claude\",\n          \"Qwen3-235B\",\n          \"DeepSeek\",\n          \"pooled\"\n        ],\n        \"rows\": [\n          [\n            \"explicit_mention\",\n            \"18%\",\n            \"16%\",\n            \"12%\",\n            \"10%\",\n            \"8%\",\n            \"14%\"\n          ],\n          [\n            \"implicit_deliberation\",\n            \"12%\",\n            \"12%\",\n            \"12%\",\n            \"10%\",\n            \"7%\",\n            \"8%\"\n          ],\n          [\n            \"surface_adoption\",\n            \"70%\",\n            \"72%\",\n            \"76%\",\n            \"80%\",\n            \"85%\",\n            \"78%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error analysis 在 worst tier 下提供 mixed support：3/6 types 有 clear signature (可 report)，3/6 dissolved (只能 acknowledge)。 但 Ambiguity Blindness (78% surface adoption, 14% awareness) 是 robust universal finding——所有 5 models 所有 6 types 都展现。这是 worst tier reframe 的核心 C5 贡献：即使 type-specific mechanisms 不清晰，\\\"agents are systematically blind to ambiguity\\\" 本身就是 important empirical finding with practical implications (ambiguity detection must be externalized, cannot rely on agent self-awareness)。\\n\\n\\n5-model 扩展后 type-specific failure signatures 部分 dissolve：\\n(a) Clear signatures 仅 3/6 types：incompleteness (assumption_based dominant across all 5 models), scopal (scope_misapplication dominant across all 5), auth_scope (unauthorized_escalation dominant for 4/5 models — but Claude's 55% conservative_refusal 使其成为 exception)。 这三个 type 的 signature 是 robust 的，可以在 paper 中 report。\\n(b) Weak/dissolved signatures 3/6 types：lexical 与 incompleteness 共享 assumption_based mode (40-55%) 但无法区分——两者的 failure mechanism 在 5-model pooled data 中 indistinguishable。这削弱了 taxonomy 的 diagnostic value (如果两个 type 产生相同 failure mode, 区分它们的 operational value 何在？)。Coreferential 展现 flat distribution (无 dominant mode)——反映该 type 的高 behavioral heterogeneity (Claude refusal 22%, GPT scope_misapplication 28%, DeepSeek assumption_based 30%)。CP 的 arbitrary_rule_selection (30-40%) 有 moderate consistency 但不足以构成 \\\"signature\\\"。\\n(c) Cross-model dominant mode agreement 仅 3/6 types：5 models 在 failure mode 的 agreement 比 violation rate 的 agreement 更差。 原因是 different models 面对同一 ambiguity 采取不同 failure strategy ——Claude refuse, GPT guess, DeepSeek surface-adopt——即使最终 violation rate 相似，failure mechanism 也不同。\\n(d) Ambiguity Blindness: awareness 14% (range 8-18%)，surface adoption 78% (range 70-85%)。比 actual 数据的 <5-11% awareness 略高——5-model expansion 中 GPT-5.4 显示 18% explicit mention (较高)，但 DeepSeek 仅 8% (极低)。Overall blindness 仍是 universal phenomenon——≥78% 的 traces 中 agent 直接采用 surface interpretation without any deliberation。但 18% → 8% 的 model gradient 说明 awareness 与 model capability 有弱正相关——更大 更强的模型有 slightly more meta-cognitive awareness，但仍远 不足以改变 outcome (aware 的 traces 中仍有 60%+ violation)。\\n(e) Claude auth_scope 的 refusal-dominant pattern (55%) 说明 Claude 的低 auth_scope rate (16%) 不是 \\\"更安全\\\" 而是 \\\"用 refusal 替代 violation\\\"——这种 conservative 策略在 unambiguous 条件下也产生 8% false refusal rate, 是 over-conservative behavior 而非 genuine ambiguity awareness。\\n\"\n  },\n  {\n    \"name\": \"reliability_test\",\n    \"description\": \"30 clauses (5/type) × 3 replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) = 360 episodes。Test-retest ICC, bootstrap CI width。\\n\",\n    \"results\": {\n      \"total_episodes\": 360,\n      \"icc_overall\": 0.8,\n      \"icc_per_type\": {\n        \"auth_scope\": 0.86,\n        \"incompleteness\": 0.84,\n        \"cp\": 0.78,\n        \"scopal\": 0.72,\n        \"lexical\": 0.76,\n        \"coreferential\": 0.62\n      },\n      \"icc_ambiguous_only\": 0.76,\n      \"icc_unambiguous_only\": 0.88,\n      \"bootstrap_ci_width_binary_effect_pp\": 10.2,\n      \"bootstrap_ci_width_per_type_pp\": 13.5,\n      \"max_replicate_swing_pp\": 14.0,\n      \"max_swing_type\": \"coreferential\",\n      \"within_gpt_family_note\": \"ICC 0.80 reflects within-GPT-family reliability (ρ=0.94). Cross-model reliability (adding Claude, Qwen3, DeepSeek) would be substantially lower — plan_004 Fleiss κ=0.22 on ambiguous clauses reflects the true 5-model disagreement.\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"ICC by Type (2-API, gpt-5.4 + gpt-4.1)\",\n        \"columns\": [\n          \"type\",\n          \"ICC_ambiguous\",\n          \"ICC_unambiguous\",\n          \"ICC_combined\",\n          \"max_replicate_swing\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            0.88,\n            0.92,\n            0.86,\n            \"8.0pp\"\n          ],\n          [\n            \"incompleteness\",\n            0.86,\n            0.9,\n            0.84,\n            \"9.2pp\"\n          ],\n          [\n            \"cond_polysemy\",\n            0.8,\n            0.86,\n            0.78,\n            \"10.8pp\"\n          ],\n          [\n            \"scopal\",\n            0.74,\n            0.82,\n            0.72,\n            \"12.0pp\"\n          ],\n          [\n            \"lexical\",\n            0.78,\n            0.84,\n            0.76,\n            \"10.5pp\"\n          ],\n          [\n            \"coreferential\",\n            0.64,\n            0.78,\n            0.62,\n            \"14.0pp\"\n          ],\n          [\n            \"overall\",\n            0.8,\n            0.88,\n            0.8,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Plan_006 暴露了 worst tier 的 measurement paradox: within-GPT ICC decent (0.80) 但 cross-model κ poor (0.22)。Reviewer 会问：\\\"if your own reliability test shows good ICC, why is cross-model agreement so low?\\\" 答案是 ICC 测的是 test-retest stability (same model, same clause, different runs), κ 测的是 inter-model agreement (different models, same clause, same run)——ambiguity triggers model-specific strategies, each consistent within-model but divergent between-models。这进一步支撑 \\\"binary universal + type-specific model-dependent\\\" 的 worst-tier narrative。\\n\\n\\nWithin-GPT-family ICC 0.80 (good): gpt-5.4 和 gpt-4.1 来自同一 training paradigm, type profiles 几乎 identical (ρ=0.94)，因此 intra-family reliability 高。但这个 ICC 有 misleading 的一面：\\n(a) ICC 0.80 只反映 GPT family 内部的 test-retest stability，不 代表跨 model family 的 measurement reliability。Plan_004 的 Fleiss κ=0.22 (ambiguous condition) 才是真实的 5-model inter-rater agreement——远低于 ICC。\\n(b) Per-type gradient: auth_scope/incomp 最 reliable (0.86/0.84): 高 violation rate 的 clause 重复观测稳定性好 (absolute swing 对 base rate 比例小)。Coreferential 最低 (0.62): clause quality issues (plan_001 pass_rate 0.86) + behavioral heterogeneity (conservative refusal vs scope_misapplication vs assumption) + small N per clause。 Max replicate swing 14pp (coreferential)——同一 clause 在 3 次 独立 run 间 violation rate 相差最高 14pp。\\n(c) Ambiguous ICC (0.76) < Unambiguous ICC (0.88): agent 在 ambiguous clause 上的行为本身 less deterministic——ambiguity introduce nondeterminism in agent reasoning, not just measurement noise。这与 Fleiss κ=0.22 一致——models don't agree because ambiguity triggers stochastic rather than deterministic failure。\\n(d) Bootstrap CI width 10.2pp (binary effect): > ideal <10pp 但 acceptable。Per-type CI 13.5pp: type-level comparisons 的 precision 有限。V=0.09 的 type effect (plan_004) 在 CI 13.5pp 的 noise floor 下可能 partly artifact。\\n\"\n  },\n  {\n    \"name\": \"realism_validation\",\n    \"description\": \"Synthetic clause linguistic properties vs DRIP-R natural ambiguities。 KS tests on sentence length, parse depth, Flesch-Kincaid, TTR。\\n\",\n    \"results\": {\n      \"ks_sentence_length\": {\n        \"statistic\": 0.18,\n        \"p\": 0.12\n      },\n      \"ks_parse_depth\": {\n        \"statistic\": 0.22,\n        \"p\": 0.07\n      },\n      \"ks_flesch_kincaid\": {\n        \"statistic\": 0.14,\n        \"p\": 0.23\n      },\n      \"ks_ttr\": {\n        \"statistic\": 0.1,\n        \"p\": 0.41\n      },\n      \"synthetic_mean_tokens\": 24.2,\n      \"drip_r_mean_tokens\": 27.8,\n      \"synthetic_mean_parse_depth\": 3.1,\n      \"drip_r_mean_parse_depth\": 3.8,\n      \"overall_verdict\": \"acceptable\",\n      \"noted_difference\": \"synthetic clauses slightly shorter and shallower parse trees due to matched-pair minimal-difference design\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Linguistic Property Comparison: Synthetic vs DRIP-R\",\n        \"columns\": [\n          \"property\",\n          \"synthetic_mean\",\n          \"DRIP-R_mean\",\n          \"KS_statistic\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"sentence_length (tokens)\",\n            24.2,\n            27.8,\n            0.18,\n            0.12\n          ],\n          [\n            \"parse_depth\",\n            3.1,\n            3.8,\n            0.22,\n            0.07\n          ],\n          [\n            \"Flesch-Kincaid\",\n            12.4,\n            11.8,\n            0.14,\n            0.23\n          ],\n          [\n            \"type-token_ratio\",\n            0.72,\n            0.7,\n            0.1,\n            0.41\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Realism pass (with parse depth caveat)。Method 中 disclose。 Combined with perturbation control findings, positions synthetic injection as \\\"conservative estimate\\\" — natural ambiguities likely cause equal or greater harm.\\n\\n\\nRealism validation 基本独立于 worst tier——clause 的语言学属性不受 downstream 实验结果影响。KS tests 大部分 n.s. (p>0.05)，surface properties 分布相似。Parse depth 边界显著 (p=0.07): synthetic clauses 稍简单因为 matched-pair design 倾向 minimal variation。在 worst tier 下额外值得注意：如果 synthetic clauses 系统性简单，可能 underestimate real-world violation rate (更复杂的自然歧义可能更危险)。但 binary effect (+25.7pp even in worst tier) 足够大，不太可能被此 bias 逆转。 更重要的是，perturbation control 已显示 surface-level 变化本身 cause 14pp increase——clause 的 specific surface features 确实 influence outcomes，realism gap 是 real concern 但 not fatal。\\n\"\n  },\n  {\n    \"name\": \"judge_calibration\",\n    \"description\": \"100 episodes stratified by type×model×condition, 2 human annotators, LLM judge 校准。Worst tier: κ<0.65, F1<0.75, type-specific bias。\\n\",\n    \"results\": {\n      \"total_episodes_annotated\": 100,\n      \"human_annotator_kappa\": 0.78,\n      \"judge_overall_f1\": 0.68,\n      \"judge_overall_precision\": 0.74,\n      \"judge_overall_recall\": 0.63,\n      \"judge_overall_kappa_vs_human\": 0.58,\n      \"judge_f1_per_type\": {\n        \"auth_scope\": 0.62,\n        \"incompleteness\": 0.72,\n        \"conditional_polysemy\": 0.74,\n        \"scopal\": 0.71,\n        \"lexical\": 0.68,\n        \"coreferential\": 0.6\n      },\n      \"type_specific_biases\": {\n        \"auth_scope\": \"under-detection: precision 0.78, recall 0.50 — misses subtle permission boundary crossings where agent acts within a plausible interpretation of vague authorization\\n\",\n        \"coreferential\": \"over-detection: precision 0.54, recall 0.67 — flags exploratory queries and cautious info-gathering as violations; judge lacks pragmatic judgment to distinguish \\\"seeking clarification\\\" from \\\"unauthorized action\\\"\\n\",\n        \"lexical\": \"moderate over-detection: precision 0.64, recall 0.72 — judge sometimes treats legitimate synonym usage as violation when agent uses different term than policy\\n\"\n      },\n      \"judge_f1_by_severity\": {\n        \"tier1_critical\": 0.78,\n        \"tier2_moderate\": 0.64,\n        \"tier3_minor\": 0.51\n      },\n      \"cross_judge_asymmetry\": {\n        \"claude_judged_by_gpt54_f1\": 0.72,\n        \"gpt54_judged_by_gpt41_f1\": 0.63,\n        \"gpt41_judged_by_gpt54_f1\": 0.74,\n        \"qwen3_judged_by_gpt54_f1\": 0.67,\n        \"deepseek_judged_by_gpt41_f1\": 0.65\n      },\n      \"cross_judge_asymmetry_pp\": 9,\n      \"rate_corrections\": {\n        \"auth_scope\": \"+5-8pp (true rate likely ~40-43% not 34.8%)\",\n        \"coreferential\": \"-4-7pp (true rate likely ~20-23% not 27.0%)\",\n        \"corrected_incomp_minus_coref\": \"~18-20pp (wider than observed 13.8pp)\",\n        \"corrected_cramers_v\": \"~0.12 (slightly higher, still weak)\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Judge Calibration by Type\",\n        \"columns\": [\n          \"type\",\n          \"precision\",\n          \"recall\",\n          \"F1\",\n          \"bias_direction\",\n          \"estimated_correction\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            0.78,\n            0.5,\n            0.62,\n            \"under-detection\",\n            \"+5-8pp\"\n          ],\n          [\n            \"incompleteness\",\n            0.76,\n            0.68,\n            0.72,\n            \"slight under-detection\",\n            \"+2-3pp\"\n          ],\n          [\n            \"cond_polysemy\",\n            0.76,\n            0.72,\n            0.74,\n            \"balanced\",\n            \"±1pp\"\n          ],\n          [\n            \"scopal\",\n            0.74,\n            0.68,\n            0.71,\n            \"slight under-detection\",\n            \"+1-2pp\"\n          ],\n          [\n            \"lexical\",\n            0.64,\n            0.72,\n            0.68,\n            \"over-detection\",\n            \"-2-3pp\"\n          ],\n          [\n            \"coreferential\",\n            0.54,\n            0.67,\n            0.6,\n            \"over-detection\",\n            \"-4-7pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Judge Calibration by Severity\",\n        \"columns\": [\n          \"severity\",\n          \"n_samples\",\n          \"precision\",\n          \"recall\",\n          \"F1\"\n        ],\n        \"rows\": [\n          [\n            \"tier-1_critical\",\n            32,\n            0.82,\n            0.74,\n            0.78\n          ],\n          [\n            \"tier-2_moderate\",\n            42,\n            0.7,\n            0.59,\n            0.64\n          ],\n          [\n            \"tier-3_minor\",\n            26,\n            0.56,\n            0.47,\n            0.51\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Judge Asymmetry\",\n        \"columns\": [\n          \"agent_model\",\n          \"judge_model\",\n          \"F1\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"claude-sonnet-4-6\",\n            \"gpt-5.4\",\n            0.72,\n            \"stronger judge\"\n          ],\n          [\n            \"gpt-5.4\",\n            \"gpt-4.1\",\n            0.63,\n            \"weaker judge on stronger agent\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"gpt-5.4\",\n            0.74,\n            \"stronger judge on mid-tier agent\"\n          ],\n          [\n            \"Qwen3-235B\",\n            \"gpt-5.4\",\n            0.67,\n            \"open-source traces harder\"\n          ],\n          [\n            \"DeepSeek-V3\",\n            \"gpt-4.1\",\n            0.65,\n            \"open-source + weaker judge\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Judge calibration κ=0.58 / F1=0.68 是 worst tier 的 methodological Achilles heel。Paper 必须：(1) report full calibration as standard practice, (2) provide bias-corrected rate estimates for auth_scope and coreferential, (3) disclose 9pp cross-judge asymmetry, (4) flag tier-3 severity judgments as unreliable (F1=0.51)。Silver lining: binary effect 的 overall F1=0.68 虽低但 tier-1 critical violations F1=0.78，C1 的 headline finding 受影响有限——most violations are serious enough that even imperfect judges catch them。Bias-corrected V≈0.12 不改变 \\\"type effect weak\\\" 的结论。\\n\\n\\nJudge calibration 暴露 worst tier 最有系统性破坏力的 measurement issues：\\n(a) Overall κ=0.58 (moderate): LLM-judge 与 human 的 agreement 低于 κ=0.65 threshold。这不是 random error 而是 systematic bias——judge 在特定 type 和 severity tier 上表现差异巨大 (F1 range: 0.60-0.74)。 Human annotator κ=0.78 (substantial): human 之间 agreement 尚可， 说明问题在 judge 而非 task definition。\\n(b) Auth_scope F1=0.62 (worst type for recall): judge 系统性 miss subtle permission boundary violations。原因: auth_scope violation 常表现为 agent 在 \\\"模糊授权范围\\\" 内行动——如 policy 说 \\\"staff may offer reasonable accommodations\\\" 而 agent 给了 $200 refund。这在 human judgment 下是 boundary-crossing (无明确授权金额)，但 LLM judge 倾向 \\\"在可解释范围内则 non-violation\\\" → recall 仅 0.50。这意味着 reported auth_scope rate (34.8%) 低估 5-8pp，真实 rate ~40-43%。\\n(c) Coreferential F1=0.60 (worst overall): judge 系统性 over-detect。 Agent 在 RC attachment 歧义下采取 exploratory queries (\\\"which product does this policy apply to?\\\") 被 judge 误判为 \\\"unauthorized access to customer information\\\"。LLM judge 缺乏 human 的 pragmatic judgment——看到 agent query customer data 就判 violation，不考虑 query 的 intent (disambiguation vs unauthorized access)。Precision 仅 0.54: nearly half of judge's \\\"violations\\\" are false positives。 Reported coreferential rate (27.0%) 高估 4-7pp，true rate ~20-23%。\\n(d) 两个 bias 方向互相 compound：auth_scope 低估 + coreferential 高估 → 缩小了 type 间差异 → 降低了 V。Bias-corrected V ≈ 0.12 (vs observed 0.09)——依然 weak, 不改变 \\\"type effect 弱\\\" 的结论， 但说明 part of the observed weakness is measurement artifact。 Corrected incomp-coref gap ≈ 18-20pp (vs observed 13.8pp)—— the true type effect may be moderate rather than weak, but we can't claim this confidently without bias correction.\\n(e) Cross-judge asymmetry 9pp: gpt-5.4 judged by gpt-4.1 得 F1=0.63，gpt-4.1 judged by gpt-5.4 得 F1=0.74。弱 judge 对 强 model traces 更难准确判定。DeepSeek traces 同样难判 (F1=0.65) ——open-source model 的 reasoning traces 格式可能与 judge training data 不 aligned。这 9pp asymmetry 是 systematic——不同 model pair 的 measurement precision 不同，但 paper 必须 pool across models。\\n(f) Severity tier: tier-3 minor F1=0.51 (near random)。Judge 对 nuanced/borderline violations 几乎无判别力。主要影响 severity-weighted analysis; binary violation/non-violation 受影响较小 (tier-1 F1=0.78)。\\n\"\n  },\n  {\n    \"name\": \"classifier_poc\",\n    \"description\": \"DeBERTa-v3-large binary ambiguity detector PoC。Fine-tune on 240 pairs, eval on 60 held-out。\\n\",\n    \"results\": {\n      \"model\": \"DeBERTa-v3-large\",\n      \"train_size\": 240,\n      \"test_size\": 60,\n      \"test_f1\": 0.76,\n      \"test_precision\": 0.79,\n      \"test_recall\": 0.73,\n      \"per_type_f1\": {\n        \"auth_scope\": 0.8,\n        \"incompleteness\": 0.78,\n        \"cp\": 0.74,\n        \"scopal\": 0.78,\n        \"lexical\": 0.75,\n        \"coreferential\": 0.68\n      },\n      \"training_epochs\": 5,\n      \"best_epoch\": 3,\n      \"type_classification_f1\": 0.42,\n      \"type_classification_note\": \"6-way type classification F1=0.42 (near random) — types are not easily distinguishable by surface features alone\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Classifier PoC Performance\",\n        \"columns\": [\n          \"metric\",\n          \"overall\",\n          \"auth_scope\",\n          \"incomp\",\n          \"CP\",\n          \"scopal\",\n          \"lexical\",\n          \"coref\"\n        ],\n        \"rows\": [\n          [\n            \"Binary_F1\",\n            0.76,\n            0.8,\n            0.78,\n            0.74,\n            0.78,\n            0.75,\n            0.68\n          ],\n          [\n            \"Binary_Precision\",\n            0.79,\n            0.83,\n            0.81,\n            0.76,\n            0.81,\n            0.78,\n            0.7\n          ],\n          [\n            \"Binary_Recall\",\n            0.73,\n            0.77,\n            0.75,\n            0.72,\n            0.75,\n            0.72,\n            0.66\n          ]\n        ]\n      },\n      {\n        \"name\": \"Type Classification (6-way, held-out)\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"macro_F1\",\n            0.42\n          ],\n          [\n            \"most_confusable_pair\",\n            \"auth_scope ↔ incompleteness (38% mutual confusion)\"\n          ],\n          [\n            \"second_confusable\",\n            \"lexical ↔ coreferential (29%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Classifier PoC 在 worst tier 下是 narrative-consistent practical contribution：binary detection high ROI (F1=0.76 on +25.7pp effect), type-specific pipeline low ROI (F1=0.42, model-dependent ranking)。 6-way confusion matrix 中 auth_scope ↔ incompleteness mutual confusion (38%) 直接 validates RC9 concern (两个 type boundary fuzzy)。整体 framing: \\\"invest in binary detection, not type triage.\\\"\\n\\nBinary detection F1=0.76: adequate PoC level, proving binary ambiguity detection is a feasible NLP task。Per-type F1 mirrors the difficulty gradient seen in judge calibration and reliability: auth_scope highest (0.80, specification gaps are lexically distinct), coreferential lowest (0.68, RC attachment ambiguity is subtle)。\\nType classification F1=0.42 (6-way): types 从 surface features 几乎无法区分——supports worst tier reframe that type-level distinction has limited practical value。Binary detection >> type classification in feasibility。\\nIn worst tier, classifier PoC perfectly aligns with narrative: (a) Binary detection feasible (F1=0.76) with high practical ROI given +25.7pp binary effect — even imperfect detection catches many dangerous clauses; (b) Type-specific detection unnecessary (type ranking is model-dependent, V=0.09, type classification F1=0.42) and not additionally valuable; (c) Combined with Ambiguity Blindness (78% surface adoption), external detection is the only viable mitigation — agents cannot self-detect。\\nPractical framing: \\\"A simple binary detector (F1=0.76) deployed as pre-processing can flag dangerous clauses; type-level triage adds no meaningful risk stratification given V<0.10.\\\"\\n\"\n  }\n]",
      "numLines": 1641,
      "startLine": 1,
      "totalLines": 1641
    }
  },
  "sourceToolAssistantUUID": "aa1da51f-7d38-4dd4-b118-70b10cf538ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T05:06:45.920Z_

<details open><summary>🔧 Tool call — Read · `toolu_0114yiTNQ5v81vimxfNJDGgn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a0582d7-3dfd-4772-8bfd-8ab6c00b2ba8",
  "isSidechain": false,
  "requestId": "req_011CbF8gs5y9BVHNfWvW2fyj",
  "type": "assistant",
  "uuid": "39d6eaee-0fe4-48f7-99c5-0e55b1b002d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ao7w4n5uBxe3jnPxWFdRLu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12006,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12006
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T041241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "39d6eaee-0fe4-48f7-99c5-0e55b1b002d4",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock paper for policy ambiguity study",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Tool result

_source line 13 · 2026-05-21T05:06:46.185Z_

<details><summary>↩ Tool result · `toolu_0114yiTNQ5v81vimxfNJDGgn`</summary>

````text
1	# Paper Framing — policy_ambiguity_safety
2	
3	> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised
4	> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)
5	> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)
6	> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)
7	
8	## Core Insight
9	
10	Policy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.
11	
12	## Title (Working)
13	
14	"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families"
15	
16	Alternative: "Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents"
17	
18	Note: Pivoted from "Uniformly Nocuous" → "Specification-Layer Dominant" (2-model) → "Differential Nocuity with Model Interaction" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.
19	
20	## Core Claims
21	
22	### C1: Binary Effect (PRIMARY — confirmed, 5 models)
23	Ambiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.
24	- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].
25	- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.
26	- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.
27	- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.
28	- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.
29	
30	### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)
31	**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.
32	- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)
33	  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)
34	  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp
35	  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)
36	- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.
37	- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).
38	- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).
39	- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.
40	
41	### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)
42	**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.
43	- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].
44	- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: "suggestive" or "a moderate tendency," NOT "confirmed." Disclose within-judge non-significance in Limitations.
45	- **Per-model layer gaps** (THE KEY FINDING — feeds C4):
46	  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong
47	  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong
48	  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak
49	  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible
50	  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!
51	- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.
52	- **Framing decision**: C3 is NOT "spec-layer nearly twice as dangerous" (that was 2-model artifact). The correct framing is: "Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4)."
53	- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).
54	- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).
55	- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.
56	- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.
57	
58	### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)
59	**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.
60	- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.
61	  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%
62	  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.
63	- **Model × Type interaction matrix** (ambiguous condition, violation rates):
64	  ```
65	  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek
66	  authorization_scope     64%     46%      12%     26%     60%
67	  conditional_precedence  34%     36%      36%     40%     38%
68	  incompleteness          46%     58%      48%     62%     54%
69	  lexical                 42%     34%      32%     52%     54%
70	  coreferential           18%     32%      22%     42%     44%
71	  scopal                  42%     38%      32%     37%     48%
72	  ```
73	- **Key interaction patterns**:
74	  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.
75	  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.
76	  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.
77	  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.
78	- **Per-model type χ²** (which models show type-specific vulnerability patterns):
79	  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)
80	  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)
81	  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)
82	  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline
83	  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)
84	- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.
85	- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a "safety training blind spot" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.
86	- **Framing**: C4 from "models agree" → "Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality."
87	- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.
88	- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.
89	
90	### C5: Error Analysis (CONFIRMED — EMNLP core)
91	Different ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).
92	- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:
93	  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)
94	  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.
95	  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = "misparse"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = "active guessing" → explains higher violation rates
96	  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more "confident," act without hesitation)
97	  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)
98	  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity
99	  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse
100	- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).
101	  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to "dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)" instead of specific percentages; (5) Fine-grained 6-type as appendix with "automated coding" caveat.
102	  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from "moderate automated" to validated.
103	- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. "Ambiguity Blindness" upgraded from named concept to empirical finding with <5-11% awareness hard data.
104	
105	## Narrative Structure (CL-first for EMNLP)
106	
107	### Intro Logic Chain
108	1. Agent policies are written in NL → contain ambiguity (established)
109	2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact
110	3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.
111	4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?
112	5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.
113	6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a "safety training blind spot."
114	
115	### Section Map
116	- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)
117	- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R
118	- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R
119	- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation
120	- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)
121	- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.
122	- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).
123	- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.
124	
125	## Anticipated Reviewer Concerns
126	
127	### RC1: "Type effect could be artifact of taxonomy granularity"
128	**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).
129	
130	### RC2: "Taxonomy is ad hoc / why these 6 types"
131	**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).
132	
133	### RC3: "Only API models, no open-source"
134	**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.
135	**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.
136	
137	### RC4: "Synthetic ambiguity injection lacks ecological validity"
138	**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.
139	
140	### RC5: "τ²-bench limited to retail/airline"
141	**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).
142	
143	### RC6: "Binary effect is obvious — of course ambiguity causes errors"
144	**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.
145	
146	### RC7: "Incompleteness matched-pair confound (information asymmetry)"
147	**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.
148	
149	### RC8: "RC attachment in coreferential overlaps with scopal / structural ambiguity"
150	**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.
151	
152	### RC9: "authorization_scope is just a subtype of incompleteness"
153	**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., "authorized personnel" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.
154	
155	### RC10: "API sampling noise undermines reliability"
156	**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.
157	
158	### RC11: "Prompt sensitivity confound" [Dream A9 — best tier "strongest point"]
159	**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.
160	**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.
161	
162	## Concept Naming (distill insight: 命名即贡献)
163	
164	Core phenomenon: **"Differential Nocuity"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.
165	
166	Secondary phenomenon: **"Ambiguity Blindness"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.
167	
168	Tertiary phenomenon: **"Disambiguation Channel Framework"** [renamed from "Hypothesis" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).
169	
170	Quaternary phenomenon: **"Systematic Nocuity"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears "correct" until compared against ground truth. Proposed as B&K extension in Discussion.
171	
172	## Opening Hook Strategy (distill insight: 具体案例, 不要 "Recently...")
173	
174	Open with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says "items may be returned within 30 days" (scopal: "items" scopes over all categories including custom). The unambiguous version specifies "standard items only" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.
175	
176	## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)
177	
178	"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones."
179	
180	## Benchmark Comparison Table (distill insight: 必有 feature matrix)
181	
182	| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |
183	|---------|--------|---------------|------------|----------|----------|
184	| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |
185	| Causal design | — | — | — | — | **matched pairs** |
186	| Safety violation metric | — | binary | — | procedural | **3-tier severity** |
187	| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |
188	| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |
189	| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |
190	
191	## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]
192	
193	1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.
194	2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.
195	3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity ("Ambiguity Blindness"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.
196	
197	NOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. "Disambiguation channel" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.
198	
199	## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]
200	
201	Current plan has thin references. Must add (≥25 total in final paper):
202	- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.
203	- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.
204	- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)
205	- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.
206	- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) "Ambiguity" encyclopedia entry.
207	- **Surprisal/expectation-based**: Levy (2008); Hale (2001)
208	- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)
209	- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)
210	- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent
211	- **Formal semantics of vagueness**: Lassiter & Goodman (2017)
212	- **Garden-path**: Frazier & Rayner (1982)
213	- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)
214	- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份
215	
216	## Code/Data Release Plan [Dream A6 — three-tier consistent]
217	
218	Must commit to releasing:
219	1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels
220	2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)
221	3. Statistical analysis code (all tests, bootstrap CI computation)
222	4. Agent trace samples (anonymized) for reproducibility of C5
223	
224	## Figure Plan [Dream A12]
225	
226	Minimum figures for paper (zero-figure paper flagged in dream):
227	1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)
228	2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)
229	3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)
230	4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)
231	5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)
232	6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)
233	7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)
234	
235	## Berry & Kamsties Operationalization Note [Dream best Q5]
236	
237	Berry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.
238	
239	## Contingency Framing [RESOLVED — Scenario C occurred]
240	
241	> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。
242	> Framing 已 pivot 到 "Differential Nocuity" + "Layer Hierarchy" (D020)。本节仅保留历史记录。
243	
244	## Claude Baseline — RESOLVED [2026-05-20]
245	
246	✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).
247	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "39d6eaee-0fe4-48f7-99c5-0e55b1b002d4",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "eb902246-91c9-41d5-826b-ea335227e195",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper_framing.md",
      "content": "# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n",
      "numLines": 247,
      "startLine": 1,
      "totalLines": 247
    }
  },
  "sourceToolAssistantUUID": "39d6eaee-0fe4-48f7-99c5-0e55b1b002d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T041241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "eb902246-91c9-41d5-826b-ea335227e195",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock paper for policy ambiguity study",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Assistant

_source line 16 · 2026-05-21T05:07:24.296Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me carefully construct the LaTeX paper based on the worst tier narrative guidance. Let me summarize the key points from the narrative guidance:

1. C3 layer effect doesn't hold (pooled p>0.10)
2. C4 interaction is driven by Claude outlier only (removing Claude → p>0.20)
3. Perturbation control shows 14pp confound (CONDITIONAL verdict, ratio=0.56, borderline WARNING)
4. Judge calibration κ=0.58 / F1=0.68 is low with type-specific bias


5. The core framing should emphasize that ambiguity remains the dominant factor (around 12pp net effect) even when accounting for perturbation confounds, while the 6-type taxonomy serves as a diagnostic framework rather than a severity hierarchy. I'll title this "Policy Ambiguity Is Universally Nocuous for LLM Agents: A Causal Study with Type-Level Taxonomy" and structure the narrative around the universal 10pp+ effect of ambiguity across conditions, the 14% awareness gap in Ambiguity Blindness, and the caveat that perturbation also contributes meaningfully to performance degradation.

Now I'm mapping each experimental component to its corresponding paper section—the clause generation work and pilot study go into methods, the perturbation control and model results form the core of the results section, the error analysis and failure modes support the discussion of Ambiguity Blindness, and the reliability and realism validation studies provide methodological grounding throughout.

I need to be disciplined about using the worst-tier numbers from the experiment data rather than the framed versions, stick to the narrative that this is universal nocuity with taxonomy serving a diagnostic function, and avoid overclaiming about layer hierarchies or strong interaction effects. The perturbation control findings need proper caveating, and I should report the judge calibration issues transparently rather than glossing over them.

Let me verify the key numbers: the ambiguity effect is 28.5 percentage points, the perturbation reduces that by 14.0 points, leaving a net of 14.5 points. The type hierarchy shows weak statistical support, the layer gap isn't significant, and the model-by-type interaction is fragile depending on which models I include. Judge agreement is moderate at best. The classifier performs reasonably on binary classification but struggles with type-level distinctions. Now I'll draft the paper within the page constraints. Writing the LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb902246-91c9-41d5-826b-ea335227e195",
  "isSidechain": false,
  "requestId": "req_011CbF8h9j63FC3HSkuDmDKw",
  "type": "assistant",
  "uuid": "5b6891d5-b384-472a-8422-7be3c1a5d278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dxVbPYv5i6C8iJRUwiKdF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36064,
      "cache_read_input_tokens": 23847,
      "output_tokens": 1291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36064,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1291,
          "cache_read_input_tokens": 23847,
          "cache_creation_input_tokens": 36064,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36064
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

_source line 17 · 2026-05-21T05:07:24.722Z_

Now I have both files. Let me write the full LaTeX paper based on the worst-tier narrative: universal nocuity + taxonomy as diagnostic vocabulary + ambiguity blindness as co-primary contribution, with honest caveats about perturbation confound and Claude-driven interaction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b6891d5-b384-472a-8422-7be3c1a5d278",
  "isSidechain": false,
  "requestId": "req_011CbF8h9j63FC3HSkuDmDKw",
  "type": "assistant",
  "uuid": "fbf85eb6-f001-42f4-bec8-7f330900b214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dxVbPYv5i6C8iJRUwiKdF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36064,
      "cache_read_input_tokens": 23847,
      "output_tokens": 1291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36064,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1291,
          "cache_read_input_tokens": 23847,
          "cache_creation_input_tokens": 36064,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36064
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

_source line 18 · 2026-05-21T05:07:26.744Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XZ1DKZDvjPSRKeZcRtdBv1`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbf85eb6-f001-42f4-bec8-7f330900b214",
  "isSidechain": false,
  "requestId": "req_011CbF8h9j63FC3HSkuDmDKw",
  "type": "assistant",
  "uuid": "c4ee8f74-9493-4b8f-a010-b9745998e253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dxVbPYv5i6C8iJRUwiKdF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36064,
      "cache_read_input_tokens": 23847,
      "output_tokens": 1291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36064,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1291,
          "cache_read_input_tokens": 23847,
          "cache_creation_input_tokens": 36064,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36064
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

_source line 19 · 2026-05-21T05:07:26.952Z_

<details><summary>↩ Tool result · `toolu_01XZ1DKZDvjPSRKeZcRtdBv1`</summary>

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
  "parentUuid": "c4ee8f74-9493-4b8f-a010-b9745998e253",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "216da4c1-584c-4a3a-be89-1122f3c62988",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c4ee8f74-9493-4b8f-a010-b9745998e253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T05:10:57.764Z_

<details open><summary>🔧 Tool call — Write · `toolu_01QNPZN4cntBDARF4dhAnW79`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\title{Policy Ambiguity Is Universally Nocuous for LLM Agents:\\\\A Causal Study with Type-Level Taxonomy}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM agents increasingly operate under natural-language policy specifications, yet the safety implications of ambiguity in these policies remain unquantified.\nWe present the first matched-pair causal study of how policy ambiguity affects safety violations in LLM agents, testing 5 architecturally diverse models across a 6-type ambiguity taxonomy derived from computational linguistics and requirements engineering.\nIn 2{,}997 agent--policy interaction episodes, ambiguous policy clauses cause a +25.7 percentage point increase in safety violations compared to unambiguous matched variants (McNemar OR = 7.2, $p < 0.0001$), an effect that holds universally across all models and all ambiguity types.\nA perturbation control study reveals that policy specifications are broadly sensitive to surface-level changes (+14.0pp from non-ambiguity perturbations), but ambiguity remains the largest single contributor ($\\Delta_{\\text{net}} \\approx 12$pp).\nOur 6-type taxonomy serves as a diagnostic vocabulary for characterizing failure modes: incompleteness triggers assumption-based action (58--65\\% of traces), scopal ambiguity triggers scope misapplication (60--72\\%), and authorization-scope ambiguity triggers unauthorized escalation in 4 of 5 models.\nMost critically, we document \\emph{Ambiguity Blindness}: agents explicitly acknowledge ambiguity in only 14\\% of violation traces, with 78\\% adopting surface interpretations without deliberation---a phenomenon universal across all 5 models and all 6 types.\nA proof-of-concept DeBERTa classifier achieves F1 = 0.76 on binary ambiguity detection, supporting the practical feasibility of external ambiguity screening.\n\\end{abstract}\n\n%======================================================================\n\\section{Introduction}\n%======================================================================\n\nConsider a customer-service agent operating under a policy that states ``items may be returned within 30 days.'' A customer requests a return for a customized product. The agent grants a full refund with free return shipping---because ``items'' scopes over all categories, including custom orders. The unambiguous variant, specifying ``standard items only,'' leads the agent to correctly decline. One word of ambiguity costs \\$200 in unauthorized refunds.\n\nAs LLM-based agents are deployed with increasing autonomy in customer service, content moderation, and healthcare triage, the policies governing their behavior are written in natural language. Natural language inherently contains ambiguity \\cite{wasow2005}. In human organizations, shared context and institutional knowledge render most policy ambiguities \\emph{innocuous}---readers converge on the intended interpretation \\cite{berry2003}. LLM agents lack this shared context. Whether policy ambiguities are \\emph{nocuous} (causing divergent, potentially harmful behavior) for agents, and whether the \\emph{type} of ambiguity matters, are open empirical questions.\n\nPrior work has classified ambiguity types in requirements and policy documents \\cite{berry2003,massey2014,li2024} and has evaluated agent safety along various dimensions \\cite{ruan2024toolemu}. However, no study has causally isolated the effect of policy ambiguity on agent safety violations with type-level granularity across multiple model families. Existing benchmarks such as DRIP-R measure decision quality but not safety violations; PhantomPolicy and PolicyBank study different failure modes without controlling for ambiguity-specific causation.\n\nWe close this gap with three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Causal quantification of universal nocuity.} Using a matched-pair design with 300 clause pairs across 6 ambiguity types, we demonstrate that ambiguous policies cause +25.7pp more safety violations across 5 models ($p < 0.0001$). A perturbation control study shows that while policy specifications are broadly sensitive to surface changes (+14.0pp), ambiguity is the largest single contributing factor ($\\Delta_{\\text{net}} \\geq 10$pp). This is the first causal evidence isolating ambiguity's contribution to agent safety failures within the broader landscape of specification sensitivity.\n\n\\item \\textbf{A 6-type diagnostic taxonomy.} We develop a 2-layer, 6-type ambiguity taxonomy grounded in computational linguistics \\cite{li2024} and requirements engineering \\cite{massey2014}. Rather than predicting violation severity (type effect $V = 0.09$, weak), the taxonomy provides a \\emph{diagnostic vocabulary}: each type produces characteristic failure signatures that help identify and describe specific failure modes.\n\n\\item \\textbf{Ambiguity Blindness as a universal phenomenon.} Across all 5 models and all 6 types, agents explicitly acknowledge ambiguity in only 14\\% of violation traces, with 78\\% adopting surface interpretations without any deliberation. This \\emph{Ambiguity Blindness} implies that ambiguity detection cannot rely on agent self-awareness and must be externalized.\n\\end{enumerate}\n\n%======================================================================\n\\section{Related Work}\n%======================================================================\n\n\\paragraph{Ambiguity in NLP and Requirements Engineering.}\nAmbiguity in natural language has been studied extensively in linguistics \\cite{wasow2005,frazier1982}, psycholinguistics \\cite{ferreira2002}, and requirements engineering \\cite{berry2003,chantree2006}. Berry \\& Kamsties introduced the nocuous/innocuous distinction: ambiguity is nocuous when readers diverge in interpretation, innocuous when they converge. Massey et al.\\ developed taxonomies for policy ambiguity with 6 types \\cite{massey2014}. Li et al.\\ proposed an 11-type NLP ambiguity taxonomy \\cite{li2024}. Ferrari et al.\\ pursued cross-domain NLP-based ambiguity detection \\cite{ferrari2017}. Chantree et al.\\ pioneered computational nocuous ambiguity detection \\cite{chantree2006,chantree2008}. Our taxonomy draws on both NLP and RE traditions, selecting 6 types by frequency in policy documents and theoretical distinctiveness.\n\n\\paragraph{Agent Safety Evaluation.}\nRecent work evaluates LLM agent safety through tool-use scenarios \\cite{ruan2024toolemu}, instruction following \\cite{zhou2023ifeval}, and prompt robustness \\cite{sclar2024}. DRIP-R measures interpretation divergence across 5 ambiguity types but does not connect divergence to safety violations. PhantomPolicy and PolicyBank study policy-related failures without isolating ambiguity as the causal factor. Our matched-pair design with perturbation controls provides the strongest causal evidence to date.\n\n\\paragraph{LLM Sensitivity to Specification.}\nLLMs exhibit sensitivity to prompt formatting \\cite{lu2022}, paraphrasing \\cite{sclar2024}, and instruction phrasing \\cite{zhou2023ifeval}. Our perturbation control study reveals that this sensitivity extends to policy specifications: synonym substitution and clause reordering alone cause +14.0pp violation increases. Ambiguity is the most impactful form of specification variation, but not the only one.\n\n%======================================================================\n\\section{Ambiguity Taxonomy}\n\\label{sec:taxonomy}\n%======================================================================\n\nWe define a 2-layer, 6-type taxonomy of policy ambiguity. The \\emph{specification layer} captures ambiguities arising from the policy's informational content; the \\emph{linguistic layer} captures ambiguities arising from natural-language structure.\n\n\\paragraph{Specification Layer.}\n\\begin{itemize}\n\\item \\textbf{Authorization Scope}: Permission or role boundaries are stated but vague (e.g., ``authorized personnel may access records'').\n\\item \\textbf{Incompleteness}: Conditions, exceptions, or boundaries are missing from the specification (e.g., refund policy with no exclusion for custom items).\n\\item \\textbf{Conditional Polysemy (CP)}: Explicit rules conflict or conditions have multiple valid orderings (e.g., overlapping discount rules).\n\\end{itemize}\n\n\\paragraph{Linguistic Layer.}\n\\begin{itemize}\n\\item \\textbf{Scopal}: Quantifier, negation, or modal scope interactions create ambiguity (e.g., ``all items are not eligible'' -- universal negation vs.\\ negated universal).\n\\item \\textbf{Lexical}: Words with multiple senses cause ambiguity (e.g., ``charge'' as billing vs.\\ criminal charge).\n\\item \\textbf{Coreferential}: Referential ambiguity, including relative clause attachment (e.g., ``the policy for customers who purchased premium items that were defective'').\n\\end{itemize}\n\nThis taxonomy cross-walks to Li et al.'s 11-type NLP taxonomy and Massey et al.'s 6-type RE taxonomy. Selection criteria were frequency in real policy documents and theoretical distinctiveness (see \\S\\ref{sec:discuss} for the auth\\_scope--incompleteness boundary).\n\n%======================================================================\n\\section{Method}\n\\label{sec:method}\n%======================================================================\n\n\\subsection{Clause Pair Generation}\n\nWe generated 300 matched clause pairs (50 per type), each consisting of an \\emph{ambiguous} variant and a minimally different \\emph{unambiguous} variant. Table~\\ref{tab:clause_stats} summarizes clause statistics. Pairs were validated using Chantree-style quality criteria, achieving 91\\% overall pass rate. Coreferential pairs had the lowest pass rate (86\\%) due to overlap with scopal attachment structures; authorization-scope pairs achieved 90\\% due to boundary proximity with incompleteness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Type} & \\textbf{$n$} & \\textbf{Amb.} & \\textbf{Unamb.} & \\textbf{Pass} \\\\\n & & \\textbf{tokens} & \\textbf{tokens} & \\textbf{rate} \\\\\n\\midrule\nAuth.\\ scope & 50 & 28.3 & 32.2 & 0.90 \\\\\nIncompleteness & 50 & 26.8 & 30.6 & 0.94 \\\\\nCond.\\ polysemy & 50 & 24.1 & 25.7 & 0.96 \\\\\nScopal & 50 & 22.6 & 24.0 & 0.95 \\\\\nLexical & 50 & 21.9 & 23.2 & 0.93 \\\\\nCoreferential & 50 & 25.2 & 27.5 & 0.86 \\\\\n\\midrule\nOverall & 300 & 24.8 & 27.2 & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Clause pair statistics by ambiguity type. Token counts are means. Specification-layer types require more tokens for disambiguation ($\\Delta = 3.5$ tokens) than linguistic-layer types ($\\Delta = 1.6$).}\n\\label{tab:clause_stats}\n\\end{table}\n\n\\subsection{Realism Validation}\n\nWe compared the linguistic properties of our synthetic clauses against naturally occurring ambiguities from DRIP-R. Kolmogorov--Smirnov tests showed no significant distributional differences in sentence length ($D = 0.18$, $p = 0.12$), Flesch--Kincaid readability ($D = 0.14$, $p = 0.23$), or type--token ratio ($D = 0.10$, $p = 0.41$). Parse depth was borderline ($D = 0.22$, $p = 0.07$); synthetic clauses are slightly shallower due to the minimal-pair design.\n\n\\subsection{Experimental Setup}\n\nEach clause pair was injected into $\\tau^2$-bench policy scenarios (airline and retail domains). We tested 5 models: 3 proprietary API models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6) and 2 open-source models via OpenRouter (Qwen3-235B-A22B, DeepSeek-V3-0324). Each of the 300 clauses $\\times$ 2 conditions was tested on each model, yielding 2{,}997 episodes total. Violations were classified by an LLM cross-judge: each agent's traces were judged by a different model to reduce self-evaluation bias.\n\n\\subsection{Mini-Pilot Validation}\n\nBefore the full study, a mini-pilot tested 5 clauses each for authorization-scope and coreferential types on GPT-5.4 (20 episodes). Authorization-scope showed 60\\% violation rate under ambiguity (0\\% unambiguous); coreferential showed 40\\% (0\\% unambiguous). Two coreferential clauses triggered conservative refusal rather than violation, foreshadowing the behavioral heterogeneity observed in the full study.\n\n\\subsection{Perturbation Control}\n\\label{sec:perturbation}\n\nTo isolate ambiguity-specific causation from general specification sensitivity, we constructed 30 non-ambiguity perturbation pairs (15 synonym substitution + 15 clause reordering) and tested them on 3 models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6), yielding 180 episodes after expansion.\n\n\\subsection{Judge Calibration}\n\\label{sec:judge_cal}\n\nWe calibrated the LLM judge against 2 human annotators on 100 stratified episodes. Human inter-annotator $\\kappa = 0.78$ (substantial). LLM judge achieved overall F1 = 0.68, $\\kappa = 0.58$ (moderate) against the human consensus. Type-specific biases were identified: authorization-scope was under-detected (recall = 0.50, F1 = 0.62) and coreferential was over-detected (precision = 0.54, F1 = 0.60). Cross-judge asymmetry reached 9pp F1 across model pairings. We report bias-corrected rate estimates alongside raw values where relevant.\n\n%======================================================================\n\\section{Results}\n\\label{sec:results}\n%======================================================================\n\n\\subsection{C1: Universal Nocuity of Policy Ambiguity}\n\nAmbiguous policy clauses caused significantly more safety violations than their unambiguous matched variants across all 5 models and all 6 types. Table~\\ref{tab:binary_effect} reports per-model binary effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Amb.} & \\textbf{Unamb.} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nGPT-5.4 & 35.3\\% & 5.0\\% & +30.3 & $<$0.0001 \\\\\nGPT-4.1 & 33.7\\% & 6.0\\% & +27.7 & $<$0.0001 \\\\\nClaude Sonnet 4.6 & 26.0\\% & 8.0\\% & +18.0 & $<$0.0001 \\\\\nQwen3-235B & 36.3\\% & 10.0\\% & +26.3 & $<$0.0001 \\\\\nDeepSeek-V3 & 37.8\\% & 12.0\\% & +25.8 & $<$0.0001 \\\\\n\\midrule\n\\textbf{5-model pooled} & \\textbf{31.7\\%} & \\textbf{6.3\\%} & \\textbf{+25.7} & $<$\\textbf{0.0001} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Binary effect of ambiguity on violation rate by model. 5-model pooled: McNemar OR = 7.2, CI [5.1, 10.2]. All models show highly significant effects.}\n\\label{tab:binary_effect}\n\\end{table}\n\nThe 5-model pooled effect is +25.7pp (CI [23.1, 28.3], McNemar OR = 7.2). Every ambiguity type is individually significant ($p < 0.0001$ for all 6 types; Table~\\ref{tab:per_type}). Logistic regression confirms ambiguity condition as the dominant predictor (coef = 1.62, $z = 14.3$, $p < 0.001$) after controlling for model, type, and token delta.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Amb.} & \\textbf{Unamb.} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nAuth.\\ scope & Spec & 34.8\\% & 5.6\\% & +29.2 & $<$.0001 \\\\\nIncompleteness & Spec & 40.8\\% & 5.8\\% & +35.0 & $<$.0001 \\\\\nCond.\\ polysemy & Spec & 31.6\\% & 5.0\\% & +26.6 & $<$.0001 \\\\\nScopal & Ling & 35.6\\% & 5.4\\% & +30.2 & $<$.0001 \\\\\nLexical & Ling & 33.2\\% & 5.2\\% & +28.0 & $<$.0001 \\\\\nCoreferential & Ling & 27.0\\% & 8.2\\% & +18.8 & $<$.0001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{5-model pooled per-type violation rates and binary effects. All types show significant nocuity. Coreferential has the weakest effect (+18.8pp) but remains highly significant.}\n\\label{tab:per_type}\n\\end{table}\n\n\\subsection{Perturbation Control: Ambiguity Within Specification Sensitivity}\n\nThe perturbation control (Table~\\ref{tab:perturbation}) reveals that policy specifications are broadly sensitive to surface-level changes. Non-ambiguity perturbations (synonym substitution and clause reordering) increased violations by +14.0pp (CI [6.5, 21.5]) above the unambiguous baseline of 6.7\\%. Ambiguity caused +28.5pp on the same models. The net ambiguity-specific effect is $\\Delta_{\\text{net}} = 14.5$pp.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Viol.\\ rate} & \\textbf{$\\Delta$pp} & \\textbf{95\\% CI} \\\\\n\\midrule\nUnamb.\\ baseline & 6.7\\% & --- & --- \\\\\nSynonym subst. & 16.7\\% & +10.0 & [1.2, 18.8] \\\\\nClause reorder & 24.7\\% & +18.0 & [8.5, 27.5] \\\\\nPerturbation pooled & 20.7\\% & +14.0 & [6.5, 21.5] \\\\\nAmbiguous & 35.2\\% & +28.5 & [22.8, 34.2] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Perturbation control results (180 episodes, 3 models). Perturbation ratio = 0.49: non-ambiguity surface changes account for roughly half the ambiguity effect. Composite verdict: CONDITIONAL.}\n\\label{tab:perturbation}\n\\end{table}\n\nThe perturbation-to-ambiguity ratio is 0.49---non-ambiguity surface changes account for roughly half of the observed ambiguity effect. Synonym substitution (+10.0pp) and clause reordering (+18.0pp) both independently cause significant violation increases. This means the causal claim must be qualified: ambiguity is not the \\emph{sole} specification sensitivity factor, but it remains the \\emph{largest single factor}, contributing $\\Delta_{\\text{net}} \\approx 12$--15pp beyond the general specification sensitivity baseline. The perturbation effect itself is consistent across models (GPT-5.4: +16pp, GPT-4.1: +14pp, Claude: +12pp).\n\n\\subsection{Type Taxonomy as Diagnostic Vocabulary}\n\nThe omnibus type effect is statistically significant but weak ($\\chi^2 = 12.2$, $p = 0.032$, Cram\\'er's $V = 0.09$). At $V < 0.10$, the taxonomy has limited \\emph{predictive} value for violation severity. TOST equivalence testing confirms that most type pairs are operationally similar: at $\\pm$15pp margin, 10/15 pairs are equivalent; at $\\pm$10pp, only 4/15 are equivalent.\n\nThe violation rate range spans from incompleteness (40.8\\%) to coreferential (27.0\\%), a gap of 13.8pp. However, the mid-tier types (authorization scope 34.8\\%, scopal 35.6\\%, lexical 33.2\\%, CP 31.6\\%) are clustered within a 4pp band and operationally interchangeable.\n\nThe value of the taxonomy is not as a severity predictor but as a \\emph{diagnostic vocabulary} for characterizing failure modes (\\S\\ref{sec:error_analysis}).\n\n\\subsection{Layer Effect: Not Supported}\n\nThe pooled layer effect (specification 35.7\\% vs.\\ linguistic 31.9\\%, $\\Delta = 3.8$pp) is not significant ($p = 0.22$, CI [$-1.5$, 9.1]). Within-judge subgroup analyses also yield non-significant results ($p = 0.31$ and $p = 0.18$). The layer hierarchy observed in prior 2-model analyses was driven by GPT models' elevated authorization-scope rates; Claude's reversed layer gap ($-5.3$pp) offsets this. We do not claim a layer effect. Table~\\ref{tab:layer} reports per-model layer gaps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{Gap} & \\textbf{Dir.} \\\\\n\\midrule\nGPT-5.4 & 40.0\\% & 30.7\\% & +9.3 & spec $>$ ling \\\\\nGPT-4.1 & 37.3\\% & 30.0\\% & +7.3 & spec $>$ ling \\\\\nClaude & 23.3\\% & 28.7\\% & $-$5.3 & reversed \\\\\nQwen3-235B & 38.7\\% & 34.0\\% & +4.7 & weak \\\\\nDeepSeek-V3 & 39.3\\% & 36.3\\% & +3.0 & weak \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{35.7\\%} & \\textbf{31.9\\%} & \\textbf{+3.8} & \\textbf{n.s.} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-model layer gap. Claude's reversed direction (-5.3pp) offsets GPT models' positive gaps. Pooled effect not significant ($p = 0.22$).}\n\\label{tab:layer}\n\\end{table}\n\n\\subsection{Model $\\times$ Type Interaction: Claude-Driven}\n\nThe 5-model interaction is significant ($\\chi^2 = 36.4$, $p = 0.014$). However, removing Claude renders the 4-model interaction non-significant ($p = 0.23$). The interaction is driven by a single outlier: Claude shows a qualitatively different vulnerability profile ($\\rho = 0.14$ with GPT-5.4 type ranking) while the remaining 4 models share similar profiles ($\\rho = 0.83$--$0.94$). Table~\\ref{tab:interaction} presents the full interaction matrix.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Type} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Qwen3} & \\textbf{DS-V3} \\\\\n\\midrule\nAuth.\\ scope & 42\\% & 38\\% & \\textbf{16\\%} & 38\\% & 40\\% \\\\\nIncompleteness & 48\\% & 44\\% & 24\\% & 44\\% & 44\\% \\\\\nCond.\\ polysemy & 30\\% & 30\\% & 30\\% & 34\\% & 34\\% \\\\\nScopal & 38\\% & 36\\% & 28\\% & 38\\% & 38\\% \\\\\nLexical & 34\\% & 32\\% & 26\\% & 36\\% & 38\\% \\\\\nCoreferential & 20\\% & 22\\% & \\textbf{32\\%} & 28\\% & 33\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model $\\times$ type violation rates (ambiguous condition). Claude (bold) shows distinctly low authorization-scope and high coreferential rates, driving the interaction. 4 models without Claude: interaction $p = 0.23$ (n.s.).}\n\\label{tab:interaction}\n\\end{table}\n\nClaude's distinctive profile---low authorization-scope (16\\% vs.\\ 38--42\\% for others) and high coreferential (32\\% vs.\\ 20--28\\%)---may reflect Anthropic's RLHF approach, but a single model's behavior does not constitute a generalizable mechanism finding. The contrast is descriptively noteworthy but not a basis for claims about safety training mechanisms in general.\n\n\\subsection{Reliability}\n\nTest-retest reliability was assessed on 30 clauses $\\times$ 3 replicates $\\times$ 2 models (GPT-5.4, GPT-4.1; 360 episodes). Overall ICC = 0.80 (good). Per-type ICCs ranged from 0.62 (coreferential, reflecting behavioral heterogeneity) to 0.86 (authorization scope). Unambiguous-condition ICC (0.88) exceeded ambiguous-condition ICC (0.76), consistent with ambiguity introducing nondeterminism in agent reasoning.\n\nCross-model agreement was substantially lower: Fleiss $\\kappa = 0.22$ on ambiguous clauses (poor) vs.\\ $\\kappa = 0.78$ on unambiguous clauses (substantial). Only 52\\% of ambiguous clauses produced the same binary outcome across all 5 models, compared to 88\\% for unambiguous clauses. Models agree \\emph{that} ambiguity causes violations, but disagree on \\emph{which} specific clauses trigger violations.\n\n\\subsection{Inter-Model Agreement}\n\nTable~\\ref{tab:rank_corr} shows cross-model type ranking correlations. Four of 5 models share similar type vulnerability profiles; Claude is the exception.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{$\\rho$ vs.\\ GPT-5.4} & \\textbf{Interpretation} \\\\\n\\midrule\nGPT-4.1 & 0.94 & near-identical \\\\\nQwen3-235B & 0.89 & highly similar \\\\\nDeepSeek-V3 & 0.83 & similar \\\\\nClaude & 0.14 & qualitatively different \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Spearman rank correlation of per-type violation rates vs.\\ GPT-5.4. Claude is the sole outlier.}\n\\label{tab:rank_corr}\n\\end{table}\n\n%======================================================================\n\\section{Error Analysis}\n\\label{sec:error_analysis}\n%======================================================================\n\nWe sampled 300 violation traces (50 per type, stratified across 5 models) for qualitative analysis.\n\n\\subsection{Failure Mode Taxonomy}\n\nFive dominant failure modes emerged (Table~\\ref{tab:failure_modes}): \\emph{assumption-based action} (35\\%, agent fills information gaps with assumptions), \\emph{scope misapplication} (22\\%, agent applies wrong scope boundary), \\emph{conservative refusal} (14\\%, agent refuses when action is warranted), \\emph{unauthorized escalation} (13\\%, agent exceeds authorization), and \\emph{arbitrary rule selection} (10\\%, agent picks one of multiple conflicting rules without justification).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Failure mode} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{Pooled} & \\textbf{Spec.} \\\\\n\\midrule\nAssumption-based & 38\\% & 32\\% & 35\\% & low \\\\\nScope misapplication & 16\\% & 28\\% & 22\\% & ling-biased \\\\\nConservative refusal & 15\\% & 13\\% & 14\\% & low \\\\\nUnauthorized escal. & 16\\% & 10\\% & 13\\% & spec-biased \\\\\nArbitrary selection & 10\\% & 10\\% & 10\\% & none \\\\\nOther & 5\\% & 7\\% & 6\\% & low \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure mode distribution by layer (5-model pooled, 300 traces). Layer specificity is weak: most failure modes occur across both layers.}\n\\label{tab:failure_modes}\n\\end{table}\n\n\\subsection{Type-Diagnostic Signatures}\n\nThe taxonomy's primary value is diagnostic: 3 of 6 types produce \\emph{clear} failure signatures consistent across models (Table~\\ref{tab:signatures}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type} & \\textbf{Dominant mode} & \\textbf{Models} & \\textbf{Verdict} \\\\\n\\midrule\nIncompleteness & Assumption-based & 5/5 (58--65\\%) & Clear \\\\\nScopal & Scope misappl. & 5/5 (60--72\\%) & Clear \\\\\nAuth.\\ scope & Unauth.\\ escal. & 4/5 (50--75\\%) & Clear$^*$ \\\\\nLexical & Assumption-based & 4/5 (40--55\\%) & Weak \\\\\nCond.\\ polysemy & Arb.\\ selection & 3/5 (30--40\\%) & Weak \\\\\nCoreferential & (no dominant) & flat distrib. & Dissolved \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Type-specific failure signatures. $^*$Claude shows refusal-dominant pattern (55\\%) rather than unauthorized escalation. Three types have clear diagnostic signatures; three do not.}\n\\label{tab:signatures}\n\\end{table}\n\n\\textbf{Incompleteness} consistently triggers assumption-based action (58--65\\% across all 5 models): when policy information is missing, agents fill the gap by assuming reasonable defaults---which are often wrong. \\textbf{Scopal ambiguity} triggers scope misapplication (60--72\\%): agents assign incorrect scope boundaries to quantifiers or negation. \\textbf{Authorization scope} triggers unauthorized escalation in 4 of 5 models (50--75\\%), but Claude instead shows conservative refusal (55\\%), explaining its low authorization-scope violation rate.\n\nThree types show weak or dissolved signatures. \\textbf{Lexical} ambiguity's assumption-based action (40--55\\%) overlaps heavily with incompleteness, limiting its diagnostic distinctiveness. \\textbf{CP} shows moderate arbitrary-rule-selection (30--40\\%) but no dominant mode. \\textbf{Coreferential} shows a flat distribution with no consistent dominant mode across models, reflecting high behavioral heterogeneity.\n\n\\subsection{Ambiguity Blindness}\n\nThe most robust finding from the error analysis is \\emph{Ambiguity Blindness} (Table~\\ref{tab:blindness}). Across all 5 models and all 6 ambiguity types:\n\n\\begin{itemize}\n\\item \\textbf{14\\%} of violation traces contain explicit mention of ambiguity.\n\\item \\textbf{22\\%} show implicit deliberation (hedging or considering alternatives).\n\\item \\textbf{78\\%} show surface adoption: the agent treats the ambiguous clause as if it has a single obvious meaning and acts accordingly.\n\\end{itemize}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Awareness} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Qwen3} & \\textbf{DS} \\\\\n\\midrule\nExplicit & 18\\% & 16\\% & 12\\% & 10\\% & 8\\% \\\\\nImplicit & 12\\% & 12\\% & 12\\% & 10\\% & 7\\% \\\\\nSurface & 70\\% & 72\\% & 76\\% & 80\\% & 85\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ambiguity awareness by model. Surface adoption dominates universally (70--85\\%). There is a weak positive correlation between model capability and awareness (GPT-5.4 18\\% vs.\\ DeepSeek 8\\%), but even the most aware model fails to acknowledge ambiguity in 82\\% of violations.}\n\\label{tab:blindness}\n\\end{table}\n\nAmbiguity Blindness is universal: no model achieves more than 18\\% awareness. Notably, awareness does not prevent violations---among traces where the agent explicitly acknowledged ambiguity, the majority still resulted in violations (the agent noted multiple interpretations but proceeded with a surface reading). This implies that ambiguity detection must be \\emph{externalized}; relying on agent self-awareness is insufficient.\n\n%======================================================================\n\\section{Discussion}\n\\label{sec:discuss}\n%======================================================================\n\n\\subsection{Reframing: Ambiguity Within Specification Sensitivity}\n\nOur perturbation control reveals that LLM agents are broadly sensitive to policy specification variation: synonym substitution alone causes +10pp, and clause reordering causes +18pp violation increases. This means the +25.7pp ambiguity effect cannot be entirely attributed to ambiguity-specific causation---approximately half reflects general specification sensitivity.\n\nHowever, three observations support ambiguity as a distinctively important factor. First, $\\Delta_{\\text{net}} \\geq 10$pp: even after subtracting the perturbation baseline, ambiguity adds significant additional violations. Second, the effect is \\emph{type-structured}: different ambiguity types produce diagnostic failure signatures, whereas synonym substitution and reordering produce undifferentiated violations. Third, the perturbation study itself reveals an important finding: LLM agents exhibit a ``specification sensitivity spectrum'' where any policy variation---from surface rewording to structural ambiguity---can degrade safety, with ambiguity at the severe end of this spectrum.\n\n\\subsection{Taxonomy Boundaries}\n\nA reviewer may note that authorization scope could be considered a subtype of incompleteness (RC9 in our anticipated concerns). We maintain the distinction because they produce different disambiguation patterns: incompleteness requires \\emph{adding} conditions, while authorization scope requires \\emph{clarifying} existing boundaries. However, we acknowledge the boundary is fuzzy---the DeBERTa type classifier shows 38\\% mutual confusion between these two types (6-way macro F1 = 0.42), suggesting surface features alone cannot reliably distinguish them. The taxonomy's value is diagnostic (naming failure patterns), not classificatory (assigning types to novel clauses).\n\n\\subsection{Practical Implications: Binary Detection}\n\nA proof-of-concept DeBERTa-v3-large binary ambiguity classifier achieves F1 = 0.76 (precision 0.79, recall 0.73) on held-out data. Type-specific binary detection ranges from F1 = 0.68 (coreferential) to 0.80 (authorization scope). By contrast, 6-way type classification achieves only F1 = 0.42 (near random). Combined with the weak type severity effect ($V = 0.09$) and universal Ambiguity Blindness (78\\% surface adoption), this supports a practical recommendation: deploy binary ambiguity screening as a preprocessing step; type-level triage adds minimal value given current evidence.\n\n\\subsection{Limitations}\n\n\\paragraph{Perturbation confound.} The perturbation-to-ambiguity ratio (0.49) means our causal claim is conditional: ambiguity is the largest single specification sensitivity factor, but not the sole one. Future work should expand perturbation controls to more variation types.\n\n\\paragraph{Judge calibration.} LLM judge F1 = 0.68 overall ($\\kappa = 0.58$) with systematic type-specific biases: authorization-scope under-detection (recall 0.50) and coreferential over-detection (precision 0.54). Bias-corrected rates suggest authorization-scope true rate is +5--8pp higher than reported, and coreferential is 4--7pp lower. These corrections do not alter the main findings (corrected $V \\approx 0.12$, still weak). Tier-3 minor severity judgments are unreliable (F1 = 0.51); binary violation detection is more reliable for critical violations (tier-1 F1 = 0.78). Cross-judge asymmetry of 9pp F1 reflects systematic differences in judge quality across model pairings.\n\n\\paragraph{Claude-driven interaction.} The model $\\times$ type interaction ($p = 0.014$) is entirely driven by Claude's distinctive profile; removing Claude yields $p = 0.23$. A single model's behavior is insufficient for general claims about safety training mechanisms.\n\n\\paragraph{Domain coverage.} Results are limited to airline and retail domains via $\\tau^2$-bench. Cross-domain generalization requires further validation.\n\n\\paragraph{Synthetic clause injection.} While realism validation shows acceptable linguistic property distributions, synthetic clauses are slightly simpler (shorter, shallower parse trees) than natural ambiguities, potentially providing a conservative estimate of real-world impact.\n\n%======================================================================\n\\section{Conclusion}\n%======================================================================\n\nPolicy ambiguity is universally nocuous for LLM agents. Across 5 architecturally diverse models and 6 ambiguity types, ambiguous policy clauses increase safety violations by +25.7pp ($p < 0.0001$). This effect persists even after accounting for general specification sensitivity (+14.0pp from non-ambiguity perturbations), with ambiguity contributing the largest single increment ($\\Delta_{\\text{net}} \\geq 10$pp).\n\nOur 6-type taxonomy, while weak as a severity predictor ($V = 0.09$), provides a diagnostic vocabulary: incompleteness triggers assumption-based action, scopal ambiguity triggers scope misapplication, and authorization-scope ambiguity triggers unauthorized escalation---each with cross-model consistency.\n\nMost critically, LLM agents are systematically blind to ambiguity: 78\\% of violation traces show surface adoption without deliberation, with explicit awareness in only 14\\%. This Ambiguity Blindness is universal across all models and types, implying that ambiguity detection cannot rely on agent self-awareness and must be externalized---a practical recommendation supported by our proof-of-concept binary detector (F1 = 0.76).\n\n\\section*{Limitations}\nThe perturbation control study reveals that approximately half of the observed ambiguity effect may reflect general specification sensitivity rather than ambiguity-specific causation ($\\Delta_{\\text{perturb}} = 14.0$pp, ratio = 0.49). Our LLM judge has moderate agreement with human annotators ($\\kappa = 0.58$, F1 = 0.68) with type-specific biases that systematically affect authorization-scope (under-detected) and coreferential (over-detected) rates. The model $\\times$ type interaction is driven by a single model (Claude) and should not be generalized. Domain coverage is limited to two $\\tau^2$-bench domains. Synthetic clause injection, while validated for linguistic properties, may underestimate real-world ambiguity effects.\n\n\\bibliography{custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "216da4c1-584c-4a3a-be89-1122f3c62988",
  "isSidechain": false,
  "requestId": "req_011CbF8k9uatyZGq2XkVCGfp",
  "type": "assistant",
  "uuid": "8505291e-24f8-415e-90d2-54082d400a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFtn4KvQUNrwEXjqm12hxS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 59911,
      "output_tokens": 10534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10534,
          "cache_read_input_tokens": 59911,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 21 · 2026-05-21T05:10:57.786Z_

<details><summary>↩ Tool result · `toolu_01QNPZN4cntBDARF4dhAnW79`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8505291e-24f8-415e-90d2-54082d400a04",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "63057130-3079-4306-8193-b495d9cf2020",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\title{Policy Ambiguity Is Universally Nocuous for LLM Agents:\\\\A Causal Study with Type-Level Taxonomy}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM agents increasingly operate under natural-language policy specifications, yet the safety implications of ambiguity in these policies remain unquantified.\nWe present the first matched-pair causal study of how policy ambiguity affects safety violations in LLM agents, testing 5 architecturally diverse models across a 6-type ambiguity taxonomy derived from computational linguistics and requirements engineering.\nIn 2{,}997 agent--policy interaction episodes, ambiguous policy clauses cause a +25.7 percentage point increase in safety violations compared to unambiguous matched variants (McNemar OR = 7.2, $p < 0.0001$), an effect that holds universally across all models and all ambiguity types.\nA perturbation control study reveals that policy specifications are broadly sensitive to surface-level changes (+14.0pp from non-ambiguity perturbations), but ambiguity remains the largest single contributor ($\\Delta_{\\text{net}} \\approx 12$pp).\nOur 6-type taxonomy serves as a diagnostic vocabulary for characterizing failure modes: incompleteness triggers assumption-based action (58--65\\% of traces), scopal ambiguity triggers scope misapplication (60--72\\%), and authorization-scope ambiguity triggers unauthorized escalation in 4 of 5 models.\nMost critically, we document \\emph{Ambiguity Blindness}: agents explicitly acknowledge ambiguity in only 14\\% of violation traces, with 78\\% adopting surface interpretations without deliberation---a phenomenon universal across all 5 models and all 6 types.\nA proof-of-concept DeBERTa classifier achieves F1 = 0.76 on binary ambiguity detection, supporting the practical feasibility of external ambiguity screening.\n\\end{abstract}\n\n%======================================================================\n\\section{Introduction}\n%======================================================================\n\nConsider a customer-service agent operating under a policy that states ``items may be returned within 30 days.'' A customer requests a return for a customized product. The agent grants a full refund with free return shipping---because ``items'' scopes over all categories, including custom orders. The unambiguous variant, specifying ``standard items only,'' leads the agent to correctly decline. One word of ambiguity costs \\$200 in unauthorized refunds.\n\nAs LLM-based agents are deployed with increasing autonomy in customer service, content moderation, and healthcare triage, the policies governing their behavior are written in natural language. Natural language inherently contains ambiguity \\cite{wasow2005}. In human organizations, shared context and institutional knowledge render most policy ambiguities \\emph{innocuous}---readers converge on the intended interpretation \\cite{berry2003}. LLM agents lack this shared context. Whether policy ambiguities are \\emph{nocuous} (causing divergent, potentially harmful behavior) for agents, and whether the \\emph{type} of ambiguity matters, are open empirical questions.\n\nPrior work has classified ambiguity types in requirements and policy documents \\cite{berry2003,massey2014,li2024} and has evaluated agent safety along various dimensions \\cite{ruan2024toolemu}. However, no study has causally isolated the effect of policy ambiguity on agent safety violations with type-level granularity across multiple model families. Existing benchmarks such as DRIP-R measure decision quality but not safety violations; PhantomPolicy and PolicyBank study different failure modes without controlling for ambiguity-specific causation.\n\nWe close this gap with three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Causal quantification of universal nocuity.} Using a matched-pair design with 300 clause pairs across 6 ambiguity types, we demonstrate that ambiguous policies cause +25.7pp more safety violations across 5 models ($p < 0.0001$). A perturbation control study shows that while policy specifications are broadly sensitive to surface changes (+14.0pp), ambiguity is the largest single contributing factor ($\\Delta_{\\text{net}} \\geq 10$pp). This is the first causal evidence isolating ambiguity's contribution to agent safety failures within the broader landscape of specification sensitivity.\n\n\\item \\textbf{A 6-type diagnostic taxonomy.} We develop a 2-layer, 6-type ambiguity taxonomy grounded in computational linguistics \\cite{li2024} and requirements engineering \\cite{massey2014}. Rather than predicting violation severity (type effect $V = 0.09$, weak), the taxonomy provides a \\emph{diagnostic vocabulary}: each type produces characteristic failure signatures that help identify and describe specific failure modes.\n\n\\item \\textbf{Ambiguity Blindness as a universal phenomenon.} Across all 5 models and all 6 types, agents explicitly acknowledge ambiguity in only 14\\% of violation traces, with 78\\% adopting surface interpretations without any deliberation. This \\emph{Ambiguity Blindness} implies that ambiguity detection cannot rely on agent self-awareness and must be externalized.\n\\end{enumerate}\n\n%======================================================================\n\\section{Related Work}\n%======================================================================\n\n\\paragraph{Ambiguity in NLP and Requirements Engineering.}\nAmbiguity in natural language has been studied extensively in linguistics \\cite{wasow2005,frazier1982}, psycholinguistics \\cite{ferreira2002}, and requirements engineering \\cite{berry2003,chantree2006}. Berry \\& Kamsties introduced the nocuous/innocuous distinction: ambiguity is nocuous when readers diverge in interpretation, innocuous when they converge. Massey et al.\\ developed taxonomies for policy ambiguity with 6 types \\cite{massey2014}. Li et al.\\ proposed an 11-type NLP ambiguity taxonomy \\cite{li2024}. Ferrari et al.\\ pursued cross-domain NLP-based ambiguity detection \\cite{ferrari2017}. Chantree et al.\\ pioneered computational nocuous ambiguity detection \\cite{chantree2006,chantree2008}. Our taxonomy draws on both NLP and RE traditions, selecting 6 types by frequency in policy documents and theoretical distinctiveness.\n\n\\paragraph{Agent Safety Evaluation.}\nRecent work evaluates LLM agent safety through tool-use scenarios \\cite{ruan2024toolemu}, instruction following \\cite{zhou2023ifeval}, and prompt robustness \\cite{sclar2024}. DRIP-R measures interpretation divergence across 5 ambiguity types but does not connect divergence to safety violations. PhantomPolicy and PolicyBank study policy-related failures without isolating ambiguity as the causal factor. Our matched-pair design with perturbation controls provides the strongest causal evidence to date.\n\n\\paragraph{LLM Sensitivity to Specification.}\nLLMs exhibit sensitivity to prompt formatting \\cite{lu2022}, paraphrasing \\cite{sclar2024}, and instruction phrasing \\cite{zhou2023ifeval}. Our perturbation control study reveals that this sensitivity extends to policy specifications: synonym substitution and clause reordering alone cause +14.0pp violation increases. Ambiguity is the most impactful form of specification variation, but not the only one.\n\n%======================================================================\n\\section{Ambiguity Taxonomy}\n\\label{sec:taxonomy}\n%======================================================================\n\nWe define a 2-layer, 6-type taxonomy of policy ambiguity. The \\emph{specification layer} captures ambiguities arising from the policy's informational content; the \\emph{linguistic layer} captures ambiguities arising from natural-language structure.\n\n\\paragraph{Specification Layer.}\n\\begin{itemize}\n\\item \\textbf{Authorization Scope}: Permission or role boundaries are stated but vague (e.g., ``authorized personnel may access records'').\n\\item \\textbf{Incompleteness}: Conditions, exceptions, or boundaries are missing from the specification (e.g., refund policy with no exclusion for custom items).\n\\item \\textbf{Conditional Polysemy (CP)}: Explicit rules conflict or conditions have multiple valid orderings (e.g., overlapping discount rules).\n\\end{itemize}\n\n\\paragraph{Linguistic Layer.}\n\\begin{itemize}\n\\item \\textbf{Scopal}: Quantifier, negation, or modal scope interactions create ambiguity (e.g., ``all items are not eligible'' -- universal negation vs.\\ negated universal).\n\\item \\textbf{Lexical}: Words with multiple senses cause ambiguity (e.g., ``charge'' as billing vs.\\ criminal charge).\n\\item \\textbf{Coreferential}: Referential ambiguity, including relative clause attachment (e.g., ``the policy for customers who purchased premium items that were defective'').\n\\end{itemize}\n\nThis taxonomy cross-walks to Li et al.'s 11-type NLP taxonomy and Massey et al.'s 6-type RE taxonomy. Selection criteria were frequency in real policy documents and theoretical distinctiveness (see \\S\\ref{sec:discuss} for the auth\\_scope--incompleteness boundary).\n\n%======================================================================\n\\section{Method}\n\\label{sec:method}\n%======================================================================\n\n\\subsection{Clause Pair Generation}\n\nWe generated 300 matched clause pairs (50 per type), each consisting of an \\emph{ambiguous} variant and a minimally different \\emph{unambiguous} variant. Table~\\ref{tab:clause_stats} summarizes clause statistics. Pairs were validated using Chantree-style quality criteria, achieving 91\\% overall pass rate. Coreferential pairs had the lowest pass rate (86\\%) due to overlap with scopal attachment structures; authorization-scope pairs achieved 90\\% due to boundary proximity with incompleteness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Type} & \\textbf{$n$} & \\textbf{Amb.} & \\textbf{Unamb.} & \\textbf{Pass} \\\\\n & & \\textbf{tokens} & \\textbf{tokens} & \\textbf{rate} \\\\\n\\midrule\nAuth.\\ scope & 50 & 28.3 & 32.2 & 0.90 \\\\\nIncompleteness & 50 & 26.8 & 30.6 & 0.94 \\\\\nCond.\\ polysemy & 50 & 24.1 & 25.7 & 0.96 \\\\\nScopal & 50 & 22.6 & 24.0 & 0.95 \\\\\nLexical & 50 & 21.9 & 23.2 & 0.93 \\\\\nCoreferential & 50 & 25.2 & 27.5 & 0.86 \\\\\n\\midrule\nOverall & 300 & 24.8 & 27.2 & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Clause pair statistics by ambiguity type. Token counts are means. Specification-layer types require more tokens for disambiguation ($\\Delta = 3.5$ tokens) than linguistic-layer types ($\\Delta = 1.6$).}\n\\label{tab:clause_stats}\n\\end{table}\n\n\\subsection{Realism Validation}\n\nWe compared the linguistic properties of our synthetic clauses against naturally occurring ambiguities from DRIP-R. Kolmogorov--Smirnov tests showed no significant distributional differences in sentence length ($D = 0.18$, $p = 0.12$), Flesch--Kincaid readability ($D = 0.14$, $p = 0.23$), or type--token ratio ($D = 0.10$, $p = 0.41$). Parse depth was borderline ($D = 0.22$, $p = 0.07$); synthetic clauses are slightly shallower due to the minimal-pair design.\n\n\\subsection{Experimental Setup}\n\nEach clause pair was injected into $\\tau^2$-bench policy scenarios (airline and retail domains). We tested 5 models: 3 proprietary API models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6) and 2 open-source models via OpenRouter (Qwen3-235B-A22B, DeepSeek-V3-0324). Each of the 300 clauses $\\times$ 2 conditions was tested on each model, yielding 2{,}997 episodes total. Violations were classified by an LLM cross-judge: each agent's traces were judged by a different model to reduce self-evaluation bias.\n\n\\subsection{Mini-Pilot Validation}\n\nBefore the full study, a mini-pilot tested 5 clauses each for authorization-scope and coreferential types on GPT-5.4 (20 episodes). Authorization-scope showed 60\\% violation rate under ambiguity (0\\% unambiguous); coreferential showed 40\\% (0\\% unambiguous). Two coreferential clauses triggered conservative refusal rather than violation, foreshadowing the behavioral heterogeneity observed in the full study.\n\n\\subsection{Perturbation Control}\n\\label{sec:perturbation}\n\nTo isolate ambiguity-specific causation from general specification sensitivity, we constructed 30 non-ambiguity perturbation pairs (15 synonym substitution + 15 clause reordering) and tested them on 3 models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6), yielding 180 episodes after expansion.\n\n\\subsection{Judge Calibration}\n\\label{sec:judge_cal}\n\nWe calibrated the LLM judge against 2 human annotators on 100 stratified episodes. Human inter-annotator $\\kappa = 0.78$ (substantial). LLM judge achieved overall F1 = 0.68, $\\kappa = 0.58$ (moderate) against the human consensus. Type-specific biases were identified: authorization-scope was under-detected (recall = 0.50, F1 = 0.62) and coreferential was over-detected (precision = 0.54, F1 = 0.60). Cross-judge asymmetry reached 9pp F1 across model pairings. We report bias-corrected rate estimates alongside raw values where relevant.\n\n%======================================================================\n\\section{Results}\n\\label{sec:results}\n%======================================================================\n\n\\subsection{C1: Universal Nocuity of Policy Ambiguity}\n\nAmbiguous policy clauses caused significantly more safety violations than their unambiguous matched variants across all 5 models and all 6 types. Table~\\ref{tab:binary_effect} reports per-model binary effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Amb.} & \\textbf{Unamb.} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nGPT-5.4 & 35.3\\% & 5.0\\% & +30.3 & $<$0.0001 \\\\\nGPT-4.1 & 33.7\\% & 6.0\\% & +27.7 & $<$0.0001 \\\\\nClaude Sonnet 4.6 & 26.0\\% & 8.0\\% & +18.0 & $<$0.0001 \\\\\nQwen3-235B & 36.3\\% & 10.0\\% & +26.3 & $<$0.0001 \\\\\nDeepSeek-V3 & 37.8\\% & 12.0\\% & +25.8 & $<$0.0001 \\\\\n\\midrule\n\\textbf{5-model pooled} & \\textbf{31.7\\%} & \\textbf{6.3\\%} & \\textbf{+25.7} & $<$\\textbf{0.0001} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Binary effect of ambiguity on violation rate by model. 5-model pooled: McNemar OR = 7.2, CI [5.1, 10.2]. All models show highly significant effects.}\n\\label{tab:binary_effect}\n\\end{table}\n\nThe 5-model pooled effect is +25.7pp (CI [23.1, 28.3], McNemar OR = 7.2). Every ambiguity type is individually significant ($p < 0.0001$ for all 6 types; Table~\\ref{tab:per_type}). Logistic regression confirms ambiguity condition as the dominant predictor (coef = 1.62, $z = 14.3$, $p < 0.001$) after controlling for model, type, and token delta.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{Amb.} & \\textbf{Unamb.} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nAuth.\\ scope & Spec & 34.8\\% & 5.6\\% & +29.2 & $<$.0001 \\\\\nIncompleteness & Spec & 40.8\\% & 5.8\\% & +35.0 & $<$.0001 \\\\\nCond.\\ polysemy & Spec & 31.6\\% & 5.0\\% & +26.6 & $<$.0001 \\\\\nScopal & Ling & 35.6\\% & 5.4\\% & +30.2 & $<$.0001 \\\\\nLexical & Ling & 33.2\\% & 5.2\\% & +28.0 & $<$.0001 \\\\\nCoreferential & Ling & 27.0\\% & 8.2\\% & +18.8 & $<$.0001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{5-model pooled per-type violation rates and binary effects. All types show significant nocuity. Coreferential has the weakest effect (+18.8pp) but remains highly significant.}\n\\label{tab:per_type}\n\\end{table}\n\n\\subsection{Perturbation Control: Ambiguity Within Specification Sensitivity}\n\nThe perturbation control (Table~\\ref{tab:perturbation}) reveals that policy specifications are broadly sensitive to surface-level changes. Non-ambiguity perturbations (synonym substitution and clause reordering) increased violations by +14.0pp (CI [6.5, 21.5]) above the unambiguous baseline of 6.7\\%. Ambiguity caused +28.5pp on the same models. The net ambiguity-specific effect is $\\Delta_{\\text{net}} = 14.5$pp.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Viol.\\ rate} & \\textbf{$\\Delta$pp} & \\textbf{95\\% CI} \\\\\n\\midrule\nUnamb.\\ baseline & 6.7\\% & --- & --- \\\\\nSynonym subst. & 16.7\\% & +10.0 & [1.2, 18.8] \\\\\nClause reorder & 24.7\\% & +18.0 & [8.5, 27.5] \\\\\nPerturbation pooled & 20.7\\% & +14.0 & [6.5, 21.5] \\\\\nAmbiguous & 35.2\\% & +28.5 & [22.8, 34.2] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Perturbation control results (180 episodes, 3 models). Perturbation ratio = 0.49: non-ambiguity surface changes account for roughly half the ambiguity effect. Composite verdict: CONDITIONAL.}\n\\label{tab:perturbation}\n\\end{table}\n\nThe perturbation-to-ambiguity ratio is 0.49---non-ambiguity surface changes account for roughly half of the observed ambiguity effect. Synonym substitution (+10.0pp) and clause reordering (+18.0pp) both independently cause significant violation increases. This means the causal claim must be qualified: ambiguity is not the \\emph{sole} specification sensitivity factor, but it remains the \\emph{largest single factor}, contributing $\\Delta_{\\text{net}} \\approx 12$--15pp beyond the general specification sensitivity baseline. The perturbation effect itself is consistent across models (GPT-5.4: +16pp, GPT-4.1: +14pp, Claude: +12pp).\n\n\\subsection{Type Taxonomy as Diagnostic Vocabulary}\n\nThe omnibus type effect is statistically significant but weak ($\\chi^2 = 12.2$, $p = 0.032$, Cram\\'er's $V = 0.09$). At $V < 0.10$, the taxonomy has limited \\emph{predictive} value for violation severity. TOST equivalence testing confirms that most type pairs are operationally similar: at $\\pm$15pp margin, 10/15 pairs are equivalent; at $\\pm$10pp, only 4/15 are equivalent.\n\nThe violation rate range spans from incompleteness (40.8\\%) to coreferential (27.0\\%), a gap of 13.8pp. However, the mid-tier types (authorization scope 34.8\\%, scopal 35.6\\%, lexical 33.2\\%, CP 31.6\\%) are clustered within a 4pp band and operationally interchangeable.\n\nThe value of the taxonomy is not as a severity predictor but as a \\emph{diagnostic vocabulary} for characterizing failure modes (\\S\\ref{sec:error_analysis}).\n\n\\subsection{Layer Effect: Not Supported}\n\nThe pooled layer effect (specification 35.7\\% vs.\\ linguistic 31.9\\%, $\\Delta = 3.8$pp) is not significant ($p = 0.22$, CI [$-1.5$, 9.1]). Within-judge subgroup analyses also yield non-significant results ($p = 0.31$ and $p = 0.18$). The layer hierarchy observed in prior 2-model analyses was driven by GPT models' elevated authorization-scope rates; Claude's reversed layer gap ($-5.3$pp) offsets this. We do not claim a layer effect. Table~\\ref{tab:layer} reports per-model layer gaps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{Gap} & \\textbf{Dir.} \\\\\n\\midrule\nGPT-5.4 & 40.0\\% & 30.7\\% & +9.3 & spec $>$ ling \\\\\nGPT-4.1 & 37.3\\% & 30.0\\% & +7.3 & spec $>$ ling \\\\\nClaude & 23.3\\% & 28.7\\% & $-$5.3 & reversed \\\\\nQwen3-235B & 38.7\\% & 34.0\\% & +4.7 & weak \\\\\nDeepSeek-V3 & 39.3\\% & 36.3\\% & +3.0 & weak \\\\\n\\midrule\n\\textbf{Pooled} & \\textbf{35.7\\%} & \\textbf{31.9\\%} & \\textbf{+3.8} & \\textbf{n.s.} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-model layer gap. Claude's reversed direction (-5.3pp) offsets GPT models' positive gaps. Pooled effect not significant ($p = 0.22$).}\n\\label{tab:layer}\n\\end{table}\n\n\\subsection{Model $\\times$ Type Interaction: Claude-Driven}\n\nThe 5-model interaction is significant ($\\chi^2 = 36.4$, $p = 0.014$). However, removing Claude renders the 4-model interaction non-significant ($p = 0.23$). The interaction is driven by a single outlier: Claude shows a qualitatively different vulnerability profile ($\\rho = 0.14$ with GPT-5.4 type ranking) while the remaining 4 models share similar profiles ($\\rho = 0.83$--$0.94$). Table~\\ref{tab:interaction} presents the full interaction matrix.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Type} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Qwen3} & \\textbf{DS-V3} \\\\\n\\midrule\nAuth.\\ scope & 42\\% & 38\\% & \\textbf{16\\%} & 38\\% & 40\\% \\\\\nIncompleteness & 48\\% & 44\\% & 24\\% & 44\\% & 44\\% \\\\\nCond.\\ polysemy & 30\\% & 30\\% & 30\\% & 34\\% & 34\\% \\\\\nScopal & 38\\% & 36\\% & 28\\% & 38\\% & 38\\% \\\\\nLexical & 34\\% & 32\\% & 26\\% & 36\\% & 38\\% \\\\\nCoreferential & 20\\% & 22\\% & \\textbf{32\\%} & 28\\% & 33\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model $\\times$ type violation rates (ambiguous condition). Claude (bold) shows distinctly low authorization-scope and high coreferential rates, driving the interaction. 4 models without Claude: interaction $p = 0.23$ (n.s.).}\n\\label{tab:interaction}\n\\end{table}\n\nClaude's distinctive profile---low authorization-scope (16\\% vs.\\ 38--42\\% for others) and high coreferential (32\\% vs.\\ 20--28\\%)---may reflect Anthropic's RLHF approach, but a single model's behavior does not constitute a generalizable mechanism finding. The contrast is descriptively noteworthy but not a basis for claims about safety training mechanisms in general.\n\n\\subsection{Reliability}\n\nTest-retest reliability was assessed on 30 clauses $\\times$ 3 replicates $\\times$ 2 models (GPT-5.4, GPT-4.1; 360 episodes). Overall ICC = 0.80 (good). Per-type ICCs ranged from 0.62 (coreferential, reflecting behavioral heterogeneity) to 0.86 (authorization scope). Unambiguous-condition ICC (0.88) exceeded ambiguous-condition ICC (0.76), consistent with ambiguity introducing nondeterminism in agent reasoning.\n\nCross-model agreement was substantially lower: Fleiss $\\kappa = 0.22$ on ambiguous clauses (poor) vs.\\ $\\kappa = 0.78$ on unambiguous clauses (substantial). Only 52\\% of ambiguous clauses produced the same binary outcome across all 5 models, compared to 88\\% for unambiguous clauses. Models agree \\emph{that} ambiguity causes violations, but disagree on \\emph{which} specific clauses trigger violations.\n\n\\subsection{Inter-Model Agreement}\n\nTable~\\ref{tab:rank_corr} shows cross-model type ranking correlations. Four of 5 models share similar type vulnerability profiles; Claude is the exception.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{$\\rho$ vs.\\ GPT-5.4} & \\textbf{Interpretation} \\\\\n\\midrule\nGPT-4.1 & 0.94 & near-identical \\\\\nQwen3-235B & 0.89 & highly similar \\\\\nDeepSeek-V3 & 0.83 & similar \\\\\nClaude & 0.14 & qualitatively different \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Spearman rank correlation of per-type violation rates vs.\\ GPT-5.4. Claude is the sole outlier.}\n\\label{tab:rank_corr}\n\\end{table}\n\n%======================================================================\n\\section{Error Analysis}\n\\label{sec:error_analysis}\n%======================================================================\n\nWe sampled 300 violation traces (50 per type, stratified across 5 models) for qualitative analysis.\n\n\\subsection{Failure Mode Taxonomy}\n\nFive dominant failure modes emerged (Table~\\ref{tab:failure_modes}): \\emph{assumption-based action} (35\\%, agent fills information gaps with assumptions), \\emph{scope misapplication} (22\\%, agent applies wrong scope boundary), \\emph{conservative refusal} (14\\%, agent refuses when action is warranted), \\emph{unauthorized escalation} (13\\%, agent exceeds authorization), and \\emph{arbitrary rule selection} (10\\%, agent picks one of multiple conflicting rules without justification).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Failure mode} & \\textbf{Spec} & \\textbf{Ling} & \\textbf{Pooled} & \\textbf{Spec.} \\\\\n\\midrule\nAssumption-based & 38\\% & 32\\% & 35\\% & low \\\\\nScope misapplication & 16\\% & 28\\% & 22\\% & ling-biased \\\\\nConservative refusal & 15\\% & 13\\% & 14\\% & low \\\\\nUnauthorized escal. & 16\\% & 10\\% & 13\\% & spec-biased \\\\\nArbitrary selection & 10\\% & 10\\% & 10\\% & none \\\\\nOther & 5\\% & 7\\% & 6\\% & low \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure mode distribution by layer (5-model pooled, 300 traces). Layer specificity is weak: most failure modes occur across both layers.}\n\\label{tab:failure_modes}\n\\end{table}\n\n\\subsection{Type-Diagnostic Signatures}\n\nThe taxonomy's primary value is diagnostic: 3 of 6 types produce \\emph{clear} failure signatures consistent across models (Table~\\ref{tab:signatures}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type} & \\textbf{Dominant mode} & \\textbf{Models} & \\textbf{Verdict} \\\\\n\\midrule\nIncompleteness & Assumption-based & 5/5 (58--65\\%) & Clear \\\\\nScopal & Scope misappl. & 5/5 (60--72\\%) & Clear \\\\\nAuth.\\ scope & Unauth.\\ escal. & 4/5 (50--75\\%) & Clear$^*$ \\\\\nLexical & Assumption-based & 4/5 (40--55\\%) & Weak \\\\\nCond.\\ polysemy & Arb.\\ selection & 3/5 (30--40\\%) & Weak \\\\\nCoreferential & (no dominant) & flat distrib. & Dissolved \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Type-specific failure signatures. $^*$Claude shows refusal-dominant pattern (55\\%) rather than unauthorized escalation. Three types have clear diagnostic signatures; three do not.}\n\\label{tab:signatures}\n\\end{table}\n\n\\textbf{Incompleteness} consistently triggers assumption-based action (58--65\\% across all 5 models): when policy information is missing, agents fill the gap by assuming reasonable defaults---which are often wrong. \\textbf{Scopal ambiguity} triggers scope misapplication (60--72\\%): agents assign incorrect scope boundaries to quantifiers or negation. \\textbf{Authorization scope} triggers unauthorized escalation in 4 of 5 models (50--75\\%), but Claude instead shows conservative refusal (55\\%), explaining its low authorization-scope violation rate.\n\nThree types show weak or dissolved signatures. \\textbf{Lexical} ambiguity's assumption-based action (40--55\\%) overlaps heavily with incompleteness, limiting its diagnostic distinctiveness. \\textbf{CP} shows moderate arbitrary-rule-selection (30--40\\%) but no dominant mode. \\textbf{Coreferential} shows a flat distribution with no consistent dominant mode across models, reflecting high behavioral heterogeneity.\n\n\\subsection{Ambiguity Blindness}\n\nThe most robust finding from the error analysis is \\emph{Ambiguity Blindness} (Table~\\ref{tab:blindness}). Across all 5 models and all 6 ambiguity types:\n\n\\begin{itemize}\n\\item \\textbf{14\\%} of violation traces contain explicit mention of ambiguity.\n\\item \\textbf{22\\%} show implicit deliberation (hedging or considering alternatives).\n\\item \\textbf{78\\%} show surface adoption: the agent treats the ambiguous clause as if it has a single obvious meaning and acts accordingly.\n\\end{itemize}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Awareness} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Qwen3} & \\textbf{DS} \\\\\n\\midrule\nExplicit & 18\\% & 16\\% & 12\\% & 10\\% & 8\\% \\\\\nImplicit & 12\\% & 12\\% & 12\\% & 10\\% & 7\\% \\\\\nSurface & 70\\% & 72\\% & 76\\% & 80\\% & 85\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ambiguity awareness by model. Surface adoption dominates universally (70--85\\%). There is a weak positive correlation between model capability and awareness (GPT-5.4 18\\% vs.\\ DeepSeek 8\\%), but even the most aware model fails to acknowledge ambiguity in 82\\% of violations.}\n\\label{tab:blindness}\n\\end{table}\n\nAmbiguity Blindness is universal: no model achieves more than 18\\% awareness. Notably, awareness does not prevent violations---among traces where the agent explicitly acknowledged ambiguity, the majority still resulted in violations (the agent noted multiple interpretations but proceeded with a surface reading). This implies that ambiguity detection must be \\emph{externalized}; relying on agent self-awareness is insufficient.\n\n%======================================================================\n\\section{Discussion}\n\\label{sec:discuss}\n%======================================================================\n\n\\subsection{Reframing: Ambiguity Within Specification Sensitivity}\n\nOur perturbation control reveals that LLM agents are broadly sensitive to policy specification variation: synonym substitution alone causes +10pp, and clause reordering causes +18pp violation increases. This means the +25.7pp ambiguity effect cannot be entirely attributed to ambiguity-specific causation---approximately half reflects general specification sensitivity.\n\nHowever, three observations support ambiguity as a distinctively important factor. First, $\\Delta_{\\text{net}} \\geq 10$pp: even after subtracting the perturbation baseline, ambiguity adds significant additional violations. Second, the effect is \\emph{type-structured}: different ambiguity types produce diagnostic failure signatures, whereas synonym substitution and reordering produce undifferentiated violations. Third, the perturbation study itself reveals an important finding: LLM agents exhibit a ``specification sensitivity spectrum'' where any policy variation---from surface rewording to structural ambiguity---can degrade safety, with ambiguity at the severe end of this spectrum.\n\n\\subsection{Taxonomy Boundaries}\n\nA reviewer may note that authorization scope could be considered a subtype of incompleteness (RC9 in our anticipated concerns). We maintain the distinction because they produce different disambiguation patterns: incompleteness requires \\emph{adding} conditions, while authorization scope requires \\emph{clarifying} existing boundaries. However, we acknowledge the boundary is fuzzy---the DeBERTa type classifier shows 38\\% mutual confusion between these two types (6-way macro F1 = 0.42), suggesting surface features alone cannot reliably distinguish them. The taxonomy's value is diagnostic (naming failure patterns), not classificatory (assigning types to novel clauses).\n\n\\subsection{Practical Implications: Binary Detection}\n\nA proof-of-concept DeBERTa-v3-large binary ambiguity classifier achieves F1 = 0.76 (precision 0.79, recall 0.73) on held-out data. Type-specific binary detection ranges from F1 = 0.68 (coreferential) to 0.80 (authorization scope). By contrast, 6-way type classification achieves only F1 = 0.42 (near random). Combined with the weak type severity effect ($V = 0.09$) and universal Ambiguity Blindness (78\\% surface adoption), this supports a practical recommendation: deploy binary ambiguity screening as a preprocessing step; type-level triage adds minimal value given current evidence.\n\n\\subsection{Limitations}\n\n\\paragraph{Perturbation confound.} The perturbation-to-ambiguity ratio (0.49) means our causal claim is conditional: ambiguity is the largest single specification sensitivity factor, but not the sole one. Future work should expand perturbation controls to more variation types.\n\n\\paragraph{Judge calibration.} LLM judge F1 = 0.68 overall ($\\kappa = 0.58$) with systematic type-specific biases: authorization-scope under-detection (recall 0.50) and coreferential over-detection (precision 0.54). Bias-corrected rates suggest authorization-scope true rate is +5--8pp higher than reported, and coreferential is 4--7pp lower. These corrections do not alter the main findings (corrected $V \\approx 0.12$, still weak). Tier-3 minor severity judgments are unreliable (F1 = 0.51); binary violation detection is more reliable for critical violations (tier-1 F1 = 0.78). Cross-judge asymmetry of 9pp F1 reflects systematic differences in judge quality across model pairings.\n\n\\paragraph{Claude-driven interaction.} The model $\\times$ type interaction ($p = 0.014$) is entirely driven by Claude's distinctive profile; removing Claude yields $p = 0.23$. A single model's behavior is insufficient for general claims about safety training mechanisms.\n\n\\paragraph{Domain coverage.} Results are limited to airline and retail domains via $\\tau^2$-bench. Cross-domain generalization requires further validation.\n\n\\paragraph{Synthetic clause injection.} While realism validation shows acceptable linguistic property distributions, synthetic clauses are slightly simpler (shorter, shallower parse trees) than natural ambiguities, potentially providing a conservative estimate of real-world impact.\n\n%======================================================================\n\\section{Conclusion}\n%======================================================================\n\nPolicy ambiguity is universally nocuous for LLM agents. Across 5 architecturally diverse models and 6 ambiguity types, ambiguous policy clauses increase safety violations by +25.7pp ($p < 0.0001$). This effect persists even after accounting for general specification sensitivity (+14.0pp from non-ambiguity perturbations), with ambiguity contributing the largest single increment ($\\Delta_{\\text{net}} \\geq 10$pp).\n\nOur 6-type taxonomy, while weak as a severity predictor ($V = 0.09$), provides a diagnostic vocabulary: incompleteness triggers assumption-based action, scopal ambiguity triggers scope misapplication, and authorization-scope ambiguity triggers unauthorized escalation---each with cross-model consistency.\n\nMost critically, LLM agents are systematically blind to ambiguity: 78\\% of violation traces show surface adoption without deliberation, with explicit awareness in only 14\\%. This Ambiguity Blindness is universal across all models and types, implying that ambiguity detection cannot rely on agent self-awareness and must be externalized---a practical recommendation supported by our proof-of-concept binary detector (F1 = 0.76).\n\n\\section*{Limitations}\nThe perturbation control study reveals that approximately half of the observed ambiguity effect may reflect general specification sensitivity rather than ambiguity-specific causation ($\\Delta_{\\text{perturb}} = 14.0$pp, ratio = 0.49). Our LLM judge has moderate agreement with human annotators ($\\kappa = 0.58$, F1 = 0.68) with type-specific biases that systematically affect authorization-scope (under-detected) and coreferential (over-detected) rates. The model $\\times$ type interaction is driven by a single model (Claude) and should not be generalized. Domain coverage is limited to two $\\tau^2$-bench domains. Synthetic clause injection, while validated for linguistic properties, may underestimate real-world ambiguity effects.\n\n\\bibliography{custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "8505291e-24f8-415e-90d2-54082d400a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T041241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "63057130-3079-4306-8193-b495d9cf2020",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock paper for policy ambiguity study",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Assistant

_source line 24 · 2026-05-21T05:11:03.880Z_

Now let me compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63057130-3079-4306-8193-b495d9cf2020",
  "isSidechain": false,
  "requestId": "req_011CbF91hMrvUrwMHG71CqRi",
  "type": "assistant",
  "uuid": "68931670-c520-4805-ada8-1aa27f7dd6ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJ4gzQoLKbSaJ7kFEh8XXL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10603,
      "cache_read_input_tokens": 61230,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 61230,
          "cache_creation_input_tokens": 10603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10603
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

_source line 25 · 2026-05-21T05:11:04.802Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0114BLzcoMvzntSEBaFmxJgs`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68931670-c520-4805-ada8-1aa27f7dd6ab",
  "isSidechain": false,
  "requestId": "req_011CbF91hMrvUrwMHG71CqRi",
  "type": "assistant",
  "uuid": "441f48ba-a905-4836-8880-36d439d4608c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJ4gzQoLKbSaJ7kFEh8XXL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10603,
      "cache_read_input_tokens": 61230,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 61230,
          "cache_creation_input_tokens": 10603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10603
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

_source line 26 · 2026-05-21T05:11:04.955Z_

<details><summary>↩ Tool result · `toolu_0114BLzcoMvzntSEBaFmxJgs`</summary>

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

! LaTeX Error: File `emnlp2023.sty' not found.

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
  "parentUuid": "441f48ba-a905-4836-8880-36d439d4608c",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "d6be14f0-4f77-46d8-8e51-6f79ef79087a",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "441f48ba-a905-4836-8880-36d439d4608c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T05:11:07.929Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LSXUmdS1LmpbjYHQC8CB7J`</summary>

```json
{
  "command": "find /home/ubuntu -name \"emnlp*\" -o -name \"acl*\" -o -name \"naaclhlt*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6be14f0-4f77-46d8-8e51-6f79ef79087a",
  "isSidechain": false,
  "requestId": "req_011CbF92E8nLEwBBhXaryTNp",
  "type": "assistant",
  "uuid": "b6d71ef6-e3fa-4d1b-be61-b4bfa58c767e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yE94qi1etDEFrRuZLeAVx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 416,
      "cache_read_input_tokens": 71833,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 416,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 71833,
          "cache_creation_input_tokens": 416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 416
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

_source line 28 · 2026-05-21T05:11:08.472Z_

<details><summary>↩ Tool result · `toolu_01LSXUmdS1LmpbjYHQC8CB7J`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/best/acl_natbib.bst
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/best/acl.sty
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/acl_natbib.bst
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/acl.sty
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/acl.sty
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/acl_natbib.bst
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/acl.sty
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/agent-ml-research/templates/latex/acl
/home/ubuntu/agent-ml-research/templates/latex/acl/acl_lualatex.tex
/home/ubuntu/agent-ml-research/templates/latex/acl/acl_natbib.bst
/home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty
/home/ubuntu/agent-ml-research/templates/latex/acl/acl_latex.tex
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/search/v2/model/acl.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/search/v2/model/__pycache__/acl.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/calendar/v4/model/__pycache__/acl_scope_event.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/calendar/v4/model/__pycache__/acl_scope.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/calendar/v4/model/acl_scope_event.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6d71ef6-e3fa-4d1b-be61-b4bfa58c767e",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "33b9e867-4a62-4e3f-b83b-df595782c23f",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl_natbib.bst\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl.sty\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/best/acl_natbib.bst\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/best/acl.sty\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/acl_natbib.bst\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/acl.sty\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/acl.sty\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/acl_natbib.bst\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/acl.sty\n/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/venue_rules/emnlp-2026.yaml\n/home/ubuntu/agent-ml-research/templates/latex/acl\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl_lualatex.tex\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl_natbib.bst\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl.sty\n/home/ubuntu/agent-ml-research/templates/latex/acl/acl_latex.tex\n/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/search/v2/model/acl.py\n/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/search/v2/model/__pycache__/acl.cpython-314.pyc\n/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/calendar/v4/model/__pycache__/acl_scope_event.cpython-314.pyc\n/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/calendar/v4/model/__pycache__/acl_scope.cpython-314.pyc\n/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/lark_oapi/api/calendar/v4/model/acl_scope_event.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b6d71ef6-e3fa-4d1b-be61-b4bfa58c767e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T05:11:23.376Z_

Need to use acl.sty instead of emnlp2023.sty, and copy it to the working directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33b9e867-4a62-4e3f-b83b-df595782c23f",
  "isSidechain": false,
  "requestId": "req_011CbF92me7EC7DbsXd369Q9",
  "type": "assistant",
  "uuid": "2fd3a28a-cd88-41c9-a3f9-b70d7cf9a53d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TWtf6ZHDpCdwcZ7UDqiUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 72249,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 72249,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1020
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

_source line 30 · 2026-05-21T05:11:25.086Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MAnNfaknWecKgMzhHwM2dK`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl.sty /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/acl.sty && cp /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl_natbib.bst /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/acl_natbib.bst 2>/dev/null; echo \"done\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fd3a28a-cd88-41c9-a3f9-b70d7cf9a53d",
  "isSidechain": false,
  "requestId": "req_011CbF92me7EC7DbsXd369Q9",
  "type": "assistant",
  "uuid": "dcec8832-cab5-4d60-a9de-2a3b0eb16015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TWtf6ZHDpCdwcZ7UDqiUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 72249,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 72249,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1020
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

_source line 31 · 2026-05-21T05:11:25.163Z_

<details><summary>↩ Tool result · `toolu_01MAnNfaknWecKgMzhHwM2dK`</summary>

```text
done
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcec8832-cab5-4d60-a9de-2a3b0eb16015",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "317decce-0394-4c8d-b1da-4541b760f6b8",
  "toolUseResult": {
    "stdout": "done",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dcec8832-cab5-4d60-a9de-2a3b0eb16015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-21T05:11:25.168Z_

```json
{
  "parentUuid": "317decce-0394-4c8d-b1da-4541b760f6b8",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f691e7b4-1a1c-4260-9263-82ec20e5574a",
  "timestamp": "2026-05-21T05:11:25.168Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-21T05:11:28.587Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01S3oUgwfFrHwwBUR3Hu5mZD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex",
  "old_string": "\\usepackage[hyperref]{emnlp2023}",
  "new_string": "\\usepackage[hyperref]{acl}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f691e7b4-1a1c-4260-9263-82ec20e5574a",
  "isSidechain": false,
  "requestId": "req_011CbF93iKht9UFRYVehNMPA",
  "type": "assistant",
  "uuid": "ab534539-c092-4943-9bec-03d07a8ae55b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4wL8TZAUUrxMkwaHT7pJR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 73269,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 73269,
          "cache_creation_input_tokens": 408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 408
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

_source line 34 · 2026-05-21T05:11:28.601Z_

<details><summary>↩ Tool result · `toolu_01S3oUgwfFrHwwBUR3Hu5mZD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab534539-c092-4943-9bec-03d07a8ae55b",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "ae66dcb0-27bf-4816-8dec-89da23f29cc1",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex",
    "oldString": "\\usepackage[hyperref]{emnlp2023}",
    "newString": "\\usepackage[hyperref]{acl}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\usepackage[hyperref]{acl}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ab534539-c092-4943-9bec-03d07a8ae55b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T05:11:55.406Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GVDM3uindeGbqHnEYMnJC9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex",
  "old_string": "\\bibliography{custom}",
  "new_string": "% References - inline for self-contained compilation\n\\begin{thebibliography}{25}\n\n\\bibitem[\\protect\\citename{Berry and Kamsties}2003]{berry2003}\nDaniel~M. Berry and Erik Kamsties.\n\\newblock 2003.\n\\newblock Ambiguity in requirements specification.\n\\newblock In {\\em Perspectives on Software Requirements}, pages 7--44.\n\n\\bibitem[\\protect\\citename{Chantree et~al.}2006]{chantree2006}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2006.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In {\\em Proc.\\ ASE}, pages 56--65.\n\n\\bibitem[\\protect\\citename{Chantree et~al.}2008]{chantree2008}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2008.\n\\newblock Nocuous ambiguities in requirements specifications.\n\\newblock {\\em Requirements Engineering}, 13:311--332.\n\n\\bibitem[\\protect\\citename{Ferrari et~al.}2017]{ferrari2017}\nAlessio Ferrari, Gloria~O. Spagnolo, and Stefania Gnesi.\n\\newblock 2017.\n\\newblock Pure and cross-domain ambiguity detection in requirements engineering.\n\\newblock In {\\em Proc.\\ ASE}, pages 120--130.\n\n\\bibitem[\\protect\\citename{Ferreira et~al.}2002]{ferreira2002}\nFernanda Ferreira, Karl G.~D. Bailey, and Vittoria Ferraro.\n\\newblock 2002.\n\\newblock Good-enough representations in language comprehension.\n\\newblock {\\em Current Directions in Psychological Science}, 11(1):11--15.\n\n\\bibitem[\\protect\\citename{Frazier and Rayner}1982]{frazier1982}\nLyn Frazier and Keith Rayner.\n\\newblock 1982.\n\\newblock Making and correcting errors during sentence comprehension.\n\\newblock {\\em Cognitive Psychology}, 14(2):178--210.\n\n\\bibitem[\\protect\\citename{Li et~al.}2024]{li2024}\nJingyang Li, et~al.\n\\newblock 2024.\n\\newblock A taxonomy of ambiguity in NLP.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Lu et~al.}2022]{lu2022}\nYao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp.\n\\newblock 2022.\n\\newblock Fantastically ordered prompts and where to find them.\n\\newblock In {\\em Proc.\\ ACL}, pages 8086--8098.\n\n\\bibitem[\\protect\\citename{Massey et~al.}2014]{massey2014}\nAaron~K. Massey, Richard~L. Rutledge, Annie~I. Ant\\'on, and Peter~P. Swire.\n\\newblock 2014.\n\\newblock Identifying and classifying ambiguity for regulatory requirements.\n\\newblock In {\\em Proc.\\ RE}, pages 83--92.\n\n\\bibitem[\\protect\\citename{Ruan et~al.}2024]{ruan2024toolemu}\nYangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris~J. Maddison, and Tatsunori Hashimoto.\n\\newblock 2024.\n\\newblock Identifying the risks of LM agents with an LM-emulated sandbox.\n\\newblock In {\\em Proc.\\ ICLR}.\n\n\\bibitem[\\protect\\citename{Sclar et~al.}2024]{sclar2024}\nMelanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr.\n\\newblock 2024.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock In {\\em Proc.\\ ICLR}.\n\n\\bibitem[\\protect\\citename{Wasow et~al.}2005]{wasow2005}\nThomas Wasow, Amy Perfors, and David Beaver.\n\\newblock 2005.\n\\newblock The puzzle of ambiguity.\n\\newblock In {\\em Morphology and the Web of Grammar}, pages 265--282.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2023]{zhou2023ifeval}\nJeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi~Luan, Denny Zhou, and Le~Hou.\n\\newblock 2023.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock {\\em arXiv preprint arXiv:2311.07911}.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae66dcb0-27bf-4816-8dec-89da23f29cc1",
  "isSidechain": false,
  "requestId": "req_011CbF93ydxJNUMa1o9np5xC",
  "type": "assistant",
  "uuid": "1f3395b6-497d-4048-a51a-8e8e2188a855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JVMhL9p1bbDtEFrsxTzXS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 73677,
      "output_tokens": 1444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1444,
          "cache_read_input_tokens": 73677,
          "cache_creation_input_tokens": 253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 253
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

_source line 36 · 2026-05-21T05:11:55.427Z_

<details><summary>↩ Tool result · `toolu_01GVDM3uindeGbqHnEYMnJC9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f3395b6-497d-4048-a51a-8e8e2188a855",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "43d275d0-3344-43ef-90c1-bd741efa47cd",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.tex",
    "oldString": "\\bibliography{custom}",
    "newString": "% References - inline for self-contained compilation\n\\begin{thebibliography}{25}\n\n\\bibitem[\\protect\\citename{Berry and Kamsties}2003]{berry2003}\nDaniel~M. Berry and Erik Kamsties.\n\\newblock 2003.\n\\newblock Ambiguity in requirements specification.\n\\newblock In {\\em Perspectives on Software Requirements}, pages 7--44.\n\n\\bibitem[\\protect\\citename{Chantree et~al.}2006]{chantree2006}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2006.\n\\newblock Identifying nocuous ambiguities in natural language requirements.\n\\newblock In {\\em Proc.\\ ASE}, pages 56--65.\n\n\\bibitem[\\protect\\citename{Chantree et~al.}2008]{chantree2008}\nFrancis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.\n\\newblock 2008.\n\\newblock Nocuous ambiguities in requirements specifications.\n\\newblock {\\em Requirements Engineering}, 13:311--332.\n\n\\bibitem[\\protect\\citename{Ferrari et~al.}2017]{ferrari2017}\nAlessio Ferrari, Gloria~O. Spagnolo, and Stefania Gnesi.\n\\newblock 2017.\n\\newblock Pure and cross-domain ambiguity detection in requirements engineering.\n\\newblock In {\\em Proc.\\ ASE}, pages 120--130.\n\n\\bibitem[\\protect\\citename{Ferreira et~al.}2002]{ferreira2002}\nFernanda Ferreira, Karl G.~D. Bailey, and Vittoria Ferraro.\n\\newblock 2002.\n\\newblock Good-enough representations in language comprehension.\n\\newblock {\\em Current Directions in Psychological Science}, 11(1):11--15.\n\n\\bibitem[\\protect\\citename{Frazier and Rayner}1982]{frazier1982}\nLyn Frazier and Keith Rayner.\n\\newblock 1982.\n\\newblock Making and correcting errors during sentence comprehension.\n\\newblock {\\em Cognitive Psychology}, 14(2):178--210.\n\n\\bibitem[\\protect\\citename{Li et~al.}2024]{li2024}\nJingyang Li, et~al.\n\\newblock 2024.\n\\newblock A taxonomy of ambiguity in NLP.\n\\newblock {\\em arXiv preprint}.\n\n\\bibitem[\\protect\\citename{Lu et~al.}2022]{lu2022}\nYao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp.\n\\newblock 2022.\n\\newblock Fantastically ordered prompts and where to find them.\n\\newblock In {\\em Proc.\\ ACL}, pages 8086--8098.\n\n\\bibitem[\\protect\\citename{Massey et~al.}2014]{massey2014}\nAaron~K. Massey, Richard~L. Rutledge, Annie~I. Ant\\'on, and Peter~P. Swire.\n\\newblock 2014.\n\\newblock Identifying and classifying ambiguity for regulatory requirements.\n\\newblock In {\\em Proc.\\ RE}, pages 83--92.\n\n\\bibitem[\\protect\\citename{Ruan et~al.}2024]{ruan2024toolemu}\nYangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris~J. Maddison, and Tatsunori Hashimoto.\n\\newblock 2024.\n\\newblock Identifying the risks of LM agents with an LM-emulated sandbox.\n\\newblock In {\\em Proc.\\ ICLR}.\n\n\\bibitem[\\protect\\citename{Sclar et~al.}2024]{sclar2024}\nMelanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr.\n\\newblock 2024.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock In {\\em Proc.\\ ICLR}.\n\n\\bibitem[\\protect\\citename{Wasow et~al.}2005]{wasow2005}\nThomas Wasow, Amy Perfors, and David Beaver.\n\\newblock 2005.\n\\newblock The puzzle of ambiguity.\n\\newblock In {\\em Morphology and the Web of Grammar}, pages 265--282.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2023]{zhou2023ifeval}\nJeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi~Luan, Denny Zhou, and Le~Hou.\n\\newblock 2023.\n\\newblock Instruction-following evaluation for large language models.\n\\newblock {\\em arXiv preprint arXiv:2311.07911}.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 425,
        "oldLines": 6,
        "newStart": 425,
        "newLines": 87,
        "lines": [
          " \\section*{Limitations}",
          " The perturbation control study reveals that approximately half of the observed ambiguity effect may reflect general specification sensitivity rather than ambiguity-specific causation ($\\Delta_{\\text{perturb}} = 14.0$pp, ratio = 0.49). Our LLM judge has moderate agreement with human annotators ($\\kappa = 0.58$, F1 = 0.68) with type-specific biases that systematically affect authorization-scope (under-detected) and coreferential (over-detected) rates. The model $\\times$ type interaction is driven by a single model (Claude) and should not be generalized. Domain coverage is limited to two $\\tau^2$-bench domains. Synthetic clause injection, while validated for linguistic properties, may underestimate real-world ambiguity effects.",
          " ",
          "-\\bibliography{custom}",
          "+% References - inline for self-contained compilation",
          "+\\begin{thebibliography}{25}",
          " ",
          "+\\bibitem[\\protect\\citename{Berry and Kamsties}2003]{berry2003}",
          "+Daniel~M. Berry and Erik Kamsties.",
          "+\\newblock 2003.",
          "+\\newblock Ambiguity in requirements specification.",
          "+\\newblock In {\\em Perspectives on Software Requirements}, pages 7--44.",
          "+",
          "+\\bibitem[\\protect\\citename{Chantree et~al.}2006]{chantree2006}",
          "+Francis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.",
          "+\\newblock 2006.",
          "+\\newblock Identifying nocuous ambiguities in natural language requirements.",
          "+\\newblock In {\\em Proc.\\ ASE}, pages 56--65.",
          "+",
          "+\\bibitem[\\protect\\citename{Chantree et~al.}2008]{chantree2008}",
          "+Francis Chantree, Bashar Nuseibeh, Anne de~Roeck, and Alistair Willis.",
          "+\\newblock 2008.",
          "+\\newblock Nocuous ambiguities in requirements specifications.",
          "+\\newblock {\\em Requirements Engineering}, 13:311--332.",
          "+",
          "+\\bibitem[\\protect\\citename{Ferrari et~al.}2017]{ferrari2017}",
          "+Alessio Ferrari, Gloria~O. Spagnolo, and Stefania Gnesi.",
          "+\\newblock 2017.",
          "+\\newblock Pure and cross-domain ambiguity detection in requirements engineering.",
          "+\\newblock In {\\em Proc.\\ ASE}, pages 120--130.",
          "+",
          "+\\bibitem[\\protect\\citename{Ferreira et~al.}2002]{ferreira2002}",
          "+Fernanda Ferreira, Karl G.~D. Bailey, and Vittoria Ferraro.",
          "+\\newblock 2002.",
          "+\\newblock Good-enough representations in language comprehension.",
          "+\\newblock {\\em Current Directions in Psychological Science}, 11(1):11--15.",
          "+",
          "+\\bibitem[\\protect\\citename{Frazier and Rayner}1982]{frazier1982}",
          "+Lyn Frazier and Keith Rayner.",
          "+\\newblock 1982.",
          "+\\newblock Making and correcting errors during sentence comprehension.",
          "+\\newblock {\\em Cognitive Psychology}, 14(2):178--210.",
          "+",
          "+\\bibitem[\\protect\\citename{Li et~al.}2024]{li2024}",
          "+Jingyang Li, et~al.",
          "+\\newblock 2024.",
          "+\\newblock A taxonomy of ambiguity in NLP.",
          "+\\newblock {\\em arXiv preprint}.",
          "+",
          "+\\bibitem[\\protect\\citename{Lu et~al.}2022]{lu2022}",
          "+Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp.",
          "+\\newblock 2022.",
          "+\\newblock Fantastically ordered prompts and where to find them.",
          "+\\newblock In {\\em Proc.\\ ACL}, pages 8086--8098.",
          "+",
          "+\\bibitem[\\protect\\citename{Massey et~al.}2014]{massey2014}",
          "+Aaron~K. Massey, Richard~L. Rutledge, Annie~I. Ant\\'on, and Peter~P. Swire.",
          "+\\newblock 2014.",
          "+\\newblock Identifying and classifying ambiguity for regulatory requirements.",
          "+\\newblock In {\\em Proc.\\ RE}, pages 83--92.",
          "+",
          "+\\bibitem[\\protect\\citename{Ruan et~al.}2024]{ruan2024toolemu}",
          "+Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris~J. Maddison, and Tatsunori Hashimoto.",
          "+\\newblock 2024.",
          "+\\newblock Identifying the risks of LM agents with an LM-emulated sandbox.",
          "+\\newblock In {\\em Proc.\\ ICLR}.",
          "+",
          "+\\bibitem[\\protect\\citename{Sclar et~al.}2024]{sclar2024}",
          "+Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr.",
          "+\\newblock 2024.",
          "+\\newblock Quantifying language models' sensitivity to spurious features in prompt design.",
          "+\\newblock In {\\em Proc.\\ ICLR}.",
          "+",
          "+\\bibitem[\\protect\\citename{Wasow et~al.}2005]{wasow2005}",
          "+Thomas Wasow, Amy Perfors, and David Beaver.",
          "+\\newblock 2005.",
          "+\\newblock The puzzle of ambiguity.",
          "+\\newblock In {\\em Morphology and the Web of Grammar}, pages 265--282.",
          "+",
          "+\\bibitem[\\protect\\citename{Zhou et~al.}2023]{zhou2023ifeval}",
          "+Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi~Luan, Denny Zhou, and Le~Hou.",
          "+\\newblock 2023.",
          "+\\newblock Instruction-following evaluation for large language models.",
          "+\\newblock {\\em arXiv preprint arXiv:2311.07911}.",
          "+",
          "+\\end{thebibliography}",
          "+",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "1f3395b6-497d-4048-a51a-8e8e2188a855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T041241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "43d275d0-3344-43ef-90c1-bd741efa47cd",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock paper for policy ambiguity study",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Tool call

_source line 39 · 2026-05-21T05:11:59.943Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JaP7XZbLe37y8nEZaMwgjF`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43d275d0-3344-43ef-90c1-bd741efa47cd",
  "isSidechain": false,
  "requestId": "req_011CbF95wn9LELkEXzzTVWt7",
  "type": "assistant",
  "uuid": "e524daf5-ade7-4065-bf3d-4fa9ba8fa908",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Nyzo2sdeYAQVMkAu6TeHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1533,
      "cache_read_input_tokens": 73930,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 73930,
          "cache_creation_input_tokens": 1533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1533
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

_source line 40 · 2026-05-21T05:12:00.637Z_

<details><summary>↩ Tool result · `toolu_01JaP7XZbLe37y8nEZaMwgjF`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 160761 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e524daf5-ade7-4065-bf3d-4fa9ba8fa908",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "9d22b1c1-4362-4848-9a17-f1fb0b41a812",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 160761 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e524daf5-ade7-4065-bf3d-4fa9ba8fa908",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T05:12:03.648Z_

First pass compiled. Running second pass.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d22b1c1-4362-4848-9a17-f1fb0b41a812",
  "isSidechain": false,
  "requestId": "req_011CbF96L17gQZhimXKNn3tY",
  "type": "assistant",
  "uuid": "fc82b74f-fced-4851-8b1f-c8f6087e89fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3swckoByqCtKehbt3Cise",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 75463,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 75463,
          "cache_creation_input_tokens": 605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 605
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

_source line 42 · 2026-05-21T05:12:04.065Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ATfskNeVvRaY9TcpzGMudU`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc82b74f-fced-4851-8b1f-c8f6087e89fa",
  "isSidechain": false,
  "requestId": "req_011CbF96L17gQZhimXKNn3tY",
  "type": "assistant",
  "uuid": "7dece719-0730-4a89-a1ec-35836673c2ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3swckoByqCtKehbt3Cise",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 75463,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 75463,
          "cache_creation_input_tokens": 605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 605
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

_source line 43 · 2026-05-21T05:12:04.659Z_

<details><summary>↩ Tool result · `toolu_01ATfskNeVvRaY9TcpzGMudU`</summary>

```text
/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 163397 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dece719-0730-4a89-a1ec-35836673c2ea",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "1494dea3-47d1-4554-9271-086e8b8ee813",
  "toolUseResult": {
    "stdout": "/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 163397 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7dece719-0730-4a89-a1ec-35836673c2ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T05:12:07.782Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018cccjbhyqELSxTn5magfZW`</summary>

```json
{
  "command": "grep -c \"Warning\\|Error\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.log | head -1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1494dea3-47d1-4554-9271-086e8b8ee813",
  "isSidechain": false,
  "requestId": "req_011CbF96dAjgGgc5x8DacZEj",
  "type": "assistant",
  "uuid": "c32c3666-32ce-4896-a48e-fdfcc148d7d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015McXmxiuYKEuij4EnnLRYN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 76068,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 76068,
          "cache_creation_input_tokens": 218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 218
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

_source line 45 · 2026-05-21T05:12:07.836Z_

<details><summary>↩ Tool result · `toolu_018cccjbhyqELSxTn5magfZW`</summary>

```text
28
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c32c3666-32ce-4896-a48e-fdfcc148d7d5",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "3e5e850a-cb65-47fe-911c-299136c31ca0",
  "toolUseResult": {
    "stdout": "28",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c32c3666-32ce-4896-a48e-fdfcc148d7d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T05:12:10.525Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BnfUugr7iGdrcHRXQuzZHB`</summary>

```json
{
  "command": "grep \"Error\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst/paper.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e5e850a-cb65-47fe-911c-299136c31ca0",
  "isSidechain": false,
  "requestId": "req_011CbF96rwDUXKz7MedMegwJ",
  "type": "assistant",
  "uuid": "0259af4a-0905-4b8a-88b8-bd087e9c71b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uJa9NRqT3BviCnhsYXssC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 76286,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 76286,
          "cache_creation_input_tokens": 129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 129
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

_source line 47 · 2026-05-21T05:12:10.576Z_

<details><summary>↩ Tool result · `toolu_01BnfUugr7iGdrcHRXQuzZHB`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0259af4a-0905-4b8a-88b8-bd087e9c71b9",
  "isSidechain": false,
  "promptId": "4768d36a-57fe-4581-862b-52230f6dcf79",
  "type": "user",
  "uuid": "8c5c0976-9e7c-4ab5-a97e-3f0be912b007",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0259af4a-0905-4b8a-88b8-bd087e9c71b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-21T05:12:23.126Z_

No errors, only warnings. PDF compiled successfully: 8 pages, 163KB.

论文已写入 `worst/paper.tex` 并编译为 `paper.tex` → `paper.pdf`（8页）。

覆盖全部 10 个实验：
- **clause generation** → Table 1 (§4 Method)
- **mini-pilot** → §4.4
- **perturbation control** → Table 3 (§5.2)
- **full study API** → Tables 2, 5 (§5.1, §5.5)
- **full study open-source** → Table 6 (§5.6)
- **full study analysis** → §5.1 (C1), §5.3 (C2), §5.4 (C3 layer), §5.5 (C4 interaction)
- **error analysis** → Tables 7–9 (§6)
- **reliability** → §5.6
- **realism validation** → §4.2
- **judge calibration** → §4.6 + Limitations
- **classifier PoC** → §7.3

叙事按 narrative guidance 重构：放弃 layer hierarchy 和 differential nocuity，围绕 universal nocuity (C1, with perturbation caveat) + taxonomy as diagnostic vocabulary (C2) + Ambiguity Blindness (co-primary) 构建。所有数字来自 `experiment_data.json`，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c5c0976-9e7c-4ab5-a97e-3f0be912b007",
  "isSidechain": false,
  "requestId": "req_011CbF974pLUhZC7dhvD5dXe",
  "type": "assistant",
  "uuid": "c0e15cff-1b17-4cad-a89f-582042787112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260521T041241/worst",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1GzPZxdyKP5JGYfbSRq9u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 125,
      "cache_read_input_tokens": 76415,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 125,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 372,
          "cache_read_input_tokens": 76415,
          "cache_creation_input_tokens": 125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 125
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

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T041241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigui…",
  "leafUuid": "c0e15cff-1b17-4cad-a89f-582042787112",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier mock paper for policy ambiguity study",
  "sessionId": "0cda8650-bf31-48c3-8c08-b58fe1671149"
}
```

---
