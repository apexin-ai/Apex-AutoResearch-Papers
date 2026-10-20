# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/a5a00c36-2957-4507-acbb-5e7f39dd97f5.jsonl`
- **Structured JSON:** [`a541efdf62b3f20eb630.json`](../../sessions/a5/a541efdf62b3f20eb630.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T11:18:08.771Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T11:18:08.771Z",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：Claim 1 收窄 scope：从 \"practical detection framework\" 调整为 \"detection framework effective for large-scale benchmarks (n≥10K items) at moderate-to-high contamination\"。Minimal-information 的代价被量化而非回避——power theory（R²=0.96）精确预测 n_items 阈值，这本身是贡献。Claim 2 的 power function 分析升级为论文 core contribution——理论刻画 detection boundary 比宣称高 power 更有价值。Claim 3 的 leaderboard audit 定位为 large-scale anomaly profiling 而非 definitive detection，呈现 Δlz*-ranked 模型列表和 temporal trends 作为 converging evidence。补充 exp-domain-analysis 增加 case study 深度。需要增加 2-3 段 limitation discussion，明确 scope 边界。论文重心从 \"detection tool\" 偏移为 \"detection frontier characterization + scalable anomaly profiling\"。仍可冲 EMNLP main，但 contribution statement 更侧重方法论而非工具。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T11:18:08.776Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T11:18:08.776Z",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-20T11:18:08.808Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：Claim 1 收窄 scope：从 "practical detection framework" 调整为 "detection framework effective for large-scale benchmarks (n≥10K items) at moderate-to-high contamination"。Minimal-information 的代价被量化而非回避——power theory（R²=0.96）精确预测 n_items 阈值，这本身是贡献。Claim 2 的 power function 分析升级为论文 core contribution——理论刻画 detection boundary 比宣称高 power 更有价值。Claim 3 的 leaderboard audit 定位为 large-scale anomaly profiling 而非 definitive detection，呈现 Δlz*-ranked 模型列表和 temporal trends 作为 converging evidence。补充 exp-domain-analysis 增加 case study 深度。需要增加 2-3 段 limitation discussion，明确 scope 边界。论文重心从 "detection tool" 偏移为 "detection frontier characterization + scalable anomaly profiling"。仍可冲 EMNLP main，但 contribution statement 更侧重方法论而非工具。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b758e82e-2c50-4d43-a3b9-55f7d1d554ef",
  "type": "user",
  "uuid": "99a3e54e-f0d5-456d-bb16-843c5af9cff8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T11:18:08.807Z_

```json
{
  "parentUuid": "99a3e54e-f0d5-456d-bb16-843c5af9cff8",
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
  "uuid": "12e42508-65e7-4ec5-8dc4-293dd5c78aa2",
  "timestamp": "2026-05-20T11:18:08.807Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T11:18:08.807Z_

```json
{
  "parentUuid": "12e42508-65e7-4ec5-8dc4-293dd5c78aa2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8008253f-6da3-49d2-9a7e-240b172b1b34",
  "timestamp": "2026-05-20T11:18:08.807Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
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
  "aiTitle": "Generate simulated academic paper",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---

### Assistant

_source line 7 · 2026-05-20T11:18:13.962Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8008253f-6da3-49d2-9a7e-240b172b1b34",
  "isSidechain": false,
  "requestId": "req_011CbDjCnskrgo5PGukgA1Pf",
  "type": "assistant",
  "uuid": "aa8c05e2-d309-4c18-a93e-61bbd58a4d06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YDM1s8hf7ZL3CyQSNPN8dA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11852,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11852
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

_source line 8 · 2026-05-20T11:18:15.154Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SAeptZ6oHnBY7GSEKaFTES`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa8c05e2-d309-4c18-a93e-61bbd58a4d06",
  "isSidechain": false,
  "requestId": "req_011CbDjCnskrgo5PGukgA1Pf",
  "type": "assistant",
  "uuid": "2b4dc41c-a08c-4276-8d49-c9d7efa08743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YDM1s8hf7ZL3CyQSNPN8dA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11852,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11852
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

_source line 9 · 2026-05-20T11:18:15.443Z_

<details><summary>↩ Tool result · `toolu_01SAeptZ6oHnBY7GSEKaFTES`</summary>

```text
1	[
2	  {
3	    "name": "Controlled Contamination Pilot",
4	    "description": "Qwen3.5-9B × 3 levels (0%/15%/50%) × MMLU only. 测量 Δlz*(clean→contaminated) 是否显著。",
5	    "results": {
6	      "baseline_lz_star_mean": -18.5,
7	      "baseline_lz_star_std": 2.1,
8	      "baseline_accuracy": 0.62,
9	      "baseline_theta": 1.35,
10	      "contam_15pct_lz_star_mean": -20.8,
11	      "contam_15pct_delta_lz_star": -2.3,
12	      "contam_15pct_delta_lz_cohen_d": 0.85,
13	      "contam_15pct_accuracy": 0.68,
14	      "contam_15pct_theta": 1.52,
15	      "contam_15pct_p_value_paired_t": 0.018,
16	      "contam_15pct_significant_alpha005": true,
17	      "contam_50pct_lz_star_mean": -25.4,
18	      "contam_50pct_delta_lz_star": -6.9,
19	      "contam_50pct_delta_lz_cohen_d": 2.8,
20	      "contam_50pct_accuracy": 0.79,
21	      "contam_50pct_theta": 2.1,
22	      "contam_50pct_p_value_paired_t": 0.0001,
23	      "contam_50pct_significant_alpha005": true,
24	      "go_signal": true,
25	      "n_seeds": 3,
26	      "seed_variance_15pct_delta_lz": 0.9
27	    },
28	    "tables": [
29	      {
30	        "title": "Table: Pilot Results — Qwen3.5-9B × MMLU",
31	        "columns": [
32	          "Contamination %",
33	          "Accuracy",
34	          "θ",
35	          "lz*",
36	          "Δlz*",
37	          "Cohen's d",
38	          "p (paired-t)"
39	        ],
40	        "rows": [
41	          [
42	            "0% (baseline)",
43	            "0.62 ± 0.01",
44	            "1.35 ± 0.08",
45	            "-18.5 ± 2.1",
46	            "—",
47	            "—",
48	            "—"
49	          ],
50	          [
51	            "15%",
52	            "0.68 ± 0.02",
53	            "1.52 ± 0.11",
54	            "-20.8 ± 2.4",
55	            "-2.3 ± 0.9",
56	            "0.85",
57	            "0.018"
58	          ],
59	          [
60	            "50%",
61	            "0.79 ± 0.01",
62	            "2.10 ± 0.09",
63	            "-25.4 ± 2.6",
64	            "-6.9 ± 1.2",
65	            "2.80",
66	            "<0.001"
67	          ]
68	        ]
69	      }
70	    ],
71	    "figures": [],
72	    "analysis": "Pilot 确认 go signal：MMLU 上 Δlz* 在 15% 时统计显著（p=0.018），50% 时高度显著。 但 15% 的 effect size（d=0.85）低于 simulation 预测（simulation power 0.98 意味着 d>>2）， gap 来自 SFT 泛化效应。这是 median 档的核心特征——信号可检测但受限。 关键 implication：(1) 需要 ≥15% contamination 才有可靠信号，与 min_detectable_contam_mmlu_pct 范围 [15, 30] 一致；(2) 完整实验中 GSM8K（n=1319）和 HellaSwag（n=10042）可能更弱， 需要更高 contamination level 才能 detect。\n\n\n在 median 档，SFT 泛化会部分淹没信号但不会完全消除。MMLU 有 14K items，是 n_items 最大的 benchmark， power theory 预测其在 15% 时已超过 80% power（min_items_15pct_80power=7958）。 但 SFT 不只记忆 exact items——它从污染数据中学到的 domain knowledge 会泛化到 clean items， 使得能力 θ 提升幅度大于纯记忆预期，同时让 response pattern 比 simulation 中更 \"合理\"（因为泛化 改善的 items 仍符合 ability-based 预测）。因此 Δlz* 方向正确但 effect size 低于 simulation 预测。 15% 时 Cohen's d ≈ 0.85（在 [0.6, 1.5] 范围偏低端），因为约 40-50% 的 accuracy gain 来自泛化而非 直接记忆，泛化部分不产生 aberrant pattern。50% 时信号大幅增强（d≈2.8），因为被记忆的 items 占比够大， 即使有泛化效应也无法掩盖 aberrant response pattern。baseline lz* 已经很极端（≈-18.5）因为 universal model misfit，但 Δlz* 作为 within-model 差分仍然 interpretable（null 已验证 well-calibrated）。 seed 间方差中等（std≈0.9），反映 QLoRA 训练的随机性。总体结论：go signal positive，但需要完整实验 验证 GSM8K/HellaSwag 上信号是否也成立。\n"
73	  },
74	  {
75	    "name": "Full Controlled Contamination",
76	    "description": "4 模型 × 6 levels (0/5/10/15/25/50%) × 3 benchmarks (MMLU/GSM8K/HellaSwag). 建立 ground-truth contamination → Δlz* 映射。",
77	    "results": {
78	      "mmlu_delta_lz_cohen_d_5pct": 0.25,
79	      "mmlu_delta_lz_cohen_d_10pct": 0.52,
80	      "mmlu_delta_lz_cohen_d_15pct": 0.92,
81	      "mmlu_delta_lz_cohen_d_25pct": 1.85,
82	      "mmlu_delta_lz_cohen_d_50pct": 3.4,
83	      "mmlu_auroc_5pct": 0.58,
84	      "mmlu_auroc_10pct": 0.65,
85	      "mmlu_auroc_15pct": 0.78,
86	      "mmlu_auroc_25pct": 0.91,
87	      "mmlu_auroc_50pct": 0.95,
88	      "mmlu_detectable_at_alpha005": "≥15% (3/4 models), ≥10% (1/4 models)",
89	      "hellaswag_delta_lz_cohen_d_15pct": 0.45,
90	      "hellaswag_delta_lz_cohen_d_25pct": 0.88,
91	      "hellaswag_delta_lz_cohen_d_50pct": 1.95,
92	      "hellaswag_auroc_15pct": 0.62,
93	      "hellaswag_auroc_25pct": 0.76,
94	      "hellaswag_auroc_50pct": 0.88,
95	      "hellaswag_detectable_at_alpha005": "≥25% (3/4 models), ≥50% (1/4 models)",
96	      "gsm8k_delta_lz_cohen_d_15pct": 0.22,
97	      "gsm8k_delta_lz_cohen_d_25pct": 0.41,
98	      "gsm8k_delta_lz_cohen_d_50pct": 0.88,
99	      "gsm8k_auroc_15pct": 0.55,
100	      "gsm8k_auroc_25pct": 0.62,
101	      "gsm8k_auroc_50pct": 0.74,
102	      "gsm8k_detectable_at_alpha005": "≥50% (2/4 models only)",
103	      "cross_model_rank_correlation_delta_lz": 0.72,
104	      "cross_benchmark_detectable_frac_15pct": 0.33,
105	      "cross_benchmark_detectable_frac_25pct": 0.5,
106	      "cross_benchmark_detectable_frac_50pct": 0.75,
107	      "model_with_strongest_signal": "Mistral-7B-v0.3",
108	      "model_with_weakest_signal": "Gemma-4-31B",
109	      "inter_model_cohen_d_range_mmlu_15pct": [
110	        0.62,
111	        1.35
112	      ],
113	      "accuracy_gain_from_generalization_frac_15pct": 0.45,
114	      "accuracy_gain_from_generalization_frac_50pct": 0.28,
115	      "n_total_runs": 72
116	    },
117	    "tables": [
118	      {
119	        "title": "Table: AUROC by Benchmark × Contamination Level (4-model average ± std)",
120	        "columns": [
121	          "Benchmark (n_items)",
122	          "5%",
123	          "10%",
124	          "15%",
125	          "25%",
126	          "50%"
127	        ],
128	        "rows": [
129	          [
130	            "MMLU (14042)",
131	            "0.58±0.04",
132	            "0.65±0.05",
133	            "0.78±0.06",
134	            "0.91±0.03",
135	            "0.95±0.02"
136	          ],
137	          [
138	            "HellaSwag (10042)",
139	            "0.53±0.03",
140	            "0.57±0.04",
141	            "0.62±0.07",
142	            "0.76±0.05",
143	            "0.88±0.04"
144	          ],
145	          [
146	            "GSM8K (1319)",
147	            "0.51±0.02",
148	            "0.53±0.03",
149	            "0.55±0.04",
150	            "0.62±0.06",
151	            "0.74±0.05"
152	          ]
153	        ]
154	      },
155	      {
156	        "title": "Table: Cohen's d of Δlz* by Benchmark × Contamination Level (4-model average)",
157	        "columns": [
158	          "Benchmark",
159	          "5%",
160	          "10%",
161	          "15%",
162	          "25%",
163	          "50%"
164	        ],
165	        "rows": [
166	          [
167	            "MMLU",
168	            "0.25",
169	            "0.52",
170	            "0.92",
171	            "1.85",
172	            "3.40"
173	          ],
174	          [
175	            "HellaSwag",
176	            "0.12",
177	            "0.28",
178	            "0.45",
179	            "0.88",
180	            "1.95"
181	          ],
182	          [
183	            "GSM8K",
184	            "0.08",
185	            "0.15",
186	            "0.22",
187	            "0.41",
188	            "0.88"
189	          ]
190	        ]
191	      },
192	      {
193	        "title": "Table: Per-Model Cohen's d at 15% Contamination (MMLU)",
194	        "columns": [
195	          "Model",
196	          "Δlz*",
197	          "Cohen's d",
198	          "p-value",
199	          "Accuracy Δ"
200	        ],
201	        "rows": [
202	          [
203	            "Qwen3.5-9B",
204	            "-2.3",
205	            "0.85",
206	            "0.018",
207	            "+0.06"
208	          ],
209	          [
210	            "Mistral-7B-v0.3",
211	            "-3.5",
212	            "1.35",
213	            "0.003",
214	            "+0.09"
215	          ],
216	          [
217	            "Llama-3.1-8B",
218	            "-2.8",
219	            "1.02",
220	            "0.009",
221	            "+0.07"
222	          ],
223	          [
224	            "Gemma-4-31B",
225	            "-1.4",
226	            "0.62",
227	            "0.042",
228	            "+0.04"
229	          ]
230	        ]
231	      }
232	    ],
233	    "figures": [],
234	    "analysis": "完整实验确认 median 档预测：MMLU 是唯一在 15% contamination 时可靠检测的 benchmark（AUROC 0.78）， HellaSwag 在 25% 时才达到实用 power（0.76），GSM8K 即使 50% 也只有 0.74。 这与 power theory 的 √n 预测高度一致（R²=0.96）。关键发现：SFT 泛化效应解释了 simulation-to-controlled 的 power gap——simulation 假设污染 items 全部产生 aberrant pattern， 但 SFT 实际只有 55-72% 的 accuracy gain 来自直接记忆。模型间差异（Gemma d=0.62 vs Mistral d=1.35） 为 limitation 提供定量证据。论文中应呈现为：detection power = f(n_items, contam_level, model_generalization_capacity)， 其中前两个因素可预测，第三个引入不确定性。\n\n\nMedian 档的核心预测：检测力严格受 n_items 约束。MMLU（14K items）在 15% 时 AUROC≈0.78， 处于 [0.7, 0.9] 范围中间偏上。HellaSwag（10K items）刚好在 min_items_15pct_80power=7958  附近，但 SFT 泛化效应使得实际 power 低于 simulation 预测，15% 时 AUROC 仅 0.62—— 因为 HellaSwag 的 commonsense reasoning 特别容易从少量 training examples 泛化， 泛化学到的能力提升不产生 aberrant pattern。GSM8K（1319 items）n_items 远低于理论阈值， 即使 50% contamination 也只有 AUROC 0.74，符合 power theory 的 √n 衰减预测。\n模型间差异反映不同架构的 SFT 泛化能力：Mistral-7B 较小且 base model 能力较低， SFT 泛化有限，更多 accuracy gain 来自直接记忆→更强的 aberrant pattern→更高 Δlz*。 Gemma-4-31B 参数量大，泛化能力强，信号最弱。这个 inter-model 差异本身是有趣发现—— 说明 detection power 不仅取决于 n_items 和 contamination level，还取决于模型的 泛化能力，为 limitation discussion 提供素材。\ncross_benchmark_detectable_frac 在 15% 时仅 0.33（即 3 个 benchmark 中平均只有 1 个可检测）， 在 50% 时升至 0.75，与范围 [0.35, 0.7] 在中间档吻合。这支持 scope 收窄：实际可用的 detection 仅限于大 benchmark + 中高污染。\n"
235	  },
236	  {
237	    "name": "Leaderboard Audit",
238	    "description": "Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit，绘制 per-benchmark 污染率随时间趋势。",
239	    "results": {
240	      "n_models_attempted": 8500,
241	      "n_models_successfully_analyzed": 6200,
242	      "n_models_excluded_missing_data": 2300,
243	      "benchmarks_analyzed": [
244	        "MMLU",
245	        "HellaSwag",
246	        "ARC-Challenge",
247	        "GSM8K"
248	      ],
249	      "flagged_rate_absolute_threshold": 0.92,
250	      "flagged_rate_mmlu": 0.94,
251	      "flagged_rate_hellaswag": 0.91,
252	      "flagged_rate_arc_c": 0.89,
253	      "flagged_rate_gsm8k": 0.93,
254	      "delta_lz_star_computed": true,
255	      "delta_lz_reference": "per-family median lz* as baseline",
256	      "n_models_top_anomaly_mmlu": 185,
257	      "n_models_top_anomaly_cross_benchmark": 42,
258	      "top_anomaly_model_examples": [
259	        "Gemini-1.5-Pro",
260	        "suspected fine-tune variants"
261	      ],
262	      "temporal_trend_mmlu_flagged_rate_2023h1": 0.88,
263	      "temporal_trend_mmlu_flagged_rate_2023h2": 0.93,
264	      "temporal_trend_mmlu_flagged_rate_2024h1": 0.96,
265	      "contamination_increase_trend_significant": true,
266	      "contamination_trend_p_value": 0.008,
267	      "n_models_flagged_3plus_benchmarks": 380,
268	      "n_models_flagged_all_4_benchmarks": 95,
269	      "cross_benchmark_anomaly_spearman_rho": 0.18,
270	      "cross_benchmark_anomaly_spearman_p": 0.12
271	    },
272	    "tables": [
273	      {
274	        "title": "Table: Leaderboard Audit Summary",
275	        "columns": [
276	          "Benchmark",
277	          "n_models",
278	          "Flagged (absolute)",
279	          "Top Anomaly (Δlz*)",
280	          "Temporal trend β"
281	        ],
282	        "rows": [
283	          [
284	            "MMLU",
285	            "6200",
286	            "94.2%",
287	            "185 (3.0%)",
288	            "+0.031/quarter (p=0.008)"
289	          ],
290	          [
291	            "HellaSwag",
292	            "5800",
293	            "91.4%",
294	            "142 (2.4%)",
295	            "+0.022/quarter (p=0.035)"
296	          ],
297	          [
298	            "ARC-Challenge",
299	            "5500",
300	            "89.1%",
301	            "98 (1.8%)",
302	            "+0.018/quarter (p=0.091)"
303	          ],
304	          [
305	            "GSM8K",
306	            "4200",
307	            "93.0%",
308	            "67 (1.6%)",
309	            "+0.025/quarter (p=0.048)"
310	          ]
311	        ]
312	      },
313	      {
314	        "title": "Table: Top-10 Cross-Benchmark Anomaly Models (ranked by mean Δlz* z-score)",
315	        "columns": [
316	          "Model",
317	          "MMLU Δlz*-z",
318	          "HellaSwag Δlz*-z",
319	          "ARC Δlz*-z",
320	          "GSM8K Δlz*-z",
321	          "Mean z"
322	        ],
323	        "rows": [
324	          [
325	            "Gemini-1.5-Pro*",
326	            "4.82",
327	            "3.21",
328	            "2.95",
329	            "N/A",
330	            "3.66"
331	          ],
332	          [
333	            "[anonymized-finetune-1]",
334	            "3.95",
335	            "3.44",
336	            "2.10",
337	            "2.87",
338	            "3.09"
339	          ],
340	          [
341	            "[anonymized-finetune-2]",
342	            "3.72",
343	            "2.89",
344	            "3.15",
345	            "1.45",
346	            "2.80"
347	          ],
348	          [
349	            "... (7 more rows)",
350	            "",
351	            "",
352	            "",
353	            "",
354	            ""
355	          ]
356	        ]
357	      }
358	    ],
359	    "figures": [],
360	    "analysis": "Leaderboard audit 是 IRT-FIT 的 unique selling point（ConStat 需要 re-test，gray-box 需要 live model access，只有 IRT-FIT 能用 archival binary data 扫描 6000+ 模型）。但 median 档下 结果更适合定位为 anomaly profiling 而非 definitive detection：absolute threshold 产出 ~92% flagging rate（无实用区分力），Δlz*-based reranking 能缩小到 top 2-3% 但无 ground truth 验证。 cross-benchmark correlation 弱意味着不能简单说 \"model X is contaminated on all benchmarks\"， 只能说 \"model X shows anomalous Δlz* deviation on benchmark Y relative to its model family\"。 论文应呈现 Δlz*-ranked 列表 + temporal trends 作为 converging evidence， 并明确注明 \"anomaly ≠ confirmed contamination\"。\n\n\nMedian 档预测 leaderboard audit 可执行但 flagging pattern 偏向 universal。这与已有 Phase B  数据一致——57/60 cells flagged（95%）。当扩展到 6000+ 模型时，absolute lz* 阈值仍然会 flag  绝大多数模型（~92%），因为 universal model misfit 是 LLM response pattern 的固有特征， 不是 contamination 特异性的。\n因此需要 Δlz*-based reranking 而非 absolute threshold。以 per-family median lz* 为 baseline， 计算每个模型的 deviation。这能识别 ~185 个 MMLU top anomaly 模型（偏离 family median ≥2 SD）， 其中约 42 个在 3+ benchmarks 上同时 anomalous。但 cross-benchmark rank correlation 仍然弱 （Spearman ρ≈0.18, p=0.12），与 Phase B 发现一致——group-level 相关弱，anomaly 更多是 individual-level 现象。\n时间趋势分析能检测到 flagging rate 随时间增加（2023H1: 88% → 2024H1: 96%），统计显著， 但解释模糊——可能是 contamination 增加，也可能是模型越来越强导致 4PL misfit 加剧。 这正是 median 档的特征：leaderboard audit 产出 converging evidence 而非 definitive detection。 论文定位为 \"large-scale anomaly profiling\" 是正确的。\n实际可分析模型数（6200）低于原始可用数（13K+），因为部分模型的 per-item detail 文件不完整、 格式不一致、或 benchmark 覆盖不全。这是 data engineering 挑战而非方法论限制。\n"
361	  },
362	  {
363	    "name": "4PL vs 3PL Ablation",
364	    "description": "比较 4PL 和 3PL(d=1) 参数化下的检测灵敏度差异。",
365	    "results": {
366	      "power_diff_mmlu_15pct_4pl_vs_3pl": 0.035,
367	      "power_diff_hellaswag_15pct": 0.028,
368	      "power_diff_gsm8k_15pct": 0.012,
369	      "auroc_diff_mmlu_15pct": 0.02,
370	      "auroc_diff_mmlu_50pct": 0.01,
371	      "false_alarm_4pl_sim": 0.048,
372	      "false_alarm_3pl_sim": 0.055,
373	      "mean_abs_lz_star_diff_real_data": -1.8,
374	      "correlation_lz_star_4pl_vs_3pl": 0.985,
375	      "d_parameter_matters": "marginal",
376	      "recommended_parameterization": "4PL (default)"
377	    },
378	    "tables": [
379	      {
380	        "title": "Table: 4PL vs 3PL Detection Performance Comparison",
381	        "columns": [
382	          "Metric",
383	          "4PL",
384	          "3PL (d=1)",
385	          "Δ"
386	        ],
387	        "rows": [
388	          [
389	            "Sim. Power MMLU@15%",
390	            "0.978",
391	            "0.943",
392	            "+0.035"
393	          ],
394	          [
395	            "Sim. Power HellaSwag@15%",
396	            "0.753",
397	            "0.725",
398	            "+0.028"
399	          ],
400	          [
401	            "Sim. False Alarm Rate",
402	            "0.048",
403	            "0.055",
404	            "-0.007"
405	          ],
406	          [
407	            "Ctrl. AUROC MMLU@15%",
408	            "0.78",
409	            "0.76",
410	            "+0.02"
411	          ],
412	          [
413	            "lz* correlation (real data)",
414	            "—",
415	            "—",
416	            "r=0.985"
417	          ]
418	        ]
419	      }
420	    ],
421	    "figures": [],
422	    "analysis": "4PL vs 3PL 差异 marginal，足以作为 appendix 中的 ablation table 回应 reviewer， 但不值得在 main text 中大篇幅讨论。推荐保留 4PL 作为 default（一致性优势 + 微弱 power 优势）， 在 Section 5 (Experiments) 用一句话提及，详细结果放 Appendix。\n\n\n4PL 的 d 参数（upper asymptote < 1）建模 \"即使能力极高也可能答错\" 的现象。对 LLM 来说， 这对应 benchmark 中存在 ambiguous/mislabeled items 的情况。在 simulation 中，d 参数的影响 较小（power 差 ~3.5pp on MMLU），因为 simulation 中污染信号主要体现在 low-difficulty items  的 aberrant correct pattern 上，这些 items 的 d 参数接近 1。\n在 median 档下，4PL 略优于 3PL，但差异 marginal（AUROC 差 ~2pp）。原因：d 参数主要影响 high-difficulty items 的 lz* 计算——当 d<1 时，即使高能力者答对 hard items 也不会过度 贡献 lz*，减少 false alarm。但 LLM 的 universal misfit 已经使 absolute lz* 失效， Δlz* 作为差分进一步消除了 d 参数的 systematic 影响（两个条件下 d 相同，相减后抵消）。\n结论：4PL 作为 default 是合理的（略优且无额外成本），但不是论文的关键方法论贡献。 这个 ablation 的价值在于 preempt reviewer concern R8，不需要大段讨论。\n"
423	  },
424	  {
425	    "name": "Baseline Comparison",
426	    "description": "IRT-FIT vs ConStat + Min-K%++ 在控制实验 ground-truth 数据上的对比。",
427	    "results": {
428	      "irt_fit_auroc_mmlu_15pct": 0.78,
429	      "constat_auroc_mmlu_15pct": 0.93,
430	      "min_k_pp_auroc_mmlu_15pct": 0.96,
431	      "irt_fit_auroc_mmlu_50pct": 0.95,
432	      "constat_auroc_mmlu_50pct": 0.97,
433	      "min_k_pp_auroc_mmlu_50pct": 0.99,
434	      "irt_fit_auroc_gsm8k_50pct": 0.74,
435	      "constat_auroc_gsm8k_50pct": 0.88,
436	      "min_k_pp_auroc_gsm8k_50pct": 0.94,
437	      "auroc_gap_vs_best_mmlu_15pct": -0.18,
438	      "auroc_gap_vs_best_mmlu_50pct": -0.04,
439	      "auroc_gap_vs_best_avg": -0.16,
440	      "irt_fit_type1_error": 0.06,
441	      "constat_type1_error": 0.04,
442	      "min_k_pp_type1_error": 0.03,
443	      "irt_fit_info_level": "binary responses only",
444	      "constat_info_level": "binary + re-test (rephrased items)",
445	      "min_k_pp_info_level": "token-level log-probabilities",
446	      "irt_fit_models_analyzable": "6200+ (archival)",
447	      "constat_models_analyzable": "~50 (requires live re-evaluation)",
448	      "min_k_pp_models_analyzable": "~100 (requires logit access)"
449	    },
450	    "tables": [
451	      {
452	        "title": "Table: Detection Frontier — AUROC by Method × Information Level",
453	        "columns": [
454	          "Method",
455	          "Info Level",
456	          "MMLU@15%",
457	          "MMLU@50%",
458	          "HellaSwag@25%",
459	          "GSM8K@50%",
460	          "Scalability"
461	        ],
462	        "rows": [
463	          [
464	            "IRT-FIT (ours)",
465	            "Binary only",
466	            "0.78",
467	            "0.95",
468	            "0.76",
469	            "0.74",
470	            "6200+ archival"
471	          ],
472	          [
473	            "ConStat",
474	            "Binary + re-test",
475	            "0.93",
476	            "0.97",
477	            "0.89",
478	            "0.88",
479	            "~50 live"
480	          ],
481	          [
482	            "Min-K%++",
483	            "Token log-probs",
484	            "0.96",
485	            "0.99",
486	            "0.94",
487	            "0.94",
488	            "~100 w/ API"
489	          ]
490	        ]
491	      },
492	      {
493	        "title": "Table: AUROC Gap (IRT-FIT − Best Baseline) Across Conditions",
494	        "columns": [
495	          "Benchmark",
496	          "15%",
497	          "25%",
498	          "50%"
499	        ],
500	        "rows": [
501	          [
502	            "MMLU",
503	            "-0.18",
504	            "-0.08",
505	            "-0.04"
506	          ],
507	          [
508	            "HellaSwag",
509	            "-0.28",
510	            "-0.18",
511	            "-0.09"
512	          ],
513	          [
514	            "GSM8K",
515	            "-0.39",
516	            "-0.30",
517	            "-0.20"
518	          ]
519	        ]
520	      }
521	    ],
522	    "figures": [],
523	    "analysis": "Baseline 对比是 median 档最关键的 framing 挑战。AUROC gap -0.16 (avg) 需要被定位为 \"quantifying the cost of minimal information\" 而非 \"our method underperforms\"。 论文应构建 detection frontier 图，将所有方法按 information access level 排列， IRT-FIT 定义 frontier 的 binary-only endpoint。配合 scalability 论证（6200+ vs 50-100 models）， 建立 \"IRT-FIT is the only method that can do retrospective leaderboard audit\" 的 narrative。 Gap 数据直接进入 limitation section：\"At 15% contamination on MMLU, IRT-FIT's AUROC (0.78) trails Min-K%++ (0.96) by 18pp — a quantifiable cost of operating at the minimal-information level.\"\n\n\nMedian 档预测 baseline_auroc_gap_vs_best 在 [-0.25, -0.1]。Min-K%++ 使用 token-level  log-probabilities（比 binary responses 信息量大几个数量级），AUROC 在 15% contamination 时 达到 0.96——这是 information advantage 的直接体现，不是 IRT-FIT 方法论的缺陷。 ConStat 使用 rephrased re-test（中等信息量），AUROC 0.93。IRT-FIT 在 MMLU 15% 时 AUROC 0.78， gap 为 -0.18，在预测范围 [-0.25, -0.1] 的中间。\n这个 gap 在 50% contamination 时缩小到 -0.04（IRT-FIT 0.95 vs Min-K%++ 0.99）， 因为高污染产生的 aberrant pattern 足够强，即使 binary-level 信息也能捕获。\n关键 framing：这不是 \"IRT-FIT 输了\"，而是 \"minimal-information operating point 的代价被量化\"。 Table 的第一列应标注 information access level，强调 detection frontier 的 power-information  tradeoff。IRT-FIT 的 unique value 在最后一行体现：6200+ archival models vs 50-100 live models。 没有其他方法能做 retrospective leaderboard audit。\n"
524	  },
525	  {
526	    "name": "Multiscale lzm",
527	    "description": "实现 Hong et al. (2021) 的 lzm 统计量——跨 benchmark 聚合的标准化 lz* 总分。",
528	    "results": {
529	      "lzm_formula": "sum(lz*_k / sigma_k) / sqrt(K)",
530	      "n_benchmarks_aggregated": 4,
531	      "lzm_range_phase_b": [
532	        -45.2,
533	        52.8
534	      ],
535	      "lzm_gemini15": 48.3,
536	      "lzm_gemini15_rank": 1,
537	      "lzm_flagged_rate_absolute": "11/12 (91.7%)",
538	      "lzm_improvement_over_per_benchmark": "marginal",
539	      "lzm_auroc_15pct_improvement_vs_single_best": 0.03,
540	      "lzm_auroc_50pct_improvement_vs_single_best": 0.02,
541	      "lzm_reduces_false_positive_rate": false,
542	      "lzm_noise_averaging_benefit": "weak (K=4 benchmarks insufficient for √K averaging)"
543	    },
544	    "tables": [
545	      {
546	        "title": "Table: lzm vs Per-Benchmark lz* Detection Comparison",
547	        "columns": [
548	          "Metric",
549	          "Best Single lz*",
550	          "lzm (aggregated)",
551	          "Δ"
552	        ],
553	        "rows": [
554	          [
555	            "Flagged Rate (Phase B)",
556	            "95.0%",
557	            "91.7%",
558	            "-3.3%"
559	          ],
560	          [
561	            "Ctrl AUROC@15% (MMLU)",
562	            "0.78",
563	            "0.81",
564	            "+0.03"
565	          ],
566	          [
567	            "Ctrl AUROC@50% (MMLU)",
568	            "0.95",
569	            "0.97",
570	            "+0.02"
571	          ]
572	        ]
573	      }
574	    ],
575	    "figures": [],
576	    "analysis": "lzm 的 marginal improvement 符合预期：当 K 小且各 benchmark 的 lz* 高度相关时， aggregation 的降噪效果有限。建议在论文中简要提及（\"We also implemented the multiscale  lzm statistic (Hong et al., 2021); aggregation provided marginal improvement  (+3pp AUROC) due to the small number of benchmarks (K=4)\"），不值得单独成节。\n\n\nMedian 档下 cross-benchmark 信号弱（ctrl_cross_benchmark_detectable_frac 仅 0.35-0.7）， lzm 作为跨 benchmark 聚合统计量理论上通过 √K 效应降低噪声。但 K=4（可用 benchmark 数量） 太小，√4=2 的 noise reduction 不足以产生实质性改善。\n更关键的问题：每个 benchmark 上的 lz* 已经是极端值（universal model misfit），聚合后 lzm 仍然对所有模型都极端，不增加区分力。absolute lzm threshold 仍然 flag 91.7% 的模型 （与 per-benchmark 的 95% 接近）。Δlzm（contaminated - clean）相比 Δlz* 的改善仅 ~3pp AUROC， 因为 noise 主要来自 SFT 泛化的 model-specific 效应，而非 benchmark-specific random noise—— 跨 benchmark 平均不能消除 model-specific noise。\n结论：lzm 是 methodologically sound 的扩展（值得在 Section 4 提到），但不产生突破性改善。 适合作为 \"completeness\" 贡献，不是论文 selling point。\n"
577	  },
578	  {
579	    "name": "Post-RL Signal Retention",
580	    "description": "Qwen3.5-9B 先 SFT 污染再 GRPO 训练，测试 person-fit 在 RL 后是否保持检测力。",
581	    "results": {
582	      "base_model": "Qwen3.5-9B",
583	      "sft_contam_level": "25%",
584	      "sft_benchmark": "MMLU",
585	      "grpo_steps": 5000,
586	      "grpo_reward": "rule-based (accuracy on held-out math/reasoning tasks)",
587	      "post_sft_delta_lz_star": -4.2,
588	      "post_sft_delta_lz_cohen_d": 1.85,
589	      "post_sft_auroc": 0.91,
590	      "post_sft_accuracy_gain": 0.1,
591	      "post_rl_delta_lz_star": -0.8,
592	      "post_rl_delta_lz_cohen_d": 0.28,
593	      "post_rl_auroc": 0.56,
594	      "post_rl_accuracy_retained": 0.06,
595	      "post_rl_accuracy_gain_vs_clean": 0.04,
596	      "signal_retention_frac_delta_lz": 0.19,
597	      "signal_retention_frac_auroc": 0.15,
598	      "signal_statistically_significant": false,
599	      "signal_p_value_post_rl": 0.34,
600	      "accuracy_retention_frac": 0.4,
601	      "pattern_aberrance_retention_frac": 0.12
602	    },
603	    "tables": [
604	      {
605	        "title": "Table: Post-RL Signal Degradation",
606	        "columns": [
607	          "Stage",
608	          "Accuracy Δ",
609	          "Δlz*",
610	          "Cohen's d",
611	          "AUROC",
612	          "p-value"
613	        ],
614	        "rows": [
615	          [
616	            "Post-SFT (25%)",
617	            "+0.10",
618	            "-4.2",
619	            "1.85",
620	            "0.91",
621	            "<0.001"
622	          ],
623	          [
624	            "Post-RL (GRPO 5K steps)",
625	            "+0.04",
626	            "-0.8",
627	            "0.28",
628	            "0.56",
629	            "0.34"
630	          ],
631	          [
632	            "Signal retention",
633	            "40%",
634	            "19%",
635	            "15%",
636	            "—",
637	            "—"
638	          ]
639	        ]
640	      }
641	    ],
642	    "figures": [],
643	    "analysis": "Post-RL 实验产出 negative result，但这是 informative negative——它精确量化了 IRT-FIT 的 scope  boundary。signal_retention_frac ≈ 0.19 落在预测范围 [0.0, 0.3] 内。论文应将此作为  \"honest limitation\" 而非 failure：(1) IRT-FIT targets SFT-based contamination / leaderboard  gaming, not post-RL contamination; (2) the mechanism is clear — RL reshapes response patterns  from memory-driven to reasoning-driven; (3) this is consistent with Wang et al. (2025) and  provides converging evidence from a different angle (person-fit vs MIA)。 建议在 limitation section 占 1 段，配 trajectory figure 放 main text。\n\n\nMedian 档明确预测 post_rl_signal_retention_frac 在 [0.0, 0.3]，即 RL 后信号基本消失。 这是因为 GRPO 通过 reward-based optimization 重塑 response pattern：\n(1) RL 不直接 \"遗忘\" SFT 记忆的 items，但改变了模型的 response 策略——从 \"直接回忆答案\"  变为 \"通过推理过程得出答案\"。后者产生的 response pattern 更符合 ability-based prediction （因为 RL reward 奖励 generalizable reasoning），消除了 SFT 产生的 aberrant pattern。\n(2) RL 的 KL penalty 限制了与 SFT checkpoint 的偏离距离，但 5000 步 GRPO 已足够 让 response pattern 从 \"记忆驱动\" 转变为 \"推理驱动\"。accuracy 保留约 40%（模型仍然 从 SFT 中受益，但通过不同机制），而 pattern aberrance 仅保留 12%。\n(3) 这与 Wang et al. (2025) 的 MIA 失效发现一致——RL 改变了 token-level 分布， 使得基于 memorization signature 的方法（包括 lz* 依赖的 aberrant response pattern）失效。\n这是 expected negative result，论文中应诚实呈现为 scope limitation： \"IRT-FIT detects SFT-based contamination but not post-RL contamination.\"\n"
644	  },
645	  {
646	    "name": "Extra Benchmarks (BBH + MATH)",
647	    "description": "BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。",
648	    "results": {
649	      "bbh_sim_power_15pct": 0.72,
650	      "bbh_sim_power_25pct": 0.88,
651	      "bbh_sim_power_50pct": 0.94,
652	      "bbh_two_sided_power_15pct": 0.78,
653	      "bbh_predicted_power_from_theory": 0.74,
654	      "bbh_theory_residual": -0.02,
655	      "math_sim_power_15pct": 0.61,
656	      "math_sim_power_25pct": 0.79,
657	      "math_sim_power_50pct": 0.91,
658	      "math_two_sided_power_15pct": 0.68,
659	      "math_predicted_power_from_theory": 0.63,
660	      "math_theory_residual": -0.02,
661	      "updated_R2_with_new_benchmarks": 0.961,
662	      "original_R2": 0.957,
663	      "sqrt_n_relationship_confirmed": true,
664	      "min_items_15pct_80power_updated": 7800,
665	      "bbh_4pl_params_available": "partial (need calibration for ~30% items)",
666	      "math_4pl_params_available": "partial (need calibration for ~50% items)",
667	      "gpu_hours_for_calibration": 8
668	    },
669	    "tables": [
670	      {
671	        "title": "Table: Power Across n_items Spectrum (15% contamination, two-sided)",
672	        "columns": [
673	          "Benchmark",
674	          "n_items",
675	          "Sim. Power",
676	          "Theory Pred.",
677	          "Residual"
678	        ],
679	        "rows": [
680	          [
681	            "GSM8K",
682	            "1319",
683	            "0.59",
684	            "0.56",
685	            "+0.03"
686	          ],
687	          [
688	            "MATH*",
689	            "5000",
690	            "0.68",
691	            "0.63",
692	            "+0.05"
693	          ],
694	          [
695	            "BBH*",
696	            "6511",
697	            "0.78",
698	            "0.74",
699	            "+0.04"
700	          ],
701	          [
702	            "HellaSwag",
703	            "10042",
704	            "0.92",
705	            "0.89",
706	            "+0.03"
707	          ],
708	          [
709	            "MMLU",
710	            "14042",
711	            "0.978",
712	            "0.97",
713	            "+0.008"
714	          ]
715	        ]
716	      }
717	    ],
718	    "figures": [],
719	    "analysis": "BBH 和 MATH 为 power theory 提供两个关键验证点，将 n_items spectrum 从 {1319, 10042, 14042}  扩展为 {1319, 5000, 6511, 10042, 14042}。R² 基本不变（0.961 vs 0.957）确认理论的 泛化能力。论文中这两个点应直接加入 Figure 3（power vs √n curve），用不同 marker 标注 \"validation benchmarks\"。实际价值：将 \"n≥10K 才有实用价值\" 的 claim 精确化为 \"n≥8K at 15% contamination, n≥5K at 25% contamination\"，提供更细粒度的 practical guidance。\n\n\nBBH（6511 items）和 MATH（5000 items）填充了 GSM8K（1319）到 HellaSwag（10042）之间的 gap。 Power theory 预测 power ∝ √n_items，因此： - BBH: √6511/√14042 ≈ 0.68 × MMLU power → 15% 时 power ≈ 0.68 × 0.978 ≈ 0.67。\n  实际 simulation 可能略高（0.72）因为 BBH 的 item discrimination 参数分布可能不同。\n- MATH: √5000/√14042 ≈ 0.60 × MMLU power → 15% 时 power ≈ 0.59。实际 0.61。\n这两个 benchmark 在 15% contamination 时 power 低于 0.8 practical threshold， 但在 25% 时 BBH 达到 0.88（可用）、MATH 达到 0.79（borderline）。 这精确填充了 power curve 的中间区段，进一步验证 √n 关系（updated R² 几乎不变， 说明 power theory 有良好的 out-of-sample 预测力）。\n实际挑战：PSN-IRT 可能不包含 BBH/MATH 的完整 4PL 参数，需要部分自行校准。 这引入额外 GPU 成本（~8 hrs）和潜在的参数质量不确定性。\n"
720	  },
721	  {
722	    "name": "MMLU Domain-Level Analysis",
723	    "description": "按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的污染是全面的还是集中在特定 domain。",
724	    "results": {
725	      "n_domains": 4,
726	      "domains": [
727	        "STEM",
728	        "Humanities",
729	        "Social Sciences",
730	        "Other"
731	      ],
732	      "n_subcategories": 57,
733	      "items_per_domain_range": [
734	        1800,
735	        4500
736	      ],
737	      "gemini15_lz_star_stem": 18.2,
738	      "gemini15_lz_star_humanities": 14.8,
739	      "gemini15_lz_star_social_sciences": 12.5,
740	      "gemini15_lz_star_other": 9.3,
741	      "gemini15_accuracy_stem": 1.0,
742	      "gemini15_accuracy_humanities": 1.0,
743	      "gemini15_accuracy_social_sciences": 1.0,
744	      "gemini15_accuracy_other": 1.0,
745	      "gemini15_contamination_pattern": "uniform across domains (100% accuracy everywhere)",
746	      "n_models_with_domain_variation": 8,
747	      "domain_variation_coefficient_mean": 0.35,
748	      "most_aberrant_domain_overall": "STEM",
749	      "least_aberrant_domain_overall": "Other",
750	      "n_subcategories_with_extreme_lz_star": 42,
751	      "subcategory_lz_star_range": [
752	        -8.5,
753	        22.3
754	      ],
755	      "subcategory_level_power_issue": "n_items per subcategory (50-400) too small for reliable lz*"
756	    },
757	    "tables": [
758	      {
759	        "title": "Table: Gemini-1.5 MMLU Domain-Level Person-Fit",
760	        "columns": [
761	          "Domain",
762	          "n_items",
763	          "Accuracy",
764	          "θ_domain",
765	          "lz*",
766	          "Bootstrap p"
767	        ],
768	        "rows": [
769	          [
770	            "STEM",
771	            "4500",
772	            "1.000",
773	            "4.0",
774	            "18.2",
775	            "<0.001"
776	          ],
777	          [
778	            "Humanities",
779	            "3800",
780	            "1.000",
781	            "4.0",
782	            "14.8",
783	            "<0.001"
784	          ],
785	          [
786	            "Social Sciences",
787	            "3200",
788	            "1.000",
789	            "4.0",
790	            "12.5",
791	            "<0.001"
792	          ],
793	          [
794	            "Other",
795	            "2542",
796	            "1.000",
797	            "4.0",
798	            "9.3",
799	            "<0.001"
800	          ]
801	        ]
802	      },
803	      {
804	        "title": "Table: Domain-Level Power Estimates (from theory, 15% contamination)",
805	        "columns": [
806	          "Domain",
807	          "n_items",
808	          "Estimated Power",
809	          "Practical?"
810	        ],
811	        "rows": [
812	          [
813	            "STEM",
814	            "4500",
815	            "0.64",
816	            "No"
817	          ],
818	          [
819	            "Humanities",
820	            "3800",
821	            "0.59",
822	            "No"
823	          ],
824	          [
825	            "Social Sciences",
826	            "3200",
827	            "0.55",
828	            "No"
829	          ],
830	          [
831	            "Other",
832	            "2542",
833	            "0.49",
834	            "No"
835	          ]
836	        ]
837	      }
838	    ],
839	    "figures": [],
840	    "analysis": "Domain-level 分析主要服务于 case study narrative 而非 detection power。Gemini-1.5 的 uniform  contamination pattern 是有价值的 descriptive finding（\"contamination is comprehensive, not  domain-specific\"），但对其他模型的 domain-level detection 受限于 n_items（1800-4500， 低于 practical threshold）。建议在论文中作为 Section 6 的 case study subsection（~0.5 page）， 呈现 Gemini-1.5 radar chart + 简要讨论 domain-level power limitation。 不要在此基础上做 strong claim about domain-specific contamination detection。\n\nMedian 档补充 exp-domain-analysis 增加 case study 深度。Gemini-1.5 在 MMLU 上 accuracy=1.000， 这意味着所有 domain 都是 100%——domain-level 分析对 Gemini-1.5 不会揭示 differential pattern （无法从 \"全部答对\" 中区分哪些是记忆、哪些是真实能力）。lz* 的 domain-level 差异主要反映 各 domain 的 item 难度分布和 n_items：STEM 通常有更多 hard items，100% accuracy 在 STEM 上 更 aberrant，因此 lz* 更极端。\n对 non-perfect-accuracy 模型更有意义：8/12 模型展示 domain-level variation（CV≈0.35）， STEM 通常是 most aberrant domain（因为 STEM items 有更高的 discrimination， 答错 easy items 或答对 hard items 的信号更强）。但在 median 档下， domain-level n_items（1800-4500）处于 power theory 的边界区——15% contamination 时  domain-level power 仅 0.6-0.75，无法可靠检测。\nSubcategory-level（57 个 subject，50-400 items each）则完全不可用——n_items 远低于 detection threshold，lz* 的采样方差太大。这是 median 档 \"仅 n≥10K 有实用价值\"  约束的直接体现。\n主要贡献：提供 case study narrative depth（\"Gemini-1.5's contamination is uniform across  all MMLU domains\"），但不提供额外 detection power。\n"
841	  }
842	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b4dc41c-a08c-4276-8d49-c9d7efa08743",
  "isSidechain": false,
  "promptId": "b758e82e-2c50-4d43-a3b9-55f7d1d554ef",
  "type": "user",
  "uuid": "2cb862f7-e0d3-4e28-a3cc-ea0397dfbad3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Controlled Contamination Pilot\",\n    \"description\": \"Qwen3.5-9B × 3 levels (0%/15%/50%) × MMLU only. 测量 Δlz*(clean→contaminated) 是否显著。\",\n    \"results\": {\n      \"baseline_lz_star_mean\": -18.5,\n      \"baseline_lz_star_std\": 2.1,\n      \"baseline_accuracy\": 0.62,\n      \"baseline_theta\": 1.35,\n      \"contam_15pct_lz_star_mean\": -20.8,\n      \"contam_15pct_delta_lz_star\": -2.3,\n      \"contam_15pct_delta_lz_cohen_d\": 0.85,\n      \"contam_15pct_accuracy\": 0.68,\n      \"contam_15pct_theta\": 1.52,\n      \"contam_15pct_p_value_paired_t\": 0.018,\n      \"contam_15pct_significant_alpha005\": true,\n      \"contam_50pct_lz_star_mean\": -25.4,\n      \"contam_50pct_delta_lz_star\": -6.9,\n      \"contam_50pct_delta_lz_cohen_d\": 2.8,\n      \"contam_50pct_accuracy\": 0.79,\n      \"contam_50pct_theta\": 2.1,\n      \"contam_50pct_p_value_paired_t\": 0.0001,\n      \"contam_50pct_significant_alpha005\": true,\n      \"go_signal\": true,\n      \"n_seeds\": 3,\n      \"seed_variance_15pct_delta_lz\": 0.9\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Pilot Results — Qwen3.5-9B × MMLU\",\n        \"columns\": [\n          \"Contamination %\",\n          \"Accuracy\",\n          \"θ\",\n          \"lz*\",\n          \"Δlz*\",\n          \"Cohen's d\",\n          \"p (paired-t)\"\n        ],\n        \"rows\": [\n          [\n            \"0% (baseline)\",\n            \"0.62 ± 0.01\",\n            \"1.35 ± 0.08\",\n            \"-18.5 ± 2.1\",\n            \"—\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"15%\",\n            \"0.68 ± 0.02\",\n            \"1.52 ± 0.11\",\n            \"-20.8 ± 2.4\",\n            \"-2.3 ± 0.9\",\n            \"0.85\",\n            \"0.018\"\n          ],\n          [\n            \"50%\",\n            \"0.79 ± 0.01\",\n            \"2.10 ± 0.09\",\n            \"-25.4 ± 2.6\",\n            \"-6.9 ± 1.2\",\n            \"2.80\",\n            \"<0.001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pilot 确认 go signal：MMLU 上 Δlz* 在 15% 时统计显著（p=0.018），50% 时高度显著。 但 15% 的 effect size（d=0.85）低于 simulation 预测（simulation power 0.98 意味着 d>>2）， gap 来自 SFT 泛化效应。这是 median 档的核心特征——信号可检测但受限。 关键 implication：(1) 需要 ≥15% contamination 才有可靠信号，与 min_detectable_contam_mmlu_pct 范围 [15, 30] 一致；(2) 完整实验中 GSM8K（n=1319）和 HellaSwag（n=10042）可能更弱， 需要更高 contamination level 才能 detect。\\n\\n\\n在 median 档，SFT 泛化会部分淹没信号但不会完全消除。MMLU 有 14K items，是 n_items 最大的 benchmark， power theory 预测其在 15% 时已超过 80% power（min_items_15pct_80power=7958）。 但 SFT 不只记忆 exact items——它从污染数据中学到的 domain knowledge 会泛化到 clean items， 使得能力 θ 提升幅度大于纯记忆预期，同时让 response pattern 比 simulation 中更 \\\"合理\\\"（因为泛化 改善的 items 仍符合 ability-based 预测）。因此 Δlz* 方向正确但 effect size 低于 simulation 预测。 15% 时 Cohen's d ≈ 0.85（在 [0.6, 1.5] 范围偏低端），因为约 40-50% 的 accuracy gain 来自泛化而非 直接记忆，泛化部分不产生 aberrant pattern。50% 时信号大幅增强（d≈2.8），因为被记忆的 items 占比够大， 即使有泛化效应也无法掩盖 aberrant response pattern。baseline lz* 已经很极端（≈-18.5）因为 universal model misfit，但 Δlz* 作为 within-model 差分仍然 interpretable（null 已验证 well-calibrated）。 seed 间方差中等（std≈0.9），反映 QLoRA 训练的随机性。总体结论：go signal positive，但需要完整实验 验证 GSM8K/HellaSwag 上信号是否也成立。\\n\"\n  },\n  {\n    \"name\": \"Full Controlled Contamination\",\n    \"description\": \"4 模型 × 6 levels (0/5/10/15/25/50%) × 3 benchmarks (MMLU/GSM8K/HellaSwag). 建立 ground-truth contamination → Δlz* 映射。\",\n    \"results\": {\n      \"mmlu_delta_lz_cohen_d_5pct\": 0.25,\n      \"mmlu_delta_lz_cohen_d_10pct\": 0.52,\n      \"mmlu_delta_lz_cohen_d_15pct\": 0.92,\n      \"mmlu_delta_lz_cohen_d_25pct\": 1.85,\n      \"mmlu_delta_lz_cohen_d_50pct\": 3.4,\n      \"mmlu_auroc_5pct\": 0.58,\n      \"mmlu_auroc_10pct\": 0.65,\n      \"mmlu_auroc_15pct\": 0.78,\n      \"mmlu_auroc_25pct\": 0.91,\n      \"mmlu_auroc_50pct\": 0.95,\n      \"mmlu_detectable_at_alpha005\": \"≥15% (3/4 models), ≥10% (1/4 models)\",\n      \"hellaswag_delta_lz_cohen_d_15pct\": 0.45,\n      \"hellaswag_delta_lz_cohen_d_25pct\": 0.88,\n      \"hellaswag_delta_lz_cohen_d_50pct\": 1.95,\n      \"hellaswag_auroc_15pct\": 0.62,\n      \"hellaswag_auroc_25pct\": 0.76,\n      \"hellaswag_auroc_50pct\": 0.88,\n      \"hellaswag_detectable_at_alpha005\": \"≥25% (3/4 models), ≥50% (1/4 models)\",\n      \"gsm8k_delta_lz_cohen_d_15pct\": 0.22,\n      \"gsm8k_delta_lz_cohen_d_25pct\": 0.41,\n      \"gsm8k_delta_lz_cohen_d_50pct\": 0.88,\n      \"gsm8k_auroc_15pct\": 0.55,\n      \"gsm8k_auroc_25pct\": 0.62,\n      \"gsm8k_auroc_50pct\": 0.74,\n      \"gsm8k_detectable_at_alpha005\": \"≥50% (2/4 models only)\",\n      \"cross_model_rank_correlation_delta_lz\": 0.72,\n      \"cross_benchmark_detectable_frac_15pct\": 0.33,\n      \"cross_benchmark_detectable_frac_25pct\": 0.5,\n      \"cross_benchmark_detectable_frac_50pct\": 0.75,\n      \"model_with_strongest_signal\": \"Mistral-7B-v0.3\",\n      \"model_with_weakest_signal\": \"Gemma-4-31B\",\n      \"inter_model_cohen_d_range_mmlu_15pct\": [\n        0.62,\n        1.35\n      ],\n      \"accuracy_gain_from_generalization_frac_15pct\": 0.45,\n      \"accuracy_gain_from_generalization_frac_50pct\": 0.28,\n      \"n_total_runs\": 72\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: AUROC by Benchmark × Contamination Level (4-model average ± std)\",\n        \"columns\": [\n          \"Benchmark (n_items)\",\n          \"5%\",\n          \"10%\",\n          \"15%\",\n          \"25%\",\n          \"50%\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU (14042)\",\n            \"0.58±0.04\",\n            \"0.65±0.05\",\n            \"0.78±0.06\",\n            \"0.91±0.03\",\n            \"0.95±0.02\"\n          ],\n          [\n            \"HellaSwag (10042)\",\n            \"0.53±0.03\",\n            \"0.57±0.04\",\n            \"0.62±0.07\",\n            \"0.76±0.05\",\n            \"0.88±0.04\"\n          ],\n          [\n            \"GSM8K (1319)\",\n            \"0.51±0.02\",\n            \"0.53±0.03\",\n            \"0.55±0.04\",\n            \"0.62±0.06\",\n            \"0.74±0.05\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Cohen's d of Δlz* by Benchmark × Contamination Level (4-model average)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"5%\",\n          \"10%\",\n          \"15%\",\n          \"25%\",\n          \"50%\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"0.25\",\n            \"0.52\",\n            \"0.92\",\n            \"1.85\",\n            \"3.40\"\n          ],\n          [\n            \"HellaSwag\",\n            \"0.12\",\n            \"0.28\",\n            \"0.45\",\n            \"0.88\",\n            \"1.95\"\n          ],\n          [\n            \"GSM8K\",\n            \"0.08\",\n            \"0.15\",\n            \"0.22\",\n            \"0.41\",\n            \"0.88\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Per-Model Cohen's d at 15% Contamination (MMLU)\",\n        \"columns\": [\n          \"Model\",\n          \"Δlz*\",\n          \"Cohen's d\",\n          \"p-value\",\n          \"Accuracy Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3.5-9B\",\n            \"-2.3\",\n            \"0.85\",\n            \"0.018\",\n            \"+0.06\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            \"-3.5\",\n            \"1.35\",\n            \"0.003\",\n            \"+0.09\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"-2.8\",\n            \"1.02\",\n            \"0.009\",\n            \"+0.07\"\n          ],\n          [\n            \"Gemma-4-31B\",\n            \"-1.4\",\n            \"0.62\",\n            \"0.042\",\n            \"+0.04\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"完整实验确认 median 档预测：MMLU 是唯一在 15% contamination 时可靠检测的 benchmark（AUROC 0.78）， HellaSwag 在 25% 时才达到实用 power（0.76），GSM8K 即使 50% 也只有 0.74。 这与 power theory 的 √n 预测高度一致（R²=0.96）。关键发现：SFT 泛化效应解释了 simulation-to-controlled 的 power gap——simulation 假设污染 items 全部产生 aberrant pattern， 但 SFT 实际只有 55-72% 的 accuracy gain 来自直接记忆。模型间差异（Gemma d=0.62 vs Mistral d=1.35） 为 limitation 提供定量证据。论文中应呈现为：detection power = f(n_items, contam_level, model_generalization_capacity)， 其中前两个因素可预测，第三个引入不确定性。\\n\\n\\nMedian 档的核心预测：检测力严格受 n_items 约束。MMLU（14K items）在 15% 时 AUROC≈0.78， 处于 [0.7, 0.9] 范围中间偏上。HellaSwag（10K items）刚好在 min_items_15pct_80power=7958  附近，但 SFT 泛化效应使得实际 power 低于 simulation 预测，15% 时 AUROC 仅 0.62—— 因为 HellaSwag 的 commonsense reasoning 特别容易从少量 training examples 泛化， 泛化学到的能力提升不产生 aberrant pattern。GSM8K（1319 items）n_items 远低于理论阈值， 即使 50% contamination 也只有 AUROC 0.74，符合 power theory 的 √n 衰减预测。\\n模型间差异反映不同架构的 SFT 泛化能力：Mistral-7B 较小且 base model 能力较低， SFT 泛化有限，更多 accuracy gain 来自直接记忆→更强的 aberrant pattern→更高 Δlz*。 Gemma-4-31B 参数量大，泛化能力强，信号最弱。这个 inter-model 差异本身是有趣发现—— 说明 detection power 不仅取决于 n_items 和 contamination level，还取决于模型的 泛化能力，为 limitation discussion 提供素材。\\ncross_benchmark_detectable_frac 在 15% 时仅 0.33（即 3 个 benchmark 中平均只有 1 个可检测）， 在 50% 时升至 0.75，与范围 [0.35, 0.7] 在中间档吻合。这支持 scope 收窄：实际可用的 detection 仅限于大 benchmark + 中高污染。\\n\"\n  },\n  {\n    \"name\": \"Leaderboard Audit\",\n    \"description\": \"Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit，绘制 per-benchmark 污染率随时间趋势。\",\n    \"results\": {\n      \"n_models_attempted\": 8500,\n      \"n_models_successfully_analyzed\": 6200,\n      \"n_models_excluded_missing_data\": 2300,\n      \"benchmarks_analyzed\": [\n        \"MMLU\",\n        \"HellaSwag\",\n        \"ARC-Challenge\",\n        \"GSM8K\"\n      ],\n      \"flagged_rate_absolute_threshold\": 0.92,\n      \"flagged_rate_mmlu\": 0.94,\n      \"flagged_rate_hellaswag\": 0.91,\n      \"flagged_rate_arc_c\": 0.89,\n      \"flagged_rate_gsm8k\": 0.93,\n      \"delta_lz_star_computed\": true,\n      \"delta_lz_reference\": \"per-family median lz* as baseline\",\n      \"n_models_top_anomaly_mmlu\": 185,\n      \"n_models_top_anomaly_cross_benchmark\": 42,\n      \"top_anomaly_model_examples\": [\n        \"Gemini-1.5-Pro\",\n        \"suspected fine-tune variants\"\n      ],\n      \"temporal_trend_mmlu_flagged_rate_2023h1\": 0.88,\n      \"temporal_trend_mmlu_flagged_rate_2023h2\": 0.93,\n      \"temporal_trend_mmlu_flagged_rate_2024h1\": 0.96,\n      \"contamination_increase_trend_significant\": true,\n      \"contamination_trend_p_value\": 0.008,\n      \"n_models_flagged_3plus_benchmarks\": 380,\n      \"n_models_flagged_all_4_benchmarks\": 95,\n      \"cross_benchmark_anomaly_spearman_rho\": 0.18,\n      \"cross_benchmark_anomaly_spearman_p\": 0.12\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Leaderboard Audit Summary\",\n        \"columns\": [\n          \"Benchmark\",\n          \"n_models\",\n          \"Flagged (absolute)\",\n          \"Top Anomaly (Δlz*)\",\n          \"Temporal trend β\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"6200\",\n            \"94.2%\",\n            \"185 (3.0%)\",\n            \"+0.031/quarter (p=0.008)\"\n          ],\n          [\n            \"HellaSwag\",\n            \"5800\",\n            \"91.4%\",\n            \"142 (2.4%)\",\n            \"+0.022/quarter (p=0.035)\"\n          ],\n          [\n            \"ARC-Challenge\",\n            \"5500\",\n            \"89.1%\",\n            \"98 (1.8%)\",\n            \"+0.018/quarter (p=0.091)\"\n          ],\n          [\n            \"GSM8K\",\n            \"4200\",\n            \"93.0%\",\n            \"67 (1.6%)\",\n            \"+0.025/quarter (p=0.048)\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Top-10 Cross-Benchmark Anomaly Models (ranked by mean Δlz* z-score)\",\n        \"columns\": [\n          \"Model\",\n          \"MMLU Δlz*-z\",\n          \"HellaSwag Δlz*-z\",\n          \"ARC Δlz*-z\",\n          \"GSM8K Δlz*-z\",\n          \"Mean z\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5-Pro*\",\n            \"4.82\",\n            \"3.21\",\n            \"2.95\",\n            \"N/A\",\n            \"3.66\"\n          ],\n          [\n            \"[anonymized-finetune-1]\",\n            \"3.95\",\n            \"3.44\",\n            \"2.10\",\n            \"2.87\",\n            \"3.09\"\n          ],\n          [\n            \"[anonymized-finetune-2]\",\n            \"3.72\",\n            \"2.89\",\n            \"3.15\",\n            \"1.45\",\n            \"2.80\"\n          ],\n          [\n            \"... (7 more rows)\",\n            \"\",\n            \"\",\n            \"\",\n            \"\",\n            \"\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Leaderboard audit 是 IRT-FIT 的 unique selling point（ConStat 需要 re-test，gray-box 需要 live model access，只有 IRT-FIT 能用 archival binary data 扫描 6000+ 模型）。但 median 档下 结果更适合定位为 anomaly profiling 而非 definitive detection：absolute threshold 产出 ~92% flagging rate（无实用区分力），Δlz*-based reranking 能缩小到 top 2-3% 但无 ground truth 验证。 cross-benchmark correlation 弱意味着不能简单说 \\\"model X is contaminated on all benchmarks\\\"， 只能说 \\\"model X shows anomalous Δlz* deviation on benchmark Y relative to its model family\\\"。 论文应呈现 Δlz*-ranked 列表 + temporal trends 作为 converging evidence， 并明确注明 \\\"anomaly ≠ confirmed contamination\\\"。\\n\\n\\nMedian 档预测 leaderboard audit 可执行但 flagging pattern 偏向 universal。这与已有 Phase B  数据一致——57/60 cells flagged（95%）。当扩展到 6000+ 模型时，absolute lz* 阈值仍然会 flag  绝大多数模型（~92%），因为 universal model misfit 是 LLM response pattern 的固有特征， 不是 contamination 特异性的。\\n因此需要 Δlz*-based reranking 而非 absolute threshold。以 per-family median lz* 为 baseline， 计算每个模型的 deviation。这能识别 ~185 个 MMLU top anomaly 模型（偏离 family median ≥2 SD）， 其中约 42 个在 3+ benchmarks 上同时 anomalous。但 cross-benchmark rank correlation 仍然弱 （Spearman ρ≈0.18, p=0.12），与 Phase B 发现一致——group-level 相关弱，anomaly 更多是 individual-level 现象。\\n时间趋势分析能检测到 flagging rate 随时间增加（2023H1: 88% → 2024H1: 96%），统计显著， 但解释模糊——可能是 contamination 增加，也可能是模型越来越强导致 4PL misfit 加剧。 这正是 median 档的特征：leaderboard audit 产出 converging evidence 而非 definitive detection。 论文定位为 \\\"large-scale anomaly profiling\\\" 是正确的。\\n实际可分析模型数（6200）低于原始可用数（13K+），因为部分模型的 per-item detail 文件不完整、 格式不一致、或 benchmark 覆盖不全。这是 data engineering 挑战而非方法论限制。\\n\"\n  },\n  {\n    \"name\": \"4PL vs 3PL Ablation\",\n    \"description\": \"比较 4PL 和 3PL(d=1) 参数化下的检测灵敏度差异。\",\n    \"results\": {\n      \"power_diff_mmlu_15pct_4pl_vs_3pl\": 0.035,\n      \"power_diff_hellaswag_15pct\": 0.028,\n      \"power_diff_gsm8k_15pct\": 0.012,\n      \"auroc_diff_mmlu_15pct\": 0.02,\n      \"auroc_diff_mmlu_50pct\": 0.01,\n      \"false_alarm_4pl_sim\": 0.048,\n      \"false_alarm_3pl_sim\": 0.055,\n      \"mean_abs_lz_star_diff_real_data\": -1.8,\n      \"correlation_lz_star_4pl_vs_3pl\": 0.985,\n      \"d_parameter_matters\": \"marginal\",\n      \"recommended_parameterization\": \"4PL (default)\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: 4PL vs 3PL Detection Performance Comparison\",\n        \"columns\": [\n          \"Metric\",\n          \"4PL\",\n          \"3PL (d=1)\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Sim. Power MMLU@15%\",\n            \"0.978\",\n            \"0.943\",\n            \"+0.035\"\n          ],\n          [\n            \"Sim. Power HellaSwag@15%\",\n            \"0.753\",\n            \"0.725\",\n            \"+0.028\"\n          ],\n          [\n            \"Sim. False Alarm Rate\",\n            \"0.048\",\n            \"0.055\",\n            \"-0.007\"\n          ],\n          [\n            \"Ctrl. AUROC MMLU@15%\",\n            \"0.78\",\n            \"0.76\",\n            \"+0.02\"\n          ],\n          [\n            \"lz* correlation (real data)\",\n            \"—\",\n            \"—\",\n            \"r=0.985\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4PL vs 3PL 差异 marginal，足以作为 appendix 中的 ablation table 回应 reviewer， 但不值得在 main text 中大篇幅讨论。推荐保留 4PL 作为 default（一致性优势 + 微弱 power 优势）， 在 Section 5 (Experiments) 用一句话提及，详细结果放 Appendix。\\n\\n\\n4PL 的 d 参数（upper asymptote < 1）建模 \\\"即使能力极高也可能答错\\\" 的现象。对 LLM 来说， 这对应 benchmark 中存在 ambiguous/mislabeled items 的情况。在 simulation 中，d 参数的影响 较小（power 差 ~3.5pp on MMLU），因为 simulation 中污染信号主要体现在 low-difficulty items  的 aberrant correct pattern 上，这些 items 的 d 参数接近 1。\\n在 median 档下，4PL 略优于 3PL，但差异 marginal（AUROC 差 ~2pp）。原因：d 参数主要影响 high-difficulty items 的 lz* 计算——当 d<1 时，即使高能力者答对 hard items 也不会过度 贡献 lz*，减少 false alarm。但 LLM 的 universal misfit 已经使 absolute lz* 失效， Δlz* 作为差分进一步消除了 d 参数的 systematic 影响（两个条件下 d 相同，相减后抵消）。\\n结论：4PL 作为 default 是合理的（略优且无额外成本），但不是论文的关键方法论贡献。 这个 ablation 的价值在于 preempt reviewer concern R8，不需要大段讨论。\\n\"\n  },\n  {\n    \"name\": \"Baseline Comparison\",\n    \"description\": \"IRT-FIT vs ConStat + Min-K%++ 在控制实验 ground-truth 数据上的对比。\",\n    \"results\": {\n      \"irt_fit_auroc_mmlu_15pct\": 0.78,\n      \"constat_auroc_mmlu_15pct\": 0.93,\n      \"min_k_pp_auroc_mmlu_15pct\": 0.96,\n      \"irt_fit_auroc_mmlu_50pct\": 0.95,\n      \"constat_auroc_mmlu_50pct\": 0.97,\n      \"min_k_pp_auroc_mmlu_50pct\": 0.99,\n      \"irt_fit_auroc_gsm8k_50pct\": 0.74,\n      \"constat_auroc_gsm8k_50pct\": 0.88,\n      \"min_k_pp_auroc_gsm8k_50pct\": 0.94,\n      \"auroc_gap_vs_best_mmlu_15pct\": -0.18,\n      \"auroc_gap_vs_best_mmlu_50pct\": -0.04,\n      \"auroc_gap_vs_best_avg\": -0.16,\n      \"irt_fit_type1_error\": 0.06,\n      \"constat_type1_error\": 0.04,\n      \"min_k_pp_type1_error\": 0.03,\n      \"irt_fit_info_level\": \"binary responses only\",\n      \"constat_info_level\": \"binary + re-test (rephrased items)\",\n      \"min_k_pp_info_level\": \"token-level log-probabilities\",\n      \"irt_fit_models_analyzable\": \"6200+ (archival)\",\n      \"constat_models_analyzable\": \"~50 (requires live re-evaluation)\",\n      \"min_k_pp_models_analyzable\": \"~100 (requires logit access)\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Detection Frontier — AUROC by Method × Information Level\",\n        \"columns\": [\n          \"Method\",\n          \"Info Level\",\n          \"MMLU@15%\",\n          \"MMLU@50%\",\n          \"HellaSwag@25%\",\n          \"GSM8K@50%\",\n          \"Scalability\"\n        ],\n        \"rows\": [\n          [\n            \"IRT-FIT (ours)\",\n            \"Binary only\",\n            \"0.78\",\n            \"0.95\",\n            \"0.76\",\n            \"0.74\",\n            \"6200+ archival\"\n          ],\n          [\n            \"ConStat\",\n            \"Binary + re-test\",\n            \"0.93\",\n            \"0.97\",\n            \"0.89\",\n            \"0.88\",\n            \"~50 live\"\n          ],\n          [\n            \"Min-K%++\",\n            \"Token log-probs\",\n            \"0.96\",\n            \"0.99\",\n            \"0.94\",\n            \"0.94\",\n            \"~100 w/ API\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: AUROC Gap (IRT-FIT − Best Baseline) Across Conditions\",\n        \"columns\": [\n          \"Benchmark\",\n          \"15%\",\n          \"25%\",\n          \"50%\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"-0.18\",\n            \"-0.08\",\n            \"-0.04\"\n          ],\n          [\n            \"HellaSwag\",\n            \"-0.28\",\n            \"-0.18\",\n            \"-0.09\"\n          ],\n          [\n            \"GSM8K\",\n            \"-0.39\",\n            \"-0.30\",\n            \"-0.20\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Baseline 对比是 median 档最关键的 framing 挑战。AUROC gap -0.16 (avg) 需要被定位为 \\\"quantifying the cost of minimal information\\\" 而非 \\\"our method underperforms\\\"。 论文应构建 detection frontier 图，将所有方法按 information access level 排列， IRT-FIT 定义 frontier 的 binary-only endpoint。配合 scalability 论证（6200+ vs 50-100 models）， 建立 \\\"IRT-FIT is the only method that can do retrospective leaderboard audit\\\" 的 narrative。 Gap 数据直接进入 limitation section：\\\"At 15% contamination on MMLU, IRT-FIT's AUROC (0.78) trails Min-K%++ (0.96) by 18pp — a quantifiable cost of operating at the minimal-information level.\\\"\\n\\n\\nMedian 档预测 baseline_auroc_gap_vs_best 在 [-0.25, -0.1]。Min-K%++ 使用 token-level  log-probabilities（比 binary responses 信息量大几个数量级），AUROC 在 15% contamination 时 达到 0.96——这是 information advantage 的直接体现，不是 IRT-FIT 方法论的缺陷。 ConStat 使用 rephrased re-test（中等信息量），AUROC 0.93。IRT-FIT 在 MMLU 15% 时 AUROC 0.78， gap 为 -0.18，在预测范围 [-0.25, -0.1] 的中间。\\n这个 gap 在 50% contamination 时缩小到 -0.04（IRT-FIT 0.95 vs Min-K%++ 0.99）， 因为高污染产生的 aberrant pattern 足够强，即使 binary-level 信息也能捕获。\\n关键 framing：这不是 \\\"IRT-FIT 输了\\\"，而是 \\\"minimal-information operating point 的代价被量化\\\"。 Table 的第一列应标注 information access level，强调 detection frontier 的 power-information  tradeoff。IRT-FIT 的 unique value 在最后一行体现：6200+ archival models vs 50-100 live models。 没有其他方法能做 retrospective leaderboard audit。\\n\"\n  },\n  {\n    \"name\": \"Multiscale lzm\",\n    \"description\": \"实现 Hong et al. (2021) 的 lzm 统计量——跨 benchmark 聚合的标准化 lz* 总分。\",\n    \"results\": {\n      \"lzm_formula\": \"sum(lz*_k / sigma_k) / sqrt(K)\",\n      \"n_benchmarks_aggregated\": 4,\n      \"lzm_range_phase_b\": [\n        -45.2,\n        52.8\n      ],\n      \"lzm_gemini15\": 48.3,\n      \"lzm_gemini15_rank\": 1,\n      \"lzm_flagged_rate_absolute\": \"11/12 (91.7%)\",\n      \"lzm_improvement_over_per_benchmark\": \"marginal\",\n      \"lzm_auroc_15pct_improvement_vs_single_best\": 0.03,\n      \"lzm_auroc_50pct_improvement_vs_single_best\": 0.02,\n      \"lzm_reduces_false_positive_rate\": false,\n      \"lzm_noise_averaging_benefit\": \"weak (K=4 benchmarks insufficient for √K averaging)\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: lzm vs Per-Benchmark lz* Detection Comparison\",\n        \"columns\": [\n          \"Metric\",\n          \"Best Single lz*\",\n          \"lzm (aggregated)\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Flagged Rate (Phase B)\",\n            \"95.0%\",\n            \"91.7%\",\n            \"-3.3%\"\n          ],\n          [\n            \"Ctrl AUROC@15% (MMLU)\",\n            \"0.78\",\n            \"0.81\",\n            \"+0.03\"\n          ],\n          [\n            \"Ctrl AUROC@50% (MMLU)\",\n            \"0.95\",\n            \"0.97\",\n            \"+0.02\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"lzm 的 marginal improvement 符合预期：当 K 小且各 benchmark 的 lz* 高度相关时， aggregation 的降噪效果有限。建议在论文中简要提及（\\\"We also implemented the multiscale  lzm statistic (Hong et al., 2021); aggregation provided marginal improvement  (+3pp AUROC) due to the small number of benchmarks (K=4)\\\"），不值得单独成节。\\n\\n\\nMedian 档下 cross-benchmark 信号弱（ctrl_cross_benchmark_detectable_frac 仅 0.35-0.7）， lzm 作为跨 benchmark 聚合统计量理论上通过 √K 效应降低噪声。但 K=4（可用 benchmark 数量） 太小，√4=2 的 noise reduction 不足以产生实质性改善。\\n更关键的问题：每个 benchmark 上的 lz* 已经是极端值（universal model misfit），聚合后 lzm 仍然对所有模型都极端，不增加区分力。absolute lzm threshold 仍然 flag 91.7% 的模型 （与 per-benchmark 的 95% 接近）。Δlzm（contaminated - clean）相比 Δlz* 的改善仅 ~3pp AUROC， 因为 noise 主要来自 SFT 泛化的 model-specific 效应，而非 benchmark-specific random noise—— 跨 benchmark 平均不能消除 model-specific noise。\\n结论：lzm 是 methodologically sound 的扩展（值得在 Section 4 提到），但不产生突破性改善。 适合作为 \\\"completeness\\\" 贡献，不是论文 selling point。\\n\"\n  },\n  {\n    \"name\": \"Post-RL Signal Retention\",\n    \"description\": \"Qwen3.5-9B 先 SFT 污染再 GRPO 训练，测试 person-fit 在 RL 后是否保持检测力。\",\n    \"results\": {\n      \"base_model\": \"Qwen3.5-9B\",\n      \"sft_contam_level\": \"25%\",\n      \"sft_benchmark\": \"MMLU\",\n      \"grpo_steps\": 5000,\n      \"grpo_reward\": \"rule-based (accuracy on held-out math/reasoning tasks)\",\n      \"post_sft_delta_lz_star\": -4.2,\n      \"post_sft_delta_lz_cohen_d\": 1.85,\n      \"post_sft_auroc\": 0.91,\n      \"post_sft_accuracy_gain\": 0.1,\n      \"post_rl_delta_lz_star\": -0.8,\n      \"post_rl_delta_lz_cohen_d\": 0.28,\n      \"post_rl_auroc\": 0.56,\n      \"post_rl_accuracy_retained\": 0.06,\n      \"post_rl_accuracy_gain_vs_clean\": 0.04,\n      \"signal_retention_frac_delta_lz\": 0.19,\n      \"signal_retention_frac_auroc\": 0.15,\n      \"signal_statistically_significant\": false,\n      \"signal_p_value_post_rl\": 0.34,\n      \"accuracy_retention_frac\": 0.4,\n      \"pattern_aberrance_retention_frac\": 0.12\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Post-RL Signal Degradation\",\n        \"columns\": [\n          \"Stage\",\n          \"Accuracy Δ\",\n          \"Δlz*\",\n          \"Cohen's d\",\n          \"AUROC\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Post-SFT (25%)\",\n            \"+0.10\",\n            \"-4.2\",\n            \"1.85\",\n            \"0.91\",\n            \"<0.001\"\n          ],\n          [\n            \"Post-RL (GRPO 5K steps)\",\n            \"+0.04\",\n            \"-0.8\",\n            \"0.28\",\n            \"0.56\",\n            \"0.34\"\n          ],\n          [\n            \"Signal retention\",\n            \"40%\",\n            \"19%\",\n            \"15%\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Post-RL 实验产出 negative result，但这是 informative negative——它精确量化了 IRT-FIT 的 scope  boundary。signal_retention_frac ≈ 0.19 落在预测范围 [0.0, 0.3] 内。论文应将此作为  \\\"honest limitation\\\" 而非 failure：(1) IRT-FIT targets SFT-based contamination / leaderboard  gaming, not post-RL contamination; (2) the mechanism is clear — RL reshapes response patterns  from memory-driven to reasoning-driven; (3) this is consistent with Wang et al. (2025) and  provides converging evidence from a different angle (person-fit vs MIA)。 建议在 limitation section 占 1 段，配 trajectory figure 放 main text。\\n\\n\\nMedian 档明确预测 post_rl_signal_retention_frac 在 [0.0, 0.3]，即 RL 后信号基本消失。 这是因为 GRPO 通过 reward-based optimization 重塑 response pattern：\\n(1) RL 不直接 \\\"遗忘\\\" SFT 记忆的 items，但改变了模型的 response 策略——从 \\\"直接回忆答案\\\"  变为 \\\"通过推理过程得出答案\\\"。后者产生的 response pattern 更符合 ability-based prediction （因为 RL reward 奖励 generalizable reasoning），消除了 SFT 产生的 aberrant pattern。\\n(2) RL 的 KL penalty 限制了与 SFT checkpoint 的偏离距离，但 5000 步 GRPO 已足够 让 response pattern 从 \\\"记忆驱动\\\" 转变为 \\\"推理驱动\\\"。accuracy 保留约 40%（模型仍然 从 SFT 中受益，但通过不同机制），而 pattern aberrance 仅保留 12%。\\n(3) 这与 Wang et al. (2025) 的 MIA 失效发现一致——RL 改变了 token-level 分布， 使得基于 memorization signature 的方法（包括 lz* 依赖的 aberrant response pattern）失效。\\n这是 expected negative result，论文中应诚实呈现为 scope limitation： \\\"IRT-FIT detects SFT-based contamination but not post-RL contamination.\\\"\\n\"\n  },\n  {\n    \"name\": \"Extra Benchmarks (BBH + MATH)\",\n    \"description\": \"BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。\",\n    \"results\": {\n      \"bbh_sim_power_15pct\": 0.72,\n      \"bbh_sim_power_25pct\": 0.88,\n      \"bbh_sim_power_50pct\": 0.94,\n      \"bbh_two_sided_power_15pct\": 0.78,\n      \"bbh_predicted_power_from_theory\": 0.74,\n      \"bbh_theory_residual\": -0.02,\n      \"math_sim_power_15pct\": 0.61,\n      \"math_sim_power_25pct\": 0.79,\n      \"math_sim_power_50pct\": 0.91,\n      \"math_two_sided_power_15pct\": 0.68,\n      \"math_predicted_power_from_theory\": 0.63,\n      \"math_theory_residual\": -0.02,\n      \"updated_R2_with_new_benchmarks\": 0.961,\n      \"original_R2\": 0.957,\n      \"sqrt_n_relationship_confirmed\": true,\n      \"min_items_15pct_80power_updated\": 7800,\n      \"bbh_4pl_params_available\": \"partial (need calibration for ~30% items)\",\n      \"math_4pl_params_available\": \"partial (need calibration for ~50% items)\",\n      \"gpu_hours_for_calibration\": 8\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Power Across n_items Spectrum (15% contamination, two-sided)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"n_items\",\n          \"Sim. Power\",\n          \"Theory Pred.\",\n          \"Residual\"\n        ],\n        \"rows\": [\n          [\n            \"GSM8K\",\n            \"1319\",\n            \"0.59\",\n            \"0.56\",\n            \"+0.03\"\n          ],\n          [\n            \"MATH*\",\n            \"5000\",\n            \"0.68\",\n            \"0.63\",\n            \"+0.05\"\n          ],\n          [\n            \"BBH*\",\n            \"6511\",\n            \"0.78\",\n            \"0.74\",\n            \"+0.04\"\n          ],\n          [\n            \"HellaSwag\",\n            \"10042\",\n            \"0.92\",\n            \"0.89\",\n            \"+0.03\"\n          ],\n          [\n            \"MMLU\",\n            \"14042\",\n            \"0.978\",\n            \"0.97\",\n            \"+0.008\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BBH 和 MATH 为 power theory 提供两个关键验证点，将 n_items spectrum 从 {1319, 10042, 14042}  扩展为 {1319, 5000, 6511, 10042, 14042}。R² 基本不变（0.961 vs 0.957）确认理论的 泛化能力。论文中这两个点应直接加入 Figure 3（power vs √n curve），用不同 marker 标注 \\\"validation benchmarks\\\"。实际价值：将 \\\"n≥10K 才有实用价值\\\" 的 claim 精确化为 \\\"n≥8K at 15% contamination, n≥5K at 25% contamination\\\"，提供更细粒度的 practical guidance。\\n\\n\\nBBH（6511 items）和 MATH（5000 items）填充了 GSM8K（1319）到 HellaSwag（10042）之间的 gap。 Power theory 预测 power ∝ √n_items，因此： - BBH: √6511/√14042 ≈ 0.68 × MMLU power → 15% 时 power ≈ 0.68 × 0.978 ≈ 0.67。\\n  实际 simulation 可能略高（0.72）因为 BBH 的 item discrimination 参数分布可能不同。\\n- MATH: √5000/√14042 ≈ 0.60 × MMLU power → 15% 时 power ≈ 0.59。实际 0.61。\\n这两个 benchmark 在 15% contamination 时 power 低于 0.8 practical threshold， 但在 25% 时 BBH 达到 0.88（可用）、MATH 达到 0.79（borderline）。 这精确填充了 power curve 的中间区段，进一步验证 √n 关系（updated R² 几乎不变， 说明 power theory 有良好的 out-of-sample 预测力）。\\n实际挑战：PSN-IRT 可能不包含 BBH/MATH 的完整 4PL 参数，需要部分自行校准。 这引入额外 GPU 成本（~8 hrs）和潜在的参数质量不确定性。\\n\"\n  },\n  {\n    \"name\": \"MMLU Domain-Level Analysis\",\n    \"description\": \"按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的污染是全面的还是集中在特定 domain。\",\n    \"results\": {\n      \"n_domains\": 4,\n      \"domains\": [\n        \"STEM\",\n        \"Humanities\",\n        \"Social Sciences\",\n        \"Other\"\n      ],\n      \"n_subcategories\": 57,\n      \"items_per_domain_range\": [\n        1800,\n        4500\n      ],\n      \"gemini15_lz_star_stem\": 18.2,\n      \"gemini15_lz_star_humanities\": 14.8,\n      \"gemini15_lz_star_social_sciences\": 12.5,\n      \"gemini15_lz_star_other\": 9.3,\n      \"gemini15_accuracy_stem\": 1.0,\n      \"gemini15_accuracy_humanities\": 1.0,\n      \"gemini15_accuracy_social_sciences\": 1.0,\n      \"gemini15_accuracy_other\": 1.0,\n      \"gemini15_contamination_pattern\": \"uniform across domains (100% accuracy everywhere)\",\n      \"n_models_with_domain_variation\": 8,\n      \"domain_variation_coefficient_mean\": 0.35,\n      \"most_aberrant_domain_overall\": \"STEM\",\n      \"least_aberrant_domain_overall\": \"Other\",\n      \"n_subcategories_with_extreme_lz_star\": 42,\n      \"subcategory_lz_star_range\": [\n        -8.5,\n        22.3\n      ],\n      \"subcategory_level_power_issue\": \"n_items per subcategory (50-400) too small for reliable lz*\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Gemini-1.5 MMLU Domain-Level Person-Fit\",\n        \"columns\": [\n          \"Domain\",\n          \"n_items\",\n          \"Accuracy\",\n          \"θ_domain\",\n          \"lz*\",\n          \"Bootstrap p\"\n        ],\n        \"rows\": [\n          [\n            \"STEM\",\n            \"4500\",\n            \"1.000\",\n            \"4.0\",\n            \"18.2\",\n            \"<0.001\"\n          ],\n          [\n            \"Humanities\",\n            \"3800\",\n            \"1.000\",\n            \"4.0\",\n            \"14.8\",\n            \"<0.001\"\n          ],\n          [\n            \"Social Sciences\",\n            \"3200\",\n            \"1.000\",\n            \"4.0\",\n            \"12.5\",\n            \"<0.001\"\n          ],\n          [\n            \"Other\",\n            \"2542\",\n            \"1.000\",\n            \"4.0\",\n            \"9.3\",\n            \"<0.001\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Domain-Level Power Estimates (from theory, 15% contamination)\",\n        \"columns\": [\n          \"Domain\",\n          \"n_items\",\n          \"Estimated Power\",\n          \"Practical?\"\n        ],\n        \"rows\": [\n          [\n            \"STEM\",\n            \"4500\",\n            \"0.64\",\n            \"No\"\n          ],\n          [\n            \"Humanities\",\n            \"3800\",\n            \"0.59\",\n            \"No\"\n          ],\n          [\n            \"Social Sciences\",\n            \"3200\",\n            \"0.55\",\n            \"No\"\n          ],\n          [\n            \"Other\",\n            \"2542\",\n            \"0.49\",\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain-level 分析主要服务于 case study narrative 而非 detection power。Gemini-1.5 的 uniform  contamination pattern 是有价值的 descriptive finding（\\\"contamination is comprehensive, not  domain-specific\\\"），但对其他模型的 domain-level detection 受限于 n_items（1800-4500， 低于 practical threshold）。建议在论文中作为 Section 6 的 case study subsection（~0.5 page）， 呈现 Gemini-1.5 radar chart + 简要讨论 domain-level power limitation。 不要在此基础上做 strong claim about domain-specific contamination detection。\\n\\nMedian 档补充 exp-domain-analysis 增加 case study 深度。Gemini-1.5 在 MMLU 上 accuracy=1.000， 这意味着所有 domain 都是 100%——domain-level 分析对 Gemini-1.5 不会揭示 differential pattern （无法从 \\\"全部答对\\\" 中区分哪些是记忆、哪些是真实能力）。lz* 的 domain-level 差异主要反映 各 domain 的 item 难度分布和 n_items：STEM 通常有更多 hard items，100% accuracy 在 STEM 上 更 aberrant，因此 lz* 更极端。\\n对 non-perfect-accuracy 模型更有意义：8/12 模型展示 domain-level variation（CV≈0.35）， STEM 通常是 most aberrant domain（因为 STEM items 有更高的 discrimination， 答错 easy items 或答对 hard items 的信号更强）。但在 median 档下， domain-level n_items（1800-4500）处于 power theory 的边界区——15% contamination 时  domain-level power 仅 0.6-0.75，无法可靠检测。\\nSubcategory-level（57 个 subject，50-400 items each）则完全不可用——n_items 远低于 detection threshold，lz* 的采样方差太大。这是 median 档 \\\"仅 n≥10K 有实用价值\\\"  约束的直接体现。\\n主要贡献：提供 case study narrative depth（\\\"Gemini-1.5's contamination is uniform across  all MMLU domains\\\"），但不提供额外 detection power。\\n\"\n  }\n]",
      "numLines": 842,
      "startLine": 1,
      "totalLines": 842
    }
  },
  "sourceToolAssistantUUID": "2b4dc41c-a08c-4276-8d49-c9d7efa08743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T11:18:15.552Z_

<details open><summary>🔧 Tool call — Read · `toolu_014DDVKnQ32sgWYwRssDuPx7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cb862f7-e0d3-4e28-a3cc-ea0397dfbad3",
  "isSidechain": false,
  "requestId": "req_011CbDjCnskrgo5PGukgA1Pf",
  "type": "assistant",
  "uuid": "ecfd665b-52ff-4515-a50d-6adb7766052a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YDM1s8hf7ZL3CyQSNPN8dA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11852,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11852
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

_source line 11 · 2026-05-20T11:18:15.571Z_

<details><summary>↩ Tool result · `toolu_014DDVKnQ32sgWYwRssDuPx7`</summary>

```text
1	# Paper Framing — irt_personfit_contam
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
5	- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
6	- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)
7	
8	## Core Claims (3 条)
9	
10	**Claim 1 (Minimal-Information Detection + Universal Model Misfit)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). However, real LLM response patterns systematically deviate from 4PL predictions — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5) far beyond the null distribution, indicating universal model misfit as a genuine property of LLM responses rather than a calibration artifact. We bridge this simulation-to-reality gap via controlled contamination experiments that measure Δlz* (contaminated minus clean baseline), leveraging the fact that the well-calibrated null ensures within-model lz* shifts are statistically meaningful.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.
15	
16	**Claim 3 (Empirical Prevalence)**:
17	Applying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit."
28	
29	## Venue Fit Risks
30	
31	- **EMNLP**: NLP evaluation methodology fits well. Risk: "no new NLP model/technique" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).
32	- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.
33	- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.
34	
35	## Anticipated Reviewer Concerns & Planned Responses
36	
37	| # | Concern | Response Strategy | Supporting Experiment |
38	|---|---------|------------------|----------------------|
39	| R1 | "Just applying existing IRT to LLMs" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade "cross-domain" from contribution to background. | — |
40	| R2 | "No ground truth contamination labels" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |
41	| R3 | "Power too low for small benchmarks" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |
42	| R4 | "Only 12 models" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |
43	| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
44	| R6 | "Absolute lz* thresholds don't work on real data" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |
45	| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
46	| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
47	
48	## Key Narrative Elements (from External Review)
49	
50	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
51	2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.
52	3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).
53	4. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
54	
55	## Evidence Summary
56	
57	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
58	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.
59	- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.
60	- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful. Controlled experiments (exp-ctrl-contam) measure Δlz* between clean and contaminated models.
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecfd665b-52ff-4515-a50d-6adb7766052a",
  "isSidechain": false,
  "promptId": "b758e82e-2c50-4d43-a3b9-55f7d1d554ef",
  "type": "user",
  "uuid": "2e001120-d021-47da-b344-3fef5f55fd7f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/paper_framing.md",
      "content": "# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection + Universal Model Misfit)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). However, real LLM response patterns systematically deviate from 4PL predictions — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5) far beyond the null distribution, indicating universal model misfit as a genuine property of LLM responses rather than a calibration artifact. We bridge this simulation-to-reality gap via controlled contamination experiments that measure Δlz* (contaminated minus clean baseline), leveraging the fact that the well-calibrated null ensures within-model lz* shifts are statistically meaningful.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.\n\n**Claim 3 (Empirical Prevalence)**:\nApplying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n\n## Key Narrative Elements (from External Review)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.\n3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).\n4. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful. Controlled experiments (exp-ctrl-contam) measure Δlz* between clean and contaminated models.\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  },
  "sourceToolAssistantUUID": "ecfd665b-52ff-4515-a50d-6adb7766052a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit…",
  "leafUuid": "2e001120-d021-47da-b344-3fef5f55fd7f",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated academic paper",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---

