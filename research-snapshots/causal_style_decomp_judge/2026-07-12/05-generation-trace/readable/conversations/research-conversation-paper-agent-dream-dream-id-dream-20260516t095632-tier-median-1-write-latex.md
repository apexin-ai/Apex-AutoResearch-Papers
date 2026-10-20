# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/a3a89adf-a587-4b3b-9fc7-e5c70454161c.jsonl`
- **Structured JSON:** [`9f17319b1e1599d4ec43.json`](../../sessions/9f/9f17319b1e1599d4ec43.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T10:19:50.784Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T10:19:50.784Z",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 1 核心成立但需降级措辞：ρ 从 \"reliably monotonic\" 改为 \"generally monotonic with occasional non-monotonicity at intermediate fractions\"；bootstrap CIs 变宽但下界仍 > 0.8。 Claim 2 within-gen early warning 从 \"AUC=0.984\" 降为 \"AUC=0.85-0.93 across scales\"， 加 caveat \"sensitivity amplitude decreases with model scale\"。Stable_rank 不再定位为 无条件最强 within-gen signal——改为 \"most sensitive but seed-variable; practitioners should combine with training_loss for robustness\"。PPL within-gen 失效仍是强论点但标注 \"N=1 scale verified, pending cross-config confirmation\"。Claim 3 taxonomy 保留但 LLaMA 列标注 \"preliminary (N=1, partial consistency)\"，Full FT method-dependence 标注 N=1 seed 限制。 论文仍可投 ARR 5/25，但 Limitations 需 1 整段讨论 statistical power 不足和 cross-family evidence 初步性。若推迟到 6/15 cycle 可能更安全。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T10:19:50.788Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T10:19:50.788Z",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-16T10:19:50.815Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 1 核心成立但需降级措辞：ρ 从 "reliably monotonic" 改为 "generally monotonic with occasional non-monotonicity at intermediate fractions"；bootstrap CIs 变宽但下界仍 > 0.8。 Claim 2 within-gen early warning 从 "AUC=0.984" 降为 "AUC=0.85-0.93 across scales"， 加 caveat "sensitivity amplitude decreases with model scale"。Stable_rank 不再定位为 无条件最强 within-gen signal——改为 "most sensitive but seed-variable; practitioners should combine with training_loss for robustness"。PPL within-gen 失效仍是强论点但标注 "N=1 scale verified, pending cross-config confirmation"。Claim 3 taxonomy 保留但 LLaMA 列标注 "preliminary (N=1, partial consistency)"，Full FT method-dependence 标注 N=1 seed 限制。 论文仍可投 ARR 5/25，但 Limitations 需 1 整段讨论 statistical power 不足和 cross-family evidence 初步性。若推迟到 6/15 cycle 可能更安全。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "55f86a0c-47b7-4429-a4ed-a402f351ff70",
  "type": "user",
  "uuid": "8fc62917-3837-403f-a8f1-cafddd3fe7b8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T10:19:50.814Z_

```json
{
  "parentUuid": "8fc62917-3837-403f-a8f1-cafddd3fe7b8",
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
  "uuid": "399ce771-98ae-47c2-affb-a9446966d5fd",
  "timestamp": "2026-05-16T10:19:50.814Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T10:19:50.814Z_

```json
{
  "parentUuid": "399ce771-98ae-47c2-affb-a9446966d5fd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3897ede5-c2a0-4ecc-9c29-ab7db0c7d021",
  "timestamp": "2026-05-16T10:19:50.814Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
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
  "aiTitle": "Generate simulated research paper for dream 20260516T095632",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---

### Assistant

_source line 7 · 2026-05-16T10:19:54.457Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3897ede5-c2a0-4ecc-9c29-ab7db0c7d021",
  "isSidechain": false,
  "requestId": "req_011Cb65XGWDnDT1LioFea1xA",
  "type": "assistant",
  "uuid": "ce9e23b0-7959-47fd-bb6d-b44dc8dabef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RTxihPcyrwJH4cCdBVNpnm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11351,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11351
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

_source line 8 · 2026-05-16T10:19:54.956Z_

<details open><summary>🔧 Tool call — Read · `toolu_0157ho5Yb3FvoTA4V59qHb15`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce9e23b0-7959-47fd-bb6d-b44dc8dabef0",
  "isSidechain": false,
  "requestId": "req_011Cb65XGWDnDT1LioFea1xA",
  "type": "assistant",
  "uuid": "08ed3c0e-2306-4597-b6fc-9533c650f0ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RTxihPcyrwJH4cCdBVNpnm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11351,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11351
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

_source line 9 · 2026-05-16T10:19:55.227Z_

<details><summary>↩ Tool result · `toolu_0157ho5Yb3FvoTA4V59qHb15`</summary>

```text
1	[
2	  {
3	    "name": "1.5B Within-Gen Early Warning Analysis",
4	    "description": "对 plan_001 已完成的 3-4 seeds × 4-5 fractions 数据做 within-gen 信号发散分析。 计算 step 50/100/200/500 各信号相对 baseline 的偏离幅度和检测 AUC。\n",
5	    "results": {
6	      "data_coverage_seeds": 4,
7	      "data_coverage_fractions": 5,
8	      "data_coverage_observations": 850,
9	      "stable_rank_step50_rel_divergence": 0.21,
10	      "stable_rank_step100_rel_divergence": 0.34,
11	      "training_loss_step50_rel_divergence": 0.15,
12	      "training_loss_step100_rel_divergence": 0.28,
13	      "perplexity_step50_rel_divergence": 0.04,
14	      "perplexity_step100_rel_divergence": 0.08,
15	      "spectral_entropy_step50_rel_divergence": 0.02,
16	      "spectral_entropy_step100_rel_divergence": 0.05,
17	      "stable_rank_within_gen_auc_1.5B": 0.89,
18	      "training_loss_within_gen_auc_1.5B": 0.83,
19	      "perplexity_within_gen_auc_1.5B": 0.56,
20	      "spectral_entropy_within_gen_auc_1.5B": 0.62,
21	      "token_entropy_within_gen_auc_1.5B": 0.51,
22	      "earliest_detection_step_stable_rank": 50,
23	      "earliest_detection_step_training_loss": 100,
24	      "amplitude_ratio_1.5B_vs_0.5B_stable_rank": 0.61,
25	      "amplitude_ratio_1.5B_vs_0.5B_training_loss": 0.72,
26	      "seed_variance_cv_stable_rank_step50": 0.045,
27	      "seed_variance_cv_training_loss_step50": 0.028
28	    },
29	    "tables": [
30	      {
31	        "name": "divergence_by_step_and_signal_1.5B",
32	        "columns": [
33	          "signal",
34	          "step_50_div",
35	          "step_100_div",
36	          "step_200_div",
37	          "step_500_div",
38	          "auc",
39	          "seed_cv"
40	        ],
41	        "rows": [
42	          [
43	            "stable_rank",
44	            0.21,
45	            0.34,
46	            0.52,
47	            0.71,
48	            0.89,
49	            0.045
50	          ],
51	          [
52	            "training_loss",
53	            0.15,
54	            0.28,
55	            0.41,
56	            0.58,
57	            0.83,
58	            0.028
59	          ],
60	          [
61	            "spectral_entropy",
62	            0.02,
63	            0.05,
64	            0.09,
65	            0.18,
66	            0.62,
67	            0.022
68	          ],
69	          [
70	            "perplexity",
71	            0.04,
72	            0.08,
73	            0.12,
74	            0.19,
75	            0.56,
76	            0.035
77	          ],
78	          [
79	            "token_entropy",
80	            0.03,
81	            0.06,
82	            0.11,
83	            0.15,
84	            0.51,
85	            0.041
86	          ]
87	        ]
88	      },
89	      {
90	        "name": "scale_comparison_within_gen_auc",
91	        "columns": [
92	          "signal",
93	          "auc_0.5B",
94	          "auc_1.5B",
95	          "amplitude_ratio",
96	          "scale_sensitivity"
97	        ],
98	        "rows": [
99	          [
100	            "stable_rank",
101	            0.984,
102	            0.89,
103	            0.61,
104	            "high"
105	          ],
106	          [
107	            "training_loss",
108	            0.923,
109	            0.83,
110	            0.72,
111	            "moderate"
112	          ],
113	          [
114	            "perplexity",
115	            0.534,
116	            0.56,
117	            "~1.0",
118	            "none"
119	          ],
120	          [
121	            "spectral_entropy",
122	            0.58,
123	            0.62,
124	            "~1.0",
125	            "none"
126	          ],
127	          [
128	            "token_entropy",
129	            0.478,
130	            0.51,
131	            "~1.0",
132	            "none"
133	          ]
134	        ]
135	      }
136	    ],
137	    "figures": [],
138	    "analysis": "核心发现：within-gen early warning 在 1.5B 上成立但 amplitude 系统性衰减。 stable_rank 仍为最强 within-gen detector（AUC=0.89），但与 training_loss（0.83） 差距缩小。PPL within-gen 失效在 1.5B 上再次确认（AUC=0.56 ≈ random）。 论文措辞从 \"AUC=0.984\" 改为 \"AUC=0.89-0.98 across scales (amplitude decreases with model scale)\"。seed CV=0.045 意味着个别 seed 的 AUC 可能低至 0.82。 4-seed bootstrap 95% CI 估计：[0.82, 0.94]，下界仍有意义但远不如 0.5B 的 [0.978, 0.989]。 Limitation 段需要讨论：更大模型的参数冗余稀释了 adapter 的谱信号。\n\n\n1.5B 模型参数冗余度高于 0.5B：QLoRA adapter 仅修改 ~2% 参数，同等 contamination 对权重矩阵谱结构的扰动被更大的 frozen 参数空间稀释。stable_rank 在 step 50 的 相对偏离从 0.5B 的 0.344 降至 ~0.21，仍可检测但幅度缩小约 40%。training_loss 作为训练集 CE 直接测量被污染分布的学习动态，受模型规模影响较小（优化器对 corrupted tokens 的梯度信号依然存在），因此 AUC 降幅温和（0.923→0.83）。 held-out PPL 在 0.5B 上已经 within-gen 无效（AUC=0.534），1.5B 上稍有上升至 0.56 但仍接近 random——原因是 QLoRA 早期微调对 held-out 分布影响极微弱，需多代累积。 spectral_entropy 在 0.5B 上也是 late detector（仅 100% 下显著），1.5B 上类似。 seed 间 CV 在 0.03-0.06 范围内，因为 3-4 seeds 的 stable_rank 对初始化和 synthetic data 随机性敏感（seed44 经验已证实）。总体结论：within-gen early warning 在 1.5B 上成立但需降级 amplitude claim。\n"
139	  },
140	  {
141	    "name": "Early Warning Threshold Calibration & Cross-Config ROC",
142	    "description": "汇总 plan_001 (3-4 seeds) + plan_002 (3 seeds PubMed) 数据，计算 clustered bootstrap ROC，确定最小可靠检测阈值，验证 PPL within-gen 失效是否跨配置一致。\n",
143	    "results": {
144	      "n_seeds_wikitext": 4,
145	      "n_seeds_pubmed": 3,
146	      "n_fractions_wikitext": 5,
147	      "n_fractions_pubmed": 5,
148	      "clustered_bootstrap_n_resamples": 1000,
149	      "stable_rank_auc_wikitext_1.5B": 0.89,
150	      "stable_rank_auc_wikitext_1.5B_ci_lower": 0.81,
151	      "stable_rank_auc_wikitext_1.5B_ci_upper": 0.94,
152	      "stable_rank_auc_pubmed_1.5B": 0.86,
153	      "stable_rank_auc_pubmed_1.5B_ci_lower": 0.77,
154	      "stable_rank_auc_pubmed_1.5B_ci_upper": 0.93,
155	      "training_loss_auc_wikitext_1.5B": 0.83,
156	      "training_loss_auc_pubmed_1.5B": 0.8,
157	      "perplexity_auc_wikitext_1.5B": 0.56,
158	      "perplexity_auc_pubmed_1.5B": 0.52,
159	      "perplexity_auc_cross_config_range": [
160	        0.5,
161	        0.58
162	      ],
163	      "optimal_threshold_stable_rank_sensitivity": 0.72,
164	      "optimal_threshold_stable_rank_specificity": 0.95,
165	      "min_fraction_detectable_at_step100": 0.25,
166	      "false_positive_rate_at_frac0": 0.04
167	    },
168	    "tables": [
169	      {
170	        "name": "cross_config_within_gen_auc_comparison",
171	        "columns": [
172	          "signal",
173	          "wikitext_0.5B",
174	          "wikitext_1.5B",
175	          "pubmed_1.5B",
176	          "cross_config_consistency"
177	        ],
178	        "rows": [
179	          [
180	            "stable_rank",
181	            0.984,
182	            "0.89 [0.81,0.94]",
183	            "0.86 [0.77,0.93]",
184	            "consistent_but_attenuated"
185	          ],
186	          [
187	            "training_loss",
188	            0.923,
189	            "0.83 [0.74,0.90]",
190	            "0.80 [0.70,0.88]",
191	            "consistent_but_attenuated"
192	          ],
193	          [
194	            "perplexity",
195	            0.534,
196	            "0.56 [0.44,0.66]",
197	            "0.52 [0.41,0.63]",
198	            "consistent_near_random"
199	          ],
200	          [
201	            "spectral_entropy",
202	            0.58,
203	            "0.62 [0.50,0.72]",
204	            "0.59 [0.47,0.70]",
205	            "consistent_weak"
206	          ],
207	          [
208	            "token_entropy",
209	            0.478,
210	            "0.51 [0.40,0.62]",
211	            "0.49 [0.38,0.60]",
212	            "consistent_near_random"
213	          ]
214	        ]
215	      },
216	      {
217	        "name": "threshold_operating_points",
218	        "columns": [
219	          "signal",
220	          "threshold_pct_deviation",
221	          "sensitivity",
222	          "specificity",
223	          "ppv",
224	          "frac_min_detectable"
225	        ],
226	        "rows": [
227	          [
228	            "stable_rank",
229	            "15%",
230	            0.72,
231	            0.95,
232	            0.88,
233	            0.25
234	          ],
235	          [
236	            "training_loss",
237	            "10%",
238	            0.68,
239	            0.92,
240	            0.82,
241	            0.25
242	          ],
243	          [
244	            "combined_sr_tl",
245	            "SR>10% OR TL>8%",
246	            0.85,
247	            0.9,
248	            0.81,
249	            0.1
250	          ]
251	        ]
252	      }
253	    ],
254	    "figures": [],
255	    "analysis": "3-4 seed clustered bootstrap 的 CI 太宽无法做 formal significance claim（CI lower bound 0.81 跨过了一些 \"clinically meaningful\" 阈值但未跨 0.5）。 Cross-config PPL within-gen 失效验证是强结果——两个 domain 两个 scale 一致 AUC~0.5，但只有 3 个 data points（0.5B-Wiki, 1.5B-Wiki, 1.5B-PubMed）， camera-ready 需 plan_012 Full FT 数据。Combined threshold (SR>10% OR TL>8%) 提升 sensitivity 到 0.85 且能检测 frac=0.10——这是 practitioner recommendation 的基础。Limitations：threshold 优化在 same data 上做有 overfitting risk， 理想需 held-out seed 验证。\n\n\nClustered bootstrap 以 seed 为聚类单位（而非 pooling 所有 step×gen observations）， 有效样本量从数百降到 3-4，导致 CIs 显著变宽。stable_rank CI 宽度 ~0.13（对比 0.5B N=1 的 [0.978, 0.989] 宽度 0.011），这是 median 档 statistical power 不足的直接体现。PubMed AUC 略低于 WikiText（0.86 vs 0.89）因为 biomedical domain 的 baseline variance 更高（specialized tokens 的梯度更 noisy）。 PPL within-gen AUC 跨两个 domain 一致在 0.50-0.58 范围，这强化了 \"held-out PPL within-gen 失效\" 的 claim 但仅有 2 个 config 验证，无法升级到 camera-ready 措辞。 最优阈值 sensitivity=0.72 意味着 28% false negative——practitioners 不能仅靠 单一信号，需组合 stable_rank + training_loss。frac=0.25 在 step 100 可检出 说明 moderate contamination 的 early warning 仍然可能，但 frac=0.1 不行。\n"
256	  },
257	  {
258	    "name": "Per-Layer Collapse Propagation Analysis (1.5B)",
259	    "description": "对 plan_001 已完成的 3-4 seeds 的 1.5B checkpoints 做 forward-pass SVD， 分析 28 层 × 各 sub-module 的谱变化模式。\n",
260	    "results": {
261	      "n_layers_analyzed": 28,
262	      "n_submodules_per_layer": 7,
263	      "n_seeds_available": 3,
264	      "v_proj_mean_sr_increase_100pct": 4.2,
265	      "v_proj_sr_increase_range": [
266	        2.8,
267	        5.6
268	      ],
269	      "down_proj_collapse_layers": [
270	        22,
271	        23,
272	        24,
273	        25
274	      ],
275	      "down_proj_sr_decrease_max": -4.8,
276	      "k_proj_mean_sr_increase": 1.1,
277	      "q_proj_mean_sr_increase": 1.4,
278	      "o_proj_mean_sr_change": 0.3,
279	      "most_sensitive_submodule": "v_proj",
280	      "most_sensitive_layer_range": [
281	        20,
282	        27
283	      ],
284	      "layer_onset_order": "late layers (L22-27) → mid layers (L12-18) → early layers (L0-5)",
285	      "cross_seed_layer_pattern_consistency": "2/3 seeds agree on v_proj dominance; 1 seed shows k_proj co-dominant",
286	      "baseline_0pct_max_sr_drift": 0.45
287	    },
288	    "tables": [
289	      {
290	        "name": "submodule_sensitivity_ranking_1.5B",
291	        "columns": [
292	          "submodule",
293	          "mean_delta_sr_100pct",
294	          "std_across_seeds",
295	          "rank",
296	          "consistent_with_0.5B"
297	        ],
298	        "rows": [
299	          [
300	            "v_proj",
301	            4.2,
302	            1.1,
303	            1,
304	            true
305	          ],
306	          [
307	            "q_proj",
308	            1.4,
309	            0.6,
310	            2,
311	            true
312	          ],
313	          [
314	            "k_proj",
315	            1.1,
316	            0.8,
317	            3,
318	            true
319	          ],
320	          [
321	            "up_proj",
322	            0.8,
323	            0.4,
324	            4,
325	            true
326	          ],
327	          [
328	            "gate_proj",
329	            0.5,
330	            0.3,
331	            5,
332	            true
333	          ],
334	          [
335	            "o_proj",
336	            0.3,
337	            0.2,
338	            6,
339	            true
340	          ],
341	          [
342	            "down_proj",
343	            -3.2,
344	            1.5,
345	            "N/A (collapse)",
346	            true
347	          ]
348	        ]
349	      }
350	    ],
351	    "figures": [],
352	    "analysis": "1.5B per-layer 分析确认 sub-module-centric pattern 跨 scale 泛化。v_proj 仍是最敏感 indicator（practitioner takeaway 不变）。新发现：1.5B 的 layer onset 更清晰呈现 \"late→mid→early\" 的传播序列（0.5B 层数少区分度不够）。 但 N=3 seeds 的 cross-seed consistency 不足以做 formal claim——1 个 seed 的 k_proj 与 v_proj 接近等强度。论文中标注为 \"predominant pattern\" 而非 \"universal\"。down_proj collapse 位置从 0.5B 的 L11-12 移到 1.5B 的 L22-25 （相对位置一致 ~78-89% depth），支持 \"FFN bottleneck vulnerability\" 解释。\n\n\n1.5B (28 layers) 比 0.5B (24 layers) 有更多层供 collapse 传播。0.5B 已显示 v_proj 在几乎所有层 diffuse（ΔSR +1~+3），1.5B 的更深架构预期显示类似 pattern 但幅度更大（更多参数 → 每层 adapter 修改的相对占比更小 → 需要更多层协同才能 表达 same level of corruption → late layers 先 collapse 因为离 loss 最近）。 down_proj collapse 出现在 L22-25（对应 0.5B 的 L11-12），因为 down_proj 是 FFN 的压缩瓶颈，synthetic data 的低 diversity 导致这些投影矩阵的 effective rank 降低。cross-seed consistency 在 median 档下不完美（3 seeds 中 1 个 因初始化差异可能显示稍不同的 sub-module ranking），但 v_proj 作为 most sensitive 的结论在 2/3 seeds 中一致。layer onset order \"late→mid→early\" 反映 梯度从 loss 向前传播的 collapse 扩散模式。\n"
353	  },
354	  {
355	    "name": "LLaMA-3.2-1B Cross-Family Validation",
356	    "description": "LLaMA-3.2-1B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens。 验证 collapse monitoring signals 是否跨 model family 泛化。\n",
357	    "results": {
358	      "model": "LLaMA-3.2-1B",
359	      "n_fractions": 3,
360	      "n_seeds": 1,
361	      "n_generations": 5,
362	      "signals_direction_consistent": 7,
363	      "signals_total": 11,
364	      "signals_inconsistent": 2,
365	      "signals_insignificant": 2,
366	      "consistent_signals": [
367	        "stable_rank",
368	        "spectral_entropy",
369	        "perplexity",
370	        "token_entropy",
371	        "training_loss",
372	        "self_bleu",
373	        "gradient_norm"
374	      ],
375	      "inconsistent_signals": [
376	        "distinct_1",
377	        "hellaswag"
378	      ],
379	      "insignificant_signals": [
380	        "distinct_2",
381	        "distinct_3"
382	      ],
383	      "llama_gen4_100pct_ppl": 580.0,
384	      "llama_gen4_100pct_stable_rank": 142.5,
385	      "llama_gen4_100pct_spectral_entropy": 0.871,
386	      "llama_gen4_100pct_token_entropy": 0.91,
387	      "llama_gen4_50pct_ppl": 14.8,
388	      "llama_gen4_0pct_ppl": 13.1,
389	      "spearman_rho_core_4signals": 1.0,
390	      "collapse_magnitude_ppl": "44x (vs Qwen 0.5B 53x, Qwen 1.5B ~35x)",
391	      "collapse_magnitude_stable_rank": "5.8x (vs Qwen 0.5B 6.6x)",
392	      "hellaswag_100pct_gen4": 0.38,
393	      "hellaswag_50pct_gen4": 0.41,
394	      "hellaswag_0pct_gen4": 0.4,
395	      "self_recovery_50pct_present": true,
396	      "recovery_ratio_ppl": 0.48
397	    },
398	    "tables": [
399	      {
400	        "name": "llama_vs_qwen_signal_direction",
401	        "columns": [
402	          "signal",
403	          "qwen_0.5B_direction",
404	          "qwen_1.5B_direction",
405	          "llama_1B_direction",
406	          "consistent"
407	        ],
408	        "rows": [
409	          [
410	            "stable_rank",
411	            "↑",
412	            "↑",
413	            "↑",
414	            "✓"
415	          ],
416	          [
417	            "spectral_entropy",
418	            "↑",
419	            "↑",
420	            "↑",
421	            "✓"
422	          ],
423	          [
424	            "perplexity",
425	            "↑",
426	            "↑",
427	            "↑",
428	            "✓"
429	          ],
430	          [
431	            "token_entropy",
432	            "↓",
433	            "↓",
434	            "↓",
435	            "✓"
436	          ],
437	          [
438	            "training_loss",
439	            "↑",
440	            "↑",
441	            "↑",
442	            "✓"
443	          ],
444	          [
445	            "gradient_norm",
446	            "↓",
447	            "↓",
448	            "↓",
449	            "✓"
450	          ],
451	          [
452	            "self_bleu",
453	            "↑",
454	            "↑",
455	            "↑",
456	            "✓"
457	          ],
458	          [
459	            "distinct_1",
460	            "↓",
461	            "↓",
462	            "↑ (weak)",
463	            "✗"
464	          ],
465	          [
466	            "distinct_2",
467	            "↓",
468	            "↓",
469	            "≈0",
470	            "?"
471	          ],
472	          [
473	            "distinct_3",
474	            "↓",
475	            "↓",
476	            "≈0",
477	            "?"
478	          ],
479	          [
480	            "hellaswag",
481	            "↓ (weak)",
482	            "↓",
483	            "↑ (0.01)",
484	            "✗"
485	          ]
486	        ]
487	      },
488	      {
489	        "name": "llama_collapse_trajectory",
490	        "columns": [
491	          "fraction",
492	          "gen0_ppl",
493	          "gen1_ppl",
494	          "gen2_ppl",
495	          "gen3_ppl",
496	          "gen4_ppl",
497	          "gen4_sr",
498	          "gen4_se"
499	        ],
500	        "rows": [
501	          [
502	            "0%",
503	            13.1,
504	            13.0,
505	            13.2,
506	            13.1,
507	            13.1,
508	            25.6,
509	            0.712
510	          ],
511	          [
512	            "50%",
513	            13.1,
514	            14.2,
515	            14.9,
516	            15.1,
517	            14.8,
518	            27.1,
519	            0.724
520	          ],
521	          [
522	            "100%",
523	            13.1,
524	            118.5,
525	            342.0,
526	            498.0,
527	            580.0,
528	            142.5,
529	            0.871
530	          ]
531	        ]
532	      }
533	    ],
534	    "figures": [],
535	    "analysis": "7/11 signals direction-consistent 足以支撑 \"cross-family validated (preliminary)\" 但不足以 claim \"architecture-agnostic\"。论文 taxonomy table 的 LLaMA 列标注 \"N=1, 7/11 consistent\"。inconsistent signals（distinct_1, hellaswag）恰好是 在 Qwen QLoRA 上已被标注为 weak/method-dependent 的信号，因此不削弱核心 claims。 4 个 core signals（SR, SE, PPL, TE）全部一致，核心 Claim 1 的 cross-family evidence 较强。但 N=1 seed 无法排除 cherry-pick effect——Discussion 段标注 \"single seed, pending multi-seed confirmation\"。collapse magnitude（44x PPL） 在合理范围内，架构差异只影响 absolute scale 不影响 direction。Self-recovery 跨 family 观察到进一步支持 \"data mixing effect\" 解释（非 Qwen-specific）。 若推迟到 6/15 可补 1-2 seeds 显著加强此 claim。\n\n\nLLaMA-3.2-1B（1.24B params, 16 layers, vocab=128k）与 Qwen2.5 系列架构差异： (1) RoPE 实现不同, (2) vocab size 128k vs 151k, (3) GQA vs MQA。核心 spectral/output signals 的方向（SR↑, SE↑, TE↓, PPL↑）由 collapse 的基本物理决定（重复训练 → 权重矩阵 rank 膨胀 + 输出分布收缩），这些与架构细节无关，因此 7/11 方向一致。\ndistinct_1 不一致：LLaMA 128k vocab 的 token granularity 更细（subword 切分更碎）， collapsed model 的词汇多样性表现不同——Qwen 上 distinct_1 下降 3% 而 LLaMA 上 可能因 subword 效应反而轻微上升。hellaswag 在 LLaMA 上不一致原因：QLoRA 正则化 + LLaMA 的 downstream task 对 collapse 的 sensitivity 不同（0.5B Qwen 已经 显示 QLoRA 下 hellaswag 基本不动，LLaMA 可能出现轻微反向——gen4 collapsed model 偶然在某些 hellaswag 模式上表现稍好）。distinct_2/3 不显著因 N=1 variance 大。\nPPL collapse 幅度 44x 略低于 Qwen 0.5B 的 53x，因为 LLaMA 128k vocab 的 token-level entropy baseline 不同（更大 vocab → 更分散的 softmax → 不同的 PPL dynamics）。但方向一致且幅度在同一量级。self-recovery 在 50% 处仍观察到 （RR=0.48）因为这是 data mixing 的通用效应，非 architecture-specific。\n"
536	  },
537	  {
538	    "name": "Full FT Multi-Seed Extension",
539	    "description": "0.5B × WikiText-2 × 3 fractions (0/50/100%) × 2 additional seeds × 5 gens， 将 Full FT 对比从 N=1 扩展到 N=3。\n",
540	    "results": {
541	      "status": "NOT_STARTED",
542	      "reason": "GPU budget exhausted by plan_001/002/010/011; no remaining capacity before ARR 5/25",
543	      "implication_for_paper": "Claim 3 method-dependence 仍基于 N=1 Full FT seed。Limitations 必须标注： \"Full FT comparison based on single seed; direction consistency observed but variance uncharacterized. Multi-seed replication planned for camera-ready.\"\n",
544	      "risk_assessment": "Reviewer 要求 Full FT replication 的概率 ~40%。如果 6/15 cycle 提交， 可在 rebuttal 前完成 2 extra seeds。5/25 提交则只能在 response 中 promise。\n",
545	      "mitigation": "plan_003 的 signal direction consistency 6/6 + plan_010 3B spot-check direction match 提供间接 evidence（不同 scale 方向一致暗示 robustness）， 但不替代 same-config multi-seed。\n"
546	    },
547	    "tables": [],
548	    "figures": [],
549	    "analysis": "Plan_012 未启动是 median 档 \"scope 升级后 resource 不足\" 的典型表现。 5/25 提交版本中 Claim 3 的 method-dependence evidence 仍为 N=1，这是 最可能被 reviewer flag 的单点。缓解策略：(1) 在 Limitations 中 proactively 标注, (2) 强调 direction consistency 6/6 的 qualitative strength, (3) 承诺 camera-ready 补充 2 extra seeds。若选择 6/15 cycle，有 3 周 GPU 时间可完成此实验。\n\n\nMedian 档核心假设之一是 \"Full FT multi-seed (plan012) 未启动，N=1 限制仍在\"。 原因：plan_001 的 30 runs 在 2 GPU 上消耗 ~150h（已 10/30 completed）， plan_002 在 3 GPU 上消耗 ~45h（仍在运行），plan_010 3B spot-check 占 1 GPU ~8h。在 5/25 deadline 前无 GPU slot 给 plan_012 的额外 30 runs（~40h on 0.5B Full FT, A6000 ~1.3h/run）。这不是技术困难而是纯粹的 resource scheduling constraint。\n"
550	  },
551	  {
552	    "name": "MMLU-Mini Downstream Evaluation",
553	    "description": "对 plan_001 已完成 checkpoints 运行 MMLU-mini（~100 questions × 4 subjects）， 作为第二个 downstream benchmark 补充 HellaSwag。\n",
554	    "results": {
555	      "n_checkpoints_evaluated": 60,
556	      "n_seeds_available": 3,
557	      "mmlu_baseline_0pct_gen0": 0.36,
558	      "mmlu_0pct_gen4": 0.35,
559	      "mmlu_50pct_gen4": 0.34,
560	      "mmlu_100pct_gen4": 0.29,
561	      "mmlu_cross_frac_rho": -0.87,
562	      "mmlu_cross_gen_rho_100pct": -0.8,
563	      "mmlu_sensitivity_vs_hellaswag": "slightly higher (Δ=-0.07 at 100% vs HellaSwag Δ=-0.03 QLoRA)",
564	      "mmlu_method_dependence": "QLoRA: weak degradation (-7pt); consistent with HellaSwag pattern",
565	      "seed_variance_mmlu_100pct": 0.025,
566	      "mmlu_within_gen_auc": 0.55,
567	      "mmlu_per_subject_variance": "STEM -9pt, Humanities -5pt, Social -6pt, Other -4pt"
568	    },
569	    "tables": [
570	      {
571	        "name": "mmlu_mini_by_fraction_and_generation",
572	        "columns": [
573	          "fraction",
574	          "gen0",
575	          "gen1",
576	          "gen2",
577	          "gen3",
578	          "gen4",
579	          "delta_gen04"
580	        ],
581	        "rows": [
582	          [
583	            "0%",
584	            0.36,
585	            0.36,
586	            0.35,
587	            0.35,
588	            0.35,
589	            -0.01
590	          ],
591	          [
592	            "50%",
593	            0.36,
594	            0.35,
595	            0.35,
596	            0.34,
597	            0.34,
598	            -0.02
599	          ],
600	          [
601	            "100%",
602	            0.36,
603	            0.33,
604	            0.31,
605	            0.3,
606	            0.29,
607	            -0.07
608	          ]
609	        ]
610	      },
611	      {
612	        "name": "mmlu_vs_hellaswag_comparison",
613	        "columns": [
614	          "metric",
615	          "hellaswag_delta_100pct",
616	          "mmlu_delta_100pct",
617	          "within_gen_auc",
618	          "cross_frac_rho"
619	        ],
620	        "rows": [
621	          [
622	            "QLoRA_0.5B",
623	            -0.002,
624	            -0.07,
625	            "0.51 / 0.55",
626	            "-0.72 / -0.87"
627	          ],
628	          [
629	            "QLoRA_1.5B",
630	            "pending",
631	            -0.07,
632	            "pending / 0.55",
633	            "pending / -0.87"
634	          ]
635	        ]
636	      }
637	    ],
638	    "figures": [],
639	    "analysis": "MMLU-mini 提供了比 HellaSwag 更敏感的 downstream collapse indicator（under QLoRA）， 部分解决 \"HellaSwag 在 QLoRA 下不动\" 的问题。但 within-gen AUC 仍近 random， 确认 downstream metrics 不适合 early warning。论文可新增一句： \"Knowledge benchmarks (MMLU) show moderate sensitivity to collapse (-7pt at frac=100%) while commonsense reasoning (HellaSwag) remains stable under QLoRA, suggesting collapse selectively erodes factual knowledge before reasoning ability.\" 这强化 Claim 3 taxonomy 的 granularity。Limitations：MMLU-mini 只 100 题， per-subject N=25 的 variance 大；full MMLU 验证留作 camera-ready。\n\n\nMMLU-mini 测量知识保留而非语言建模能力。在 QLoRA collapse 下，模型的 token 分布坍缩但参数空间大部分 frozen，因此知识保留受损程度有限。100% contamination gen4 的 -7pt 下降（0.36→0.29）比 HellaSwag 的 -0.3pt（QLoRA 下几乎不动） 更大，因为 MMLU 需要 factual recall 而 HellaSwag 是 commonsense reasoning—— collapse 优先损害 fact-level 记忆（被 synthetic noise 覆盖）而非推理能力 （由 frozen 参数维持）。但总体幅度仍然 modest（-7pt on random=25% baseline）， 这与 writing note 10 的 \"QLoRA 正则化保护 downstream\" 结论一致。\nMMLU within-gen AUC=0.55 接近 random，原因同 HellaSwag/PPL：downstream 评估 需要多代累积才能看到效果，within-gen 的参数变化太小。cross-frac ρ=-0.87 （非完美 -1.0 因为 50% 和 0% 差异很小，只有 100% 有显著 drop）。 STEM 受损最大因为 factual precision 要求最高。seed variance 0.025 意味着 3 seeds 的 MMLU scores 相当一致（downstream eval 的 variance 主要来自 question sampling 而非 model 随机性）。\n"
640	  },
641	  {
642	    "name": "Within-Gen AUROC Formal Statistics (1.5B, 3-4 Seeds)",
643	    "description": "使用 plan_001 的 3-4 seed 数据重算 within-generation binary AUROC， 从 N=1 (0.5B) 升级到 N=3-4 (1.5B) 的 clustered bootstrap 正式统计。\n",
644	    "results": {
645	      "n_seeds_used": 4,
646	      "bootstrap_method": "clustered by seed, 2000 resamples",
647	      "stable_rank_auc_mean": 0.88,
648	      "stable_rank_auc_ci_95": [
649	        0.8,
650	        0.94
651	      ],
652	      "stable_rank_auc_ci_width": 0.14,
653	      "training_loss_auc_mean": 0.82,
654	      "training_loss_auc_ci_95": [
655	        0.73,
656	        0.89
657	      ],
658	      "perplexity_auc_mean": 0.55,
659	      "perplexity_auc_ci_95": [
660	        0.43,
661	        0.65
662	      ],
663	      "spectral_entropy_auc_mean": 0.61,
664	      "spectral_entropy_auc_ci_95": [
665	        0.48,
666	        0.72
667	      ],
668	      "token_entropy_auc_mean": 0.5,
669	      "token_entropy_auc_ci_95": [
670	        0.39,
671	        0.61
672	      ],
673	      "formal_significance_stable_rank": "CI lower bound 0.80 > 0.5, significant",
674	      "formal_significance_training_loss": "CI lower bound 0.73 > 0.5, significant",
675	      "formal_significance_perplexity": "CI crosses 0.5, NOT significant for within-gen",
676	      "comparison_to_0.5B_N1": "0.5B AUC=0.984 falls outside 1.5B 95% CI upper bound (0.94), confirming scale attenuation",
677	      "practical_implication": "stable_rank remains actionable at 1.5B but recommend combined threshold with training_loss"
678	    },
679	    "tables": [
680	      {
681	        "name": "formal_within_gen_auroc_1.5B",
682	        "columns": [
683	          "signal",
684	          "auc_mean",
685	          "ci_lower",
686	          "ci_upper",
687	          "significant_vs_random",
688	          "rank"
689	        ],
690	        "rows": [
691	          [
692	            "stable_rank",
693	            0.88,
694	            0.8,
695	            0.94,
696	            true,
697	            1
698	          ],
699	          [
700	            "training_loss",
701	            0.82,
702	            0.73,
703	            0.89,
704	            true,
705	            2
706	          ],
707	          [
708	            "spectral_entropy",
709	            0.61,
710	            0.48,
711	            0.72,
712	            false,
713	            3
714	          ],
715	          [
716	            "perplexity",
717	            0.55,
718	            0.43,
719	            0.65,
720	            false,
721	            4
722	          ],
723	          [
724	            "token_entropy",
725	            0.5,
726	            0.39,
727	            0.61,
728	            false,
729	            5
730	          ]
731	        ]
732	      },
733	      {
734	        "name": "scale_attenuation_summary",
735	        "columns": [
736	          "signal",
737	          "auc_0.5B_N1",
738	          "auc_1.5B_N4",
739	          "attenuation_pct",
740	          "ci_overlap"
741	        ],
742	        "rows": [
743	          [
744	            "stable_rank",
745	            0.984,
746	            0.88,
747	            "-10.6%",
748	            "0.5B point outside 1.5B CI"
749	          ],
750	          [
751	            "training_loss",
752	            0.923,
753	            0.82,
754	            "-11.2%",
755	            "0.5B point outside 1.5B CI"
756	          ],
757	          [
758	            "perplexity",
759	            0.534,
760	            0.55,
761	            "+3.0%",
762	            "overlapping"
763	          ]
764	        ]
765	      }
766	    ],
767	    "figures": [],
768	    "analysis": "Plan_014 是将 Claim 2 从 \"anecdotal\" 升级到 \"formally supported\" 的关键。 4-seed clustered bootstrap 证明 stable_rank within-gen detection 在 1.5B 上 statistically significant（CI lower > 0.5）但不 excellent（CI upper < 0.95 in some resamples）。论文措辞从 \"AUC=0.984\" 改为 \"AUC=0.88 [0.80, 0.94] at 1.5B scale\"。Scale attenuation 本身成为一个 finding：\"sensitivity amplitude decreases with model scale, consistent with larger parameter spaces absorbing adapter perturbations\"。PPL within-gen 失效获得 formal backing：CI 跨 0.5 意味着无法 reject random detection。Combined recommendation（SR + TL）成为 唯一 robust practitioner guidance。如果 5/25 提交，这是 Claim 2 的 definitive statement——弱于原始但仍有价值。6/15 cycle 可补 seed46 收窄 CI。\n\n从 N=1 到 N=4 的 clustered bootstrap 是 median 档的核心 statistical upgrade。 seed 作为聚类单位意味着 effective N=4（不是 4 seeds × 5 fracs × 5 gens = 100 的 naive pooling）。Bootstrap CI 宽度 ~0.14 对应 4 个独立聚类的标准误 ~0.035（SE ≈ σ/√N, σ~0.07, N=4 → SE=0.035, 95% CI ≈ ±1.96×0.035 = ±0.07, total width 0.14）。这比 0.5B N=1 的 parametric CI [0.978, 0.989]（width 0.011） 宽 13 倍——不是因为 1.5B 更 noisy，而是因为 clustered bootstrap correctly accounts for seed-level dependence。\nstable_rank AUC=0.88 低于 0.5B 的 0.984 因为 scale attenuation（写作笔记已预期）。 CI lower bound 0.80 仍高于 random (0.5)，可以 claim \"significant within-gen detection\"。但不能 claim \"excellent detection\" (conventionally AUC>0.9)。 perplexity CI [0.43, 0.65] 跨越 0.5——formally 不能 reject null hypothesis of random detection。这paradoxically 让 \"PPL within-gen 失效\" 成为 statistically validated result（不能 reject H0: AUC=0.5）。\n5-seed 无法实现因 seed46 未 start + seed45 部分完成（median 档假设）， 故降为 4-seed bootstrap。如果 seed45 的 frac=0.5/1.0 数据缺失，可能 进一步降为 3-seed（CI width ~0.18），此时 stable_rank CI lower bound 可能落到 0.76，仍 significant 但 barely。\n"
769	  }
770	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08ed3c0e-2306-4597-b6fc-9533c650f0ea",
  "isSidechain": false,
  "promptId": "55f86a0c-47b7-4429-a4ed-a402f351ff70",
  "type": "user",
  "uuid": "5a77e1b5-04dc-439f-a137-1856fe8de5c8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"1.5B Within-Gen Early Warning Analysis\",\n    \"description\": \"对 plan_001 已完成的 3-4 seeds × 4-5 fractions 数据做 within-gen 信号发散分析。 计算 step 50/100/200/500 各信号相对 baseline 的偏离幅度和检测 AUC。\\n\",\n    \"results\": {\n      \"data_coverage_seeds\": 4,\n      \"data_coverage_fractions\": 5,\n      \"data_coverage_observations\": 850,\n      \"stable_rank_step50_rel_divergence\": 0.21,\n      \"stable_rank_step100_rel_divergence\": 0.34,\n      \"training_loss_step50_rel_divergence\": 0.15,\n      \"training_loss_step100_rel_divergence\": 0.28,\n      \"perplexity_step50_rel_divergence\": 0.04,\n      \"perplexity_step100_rel_divergence\": 0.08,\n      \"spectral_entropy_step50_rel_divergence\": 0.02,\n      \"spectral_entropy_step100_rel_divergence\": 0.05,\n      \"stable_rank_within_gen_auc_1.5B\": 0.89,\n      \"training_loss_within_gen_auc_1.5B\": 0.83,\n      \"perplexity_within_gen_auc_1.5B\": 0.56,\n      \"spectral_entropy_within_gen_auc_1.5B\": 0.62,\n      \"token_entropy_within_gen_auc_1.5B\": 0.51,\n      \"earliest_detection_step_stable_rank\": 50,\n      \"earliest_detection_step_training_loss\": 100,\n      \"amplitude_ratio_1.5B_vs_0.5B_stable_rank\": 0.61,\n      \"amplitude_ratio_1.5B_vs_0.5B_training_loss\": 0.72,\n      \"seed_variance_cv_stable_rank_step50\": 0.045,\n      \"seed_variance_cv_training_loss_step50\": 0.028\n    },\n    \"tables\": [\n      {\n        \"name\": \"divergence_by_step_and_signal_1.5B\",\n        \"columns\": [\n          \"signal\",\n          \"step_50_div\",\n          \"step_100_div\",\n          \"step_200_div\",\n          \"step_500_div\",\n          \"auc\",\n          \"seed_cv\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            0.21,\n            0.34,\n            0.52,\n            0.71,\n            0.89,\n            0.045\n          ],\n          [\n            \"training_loss\",\n            0.15,\n            0.28,\n            0.41,\n            0.58,\n            0.83,\n            0.028\n          ],\n          [\n            \"spectral_entropy\",\n            0.02,\n            0.05,\n            0.09,\n            0.18,\n            0.62,\n            0.022\n          ],\n          [\n            \"perplexity\",\n            0.04,\n            0.08,\n            0.12,\n            0.19,\n            0.56,\n            0.035\n          ],\n          [\n            \"token_entropy\",\n            0.03,\n            0.06,\n            0.11,\n            0.15,\n            0.51,\n            0.041\n          ]\n        ]\n      },\n      {\n        \"name\": \"scale_comparison_within_gen_auc\",\n        \"columns\": [\n          \"signal\",\n          \"auc_0.5B\",\n          \"auc_1.5B\",\n          \"amplitude_ratio\",\n          \"scale_sensitivity\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            0.984,\n            0.89,\n            0.61,\n            \"high\"\n          ],\n          [\n            \"training_loss\",\n            0.923,\n            0.83,\n            0.72,\n            \"moderate\"\n          ],\n          [\n            \"perplexity\",\n            0.534,\n            0.56,\n            \"~1.0\",\n            \"none\"\n          ],\n          [\n            \"spectral_entropy\",\n            0.58,\n            0.62,\n            \"~1.0\",\n            \"none\"\n          ],\n          [\n            \"token_entropy\",\n            0.478,\n            0.51,\n            \"~1.0\",\n            \"none\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：within-gen early warning 在 1.5B 上成立但 amplitude 系统性衰减。 stable_rank 仍为最强 within-gen detector（AUC=0.89），但与 training_loss（0.83） 差距缩小。PPL within-gen 失效在 1.5B 上再次确认（AUC=0.56 ≈ random）。 论文措辞从 \\\"AUC=0.984\\\" 改为 \\\"AUC=0.89-0.98 across scales (amplitude decreases with model scale)\\\"。seed CV=0.045 意味着个别 seed 的 AUC 可能低至 0.82。 4-seed bootstrap 95% CI 估计：[0.82, 0.94]，下界仍有意义但远不如 0.5B 的 [0.978, 0.989]。 Limitation 段需要讨论：更大模型的参数冗余稀释了 adapter 的谱信号。\\n\\n\\n1.5B 模型参数冗余度高于 0.5B：QLoRA adapter 仅修改 ~2% 参数，同等 contamination 对权重矩阵谱结构的扰动被更大的 frozen 参数空间稀释。stable_rank 在 step 50 的 相对偏离从 0.5B 的 0.344 降至 ~0.21，仍可检测但幅度缩小约 40%。training_loss 作为训练集 CE 直接测量被污染分布的学习动态，受模型规模影响较小（优化器对 corrupted tokens 的梯度信号依然存在），因此 AUC 降幅温和（0.923→0.83）。 held-out PPL 在 0.5B 上已经 within-gen 无效（AUC=0.534），1.5B 上稍有上升至 0.56 但仍接近 random——原因是 QLoRA 早期微调对 held-out 分布影响极微弱，需多代累积。 spectral_entropy 在 0.5B 上也是 late detector（仅 100% 下显著），1.5B 上类似。 seed 间 CV 在 0.03-0.06 范围内，因为 3-4 seeds 的 stable_rank 对初始化和 synthetic data 随机性敏感（seed44 经验已证实）。总体结论：within-gen early warning 在 1.5B 上成立但需降级 amplitude claim。\\n\"\n  },\n  {\n    \"name\": \"Early Warning Threshold Calibration & Cross-Config ROC\",\n    \"description\": \"汇总 plan_001 (3-4 seeds) + plan_002 (3 seeds PubMed) 数据，计算 clustered bootstrap ROC，确定最小可靠检测阈值，验证 PPL within-gen 失效是否跨配置一致。\\n\",\n    \"results\": {\n      \"n_seeds_wikitext\": 4,\n      \"n_seeds_pubmed\": 3,\n      \"n_fractions_wikitext\": 5,\n      \"n_fractions_pubmed\": 5,\n      \"clustered_bootstrap_n_resamples\": 1000,\n      \"stable_rank_auc_wikitext_1.5B\": 0.89,\n      \"stable_rank_auc_wikitext_1.5B_ci_lower\": 0.81,\n      \"stable_rank_auc_wikitext_1.5B_ci_upper\": 0.94,\n      \"stable_rank_auc_pubmed_1.5B\": 0.86,\n      \"stable_rank_auc_pubmed_1.5B_ci_lower\": 0.77,\n      \"stable_rank_auc_pubmed_1.5B_ci_upper\": 0.93,\n      \"training_loss_auc_wikitext_1.5B\": 0.83,\n      \"training_loss_auc_pubmed_1.5B\": 0.8,\n      \"perplexity_auc_wikitext_1.5B\": 0.56,\n      \"perplexity_auc_pubmed_1.5B\": 0.52,\n      \"perplexity_auc_cross_config_range\": [\n        0.5,\n        0.58\n      ],\n      \"optimal_threshold_stable_rank_sensitivity\": 0.72,\n      \"optimal_threshold_stable_rank_specificity\": 0.95,\n      \"min_fraction_detectable_at_step100\": 0.25,\n      \"false_positive_rate_at_frac0\": 0.04\n    },\n    \"tables\": [\n      {\n        \"name\": \"cross_config_within_gen_auc_comparison\",\n        \"columns\": [\n          \"signal\",\n          \"wikitext_0.5B\",\n          \"wikitext_1.5B\",\n          \"pubmed_1.5B\",\n          \"cross_config_consistency\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            0.984,\n            \"0.89 [0.81,0.94]\",\n            \"0.86 [0.77,0.93]\",\n            \"consistent_but_attenuated\"\n          ],\n          [\n            \"training_loss\",\n            0.923,\n            \"0.83 [0.74,0.90]\",\n            \"0.80 [0.70,0.88]\",\n            \"consistent_but_attenuated\"\n          ],\n          [\n            \"perplexity\",\n            0.534,\n            \"0.56 [0.44,0.66]\",\n            \"0.52 [0.41,0.63]\",\n            \"consistent_near_random\"\n          ],\n          [\n            \"spectral_entropy\",\n            0.58,\n            \"0.62 [0.50,0.72]\",\n            \"0.59 [0.47,0.70]\",\n            \"consistent_weak\"\n          ],\n          [\n            \"token_entropy\",\n            0.478,\n            \"0.51 [0.40,0.62]\",\n            \"0.49 [0.38,0.60]\",\n            \"consistent_near_random\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"threshold_operating_points\",\n        \"columns\": [\n          \"signal\",\n          \"threshold_pct_deviation\",\n          \"sensitivity\",\n          \"specificity\",\n          \"ppv\",\n          \"frac_min_detectable\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            \"15%\",\n            0.72,\n            0.95,\n            0.88,\n            0.25\n          ],\n          [\n            \"training_loss\",\n            \"10%\",\n            0.68,\n            0.92,\n            0.82,\n            0.25\n          ],\n          [\n            \"combined_sr_tl\",\n            \"SR>10% OR TL>8%\",\n            0.85,\n            0.9,\n            0.81,\n            0.1\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3-4 seed clustered bootstrap 的 CI 太宽无法做 formal significance claim（CI lower bound 0.81 跨过了一些 \\\"clinically meaningful\\\" 阈值但未跨 0.5）。 Cross-config PPL within-gen 失效验证是强结果——两个 domain 两个 scale 一致 AUC~0.5，但只有 3 个 data points（0.5B-Wiki, 1.5B-Wiki, 1.5B-PubMed）， camera-ready 需 plan_012 Full FT 数据。Combined threshold (SR>10% OR TL>8%) 提升 sensitivity 到 0.85 且能检测 frac=0.10——这是 practitioner recommendation 的基础。Limitations：threshold 优化在 same data 上做有 overfitting risk， 理想需 held-out seed 验证。\\n\\n\\nClustered bootstrap 以 seed 为聚类单位（而非 pooling 所有 step×gen observations）， 有效样本量从数百降到 3-4，导致 CIs 显著变宽。stable_rank CI 宽度 ~0.13（对比 0.5B N=1 的 [0.978, 0.989] 宽度 0.011），这是 median 档 statistical power 不足的直接体现。PubMed AUC 略低于 WikiText（0.86 vs 0.89）因为 biomedical domain 的 baseline variance 更高（specialized tokens 的梯度更 noisy）。 PPL within-gen AUC 跨两个 domain 一致在 0.50-0.58 范围，这强化了 \\\"held-out PPL within-gen 失效\\\" 的 claim 但仅有 2 个 config 验证，无法升级到 camera-ready 措辞。 最优阈值 sensitivity=0.72 意味着 28% false negative——practitioners 不能仅靠 单一信号，需组合 stable_rank + training_loss。frac=0.25 在 step 100 可检出 说明 moderate contamination 的 early warning 仍然可能，但 frac=0.1 不行。\\n\"\n  },\n  {\n    \"name\": \"Per-Layer Collapse Propagation Analysis (1.5B)\",\n    \"description\": \"对 plan_001 已完成的 3-4 seeds 的 1.5B checkpoints 做 forward-pass SVD， 分析 28 层 × 各 sub-module 的谱变化模式。\\n\",\n    \"results\": {\n      \"n_layers_analyzed\": 28,\n      \"n_submodules_per_layer\": 7,\n      \"n_seeds_available\": 3,\n      \"v_proj_mean_sr_increase_100pct\": 4.2,\n      \"v_proj_sr_increase_range\": [\n        2.8,\n        5.6\n      ],\n      \"down_proj_collapse_layers\": [\n        22,\n        23,\n        24,\n        25\n      ],\n      \"down_proj_sr_decrease_max\": -4.8,\n      \"k_proj_mean_sr_increase\": 1.1,\n      \"q_proj_mean_sr_increase\": 1.4,\n      \"o_proj_mean_sr_change\": 0.3,\n      \"most_sensitive_submodule\": \"v_proj\",\n      \"most_sensitive_layer_range\": [\n        20,\n        27\n      ],\n      \"layer_onset_order\": \"late layers (L22-27) → mid layers (L12-18) → early layers (L0-5)\",\n      \"cross_seed_layer_pattern_consistency\": \"2/3 seeds agree on v_proj dominance; 1 seed shows k_proj co-dominant\",\n      \"baseline_0pct_max_sr_drift\": 0.45\n    },\n    \"tables\": [\n      {\n        \"name\": \"submodule_sensitivity_ranking_1.5B\",\n        \"columns\": [\n          \"submodule\",\n          \"mean_delta_sr_100pct\",\n          \"std_across_seeds\",\n          \"rank\",\n          \"consistent_with_0.5B\"\n        ],\n        \"rows\": [\n          [\n            \"v_proj\",\n            4.2,\n            1.1,\n            1,\n            true\n          ],\n          [\n            \"q_proj\",\n            1.4,\n            0.6,\n            2,\n            true\n          ],\n          [\n            \"k_proj\",\n            1.1,\n            0.8,\n            3,\n            true\n          ],\n          [\n            \"up_proj\",\n            0.8,\n            0.4,\n            4,\n            true\n          ],\n          [\n            \"gate_proj\",\n            0.5,\n            0.3,\n            5,\n            true\n          ],\n          [\n            \"o_proj\",\n            0.3,\n            0.2,\n            6,\n            true\n          ],\n          [\n            \"down_proj\",\n            -3.2,\n            1.5,\n            \"N/A (collapse)\",\n            true\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"1.5B per-layer 分析确认 sub-module-centric pattern 跨 scale 泛化。v_proj 仍是最敏感 indicator（practitioner takeaway 不变）。新发现：1.5B 的 layer onset 更清晰呈现 \\\"late→mid→early\\\" 的传播序列（0.5B 层数少区分度不够）。 但 N=3 seeds 的 cross-seed consistency 不足以做 formal claim——1 个 seed 的 k_proj 与 v_proj 接近等强度。论文中标注为 \\\"predominant pattern\\\" 而非 \\\"universal\\\"。down_proj collapse 位置从 0.5B 的 L11-12 移到 1.5B 的 L22-25 （相对位置一致 ~78-89% depth），支持 \\\"FFN bottleneck vulnerability\\\" 解释。\\n\\n\\n1.5B (28 layers) 比 0.5B (24 layers) 有更多层供 collapse 传播。0.5B 已显示 v_proj 在几乎所有层 diffuse（ΔSR +1~+3），1.5B 的更深架构预期显示类似 pattern 但幅度更大（更多参数 → 每层 adapter 修改的相对占比更小 → 需要更多层协同才能 表达 same level of corruption → late layers 先 collapse 因为离 loss 最近）。 down_proj collapse 出现在 L22-25（对应 0.5B 的 L11-12），因为 down_proj 是 FFN 的压缩瓶颈，synthetic data 的低 diversity 导致这些投影矩阵的 effective rank 降低。cross-seed consistency 在 median 档下不完美（3 seeds 中 1 个 因初始化差异可能显示稍不同的 sub-module ranking），但 v_proj 作为 most sensitive 的结论在 2/3 seeds 中一致。layer onset order \\\"late→mid→early\\\" 反映 梯度从 loss 向前传播的 collapse 扩散模式。\\n\"\n  },\n  {\n    \"name\": \"LLaMA-3.2-1B Cross-Family Validation\",\n    \"description\": \"LLaMA-3.2-1B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens。 验证 collapse monitoring signals 是否跨 model family 泛化。\\n\",\n    \"results\": {\n      \"model\": \"LLaMA-3.2-1B\",\n      \"n_fractions\": 3,\n      \"n_seeds\": 1,\n      \"n_generations\": 5,\n      \"signals_direction_consistent\": 7,\n      \"signals_total\": 11,\n      \"signals_inconsistent\": 2,\n      \"signals_insignificant\": 2,\n      \"consistent_signals\": [\n        \"stable_rank\",\n        \"spectral_entropy\",\n        \"perplexity\",\n        \"token_entropy\",\n        \"training_loss\",\n        \"self_bleu\",\n        \"gradient_norm\"\n      ],\n      \"inconsistent_signals\": [\n        \"distinct_1\",\n        \"hellaswag\"\n      ],\n      \"insignificant_signals\": [\n        \"distinct_2\",\n        \"distinct_3\"\n      ],\n      \"llama_gen4_100pct_ppl\": 580.0,\n      \"llama_gen4_100pct_stable_rank\": 142.5,\n      \"llama_gen4_100pct_spectral_entropy\": 0.871,\n      \"llama_gen4_100pct_token_entropy\": 0.91,\n      \"llama_gen4_50pct_ppl\": 14.8,\n      \"llama_gen4_0pct_ppl\": 13.1,\n      \"spearman_rho_core_4signals\": 1.0,\n      \"collapse_magnitude_ppl\": \"44x (vs Qwen 0.5B 53x, Qwen 1.5B ~35x)\",\n      \"collapse_magnitude_stable_rank\": \"5.8x (vs Qwen 0.5B 6.6x)\",\n      \"hellaswag_100pct_gen4\": 0.38,\n      \"hellaswag_50pct_gen4\": 0.41,\n      \"hellaswag_0pct_gen4\": 0.4,\n      \"self_recovery_50pct_present\": true,\n      \"recovery_ratio_ppl\": 0.48\n    },\n    \"tables\": [\n      {\n        \"name\": \"llama_vs_qwen_signal_direction\",\n        \"columns\": [\n          \"signal\",\n          \"qwen_0.5B_direction\",\n          \"qwen_1.5B_direction\",\n          \"llama_1B_direction\",\n          \"consistent\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            \"↑\",\n            \"↑\",\n            \"↑\",\n            \"✓\"\n          ],\n          [\n            \"spectral_entropy\",\n            \"↑\",\n            \"↑\",\n            \"↑\",\n            \"✓\"\n          ],\n          [\n            \"perplexity\",\n            \"↑\",\n            \"↑\",\n            \"↑\",\n            \"✓\"\n          ],\n          [\n            \"token_entropy\",\n            \"↓\",\n            \"↓\",\n            \"↓\",\n            \"✓\"\n          ],\n          [\n            \"training_loss\",\n            \"↑\",\n            \"↑\",\n            \"↑\",\n            \"✓\"\n          ],\n          [\n            \"gradient_norm\",\n            \"↓\",\n            \"↓\",\n            \"↓\",\n            \"✓\"\n          ],\n          [\n            \"self_bleu\",\n            \"↑\",\n            \"↑\",\n            \"↑\",\n            \"✓\"\n          ],\n          [\n            \"distinct_1\",\n            \"↓\",\n            \"↓\",\n            \"↑ (weak)\",\n            \"✗\"\n          ],\n          [\n            \"distinct_2\",\n            \"↓\",\n            \"↓\",\n            \"≈0\",\n            \"?\"\n          ],\n          [\n            \"distinct_3\",\n            \"↓\",\n            \"↓\",\n            \"≈0\",\n            \"?\"\n          ],\n          [\n            \"hellaswag\",\n            \"↓ (weak)\",\n            \"↓\",\n            \"↑ (0.01)\",\n            \"✗\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"llama_collapse_trajectory\",\n        \"columns\": [\n          \"fraction\",\n          \"gen0_ppl\",\n          \"gen1_ppl\",\n          \"gen2_ppl\",\n          \"gen3_ppl\",\n          \"gen4_ppl\",\n          \"gen4_sr\",\n          \"gen4_se\"\n        ],\n        \"rows\": [\n          [\n            \"0%\",\n            13.1,\n            13.0,\n            13.2,\n            13.1,\n            13.1,\n            25.6,\n            0.712\n          ],\n          [\n            \"50%\",\n            13.1,\n            14.2,\n            14.9,\n            15.1,\n            14.8,\n            27.1,\n            0.724\n          ],\n          [\n            \"100%\",\n            13.1,\n            118.5,\n            342.0,\n            498.0,\n            580.0,\n            142.5,\n            0.871\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7/11 signals direction-consistent 足以支撑 \\\"cross-family validated (preliminary)\\\" 但不足以 claim \\\"architecture-agnostic\\\"。论文 taxonomy table 的 LLaMA 列标注 \\\"N=1, 7/11 consistent\\\"。inconsistent signals（distinct_1, hellaswag）恰好是 在 Qwen QLoRA 上已被标注为 weak/method-dependent 的信号，因此不削弱核心 claims。 4 个 core signals（SR, SE, PPL, TE）全部一致，核心 Claim 1 的 cross-family evidence 较强。但 N=1 seed 无法排除 cherry-pick effect——Discussion 段标注 \\\"single seed, pending multi-seed confirmation\\\"。collapse magnitude（44x PPL） 在合理范围内，架构差异只影响 absolute scale 不影响 direction。Self-recovery 跨 family 观察到进一步支持 \\\"data mixing effect\\\" 解释（非 Qwen-specific）。 若推迟到 6/15 可补 1-2 seeds 显著加强此 claim。\\n\\n\\nLLaMA-3.2-1B（1.24B params, 16 layers, vocab=128k）与 Qwen2.5 系列架构差异： (1) RoPE 实现不同, (2) vocab size 128k vs 151k, (3) GQA vs MQA。核心 spectral/output signals 的方向（SR↑, SE↑, TE↓, PPL↑）由 collapse 的基本物理决定（重复训练 → 权重矩阵 rank 膨胀 + 输出分布收缩），这些与架构细节无关，因此 7/11 方向一致。\\ndistinct_1 不一致：LLaMA 128k vocab 的 token granularity 更细（subword 切分更碎）， collapsed model 的词汇多样性表现不同——Qwen 上 distinct_1 下降 3% 而 LLaMA 上 可能因 subword 效应反而轻微上升。hellaswag 在 LLaMA 上不一致原因：QLoRA 正则化 + LLaMA 的 downstream task 对 collapse 的 sensitivity 不同（0.5B Qwen 已经 显示 QLoRA 下 hellaswag 基本不动，LLaMA 可能出现轻微反向——gen4 collapsed model 偶然在某些 hellaswag 模式上表现稍好）。distinct_2/3 不显著因 N=1 variance 大。\\nPPL collapse 幅度 44x 略低于 Qwen 0.5B 的 53x，因为 LLaMA 128k vocab 的 token-level entropy baseline 不同（更大 vocab → 更分散的 softmax → 不同的 PPL dynamics）。但方向一致且幅度在同一量级。self-recovery 在 50% 处仍观察到 （RR=0.48）因为这是 data mixing 的通用效应，非 architecture-specific。\\n\"\n  },\n  {\n    \"name\": \"Full FT Multi-Seed Extension\",\n    \"description\": \"0.5B × WikiText-2 × 3 fractions (0/50/100%) × 2 additional seeds × 5 gens， 将 Full FT 对比从 N=1 扩展到 N=3。\\n\",\n    \"results\": {\n      \"status\": \"NOT_STARTED\",\n      \"reason\": \"GPU budget exhausted by plan_001/002/010/011; no remaining capacity before ARR 5/25\",\n      \"implication_for_paper\": \"Claim 3 method-dependence 仍基于 N=1 Full FT seed。Limitations 必须标注： \\\"Full FT comparison based on single seed; direction consistency observed but variance uncharacterized. Multi-seed replication planned for camera-ready.\\\"\\n\",\n      \"risk_assessment\": \"Reviewer 要求 Full FT replication 的概率 ~40%。如果 6/15 cycle 提交， 可在 rebuttal 前完成 2 extra seeds。5/25 提交则只能在 response 中 promise。\\n\",\n      \"mitigation\": \"plan_003 的 signal direction consistency 6/6 + plan_010 3B spot-check direction match 提供间接 evidence（不同 scale 方向一致暗示 robustness）， 但不替代 same-config multi-seed。\\n\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Plan_012 未启动是 median 档 \\\"scope 升级后 resource 不足\\\" 的典型表现。 5/25 提交版本中 Claim 3 的 method-dependence evidence 仍为 N=1，这是 最可能被 reviewer flag 的单点。缓解策略：(1) 在 Limitations 中 proactively 标注, (2) 强调 direction consistency 6/6 的 qualitative strength, (3) 承诺 camera-ready 补充 2 extra seeds。若选择 6/15 cycle，有 3 周 GPU 时间可完成此实验。\\n\\n\\nMedian 档核心假设之一是 \\\"Full FT multi-seed (plan012) 未启动，N=1 限制仍在\\\"。 原因：plan_001 的 30 runs 在 2 GPU 上消耗 ~150h（已 10/30 completed）， plan_002 在 3 GPU 上消耗 ~45h（仍在运行），plan_010 3B spot-check 占 1 GPU ~8h。在 5/25 deadline 前无 GPU slot 给 plan_012 的额外 30 runs（~40h on 0.5B Full FT, A6000 ~1.3h/run）。这不是技术困难而是纯粹的 resource scheduling constraint。\\n\"\n  },\n  {\n    \"name\": \"MMLU-Mini Downstream Evaluation\",\n    \"description\": \"对 plan_001 已完成 checkpoints 运行 MMLU-mini（~100 questions × 4 subjects）， 作为第二个 downstream benchmark 补充 HellaSwag。\\n\",\n    \"results\": {\n      \"n_checkpoints_evaluated\": 60,\n      \"n_seeds_available\": 3,\n      \"mmlu_baseline_0pct_gen0\": 0.36,\n      \"mmlu_0pct_gen4\": 0.35,\n      \"mmlu_50pct_gen4\": 0.34,\n      \"mmlu_100pct_gen4\": 0.29,\n      \"mmlu_cross_frac_rho\": -0.87,\n      \"mmlu_cross_gen_rho_100pct\": -0.8,\n      \"mmlu_sensitivity_vs_hellaswag\": \"slightly higher (Δ=-0.07 at 100% vs HellaSwag Δ=-0.03 QLoRA)\",\n      \"mmlu_method_dependence\": \"QLoRA: weak degradation (-7pt); consistent with HellaSwag pattern\",\n      \"seed_variance_mmlu_100pct\": 0.025,\n      \"mmlu_within_gen_auc\": 0.55,\n      \"mmlu_per_subject_variance\": \"STEM -9pt, Humanities -5pt, Social -6pt, Other -4pt\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"mmlu_mini_by_fraction_and_generation\",\n        \"columns\": [\n          \"fraction\",\n          \"gen0\",\n          \"gen1\",\n          \"gen2\",\n          \"gen3\",\n          \"gen4\",\n          \"delta_gen04\"\n        ],\n        \"rows\": [\n          [\n            \"0%\",\n            0.36,\n            0.36,\n            0.35,\n            0.35,\n            0.35,\n            -0.01\n          ],\n          [\n            \"50%\",\n            0.36,\n            0.35,\n            0.35,\n            0.34,\n            0.34,\n            -0.02\n          ],\n          [\n            \"100%\",\n            0.36,\n            0.33,\n            0.31,\n            0.3,\n            0.29,\n            -0.07\n          ]\n        ]\n      },\n      {\n        \"name\": \"mmlu_vs_hellaswag_comparison\",\n        \"columns\": [\n          \"metric\",\n          \"hellaswag_delta_100pct\",\n          \"mmlu_delta_100pct\",\n          \"within_gen_auc\",\n          \"cross_frac_rho\"\n        ],\n        \"rows\": [\n          [\n            \"QLoRA_0.5B\",\n            -0.002,\n            -0.07,\n            \"0.51 / 0.55\",\n            \"-0.72 / -0.87\"\n          ],\n          [\n            \"QLoRA_1.5B\",\n            \"pending\",\n            -0.07,\n            \"pending / 0.55\",\n            \"pending / -0.87\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MMLU-mini 提供了比 HellaSwag 更敏感的 downstream collapse indicator（under QLoRA）， 部分解决 \\\"HellaSwag 在 QLoRA 下不动\\\" 的问题。但 within-gen AUC 仍近 random， 确认 downstream metrics 不适合 early warning。论文可新增一句： \\\"Knowledge benchmarks (MMLU) show moderate sensitivity to collapse (-7pt at frac=100%) while commonsense reasoning (HellaSwag) remains stable under QLoRA, suggesting collapse selectively erodes factual knowledge before reasoning ability.\\\" 这强化 Claim 3 taxonomy 的 granularity。Limitations：MMLU-mini 只 100 题， per-subject N=25 的 variance 大；full MMLU 验证留作 camera-ready。\\n\\n\\nMMLU-mini 测量知识保留而非语言建模能力。在 QLoRA collapse 下，模型的 token 分布坍缩但参数空间大部分 frozen，因此知识保留受损程度有限。100% contamination gen4 的 -7pt 下降（0.36→0.29）比 HellaSwag 的 -0.3pt（QLoRA 下几乎不动） 更大，因为 MMLU 需要 factual recall 而 HellaSwag 是 commonsense reasoning—— collapse 优先损害 fact-level 记忆（被 synthetic noise 覆盖）而非推理能力 （由 frozen 参数维持）。但总体幅度仍然 modest（-7pt on random=25% baseline）， 这与 writing note 10 的 \\\"QLoRA 正则化保护 downstream\\\" 结论一致。\\nMMLU within-gen AUC=0.55 接近 random，原因同 HellaSwag/PPL：downstream 评估 需要多代累积才能看到效果，within-gen 的参数变化太小。cross-frac ρ=-0.87 （非完美 -1.0 因为 50% 和 0% 差异很小，只有 100% 有显著 drop）。 STEM 受损最大因为 factual precision 要求最高。seed variance 0.025 意味着 3 seeds 的 MMLU scores 相当一致（downstream eval 的 variance 主要来自 question sampling 而非 model 随机性）。\\n\"\n  },\n  {\n    \"name\": \"Within-Gen AUROC Formal Statistics (1.5B, 3-4 Seeds)\",\n    \"description\": \"使用 plan_001 的 3-4 seed 数据重算 within-generation binary AUROC， 从 N=1 (0.5B) 升级到 N=3-4 (1.5B) 的 clustered bootstrap 正式统计。\\n\",\n    \"results\": {\n      \"n_seeds_used\": 4,\n      \"bootstrap_method\": \"clustered by seed, 2000 resamples\",\n      \"stable_rank_auc_mean\": 0.88,\n      \"stable_rank_auc_ci_95\": [\n        0.8,\n        0.94\n      ],\n      \"stable_rank_auc_ci_width\": 0.14,\n      \"training_loss_auc_mean\": 0.82,\n      \"training_loss_auc_ci_95\": [\n        0.73,\n        0.89\n      ],\n      \"perplexity_auc_mean\": 0.55,\n      \"perplexity_auc_ci_95\": [\n        0.43,\n        0.65\n      ],\n      \"spectral_entropy_auc_mean\": 0.61,\n      \"spectral_entropy_auc_ci_95\": [\n        0.48,\n        0.72\n      ],\n      \"token_entropy_auc_mean\": 0.5,\n      \"token_entropy_auc_ci_95\": [\n        0.39,\n        0.61\n      ],\n      \"formal_significance_stable_rank\": \"CI lower bound 0.80 > 0.5, significant\",\n      \"formal_significance_training_loss\": \"CI lower bound 0.73 > 0.5, significant\",\n      \"formal_significance_perplexity\": \"CI crosses 0.5, NOT significant for within-gen\",\n      \"comparison_to_0.5B_N1\": \"0.5B AUC=0.984 falls outside 1.5B 95% CI upper bound (0.94), confirming scale attenuation\",\n      \"practical_implication\": \"stable_rank remains actionable at 1.5B but recommend combined threshold with training_loss\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"formal_within_gen_auroc_1.5B\",\n        \"columns\": [\n          \"signal\",\n          \"auc_mean\",\n          \"ci_lower\",\n          \"ci_upper\",\n          \"significant_vs_random\",\n          \"rank\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            0.88,\n            0.8,\n            0.94,\n            true,\n            1\n          ],\n          [\n            \"training_loss\",\n            0.82,\n            0.73,\n            0.89,\n            true,\n            2\n          ],\n          [\n            \"spectral_entropy\",\n            0.61,\n            0.48,\n            0.72,\n            false,\n            3\n          ],\n          [\n            \"perplexity\",\n            0.55,\n            0.43,\n            0.65,\n            false,\n            4\n          ],\n          [\n            \"token_entropy\",\n            0.5,\n            0.39,\n            0.61,\n            false,\n            5\n          ]\n        ]\n      },\n      {\n        \"name\": \"scale_attenuation_summary\",\n        \"columns\": [\n          \"signal\",\n          \"auc_0.5B_N1\",\n          \"auc_1.5B_N4\",\n          \"attenuation_pct\",\n          \"ci_overlap\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            0.984,\n            0.88,\n            \"-10.6%\",\n            \"0.5B point outside 1.5B CI\"\n          ],\n          [\n            \"training_loss\",\n            0.923,\n            0.82,\n            \"-11.2%\",\n            \"0.5B point outside 1.5B CI\"\n          ],\n          [\n            \"perplexity\",\n            0.534,\n            0.55,\n            \"+3.0%\",\n            \"overlapping\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Plan_014 是将 Claim 2 从 \\\"anecdotal\\\" 升级到 \\\"formally supported\\\" 的关键。 4-seed clustered bootstrap 证明 stable_rank within-gen detection 在 1.5B 上 statistically significant（CI lower > 0.5）但不 excellent（CI upper < 0.95 in some resamples）。论文措辞从 \\\"AUC=0.984\\\" 改为 \\\"AUC=0.88 [0.80, 0.94] at 1.5B scale\\\"。Scale attenuation 本身成为一个 finding：\\\"sensitivity amplitude decreases with model scale, consistent with larger parameter spaces absorbing adapter perturbations\\\"。PPL within-gen 失效获得 formal backing：CI 跨 0.5 意味着无法 reject random detection。Combined recommendation（SR + TL）成为 唯一 robust practitioner guidance。如果 5/25 提交，这是 Claim 2 的 definitive statement——弱于原始但仍有价值。6/15 cycle 可补 seed46 收窄 CI。\\n\\n从 N=1 到 N=4 的 clustered bootstrap 是 median 档的核心 statistical upgrade。 seed 作为聚类单位意味着 effective N=4（不是 4 seeds × 5 fracs × 5 gens = 100 的 naive pooling）。Bootstrap CI 宽度 ~0.14 对应 4 个独立聚类的标准误 ~0.035（SE ≈ σ/√N, σ~0.07, N=4 → SE=0.035, 95% CI ≈ ±1.96×0.035 = ±0.07, total width 0.14）。这比 0.5B N=1 的 parametric CI [0.978, 0.989]（width 0.011） 宽 13 倍——不是因为 1.5B 更 noisy，而是因为 clustered bootstrap correctly accounts for seed-level dependence。\\nstable_rank AUC=0.88 低于 0.5B 的 0.984 因为 scale attenuation（写作笔记已预期）。 CI lower bound 0.80 仍高于 random (0.5)，可以 claim \\\"significant within-gen detection\\\"。但不能 claim \\\"excellent detection\\\" (conventionally AUC>0.9)。 perplexity CI [0.43, 0.65] 跨越 0.5——formally 不能 reject null hypothesis of random detection。这paradoxically 让 \\\"PPL within-gen 失效\\\" 成为 statistically validated result（不能 reject H0: AUC=0.5）。\\n5-seed 无法实现因 seed46 未 start + seed45 部分完成（median 档假设）， 故降为 4-seed bootstrap。如果 seed45 的 frac=0.5/1.0 数据缺失，可能 进一步降为 3-seed（CI width ~0.18），此时 stable_rank CI lower bound 可能落到 0.76，仍 significant 但 barely。\\n\"\n  }\n]",
      "numLines": 770,
      "startLine": 1,
      "totalLines": 770
    }
  },
  "sourceToolAssistantUUID": "08ed3c0e-2306-4597-b6fc-9533c650f0ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T10:19:55.520Z_

<details><summary>↩ Tool result · `toolu_01KAsuoFrHfJFRZPKvsLGPzb`</summary>

```text
1	# Paper Framing — collapse_severity_monitor
2	
3	## Target Venue
4	- Primary: EMNLP 2026 via ACL Rolling Review (ARR)
5	- Deadline: ARR submission 2026-05-25
6	- Backup: ARR June cycle (2026-06-15) if 5/25 not feasible
7	
8	## Core Claims (3 条)
9	
10	1. **Signal-Severity Correlation**: Spectral signals (stable rank, spectral entropy) and output signals (token entropy, perplexity) reliably track model collapse severity across synthetic data contamination levels, maintaining monotonic ordering across tested fractions and generations. (MVP: ρ=1.0 with n=3; to be validated with n=6 fractions × 5 seeds in plan_001. Primary evidence: Spearman ρ with bootstrap CIs; effect sizes elevated as primary evidence, ρ as supporting.)
11	
12	2. **Early Warning Capability**: Collapse can be detected at moderate contamination (50%) within a single training run: stable rank achieves AUC=0.984 [0.978, 0.989] for within-gen collapse detection, reaching AUC=0.94 (sens=0.78, spec=1.00) at just 10% training progress. Training loss is the second-best within-gen detector (AUC=0.923). ROC analysis must use clustered bootstrap (one observation per fraction×seed) to avoid inflating AUC from serial generation dependence. **Featured sub-result: held-out evaluation perplexity — the metric practitioners most commonly check at eval checkpoints — provides no within-generation early warning (AUC=0.534 ≈ random).** This is because held-out PPL requires multi-generation accumulation before collapse manifests; in contrast, train-set loss (AUC=0.923) detects earlier because it directly measures learning dynamics on the contaminated distribution. Claim 2 Results 段落结构：(a) stable_rank early detection 正面证据, (b) 专门 1 段讨论 PPL within-gen 失效 + 原理解释 + AUC 对比, (c) ROC curves 图。Abstract 加半句："notably, held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.53)"。(Note: stable_rank is seed-sensitive but early-detecting; spectral_entropy is seed-robust but late-detecting (only at 100%). Practitioner recommendation: use stable_rank for within-gen early warning, perplexity for cross-gen severity comparison, spectral_entropy for severity discrimination. Cross-validation needed: plan001 5-seed + plan002 PubMed within-gen ROC, 如果多配置 PPL AUC 一致 ~0.5，camera-ready 可升级措辞。See writing notes 17, 18, 19.)
13	
14	3. **Non-Uniform Signal Behavior**: The same monitoring signal can be informative under one training method and misleading under another. Spectral signals saturate at extreme severity; gradient norm is non-monotonic under QLoRA but monotonic under Full FT; downstream metrics (HellaSwag) track collapse under Full FT but remain stable under QLoRA. Both methods show large gen1 PPL jumps (Full FT 15.3x, QLoRA 8.7x) but diverge in subsequent evolution: Full FT saturates (gen1→4: 1.11x), QLoRA decelerates but continues (gen1→4: 6.13x). Featured sub-result: PPL-downstream dissociation — QLoRA PPL=839 but hellaswag=0.430 vs Full FT PPL=326 but hellaswag=0.372, meaning PPL-based monitoring overestimates damage under QLoRA and practitioners must consider training method when selecting collapse signals. Terminal spectral convergence (SR ~154-156) noted as observation, not claimed as finding (N=1). Signal taxonomy table should include "method-dependence" column.
15	
16	## Story Spine
17	
18	- **Problem**: Model collapse from iterative training on synthetic data is a growing concern as LLM-generated text pervades training corpora. While the phenomenon is well-characterized theoretically (Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024), practitioners lack actionable tools to detect and quantify collapse severity during training. Current work focuses on post-hoc analysis or output-level detection, missing the rich signal available in training dynamics.
19	
20	- **Existing approaches & gaps**: SIGMA (2025) monitors output embedding spectral properties but requires access to a clean reference distribution (plan_009 adds head-to-head to clarify operational vs fundamental advantage). Kalinowski (2024) uses topological analysis but is computationally expensive. Data mixing strategies (Gerstgrasser et al. 2024, Kazdan et al. 2024) study prevention rather than detection. Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they examine within-generation temporal dynamics for early warning.
21	
22	- **Our framing**: We conduct a systematic empirical analysis of training dynamic signals as collapse severity monitors. Across 4 signal families (spectral, output, gradient, downstream) × 6 contamination levels × 2 model scales × 2 domains × 2 fine-tuning methods, we characterize which signals track collapse, when they diverge, and where they fail. Key insight: stable rank provides the earliest within-gen warning (AUC=0.94 at 10% training progress) while perplexity provides the most reliable cross-generation severity tracking — but these roles are non-interchangeable. We document a partial self-recovery phenomenon at moderate contamination consistent with known data mixing effects (Gerstgrasser et al. 2024), and characterize where standard monitoring signals mislead practitioners.
23	
24	- **Headline result template**: "Stable rank detects within-generation collapse with AUC=0.984, reaching actionable sensitivity (AUC=0.94) at 10% training progress. Across generations, spectral entropy provides the most robust severity discrimination (CV=0.0015) but is a late detector (only at 100% contamination). Held-out evaluation perplexity — often the go-to metric at eval checkpoints — is nearly ineffective for within-generation detection (AUC=0.534), while train-set loss detects data distribution shift (AUC=0.923) but not model quality degradation; evaluation perplexity remains the strongest cross-generation severity tracker. Different signals have complementary operating ranges; no single signal suffices across all detection contexts." (Note: ρ ≥ 0.94 是 plan001 验证目标，非当前实际数值，到手前用 effect size 表述。分层信号策略替代单一 headline signal。ROC 数据来自 plan005 within-gen 分析，N=1 seed。)
25	
26	## Anticipated Reviewer Concerns & Mitigation
27	
28	| Concern | Severity | Mitigation |
29	|---------|----------|------------|
30	| Statistical power (seeds) | CRITICAL | 5 seeds WikiText, 3 seeds PubMed; bootstrap CIs for all claims |
31	| n=3 fractions → trivial ρ=1.0 | HIGH | 6 fractions (0/10/25/50/75/100%) |
32	| Single model scale | HIGH | 0.5B + 1.5B (+ 3B spot-check if GPU permits) |
33	| Single dataset | HIGH | WikiText-2 + PubMed (3 seeds each) |
34	| QLoRA only | MEDIUM | Full FT comparison on 1 config (plan_003) |
35	| ROC pools non-independent observations | HIGH | Clustered bootstrap or one-gen-per-run restriction (plan_005) |
36	| Stable rank direction under collapse | MEDIUM | Clarify: ‖W‖_F² grows faster than σ₁² → SR increases = energy dispersal, not concentration. Fix text |
37	| No theoretical grounding | MEDIUM | Informal argument: 75% phase transition ↔ distributional shift theory; when spectral monitoring fails (capacity redundancy) |
38	| "First" claims overclaimed | MEDIUM | Qualify: "first systematic multi-axis comparison in iterative fine-tuning setting." Self-recovery → cite Gerstgrasser et al. |
39	| SIGMA differentiation thin | MEDIUM | Head-to-head (plan_009): run SIGMA at training checkpoints |
40	| Related work too thin | HIGH | ≥20 refs: Briesch 2023, Hataya 2023, Gerstgrasser 2024, Seddik 2024, Dohmatob "Tale of Tails" 2024, Pennington & Worah 2017 |
41	| Missing synthetic data gen params | LOW | Document temperature, top-p/k, max length, prompt format in Methods |
42	| No code/data release | MEDIUM | Release monitoring toolkit + signal trajectories + generation scripts |
43	| "Not a monitoring system" | LOW | Frame as analysis paper; taxonomy + early warning = practical value |
44	| No intervention/mitigation | LOW | Explicit non-goal; future work |
45	
46	## Core Insight (一句话)
47	
48	Training dynamic signals provide a free, model-agnostic early warning system for model collapse — but different signal families have distinct operating ranges, and practitioners need to know which signal to trust at which severity level.
49	
50	## Novelty Statement
51	
52	We provide the first systematic multi-axis comparison of training-time signal families as collapse severity monitors, spanning contamination levels, model scales, text domains, and fine-tuning methods. The within-generation early warning capability (stable rank AUC=0.94 at 10% training progress), the signal operating-range taxonomy, and the documentation of where standard monitoring signals actively mislead practitioners are the primary empirical contributions. The self-recovery observation at moderate contamination is consistent with known data mixing effects and is positioned as a finding rather than a novel phenomenon.
53	
54	## Key Writing Notes (from Dream review, 2026-05-14)
55	
56	1. **Effect sizes > ρ**: Elevate effect size tables as primary evidence; ρ as supporting.
57	2. **Stable rank direction**: SR increases under collapse = energy dispersal (Frobenius norm grows faster than spectral norm), not concentration. Fix text.
58	3. **25% contamination**: "mild degradation / near-stability", NOT "strong recovery" (PPL monotonically increases).
59	4. **Figures required**: Severity curves, ROC curves, heatmaps, per-layer propagation. Analysis paper without figures is a major gap.
60	5. **Reproducibility**: Code release, signal trajectories, generation scripts for D&B track.
61	6. **Collapse protocol**: Explicitly state whether fine-tuning from M₀ or M_{g-1} and discuss implications.
62	7. **Per-layer 叙事修正 (D011, 2026-05-15)**: 废弃"三区结构"（boundary/middle-neutral/late-bifurcation），改为 sub-module-centric 分析。真实数据显示 v_proj 在几乎所有层 diffuse（ΔSR +1~+3），down_proj 在 L11-L12 局部 collapse，其余子模块温和。Practitioner takeaway: 优先监控 v_proj stable rank 作为最敏感的 within-run collapse indicator。（注：cross-seed 稳定性另论，参见写作笔记 16。within-run 灵敏度与 cross-seed 排名是不同维度。）
63	8. **SIGMA 方向 provisional (C001/D014, 2026-05-15)**: expected_direction=+1（effective_rank 在 collapse 时上升）是 N=2 观测，非已验证结论。禁止在论文中当发现写。验证条件：plan_001 seed43-46 全量数据 + plan_003 Full FT SIGMA 数据。如果 Full FT 方向一致(+1)可排除 QLoRA confound；如果不一致需重写分析。"Within-gen corruption vs recursive collapse 方向差异"作为 discussion 论点需要等验证后才能使用。
64	9. **Non-monotonic claim scope (plan008/plan003, 2026-05-15)**: "Non-monotonic" 仅适用于 frac=50% 的 plateau 行为（ppl 26.9→25.6→25.7→25.6，真正收敛）。frac=100% gen1→gen2 的 -1.9% 下降（294→288）是噪声级波动，N=1 无法区分，禁止称为 "non-monotonic pattern"。100% 的正确描述："catastrophic jump at gen1 followed by continued degradation"。
65	10. **HellaSwag method-dependence + 归因修正 (plan003, 2026-05-15; 合并原 Note 10+13)**: HellaSwag 追踪 collapse 能力取决于训练方法（Full FT: 有效, -12.5%；QLoRA: 无效/稳定）。D015/D017 的"0.5B 失效"诊断错误——失效的是 QLoRA 的隐式正则化，非模型规模。论文归因必须是 method 而非 scale。反直觉：QLoRA gen4 PPL (839) > Full FT gen4 PPL (326)，但 QLoRA hellaswag (0.430) > Full FT hellaswag (0.372)——PPL 不是下游质量的唯一预测器。
66	11. **Collapse trajectory: 两种方法都 gen1 大跳，差异在后续 (plan003, 2026-05-15; D026 修正 D024)**: Full FT gen1=15.3x 后饱和（gen1→4: 1.11x）；QLoRA gen1=8.7x 后减速增长（gen1→4: 6.13x，gen4 PPL=839）。**禁止**使用 "slow onset" / "snowball" / "exponential" 描述 QLoRA——QLoRA gen1 也是大跳（8.7x），不是缓慢起步。正确叙事：两种方法初始冲击程度不同（Full FT 更剧烈），后续演化模式不同（饱和 vs 减速增长）。终态谱收敛（SR ~154 vs ~156）需用正确数据重新验证后方可使用。
67	12. **Diversity 指标对 collapse 不敏感 (plan003, 2026-05-15)**: distinct_1 在 Full FT frac=100% 仅 -3%（0.0925→0.0897），self_bleu 几乎不变，即使 PPL 暴涨 17x。原因：collapsed model 输出分布坍缩到少数 token（token_entropy -55%），但采样随机性维持了 lexical diversity 的表面指标。论文中需明确将 diversity 族排除在有效 collapse indicator 之外，或专门讨论 entropy vs diversity 解耦现象。
68	13. *[已合并到 Note 10]*
69	14. **Claim 3 措辞升级方向 (Reviewer 评估, 2026-05-15)**: 从 "different signals respond differently" 升级为 "the same signal can be informative under one training method and misleading under another"——直击 practitioner pain point。PPL-downstream dissociation 作为 Claim 3 featured sub-result（1 段专门讨论），不独立成 claim（N=1 seed, 1 downstream task, 无法排除 HellaSwag ceiling/floor effect）。Signal taxonomy table 加 "method-dependence" 列。Abstract 用一句："perplexity and downstream metrics can diverge under parameter-efficient FT, cautioning against single-signal monitoring"。Terminal spectral convergence 降级为 observation（N=1 无法区分"收敛"和"碰巧接近"）。Limitations 必须标注 Full FT 对比的 N=1 限制。
70	15. **Self-recovery prevalence 对比禁令 (Reviewer, 2026-05-16)**: 3-seed 的 9/9=100% vs plan008 的 16/18=89% 不可比——前者仅用 3 个信号（PPL, stable_rank, spectral_entropy），后者用 6 个信号。选取的恰好是最一致的信号。论文中讨论 self-recovery 时必须标注信号覆盖范围，禁止跨不同信号集做 prevalence 对比。
71	16. **Signal ranking instability: stable_rank seed-sensitive (plan006/008 3-seed update, 2026-05-16)**: 3-seed 数据显示 stable_rank 的 Cohen's d 从 61.7 暴跌到 9.43（rank 1→4），原因是 seed44 引入 frac=50% 方差（CV=0.022）。spectral_entropy 最稳定（CV=0.0015，d=33.48，rank 2→1）。**禁止**在论文中将 stable_rank 定位为"最敏感信号"——正确叙事见写作笔记 17 分层策略。最终 taxonomy ranking 需等 plan001 5-seed 数据确认。
72	17. **分层信号策略（Signal Heatmap 发现, 2026-05-16; 修正 D029）**: spectral_entropy 虽 cross-seed 最稳定（d=33.48, CV=0.0015），但是 **late detector**——仅在 frac=100% 下显著（Δ+25.7%），frac=50% 下 effect size < 5%。stable_rank 和 perplexity 是 **early detectors**（50% 即可检出：SR +564.8%, PPL +5255%）。**禁止**推单一 headline signal。正确叙事："signals have complementary operating ranges"——stable_rank + perplexity 用于 early warning（Claim 2），spectral_entropy 用于 severity discrimination（区分 50% vs 100%）。这个分层发现本身就是 Claim 3 taxonomy 的核心价值：no single signal suffices。6/7 信号方向跨 QLoRA/Full FT 一致，强化 Claim 1 泛化性。
73	18. **Within-gen ROC 证据精确化 Claim 2（plan005 ROC 分析, 2026-05-16; 修正写作笔记 17 的 perplexity 角色）**: ROC 分析揭示信号在 within-gen vs cross-gen 两个维度的能力完全不同。stable_rank 是 within-gen 最强检测器（AUC=0.984, 10% progress 即达 AUC=0.94）；training_loss 次之（AUC=0.923）；**perplexity within-gen 几乎无效（AUC=0.534）**——但 cross-gen 仍是最强 severity tracker。spectral_entropy within-gen 非单调（20% progress 时 AUC 降到 0.30，方向翻转），**不适合 threshold-based 早期检测**。这修正了写作笔记 17 将 perplexity 归入 "early detectors" 的表述——perplexity 是 cross-gen early detector（50% contamination 可检出），但 within-gen early detector 只有 stable_rank 和 training_loss。论文叙事三维分层：(1) within-gen early alarm → stable_rank; (2) cross-gen severity tracking → perplexity; (3) cross-seed robust severity discrimination → spectral_entropy。Perplexity within-gen 失效是个有力的 practitioner 论点："the most commonly used collapse indicator fails at the earliest detection window"。**ROC 数据为 N=1 seed, 0.5B only，plan001 5-seed 后需验证。**
74	19. **信号定义精确化：三个 loss/PPL 信号的数据源（D035, 2026-05-15; 修正原 Note 19 错误归因）**: 代码中存在三个容易混淆的信号，必须在 Method 中精确定义：
75	    - **training_loss** = Trainer running avg CE on **训练集**（含 synthetic 混合数据），每 50 step 记录（`train.py:109-110`）。Within-gen AUC=0.923（有效）。原因：直接测量模型对被污染训练分布的学习动态。
76	    - **perplexity** = exp(mean NLL) on **固定 held-out 验证集**，model.eval() 模式，每 50 step 记录（`signals.py:92-108`）。Within-gen AUC=0.534（无效）。原因：QLoRA 早期微调对 held-out 分布影响微弱，collapse 效应需多代累积。Cross-gen d=20.82（有效）。
77	    - **token_entropy** = output token 分布的 Shannon entropy，within-gen AUC=0.478（无效）。
78	    **原 Note 19 的错误**：将 AUC=0.534 的信号标注为"training perplexity"（训练数据上的 PPL），实际该信号是 held-out eval PPL。training_loss（训练数据上的 CE）反而 AUC=0.923。
79	    **论文叙事修正**：Claim 2 featured sub-result 从"training perplexity fails"修正为"**held-out evaluation perplexity** fails at within-gen detection (AUC=0.534), while train-set loss detects effectively (AUC=0.923)"。Practitioners 通常在 eval checkpoints 看 held-out PPL，这个指标恰恰是 within-gen 最弱的。训练 loss 是间接的分布变化探测器，但 stable_rank (AUC=0.984) 仍最强因为它检测权重结构变化。
80	    **Abstract/Intro 措辞**：从 "training perplexity provides no within-gen early warning" 改为 "held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.534)"。
81	    Method 必须加入 training_loss 作为正式信号（Output 家族），明确标注数据源。Fig 3 展示 training_loss 合理（within-gen 第二强），需与 Method 信号列表一致。Camera-ready 升级条件：plan001 + plan002 cross-validation ROC 中 held-out PPL within-gen AUC 跨配置一致 ~0.5。
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f815293-8fb0-48bd-b5f4-ef4f14def78d",
  "isSidechain": false,
  "promptId": "55f86a0c-47b7-4429-a4ed-a402f351ff70",
  "type": "user",
  "uuid": "2ca57935-3672-4adf-99ac-8810e845c770",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper_framing.md",
      "content": "# Paper Framing — collapse_severity_monitor\n\n## Target Venue\n- Primary: EMNLP 2026 via ACL Rolling Review (ARR)\n- Deadline: ARR submission 2026-05-25\n- Backup: ARR June cycle (2026-06-15) if 5/25 not feasible\n\n## Core Claims (3 条)\n\n1. **Signal-Severity Correlation**: Spectral signals (stable rank, spectral entropy) and output signals (token entropy, perplexity) reliably track model collapse severity across synthetic data contamination levels, maintaining monotonic ordering across tested fractions and generations. (MVP: ρ=1.0 with n=3; to be validated with n=6 fractions × 5 seeds in plan_001. Primary evidence: Spearman ρ with bootstrap CIs; effect sizes elevated as primary evidence, ρ as supporting.)\n\n2. **Early Warning Capability**: Collapse can be detected at moderate contamination (50%) within a single training run: stable rank achieves AUC=0.984 [0.978, 0.989] for within-gen collapse detection, reaching AUC=0.94 (sens=0.78, spec=1.00) at just 10% training progress. Training loss is the second-best within-gen detector (AUC=0.923). ROC analysis must use clustered bootstrap (one observation per fraction×seed) to avoid inflating AUC from serial generation dependence. **Featured sub-result: held-out evaluation perplexity — the metric practitioners most commonly check at eval checkpoints — provides no within-generation early warning (AUC=0.534 ≈ random).** This is because held-out PPL requires multi-generation accumulation before collapse manifests; in contrast, train-set loss (AUC=0.923) detects earlier because it directly measures learning dynamics on the contaminated distribution. Claim 2 Results 段落结构：(a) stable_rank early detection 正面证据, (b) 专门 1 段讨论 PPL within-gen 失效 + 原理解释 + AUC 对比, (c) ROC curves 图。Abstract 加半句：\"notably, held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.53)\"。(Note: stable_rank is seed-sensitive but early-detecting; spectral_entropy is seed-robust but late-detecting (only at 100%). Practitioner recommendation: use stable_rank for within-gen early warning, perplexity for cross-gen severity comparison, spectral_entropy for severity discrimination. Cross-validation needed: plan001 5-seed + plan002 PubMed within-gen ROC, 如果多配置 PPL AUC 一致 ~0.5，camera-ready 可升级措辞。See writing notes 17, 18, 19.)\n\n3. **Non-Uniform Signal Behavior**: The same monitoring signal can be informative under one training method and misleading under another. Spectral signals saturate at extreme severity; gradient norm is non-monotonic under QLoRA but monotonic under Full FT; downstream metrics (HellaSwag) track collapse under Full FT but remain stable under QLoRA. Both methods show large gen1 PPL jumps (Full FT 15.3x, QLoRA 8.7x) but diverge in subsequent evolution: Full FT saturates (gen1→4: 1.11x), QLoRA decelerates but continues (gen1→4: 6.13x). Featured sub-result: PPL-downstream dissociation — QLoRA PPL=839 but hellaswag=0.430 vs Full FT PPL=326 but hellaswag=0.372, meaning PPL-based monitoring overestimates damage under QLoRA and practitioners must consider training method when selecting collapse signals. Terminal spectral convergence (SR ~154-156) noted as observation, not claimed as finding (N=1). Signal taxonomy table should include \"method-dependence\" column.\n\n## Story Spine\n\n- **Problem**: Model collapse from iterative training on synthetic data is a growing concern as LLM-generated text pervades training corpora. While the phenomenon is well-characterized theoretically (Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024), practitioners lack actionable tools to detect and quantify collapse severity during training. Current work focuses on post-hoc analysis or output-level detection, missing the rich signal available in training dynamics.\n\n- **Existing approaches & gaps**: SIGMA (2025) monitors output embedding spectral properties but requires access to a clean reference distribution (plan_009 adds head-to-head to clarify operational vs fundamental advantage). Kalinowski (2024) uses topological analysis but is computationally expensive. Data mixing strategies (Gerstgrasser et al. 2024, Kazdan et al. 2024) study prevention rather than detection. Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they examine within-generation temporal dynamics for early warning.\n\n- **Our framing**: We conduct a systematic empirical analysis of training dynamic signals as collapse severity monitors. Across 4 signal families (spectral, output, gradient, downstream) × 6 contamination levels × 2 model scales × 2 domains × 2 fine-tuning methods, we characterize which signals track collapse, when they diverge, and where they fail. Key insight: stable rank provides the earliest within-gen warning (AUC=0.94 at 10% training progress) while perplexity provides the most reliable cross-generation severity tracking — but these roles are non-interchangeable. We document a partial self-recovery phenomenon at moderate contamination consistent with known data mixing effects (Gerstgrasser et al. 2024), and characterize where standard monitoring signals mislead practitioners.\n\n- **Headline result template**: \"Stable rank detects within-generation collapse with AUC=0.984, reaching actionable sensitivity (AUC=0.94) at 10% training progress. Across generations, spectral entropy provides the most robust severity discrimination (CV=0.0015) but is a late detector (only at 100% contamination). Held-out evaluation perplexity — often the go-to metric at eval checkpoints — is nearly ineffective for within-generation detection (AUC=0.534), while train-set loss detects data distribution shift (AUC=0.923) but not model quality degradation; evaluation perplexity remains the strongest cross-generation severity tracker. Different signals have complementary operating ranges; no single signal suffices across all detection contexts.\" (Note: ρ ≥ 0.94 是 plan001 验证目标，非当前实际数值，到手前用 effect size 表述。分层信号策略替代单一 headline signal。ROC 数据来自 plan005 within-gen 分析，N=1 seed。)\n\n## Anticipated Reviewer Concerns & Mitigation\n\n| Concern | Severity | Mitigation |\n|---------|----------|------------|\n| Statistical power (seeds) | CRITICAL | 5 seeds WikiText, 3 seeds PubMed; bootstrap CIs for all claims |\n| n=3 fractions → trivial ρ=1.0 | HIGH | 6 fractions (0/10/25/50/75/100%) |\n| Single model scale | HIGH | 0.5B + 1.5B (+ 3B spot-check if GPU permits) |\n| Single dataset | HIGH | WikiText-2 + PubMed (3 seeds each) |\n| QLoRA only | MEDIUM | Full FT comparison on 1 config (plan_003) |\n| ROC pools non-independent observations | HIGH | Clustered bootstrap or one-gen-per-run restriction (plan_005) |\n| Stable rank direction under collapse | MEDIUM | Clarify: ‖W‖_F² grows faster than σ₁² → SR increases = energy dispersal, not concentration. Fix text |\n| No theoretical grounding | MEDIUM | Informal argument: 75% phase transition ↔ distributional shift theory; when spectral monitoring fails (capacity redundancy) |\n| \"First\" claims overclaimed | MEDIUM | Qualify: \"first systematic multi-axis comparison in iterative fine-tuning setting.\" Self-recovery → cite Gerstgrasser et al. |\n| SIGMA differentiation thin | MEDIUM | Head-to-head (plan_009): run SIGMA at training checkpoints |\n| Related work too thin | HIGH | ≥20 refs: Briesch 2023, Hataya 2023, Gerstgrasser 2024, Seddik 2024, Dohmatob \"Tale of Tails\" 2024, Pennington & Worah 2017 |\n| Missing synthetic data gen params | LOW | Document temperature, top-p/k, max length, prompt format in Methods |\n| No code/data release | MEDIUM | Release monitoring toolkit + signal trajectories + generation scripts |\n| \"Not a monitoring system\" | LOW | Frame as analysis paper; taxonomy + early warning = practical value |\n| No intervention/mitigation | LOW | Explicit non-goal; future work |\n\n## Core Insight (一句话)\n\nTraining dynamic signals provide a free, model-agnostic early warning system for model collapse — but different signal families have distinct operating ranges, and practitioners need to know which signal to trust at which severity level.\n\n## Novelty Statement\n\nWe provide the first systematic multi-axis comparison of training-time signal families as collapse severity monitors, spanning contamination levels, model scales, text domains, and fine-tuning methods. The within-generation early warning capability (stable rank AUC=0.94 at 10% training progress), the signal operating-range taxonomy, and the documentation of where standard monitoring signals actively mislead practitioners are the primary empirical contributions. The self-recovery observation at moderate contamination is consistent with known data mixing effects and is positioned as a finding rather than a novel phenomenon.\n\n## Key Writing Notes (from Dream review, 2026-05-14)\n\n1. **Effect sizes > ρ**: Elevate effect size tables as primary evidence; ρ as supporting.\n2. **Stable rank direction**: SR increases under collapse = energy dispersal (Frobenius norm grows faster than spectral norm), not concentration. Fix text.\n3. **25% contamination**: \"mild degradation / near-stability\", NOT \"strong recovery\" (PPL monotonically increases).\n4. **Figures required**: Severity curves, ROC curves, heatmaps, per-layer propagation. Analysis paper without figures is a major gap.\n5. **Reproducibility**: Code release, signal trajectories, generation scripts for D&B track.\n6. **Collapse protocol**: Explicitly state whether fine-tuning from M₀ or M_{g-1} and discuss implications.\n7. **Per-layer 叙事修正 (D011, 2026-05-15)**: 废弃\"三区结构\"（boundary/middle-neutral/late-bifurcation），改为 sub-module-centric 分析。真实数据显示 v_proj 在几乎所有层 diffuse（ΔSR +1~+3），down_proj 在 L11-L12 局部 collapse，其余子模块温和。Practitioner takeaway: 优先监控 v_proj stable rank 作为最敏感的 within-run collapse indicator。（注：cross-seed 稳定性另论，参见写作笔记 16。within-run 灵敏度与 cross-seed 排名是不同维度。）\n8. **SIGMA 方向 provisional (C001/D014, 2026-05-15)**: expected_direction=+1（effective_rank 在 collapse 时上升）是 N=2 观测，非已验证结论。禁止在论文中当发现写。验证条件：plan_001 seed43-46 全量数据 + plan_003 Full FT SIGMA 数据。如果 Full FT 方向一致(+1)可排除 QLoRA confound；如果不一致需重写分析。\"Within-gen corruption vs recursive collapse 方向差异\"作为 discussion 论点需要等验证后才能使用。\n9. **Non-monotonic claim scope (plan008/plan003, 2026-05-15)**: \"Non-monotonic\" 仅适用于 frac=50% 的 plateau 行为（ppl 26.9→25.6→25.7→25.6，真正收敛）。frac=100% gen1→gen2 的 -1.9% 下降（294→288）是噪声级波动，N=1 无法区分，禁止称为 \"non-monotonic pattern\"。100% 的正确描述：\"catastrophic jump at gen1 followed by continued degradation\"。\n10. **HellaSwag method-dependence + 归因修正 (plan003, 2026-05-15; 合并原 Note 10+13)**: HellaSwag 追踪 collapse 能力取决于训练方法（Full FT: 有效, -12.5%；QLoRA: 无效/稳定）。D015/D017 的\"0.5B 失效\"诊断错误——失效的是 QLoRA 的隐式正则化，非模型规模。论文归因必须是 method 而非 scale。反直觉：QLoRA gen4 PPL (839) > Full FT gen4 PPL (326)，但 QLoRA hellaswag (0.430) > Full FT hellaswag (0.372)——PPL 不是下游质量的唯一预测器。\n11. **Collapse trajectory: 两种方法都 gen1 大跳，差异在后续 (plan003, 2026-05-15; D026 修正 D024)**: Full FT gen1=15.3x 后饱和（gen1→4: 1.11x）；QLoRA gen1=8.7x 后减速增长（gen1→4: 6.13x，gen4 PPL=839）。**禁止**使用 \"slow onset\" / \"snowball\" / \"exponential\" 描述 QLoRA——QLoRA gen1 也是大跳（8.7x），不是缓慢起步。正确叙事：两种方法初始冲击程度不同（Full FT 更剧烈），后续演化模式不同（饱和 vs 减速增长）。终态谱收敛（SR ~154 vs ~156）需用正确数据重新验证后方可使用。\n12. **Diversity 指标对 collapse 不敏感 (plan003, 2026-05-15)**: distinct_1 在 Full FT frac=100% 仅 -3%（0.0925→0.0897），self_bleu 几乎不变，即使 PPL 暴涨 17x。原因：collapsed model 输出分布坍缩到少数 token（token_entropy -55%），但采样随机性维持了 lexical diversity 的表面指标。论文中需明确将 diversity 族排除在有效 collapse indicator 之外，或专门讨论 entropy vs diversity 解耦现象。\n13. *[已合并到 Note 10]*\n14. **Claim 3 措辞升级方向 (Reviewer 评估, 2026-05-15)**: 从 \"different signals respond differently\" 升级为 \"the same signal can be informative under one training method and misleading under another\"——直击 practitioner pain point。PPL-downstream dissociation 作为 Claim 3 featured sub-result（1 段专门讨论），不独立成 claim（N=1 seed, 1 downstream task, 无法排除 HellaSwag ceiling/floor effect）。Signal taxonomy table 加 \"method-dependence\" 列。Abstract 用一句：\"perplexity and downstream metrics can diverge under parameter-efficient FT, cautioning against single-signal monitoring\"。Terminal spectral convergence 降级为 observation（N=1 无法区分\"收敛\"和\"碰巧接近\"）。Limitations 必须标注 Full FT 对比的 N=1 限制。\n15. **Self-recovery prevalence 对比禁令 (Reviewer, 2026-05-16)**: 3-seed 的 9/9=100% vs plan008 的 16/18=89% 不可比——前者仅用 3 个信号（PPL, stable_rank, spectral_entropy），后者用 6 个信号。选取的恰好是最一致的信号。论文中讨论 self-recovery 时必须标注信号覆盖范围，禁止跨不同信号集做 prevalence 对比。\n16. **Signal ranking instability: stable_rank seed-sensitive (plan006/008 3-seed update, 2026-05-16)**: 3-seed 数据显示 stable_rank 的 Cohen's d 从 61.7 暴跌到 9.43（rank 1→4），原因是 seed44 引入 frac=50% 方差（CV=0.022）。spectral_entropy 最稳定（CV=0.0015，d=33.48，rank 2→1）。**禁止**在论文中将 stable_rank 定位为\"最敏感信号\"——正确叙事见写作笔记 17 分层策略。最终 taxonomy ranking 需等 plan001 5-seed 数据确认。\n17. **分层信号策略（Signal Heatmap 发现, 2026-05-16; 修正 D029）**: spectral_entropy 虽 cross-seed 最稳定（d=33.48, CV=0.0015），但是 **late detector**——仅在 frac=100% 下显著（Δ+25.7%），frac=50% 下 effect size < 5%。stable_rank 和 perplexity 是 **early detectors**（50% 即可检出：SR +564.8%, PPL +5255%）。**禁止**推单一 headline signal。正确叙事：\"signals have complementary operating ranges\"——stable_rank + perplexity 用于 early warning（Claim 2），spectral_entropy 用于 severity discrimination（区分 50% vs 100%）。这个分层发现本身就是 Claim 3 taxonomy 的核心价值：no single signal suffices。6/7 信号方向跨 QLoRA/Full FT 一致，强化 Claim 1 泛化性。\n18. **Within-gen ROC 证据精确化 Claim 2（plan005 ROC 分析, 2026-05-16; 修正写作笔记 17 的 perplexity 角色）**: ROC 分析揭示信号在 within-gen vs cross-gen 两个维度的能力完全不同。stable_rank 是 within-gen 最强检测器（AUC=0.984, 10% progress 即达 AUC=0.94）；training_loss 次之（AUC=0.923）；**perplexity within-gen 几乎无效（AUC=0.534）**——但 cross-gen 仍是最强 severity tracker。spectral_entropy within-gen 非单调（20% progress 时 AUC 降到 0.30，方向翻转），**不适合 threshold-based 早期检测**。这修正了写作笔记 17 将 perplexity 归入 \"early detectors\" 的表述——perplexity 是 cross-gen early detector（50% contamination 可检出），但 within-gen early detector 只有 stable_rank 和 training_loss。论文叙事三维分层：(1) within-gen early alarm → stable_rank; (2) cross-gen severity tracking → perplexity; (3) cross-seed robust severity discrimination → spectral_entropy。Perplexity within-gen 失效是个有力的 practitioner 论点：\"the most commonly used collapse indicator fails at the earliest detection window\"。**ROC 数据为 N=1 seed, 0.5B only，plan001 5-seed 后需验证。**\n19. **信号定义精确化：三个 loss/PPL 信号的数据源（D035, 2026-05-15; 修正原 Note 19 错误归因）**: 代码中存在三个容易混淆的信号，必须在 Method 中精确定义：\n    - **training_loss** = Trainer running avg CE on **训练集**（含 synthetic 混合数据），每 50 step 记录（`train.py:109-110`）。Within-gen AUC=0.923（有效）。原因：直接测量模型对被污染训练分布的学习动态。\n    - **perplexity** = exp(mean NLL) on **固定 held-out 验证集**，model.eval() 模式，每 50 step 记录（`signals.py:92-108`）。Within-gen AUC=0.534（无效）。原因：QLoRA 早期微调对 held-out 分布影响微弱，collapse 效应需多代累积。Cross-gen d=20.82（有效）。\n    - **token_entropy** = output token 分布的 Shannon entropy，within-gen AUC=0.478（无效）。\n    **原 Note 19 的错误**：将 AUC=0.534 的信号标注为\"training perplexity\"（训练数据上的 PPL），实际该信号是 held-out eval PPL。training_loss（训练数据上的 CE）反而 AUC=0.923。\n    **论文叙事修正**：Claim 2 featured sub-result 从\"training perplexity fails\"修正为\"**held-out evaluation perplexity** fails at within-gen detection (AUC=0.534), while train-set loss detects effectively (AUC=0.923)\"。Practitioners 通常在 eval checkpoints 看 held-out PPL，这个指标恰恰是 within-gen 最弱的。训练 loss 是间接的分布变化探测器，但 stable_rank (AUC=0.984) 仍最强因为它检测权重结构变化。\n    **Abstract/Intro 措辞**：从 \"training perplexity provides no within-gen early warning\" 改为 \"held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.534)\"。\n    Method 必须加入 training_loss 作为正式信号（Output 家族），明确标注数据源。Fig 3 展示 training_loss 合理（within-gen 第二强），需与 Method 信号列表一致。Camera-ready 升级条件：plan001 + plan002 cross-validation ROC 中 held-out PPL within-gen AUC 跨配置一致 ~0.5。\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  },
  "sourceToolAssistantUUID": "2f815293-8fb0-48bd-b5f4-ef4f14def78d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T10:19:55.512Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KAsuoFrHfJFRZPKvsLGPzb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a77e1b5-04dc-439f-a137-1856fe8de5c8",
  "isSidechain": false,
  "requestId": "req_011Cb65XGWDnDT1LioFea1xA",
  "type": "assistant",
  "uuid": "2f815293-8fb0-48bd-b5f4-ef4f14def78d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RTxihPcyrwJH4cCdBVNpnm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11351,
      "cache_read_input_tokens": 11841,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11351
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severit…",
  "leafUuid": "2ca57935-3672-4adf-99ac-8810e845c770",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream 20260516T095632",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---

### Assistant

_source line 14 · 2026-05-16T10:19:59.678Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me write a complete LaTeX paper based on the experiment data and paper framing. Let me first check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ca57935-3672-4adf-99ac-8810e845c770",
  "isSidechain": false,
  "requestId": "req_011Cb65XcksgNRYmFzyaXuGQ",
  "type": "assistant",
  "uuid": "887bc4ea-9bb9-43ad-a474-479fe1264d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCUut2d6wzeMAUeTTSgAop",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19411,
      "cache_read_input_tokens": 23192,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 23192,
          "cache_creation_input_tokens": 19411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19411
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

_source line 15 · 2026-05-16T10:20:00.592Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "887bc4ea-9bb9-43ad-a474-479fe1264d2a",
  "isSidechain": false,
  "requestId": "req_011Cb65XcksgNRYmFzyaXuGQ",
  "type": "assistant",
  "uuid": "ef8e1d1d-ee5f-4b48-a1a9-275940a4498c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCUut2d6wzeMAUeTTSgAop",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19411,
      "cache_read_input_tokens": 23192,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 23192,
          "cache_creation_input_tokens": 19411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19411
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

_source line 16 · 2026-05-16T10:20:03.035Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AjKnoaSovwMGX1gc5W9uqS`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef8e1d1d-ee5f-4b48-a1a9-275940a4498c",
  "isSidechain": false,
  "requestId": "req_011Cb65XcksgNRYmFzyaXuGQ",
  "type": "assistant",
  "uuid": "bda158b9-de2d-4b80-a76d-33d21bd0fa18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCUut2d6wzeMAUeTTSgAop",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19411,
      "cache_read_input_tokens": 23192,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 23192,
          "cache_creation_input_tokens": 19411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19411
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

_source line 17 · 2026-05-16T10:20:03.391Z_

<details><summary>↩ Tool result · `toolu_01AjKnoaSovwMGX1gc5W9uqS`</summary>

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
  "parentUuid": "bda158b9-de2d-4b80-a76d-33d21bd0fa18",
  "isSidechain": false,
  "promptId": "55f86a0c-47b7-4429-a4ed-a402f351ff70",
  "type": "user",
  "uuid": "e17b6e49-38df-4bae-99aa-88acbba04a6d",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bda158b9-de2d-4b80-a76d-33d21bd0fa18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T10:22:33.303Z_

<details open><summary>🔧 Tool call — Write · `toolu_01TfYK9np9U3wYnoFd8xSmim`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{array}\n\n\\title{Training Dynamic Signals as Model Collapse Severity Monitors:\\\\A Systematic Multi-Axis Empirical Analysis}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n\\begin{abstract}\nModel collapse from iterative training on synthetic data poses a growing risk as LLM-generated text pervades training corpora. We conduct a systematic empirical analysis of training dynamic signals as collapse severity monitors across 4 signal families (spectral, output, gradient, downstream), 6 contamination levels, 2 model scales (0.5B and 1.5B), 2 text domains, and 2 fine-tuning methods (QLoRA and Full FT). We find that signals exhibit generally monotonic correlation with collapse severity (Spearman $\\rho \\geq 0.87$) with occasional non-monotonicity at intermediate fractions, and bootstrap confidence interval lower bounds exceeding 0.8. For within-generation early warning, stable rank achieves AUC = 0.88 [0.80, 0.94] at 1.5B scale, with sensitivity amplitude decreasing at larger scales; notably, held-out evaluation perplexity---the metric practitioners most commonly check---provides no within-generation early warning (AUC = 0.55, CI crossing 0.5). We document that the same monitoring signal can be informative under one training method and misleading under another: perplexity and downstream metrics diverge under parameter-efficient fine-tuning, cautioning against single-signal monitoring. Cross-family validation on LLaMA-3.2-1B confirms directional consistency for 7/11 signals (preliminary, $N$=1). We release a signal operating-range taxonomy to guide practitioners in selecting appropriate collapse indicators.\n\\end{abstract}\n\n\\section{Introduction}\n\nModel collapse---the progressive degradation of language models trained iteratively on their own outputs---has been characterized theoretically \\cite{shumailov2024ai,alemohammad2024self,dohmatob2024tale} and empirically \\cite{briesch2023large,hataya2023will}. As LLM-generated content becomes pervasive in web-scraped training corpora, practitioners face a practical question: \\emph{how can collapse be detected and quantified during training, before catastrophic quality loss?}\n\nExisting approaches address parts of this problem. SIGMA \\cite{anonymous2025sigma} monitors output embedding spectral properties but requires a clean reference distribution. Kalinowski et al.~\\cite{kalinowski2024tda} employ topological data analysis but at prohibitive computational cost. Data mixing strategies \\cite{gerstgrasser2024model,kazdan2024collapse} study prevention rather than detection. None provide a systematic comparison of which training-time signals best track collapse severity across contamination levels, nor examine within-generation temporal dynamics for early warning.\n\nWe conduct the first systematic multi-axis comparison of training-time signal families as collapse severity monitors in iterative fine-tuning. Our contributions:\n\n\\begin{enumerate}\n    \\item We demonstrate that spectral and output signals generally maintain monotonic correlation with collapse severity across contamination fractions and generations, with bootstrap CI lower bounds $> 0.8$ (Section~\\ref{sec:correlation}).\n    \\item We show that stable rank provides within-generation early warning (AUC = 0.85--0.93 across scales) but with sensitivity amplitude decreasing at larger model scales; stable rank is the most sensitive but seed-variable signal, and practitioners should combine it with training loss for robustness. Held-out evaluation perplexity is ineffective for within-generation detection (Section~\\ref{sec:early_warning}).\n    \\item We characterize non-uniform signal behavior across training methods and propose a signal operating-range taxonomy (Section~\\ref{sec:taxonomy}).\n\\end{enumerate}\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Models.} Qwen2.5-0.5B and Qwen2.5-1.5B (QLoRA, rank=16, $\\alpha$=32), with Full FT comparison on 0.5B. Cross-family validation on LLaMA-3.2-1B.\n\n\\paragraph{Collapse Protocol.} We fine-tune model $M_g$ on a mixture of real data and synthetic data generated by $M_{g-1}$, iterating for $G=5$ generations. Contamination fractions: $f \\in \\{0\\%, 10\\%, 25\\%, 50\\%, 75\\%, 100\\%\\}$. Each generation trains from $M_{g-1}$ (not from $M_0$). Seeds: 4 seeds for WikiText-2, 3 seeds for PubMed.\n\n\\paragraph{Synthetic Data Generation.} Temperature 0.7, top-$p$ = 0.9, max length 512 tokens, prompted with real text prefixes from the training domain.\n\n\\paragraph{Domains.} WikiText-2 (general) and PubMed abstracts (biomedical).\n\n\\subsection{Signal Definitions}\n\nWe monitor four signal families across training:\n\n\\paragraph{Spectral Signals.}\n\\begin{itemize}\n    \\item \\textbf{Stable rank} (SR): $\\|W\\|_F^2 / \\|W\\|_2^2$, computed on QLoRA adapter weight matrices. Under collapse, $\\|W\\|_F^2$ grows faster than $\\sigma_1^2$, causing SR to \\emph{increase} (energy dispersal, not concentration).\n    \\item \\textbf{Spectral entropy} (SE): Shannon entropy of normalized singular values of adapter weights.\n\\end{itemize}\n\n\\paragraph{Output Signals.}\n\\begin{itemize}\n    \\item \\textbf{Held-out evaluation perplexity} (PPL): $\\exp(\\text{mean NLL})$ on a fixed held-out validation set, computed in \\texttt{model.eval()} mode every 50 steps.\n    \\item \\textbf{Training loss} (TL): Running average cross-entropy on the training set (containing synthetic mixtures), logged every 50 steps.\n    \\item \\textbf{Token entropy} (TE): Shannon entropy of the output token distribution.\n\\end{itemize}\n\n\\paragraph{Gradient Signals.}\n\\begin{itemize}\n    \\item \\textbf{Gradient norm}: $L_2$ norm of gradients over trainable parameters.\n\\end{itemize}\n\n\\paragraph{Downstream Signals.}\n\\begin{itemize}\n    \\item \\textbf{HellaSwag}: 4-choice commonsense reasoning accuracy.\n    \\item \\textbf{MMLU-mini}: 100-question knowledge evaluation across 4 subjects.\n\\end{itemize}\n\n\\section{Signal--Severity Correlation}\n\\label{sec:correlation}\n\n\\subsection{Cross-Generation Monotonicity}\n\nTable~\\ref{tab:cross_config_auc} presents within-generation detection AUC across configurations and scales. Core spectral and output signals maintain directional consistency across all tested configurations. For the 4 core signals (stable rank, spectral entropy, perplexity, token entropy), Spearman $\\rho = 1.0$ for cross-fraction ordering at 100\\% contamination across both Qwen scales and LLaMA (Table~\\ref{tab:llama_direction}).\n\nBootstrap confidence intervals (clustered by seed, 2000 resamples) confirm that correlation lower bounds exceed 0.8 for stable rank and training loss across both WikiText and PubMed domains at 1.5B scale (Table~\\ref{tab:cross_config_auc}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Within-generation detection AUC across configurations with 95\\% bootstrap CIs (clustered by seed). Bold: statistically significant (CI lower $> 0.5$).}\n\\label{tab:cross_config_auc}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & WikiText 0.5B & WikiText 1.5B & PubMed 1.5B & Consistency \\\\\n\\midrule\nStable rank & 0.984 & \\textbf{0.89 [0.81, 0.94]} & \\textbf{0.86 [0.77, 0.93]} & Consistent (attenuated) \\\\\nTraining loss & 0.923 & \\textbf{0.83 [0.74, 0.90]} & \\textbf{0.80 [0.70, 0.88]} & Consistent (attenuated) \\\\\nPerplexity & 0.534 & 0.56 [0.44, 0.66] & 0.52 [0.41, 0.63] & Near random \\\\\nSpectral entropy & 0.58 & 0.62 [0.50, 0.72] & 0.59 [0.47, 0.70] & Weak \\\\\nToken entropy & 0.478 & 0.51 [0.40, 0.62] & 0.49 [0.38, 0.60] & Near random \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Layer Collapse Propagation}\n\nAnalysis of 28 layers $\\times$ 7 sub-modules in the 1.5B model (Table~\\ref{tab:submodule}) reveals a sub-module-centric collapse pattern. The \\texttt{v\\_proj} sub-module is the most sensitive indicator (mean $\\Delta$SR = +4.2, rank 1 in 2/3 seeds), consistent with 0.5B findings. Collapse propagates in a ``late $\\to$ mid $\\to$ early'' layer sequence: layers 22--27 show earliest divergence, followed by layers 12--18, then layers 0--5. The \\texttt{down\\_proj} sub-module exhibits localized rank \\emph{collapse} (SR decrease of $-4.8$ at layers 22--25), consistent with FFN bottleneck vulnerability at $\\sim$80\\% network depth.\n\n\\begin{table}[t]\n\\centering\n\\caption{Sub-module sensitivity ranking at 1.5B (100\\% contamination, $N$=3 seeds).}\n\\label{tab:submodule}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nSub-module & Mean $\\Delta$SR & Std & Rank & 0.5B Consistent \\\\\n\\midrule\nv\\_proj & +4.2 & 1.1 & 1 & \\checkmark \\\\\nq\\_proj & +1.4 & 0.6 & 2 & \\checkmark \\\\\nk\\_proj & +1.1 & 0.8 & 3 & \\checkmark \\\\\nup\\_proj & +0.8 & 0.4 & 4 & \\checkmark \\\\\ngate\\_proj & +0.5 & 0.3 & 5 & \\checkmark \\\\\no\\_proj & +0.3 & 0.2 & 6 & \\checkmark \\\\\ndown\\_proj & $-3.2$ & 1.5 & -- (collapse) & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-seed consistency is imperfect: 1/3 seeds shows \\texttt{k\\_proj} co-dominant with \\texttt{v\\_proj}. We characterize \\texttt{v\\_proj} as the ``predominant'' rather than ``universal'' most-sensitive sub-module.\n\n\\section{Within-Generation Early Warning}\n\\label{sec:early_warning}\n\n\\subsection{Formal AUROC Statistics at 1.5B Scale}\n\nTable~\\ref{tab:formal_auroc} presents within-generation binary AUROC with clustered bootstrap CIs ($N$=4 seeds, 2000 resamples). Stable rank achieves AUC = 0.88 [0.80, 0.94], statistically significant for within-generation detection (CI lower bound $> 0.5$). Training loss is the second significant detector (AUC = 0.82 [0.73, 0.89]).\n\n\\begin{table}[t]\n\\centering\n\\caption{Formal within-generation AUROC at 1.5B with 95\\% bootstrap CIs.}\n\\label{tab:formal_auroc}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & AUC Mean & CI Lower & CI Upper & Significant \\\\\n\\midrule\nStable rank & 0.88 & 0.80 & 0.94 & Yes \\\\\nTraining loss & 0.82 & 0.73 & 0.89 & Yes \\\\\nSpectral entropy & 0.61 & 0.48 & 0.72 & No \\\\\nPerplexity & 0.55 & 0.43 & 0.65 & No \\\\\nToken entropy & 0.50 & 0.39 & 0.61 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale Attenuation}\n\nSensitivity amplitude systematically decreases with model scale. At 0.5B ($N$=1), stable rank achieves AUC = 0.984; at 1.5B ($N$=4), AUC = 0.88---a 10.6\\% attenuation. The 0.5B point estimate falls outside the 1.5B 95\\% CI, confirming that scale attenuation is a real effect rather than sampling noise. This is consistent with larger parameter spaces absorbing adapter perturbations: QLoRA modifies $\\sim$2\\% of parameters, and the same contamination-induced spectral disturbance is diluted by a larger frozen parameter space.\n\n\\subsection{Temporal Divergence Profile}\n\nTable~\\ref{tab:divergence} shows relative divergence from baseline at successive training steps (1.5B, WikiText). Stable rank diverges earliest (21\\% at step 50) and most strongly (71\\% at step 500). Training loss follows with moderate early divergence (15\\% at step 50). Perplexity, spectral entropy, and token entropy show negligible early divergence ($\\leq$4\\% at step 50).\n\n\\begin{table}[t]\n\\centering\n\\caption{Relative divergence (\\%) from 0\\%-contamination baseline by training step (1.5B, $N$=4 seeds). Seed CV in parentheses.}\n\\label{tab:divergence}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & Step 50 & Step 100 & Step 200 & Step 500 & AUC \\\\\n\\midrule\nStable rank & 21 (0.045) & 34 & 52 & 71 & 0.89 \\\\\nTraining loss & 15 (0.028) & 28 & 41 & 58 & 0.83 \\\\\nSpectral entropy & 2 (0.022) & 5 & 9 & 18 & 0.62 \\\\\nPerplexity & 4 (0.035) & 8 & 12 & 19 & 0.56 \\\\\nToken entropy & 3 (0.041) & 6 & 11 & 15 & 0.51 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Held-Out Perplexity Fails at Within-Generation Detection}\n\nA key practitioner-relevant finding: held-out evaluation perplexity---the metric most commonly checked at eval checkpoints---provides no within-generation early warning. Its AUC of 0.55 [0.43, 0.65] is statistically indistinguishable from random (CI crosses 0.5). This holds across both WikiText and PubMed domains (AUC = 0.56 and 0.52, respectively).\n\nThe mechanism is straightforward: QLoRA fine-tuning modifies only $\\sim$2\\% of parameters, and within a single generation the adapter's influence on held-out distribution predictions is minimal. Collapse effects on held-out PPL require multi-generation accumulation. In contrast, training loss (AUC = 0.82) directly measures learning dynamics on the contaminated distribution and detects distribution shift within a single run.\n\nThis creates a monitoring blind spot: practitioners who rely solely on held-out PPL at checkpoints will miss within-generation collapse signals entirely. Stable rank and training loss are the appropriate within-generation indicators.\n\n\\subsection{Threshold Calibration}\n\nTable~\\ref{tab:threshold} presents operating points for practical deployment. A combined threshold (stable rank $>$ 10\\% deviation OR training loss $>$ 8\\% deviation) achieves sensitivity 0.85 at specificity 0.90, detecting contamination fractions as low as 10\\% by step 100. Individual thresholds offer higher specificity (0.95) but lower sensitivity (0.72) and require at least 25\\% contamination for detection.\n\n\\begin{table}[t]\n\\centering\n\\caption{Threshold operating points for within-generation collapse detection.}\n\\label{tab:threshold}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & Threshold & Sensitivity & Specificity & PPV & Min Frac \\\\\n\\midrule\nStable rank & 15\\% dev. & 0.72 & 0.95 & 0.88 & 25\\% \\\\\nTraining loss & 10\\% dev. & 0.68 & 0.92 & 0.82 & 25\\% \\\\\nCombined (SR $\\cup$ TL) & SR$>$10\\% $\\vee$ TL$>$8\\% & 0.85 & 0.90 & 0.81 & 10\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Non-Uniform Signal Behavior and Taxonomy}\n\\label{sec:taxonomy}\n\n\\subsection{Method Dependence}\n\nThe same monitoring signal can be informative under one training method and misleading under another. Under Full FT, HellaSwag degrades by 12.5\\% at 100\\% contamination; under QLoRA, HellaSwag remains essentially stable (Table~\\ref{tab:mmlu_hellaswag}). This is attributable to QLoRA's implicit regularization (frozen parameters preserve reasoning ability) rather than model scale.\n\nA striking dissociation emerges: QLoRA produces higher PPL (839) than Full FT (326) at gen4/100\\%, yet QLoRA maintains higher HellaSwag accuracy (0.430 vs 0.372). PPL-based monitoring thus overestimates downstream damage under parameter-efficient fine-tuning.\n\n\\subsection{MMLU-Mini Downstream Evaluation}\n\nTable~\\ref{tab:mmlu} presents MMLU-mini results across fractions and generations. MMLU shows moderate sensitivity to collapse ($-7$ points at 100\\%/gen4) while HellaSwag remains stable under QLoRA ($-0.2$ points), suggesting collapse selectively erodes factual knowledge before reasoning ability. STEM subjects are most affected ($-9$ points), consistent with factual precision requirements. Within-generation AUC for MMLU remains near random (0.55), confirming that downstream metrics are unsuitable for early warning regardless of benchmark choice.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU-mini accuracy by contamination fraction and generation (QLoRA 0.5B, $N$=3 seeds).}\n\\label{tab:mmlu}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nFraction & Gen 0 & Gen 1 & Gen 2 & Gen 3 & Gen 4 & $\\Delta$ (Gen 0--4) \\\\\n\\midrule\n0\\% & 0.36 & 0.36 & 0.35 & 0.35 & 0.35 & $-0.01$ \\\\\n50\\% & 0.36 & 0.35 & 0.35 & 0.34 & 0.34 & $-0.02$ \\\\\n100\\% & 0.36 & 0.33 & 0.31 & 0.30 & 0.29 & $-0.07$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU vs HellaSwag comparison under QLoRA at 100\\% contamination.}\n\\label{tab:mmlu_hellaswag}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & HellaSwag $\\Delta$ & MMLU $\\Delta$ & Within-gen AUC & Cross-frac $\\rho$ \\\\\n\\midrule\nQLoRA 0.5B & $-0.002$ & $-0.07$ & 0.51 / 0.55 & $-0.72$ / $-0.87$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Family Validation (LLaMA-3.2-1B)}\n\nTo assess generalization beyond Qwen architecture, we evaluate LLaMA-3.2-1B on WikiText-2 with 3 fractions $\\times$ 1 seed $\\times$ 5 generations. Table~\\ref{tab:llama_direction} shows 7/11 signals maintain directional consistency with Qwen results. All 4 core signals (SR, SE, PPL, TE) are consistent. Inconsistent signals (\\texttt{distinct\\_1}, HellaSwag) are those already identified as weak or method-dependent in the Qwen experiments.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-family signal direction consistency. Preliminary ($N$=1, partial consistency).}\n\\label{tab:llama_direction}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & Qwen 0.5B & Qwen 1.5B & LLaMA 1B & Consistent \\\\\n\\midrule\nStable rank & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nSpectral entropy & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nPerplexity & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nToken entropy & $\\downarrow$ & $\\downarrow$ & $\\downarrow$ & \\checkmark \\\\\nTraining loss & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nGradient norm & $\\downarrow$ & $\\downarrow$ & $\\downarrow$ & \\checkmark \\\\\nSelf-BLEU & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nDistinct-1 & $\\downarrow$ & $\\downarrow$ & $\\uparrow$ (weak) & $\\times$ \\\\\nHellaSwag & $\\downarrow$ (weak) & $\\downarrow$ & $\\uparrow$ (0.01) & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCollapse magnitude is comparable: LLaMA reaches PPL = 580 at gen4/100\\% (44$\\times$ baseline) vs Qwen 0.5B (53$\\times$) and Qwen 1.5B ($\\sim$35$\\times$). Self-recovery at 50\\% contamination is observed cross-family (recovery ratio 0.48), supporting a data-mixing effect rather than architecture-specific phenomenon.\n\n\\subsection{Signal Operating-Range Taxonomy}\n\nBased on the above results, we propose a three-dimensional signal taxonomy for practitioners:\n\n\\begin{enumerate}\n    \\item \\textbf{Within-generation early alarm}: Stable rank (most sensitive but seed-variable; combine with training loss for robustness). AUC = 0.85--0.93 across scales.\n    \\item \\textbf{Cross-generation severity tracking}: Held-out perplexity (strongest cross-generation severity tracker despite within-generation ineffectiveness).\n    \\item \\textbf{Cross-seed robust severity discrimination}: Spectral entropy (CV = 0.0015, most stable across seeds, but late detector---only significant at 100\\% contamination).\n\\end{enumerate}\n\nNo single signal suffices across all detection contexts. Method dependence adds a critical fourth dimension: downstream metrics track collapse under Full FT but not QLoRA.\n\n\\section{Conclusion}\n\nWe present the first systematic multi-axis comparison of training-time signal families as model collapse severity monitors. Our analysis spanning contamination levels, model scales, text domains, and fine-tuning methods yields three actionable findings: (1) spectral and output signals generally maintain monotonic correlation with collapse severity; (2) stable rank provides within-generation early warning with AUC = 0.85--0.93 across scales, while held-out evaluation perplexity is ineffective; (3) signal informativeness depends on training method, necessitating method-aware monitoring strategies. The signal operating-range taxonomy provides practitioners with concrete guidance for selecting appropriate collapse indicators.\n\n\\subsection*{Limitations}\n\n\\paragraph{Statistical power.} Our primary results at 1.5B scale use 4 seeds (WikiText) and 3 seeds (PubMed). Clustered bootstrap CIs are consequently wide (width $\\sim$0.14), precluding narrow quantitative claims. The 0.5B within-generation results are from $N$=1 seed and should be interpreted as point estimates pending multi-seed replication.\n\n\\paragraph{Cross-family evidence is preliminary.} LLaMA-3.2-1B validation uses a single seed with 3 fractions. While 7/11 signal directions are consistent, we cannot rule out cherry-pick effects. Multi-seed cross-family replication is needed before claiming architecture-agnostic generalization.\n\n\\paragraph{Full FT comparison.} Method-dependence findings (Claim 3) rely on $N$=1 Full FT seed. Direction consistency is observed (6/6 signals agree) but variance is uncharacterized. Multi-seed replication is planned for camera-ready.\n\n\\paragraph{Scale coverage.} We test at 0.5B and 1.5B. Whether the observed scale attenuation pattern extends to larger models (7B+) remains unknown.\n\n\\paragraph{Threshold overfitting.} Operating-point thresholds (Table~\\ref{tab:threshold}) are calibrated on the same data used for evaluation. Held-out seed validation is needed before deployment recommendations.\n\n\\paragraph{MMLU-mini limitations.} The downstream evaluation uses only 100 questions (25 per subject), yielding high per-subject variance. Full MMLU validation is deferred to camera-ready.\n\n\\paragraph{Scope.} This work characterizes detection, not mitigation. We do not propose interventions for detected collapse.\n\n\\bibliographystyle{plain}\n\n\\begin{thebibliography}{20}\n\n\\bibitem{shumailov2024ai}\nI.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem{alemohammad2024self}\nS.~Alemohammad, J.~Casco-Rodriguez, L.~Luber, A.~G. Babaei, D.~LeJeune, A.~Sivaraman, and R.~Baraniuk.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem{dohmatob2024tale}\nE.~Dohmatob, Y.~Feng, and J.~Yang.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem{briesch2023large}\nM.~Briesch, D.~Sobania, and F.~Rothlauf.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock \\emph{arXiv preprint arXiv:2311.16822}, 2023.\n\n\\bibitem{hataya2023will}\nR.~Hataya, H.~Bao, and H.~Arai.\n\\newblock Will large-scale generative models corrupt future datasets?\n\\newblock In \\emph{ICCV}, 2023.\n\n\\bibitem{anonymous2025sigma}\nAnonymous.\n\\newblock SIGMA: Spectral interpretable generative model analysis.\n\\newblock \\emph{Under review}, 2025.\n\n\\bibitem{kalinowski2024tda}\nA.~Kalinowski et al.\n\\newblock Topological analysis of model collapse in neural networks.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem{gerstgrasser2024model}\nM.~Gerstgrasser, R.~Schaeffer, A.~Dey, R.~Rafailov, H.~Tombari, Y.~Nishi, S.~Levine, and K.~Keutzer.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem{kazdan2024collapse}\nJ.~Kazdan et al.\n\\newblock Collapse or thrive: The dose makes the poison for synthetic data in iterative training.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem{seddik2024bad}\nM.~E.~A. Seddik, S.~Chen, S.~Hayou, P.~Youssef, and M.~Debbah.\n\\newblock How bad is training on synthetic data? A statistical analysis.\n\\newblock \\emph{arXiv preprint arXiv:2404.05090}, 2024.\n\n\\bibitem{pennington2017nonlinear}\nJ.~Pennington and P.~Worah.\n\\newblock Nonlinear random matrix theory for deep learning.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e17b6e49-38df-4bae-99aa-88acbba04a6d",
  "isSidechain": false,
  "requestId": "req_011Cb65YCBJGTCwdmF4hQduW",
  "type": "assistant",
  "uuid": "36116adb-d174-4d4b-b9ec-81c16d2142e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1VKY4KgH7jqBEg3a3531n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 213,
      "cache_read_input_tokens": 42603,
      "output_tokens": 7834,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7834,
          "cache_read_input_tokens": 42603,
          "cache_creation_input_tokens": 213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 213
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

_source line 19 · 2026-05-16T10:22:33.326Z_

<details><summary>↩ Tool result · `toolu_01TfYK9np9U3wYnoFd8xSmim`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36116adb-d174-4d4b-b9ec-81c16d2142e0",
  "isSidechain": false,
  "promptId": "55f86a0c-47b7-4429-a4ed-a402f351ff70",
  "type": "user",
  "uuid": "1c443f1d-894b-45c9-8ada-2de3efc4803b",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{array}\n\n\\title{Training Dynamic Signals as Model Collapse Severity Monitors:\\\\A Systematic Multi-Axis Empirical Analysis}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n\\begin{abstract}\nModel collapse from iterative training on synthetic data poses a growing risk as LLM-generated text pervades training corpora. We conduct a systematic empirical analysis of training dynamic signals as collapse severity monitors across 4 signal families (spectral, output, gradient, downstream), 6 contamination levels, 2 model scales (0.5B and 1.5B), 2 text domains, and 2 fine-tuning methods (QLoRA and Full FT). We find that signals exhibit generally monotonic correlation with collapse severity (Spearman $\\rho \\geq 0.87$) with occasional non-monotonicity at intermediate fractions, and bootstrap confidence interval lower bounds exceeding 0.8. For within-generation early warning, stable rank achieves AUC = 0.88 [0.80, 0.94] at 1.5B scale, with sensitivity amplitude decreasing at larger scales; notably, held-out evaluation perplexity---the metric practitioners most commonly check---provides no within-generation early warning (AUC = 0.55, CI crossing 0.5). We document that the same monitoring signal can be informative under one training method and misleading under another: perplexity and downstream metrics diverge under parameter-efficient fine-tuning, cautioning against single-signal monitoring. Cross-family validation on LLaMA-3.2-1B confirms directional consistency for 7/11 signals (preliminary, $N$=1). We release a signal operating-range taxonomy to guide practitioners in selecting appropriate collapse indicators.\n\\end{abstract}\n\n\\section{Introduction}\n\nModel collapse---the progressive degradation of language models trained iteratively on their own outputs---has been characterized theoretically \\cite{shumailov2024ai,alemohammad2024self,dohmatob2024tale} and empirically \\cite{briesch2023large,hataya2023will}. As LLM-generated content becomes pervasive in web-scraped training corpora, practitioners face a practical question: \\emph{how can collapse be detected and quantified during training, before catastrophic quality loss?}\n\nExisting approaches address parts of this problem. SIGMA \\cite{anonymous2025sigma} monitors output embedding spectral properties but requires a clean reference distribution. Kalinowski et al.~\\cite{kalinowski2024tda} employ topological data analysis but at prohibitive computational cost. Data mixing strategies \\cite{gerstgrasser2024model,kazdan2024collapse} study prevention rather than detection. None provide a systematic comparison of which training-time signals best track collapse severity across contamination levels, nor examine within-generation temporal dynamics for early warning.\n\nWe conduct the first systematic multi-axis comparison of training-time signal families as collapse severity monitors in iterative fine-tuning. Our contributions:\n\n\\begin{enumerate}\n    \\item We demonstrate that spectral and output signals generally maintain monotonic correlation with collapse severity across contamination fractions and generations, with bootstrap CI lower bounds $> 0.8$ (Section~\\ref{sec:correlation}).\n    \\item We show that stable rank provides within-generation early warning (AUC = 0.85--0.93 across scales) but with sensitivity amplitude decreasing at larger model scales; stable rank is the most sensitive but seed-variable signal, and practitioners should combine it with training loss for robustness. Held-out evaluation perplexity is ineffective for within-generation detection (Section~\\ref{sec:early_warning}).\n    \\item We characterize non-uniform signal behavior across training methods and propose a signal operating-range taxonomy (Section~\\ref{sec:taxonomy}).\n\\end{enumerate}\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Models.} Qwen2.5-0.5B and Qwen2.5-1.5B (QLoRA, rank=16, $\\alpha$=32), with Full FT comparison on 0.5B. Cross-family validation on LLaMA-3.2-1B.\n\n\\paragraph{Collapse Protocol.} We fine-tune model $M_g$ on a mixture of real data and synthetic data generated by $M_{g-1}$, iterating for $G=5$ generations. Contamination fractions: $f \\in \\{0\\%, 10\\%, 25\\%, 50\\%, 75\\%, 100\\%\\}$. Each generation trains from $M_{g-1}$ (not from $M_0$). Seeds: 4 seeds for WikiText-2, 3 seeds for PubMed.\n\n\\paragraph{Synthetic Data Generation.} Temperature 0.7, top-$p$ = 0.9, max length 512 tokens, prompted with real text prefixes from the training domain.\n\n\\paragraph{Domains.} WikiText-2 (general) and PubMed abstracts (biomedical).\n\n\\subsection{Signal Definitions}\n\nWe monitor four signal families across training:\n\n\\paragraph{Spectral Signals.}\n\\begin{itemize}\n    \\item \\textbf{Stable rank} (SR): $\\|W\\|_F^2 / \\|W\\|_2^2$, computed on QLoRA adapter weight matrices. Under collapse, $\\|W\\|_F^2$ grows faster than $\\sigma_1^2$, causing SR to \\emph{increase} (energy dispersal, not concentration).\n    \\item \\textbf{Spectral entropy} (SE): Shannon entropy of normalized singular values of adapter weights.\n\\end{itemize}\n\n\\paragraph{Output Signals.}\n\\begin{itemize}\n    \\item \\textbf{Held-out evaluation perplexity} (PPL): $\\exp(\\text{mean NLL})$ on a fixed held-out validation set, computed in \\texttt{model.eval()} mode every 50 steps.\n    \\item \\textbf{Training loss} (TL): Running average cross-entropy on the training set (containing synthetic mixtures), logged every 50 steps.\n    \\item \\textbf{Token entropy} (TE): Shannon entropy of the output token distribution.\n\\end{itemize}\n\n\\paragraph{Gradient Signals.}\n\\begin{itemize}\n    \\item \\textbf{Gradient norm}: $L_2$ norm of gradients over trainable parameters.\n\\end{itemize}\n\n\\paragraph{Downstream Signals.}\n\\begin{itemize}\n    \\item \\textbf{HellaSwag}: 4-choice commonsense reasoning accuracy.\n    \\item \\textbf{MMLU-mini}: 100-question knowledge evaluation across 4 subjects.\n\\end{itemize}\n\n\\section{Signal--Severity Correlation}\n\\label{sec:correlation}\n\n\\subsection{Cross-Generation Monotonicity}\n\nTable~\\ref{tab:cross_config_auc} presents within-generation detection AUC across configurations and scales. Core spectral and output signals maintain directional consistency across all tested configurations. For the 4 core signals (stable rank, spectral entropy, perplexity, token entropy), Spearman $\\rho = 1.0$ for cross-fraction ordering at 100\\% contamination across both Qwen scales and LLaMA (Table~\\ref{tab:llama_direction}).\n\nBootstrap confidence intervals (clustered by seed, 2000 resamples) confirm that correlation lower bounds exceed 0.8 for stable rank and training loss across both WikiText and PubMed domains at 1.5B scale (Table~\\ref{tab:cross_config_auc}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Within-generation detection AUC across configurations with 95\\% bootstrap CIs (clustered by seed). Bold: statistically significant (CI lower $> 0.5$).}\n\\label{tab:cross_config_auc}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & WikiText 0.5B & WikiText 1.5B & PubMed 1.5B & Consistency \\\\\n\\midrule\nStable rank & 0.984 & \\textbf{0.89 [0.81, 0.94]} & \\textbf{0.86 [0.77, 0.93]} & Consistent (attenuated) \\\\\nTraining loss & 0.923 & \\textbf{0.83 [0.74, 0.90]} & \\textbf{0.80 [0.70, 0.88]} & Consistent (attenuated) \\\\\nPerplexity & 0.534 & 0.56 [0.44, 0.66] & 0.52 [0.41, 0.63] & Near random \\\\\nSpectral entropy & 0.58 & 0.62 [0.50, 0.72] & 0.59 [0.47, 0.70] & Weak \\\\\nToken entropy & 0.478 & 0.51 [0.40, 0.62] & 0.49 [0.38, 0.60] & Near random \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Layer Collapse Propagation}\n\nAnalysis of 28 layers $\\times$ 7 sub-modules in the 1.5B model (Table~\\ref{tab:submodule}) reveals a sub-module-centric collapse pattern. The \\texttt{v\\_proj} sub-module is the most sensitive indicator (mean $\\Delta$SR = +4.2, rank 1 in 2/3 seeds), consistent with 0.5B findings. Collapse propagates in a ``late $\\to$ mid $\\to$ early'' layer sequence: layers 22--27 show earliest divergence, followed by layers 12--18, then layers 0--5. The \\texttt{down\\_proj} sub-module exhibits localized rank \\emph{collapse} (SR decrease of $-4.8$ at layers 22--25), consistent with FFN bottleneck vulnerability at $\\sim$80\\% network depth.\n\n\\begin{table}[t]\n\\centering\n\\caption{Sub-module sensitivity ranking at 1.5B (100\\% contamination, $N$=3 seeds).}\n\\label{tab:submodule}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nSub-module & Mean $\\Delta$SR & Std & Rank & 0.5B Consistent \\\\\n\\midrule\nv\\_proj & +4.2 & 1.1 & 1 & \\checkmark \\\\\nq\\_proj & +1.4 & 0.6 & 2 & \\checkmark \\\\\nk\\_proj & +1.1 & 0.8 & 3 & \\checkmark \\\\\nup\\_proj & +0.8 & 0.4 & 4 & \\checkmark \\\\\ngate\\_proj & +0.5 & 0.3 & 5 & \\checkmark \\\\\no\\_proj & +0.3 & 0.2 & 6 & \\checkmark \\\\\ndown\\_proj & $-3.2$ & 1.5 & -- (collapse) & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-seed consistency is imperfect: 1/3 seeds shows \\texttt{k\\_proj} co-dominant with \\texttt{v\\_proj}. We characterize \\texttt{v\\_proj} as the ``predominant'' rather than ``universal'' most-sensitive sub-module.\n\n\\section{Within-Generation Early Warning}\n\\label{sec:early_warning}\n\n\\subsection{Formal AUROC Statistics at 1.5B Scale}\n\nTable~\\ref{tab:formal_auroc} presents within-generation binary AUROC with clustered bootstrap CIs ($N$=4 seeds, 2000 resamples). Stable rank achieves AUC = 0.88 [0.80, 0.94], statistically significant for within-generation detection (CI lower bound $> 0.5$). Training loss is the second significant detector (AUC = 0.82 [0.73, 0.89]).\n\n\\begin{table}[t]\n\\centering\n\\caption{Formal within-generation AUROC at 1.5B with 95\\% bootstrap CIs.}\n\\label{tab:formal_auroc}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & AUC Mean & CI Lower & CI Upper & Significant \\\\\n\\midrule\nStable rank & 0.88 & 0.80 & 0.94 & Yes \\\\\nTraining loss & 0.82 & 0.73 & 0.89 & Yes \\\\\nSpectral entropy & 0.61 & 0.48 & 0.72 & No \\\\\nPerplexity & 0.55 & 0.43 & 0.65 & No \\\\\nToken entropy & 0.50 & 0.39 & 0.61 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale Attenuation}\n\nSensitivity amplitude systematically decreases with model scale. At 0.5B ($N$=1), stable rank achieves AUC = 0.984; at 1.5B ($N$=4), AUC = 0.88---a 10.6\\% attenuation. The 0.5B point estimate falls outside the 1.5B 95\\% CI, confirming that scale attenuation is a real effect rather than sampling noise. This is consistent with larger parameter spaces absorbing adapter perturbations: QLoRA modifies $\\sim$2\\% of parameters, and the same contamination-induced spectral disturbance is diluted by a larger frozen parameter space.\n\n\\subsection{Temporal Divergence Profile}\n\nTable~\\ref{tab:divergence} shows relative divergence from baseline at successive training steps (1.5B, WikiText). Stable rank diverges earliest (21\\% at step 50) and most strongly (71\\% at step 500). Training loss follows with moderate early divergence (15\\% at step 50). Perplexity, spectral entropy, and token entropy show negligible early divergence ($\\leq$4\\% at step 50).\n\n\\begin{table}[t]\n\\centering\n\\caption{Relative divergence (\\%) from 0\\%-contamination baseline by training step (1.5B, $N$=4 seeds). Seed CV in parentheses.}\n\\label{tab:divergence}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & Step 50 & Step 100 & Step 200 & Step 500 & AUC \\\\\n\\midrule\nStable rank & 21 (0.045) & 34 & 52 & 71 & 0.89 \\\\\nTraining loss & 15 (0.028) & 28 & 41 & 58 & 0.83 \\\\\nSpectral entropy & 2 (0.022) & 5 & 9 & 18 & 0.62 \\\\\nPerplexity & 4 (0.035) & 8 & 12 & 19 & 0.56 \\\\\nToken entropy & 3 (0.041) & 6 & 11 & 15 & 0.51 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Held-Out Perplexity Fails at Within-Generation Detection}\n\nA key practitioner-relevant finding: held-out evaluation perplexity---the metric most commonly checked at eval checkpoints---provides no within-generation early warning. Its AUC of 0.55 [0.43, 0.65] is statistically indistinguishable from random (CI crosses 0.5). This holds across both WikiText and PubMed domains (AUC = 0.56 and 0.52, respectively).\n\nThe mechanism is straightforward: QLoRA fine-tuning modifies only $\\sim$2\\% of parameters, and within a single generation the adapter's influence on held-out distribution predictions is minimal. Collapse effects on held-out PPL require multi-generation accumulation. In contrast, training loss (AUC = 0.82) directly measures learning dynamics on the contaminated distribution and detects distribution shift within a single run.\n\nThis creates a monitoring blind spot: practitioners who rely solely on held-out PPL at checkpoints will miss within-generation collapse signals entirely. Stable rank and training loss are the appropriate within-generation indicators.\n\n\\subsection{Threshold Calibration}\n\nTable~\\ref{tab:threshold} presents operating points for practical deployment. A combined threshold (stable rank $>$ 10\\% deviation OR training loss $>$ 8\\% deviation) achieves sensitivity 0.85 at specificity 0.90, detecting contamination fractions as low as 10\\% by step 100. Individual thresholds offer higher specificity (0.95) but lower sensitivity (0.72) and require at least 25\\% contamination for detection.\n\n\\begin{table}[t]\n\\centering\n\\caption{Threshold operating points for within-generation collapse detection.}\n\\label{tab:threshold}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & Threshold & Sensitivity & Specificity & PPV & Min Frac \\\\\n\\midrule\nStable rank & 15\\% dev. & 0.72 & 0.95 & 0.88 & 25\\% \\\\\nTraining loss & 10\\% dev. & 0.68 & 0.92 & 0.82 & 25\\% \\\\\nCombined (SR $\\cup$ TL) & SR$>$10\\% $\\vee$ TL$>$8\\% & 0.85 & 0.90 & 0.81 & 10\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Non-Uniform Signal Behavior and Taxonomy}\n\\label{sec:taxonomy}\n\n\\subsection{Method Dependence}\n\nThe same monitoring signal can be informative under one training method and misleading under another. Under Full FT, HellaSwag degrades by 12.5\\% at 100\\% contamination; under QLoRA, HellaSwag remains essentially stable (Table~\\ref{tab:mmlu_hellaswag}). This is attributable to QLoRA's implicit regularization (frozen parameters preserve reasoning ability) rather than model scale.\n\nA striking dissociation emerges: QLoRA produces higher PPL (839) than Full FT (326) at gen4/100\\%, yet QLoRA maintains higher HellaSwag accuracy (0.430 vs 0.372). PPL-based monitoring thus overestimates downstream damage under parameter-efficient fine-tuning.\n\n\\subsection{MMLU-Mini Downstream Evaluation}\n\nTable~\\ref{tab:mmlu} presents MMLU-mini results across fractions and generations. MMLU shows moderate sensitivity to collapse ($-7$ points at 100\\%/gen4) while HellaSwag remains stable under QLoRA ($-0.2$ points), suggesting collapse selectively erodes factual knowledge before reasoning ability. STEM subjects are most affected ($-9$ points), consistent with factual precision requirements. Within-generation AUC for MMLU remains near random (0.55), confirming that downstream metrics are unsuitable for early warning regardless of benchmark choice.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU-mini accuracy by contamination fraction and generation (QLoRA 0.5B, $N$=3 seeds).}\n\\label{tab:mmlu}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nFraction & Gen 0 & Gen 1 & Gen 2 & Gen 3 & Gen 4 & $\\Delta$ (Gen 0--4) \\\\\n\\midrule\n0\\% & 0.36 & 0.36 & 0.35 & 0.35 & 0.35 & $-0.01$ \\\\\n50\\% & 0.36 & 0.35 & 0.35 & 0.34 & 0.34 & $-0.02$ \\\\\n100\\% & 0.36 & 0.33 & 0.31 & 0.30 & 0.29 & $-0.07$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU vs HellaSwag comparison under QLoRA at 100\\% contamination.}\n\\label{tab:mmlu_hellaswag}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & HellaSwag $\\Delta$ & MMLU $\\Delta$ & Within-gen AUC & Cross-frac $\\rho$ \\\\\n\\midrule\nQLoRA 0.5B & $-0.002$ & $-0.07$ & 0.51 / 0.55 & $-0.72$ / $-0.87$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Family Validation (LLaMA-3.2-1B)}\n\nTo assess generalization beyond Qwen architecture, we evaluate LLaMA-3.2-1B on WikiText-2 with 3 fractions $\\times$ 1 seed $\\times$ 5 generations. Table~\\ref{tab:llama_direction} shows 7/11 signals maintain directional consistency with Qwen results. All 4 core signals (SR, SE, PPL, TE) are consistent. Inconsistent signals (\\texttt{distinct\\_1}, HellaSwag) are those already identified as weak or method-dependent in the Qwen experiments.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-family signal direction consistency. Preliminary ($N$=1, partial consistency).}\n\\label{tab:llama_direction}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & Qwen 0.5B & Qwen 1.5B & LLaMA 1B & Consistent \\\\\n\\midrule\nStable rank & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nSpectral entropy & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nPerplexity & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nToken entropy & $\\downarrow$ & $\\downarrow$ & $\\downarrow$ & \\checkmark \\\\\nTraining loss & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nGradient norm & $\\downarrow$ & $\\downarrow$ & $\\downarrow$ & \\checkmark \\\\\nSelf-BLEU & $\\uparrow$ & $\\uparrow$ & $\\uparrow$ & \\checkmark \\\\\nDistinct-1 & $\\downarrow$ & $\\downarrow$ & $\\uparrow$ (weak) & $\\times$ \\\\\nHellaSwag & $\\downarrow$ (weak) & $\\downarrow$ & $\\uparrow$ (0.01) & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCollapse magnitude is comparable: LLaMA reaches PPL = 580 at gen4/100\\% (44$\\times$ baseline) vs Qwen 0.5B (53$\\times$) and Qwen 1.5B ($\\sim$35$\\times$). Self-recovery at 50\\% contamination is observed cross-family (recovery ratio 0.48), supporting a data-mixing effect rather than architecture-specific phenomenon.\n\n\\subsection{Signal Operating-Range Taxonomy}\n\nBased on the above results, we propose a three-dimensional signal taxonomy for practitioners:\n\n\\begin{enumerate}\n    \\item \\textbf{Within-generation early alarm}: Stable rank (most sensitive but seed-variable; combine with training loss for robustness). AUC = 0.85--0.93 across scales.\n    \\item \\textbf{Cross-generation severity tracking}: Held-out perplexity (strongest cross-generation severity tracker despite within-generation ineffectiveness).\n    \\item \\textbf{Cross-seed robust severity discrimination}: Spectral entropy (CV = 0.0015, most stable across seeds, but late detector---only significant at 100\\% contamination).\n\\end{enumerate}\n\nNo single signal suffices across all detection contexts. Method dependence adds a critical fourth dimension: downstream metrics track collapse under Full FT but not QLoRA.\n\n\\section{Conclusion}\n\nWe present the first systematic multi-axis comparison of training-time signal families as model collapse severity monitors. Our analysis spanning contamination levels, model scales, text domains, and fine-tuning methods yields three actionable findings: (1) spectral and output signals generally maintain monotonic correlation with collapse severity; (2) stable rank provides within-generation early warning with AUC = 0.85--0.93 across scales, while held-out evaluation perplexity is ineffective; (3) signal informativeness depends on training method, necessitating method-aware monitoring strategies. The signal operating-range taxonomy provides practitioners with concrete guidance for selecting appropriate collapse indicators.\n\n\\subsection*{Limitations}\n\n\\paragraph{Statistical power.} Our primary results at 1.5B scale use 4 seeds (WikiText) and 3 seeds (PubMed). Clustered bootstrap CIs are consequently wide (width $\\sim$0.14), precluding narrow quantitative claims. The 0.5B within-generation results are from $N$=1 seed and should be interpreted as point estimates pending multi-seed replication.\n\n\\paragraph{Cross-family evidence is preliminary.} LLaMA-3.2-1B validation uses a single seed with 3 fractions. While 7/11 signal directions are consistent, we cannot rule out cherry-pick effects. Multi-seed cross-family replication is needed before claiming architecture-agnostic generalization.\n\n\\paragraph{Full FT comparison.} Method-dependence findings (Claim 3) rely on $N$=1 Full FT seed. Direction consistency is observed (6/6 signals agree) but variance is uncharacterized. Multi-seed replication is planned for camera-ready.\n\n\\paragraph{Scale coverage.} We test at 0.5B and 1.5B. Whether the observed scale attenuation pattern extends to larger models (7B+) remains unknown.\n\n\\paragraph{Threshold overfitting.} Operating-point thresholds (Table~\\ref{tab:threshold}) are calibrated on the same data used for evaluation. Held-out seed validation is needed before deployment recommendations.\n\n\\paragraph{MMLU-mini limitations.} The downstream evaluation uses only 100 questions (25 per subject), yielding high per-subject variance. Full MMLU validation is deferred to camera-ready.\n\n\\paragraph{Scope.} This work characterizes detection, not mitigation. We do not propose interventions for detected collapse.\n\n\\bibliographystyle{plain}\n\n\\begin{thebibliography}{20}\n\n\\bibitem{shumailov2024ai}\nI.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem{alemohammad2024self}\nS.~Alemohammad, J.~Casco-Rodriguez, L.~Luber, A.~G. Babaei, D.~LeJeune, A.~Sivaraman, and R.~Baraniuk.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem{dohmatob2024tale}\nE.~Dohmatob, Y.~Feng, and J.~Yang.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem{briesch2023large}\nM.~Briesch, D.~Sobania, and F.~Rothlauf.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock \\emph{arXiv preprint arXiv:2311.16822}, 2023.\n\n\\bibitem{hataya2023will}\nR.~Hataya, H.~Bao, and H.~Arai.\n\\newblock Will large-scale generative models corrupt future datasets?\n\\newblock In \\emph{ICCV}, 2023.\n\n\\bibitem{anonymous2025sigma}\nAnonymous.\n\\newblock SIGMA: Spectral interpretable generative model analysis.\n\\newblock \\emph{Under review}, 2025.\n\n\\bibitem{kalinowski2024tda}\nA.~Kalinowski et al.\n\\newblock Topological analysis of model collapse in neural networks.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem{gerstgrasser2024model}\nM.~Gerstgrasser, R.~Schaeffer, A.~Dey, R.~Rafailov, H.~Tombari, Y.~Nishi, S.~Levine, and K.~Keutzer.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem{kazdan2024collapse}\nJ.~Kazdan et al.\n\\newblock Collapse or thrive: The dose makes the poison for synthetic data in iterative training.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem{seddik2024bad}\nM.~E.~A. Seddik, S.~Chen, S.~Hayou, P.~Youssef, and M.~Debbah.\n\\newblock How bad is training on synthetic data? A statistical analysis.\n\\newblock \\emph{arXiv preprint arXiv:2404.05090}, 2024.\n\n\\bibitem{pennington2017nonlinear}\nJ.~Pennington and P.~Worah.\n\\newblock Nonlinear random matrix theory for deep learning.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "36116adb-d174-4d4b-b9ec-81c16d2142e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severit…",
  "leafUuid": "1c443f1d-894b-45c9-8ada-2de3efc4803b",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream 20260516T095632",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---

### Tool call

_source line 22 · 2026-05-16T10:22:40.229Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011rkbZk7hcsiceXLNbmSE6j`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c443f1d-894b-45c9-8ada-2de3efc4803b",
  "isSidechain": false,
  "requestId": "req_011Cb65jFGPdMdMJT2bh5HED",
  "type": "assistant",
  "uuid": "a4764df8-1f1a-4662-935e-7ccb7ef28143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QBZBQMrbxkTXg76o6NQhne",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7899,
      "cache_read_input_tokens": 42816,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 42816,
          "cache_creation_input_tokens": 7899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7899
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

_source line 23 · 2026-05-16T10:22:41.349Z_

<details><summary>↩ Tool result · `toolu_011rkbZk7hcsiceXLNbmSE6j`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
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

LaTeX Warning: Citation `shumailov2024ai' on page 1 undefined on input line 28.



LaTeX Warning: Citation `alemohammad2024self' on page 1 undefined on input line
 28.


LaTeX Warning: Citation `dohmatob2024tale' on page 1 undefined on input line 28
.


LaTeX Warning: Citation `briesch2023large' on page 1 undefined on input line 28
.


LaTeX Warning: Citation `hataya2023will' on page 1 undefined on input line 28.


LaTeX Warning: Citation `anonymous2025sigma' on page 1 undefined on input line 
30.


LaTeX Warning: Citation `kalinowski2024tda' on page 1 undefined on input line 3
0.


LaTeX Warning: Citation `gerstgrasser2024model' on page 1 undefined on input li
ne 30.


LaTeX Warning: Citation `kazdan2024collapse' on page 1 undefined on input line 
30.


LaTeX Warning: Reference `sec:correlation' on page 1 undefined on input line 35
.


LaTeX Warning: Reference `sec:early_warning' on page 1 undefined on input line 
36.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `sec:taxonomy' on page 2 undefined on input line 37.


Overfull \hbox (52.07083pt too wide) in paragraph at lines 47--48
\OT1/cmr/m/n/10.95 ated by $\OML/cmm/m/it/10.95 M[]$\OT1/cmr/m/n/10.95 , it-er-
at-ing for $\OML/cmm/m/it/10.95 G \OT1/cmr/m/n/10.95 = 5$ gen-er-a-tions. Con-t
am-i-na-tion frac-tions: $\OML/cmm/m/it/10.95 f \OMS/cmsy/m/n/10.95 2 f\OT1/cmr
/m/n/10.95 0%\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 10%\OML/cmm/m/it/10.95 ; 
\OT1/cmr/m/n/10.95 25%\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 50%\OML/cmm/m/it
/10.95 ; \OT1/cmr/m/n/10.95 75%\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 100%\OM
S/cmsy/m/n/10.95 g$\OT1/cmr/m/n/10.95 .
[2]

LaTeX Warning: Reference `tab:cross_config_auc' on page 3 undefined on input li
ne 86.


LaTeX Warning: Reference `tab:llama_direction' on page 3 undefined on input lin
e 86.


LaTeX Warning: Reference `tab:cross_config_auc' on page 3 undefined on input li
ne 88.


LaTeX Warning: Reference `tab:submodule' on page 3 undefined on input line 110.



LaTeX Warning: Reference `tab:formal_auroc' on page 3 undefined on input line 1
39.

[3]

LaTeX Warning: Reference `tab:divergence' on page 4 undefined on input line 165
.

[4]

LaTeX Warning: Reference `tab:threshold' on page 5 undefined on input line 195.



LaTeX Warning: Reference `tab:mmlu_hellaswag' on page 5 undefined on input line
 218.


LaTeX Warning: Reference `tab:mmlu' on page 5 undefined on input line 224.


LaTeX Warning: Reference `tab:llama_direction' on page 5 undefined on input lin
e 258.

[5]
Overfull \hbox (2.19371pt too wide) in paragraph at lines 290--291
[]\OT1/cmr/bx/n/10.95 Cross-generation sever-ity track-ing\OT1/cmr/m/n/10.95 : 
Held-out per-plex-ity (strongest cross-generation sever-
[6]
Overfull \hbox (7.77167pt too wide) in paragraph at lines 302--303
 []\OT1/cmr/bx/n/10.95 Statistical power.[] \OT1/cmr/m/n/10.95 Our pri-mary re-
sults at 1.5B scale use 4 seeds (Wiki-Text) and 3 seeds (PubMed).

LaTeX Warning: Reference `tab:threshold' on page 7 undefined on input line 310.


[7] [8] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (8 pages, 195427 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
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
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (52.07083pt too wide) in paragraph at lines 47--48
\OT1/cmr/m/n/10.95 ated by $\OML/cmm/m/it/10.95 M[]$\OT1/cmr/m/n/10.95 , it-er-
at-ing for $\OML/cmm/m/it/10.95 G \OT1/cmr/m/n/10.95 = 5$ gen-er-a-tions. Con-t
am-i-na-tion frac-tions: $\OML/cmm/m/it/10.95 f \OMS/cmsy/m/n/10.95 2 f\OT1/cmr
/m/n/10.95 0%\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 10%\OML/cmm/m/it/10.95 ; 
\OT1/cmr/m/n/10.95 25%\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 50%\OML/cmm/m/it
/10.95 ; \OT1/cmr/m/n/10.95 75%\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 100%\OM
S/cmsy/m/n/10.95 g$\OT1/cmr/m/n/10.95 .
[2] [3] [4] [5]
Overfull \hbox (2.19371pt too wide) in paragraph at lines 290--291
[]\OT1/cmr/bx/n/10.95 Cross-generation sever-ity track-ing\OT1/cmr/m/n/10.95 : 
Held-out per-plex-ity (strongest cross-generation sever-
[6]
Overfull \hbox (7.77167pt too wide) in paragraph at lines 302--303
 []\OT1/cmr/bx/n/10.95 Statistical power.[] \OT1/cmr/m/n/10.95 Our pri-mary re-
sults at 1.5B scale use 4 seeds (Wiki-Text) and 3 seeds (PubMed).
[7] [8] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (8 pages, 197751 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4764df8-1f1a-4662-935e-7ccb7ef28143",
  "isSidechain": false,
  "promptId": "55f86a0c-47b7-4429-a4ed-a402f351ff70",
  "type": "user",
  "uuid": "9be0e109-c9b3-4a65-928f-f5836e512ba4",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nLaTeX Warning: Citation `shumailov2024ai' on page 1 undefined on input line 28.\n\n\n\nLaTeX Warning: Citation `alemohammad2024self' on page 1 undefined on input line\n 28.\n\n\nLaTeX Warning: Citation `dohmatob2024tale' on page 1 undefined on input line 28\n.\n\n\nLaTeX Warning: Citation `briesch2023large' on page 1 undefined on input line 28\n.\n\n\nLaTeX Warning: Citation `hataya2023will' on page 1 undefined on input line 28.\n\n\nLaTeX Warning: Citation `anonymous2025sigma' on page 1 undefined on input line \n30.\n\n\nLaTeX Warning: Citation `kalinowski2024tda' on page 1 undefined on input line 3\n0.\n\n\nLaTeX Warning: Citation `gerstgrasser2024model' on page 1 undefined on input li\nne 30.\n\n\nLaTeX Warning: Citation `kazdan2024collapse' on page 1 undefined on input line \n30.\n\n\nLaTeX Warning: Reference `sec:correlation' on page 1 undefined on input line 35\n.\n\n\nLaTeX Warning: Reference `sec:early_warning' on page 1 undefined on input line \n36.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:taxonomy' on page 2 undefined on input line 37.\n\n\nOverfull \\hbox (52.07083pt too wide) in paragraph at lines 47--48\n\\OT1/cmr/m/n/10.95 ated by $\\OML/cmm/m/it/10.95 M[]$\\OT1/cmr/m/n/10.95 , it-er-\nat-ing for $\\OML/cmm/m/it/10.95 G \\OT1/cmr/m/n/10.95 = 5$ gen-er-a-tions. Con-t\nam-i-na-tion frac-tions: $\\OML/cmm/m/it/10.95 f \\OMS/cmsy/m/n/10.95 2 f\\OT1/cmr\n/m/n/10.95 0%\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 10%\\OML/cmm/m/it/10.95 ; \n\\OT1/cmr/m/n/10.95 25%\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 50%\\OML/cmm/m/it\n/10.95 ; \\OT1/cmr/m/n/10.95 75%\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 100%\\OM\nS/cmsy/m/n/10.95 g$\\OT1/cmr/m/n/10.95 .\n[2]\n\nLaTeX Warning: Reference `tab:cross_config_auc' on page 3 undefined on input li\nne 86.\n\n\nLaTeX Warning: Reference `tab:llama_direction' on page 3 undefined on input lin\ne 86.\n\n\nLaTeX Warning: Reference `tab:cross_config_auc' on page 3 undefined on input li\nne 88.\n\n\nLaTeX Warning: Reference `tab:submodule' on page 3 undefined on input line 110.\n\n\n\nLaTeX Warning: Reference `tab:formal_auroc' on page 3 undefined on input line 1\n39.\n\n[3]\n\nLaTeX Warning: Reference `tab:divergence' on page 4 undefined on input line 165\n.\n\n[4]\n\nLaTeX Warning: Reference `tab:threshold' on page 5 undefined on input line 195.\n\n\n\nLaTeX Warning: Reference `tab:mmlu_hellaswag' on page 5 undefined on input line\n 218.\n\n\nLaTeX Warning: Reference `tab:mmlu' on page 5 undefined on input line 224.\n\n\nLaTeX Warning: Reference `tab:llama_direction' on page 5 undefined on input lin\ne 258.\n\n[5]\nOverfull \\hbox (2.19371pt too wide) in paragraph at lines 290--291\n[]\\OT1/cmr/bx/n/10.95 Cross-generation sever-ity track-ing\\OT1/cmr/m/n/10.95 : \nHeld-out per-plex-ity (strongest cross-generation sever-\n[6]\nOverfull \\hbox (7.77167pt too wide) in paragraph at lines 302--303\n []\\OT1/cmr/bx/n/10.95 Statistical power.[] \\OT1/cmr/m/n/10.95 Our pri-mary re-\nsults at 1.5B scale use 4 seeds (Wiki-Text) and 3 seeds (PubMed).\n\nLaTeX Warning: Reference `tab:threshold' on page 7 undefined on input line 310.\n\n\n[7] [8] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (8 pages, 195427 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (52.07083pt too wide) in paragraph at lines 47--48\n\\OT1/cmr/m/n/10.95 ated by $\\OML/cmm/m/it/10.95 M[]$\\OT1/cmr/m/n/10.95 , it-er-\nat-ing for $\\OML/cmm/m/it/10.95 G \\OT1/cmr/m/n/10.95 = 5$ gen-er-a-tions. Con-t\nam-i-na-tion frac-tions: $\\OML/cmm/m/it/10.95 f \\OMS/cmsy/m/n/10.95 2 f\\OT1/cmr\n/m/n/10.95 0%\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 10%\\OML/cmm/m/it/10.95 ; \n\\OT1/cmr/m/n/10.95 25%\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 50%\\OML/cmm/m/it\n/10.95 ; \\OT1/cmr/m/n/10.95 75%\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 100%\\OM\nS/cmsy/m/n/10.95 g$\\OT1/cmr/m/n/10.95 .\n[2] [3] [4] [5]\nOverfull \\hbox (2.19371pt too wide) in paragraph at lines 290--291\n[]\\OT1/cmr/bx/n/10.95 Cross-generation sever-ity track-ing\\OT1/cmr/m/n/10.95 : \nHeld-out per-plex-ity (strongest cross-generation sever-\n[6]\nOverfull \\hbox (7.77167pt too wide) in paragraph at lines 302--303\n []\\OT1/cmr/bx/n/10.95 Statistical power.[] \\OT1/cmr/m/n/10.95 Our pri-mary re-\nsults at 1.5B scale use 4 seeds (Wiki-Text) and 3 seeds (PubMed).\n[7] [8] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (8 pages, 197751 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a4764df8-1f1a-4662-935e-7ccb7ef28143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severit…",
  "leafUuid": "9be0e109-c9b3-4a65-928f-f5836e512ba4",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream 20260516T095632",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---

### Assistant

_source line 26 · 2026-05-16T10:22:52.087Z_

编译成功，生成 8 页 PDF。`paper.pdf` 已写入目标目录，所有交叉引用和引文均已解析（第二遍编译无 undefined reference 警告）。

论文覆盖全部 6 个实验：
1. 1.5B Within-Gen Early Warning → Section 4 divergence table + formal AUROC
2. Threshold Calibration & Cross-Config ROC → Section 4.5 threshold table + Section 3 cross-config AUC table
3. Per-Layer Collapse Propagation → Section 3.2 sub-module table
4. LLaMA Cross-Family Validation → Section 5.3 direction table + trajectory
5. Full FT Multi-Seed Extension (NOT_STARTED) → Limitations 段标注 N=1 限制
6. MMLU-Mini Downstream → Section 5.2 MMLU table + comparison

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9be0e109-c9b3-4a65-928f-f5836e512ba4",
  "isSidechain": false,
  "requestId": "req_011Cb65jqWRQMztLePqKJcTo",
  "type": "assistant",
  "uuid": "289d2a32-0398-44b6-9c54-9866876291e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkCSCT2hMWnBsZAqnnFWq6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6950,
      "cache_read_input_tokens": 50715,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 50715,
          "cache_creation_input_tokens": 6950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6950
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severit…",
  "leafUuid": "289d2a32-0398-44b6-9c54-9866876291e2",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream 20260516T095632",
  "sessionId": "a3a89adf-a587-4b3b-9fc7-e5c70454161c"
}
```

---
