# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/7e7e1b6c-aed8-4cea-84f5-26f97c6334ef.jsonl`
- **Structured JSON:** [`db16cea40e15d355432a.json`](../../sessions/db/db16cea40e15d355432a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:54:26.437Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:54:26.437Z",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：Claim 1 调整为 \"principled detection framework with characterized operating conditions\"： 检测在 3/4 家族有效（|d|>2.0 @ 15%），1 家族信号较弱（|d| 1.0-2.0）。 HellaSwag/GSM8K 效果显著但 d 值受 n_items 制约。θ-fixed 在多数家族恢复单调性但非全部。 Baseline 对比诚实报告 information-access vs detection-power tradeoff，强调 minimal-information operating point 价值。 Post-RL 若不完整降为 Discussion 中 structural argument + preliminary evidence。 标题可调整为 \"Detection and Characterization of Benchmark Contamination via IRT Person-Fit\"。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T03:54:26.440Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:54:26.440Z",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-21T03:54:26.461Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：Claim 1 调整为 "principled detection framework with characterized operating conditions"： 检测在 3/4 家族有效（|d|>2.0 @ 15%），1 家族信号较弱（|d| 1.0-2.0）。 HellaSwag/GSM8K 效果显著但 d 值受 n_items 制约。θ-fixed 在多数家族恢复单调性但非全部。 Baseline 对比诚实报告 information-access vs detection-power tradeoff，强调 minimal-information operating point 价值。 Post-RL 若不完整降为 Discussion 中 structural argument + preliminary evidence。 标题可调整为 "Detection and Characterization of Benchmark Contamination via IRT Person-Fit"。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ec7c9be7-428e-4670-904e-cc8df713932d",
  "type": "user",
  "uuid": "01dae032-4dcf-416b-a6af-8ec5c6543aed",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:54:26.461Z_

```json
{
  "parentUuid": "01dae032-4dcf-416b-a6af-8ec5c6543aed",
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
  "uuid": "330d6e7a-0b1c-48eb-866e-5f23b82844a1",
  "timestamp": "2026-05-21T03:54:26.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:54:26.461Z_

```json
{
  "parentUuid": "330d6e7a-0b1c-48eb-866e-5f23b82844a1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8bcd1473-2a43-4305-afa8-cb454a601968",
  "timestamp": "2026-05-21T03:54:26.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
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
  "aiTitle": "IRT person-fit detection of benchmark contamination",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---

### Assistant

_source line 7 · 2026-05-21T03:54:29.060Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bcd1473-2a43-4305-afa8-cb454a601968",
  "isSidechain": false,
  "requestId": "req_011CbF3BFcPFKzHQ4Fa3hstG",
  "type": "assistant",
  "uuid": "54bdb8b8-b8a6-4974-af9e-3ed7b6520116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqiX2eb7Ztp2DwtNztAqix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11759,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11759
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

_source line 8 · 2026-05-21T03:54:30.136Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UQ66t4JKyfWJbGeJeAEGgV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54bdb8b8-b8a6-4974-af9e-3ed7b6520116",
  "isSidechain": false,
  "requestId": "req_011CbF3BFcPFKzHQ4Fa3hstG",
  "type": "assistant",
  "uuid": "4c0edc9a-b470-486d-8020-fd70b5d7165b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqiX2eb7Ztp2DwtNztAqix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11759,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11759
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

_source line 9 · 2026-05-21T03:54:30.531Z_

<details><summary>↩ Tool result · `toolu_01UQ66t4JKyfWJbGeJeAEGgV`</summary>

```text
1	[
2	  {
3	    "name": "Controlled Contamination Pilot",
4	    "description": "Qwen3.5-9B × MMLU, 4 conditions (0%-s1/0%-s2/15%/50%)。 Go/no-go 信号：Δlz* 是否显著，clean-vs-clean noise floor，memorization fraction。\n",
5	    "results": {
6	      "clean_s1_lz_star": 8.2,
7	      "clean_s2_lz_star": 7.5,
8	      "clean_mean_lz_star": 7.85,
9	      "clean_std_lz_star": 0.49,
10	      "contam_15_lz_star": 5.1,
11	      "contam_50_lz_star": 6.8,
12	      "contam_15_delta_lz_star": -2.75,
13	      "contam_50_delta_lz_star": -1.05,
14	      "cohens_d_contam_15": -2.5,
15	      "cohens_d_contam_50": -0.95,
16	      "clean_vs_clean_delta": 0.7,
17	      "memorization_fraction_15pct": 0.35,
18	      "memorization_fraction_50pct": 0.28,
19	      "contam_15_acc": 0.72,
20	      "contam_50_acc": 0.76,
21	      "clean_mean_acc": 0.68,
22	      "theta_shift_15pct": 0.25,
23	      "theta_shift_50pct": 0.42,
24	      "seen_unseen_lz_gap_15pct": 2.8
25	    },
26	    "tables": [
27	      {
28	        "title": "Table: Pilot Δlz* Summary (Qwen3.5-9B × MMLU)",
29	        "columns": [
30	          "condition",
31	          "lz_star",
32	          "delta_lz_star",
33	          "cohens_d",
34	          "accuracy",
35	          "theta_mle",
36	          "memorization_frac"
37	        ],
38	        "rows": [
39	          [
40	            "clean-s1",
41	            8.2,
42	            "—",
43	            "—",
44	            0.679,
45	            -0.11,
46	            "—"
47	          ],
48	          [
49	            "clean-s2",
50	            7.5,
51	            "—",
52	            "—",
53	            0.681,
54	            -0.09,
55	            "—"
56	          ],
57	          [
58	            "contam-15%",
59	            5.1,
60	            -2.75,
61	            -2.5,
62	            0.72,
63	            0.14,
64	            0.35
65	          ],
66	          [
67	            "contam-50%",
68	            6.8,
69	            -1.05,
70	            -0.95,
71	            0.76,
72	            0.31,
73	            0.28
74	          ]
75	        ]
76	      }
77	    ],
78	    "figures": [],
79	    "analysis": "Go signal confirmed: |d|>2 @ 15%。但 free-θ 非单调性（50% d < 15% d）暴露 θ-shift confound， 需要 θ-fixed 分析。n=2 clean seeds 不足以精确估计 variance，第三 seed 必须追加。 Memorization fraction 0.35 意味着 theoretical power 是 upper bound，adjusted power ≈ 0.35 × theoretical。\n\n\nMedian 档下 Qwen 作为首个测试家族表现中等偏上。|d|=2.50 @ 15% 处于 median 范围 [1.0, 2.5] 上端， 因为 MMLU 是最大 benchmark（14K items），person-fit power 最强。 50% 条件 d=0.95（borderline large）反映 θ-shift confound——污染提升 θ_MLE 吸收了部分 aberrance 信号， 导致 free-θ 下 dose-response 非单调。clean-vs-clean Δ=0.7 建立 noise floor（远小于 contam Δ）， 确认信号非随机波动。memorization_fraction=0.35 落在 median 范围 [0.25, 0.45] 中部—— QLoRA SFT 不完全记忆，约 35% 污染 items 产生记忆信号，其余被 generalization 平滑。 seen/unseen gap=2.8 是最清晰的 fingerprint：被污染 items 的 lz* 显著低于 unseen items。 只有 2 个 clean seeds（n=2）限制了 Cohen's d 的精度，motivates 第三个 seed。\n"
80	  },
81	  {
82	    "name": "Full Controlled Contamination",
83	    "description": "4 模型 (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3) × 6 levels (0/5/10/15/25/50%) × 3 benchmarks (MMLU, GSM8K, HellaSwag)。\n",
84	    "results": {
85	      "qwen_mmlu_d_15pct": -2.5,
86	      "llama_mmlu_d_15pct": -2.8,
87	      "gemma_mmlu_d_15pct": -1.3,
88	      "mistral_mmlu_d_15pct": -2.2,
89	      "mean_mmlu_d_15pct": -2.2,
90	      "min_mmlu_d_15pct": -1.3,
91	      "n_families_d_gt_2_mmlu": 3,
92	      "qwen_hellaswag_d_15pct": -1.2,
93	      "llama_hellaswag_d_15pct": -1.4,
94	      "gemma_hellaswag_d_15pct": -0.6,
95	      "mistral_hellaswag_d_15pct": -1.1,
96	      "mean_hellaswag_d_15pct": -1.08,
97	      "qwen_gsm8k_d_15pct": -0.9,
98	      "llama_gsm8k_d_15pct": -1.1,
99	      "gemma_gsm8k_d_15pct": -0.4,
100	      "mistral_gsm8k_d_15pct": -0.8,
101	      "mean_gsm8k_d_15pct": -0.8,
102	      "theta_fixed_monotonic_families_mmlu": 3,
103	      "theta_fixed_monotonic_families_hellaswag": 2,
104	      "theta_fixed_monotonic_families_gsm8k": 2,
105	      "theta_fixed_non_monotonic_family": "Gemma (residual non-monotonicity at 50%)",
106	      "memorization_fraction_mmlu_range": [
107	        0.28,
108	        0.42
109	      ],
110	      "memorization_fraction_hellaswag_range": [
111	        0.25,
112	        0.38
113	      ],
114	      "memorization_fraction_gsm8k_range": [
115	        0.22,
116	        0.35
117	      ],
118	      "n_families_any_benchmark_d_gt_2": 3,
119	      "weakest_family": "Gemma",
120	      "weakest_family_reason": "high baseline ability → smaller θ-shift, lower aberrance signal"
121	    },
122	    "tables": [
123	      {
124	        "title": "Table: Cohen's d @ 15% Contamination (n=3 seeds, ddof=1, ℓz*-corrected)",
125	        "columns": [
126	          "family",
127	          "MMLU_d",
128	          "HellaSwag_d",
129	          "GSM8K_d",
130	          "θ_fixed_monotonic"
131	        ],
132	        "rows": [
133	          [
134	            "Qwen3.5-9B",
135	            -2.5,
136	            -1.2,
137	            -0.9,
138	            "Yes"
139	          ],
140	          [
141	            "Llama-3.1-8B",
142	            -2.8,
143	            -1.4,
144	            -1.1,
145	            "Yes"
146	          ],
147	          [
148	            "Gemma-4-31B",
149	            -1.3,
150	            -0.6,
151	            -0.4,
152	            "No (50% residual)"
153	          ],
154	          [
155	            "Mistral-7B-v0.3",
156	            -2.2,
157	            -1.1,
158	            -0.8,
159	            "Yes"
160	          ],
161	          [
162	            "Mean",
163	            -2.2,
164	            -1.08,
165	            -0.8,
166	            "3/4"
167	          ]
168	        ]
169	      },
170	      {
171	        "title": "Table: Memorization Fraction by Family × Benchmark",
172	        "columns": [
173	          "family",
174	          "MMLU",
175	          "HellaSwag",
176	          "GSM8K"
177	        ],
178	        "rows": [
179	          [
180	            "Qwen3.5-9B",
181	            0.38,
182	            0.33,
183	            0.3
184	          ],
185	          [
186	            "Llama-3.1-8B",
187	            0.42,
188	            0.38,
189	            0.35
190	          ],
191	          [
192	            "Gemma-4-31B",
193	            0.28,
194	            0.25,
195	            0.22
196	          ],
197	          [
198	            "Mistral-7B-v0.3",
199	            0.36,
200	            0.32,
201	            0.28
202	          ]
203	        ]
204	      },
205	      {
206	        "title": "Table: Dose-Response (MMLU, θ-fixed, ℓz*-corrected)",
207	        "columns": [
208	          "family",
209	          "d_5pct",
210	          "d_10pct",
211	          "d_15pct",
212	          "d_25pct",
213	          "d_50pct",
214	          "monotonic"
215	        ],
216	        "rows": [
217	          [
218	            "Qwen3.5-9B",
219	            -0.6,
220	            -1.4,
221	            -2.5,
222	            -3.8,
223	            -5.2,
224	            "Yes"
225	          ],
226	          [
227	            "Llama-3.1-8B",
228	            -0.75,
229	            -1.6,
230	            -2.8,
231	            -4.2,
232	            -5.8,
233	            "Yes"
234	          ],
235	          [
236	            "Gemma-4-31B",
237	            -0.3,
238	            -0.7,
239	            -1.3,
240	            -1.8,
241	            -1.6,
242	            "No"
243	          ],
244	          [
245	            "Mistral-7B-v0.3",
246	            -0.55,
247	            -1.2,
248	            -2.2,
249	            -3.4,
250	            -4.6,
251	            "Yes"
252	          ]
253	        ]
254	      }
255	    ],
256	    "figures": [],
257	    "analysis": "3/4 家族 MMLU |d|>2.0 确认检测框架跨家族有效，但 Gemma 的 boundary condition 需在论文中显式报告。 HellaSwag/GSM8K 的较低 d 值符合 power ∝ √n_items 理论，strengthens Claim 2。 Gemma 的残余非单调性是 median 档的 key limitation——需在 §6 讨论模型 ability 对检测的调制效应。 跨 benchmark memorization fraction 差异表明 SFT generalization 是 benchmark-dependent 的， 支持 Claim 2 的 caveat（power function 是 upper bound）。\n\n\nMedian 档核心假设：3/4 家族 |d|>2.0 @ 15% on MMLU，1 家族（Gemma）信号较弱。 Gemma-4-31B 作为 31B 模型，baseline ability 高于其他 7-9B 模型，θ_MLE 已较高， contamination 产生的 θ-shift 相对较小，且高能力模型本身对 MMLU hard items 答对率就高， memorization 信号被 genuine ability 遮盖——这是 median 档的典型 boundary condition。 HellaSwag（~10K items）d 值在 [0.8, 1.5] 范围，GSM8K（~1.3K items）d 值在 [0.5, 1.2] 范围， 严格遵循 power ∝ √n_items 的理论预测——n_items 减小直接压低 lz* 的 signal-to-noise ratio。 θ-fixed 在 Qwen/Llama/Mistral 恢复单调性，但 Gemma 因 baseline misfit 较低 + 高 ability， θ-fixed 改善有限，50% 条件仍有残余非单调性。 Memorization fraction 家族间有差异（25-45%），反映不同架构的 SFT generalization 特性不同： Gemma 的 instruction tuning 基础更强，generalization 更好，记忆信号更弱。\n"
258	  },
259	  {
260	    "name": "Leaderboard Audit",
261	    "description": "Open LLM Leaderboard v1 大规模 person-fit 扫描。已 ABANDONED（D011: a_r=0.111）。\n",
262	    "results": {
263	      "status": "ABANDONED",
264	      "reason": "v1-irt-refit a_r=0.111, item alignment 54.56% → parameters too degraded for audit"
265	    },
266	    "tables": [],
267	    "figures": [],
268	    "analysis": "ABANDONED。在论文 §7 Discussion 中报告：13K+ per-item data publicly available， 但 current IRT estimation methods 的 sample size requirements 限制了大规模审计。 Frame as \"the gap between classical IRT and neural IRT estimation\" methodological contribution。\n\n\nPath D 已确认 dead：MML-EM 重拟合的 discrimination 参数 a_r=0.111 远低于 0.2 可用阈值， 意味着 v1 leaderboard 参数下的 lz* 基本退化为 accuracy-like statistic， 无法提供 person-fit 特有的 response-pattern-level 信息。 在 median 档下不需要尝试——这是一个已被充分验证的 negative result。 数据可用性（13K+ models）写入 Discussion/Future Work 即可。\n"
269	  },
270	  {
271	    "name": "Natural Experiment (base→chat pairs)",
272	    "description": "v1 leaderboard base→chat 模型 pairs，计算 Δlz* 作为 SFT 效应代理。\n",
273	    "results": {
274	      "n_pairs": 4,
275	      "n_benchmarks": 4,
276	      "n_significant_benchmarks": 1,
277	      "significant_benchmark": "HellaSwag",
278	      "hellaswag_mean_delta": -2.8,
279	      "hellaswag_p_value": 0.04,
280	      "mmlu_p_value": 0.22,
281	      "gsm8k_p_value": 0.18,
282	      "arc_c_p_value": 0.45,
283	      "individual_outlier_pairs": 0,
284	      "overall_conclusion": "weak_systematic_signal"
285	    },
286	    "tables": [
287	      {
288	        "title": "Table: Natural Experiment Δlz* (base→chat)",
289	        "columns": [
290	          "benchmark",
291	          "n_pairs",
292	          "mean_delta",
293	          "t_stat",
294	          "p_value",
295	          "significant"
296	        ],
297	        "rows": [
298	          [
299	            "MMLU",
300	            4,
301	            -1.2,
302	            -1.45,
303	            0.22,
304	            "No"
305	          ],
306	          [
307	            "HellaSwag",
308	            4,
309	            -2.8,
310	            -2.85,
311	            0.04,
312	            "Marginal"
313	          ],
314	          [
315	            "GSM8K",
316	            4,
317	            1.5,
318	            1.62,
319	            0.18,
320	            "No"
321	          ],
322	          [
323	            "ARC-C",
324	            4,
325	            -0.6,
326	            -0.82,
327	            0.45,
328	            "No"
329	          ]
330	        ]
331	      }
332	    ],
333	    "figures": [],
334	    "analysis": "Underpowered by design (n=4 pairs, a_r degraded)。HellaSwag marginal significance 可能反映 SFT 的系统效应而非 contamination。不影响论文 claims。 Appendix material，mention in §6 as \"preliminary evidence consistent with SFT effects on response patterns\"。\n\n\nMedian 档下 natural experiment 受限于两个因素： (1) a_r=0.111 使 lz* 退化为 accuracy-like，个体 Δlz* 主要反映 Δaccuracy 而非 response pattern shift； (2) 仅 4-5 usable pairs 无统计检验能力（n 太小无法做 paired t-test with power）。 HellaSwag 可能显示 marginal significance 因为它是最大的非 MMLU benchmark（~10K items）， 但 effect 不强。其他 benchmarks p>0.15。无个体 outlier pair 显示 benchmark-specific contamination。 这是一个 P2-optional 实验，median 档下结论是 \"suggestive but underpowered\"， 不进入主论文 claims，可在 appendix 报告。\n"
335	  },
336	  {
337	    "name": "v1 IRT Refit Expanded",
338	    "description": "扩大 v1 IRT 重拟合至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。\n",
339	    "results": {
340	      "n_models_downloaded": 520,
341	      "n_models_usable": 410,
342	      "a_r_3pl": 0.13,
343	      "a_r_2pl": -0.02,
344	      "b_r_3pl": 0.66,
345	      "b_r_spearman": 0.68,
346	      "fitting_time_sec": 180,
347	      "conclusion": "negative_path_d_dead"
348	    },
349	    "tables": [
350	      {
351	        "title": "Table: IRT Refit Comparison (pilot vs expanded)",
352	        "columns": [
353	          "metric",
354	          "pilot_N63",
355	          "expanded_N500",
356	          "threshold",
357	          "verdict"
358	        ],
359	        "rows": [
360	          [
361	            "3PL a_r (Pearson)",
362	            0.111,
363	            0.13,
364	            ">0.4 viable",
365	            "FAIL"
366	          ],
367	          [
368	            "2PL a_r (Pearson)",
369	            -0.084,
370	            -0.02,
371	            ">0.4 viable",
372	            "FAIL"
373	          ],
374	          [
375	            "3PL b_r (Pearson)",
376	            0.626,
377	            0.66,
378	            ">0.5 viable",
379	            "PASS"
380	          ],
381	          [
382	            "3PL b_r (Spearman)",
383	            0.656,
384	            0.68,
385	            ">0.5 viable",
386	            "PASS"
387	          ]
388	        ]
389	      }
390	    ],
391	    "figures": [],
392	    "analysis": "Path D 最终关闭。a_r<0.2 at N=500 confirms discrimination failure is structural, not sample-size-driven。 论文 §5 报告为 \"IRT parameter estimation challenges\"（Claim 3c）， framing: \"the gap between classical psychometric sample requirements and the scale needed for neural IRT\"。\n\n\nMedian 档预期 a_r 从 0.111（N=63）仅微升至 ~0.13（N=500+），远低于 0.2 可用阈值。 原因：discrimination failure 不是 sample size 问题，而是 LLM response patterns 的结构性特征—— classical IRT 假设 unidimensional latent trait，但 LLMs 的 ability profile 是 multi-dimensional 的 （不同 domain 能力独立变化），导致 item discrimination 在 aggregate 拟合中坍缩。 b_r 稳定在 0.66（difficulty 恢复尚可）进一步确认：问题在 discrimination 而非 difficulty。 这个 negative result 是 methodological contribution——量化了 classical vs neural IRT 的 sample size gap。 N=500 满足 reviewer 要求的阈值，可以最终关闭 Path D。\n"
393	  },
394	  {
395	    "name": "4PL vs 3PL Ablation",
396	    "description": "比较 4PL vs 3PL(d=1) 下的检测灵敏度差异，量化 feasibility parameter d 的影响。\n",
397	    "results": {
398	      "far_4pl": 0.05,
399	      "far_3pl_range": [
400	        0.06,
401	        0.14
402	      ],
403	      "far_2pl_range": [
404	        0.5,
405	        1.0
406	      ],
407	      "mean_power_gain_mmlu": 0.22,
408	      "mean_power_gain_hellaswag": 0.2,
409	      "mean_power_gain_gsm8k": 0.16,
410	      "mean_power_gain_arc_c": 0.11,
411	      "mean_power_gain_humaneval": 0.1,
412	      "pct_items_d_lt_0.95_mmlu": 0.46,
413	      "correlation_4pl_3pl_lz": 0.35
414	    },
415	    "tables": [
416	      {
417	        "title": "Table: Detection Power at 25% Contamination by Model",
418	        "columns": [
419	          "benchmark",
420	          "power_4PL",
421	          "power_3PL",
422	          "gain_pp",
423	          "pct_items_d_lt_0.95"
424	        ],
425	        "rows": [
426	          [
427	            "MMLU",
428	            0.72,
429	            0.5,
430	            22,
431	            "46%"
432	          ],
433	          [
434	            "HellaSwag",
435	            0.48,
436	            0.28,
437	            20,
438	            "41%"
439	          ],
440	          [
441	            "GSM8K",
442	            0.65,
443	            0.49,
444	            16,
445	            "30%"
446	          ],
447	          [
448	            "ARC-C",
449	            0.12,
450	            0.08,
451	            4,
452	            "22%"
453	          ],
454	          [
455	            "HumanEval",
456	            0.28,
457	            0.18,
458	            10,
459	            "35%"
460	          ]
461	        ]
462	      }
463	    ],
464	    "figures": [],
465	    "analysis": "4PL d parameter 对 LLM contamination detection 不可或缺。 Power gain +15-25pp 在论文中用 one sentence 总结即可： \"Ignoring the upper asymptote parameter halves detection power on benchmarks with substantial d<0.95 items.\" 2PL 的灾难性 FAR 作为 negative control 报告，确认 guessing parameter 同样必要。\n\n\nMedian 档预期 4PL 相对 3PL 的 power gain 在 +15-25pp 范围（略低于 optimistic 的 +25-30pp）。 原因：46% MMLU items 有 d<0.95（从已有 PSN-IRT 参数已知），这些 items 的 upper asymptote <1， high-ability models 在这些 items 上即使全对也不会产生极端 aberrance。 3PL(d=1) 强制 upper asymptote=1，对 high-ability models 系统性高估 expected P(correct)， 导致 false alarm inflation（6-14%）和 lz* 偏移。 相关性 r=0.35 表明 4PL vs 3PL lz* 存在根本性差异，不是简单缩放关系。 2PL 完全不可用（FAR 50-100%）因为同时忽略了 guessing 和 upper asymptote。 这个 ablation 直接支持 method design choice 的合理性。\n"
466	  },
467	  {
468	    "name": "Baseline Comparison",
469	    "description": "≥5 baselines 在 ctrl-contam ground-truth 上对比： IRT-FIT, ConStat, Min-K%++, accuracy z-score, PPL-based, random。\n",
470	    "results": {
471	      "auroc_5pct": {
472	        "lz_star": 0.65,
473	        "accuracy_zscore": 0.53,
474	        "mink_pp": 0.78,
475	        "constat": 0.72,
476	        "ppl_based": 0.75,
477	        "random": 0.5
478	      },
479	      "auroc_10pct": {
480	        "lz_star": 0.74,
481	        "accuracy_zscore": 0.58,
482	        "mink_pp": 0.86,
483	        "constat": 0.82,
484	        "ppl_based": 0.83,
485	        "random": 0.5
486	      },
487	      "auroc_15pct": {
488	        "lz_star": 0.8,
489	        "accuracy_zscore": 0.62,
490	        "mink_pp": 0.92,
491	        "constat": 0.88,
492	        "ppl_based": 0.9,
493	        "random": 0.5
494	      },
495	      "auroc_25pct": {
496	        "lz_star": 0.86,
497	        "accuracy_zscore": 0.7,
498	        "mink_pp": 0.96,
499	        "constat": 0.93,
500	        "ppl_based": 0.95,
501	        "random": 0.5
502	      },
503	      "auroc_gap_at_5pct_vs_best": -0.13,
504	      "auroc_gap_at_15pct_vs_best": -0.12,
505	      "auroc_gap_at_25pct_vs_best": -0.1,
506	      "lz_star_ci_width_15pct": 0.06,
507	      "mink_pp_ci_width_15pct": 0.04,
508	      "lz_star_rank_at_5pct": "2nd (behind Min-K%++)",
509	      "lz_star_rank_at_15pct": "4th",
510	      "lz_star_beats_accuracy_zscore_all_levels": true,
511	      "information_access": {
512	        "lz_star": "binary only",
513	        "accuracy_zscore": "binary only",
514	        "mink_pp": "token probs",
515	        "constat": "retest",
516	        "ppl_based": "log-probs",
517	        "random": "none"
518	      }
519	    },
520	    "tables": [
521	      {
522	        "title": "Table: AUROC Comparison Across Contamination Levels (MMLU, mean ± 95% CI)",
523	        "columns": [
524	          "method",
525	          "info_access",
526	          "5%",
527	          "10%",
528	          "15%",
529	          "25%"
530	        ],
531	        "rows": [
532	          [
533	            "Random",
534	            "—",
535	            "0.50",
536	            "0.50",
537	            "0.50",
538	            "0.50"
539	          ],
540	          [
541	            "Acc z-score",
542	            "binary",
543	            "0.53±0.05",
544	            "0.58±0.05",
545	            "0.62±0.05",
546	            "0.70±0.04"
547	          ],
548	          [
549	            "lz* (ours)",
550	            "binary",
551	            "0.65±0.06",
552	            "0.74±0.06",
553	            "0.80±0.06",
554	            "0.86±0.05"
555	          ],
556	          [
557	            "ConStat",
558	            "retest",
559	            "0.72±0.04",
560	            "0.82±0.04",
561	            "0.88±0.04",
562	            "0.93±0.03"
563	          ],
564	          [
565	            "PPL-based",
566	            "log-probs",
567	            "0.75±0.04",
568	            "0.83±0.04",
569	            "0.90±0.03",
570	            "0.95±0.02"
571	          ],
572	          [
573	            "Min-K%++",
574	            "token probs",
575	            "0.78±0.04",
576	            "0.86±0.03",
577	            "0.92±0.03",
578	            "0.96±0.02"
579	          ]
580	        ]
581	      },
582	      {
583	        "title": "Table: Information-Access vs Detection-Power Summary",
584	        "columns": [
585	          "operating_point",
586	          "methods",
587	          "AUROC_15pct_range",
588	          "information_required"
589	        ],
590	        "rows": [
591	          [
592	            "Minimal",
593	            "lz*, acc z-score",
594	            "0.62-0.80",
595	            "Binary response pattern only"
596	          ],
597	          [
598	            "Moderate",
599	            "ConStat",
600	            "0.88",
601	            "Retest with rephrased items"
602	          ],
603	          [
604	            "Full",
605	            "Min-K%++, PPL",
606	            "0.90-0.92",
607	            "Token-level probabilities"
608	          ]
609	        ]
610	      }
611	    ],
612	    "figures": [],
613	    "analysis": "关键叙事：lz* 是 minimal-information frontier 的 champion——在 binary-only 条件下显著优于 accuracy z-score， 且在低污染区间接近 privileged methods。15%+ 的 gap 是 information disadvantage 的直接后果，不是 method failure。 Bootstrap CIs 是论文的差异化优势（6/8 peer papers 不报告 variance）。 Detection frontier figure 是 paper 的 key contribution visualization。\n\n\nMedian 档核心：lz* 在 5% 低污染区间优势明确（0.65 vs accuracy_zscore 0.53，+0.12）， 但 15%+ 区间落后于 Min-K%++/ConStat 10-15% AUROC。 原因分析： (1) lz* @ 5% 优于 accuracy z-score 因为它利用了 response pattern 的 item-level 信息（IRT inductive bias），\n    而 accuracy z-score 只看 aggregate score；\n(2) lz* @ 5% 接近 privileged methods（gap 仅 -0.13）因为低污染下 privileged methods 的信号也弱，\n    lz* 的 IRT structure 作为 inductive bias 部分补偿了 information disadvantage；\n(3) @ 15%+ lz* 落后因为 privileged methods 获得的额外信息（token probs, retest）\n    提供了 lz* 无法获取的 fine-grained signal，信息差距随污染增加而放大；\n(4) AUROC gap [-0.15, -0.05] 在 median 范围，诚实但不灾难性。 narrative 策略：plot information-access vs detection-power frontier curve， 强调 lz* 定义了 \"minimal-information operating point\" 的价值而非绝对性能。\n"
614	  },
615	  {
616	    "name": "Multiscale lzm Statistic",
617	    "description": "实现 Hong, Lin & Cheng (2021) multiscale lzm——跨 benchmark 聚合的标准化 lz* 总分。\n",
618	    "results": {
619	      "lzm_gemini15": 45.2,
620	      "lzm_vs_per_benchmark_correlation": 0.92,
621	      "lzm_improvement_over_avg_lz": "marginal",
622	      "n_newly_flagged": 0,
623	      "n_newly_unflagged": 0,
624	      "lzm_flagged_rate": "57/60 (same as per-benchmark)",
625	      "lzm_interpretability": "lower than per-benchmark (loses benchmark-specific patterns)"
626	    },
627	    "tables": [
628	      {
629	        "title": "Table: lzm vs Per-Benchmark lz* for Top Anomalous Models",
630	        "columns": [
631	          "model",
632	          "lzm",
633	          "mmlu_lz",
634	          "hellaswag_lz",
635	          "gsm8k_lz",
636	          "pattern"
637	        ],
638	        "rows": [
639	          [
640	            "Gemini-1.5",
641	            45.2,
642	            31.8,
643	            -12.3,
644	            -8.5,
645	            "Selective (MMLU+, others-)"
646	          ],
647	          [
648	            "Yi-Lightning",
649	            52.1,
650	            48.2,
651	            35.1,
652	            22.0,
653	            "Uniform positive"
654	          ],
655	          [
656	            "Doubao",
657	            18.3,
658	            25.6,
659	            -5.2,
660	            -10.1,
661	            "Mixed"
662	          ]
663	        ]
664	      }
665	    ],
666	    "figures": [],
667	    "analysis": "lzm 不增加 detection power，但可在 supplementary 中报告为 alternative aggregation。 论文主体保留 per-benchmark profile 作为 primary presentation。\n\n\nMedian 档下 lzm 提供 marginal improvement：由于 LLM data 已经 universally flagged（57/60）， 聚合统计量无法进一步区分。r=0.92 表明 lzm 与 avg(lz*) 高度相关，额外信息有限。 更重要的是，per-benchmark lz* profile 是 contamination characterization 的核心 （如 Gemini 的 selective vs uniform misfit），而 lzm 聚合丢失了这些 benchmark-specific patterns。 在 median 档下 lzm 是 nice-to-have 但不改变任何 claim，可降为 appendix。\n"
668	  },
669	  {
670	    "name": "Post-RL Hypothesis Test",
671	    "description": "Qwen3.5-9B: SFT 污染 → GRPO 训练 → 测试 person-fit 是否保持检测力。\n",
672	    "results": {
673	      "pre_rl_d_15pct": -2.5,
674	      "post_rl_d_15pct": -1.1,
675	      "signal_retention_ratio": 0.44,
676	      "post_rl_lz_star_contam_15": 6.2,
677	      "post_rl_lz_star_clean": 7.8,
678	      "post_rl_delta_lz": -1.6,
679	      "post_rl_p_value": 0.03,
680	      "post_rl_memorization_fraction": 0.18,
681	      "grpo_training_steps": 2000,
682	      "grpo_reward": "rule-based (MMLU accuracy on held-out set)",
683	      "experiment_completed_before_ddl": "uncertain",
684	      "wang_mia_post_rl_auroc": 0.52,
685	      "lz_star_post_rl_auroc": 0.62
686	    },
687	    "tables": [
688	      {
689	        "title": "Table: Pre- vs Post-RL Detection (Qwen3.5-9B × MMLU @ 15%)",
690	        "columns": [
691	          "condition",
692	          "lz_star",
693	          "delta_lz",
694	          "cohens_d",
695	          "memorization_frac"
696	        ],
697	        "rows": [
698	          [
699	            "Clean",
700	            7.85,
701	            "—",
702	            "—",
703	            "—"
704	          ],
705	          [
706	            "SFT-contam (pre-RL)",
707	            5.1,
708	            -2.75,
709	            -2.5,
710	            0.35
711	          ],
712	          [
713	            "SFT-contam + GRPO (post-RL)",
714	            6.2,
715	            -1.6,
716	            -1.1,
717	            0.18
718	          ]
719	        ]
720	      },
721	      {
722	        "title": "Table: Post-RL Comparison with Wang et al. MIA Methods",
723	        "columns": [
724	          "method",
725	          "info_access",
726	          "pre_rl_auroc",
727	          "post_rl_auroc",
728	          "retention"
729	        ],
730	        "rows": [
731	          [
732	            "lz* (ours)",
733	            "binary",
734	            0.8,
735	            0.62,
736	            "77.5%"
737	          ],
738	          [
739	            "Min-K%++",
740	            "token probs",
741	            0.92,
742	            0.52,
743	            "56.5%"
744	          ],
745	          [
746	            "PPL-based",
747	            "log-probs",
748	            0.9,
749	            0.51,
750	            "56.7%"
751	          ]
752	        ]
753	      }
754	    ],
755	    "figures": [],
756	    "analysis": "Post-RL |d|=1.10 是 medium-to-large effect——信号衰减但 statistically significant。 若在 DDL 前完成：strengthens paper 显著（unique contribution: only binary method surviving RL）。 若不完整：降为 Discussion，做 structural argument——\"RL modifies token distributions but not binary patterns directly, so person-fit retains partial signal where MIA-based methods fail completely\"。 无论哪种情况，对 EMNLP 投稿不是 blocking issue。\n\n\nMedian 档核心假设：post-RL 信号衰减但未消失（|d| 0.5-1.5），或实验未在 DDL 前完成。 预测 |d|=1.10（从 pre-RL 2.50 衰减 56%）：GRPO 优化 reward signal 时， RL exploration 部分覆写了 SFT 记忆——模型学会了 \"更好的理由\" 来选择答案， 而非依赖记忆的 response pattern。但 binary response 层面的 aberrance 不完全消失， 因为 RL 不直接优化 response pattern distribution，只优化 outcome。 memorization_fraction 从 pre-RL ~0.35 降至 ~0.18：RL 使约一半的 \"记忆\" items 转化为 \"理解\"。 关键：即使 |d|=1.10 仍然 significant (p=0.03)，而 Wang et al. 证明 MIA methods 完全失效（AUROC≈0.50）。 这就是 binary-level 检测的 structural advantage——RL 改变 token distribution 但不完全消除 aberrant binary patterns。 但 DDL 风险：GRPO 训练需要 reward model setup + 调参 + 多 seed validation，40 GPU-hrs 可能不足。 若不完整，降为 Discussion 中 \"structural argument + preliminary evidence\"。\n"
757	  },
758	  {
759	    "name": "Extra Benchmarks (BBH + MATH)",
760	    "description": "BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。\n",
761	    "results": {
762	      "bbh_power_15pct": 0.68,
763	      "math_power_15pct": 0.55,
764	      "bbh_power_vs_theory": "within 5%",
765	      "math_power_vs_theory": "within 8%",
766	      "power_theory_R2_with_extras": 0.88,
767	      "bbh_4pl_available": false,
768	      "math_4pl_available": false,
769	      "bbh_4pl_estimation_needed": true,
770	      "math_4pl_estimation_needed": true,
771	      "estimation_gpu_hours": 8,
772	      "estimation_n_models_needed": 50
773	    },
774	    "tables": [
775	      {
776	        "title": "Table: Power Function Validation with Extended Benchmarks",
777	        "columns": [
778	          "benchmark",
779	          "n_items",
780	          "power_15pct_sim",
781	          "power_15pct_theory",
782	          "gap"
783	        ],
784	        "rows": [
785	          [
786	            "HumanEval",
787	            164,
788	            0.24,
789	            0.22,
790	            0.02
791	          ],
792	          [
793	            "ARC-C",
794	            295,
795	            0.13,
796	            0.15,
797	            -0.02
798	          ],
799	          [
800	            "MATH",
801	            5000,
802	            0.55,
803	            0.58,
804	            -0.03
805	          ],
806	          [
807	            "BBH",
808	            6511,
809	            0.68,
810	            0.72,
811	            -0.04
812	          ],
813	          [
814	            "GSM8K",
815	            1319,
816	            0.59,
817	            0.55,
818	            0.04
819	          ],
820	          [
821	            "HellaSwag",
822	            10042,
823	            0.75,
824	            0.78,
825	            -0.03
826	          ],
827	          [
828	            "MMLU",
829	            14042,
830	            0.98,
831	            0.98,
832	            0.0
833	          ]
834	        ]
835	      }
836	    ],
837	    "figures": [],
838	    "analysis": "BBH/MATH 填补 1K-10K gap，strengthens Claim 2 的 power function。 但若 4PL 参数需自行估计，quality concern 可能引入 noise。 如果 PSN-IRT 不包含这些参数，建议降为 appendix 或 future work。 核心 5 benchmarks 已足够支撑 power theory（R²=0.957）。\n\n\nMedian 档下 BBH (6.5K items) 和 MATH (5K items) 落在 power curve 的 \"中等\" 区间： power@15% 预期 0.55-0.68，验证 power ∝ √n_items 理论在 1K-10K 范围的插值。 BBH > MATH 因为 n_items 多 30%，strictly following the theoretical relationship。 关键挑战：PSN-IRT 可能不包含这些 benchmarks 的 4PL 参数。 如果需要自己估计 4PL，至少需要 50 个模型的 per-item responses + MML-EM fitting， 这引入新的 estimation quality concern（同 Path D 的 a_r 问题）。 Median 档下 R²=0.88（含新 benchmarks）略低于 simulation-only 的 0.957， 反映 SFT generalization gap（theoretical power 是 upper bound，actual power 受 memorization fraction 调制）。 这恰好支持 Claim 2 的 \"upper bound\" caveat。\n"
839	  },
840	  {
841	    "name": "Domain-Level Analysis",
842	    "description": "MMLU domain-level person-fit 分析，识别 Gemini-1.5 等模型的 domain-specific 污染模式。\n",
843	    "results": {
844	      "gemini15_all_domains_flagged": true,
845	      "gemini15_domain_concentrated": false,
846	      "gemini15_stem_lz": 22.0,
847	      "gemini15_humanities_lz": 18.5,
848	      "gemini15_social_sciences_lz": 16.2,
849	      "gemini15_other_lz": 15.8,
850	      "n_models_domain_concentrated": 2,
851	      "doubao_pattern": "Humanities/SocialSci negative, STEM neutral, Other positive",
852	      "hunyuan_pattern": "SocialSci high positive, STEM low",
853	      "domain_entropy_correlation_with_contamination": 0.45,
854	      "n_subjects_total": 57,
855	      "gemini_subjects_flagged": 52
856	    },
857	    "tables": [
858	      {
859	        "title": "Table: Domain-Level lz* for Selected Models",
860	        "columns": [
861	          "model",
862	          "STEM",
863	          "Humanities",
864	          "Social_Sci",
865	          "Other",
866	          "pattern_type"
867	        ],
868	        "rows": [
869	          [
870	            "Gemini-1.5",
871	            22.0,
872	            18.5,
873	            16.2,
874	            15.8,
875	            "Uniform positive"
876	          ],
877	          [
878	            "Yi-Lightning",
879	            50.1,
880	            45.3,
881	            48.7,
882	            42.0,
883	            "Uniform positive (extreme)"
884	          ],
885	          [
886	            "Doubao",
887	            -2.0,
888	            -13.0,
889	            -14.8,
890	            4.4,
891	            "Selective mixed"
892	          ],
893	          [
894	            "Hunyuan",
895	            1.8,
896	            8.2,
897	            13.9,
898	            6.5,
899	            "Selective positive"
900	          ],
901	          [
902	            "Mistral-Large",
903	            28.5,
904	            24.1,
905	            22.0,
906	            20.3,
907	            "Uniform positive"
908	          ]
909	        ]
910	      }
911	    ],
912	    "figures": [],
913	    "analysis": "Domain analysis 是 Claim 3 的 supporting evidence：contamination 不仅可以检测， 还可以 characterize（uniform vs selective patterns）。 Ward clustering 可能 reveal contamination typology（2-3 clusters）， 为 \"Detection and Characterization\" 标题提供直接支撑。 建议作为 §5 case study 的 subsection 呈现。\n\nMedian 档下 domain analysis 证实两种 contamination pattern： (1) Uniform contamination (Gemini-1.5): 100% accuracy across all domains，\n    所有 domain 都 flagged，STEM 略高因为 STEM items 的 discrimination 通常更高\n    （item difficulty variance 更大），产生更强的 aberrance signal。\n(2) Selective contamination (Doubao, Hunyuan): domain-specific misfit patterns，\n    某些 domain positive lz*（over-consistent，可能是 domain-specific training data exposure），\n    某些 domain negative lz*（aberrant，可能是 domain mismatch）。\nDomain entropy 与 contamination severity 的 moderate correlation (r=0.45) 表明 更均匀的 domain misfit 通常伴随更高的整体 contamination 程度——但不是强关系， 因为 SFT 的 generalization 跨 domain 不均匀。\n"
914	  }
915	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c0edc9a-b470-486d-8020-fd70b5d7165b",
  "isSidechain": false,
  "promptId": "ec7c9be7-428e-4670-904e-cc8df713932d",
  "type": "user",
  "uuid": "0546097c-91ab-42f8-bf0a-f6e3e3aaeb07",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Controlled Contamination Pilot\",\n    \"description\": \"Qwen3.5-9B × MMLU, 4 conditions (0%-s1/0%-s2/15%/50%)。 Go/no-go 信号：Δlz* 是否显著，clean-vs-clean noise floor，memorization fraction。\\n\",\n    \"results\": {\n      \"clean_s1_lz_star\": 8.2,\n      \"clean_s2_lz_star\": 7.5,\n      \"clean_mean_lz_star\": 7.85,\n      \"clean_std_lz_star\": 0.49,\n      \"contam_15_lz_star\": 5.1,\n      \"contam_50_lz_star\": 6.8,\n      \"contam_15_delta_lz_star\": -2.75,\n      \"contam_50_delta_lz_star\": -1.05,\n      \"cohens_d_contam_15\": -2.5,\n      \"cohens_d_contam_50\": -0.95,\n      \"clean_vs_clean_delta\": 0.7,\n      \"memorization_fraction_15pct\": 0.35,\n      \"memorization_fraction_50pct\": 0.28,\n      \"contam_15_acc\": 0.72,\n      \"contam_50_acc\": 0.76,\n      \"clean_mean_acc\": 0.68,\n      \"theta_shift_15pct\": 0.25,\n      \"theta_shift_50pct\": 0.42,\n      \"seen_unseen_lz_gap_15pct\": 2.8\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Pilot Δlz* Summary (Qwen3.5-9B × MMLU)\",\n        \"columns\": [\n          \"condition\",\n          \"lz_star\",\n          \"delta_lz_star\",\n          \"cohens_d\",\n          \"accuracy\",\n          \"theta_mle\",\n          \"memorization_frac\"\n        ],\n        \"rows\": [\n          [\n            \"clean-s1\",\n            8.2,\n            \"—\",\n            \"—\",\n            0.679,\n            -0.11,\n            \"—\"\n          ],\n          [\n            \"clean-s2\",\n            7.5,\n            \"—\",\n            \"—\",\n            0.681,\n            -0.09,\n            \"—\"\n          ],\n          [\n            \"contam-15%\",\n            5.1,\n            -2.75,\n            -2.5,\n            0.72,\n            0.14,\n            0.35\n          ],\n          [\n            \"contam-50%\",\n            6.8,\n            -1.05,\n            -0.95,\n            0.76,\n            0.31,\n            0.28\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Go signal confirmed: |d|>2 @ 15%。但 free-θ 非单调性（50% d < 15% d）暴露 θ-shift confound， 需要 θ-fixed 分析。n=2 clean seeds 不足以精确估计 variance，第三 seed 必须追加。 Memorization fraction 0.35 意味着 theoretical power 是 upper bound，adjusted power ≈ 0.35 × theoretical。\\n\\n\\nMedian 档下 Qwen 作为首个测试家族表现中等偏上。|d|=2.50 @ 15% 处于 median 范围 [1.0, 2.5] 上端， 因为 MMLU 是最大 benchmark（14K items），person-fit power 最强。 50% 条件 d=0.95（borderline large）反映 θ-shift confound——污染提升 θ_MLE 吸收了部分 aberrance 信号， 导致 free-θ 下 dose-response 非单调。clean-vs-clean Δ=0.7 建立 noise floor（远小于 contam Δ）， 确认信号非随机波动。memorization_fraction=0.35 落在 median 范围 [0.25, 0.45] 中部—— QLoRA SFT 不完全记忆，约 35% 污染 items 产生记忆信号，其余被 generalization 平滑。 seen/unseen gap=2.8 是最清晰的 fingerprint：被污染 items 的 lz* 显著低于 unseen items。 只有 2 个 clean seeds（n=2）限制了 Cohen's d 的精度，motivates 第三个 seed。\\n\"\n  },\n  {\n    \"name\": \"Full Controlled Contamination\",\n    \"description\": \"4 模型 (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3) × 6 levels (0/5/10/15/25/50%) × 3 benchmarks (MMLU, GSM8K, HellaSwag)。\\n\",\n    \"results\": {\n      \"qwen_mmlu_d_15pct\": -2.5,\n      \"llama_mmlu_d_15pct\": -2.8,\n      \"gemma_mmlu_d_15pct\": -1.3,\n      \"mistral_mmlu_d_15pct\": -2.2,\n      \"mean_mmlu_d_15pct\": -2.2,\n      \"min_mmlu_d_15pct\": -1.3,\n      \"n_families_d_gt_2_mmlu\": 3,\n      \"qwen_hellaswag_d_15pct\": -1.2,\n      \"llama_hellaswag_d_15pct\": -1.4,\n      \"gemma_hellaswag_d_15pct\": -0.6,\n      \"mistral_hellaswag_d_15pct\": -1.1,\n      \"mean_hellaswag_d_15pct\": -1.08,\n      \"qwen_gsm8k_d_15pct\": -0.9,\n      \"llama_gsm8k_d_15pct\": -1.1,\n      \"gemma_gsm8k_d_15pct\": -0.4,\n      \"mistral_gsm8k_d_15pct\": -0.8,\n      \"mean_gsm8k_d_15pct\": -0.8,\n      \"theta_fixed_monotonic_families_mmlu\": 3,\n      \"theta_fixed_monotonic_families_hellaswag\": 2,\n      \"theta_fixed_monotonic_families_gsm8k\": 2,\n      \"theta_fixed_non_monotonic_family\": \"Gemma (residual non-monotonicity at 50%)\",\n      \"memorization_fraction_mmlu_range\": [\n        0.28,\n        0.42\n      ],\n      \"memorization_fraction_hellaswag_range\": [\n        0.25,\n        0.38\n      ],\n      \"memorization_fraction_gsm8k_range\": [\n        0.22,\n        0.35\n      ],\n      \"n_families_any_benchmark_d_gt_2\": 3,\n      \"weakest_family\": \"Gemma\",\n      \"weakest_family_reason\": \"high baseline ability → smaller θ-shift, lower aberrance signal\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Cohen's d @ 15% Contamination (n=3 seeds, ddof=1, ℓz*-corrected)\",\n        \"columns\": [\n          \"family\",\n          \"MMLU_d\",\n          \"HellaSwag_d\",\n          \"GSM8K_d\",\n          \"θ_fixed_monotonic\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3.5-9B\",\n            -2.5,\n            -1.2,\n            -0.9,\n            \"Yes\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            -2.8,\n            -1.4,\n            -1.1,\n            \"Yes\"\n          ],\n          [\n            \"Gemma-4-31B\",\n            -1.3,\n            -0.6,\n            -0.4,\n            \"No (50% residual)\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            -2.2,\n            -1.1,\n            -0.8,\n            \"Yes\"\n          ],\n          [\n            \"Mean\",\n            -2.2,\n            -1.08,\n            -0.8,\n            \"3/4\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Memorization Fraction by Family × Benchmark\",\n        \"columns\": [\n          \"family\",\n          \"MMLU\",\n          \"HellaSwag\",\n          \"GSM8K\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3.5-9B\",\n            0.38,\n            0.33,\n            0.3\n          ],\n          [\n            \"Llama-3.1-8B\",\n            0.42,\n            0.38,\n            0.35\n          ],\n          [\n            \"Gemma-4-31B\",\n            0.28,\n            0.25,\n            0.22\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            0.36,\n            0.32,\n            0.28\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Dose-Response (MMLU, θ-fixed, ℓz*-corrected)\",\n        \"columns\": [\n          \"family\",\n          \"d_5pct\",\n          \"d_10pct\",\n          \"d_15pct\",\n          \"d_25pct\",\n          \"d_50pct\",\n          \"monotonic\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3.5-9B\",\n            -0.6,\n            -1.4,\n            -2.5,\n            -3.8,\n            -5.2,\n            \"Yes\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            -0.75,\n            -1.6,\n            -2.8,\n            -4.2,\n            -5.8,\n            \"Yes\"\n          ],\n          [\n            \"Gemma-4-31B\",\n            -0.3,\n            -0.7,\n            -1.3,\n            -1.8,\n            -1.6,\n            \"No\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            -0.55,\n            -1.2,\n            -2.2,\n            -3.4,\n            -4.6,\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3/4 家族 MMLU |d|>2.0 确认检测框架跨家族有效，但 Gemma 的 boundary condition 需在论文中显式报告。 HellaSwag/GSM8K 的较低 d 值符合 power ∝ √n_items 理论，strengthens Claim 2。 Gemma 的残余非单调性是 median 档的 key limitation——需在 §6 讨论模型 ability 对检测的调制效应。 跨 benchmark memorization fraction 差异表明 SFT generalization 是 benchmark-dependent 的， 支持 Claim 2 的 caveat（power function 是 upper bound）。\\n\\n\\nMedian 档核心假设：3/4 家族 |d|>2.0 @ 15% on MMLU，1 家族（Gemma）信号较弱。 Gemma-4-31B 作为 31B 模型，baseline ability 高于其他 7-9B 模型，θ_MLE 已较高， contamination 产生的 θ-shift 相对较小，且高能力模型本身对 MMLU hard items 答对率就高， memorization 信号被 genuine ability 遮盖——这是 median 档的典型 boundary condition。 HellaSwag（~10K items）d 值在 [0.8, 1.5] 范围，GSM8K（~1.3K items）d 值在 [0.5, 1.2] 范围， 严格遵循 power ∝ √n_items 的理论预测——n_items 减小直接压低 lz* 的 signal-to-noise ratio。 θ-fixed 在 Qwen/Llama/Mistral 恢复单调性，但 Gemma 因 baseline misfit 较低 + 高 ability， θ-fixed 改善有限，50% 条件仍有残余非单调性。 Memorization fraction 家族间有差异（25-45%），反映不同架构的 SFT generalization 特性不同： Gemma 的 instruction tuning 基础更强，generalization 更好，记忆信号更弱。\\n\"\n  },\n  {\n    \"name\": \"Leaderboard Audit\",\n    \"description\": \"Open LLM Leaderboard v1 大规模 person-fit 扫描。已 ABANDONED（D011: a_r=0.111）。\\n\",\n    \"results\": {\n      \"status\": \"ABANDONED\",\n      \"reason\": \"v1-irt-refit a_r=0.111, item alignment 54.56% → parameters too degraded for audit\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"ABANDONED。在论文 §7 Discussion 中报告：13K+ per-item data publicly available， 但 current IRT estimation methods 的 sample size requirements 限制了大规模审计。 Frame as \\\"the gap between classical IRT and neural IRT estimation\\\" methodological contribution。\\n\\n\\nPath D 已确认 dead：MML-EM 重拟合的 discrimination 参数 a_r=0.111 远低于 0.2 可用阈值， 意味着 v1 leaderboard 参数下的 lz* 基本退化为 accuracy-like statistic， 无法提供 person-fit 特有的 response-pattern-level 信息。 在 median 档下不需要尝试——这是一个已被充分验证的 negative result。 数据可用性（13K+ models）写入 Discussion/Future Work 即可。\\n\"\n  },\n  {\n    \"name\": \"Natural Experiment (base→chat pairs)\",\n    \"description\": \"v1 leaderboard base→chat 模型 pairs，计算 Δlz* 作为 SFT 效应代理。\\n\",\n    \"results\": {\n      \"n_pairs\": 4,\n      \"n_benchmarks\": 4,\n      \"n_significant_benchmarks\": 1,\n      \"significant_benchmark\": \"HellaSwag\",\n      \"hellaswag_mean_delta\": -2.8,\n      \"hellaswag_p_value\": 0.04,\n      \"mmlu_p_value\": 0.22,\n      \"gsm8k_p_value\": 0.18,\n      \"arc_c_p_value\": 0.45,\n      \"individual_outlier_pairs\": 0,\n      \"overall_conclusion\": \"weak_systematic_signal\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Natural Experiment Δlz* (base→chat)\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_pairs\",\n          \"mean_delta\",\n          \"t_stat\",\n          \"p_value\",\n          \"significant\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            4,\n            -1.2,\n            -1.45,\n            0.22,\n            \"No\"\n          ],\n          [\n            \"HellaSwag\",\n            4,\n            -2.8,\n            -2.85,\n            0.04,\n            \"Marginal\"\n          ],\n          [\n            \"GSM8K\",\n            4,\n            1.5,\n            1.62,\n            0.18,\n            \"No\"\n          ],\n          [\n            \"ARC-C\",\n            4,\n            -0.6,\n            -0.82,\n            0.45,\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Underpowered by design (n=4 pairs, a_r degraded)。HellaSwag marginal significance 可能反映 SFT 的系统效应而非 contamination。不影响论文 claims。 Appendix material，mention in §6 as \\\"preliminary evidence consistent with SFT effects on response patterns\\\"。\\n\\n\\nMedian 档下 natural experiment 受限于两个因素： (1) a_r=0.111 使 lz* 退化为 accuracy-like，个体 Δlz* 主要反映 Δaccuracy 而非 response pattern shift； (2) 仅 4-5 usable pairs 无统计检验能力（n 太小无法做 paired t-test with power）。 HellaSwag 可能显示 marginal significance 因为它是最大的非 MMLU benchmark（~10K items）， 但 effect 不强。其他 benchmarks p>0.15。无个体 outlier pair 显示 benchmark-specific contamination。 这是一个 P2-optional 实验，median 档下结论是 \\\"suggestive but underpowered\\\"， 不进入主论文 claims，可在 appendix 报告。\\n\"\n  },\n  {\n    \"name\": \"v1 IRT Refit Expanded\",\n    \"description\": \"扩大 v1 IRT 重拟合至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。\\n\",\n    \"results\": {\n      \"n_models_downloaded\": 520,\n      \"n_models_usable\": 410,\n      \"a_r_3pl\": 0.13,\n      \"a_r_2pl\": -0.02,\n      \"b_r_3pl\": 0.66,\n      \"b_r_spearman\": 0.68,\n      \"fitting_time_sec\": 180,\n      \"conclusion\": \"negative_path_d_dead\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: IRT Refit Comparison (pilot vs expanded)\",\n        \"columns\": [\n          \"metric\",\n          \"pilot_N63\",\n          \"expanded_N500\",\n          \"threshold\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"3PL a_r (Pearson)\",\n            0.111,\n            0.13,\n            \">0.4 viable\",\n            \"FAIL\"\n          ],\n          [\n            \"2PL a_r (Pearson)\",\n            -0.084,\n            -0.02,\n            \">0.4 viable\",\n            \"FAIL\"\n          ],\n          [\n            \"3PL b_r (Pearson)\",\n            0.626,\n            0.66,\n            \">0.5 viable\",\n            \"PASS\"\n          ],\n          [\n            \"3PL b_r (Spearman)\",\n            0.656,\n            0.68,\n            \">0.5 viable\",\n            \"PASS\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Path D 最终关闭。a_r<0.2 at N=500 confirms discrimination failure is structural, not sample-size-driven。 论文 §5 报告为 \\\"IRT parameter estimation challenges\\\"（Claim 3c）， framing: \\\"the gap between classical psychometric sample requirements and the scale needed for neural IRT\\\"。\\n\\n\\nMedian 档预期 a_r 从 0.111（N=63）仅微升至 ~0.13（N=500+），远低于 0.2 可用阈值。 原因：discrimination failure 不是 sample size 问题，而是 LLM response patterns 的结构性特征—— classical IRT 假设 unidimensional latent trait，但 LLMs 的 ability profile 是 multi-dimensional 的 （不同 domain 能力独立变化），导致 item discrimination 在 aggregate 拟合中坍缩。 b_r 稳定在 0.66（difficulty 恢复尚可）进一步确认：问题在 discrimination 而非 difficulty。 这个 negative result 是 methodological contribution——量化了 classical vs neural IRT 的 sample size gap。 N=500 满足 reviewer 要求的阈值，可以最终关闭 Path D。\\n\"\n  },\n  {\n    \"name\": \"4PL vs 3PL Ablation\",\n    \"description\": \"比较 4PL vs 3PL(d=1) 下的检测灵敏度差异，量化 feasibility parameter d 的影响。\\n\",\n    \"results\": {\n      \"far_4pl\": 0.05,\n      \"far_3pl_range\": [\n        0.06,\n        0.14\n      ],\n      \"far_2pl_range\": [\n        0.5,\n        1.0\n      ],\n      \"mean_power_gain_mmlu\": 0.22,\n      \"mean_power_gain_hellaswag\": 0.2,\n      \"mean_power_gain_gsm8k\": 0.16,\n      \"mean_power_gain_arc_c\": 0.11,\n      \"mean_power_gain_humaneval\": 0.1,\n      \"pct_items_d_lt_0.95_mmlu\": 0.46,\n      \"correlation_4pl_3pl_lz\": 0.35\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Detection Power at 25% Contamination by Model\",\n        \"columns\": [\n          \"benchmark\",\n          \"power_4PL\",\n          \"power_3PL\",\n          \"gain_pp\",\n          \"pct_items_d_lt_0.95\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            0.72,\n            0.5,\n            22,\n            \"46%\"\n          ],\n          [\n            \"HellaSwag\",\n            0.48,\n            0.28,\n            20,\n            \"41%\"\n          ],\n          [\n            \"GSM8K\",\n            0.65,\n            0.49,\n            16,\n            \"30%\"\n          ],\n          [\n            \"ARC-C\",\n            0.12,\n            0.08,\n            4,\n            \"22%\"\n          ],\n          [\n            \"HumanEval\",\n            0.28,\n            0.18,\n            10,\n            \"35%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4PL d parameter 对 LLM contamination detection 不可或缺。 Power gain +15-25pp 在论文中用 one sentence 总结即可： \\\"Ignoring the upper asymptote parameter halves detection power on benchmarks with substantial d<0.95 items.\\\" 2PL 的灾难性 FAR 作为 negative control 报告，确认 guessing parameter 同样必要。\\n\\n\\nMedian 档预期 4PL 相对 3PL 的 power gain 在 +15-25pp 范围（略低于 optimistic 的 +25-30pp）。 原因：46% MMLU items 有 d<0.95（从已有 PSN-IRT 参数已知），这些 items 的 upper asymptote <1， high-ability models 在这些 items 上即使全对也不会产生极端 aberrance。 3PL(d=1) 强制 upper asymptote=1，对 high-ability models 系统性高估 expected P(correct)， 导致 false alarm inflation（6-14%）和 lz* 偏移。 相关性 r=0.35 表明 4PL vs 3PL lz* 存在根本性差异，不是简单缩放关系。 2PL 完全不可用（FAR 50-100%）因为同时忽略了 guessing 和 upper asymptote。 这个 ablation 直接支持 method design choice 的合理性。\\n\"\n  },\n  {\n    \"name\": \"Baseline Comparison\",\n    \"description\": \"≥5 baselines 在 ctrl-contam ground-truth 上对比： IRT-FIT, ConStat, Min-K%++, accuracy z-score, PPL-based, random。\\n\",\n    \"results\": {\n      \"auroc_5pct\": {\n        \"lz_star\": 0.65,\n        \"accuracy_zscore\": 0.53,\n        \"mink_pp\": 0.78,\n        \"constat\": 0.72,\n        \"ppl_based\": 0.75,\n        \"random\": 0.5\n      },\n      \"auroc_10pct\": {\n        \"lz_star\": 0.74,\n        \"accuracy_zscore\": 0.58,\n        \"mink_pp\": 0.86,\n        \"constat\": 0.82,\n        \"ppl_based\": 0.83,\n        \"random\": 0.5\n      },\n      \"auroc_15pct\": {\n        \"lz_star\": 0.8,\n        \"accuracy_zscore\": 0.62,\n        \"mink_pp\": 0.92,\n        \"constat\": 0.88,\n        \"ppl_based\": 0.9,\n        \"random\": 0.5\n      },\n      \"auroc_25pct\": {\n        \"lz_star\": 0.86,\n        \"accuracy_zscore\": 0.7,\n        \"mink_pp\": 0.96,\n        \"constat\": 0.93,\n        \"ppl_based\": 0.95,\n        \"random\": 0.5\n      },\n      \"auroc_gap_at_5pct_vs_best\": -0.13,\n      \"auroc_gap_at_15pct_vs_best\": -0.12,\n      \"auroc_gap_at_25pct_vs_best\": -0.1,\n      \"lz_star_ci_width_15pct\": 0.06,\n      \"mink_pp_ci_width_15pct\": 0.04,\n      \"lz_star_rank_at_5pct\": \"2nd (behind Min-K%++)\",\n      \"lz_star_rank_at_15pct\": \"4th\",\n      \"lz_star_beats_accuracy_zscore_all_levels\": true,\n      \"information_access\": {\n        \"lz_star\": \"binary only\",\n        \"accuracy_zscore\": \"binary only\",\n        \"mink_pp\": \"token probs\",\n        \"constat\": \"retest\",\n        \"ppl_based\": \"log-probs\",\n        \"random\": \"none\"\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: AUROC Comparison Across Contamination Levels (MMLU, mean ± 95% CI)\",\n        \"columns\": [\n          \"method\",\n          \"info_access\",\n          \"5%\",\n          \"10%\",\n          \"15%\",\n          \"25%\"\n        ],\n        \"rows\": [\n          [\n            \"Random\",\n            \"—\",\n            \"0.50\",\n            \"0.50\",\n            \"0.50\",\n            \"0.50\"\n          ],\n          [\n            \"Acc z-score\",\n            \"binary\",\n            \"0.53±0.05\",\n            \"0.58±0.05\",\n            \"0.62±0.05\",\n            \"0.70±0.04\"\n          ],\n          [\n            \"lz* (ours)\",\n            \"binary\",\n            \"0.65±0.06\",\n            \"0.74±0.06\",\n            \"0.80±0.06\",\n            \"0.86±0.05\"\n          ],\n          [\n            \"ConStat\",\n            \"retest\",\n            \"0.72±0.04\",\n            \"0.82±0.04\",\n            \"0.88±0.04\",\n            \"0.93±0.03\"\n          ],\n          [\n            \"PPL-based\",\n            \"log-probs\",\n            \"0.75±0.04\",\n            \"0.83±0.04\",\n            \"0.90±0.03\",\n            \"0.95±0.02\"\n          ],\n          [\n            \"Min-K%++\",\n            \"token probs\",\n            \"0.78±0.04\",\n            \"0.86±0.03\",\n            \"0.92±0.03\",\n            \"0.96±0.02\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Information-Access vs Detection-Power Summary\",\n        \"columns\": [\n          \"operating_point\",\n          \"methods\",\n          \"AUROC_15pct_range\",\n          \"information_required\"\n        ],\n        \"rows\": [\n          [\n            \"Minimal\",\n            \"lz*, acc z-score\",\n            \"0.62-0.80\",\n            \"Binary response pattern only\"\n          ],\n          [\n            \"Moderate\",\n            \"ConStat\",\n            \"0.88\",\n            \"Retest with rephrased items\"\n          ],\n          [\n            \"Full\",\n            \"Min-K%++, PPL\",\n            \"0.90-0.92\",\n            \"Token-level probabilities\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"关键叙事：lz* 是 minimal-information frontier 的 champion——在 binary-only 条件下显著优于 accuracy z-score， 且在低污染区间接近 privileged methods。15%+ 的 gap 是 information disadvantage 的直接后果，不是 method failure。 Bootstrap CIs 是论文的差异化优势（6/8 peer papers 不报告 variance）。 Detection frontier figure 是 paper 的 key contribution visualization。\\n\\n\\nMedian 档核心：lz* 在 5% 低污染区间优势明确（0.65 vs accuracy_zscore 0.53，+0.12）， 但 15%+ 区间落后于 Min-K%++/ConStat 10-15% AUROC。 原因分析： (1) lz* @ 5% 优于 accuracy z-score 因为它利用了 response pattern 的 item-level 信息（IRT inductive bias），\\n    而 accuracy z-score 只看 aggregate score；\\n(2) lz* @ 5% 接近 privileged methods（gap 仅 -0.13）因为低污染下 privileged methods 的信号也弱，\\n    lz* 的 IRT structure 作为 inductive bias 部分补偿了 information disadvantage；\\n(3) @ 15%+ lz* 落后因为 privileged methods 获得的额外信息（token probs, retest）\\n    提供了 lz* 无法获取的 fine-grained signal，信息差距随污染增加而放大；\\n(4) AUROC gap [-0.15, -0.05] 在 median 范围，诚实但不灾难性。 narrative 策略：plot information-access vs detection-power frontier curve， 强调 lz* 定义了 \\\"minimal-information operating point\\\" 的价值而非绝对性能。\\n\"\n  },\n  {\n    \"name\": \"Multiscale lzm Statistic\",\n    \"description\": \"实现 Hong, Lin & Cheng (2021) multiscale lzm——跨 benchmark 聚合的标准化 lz* 总分。\\n\",\n    \"results\": {\n      \"lzm_gemini15\": 45.2,\n      \"lzm_vs_per_benchmark_correlation\": 0.92,\n      \"lzm_improvement_over_avg_lz\": \"marginal\",\n      \"n_newly_flagged\": 0,\n      \"n_newly_unflagged\": 0,\n      \"lzm_flagged_rate\": \"57/60 (same as per-benchmark)\",\n      \"lzm_interpretability\": \"lower than per-benchmark (loses benchmark-specific patterns)\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: lzm vs Per-Benchmark lz* for Top Anomalous Models\",\n        \"columns\": [\n          \"model\",\n          \"lzm\",\n          \"mmlu_lz\",\n          \"hellaswag_lz\",\n          \"gsm8k_lz\",\n          \"pattern\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5\",\n            45.2,\n            31.8,\n            -12.3,\n            -8.5,\n            \"Selective (MMLU+, others-)\"\n          ],\n          [\n            \"Yi-Lightning\",\n            52.1,\n            48.2,\n            35.1,\n            22.0,\n            \"Uniform positive\"\n          ],\n          [\n            \"Doubao\",\n            18.3,\n            25.6,\n            -5.2,\n            -10.1,\n            \"Mixed\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"lzm 不增加 detection power，但可在 supplementary 中报告为 alternative aggregation。 论文主体保留 per-benchmark profile 作为 primary presentation。\\n\\n\\nMedian 档下 lzm 提供 marginal improvement：由于 LLM data 已经 universally flagged（57/60）， 聚合统计量无法进一步区分。r=0.92 表明 lzm 与 avg(lz*) 高度相关，额外信息有限。 更重要的是，per-benchmark lz* profile 是 contamination characterization 的核心 （如 Gemini 的 selective vs uniform misfit），而 lzm 聚合丢失了这些 benchmark-specific patterns。 在 median 档下 lzm 是 nice-to-have 但不改变任何 claim，可降为 appendix。\\n\"\n  },\n  {\n    \"name\": \"Post-RL Hypothesis Test\",\n    \"description\": \"Qwen3.5-9B: SFT 污染 → GRPO 训练 → 测试 person-fit 是否保持检测力。\\n\",\n    \"results\": {\n      \"pre_rl_d_15pct\": -2.5,\n      \"post_rl_d_15pct\": -1.1,\n      \"signal_retention_ratio\": 0.44,\n      \"post_rl_lz_star_contam_15\": 6.2,\n      \"post_rl_lz_star_clean\": 7.8,\n      \"post_rl_delta_lz\": -1.6,\n      \"post_rl_p_value\": 0.03,\n      \"post_rl_memorization_fraction\": 0.18,\n      \"grpo_training_steps\": 2000,\n      \"grpo_reward\": \"rule-based (MMLU accuracy on held-out set)\",\n      \"experiment_completed_before_ddl\": \"uncertain\",\n      \"wang_mia_post_rl_auroc\": 0.52,\n      \"lz_star_post_rl_auroc\": 0.62\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Pre- vs Post-RL Detection (Qwen3.5-9B × MMLU @ 15%)\",\n        \"columns\": [\n          \"condition\",\n          \"lz_star\",\n          \"delta_lz\",\n          \"cohens_d\",\n          \"memorization_frac\"\n        ],\n        \"rows\": [\n          [\n            \"Clean\",\n            7.85,\n            \"—\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"SFT-contam (pre-RL)\",\n            5.1,\n            -2.75,\n            -2.5,\n            0.35\n          ],\n          [\n            \"SFT-contam + GRPO (post-RL)\",\n            6.2,\n            -1.6,\n            -1.1,\n            0.18\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table: Post-RL Comparison with Wang et al. MIA Methods\",\n        \"columns\": [\n          \"method\",\n          \"info_access\",\n          \"pre_rl_auroc\",\n          \"post_rl_auroc\",\n          \"retention\"\n        ],\n        \"rows\": [\n          [\n            \"lz* (ours)\",\n            \"binary\",\n            0.8,\n            0.62,\n            \"77.5%\"\n          ],\n          [\n            \"Min-K%++\",\n            \"token probs\",\n            0.92,\n            0.52,\n            \"56.5%\"\n          ],\n          [\n            \"PPL-based\",\n            \"log-probs\",\n            0.9,\n            0.51,\n            \"56.7%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Post-RL |d|=1.10 是 medium-to-large effect——信号衰减但 statistically significant。 若在 DDL 前完成：strengthens paper 显著（unique contribution: only binary method surviving RL）。 若不完整：降为 Discussion，做 structural argument——\\\"RL modifies token distributions but not binary patterns directly, so person-fit retains partial signal where MIA-based methods fail completely\\\"。 无论哪种情况，对 EMNLP 投稿不是 blocking issue。\\n\\n\\nMedian 档核心假设：post-RL 信号衰减但未消失（|d| 0.5-1.5），或实验未在 DDL 前完成。 预测 |d|=1.10（从 pre-RL 2.50 衰减 56%）：GRPO 优化 reward signal 时， RL exploration 部分覆写了 SFT 记忆——模型学会了 \\\"更好的理由\\\" 来选择答案， 而非依赖记忆的 response pattern。但 binary response 层面的 aberrance 不完全消失， 因为 RL 不直接优化 response pattern distribution，只优化 outcome。 memorization_fraction 从 pre-RL ~0.35 降至 ~0.18：RL 使约一半的 \\\"记忆\\\" items 转化为 \\\"理解\\\"。 关键：即使 |d|=1.10 仍然 significant (p=0.03)，而 Wang et al. 证明 MIA methods 完全失效（AUROC≈0.50）。 这就是 binary-level 检测的 structural advantage——RL 改变 token distribution 但不完全消除 aberrant binary patterns。 但 DDL 风险：GRPO 训练需要 reward model setup + 调参 + 多 seed validation，40 GPU-hrs 可能不足。 若不完整，降为 Discussion 中 \\\"structural argument + preliminary evidence\\\"。\\n\"\n  },\n  {\n    \"name\": \"Extra Benchmarks (BBH + MATH)\",\n    \"description\": \"BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。\\n\",\n    \"results\": {\n      \"bbh_power_15pct\": 0.68,\n      \"math_power_15pct\": 0.55,\n      \"bbh_power_vs_theory\": \"within 5%\",\n      \"math_power_vs_theory\": \"within 8%\",\n      \"power_theory_R2_with_extras\": 0.88,\n      \"bbh_4pl_available\": false,\n      \"math_4pl_available\": false,\n      \"bbh_4pl_estimation_needed\": true,\n      \"math_4pl_estimation_needed\": true,\n      \"estimation_gpu_hours\": 8,\n      \"estimation_n_models_needed\": 50\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Power Function Validation with Extended Benchmarks\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"power_15pct_sim\",\n          \"power_15pct_theory\",\n          \"gap\"\n        ],\n        \"rows\": [\n          [\n            \"HumanEval\",\n            164,\n            0.24,\n            0.22,\n            0.02\n          ],\n          [\n            \"ARC-C\",\n            295,\n            0.13,\n            0.15,\n            -0.02\n          ],\n          [\n            \"MATH\",\n            5000,\n            0.55,\n            0.58,\n            -0.03\n          ],\n          [\n            \"BBH\",\n            6511,\n            0.68,\n            0.72,\n            -0.04\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            0.59,\n            0.55,\n            0.04\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            0.75,\n            0.78,\n            -0.03\n          ],\n          [\n            \"MMLU\",\n            14042,\n            0.98,\n            0.98,\n            0.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BBH/MATH 填补 1K-10K gap，strengthens Claim 2 的 power function。 但若 4PL 参数需自行估计，quality concern 可能引入 noise。 如果 PSN-IRT 不包含这些参数，建议降为 appendix 或 future work。 核心 5 benchmarks 已足够支撑 power theory（R²=0.957）。\\n\\n\\nMedian 档下 BBH (6.5K items) 和 MATH (5K items) 落在 power curve 的 \\\"中等\\\" 区间： power@15% 预期 0.55-0.68，验证 power ∝ √n_items 理论在 1K-10K 范围的插值。 BBH > MATH 因为 n_items 多 30%，strictly following the theoretical relationship。 关键挑战：PSN-IRT 可能不包含这些 benchmarks 的 4PL 参数。 如果需要自己估计 4PL，至少需要 50 个模型的 per-item responses + MML-EM fitting， 这引入新的 estimation quality concern（同 Path D 的 a_r 问题）。 Median 档下 R²=0.88（含新 benchmarks）略低于 simulation-only 的 0.957， 反映 SFT generalization gap（theoretical power 是 upper bound，actual power 受 memorization fraction 调制）。 这恰好支持 Claim 2 的 \\\"upper bound\\\" caveat。\\n\"\n  },\n  {\n    \"name\": \"Domain-Level Analysis\",\n    \"description\": \"MMLU domain-level person-fit 分析，识别 Gemini-1.5 等模型的 domain-specific 污染模式。\\n\",\n    \"results\": {\n      \"gemini15_all_domains_flagged\": true,\n      \"gemini15_domain_concentrated\": false,\n      \"gemini15_stem_lz\": 22.0,\n      \"gemini15_humanities_lz\": 18.5,\n      \"gemini15_social_sciences_lz\": 16.2,\n      \"gemini15_other_lz\": 15.8,\n      \"n_models_domain_concentrated\": 2,\n      \"doubao_pattern\": \"Humanities/SocialSci negative, STEM neutral, Other positive\",\n      \"hunyuan_pattern\": \"SocialSci high positive, STEM low\",\n      \"domain_entropy_correlation_with_contamination\": 0.45,\n      \"n_subjects_total\": 57,\n      \"gemini_subjects_flagged\": 52\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table: Domain-Level lz* for Selected Models\",\n        \"columns\": [\n          \"model\",\n          \"STEM\",\n          \"Humanities\",\n          \"Social_Sci\",\n          \"Other\",\n          \"pattern_type\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5\",\n            22.0,\n            18.5,\n            16.2,\n            15.8,\n            \"Uniform positive\"\n          ],\n          [\n            \"Yi-Lightning\",\n            50.1,\n            45.3,\n            48.7,\n            42.0,\n            \"Uniform positive (extreme)\"\n          ],\n          [\n            \"Doubao\",\n            -2.0,\n            -13.0,\n            -14.8,\n            4.4,\n            \"Selective mixed\"\n          ],\n          [\n            \"Hunyuan\",\n            1.8,\n            8.2,\n            13.9,\n            6.5,\n            \"Selective positive\"\n          ],\n          [\n            \"Mistral-Large\",\n            28.5,\n            24.1,\n            22.0,\n            20.3,\n            \"Uniform positive\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain analysis 是 Claim 3 的 supporting evidence：contamination 不仅可以检测， 还可以 characterize（uniform vs selective patterns）。 Ward clustering 可能 reveal contamination typology（2-3 clusters）， 为 \\\"Detection and Characterization\\\" 标题提供直接支撑。 建议作为 §5 case study 的 subsection 呈现。\\n\\nMedian 档下 domain analysis 证实两种 contamination pattern： (1) Uniform contamination (Gemini-1.5): 100% accuracy across all domains，\\n    所有 domain 都 flagged，STEM 略高因为 STEM items 的 discrimination 通常更高\\n    （item difficulty variance 更大），产生更强的 aberrance signal。\\n(2) Selective contamination (Doubao, Hunyuan): domain-specific misfit patterns，\\n    某些 domain positive lz*（over-consistent，可能是 domain-specific training data exposure），\\n    某些 domain negative lz*（aberrant，可能是 domain mismatch）。\\nDomain entropy 与 contamination severity 的 moderate correlation (r=0.45) 表明 更均匀的 domain misfit 通常伴随更高的整体 contamination 程度——但不是强关系， 因为 SFT 的 generalization 跨 domain 不均匀。\\n\"\n  }\n]",
      "numLines": 915,
      "startLine": 1,
      "totalLines": 915
    }
  },
  "sourceToolAssistantUUID": "4c0edc9a-b470-486d-8020-fd70b5d7165b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T03:54:30.607Z_

<details><summary>↩ Tool result · `toolu_01HtVA2sEiyPMion5JN5CA3A`</summary>

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
10	**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted ("expected") power. Both upper bound and adjusted power should be reported.
15	
16	**Claim 3 (Empirical Findings from Real LLM Data)**:
17	Three empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit."
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
42	| R4 | "Only 12 models" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |
43	| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
44	| R6 | "Absolute lz* thresholds don't work on real data" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |
45	| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
46	| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
47	| R9 | "No same-level binary-only baselines" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |
48	| R10 | "Leaderboard audit baseline unreliable" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |
49	| R11 | "Power function is upper bound" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |
50	
51	## Key Narrative Elements (from External Review + Distillation)
52	
53	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
54	2. **Definitional pivot (à la ConStat)** — "All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?" This reframes our work as problem reformulation, not just cross-domain transfer.
55	3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.
56	4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim "leaderboard audit" or "large-scale detection" in current paper.
57	5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.
58	6. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
59	7. **Terminology guard** — NEVER use "binary information bottleneck" or "information-theoretic lower bound for all binary-only methods." We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: "IRT person-fit as a principled framework at the minimal-information operating point."
60	8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.
61	9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.
62	10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are "honest negative results that become positive contributions": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: "the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative."
63	11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as "principled detection with quantified operating characteristics + θ-shift boundary condition." Headline: "We don't just detect — we characterize, including the conditions under which detection degrades." Do NOT claim "state-of-the-art detection."
64	12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.
65	13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look "normal") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.
66	
67	## Writing Strategy (from Distillation)
68	
69	- **Story type**: "跨界迁移型" — unused in 0/8 peer papers. Our unique angle.
70	- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).
71	- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.
72	- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.
73	- **Numbered findings**: Adopt PSN-IRT's "Key Discoveries" strategy for scannable presentation.
74	- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.
75	- **Baseline count**: Peer median ~5. Target ≥5 baselines.
76	
77	## Evidence Summary
78	
79	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
80	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.
81	- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).
82	- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.
83	- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.
84	- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = "θ_fixed repairs non-monotonicity"; Llama story = "θ_fixed enhances existing monotonicity". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.
85	- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c93a4f02-1ed3-4ec0-a2d2-b9cf86a839c6",
  "isSidechain": false,
  "promptId": "ec7c9be7-428e-4670-904e-cc8df713932d",
  "type": "user",
  "uuid": "2f71e836-b23b-4f62-8d39-1e3a262890f6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/paper_framing.md",
      "content": "# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.\n6. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n7. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.\n- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = \"θ_fixed repairs non-monotonicity\"; Llama story = \"θ_fixed enhances existing monotonicity\". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  },
  "sourceToolAssistantUUID": "c93a4f02-1ed3-4ec0-a2d2-b9cf86a839c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T03:54:30.602Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HtVA2sEiyPMion5JN5CA3A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0546097c-91ab-42f8-bf0a-f6e3e3aaeb07",
  "isSidechain": false,
  "requestId": "req_011CbF3BFcPFKzHQ4Fa3hstG",
  "type": "assistant",
  "uuid": "c93a4f02-1ed3-4ec0-a2d2-b9cf86a839c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqiX2eb7Ztp2DwtNztAqix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11759,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11759
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit…",
  "leafUuid": "2f71e836-b23b-4f62-8d39-1e3a262890f6",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit detection of benchmark contamination",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---

### Assistant

_source line 14 · 2026-05-21T03:55:27.473Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me also read the paper writing norms skill to ensure I follow the right conventions, and check what LaTeX packages are available.

Actually, given the instruction to be concise and direct, let me just proceed to write the paper. I have all the information I need.

Let me plan the paper structure:

1. **Abstract** - Summarize the problem, method, key results
2. **Introduction** - Problem, gap, our approach, contributions
3. **Background** - IRT, person-fit statistics, 4PL model


4. **Method** - Detection framework, lz* statistic, θ-fixed analysis, Δlz* design
5. **Experiments** - I'll organize this around the main experimental themes: controlled contamination studies, model comparisons between 4PL and 3PL, baseline comparisons, power function analysis, domain-level analysis, and post-RL hypothesis testing
6. **Discussion**

Now I'm realizing I need to account for all eleven experiments across the paper, including the leaderboard audit, natural experiment with base-to-chat model pairs, IRT refit analysis, and the multiscale lzm statistic work. Let me restructure to ensure every experiment gets proper coverage in the results and discussion sections.

7. **Conclusion** - §6.4: Multiscale lzm (exp 8)

Now I'm ready to write the paper itself. I need to pull exact numbers from experiment_data.json without any fabrication, include results tables for each experiment, and structure everything around the core narrative of a principled detection framework with well-characterized operating conditions. The target is 8 pages for EMNLP 2026 in standard ACL format, so I'll set up the LaTeX document with proper styling and begin drafting the sections.

My approach: map the narrative claims directly to the experimental evidence. Detection succeeds across three of four families at |d| > 2.0 with 15% contamination, while one family shows weaker performance in the 1.0-2.0 range. The HellaSwag and GSM8K effects are substantial but constrained by item counts. The θ-fixed condition mostly restores monotonicity. I'll present the baseline comparison honestly, highlighting the information-access versus detection-power tradeoff and emphasizing why the minimal-information operating point matters. Post-RL results stay in the Discussion as structural reasoning plus preliminary findings. The title frames this as "Detection and Characterization of Benchmark Contamination via IRT Person-Fit."

Writing the full LaTeX document now... Writing the LaTeX paper structure... .5 Detection Power Function (Table from exp 10)
   5.6 Domain-Level Analysis (Table from exp 11)
6. Discussion
   6.1 Post-RL Robustness (Tables from exp 9)
   6.2 IRT Parameter Estimation Challenges (Table from exp 5)
   6.3 Natural Experiment (Table from exp 4)
   6.4 Multiscale Aggregation (Table from exp 8)
   6.5 Leaderboard Audit Challenges (exp 3)
   6.6 Limitations
7. Conclusion

Good, that covers all 11 experiments. Now I'm mapping out which tables I need to generate — starting with the pilot summary showing effect sizes, then Cohen's d values at the 15% contamination level, and continuing through the memorization fractions. Now I'm realizing this is way too many tables for an 8-page paper, so I need to be more selective. I'll keep the most critical ones that establish the method, show the core results, and support my main claims—the pilot results, contamination findings, dose-response validation, method ablation, competitive baseline, and power function evidence. I've decided to include all the tables since the paper doesn't have strict page limits and the instructions call for covering every experiment. Now I'm setting up the LaTeX document with a standard article class and basic geometry settings for readability, then I'll write out the full paper in one go. Let me also make sure the output directory is ready before I start generating the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f71e836-b23b-4f62-8d39-1e3a262890f6",
  "isSidechain": false,
  "requestId": "req_011CbF3BZPTnCoV8WaCrvZk2",
  "type": "assistant",
  "uuid": "2276b8ec-4f36-44de-8cc0-6eea48f28776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011m48R7trjNKhpkCpPguwPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20355,
      "cache_read_input_tokens": 23600,
      "output_tokens": 2858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2858,
          "cache_read_input_tokens": 23600,
          "cache_creation_input_tokens": 20355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20355
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

_source line 15 · 2026-05-21T03:55:27.475Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2276b8ec-4f36-44de-8cc0-6eea48f28776",
  "isSidechain": false,
  "requestId": "req_011CbF3BZPTnCoV8WaCrvZk2",
  "type": "assistant",
  "uuid": "a27fce7c-eb3c-484d-a0c4-33706eb0859d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011m48R7trjNKhpkCpPguwPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20355,
      "cache_read_input_tokens": 23600,
      "output_tokens": 2858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2858,
          "cache_read_input_tokens": 23600,
          "cache_creation_input_tokens": 20355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20355
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

_source line 16 · 2026-05-21T03:55:28.605Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QBrgH3PPFMM1rLE8DcfN4n`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/",
  "description": "Check output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a27fce7c-eb3c-484d-a0c4-33706eb0859d",
  "isSidechain": false,
  "requestId": "req_011CbF3BZPTnCoV8WaCrvZk2",
  "type": "assistant",
  "uuid": "d1c7e449-34fc-4e76-a182-285161ed9743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011m48R7trjNKhpkCpPguwPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20355,
      "cache_read_input_tokens": 23600,
      "output_tokens": 2858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20355,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2858,
          "cache_read_input_tokens": 23600,
          "cache_creation_input_tokens": 20355,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20355
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

_source line 17 · 2026-05-21T03:55:28.765Z_

<details><summary>↩ Tool result · `toolu_01QBrgH3PPFMM1rLE8DcfN4n`</summary>

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
  "parentUuid": "d1c7e449-34fc-4e76-a182-285161ed9743",
  "isSidechain": false,
  "promptId": "ec7c9be7-428e-4670-904e-cc8df713932d",
  "type": "user",
  "uuid": "4086a307-07c6-4f0c-a55e-2163dae0c52b",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d1c7e449-34fc-4e76-a182-285161ed9743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-21T03:55:42.797Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now let me write the full LaTeX paper. I'll be comprehensive and include all experiments with their tables.

Let me carefully construct the paper now. I need to use the exact numbers from experiment_data.json.

Key numbers to use:
- Pilot: clean lz*=7.85±0.49, contam_15 lz*=5.1, Δ=-2.75, d=-2.5, contam_50 lz*=6.8, Δ=-1.05, d=-0.95
- Full: Qwen MMLU d=-2.5, Llama d=-2.8, Gemma d=-1.3, Mistral d=-2.2; 3/4 |d|>2.0


- 4PL vs 3PL: MMLU power 0.72 vs 0.50, +22pp gain
- Baselines: lz* AUROC@15%=0.80, Min-K++=0.92, ConStat=0.88, PPL=0.90, Acc z=0.62
- Power function: R²=0.88, BBH power=0.68, MATH=0.55
- Domain: Gemini STEM=22.0, Humanities=18.5, etc.
- Post-RL: pre d=-2.5, post d=-1.1, retention 44%
- Post-RL performance shows lz* dropping to 0.62 AUROC while Min-K++ falls further to 0.52, and the IRT refit reveals the discrimination parameter fails but the difficulty parameter holds up. The natural experiment on HellaSwag shows marginal significance, with other benchmarks not reaching statistical significance. The lzm variant maintains strong correlation at 0.92 with per-benchmark metrics, though the gains are modest.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4086a307-07c6-4f0c-a55e-2163dae0c52b",
  "isSidechain": false,
  "requestId": "req_011CbF3FqnZY7hgPBbD9rm5S",
  "type": "assistant",
  "uuid": "91b05b18-c5af-4ffa-8aa6-9428cac02977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYKUTPLJ2bJ2iwTSXHdMxN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2879,
      "cache_read_input_tokens": 43955,
      "output_tokens": 12858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12858,
          "cache_read_input_tokens": 43955,
          "cache_creation_input_tokens": 2879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2879
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

_source line 19 · 2026-05-21T03:55:42.800Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91b05b18-c5af-4ffa-8aa6-9428cac02977",
  "isSidechain": false,
  "requestId": "req_011CbF3FqnZY7hgPBbD9rm5S",
  "type": "assistant",
  "uuid": "d9db0131-cb1b-4ac0-9003-fcc75667ddb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYKUTPLJ2bJ2iwTSXHdMxN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2879,
      "cache_read_input_tokens": 43955,
      "output_tokens": 12858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12858,
          "cache_read_input_tokens": 43955,
          "cache_creation_input_tokens": 2879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2879
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

_source line 20 · 2026-05-21T03:59:37.939Z_

<details open><summary>🔧 Tool call — Write · `toolu_012GCRuehTc61S8ZrYd6evFv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{caption}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\title{Detection and Characterization of Benchmark Contamination\\\\via IRT Person-Fit Statistics}\n\n\\author{\n  Anonymous Submission\n}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nBenchmark contamination undermines the reliability of LLM evaluation, yet all existing detection methods require privileged access to token probabilities, model weights, or specially crafted prompts.\nWe establish a \\emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics---originally developed for detecting exam cheating---to identify anomalous LLM response patterns using only binary (correct/incorrect) outcomes.\nWe formalize a detection framework based on the $\\ell_z^*$ statistic under a 4-parameter logistic (4PL) IRT model and validate it through controlled contamination experiments across four model families (Qwen, Llama, Gemma, Mistral) and three benchmarks (MMLU, HellaSwag, GSM8K).\nAt 15\\% contamination, the framework achieves $|\\text{Cohen's } d| > 2.0$ in three of four model families on MMLU, with the fourth (Gemma) showing a weaker but detectable signal ($|d|=1.3$).\nDetection power follows a predictable function of benchmark size ($R^2=0.88$), and a $\\theta$-fixed analysis recovers monotonic dose-response curves in three of four families.\nIn baseline comparisons, $\\ell_z^*$ achieves AUROC 0.80 at 15\\% contamination using only binary data, compared to 0.92 for Min-K\\%++ (requiring token probabilities) and 0.62 for accuracy z-scores---defining the best achievable detection at the minimal-information level.\nPreliminary evidence suggests $\\ell_z^*$ retains partial detection signal after reinforcement learning ($|d|=1.1$, AUROC 0.62), where token-probability methods degrade to chance.\nDomain-level analysis reveals distinct contamination typologies (uniform vs.\\ selective), enabling contamination characterization beyond binary detection.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nBenchmark contamination---the presence of evaluation data in model training corpora---poses a fundamental threat to the integrity of LLM evaluation \\citep{sainz2023chatgpt,magar2022data}.\nAs benchmarks proliferate and training corpora scale to trillions of tokens, the risk of inadvertent or intentional contamination grows.\nLeaderboard rankings, model selection decisions, and research conclusions all depend on benchmark scores reflecting genuine capability rather than memorization artifacts.\n\nA growing literature addresses contamination detection, spanning time-based partition methods, membership inference attacks (MIA/Min-K\\%++; \\citealp{shi2024detecting}), probing techniques (Time Travel; \\citealp{deng2024investigating}), performance-based testing (ConStat; \\citealp{oren2024proving}), and in-context learning effects (CoDeC; \\citealp{dong2024codec}).\nHowever, all existing methods require more than binary response patterns: token-level probabilities, log-likelihoods, model weights, or access to rephrase benchmark items.\nFurthermore, \\citet{wang2025rlcontam} demonstrate that all ten log-probability-based methods they evaluate degrade to near-random performance on RL-trained reasoning models, exposing a structural vulnerability in the dominant detection paradigm.\n\nWe address a more fundamental question: \\emph{what can be detected from binary response patterns alone?}\nThis question is practically motivated---binary outcomes (correct/incorrect on benchmark items) are available for any model on any benchmark, including proprietary APIs and historical leaderboard submissions.\nIt is also theoretically grounded: a contaminated LLM producing anomalous response patterns is functionally analogous to an examinee with item preknowledge, a problem studied for decades in psychometrics.\n\nWe establish the minimal-information operating point on the contamination detection frontier by adapting IRT person-fit statistics \\citep{drasgow1985appropriateness,snijders2001item} to LLM benchmark evaluation.\nOur framework uses the $\\ell_z^*$ statistic under a 4-parameter logistic (4PL) IRT model, which captures both guessing and ceiling effects critical for modeling LLM responses.\nThrough controlled contamination experiments (QLoRA SFT injection across four model families), we validate the framework and characterize its operating conditions:\n\n\\begin{enumerate}\n\\item \\textbf{Principled detection with characterized conditions.} At 15\\% contamination, detection achieves $|\\text{Cohen's } d| > 2.0$ in three of four model families on MMLU.\nThe fourth family (Gemma-4-31B) shows a weaker signal ($|d|=1.3$), a boundary condition attributable to high baseline ability.\nA $\\theta$-fixed analysis recovers monotonic dose-response in three of four families.\n\n\\item \\textbf{Predictable detection power.} Power is a monotonic function of benchmark size ($n_\\text{items}$) and contamination level, following theoretical predictions with $R^2=0.88$ across seven benchmarks spanning 164--14,042 items.\n\n\\item \\textbf{Empirical findings.} Applying person-fit to real LLM data reveals universal 4PL model misfit (57/60 model--benchmark cells flagged), domain-level contamination typologies (uniform vs.\\ selective), and IRT parameter estimation challenges that quantify the gap between classical and neural IRT.\n\\end{enumerate}\n\n% ============================================================\n\\section{Background}\n\n\\subsection{Item Response Theory and the 4PL Model}\n\nIRT models the probability of a correct response as a function of person ability ($\\theta$) and item parameters.\nThe 4-parameter logistic (4PL) model specifies:\n\\begin{equation}\nP(X_{ij}=1 \\mid \\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is item discrimination, $b_i$ is item difficulty, $c_i$ is the guessing (lower asymptote) parameter, and $d_i$ is the upper asymptote (ceiling) parameter.\nThe 3PL model sets $d_i=1$; the 2PL further sets $c_i=0$.\n\nFor LLM evaluation, the $d_i$ parameter is critical: many items have $d_i < 1$, meaning even high-ability models may not achieve perfect performance due to item-specific confounds (ambiguous wording, multiple defensible answers).\nIgnoring this parameter systematically inflates expected performance for high-ability models.\n\n\\subsection{Person-Fit Statistics}\n\nPerson-fit statistics detect response patterns that are improbable given estimated ability.\nThe $\\ell_z^*$ statistic \\citep{snijders2001item} is the standardized log-likelihood of an individual's response pattern:\n\\begin{equation}\n\\ell_z^* = \\frac{\\ell_0 - E[\\ell_0]}{\\sqrt{\\text{Var}[\\ell_0]}}\n\\label{eq:lzstar}\n\\end{equation}\nwhere $\\ell_0 = \\sum_{i=1}^{n} [x_i \\log P_i + (1-x_i) \\log(1-P_i)]$ is the log-likelihood of observed responses $\\{x_i\\}$ given model-predicted probabilities $\\{P_i\\}$.\nUnder the null hypothesis (responses generated by the IRT model), $\\ell_z^* \\sim \\mathcal{N}(0,1)$ asymptotically.\n\nTwo response anomaly types are relevant:\n\\begin{itemize}\n\\item \\textbf{Aberrant patterns} ($\\ell_z^* \\ll 0$): unexpected responses given ability---e.g., a high-ability model failing easy items while succeeding on hard ones. Partial contamination (memorizing a subset of items) produces this signature.\n\\item \\textbf{Over-consistent patterns} ($\\ell_z^* \\gg 0$): responses more consistent with the model than expected---e.g., perfect accuracy with $\\theta$ far below what perfect performance would require. Complete contamination produces this signature.\n\\end{itemize}\n\n\\subsection{Contamination as Item Preknowledge}\n\nIn psychometrics, item preknowledge refers to examinees who have advance access to test items.\nSuch examinees produce anomalous response patterns: they answer ``preknown'' items correctly regardless of difficulty, while their performance on unknown items reflects genuine ability.\nThis creates a detectable mismatch between observed and expected response patterns---precisely what $\\ell_z^*$ measures.\n\nLLM benchmark contamination through SFT on benchmark items is functionally identical: the model memorizes a subset of items, producing correct responses independent of item difficulty, while generalizing from training on the remaining items.\nThe memorization fraction---the proportion of contaminated items that produce memorized (rather than generalized) responses---determines the strength of the person-fit signal.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Detection Framework}\n\nOur detection framework operates in three stages:\n\n\\textbf{Stage 1: IRT Parameter Estimation.}\nGiven binary response matrices from a reference population of LLMs on benchmark items, we estimate 4PL item parameters $(a_i, b_i, c_i, d_i)$ using marginal maximum likelihood with an EM algorithm.\nWe use pre-estimated parameters from PSN-IRT \\citep{psnirt2026} where available, ensuring parameter quality is independent of our detection procedure.\n\n\\textbf{Stage 2: Person-Fit Computation.}\nFor a target model with response vector $\\mathbf{x} = (x_1, \\ldots, x_n)$ on $n$ benchmark items, we estimate ability $\\hat{\\theta}$ via maximum likelihood and compute $\\ell_z^*$ (Eq.~\\ref{eq:lzstar}).\n\n\\textbf{Stage 3: $\\Delta\\ell_z^*$ Analysis.}\nSince LLM response patterns universally deviate from 4PL predictions (Section~\\ref{sec:universal-misfit}), absolute $\\ell_z^*$ thresholds are uninformative for contamination detection.\nInstead, we compute the within-model shift:\n\\begin{equation}\n\\Delta\\ell_z^* = \\ell_z^*(\\text{contaminated}) - \\overline{\\ell_z^*}(\\text{clean baselines})\n\\end{equation}\nstandardized by the clean-baseline variance (Cohen's $d$).\nThe well-calibrated bootstrap null ensures that $\\Delta\\ell_z^*$ is statistically interpretable.\n\n\\subsection{$\\theta$-Fixed Analysis}\n\nA methodological contribution of this work is identifying the $\\theta$-shift confound: when $\\theta$ is re-estimated on contaminated data, the increased accuracy raises $\\hat{\\theta}$, which partially absorbs the aberrance signal.\nThis can produce non-monotonic dose-response under free-$\\theta$ estimation (higher contamination $\\not\\Rightarrow$ larger $|\\Delta\\ell_z^*|$).\n\nWe address this via $\\theta$-fixed analysis: fixing $\\theta$ to the pre-contamination baseline estimate $\\hat{\\theta}_\\text{clean}$ and recomputing $\\ell_z^*$.\nThis isolates the response-pattern anomaly from ability shift, recovering monotonic dose-response in most model families.\n\n\\subsection{Detection Power Theory}\n\nDetection power depends on three factors: benchmark size ($n_\\text{items}$), contamination level ($\\rho$), and memorization fraction ($\\phi$).\nTheoretical power under the 4PL model follows:\n\\begin{equation}\n\\text{Power} \\propto \\Phi\\!\\left(\\frac{\\phi \\cdot \\rho \\cdot \\sqrt{n_\\text{items}} \\cdot \\bar{a}}{\\sigma_{\\ell_z^*}}\\right)\n\\end{equation}\nwhere $\\bar{a}$ is mean item discrimination and $\\Phi$ is the standard normal CDF.\nThis gives an upper bound assuming all memorized items produce maximal aberrance; the memorization fraction $\\phi$ adjusts for SFT generalization.\n\n% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Models and Benchmarks}\n\n\\textbf{Controlled contamination.}\nWe use four model families: Qwen3.5-9B, Llama-3.1-8B, Gemma-4-31B, and Mistral-7B-v0.3.\nFor each family, we create contaminated variants via QLoRA SFT on benchmark items at six contamination levels: 0\\% (clean, 3 seeds), 5\\%, 10\\%, 15\\%, 25\\%, and 50\\%.\nThree benchmarks serve as contamination targets: MMLU (14,042 items), HellaSwag (10,042 items), and GSM8K (1,319 items).\n\n\\textbf{Real-data analysis.}\nWe analyze 12 models with validated 4PL parameters from PSN-IRT across five benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval).\n\n\\subsection{IRT Parameters}\n\nItem parameters are sourced from PSN-IRT \\citep{psnirt2026}, which provides validated 4PL estimates for major benchmarks.\nFor the power function validation (Section~\\ref{sec:power}), BBH and MATH require separate 4PL estimation from 50+ model responses.\n\n\\subsection{Baselines}\n\nWe compare against five baselines spanning the information-access spectrum:\n\\begin{itemize}\n\\item \\textbf{Accuracy z-score} (binary): standardized accuracy relative to population mean.\n\\item \\textbf{ConStat} (retest): performance-based testing with rephrased items \\citep{oren2024proving}.\n\\item \\textbf{PPL-based} (log-probs): perplexity-based detection using model log-probabilities.\n\\item \\textbf{Min-K\\%++} (token probs): token-probability-based MIA \\citep{shi2024detecting}.\n\\item \\textbf{Random}: uniform random baseline.\n\\end{itemize}\n\n\\subsection{Evaluation Metrics}\n\nPrimary: Cohen's $d$ (effect size between clean and contaminated $\\ell_z^*$), AUROC (discrimination between clean and contaminated models).\nAll Cohen's $d$ values computed with $n=3$ clean seeds, $\\text{ddof}=1$, on $\\ell_z^*$-corrected values.\nBootstrap 95\\% confidence intervals reported where applicable.\n\n% ============================================================\n\\section{Results}\n\n\\subsection{Controlled Contamination Pilot}\n\\label{sec:pilot}\n\nWe first validate the detection framework on a single model--benchmark pair (Qwen3.5-9B $\\times$ MMLU) with four conditions.\nTable~\\ref{tab:pilot} summarizes the results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pilot $\\Delta\\ell_z^*$ summary (Qwen3.5-9B $\\times$ MMLU). $\\ell_z^*$ corrected per \\citet{snijders2001item}. Cohen's $d$ relative to clean mean ($n=2$, $\\text{ddof}=1$).}\n\\label{tab:pilot}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & $\\ell_z^*$ & $\\Delta\\ell_z^*$ & $d$ & Acc & Mem.\\ frac \\\\\n\\midrule\nClean-s1 & 8.20 & --- & --- & .679 & --- \\\\\nClean-s2 & 7.50 & --- & --- & .681 & --- \\\\\nContam-15\\% & 5.10 & $-2.75$ & $-2.50$ & .720 & .35 \\\\\nContam-50\\% & 6.80 & $-1.05$ & $-0.95$ & .760 & .28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 15\\% contamination condition produces $|d|=2.50$, a large effect, confirming that person-fit detects the injected contamination signal.\nThe clean-vs-clean difference ($\\Delta=0.70$) establishes a noise floor well below the contamination signal.\nCritically, the free-$\\theta$ dose-response is \\emph{non-monotonic}: the 50\\% condition ($|d|=0.95$) produces a weaker signal than 15\\% ($|d|=2.50$).\nThis motivates the $\\theta$-fixed analysis (Section~\\ref{sec:full-contam}).\n\nThe memorization fraction of 0.35 at 15\\% contamination indicates that approximately 35\\% of injected items produce memorization signatures, while the remainder are absorbed by SFT generalization.\nThe seen/unseen $\\ell_z^*$ gap of 2.8 provides the clearest contamination fingerprint: items present in training show expected response patterns, while unseen items exhibit aberrant patterns.\n\n\\subsection{Full Controlled Contamination}\n\\label{sec:full-contam}\n\nWe extend to four model families and three benchmarks.\nTable~\\ref{tab:full-d} presents Cohen's $d$ at 15\\% contamination, and Table~\\ref{tab:dose-response} shows the full dose-response curve on MMLU under $\\theta$-fixed analysis.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cohen's $d$ at 15\\% contamination ($n=3$ seeds, $\\text{ddof}=1$, $\\ell_z^*$-corrected). $\\theta$-fixed monotonicity indicates whether $|d|$ increases monotonically across all contamination levels under fixed-$\\theta$ analysis.}\n\\label{tab:full-d}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nFamily & MMLU & HellaSwag & GSM8K & $\\theta$-mono \\\\\n\\midrule\nQwen3.5-9B & $-2.50$ & $-1.20$ & $-0.90$ & Yes \\\\\nLlama-3.1-8B & $-2.80$ & $-1.40$ & $-1.10$ & Yes \\\\\nGemma-4-31B & $-1.30$ & $-0.60$ & $-0.40$ & No \\\\\nMistral-7B-v0.3 & $-2.20$ & $-1.10$ & $-0.80$ & Yes \\\\\n\\midrule\nMean & $-2.20$ & $-1.08$ & $-0.80$ & 3/4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree of four families achieve $|d| > 2.0$ on MMLU at 15\\% contamination.\nGemma-4-31B is the exception ($|d|=1.3$), attributable to its higher baseline ability: as a 31B model, its $\\hat{\\theta}$ is already high, reducing the marginal $\\theta$-shift from contamination and producing a weaker aberrance signal.\nThis represents a characterized boundary condition rather than a framework failure.\n\nDetection strength decreases from MMLU (mean $|d|=2.20$) to HellaSwag ($|d|=1.08$) to GSM8K ($|d|=0.80$), consistent with the theoretical dependence on $n_\\text{items}$: MMLU has 14K items, HellaSwag 10K, and GSM8K 1.3K.\n\n\\begin{table}[t]\n\\centering\n\\caption{Dose-response on MMLU under $\\theta$-fixed analysis ($\\ell_z^*$-corrected Cohen's $d$). Monotonic increase in $|d|$ with contamination level is expected under the framework.}\n\\label{tab:dose-response}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nFamily & 5\\% & 10\\% & 15\\% & 25\\% & 50\\% & Mono \\\\\n\\midrule\nQwen3.5-9B & $-0.60$ & $-1.40$ & $-2.50$ & $-3.80$ & $-5.20$ & Yes \\\\\nLlama-3.1-8B & $-0.75$ & $-1.60$ & $-2.80$ & $-4.20$ & $-5.80$ & Yes \\\\\nGemma-4-31B & $-0.30$ & $-0.70$ & $-1.30$ & $-1.80$ & $-1.60$ & No \\\\\nMistral-7B & $-0.55$ & $-1.20$ & $-2.20$ & $-3.40$ & $-4.60$ & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\theta$-fixed analysis recovers monotonic dose-response in Qwen, Llama, and Mistral (Table~\\ref{tab:dose-response}).\nGemma retains residual non-monotonicity at 50\\% ($|d|=1.6 < |d|_{25\\%}=1.8$), consistent with its high baseline ability creating a ceiling effect on the person-fit signal.\n\nTable~\\ref{tab:mem-frac} reports memorization fractions, which range from 0.22 (Gemma, GSM8K) to 0.42 (Llama, MMLU), reflecting architecture-dependent SFT generalization.\nGemma consistently shows the lowest memorization fractions, indicating stronger generalization from instruction tuning---which paradoxically weakens the contamination detection signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Memorization fraction by model family and benchmark (at 15\\% contamination). Higher values indicate more items producing memorization rather than generalization signatures.}\n\\label{tab:mem-frac}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nFamily & MMLU & HellaSwag & GSM8K \\\\\n\\midrule\nQwen3.5-9B & .38 & .33 & .30 \\\\\nLlama-3.1-8B & .42 & .38 & .35 \\\\\nGemma-4-31B & .28 & .25 & .22 \\\\\nMistral-7B-v0.3 & .36 & .32 & .28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{4PL vs 3PL Ablation}\n\\label{sec:4pl-ablation}\n\nWe evaluate whether the 4PL upper asymptote parameter $d_i$ is necessary for contamination detection by comparing 4PL against 3PL ($d_i=1$) and 2PL ($c_i=0, d_i=1$).\nTable~\\ref{tab:4pl-ablation} reports detection power at 25\\% contamination.\n\n\\begin{table}[t]\n\\centering\n\\caption{Detection power at 25\\% contamination: 4PL vs 3PL($d{=}1$). Gain in percentage points (pp). The last column shows the fraction of items with $d_i < 0.95$, which drives the 4PL advantage.}\n\\label{tab:4pl-ablation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & 4PL & 3PL & Gain (pp) & $d{<}0.95$ \\\\\n\\midrule\nMMLU & .72 & .50 & +22 & 46\\% \\\\\nHellaSwag & .48 & .28 & +20 & 41\\% \\\\\nGSM8K & .65 & .49 & +16 & 30\\% \\\\\nARC-C & .12 & .08 & +4 & 22\\% \\\\\nHumanEval & .28 & .18 & +10 & 35\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 4PL model provides a 10--22 percentage point power advantage over 3PL across benchmarks.\nThe gain correlates with the proportion of items having $d_i < 0.95$: MMLU (46\\% such items) shows the largest gain (+22pp).\nIgnoring the upper asymptote systematically overestimates expected performance for high-ability models, inflating false alarm rates from the nominal 5\\% to 6--14\\% under 3PL.\nThe 2PL model is unusable, with false alarm rates of 50--100\\% (not shown), confirming that both the guessing and ceiling parameters are essential for LLM person-fit analysis.\n\nThe correlation between 4PL and 3PL $\\ell_z^*$ values is only $r=0.35$, indicating these are fundamentally different measurements rather than scaled versions of each other.\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} compares detection performance across contamination levels on MMLU using the controlled contamination ground truth.\n\n\\begin{table}[t]\n\\centering\n\\caption{AUROC comparison across contamination levels (MMLU, mean $\\pm$ 95\\% bootstrap CI). Methods ordered by information access level.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Info & 5\\% & 10\\% & 15\\% & 25\\% \\\\\n\\midrule\nRandom & --- & .50 & .50 & .50 & .50 \\\\\nAcc z & bin & .53{\\scriptsize$\\pm$.05} & .58{\\scriptsize$\\pm$.05} & .62{\\scriptsize$\\pm$.05} & .70{\\scriptsize$\\pm$.04} \\\\\n$\\ell_z^*$ & bin & .65{\\scriptsize$\\pm$.06} & .74{\\scriptsize$\\pm$.06} & .80{\\scriptsize$\\pm$.06} & .86{\\scriptsize$\\pm$.05} \\\\\nConStat & ret & .72{\\scriptsize$\\pm$.04} & .82{\\scriptsize$\\pm$.04} & .88{\\scriptsize$\\pm$.04} & .93{\\scriptsize$\\pm$.03} \\\\\nPPL & lp & .75{\\scriptsize$\\pm$.04} & .83{\\scriptsize$\\pm$.04} & .90{\\scriptsize$\\pm$.03} & .95{\\scriptsize$\\pm$.02} \\\\\nMin-K++ & tok & .78{\\scriptsize$\\pm$.04} & .86{\\scriptsize$\\pm$.03} & .92{\\scriptsize$\\pm$.03} & .96{\\scriptsize$\\pm$.02} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe results reveal a clear information--accuracy tradeoff (Table~\\ref{tab:info-access}).\n$\\ell_z^*$ substantially outperforms the only other binary-only baseline (accuracy z-score) by 12--16 AUROC points across contamination levels, demonstrating that IRT structure provides meaningful inductive bias beyond aggregate accuracy.\nAt 5\\% contamination, the gap between $\\ell_z^*$ (0.65) and the best privileged method (Min-K\\%++, 0.78) is only 0.13---IRT structure partially compensates for information disadvantage when signals are weak.\nAt higher contamination levels (15--25\\%), the gap widens to 0.10--0.12, as the additional information from token probabilities provides increasingly fine-grained signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Information-access vs detection-power operating points at 15\\% contamination on MMLU.}\n\\label{tab:info-access}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nOperating Point & Methods & AUROC & Info Required \\\\\n\\midrule\nMinimal & $\\ell_z^*$, acc z & .62--.80 & Binary only \\\\\nModerate & ConStat & .88 & Rephrased items \\\\\nFull & Min-K++, PPL & .90--.92 & Token probs \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe value of the minimal-information operating point lies in its universal applicability: $\\ell_z^*$ can be computed for any model on any benchmark from archival binary data, including proprietary APIs and historical leaderboard submissions where token probabilities are unavailable.\n\n\\subsection{Detection Power Function}\n\\label{sec:power}\n\nWe validate the theoretical power function across seven benchmarks spanning two orders of magnitude in item count (164--14,042 items).\nTable~\\ref{tab:power} presents simulated and theoretical power at 15\\% contamination alongside the theory--practice gap.\n\n\\begin{table}[t]\n\\centering\n\\caption{Power function validation at 15\\% contamination. Theoretical power derived from 4PL model; simulated power from controlled contamination. $R^2=0.88$ across all benchmarks.}\n\\label{tab:power}\n\\small\n\\begin{tabular}{lrccc}\n\\toprule\nBenchmark & $n$ & Sim & Theory & Gap \\\\\n\\midrule\nHumanEval & 164 & .24 & .22 & +.02 \\\\\nARC-C & 295 & .13 & .15 & $-.02$ \\\\\nGSM8K & 1,319 & .59 & .55 & +.04 \\\\\nMATH & 5,000 & .55 & .58 & $-.03$ \\\\\nBBH & 6,511 & .68 & .72 & $-.04$ \\\\\nHellaSwag & 10,042 & .75 & .78 & $-.03$ \\\\\nMMLU & 14,042 & .98 & .98 & .00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe theoretical power function fits the observed data with $R^2=0.88$, confirming that detection power is a predictable function of benchmark size.\nThe theory provides an upper bound (assuming all contaminated items produce maximal aberrance); the gap between theoretical and simulated power reflects the memorization fraction---SFT generalization absorbs a portion of the contamination signal.\n\nThe practical implication is a minimum benchmark size for effective detection: benchmarks with $n < 1{,}000$ items (HumanEval, ARC-C) have insufficient statistical power for reliable person-fit detection at practical contamination levels.\nBenchmarks with $n > 5{,}000$ items (BBH, HellaSwag, MMLU) achieve power $\\geq 0.68$ at 15\\% contamination.\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain}\n\nBeyond binary detection, person-fit analysis enables contamination \\emph{characterization} through domain-level decomposition.\nWe decompose MMLU $\\ell_z^*$ by subject domain (STEM, Humanities, Social Sciences, Other) for selected models from the PSN-IRT 12-model case study (Table~\\ref{tab:domain}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-level $\\ell_z^*$ for selected models (MMLU, 57 subjects grouped into 4 domains). Pattern type characterizes the contamination profile.}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\nModel & STEM & Hum & SocSci & Other & Pattern \\\\\n\\midrule\nGemini-1.5 & 22.0 & 18.5 & 16.2 & 15.8 & Unif.\\ pos \\\\\nYi-Light & 50.1 & 45.3 & 48.7 & 42.0 & Unif.\\ pos (ext) \\\\\nDoubao & $-2.0$ & $-13.0$ & $-14.8$ & 4.4 & Sel.\\ mixed \\\\\nHunyuan & 1.8 & 8.2 & 13.9 & 6.5 & Sel.\\ positive \\\\\nMistral-L & 28.5 & 24.1 & 22.0 & 20.3 & Unif.\\ pos \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo distinct contamination typologies emerge:\n\\begin{itemize}\n\\item \\textbf{Uniform positive}: All domains show high positive $\\ell_z^*$ (Gemini-1.5, Yi-Lightning, Mistral-Large), consistent with broad-spectrum contamination or training data that systematically overlaps with benchmark content.\n\\item \\textbf{Selective}: Domain-specific patterns (Doubao: negative in Humanities/Social Sciences, positive in Other; Hunyuan: concentrated in Social Sciences), suggesting domain-targeted training data exposure.\n\\end{itemize}\n\nThe domain entropy of misfit patterns shows moderate correlation with overall contamination severity ($r=0.45$), suggesting that more uniform misfit accompanies higher contamination levels.\nGemini-1.5 shows the highest STEM $\\ell_z^*$ (22.0), consistent with STEM items having higher discrimination parameters that amplify the person-fit signal.\n\n% ============================================================\n\\section{Discussion}\n\n\\subsection{Post-RL Robustness}\n\\label{sec:post-rl}\n\n\\citet{wang2025rlcontam} demonstrate that all log-probability-based detection methods degrade to near-chance after RL training.\nSince $\\ell_z^*$ operates on binary patterns rather than token distributions, it is structurally insulated from RL-induced distributional shifts.\nWe test this hypothesis with a preliminary experiment: Qwen3.5-9B contaminated at 15\\% via SFT, followed by 2,000 steps of GRPO training with rule-based reward.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pre- vs post-RL detection (Qwen3.5-9B $\\times$ MMLU @ 15\\% contamination).}\n\\label{tab:post-rl}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & $\\ell_z^*$ & $\\Delta\\ell_z^*$ & $d$ & Mem.\\ frac \\\\\n\\midrule\nClean & 7.85 & --- & --- & --- \\\\\nSFT-contam & 5.10 & $-2.75$ & $-2.50$ & .35 \\\\\nSFT + GRPO & 6.20 & $-1.60$ & $-1.10$ & .18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPost-RL, the person-fit signal attenuates ($|d|$ from 2.50 to 1.10, 44\\% retention) but remains statistically significant ($p=0.03$).\nThe memorization fraction drops from 0.35 to 0.18, consistent with RL exploration overwriting approximately half of the SFT memorization while preserving binary-level aberrance patterns.\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-RL detection: $\\ell_z^*$ vs token-probability methods. AUROC on MMLU at 15\\% contamination, pre- and post-GRPO.}\n\\label{tab:post-rl-comparison}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nMethod & Info & Pre-RL & Post-RL & Retention \\\\\n\\midrule\n$\\ell_z^*$ & binary & .80 & .62 & 77.5\\% \\\\\nMin-K\\%++ & tok & .92 & .52 & 56.5\\% \\\\\nPPL-based & lp & .90 & .51 & 56.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:post-rl-comparison} reveals a structural advantage: while all methods degrade post-RL, $\\ell_z^*$ retains 77.5\\% of its pre-RL AUROC (0.62 vs 0.80), whereas Min-K\\%++ and PPL-based methods collapse to near-chance (AUROC $\\approx$ 0.52).\nThe mechanism is that RL modifies token-level distributions (which log-probability methods depend on) but does not directly optimize binary response patterns---a model that ``learned to reason differently'' about contaminated items may still produce the same correct/incorrect pattern.\n\nWe present these results as preliminary evidence rather than a validated claim: the experiment covers a single model family with one RL configuration, and signal retention (44\\% of Cohen's $d$) is moderate.\nThe structural argument---that binary-level detection is orthogonal to token-distribution perturbation---warrants further investigation across model families and RL methods.\n\n\\subsection{IRT Parameter Estimation Challenges}\n\\label{sec:irt-refit}\n\nA natural extension of our framework would be large-scale leaderboard auditing using IRT parameters estimated from leaderboard data itself.\nWe investigated this by re-fitting IRT models to Open LLM Leaderboard v1 data, expanding from a pilot sample ($N=63$) to $N=500+$ models.\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT parameter recovery: pilot ($N=63$) vs expanded ($N=500$) refit. $a_r$: discrimination Pearson correlation with reference parameters; $b_r$: difficulty correlation.}\n\\label{tab:irt-refit}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Pilot & Expanded & Threshold & Verdict \\\\\n\\midrule\n3PL $a_r$ & .111 & .130 & $>$0.4 & Fail \\\\\n2PL $a_r$ & $-.084$ & $-.020$ & $>$0.4 & Fail \\\\\n3PL $b_r$ (Pearson) & .626 & .660 & $>$0.5 & Pass \\\\\n3PL $b_r$ (Spearman) & .656 & .680 & $>$0.5 & Pass \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:irt-refit} shows that expanding from $N=63$ to $N=500+$ produces negligible improvement in discrimination recovery ($a_r$: 0.111 $\\to$ 0.130, far below the 0.4 viability threshold).\nDifficulty parameters recover moderately well ($b_r \\approx 0.66$), confirming that the failure is specific to discrimination, not a general estimation failure.\n\nThis negative result quantifies a fundamental gap between classical and neural IRT estimation.\nClassical IRT assumes unidimensional latent ability, but LLM ability profiles are inherently multidimensional (e.g., a model strong in reasoning but weak in factual recall).\nThis dimensionality mismatch causes item discrimination to collapse in aggregate fitting.\nThe 13,000+ per-item model response records from v1 remain publicly available for future work once estimation methods for multidimensional LLM ability are developed.\n\n\\subsection{Natural Experiment: Base$\\to$Chat Pairs}\n\nAs complementary evidence, we examine base-to-chat model pairs from the v1 leaderboard, using the $\\Delta\\ell_z^*$ shift as a proxy for SFT effects on response patterns.\n\n\\begin{table}[t]\n\\centering\n\\caption{Natural experiment: $\\Delta\\ell_z^*$ between base and chat model pairs ($n=4$ pairs). Marginal significance at HellaSwag only; overall evidence is suggestive but underpowered.}\n\\label{tab:natural}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & $n$ & Mean $\\Delta$ & $t$ & $p$ \\\\\n\\midrule\nMMLU & 4 & $-1.20$ & $-1.45$ & .22 \\\\\nHellaSwag & 4 & $-2.80$ & $-2.85$ & .04 \\\\\nGSM8K & 4 & $+1.50$ & $+1.62$ & .18 \\\\\nARC-C & 4 & $-0.60$ & $-0.82$ & .45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly HellaSwag shows marginal significance ($p=0.04$), possibly reflecting systematic SFT effects on response patterns for this benchmark's commonsense reasoning format.\nThe experiment is fundamentally underpowered ($n=4$ pairs) and confounded by degraded IRT parameters ($a_r = 0.13$), which reduce $\\ell_z^*$ to an accuracy-like statistic.\nWe report these results as preliminary evidence consistent with SFT effects on response patterns, without drawing causal conclusions about contamination.\n\n\\subsection{Multiscale Aggregation}\n\nWe implemented the multiscale $\\ell_{z_m}$ statistic \\citep{hong2021multiscale} to aggregate person-fit across benchmarks into a single score.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiscale $\\ell_{z_m}$ vs per-benchmark $\\ell_z^*$ for selected models. $\\ell_{z_m}$ correlates highly with per-benchmark averages ($r=0.92$) without flagging additional models.}\n\\label{tab:lzm}\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\nModel & $\\ell_{z_m}$ & MMLU & Hella & GSM & Pattern \\\\\n\\midrule\nGemini-1.5 & 45.2 & 31.8 & $-12.3$ & $-8.5$ & Selective \\\\\nYi-Light & 52.1 & 48.2 & 35.1 & 22.0 & Uniform \\\\\nDoubao & 18.3 & 25.6 & $-5.2$ & $-10.1$ & Mixed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe multiscale statistic provides marginal additional value: $r=0.92$ with the average of per-benchmark $\\ell_z^*$ values, with no models newly flagged or unflagged (57/60 cells flagged under both approaches).\nImportantly, cross-benchmark aggregation obscures benchmark-specific contamination patterns---Gemini-1.5's selective profile (high MMLU, negative HellaSwag/GSM8K) is lost in the $\\ell_{z_m}$ summary.\nWe therefore retain per-benchmark $\\ell_z^*$ profiles as the primary presentation throughout this paper.\n\n\\subsection{Universal 4PL Model Misfit}\n\\label{sec:universal-misfit}\n\nA finding that emerged from our real-data analysis is that nearly all LLM response patterns deviate substantially from 4PL model predictions: 57 of 60 (model, benchmark) cells produce $|\\ell_z^*| \\gg 5$ after BH-FDR correction.\nThis is not a calibration artifact---bootstrap null distributions are well-calibrated for large benchmarks (MMLU KS rejection rate: 8.3\\%).\nRather, LLM response patterns genuinely violate IRT assumptions (local independence, unidimensionality) in ways that human test-takers typically do not.\n\nThis finding motivates our $\\Delta\\ell_z^*$ design: since absolute thresholds are uninformative (all models are ``anomalous''), we detect contamination through within-model shifts relative to clean baselines.\nThe universal misfit is itself a contribution to the understanding of how LLMs interact with psychometric evaluation frameworks.\n\n\\subsection{Limitations}\n\nSeveral limitations qualify our findings.\nFirst, the framework requires pre-estimated IRT parameters from a validated source (PSN-IRT), limiting applicability to benchmarks with available parameters.\nSecond, the Gemma boundary condition ($|d|=1.3$ at 15\\%) demonstrates that high-baseline-ability models present detection challenges, as genuine ability masks contamination signal.\nThird, the memorization fraction (0.22--0.42) means the theoretical power function provides an upper bound; actual detection power depends on SFT generalization characteristics that vary across architectures.\nFourth, our controlled contamination uses QLoRA SFT, which may not capture all real-world contamination pathways (e.g., pretraining exposure, data augmentation).\nFinally, the post-RL results are preliminary and cover only one model family.\n\n% ============================================================\n\\section{Related Work}\n\n\\textbf{Benchmark contamination detection.}\nEarly work used $n$-gram overlap between training and evaluation data \\citep{dodge2021documenting,brown2020language}.\n\\citet{shi2024detecting} introduced Min-K\\%++ for membership inference from token probabilities.\n\\citet{deng2024investigating} proposed Time Travel probing using model weights.\n\\citet{oren2024proving} developed ConStat, a performance-based approach using rephrased items.\n\\citet{dong2024codec} detect contamination via in-context learning effects.\n\\citet{wang2025rlcontam} demonstrated that all log-probability methods fail under RL training.\nOur work differs fundamentally in operating at the minimal-information level, requiring only binary response patterns.\n\n\\textbf{IRT for LLM evaluation.}\n\\citet{psnirt2026} introduced PSN-IRT, fitting 4PL models to LLM benchmark data and establishing validated item parameters.\n\\citet{polo2024tinybenchmarks} used IRT for efficient benchmark subsampling.\nOur work extends IRT from evaluation to contamination detection via person-fit statistics, a connection not previously explored.\n\n\\textbf{Person-fit in psychometrics.}\nPerson-fit statistics have a long history in educational testing \\citep{drasgow1985appropriateness,meijer1996person}.\nThe $\\ell_z^*$ statistic \\citep{snijders2001item} corrects for ability estimation error.\nOur contribution is connecting this literature to LLM contamination detection and identifying the $\\theta$-shift confound specific to the LLM setting.\n\n% ============================================================\n\\section{Conclusion}\n\nWe establish IRT person-fit statistics as a principled contamination detection framework operating at the minimal-information point---requiring only binary response patterns.\nThrough controlled experiments across four model families, we demonstrate detection with $|\\text{Cohen's } d| > 2.0$ in three of four families at 15\\% contamination on MMLU, with characterized boundary conditions for the fourth (Gemma, $|d|=1.3$).\nDetection power follows a predictable function of benchmark size ($R^2 = 0.88$), and $\\theta$-fixed analysis recovers monotonic dose-response in most families.\n\nIn the information-access landscape of contamination detection, $\\ell_z^*$ defines the best achievable detection from binary data alone (AUROC 0.80 at 15\\%, vs 0.62 for accuracy z-scores), while honestly trailing methods with privileged access (Min-K\\%++ AUROC 0.92).\nPreliminary evidence suggests structural robustness to RL-induced perturbation, where token-probability methods collapse.\nDomain-level analysis extends detection to contamination characterization, revealing distinct typologies in real-world models.\n\nThe universal 4PL model misfit finding---that LLM response patterns fundamentally differ from classical test-taker patterns---contributes to the broader understanding of psychometric methods applied to artificial agents, and the IRT parameter estimation challenges quantify the gap between classical and neural IRT that future work must bridge to enable large-scale leaderboard auditing.\n\n\\bibliographystyle{acl_natbib}\n\\bibliography{references}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9db0131-cb1b-4ac0-9003-fcc75667ddb4",
  "isSidechain": false,
  "requestId": "req_011CbF3FqnZY7hgPBbD9rm5S",
  "type": "assistant",
  "uuid": "73c72b88-4b1b-41e4-8aee-8ef4f60cbcab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYKUTPLJ2bJ2iwTSXHdMxN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2879,
      "cache_read_input_tokens": 43955,
      "output_tokens": 12858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12858,
          "cache_read_input_tokens": 43955,
          "cache_creation_input_tokens": 2879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2879
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

_source line 21 · 2026-05-21T03:59:37.959Z_

<details><summary>↩ Tool result · `toolu_012GCRuehTc61S8ZrYd6evFv`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73c72b88-4b1b-41e4-8aee-8ef4f60cbcab",
  "isSidechain": false,
  "promptId": "ec7c9be7-428e-4670-904e-cc8df713932d",
  "type": "user",
  "uuid": "7a0e9333-fd75-42d3-a526-e18d4e580ba9",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{caption}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\title{Detection and Characterization of Benchmark Contamination\\\\via IRT Person-Fit Statistics}\n\n\\author{\n  Anonymous Submission\n}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nBenchmark contamination undermines the reliability of LLM evaluation, yet all existing detection methods require privileged access to token probabilities, model weights, or specially crafted prompts.\nWe establish a \\emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics---originally developed for detecting exam cheating---to identify anomalous LLM response patterns using only binary (correct/incorrect) outcomes.\nWe formalize a detection framework based on the $\\ell_z^*$ statistic under a 4-parameter logistic (4PL) IRT model and validate it through controlled contamination experiments across four model families (Qwen, Llama, Gemma, Mistral) and three benchmarks (MMLU, HellaSwag, GSM8K).\nAt 15\\% contamination, the framework achieves $|\\text{Cohen's } d| > 2.0$ in three of four model families on MMLU, with the fourth (Gemma) showing a weaker but detectable signal ($|d|=1.3$).\nDetection power follows a predictable function of benchmark size ($R^2=0.88$), and a $\\theta$-fixed analysis recovers monotonic dose-response curves in three of four families.\nIn baseline comparisons, $\\ell_z^*$ achieves AUROC 0.80 at 15\\% contamination using only binary data, compared to 0.92 for Min-K\\%++ (requiring token probabilities) and 0.62 for accuracy z-scores---defining the best achievable detection at the minimal-information level.\nPreliminary evidence suggests $\\ell_z^*$ retains partial detection signal after reinforcement learning ($|d|=1.1$, AUROC 0.62), where token-probability methods degrade to chance.\nDomain-level analysis reveals distinct contamination typologies (uniform vs.\\ selective), enabling contamination characterization beyond binary detection.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\nBenchmark contamination---the presence of evaluation data in model training corpora---poses a fundamental threat to the integrity of LLM evaluation \\citep{sainz2023chatgpt,magar2022data}.\nAs benchmarks proliferate and training corpora scale to trillions of tokens, the risk of inadvertent or intentional contamination grows.\nLeaderboard rankings, model selection decisions, and research conclusions all depend on benchmark scores reflecting genuine capability rather than memorization artifacts.\n\nA growing literature addresses contamination detection, spanning time-based partition methods, membership inference attacks (MIA/Min-K\\%++; \\citealp{shi2024detecting}), probing techniques (Time Travel; \\citealp{deng2024investigating}), performance-based testing (ConStat; \\citealp{oren2024proving}), and in-context learning effects (CoDeC; \\citealp{dong2024codec}).\nHowever, all existing methods require more than binary response patterns: token-level probabilities, log-likelihoods, model weights, or access to rephrase benchmark items.\nFurthermore, \\citet{wang2025rlcontam} demonstrate that all ten log-probability-based methods they evaluate degrade to near-random performance on RL-trained reasoning models, exposing a structural vulnerability in the dominant detection paradigm.\n\nWe address a more fundamental question: \\emph{what can be detected from binary response patterns alone?}\nThis question is practically motivated---binary outcomes (correct/incorrect on benchmark items) are available for any model on any benchmark, including proprietary APIs and historical leaderboard submissions.\nIt is also theoretically grounded: a contaminated LLM producing anomalous response patterns is functionally analogous to an examinee with item preknowledge, a problem studied for decades in psychometrics.\n\nWe establish the minimal-information operating point on the contamination detection frontier by adapting IRT person-fit statistics \\citep{drasgow1985appropriateness,snijders2001item} to LLM benchmark evaluation.\nOur framework uses the $\\ell_z^*$ statistic under a 4-parameter logistic (4PL) IRT model, which captures both guessing and ceiling effects critical for modeling LLM responses.\nThrough controlled contamination experiments (QLoRA SFT injection across four model families), we validate the framework and characterize its operating conditions:\n\n\\begin{enumerate}\n\\item \\textbf{Principled detection with characterized conditions.} At 15\\% contamination, detection achieves $|\\text{Cohen's } d| > 2.0$ in three of four model families on MMLU.\nThe fourth family (Gemma-4-31B) shows a weaker signal ($|d|=1.3$), a boundary condition attributable to high baseline ability.\nA $\\theta$-fixed analysis recovers monotonic dose-response in three of four families.\n\n\\item \\textbf{Predictable detection power.} Power is a monotonic function of benchmark size ($n_\\text{items}$) and contamination level, following theoretical predictions with $R^2=0.88$ across seven benchmarks spanning 164--14,042 items.\n\n\\item \\textbf{Empirical findings.} Applying person-fit to real LLM data reveals universal 4PL model misfit (57/60 model--benchmark cells flagged), domain-level contamination typologies (uniform vs.\\ selective), and IRT parameter estimation challenges that quantify the gap between classical and neural IRT.\n\\end{enumerate}\n\n% ============================================================\n\\section{Background}\n\n\\subsection{Item Response Theory and the 4PL Model}\n\nIRT models the probability of a correct response as a function of person ability ($\\theta$) and item parameters.\nThe 4-parameter logistic (4PL) model specifies:\n\\begin{equation}\nP(X_{ij}=1 \\mid \\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is item discrimination, $b_i$ is item difficulty, $c_i$ is the guessing (lower asymptote) parameter, and $d_i$ is the upper asymptote (ceiling) parameter.\nThe 3PL model sets $d_i=1$; the 2PL further sets $c_i=0$.\n\nFor LLM evaluation, the $d_i$ parameter is critical: many items have $d_i < 1$, meaning even high-ability models may not achieve perfect performance due to item-specific confounds (ambiguous wording, multiple defensible answers).\nIgnoring this parameter systematically inflates expected performance for high-ability models.\n\n\\subsection{Person-Fit Statistics}\n\nPerson-fit statistics detect response patterns that are improbable given estimated ability.\nThe $\\ell_z^*$ statistic \\citep{snijders2001item} is the standardized log-likelihood of an individual's response pattern:\n\\begin{equation}\n\\ell_z^* = \\frac{\\ell_0 - E[\\ell_0]}{\\sqrt{\\text{Var}[\\ell_0]}}\n\\label{eq:lzstar}\n\\end{equation}\nwhere $\\ell_0 = \\sum_{i=1}^{n} [x_i \\log P_i + (1-x_i) \\log(1-P_i)]$ is the log-likelihood of observed responses $\\{x_i\\}$ given model-predicted probabilities $\\{P_i\\}$.\nUnder the null hypothesis (responses generated by the IRT model), $\\ell_z^* \\sim \\mathcal{N}(0,1)$ asymptotically.\n\nTwo response anomaly types are relevant:\n\\begin{itemize}\n\\item \\textbf{Aberrant patterns} ($\\ell_z^* \\ll 0$): unexpected responses given ability---e.g., a high-ability model failing easy items while succeeding on hard ones. Partial contamination (memorizing a subset of items) produces this signature.\n\\item \\textbf{Over-consistent patterns} ($\\ell_z^* \\gg 0$): responses more consistent with the model than expected---e.g., perfect accuracy with $\\theta$ far below what perfect performance would require. Complete contamination produces this signature.\n\\end{itemize}\n\n\\subsection{Contamination as Item Preknowledge}\n\nIn psychometrics, item preknowledge refers to examinees who have advance access to test items.\nSuch examinees produce anomalous response patterns: they answer ``preknown'' items correctly regardless of difficulty, while their performance on unknown items reflects genuine ability.\nThis creates a detectable mismatch between observed and expected response patterns---precisely what $\\ell_z^*$ measures.\n\nLLM benchmark contamination through SFT on benchmark items is functionally identical: the model memorizes a subset of items, producing correct responses independent of item difficulty, while generalizing from training on the remaining items.\nThe memorization fraction---the proportion of contaminated items that produce memorized (rather than generalized) responses---determines the strength of the person-fit signal.\n\n% ============================================================\n\\section{Method}\n\n\\subsection{Detection Framework}\n\nOur detection framework operates in three stages:\n\n\\textbf{Stage 1: IRT Parameter Estimation.}\nGiven binary response matrices from a reference population of LLMs on benchmark items, we estimate 4PL item parameters $(a_i, b_i, c_i, d_i)$ using marginal maximum likelihood with an EM algorithm.\nWe use pre-estimated parameters from PSN-IRT \\citep{psnirt2026} where available, ensuring parameter quality is independent of our detection procedure.\n\n\\textbf{Stage 2: Person-Fit Computation.}\nFor a target model with response vector $\\mathbf{x} = (x_1, \\ldots, x_n)$ on $n$ benchmark items, we estimate ability $\\hat{\\theta}$ via maximum likelihood and compute $\\ell_z^*$ (Eq.~\\ref{eq:lzstar}).\n\n\\textbf{Stage 3: $\\Delta\\ell_z^*$ Analysis.}\nSince LLM response patterns universally deviate from 4PL predictions (Section~\\ref{sec:universal-misfit}), absolute $\\ell_z^*$ thresholds are uninformative for contamination detection.\nInstead, we compute the within-model shift:\n\\begin{equation}\n\\Delta\\ell_z^* = \\ell_z^*(\\text{contaminated}) - \\overline{\\ell_z^*}(\\text{clean baselines})\n\\end{equation}\nstandardized by the clean-baseline variance (Cohen's $d$).\nThe well-calibrated bootstrap null ensures that $\\Delta\\ell_z^*$ is statistically interpretable.\n\n\\subsection{$\\theta$-Fixed Analysis}\n\nA methodological contribution of this work is identifying the $\\theta$-shift confound: when $\\theta$ is re-estimated on contaminated data, the increased accuracy raises $\\hat{\\theta}$, which partially absorbs the aberrance signal.\nThis can produce non-monotonic dose-response under free-$\\theta$ estimation (higher contamination $\\not\\Rightarrow$ larger $|\\Delta\\ell_z^*|$).\n\nWe address this via $\\theta$-fixed analysis: fixing $\\theta$ to the pre-contamination baseline estimate $\\hat{\\theta}_\\text{clean}$ and recomputing $\\ell_z^*$.\nThis isolates the response-pattern anomaly from ability shift, recovering monotonic dose-response in most model families.\n\n\\subsection{Detection Power Theory}\n\nDetection power depends on three factors: benchmark size ($n_\\text{items}$), contamination level ($\\rho$), and memorization fraction ($\\phi$).\nTheoretical power under the 4PL model follows:\n\\begin{equation}\n\\text{Power} \\propto \\Phi\\!\\left(\\frac{\\phi \\cdot \\rho \\cdot \\sqrt{n_\\text{items}} \\cdot \\bar{a}}{\\sigma_{\\ell_z^*}}\\right)\n\\end{equation}\nwhere $\\bar{a}$ is mean item discrimination and $\\Phi$ is the standard normal CDF.\nThis gives an upper bound assuming all memorized items produce maximal aberrance; the memorization fraction $\\phi$ adjusts for SFT generalization.\n\n% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Models and Benchmarks}\n\n\\textbf{Controlled contamination.}\nWe use four model families: Qwen3.5-9B, Llama-3.1-8B, Gemma-4-31B, and Mistral-7B-v0.3.\nFor each family, we create contaminated variants via QLoRA SFT on benchmark items at six contamination levels: 0\\% (clean, 3 seeds), 5\\%, 10\\%, 15\\%, 25\\%, and 50\\%.\nThree benchmarks serve as contamination targets: MMLU (14,042 items), HellaSwag (10,042 items), and GSM8K (1,319 items).\n\n\\textbf{Real-data analysis.}\nWe analyze 12 models with validated 4PL parameters from PSN-IRT across five benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval).\n\n\\subsection{IRT Parameters}\n\nItem parameters are sourced from PSN-IRT \\citep{psnirt2026}, which provides validated 4PL estimates for major benchmarks.\nFor the power function validation (Section~\\ref{sec:power}), BBH and MATH require separate 4PL estimation from 50+ model responses.\n\n\\subsection{Baselines}\n\nWe compare against five baselines spanning the information-access spectrum:\n\\begin{itemize}\n\\item \\textbf{Accuracy z-score} (binary): standardized accuracy relative to population mean.\n\\item \\textbf{ConStat} (retest): performance-based testing with rephrased items \\citep{oren2024proving}.\n\\item \\textbf{PPL-based} (log-probs): perplexity-based detection using model log-probabilities.\n\\item \\textbf{Min-K\\%++} (token probs): token-probability-based MIA \\citep{shi2024detecting}.\n\\item \\textbf{Random}: uniform random baseline.\n\\end{itemize}\n\n\\subsection{Evaluation Metrics}\n\nPrimary: Cohen's $d$ (effect size between clean and contaminated $\\ell_z^*$), AUROC (discrimination between clean and contaminated models).\nAll Cohen's $d$ values computed with $n=3$ clean seeds, $\\text{ddof}=1$, on $\\ell_z^*$-corrected values.\nBootstrap 95\\% confidence intervals reported where applicable.\n\n% ============================================================\n\\section{Results}\n\n\\subsection{Controlled Contamination Pilot}\n\\label{sec:pilot}\n\nWe first validate the detection framework on a single model--benchmark pair (Qwen3.5-9B $\\times$ MMLU) with four conditions.\nTable~\\ref{tab:pilot} summarizes the results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pilot $\\Delta\\ell_z^*$ summary (Qwen3.5-9B $\\times$ MMLU). $\\ell_z^*$ corrected per \\citet{snijders2001item}. Cohen's $d$ relative to clean mean ($n=2$, $\\text{ddof}=1$).}\n\\label{tab:pilot}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & $\\ell_z^*$ & $\\Delta\\ell_z^*$ & $d$ & Acc & Mem.\\ frac \\\\\n\\midrule\nClean-s1 & 8.20 & --- & --- & .679 & --- \\\\\nClean-s2 & 7.50 & --- & --- & .681 & --- \\\\\nContam-15\\% & 5.10 & $-2.75$ & $-2.50$ & .720 & .35 \\\\\nContam-50\\% & 6.80 & $-1.05$ & $-0.95$ & .760 & .28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 15\\% contamination condition produces $|d|=2.50$, a large effect, confirming that person-fit detects the injected contamination signal.\nThe clean-vs-clean difference ($\\Delta=0.70$) establishes a noise floor well below the contamination signal.\nCritically, the free-$\\theta$ dose-response is \\emph{non-monotonic}: the 50\\% condition ($|d|=0.95$) produces a weaker signal than 15\\% ($|d|=2.50$).\nThis motivates the $\\theta$-fixed analysis (Section~\\ref{sec:full-contam}).\n\nThe memorization fraction of 0.35 at 15\\% contamination indicates that approximately 35\\% of injected items produce memorization signatures, while the remainder are absorbed by SFT generalization.\nThe seen/unseen $\\ell_z^*$ gap of 2.8 provides the clearest contamination fingerprint: items present in training show expected response patterns, while unseen items exhibit aberrant patterns.\n\n\\subsection{Full Controlled Contamination}\n\\label{sec:full-contam}\n\nWe extend to four model families and three benchmarks.\nTable~\\ref{tab:full-d} presents Cohen's $d$ at 15\\% contamination, and Table~\\ref{tab:dose-response} shows the full dose-response curve on MMLU under $\\theta$-fixed analysis.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cohen's $d$ at 15\\% contamination ($n=3$ seeds, $\\text{ddof}=1$, $\\ell_z^*$-corrected). $\\theta$-fixed monotonicity indicates whether $|d|$ increases monotonically across all contamination levels under fixed-$\\theta$ analysis.}\n\\label{tab:full-d}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nFamily & MMLU & HellaSwag & GSM8K & $\\theta$-mono \\\\\n\\midrule\nQwen3.5-9B & $-2.50$ & $-1.20$ & $-0.90$ & Yes \\\\\nLlama-3.1-8B & $-2.80$ & $-1.40$ & $-1.10$ & Yes \\\\\nGemma-4-31B & $-1.30$ & $-0.60$ & $-0.40$ & No \\\\\nMistral-7B-v0.3 & $-2.20$ & $-1.10$ & $-0.80$ & Yes \\\\\n\\midrule\nMean & $-2.20$ & $-1.08$ & $-0.80$ & 3/4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree of four families achieve $|d| > 2.0$ on MMLU at 15\\% contamination.\nGemma-4-31B is the exception ($|d|=1.3$), attributable to its higher baseline ability: as a 31B model, its $\\hat{\\theta}$ is already high, reducing the marginal $\\theta$-shift from contamination and producing a weaker aberrance signal.\nThis represents a characterized boundary condition rather than a framework failure.\n\nDetection strength decreases from MMLU (mean $|d|=2.20$) to HellaSwag ($|d|=1.08$) to GSM8K ($|d|=0.80$), consistent with the theoretical dependence on $n_\\text{items}$: MMLU has 14K items, HellaSwag 10K, and GSM8K 1.3K.\n\n\\begin{table}[t]\n\\centering\n\\caption{Dose-response on MMLU under $\\theta$-fixed analysis ($\\ell_z^*$-corrected Cohen's $d$). Monotonic increase in $|d|$ with contamination level is expected under the framework.}\n\\label{tab:dose-response}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nFamily & 5\\% & 10\\% & 15\\% & 25\\% & 50\\% & Mono \\\\\n\\midrule\nQwen3.5-9B & $-0.60$ & $-1.40$ & $-2.50$ & $-3.80$ & $-5.20$ & Yes \\\\\nLlama-3.1-8B & $-0.75$ & $-1.60$ & $-2.80$ & $-4.20$ & $-5.80$ & Yes \\\\\nGemma-4-31B & $-0.30$ & $-0.70$ & $-1.30$ & $-1.80$ & $-1.60$ & No \\\\\nMistral-7B & $-0.55$ & $-1.20$ & $-2.20$ & $-3.40$ & $-4.60$ & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\theta$-fixed analysis recovers monotonic dose-response in Qwen, Llama, and Mistral (Table~\\ref{tab:dose-response}).\nGemma retains residual non-monotonicity at 50\\% ($|d|=1.6 < |d|_{25\\%}=1.8$), consistent with its high baseline ability creating a ceiling effect on the person-fit signal.\n\nTable~\\ref{tab:mem-frac} reports memorization fractions, which range from 0.22 (Gemma, GSM8K) to 0.42 (Llama, MMLU), reflecting architecture-dependent SFT generalization.\nGemma consistently shows the lowest memorization fractions, indicating stronger generalization from instruction tuning---which paradoxically weakens the contamination detection signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Memorization fraction by model family and benchmark (at 15\\% contamination). Higher values indicate more items producing memorization rather than generalization signatures.}\n\\label{tab:mem-frac}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nFamily & MMLU & HellaSwag & GSM8K \\\\\n\\midrule\nQwen3.5-9B & .38 & .33 & .30 \\\\\nLlama-3.1-8B & .42 & .38 & .35 \\\\\nGemma-4-31B & .28 & .25 & .22 \\\\\nMistral-7B-v0.3 & .36 & .32 & .28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{4PL vs 3PL Ablation}\n\\label{sec:4pl-ablation}\n\nWe evaluate whether the 4PL upper asymptote parameter $d_i$ is necessary for contamination detection by comparing 4PL against 3PL ($d_i=1$) and 2PL ($c_i=0, d_i=1$).\nTable~\\ref{tab:4pl-ablation} reports detection power at 25\\% contamination.\n\n\\begin{table}[t]\n\\centering\n\\caption{Detection power at 25\\% contamination: 4PL vs 3PL($d{=}1$). Gain in percentage points (pp). The last column shows the fraction of items with $d_i < 0.95$, which drives the 4PL advantage.}\n\\label{tab:4pl-ablation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & 4PL & 3PL & Gain (pp) & $d{<}0.95$ \\\\\n\\midrule\nMMLU & .72 & .50 & +22 & 46\\% \\\\\nHellaSwag & .48 & .28 & +20 & 41\\% \\\\\nGSM8K & .65 & .49 & +16 & 30\\% \\\\\nARC-C & .12 & .08 & +4 & 22\\% \\\\\nHumanEval & .28 & .18 & +10 & 35\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 4PL model provides a 10--22 percentage point power advantage over 3PL across benchmarks.\nThe gain correlates with the proportion of items having $d_i < 0.95$: MMLU (46\\% such items) shows the largest gain (+22pp).\nIgnoring the upper asymptote systematically overestimates expected performance for high-ability models, inflating false alarm rates from the nominal 5\\% to 6--14\\% under 3PL.\nThe 2PL model is unusable, with false alarm rates of 50--100\\% (not shown), confirming that both the guessing and ceiling parameters are essential for LLM person-fit analysis.\n\nThe correlation between 4PL and 3PL $\\ell_z^*$ values is only $r=0.35$, indicating these are fundamentally different measurements rather than scaled versions of each other.\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} compares detection performance across contamination levels on MMLU using the controlled contamination ground truth.\n\n\\begin{table}[t]\n\\centering\n\\caption{AUROC comparison across contamination levels (MMLU, mean $\\pm$ 95\\% bootstrap CI). Methods ordered by information access level.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Info & 5\\% & 10\\% & 15\\% & 25\\% \\\\\n\\midrule\nRandom & --- & .50 & .50 & .50 & .50 \\\\\nAcc z & bin & .53{\\scriptsize$\\pm$.05} & .58{\\scriptsize$\\pm$.05} & .62{\\scriptsize$\\pm$.05} & .70{\\scriptsize$\\pm$.04} \\\\\n$\\ell_z^*$ & bin & .65{\\scriptsize$\\pm$.06} & .74{\\scriptsize$\\pm$.06} & .80{\\scriptsize$\\pm$.06} & .86{\\scriptsize$\\pm$.05} \\\\\nConStat & ret & .72{\\scriptsize$\\pm$.04} & .82{\\scriptsize$\\pm$.04} & .88{\\scriptsize$\\pm$.04} & .93{\\scriptsize$\\pm$.03} \\\\\nPPL & lp & .75{\\scriptsize$\\pm$.04} & .83{\\scriptsize$\\pm$.04} & .90{\\scriptsize$\\pm$.03} & .95{\\scriptsize$\\pm$.02} \\\\\nMin-K++ & tok & .78{\\scriptsize$\\pm$.04} & .86{\\scriptsize$\\pm$.03} & .92{\\scriptsize$\\pm$.03} & .96{\\scriptsize$\\pm$.02} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe results reveal a clear information--accuracy tradeoff (Table~\\ref{tab:info-access}).\n$\\ell_z^*$ substantially outperforms the only other binary-only baseline (accuracy z-score) by 12--16 AUROC points across contamination levels, demonstrating that IRT structure provides meaningful inductive bias beyond aggregate accuracy.\nAt 5\\% contamination, the gap between $\\ell_z^*$ (0.65) and the best privileged method (Min-K\\%++, 0.78) is only 0.13---IRT structure partially compensates for information disadvantage when signals are weak.\nAt higher contamination levels (15--25\\%), the gap widens to 0.10--0.12, as the additional information from token probabilities provides increasingly fine-grained signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Information-access vs detection-power operating points at 15\\% contamination on MMLU.}\n\\label{tab:info-access}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nOperating Point & Methods & AUROC & Info Required \\\\\n\\midrule\nMinimal & $\\ell_z^*$, acc z & .62--.80 & Binary only \\\\\nModerate & ConStat & .88 & Rephrased items \\\\\nFull & Min-K++, PPL & .90--.92 & Token probs \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe value of the minimal-information operating point lies in its universal applicability: $\\ell_z^*$ can be computed for any model on any benchmark from archival binary data, including proprietary APIs and historical leaderboard submissions where token probabilities are unavailable.\n\n\\subsection{Detection Power Function}\n\\label{sec:power}\n\nWe validate the theoretical power function across seven benchmarks spanning two orders of magnitude in item count (164--14,042 items).\nTable~\\ref{tab:power} presents simulated and theoretical power at 15\\% contamination alongside the theory--practice gap.\n\n\\begin{table}[t]\n\\centering\n\\caption{Power function validation at 15\\% contamination. Theoretical power derived from 4PL model; simulated power from controlled contamination. $R^2=0.88$ across all benchmarks.}\n\\label{tab:power}\n\\small\n\\begin{tabular}{lrccc}\n\\toprule\nBenchmark & $n$ & Sim & Theory & Gap \\\\\n\\midrule\nHumanEval & 164 & .24 & .22 & +.02 \\\\\nARC-C & 295 & .13 & .15 & $-.02$ \\\\\nGSM8K & 1,319 & .59 & .55 & +.04 \\\\\nMATH & 5,000 & .55 & .58 & $-.03$ \\\\\nBBH & 6,511 & .68 & .72 & $-.04$ \\\\\nHellaSwag & 10,042 & .75 & .78 & $-.03$ \\\\\nMMLU & 14,042 & .98 & .98 & .00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe theoretical power function fits the observed data with $R^2=0.88$, confirming that detection power is a predictable function of benchmark size.\nThe theory provides an upper bound (assuming all contaminated items produce maximal aberrance); the gap between theoretical and simulated power reflects the memorization fraction---SFT generalization absorbs a portion of the contamination signal.\n\nThe practical implication is a minimum benchmark size for effective detection: benchmarks with $n < 1{,}000$ items (HumanEval, ARC-C) have insufficient statistical power for reliable person-fit detection at practical contamination levels.\nBenchmarks with $n > 5{,}000$ items (BBH, HellaSwag, MMLU) achieve power $\\geq 0.68$ at 15\\% contamination.\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain}\n\nBeyond binary detection, person-fit analysis enables contamination \\emph{characterization} through domain-level decomposition.\nWe decompose MMLU $\\ell_z^*$ by subject domain (STEM, Humanities, Social Sciences, Other) for selected models from the PSN-IRT 12-model case study (Table~\\ref{tab:domain}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-level $\\ell_z^*$ for selected models (MMLU, 57 subjects grouped into 4 domains). Pattern type characterizes the contamination profile.}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\nModel & STEM & Hum & SocSci & Other & Pattern \\\\\n\\midrule\nGemini-1.5 & 22.0 & 18.5 & 16.2 & 15.8 & Unif.\\ pos \\\\\nYi-Light & 50.1 & 45.3 & 48.7 & 42.0 & Unif.\\ pos (ext) \\\\\nDoubao & $-2.0$ & $-13.0$ & $-14.8$ & 4.4 & Sel.\\ mixed \\\\\nHunyuan & 1.8 & 8.2 & 13.9 & 6.5 & Sel.\\ positive \\\\\nMistral-L & 28.5 & 24.1 & 22.0 & 20.3 & Unif.\\ pos \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo distinct contamination typologies emerge:\n\\begin{itemize}\n\\item \\textbf{Uniform positive}: All domains show high positive $\\ell_z^*$ (Gemini-1.5, Yi-Lightning, Mistral-Large), consistent with broad-spectrum contamination or training data that systematically overlaps with benchmark content.\n\\item \\textbf{Selective}: Domain-specific patterns (Doubao: negative in Humanities/Social Sciences, positive in Other; Hunyuan: concentrated in Social Sciences), suggesting domain-targeted training data exposure.\n\\end{itemize}\n\nThe domain entropy of misfit patterns shows moderate correlation with overall contamination severity ($r=0.45$), suggesting that more uniform misfit accompanies higher contamination levels.\nGemini-1.5 shows the highest STEM $\\ell_z^*$ (22.0), consistent with STEM items having higher discrimination parameters that amplify the person-fit signal.\n\n% ============================================================\n\\section{Discussion}\n\n\\subsection{Post-RL Robustness}\n\\label{sec:post-rl}\n\n\\citet{wang2025rlcontam} demonstrate that all log-probability-based detection methods degrade to near-chance after RL training.\nSince $\\ell_z^*$ operates on binary patterns rather than token distributions, it is structurally insulated from RL-induced distributional shifts.\nWe test this hypothesis with a preliminary experiment: Qwen3.5-9B contaminated at 15\\% via SFT, followed by 2,000 steps of GRPO training with rule-based reward.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pre- vs post-RL detection (Qwen3.5-9B $\\times$ MMLU @ 15\\% contamination).}\n\\label{tab:post-rl}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & $\\ell_z^*$ & $\\Delta\\ell_z^*$ & $d$ & Mem.\\ frac \\\\\n\\midrule\nClean & 7.85 & --- & --- & --- \\\\\nSFT-contam & 5.10 & $-2.75$ & $-2.50$ & .35 \\\\\nSFT + GRPO & 6.20 & $-1.60$ & $-1.10$ & .18 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPost-RL, the person-fit signal attenuates ($|d|$ from 2.50 to 1.10, 44\\% retention) but remains statistically significant ($p=0.03$).\nThe memorization fraction drops from 0.35 to 0.18, consistent with RL exploration overwriting approximately half of the SFT memorization while preserving binary-level aberrance patterns.\n\n\\begin{table}[t]\n\\centering\n\\caption{Post-RL detection: $\\ell_z^*$ vs token-probability methods. AUROC on MMLU at 15\\% contamination, pre- and post-GRPO.}\n\\label{tab:post-rl-comparison}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nMethod & Info & Pre-RL & Post-RL & Retention \\\\\n\\midrule\n$\\ell_z^*$ & binary & .80 & .62 & 77.5\\% \\\\\nMin-K\\%++ & tok & .92 & .52 & 56.5\\% \\\\\nPPL-based & lp & .90 & .51 & 56.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:post-rl-comparison} reveals a structural advantage: while all methods degrade post-RL, $\\ell_z^*$ retains 77.5\\% of its pre-RL AUROC (0.62 vs 0.80), whereas Min-K\\%++ and PPL-based methods collapse to near-chance (AUROC $\\approx$ 0.52).\nThe mechanism is that RL modifies token-level distributions (which log-probability methods depend on) but does not directly optimize binary response patterns---a model that ``learned to reason differently'' about contaminated items may still produce the same correct/incorrect pattern.\n\nWe present these results as preliminary evidence rather than a validated claim: the experiment covers a single model family with one RL configuration, and signal retention (44\\% of Cohen's $d$) is moderate.\nThe structural argument---that binary-level detection is orthogonal to token-distribution perturbation---warrants further investigation across model families and RL methods.\n\n\\subsection{IRT Parameter Estimation Challenges}\n\\label{sec:irt-refit}\n\nA natural extension of our framework would be large-scale leaderboard auditing using IRT parameters estimated from leaderboard data itself.\nWe investigated this by re-fitting IRT models to Open LLM Leaderboard v1 data, expanding from a pilot sample ($N=63$) to $N=500+$ models.\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT parameter recovery: pilot ($N=63$) vs expanded ($N=500$) refit. $a_r$: discrimination Pearson correlation with reference parameters; $b_r$: difficulty correlation.}\n\\label{tab:irt-refit}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Pilot & Expanded & Threshold & Verdict \\\\\n\\midrule\n3PL $a_r$ & .111 & .130 & $>$0.4 & Fail \\\\\n2PL $a_r$ & $-.084$ & $-.020$ & $>$0.4 & Fail \\\\\n3PL $b_r$ (Pearson) & .626 & .660 & $>$0.5 & Pass \\\\\n3PL $b_r$ (Spearman) & .656 & .680 & $>$0.5 & Pass \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:irt-refit} shows that expanding from $N=63$ to $N=500+$ produces negligible improvement in discrimination recovery ($a_r$: 0.111 $\\to$ 0.130, far below the 0.4 viability threshold).\nDifficulty parameters recover moderately well ($b_r \\approx 0.66$), confirming that the failure is specific to discrimination, not a general estimation failure.\n\nThis negative result quantifies a fundamental gap between classical and neural IRT estimation.\nClassical IRT assumes unidimensional latent ability, but LLM ability profiles are inherently multidimensional (e.g., a model strong in reasoning but weak in factual recall).\nThis dimensionality mismatch causes item discrimination to collapse in aggregate fitting.\nThe 13,000+ per-item model response records from v1 remain publicly available for future work once estimation methods for multidimensional LLM ability are developed.\n\n\\subsection{Natural Experiment: Base$\\to$Chat Pairs}\n\nAs complementary evidence, we examine base-to-chat model pairs from the v1 leaderboard, using the $\\Delta\\ell_z^*$ shift as a proxy for SFT effects on response patterns.\n\n\\begin{table}[t]\n\\centering\n\\caption{Natural experiment: $\\Delta\\ell_z^*$ between base and chat model pairs ($n=4$ pairs). Marginal significance at HellaSwag only; overall evidence is suggestive but underpowered.}\n\\label{tab:natural}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & $n$ & Mean $\\Delta$ & $t$ & $p$ \\\\\n\\midrule\nMMLU & 4 & $-1.20$ & $-1.45$ & .22 \\\\\nHellaSwag & 4 & $-2.80$ & $-2.85$ & .04 \\\\\nGSM8K & 4 & $+1.50$ & $+1.62$ & .18 \\\\\nARC-C & 4 & $-0.60$ & $-0.82$ & .45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly HellaSwag shows marginal significance ($p=0.04$), possibly reflecting systematic SFT effects on response patterns for this benchmark's commonsense reasoning format.\nThe experiment is fundamentally underpowered ($n=4$ pairs) and confounded by degraded IRT parameters ($a_r = 0.13$), which reduce $\\ell_z^*$ to an accuracy-like statistic.\nWe report these results as preliminary evidence consistent with SFT effects on response patterns, without drawing causal conclusions about contamination.\n\n\\subsection{Multiscale Aggregation}\n\nWe implemented the multiscale $\\ell_{z_m}$ statistic \\citep{hong2021multiscale} to aggregate person-fit across benchmarks into a single score.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiscale $\\ell_{z_m}$ vs per-benchmark $\\ell_z^*$ for selected models. $\\ell_{z_m}$ correlates highly with per-benchmark averages ($r=0.92$) without flagging additional models.}\n\\label{tab:lzm}\n\\small\n\\begin{tabular}{lrrrrl}\n\\toprule\nModel & $\\ell_{z_m}$ & MMLU & Hella & GSM & Pattern \\\\\n\\midrule\nGemini-1.5 & 45.2 & 31.8 & $-12.3$ & $-8.5$ & Selective \\\\\nYi-Light & 52.1 & 48.2 & 35.1 & 22.0 & Uniform \\\\\nDoubao & 18.3 & 25.6 & $-5.2$ & $-10.1$ & Mixed \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe multiscale statistic provides marginal additional value: $r=0.92$ with the average of per-benchmark $\\ell_z^*$ values, with no models newly flagged or unflagged (57/60 cells flagged under both approaches).\nImportantly, cross-benchmark aggregation obscures benchmark-specific contamination patterns---Gemini-1.5's selective profile (high MMLU, negative HellaSwag/GSM8K) is lost in the $\\ell_{z_m}$ summary.\nWe therefore retain per-benchmark $\\ell_z^*$ profiles as the primary presentation throughout this paper.\n\n\\subsection{Universal 4PL Model Misfit}\n\\label{sec:universal-misfit}\n\nA finding that emerged from our real-data analysis is that nearly all LLM response patterns deviate substantially from 4PL model predictions: 57 of 60 (model, benchmark) cells produce $|\\ell_z^*| \\gg 5$ after BH-FDR correction.\nThis is not a calibration artifact---bootstrap null distributions are well-calibrated for large benchmarks (MMLU KS rejection rate: 8.3\\%).\nRather, LLM response patterns genuinely violate IRT assumptions (local independence, unidimensionality) in ways that human test-takers typically do not.\n\nThis finding motivates our $\\Delta\\ell_z^*$ design: since absolute thresholds are uninformative (all models are ``anomalous''), we detect contamination through within-model shifts relative to clean baselines.\nThe universal misfit is itself a contribution to the understanding of how LLMs interact with psychometric evaluation frameworks.\n\n\\subsection{Limitations}\n\nSeveral limitations qualify our findings.\nFirst, the framework requires pre-estimated IRT parameters from a validated source (PSN-IRT), limiting applicability to benchmarks with available parameters.\nSecond, the Gemma boundary condition ($|d|=1.3$ at 15\\%) demonstrates that high-baseline-ability models present detection challenges, as genuine ability masks contamination signal.\nThird, the memorization fraction (0.22--0.42) means the theoretical power function provides an upper bound; actual detection power depends on SFT generalization characteristics that vary across architectures.\nFourth, our controlled contamination uses QLoRA SFT, which may not capture all real-world contamination pathways (e.g., pretraining exposure, data augmentation).\nFinally, the post-RL results are preliminary and cover only one model family.\n\n% ============================================================\n\\section{Related Work}\n\n\\textbf{Benchmark contamination detection.}\nEarly work used $n$-gram overlap between training and evaluation data \\citep{dodge2021documenting,brown2020language}.\n\\citet{shi2024detecting} introduced Min-K\\%++ for membership inference from token probabilities.\n\\citet{deng2024investigating} proposed Time Travel probing using model weights.\n\\citet{oren2024proving} developed ConStat, a performance-based approach using rephrased items.\n\\citet{dong2024codec} detect contamination via in-context learning effects.\n\\citet{wang2025rlcontam} demonstrated that all log-probability methods fail under RL training.\nOur work differs fundamentally in operating at the minimal-information level, requiring only binary response patterns.\n\n\\textbf{IRT for LLM evaluation.}\n\\citet{psnirt2026} introduced PSN-IRT, fitting 4PL models to LLM benchmark data and establishing validated item parameters.\n\\citet{polo2024tinybenchmarks} used IRT for efficient benchmark subsampling.\nOur work extends IRT from evaluation to contamination detection via person-fit statistics, a connection not previously explored.\n\n\\textbf{Person-fit in psychometrics.}\nPerson-fit statistics have a long history in educational testing \\citep{drasgow1985appropriateness,meijer1996person}.\nThe $\\ell_z^*$ statistic \\citep{snijders2001item} corrects for ability estimation error.\nOur contribution is connecting this literature to LLM contamination detection and identifying the $\\theta$-shift confound specific to the LLM setting.\n\n% ============================================================\n\\section{Conclusion}\n\nWe establish IRT person-fit statistics as a principled contamination detection framework operating at the minimal-information point---requiring only binary response patterns.\nThrough controlled experiments across four model families, we demonstrate detection with $|\\text{Cohen's } d| > 2.0$ in three of four families at 15\\% contamination on MMLU, with characterized boundary conditions for the fourth (Gemma, $|d|=1.3$).\nDetection power follows a predictable function of benchmark size ($R^2 = 0.88$), and $\\theta$-fixed analysis recovers monotonic dose-response in most families.\n\nIn the information-access landscape of contamination detection, $\\ell_z^*$ defines the best achievable detection from binary data alone (AUROC 0.80 at 15\\%, vs 0.62 for accuracy z-scores), while honestly trailing methods with privileged access (Min-K\\%++ AUROC 0.92).\nPreliminary evidence suggests structural robustness to RL-induced perturbation, where token-probability methods collapse.\nDomain-level analysis extends detection to contamination characterization, revealing distinct typologies in real-world models.\n\nThe universal 4PL model misfit finding---that LLM response patterns fundamentally differ from classical test-taker patterns---contributes to the broader understanding of psychometric methods applied to artificial agents, and the IRT parameter estimation challenges quantify the gap between classical and neural IRT that future work must bridge to enable large-scale leaderboard auditing.\n\n\\bibliographystyle{acl_natbib}\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "73c72b88-4b1b-41e4-8aee-8ef4f60cbcab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit…",
  "leafUuid": "7a0e9333-fd75-42d3-a526-e18d4e580ba9",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit detection of benchmark contamination",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---

### Tool call

_source line 24 · 2026-05-21T03:59:42.474Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013PinxkQdk1sWnVro6KJU9m`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a0e9333-fd75-42d3-a526-e18d4e580ba9",
  "isSidechain": false,
  "requestId": "req_011CbF3aDuakto6MTPizx2BD",
  "type": "assistant",
  "uuid": "8c275e7e-5fe5-4df4-8313-4a9e63ad329e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tngjuy2h8PiPPcZ51UJfHY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12926,
      "cache_read_input_tokens": 46834,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12926,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 46834,
          "cache_creation_input_tokens": 12926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12926
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

_source line 25 · 2026-05-21T03:59:43.896Z_

<details><summary>↩ Tool result · `toolu_013PinxkQdk1sWnVro6KJU9m`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
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

Package natbib Warning: Citation `sainz2023chatgpt' on page 1 undefined on inpu
t line 42.


Package natbib Warning: Citation `magar2022data' on page 1 undefined on input l
ine 42.


Package natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu
t line 46.


Package natbib Warning: Citation `deng2024investigating' on page 1 undefined on
 input line 46.


Package natbib Warning: Citation `oren2024proving' on page 1 undefined on input
 line 46.


Package natbib Warning: Citation `dong2024codec' on page 1 undefined on input l
ine 46.


Package natbib Warning: Citation `wang2025rlcontam' on page 1 undefined on inpu
t line 48.


Package natbib Warning: Citation `drasgow1985appropriateness' on page 1 undefin
ed on input line 54.


Package natbib Warning: Citation `snijders2001item' on page 1 undefined on inpu
t line 54.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `snijders2001item' on page 2 undefined on inpu
t line 88.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [2]

Package natbib Warning: Citation `psnirt2026' on page 3 undefined on input line
 120.


LaTeX Warning: Reference `eq:lzstar' on page 3 undefined on input line 123.


LaTeX Warning: Reference `sec:universal-misfit' on page 3 undefined on input li
ne 126.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 134.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 134.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 134.

[3]

Package natbib Warning: Citation `psnirt2026' on page 4 undefined on input line
 167.


LaTeX Warning: Reference `sec:power' on page 4 undefined on input line 168.


Package natbib Warning: Citation `oren2024proving' on page 4 undefined on input
 line 175.


Package natbib Warning: Citation `shi2024detecting' on page 4 undefined on inpu
t line 177.


LaTeX Warning: Reference `tab:pilot' on page 4 undefined on input line 194.


Package natbib Warning: Citation `snijders2001item' on page 4 undefined on inpu
t line 198.


Package natbib Warning: Citation `snijders2001item' on page 4 undefined on inpu
t line 198.


LaTeX Warning: Reference `sec:full-contam' on page 4 undefined on input line 21
6.

[4]

LaTeX Warning: Reference `tab:full-d' on page 5 undefined on input line 225.


LaTeX Warning: Reference `tab:dose-response' on page 5 undefined on input line 
225.


LaTeX Warning: Reference `tab:dose-response' on page 5 undefined on input line 
269.


LaTeX Warning: Reference `tab:mem-frac' on page 5 undefined on input line 272.


LaTeX Warning: Reference `tab:4pl-ablation' on page 5 undefined on input line 2
96.

[5]

LaTeX Warning: Reference `tab:baselines' on page 6 undefined on input line 326.



LaTeX Warning: Reference `tab:info-access' on page 6 undefined on input line 34
7.


LaTeX Warning: Reference `tab:power' on page 6 undefined on input line 374.

[6]

LaTeX Warning: Reference `tab:domain' on page 7 undefined on input line 406.


Package natbib Warning: Citation `wang2025rlcontam' on page 7 undefined on inpu
t line 441.

[7]

LaTeX Warning: Reference `tab:post-rl-comparison' on page 8 undefined on input 
line 480.


LaTeX Warning: Reference `tab:irt-refit' on page 8 undefined on input line 509.


[8]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 517.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 517.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 517.


Package natbib Warning: Citation `hong2021multiscale' on page 9 undefined on in
put line 544.


Overfull \hbox (18.18495pt too wide) in paragraph at lines 562--565
\T1/ptm/m/n/10.95 proaches). Im-por-tantly, cross-benchmark ag-gre-ga-tion ob-s
cures benchmark-specific con-tam-i-na-tion patterns---
[9]

Package natbib Warning: Citation `dodge2021documenting' on page 10 undefined on
 input line 589.


Package natbib Warning: Citation `brown2020language' on page 10 undefined on in
put line 589.


Package natbib Warning: Citation `shi2024detecting' on page 10 undefined on inp
ut line 590.


Package natbib Warning: Citation `deng2024investigating' on page 10 undefined o
n input line 591.


Package natbib Warning: Citation `oren2024proving' on page 10 undefined on inpu
t line 592.


Package natbib Warning: Citation `dong2024codec' on page 10 undefined on input 
line 593.


Package natbib Warning: Citation `wang2025rlcontam' on page 10 undefined on inp
ut line 594.


Package natbib Warning: Citation `psnirt2026' on page 10 undefined on input lin
e 598.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 10 undefined 
on input line 599.


Package natbib Warning: Citation `drasgow1985appropriateness' on page 10 undefi
ned on input line 603.


Package natbib Warning: Citation `meijer1996person' on page 10 undefined on inp
ut line 603.


Package natbib Warning: Citation `snijders2001item' on page 10 undefined on inp
ut line 604.

[10]
No file paper.bbl.

Package natbib Warning: There were undefined citations.

[11] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim
es/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 224589 bytes).
Transcript written on paper.log.


Package natbib Warning: Citation `snijders2001item' on page 10 undefined on inp
ut line 604.

[10]
No file paper.bbl.

Package natbib Warning: There were undefined citations.

[11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim
es/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 227529 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c275e7e-5fe5-4df4-8313-4a9e63ad329e",
  "isSidechain": false,
  "promptId": "ec7c9be7-428e-4670-904e-cc8df713932d",
  "type": "user",
  "uuid": "721edca1-f79a-4102-bf64-9588bfb1c5be",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `sainz2023chatgpt' on page 1 undefined on inpu\nt line 42.\n\n\nPackage natbib Warning: Citation `magar2022data' on page 1 undefined on input l\nine 42.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu\nt line 46.\n\n\nPackage natbib Warning: Citation `deng2024investigating' on page 1 undefined on\n input line 46.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 1 undefined on input\n line 46.\n\n\nPackage natbib Warning: Citation `dong2024codec' on page 1 undefined on input l\nine 46.\n\n\nPackage natbib Warning: Citation `wang2025rlcontam' on page 1 undefined on inpu\nt line 48.\n\n\nPackage natbib Warning: Citation `drasgow1985appropriateness' on page 1 undefin\ned on input line 54.\n\n\nPackage natbib Warning: Citation `snijders2001item' on page 1 undefined on inpu\nt line 54.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `snijders2001item' on page 2 undefined on inpu\nt line 88.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [2]\n\nPackage natbib Warning: Citation `psnirt2026' on page 3 undefined on input line\n 120.\n\n\nLaTeX Warning: Reference `eq:lzstar' on page 3 undefined on input line 123.\n\n\nLaTeX Warning: Reference `sec:universal-misfit' on page 3 undefined on input li\nne 126.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 134.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\theta' on input line 134.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 134.\n\n[3]\n\nPackage natbib Warning: Citation `psnirt2026' on page 4 undefined on input line\n 167.\n\n\nLaTeX Warning: Reference `sec:power' on page 4 undefined on input line 168.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 4 undefined on input\n line 175.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 4 undefined on inpu\nt line 177.\n\n\nLaTeX Warning: Reference `tab:pilot' on page 4 undefined on input line 194.\n\n\nPackage natbib Warning: Citation `snijders2001item' on page 4 undefined on inpu\nt line 198.\n\n\nPackage natbib Warning: Citation `snijders2001item' on page 4 undefined on inpu\nt line 198.\n\n\nLaTeX Warning: Reference `sec:full-contam' on page 4 undefined on input line 21\n6.\n\n[4]\n\nLaTeX Warning: Reference `tab:full-d' on page 5 undefined on input line 225.\n\n\nLaTeX Warning: Reference `tab:dose-response' on page 5 undefined on input line \n225.\n\n\nLaTeX Warning: Reference `tab:dose-response' on page 5 undefined on input line \n269.\n\n\nLaTeX Warning: Reference `tab:mem-frac' on page 5 undefined on input line 272.\n\n\nLaTeX Warning: Reference `tab:4pl-ablation' on page 5 undefined on input line 2\n96.\n\n[5]\n\nLaTeX Warning: Reference `tab:baselines' on page 6 undefined on input line 326.\n\n\n\nLaTeX Warning: Reference `tab:info-access' on page 6 undefined on input line 34\n7.\n\n\nLaTeX Warning: Reference `tab:power' on page 6 undefined on input line 374.\n\n[6]\n\nLaTeX Warning: Reference `tab:domain' on page 7 undefined on input line 406.\n\n\nPackage natbib Warning: Citation `wang2025rlcontam' on page 7 undefined on inpu\nt line 441.\n\n[7]\n\nLaTeX Warning: Reference `tab:post-rl-comparison' on page 8 undefined on input \nline 480.\n\n\nLaTeX Warning: Reference `tab:irt-refit' on page 8 undefined on input line 509.\n\n\n[8]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 517.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 517.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 517.\n\n\nPackage natbib Warning: Citation `hong2021multiscale' on page 9 undefined on in\nput line 544.\n\n\nOverfull \\hbox (18.18495pt too wide) in paragraph at lines 562--565\n\\T1/ptm/m/n/10.95 proaches). Im-por-tantly, cross-benchmark ag-gre-ga-tion ob-s\ncures benchmark-specific con-tam-i-na-tion patterns---\n[9]\n\nPackage natbib Warning: Citation `dodge2021documenting' on page 10 undefined on\n input line 589.\n\n\nPackage natbib Warning: Citation `brown2020language' on page 10 undefined on in\nput line 589.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 10 undefined on inp\nut line 590.\n\n\nPackage natbib Warning: Citation `deng2024investigating' on page 10 undefined o\nn input line 591.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 10 undefined on inpu\nt line 592.\n\n\nPackage natbib Warning: Citation `dong2024codec' on page 10 undefined on input \nline 593.\n\n\nPackage natbib Warning: Citation `wang2025rlcontam' on page 10 undefined on inp\nut line 594.\n\n\nPackage natbib Warning: Citation `psnirt2026' on page 10 undefined on input lin\ne 598.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 10 undefined \non input line 599.\n\n\nPackage natbib Warning: Citation `drasgow1985appropriateness' on page 10 undefi\nned on input line 603.\n\n\nPackage natbib Warning: Citation `meijer1996person' on page 10 undefined on inp\nut line 603.\n\n\nPackage natbib Warning: Citation `snijders2001item' on page 10 undefined on inp\nut line 604.\n\n[10]\nNo file paper.bbl.\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim\nes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 224589 bytes).\nTranscript written on paper.log.\n\n\nPackage natbib Warning: Citation `snijders2001item' on page 10 undefined on inp\nut line 604.\n\n[10]\nNo file paper.bbl.\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim\nes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 227529 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8c275e7e-5fe5-4df4-8313-4a9e63ad329e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-21T03:59:50.246Z_

<details><summary>Logged reasoning block</summary>

```text
The paper compiled successfully to 11 pages PDF. There are expected warnings about undefined citations (no .bbl file since we don't have a references.bib) and some label reference warnings that resolved on the second pass. The PDF is generated at 227KB.

Let me verify the output file exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "721edca1-f79a-4102-bf64-9588bfb1c5be",
  "isSidechain": false,
  "requestId": "req_011CbF3aeYAf5wWXCmzu51bu",
  "type": "assistant",
  "uuid": "36f11eb7-acef-4202-af49-1f98a052724a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AzKFM7Ew9AsuNcza133r8E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5487,
      "cache_read_input_tokens": 59760,
      "output_tokens": 401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 401,
          "cache_read_input_tokens": 59760,
          "cache_creation_input_tokens": 5487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5487
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

_source line 27 · 2026-05-21T03:59:56.187Z_

PDF compiled successfully (11 pages, 228KB). All 10 experiments from `experiment_data.json` are covered:

| Experiment | Section | Table(s) |
|---|---|---|
| Controlled Contamination Pilot | §5.1 | Table 1 |
| Full Controlled Contamination | §5.2 | Tables 2, 3, 4 |
| 4PL vs 3PL Ablation | §5.3 | Table 5 |
| Baseline Comparison | §5.4 | Tables 6, 7 |
| Extra Benchmarks (BBH+MATH) | §5.5 | Table 8 |
| Domain-Level Analysis | §5.6 | Table 9 |
| Post-RL Hypothesis Test | §6.1 | Tables 10, 11 |
| v1 IRT Refit Expanded | §6.2 | Table 12 |
| Natural Experiment | §6.3 | Table 13 |
| Multiscale lzm | §6.4 | Table 14 |
| Leaderboard Audit (ABANDONED) | §6.2 | mentioned in text |

Citations are undefined (no .bib file) but all cross-references resolve. Output at `median/paper.pdf`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36f11eb7-acef-4202-af49-1f98a052724a",
  "isSidechain": false,
  "requestId": "req_011CbF3aeYAf5wWXCmzu51bu",
  "type": "assistant",
  "uuid": "27ba3284-0af7-4ee4-ad0a-85ed4760e425",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260521T032820/median",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AzKFM7Ew9AsuNcza133r8E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5487,
      "cache_read_input_tokens": 59760,
      "output_tokens": 401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 401,
          "cache_read_input_tokens": 59760,
          "cache_creation_input_tokens": 5487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5487
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit…",
  "leafUuid": "27ba3284-0af7-4ee4-ad0a-85ed4760e425",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit detection of benchmark contamination",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T032820 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit…",
  "leafUuid": "27ba3284-0af7-4ee4-ad0a-85ed4760e425",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit detection of benchmark contamination",
  "sessionId": "7e7e1b6c-aed8-4cea-84f5-26f97c6334ef"
}
```

---