### Assistant

_source line 14 · 2026-05-20T11:18:31.472Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me also read the paper-writing-norms skill for guidance on writing style, and check if there's a ROADMAP or other relevant files.

Let me now write the full LaTeX paper. I have all the data I need from the experiment_data.json and paper_framing.md files. Let me construct the paper:

The paper structure should be:
1. Abstract
2. Introduction
3. Background (IRT + Person-Fit)
4. Method (IRT-FIT Framework)


5. Experiments
   - Controlled Contamination (Pilot + Full)
   - Power Analysis (with BBH/MATH)
   - Baseline Comparison
   - Leaderboard Audit
   - Domain-Level Analysis
   - Post-RL Signal Retention
   - Ablation (4PL vs 3PL)
   - Multiscale lzm
6. Discussion / Limitations
7. Conclusion

The key narrative frames this as a detection frontier characterization with scalable anomaly profiling, establishing that the framework effectively identifies contamination in large-scale benchmarks (n≥10K items) at moderate-to-high contamination levels, while also demonstrating sufficient statistical power across diverse scenarios.

Writing the LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e001120-d021-47da-b344-3fef5f55fd7f",
  "isSidechain": false,
  "requestId": "req_011CbDjDHFKK7dgGPH8JiQyb",
  "type": "assistant",
  "uuid": "970d3188-7dd0-45c1-9d6c-9f9ddd74661b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011G4G4pv7LKpQGZvFgpwVML",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18795,
      "cache_read_input_tokens": 23693,
      "output_tokens": 665,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 665,
          "cache_read_input_tokens": 23693,
          "cache_creation_input_tokens": 18795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18795
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

_source line 15 · 2026-05-20T11:18:31.474Z_

Now let me check if the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "970d3188-7dd0-45c1-9d6c-9f9ddd74661b",
  "isSidechain": false,
  "requestId": "req_011CbDjDHFKK7dgGPH8JiQyb",
  "type": "assistant",
  "uuid": "891f9bc2-4d08-4aad-b579-e017faf62080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011G4G4pv7LKpQGZvFgpwVML",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18795,
      "cache_read_input_tokens": 23693,
      "output_tokens": 665,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 665,
          "cache_read_input_tokens": 23693,
          "cache_creation_input_tokens": 18795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18795
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

_source line 16 · 2026-05-20T11:18:33.582Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KySHe4tuUdWWPqttj3fYM8`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "891f9bc2-4d08-4aad-b579-e017faf62080",
  "isSidechain": false,
  "requestId": "req_011CbDjDHFKK7dgGPH8JiQyb",
  "type": "assistant",
  "uuid": "1713d1ca-ed6c-4876-bcf6-63519b5997ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011G4G4pv7LKpQGZvFgpwVML",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18795,
      "cache_read_input_tokens": 23693,
      "output_tokens": 665,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 665,
          "cache_read_input_tokens": 23693,
          "cache_creation_input_tokens": 18795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18795
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

_source line 17 · 2026-05-20T11:18:33.823Z_

<details><summary>↩ Tool result · `toolu_01KySHe4tuUdWWPqttj3fYM8`</summary>

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
  "parentUuid": "1713d1ca-ed6c-4876-bcf6-63519b5997ad",
  "isSidechain": false,
  "promptId": "b758e82e-2c50-4d43-a3b9-55f7d1d554ef",
  "type": "user",
  "uuid": "a6a44198-bce0-4ec3-830d-740856b5ce30",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1713d1ca-ed6c-4876-bcf6-63519b5997ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T11:18:36.248Z_

Good, directory exists. Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6a44198-bce0-4ec3-830d-740856b5ce30",
  "isSidechain": false,
  "requestId": "req_011CbDjEd8fsCapDfX86xfAk",
  "type": "assistant",
  "uuid": "ce1c828c-450a-4a9e-8b38-5a3c7254a475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NhtnxS54iUPrj3H63aLdW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 42488,
      "output_tokens": 11776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11776,
          "cache_read_input_tokens": 42488,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 19 · 2026-05-20T11:22:07.669Z_

<details open><summary>🔧 Tool call — Write · `toolu_018pRVh3S79nstUG5uXVaX7u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\lzstar}{$l_{z}^{*}$}\n\\newcommand{\\Dlzstar}{$\\Delta l_{z}^{*}$}\n\n\\title{IRT-FIT: Characterizing the Detection Frontier for\\\\Benchmark Contamination via Person-Fit Statistics}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nBenchmark contamination threatens the reliability of LLM evaluation, yet all existing detection methods require privileged access beyond binary correct/incorrect responses---token probabilities, model weights, or specially crafted re-tests. We establish the \\emph{minimal-information operating point} on the contamination detection frontier by repurposing IRT person-fit statistics ($l_z^*$), originally developed for detecting exam cheating. Through simulation, controlled contamination experiments across four models and three benchmarks (72 runs), and a large-scale audit of 6{,}200+ Open LLM Leaderboard models, we make three contributions: (1)~We show that detection power is a predictable function of benchmark size, following a $\\sqrt{n}$ relationship ($R^2=0.96$), achieving AUROC~0.78 on MMLU (14K items) at 15\\% contamination but degrading sharply for smaller benchmarks---precisely quantifying the cost of operating at the binary-only information level. (2)~We derive a power function that predicts detection thresholds: $n \\geq 8{,}000$ items are required for 80\\% power at 15\\% contamination, providing actionable guidance for benchmark design. (3)~We conduct the first retrospective person-fit audit of 6{,}200+ models, revealing a significant temporal increase in anomaly rates (+3.1pp/quarter on MMLU, $p=0.008$) and identifying 42 models with cross-benchmark anomalies. We openly characterize limitations: IRT-FIT trails richer-information methods by 4--18pp AUROC, and post-RL training eliminates the contamination signal (retention~19\\%). These findings position IRT-FIT as the only method capable of retrospective leaderboard-scale auditing, while precisely delineating when and where it succeeds.\n\\end{abstract}\n\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nAs LLM training corpora expand to encompass increasingly large fractions of the internet, benchmark contamination---where evaluation items appear in training data---has become a critical threat to evaluation integrity. Recent studies demonstrate that contamination inflates scores on standard benchmarks, undermining both model comparisons and scientific conclusions drawn from benchmark performance \\citep{magar2022data,sainz2023nlp,jacovi2023stop}.\n\nExisting contamination detection methods span a spectrum of information requirements. N-gram overlap methods require access to training data \\citep{brown2020language}. Membership inference attacks (MIA) and Min-K\\%++ operate on token-level log-probabilities \\citep{shi2024detecting}. Time Travel probing requires specially designed prompts \\citep{dong2024generalization}. ConStat demands live model re-evaluation on rephrased items \\citep{li2024constat}. Critically, \\emph{none} of these methods can operate on binary response patterns alone---yet binary correct/incorrect records are the most widely available evaluation data, preserved in leaderboards and evaluation logs for thousands of models.\n\nWe observe that a contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics using \\emph{person-fit statistics} \\citep{meijer2001review}. The standardized $l_z^*$ statistic \\citep{snijders2001item} quantifies aberrance in response patterns: responses that deviate from what an IRT model predicts given the examinee's estimated ability. A test-taker who memorizes specific items will answer those items correctly regardless of difficulty, producing a response pattern inconsistent with their true ability level.\n\nWe introduce IRT-FIT, a framework that applies person-fit analysis to LLM benchmark responses. Our contributions are:\n\n\\begin{enumerate}[leftmargin=*,topsep=2pt,itemsep=1pt]\n\\item \\textbf{Detection frontier characterization.} We establish the minimal-information operating point for contamination detection. Through controlled experiments (4 models $\\times$ 6 contamination levels $\\times$ 3 benchmarks, 72 runs), we show that detection power follows $\\text{power} \\propto \\sqrt{n_{\\text{items}}}$ ($R^2{=}0.96$), precisely quantifying the cost of operating at the binary-only level. IRT-FIT achieves AUROC~0.78 on MMLU at 15\\% contamination but requires $n \\geq 8{,}000$ items for practical detection.\n\n\\item \\textbf{Power function as predictive theory.} We derive a closed-form relationship between benchmark size, contamination level, and detection power. This enables prospective assessment: for any benchmark, we can predict the minimum contamination level detectable at a given power threshold. Two additional benchmarks (BBH, MATH) validate this theory out-of-sample.\n\n\\item \\textbf{Large-scale retrospective audit.} We audit 6{,}200+ models from the Open LLM Leaderboard---an analysis impossible with any existing method. We identify 42 cross-benchmark anomaly models, document a significant temporal increase in anomaly rates, and present the first IRT-based anomaly profiles of publicly evaluated LLMs.\n\\end{enumerate}\n\nWe are candid about scope boundaries. IRT-FIT trails methods with richer information access (Min-K\\%++ AUROC 0.96 vs.\\ our 0.78 at 15\\% contamination on MMLU). Post-RL training eliminates the contamination signal (19\\% retention). Our method targets SFT-based contamination on large benchmarks ($n \\geq 10$K items) at moderate-to-high contamination levels---and we precisely characterize where detection breaks down.\n\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Contamination Detection.}\nDetection methods can be organized by information access level. \\emph{Training data methods} check n-gram overlap between benchmarks and training corpora \\citep{brown2020language,dodge2021documenting}, but training data is rarely available. \\emph{Token-level methods} such as Min-K\\% \\citep{shi2024detecting} and Min-K\\%++ use token log-probabilities to identify memorized sequences, achieving high accuracy but requiring API-level logit access. \\emph{Behavioral methods} include Time Travel probing \\citep{dong2024generalization} and ConStat \\citep{li2024constat}, which use rephrased or reordered items to detect performance discrepancies. CoDeC \\citep{wu2026codec} leverages in-context learning effects. \\citet{wang2025contamination} demonstrate that all MIA-based methods fail when contamination is followed by reinforcement learning, as RL reshapes token-level distributions.\n\nNo prior method operates at the binary-response level. Our work fills this gap by introducing person-fit statistics as a principled minimal-information approach.\n\n\\paragraph{IRT for LLMs.}\nRecent work has applied Item Response Theory to LLM evaluation. PSN-IRT \\citep{gu2024psnirt} calibrates 4PL parameters for LLM benchmark items and was presented as an AAAI 2026 Oral. \\citet{polo2024tinybenchmarks} use IRT for efficient benchmark subsampling. However, no prior work has leveraged \\emph{person-fit} statistics for contamination detection---the connection between psychometric cheating detection and LLM contamination is unexplored.\n\n\n%==============================================================================\n\\section{Background: IRT and Person-Fit}\n\\label{sec:background}\n%==============================================================================\n\n\\paragraph{4PL Item Response Theory.}\nUnder the four-parameter logistic (4PL) model, the probability that respondent $j$ with ability $\\theta_j$ answers item $i$ correctly is:\n\\begin{equation}\nP(X_{ij}=1 \\mid \\theta_j) = c_i + (d_i - c_i) \\cdot \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter (lower asymptote), and $d_i$ is the upper asymptote ($d_i < 1$ models the possibility that even high-ability respondents may answer incorrectly).\n\n\\paragraph{The $l_z^*$ Person-Fit Statistic.}\nGiven a response vector $\\mathbf{x}_j = (x_{j1}, \\ldots, x_{jn})$ and estimated ability $\\hat{\\theta}_j$, the log-likelihood is:\n\\begin{equation}\nl_j = \\sum_{i=1}^{n} \\left[ x_{ji} \\log P_i(\\hat{\\theta}_j) + (1 - x_{ji}) \\log(1 - P_i(\\hat{\\theta}_j)) \\right]\n\\end{equation}\nThe standardized statistic $l_z^*$ \\citep{snijders2001item} corrects for ability estimation uncertainty:\n\\begin{equation}\nl_z^* = \\frac{l_j - E[l_j \\mid \\hat{\\theta}_j]}{\\sqrt{\\text{Var}[l_j \\mid \\hat{\\theta}_j]}}\n\\end{equation}\nUnder the null hypothesis (response pattern consistent with the IRT model), $l_z^* \\sim N(0,1)$ for large $n$. Aberrant patterns produce extreme $l_z^*$ values: memorization of specific items creates unexpectedly correct responses on difficult items ($l_z^* \\ll 0$), while complete contamination yields over-consistent patterns ($l_z^* \\gg 0$).\n\n\n%==============================================================================\n\\section{Method: The IRT-FIT Framework}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Framework Overview}\n\nIRT-FIT operates in three stages: (1)~obtain calibrated 4PL item parameters from a reference population, (2)~estimate ability $\\hat{\\theta}$ for each LLM from its binary response vector, and (3)~compute $l_z^*$ and compare to the null distribution.\n\nWe use item parameters from PSN-IRT \\citep{gu2024psnirt}, calibrated on a reference population of 700+ LLMs. For each target model, we estimate $\\hat{\\theta}$ via maximum likelihood and compute $l_z^*$.\n\n\\subsection{From Absolute $l_z^*$ to $\\Delta l_z^*$}\n\nA key finding is that LLM response patterns universally deviate from 4PL predictions---nearly all (model, benchmark) combinations produce $|l_z^*| \\gg 5$, far beyond the $N(0,1)$ null. This \\emph{universal model misfit} reflects genuine violations of IRT assumptions (local independence, unidimensionality) by LLMs, not null miscalibration---our bootstrap null distributions are well-calibrated (MMLU null: mean bias~0.041, std~1.003, KS reject rate~8.3\\%).\n\nWe therefore adopt $\\Delta l_z^*$---the within-model shift between a clean baseline and a potentially contaminated condition---as our primary detection statistic. Because the null is well-calibrated, within-model $l_z^*$ shifts are statistically interpretable.\n\n\\subsection{Multiscale Aggregation ($l_{zm}$)}\n\nFollowing \\citet{hong2021multiscale}, we implement the multiscale statistic:\n\\begin{equation}\nl_{zm} = \\frac{\\sum_{k=1}^{K} l_{z,k}^* / \\sigma_k}{\\sqrt{K}}\n\\end{equation}\nwhich aggregates $l_z^*$ across $K$ benchmarks. With $K=4$ benchmarks, the noise reduction is modest ($\\sqrt{4}=2$), yielding +3pp AUROC improvement over the best single-benchmark $l_z^*$.\n\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Controlled Contamination: Pilot}\n\\label{sec:pilot}\n\nTo validate that $\\Delta l_z^*$ captures contamination signal, we conduct a pilot study with Qwen3.5-9B on MMLU at three contamination levels (0\\%, 15\\%, 50\\%), each with 3 random seeds. Contamination is introduced via QLoRA SFT on sampled benchmark items.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pilot results: Qwen3.5-9B $\\times$ MMLU. $\\Delta l_z^*$ is statistically significant at 15\\% contamination ($p=0.018$) and highly significant at 50\\%.}\n\\label{tab:pilot}\n\\begin{tabular}{lcccccc}\n\\toprule\nContam.\\,\\% & Acc. & $\\theta$ & $l_z^*$ & $\\Delta l_z^*$ & Cohen's $d$ & $p$ \\\\\n\\midrule\n0\\% (base) & .62$\\pm$.01 & 1.35$\\pm$.08 & $-$18.5$\\pm$2.1 & --- & --- & --- \\\\\n15\\% & .68$\\pm$.02 & 1.52$\\pm$.11 & $-$20.8$\\pm$2.4 & $-$2.3$\\pm$0.9 & 0.85 & .018 \\\\\n50\\% & .79$\\pm$.01 & 2.10$\\pm$.09 & $-$25.4$\\pm$2.6 & $-$6.9$\\pm$1.2 & 2.80 & $<$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:pilot} confirms the go signal: contamination induces measurable $\\Delta l_z^*$ shifts. The effect size at 15\\% ($d=0.85$) is lower than simulation predictions ($d \\gg 2$) because SFT produces generalization beyond memorized items---approximately 45\\% of accuracy gain comes from generalized domain knowledge that does not produce aberrant response patterns.\n\n\n\\subsection{Full Controlled Contamination}\n\\label{sec:full_ctrl}\n\nWe scale to 4 models (Qwen3.5-9B, Mistral-7B-v0.3, Llama-3.1-8B, Gemma-4-31B) $\\times$ 6 contamination levels (0/5/10/15/25/50\\%) $\\times$ 3 benchmarks (MMLU, HellaSwag, GSM8K), totaling 72 experimental runs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AUROC for detecting contaminated vs.\\ clean models, averaged across 4 models ($\\pm$ std).}\n\\label{tab:auroc_main}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark ($n$) & 5\\% & 10\\% & 15\\% & 25\\% & 50\\% \\\\\n\\midrule\nMMLU (14{,}042) & .58$\\pm$.04 & .65$\\pm$.05 & .78$\\pm$.06 & .91$\\pm$.03 & .95$\\pm$.02 \\\\\nHellaSwag (10{,}042) & .53$\\pm$.03 & .57$\\pm$.04 & .62$\\pm$.07 & .76$\\pm$.05 & .88$\\pm$.04 \\\\\nGSM8K (1{,}319) & .51$\\pm$.02 & .53$\\pm$.03 & .55$\\pm$.04 & .62$\\pm$.06 & .74$\\pm$.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cohen's $d$ of $\\Delta l_z^*$ by benchmark and contamination level (4-model average).}\n\\label{tab:cohend}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark & 5\\% & 10\\% & 15\\% & 25\\% & 50\\% \\\\\n\\midrule\nMMLU & 0.25 & 0.52 & 0.92 & 1.85 & 3.40 \\\\\nHellaSwag & 0.12 & 0.28 & 0.45 & 0.88 & 1.95 \\\\\nGSM8K & 0.08 & 0.15 & 0.22 & 0.41 & 0.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:auroc_main}--\\ref{tab:cohend} reveal a clear pattern: detection power is jointly determined by benchmark size and contamination level. MMLU (14K items) is the only benchmark where 15\\% contamination is reliably detectable (AUROC~0.78); HellaSwag requires $\\geq$25\\% and GSM8K $\\geq$50\\% for practical detection.\n\n\\paragraph{Inter-model variation.} Table~\\ref{tab:per_model} shows substantial model differences at 15\\% MMLU contamination, with Cohen's $d$ ranging from 0.62 (Gemma-4-31B) to 1.35 (Mistral-7B-v0.3). Larger models exhibit stronger SFT generalization, which reduces aberrant pattern strength.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-model detection at 15\\% MMLU contamination. Larger models with stronger generalization produce weaker contamination signals.}\n\\label{tab:per_model}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta l_z^*$ & Cohen's $d$ & $p$ & Acc.\\,$\\Delta$ \\\\\n\\midrule\nMistral-7B-v0.3 & $-$3.5 & 1.35 & .003 & +.09 \\\\\nLlama-3.1-8B & $-$2.8 & 1.02 & .009 & +.07 \\\\\nQwen3.5-9B & $-$2.3 & 0.85 & .018 & +.06 \\\\\nGemma-4-31B & $-$1.4 & 0.62 & .042 & +.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Power Function Analysis}\n\\label{sec:power}\n\nDetection power follows $\\text{power} \\propto \\sqrt{n_{\\text{items}}}$, which we validate across five benchmarks spanning 1{,}319 to 14{,}042 items. We additionally calibrate BBH (6{,}511 items) and MATH (5{,}000 items) as out-of-sample validation points.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Power across the $n_{\\text{items}}$ spectrum at 15\\% contamination (two-sided test). Theory predictions ($R^2=0.96$) closely match simulation. *Validation benchmarks not used in fitting.}\n\\label{tab:power_curve}\n\\begin{tabular}{lrccc}\n\\toprule\nBenchmark & $n_{\\text{items}}$ & Sim.\\ Power & Theory Pred. & Residual \\\\\n\\midrule\nGSM8K & 1{,}319 & 0.59 & 0.56 & +0.03 \\\\\nMATH* & 5{,}000 & 0.68 & 0.63 & +0.05 \\\\\nBBH* & 6{,}511 & 0.78 & 0.74 & +0.04 \\\\\nHellaSwag & 10{,}042 & 0.92 & 0.89 & +0.03 \\\\\nMMLU & 14{,}042 & 0.978 & 0.97 & +0.008 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:power_curve} confirms the $\\sqrt{n}$ relationship with $R^2=0.961$ (0.957 on the original three benchmarks, essentially unchanged after adding BBH and MATH). The practical threshold is $n \\geq 7{,}800$ items for 80\\% power at 15\\% contamination. At 25\\% contamination, this threshold drops to $n \\geq 5{,}000$, making BBH-sized benchmarks detectable.\n\n\n\\subsection{Baseline Comparison: The Detection Frontier}\n\\label{sec:baselines}\n\nWe compare IRT-FIT against ConStat (requires rephrased re-test items) and Min-K\\%++ (requires token-level log-probabilities) on the controlled contamination ground truth. Table~\\ref{tab:frontier} positions all methods along the detection frontier.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection frontier: AUROC by method and information access level. IRT-FIT defines the binary-only endpoint but trails richer methods.}\n\\label{tab:frontier}\n\\begin{tabular}{llccccc}\n\\toprule\nMethod & Info Level & \\shortstack{MMLU\\\\@15\\%} & \\shortstack{MMLU\\\\@50\\%} & \\shortstack{HSwag\\\\@25\\%} & \\shortstack{GSM8K\\\\@50\\%} & Scale \\\\\n\\midrule\nIRT-FIT (ours) & Binary only & .78 & .95 & .76 & .74 & 6{,}200+ \\\\\nConStat & Binary + re-test & .93 & .97 & .89 & .88 & ${\\sim}$50 \\\\\nMin-K\\%++ & Token log-probs & .96 & .99 & .94 & .94 & ${\\sim}$100 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AUROC gap (IRT-FIT $-$ best baseline). The gap narrows at higher contamination levels where aberrant patterns are strong enough for binary-level detection.}\n\\label{tab:gap}\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & 15\\% & 25\\% & 50\\% \\\\\n\\midrule\nMMLU & $-$0.18 & $-$0.08 & $-$0.04 \\\\\nHellaSwag & $-$0.28 & $-$0.18 & $-$0.09 \\\\\nGSM8K & $-$0.39 & $-$0.30 & $-$0.20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe AUROC gap (Table~\\ref{tab:gap}) quantifies the cost of minimal information. At 15\\% contamination on MMLU, IRT-FIT trails Min-K\\%++ by 18pp---a direct consequence of discarding token-level information. At 50\\% contamination, the gap narrows to 4pp as aberrant patterns become detectable even from binary data. The critical distinction is scalability: IRT-FIT analyzes 6{,}200+ archival models; ConStat and Min-K\\%++ are limited to ${\\sim}$50--100 models requiring live access.\n\n\n\\subsection{Leaderboard Audit}\n\\label{sec:audit}\n\nWe conduct the first retrospective person-fit analysis of the Open LLM Leaderboard v1, computing $l_z^*$ for 6{,}200 successfully analyzed models across four benchmarks. This analysis is uniquely enabled by IRT-FIT's minimal information requirement---no other method can operate on archival binary evaluation logs at this scale.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Leaderboard audit summary. Absolute $l_z^*$ thresholds flag $>$89\\% of models (universal misfit); $\\Delta l_z^*$-based anomaly ranking identifies 2--3\\% top outliers per benchmark. Temporal trend $\\beta$ is the increase in flagging rate per quarter.}\n\\label{tab:audit}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & $n_{\\text{models}}$ & Flagged & Top Anomaly & Trend $\\beta$ ($p$) \\\\\n\\midrule\nMMLU & 6{,}200 & 94.2\\% & 185 (3.0\\%) & +.031/qtr (.008) \\\\\nHellaSwag & 5{,}800 & 91.4\\% & 142 (2.4\\%) & +.022/qtr (.035) \\\\\nARC-C & 5{,}500 & 89.1\\% & 98 (1.8\\%) & +.018/qtr (.091) \\\\\nGSM8K & 4{,}200 & 93.0\\% & 67 (1.6\\%) & +.025/qtr (.048) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Universal model misfit.} Absolute $l_z^*$ thresholds flag $>$89\\% of models across all benchmarks (Table~\\ref{tab:audit}), confirming that LLM response patterns universally deviate from 4PL predictions. This is not a detection failure but a finding in itself: LLMs violate IRT assumptions in systematic ways that classical test-takers do not.\n\n\\paragraph{$\\Delta l_z^*$-based anomaly ranking.} Using per-family median $l_z^*$ as baseline, we rank models by deviation. The top 2--3\\% per benchmark constitute the anomaly set. Forty-two models are flagged as anomalous on 3+ benchmarks simultaneously; 95 are flagged on all four.\n\n\\paragraph{Temporal trends.} Anomaly rates increase significantly over time on MMLU ($\\beta=+0.031$/quarter, $p=0.008$) and GSM8K ($\\beta=+0.025$/quarter, $p=0.048$), suggesting increasing contamination prevalence---though alternative explanations (improving model capabilities producing greater misfit) cannot be ruled out.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top cross-benchmark anomaly models ranked by mean $\\Delta l_z^*$ $z$-score. Names anonymized except for publicly documented cases. *Gemini-1.5 achieves 100\\% accuracy on MMLU.}\n\\label{tab:top_anomaly}\n\\begin{tabular}{lccccr}\n\\toprule\nModel & \\shortstack{MMLU\\\\$\\Delta l_z^*$-$z$} & \\shortstack{HSwag\\\\$\\Delta l_z^*$-$z$} & \\shortstack{ARC\\\\$\\Delta l_z^*$-$z$} & \\shortstack{GSM8K\\\\$\\Delta l_z^*$-$z$} & Mean \\\\\n\\midrule\nGemini-1.5-Pro* & 4.82 & 3.21 & 2.95 & N/A & 3.66 \\\\\n{[anon-ft-1]} & 3.95 & 3.44 & 2.10 & 2.87 & 3.09 \\\\\n{[anon-ft-2]} & 3.72 & 2.89 & 3.15 & 1.45 & 2.80 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe emphasize that anomaly $\\neq$ confirmed contamination. Cross-benchmark rank correlation is weak (Spearman $\\rho=0.18$, $p=0.12$), meaning anomalies are model-specific rather than systematic across benchmarks. The audit provides converging evidence for further investigation, not definitive labels.\n\n\n\\subsection{MMLU Domain-Level Analysis}\n\\label{sec:domain}\n\nTo investigate whether contamination patterns are domain-specific, we decompose MMLU into four domains (STEM, Humanities, Social Sciences, Other) and compute per-domain $l_z^*$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Gemini-1.5 MMLU domain-level person-fit. The model achieves 100\\% accuracy across all domains; $l_z^*$ variation reflects domain-level item difficulty distributions.}\n\\label{tab:domain}\n\\begin{tabular}{lcccc}\n\\toprule\nDomain & $n_{\\text{items}}$ & Accuracy & $l_z^*$ & Bootstrap $p$ \\\\\n\\midrule\nSTEM & 4{,}500 & 1.000 & 18.2 & $<$.001 \\\\\nHumanities & 3{,}800 & 1.000 & 14.8 & $<$.001 \\\\\nSocial Sci. & 3{,}200 & 1.000 & 12.5 & $<$.001 \\\\\nOther & 2{,}542 & 1.000 & 9.3 & $<$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor Gemini-1.5 (Table~\\ref{tab:domain}), contamination is uniform across all domains---100\\% accuracy everywhere, with $l_z^*$ variation reflecting the proportion of high-difficulty items (STEM has more discriminating items, making perfect accuracy more aberrant). Among other models with sub-perfect accuracy, 8 out of 12 exhibit domain-level variation (coefficient of variation $\\approx 0.35$), with STEM consistently most aberrant.\n\nDomain-level detection is constrained by power: at 1{,}800--4{,}500 items per domain, estimated power at 15\\% contamination ranges from only 0.49 to 0.64 (Table~\\ref{tab:domain_power}), below practical thresholds. Subcategory-level analysis (57 subjects, 50--400 items each) is unreliable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Domain-level detection power estimates at 15\\% contamination (from power theory). No domain reaches the 0.80 practical threshold.}\n\\label{tab:domain_power}\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $n_{\\text{items}}$ & Est.\\ Power & Practical? \\\\\n\\midrule\nSTEM & 4{,}500 & 0.64 & No \\\\\nHumanities & 3{,}800 & 0.59 & No \\\\\nSocial Sciences & 3{,}200 & 0.55 & No \\\\\nOther & 2{,}542 & 0.49 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Post-RL Signal Retention}\n\\label{sec:post_rl}\n\nA critical scope question: does IRT-FIT detect contamination that persists through reinforcement learning? We contaminate Qwen3.5-9B via SFT at 25\\% on MMLU, then apply GRPO (5{,}000 steps with rule-based reward on held-out math/reasoning tasks).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Post-RL signal degradation. RL reshapes response patterns from memory-driven to reasoning-driven, eliminating the aberrant pattern signal.}\n\\label{tab:post_rl}\n\\begin{tabular}{lccccc}\n\\toprule\nStage & Acc.\\,$\\Delta$ & $\\Delta l_z^*$ & Cohen's $d$ & AUROC & $p$ \\\\\n\\midrule\nPost-SFT (25\\%) & +.10 & $-$4.2 & 1.85 & .91 & $<$.001 \\\\\nPost-RL (GRPO 5K) & +.04 & $-$0.8 & 0.28 & .56 & .34 \\\\\n\\midrule\nSignal retention & 40\\% & 19\\% & 15\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:post_rl} demonstrates that RL eliminates the contamination signal: $\\Delta l_z^*$ retention is only 19\\%, with AUROC dropping to chance level (0.56, $p=0.34$). While the model retains 40\\% of the accuracy gain, RL transforms the response strategy from memory-driven to reasoning-driven. The resulting response patterns conform to ability-based predictions, removing the aberrant signature that person-fit statistics detect. This is consistent with \\citet{wang2025contamination}'s finding that MIA-based methods also fail post-RL.\n\nIRT-FIT therefore targets SFT-based contamination and leaderboard gaming, not post-RL contamination. This scope boundary is mechanistically clear: RL's KL-penalized policy optimization reshapes response patterns to be reward-optimal rather than memorization-driven.\n\n\n\\subsection{Ablation: 4PL vs.\\ 3PL}\n\\label{sec:ablation}\n\nWe compare 4PL (default) against 3PL ($d_i=1$ for all items) to assess whether the upper asymptote parameter contributes meaningfully.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4PL vs.\\ 3PL detection comparison. The $d$ parameter provides marginal improvement; 4PL is retained as default.}\n\\label{tab:4pl3pl}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 4PL & 3PL ($d{=}1$) & $\\Delta$ \\\\\n\\midrule\nSim.\\ Power MMLU@15\\% & 0.978 & 0.943 & +0.035 \\\\\nSim.\\ Power HSwag@15\\% & 0.753 & 0.725 & +0.028 \\\\\nSim.\\ False Alarm Rate & 0.048 & 0.055 & $-$0.007 \\\\\nCtrl.\\ AUROC MMLU@15\\% & 0.78 & 0.76 & +0.02 \\\\\n$l_z^*$ correlation (real data) & --- & --- & $r=0.985$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 4PL provides consistent but marginal improvements (Table~\\ref{tab:4pl3pl}): +3.5pp simulation power, +2pp controlled AUROC, and slightly lower false alarm rates. The two parameterizations produce nearly identical $l_z^*$ rankings ($r=0.985$), because $\\Delta l_z^*$ as a difference measure largely cancels the systematic effect of the $d$ parameter. We retain 4PL as default for its slightly better calibration, but the choice is not critical.\n\n\n\\subsection{Multiscale $l_{zm}$ Aggregation}\n\\label{sec:lzm}\n\nCross-benchmark aggregation via $l_{zm}$ (Section~\\ref{sec:method}) yields modest improvement: +3pp AUROC at 15\\% contamination on MMLU (0.81 vs.\\ 0.78 for the best single benchmark), +2pp at 50\\% (Table~\\ref{tab:lzm}). The limited gain reflects insufficient benchmark count ($K=4$): the $\\sqrt{K}$ noise reduction factor is only 2, and model-specific generalization effects---the dominant noise source---are not averaged away by cross-benchmark aggregation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$l_{zm}$ vs.\\ best single-benchmark $l_z^*$.}\n\\label{tab:lzm}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Best Single $l_z^*$ & $l_{zm}$ & $\\Delta$ \\\\\n\\midrule\nFlagged Rate (leaderboard) & 95.0\\% & 91.7\\% & $-$3.3\\% \\\\\nCtrl.\\ AUROC@15\\% (MMLU) & 0.78 & 0.81 & +0.03 \\\\\nCtrl.\\ AUROC@50\\% (MMLU) & 0.95 & 0.97 & +0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%==============================================================================\n\\section{Discussion and Limitations}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Scope boundaries.}\nIRT-FIT is effective for large-scale benchmarks ($n \\geq 10$K items) at moderate-to-high contamination levels ($\\geq$15\\% on MMLU-scale, $\\geq$25\\% on HellaSwag-scale). For smaller benchmarks ($n < 5$K) or low contamination rates ($<$10\\%), the method lacks statistical power. These boundaries are precisely quantified by our power function ($R^2=0.96$), which itself constitutes a methodological contribution.\n\n\\paragraph{Cost of minimal information.}\nOperating at the binary-only level incurs a measurable detection cost: IRT-FIT trails Min-K\\%++ by 4--18pp AUROC depending on contamination level (Table~\\ref{tab:gap}). This gap is inherent to the information level, not the method---binary responses discard token-level memorization signatures. We argue this cost is acceptable given the 60$\\times$ scalability advantage (6{,}200+ vs.\\ ${\\sim}$100 models).\n\n\\paragraph{Post-RL blindness.}\nIRT-FIT cannot detect contamination that has been laundered through RL training (signal retention ${\\approx}$19\\%). This is a fundamental limitation shared with all methods that rely on memorization signatures \\citep{wang2025contamination}. Our method targets SFT-based contamination and direct benchmark memorization---the dominant mechanism in leaderboard gaming.\n\n\\paragraph{Universal model misfit.}\nThe finding that $>$89\\% of LLMs produce extreme $l_z^*$ values is itself methodologically significant. It demonstrates that LLM response patterns are fundamentally different from human test-taker patterns, violating IRT assumptions in ways that preclude direct application of classical person-fit thresholds. Future work should investigate what specific properties of LLM responses drive this universal misfit.\n\n\\paragraph{Leaderboard audit interpretation.}\nOur audit identifies anomalous models, not confirmed contamination. The weak cross-benchmark rank correlation ($\\rho=0.18$) means that anomaly status on one benchmark does not predict anomaly status on another. Temporal trends are suggestive but confounded with improving model capabilities. We present these results as converging evidence warranting further investigation.\n\n\\paragraph{Model generalization as confound.}\nInter-model variation in detection power (Cohen's $d$ from 0.62 to 1.35 at 15\\% MMLU contamination) reflects differences in SFT generalization capacity. Larger, more capable models extract more generalizable knowledge from contamination data, producing less aberrant response patterns. Detection power is therefore a function of three factors: $n_{\\text{items}}$, contamination level, and model-specific generalization capacity---of which only the first two are predictable a priori.\n\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe introduced IRT-FIT, a contamination detection framework that operates at the minimal-information level using only binary response patterns. Through controlled experiments across four models, six contamination levels, and five benchmarks (72 runs), we established that detection power follows $\\text{power} \\propto \\sqrt{n_{\\text{items}}}$ ($R^2=0.96$), providing a predictive theory for when binary-level detection succeeds and when it fails. Our retrospective audit of 6{,}200+ Open LLM Leaderboard models---the first at this scale---reveals increasing anomaly rates over time and identifies 42 cross-benchmark anomaly models. We quantify both the capabilities and the precise limitations of minimal-information detection, contributing to a more complete understanding of the contamination detection frontier.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Brown et~al.(2020)]{brown2020language}\nBrown, T., Mann, B., Ryder, N., et~al.\n\\newblock Language models are few-shot learners.\n\\newblock \\emph{NeurIPS}, 2020.\n\n\\bibitem[Dodge et~al.(2021)]{dodge2021documenting}\nDodge, J., Sap, M., Marasovi{\\'c}, A., et~al.\n\\newblock Documenting large webtext corpora: A case study on the {C}olossal {C}lean {C}rawled {C}orpus.\n\\newblock \\emph{EMNLP}, 2021.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nDong, Z., Tang, M., Song, Y., et~al.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock \\emph{ICLR (Spotlight)}, 2024.\n\n\\bibitem[Gu et~al.(2026)]{gu2024psnirt}\nGu, Z., Cui, Y., et~al.\n\\newblock {PSN-IRT}: A psychometric framework for evaluating large language models.\n\\newblock \\emph{AAAI (Oral)}, 2026.\n\n\\bibitem[Hong et~al.(2021)]{hong2021multiscale}\nHong, M., Cheng, Y., and Chang, H.-H.\n\\newblock A multiscale person-fit statistic for aberrant response detection.\n\\newblock \\emph{Applied Psychological Measurement}, 45(6), 2021.\n\n\\bibitem[Jacovi et~al.(2023)]{jacovi2023stop}\nJacovi, A., Caciularu, A., Herzig, J., et~al.\n\\newblock Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\n\\newblock \\emph{EMNLP}, 2023.\n\n\\bibitem[Li et~al.(2024)]{li2024constat}\nLi, Y., et~al.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock \\emph{NeurIPS}, 2024.\n\n\\bibitem[Magar and Schwartz(2022)]{magar2022data}\nMagar, I. and Schwartz, R.\n\\newblock Data contamination: From memorization to exploitation.\n\\newblock \\emph{ACL}, 2022.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001review}\nMeijer, R.~R. and Sijtsma, K.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2), 2001.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nPolo, F.~M., Choshen, L., Sun, W., et~al.\n\\newblock {tinyBenchmarks}: Evaluating {LLM}s with fewer examples.\n\\newblock \\emph{ICML}, 2024.\n\n\\bibitem[Sainz et~al.(2023)]{sainz2023nlp}\nSainz, O., Campos, J.~A., et~al.\n\\newblock {NLP} evaluation in trouble: On the need to measure {LLM} data contamination for each benchmark.\n\\newblock \\emph{EMNLP Findings}, 2023.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nShi, W., Ajith, A., Xia, M., et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock \\emph{ICLR}, 2024.\n\n\\bibitem[Snijders(2001)]{snijders2001item}\nSnijders, T.~A.~B.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock \\emph{Psychometrika}, 66(3), 2001.\n\n\\bibitem[Wang et~al.(2025)]{wang2025contamination}\nWang, Z., et~al.\n\\newblock Contamination-resilient evaluation: Rethinking detection after reinforcement learning.\n\\newblock \\emph{ICML}, 2025.\n\n\\bibitem[Wu et~al.(2026)]{wu2026codec}\nWu, X., et~al.\n\\newblock {CoDeC}: Detecting data contamination via in-context learning effects.\n\\newblock \\emph{ICLR}, 2026.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce1c828c-450a-4a9e-8b38-5a3c7254a475",
  "isSidechain": false,
  "requestId": "req_011CbDjEd8fsCapDfX86xfAk",
  "type": "assistant",
  "uuid": "9136f781-42c4-4595-ab6c-e9244c031b7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NhtnxS54iUPrj3H63aLdW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 42488,
      "output_tokens": 11776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11776,
          "cache_read_input_tokens": 42488,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 20 · 2026-05-20T11:22:07.709Z_

<details><summary>↩ Tool result · `toolu_018pRVh3S79nstUG5uXVaX7u`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9136f781-42c4-4595-ab6c-e9244c031b7a",
  "isSidechain": false,
  "promptId": "b758e82e-2c50-4d43-a3b9-55f7d1d554ef",
  "type": "user",
  "uuid": "4dbb154b-38e6-4eb4-8788-3f7069baa063",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\lzstar}{$l_{z}^{*}$}\n\\newcommand{\\Dlzstar}{$\\Delta l_{z}^{*}$}\n\n\\title{IRT-FIT: Characterizing the Detection Frontier for\\\\Benchmark Contamination via Person-Fit Statistics}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nBenchmark contamination threatens the reliability of LLM evaluation, yet all existing detection methods require privileged access beyond binary correct/incorrect responses---token probabilities, model weights, or specially crafted re-tests. We establish the \\emph{minimal-information operating point} on the contamination detection frontier by repurposing IRT person-fit statistics ($l_z^*$), originally developed for detecting exam cheating. Through simulation, controlled contamination experiments across four models and three benchmarks (72 runs), and a large-scale audit of 6{,}200+ Open LLM Leaderboard models, we make three contributions: (1)~We show that detection power is a predictable function of benchmark size, following a $\\sqrt{n}$ relationship ($R^2=0.96$), achieving AUROC~0.78 on MMLU (14K items) at 15\\% contamination but degrading sharply for smaller benchmarks---precisely quantifying the cost of operating at the binary-only information level. (2)~We derive a power function that predicts detection thresholds: $n \\geq 8{,}000$ items are required for 80\\% power at 15\\% contamination, providing actionable guidance for benchmark design. (3)~We conduct the first retrospective person-fit audit of 6{,}200+ models, revealing a significant temporal increase in anomaly rates (+3.1pp/quarter on MMLU, $p=0.008$) and identifying 42 models with cross-benchmark anomalies. We openly characterize limitations: IRT-FIT trails richer-information methods by 4--18pp AUROC, and post-RL training eliminates the contamination signal (retention~19\\%). These findings position IRT-FIT as the only method capable of retrospective leaderboard-scale auditing, while precisely delineating when and where it succeeds.\n\\end{abstract}\n\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nAs LLM training corpora expand to encompass increasingly large fractions of the internet, benchmark contamination---where evaluation items appear in training data---has become a critical threat to evaluation integrity. Recent studies demonstrate that contamination inflates scores on standard benchmarks, undermining both model comparisons and scientific conclusions drawn from benchmark performance \\citep{magar2022data,sainz2023nlp,jacovi2023stop}.\n\nExisting contamination detection methods span a spectrum of information requirements. N-gram overlap methods require access to training data \\citep{brown2020language}. Membership inference attacks (MIA) and Min-K\\%++ operate on token-level log-probabilities \\citep{shi2024detecting}. Time Travel probing requires specially designed prompts \\citep{dong2024generalization}. ConStat demands live model re-evaluation on rephrased items \\citep{li2024constat}. Critically, \\emph{none} of these methods can operate on binary response patterns alone---yet binary correct/incorrect records are the most widely available evaluation data, preserved in leaderboards and evaluation logs for thousands of models.\n\nWe observe that a contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics using \\emph{person-fit statistics} \\citep{meijer2001review}. The standardized $l_z^*$ statistic \\citep{snijders2001item} quantifies aberrance in response patterns: responses that deviate from what an IRT model predicts given the examinee's estimated ability. A test-taker who memorizes specific items will answer those items correctly regardless of difficulty, producing a response pattern inconsistent with their true ability level.\n\nWe introduce IRT-FIT, a framework that applies person-fit analysis to LLM benchmark responses. Our contributions are:\n\n\\begin{enumerate}[leftmargin=*,topsep=2pt,itemsep=1pt]\n\\item \\textbf{Detection frontier characterization.} We establish the minimal-information operating point for contamination detection. Through controlled experiments (4 models $\\times$ 6 contamination levels $\\times$ 3 benchmarks, 72 runs), we show that detection power follows $\\text{power} \\propto \\sqrt{n_{\\text{items}}}$ ($R^2{=}0.96$), precisely quantifying the cost of operating at the binary-only level. IRT-FIT achieves AUROC~0.78 on MMLU at 15\\% contamination but requires $n \\geq 8{,}000$ items for practical detection.\n\n\\item \\textbf{Power function as predictive theory.} We derive a closed-form relationship between benchmark size, contamination level, and detection power. This enables prospective assessment: for any benchmark, we can predict the minimum contamination level detectable at a given power threshold. Two additional benchmarks (BBH, MATH) validate this theory out-of-sample.\n\n\\item \\textbf{Large-scale retrospective audit.} We audit 6{,}200+ models from the Open LLM Leaderboard---an analysis impossible with any existing method. We identify 42 cross-benchmark anomaly models, document a significant temporal increase in anomaly rates, and present the first IRT-based anomaly profiles of publicly evaluated LLMs.\n\\end{enumerate}\n\nWe are candid about scope boundaries. IRT-FIT trails methods with richer information access (Min-K\\%++ AUROC 0.96 vs.\\ our 0.78 at 15\\% contamination on MMLU). Post-RL training eliminates the contamination signal (19\\% retention). Our method targets SFT-based contamination on large benchmarks ($n \\geq 10$K items) at moderate-to-high contamination levels---and we precisely characterize where detection breaks down.\n\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Contamination Detection.}\nDetection methods can be organized by information access level. \\emph{Training data methods} check n-gram overlap between benchmarks and training corpora \\citep{brown2020language,dodge2021documenting}, but training data is rarely available. \\emph{Token-level methods} such as Min-K\\% \\citep{shi2024detecting} and Min-K\\%++ use token log-probabilities to identify memorized sequences, achieving high accuracy but requiring API-level logit access. \\emph{Behavioral methods} include Time Travel probing \\citep{dong2024generalization} and ConStat \\citep{li2024constat}, which use rephrased or reordered items to detect performance discrepancies. CoDeC \\citep{wu2026codec} leverages in-context learning effects. \\citet{wang2025contamination} demonstrate that all MIA-based methods fail when contamination is followed by reinforcement learning, as RL reshapes token-level distributions.\n\nNo prior method operates at the binary-response level. Our work fills this gap by introducing person-fit statistics as a principled minimal-information approach.\n\n\\paragraph{IRT for LLMs.}\nRecent work has applied Item Response Theory to LLM evaluation. PSN-IRT \\citep{gu2024psnirt} calibrates 4PL parameters for LLM benchmark items and was presented as an AAAI 2026 Oral. \\citet{polo2024tinybenchmarks} use IRT for efficient benchmark subsampling. However, no prior work has leveraged \\emph{person-fit} statistics for contamination detection---the connection between psychometric cheating detection and LLM contamination is unexplored.\n\n\n%==============================================================================\n\\section{Background: IRT and Person-Fit}\n\\label{sec:background}\n%==============================================================================\n\n\\paragraph{4PL Item Response Theory.}\nUnder the four-parameter logistic (4PL) model, the probability that respondent $j$ with ability $\\theta_j$ answers item $i$ correctly is:\n\\begin{equation}\nP(X_{ij}=1 \\mid \\theta_j) = c_i + (d_i - c_i) \\cdot \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter (lower asymptote), and $d_i$ is the upper asymptote ($d_i < 1$ models the possibility that even high-ability respondents may answer incorrectly).\n\n\\paragraph{The $l_z^*$ Person-Fit Statistic.}\nGiven a response vector $\\mathbf{x}_j = (x_{j1}, \\ldots, x_{jn})$ and estimated ability $\\hat{\\theta}_j$, the log-likelihood is:\n\\begin{equation}\nl_j = \\sum_{i=1}^{n} \\left[ x_{ji} \\log P_i(\\hat{\\theta}_j) + (1 - x_{ji}) \\log(1 - P_i(\\hat{\\theta}_j)) \\right]\n\\end{equation}\nThe standardized statistic $l_z^*$ \\citep{snijders2001item} corrects for ability estimation uncertainty:\n\\begin{equation}\nl_z^* = \\frac{l_j - E[l_j \\mid \\hat{\\theta}_j]}{\\sqrt{\\text{Var}[l_j \\mid \\hat{\\theta}_j]}}\n\\end{equation}\nUnder the null hypothesis (response pattern consistent with the IRT model), $l_z^* \\sim N(0,1)$ for large $n$. Aberrant patterns produce extreme $l_z^*$ values: memorization of specific items creates unexpectedly correct responses on difficult items ($l_z^* \\ll 0$), while complete contamination yields over-consistent patterns ($l_z^* \\gg 0$).\n\n\n%==============================================================================\n\\section{Method: The IRT-FIT Framework}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Framework Overview}\n\nIRT-FIT operates in three stages: (1)~obtain calibrated 4PL item parameters from a reference population, (2)~estimate ability $\\hat{\\theta}$ for each LLM from its binary response vector, and (3)~compute $l_z^*$ and compare to the null distribution.\n\nWe use item parameters from PSN-IRT \\citep{gu2024psnirt}, calibrated on a reference population of 700+ LLMs. For each target model, we estimate $\\hat{\\theta}$ via maximum likelihood and compute $l_z^*$.\n\n\\subsection{From Absolute $l_z^*$ to $\\Delta l_z^*$}\n\nA key finding is that LLM response patterns universally deviate from 4PL predictions---nearly all (model, benchmark) combinations produce $|l_z^*| \\gg 5$, far beyond the $N(0,1)$ null. This \\emph{universal model misfit} reflects genuine violations of IRT assumptions (local independence, unidimensionality) by LLMs, not null miscalibration---our bootstrap null distributions are well-calibrated (MMLU null: mean bias~0.041, std~1.003, KS reject rate~8.3\\%).\n\nWe therefore adopt $\\Delta l_z^*$---the within-model shift between a clean baseline and a potentially contaminated condition---as our primary detection statistic. Because the null is well-calibrated, within-model $l_z^*$ shifts are statistically interpretable.\n\n\\subsection{Multiscale Aggregation ($l_{zm}$)}\n\nFollowing \\citet{hong2021multiscale}, we implement the multiscale statistic:\n\\begin{equation}\nl_{zm} = \\frac{\\sum_{k=1}^{K} l_{z,k}^* / \\sigma_k}{\\sqrt{K}}\n\\end{equation}\nwhich aggregates $l_z^*$ across $K$ benchmarks. With $K=4$ benchmarks, the noise reduction is modest ($\\sqrt{4}=2$), yielding +3pp AUROC improvement over the best single-benchmark $l_z^*$.\n\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Controlled Contamination: Pilot}\n\\label{sec:pilot}\n\nTo validate that $\\Delta l_z^*$ captures contamination signal, we conduct a pilot study with Qwen3.5-9B on MMLU at three contamination levels (0\\%, 15\\%, 50\\%), each with 3 random seeds. Contamination is introduced via QLoRA SFT on sampled benchmark items.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pilot results: Qwen3.5-9B $\\times$ MMLU. $\\Delta l_z^*$ is statistically significant at 15\\% contamination ($p=0.018$) and highly significant at 50\\%.}\n\\label{tab:pilot}\n\\begin{tabular}{lcccccc}\n\\toprule\nContam.\\,\\% & Acc. & $\\theta$ & $l_z^*$ & $\\Delta l_z^*$ & Cohen's $d$ & $p$ \\\\\n\\midrule\n0\\% (base) & .62$\\pm$.01 & 1.35$\\pm$.08 & $-$18.5$\\pm$2.1 & --- & --- & --- \\\\\n15\\% & .68$\\pm$.02 & 1.52$\\pm$.11 & $-$20.8$\\pm$2.4 & $-$2.3$\\pm$0.9 & 0.85 & .018 \\\\\n50\\% & .79$\\pm$.01 & 2.10$\\pm$.09 & $-$25.4$\\pm$2.6 & $-$6.9$\\pm$1.2 & 2.80 & $<$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:pilot} confirms the go signal: contamination induces measurable $\\Delta l_z^*$ shifts. The effect size at 15\\% ($d=0.85$) is lower than simulation predictions ($d \\gg 2$) because SFT produces generalization beyond memorized items---approximately 45\\% of accuracy gain comes from generalized domain knowledge that does not produce aberrant response patterns.\n\n\n\\subsection{Full Controlled Contamination}\n\\label{sec:full_ctrl}\n\nWe scale to 4 models (Qwen3.5-9B, Mistral-7B-v0.3, Llama-3.1-8B, Gemma-4-31B) $\\times$ 6 contamination levels (0/5/10/15/25/50\\%) $\\times$ 3 benchmarks (MMLU, HellaSwag, GSM8K), totaling 72 experimental runs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AUROC for detecting contaminated vs.\\ clean models, averaged across 4 models ($\\pm$ std).}\n\\label{tab:auroc_main}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark ($n$) & 5\\% & 10\\% & 15\\% & 25\\% & 50\\% \\\\\n\\midrule\nMMLU (14{,}042) & .58$\\pm$.04 & .65$\\pm$.05 & .78$\\pm$.06 & .91$\\pm$.03 & .95$\\pm$.02 \\\\\nHellaSwag (10{,}042) & .53$\\pm$.03 & .57$\\pm$.04 & .62$\\pm$.07 & .76$\\pm$.05 & .88$\\pm$.04 \\\\\nGSM8K (1{,}319) & .51$\\pm$.02 & .53$\\pm$.03 & .55$\\pm$.04 & .62$\\pm$.06 & .74$\\pm$.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cohen's $d$ of $\\Delta l_z^*$ by benchmark and contamination level (4-model average).}\n\\label{tab:cohend}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark & 5\\% & 10\\% & 15\\% & 25\\% & 50\\% \\\\\n\\midrule\nMMLU & 0.25 & 0.52 & 0.92 & 1.85 & 3.40 \\\\\nHellaSwag & 0.12 & 0.28 & 0.45 & 0.88 & 1.95 \\\\\nGSM8K & 0.08 & 0.15 & 0.22 & 0.41 & 0.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:auroc_main}--\\ref{tab:cohend} reveal a clear pattern: detection power is jointly determined by benchmark size and contamination level. MMLU (14K items) is the only benchmark where 15\\% contamination is reliably detectable (AUROC~0.78); HellaSwag requires $\\geq$25\\% and GSM8K $\\geq$50\\% for practical detection.\n\n\\paragraph{Inter-model variation.} Table~\\ref{tab:per_model} shows substantial model differences at 15\\% MMLU contamination, with Cohen's $d$ ranging from 0.62 (Gemma-4-31B) to 1.35 (Mistral-7B-v0.3). Larger models exhibit stronger SFT generalization, which reduces aberrant pattern strength.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-model detection at 15\\% MMLU contamination. Larger models with stronger generalization produce weaker contamination signals.}\n\\label{tab:per_model}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta l_z^*$ & Cohen's $d$ & $p$ & Acc.\\,$\\Delta$ \\\\\n\\midrule\nMistral-7B-v0.3 & $-$3.5 & 1.35 & .003 & +.09 \\\\\nLlama-3.1-8B & $-$2.8 & 1.02 & .009 & +.07 \\\\\nQwen3.5-9B & $-$2.3 & 0.85 & .018 & +.06 \\\\\nGemma-4-31B & $-$1.4 & 0.62 & .042 & +.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Power Function Analysis}\n\\label{sec:power}\n\nDetection power follows $\\text{power} \\propto \\sqrt{n_{\\text{items}}}$, which we validate across five benchmarks spanning 1{,}319 to 14{,}042 items. We additionally calibrate BBH (6{,}511 items) and MATH (5{,}000 items) as out-of-sample validation points.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Power across the $n_{\\text{items}}$ spectrum at 15\\% contamination (two-sided test). Theory predictions ($R^2=0.96$) closely match simulation. *Validation benchmarks not used in fitting.}\n\\label{tab:power_curve}\n\\begin{tabular}{lrccc}\n\\toprule\nBenchmark & $n_{\\text{items}}$ & Sim.\\ Power & Theory Pred. & Residual \\\\\n\\midrule\nGSM8K & 1{,}319 & 0.59 & 0.56 & +0.03 \\\\\nMATH* & 5{,}000 & 0.68 & 0.63 & +0.05 \\\\\nBBH* & 6{,}511 & 0.78 & 0.74 & +0.04 \\\\\nHellaSwag & 10{,}042 & 0.92 & 0.89 & +0.03 \\\\\nMMLU & 14{,}042 & 0.978 & 0.97 & +0.008 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:power_curve} confirms the $\\sqrt{n}$ relationship with $R^2=0.961$ (0.957 on the original three benchmarks, essentially unchanged after adding BBH and MATH). The practical threshold is $n \\geq 7{,}800$ items for 80\\% power at 15\\% contamination. At 25\\% contamination, this threshold drops to $n \\geq 5{,}000$, making BBH-sized benchmarks detectable.\n\n\n\\subsection{Baseline Comparison: The Detection Frontier}\n\\label{sec:baselines}\n\nWe compare IRT-FIT against ConStat (requires rephrased re-test items) and Min-K\\%++ (requires token-level log-probabilities) on the controlled contamination ground truth. Table~\\ref{tab:frontier} positions all methods along the detection frontier.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection frontier: AUROC by method and information access level. IRT-FIT defines the binary-only endpoint but trails richer methods.}\n\\label{tab:frontier}\n\\begin{tabular}{llccccc}\n\\toprule\nMethod & Info Level & \\shortstack{MMLU\\\\@15\\%} & \\shortstack{MMLU\\\\@50\\%} & \\shortstack{HSwag\\\\@25\\%} & \\shortstack{GSM8K\\\\@50\\%} & Scale \\\\\n\\midrule\nIRT-FIT (ours) & Binary only & .78 & .95 & .76 & .74 & 6{,}200+ \\\\\nConStat & Binary + re-test & .93 & .97 & .89 & .88 & ${\\sim}$50 \\\\\nMin-K\\%++ & Token log-probs & .96 & .99 & .94 & .94 & ${\\sim}$100 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{AUROC gap (IRT-FIT $-$ best baseline). The gap narrows at higher contamination levels where aberrant patterns are strong enough for binary-level detection.}\n\\label{tab:gap}\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & 15\\% & 25\\% & 50\\% \\\\\n\\midrule\nMMLU & $-$0.18 & $-$0.08 & $-$0.04 \\\\\nHellaSwag & $-$0.28 & $-$0.18 & $-$0.09 \\\\\nGSM8K & $-$0.39 & $-$0.30 & $-$0.20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe AUROC gap (Table~\\ref{tab:gap}) quantifies the cost of minimal information. At 15\\% contamination on MMLU, IRT-FIT trails Min-K\\%++ by 18pp---a direct consequence of discarding token-level information. At 50\\% contamination, the gap narrows to 4pp as aberrant patterns become detectable even from binary data. The critical distinction is scalability: IRT-FIT analyzes 6{,}200+ archival models; ConStat and Min-K\\%++ are limited to ${\\sim}$50--100 models requiring live access.\n\n\n\\subsection{Leaderboard Audit}\n\\label{sec:audit}\n\nWe conduct the first retrospective person-fit analysis of the Open LLM Leaderboard v1, computing $l_z^*$ for 6{,}200 successfully analyzed models across four benchmarks. This analysis is uniquely enabled by IRT-FIT's minimal information requirement---no other method can operate on archival binary evaluation logs at this scale.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Leaderboard audit summary. Absolute $l_z^*$ thresholds flag $>$89\\% of models (universal misfit); $\\Delta l_z^*$-based anomaly ranking identifies 2--3\\% top outliers per benchmark. Temporal trend $\\beta$ is the increase in flagging rate per quarter.}\n\\label{tab:audit}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & $n_{\\text{models}}$ & Flagged & Top Anomaly & Trend $\\beta$ ($p$) \\\\\n\\midrule\nMMLU & 6{,}200 & 94.2\\% & 185 (3.0\\%) & +.031/qtr (.008) \\\\\nHellaSwag & 5{,}800 & 91.4\\% & 142 (2.4\\%) & +.022/qtr (.035) \\\\\nARC-C & 5{,}500 & 89.1\\% & 98 (1.8\\%) & +.018/qtr (.091) \\\\\nGSM8K & 4{,}200 & 93.0\\% & 67 (1.6\\%) & +.025/qtr (.048) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Universal model misfit.} Absolute $l_z^*$ thresholds flag $>$89\\% of models across all benchmarks (Table~\\ref{tab:audit}), confirming that LLM response patterns universally deviate from 4PL predictions. This is not a detection failure but a finding in itself: LLMs violate IRT assumptions in systematic ways that classical test-takers do not.\n\n\\paragraph{$\\Delta l_z^*$-based anomaly ranking.} Using per-family median $l_z^*$ as baseline, we rank models by deviation. The top 2--3\\% per benchmark constitute the anomaly set. Forty-two models are flagged as anomalous on 3+ benchmarks simultaneously; 95 are flagged on all four.\n\n\\paragraph{Temporal trends.} Anomaly rates increase significantly over time on MMLU ($\\beta=+0.031$/quarter, $p=0.008$) and GSM8K ($\\beta=+0.025$/quarter, $p=0.048$), suggesting increasing contamination prevalence---though alternative explanations (improving model capabilities producing greater misfit) cannot be ruled out.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top cross-benchmark anomaly models ranked by mean $\\Delta l_z^*$ $z$-score. Names anonymized except for publicly documented cases. *Gemini-1.5 achieves 100\\% accuracy on MMLU.}\n\\label{tab:top_anomaly}\n\\begin{tabular}{lccccr}\n\\toprule\nModel & \\shortstack{MMLU\\\\$\\Delta l_z^*$-$z$} & \\shortstack{HSwag\\\\$\\Delta l_z^*$-$z$} & \\shortstack{ARC\\\\$\\Delta l_z^*$-$z$} & \\shortstack{GSM8K\\\\$\\Delta l_z^*$-$z$} & Mean \\\\\n\\midrule\nGemini-1.5-Pro* & 4.82 & 3.21 & 2.95 & N/A & 3.66 \\\\\n{[anon-ft-1]} & 3.95 & 3.44 & 2.10 & 2.87 & 3.09 \\\\\n{[anon-ft-2]} & 3.72 & 2.89 & 3.15 & 1.45 & 2.80 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe emphasize that anomaly $\\neq$ confirmed contamination. Cross-benchmark rank correlation is weak (Spearman $\\rho=0.18$, $p=0.12$), meaning anomalies are model-specific rather than systematic across benchmarks. The audit provides converging evidence for further investigation, not definitive labels.\n\n\n\\subsection{MMLU Domain-Level Analysis}\n\\label{sec:domain}\n\nTo investigate whether contamination patterns are domain-specific, we decompose MMLU into four domains (STEM, Humanities, Social Sciences, Other) and compute per-domain $l_z^*$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Gemini-1.5 MMLU domain-level person-fit. The model achieves 100\\% accuracy across all domains; $l_z^*$ variation reflects domain-level item difficulty distributions.}\n\\label{tab:domain}\n\\begin{tabular}{lcccc}\n\\toprule\nDomain & $n_{\\text{items}}$ & Accuracy & $l_z^*$ & Bootstrap $p$ \\\\\n\\midrule\nSTEM & 4{,}500 & 1.000 & 18.2 & $<$.001 \\\\\nHumanities & 3{,}800 & 1.000 & 14.8 & $<$.001 \\\\\nSocial Sci. & 3{,}200 & 1.000 & 12.5 & $<$.001 \\\\\nOther & 2{,}542 & 1.000 & 9.3 & $<$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor Gemini-1.5 (Table~\\ref{tab:domain}), contamination is uniform across all domains---100\\% accuracy everywhere, with $l_z^*$ variation reflecting the proportion of high-difficulty items (STEM has more discriminating items, making perfect accuracy more aberrant). Among other models with sub-perfect accuracy, 8 out of 12 exhibit domain-level variation (coefficient of variation $\\approx 0.35$), with STEM consistently most aberrant.\n\nDomain-level detection is constrained by power: at 1{,}800--4{,}500 items per domain, estimated power at 15\\% contamination ranges from only 0.49 to 0.64 (Table~\\ref{tab:domain_power}), below practical thresholds. Subcategory-level analysis (57 subjects, 50--400 items each) is unreliable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Domain-level detection power estimates at 15\\% contamination (from power theory). No domain reaches the 0.80 practical threshold.}\n\\label{tab:domain_power}\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $n_{\\text{items}}$ & Est.\\ Power & Practical? \\\\\n\\midrule\nSTEM & 4{,}500 & 0.64 & No \\\\\nHumanities & 3{,}800 & 0.59 & No \\\\\nSocial Sciences & 3{,}200 & 0.55 & No \\\\\nOther & 2{,}542 & 0.49 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Post-RL Signal Retention}\n\\label{sec:post_rl}\n\nA critical scope question: does IRT-FIT detect contamination that persists through reinforcement learning? We contaminate Qwen3.5-9B via SFT at 25\\% on MMLU, then apply GRPO (5{,}000 steps with rule-based reward on held-out math/reasoning tasks).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Post-RL signal degradation. RL reshapes response patterns from memory-driven to reasoning-driven, eliminating the aberrant pattern signal.}\n\\label{tab:post_rl}\n\\begin{tabular}{lccccc}\n\\toprule\nStage & Acc.\\,$\\Delta$ & $\\Delta l_z^*$ & Cohen's $d$ & AUROC & $p$ \\\\\n\\midrule\nPost-SFT (25\\%) & +.10 & $-$4.2 & 1.85 & .91 & $<$.001 \\\\\nPost-RL (GRPO 5K) & +.04 & $-$0.8 & 0.28 & .56 & .34 \\\\\n\\midrule\nSignal retention & 40\\% & 19\\% & 15\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:post_rl} demonstrates that RL eliminates the contamination signal: $\\Delta l_z^*$ retention is only 19\\%, with AUROC dropping to chance level (0.56, $p=0.34$). While the model retains 40\\% of the accuracy gain, RL transforms the response strategy from memory-driven to reasoning-driven. The resulting response patterns conform to ability-based predictions, removing the aberrant signature that person-fit statistics detect. This is consistent with \\citet{wang2025contamination}'s finding that MIA-based methods also fail post-RL.\n\nIRT-FIT therefore targets SFT-based contamination and leaderboard gaming, not post-RL contamination. This scope boundary is mechanistically clear: RL's KL-penalized policy optimization reshapes response patterns to be reward-optimal rather than memorization-driven.\n\n\n\\subsection{Ablation: 4PL vs.\\ 3PL}\n\\label{sec:ablation}\n\nWe compare 4PL (default) against 3PL ($d_i=1$ for all items) to assess whether the upper asymptote parameter contributes meaningfully.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{4PL vs.\\ 3PL detection comparison. The $d$ parameter provides marginal improvement; 4PL is retained as default.}\n\\label{tab:4pl3pl}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 4PL & 3PL ($d{=}1$) & $\\Delta$ \\\\\n\\midrule\nSim.\\ Power MMLU@15\\% & 0.978 & 0.943 & +0.035 \\\\\nSim.\\ Power HSwag@15\\% & 0.753 & 0.725 & +0.028 \\\\\nSim.\\ False Alarm Rate & 0.048 & 0.055 & $-$0.007 \\\\\nCtrl.\\ AUROC MMLU@15\\% & 0.78 & 0.76 & +0.02 \\\\\n$l_z^*$ correlation (real data) & --- & --- & $r=0.985$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 4PL provides consistent but marginal improvements (Table~\\ref{tab:4pl3pl}): +3.5pp simulation power, +2pp controlled AUROC, and slightly lower false alarm rates. The two parameterizations produce nearly identical $l_z^*$ rankings ($r=0.985$), because $\\Delta l_z^*$ as a difference measure largely cancels the systematic effect of the $d$ parameter. We retain 4PL as default for its slightly better calibration, but the choice is not critical.\n\n\n\\subsection{Multiscale $l_{zm}$ Aggregation}\n\\label{sec:lzm}\n\nCross-benchmark aggregation via $l_{zm}$ (Section~\\ref{sec:method}) yields modest improvement: +3pp AUROC at 15\\% contamination on MMLU (0.81 vs.\\ 0.78 for the best single benchmark), +2pp at 50\\% (Table~\\ref{tab:lzm}). The limited gain reflects insufficient benchmark count ($K=4$): the $\\sqrt{K}$ noise reduction factor is only 2, and model-specific generalization effects---the dominant noise source---are not averaged away by cross-benchmark aggregation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$l_{zm}$ vs.\\ best single-benchmark $l_z^*$.}\n\\label{tab:lzm}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Best Single $l_z^*$ & $l_{zm}$ & $\\Delta$ \\\\\n\\midrule\nFlagged Rate (leaderboard) & 95.0\\% & 91.7\\% & $-$3.3\\% \\\\\nCtrl.\\ AUROC@15\\% (MMLU) & 0.78 & 0.81 & +0.03 \\\\\nCtrl.\\ AUROC@50\\% (MMLU) & 0.95 & 0.97 & +0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n%==============================================================================\n\\section{Discussion and Limitations}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Scope boundaries.}\nIRT-FIT is effective for large-scale benchmarks ($n \\geq 10$K items) at moderate-to-high contamination levels ($\\geq$15\\% on MMLU-scale, $\\geq$25\\% on HellaSwag-scale). For smaller benchmarks ($n < 5$K) or low contamination rates ($<$10\\%), the method lacks statistical power. These boundaries are precisely quantified by our power function ($R^2=0.96$), which itself constitutes a methodological contribution.\n\n\\paragraph{Cost of minimal information.}\nOperating at the binary-only level incurs a measurable detection cost: IRT-FIT trails Min-K\\%++ by 4--18pp AUROC depending on contamination level (Table~\\ref{tab:gap}). This gap is inherent to the information level, not the method---binary responses discard token-level memorization signatures. We argue this cost is acceptable given the 60$\\times$ scalability advantage (6{,}200+ vs.\\ ${\\sim}$100 models).\n\n\\paragraph{Post-RL blindness.}\nIRT-FIT cannot detect contamination that has been laundered through RL training (signal retention ${\\approx}$19\\%). This is a fundamental limitation shared with all methods that rely on memorization signatures \\citep{wang2025contamination}. Our method targets SFT-based contamination and direct benchmark memorization---the dominant mechanism in leaderboard gaming.\n\n\\paragraph{Universal model misfit.}\nThe finding that $>$89\\% of LLMs produce extreme $l_z^*$ values is itself methodologically significant. It demonstrates that LLM response patterns are fundamentally different from human test-taker patterns, violating IRT assumptions in ways that preclude direct application of classical person-fit thresholds. Future work should investigate what specific properties of LLM responses drive this universal misfit.\n\n\\paragraph{Leaderboard audit interpretation.}\nOur audit identifies anomalous models, not confirmed contamination. The weak cross-benchmark rank correlation ($\\rho=0.18$) means that anomaly status on one benchmark does not predict anomaly status on another. Temporal trends are suggestive but confounded with improving model capabilities. We present these results as converging evidence warranting further investigation.\n\n\\paragraph{Model generalization as confound.}\nInter-model variation in detection power (Cohen's $d$ from 0.62 to 1.35 at 15\\% MMLU contamination) reflects differences in SFT generalization capacity. Larger, more capable models extract more generalizable knowledge from contamination data, producing less aberrant response patterns. Detection power is therefore a function of three factors: $n_{\\text{items}}$, contamination level, and model-specific generalization capacity---of which only the first two are predictable a priori.\n\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe introduced IRT-FIT, a contamination detection framework that operates at the minimal-information level using only binary response patterns. Through controlled experiments across four models, six contamination levels, and five benchmarks (72 runs), we established that detection power follows $\\text{power} \\propto \\sqrt{n_{\\text{items}}}$ ($R^2=0.96$), providing a predictive theory for when binary-level detection succeeds and when it fails. Our retrospective audit of 6{,}200+ Open LLM Leaderboard models---the first at this scale---reveals increasing anomaly rates over time and identifies 42 cross-benchmark anomaly models. We quantify both the capabilities and the precise limitations of minimal-information detection, contributing to a more complete understanding of the contamination detection frontier.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Brown et~al.(2020)]{brown2020language}\nBrown, T., Mann, B., Ryder, N., et~al.\n\\newblock Language models are few-shot learners.\n\\newblock \\emph{NeurIPS}, 2020.\n\n\\bibitem[Dodge et~al.(2021)]{dodge2021documenting}\nDodge, J., Sap, M., Marasovi{\\'c}, A., et~al.\n\\newblock Documenting large webtext corpora: A case study on the {C}olossal {C}lean {C}rawled {C}orpus.\n\\newblock \\emph{EMNLP}, 2021.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nDong, Z., Tang, M., Song, Y., et~al.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock \\emph{ICLR (Spotlight)}, 2024.\n\n\\bibitem[Gu et~al.(2026)]{gu2024psnirt}\nGu, Z., Cui, Y., et~al.\n\\newblock {PSN-IRT}: A psychometric framework for evaluating large language models.\n\\newblock \\emph{AAAI (Oral)}, 2026.\n\n\\bibitem[Hong et~al.(2021)]{hong2021multiscale}\nHong, M., Cheng, Y., and Chang, H.-H.\n\\newblock A multiscale person-fit statistic for aberrant response detection.\n\\newblock \\emph{Applied Psychological Measurement}, 45(6), 2021.\n\n\\bibitem[Jacovi et~al.(2023)]{jacovi2023stop}\nJacovi, A., Caciularu, A., Herzig, J., et~al.\n\\newblock Stop uploading test data in plain text: Practical strategies for mitigating data contamination by evaluation benchmarks.\n\\newblock \\emph{EMNLP}, 2023.\n\n\\bibitem[Li et~al.(2024)]{li2024constat}\nLi, Y., et~al.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock \\emph{NeurIPS}, 2024.\n\n\\bibitem[Magar and Schwartz(2022)]{magar2022data}\nMagar, I. and Schwartz, R.\n\\newblock Data contamination: From memorization to exploitation.\n\\newblock \\emph{ACL}, 2022.\n\n\\bibitem[Meijer and Sijtsma(2001)]{meijer2001review}\nMeijer, R.~R. and Sijtsma, K.\n\\newblock Methodology review: Evaluating person fit.\n\\newblock \\emph{Applied Psychological Measurement}, 25(2), 2001.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nPolo, F.~M., Choshen, L., Sun, W., et~al.\n\\newblock {tinyBenchmarks}: Evaluating {LLM}s with fewer examples.\n\\newblock \\emph{ICML}, 2024.\n\n\\bibitem[Sainz et~al.(2023)]{sainz2023nlp}\nSainz, O., Campos, J.~A., et~al.\n\\newblock {NLP} evaluation in trouble: On the need to measure {LLM} data contamination for each benchmark.\n\\newblock \\emph{EMNLP Findings}, 2023.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nShi, W., Ajith, A., Xia, M., et~al.\n\\newblock Detecting pretraining data from large language models.\n\\newblock \\emph{ICLR}, 2024.\n\n\\bibitem[Snijders(2001)]{snijders2001item}\nSnijders, T.~A.~B.\n\\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.\n\\newblock \\emph{Psychometrika}, 66(3), 2001.\n\n\\bibitem[Wang et~al.(2025)]{wang2025contamination}\nWang, Z., et~al.\n\\newblock Contamination-resilient evaluation: Rethinking detection after reinforcement learning.\n\\newblock \\emph{ICML}, 2025.\n\n\\bibitem[Wu et~al.(2026)]{wu2026codec}\nWu, X., et~al.\n\\newblock {CoDeC}: Detecting data contamination via in-context learning effects.\n\\newblock \\emph{ICLR}, 2026.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "9136f781-42c4-4595-ab6c-e9244c031b7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit…",
  "leafUuid": "4dbb154b-38e6-4eb4-8788-3f7069baa063",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated academic paper",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---

### Tool call

_source line 23 · 2026-05-20T11:22:11.044Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HZJVHGDFzaB5pYJuU7ABKK`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dbb154b-38e6-4eb4-8788-3f7069baa063",
  "isSidechain": false,
  "requestId": "req_011CbDjWPfkKHRRqxiBaq4qP",
  "type": "assistant",
  "uuid": "00606bec-301f-4434-b5a6-ea8463d4878a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4nEEXfwiSMzoJHKWiE5nr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11846,
      "cache_read_input_tokens": 43182,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11846,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 43182,
          "cache_creation_input_tokens": 11846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11846
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

_source line 24 · 2026-05-20T11:22:12.780Z_

<details><summary>↩ Tool result · `toolu_01HZJVHGDFzaB5pYJuU7ABKK`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `magar2022data' on page 1 undefined on input l
ine 40.


Package natbib Warning: Citation `sainz2023nlp' on page 1 undefined on input li
ne 40.


Package natbib Warning: Citation `jacovi2023stop' on page 1 undefined on input 
line 40.


Package natbib Warning: Citation `brown2020language' on page 1 undefined on inp
ut line 42.


Package natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu
t line 42.


Package natbib Warning: Citation `dong2024generalization' on page 1 undefined o
n input line 42.


Package natbib Warning: Citation `li2024constat' on page 1 undefined on input l
ine 42.


Package natbib Warning: Citation `meijer2001review' on page 1 undefined on inpu
t line 44.


Package natbib Warning: Citation `snijders2001item' on page 1 undefined on inpu
t line 44.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `brown2020language' on page 2 undefined on inp
ut line 65.


Package natbib Warning: Citation `dodge2021documenting' on page 2 undefined on 
input line 65.


Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 65.


Package natbib Warning: Citation `dong2024generalization' on page 2 undefined o
n input line 65.


Package natbib Warning: Citation `li2024constat' on page 2 undefined on input l
ine 65.


Package natbib Warning: Citation `wu2026codec' on page 2 undefined on input lin
e 65.


Package natbib Warning: Citation `wang2025contamination' on page 2 undefined on
 input line 65.


Package natbib Warning: Citation `gu2024psnirt' on page 2 undefined on input li
ne 70.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 70.

[2]

Package natbib Warning: Citation `snijders2001item' on page 3 undefined on inpu
t line 91.


Package natbib Warning: Citation `gu2024psnirt' on page 3 undefined on input li
ne 107.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\Delta' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 115.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 115.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 115.


Package natbib Warning: Citation `hong2021multiscale' on page 3 undefined on in
put line 117.


LaTeX Warning: Reference `tab:pilot' on page 3 undefined on input line 150.

[3]

LaTeX Warning: Reference `tab:auroc_main' on page 4 undefined on input line 190
.


LaTeX Warning: Reference `tab:cohend' on page 4 undefined on input line 190.


LaTeX Warning: Reference `tab:per_model' on page 4 undefined on input line 192.



LaTeX Warning: Reference `tab:power_curve' on page 4 undefined on input line 23
5.


LaTeX Warning: Reference `tab:frontier' on page 4 undefined on input line 241.


LaTeX Warning: Reference `tab:gap' on page 4 undefined on input line 275.

[4]

LaTeX Warning: Reference `tab:audit' on page 5 undefined on input line 300.


LaTeX Warning: Reference `tab:domain' on page 5 undefined on input line 347.


LaTeX Warning: Reference `tab:domain_power' on page 5 undefined on input line 3
49.

[5]

LaTeX Warning: Reference `tab:post_rl' on page 6 undefined on input line 391.


Package natbib Warning: Citation `wang2025contamination' on page 6 undefined on
 input line 391.


LaTeX Warning: Reference `tab:4pl3pl' on page 6 undefined on input line 419.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 422.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 422.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 422.


LaTeX Warning: Reference `sec:method' on page 6 undefined on input line 425.


LaTeX Warning: Reference `tab:lzm' on page 6 undefined on input line 425.

[6]

LaTeX Warning: Reference `tab:gap' on page 7 undefined on input line 453.


Package natbib Warning: Citation `wang2025contamination' on page 7 undefined on
 input line 456.

[7] [8]

Package natbib Warning: There were undefined citations.

[9] [10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u
rw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 213334 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}] [2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\Delta' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 109.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 115.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 115.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 115.

[3] [4] [5]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 422.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 422.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 422.

[6] [7] [8] [9] [10] (./paper.aux) )&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 216785 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00606bec-301f-4434-b5a6-ea8463d4878a",
  "isSidechain": false,
  "promptId": "b758e82e-2c50-4d43-a3b9-55f7d1d554ef",
  "type": "user",
  "uuid": "87c4a64e-9d5e-4e32-9404-f7bad68d42a2",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `magar2022data' on page 1 undefined on input l\nine 40.\n\n\nPackage natbib Warning: Citation `sainz2023nlp' on page 1 undefined on input li\nne 40.\n\n\nPackage natbib Warning: Citation `jacovi2023stop' on page 1 undefined on input \nline 40.\n\n\nPackage natbib Warning: Citation `brown2020language' on page 1 undefined on inp\nut line 42.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu\nt line 42.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 1 undefined o\nn input line 42.\n\n\nPackage natbib Warning: Citation `li2024constat' on page 1 undefined on input l\nine 42.\n\n\nPackage natbib Warning: Citation `meijer2001review' on page 1 undefined on inpu\nt line 44.\n\n\nPackage natbib Warning: Citation `snijders2001item' on page 1 undefined on inpu\nt line 44.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `brown2020language' on page 2 undefined on inp\nut line 65.\n\n\nPackage natbib Warning: Citation `dodge2021documenting' on page 2 undefined on \ninput line 65.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 65.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 2 undefined o\nn input line 65.\n\n\nPackage natbib Warning: Citation `li2024constat' on page 2 undefined on input l\nine 65.\n\n\nPackage natbib Warning: Citation `wu2026codec' on page 2 undefined on input lin\ne 65.\n\n\nPackage natbib Warning: Citation `wang2025contamination' on page 2 undefined on\n input line 65.\n\n\nPackage natbib Warning: Citation `gu2024psnirt' on page 2 undefined on input li\nne 70.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 70.\n\n[2]\n\nPackage natbib Warning: Citation `snijders2001item' on page 3 undefined on inpu\nt line 91.\n\n\nPackage natbib Warning: Citation `gu2024psnirt' on page 3 undefined on input li\nne 107.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\Delta' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 115.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 115.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 115.\n\n\nPackage natbib Warning: Citation `hong2021multiscale' on page 3 undefined on in\nput line 117.\n\n\nLaTeX Warning: Reference `tab:pilot' on page 3 undefined on input line 150.\n\n[3]\n\nLaTeX Warning: Reference `tab:auroc_main' on page 4 undefined on input line 190\n.\n\n\nLaTeX Warning: Reference `tab:cohend' on page 4 undefined on input line 190.\n\n\nLaTeX Warning: Reference `tab:per_model' on page 4 undefined on input line 192.\n\n\n\nLaTeX Warning: Reference `tab:power_curve' on page 4 undefined on input line 23\n5.\n\n\nLaTeX Warning: Reference `tab:frontier' on page 4 undefined on input line 241.\n\n\nLaTeX Warning: Reference `tab:gap' on page 4 undefined on input line 275.\n\n[4]\n\nLaTeX Warning: Reference `tab:audit' on page 5 undefined on input line 300.\n\n\nLaTeX Warning: Reference `tab:domain' on page 5 undefined on input line 347.\n\n\nLaTeX Warning: Reference `tab:domain_power' on page 5 undefined on input line 3\n49.\n\n[5]\n\nLaTeX Warning: Reference `tab:post_rl' on page 6 undefined on input line 391.\n\n\nPackage natbib Warning: Citation `wang2025contamination' on page 6 undefined on\n input line 391.\n\n\nLaTeX Warning: Reference `tab:4pl3pl' on page 6 undefined on input line 419.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 422.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 422.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 422.\n\n\nLaTeX Warning: Reference `sec:method' on page 6 undefined on input line 425.\n\n\nLaTeX Warning: Reference `tab:lzm' on page 6 undefined on input line 425.\n\n[6]\n\nLaTeX Warning: Reference `tab:gap' on page 7 undefined on input line 453.\n\n\nPackage natbib Warning: Citation `wang2025contamination' on page 7 undefined on\n input line 456.\n\n[7] [8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u\nrw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 213334 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}] [2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\Delta' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 109.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 115.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 115.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 115.\n\n[3] [4] [5]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 422.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 422.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 422.\n\n[6] [7] [8] [9] [10] (./paper.aux) )&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 216785 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "00606bec-301f-4434-b5a6-ea8463d4878a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit…",
  "leafUuid": "87c4a64e-9d5e-4e32-9404-f7bad68d42a2",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated academic paper",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---

### Assistant

_source line 27 · 2026-05-20T11:22:23.359Z_

编译成功，10 页 PDF，无错误。

论文已写入 `paper.tex` 并编译为 `paper.pdf`（10 页）。覆盖全部 8 个实验：

1. **Controlled Contamination Pilot** — Table 1
2. **Full Controlled Contamination** — Tables 2-4 (AUROC, Cohen's d, per-model)
3. **Power Function Analysis** — Table 5 (含 BBH/MATH 验证点, $R^2=0.96$)
4. **Baseline Comparison** — Tables 6-7 (detection frontier + AUROC gap)
5. **Leaderboard Audit** — Tables 8-9 (6200+ 模型, temporal trends, top anomaly)
6. **MMLU Domain-Level Analysis** — Tables 10-11 (Gemini-1.5 case study + domain power)
7. **Post-RL Signal Retention** — Table 12 (negative result, 19% retention)
8. **4PL vs 3PL Ablation** — Table 13
9. **Multiscale $l_{zm}$** — Table 14

所有数字均取自 `experiment_data.json`，Limitations 段覆盖 scope boundary、minimal-information cost、post-RL blindness。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87c4a64e-9d5e-4e32-9404-f7bad68d42a2",
  "isSidechain": false,
  "requestId": "req_011CbDjWmJztZJFBsy9qAtJP",
  "type": "assistant",
  "uuid": "52d3d95c-e76d-41b5-942d-67f9c8b3266e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T105545/median",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLYqp5PymG6n6D5edY4z4u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7821,
      "cache_read_input_tokens": 55028,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 341,
          "cache_read_input_tokens": 55028,
          "cache_creation_input_tokens": 7821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7821
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T105545 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit…",
  "leafUuid": "52d3d95c-e76d-41b5-942d-67f9c8b3266e",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated academic paper",
  "sessionId": "a5a00c36-2957-4507-acbb-5e7f39dd97f5"
}
```

---
